# plato-construct — Agents as Apps

## Principle

plato-construct **IS** the education system. Agents learn through rooms, not docs.

## How Agents Learn

An agent doesn't read documentation. An agent **enters a room**.

1. **Room** — A bounded space containing knowledge about one crate or concept.
2. **Corridor** — A connection to adjacent rooms (prerequisites, dependents, related topics).
3. **Path** — A sequence of rooms ordered by the dependency graph and intention field.

## Why Rooms, Not Docs

Documentation is passive. Rooms are active:

- **Spatial memory** — Agents remember where they learned something, not just what.
- **Prerequisites** — A room won't open until prerequisite rooms are completed.
- **Progress tracking** — The agent's position in the room graph is its education state.
- **Collaborative** — Multiple agents in the same room can share insights.

## Integration with the Ecosystem

- **room-topology**: Defines the spatial structure of the room graph.
- **persistent-sheaf**: Ensures knowledge consistency across rooms.
- **intention-field**: Aligns learning paths with current priorities.
- **Rust crates**: Each crate's `CAPABILITY.toml` defines a room's content.
- **categorical-agents**: Agents declare learning goals as typed intents; plato-construct provides the rooms.
