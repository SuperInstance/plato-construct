#!/usr/bin/env python3
"""plato-construct room builder — reads CAPABILITY.toml from crates, builds PLATO rooms."""

import json
import os
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    try:
        import tomli as tomllib  # type: ignore
    except ModuleNotFoundError:
        tomllib = None  # fallback to manual parsing


CRATES_DIR = Path(os.getenv("PLATO_CRATES_DIR", "../crates"))
OUTPUT_DIR = Path(os.getenv("PLATO_OUTPUT_DIR", "./rooms"))
STATE_FILE = Path(os.getenv("PLATO_STATE", "./si/room_state.json"))

# Rooms registry: maps crate name → room definition
ROOMS: dict[str, dict] = {}


def parse_toml_simple(path: Path) -> dict:
    """Minimal TOML parser for CAPABILITY.toml if tomllib unavailable."""
    if tomllib:
        return tomllib.loads(path.read_text())
    # Fallback: very simple [section] key = value parser
    result: dict = {}
    current_section = None
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            current_section = line[1:-1]
            result[current_section] = {}
        elif "=" in line and current_section:
            k, v = line.split("=", 1)
            result[current_section][k.strip()] = v.strip().strip('"').strip("'")
    return result


def discover_crates():
    """Walk CRATES_DIR and collect CAPABILITY.toml files."""
    crates = []
    for cap_file in CRATES_DIR.rglob("CAPABILITY.toml"):
        crate_dir = cap_file.parent
        crate_name = crate_dir.name
        cap = parse_toml_simple(cap_file)
        crates.append({"name": crate_name, "path": str(crate_dir), "capability": cap})
    return crates


def build_room(crate):
    """Create a PLATO room from a crate's CAPABILITY.toml."""
    cap = crate["capability"]
    layer = cap.get("layer", {})
    layer_name = layer.get("name", "unknown") if isinstance(layer, str) else layer.get("name", "unknown")
    provides = cap.get("provides", {})

    room = {
        "name": crate["name"],
        "layer": layer_name,
        "provides": provides,
        "source_path": crate["path"],
        "corridors": [],  # filled by dependency resolution
        "content": {
            "title": f"Room: {crate['name']}",
            "layer": layer_name,
            "capabilities": list(provides.keys()) if isinstance(provides, dict) else [],
        },
    }
    return room


def resolve_dependencies(rooms):
    """Create corridors between rooms based on layer adjacency."""
    layer_order = ["protocol", "foundation", "decomposition", "automation",
                   "education", "workspace", "application"]
    by_name = {r["name"]: r for r in rooms.values()}

    for name, room in rooms.items():
        layer_idx = layer_order.index(room["layer"]) if room["layer"] in layer_order else 99
        # Connect to rooms in adjacent layers
        for other_name, other in rooms.items():
            if other_name == name:
                continue
            other_idx = layer_order.index(other["layer"]) if other["layer"] in layer_order else 99
            if abs(layer_idx - other_idx) == 1:
                room["corridors"].append({
                    "to": other_name,
                    "direction": "next" if other_idx > layer_idx else "prev",
                })


def write_room(room):
    """Serialize room to JSON in OUTPUT_DIR."""
    room_dir = OUTPUT_DIR / room["name"]
    room_dir.mkdir(parents=True, exist_ok=True)
    (room_dir / "room.json").write_text(json.dumps(room, indent=2))


def build_learning_path(rooms):
    """Generate a default learning path through rooms by layer."""
    layer_order = ["protocol", "foundation", "decomposition", "automation",
                   "education", "workspace", "application"]
    by_layer: dict[str, list] = {}
    for room in rooms.values():
        by_layer.setdefault(room["layer"], []).append(room["name"])

    path = []
    for layer in layer_order:
        if layer in by_layer:
            path.extend(sorted(by_layer[layer]))
    return path


def main():
    print(f"[discover] scanning {CRATES_DIR} for crates...")
    crates = discover_crates()
    print(f"[discover] found {len(crates)} crate(s)")

    for crate in crates:
        room = build_room(crate)
        ROOMS[crate["name"]] = room
        print(f"  [room] {room['name']} (layer={room['layer']}, capabilities={len(room['content']['capabilities'])})")

    resolve_dependencies(ROOMS)
    print(f"[resolve] built corridors between {len(ROOMS)} rooms")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for room in ROOMS.values():
        write_room(room)

    path = build_learning_path(ROOMS)
    (OUTPUT_DIR / "learning_path.json").write_text(json.dumps(path, indent=2))
    print(f"[path] learning path: {' → '.join(path)}")

    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps({"rooms": list(ROOMS.keys()), "path": path}, indent=2))
    print(f"[done] wrote {len(ROOMS)} rooms to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
