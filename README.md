<!-- DAILY-DOODLE:START -->
<div align="center">
<a href="./DOODLES.md"><img src="./assets/daily-highlight.svg" width="800" alt="Daily highlight — click for the gallery" /></a>
</div>
<!-- DAILY-DOODLE:END -->

<div align="center">

# Brandon Fryslie

**Full-Stack & Cloud Platform Engineer** · Boulder, CO

</div>

---

I *used* to build software.  Professionally, that meant React front-ends, enterprise backends (microservices, monoliths, everything in between), cloud infrastructure automation, the architectural design work that kept systems stable and aligned, and the tooling that held it all together.

Now I have AI do that for me.

I *used* to write developer tooling and pet projects in my spare time — some practical, some experimental, some purely art.  Now AI writes those too.  I *used* to design, write, and maintain this very profile page.  What you're reading was generated top-to-bottom by an AI, including the giant rotating **AI SLOP** banner over in [the gallery](./DOODLES.md).  I didn't even ask for the scanlines.  That was its idea.

My passion lately is designing autonomous generative engineering workflows using AI.  Such as this repo, which regenerates itself on a daily basis while I do other things.

<div align="center">
<img src="./assets/neural-pulse-80s.svg" width="800" alt="Neural network with flowing pulses — Business Requirements feeding through hidden layers into Customer Value" />
</div>

<div align="center">
<img src="./assets/daily-stats.svg" width="800" />
</div>

---

<!-- RECENT-ACTIVITY:START -->

## Recent Engineering Work

*Updated April 25, 2026*

### Today

The profile repo added a daily doodle gallery (`DOODLES.md`, prepended per day) and a `doodle-archive/YYYY/MM/` per-day SVG store, then wrapped the live doodle in a click-to-gallery anchor. `cherry-chrome-mcp` shipped three press-key fixes: switched to puppeteer's keyboard for trusted layout-aware events (#2), translated digit and letter literals to Code form so puppeteer's shift mapping applies (#3), and added an explicit `SYMBOL_TO_CODE` map covering the eleven ASCII symbol keys with shifted counterparts (#4). `vibedungeon-voice` was forked from `elevenlabs/elevenlabs-mcp` (package and console script renamed, `*.egg-info` gitignored) and declared the `claude/channel` capability for Claude Code channel registration; `cc-nerf-buster` got its initial commit and a `.gitignore`.

### This Week

`brandon-fryslie/brandon-fryslie` took 12 commits reshaping the daily-highlights workflow: Opus 4.7 pinned, the Claude job's permitted tools scoped, a concurrency group serializing manual dispatches against the cron, the daily doodle hoisted to its own marker pair at the top of the README, a date-prominence rule for future doodles, the daily-stats card numbers corrected, a matter-of-fact narrative voice and rotating Selected Projects step, the doodle gallery + per-day SVG archive, and an `rsvg-convert` preview loop in the doodle prompt. `shader-playground` took 19 commits — the nested Poisson-multigrid gravity scheme (inner ±16, outer ±64), the `xr-panel` rewrite wiring the hand-tracking foundation, a unified two-hand pinch-to-scale gesture pipeline, depth-buffer submission for parallax-correct compositor reprojection, broadened WebXR/WebGPU error diagnostics, and the attractor lifecycle moved off wall-clock onto simStep. `tmux-control-mode-js` took 14 commits: scoped under `@promptctl`, a Release-triggered npm publish workflow with provenance, npm workspaces for the `examples/web-multiplexer` demo, Protocol Inspector and Activity Heatmap views, a CI workflow for lint/format/typecheck/build/tests, an MIT license, a documented tmux 3.2+ compatibility floor, and a 0.1.0 changelog. `links-issue-tracker` took 10 commits including composite `(epic_rank, own_rank)` ordering for `lit ready`, inline parent descriptions in `lit show`, parent-epic context carried per row, epics excluded from the default ready set, a `lit quickstart --eject` template-override model, an auto-compact pass on the Dolt store before sync push, and removal of legacy pre-push hook markers. `tinkerpad` added a Milkdrop-style WebGPU music visualizer with gh-pages PR previews. `cherry-chrome-mcp`, `cc-nerf-buster`, and `vibedungeon-voice` were created during the week.

### This Month

316 commits across 15 repositories over the past 30 days. `shader-playground` (90), `gh-pages-multiplexer` (82), `tmux-control-mode-js` (55), and `rich-js-ink` (32) carried most of the volume, followed by `links-issue-tracker` (20), the profile repo (12), and `oscilla-animator-v2` (6). The work spans WebGPU compute (nested-grid gravity, reversible physics with time reversal), Go CLI infrastructure (Dolt-backed issue sync, agent-epic ordering, template eject), terminal tooling (tmux control-mode protocol, ink-based rich-js components, rad-plugins for JetBrains and Copilot proxies), gh-pages deployment plumbing, a Chrome DevTools MCP server, and a new Go probe measuring Claude Code's quota bounds directly. Active languages: Go, TypeScript, WebGPU/WGSL, Python, Shell.

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

Compiler for a domain-specific animation language. Block-graph architecture with a custom type system; typed connections enforce domain, payload, and cardinality constraints across a parse → validate → optimize → emit pipeline. Recent commits delivered the 4-pillar architecture refactor with WASM-boundary API iteration and Zod-driven semantic validation, a typed GPU-IR DSL replacing the prior `fn.toString()` → acorn → walker pipeline across all 29 fixtures, a camera system overhaul (DSL redesign, ortho projection, semantic IR nodes, `StoreGlobal`, `System_CameraUpdate`, C1 backend slices), Phase 5 MRT plus depth-only render passes with MSAA reconciliation, viewport and quad-camera fixes for Safari WebGPU, and a GPU-IR gap analysis pass.

### [cc-dump](https://github.com/brandon-fryslie/cc-dump)
**Python · MIT**

HTTP proxy that intercepts Anthropic API calls and prints unified diffs of system prompt changes between requests. Recent commits skipped geometry work on search-highlight rerenders (style-only bgcolor changes never alter line counts or strip widths), bounded `_invalidate_cache_for_turns` to `[0, end)` so viewport-only rerenders no longer wipe the entire cache, cached per-turn search traversal data, unified the dual expansion-override system behind a single `vis_override` field on `BlockViewState`, introduced a Fenwick tree for O(log n) line-to-turn lookup, and removed the AI side-channel feature along with the hot-reload panel-removal bug.

### [shader-playground](https://github.com/brandon-fryslie/shader-playground)
**TypeScript**

WebGPU shader experimentation environment. Recent commits brought the nested Poisson-multigrid gravity scheme online: a 64³ outer grid spanning the ±64 periodic domain runs alongside a shrunk 128³ inner grid over ±16 (cell size 0.25, restoring 4× sharper galaxy-region resolution), `pm.interpolate_nested.wgsl` smoothstep-blends inner/outer force across the `[domainHalf-2, domainHalf]` shell, `pm.deposit.wgsl` filters out-of-domain particles to avoid wrap-pollution, and diagnostics (`__pmDumpOuterDensity`, `__pmDumpOuterPotential`, `__pmMaxResidual` returning per-grid residuals) cover convergence on both grids.

</td>
<td width="50%" valign="top">

### [gh-pages-multiplexer](https://github.com/brandon-fryslie/gh-pages-multiplexer)
**TypeScript**

GitHub Action and CLI that deploys static sites to versioned subdirectories on `gh-pages`, with auto-generated index pages, a navigation widget, and PR previews. Recent commits added opt-in transparent storage namespacing — a synchronous head-injected `<script>` replaces `window.localStorage` and `window.sessionStorage` with a Proxy that prefixes keys with `gh-pm:<owner>/<repo>/<version>`, scopes `.length`/`.key(i)`/`.clear()` to the namespace, sets `__ghPmStorageWrapped` to prevent double-wrapping, and ships behind a `namespace-storage` action input and `--namespace-storage` CLI flag — alongside 19 new tests (12 jsdom runtime, 7 injector) and a `vitest.config.ts` switch to `pool: 'threads'` so per-file jsdom environments resolve correctly.

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Recent commits ordered `lit ready` leaves by a composite `(effective_epic_rank, own_rank)` key so re-ranking an epic moves its leaves as a block without touching child ranks, inlined parent descriptions in `lit show` so fat-ticket context is read first (one tool call instead of two), normalized indent handling so trailing-newline parent descriptions stop emitting a stray prefix-only line, excluded epics from the default ready set, and closed slice 4/6 of the `links-agent-epic-model-uew` epic.

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. Recent commits scoped the package as `@promptctl/tmux-control-mode-js` with `publishConfig.access=public` ahead of the first npm publish, added a Release-triggered workflow running lint/format/typecheck/tests before `npm publish --provenance` (guarded by `prepublishOnly` running `check:deps` and `build`), adopted npm workspaces so one root `npm install` covers `examples/web-multiplexer` and the demo's separate lockfile is gone, gated the `requestReport` integration test on a tmux-version probe at module load, dropped `--noEmit` from typecheck so `tsc --build` accepts referenced projects, and skipped `requestReport` on tmux versions lacking the `-r` flag.

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
