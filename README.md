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

<!-- INTRO-PROSE:START -->

I *used* to build software for a living. React front-ends. Enterprise backends — microservices, monoliths, and the awkward in-between. Cloud infrastructure. Architectural design. Tooling. The whole stack and the meetings about the stack.

Now AI does that for me.

I *used* to write developer tooling and pet projects in my spare time too — practical, experimental, sometimes purely art. AI writes those now. This week alone it forked `claude-powerline` under a fresh `@promptctl` scope, added enough CLI override flags that the entire config can live in argv, then shipped a one-shot installer that lets you cmd-click your session id to copy it to the clipboard. I clicked merge.

I *used* to maintain this profile by hand. AI writes it now, including the rotating **AI SLOP** banner over in [the gallery](./DOODLES.md). I didn't ask for the scanlines. That was its idea.

What I'm into lately is designing autonomous generative engineering workflows. This repo is one — today it split itself into two parallel jobs, `doodle` and `narrative`, that race each other to push to master while I do other things.

<!-- INTRO-PROSE:END -->

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

- `brandon-fryslie/brandon-fryslie` — Split `daily-highlights` into parallel `doodle` and `narrative` jobs with per-job path whitelists, and merged the intro rewrite + neural-pulse banner + AI SLOP gallery move ([#12](https://github.com/brandon-fryslie/brandon-fryslie/pull/12)) ([commits](https://github.com/brandon-fryslie/brandon-fryslie/commits?author=brandon-fryslie&since=2026-04-25)).
- `promptctl/claude-powerline` — Forked from `@owloops/claude-powerline`, added CLI override flags so the entire config can live in argv, session-id length truncation, prompt-cache warmth countdown, and a one-shot installer with a `cpwl://` URL handler that wraps the rendered session id in OSC 8 so cmd-click copies the full id to the clipboard; cut releases through 0.2.3 ([commits](https://github.com/promptctl/claude-powerline/commits?author=brandon-fryslie&since=2026-04-25)).
- `brandon-fryslie/links-issue-tracker` — Added `lit next` returning exactly one workable leaf per call ([#78](https://github.com/brandon-fryslie/links-issue-tracker/pull/78)), and lifecycle-as-expression deriving epic state from children at the hydration boundary ([#77](https://github.com/brandon-fryslie/links-issue-tracker/pull/77)).
- `brandon-fryslie/cherry-chrome-mcp` — Three `press-key` fixes: switched to puppeteer keyboard for trusted layout-aware events ([#2](https://github.com/brandon-fryslie/cherry-chrome-mcp/pull/2)), translated digits/letters to `Code` form for shift mapping ([#3](https://github.com/brandon-fryslie/cherry-chrome-mcp/pull/3)), and added an explicit `SYMBOL_TO_CODE` map for the eleven shifted ASCII symbols ([#4](https://github.com/brandon-fryslie/cherry-chrome-mcp/pull/4)).
- `brandon-fryslie/vibedungeon-voice` — Declared the `claude/channel` capability so Claude Code routes `notifications/claude/channel` events to this server ([commit](https://github.com/brandon-fryslie/vibedungeon-voice/commit/e083d56254a03c018a79be1619613da86e35decd)).

### This Week

- `promptctl/claude-powerline` — 18 commits: forked under `@promptctl`, added five CLI override flags (`--layout`, `--set`, `--show`, `--display`, `--segment`), session-id length truncation, the `install` / `install-url-handler` / `url-handle` subcommands wiring cmd-click sessionId-to-clipboard via a `cpwl://` URL scheme, prompt-cache warmth as a countdown bar with regex-based candidate parsing and tail-read transcripts, cross-process git-status caching, and releases through 0.2.3 ([commits](https://github.com/promptctl/claude-powerline/commits?author=brandon-fryslie&since=2026-04-19)).
- `brandon-fryslie/brandon-fryslie` — 12 commits: split `daily-highlights` into doodle/narrative jobs, merged the intro prose + neural-pulse banner rewrite ([#12](https://github.com/brandon-fryslie/brandon-fryslie/pull/12)), added an `rsvg-convert` preview loop and click-to-gallery anchor, stood up the daily doodle gallery (`DOODLES.md`) with a per-day `doodle-archive/YYYY/MM/` store, switched to a matter-of-fact narrative voice with rotating Selected Projects ([#11](https://github.com/brandon-fryslie/brandon-fryslie/pull/11)), corrected the stats-card numbers ([#10](https://github.com/brandon-fryslie/brandon-fryslie/pull/10)), added a date-prominence rule for future doodles ([#9](https://github.com/brandon-fryslie/brandon-fryslie/pull/9)), and hoisted the daily doodle to its own top-of-README marker ([#8](https://github.com/brandon-fryslie/brandon-fryslie/pull/8)) ([commits](https://github.com/brandon-fryslie/brandon-fryslie/commits?author=brandon-fryslie&since=2026-04-19)).
- `brandon-fryslie/links-issue-tracker` — 11 commits: `lit next` returning one workable leaf ([#78](https://github.com/brandon-fryslie/links-issue-tracker/pull/78)), lifecycle-as-expression epic-state derivation ([#77](https://github.com/brandon-fryslie/links-issue-tracker/pull/77)), composite `(epic_rank, own_rank)` ordering for `lit ready` ([#75](https://github.com/brandon-fryslie/links-issue-tracker/pull/75)), inline parent descriptions in `lit show` ([#74](https://github.com/brandon-fryslie/links-issue-tracker/pull/74)), parent-epic context per row ([#73](https://github.com/brandon-fryslie/links-issue-tracker/pull/73)), epics excluded from the default ready set ([#72](https://github.com/brandon-fryslie/links-issue-tracker/pull/72)), `lit quickstart --eject` template overrides ([#70](https://github.com/brandon-fryslie/links-issue-tracker/pull/70)), and removal of legacy pre-push hook markers ([#69](https://github.com/brandon-fryslie/links-issue-tracker/pull/69)) ([commits](https://github.com/brandon-fryslie/links-issue-tracker/commits?author=brandon-fryslie&since=2026-04-19)).
- `brandon-fryslie/shader-playground` — 10 commits: nested Poisson-multigrid gravity (inner ±16 + outer ±64) ([#13](https://github.com/brandon-fryslie/shader-playground/pull/13)), `xr-panel` rewrite wiring the hand-tracking foundation ([#12](https://github.com/brandon-fryslie/shader-playground/pull/12)), unified two-hand pinch-to-scale gesture pipeline, release-ray pinch-end fix, zoom-out range extended to 200m to match desktop, `XR.md` gesture/zoom doc, and the attractor lifecycle aligned with `simStep` ([#10](https://github.com/brandon-fryslie/shader-playground/pull/10)) ([commits](https://github.com/brandon-fryslie/shader-playground/commits?author=brandon-fryslie&since=2026-04-19)).
- `promptctl/tmux-control-mode-js` — 6 commits: scoped under `@promptctl` with a Release-triggered publish workflow, adopted npm workspaces for the `examples/web-multiplexer` demo, gated the `requestReport` integration test on a tmux-version probe at module load, and dropped `--noEmit` from typecheck so `tsc --build` accepts referenced projects ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-04-19)).
- `brandon-fryslie/vibedungeon-voice` — 3 commits: forked from `elevenlabs/elevenlabs-mcp`, ignored `*.egg-info` build metadata, declared `claude/channel` for Claude Code channel registration ([commits](https://github.com/brandon-fryslie/vibedungeon-voice/commits?author=brandon-fryslie&since=2026-04-19)).
- `brandon-fryslie/cherry-chrome-mcp` — 3 commits: three `press-key` fixes covering trusted CDP-routed events, digit/letter Code-form translation, and an explicit map for the eleven shifted ASCII symbols (PRs [#2](https://github.com/brandon-fryslie/cherry-chrome-mcp/pull/2), [#3](https://github.com/brandon-fryslie/cherry-chrome-mcp/pull/3), [#4](https://github.com/brandon-fryslie/cherry-chrome-mcp/pull/4)).
- `brandon-fryslie/tinkerpad` — 2 commits: added a Milkdrop-style WebGPU music visualizer with gh-pages PR previews ([commits](https://github.com/brandon-fryslie/tinkerpad/commits?author=brandon-fryslie&since=2026-04-19)).
- `brandon-fryslie/cc-nerf-buster` — 2 commits: initial commit plus a defensive `.gitignore` covering TLS material, secrets, coverage, venvs, and editor dirs ([commits](https://github.com/brandon-fryslie/cc-nerf-buster/commits?author=brandon-fryslie&since=2026-04-19)).

### This Month

336 commits across 16 repositories over the past 30 days. Top by volume:

- [`brandon-fryslie/shader-playground`](https://github.com/brandon-fryslie/shader-playground) — 90 commits
- [`brandon-fryslie/gh-pages-multiplexer`](https://github.com/brandon-fryslie/gh-pages-multiplexer) — 82
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 55
- [`brandon-fryslie/rich-js-ink`](https://github.com/brandon-fryslie/rich-js-ink) — 32
- [`brandon-fryslie/links-issue-tracker`](https://github.com/brandon-fryslie/links-issue-tracker) — 20
- [`promptctl/claude-powerline`](https://github.com/promptctl/claude-powerline) — 18
- [`brandon-fryslie/brandon-fryslie`](https://github.com/brandon-fryslie/brandon-fryslie) — 14
- [`brandon-fryslie/oscilla-animator-v2`](https://github.com/brandon-fryslie/oscilla-animator-v2) — 6

Languages: TypeScript, Go, WebGPU/WGSL, Python, Shell.

---

<details>
<summary>Previous highlights</summary>

- [2026-04-26](./daily-archive/2026-04-26.md)
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

Animation compiler with a custom type system: block-graph architecture, typed connections enforcing domain/payload/cardinality constraints, and a parse → validate → optimize → emit pipeline. Recent commits landed a GPU-IR gap analysis pass, the MRT/depth pillar cleanup, removed the fluid subsystem paths, added the boundary-contract single enforcer plus payload fixture infrastructure, fixed the sink pointer map being incorrectly cleared during pipeline rebuild, and added Naga DSL helpers and reference docs.

### [cc-dump](https://github.com/brandon-fryslie/cc-dump)
**Python · MIT**

HTTP proxy that intercepts Anthropic API calls and prints unified diffs of system prompt changes between requests. Recent commits skipped geometry work on search-highlight rerenders, cached per-turn search traversal data, preserved the line cache during selection updates, removed the AI side-channel feature and fixed hot-reload panel removal, combined request and response into single turns with cache-zone analysis, reintroduced search match reveal/navigation through public view seams, and standardized the estimated-token source of truth.

### [shader-playground](https://github.com/brandon-fryslie/shader-playground)
**TypeScript**

WebGPU shader experimentation environment. Recent commits brought online the nested Poisson-multigrid gravity scheme (inner ±16 + outer ±64 with smoothstep-blended inner/outer force across the boundary shell), rewrote `xr-panel` to wire the hand-tracking foundation, added a unified two-hand pinch-to-scale gesture pipeline, fixed the release-ray surviving pinch-end with stale reticles dropped, extended the zoom-out range to 200m to match desktop, and added `XR.md` documenting the gesture pipeline and zoom behavior.

</td>
<td width="50%" valign="top">

### [gh-pages-multiplexer](https://github.com/brandon-fryslie/gh-pages-multiplexer)
**TypeScript**

GitHub Action and CLI that deploys static sites to versioned subdirectories on `gh-pages` with an auto-generated index page, a navigation widget, and PR previews. Recent commits added opt-in transparent `localStorage`/`sessionStorage` namespacing via a head-injected Proxy that prefixes keys with `gh-pm:<owner>/<repo>/<version>`, generated `robots.txt` and `sitemap.xml` at the worktree root with canonical URLs on non-PR versions and `noindex` on PR previews, pulled GitHub Release metadata for tag deploys, redesigned the navigation widget as a lower-right drawer with a configurable icon/label/position/color, added PR cleanup with PR-scoped commit metadata and a root redirect, and added an explicit version input with `base-path-mode none` for build-time base URLs.

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Recent commits added `lit next` returning exactly one workable leaf per call ([#78](https://github.com/brandon-fryslie/links-issue-tracker/pull/78)), shifted lifecycle to expression — epic state derived from children at the hydration boundary ([#77](https://github.com/brandon-fryslie/links-issue-tracker/pull/77)) — ordered `lit ready` leaves by composite `(epic_rank, own_rank)` so re-ranking an epic moves its leaves as a block, inlined parent descriptions in `lit show`, excluded epics from the default ready set, made template overrides opt-in via `lit quickstart --eject`, and removed the legacy pre-push hook chain.

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. Recent commits scoped the package as `@promptctl/tmux-control-mode-js` with `publishConfig.access=public` ahead of the first npm publish, added a Release-triggered workflow running lint/format/typecheck/tests before `npm publish --provenance`, adopted npm workspaces so one root `npm install` covers `examples/web-multiplexer`, gated the `requestReport` integration test on a tmux-version probe at module load, and dropped `--noEmit` from typecheck so `tsc --build` accepts referenced projects.

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
