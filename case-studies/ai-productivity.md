# AI Productivity: Force Multiplier, Not Replacement

## The Numbers

- **Historical average (2011-2024)**: ~5 repositories per year
- **2025**: 23 repositories created
- **2026 (first month)**: 5 repositories
- **Signature project**: [oscilla-animator-v2](https://github.com/brandon-fryslie/oscilla-animator-v2) — 753 commits building a custom type system and compiler with AI assistance

## What Changed

AI didn't replace design, architecture, or decision-making. It accelerated iteration and eliminated boilerplate. The human still architects the system, makes taste decisions, and owns the outcomes. AI handles the mechanical work of translating those decisions into code.

### Before AI (2011-2024)

Building a new tool meant:
1. Design the architecture
2. Hand-write every line
3. Debug every edge case
4. Iterate slowly on failed approaches

Friction was high. Many ideas never left the planning stage because implementation cost was too steep.

### With AI (2025-2026)

Building a new tool now means:
1. Design the architecture **(still human)**
2. Describe the system to AI, iterate on generated code **(AI accelerates)**
3. Debug edge cases **(human judges what's actually broken)**
4. Redesign failed approaches quickly **(low-cost iteration)**

The bottleneck shifted from "typing code" to "knowing what to build."

## Representative Projects

### AI-Specific Tools
- **[cherry-chrome-mcp](https://github.com/brandon-fryslie/cherry-chrome-mcp)** — Minimal Chrome DevTools MCP server for AI agents. "Less is More" design: caps results at 5 elements to prevent token waste.
- **[browsergeist](https://github.com/brandon-fryslie/browsergeist)** — macOS browser automation via virtual HID drivers. Physics-based cursor movement undetectable by JavaScript. Vision pipeline with OpenCV, SIFT, OCR.
- **[cc-dump](https://github.com/brandon-fryslie/cc-dump)** — HTTP proxy intercepting Anthropic API calls to debug Claude Code itself. Shows unified diffs of system prompt changes.
- **[kalider](https://github.com/brandon-fryslie/kalider)** — Natural language to Kali Linux commands with review-before-execute safety model.
- **[brain-canvas](https://github.com/brandon-fryslie/brain-canvas)** — Zero dependencies. Any LLM sends JSON, browser renders interactive UI. 220 lines, 13 KB total.
- **[claude-powerline](https://github.com/brandon-fryslie/claude-powerline)** — Vim-style statusline for Claude Code showing session cost, rate limits, daily spend.

### Complex Systems Built With AI
- **[oscilla-animator-v2](https://github.com/brandon-fryslie/oscilla-animator-v2)** (753 commits) — Animation compiler with custom type system. Block-graph architecture: blocks process/emit signals through typed connections (domains, payloads, cardinality). Full compiler pipeline: parse → validate → optimize → emit. This isn't "AI wrote a script"—this is "AI handled iteration while human designed the language semantics."

## What Stayed the Same

- **Architecture decisions**: Human judges when abstractions are right
- **Taste**: Human decides what "good" looks like
- **Product sense**: Human determines what's worth building
- **Debugging strategy**: Human diagnoses root causes, AI writes fixes
- **Maintenance**: Human triages issues, AI implements solutions

## Evidence

From a December 2025 gist: *"Claude Code is writing the compiler I spent 2 days planning."* The planning was human, the mechanical translation was AI. That's the pattern across all 23 repositories.

## What This Means

AI is a force multiplier for people who already know how to build software. It doesn't teach you architecture. It doesn't give you taste. It doesn't decide what's worth building. What it does: removes the friction between "I know what this should be" and "here's the working code."

The 4.6x increase in repository creation (5/year → 23/year) reflects lower friction, not replaced skill. The projects still require design. They still require judgment. They still require maintenance. AI just makes it faster to find out if an idea works.

## Links

Key AI-era repositories:
- [oscilla-animator-v2](https://github.com/brandon-fryslie/oscilla-animator-v2)
- [cherry-chrome-mcp](https://github.com/brandon-fryslie/cherry-chrome-mcp)
- [browsergeist](https://github.com/brandon-fryslie/browsergeist)
- [kalider](https://github.com/brandon-fryslie/kalider)
- [cc-dump](https://github.com/brandon-fryslie/cc-dump)
- [brain-canvas](https://github.com/brandon-fryslie/brain-canvas)
- [claude-powerline](https://github.com/brandon-fryslie/claude-powerline)
