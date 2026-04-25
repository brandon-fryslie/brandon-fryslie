<!-- DAILY-DOODLE:START -->
<div align="center">
<img src="./assets/daily-highlight.svg" width="800" alt="Daily highlight" />
</div>
<!-- DAILY-DOODLE:END -->

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

*Updated April 25, 2026*

### Today

`cc-nerf-buster` reached a usable shape: README rewritten around problem, approach, and measured results, security model split into its own document, MIT license added, module path renamed, CI workflow with tool-version pins added, a quota-bounds reporting workflow landed, and probe accounting, resume flow, and metric scope selection were corrected. `links-issue-tracker` shipped the agent-epic ordering work — composite `(epic_rank, own_rank)` sort for `lit ready`, inline parent descriptions in `lit show`, parent-epic context carried per row, and epics excluded from the default ready set. The profile repo's daily-highlights generator gained a matter-of-fact narrative voice, a separate Claude step that rotates Selected Projects from real commit volume, corrected daily-stats card numbers, and a legibility rule for on-canvas SVG text.

### This Week

`shader-playground` took 25 commits: the nested Poisson-multigrid gravity scheme landed (inner ±16, outer ±64, Dirichlet boundary conditions across the ±14..±16 shell), the `xr-panel` rewrite wired the hand-tracking foundation, a unified two-hand pinch-to-scale gesture pipeline arrived, depth-buffer submission for parallax-correct compositor reprojection was added, WebXR/WebGPU error diagnostics were broadened, and the attractor lifecycle moved off wall-clock onto simStep in the reversible-physics path. `tmux-control-mode-js` took 16 commits: scoped under `@promptctl`, added a Release-triggered npm publish workflow with provenance, adopted npm workspaces for the `examples/web-multiplexer` demo, added Protocol Inspector and Activity Heatmap views, a CI workflow for lint/format/typecheck/build/tests, an MIT license, a documented tmux 3.2+ compatibility floor, and a 0.1.0 changelog. `cc-nerf-buster` was created and built out over 11 commits. `links-issue-tracker` took 10 commits including a `lit quickstart --eject` template-override model, a `pflag.Changed` proxy, an auto-compact pass on the Dolt store before sync push, and removal of legacy pre-push hook markers. `tinkerpad` added a Milkdrop-style WebGPU music visualizer with gh-pages PR previews. The profile repo itself absorbed the meta-tooling pass: pinning Opus 4.7, scoping the daily Claude job's permitted tools, a concurrency group serializing manual dispatches against the cron, the daily doodle hoisted to its own marker pair at the top of the README, and a date-prominence rule for future doodles.

### This Month

317 commits across 14 repositories over the past 30 days. `shader-playground` (90), `gh-pages-multiplexer` (82), `tmux-control-mode-js` (55), and `rich-js-ink` (32) carried most of the volume, followed by `links-issue-tracker` (20), `cc-nerf-buster` (11), and the profile repo (10). The work spans WebGPU compute (nested-grid gravity, reversible physics with time reversal), Go CLI infrastructure (Dolt-backed issue sync, agent-epic ordering, template eject), terminal tooling (tmux control-mode protocol, ink-based rich-js components, rad-plugins for JetBrains and Copilot proxies), gh-pages deployment plumbing, and a new Go probe that measures Claude Code's quota bounds directly. Active languages: Go, TypeScript, WebGPU/WGSL, Python, Shell.

---

<details>
<summary>Previous highlights</summary>

- [2026-04-25](./daily-archive/2026-04-25.md)
- [2026-04-24](./daily-archive/2026-04-24.md)
- [2026-03-17](./daily-archive/2026-03-17.md)

</details>

<!-- RECENT-ACTIVITY:END -->

---

## Selected Projects

<!-- SELECTED-PROJECTS:START -->
<table>
<tr>
<td width="50%" valign="top">

### [oscilla-animator-v2](https://github.com/brandon-fryslie/oscilla-animator-v2)
**TypeScript**

Compiler for a domain-specific animation language. Block-graph architecture with a custom type system; typed connections enforce domain, payload, and cardinality constraints across a parse → validate → optimize → emit pipeline. Recently replaced the source-text-parsing GPU-IR DSL (`fn.toString()` → acorn → walker → IR) with a typed expression builder (`E` class for fluent arithmetic and swizzle, `Scope` callable for thread/instance/vertex intrinsics) covering all 29 fixtures, landed the 4-pillar architecture refactor, added Phase 5 MRT plus depth-only render passes with MSAA reconciliation, and finished a GPU-IR gap analysis pass.

### [cc-dump](https://github.com/brandon-fryslie/cc-dump)
**Python · MIT**

HTTP proxy that intercepts Anthropic API calls and prints unified diffs of system prompt changes between requests. Recently skipped geometry work on search-highlight rerenders (style-only changes never alter line counts or strip widths), fixed `_invalidate_cache_for_turns` to bound `[0, end)` correctly so viewport-only search rerenders no longer wipe the entire cache, cached per-turn search traversal data, unified expansion overrides behind a single `vis_override` field on `BlockViewState`, and removed the AI side-channel feature.

### [shader-playground](https://github.com/brandon-fryslie/shader-playground)
**TypeScript**

WebGPU shader experimentation environment. Recently scaffolded a nested Poisson-multigrid gravity scheme — a 64³ outer grid spanning the full ±64 periodic domain running alongside the existing 128³ inner grid, both reusing the same `pm.*` shaders via `gridRes`/`domainHalf`/`cellSize` uniforms — and wired diagnostics (`__pmDumpOuterDensity`, `__pmDumpOuterPotential`, `__pmMaxResidual` returning per-grid residuals) ahead of the inner-grid shrink to ±16 and the smoothstep-blended force transition.

</td>
<td width="50%" valign="top">

### [gh-pages-multiplexer](https://github.com/brandon-fryslie/gh-pages-multiplexer)
**TypeScript**

GitHub Action and CLI that deploys static sites to versioned subdirectories on `gh-pages`, with auto-generated index pages, a navigation widget, and PR previews. Recently added opt-in transparent localStorage/sessionStorage namespacing — a synchronous head-injected `<script>` that wraps `window.localStorage` and `window.sessionStorage` in a Proxy prefixing keys with `gh-pm:<owner>/<repo>/<version>` to prevent collisions across repos served from a shared `<user>.github.io` origin — plus generated `robots.txt` and `sitemap.xml`, canonical-URL injection on non-PR versions, `noindex` meta tags on PR preview directories, and GitHub Release metadata for tag deploys.

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Recently added a composite `(epic_rank, own_rank)` sort to `lit ready` so leaves group by epic without forcing cross-epic context switches (an epic re-rank now moves its leaves as a block without touching child ranks), inlined parent descriptions in `lit show` so the containing fat-ticket context is read first, normalized indent handling so trailing-newline parent descriptions stop emitting a stray prefix-only line, and excluded epics from the default ready set.

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. Recently scoped the package as `@promptctl/tmux-control-mode-js` with `publishConfig.access=public`, added a Release-triggered npm publish workflow running the full lint/format/typecheck/test gate before `npm publish --provenance`, adopted npm workspaces for the `examples/web-multiplexer` demo (one root install covers both, the demo's separate lockfile removed), gated the `requestReport` integration test on a tmux-version probe at module load, and shipped a 0.1.0 changelog with the documented tmux 3.2+ compatibility floor.

</td>
</tr>
</table>
<!-- SELECTED-PROJECTS:END -->

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

Boulder, CO

</div>
