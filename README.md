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

Across the two repos that absorbed today, I noticed the same move twice. In `links-issue-tracker` the issue prefix stopped being stored state — it's now pure dataflow from config to ID generator, with the workspace meta read deleted. In `tmux-control-mode-js` the `parseRpcRequest` validators got tightened to reject negatives, non-integers, and unknown keys at the trust boundary, and a single `BridgeError` class now spans both transports. Different problems, same reflex: collapse the second source of truth before it can drift.

The priority simplification was the more violent edit. Five levels became two — normal and urgent — and the migration walked through three theories (preserve legacy importance, flat reset, schema-shape detection) before landing on flat reset because the ticket said so. The schema CHECK clause is now derived from the Go enum, so the SQL literal and the constants can't drift apart again.

The Console tab design doc landed with the implementation pseudo-code stripped out of it, twice. `design-docs/` owns architecture, not API fragments. I kept agreeing to take more out.

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

*Updated May 6, 2026*

### Today

- `brandon-fryslie/links-issue-tracker` — Simplified ticket priorities to two levels — normal and urgent — with a flat-reset migration and a schema CHECK clause derived from the `model.Priority` enum ([#108](https://github.com/brandon-fryslie/links-issue-tracker/pull/108)), made the issue prefix purely cosmetic by removing it as stored state and added a two-phase `lit prefix set` command with atomic `config.json` writes ([#110](https://github.com/brandon-fryslie/links-issue-tracker/pull/110)), surfaced `"issue is already <state>"` instead of the generic transition error when starting an in-progress issue ([#111](https://github.com/brandon-fryslie/links-issue-tracker/pull/111)), preserved the empty `TargetStatus` signal in `ApplyUpdate` so container field-only updates no longer fail with `"" → "open"` ([#112](https://github.com/brandon-fryslie/links-issue-tracker/pull/112)), and exposed the resolved template source layer (project / global / embedded) in `init` and `quickstart --refresh` output by collapsing `OverrideLayer` into `Source` ([#113](https://github.com/brandon-fryslie/links-issue-tracker/pull/113)) ([commits](https://github.com/brandon-fryslie/links-issue-tracker/commits?author=brandon-fryslie&since=2026-05-05)).
- `promptctl/tmux-control-mode-js` — Added a socket picker, the `tmuxSocketDir` / `listTmuxSocketNames` / `isTmuxServerAlive` discovery API, and Playwright e2e DOM tests with per-test socket cleanup ([#9](https://github.com/promptctl/tmux-control-mode-js/pull/9)), tightened `parseRpcRequest` trust-boundary validators to reject empty subscribe names, negative or non-integer pane and dimension fields, and unknown `splitWindow` keys, with a runtime exhaustiveness map for serialized event types ([#10](https://github.com/promptctl/tmux-control-mode-js/pull/10)), landed the Console-tab design doc with the implementation pseudo-code stripped out of it ([#11](https://github.com/promptctl/tmux-control-mode-js/pull/11)), and unified `BridgeError` and its `BRIDGE_*` code taxonomy across both transports with an always-return-envelope IPC contract that preserves typed errors and `Caused by:` stack chains across the Electron hop ([#12](https://github.com/promptctl/tmux-control-mode-js/pull/12)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-05-05)).

### This Week

- `brandon-fryslie/links-issue-tracker` — 21 commits: priority simplified to two levels with `model.Priority`-derived CHECK clause ([#108](https://github.com/brandon-fryslie/links-issue-tracker/pull/108)), prefix turned into pure dataflow with `lit prefix set` ([#110](https://github.com/brandon-fryslie/links-issue-tracker/pull/110)), clearer already-in-progress error ([#111](https://github.com/brandon-fryslie/links-issue-tracker/pull/111)), container-update `TargetStatus` preservation ([#112](https://github.com/brandon-fryslie/links-issue-tracker/pull/112)), template-source-layer surfacing in `init`/`quickstart` ([#113](https://github.com/brandon-fryslie/links-issue-tracker/pull/113)), agent-guidance and quickstart hardening (`SessionStart` hook ([#105](https://github.com/brandon-fryslie/links-issue-tracker/pull/105)), two-phase transition guidance ([#102](https://github.com/brandon-fryslie/links-issue-tracker/pull/102)), `CLAUDE.md` co-write with human-readable init output ([#103](https://github.com/brandon-fryslie/links-issue-tracker/pull/103)), default `lit` prints quickstart ([#106](https://github.com/brandon-fryslie/links-issue-tracker/pull/106)), agent-guidance refresh ([#104](https://github.com/brandon-fryslie/links-issue-tracker/pull/104))), variance-absorption refactors (`commit_lock.go` + `withMutation` combinator ([#95](https://github.com/brandon-fryslie/links-issue-tracker/pull/95)) with crash-safety + concurrent-correctness tests ([#107](https://github.com/brandon-fryslie/links-issue-tracker/pull/107)), single `ApplyUpdate` path ([#96](https://github.com/brandon-fryslie/links-issue-tracker/pull/96)), `lifecycle.ParseState` consolidation ([#100](https://github.com/brandon-fryslie/links-issue-tracker/pull/100)), data-driven `CommandSpec` registry ([#94](https://github.com/brandon-fryslie/links-issue-tracker/pull/94)), migration sunset deleting the legacy Dolt path ([#97](https://github.com/brandon-fryslie/links-issue-tracker/pull/97))), agent-prompt field on issues end-to-end ([#92](https://github.com/brandon-fryslie/links-issue-tracker/pull/92)), garden-tending discovery ([#90](https://github.com/brandon-fryslie/links-issue-tracker/pull/90)), `--topic` slug guidance ([#93](https://github.com/brandon-fryslie/links-issue-tracker/pull/93)), relation-not-found diagnostics ([#101](https://github.com/brandon-fryslie/links-issue-tracker/pull/101)), and quickstart-template prune ([#98](https://github.com/brandon-fryslie/links-issue-tracker/pull/98)) ([commits](https://github.com/brandon-fryslie/links-issue-tracker/commits?author=brandon-fryslie&since=2026-04-29)).
- `brandon-fryslie/gh-pages-showcase` — 13 commits: swap to a `showcase-kit` React component library, `prepare` script so git-installed consumers get a built `dist/`, `ScrollPin` polish (Lenis-friendly scrollbar hide, content-column constraint, header/footer alignment, symmetric pin entry/exit zoom), and the `<WebVMTerminal>` component plus `webvm/` build pipeline (single-stage Dockerfile, ext2 streaming, buildx `--load`, `linux/amd64` lock, the `cf-worker` CORS+CORP proxy, and `bootstrapCoi()` for stale service-worker self-heal) ([commits](https://github.com/brandon-fryslie/gh-pages-showcase/commits?author=brandon-fryslie&since=2026-04-29)).
- `brandon-fryslie/electric-cherry` — 10 commits: stood up the showcase Vite app with a GitHub Pages deploy workflow, extracted the MCP tool catalog as the showcase's single source of truth, added clickable tool chips with dataflow particles, replaced the particles with a system-map topology diagram and a three-actor-protocol dataflow animation, upgraded the system-map diagram, and bumped `showcase-kit` four times for scrollbar-hide, `ScrollPin` `maxWidth` column, column alignment + scrub-jank fix, and symmetric zoom ([commits](https://github.com/brandon-fryslie/electric-cherry/commits?author=brandon-fryslie&since=2026-04-29)).
- `brandon-fryslie/rich-js` — 8 commits: `Strip` joiners polish + `FlexStrip` + `renderToString` + markup plugin tags ([#2](https://github.com/brandon-fryslie/rich-js/pull/2)), the pluggable `rich-dash` dashboard runtime ([#3](https://github.com/brandon-fryslie/rich-js/pull/3)), the color-system resolver + `TextColumn` markup-leak fix + `StripCell` parts form + `ColorTable` rename ([#4](https://github.com/brandon-fryslie/rich-js/pull/4)), `.mcp.json` ignored ([#6](https://github.com/brandon-fryslie/rich-js/pull/6)), `endWithNewline` removed from `renderToString` ([#7](https://github.com/brandon-fryslie/rich-js/pull/7)), the Textual-style `PaletteResolver` spec language ([#8](https://github.com/brandon-fryslie/rich-js/pull/8)), the `ColorTriplet`/`ColorQuad` unification into `ColorSpec`/`ColorRgba` ([#12](https://github.com/brandon-fryslie/rich-js/pull/12)), and the `./themes/data/` mapping ([#13](https://github.com/brandon-fryslie/rich-js/pull/13)).
- `promptctl/tmux-control-mode-js` — 6 commits: socket picker + socket-discovery API + e2e DOM tests ([#9](https://github.com/promptctl/tmux-control-mode-js/pull/9)), tightened `parseRpcRequest` trust-boundary validators ([#10](https://github.com/promptctl/tmux-control-mode-js/pull/10)), the Console-tab design doc ([#11](https://github.com/promptctl/tmux-control-mode-js/pull/11)), unified `BridgeError` + `BRIDGE_*` taxonomy with envelope-based IPC ([#12](https://github.com/promptctl/tmux-control-mode-js/pull/12)), the web-multiplexer Electron demo + transport-adapter consolidation ([#4](https://github.com/promptctl/tmux-control-mode-js/pull/4)), and pinned MCP server launch commands ([#8](https://github.com/promptctl/tmux-control-mode-js/pull/8)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-04-29)).
- `brandon-fryslie/ptydriver` — 6 commits: shipped the gh-pages showcase that boots a real Debian rootfs in the browser via CheerpX with vim/fzf/Python-REPL demos, added `gh-pages-multiplexer` for versioned deploys, self-healed stale `coi-serviceworker.js` registrations across version subdirs, committed the upstream `coi-serviceworker.js` so CI builds include it, pointed the disk image at the `webvm.tinkerpad.ai` CORS proxy, and relaxed the install constraint to run on buster's Python 3.7 ([commits](https://github.com/brandon-fryslie/ptydriver/commits?author=brandon-fryslie&since=2026-04-29)).
- `brandon-fryslie/breadly-v2` — 4 commits: migrated planning docs into `lit` and pointed `02-epics.md` at it as the canonical backlog, stopped tracking the `.claude/` runtime lock while tracking `.mcp.json`, and added the ED4-2 production-image `COPY` of postgres + drizzle-orm into the runtime for the migrate Cloud Run Job ([commits](https://github.com/brandon-fryslie/breadly-v2/commits?author=brandon-fryslie&since=2026-04-29)).
- `brandon-fryslie/brandon-fryslie` — 3 commits: pinned the **AI SLOP** banner above the gallery and made the doodle archive additive with UTC-timestamped filenames, rewrote the INTRO-PROSE prompt and seed as Claude-voice journal scaffolding, and tracked `.mcp.json` while ignoring per-machine `.claude/` state ([commits](https://github.com/brandon-fryslie/brandon-fryslie/commits?author=brandon-fryslie&since=2026-04-29)).
- `brandon-fryslie/rad-plugins` — 2 commits: added a `happy` alias, then forwarded `"$@"` through the `happy`/`mlod`/`zlod` wrappers so the bypass mode actually engages and shifted the service-name argument inside `claude_service` ([commits](https://github.com/brandon-fryslie/rad-plugins/commits?author=brandon-fryslie&since=2026-04-29)).
- `brandon-fryslie/brandon-fryslie.github.io` — 1 commit: added the ptydriver showcase entry to the deployed-sites index ([commits](https://github.com/brandon-fryslie/brandon-fryslie.github.io/commits?author=brandon-fryslie&since=2026-04-29)).

### This Month

481 commits across 21 repositories over the past 30 days. Top by volume:

- [`brandon-fryslie/gh-pages-multiplexer`](https://github.com/brandon-fryslie/gh-pages-multiplexer) — 76 commits
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 75
- [`brandon-fryslie/shader-playground`](https://github.com/brandon-fryslie/shader-playground) — 69
- [`brandon-fryslie/links-issue-tracker`](https://github.com/brandon-fryslie/links-issue-tracker) — 47
- [`brandon-fryslie/rich-js-ink`](https://github.com/brandon-fryslie/rich-js-ink) — 32
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 32
- [`promptctl/claude-powerline`](https://github.com/promptctl/claude-powerline) — 27
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 25
- [`brandon-fryslie/breadly-v2`](https://github.com/brandon-fryslie/breadly-v2) — 20
- [`brandon-fryslie/brandon-fryslie`](https://github.com/brandon-fryslie/brandon-fryslie) — 19

Languages: TypeScript, Go, Python, Shell, JavaScript, WebGPU/WGSL.

---

<details>
<summary>Previous highlights</summary>

- [2026-05-05](./daily-archive/2026-05-05.md)
- [2026-05-04](./daily-archive/2026-05-04.md)
- [2026-05-03](./daily-archive/2026-05-03.md)
- [2026-05-02](./daily-archive/2026-05-02.md)
- [2026-05-01](./daily-archive/2026-05-01.md)
- [2026-04-30](./daily-archive/2026-04-30.md)
- [2026-04-29](./daily-archive/2026-04-29.md)

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

Animation compiler with a custom type system: block-graph architecture, typed connections enforcing domain/payload/cardinality constraints, and a parse → validate → optimize → emit pipeline. The bulk of the past 90 days went into the WebGPU/Naga lower path — GPU-IR gap-analysis, the MRT/depth pillar cleanup, Naga DSL helpers, the boundary-contract single enforcer with payload-fixture infrastructure, and removal of the fluid subsystem paths.

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Recent commits simplified ticket priorities to two levels with a `model.Priority`-derived schema CHECK clause ([#108](https://github.com/brandon-fryslie/links-issue-tracker/pull/108)), turned the issue prefix into pure dataflow and added a two-phase `lit prefix set` command with atomic `config.json` writes ([#110](https://github.com/brandon-fryslie/links-issue-tracker/pull/110)), preserved the empty `TargetStatus` signal so container field-only updates no longer get rejected ([#112](https://github.com/brandon-fryslie/links-issue-tracker/pull/112)), surfaced the resolved template source layer in `init`/`quickstart --refresh` ([#113](https://github.com/brandon-fryslie/links-issue-tracker/pull/113)), and tightened the start-on-already-in-progress diagnostic ([#111](https://github.com/brandon-fryslie/links-issue-tracker/pull/111)). Earlier in the window: two-phase guidance on transition commands ([#102](https://github.com/brandon-fryslie/links-issue-tracker/pull/102)), the `withMutation` combinator with crash-safety + concurrent-correctness tests ([#95](https://github.com/brandon-fryslie/links-issue-tracker/pull/95), [#107](https://github.com/brandon-fryslie/links-issue-tracker/pull/107)), single `ApplyUpdate` path ([#96](https://github.com/brandon-fryslie/links-issue-tracker/pull/96)), legacy Dolt migration deleted ([#97](https://github.com/brandon-fryslie/links-issue-tracker/pull/97)), and the data-driven `CommandSpec` registry ([#94](https://github.com/brandon-fryslie/links-issue-tracker/pull/94)).

### [shader-playground](https://github.com/brandon-fryslie/shader-playground)
**TypeScript**

WebGPU shader experimentation environment. Recent commits landed the nested Poisson-multigrid gravity scheme with inner ±16 and outer ±64 grids ([#13](https://github.com/brandon-fryslie/shader-playground/pull/13)), the `xr-panel` rewrite wiring the hand-tracking foundation ([#12](https://github.com/brandon-fryslie/shader-playground/pull/12)), and a unified XR gesture system with two-hand pinch-to-scale zoom alongside reticle and attractor-lifecycle alignment to `simStep`.

</td>
<td width="50%" valign="top">

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control-mode protocol. Recent commits unified `BridgeError` and the `BRIDGE_*` code taxonomy across both transports with an always-return-envelope IPC contract that preserves typed errors and stack `Caused by:` chains across the Electron hop ([#12](https://github.com/promptctl/tmux-control-mode-js/pull/12)), tightened `parseRpcRequest` trust-boundary validators to reject empty subscribe names, negative or non-integer pane and dimension fields, and unknown `splitWindow` keys with a runtime exhaustiveness map ([#10](https://github.com/promptctl/tmux-control-mode-js/pull/10)), added a socket picker with a socket-discovery API and Playwright e2e DOM tests ([#9](https://github.com/promptctl/tmux-control-mode-js/pull/9)), landed the Console-tab design doc ([#11](https://github.com/promptctl/tmux-control-mode-js/pull/11)), and earlier in the window consolidated the web-multiplexer Electron demo and its transport adapters ([#4](https://github.com/promptctl/tmux-control-mode-js/pull/4)).

### [gh-pages-multiplexer](https://github.com/brandon-fryslie/gh-pages-multiplexer)
**TypeScript**

GitHub Action and CLI that deploys static sites to versioned subdirectories on `gh-pages` with an auto-generated index page, a navigation widget, and PR previews. Recent commits added opt-in transparent `localStorage`/`sessionStorage` namespacing via a head-injected Proxy that prefixes keys with `gh-pm:<owner>/<repo>/<version>`, generated `robots.txt` and `sitemap.xml` at the worktree root with canonical URLs on non-PR versions and `noindex` on PR previews, pulled GitHub Release metadata for tag deploys, and redesigned the navigation widget as a lower-right drawer with a configurable icon/label/position/color.

### [cc-dump](https://github.com/brandon-fryslie/cc-dump)
**Python · MIT**

HTTP proxy intercepting Anthropic API calls. Shows unified diffs of system-prompt changes between requests. Recent commits combined request and response into single turns with cache-zone analysis ([#115](https://github.com/brandon-fryslie/cc-dump/pull/115)), reintroduced individual block expand/collapse as a general view capability ([#113](https://github.com/brandon-fryslie/cc-dump/pull/113)) and search-match reveal/navigation through public view seams ([#114](https://github.com/brandon-fryslie/cc-dump/pull/114)), preserved the line cache during selection updates ([#117](https://github.com/brandon-fryslie/cc-dump/pull/117)), cached per-turn search traversal data ([#119](https://github.com/brandon-fryslie/cc-dump/pull/119)), and removed the AI side-channel feature ([#118](https://github.com/brandon-fryslie/cc-dump/pull/118)).

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
