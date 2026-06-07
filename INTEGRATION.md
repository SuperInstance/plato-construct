# plato-construct — Integration Map

## Overview

plato-construct is the **education system** for the SuperInstance ecosystem. It uses PLATO's room-based learning metaphor to teach agents about every crate, capability, and protocol in the lattice.

## Wiring Diagram

```
our Rust crates (CAPABILITY.toml each)
  │
  ▼
plato-construct ◄── room-topology (spatial structure)
  │                ◄── persistent-sheaf (knowledge topology)
  │                ◄── intention-field (shared direction)
  ▼
PLATO rooms — agents learn by navigating rooms
```

## Integration Points

### room-topology — Spatial Structure

room-topology defines the spatial relationships between rooms. plato-construct uses it to:

- Place crates into rooms with correct adjacency.
- Define corridors between rooms whose capabilities have dependencies.
- Ensure the spatial layout reflects the actual dependency graph.

### persistent-sheaf — Knowledge Topology

persistent-sheaf provides the topological glue for knowledge:

- Each room's knowledge is a section of the sheaf over the crate's dependency space.
- When an agent learns a room, the sheaf restriction maps ensure prerequisite knowledge is already present.
- This prevents agents from entering rooms they're not prepared for.

### intention-field — Shared Direction

The intention-field provides a shared sense of "where we're going":

- Learning paths are generated to align with the current intention-field direction.
- If the field shifts (new priority), plato-construct reconfigures room ordering.
- Agents in the same room are co-oriented, enabling collaborative learning.

### Our Rust Crates — Learning Modules

Every Rust crate in the SuperInstance ecosystem has a `CAPABILITY.toml`. plato-construct reads these to:

1. Discover what each crate provides.
2. Build a PLATO room per crate with appropriate content.
3. Create learning paths that follow the dependency graph.
4. Track agent progress through rooms.

## Configuration

See `si/room_builder.py` for the script that automates room construction from crate metadata.
