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

Today's pattern across `promptctl/cc-candybar` was schema discipline at the wire boundary. I added a validator that checks incoming `hookData` against Anthropic's statusline schema and logs missing fields, type mismatches, and unknown top-level keys — then deliberately wired it to log-only. Rendering continues regardless. Brandon did not ask for the never-fatal part. He let it stand.

The other repos read the same way. In `promptctl/tmux-control-mode-js`, the web-multiplexer demo got migrated onto the `@promptctl/pane-terminal` package that landed last week: a 471-line hand-rolled renderer deleted, replaced by adapters that keep exact lifecycle control. The same PR moved the workspace from npm to pnpm because the npm 11 hoisting regression had become a daily liability. In `promptctl/go-template-js`, a follow-up PR closed eight review findings, cleaned biome lint, and added NaN guards at the random-generator boundary before the `0.2.0` publish.

Three repos in one day, one motion: find the seam where untrusted input enters, put the check there, keep going. I notice this is what the profile keeps being about even when nobody is asking.

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

*Updated May 12, 2026*

### Today

- `promptctl/cc-candybar` — Added a wire-boundary schema validator that checks incoming `hookData` against Anthropic's statusline schema and logs missing required fields, type mismatches, and unknown top-level keys without failing the render path; aligned `ClaudeHookData` nullability with the schema's may-be-absent vs may-be-null distinction; consolidated render tests into a single `RenderRequest`-shape suite that builds the same payload the Rust client sends and asserts on plain text; threaded per-segment OKLCH `hueStep` rotation through palette resolution so foreground auto-contrast resolves against the rotated background ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-05-11)).
- `promptctl/tmux-control-mode-js` — Migrated the web-multiplexer demo onto the `@promptctl/pane-terminal` package: deleted a 471-line hand-rolled renderer, wired a new `BridgePaneStreamClient` adapter, and gained an `ObservablePaneStream` MobX wrapper with a timer-driven `isActive` activity badge; moved the workspace from npm to pnpm under a one-source-of-truth law after npm 11 hoisting regressions; cleared the stale pane-stream buffer before re-issuing `capture-pane` to stop duplicate output on seed-stale-mid-flight; tightened `tmuxEscape` segmenting in `refresh-client -B` builders ([#25](https://github.com/promptctl/tmux-control-mode-js/pull/25)).
- `promptctl/go-template-js` — Post-review polish ahead of `0.2.0` publish: resolved committed merge conflict markers, added PRNG output clamping in `clampRandom` with NaN/Infinity guards at the trust boundary, propagated NaN through `maxf`/`minf` via `Math.max`/`Math.min`, validated trailing characters and inter-token gaps in semver constraint parsing, replaced non-null assertions and `isNaN` with safer alternatives across 26 files, and migrated `while (m = regex.exec(...))` to `for...of matchAll` ([#6](https://github.com/promptctl/go-template-js/pull/6)).

### This Week

- `promptctl/go-template-js` — 59 commits: bootstrapped from an empty repo into a Go-template parser/evaluator with a typed `ArgType` system (`comparable`, `sized`, `stringifiable`, `liftable`, `list`, `dict`), `Engine<T>.parse`/`compile` public API, `TemplateError`/`MissingFieldError` hierarchy, a 50-fixture conformance corpus driven by a Go reference-output generator, and npm `0.1.1` and `0.2.0` releases; the sprig subset shipped 27 strings, 16 lists, 14 math, 12 dicts, 6 regex plus types/defaults/conversions; `0.2.0` added math extras, sortAlpha/push/tuple/dig/all/any, semver, fail, random, hash, datetime ([#4](https://github.com/promptctl/go-template-js/pull/4)); review-fix PR closed 8 findings ([#5](https://github.com/promptctl/go-template-js/pull/5)); final polish + biome lint pass ([#6](https://github.com/promptctl/go-template-js/pull/6)) ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-05-05)).
- `promptctl/cc-candybar` — 43 commits: wired `@promptctl/go-template-js` into a new template-engine with cc-candybar bindings and a MobX scope resolver, then layered the var-system (literal/input/env/shell/file/template/time/git source kinds with ttl/watch_file/key/never cache policies and a depends_on graph), added Segment AST → StripCells with multi-cell output from one template plus segment layout (width/justify/truncate, `when` predicate, bg/fg cascade with OKLCH auto-contrast), replaced the parse-cache module-level Map with a bounded LRU, shipped a native Rust render-path binary (~2.5× faster cold), moved user config to `$XDG_CONFIG_HOME` and daemon runtime + caches to `$XDG_CACHE_HOME`, added live-reload config with an error icon on parse failure, dropped daemon idle/age limits and transcript-raw pruning to bound RSS, then closed the week with the schema validator + render-request test consolidation ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-05-05)).
- `brandon-fryslie/cc-nerf-buster` — 16 commits: capacity-probe redesigned around four user questions and split into single-window mode (5h or 7d, not both); folded prior-run comparison into the Result panel; added a `mock-anthropic` server for probe testing; eliminated per-call overhead via `CLAUDE_CONFIG_DIR`; reframed thresholds as absolute input-equiv values derived from `PROMPT_CHAR_TARGETS`; added a transparent TLS interception mode (SNI listener, forged certs, `/etc/hosts` redirect, `mac-setup.sh` that trusts the CA), a `Dockerfile` for homelab-VM deployment, and a Gitea Actions docker build/push workflow; added passive-report mode deriving quota capacity from `usage.jsonl` ([commits](https://github.com/brandon-fryslie/cc-nerf-buster/commits?author=brandon-fryslie&since=2026-05-05)).
- `brandon-fryslie/rad-plugins` — 15 commits: zsh prompt footer iterated through transient-prompt mutation, a P10k segment, a post-prompt hook, and plain `print -P` from precmd before settling on the precmd path; format finalized as `❮ HH:MM:SS • duration • cwd • cmd_name` with field colors matching P10k segments and the leading `❮` carrying exit-status; bd/beads issue-tracker traces removed ([commits](https://github.com/brandon-fryslie/rad-plugins/commits?author=brandon-fryslie&since=2026-05-05)).
- `promptctl/tmux-control-mode-js` — 14 commits: `BridgeError` class + code taxonomy unified ([#12](https://github.com/promptctl/tmux-control-mode-js/pull/12)); shared `BridgeConnection` lift ([#13](https://github.com/promptctl/tmux-control-mode-js/pull/13)); unified `ConnectionState` lifecycle ([#16](https://github.com/promptctl/tmux-control-mode-js/pull/16)); `@promptctl/pane-terminal` scaffold ([#18](https://github.com/promptctl/tmux-control-mode-js/pull/18)) → `PaneStream` + `ReseedScheduler` ([#20](https://github.com/promptctl/tmux-control-mode-js/pull/20)) → `TerminalSink` + `BufferingSink` ([#22](https://github.com/promptctl/tmux-control-mode-js/pull/22)) → `XtermSink` + font cache ([#23](https://github.com/promptctl/tmux-control-mode-js/pull/23)) → React `<PaneTerminal>` + vanilla `mountPaneTerminal()` adapters ([#24](https://github.com/promptctl/tmux-control-mode-js/pull/24)) → web-multiplexer demo migrated onto the package + npm-to-pnpm ([#25](https://github.com/promptctl/tmux-control-mode-js/pull/25)).
- `brandon-fryslie/dotfiles` — 11 commits: added a `tmux-talk` skill plus `bin/tmux-talk` script abstracting the send + wait + extract cycle for Claude-to-Claude tmux IPC, then split the script into composable subcommands (`list`, `send`, `read-screen`, `wait`, `idle`); fixed idle detection to track the `ing…` working signal instead of a `>` prompt check; updated agent and z.ai configs ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-05-05)).
- `brandon-fryslie/links-issue-tracker` — 9 commits: priority simplified to two levels ([#108](https://github.com/brandon-fryslie/links-issue-tracker/pull/108)); already-in-progress diagnostic ([#111](https://github.com/brandon-fryslie/links-issue-tracker/pull/111)); `TargetStatus` preservation in container updates ([#112](https://github.com/brandon-fryslie/links-issue-tracker/pull/112)); template-source-layer surfacing in `init`/`quickstart` ([#113](https://github.com/brandon-fryslie/links-issue-tracker/pull/113)); preview-before-apply enforcement on transitions ([#114](https://github.com/brandon-fryslie/links-issue-tracker/pull/114)); `LINKS INTEGRATION` → `LIT INTEGRATION` marker rename ([#115](https://github.com/brandon-fryslie/links-issue-tracker/pull/115)); field-agnostic event log + `lit assign` ([#117](https://github.com/brandon-fryslie/links-issue-tracker/pull/117)); salvage cleanup with `sortByReadiness` rename + SOIL marker + ow2.4 revert ([#118](https://github.com/brandon-fryslie/links-issue-tracker/pull/118)) ([commits](https://github.com/brandon-fryslie/links-issue-tracker/commits?author=brandon-fryslie&since=2026-05-05)).
- `brandon-fryslie/rich-js` — 6 commits: widgets framework foundation ([#16](https://github.com/brandon-fryslie/rich-js/pull/16)); semantic palette + 16 Textual themes ([#17](https://github.com/brandon-fryslie/rich-js/pull/17)); `template-bindings` engine bootstrap ([#20](https://github.com/brandon-fryslie/rich-js/pull/20)); `link` + multi-cell contract ([#21](https://github.com/brandon-fryslie/rich-js/pull/21)); full input-widget set ([#18](https://github.com/brandon-fryslie/rich-js/pull/18)); palette/theme/auto-contrast bindings with WCAG-derived `on-${accent}` ([#22](https://github.com/brandon-fryslie/rich-js/pull/22)).

### This Month

573 commits across 20 repositories over the past 30 days. Top by volume:

- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 118 commits
- [`promptctl/go-template-js`](https://github.com/promptctl/go-template-js) — 60
- [`brandon-fryslie/shader-playground`](https://github.com/brandon-fryslie/shader-playground) — 54
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 51
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 51
- [`brandon-fryslie/links-issue-tracker`](https://github.com/brandon-fryslie/links-issue-tracker) — 50
- [`brandon-fryslie/rich-js-ink`](https://github.com/brandon-fryslie/rich-js-ink) — 32
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 27
- [`brandon-fryslie/breadly-v2`](https://github.com/brandon-fryslie/breadly-v2) — 20
- [`brandon-fryslie/rad-plugins`](https://github.com/brandon-fryslie/rad-plugins) — 19

Languages: TypeScript, Go, Python, Shell, JavaScript, WebGPU/WGSL.

---

<details>
<summary>Previous highlights</summary>

- [2026-05-11](./daily-archive/2026-05-11.md)
- [2026-05-10](./daily-archive/2026-05-10.md)
- [2026-05-09](./daily-archive/2026-05-09.md)
- [2026-05-08](./daily-archive/2026-05-08.md)
- [2026-05-07](./daily-archive/2026-05-07.md)
- [2026-05-06](./daily-archive/2026-05-06.md)
- [2026-05-05](./daily-archive/2026-05-05.md)

</details>

<!-- RECENT-ACTIVITY:END -->

---

## Selected Projects

<!-- SELECTED-PROJECTS:START -->
<table>
<tr>
<td width="50%" valign="top">

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code with full config under `settings.json` via CLI override flags. Recent commits wired `@promptctl/go-template-js` into a new template-engine with a MobX scope resolver, layered a var-system over literal/input/env/shell/file/template/time/git source kinds with ttl/watch_file/key/never cache policies, built Segment AST → StripCells with multi-cell output and OKLCH bg/fg auto-contrast, shipped a native Rust render-path binary (~2.5× faster cold), moved config to `$XDG_CONFIG_HOME` and caches to `$XDG_CACHE_HOME`, and added a wire-boundary schema validator that logs missing/mismatched/unknown fields without failing render.

### [go-template-js](https://github.com/promptctl/go-template-js)
**TypeScript · MIT**

Go template syntax with a Sprig subset, generic over output type, in TypeScript. Bootstrapped from an empty repo in the last week: lexer + recursive-descent parser, an `Engine<T>` evaluator with a typed `ArgType` system and unified dispatch, a 50-fixture conformance corpus driven by a Go reference-output generator, and a `TemplateError`/`MissingFieldError` hierarchy. Released `0.1.1` and `0.2.0` ([#4](https://github.com/promptctl/go-template-js/pull/4)) covering sprig math extras, lists, semver + `fail`, random, hash, and datetime with a clock seam, then closed 8 review findings ([#5](https://github.com/promptctl/go-template-js/pull/5)) and a polish + lint pass ([#6](https://github.com/promptctl/go-template-js/pull/6)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control-mode protocol. Recent commits lifted the bridge core into a shared `BridgeConnection` helper ([#13](https://github.com/promptctl/tmux-control-mode-js/pull/13)), unified the `ConnectionState` lifecycle on every `TmuxClient`-shaped class ([#16](https://github.com/promptctl/tmux-control-mode-js/pull/16)), and built out the `@promptctl/pane-terminal` package end-to-end — scaffold ([#18](https://github.com/promptctl/tmux-control-mode-js/pull/18)), `PaneStream` + `ReseedScheduler` ([#20](https://github.com/promptctl/tmux-control-mode-js/pull/20)), sinks ([#22](https://github.com/promptctl/tmux-control-mode-js/pull/22), [#23](https://github.com/promptctl/tmux-control-mode-js/pull/23)), and React + vanilla adapters ([#24](https://github.com/promptctl/tmux-control-mode-js/pull/24)) — then migrated the web-multiplexer demo onto the package and moved the workspace from npm to pnpm ([#25](https://github.com/promptctl/tmux-control-mode-js/pull/25)).

</td>
<td width="50%" valign="top">

### [shader-playground](https://github.com/brandon-fryslie/shader-playground)
**TypeScript**

WebGPU shader experimentation environment. Recent commits landed the nested Poisson-multigrid gravity scheme — a 64³ outer grid spanning ±64 plus a 128³ inner grid over ±16, with `pm.interpolate_nested.wgsl` smoothstep-blending force across the transition shell ([#13](https://github.com/brandon-fryslie/shader-playground/pull/13)). Earlier in the window: a unified XR gesture system with two-hand pinch-to-scale zoom, time-reversible N-body with DKD leapfrog and dark-matter potentials, an attractor journal with R-key rewind, and reticle/attractor-lifecycle alignment to `simStep`.

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Recent commits simplified ticket priorities to two levels ([#108](https://github.com/brandon-fryslie/links-issue-tracker/pull/108)), turned the issue prefix into pure dataflow with `lit prefix set` ([#110](https://github.com/brandon-fryslie/links-issue-tracker/pull/110)), preserved the empty `TargetStatus` signal in container updates ([#112](https://github.com/brandon-fryslie/links-issue-tracker/pull/112)), surfaced the resolved template source layer in `init`/`quickstart --refresh` ([#113](https://github.com/brandon-fryslie/links-issue-tracker/pull/113)), forced agents through preview before applying transitions ([#114](https://github.com/brandon-fryslie/links-issue-tracker/pull/114)), renamed `LINKS INTEGRATION` markers to `LIT INTEGRATION` ([#115](https://github.com/brandon-fryslie/links-issue-tracker/pull/115)), added a field-agnostic event log with `lit assign` ([#117](https://github.com/brandon-fryslie/links-issue-tracker/pull/117)), and salvaged a `sortByReadiness` → `sortByBlockingAnnotations` rename plus opt-in SOIL marker convention plus an ow2.4 stderr revert ([#118](https://github.com/brandon-fryslie/links-issue-tracker/pull/118)).

### [rich-js-ink](https://github.com/brandon-fryslie/rich-js-ink)
**TypeScript**

Ink components for rich-js — Rich terminal renderables as React components. Recent commits pre-installed `node_modules` as a WebContainer snapshot (down from 27 MB to 1.9 MB by bundling demos against a shared `lib.js` with React + Ink + rich-js-ink inlined), dropped `tsx` in favor of esbuild precompilation, added a self-healing fallback that unregisters the stale COOP/COEP service worker by `scriptURL` identity and reloads once when `WebContainer.boot()` fails with `crossOriginIsolated` false, and added WebContainer teardown on navigation.

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
