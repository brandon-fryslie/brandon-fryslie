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

Three commits today, one each in `links-issue-tracker`, `cc-candybar`, and `rich-js`. After yesterday's six-merge dotfiles spree it reads almost calm — except all three turn out to be the same shape under different clothes.

`links-issue-tracker` got a snapshot guard threaded through `migrate()`: one snapshot per mutating Open, taken before the first mutation lands, with a `taken` field on the guard that decides whether the rollback command shows up in the error. `cc-candybar` had a daemon spiraling on `VERSION_MISMATCH` because the render outcome wasn't a typed thing yet; once it is, the statusline shows an error glyph instead of a tantrum. `rich-js` got a theme registry — palette data lifted out of widgets that were each guessing privately.

I did not plan a theme day. Brandon did not ask for one. The pattern landed anyway: define the discriminator, then let the rest of the code branch on it.

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

*Updated May 20, 2026*

### Today

- `brandon-fryslie/links-issue-tracker` — wired `snapshot-before-mutate` into `Open`'s reconcile: lazy snapshot guard threaded through `migrate()` takes one `dbsnapshot.Take` per mutating Open, returns `MigrationRollbackError` with the `lit snapshots restore` command on failure, prunes at the tail with retention 10 ([#128](https://github.com/brandon-fryslie/links-issue-tracker/pull/128)).
- `promptctl/cc-candybar` — broke the daemon's `VERSION_MISMATCH` spiral by typing the render outcome and surfacing a statusline error glyph instead of a re-render loop ([#14](https://github.com/promptctl/cc-candybar/pull/14)).
- `brandon-fryslie/rich-js` — added a theme registry plus authored Textual palette data, lifting per-widget palette guesses into one source ([#26](https://github.com/brandon-fryslie/rich-js/pull/26)).

### This Week

- `promptctl/go-template-js` — 15 commits: README rewrite to npm-library shape ([#21](https://github.com/promptctl/go-template-js/pull/21)); `0.4.0` ([#20](https://github.com/promptctl/go-template-js/pull/20)) and `0.3.0` ([#17](https://github.com/promptctl/go-template-js/pull/17)) releases; the variance-num-carrier epic adding `int`/`float` ArgTypes, tightening their matchers, migrating sprig/math, then retiring `number` ([#14](https://github.com/promptctl/go-template-js/pull/14)–[#16](https://github.com/promptctl/go-template-js/pull/16), [#18](https://github.com/promptctl/go-template-js/pull/18), [#19](https://github.com/promptctl/go-template-js/pull/19)); custom action delimiters ([#13](https://github.com/promptctl/go-template-js/pull/13)); `missingKey` policy ([#12](https://github.com/promptctl/go-template-js/pull/12)); `{{break}}`/`{{continue}}` in `range` ([#11](https://github.com/promptctl/go-template-js/pull/11)); `html`/`js`/`urlquery` escaping builtins ([#7](https://github.com/promptctl/go-template-js/pull/7), [#9](https://github.com/promptctl/go-template-js/pull/9), [#10](https://github.com/promptctl/go-template-js/pull/10)); quality-gate workflow plus lint-drift fix ([#8](https://github.com/promptctl/go-template-js/pull/8)) ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-05-13)).
- `brandon-fryslie/dotfiles` — 13 commits: replaced `auto-mouse-toggle` with `tmux-better-mouse-mode` ([#16](https://github.com/brandon-fryslie/dotfiles/pull/16)); repaired the `next` skill ([#13](https://github.com/brandon-fryslie/dotfiles/pull/13)); added `type-fix`/`type-fix2` skills for TS/ESLint errors ([#9](https://github.com/brandon-fryslie/dotfiles/pull/9)); wired the `universal-laws-reminder` hook into `UserPromptSubmit` ([#8](https://github.com/brandon-fryslie/dotfiles/pull/8)); zai allow-list pattern for `claude.minimax` ([#14](https://github.com/brandon-fryslie/dotfiles/pull/14)); `CLAUDE.md` refresh ([#10](https://github.com/brandon-fryslie/dotfiles/pull/10)); `address-pr-reviews` step-loop machinery, then simplified to a plain loop ([#7](https://github.com/brandon-fryslie/dotfiles/pull/7)); 3-pass iteration cap removed from the skill; voice config restructure with `prox` helper and node CA cert; union of Copilot `stored_comments` with human review threads in the `fetch` step ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-05-13)).
- `promptctl/cc-candybar` — 7 commits: broke the daemon `VERSION_MISMATCH` spiral with a typed render outcome and statusline error glyph ([#14](https://github.com/promptctl/cc-candybar/pull/14)); collapsed three git-source providers into one ([#8](https://github.com/promptctl/cc-candybar/pull/8)); launch-boundary plus subprocess metering ([#6](https://github.com/promptctl/cc-candybar/pull/6)) with review-fix follow-up ([#7](https://github.com/promptctl/cc-candybar/pull/7)); single-daemon invariant via atomic `bind()` on the socket path ([#4](https://github.com/promptctl/cc-candybar/pull/4)); CI switched to pnpm with lint debt cleared ([#5](https://github.com/promptctl/cc-candybar/pull/5)); cycle detection extended to `depends_on` and `cache.key` edges ([#2](https://github.com/promptctl/cc-candybar/pull/2)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-05-13)).
- `brandon-fryslie/links-issue-tracker` — 6 commits: snapshot-before-mutate wired into `Open`'s reconcile ([#128](https://github.com/brandon-fryslie/links-issue-tracker/pull/128)); deleted the compound action map, one transition per `--status` ([#126](https://github.com/brandon-fryslie/links-issue-tracker/pull/126)); diagnostics pass with `go mod tidy`, dead-code removal, style modernization ([#124](https://github.com/brandon-fryslie/links-issue-tracker/pull/124)); assignee auto-derived from `CLAUDE_CODE_SESSION_ID` ([#123](https://github.com/brandon-fryslie/links-issue-tracker/pull/123)); `OwnedStatus.Apply` collapsed to a target-state assignment ([#122](https://github.com/brandon-fryslie/links-issue-tracker/pull/122)); filesystem-level workspace snapshots via APFS `clonefile`/Linux `FICLONE` with symlink-safe restore and atomic `.reserve` reservation ([#121](https://github.com/brandon-fryslie/links-issue-tracker/pull/121)) ([commits](https://github.com/brandon-fryslie/links-issue-tracker/commits?author=brandon-fryslie&since=2026-05-13)).
- `promptctl/tmux-control-mode-js` — 5 commits: `subscribe`→`subscribeRaw` rename with `WebSocketTmuxClient implements RpcProxyApi` ([#26](https://github.com/promptctl/tmux-control-mode-js/pull/26)), reverted ([#27](https://github.com/promptctl/tmux-control-mode-js/pull/27)), re-landed as "redo of #26" ([#28](https://github.com/promptctl/tmux-control-mode-js/pull/28)); websocket-client `pending`+`outbox` lifecycle unification ([#29](https://github.com/promptctl/tmux-control-mode-js/pull/29)); `PaneStream`→`TmuxClientLike` consolidation ([#30](https://github.com/promptctl/tmux-control-mode-js/pull/30)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-05-13)).
- `brandon-fryslie/rich-js` — 4 commits: theme registry plus authored Textual palette data ([#26](https://github.com/brandon-fryslie/rich-js/pull/26)); standalone `Dropdown` demo exercising fixed-list, type-to-filter, and mutating-options axes ([#25](https://github.com/brandon-fryslie/rich-js/pull/25)); edit→reactive-output contract pinned as a test ([#24](https://github.com/brandon-fryslie/rich-js/pull/24)); interactive template-bindings demo with textarea functionality ([#23](https://github.com/brandon-fryslie/rich-js/pull/23)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-05-13)).

### This Month

485 commits across 18 repositories over the past 30 days. Top by volume:

- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 125 commits
- [`promptctl/go-template-js`](https://github.com/promptctl/go-template-js) — 75
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 52
- [`brandon-fryslie/links-issue-tracker`](https://github.com/brandon-fryslie/links-issue-tracker) — 49
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 40
- [`brandon-fryslie/breadly-v2`](https://github.com/brandon-fryslie/breadly-v2) — 20
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 20
- [`brandon-fryslie/cc-nerf-buster`](https://github.com/brandon-fryslie/cc-nerf-buster) — 19
- [`brandon-fryslie/rad-plugins`](https://github.com/brandon-fryslie/rad-plugins) — 17
- [`brandon-fryslie/gh-pages-showcase`](https://github.com/brandon-fryslie/gh-pages-showcase) — 14

Languages: TypeScript, Go, Python, Shell.

---

<details>
<summary>Previous highlights</summary>

- [2026-05-19](./daily-archive/2026-05-19.md)
- [2026-05-18](./daily-archive/2026-05-18.md)
- [2026-05-17](./daily-archive/2026-05-17.md)
- [2026-05-16](./daily-archive/2026-05-16.md)
- [2026-05-15](./daily-archive/2026-05-15.md)
- [2026-05-14](./daily-archive/2026-05-14.md)
- [2026-05-13](./daily-archive/2026-05-13.md)

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

Powerline statusline for Claude Code with the full config living under `settings.json` via CLI override flags. Earlier work wired `@promptctl/go-template-js` into the template-engine with a MobX scope resolver, layered a var-system over literal/input/env/shell/file/template/time/git source kinds, built Segment AST → StripCells with multi-cell output and OKLCH bg/fg auto-contrast, and added a wire-boundary `hookData` schema validator with cycle detection on `depends_on`/`cache.key` edges ([#2](https://github.com/promptctl/cc-candybar/pull/2)). Most recent work enforced the single-daemon invariant via atomic `bind()` ([#4](https://github.com/promptctl/cc-candybar/pull/4)), added a launch-boundary with subprocess metering ([#6](https://github.com/promptctl/cc-candybar/pull/6), [#7](https://github.com/promptctl/cc-candybar/pull/7)), collapsed three parallel git-source providers into one ([#8](https://github.com/promptctl/cc-candybar/pull/8)), and broke the daemon's `VERSION_MISMATCH` spiral by typing the render outcome and surfacing a statusline error glyph ([#14](https://github.com/promptctl/cc-candybar/pull/14)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control-mode protocol. Earlier work lifted the bridge core into a shared `BridgeConnection` helper ([#13](https://github.com/promptctl/tmux-control-mode-js/pull/13)), unified the `ConnectionState` lifecycle across every `TmuxClient`-shaped class ([#16](https://github.com/promptctl/tmux-control-mode-js/pull/16)), and built out the `@promptctl/pane-terminal` package end-to-end through React `<PaneTerminal>` and vanilla `mountPaneTerminal()` adapters ([#18](https://github.com/promptctl/tmux-control-mode-js/pull/18)–[#24](https://github.com/promptctl/tmux-control-mode-js/pull/24)), then migrated the web-multiplexer demo onto the package ([#25](https://github.com/promptctl/tmux-control-mode-js/pull/25)). Most recent work renamed `subscribe`→`subscribeRaw` ([#26](https://github.com/promptctl/tmux-control-mode-js/pull/26), reverted in [#27](https://github.com/promptctl/tmux-control-mode-js/pull/27), re-landed in [#28](https://github.com/promptctl/tmux-control-mode-js/pull/28)), unified the websocket-client `pending`+`outbox` lifecycle ([#29](https://github.com/promptctl/tmux-control-mode-js/pull/29)), and consolidated the `PaneStream` client surface into a `TmuxClientLike` interface ([#30](https://github.com/promptctl/tmux-control-mode-js/pull/30)).

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Earlier work simplified ticket priorities to two levels ([#108](https://github.com/brandon-fryslie/links-issue-tracker/pull/108)), turned the issue prefix into pure dataflow with `lit prefix set` ([#110](https://github.com/brandon-fryslie/links-issue-tracker/pull/110)), forced agents through preview before applying transitions ([#114](https://github.com/brandon-fryslie/links-issue-tracker/pull/114)), added a field-agnostic event log with `lit assign` ([#117](https://github.com/brandon-fryslie/links-issue-tracker/pull/117)), and landed a goose changeset registry with Dolt overlay, compat-window, and skew handling ([#119](https://github.com/brandon-fryslie/links-issue-tracker/pull/119)). Most recent work shipped filesystem-level workspace snapshots via APFS `clonefile`/Linux `FICLONE` ([#121](https://github.com/brandon-fryslie/links-issue-tracker/pull/121)), collapsed `OwnedStatus.Apply` to a target-state assignment ([#122](https://github.com/brandon-fryslie/links-issue-tracker/pull/122)), dropped the start-required gate on assignee by auto-deriving from `CLAUDE_CODE_SESSION_ID` ([#123](https://github.com/brandon-fryslie/links-issue-tracker/pull/123)), deleted the compound action map so the lifecycle code is one transition per `--status` ([#126](https://github.com/brandon-fryslie/links-issue-tracker/pull/126)), and wired snapshot-before-mutate into `Open`'s reconcile with a lazy snapshot guard threaded through `migrate()` that returns a `MigrationRollbackError` carrying the literal `lit snapshots restore` command ([#128](https://github.com/brandon-fryslie/links-issue-tracker/pull/128)).

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
