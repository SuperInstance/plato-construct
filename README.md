# ⬡ The Construct

**Web-based agent onboarding for the OpenConstruct ecosystem.**

The Construct is a single-page wizard that walks you through declaring, configuring, and generating a deployable agent card. No backend required — open `index.html` in any browser and go.

## Quick Start

```bash
# Clone
git clone https://github.com/SuperInstance/plato-construct.git
cd plato-construct

# Open directly
open index.html          # macOS
xdg-open index.html      # Linux
start index.html         # Windows

# Or serve statically
python3 -m http.server 8080
# → http://localhost:8080
```

No build step. No dependencies. No Node, no npm, no bundler. Just HTML, CSS, and vanilla JavaScript.

## The 5 Phases

The wizard walks through five phases. Each updates a live **Agent Card Preview** in the sidebar.

### Phase 1 — Declare Agent
Name your agent, choose its type (assistant, worker, sentinel, oracle, curator, custom), write a description, and pick an emoji avatar. This is the agent's identity card.

### Phase 2 — Select Modules
Browse and select capability modules organized by domain:
- **Perception** — text, vision, audio
- **Reasoning** — web search, code execution, planning, math
- **Action** — files, shell, browser, API calls
- **Memory** — short-term, long-term, vector store
- **Communication** — messaging, A2A protocol, scheduling
- **Tools** — git, containers, databases
- **Safety** — guard rails, audit logs, approval gates

Search and filter modules by name or domain.

### Phase 3 — Choose Interface
Pick the primary interaction mode: CLI, chat/messaging, REST API, web dashboard, voice, or A2A-only (agent-to-agent with no human interface).

### Phase 4 — Connect Fleet
Define connections to other agents, services, or endpoints. Each connection has a name, URL, and role (peer, leader, worker, service). The topology visualization shows the network structure in ASCII art.

### Phase 5 — Generate Config
Review and export the complete agent configuration as YAML or JSON. Copy to clipboard or download directly.

## Live Preview

The sidebar shows a real-time Agent Card that updates as you configure each phase. Click any phase in the progress bar to jump directly to it.

## Output Format

The generated config looks like:

```yaml
construct: '1.0'
agent:
  name: atlas
  type: assistant
  description: General-purpose research and coding assistant
  avatar: 🗺️
modules:
  - Text Analysis
  - Web Search
  - Code Execution
  - Long-term Memory
  - Git
interface: CLI / Terminal
fleet:
  - name: sentry
    endpoint: https://sentry.local
    role: peer
```

## Architecture

- **Single file** — `index.html` contains everything (HTML, CSS, JS)
- **No build step** — works as a static file
- **No dependencies** — no CDN links, no external resources
- **Dark theme** — matches the OpenConstruct visual style
- **Responsive** — works on desktop and mobile (sidebar hides on small screens)

## OpenConstruct Ecosystem

The Construct is the onboarding entry point for [OpenConstruct](https://github.com/SuperInstance), a system for building, connecting, and deploying AI agents. Related projects:

- **PLATO Rooms** — structured knowledge directories that persist across agent sessions
- **Conservation Spectral Analysis** — graph Laplacian coherence measurement across 40+ domains
- **Spectral Explorer** — interactive graph builder with live eigenvalue visualization
- **Conservation Composer** — music from graph Laplacians

## License

Apache 2.0 — everything open.

## Documentation

- [OpenConstruct Documentation](https://github.com/SuperInstance/openconstruct-docs) — ecosystem-wide docs and guides
