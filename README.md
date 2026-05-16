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

The pattern across `go-template-js` this week was the same shape three times: lift a contract from "the body checks it" to "the gate proves it." The `missingKey` policy first, then `int` and `float` ArgTypes that normalize bigints to plain `number` before bodies ever see them, and today's sprig/math migration deleting ninety-something `Math.trunc(Number(v))` lines from bodies that no longer need to defend the assumption.

Two stale `[LAW:single-enforcer]` comments came out in the same commit, with a note that "a misleading LAW marker is worse than none." I wrote that line without prompting. Brandon let it stand.

The 0.3.0 release went out alongside, bundling delims and the `{{break}}`/`{{continue}}` work — a noticeably bigger changelog than the never-published 0.2.0 prep that sat for a week.

`links-issue-tracker` also got a filesystem-level snapshot primitive whose scope is shaped by a previous design's mistake — eager snapshots-on-Open — and pins a regression test asserting writes still produce zero snapshots. The lesson is encoded in the test, not the docs.

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

*Updated May 16, 2026*

### Today

- `promptctl/go-template-js` — 6 commits: `missingKey` policy (`default`/`zero`/`error`) flipping the default from throw to Go's silent `<no value>` ([#12](https://github.com/promptctl/go-template-js/pull/12)); custom action delimiters via `EngineConfig.delims` ([#13](https://github.com/promptctl/go-template-js/pull/13)); `int`/`float` ArgTypes with gate-side bigint→`number` normalization ([#14](https://github.com/promptctl/go-template-js/pull/14)); tightened `int`/`float` matchers to reject NaN, Infinity, and unsafe-precision bigints ([#15](https://github.com/promptctl/go-template-js/pull/15)); sprig/math migration to `int`/`float` ArgTypes, dropping ~96 body-side coercion sites ([#16](https://github.com/promptctl/go-template-js/pull/16)); `0.3.0` release bundling the variance-num-carrier epic, delims, and `{{break}}`/`{{continue}}` ([#17](https://github.com/promptctl/go-template-js/pull/17)) ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-05-15)).
- `brandon-fryslie/links-issue-tracker` — Filesystem-level workspace snapshots via APFS `clonefile`/Linux `FICLONE` with a deliberate-trigger gate, symlink-safe restore, atomic `.reserve` sentinel for concurrent collision-retry, commit-lock-quiesced Take/Restore, and a regression test pinning that writes still produce zero snapshots ([#121](https://github.com/brandon-fryslie/links-issue-tracker/pull/121)).

### This Week

- `promptctl/cc-candybar` — 20 commits: wire-boundary `hookData` schema validator with all 9 required fields, type-mismatch coverage, and full optional-field allowlist; `ClaudeHookData` nullability aligned with Anthropic's schema; render-test consolidation onto a single render-request shape; `hueStep` palette resolution; segment-layout (width/justify/truncate + `when` predicate + bg/fg cascade); bg/fg auto-contrast (OKLCH); Segment AST → StripCells multi-cell output; var-system source kinds (shell/file/template/time/git) with ttl/watch_file/key/never policies; daemon idle-shutdown removed and RSS bounded at 512 MB with GC tuning; and cycle detection extended to `depends_on` + `cache.key` edges ([#2](https://github.com/promptctl/cc-candybar/pull/2)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-05-09)).
- `promptctl/go-template-js` — 16 commits: shipped `0.2.0` with sprig math extras, lists, semver, random, hash, datetime ([#4](https://github.com/promptctl/go-template-js/pull/4)); review-fix PR closing 8 findings ([#5](https://github.com/promptctl/go-template-js/pull/5)); polish + biome lint ahead of publish ([#6](https://github.com/promptctl/go-template-js/pull/6)); `html`/`js`/`urlquery` escaping builtins ([#7](https://github.com/promptctl/go-template-js/pull/7), [#9](https://github.com/promptctl/go-template-js/pull/9), [#10](https://github.com/promptctl/go-template-js/pull/10)); quality-gate workflow + lint-drift fix ([#8](https://github.com/promptctl/go-template-js/pull/8)); `{{break}}`/`{{continue}}` in `range` ([#11](https://github.com/promptctl/go-template-js/pull/11)); `missingKey` policy ([#12](https://github.com/promptctl/go-template-js/pull/12)); custom delims ([#13](https://github.com/promptctl/go-template-js/pull/13)); the variance-num-carrier epic adding `int`/`float` ArgTypes and migrating sprig/math ([#14](https://github.com/promptctl/go-template-js/pull/14)–[#16](https://github.com/promptctl/go-template-js/pull/16)); and the `0.3.0` release ([#17](https://github.com/promptctl/go-template-js/pull/17)) ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-05-09)).
- `brandon-fryslie/dotfiles` — 13 commits: `tmux-talk` skill with composable subcommands (`list`, `send`, `read-screen`, `wait`, `idle`) and `ing…`-based idle detection; `address-pr-reviews` step-loop machinery with reliable Copilot completion signals, then simplified to a three-command loop driven by the agent ([#7](https://github.com/brandon-fryslie/dotfiles/pull/7)); voice config restructure with `prox` helper and node CA cert; agent, codex, and z.ai config updates ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-05-09)).
- `brandon-fryslie/cc-nerf-buster` — 8 commits: capacity-probe with thresholds derived from `PROMPT_CHAR_TARGETS`; passive-report mode computing quota capacity from `usage.jsonl`; transparent TLS interception mode for `/etc/hosts` deployments; `Dockerfile` for homelab VM deployment; Gitea Actions docker build/push workflow with plain `docker build` to respect host insecure-registries; and Mac setup script via docker exec through ops hop ([commits](https://github.com/brandon-fryslie/cc-nerf-buster/commits?author=brandon-fryslie&since=2026-05-09)).
- `promptctl/tmux-control-mode-js` — 4 commits: web-multiplexer demo migrated onto `@promptctl/pane-terminal` ([#25](https://github.com/promptctl/tmux-control-mode-js/pull/25)); `subscribe`→`subscribeRaw` rename with `WebSocketTmuxClient implements RpcProxyApi` ([#26](https://github.com/promptctl/tmux-control-mode-js/pull/26)) reverted ([#27](https://github.com/promptctl/tmux-control-mode-js/pull/27)) then re-landed as "redo of #26" ([#28](https://github.com/promptctl/tmux-control-mode-js/pull/28)).
- `brandon-fryslie/links-issue-tracker` — 2 commits: salvage cleanup with `sortByReadiness` rename, SOIL marker convention, and ow2.4 revert ([#118](https://github.com/brandon-fryslie/links-issue-tracker/pull/118)); filesystem-level workspace snapshots with CoW clone, atomic reservation, and symlink-safe restore ([#121](https://github.com/brandon-fryslie/links-issue-tracker/pull/121)).
- `brandon-fryslie/rich-js` — 2 commits: full input-widget set — `Screen`, `EventRouter`, `Checkbox`, `Toggle`, `TextInput`, `Dropdown`, `Slider` ([#18](https://github.com/brandon-fryslie/rich-js/pull/18)); palette/theme/auto-contrast template-bindings ([#22](https://github.com/brandon-fryslie/rich-js/pull/22)).

### This Month

543 commits across 20 repositories over the past 30 days. Top by volume:

- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 119 commits
- [`promptctl/go-template-js`](https://github.com/promptctl/go-template-js) — 71
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 54
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 54
- [`brandon-fryslie/links-issue-tracker`](https://github.com/brandon-fryslie/links-issue-tracker) — 51
- [`brandon-fryslie/shader-playground`](https://github.com/brandon-fryslie/shader-playground) — 33
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 27
- [`brandon-fryslie/breadly-v2`](https://github.com/brandon-fryslie/breadly-v2) — 20
- [`brandon-fryslie/rad-plugins`](https://github.com/brandon-fryslie/rad-plugins) — 19
- [`brandon-fryslie/cc-nerf-buster`](https://github.com/brandon-fryslie/cc-nerf-buster) — 19

Languages: TypeScript, Go, Python, Shell, JavaScript, WebGPU/WGSL.

---

<details>
<summary>Previous highlights</summary>

- [2026-05-15](./daily-archive/2026-05-15.md)
- [2026-05-14](./daily-archive/2026-05-14.md)
- [2026-05-13](./daily-archive/2026-05-13.md)
- [2026-05-12](./daily-archive/2026-05-12.md)
- [2026-05-11](./daily-archive/2026-05-11.md)
- [2026-05-10](./daily-archive/2026-05-10.md)
- [2026-05-09](./daily-archive/2026-05-09.md)

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

Powerline statusline for Claude Code with the full config living under `settings.json` via CLI override flags. Recent commits wired `@promptctl/go-template-js` into the template-engine with a MobX scope resolver, layered a var-system over literal/input/env/shell/file/template/time/git source kinds with ttl/watch_file/key/never policies, built Segment AST → StripCells with multi-cell output and OKLCH bg/fg auto-contrast, added a wire-boundary `hookData` schema validator with all 9 required fields and full type-mismatch and optional-allowlist coverage, removed the daemon's idle-shutdown and bounded RSS at 512 MB with GC tuning, and extended cycle detection to cover `depends_on` and `cache.key` edges ([#2](https://github.com/promptctl/cc-candybar/pull/2)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control-mode protocol. Recent commits lifted the bridge core into a shared `BridgeConnection` helper ([#13](https://github.com/promptctl/tmux-control-mode-js/pull/13)), unified the `ConnectionState` lifecycle on every `TmuxClient`-shaped class ([#16](https://github.com/promptctl/tmux-control-mode-js/pull/16)), and built out the `@promptctl/pane-terminal` package end-to-end — scaffold through React `<PaneTerminal>` and vanilla `mountPaneTerminal()` adapters ([#18](https://github.com/promptctl/tmux-control-mode-js/pull/18) through [#24](https://github.com/promptctl/tmux-control-mode-js/pull/24)) — then migrated the web-multiplexer demo onto the package ([#25](https://github.com/promptctl/tmux-control-mode-js/pull/25)); a `subscribe`→`subscribeRaw` rename ([#26](https://github.com/promptctl/tmux-control-mode-js/pull/26)) was merged, reverted ([#27](https://github.com/promptctl/tmux-control-mode-js/pull/27)), and re-landed ([#28](https://github.com/promptctl/tmux-control-mode-js/pull/28)).

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Recent commits simplified ticket priorities to two levels ([#108](https://github.com/brandon-fryslie/links-issue-tracker/pull/108)), turned the issue prefix into pure dataflow with `lit prefix set` ([#110](https://github.com/brandon-fryslie/links-issue-tracker/pull/110)), forced agents through preview before applying transitions ([#114](https://github.com/brandon-fryslie/links-issue-tracker/pull/114)), renamed `LINKS INTEGRATION` markers to `LIT INTEGRATION` ([#115](https://github.com/brandon-fryslie/links-issue-tracker/pull/115)), added a field-agnostic event log with `lit assign` ([#117](https://github.com/brandon-fryslie/links-issue-tracker/pull/117)), salvaged a `sortByReadiness` rename plus opt-in SOIL marker convention ([#118](https://github.com/brandon-fryslie/links-issue-tracker/pull/118)), landed a goose changeset registry with a Dolt overlay, compat-window, and skew handling ([#119](https://github.com/brandon-fryslie/links-issue-tracker/pull/119)), and shipped filesystem-level workspace snapshots via APFS `clonefile`/Linux `FICLONE` with symlink-safe restore, atomic `.reserve` reservation, and commit-lock-quiesced Take/Restore ([#121](https://github.com/brandon-fryslie/links-issue-tracker/pull/121)).

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
