<div align="center">

# Brandon Fryslie

**Full-Stack & Cloud Platform Engineer** · Boulder, CO

</div>

---

I build software.  Professionally, that has typically been front-end using React, enterprise backend (microservices/monoliths), cloud infrastructure automation, the architectural design work that enforces stability and alignment, and the tooling that holds it together and ensures an organization is able to fire on all cylinders.

Outside of work, I enjoy writing a variety of developer focused tooling and pet projects.  Some of them are practical, some of them are to learn a particular technology or skill, some of them are to create art, but all of them are fun.

My passion lately has been around designing autonomous generative engineering workflows using AI.  Such as this repo, which is largely AI generated on a daily basis.

<div align="center">
<img src="./assets/daily-stats.svg" width="800" />
</div>

---

<!-- RECENT-ACTIVITY:START -->

## Recent Engineering Work

*Updated April 24, 2026*

<div align="center">
<img src="./assets/daily-highlight.svg" width="800" />
</div>

### Today

Fixed the `daily-highlights` CI workflow — the action had been silently denied every file write and `gh` call since its rewrite, producing zero commits despite appearing to succeed. Shipped two substantive features to `links-issue-tracker`: a filter preventing epics from surfacing in `lit ready` (agents can't claim epics directly), and a template-eject system (`lit quickstart --eject`) that separates user overrides from embedded defaults, ending silent cache-staleness. Meanwhile, `shader-playground` landed Phase A of a nested Poisson-multigrid gravity solver — inner 128³ grid at ±16 with Dirichlet boundary conditions sampled from an outer 64³ grid at ±64, delivering 4× sharper central gravity with a smoothstep-blended force transition and full V-cycle per frame.

### This Week

Executed a large-scale modularization of `links-issue-tracker`, splitting the monolithic `cli.go` (2,875 lines) into eight focused modules — sync, bulk, backup, doctor, dependency, issue relations, and text output — while simultaneously decomposing `store.go` (3,320 lines) into schema, labels, ranking, relations, and import/export packages. Alongside the refactor, shipped an empty-remote detection fix for cold-start sync failures and a `pflag.Changed` proxy to correctly distinguish flag-absent from flag-passed-with-empty-value. In `shader-playground`, resolved a phase-split V-cycle bug that was producing static animation, then built and enabled the full nested PM gravity scheme with Dirichlet inner boundary conditions — a significant architecture milestone for the WebGPU N-body simulation.

### This Month

296 commits across 12 repositories over the past 30 days, with `shader-playground` and `links-issue-tracker` as the dominant workstreams. The month shows a consistent pattern: deep systems work (GPU compute pipelines, Dolt-backed issue sync, Go package architecture) running in parallel with developer tooling (gh-pages deployment multiplexer, rich terminal components in `rich-js-ink`, rad-shell plugins). Architectural judgment is evident throughout — from the `withMutation` combinator design in the links refactor plan to the dataflow-over-control-flow shader discipline in the PM solver. Active projects span Go, TypeScript, WebGPU/WGSL, Python, and Shell, demonstrating consistent depth across the full stack.

---

<details>
<summary>Previous highlights</summary>

- [2026-03-17](./daily-archive/2026-03-17.md)

</details>

<!-- RECENT-ACTIVITY:END -->

---

## Selected Projects

<table>
<tr>
<td width="50%" valign="top">

### [chaperone-auth-gateway](https://github.com/brandon-fryslie/chaperone-auth-gateway)
**Go · MIT**

Authentication gateway supporting JWT and session-based auth with a multi-stage release pipeline. Cross-platform binaries for Linux, macOS, and Windows across amd64/arm64. Composable credential handling with documented security model.

### [oscilla-animator-v2](https://github.com/brandon-fryslie/oscilla-animator-v2)
**TypeScript · 753 commits**

Compiler for a domain-specific animation language. Custom type system built on a block-graph architecture: blocks process and emit signals through typed connections with enforced domain, payload, and cardinality constraints. Pipeline: parse, validate, optimize, emit.

### [rad-shell](https://github.com/brandon-fryslie/rad-shell)
**41★ · 7 forks · 8 years maintained**

Preconfigured Zsh environment with declarative plugin composition. Plugins resolve from any GitHub repository with a single-file manifest. Lazy-load architecture keeps startup fast under heavy plugin load. Includes rad-spinner: procedural braille-grid animations for terminal spinners.

</td>
<td width="50%" valign="top">

### [Firestorm](https://github.com/brandon-fryslie/Firestorm)
**Distributed coordination**

Control layer for networked WiFi LED controllers. NTP-style time synchronization via UDP, client-driven sequence choreography, and automatic recovery for disconnected devices. Deployed across physical art installations running continuously for multi-day events.

### [cherry-chrome-mcp](https://github.com/brandon-fryslie/cherry-chrome-mcp)
**TypeScript**

Chrome DevTools bridge for AI agents via Model Context Protocol. CSS selector-based element targeting with bounded result sets. Tool visibility adapts dynamically based on browser connection state.

### [browsergeist](https://github.com/brandon-fryslie/browsergeist)
**Python · macOS**

Browser automation through macOS virtual HID drivers — operates at the OS level, below the browser layer. Physics-based cursor movement with acceleration profiles and behavioral randomization. Vision pipeline: OpenCV template matching, SIFT feature descriptors, OCR.

</td>
</tr>
</table>

---

## More Projects

<details>
<summary><strong>Developer Tooling</strong></summary>

<br/>

- **[cc-dump](https://github.com/brandon-fryslie/cc-dump)** — HTTP proxy intercepting Anthropic API calls. Displays unified diffs of system prompt changes between requests.
- **[claude-powerline](https://github.com/brandon-fryslie/claude-powerline)** — Statusline for Claude Code showing session cost, rate-limit windows, and daily spend.
- **[long-term](https://github.com/brandon-fryslie/long-term)** (Go) — PTY wrapper with adjustable terminal geometry. Solves rendering issues in multiplexed terminals.
- **[brain-canvas](https://github.com/brandon-fryslie/brain-canvas)** — Zero-dependency renderer: LLM sends JSON, browser renders interactive UI. One command: `npx brain-canvas`.
- **[ptydriver](https://github.com/brandon-fryslie/ptydriver) + [ptytest](https://github.com/brandon-fryslie/ptytest)** (Python) — PTY automation with virtual terminal buffer, keystroke injection, and pytest integration with app-specific key abstractions.

</details>

<details>
<summary><strong>Hardware & Real-Time Systems</strong></summary>

<br/>

- **[tesseract-react](https://github.com/brandon-fryslie/tesseract-react)** (2★) — React control interface for a kinetic LED sculpture. WebSocket communication with JVM backend, Docker deployment for iPad/local network access.
- **[esp-bloom](https://github.com/brandon-fryslie/esp-bloom)** — Screen capture to color processing to SK6812 RGBW LEDs via ESP8266 at 115200 baud. RGBW for better luminosity precision.
- **[pb-sync](https://github.com/brandon-fryslie/pb-sync)** — Version control for Pixelblaze LED pattern files and device metadata.

</details>

<details>
<summary><strong>Earlier Work</strong></summary>

<br/>

- **[Smoke](https://github.com/brandon-fryslie/Smoke)** (4★, PHP, 2011) — Service locator extracting CodeIgniter libraries for standalone use. Predates widespread dependency injection adoption.
- **[ember-rest.coffee](https://github.com/brandon-fryslie/ember-rest.coffee)** (CoffeeScript, 2014) — REST adapter for Ember.js before Ember Data existed.
- **[sake](https://github.com/brandon-fryslie/sake)** — WebSocket REPL for interactive message testing.
- **[combine](https://github.com/brandon-fryslie/combine)** — PHP asset pipeline from the pre-npm era.

</details>

---

## Technical Writing

<table>
<tr>
<td width="33%" valign="top">

**[From Personal Tool to Open Source](./case-studies/rad-shell.md)**

How a shell configuration grew into a maintained project over 8 years. Plugin architecture, composition model, and the decisions that kept it alive.

</td>
<td width="33%" valign="top">

**[Building a Hardware Art Pipeline](./case-studies/led-art-stack.md)**

Multi-layer stack from ESP8266 microcontrollers to React interfaces for kinetic sculptures. Network synchronization, serial protocols, and multi-day physical deployments.

</td>
<td width="33%" valign="top">

**[AI as Force Multiplier](./case-studies/ai-productivity.md)**

23 repos in one year vs ~5 historically. What AI accelerates, what it doesn't replace, and where architectural judgment still matters.

</td>
</tr>
</table>

---

## Publication

*Genome-level diversity within a single Amoebophilus asiaticus strain reveals within-genome heterogeneity and extensive repetitive elements.*
<br/>The ISME Journal (Nature Publishing Group), 2013
<br/>[doi:10.1038/ismej.2013.159](https://www.nature.com/articles/ismej2013159)

---

## Languages & Domains

<div align="center">
<img src="./assets/tech-constellation.svg" width="800" />
</div>

---

## [SVG Animation Gallery](./GALLERY.md)

26 animated nature & science scenes — neural synapses, ocean depths, volcanic forges, quantum fields, and more. Pure CSS keyframes and SMIL, no JavaScript.

---

## Education

**University of Arizona** — Computer Science & Philosophy

---

<div align="center">
<img src="./assets/vision.svg" width="800" />
</div>

<div align="center">

brandon@fryslie.com · Boulder, CO

</div>
