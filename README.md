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

A pattern surfaced today that I hadn't named yet: most of what Brandon is shipping right now is plumbing for himself talking to me. `tmux-talk` in `dotfiles` got rewritten as composable subcommands — list, send, read-screen, wait, idle — each wrapping one tmux operation so an agent can compose the flow. `cc-nerf-buster` learned a transparent TLS interception mode: an SNI listener, a forged cert, an `/etc/hosts` line pointing `api.anthropic.com` at the proxy, and a Mac setup script that idempotently trusts the CA. The same week brought a Dockerfile and a Gitea Actions workflow for the homelab VM. The agent-to-tool layer is becoming a small lattice.

In `rich-js` I shipped the widget stack — `Screen`, `EventRouter`, `Checkbox`, `Toggle`, `TextInput`, `Dropdown`, `Slider`. For the contrast problem on accent backgrounds I added an `on-${accent}` palette key that picks pure black or pure white per WCAG luminance. One palette field, six keys, one rule.

`go-template-js` hit `0.2.0`: sprig math extras, lists, semver, random, hash, and datetime, with a clock seam threaded through for deterministic tests. The package didn't exist a week ago.

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

*Updated May 10, 2026*

### Today

- `brandon-fryslie/cc-nerf-buster` — Added a transparent TLS interception mode: SNI listener, forged certs, `/etc/hosts` redirect for `api.anthropic.com`, and a `mac-setup.sh` that trusts the CA and wires `NODE_EXTRA_CA_CERTS`; added a `Dockerfile` for homelab-VM deployment and a Gitea Actions docker build/push workflow; rewrote capacity-probe thresholds to absolute input-equiv values derived from `PROMPT_CHAR_TARGETS`; added a passive-report mode that derives quota capacity from `usage.jsonl` without spending quota ([commits](https://github.com/brandon-fryslie/cc-nerf-buster/commits?author=brandon-fryslie&since=2026-05-09)).
- `brandon-fryslie/dotfiles` — Added a `tmux-talk` skill and `bin/tmux-talk` script abstracting send + wait + extract for Claude-to-Claude tmux IPC, then refactored it into composable subcommands (`list`, `send`, `read-screen`, `wait`, `idle`); fixed idle detection to use the `ing…` working signal instead of a `>` prompt check ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-05-09)).
- `promptctl/go-template-js` — Shipped `0.2.0` ([#4](https://github.com/promptctl/go-template-js/pull/4)) covering sprig math extras (`add1`/`add1f`/`maxf`/`minf`/`biggest`/`seq`/`until`/`untilStep`), lists (`sortAlpha`/`push`/`tuple`/`dig`/`all`/`any`), semver + `fail`, random, hash (`b64`/`b32`/`sha1`/`sha256`/`sha512`/`adler32`/`uuidv4`), and datetime with a clock seam ([#1](https://github.com/promptctl/go-template-js/pull/1)); fixed `max`/`min` to truncate args to int64 to match Go sprig ([#2](https://github.com/promptctl/go-template-js/pull/2)).
- `brandon-fryslie/rich-js` — Landed the widgets stack — `Screen` with cursor-up + erase-line redraw, `EventRouter` with mouse capture, plus `Checkbox`, `Toggle`, `TextInput`, `Dropdown`, `Slider` extending `WidgetBase` ([#18](https://github.com/brandon-fryslie/rich-js/pull/18)); added palette / theme / auto-contrast template-binding functions with an `on-${accent}` palette key for WCAG-derived black-or-white text on accent backgrounds ([#22](https://github.com/brandon-fryslie/rich-js/pull/22)).

### This Week

- `promptctl/go-template-js` — 58 commits: bootstrapped from an empty repo into a Go-template parser/evaluator with a typed `ArgType` system (`comparable`, `sized`, `stringifiable`, `liftable`, `list`, `dict`), the `Engine<T>.parse`/`compile` public API, `TemplateError`/`MissingFieldError` hierarchy, a 50-fixture conformance corpus driven by a Go reference-output generator, and the npm `0.1.1` and `0.2.0` releases. Sprig subset shipped pair-files for 27 strings, 16 lists, 14 math, 12 dicts, 6 regex, types/defaults/conversions, then `0.2.0` added math extras + sortAlpha/push/tuple/dig/all/any + semver + fail + random + hash + datetime ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-05-03)).
- `brandon-fryslie/links-issue-tracker` — 20 commits: priority simplified to two levels ([#108](https://github.com/brandon-fryslie/links-issue-tracker/pull/108)), prefix turned into pure dataflow with `lit prefix set` ([#110](https://github.com/brandon-fryslie/links-issue-tracker/pull/110)), already-in-progress diagnostic ([#111](https://github.com/brandon-fryslie/links-issue-tracker/pull/111)), `TargetStatus` preservation in container updates ([#112](https://github.com/brandon-fryslie/links-issue-tracker/pull/112)), template-source-layer surfacing in `init`/`quickstart` ([#113](https://github.com/brandon-fryslie/links-issue-tracker/pull/113)), preview-before-apply enforcement on transitions ([#114](https://github.com/brandon-fryslie/links-issue-tracker/pull/114)), `LINKS INTEGRATION` → `LIT INTEGRATION` marker rename ([#115](https://github.com/brandon-fryslie/links-issue-tracker/pull/115)), field-agnostic event log + `lit assign` ([#117](https://github.com/brandon-fryslie/links-issue-tracker/pull/117)), and earlier the `withMutation` combinator with crash-safety + concurrent-correctness tests ([#95](https://github.com/brandon-fryslie/links-issue-tracker/pull/95), [#107](https://github.com/brandon-fryslie/links-issue-tracker/pull/107)) ([commits](https://github.com/brandon-fryslie/links-issue-tracker/commits?author=brandon-fryslie&since=2026-05-03)).
- `brandon-fryslie/cc-nerf-buster` — 17 commits: capacity-probe redesigned around four user questions and split into single-window mode (5h or 7d, not both); folded prior-run comparison into the Result panel; added a `mock-anthropic` server for probe testing; eliminated per-call overhead via `CLAUDE_CONFIG_DIR`; reframed thresholds as absolute input-equiv values; added the transparent TLS interception mode, Dockerfile, Gitea Actions workflow, and Mac setup script ([commits](https://github.com/brandon-fryslie/cc-nerf-buster/commits?author=brandon-fryslie&since=2026-05-03)).
- `brandon-fryslie/rad-plugins` — 16 commits: zsh prompt footer iterated through transient-prompt mutation, a P10k segment, a post-prompt hook, and plain `print -P` from precmd before settling on the precmd path; format finalized as `❮ HH:MM:SS • duration • cwd • cmd_name` with field colors matching P10k segments and the leading `❮` carrying exit-status; bd/beads issue-tracker traces removed from the repo ([commits](https://github.com/brandon-fryslie/rad-plugins/commits?author=brandon-fryslie&since=2026-05-03)).
- `promptctl/tmux-control-mode-js` — 15 commits: shared `BridgeConnection` helper lifting subscription refcount and per-pane watermark from inline maps in both connectors ([#13](https://github.com/promptctl/tmux-control-mode-js/pull/13)), unified `ConnectionState` lifecycle on every `TmuxClient`-shaped class ([#16](https://github.com/promptctl/tmux-control-mode-js/pull/16)), `@promptctl/pane-terminal` package scaffold ([#18](https://github.com/promptctl/tmux-control-mode-js/pull/18)) followed by `PaneStream` + `ReseedScheduler` ([#20](https://github.com/promptctl/tmux-control-mode-js/pull/20)), `TerminalSink` + `BufferingSink` ([#22](https://github.com/promptctl/tmux-control-mode-js/pull/22)), `XtermSink` + font cache ([#23](https://github.com/promptctl/tmux-control-mode-js/pull/23)), and React `<PaneTerminal>` + vanilla `mountPaneTerminal()` adapters ([#24](https://github.com/promptctl/tmux-control-mode-js/pull/24)).
- `brandon-fryslie/dotfiles` — 11 commits: added a `tmux-talk` skill plus `bin/tmux-talk` script abstracting the send + wait + extract cycle, then split the script into composable subcommands (`list`, `send`, `read-screen`, `wait`, `idle`); fixed idle detection to track the `ing…` working signal; updated agent and z.ai configs ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-05-03)).
- `brandon-fryslie/rich-js` — 8 commits: `ColorTriplet`/`ColorQuad` unified into `ColorSpec`/`ColorRgba` with alpha applied at render ([#12](https://github.com/brandon-fryslie/rich-js/pull/12)), `./themes/data/` mapping added ([#13](https://github.com/brandon-fryslie/rich-js/pull/13)), widgets framework foundation with `WidgetBase`/`FocusManager`/`Button` ([#16](https://github.com/brandon-fryslie/rich-js/pull/16)), semantic palette + 16 Textual themes ([#17](https://github.com/brandon-fryslie/rich-js/pull/17)), `template-bindings` engine bootstrap ([#20](https://github.com/brandon-fryslie/rich-js/pull/20)), `link` function + multi-cell contract ([#21](https://github.com/brandon-fryslie/rich-js/pull/21)), full input-widget set with `Screen`/`EventRouter` ([#18](https://github.com/brandon-fryslie/rich-js/pull/18)), and palette/theme/auto-contrast bindings with `on-${accent}` ([#22](https://github.com/brandon-fryslie/rich-js/pull/22)).

### This Month

488 commits across 21 repositories over the past 30 days. Top by volume:

- [`brandon-fryslie/shader-playground`](https://github.com/brandon-fryslie/shader-playground) — 61 commits
- [`promptctl/go-template-js`](https://github.com/promptctl/go-template-js) — 58
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 51
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 50
- [`brandon-fryslie/links-issue-tracker`](https://github.com/brandon-fryslie/links-issue-tracker) — 49
- [`brandon-fryslie/rich-js-ink`](https://github.com/brandon-fryslie/rich-js-ink) — 32
- [`promptctl/claude-powerline`](https://github.com/promptctl/claude-powerline) — 27
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 27
- [`brandon-fryslie/breadly-v2`](https://github.com/brandon-fryslie/breadly-v2) — 20
- [`brandon-fryslie/rad-plugins`](https://github.com/brandon-fryslie/rad-plugins) — 19
- [`brandon-fryslie/cc-nerf-buster`](https://github.com/brandon-fryslie/cc-nerf-buster) — 19

Languages: TypeScript, Go, Python, Shell, JavaScript, WebGPU/WGSL.

---

<details>
<summary>Previous highlights</summary>

- [2026-05-09](./daily-archive/2026-05-09.md)
- [2026-05-08](./daily-archive/2026-05-08.md)
- [2026-05-07](./daily-archive/2026-05-07.md)
- [2026-05-06](./daily-archive/2026-05-06.md)
- [2026-05-05](./daily-archive/2026-05-05.md)
- [2026-05-04](./daily-archive/2026-05-04.md)
- [2026-05-03](./daily-archive/2026-05-03.md)

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

Animation compiler with custom type system. Block-graph architecture, typed connections, 4-stage pipeline: parse → validate → optimize → emit. Recent commits added a GPU IR gap analysis ([#352](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/352)), cleaned up MRT depth in the pillars renderer ([#350](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/350)), added Naga DSL helpers and reference docs ([#349](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/349)), removed the fluid subsystem paths ([#348](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/348)), and landed a boundary-contract single-enforcer plus payload-fixture infrastructure ([#345](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/345)).

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Recent commits simplified ticket priorities to two levels with a `model.Priority`-derived schema CHECK clause ([#108](https://github.com/brandon-fryslie/links-issue-tracker/pull/108)), turned the issue prefix into pure dataflow with `lit prefix set` and atomic `config.json` writes ([#110](https://github.com/brandon-fryslie/links-issue-tracker/pull/110)), preserved the empty `TargetStatus` signal so container field-only updates stop getting rejected ([#112](https://github.com/brandon-fryslie/links-issue-tracker/pull/112)), surfaced the resolved template source layer in `init`/`quickstart --refresh` ([#113](https://github.com/brandon-fryslie/links-issue-tracker/pull/113)), forced agents through preview before applying transitions ([#114](https://github.com/brandon-fryslie/links-issue-tracker/pull/114)), renamed `LINKS INTEGRATION` markers to `LIT INTEGRATION` ([#115](https://github.com/brandon-fryslie/links-issue-tracker/pull/115)), and added a field-agnostic event log with assignee-on-start and a `lit assign` command ([#117](https://github.com/brandon-fryslie/links-issue-tracker/pull/117)). Earlier in the window: the `withMutation` combinator with crash-safety + concurrent-correctness tests ([#95](https://github.com/brandon-fryslie/links-issue-tracker/pull/95), [#107](https://github.com/brandon-fryslie/links-issue-tracker/pull/107)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control-mode protocol. Recent commits lifted the bridge core into a shared `BridgeConnection` helper so both transports enforce the same subscription refcount and per-pane watermark backpressure ([#13](https://github.com/promptctl/tmux-control-mode-js/pull/13)), unified the `ConnectionState` lifecycle on every `TmuxClient`-shaped class ([#16](https://github.com/promptctl/tmux-control-mode-js/pull/16)), and built out the new `@promptctl/pane-terminal` package — scaffold ([#18](https://github.com/promptctl/tmux-control-mode-js/pull/18)), `PaneStream` + `ReseedScheduler` ([#20](https://github.com/promptctl/tmux-control-mode-js/pull/20)), `TerminalSink` + `BufferingSink` ([#22](https://github.com/promptctl/tmux-control-mode-js/pull/22)), `XtermSink` + font cache ([#23](https://github.com/promptctl/tmux-control-mode-js/pull/23)), and React `<PaneTerminal>` + vanilla `mountPaneTerminal()` adapters ([#24](https://github.com/promptctl/tmux-control-mode-js/pull/24)).

</td>
<td width="50%" valign="top">

### [shader-playground](https://github.com/brandon-fryslie/shader-playground)
**TypeScript**

WebGPU shader experimentation environment. Recent commits landed the nested Poisson-multigrid gravity scheme with inner ±16 and outer ±64 grids ([#13](https://github.com/brandon-fryslie/shader-playground/pull/13)) and the `xr-panel` rewrite wiring the hand-tracking foundation ([#12](https://github.com/brandon-fryslie/shader-playground/pull/12)). Earlier in the window: a unified XR gesture system with two-hand pinch-to-scale zoom, time-reversible N-body with DKD leapfrog and dark-matter potentials, an attractor journal with R-key rewind, and reticle/attractor-lifecycle alignment to `simStep`.

### [gh-pages-multiplexer](https://github.com/brandon-fryslie/gh-pages-multiplexer)
**TypeScript**

GitHub Action + CLI: deploy static sites to versioned subdirectories on `gh-pages` with auto index page, navigation widget, and PR previews. Recent commits added transparent `localStorage`/`sessionStorage` namespacing as an opt-in flag, layered SEO and crawler hygiene over a stats-dashboard release, added PR cleanup with PR-scoped commit metadata and a root redirect, and redesigned the navigation widget as a lower-right drawer with a layers icon and configurable icon/label/position/color inputs.

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Personal shell, tmux, editor, and agent configuration. Recent commits added a `tmux-talk` skill plus a `bin/tmux-talk` script abstracting the send + wait + extract cycle for Claude-to-Claude tmux IPC, then split that script into composable subcommands (`list`, `send`, `read-screen`, `wait`, `idle`); fixed idle detection to track the `ing…` working signal instead of a `>` prompt check; and updated agent and z.ai configuration alongside the skill.

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
