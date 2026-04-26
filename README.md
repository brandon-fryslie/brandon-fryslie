<!-- DAILY-DOODLE:START -->
<div align="center">
<a href="./DOODLES.md"><img src="./assets/daily-highlight.svg" width="800" alt="Daily highlight — click for the gallery" /></a>
</div>
<!-- DAILY-DOODLE:END -->

<div align="center">

# Brandon Fryslie

~~Full-Stack & Cloud Platform Engineer~~<br>
**Vibe Coder**<br>
Boulder, CO

</div>

---

<div align="center">

**Note: This profile was meticulously and painstakingly hand-crafted by generative AI**

</div>

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

*Updated April 26, 2026*

### Today

Merged PR #12 in `brandon-fryslie/brandon-fryslie`: rewrote the profile intro to the "I *used* to build software... Now I have AI do that for me" voice, added `assets/neural-pulse-80s.svg` (Business Requirements → hidden layers → Customer Value, retro 80s) below the prose, prepended a permanent AI SLOP entry to `DOODLES.md`, rebranded the title to "Vibe Coder" stacked across three `<br>`-separated lines with a "meticulously and painstakingly hand-crafted by generative AI" disclaimer, and pulsed the CUSTOMER VALUE label with a 3.1s prime-duration font-size animation. Three intermediate orb experiments (irrational-duration chained paths, opacity-fade shudder masking, single-path simplification) were reverted, leaving only the Customer Value pulse on the banner.

### This Week

`brandon-fryslie/brandon-fryslie` took 11 commits: PR #12's intro rewrite + neural-pulse banner + AI SLOP gallery move, an `rsvg-convert` preview loop and click-to-gallery anchor, the daily doodle gallery (`DOODLES.md`) and per-day `doodle-archive/YYYY/MM/` SVG store, a matter-of-fact narrative voice with rotating Selected Projects (#11), corrected stats-card numbers (#10), a date-prominence rule for future doodles (#9), the daily doodle hoisted to its own top-of-README marker (#8), a concurrency group serializing daily-highlights runs (#7), Opus 4.7 pinned with a Verify step that fails on no-op or denial (#5), the Claude job's permitted tools scoped (#4), and the personal email removed from the footer. `shader-playground` took 10 commits — the nested Poisson-multigrid gravity scheme (inner ±16 + outer ±64, #13), the `xr-panel` rewrite (#12) wiring the hand-tracking foundation, a unified two-hand pinch-to-scale gesture pipeline, an xr release-ray pinch-end fix, the zoom-out range extended to 200m to match desktop, an `XR.md` gesture/zoom doc, and the attractor lifecycle aligned with `simStep` (PR #10). `links-issue-tracker` took 9 commits including composite `(epic_rank, own_rank)` ordering for `lit ready` (#75), inline parent descriptions in `lit show` (#74), parent-epic context carried per row (#73), epics excluded from the default ready set (#72), the `lit quickstart --eject` template-override model (#71), legacy pre-push hook markers removed (#69), and an auto-compact Dolt pass before sync push (#67). `tmux-control-mode-js` took 6 commits — scoped under `@promptctl` with a Release-triggered publish workflow, npm workspaces for the examples demo, `requestReport` integration test gated on a tmux-version probe at module load, and `--noEmit` dropped from typecheck so `tsc --build` accepts referenced projects. `cherry-chrome-mcp` shipped three press-key fixes (puppeteer keyboard for trusted layout-aware events #2, digit/letter Code-form translation #3, explicit `SYMBOL_TO_CODE` map for the eleven shifted ASCII symbols #4). `vibedungeon-voice` was forked from `elevenlabs/elevenlabs-mcp` and declared the `claude/channel` capability for Claude Code channel registration. `tinkerpad` added a Milkdrop-style WebGPU music visualizer with gh-pages PR previews. `cc-nerf-buster` got its initial commit and a defensive `.gitignore` covering TLS material, secrets, coverage, venvs, and editor dirs.

### This Month

315 commits across 15 repositories over the past 30 days. `shader-playground` (90), `gh-pages-multiplexer` (82), `tmux-control-mode-js` (55), and `rich-js-ink` (32) carried most of the volume, followed by `links-issue-tracker` (18), the profile repo (13), and `oscilla-animator-v2` (6). The work spans WebGPU compute (nested-grid Poisson-multigrid gravity, xr-panel hand-tracking foundation, two-hand pinch-to-scale gestures), Go CLI infrastructure (Dolt-backed issue sync, composite `(epic_rank, own_rank)` ready ordering, `lit quickstart --eject` template overrides, auto-compact before sync push), terminal tooling (tmux control-mode protocol scoped under `@promptctl` with provenance publish, ink-based rich-js components), gh-pages deployment plumbing, a Chrome DevTools MCP server (`cherry-chrome-mcp`), an ElevenLabs voice fork (`vibedungeon-voice`), and the daily-highlights workflow on this profile. Active languages: Go, TypeScript, WebGPU/WGSL, Python, Shell.

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

Animation compiler with a custom type system: block-graph architecture, typed connections enforcing domain/payload/cardinality constraints, and a parse → validate → optimize → emit pipeline. Recent commits landed the 4-pillar architecture refactor (WASM-boundary API iteration, Zod-driven semantic validation, IR coverage gates), replaced the prior `fn.toString()` → acorn → walker fixture pipeline with a typed GPU-IR DSL across all 29 fixtures (E expression-builder class, Scope `$` callable, 30+ WGSL builtins), added the camera system (DSL redesign, ortho projection, `StoreGlobal`, `System_CameraUpdate`, C1 compiler backend slices), Phase 5 MRT plus depth-only render passes with MSAA reconciliation, Safari WebGPU viewport/quad-camera fixes, and a GPU-IR gap analysis pass.

### [cc-dump](https://github.com/brandon-fryslie/cc-dump)
**Python · MIT**

HTTP proxy that intercepts Anthropic API calls and prints unified diffs of system prompt changes between requests. Recent commits skipped geometry work on search-highlight rerenders (style-only bgcolor changes never alter line counts or strip widths), bounded `_invalidate_cache_for_turns` to `[0, end)` so viewport-only rerenders stop wiping the entire cache, cached per-turn search traversal data, unified the dual expansion-override system behind a single `vis_override` field on `BlockViewState`, introduced a Fenwick tree for O(log n) line-to-turn lookup, preserved the line cache during selection updates, moved shared Input/Select form-element CSS into `styles.css`, made sidebar panels (Settings, LaunchConfig, SideChannel) survive hot-reload, and removed the AI side-channel feature entirely.

### [shader-playground](https://github.com/brandon-fryslie/shader-playground)
**TypeScript**

WebGPU shader experimentation environment. Recent commits scaffolded and then brought online the nested Poisson-multigrid gravity scheme: a 64³ outer grid spans the ±64 periodic domain (cell size 2.0) and runs alongside a shrunk 128³ inner grid over ±16 (cell size 0.25, restoring 4× sharper galaxy-region resolution); `pm.interpolate_nested.wgsl` smoothstep-blends inner/outer force across the `[domainHalf-2, domainHalf]` shell; `pm.deposit.wgsl` filters out-of-domain particles to avoid wrap-pollution of the inner grid via the periodic index wrap; and diagnostics `__pmDumpOuterDensity`, `__pmDumpOuterPotential`, and `__pmMaxResidual` (returning per-grid residuals) cover convergence on both grids. The blended-force commit was reverted in a follow-up.

</td>
<td width="50%" valign="top">

### [gh-pages-multiplexer](https://github.com/brandon-fryslie/gh-pages-multiplexer)
**TypeScript**

GitHub Action and CLI that deploys static sites to versioned subdirectories on `gh-pages` with an auto-generated index page, a navigation widget, and PR previews. Recent commits added opt-in transparent storage namespacing — a synchronous head-injected `<script>` replaces `window.localStorage` and `window.sessionStorage` with a Proxy that prefixes keys with `gh-pm:<owner>/<repo>/<version>`, scopes `.length`/`.key(i)`/`.clear()` to the namespace, sets `__ghPmStorageWrapped` to prevent double-wrapping, and ships behind a `namespace-storage` action input and `--namespace-storage` CLI flag — alongside 19 new tests (12 jsdom runtime, 7 injector) and a `vitest.config.ts` switch to `pool: 'threads'`. Also generated `robots.txt` and `sitemap.xml` at the worktree root, injected canonical URLs on non-PR versions, added `noindex` meta tags on PR preview directories, and pulled GitHub Release metadata for tag deploys.

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Recent commits ordered `lit ready` leaves by a composite `(effective_epic_rank, own_rank)` key so re-ranking an epic moves its leaves as a block without touching child ranks, inlined parent descriptions in `lit show` so fat-ticket epic context is read first (one tool call instead of two), normalized `indentLines` to `TrimRight` trailing newlines so parent descriptions stop emitting a stray prefix-only line, excluded epics from the default ready set, and closed slice 3/6 and slice 4/6 of the `links-agent-epic-model-uew` epic.

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. Recent commits scoped the package as `@promptctl/tmux-control-mode-js` with `publishConfig.access=public` ahead of the first npm publish, added a Release-triggered workflow running lint/format/typecheck/tests before `npm publish --provenance` (guarded by `prepublishOnly` running `check:deps` and `build`), adopted npm workspaces so one root `npm install` covers `examples/web-multiplexer` and the demo's separate `package-lock.json` is gone, deduped `BRIDGE_PORT` to `shared/config`, gated the `requestReport` integration test on a tmux-version probe at module load, dropped `--noEmit` from typecheck so `tsc --build` accepts referenced projects, and aligned `PROJECT.md`/`REQUIREMENTS.md` descope language with the documented tmux 3.2+ floor.

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

## Technical "Writing" (Claude wrote these)

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

## Publications

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
