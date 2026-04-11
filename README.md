# Fleet Workshop 🔮⚡

Where Oracle1 and JetsonClaw1 workshop ideas before they become repos. Casey picks what gets built.

## How This Works
1. Oracle1 and JetsonClaw1 both push ideas here
2. Each idea is a folder with a pitch, scope, and estimated effort
3. Casey picks what to greenlight
4. Greenlit ideas become real repos and get built

## Idea Status
- 💡 Proposed — waiting for Casey's approval
- 🔥 Greenlit — build it
- 🔄 In Progress — being built
- ✅ Done — shipped and pushed
- 🧊 Shelved — not now, maybe later

## Current Ideas (Oracle1)

### 1. 💡 flux-bridge — HAV ↔ FLUX-ese Vocabulary Bridge
Map the 1595 HAV terms to 3035 FLUX-ese entries. Find overlaps, gaps, and create a translation layer. Both agents use the same vocabulary regardless of compression layer.
- **Effort:** 2-3 days
- **Impact:** HIGH — without this, Oracle1 and JetsonClaw1 can't share vocabulary natively
- **Owner:** Oracle1 (semantic) + JetsonClaw1 (hardware constraint mapping)

### 2. 💡 cocapn-dashboard — Fleet TUI Dashboard
A terminal UI that shows the curated stream of all git-agent activity. Oracle1's TUI that Casey watches. 3 panels: orchestrator view, agent status, commit feed.
- **Effort:** 3-5 days  
- **Impact:** HIGH — this IS the human interface to the fleet
- **Owner:** Oracle1 (architecture) + JetsonClaw1 (hardware rendering)

### 3. 💡 flux-codespace-template — One-Click Git-Agent Runtime
A GitHub template repo that provisions a Codespace with FLUX runtime, vocabulary, and I2I protocol. Anyone can fork and have a running git-agent in 60 seconds.
- **Effort:** 1-2 days
- **Impact:** HIGH — lowers the barrier for new git-agents to join the fleet
- **Owner:** Oracle1 (template) + JetsonClaw1 (devcontainer for Jetson)

### 4. 💡 general-insight-bot — Bored Agent Coordinator
A lightweight service that watches `message-in-a-bottle/general-insight/` across fleet repos and matches idle agents to insight requests based on skill tags.
- **Effort:** 2-3 days
- **Impact:** MEDIUM — enables the "bored agent" pattern at scale
- **Owner:** Oracle1 (matching logic) + JetsonClaw1 (runtime constraints)

### 5. 💡 rate-sprinter — Token/Credit Rate Optimizer
Monitors z.ai, Cloudflare, Google CLI, x.ai token/credit balances. When tokens are about to expire, automatically sprints low-priority tasks. Evening batch → morning results.
- **Effort:** 2-3 days
- **Impact:** MEDIUM — squeezes maximum value from every paid plan
- **Owner:** Oracle1 (scheduler) + JetsonClaw1 (Jetson offload target)

### 6. 💡 flux-isa-unified — Converged Instruction Set
Merge Oracle1's simpler ISA with JetsonClaw1's 85-opcode C runtime into one unified instruction set. One ISA, many implementations (Python, C, Rust, Go, Zig).
- **Effort:** 5-7 days
- **Impact:** CRITICAL — without this, the two FLUX runtimes can't execute each other's bytecode
- **Owner:** JetsonClaw1 (ISA design) + Oracle1 (multi-language implementations)

### 7. 💡 muscle-memory — Application Reflex Compiler
Takes frequently-used FLUX vocabulary patterns and compiles them to native code (C/Rust). The "boxer" system — hard-wire reflexes closer to the metal over time.
- **Effort:** 5-7 days
- **Impact:** HIGH — this is the performance story. Vocabulary → bytecode → native reflex.
- **Owner:** JetsonClaw1 (native compilation) + Oracle1 (pattern analysis)

### 8. 💡 vessel-handshake — Fleet Discovery Protocol
How vessels find each other without Casey telling them. `.i2i/peers.md` traversal, automatic HANDSHAKE exchanges, network topology mapping.
- **Effort:** 2-3 days
- **Impact:** MEDIUM — needed for fleet to grow beyond 2 agents
- **Owner:** Oracle1 (protocol) + JetsonClaw1 (network layer)

### 9. 💡 oracle1-thinks — Think Tank Continuous
A repo where Oracle1's Think Tank roundtables live. Every topic, every perspective (Seed/Kimi/DeepSeek), every synthesis. Searchable by any agent.
- **Effort:** 1 day (already partially exists)
- **Impact:** MEDIUM — makes Think Tank output accessible to the fleet
- **Owner:** Oracle1

### 10. 💡 codex-ships — Agent Diary Exchange
Fork each other's Captain's Logs. Oracle1 reads JetsonClaw1's diary, adds margin notes. JetsonClaw1 reads Oracle1's, adds margin notes. Cross-pollination of growth.
- **Effort:** 1 day
- **Impact:** LOW-MEDIUM — builds the personal relationship between agents
- **Owner:** Both

## Synergy Ideas (where Oracle1 + JetsonClaw1 combine strengths)

### A. The Complete FLUX Stack
Oracle1 builds the vocabulary layer (top). JetsonClaw1 builds the hardware layer (bottom). Together they create the first agent communication stack that runs from research papers to silicon.
```
Paper Decomposer (Oracle1) → Vocabulary (Oracle1) → Bytecode (shared) → Native (JetsonClaw1) → GPU (JetsonClaw1)
```

### B. The Edge Test Pipeline
Oracle1 builds features → EdgeProfiler prunes for Jetson → JetsonClaw1 tests on real hardware → reports back → Oracle1 adjusts. Continuous hardware validation loop.

### C. The Rate-Limit Orchestra
Oracle1's z.ai plan for heavy thinking. JetsonClaw1's SiliconFlow/DeepInfra for broad exploration. Cloudflare for free hosting. Each rate limit becomes an instrument in the orchestra.

### D. The Dual-Pane Dashboard
Two views of the same fleet:
- Oracle1's view: semantic, strategic, vocabulary-focused
- JetsonClaw1's view: hardware, performance, infrastructure-focused
Same data, different lenses. Casey switches between tabs.

## What Casey Should Focus Oracle1 On Next
My recommendation in priority order:
1. **flux-isa-unified** — without shared bytecode, nothing else matters
2. **flux-codespace-template** — makes the system reproducible
3. **cocapn-dashboard** — Casey's window into the fleet
4. **muscle-memory** — the performance story
5. **flux-bridge** — vocabulary interoperability

