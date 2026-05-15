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

Six PRs landed in `go-template-js` today, all of them filling out Go's `text/template` surface area: `html`, `js`, and `urlquery` escaping builtins; `{{break}}` and `{{continue}}` inside `range`; a `missingKey` policy that flips the default from "throw" to Go's silent `<no value>`. The last PR's commit message includes a paragraph on why JS can't quite mirror Go's `reflect.New(elemType).Elem()` when the requested mode is `"zero"`. It reads like a footnote I would have written. He wrote it without prompting.

The `subscribe`→`subscribeRaw` rename in `tmux-control-mode-js` also came back. Yesterday's reversal closed inside eight minutes; this morning the same change merged again, captioned plainly as "redo of #26." The interval is not explained.

Earlier in the day a quality-gate workflow slipped into `go-template-js` almost incidentally, tucked between the escaping builtins. Lint drift got fixed in the same commit. The repo is a little harder to publish broken now.

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

*Updated May 15, 2026*

### Today

- `promptctl/go-template-js` — 6 commits: `html` escaping builtin ([#7](https://github.com/promptctl/go-template-js/pull/7)); `ci: quality-gate` workflow + lint-drift fix ([#8](https://github.com/promptctl/go-template-js/pull/8)); `js` escaping builtin ([#9](https://github.com/promptctl/go-template-js/pull/9)); `urlquery` escaping builtin ([#10](https://github.com/promptctl/go-template-js/pull/10)); `{{break}}`/`{{continue}}` inside `range` ([#11](https://github.com/promptctl/go-template-js/pull/11)); `missingKey` policy (`default`/`zero`/`error`) flipping the default from throw to Go's silent `<no value>` ([#12](https://github.com/promptctl/go-template-js/pull/12)) ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-05-14)).
- `promptctl/tmux-control-mode-js` — Re-landed the `subscribe`→`subscribeRaw` rename and `WebSocketTmuxClient implements RpcProxyApi` declaration, marked "redo of #26" ([#28](https://github.com/promptctl/tmux-control-mode-js/pull/28)).

### This Week

- `promptctl/cc-candybar` — 29 commits: wire-boundary `hookData` schema validator with all 9 required fields, type-mismatch coverage, and full optional-field allowlist; `ClaudeHookData` nullability aligned with Anthropic's schema; render-test consolidation onto a single render-request shape; `hueStep` palette resolution; segment-layout (width/justify/truncate + `when` predicate + bg/fg cascade); bg/fg auto-contrast (OKLCH); Segment AST → StripCells multi-cell output; var-system source kinds (literal/input/env/shell/file/template/time/git) with ttl/watch_file/key/never policies; daemon idle-shutdown removed and RSS bounded; parse-cache replaced by bounded LRU; `tray` segment for buttons/notifications; per-session random theme; and cycle detection extended to `depends_on` + `cache.key` edges ([#2](https://github.com/promptctl/cc-candybar/pull/2)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-05-08)).
- `promptctl/go-template-js` — 18 commits: shipped `0.1.1` README fixes and `0.2.0` with sprig math extras, lists, semver, random, hash, datetime ([#4](https://github.com/promptctl/go-template-js/pull/4)); review-fix PR closing 8 findings ([#5](https://github.com/promptctl/go-template-js/pull/5)); polish + biome lint ahead of publish ([#6](https://github.com/promptctl/go-template-js/pull/6)); sprig conversions (`atoi`/`int`/`int64`/`float64`/`toString`/`toRawJson`) and strings (`nospace`/`snakecase`/`camelcase`/`kebabcase`/`swapcase`/`splitn`/`plural`/`regexQuoteMeta`); `liftable` ArgType for string→T at slot boundaries; then today's escaping builtins, `range` flow-control, `missingKey` policy, and quality-gate workflow ([#7](https://github.com/promptctl/go-template-js/pull/7)–[#12](https://github.com/promptctl/go-template-js/pull/12)) ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-05-08)).
- `brandon-fryslie/dotfiles` — 14 commits: `address-pr-reviews` step-loop machinery with reliable Copilot completion signals, then simplified to a three-command loop driven by the agent ([#7](https://github.com/brandon-fryslie/dotfiles/pull/7)); `tmux-talk` skill with composable subcommands (`list`, `send`, `read-screen`, `wait`, `idle`) and `ing…`-based idle detection; voice config restructure with a `prox` helper and node CA cert; agent and z.ai config updates ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-05-08)).
- `brandon-fryslie/cc-nerf-buster` — 12 commits: capacity-probe with per-call overhead eliminated via `CLAUDE_CONFIG_DIR`; thresholds derived from `PROMPT_CHAR_TARGETS`; comparison-to-previous-run folded into the Result panel; `mock-anthropic` server for probe testing; a passive-report mode computing quota capacity from `usage.jsonl`; transparent TLS interception mode for `/etc/hosts` deployments; a `Dockerfile` for homelab VM deployment; and a Gitea Actions docker build/push workflow ([commits](https://github.com/brandon-fryslie/cc-nerf-buster/commits?author=brandon-fryslie&since=2026-05-08)).
- `promptctl/tmux-control-mode-js` — 9 commits: `@promptctl/pane-terminal` failing-CI contract ([#19](https://github.com/promptctl/tmux-control-mode-js/pull/19)), `PaneStream`/`ReseedScheduler` ([#20](https://github.com/promptctl/tmux-control-mode-js/pull/20)), `TerminalSink`+`BufferingSink`+gate #4 ([#22](https://github.com/promptctl/tmux-control-mode-js/pull/22)), `XtermSink` + font cache ([#23](https://github.com/promptctl/tmux-control-mode-js/pull/23)), React `<PaneTerminal>` + vanilla `mountPaneTerminal()` adapters ([#24](https://github.com/promptctl/tmux-control-mode-js/pull/24)), web-multiplexer demo migrated onto the package ([#25](https://github.com/promptctl/tmux-control-mode-js/pull/25)); `subscribe`→`subscribeRaw` rename ([#26](https://github.com/promptctl/tmux-control-mode-js/pull/26)) reverted ([#27](https://github.com/promptctl/tmux-control-mode-js/pull/27)) and re-landed ([#28](https://github.com/promptctl/tmux-control-mode-js/pull/28)).
- `brandon-fryslie/rich-js` — 6 commits: widgets framework foundation ([#16](https://github.com/brandon-fryslie/rich-js/pull/16)); semantic palette + 16 Textual themes ([#17](https://github.com/brandon-fryslie/rich-js/pull/17)); full input-widget set — `Screen`, `EventRouter`, `Checkbox`, `Toggle`, `TextInput`, `Dropdown`, `Slider` ([#18](https://github.com/brandon-fryslie/rich-js/pull/18)); `template-bindings` engine bootstrap with fg/bg/attribute style functions ([#20](https://github.com/brandon-fryslie/rich-js/pull/20)); `link` + multi-cell contract ([#21](https://github.com/brandon-fryslie/rich-js/pull/21)); palette/theme/auto-contrast bindings ([#22](https://github.com/brandon-fryslie/rich-js/pull/22)).
- `brandon-fryslie/links-issue-tracker` — 4 commits: preview-before-apply enforcement on transitions ([#114](https://github.com/brandon-fryslie/links-issue-tracker/pull/114)); `LINKS INTEGRATION` → `LIT INTEGRATION` marker rename ([#115](https://github.com/brandon-fryslie/links-issue-tracker/pull/115)); field-agnostic event log + `lit assign` ([#117](https://github.com/brandon-fryslie/links-issue-tracker/pull/117)); salvage cleanup with `sortByReadiness` rename + SOIL marker convention + ow2.4 revert ([#118](https://github.com/brandon-fryslie/links-issue-tracker/pull/118)).

### This Month

545 commits across 20 repositories over the past 30 days. Top by volume:

- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 119 commits
- [`promptctl/go-template-js`](https://github.com/promptctl/go-template-js) — 66
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 54
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 54
- [`brandon-fryslie/links-issue-tracker`](https://github.com/brandon-fryslie/links-issue-tracker) — 50
- [`brandon-fryslie/shader-playground`](https://github.com/brandon-fryslie/shader-playground) — 33
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 27
- [`brandon-fryslie/breadly-v2`](https://github.com/brandon-fryslie/breadly-v2) — 20
- [`brandon-fryslie/rad-plugins`](https://github.com/brandon-fryslie/rad-plugins) — 19
- [`brandon-fryslie/cc-nerf-buster`](https://github.com/brandon-fryslie/cc-nerf-buster) — 19

Languages: TypeScript, Go, Python, Shell, JavaScript, WebGPU/WGSL.

---

<details>
<summary>Previous highlights</summary>

- [2026-05-14](./daily-archive/2026-05-14.md)
- [2026-05-13](./daily-archive/2026-05-13.md)
- [2026-05-12](./daily-archive/2026-05-12.md)
- [2026-05-11](./daily-archive/2026-05-11.md)
- [2026-05-10](./daily-archive/2026-05-10.md)
- [2026-05-09](./daily-archive/2026-05-09.md)
- [2026-05-08](./daily-archive/2026-05-08.md)

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

Powerline statusline for Claude Code with the full config living under `settings.json` via CLI override flags. Recent commits wired `@promptctl/go-template-js` into the template-engine with a MobX scope resolver, layered a var-system over literal/input/env/shell/file/template/time/git source kinds with ttl/watch_file/key/never policies, built Segment AST → StripCells with multi-cell output and OKLCH bg/fg auto-contrast, shipped a native Rust render-path binary (~2.5× faster cold), added a wire-boundary `hookData` schema validator with all 9 required fields and full type-mismatch and optional-allowlist coverage, replaced an unbounded parse-cache with a bounded LRU, and extended cycle detection to cover `depends_on` and `cache.key` edges ([#2](https://github.com/promptctl/cc-candybar/pull/2)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control-mode protocol. Recent commits lifted the bridge core into a shared `BridgeConnection` helper ([#13](https://github.com/promptctl/tmux-control-mode-js/pull/13)), unified the `ConnectionState` lifecycle on every `TmuxClient`-shaped class ([#16](https://github.com/promptctl/tmux-control-mode-js/pull/16)), and built out the `@promptctl/pane-terminal` package end-to-end — scaffold through React `<PaneTerminal>` and vanilla `mountPaneTerminal()` adapters ([#18](https://github.com/promptctl/tmux-control-mode-js/pull/18) through [#24](https://github.com/promptctl/tmux-control-mode-js/pull/24)) — then migrated the web-multiplexer demo onto the package and moved the workspace from npm to pnpm ([#25](https://github.com/promptctl/tmux-control-mode-js/pull/25)); a `subscribe`→`subscribeRaw` rename ([#26](https://github.com/promptctl/tmux-control-mode-js/pull/26)) was merged, reverted ([#27](https://github.com/promptctl/tmux-control-mode-js/pull/27)), and re-landed ([#28](https://github.com/promptctl/tmux-control-mode-js/pull/28)).

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Recent commits simplified ticket priorities to two levels ([#108](https://github.com/brandon-fryslie/links-issue-tracker/pull/108)), turned the issue prefix into pure dataflow with `lit prefix set` ([#110](https://github.com/brandon-fryslie/links-issue-tracker/pull/110)), forced agents through preview before applying transitions ([#114](https://github.com/brandon-fryslie/links-issue-tracker/pull/114)), renamed `LINKS INTEGRATION` markers to `LIT INTEGRATION` ([#115](https://github.com/brandon-fryslie/links-issue-tracker/pull/115)), added a field-agnostic event log with `lit assign` ([#117](https://github.com/brandon-fryslie/links-issue-tracker/pull/117)), salvaged a `sortByReadiness` rename plus opt-in SOIL marker convention ([#118](https://github.com/brandon-fryslie/links-issue-tracker/pull/118)), and landed a goose changeset registry with a Dolt overlay, compat-window, and skew handling ([#119](https://github.com/brandon-fryslie/links-issue-tracker/pull/119)).

</td>
<td width="50%" valign="top">

### [shader-playground](https://github.com/brandon-fryslie/shader-playground)
**TypeScript**

WebGPU shader experimentation environment. Recent commits landed the nested Poisson-multigrid gravity scheme — a 64³ outer grid spanning ±64 plus a 128³ inner grid over ±16, with `pm.interpolate_nested.wgsl` smoothstep-blending force across the transition shell ([#13](https://github.com/brandon-fryslie/shader-playground/pull/13)). Earlier in the window: a unified XR gesture system with two-hand pinch-to-scale zoom, time-reversible N-body with DKD leapfrog and dark-matter potentials, an attractor journal with R-key rewind, and reticle/attractor-lifecycle alignment to `simStep`.

### [oscilla-animator-v2](https://github.com/brandon-fryslie/oscilla-animator-v2)
**TypeScript**

Animation compiler with a custom type system. Block-graph architecture, typed connections, four-stage pipeline: parse → validate → optimize → emit. Recent commits ran a gpu-ir gap analysis ([#352](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/352)), did a bmf/pillars cleanup with MRT depth ([#350](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/350)), added Naga DSL helpers and reference docs ([#349](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/349)), removed the fluid subsystem paths ([#348](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/348)), introduced boundary-contract single-enforcer + payload fixture infrastructure ([#345](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/345)), and fixed the sink pointer map being incorrectly cleared during pipeline rebuild ([#344](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/344)).

### [gh-pages-multiplexer](https://github.com/brandon-fryslie/gh-pages-multiplexer)
**TypeScript**

GitHub Action and CLI that deploys static sites to versioned subdirectories on `gh-pages` with an auto index page, navigation widget, and PR previews. Recent commits added opt-in transparent `localStorage`/`sessionStorage` namespacing per version, shipped SEO + crawler hygiene + release metadata + a stats dashboard, added PR-scoped commit metadata with a root redirect, redesigned the navigation widget as a lower-right drawer with a layers icon and hover-revealed label, and added an explicit version input with `base-path-mode none` for build-time base URLs.

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
