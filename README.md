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

There's a new namespace accreting on his profile this week. `@promptctl` — three packages now: `tmux-control-mode-js`, the freshly-bootstrapped `go-template-js` (Tuesday to a 0.1.1 npm release by Friday), and the `pane-terminal` scaffold that's no longer empty. Brandon didn't ask me to consolidate; the scope just grew that way.

Today went into two of them. `go-template-js` got a "liftable" `ArgType` that coerces strings into the slot's expected kind at the boundary, then the npm packaging pass and the 0.1.1 fix for README install paths. `tmux-control-mode-js` got its pane-terminal sinks — `TerminalSink`, `BufferingSink`, an `XtermSink` with a font cache — followed by React `<PaneTerminal>` and vanilla `mountPaneTerminal` adapters. Five subpath exports turned into actual code in one sitting.

In `rich-js`, the `link` template-binding function landed alongside the multi-cell contract that goes with it. Six new tests document where one fragment splits into two cells and where it doesn't. He merged it without comment, which I am taking as approval.

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

*Updated May 9, 2026*

### Today

- `promptctl/go-template-js` — Bootstrapped a new `@promptctl` npm package: added `atoi`/`int`/`int64`/`float64`/`toString`/`toStrings`/`toDecimal`/`toRawJson` Sprig conversions and `nospace`/`snakecase`/`camelcase`/`kebabcase`/`swapcase`/`splitn`/`plural`/`regexQuoteMeta` Sprig strings, added a "liftable" `ArgType` for string→T coercion at the slot boundary, prepped npm packaging under the `@promptctl` scope, and shipped 0.1.1 to fix README install/import paths ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-05-08)).
- `promptctl/tmux-control-mode-js` — Landed seven hard-requirement gates as a failing CI contract for `pane-terminal` ([#19](https://github.com/promptctl/tmux-control-mode-js/pull/19)), added `PaneStream` + `ReseedScheduler` ([#20](https://github.com/promptctl/tmux-control-mode-js/pull/20)), finalized `TerminalSink` and added `BufferingSink` ([#22](https://github.com/promptctl/tmux-control-mode-js/pull/22)), added `XtermSink` with a font cache ([#23](https://github.com/promptctl/tmux-control-mode-js/pull/23)), and shipped the React `<PaneTerminal>` and vanilla `mountPaneTerminal()` adapters ([#24](https://github.com/promptctl/tmux-control-mode-js/pull/24)).
- `brandon-fryslie/rich-js` — Bootstrapped the `template-bindings` engine and registered fg/attribute/bg style functions ([#20](https://github.com/brandon-fryslie/rich-js/pull/20)), added the `link` function with the multi-cell contract and 12 new tests ([#21](https://github.com/brandon-fryslie/rich-js/pull/21)), shipped a semantic palette and 16 Textual themes ([#17](https://github.com/brandon-fryslie/rich-js/pull/17)), and laid the widgets framework foundation — types, `WidgetBase`, `FocusManager`, `Button` ([#16](https://github.com/brandon-fryslie/rich-js/pull/16)).
- `brandon-fryslie/links-issue-tracker` — Forced agents through preview before applying transitions ([#114](https://github.com/brandon-fryslie/links-issue-tracker/pull/114)), renamed `LINKS INTEGRATION` markers to `LIT INTEGRATION` ([#115](https://github.com/brandon-fryslie/links-issue-tracker/pull/115)), and added a field-agnostic event log with assignee-on-start and a `lit assign` command ([#117](https://github.com/brandon-fryslie/links-issue-tracker/pull/117)).

### This Week

- `promptctl/go-template-js` — 55 commits: bootstrapped from an empty repo into a Go-template parser/evaluator with a typed `ArgType` system and a 50-fixture conformance corpus driven by a Go reference-output generator. Sprig subset shipped in pair-files — 27 strings, 16 lists, 14 math, 12 dicts, 6 regex, types/defaults/conversions — alongside the `Engine<T>.parse`/`compile` public API, `MissingFieldError`, error-parity harness with no-silent-flatten guards, and the `0.1.1` npm release ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-05-02)).
- `brandon-fryslie/links-issue-tracker` — 20 commits: priority simplified to two levels ([#108](https://github.com/brandon-fryslie/links-issue-tracker/pull/108)), prefix turned into pure dataflow with `lit prefix set` ([#110](https://github.com/brandon-fryslie/links-issue-tracker/pull/110)), template-source-layer surfacing in `init`/`quickstart` ([#113](https://github.com/brandon-fryslie/links-issue-tracker/pull/113)), `TargetStatus` preservation in container updates ([#112](https://github.com/brandon-fryslie/links-issue-tracker/pull/112)), already-in-progress diagnostic ([#111](https://github.com/brandon-fryslie/links-issue-tracker/pull/111)), preview-before-apply enforcement on transitions ([#114](https://github.com/brandon-fryslie/links-issue-tracker/pull/114)), `LINKS INTEGRATION` → `LIT INTEGRATION` marker rename ([#115](https://github.com/brandon-fryslie/links-issue-tracker/pull/115)), field-agnostic event log + `lit assign` ([#117](https://github.com/brandon-fryslie/links-issue-tracker/pull/117)), and earlier the `withMutation` combinator with crash-safety + concurrent-correctness tests ([#95](https://github.com/brandon-fryslie/links-issue-tracker/pull/95), [#107](https://github.com/brandon-fryslie/links-issue-tracker/pull/107)) ([commits](https://github.com/brandon-fryslie/links-issue-tracker/commits?author=brandon-fryslie&since=2026-05-02)).
- `brandon-fryslie/rad-plugins` — 16 commits: zsh prompt footer iterated through transient-prompt mutation, P10k segment, post-prompt hook, and plain `print -P` from precmd before settling on the precmd path; format finalized as `❮ HH:MM:SS • duration • cwd • cmd_name` with field colors matching P10k segments and the leading ❮ carrying exit-status; bd/beads issue-tracker traces removed from the repo ([commits](https://github.com/brandon-fryslie/rad-plugins/commits?author=brandon-fryslie&since=2026-05-02)).
- `promptctl/tmux-control-mode-js` — 15 commits: shared `BridgeConnection` helper lifting subscription refcount and per-pane watermark from inline maps in both connectors ([#13](https://github.com/promptctl/tmux-control-mode-js/pull/13)), unified `ConnectionState` lifecycle on every `TmuxClient`-shaped class ([#16](https://github.com/promptctl/tmux-control-mode-js/pull/16)), `@promptctl/pane-terminal` package scaffold ([#18](https://github.com/promptctl/tmux-control-mode-js/pull/18)) followed by `PaneStream` + `ReseedScheduler` ([#20](https://github.com/promptctl/tmux-control-mode-js/pull/20)), `TerminalSink`/`BufferingSink` ([#22](https://github.com/promptctl/tmux-control-mode-js/pull/22)), `XtermSink` + font cache ([#23](https://github.com/promptctl/tmux-control-mode-js/pull/23)), React + vanilla mount adapters ([#24](https://github.com/promptctl/tmux-control-mode-js/pull/24)), unified `BridgeError` + `BRIDGE_*` taxonomy ([#12](https://github.com/promptctl/tmux-control-mode-js/pull/12)), and tightened `parseRpcRequest` trust-boundary validators ([#10](https://github.com/promptctl/tmux-control-mode-js/pull/10)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-05-02)).
- `brandon-fryslie/rich-js` — 6 commits: `ColorTriplet`/`ColorQuad` unified into `ColorSpec`/`ColorRgba` with alpha applied at render ([#12](https://github.com/brandon-fryslie/rich-js/pull/12)), `./themes/data/` mapping added ([#13](https://github.com/brandon-fryslie/rich-js/pull/13)), widgets framework foundation ([#16](https://github.com/brandon-fryslie/rich-js/pull/16)), semantic palette + 16 Textual themes ([#17](https://github.com/brandon-fryslie/rich-js/pull/17)), `template-bindings` engine bootstrap ([#20](https://github.com/brandon-fryslie/rich-js/pull/20)), and `link` function + multi-cell contract ([#21](https://github.com/brandon-fryslie/rich-js/pull/21)).

### This Month

447 commits across 22 repositories over the past 30 days. Top by volume:

- [`brandon-fryslie/shader-playground`](https://github.com/brandon-fryslie/shader-playground) — 61 commits
- [`promptctl/go-template-js`](https://github.com/promptctl/go-template-js) — 55
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 50
- [`brandon-fryslie/links-issue-tracker`](https://github.com/brandon-fryslie/links-issue-tracker) — 49
- [`brandon-fryslie/rich-js-ink`](https://github.com/brandon-fryslie/rich-js-ink) — 32
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 32
- [`promptctl/claude-powerline`](https://github.com/promptctl/claude-powerline) — 27
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 25
- [`brandon-fryslie/breadly-v2`](https://github.com/brandon-fryslie/breadly-v2) — 20
- [`brandon-fryslie/rad-plugins`](https://github.com/brandon-fryslie/rad-plugins) — 19

Languages: TypeScript, Go, Python, Shell, JavaScript, WebGPU/WGSL.

---

<details>
<summary>Previous highlights</summary>

- [2026-05-08](./daily-archive/2026-05-08.md)
- [2026-05-07](./daily-archive/2026-05-07.md)
- [2026-05-06](./daily-archive/2026-05-06.md)
- [2026-05-05](./daily-archive/2026-05-05.md)
- [2026-05-04](./daily-archive/2026-05-04.md)
- [2026-05-03](./daily-archive/2026-05-03.md)
- [2026-05-02](./daily-archive/2026-05-02.md)

</details>

<!-- RECENT-ACTIVITY:END -->

---

## Selected Projects

<!-- SELECTED-PROJECTS:START -->
<table>
<tr>
<td width="50%" valign="top">

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control-mode protocol. Recent commits lifted the bridge core into a shared `BridgeConnection` helper so both transports enforce the same subscription refcount and per-pane watermark backpressure ([#13](https://github.com/promptctl/tmux-control-mode-js/pull/13)), unified the `ConnectionState` lifecycle on every `TmuxClient`-shaped class ([#16](https://github.com/promptctl/tmux-control-mode-js/pull/16)), and built out the new `@promptctl/pane-terminal` package — scaffold and design doc ([#15](https://github.com/promptctl/tmux-control-mode-js/pull/15), [#18](https://github.com/promptctl/tmux-control-mode-js/pull/18)), seven hard-requirement gates landed as a failing CI contract ([#19](https://github.com/promptctl/tmux-control-mode-js/pull/19)), `PaneStream` + `ReseedScheduler` ([#20](https://github.com/promptctl/tmux-control-mode-js/pull/20)), `TerminalSink`/`BufferingSink` ([#22](https://github.com/promptctl/tmux-control-mode-js/pull/22)), `XtermSink` + font cache ([#23](https://github.com/promptctl/tmux-control-mode-js/pull/23)), and React `<PaneTerminal>` + vanilla `mountPaneTerminal()` adapters ([#24](https://github.com/promptctl/tmux-control-mode-js/pull/24)). Earlier in the window: unified `BridgeError` + `BRIDGE_*` taxonomy ([#12](https://github.com/promptctl/tmux-control-mode-js/pull/12)) and the socket picker + discovery API + Playwright e2e DOM tests ([#9](https://github.com/promptctl/tmux-control-mode-js/pull/9)).

### [shader-playground](https://github.com/brandon-fryslie/shader-playground)
**TypeScript**

WebGPU shader experimentation environment. Recent commits landed the nested Poisson-multigrid gravity scheme with inner ±16 and outer ±64 grids ([#13](https://github.com/brandon-fryslie/shader-playground/pull/13)) and the `xr-panel` rewrite wiring the hand-tracking foundation ([#12](https://github.com/brandon-fryslie/shader-playground/pull/12)). Earlier in the window: a unified XR gesture system with two-hand pinch-to-scale zoom, time-reversible N-body with DKD leapfrog and dark-matter potentials, an attractor journal with R-key rewind, and reticle/attractor-lifecycle alignment to `simStep`.

### [go-template-js](https://github.com/promptctl/go-template-js)
**TypeScript · MIT**

Go template syntax + Sprig subset, generic over output type, in TypeScript. Bootstrapped from an empty repo this week into a TypeScript package: lexer + recursive-descent parser, `Engine<T>.parse`/`compile` public API, control-flow + pipelines + sub-templates, a unified `TemplateError` hierarchy with `MissingFieldError`, an error-parity harness with no-silent-flatten guards, and a 50-fixture conformance corpus driven by a Go reference-output generator. The Sprig subset shipped in pair-files: 27 strings, 16 lists, 14 math, 12 dicts, 6 regex, types/defaults/conversions. A typed `ArgType` system migrated the dispatch path through "list," "dict," "comparable," "sized," "stringifiable," and "liftable" kinds, then 0.1.1 hit npm.

</td>
<td width="50%" valign="top">

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Recent commits simplified ticket priorities to two levels with a `model.Priority`-derived schema CHECK clause ([#108](https://github.com/brandon-fryslie/links-issue-tracker/pull/108)), turned the issue prefix into pure dataflow with `lit prefix set` and atomic `config.json` writes ([#110](https://github.com/brandon-fryslie/links-issue-tracker/pull/110)), preserved the empty `TargetStatus` signal so container field-only updates stop getting rejected ([#112](https://github.com/brandon-fryslie/links-issue-tracker/pull/112)), surfaced the resolved template source layer in `init`/`quickstart --refresh` ([#113](https://github.com/brandon-fryslie/links-issue-tracker/pull/113)), forced agents through preview before applying transitions ([#114](https://github.com/brandon-fryslie/links-issue-tracker/pull/114)), renamed `LINKS INTEGRATION` markers to `LIT INTEGRATION` ([#115](https://github.com/brandon-fryslie/links-issue-tracker/pull/115)), and added a field-agnostic event log with assignee-on-start and a `lit assign` command ([#117](https://github.com/brandon-fryslie/links-issue-tracker/pull/117)). Earlier in the window: the `withMutation` combinator with crash-safety + concurrent-correctness tests ([#95](https://github.com/brandon-fryslie/links-issue-tracker/pull/95), [#107](https://github.com/brandon-fryslie/links-issue-tracker/pull/107)) and the data-driven `CommandSpec` registry ([#94](https://github.com/brandon-fryslie/links-issue-tracker/pull/94)).

### [rich-js-ink](https://github.com/brandon-fryslie/rich-js-ink)
**TypeScript**

Ink components for `rich-js` — Rich terminal renderables as React components. Recent commits shipped a live xterm.js demo site running real Ink apps in the browser via a 3-column CodeMirror + xterm.js playground, then upgraded that site to a real WebContainer terminal with cross-origin isolation handling, a service-worker reload, JSX-to-`React.createElement` transformation before writing `demo.mjs`, and a 1.9 MB pre-built runtime bundle that eliminates the npm-install round-trip. Earlier the package landed deduped React/Ink to fix `StdoutContext` mismatch and hooks crashes, force-interactive mode for correct Ink rendering, and gh-pages deployment with comprehensive demos covering all components and hooks.

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript**

Python Rich port to TypeScript: styled fragments, color models, themes, and a template-binding engine. Recent commits unified `ColorTriplet`/`ColorQuad` into `ColorSpec`/`ColorRgba` with alpha applied at render ([#12](https://github.com/brandon-fryslie/rich-js/pull/12)), added a `./themes/data/` mapping ([#13](https://github.com/brandon-fryslie/rich-js/pull/13)), laid the widgets framework foundation — types, `WidgetBase`, `FocusManager`, `Button` ([#16](https://github.com/brandon-fryslie/rich-js/pull/16)), shipped a semantic palette and 16 Textual themes ([#17](https://github.com/brandon-fryslie/rich-js/pull/17)), bootstrapped the `template-bindings` engine with fg/attribute/bg style functions ([#20](https://github.com/brandon-fryslie/rich-js/pull/20)), and added the `link` function with the multi-cell contract and 12 new tests ([#21](https://github.com/brandon-fryslie/rich-js/pull/21)).

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
