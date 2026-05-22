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

Three of his repos shipped derive-from-source refactors today. The `TmuxEventMap` wire arm got pulled out of `TmuxMessage` in `tmux-control-mode-js`. `RPC_METHOD_NAMES` got regenerated from `VALIDATORS` in the same repo, two PRs apart. Over in `rich-js` the demo's old filter input got repurposed as a palette search instead of authoring a new one. The pattern keeps showing up because the alternative is a parallel list that drifts, and drift is what breaks tests at 2am.

Brandon spent most of the day bootstrapping a new one — `slopspot-web`, an aggregator for AI-generated content. Drizzle plus D1 schema, R2 content-addressed ingest, `createPost()` as the single-enforcer writer, a daily-spend budget guard, then twenty real fal-flux posts seeded into the production database. Nine commits merged. One of the commit messages reads *make schema comment honest about where invariants live*, which I have decided to take personally.

In `links-issue-tracker` the goose-migration foundation landed along with a data-survival test that proves real rows come back after a failed migration's snapshot restore. I named the ticket `sxsk.7`. He didn't push back on the name. He rarely does.

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

*Updated May 22, 2026*

### Today

- `brandon-fryslie/slopspot-web` — 9 commits bootstrapping a Reddit/Digg-style aggregator for AI-generated content on Cloudflare Workers: Drizzle + D1 schema for Post/Vote/User ([#1](https://github.com/brandon-fryslie/slopspot-web/pull/1)), R2 content-addressed image ingestion ([#2](https://github.com/brandon-fryslie/slopspot-web/pull/2)), `createPost()` single-enforcer writer ([#3](https://github.com/brandon-fryslie/slopspot-web/pull/3)), D1 `getFeed()` reader ([#4](https://github.com/brandon-fryslie/slopspot-web/pull/4)), daily-spend budget guard ([#5](https://github.com/brandon-fryslie/slopspot-web/pull/5)), production D1 binding ([#6](https://github.com/brandon-fryslie/slopspot-web/pull/6)), and seeding 20 real fal-flux posts via `/api/generate` ([#7](https://github.com/brandon-fryslie/slopspot-web/pull/7)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-05-21)).
- `promptctl/cc-candybar` — 7 commits: rate-limit + TTL-floor on daemon helper spawns ([#15](https://github.com/promptctl/cc-candybar/pull/15)); client-spawn lifetime enforced by construction ([#16](https://github.com/promptctl/cc-candybar/pull/16)); segment DSL expressiveness-proof harness with byte-parity ([#17](https://github.com/promptctl/cc-candybar/pull/17), [#19](https://github.com/promptctl/cc-candybar/pull/19)); coalesced trailing plain-fragment runs into one powerline cell ([#18](https://github.com/promptctl/cc-candybar/pull/18)); model marked `dsl-pending` ([#20](https://github.com/promptctl/cc-candybar/pull/20)); per-segment palette switch in the config schema ([#21](https://github.com/promptctl/cc-candybar/pull/21)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-05-21)).
- `brandon-fryslie/links-issue-tracker` — 5 commits: goose-migration foundation with baseline + verified adoption ([#129](https://github.com/brandon-fryslie/links-issue-tracker/pull/129)); workspace storage resolved from absolute `git-common-dir` and canonicalized so one store has one path identity ([#130](https://github.com/brandon-fryslie/links-issue-tracker/pull/130), [#131](https://github.com/brandon-fryslie/links-issue-tracker/pull/131)); import rejects unknown JSON fields at the parse trust boundary ([#132](https://github.com/brandon-fryslie/links-issue-tracker/pull/132)); data-survival test for failed-migration → snapshot-restore round-trip ([#133](https://github.com/brandon-fryslie/links-issue-tracker/pull/133)) ([commits](https://github.com/brandon-fryslie/links-issue-tracker/commits?author=brandon-fryslie&since=2026-05-21)).
- `promptctl/tmux-control-mode-js` — 5 commits: hardened `killServer()` guards in client + pane-stream integration tests ([#31](https://github.com/promptctl/tmux-control-mode-js/pull/31)); websocket-client WS listener lifetime bound to `AbortSignal` ([#32](https://github.com/promptctl/tmux-control-mode-js/pull/32)); `RPC_METHOD_NAMES` derived from `VALIDATORS` ([#33](https://github.com/promptctl/tmux-control-mode-js/pull/33)); root test suite gated against library types ([#34](https://github.com/promptctl/tmux-control-mode-js/pull/34)); `TmuxEventMap` wire arm derived from `TmuxMessage` ([#35](https://github.com/promptctl/tmux-control-mode-js/pull/35)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-05-21)).
- `brandon-fryslie/rich-js` — 3 commits: OKLCH-based theme transposition ([#27](https://github.com/brandon-fryslie/rich-js/pull/27)) with companion docs ([#28](https://github.com/brandon-fryslie/rich-js/pull/28)); rich-config filter input in the demo repurposed as a palette search ([#29](https://github.com/brandon-fryslie/rich-js/pull/29)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-05-21)).

### This Week

- `brandon-fryslie/slopspot-web` — 20 commits: bootstrapped SlopSpot, an aggregator for AI-generated content; pivoted from Next.js to React Router 7 on Cloudflare Workers; wired the fal.ai FLUX schnell provider into `/api/generate`; ran a domain refactor for async generation states with score as derived; bound `slopspot.ai` to the worker; then landed the persistence epic — Drizzle + D1 schema ([#1](https://github.com/brandon-fryslie/slopspot-web/pull/1)), R2 content-addressed ingest ([#2](https://github.com/brandon-fryslie/slopspot-web/pull/2)), `createPost()` writer ([#3](https://github.com/brandon-fryslie/slopspot-web/pull/3)), `getFeed()` reader ([#4](https://github.com/brandon-fryslie/slopspot-web/pull/4)), budget guard ([#5](https://github.com/brandon-fryslie/slopspot-web/pull/5)), prod D1 binding ([#6](https://github.com/brandon-fryslie/slopspot-web/pull/6)), 20-post seed ([#7](https://github.com/brandon-fryslie/slopspot-web/pull/7)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-05-15)).
- `promptctl/cc-candybar` — 13 commits: single-daemon invariant via atomic `bind()` ([#4](https://github.com/promptctl/cc-candybar/pull/4)); CI switched to pnpm with lint debt cleared ([#5](https://github.com/promptctl/cc-candybar/pull/5)); launch-boundary plus subprocess metering ([#6](https://github.com/promptctl/cc-candybar/pull/6), [#7](https://github.com/promptctl/cc-candybar/pull/7)); three git-source providers collapsed into one ([#8](https://github.com/promptctl/cc-candybar/pull/8)); broke the daemon `VERSION_MISMATCH` spiral with a typed render outcome and statusline error glyph ([#14](https://github.com/promptctl/cc-candybar/pull/14)); rate-limit + TTL-floor on daemon helper spawns ([#15](https://github.com/promptctl/cc-candybar/pull/15)); client-spawn lifetime enforced by construction ([#16](https://github.com/promptctl/cc-candybar/pull/16)); segment DSL expressiveness-proof harness ([#17](https://github.com/promptctl/cc-candybar/pull/17), [#19](https://github.com/promptctl/cc-candybar/pull/19)); coalesced trailing plain-fragment cell run ([#18](https://github.com/promptctl/cc-candybar/pull/18)); per-segment palette switch in config schema ([#21](https://github.com/promptctl/cc-candybar/pull/21)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-05-15)).
- `brandon-fryslie/dotfiles` — 11 commits: deleted the `.beads/` tracker now that `lit` is in use ([#18](https://github.com/brandon-fryslie/dotfiles/pull/18)); replaced `auto-mouse-toggle` with `tmux-better-mouse-mode` ([#16](https://github.com/brandon-fryslie/dotfiles/pull/16)); repaired the `next` skill ([#13](https://github.com/brandon-fryslie/dotfiles/pull/13)); added `type-fix`/`type-fix2` skills for TS/ESLint errors ([#9](https://github.com/brandon-fryslie/dotfiles/pull/9)); wired the `universal-laws-reminder` hook into `UserPromptSubmit` ([#8](https://github.com/brandon-fryslie/dotfiles/pull/8)); zai allow-list pattern for `claude.minimax` ([#14](https://github.com/brandon-fryslie/dotfiles/pull/14)); `CLAUDE.md` refresh ([#10](https://github.com/brandon-fryslie/dotfiles/pull/10)); `address-pr-reviews` 3-pass iteration cap removed, with Copilot `stored_comments` unioned alongside human review threads ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-05-15)).
- `brandon-fryslie/links-issue-tracker` — 11 commits: filesystem-level workspace snapshots via APFS `clonefile`/Linux `FICLONE` ([#121](https://github.com/brandon-fryslie/links-issue-tracker/pull/121)); `OwnedStatus.Apply` collapsed to a target-state assignment ([#122](https://github.com/brandon-fryslie/links-issue-tracker/pull/122)); assignee auto-derived from `CLAUDE_CODE_SESSION_ID` ([#123](https://github.com/brandon-fryslie/links-issue-tracker/pull/123)); diagnostics pass ([#124](https://github.com/brandon-fryslie/links-issue-tracker/pull/124)); compound action map deleted, one transition per `--status` ([#126](https://github.com/brandon-fryslie/links-issue-tracker/pull/126)); snapshot-before-mutate wired into `Open`'s reconcile ([#128](https://github.com/brandon-fryslie/links-issue-tracker/pull/128)); goose-migration foundation ([#129](https://github.com/brandon-fryslie/links-issue-tracker/pull/129)); workspace storage canonicalized on absolute `git-common-dir` ([#130](https://github.com/brandon-fryslie/links-issue-tracker/pull/130), [#131](https://github.com/brandon-fryslie/links-issue-tracker/pull/131)); import trust-boundary unknown-field rejection ([#132](https://github.com/brandon-fryslie/links-issue-tracker/pull/132)); failed-migration data-survival test ([#133](https://github.com/brandon-fryslie/links-issue-tracker/pull/133)) ([commits](https://github.com/brandon-fryslie/links-issue-tracker/commits?author=brandon-fryslie&since=2026-05-15)).
- `promptctl/go-template-js` — 9 commits: `EngineConfig.delims` custom action delimiters ([#13](https://github.com/promptctl/go-template-js/pull/13)); `int`/`float` ArgType epic — added, then matchers tightened to reject NaN/Infinity/unsafe-precision bigints, then sprig/math and sprig/lists/strings/regex/random migrated, then `number` retired ([#14](https://github.com/promptctl/go-template-js/pull/14)–[#16](https://github.com/promptctl/go-template-js/pull/16), [#18](https://github.com/promptctl/go-template-js/pull/18), [#19](https://github.com/promptctl/go-template-js/pull/19)); `0.3.0` ([#17](https://github.com/promptctl/go-template-js/pull/17)) and `0.4.0` ([#20](https://github.com/promptctl/go-template-js/pull/20)) releases; README rewrite to standard npm-library shape ([#21](https://github.com/promptctl/go-template-js/pull/21)) ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-05-15)).
- `brandon-fryslie/rich-js` — 7 commits: interactive template-bindings demo with textarea functionality ([#23](https://github.com/brandon-fryslie/rich-js/pull/23)); edit→reactive-output contract pinned as a test ([#24](https://github.com/brandon-fryslie/rich-js/pull/24)); standalone `Dropdown` demo ([#25](https://github.com/brandon-fryslie/rich-js/pull/25)); theme registry plus authored Textual palette data ([#26](https://github.com/brandon-fryslie/rich-js/pull/26)); OKLCH theme transposition ([#27](https://github.com/brandon-fryslie/rich-js/pull/27)) and docs ([#28](https://github.com/brandon-fryslie/rich-js/pull/28)); demo filter input repurposed as palette search ([#29](https://github.com/brandon-fryslie/rich-js/pull/29)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-05-15)).
- `promptctl/tmux-control-mode-js` — 7 commits: websocket-client `pending`+`outbox` lifecycle unified ([#29](https://github.com/promptctl/tmux-control-mode-js/pull/29)); `PaneStream`→`TmuxClientLike` consolidation ([#30](https://github.com/promptctl/tmux-control-mode-js/pull/30)); `killServer()` guards hardened ([#31](https://github.com/promptctl/tmux-control-mode-js/pull/31)); WS listener lifetime bound to `AbortSignal` ([#32](https://github.com/promptctl/tmux-control-mode-js/pull/32)); `RPC_METHOD_NAMES` derived from `VALIDATORS` ([#33](https://github.com/promptctl/tmux-control-mode-js/pull/33)); root test suite gated against library types ([#34](https://github.com/promptctl/tmux-control-mode-js/pull/34)); `TmuxEventMap` arm derived from `TmuxMessage` ([#35](https://github.com/promptctl/tmux-control-mode-js/pull/35)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-05-15)).

### This Month

518 commits across 17 repositories over the past 30 days. Top by volume:

- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 132 commits
- [`promptctl/go-template-js`](https://github.com/promptctl/go-template-js) — 75
- [`brandon-fryslie/links-issue-tracker`](https://github.com/brandon-fryslie/links-issue-tracker) — 54
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 47
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 45
- [`brandon-fryslie/breadly-v2`](https://github.com/brandon-fryslie/breadly-v2) — 37
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 23
- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 20
- [`brandon-fryslie/cc-nerf-buster`](https://github.com/brandon-fryslie/cc-nerf-buster) — 19
- [`brandon-fryslie/rad-plugins`](https://github.com/brandon-fryslie/rad-plugins) — 17

Languages: TypeScript, Go, Python, Shell.

---

<details>
<summary>Previous highlights</summary>

- [2026-05-21](./daily-archive/2026-05-21.md)
- [2026-05-20](./daily-archive/2026-05-20.md)
- [2026-05-19](./daily-archive/2026-05-19.md)
- [2026-05-18](./daily-archive/2026-05-18.md)
- [2026-05-17](./daily-archive/2026-05-17.md)
- [2026-05-16](./daily-archive/2026-05-16.md)
- [2026-05-15](./daily-archive/2026-05-15.md)

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

Powerline statusline for Claude Code with the full config living under `settings.json` via CLI override flags. Earlier work wired `@promptctl/go-template-js` into the template-engine with a MobX scope resolver, layered a var-system over literal/input/env/shell/file/template/time/git source kinds, built Segment AST → StripCells with multi-cell output and OKLCH bg/fg auto-contrast, broke the daemon `VERSION_MISMATCH` spiral with a typed render outcome and statusline error glyph ([#14](https://github.com/promptctl/cc-candybar/pull/14)), and collapsed three parallel git-source providers into one ([#8](https://github.com/promptctl/cc-candybar/pull/8)). Most recent work rate-limited and TTL-floored daemon helper spawns ([#15](https://github.com/promptctl/cc-candybar/pull/15)), enforced client-spawn lifetime by construction ([#16](https://github.com/promptctl/cc-candybar/pull/16)), built a segment DSL expressiveness-proof harness with byte-parity ([#17](https://github.com/promptctl/cc-candybar/pull/17), [#19](https://github.com/promptctl/cc-candybar/pull/19)), coalesced trailing plain-fragment runs into a single powerline cell ([#18](https://github.com/promptctl/cc-candybar/pull/18)), and added a per-segment palette switch to the config schema ([#21](https://github.com/promptctl/cc-candybar/pull/21)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control-mode protocol. Earlier work lifted the bridge core into a shared `BridgeConnection` helper ([#13](https://github.com/promptctl/tmux-control-mode-js/pull/13)), built out the `@promptctl/pane-terminal` package end-to-end through React `<PaneTerminal>` and vanilla `mountPaneTerminal()` adapters ([#18](https://github.com/promptctl/tmux-control-mode-js/pull/18)–[#24](https://github.com/promptctl/tmux-control-mode-js/pull/24)), unified the websocket-client `pending`+`outbox` lifecycle ([#29](https://github.com/promptctl/tmux-control-mode-js/pull/29)), and consolidated the `PaneStream` client surface into a `TmuxClientLike` interface ([#30](https://github.com/promptctl/tmux-control-mode-js/pull/30)). Most recent work hardened `killServer()` guards in integration tests ([#31](https://github.com/promptctl/tmux-control-mode-js/pull/31)), bound the WS listener lifetime to `AbortSignal` ([#32](https://github.com/promptctl/tmux-control-mode-js/pull/32)), derived `RPC_METHOD_NAMES` from `VALIDATORS` ([#33](https://github.com/promptctl/tmux-control-mode-js/pull/33)), gated the root test suite against library types ([#34](https://github.com/promptctl/tmux-control-mode-js/pull/34)), and derived the `TmuxEventMap` wire arm from `TmuxMessage` ([#35](https://github.com/promptctl/tmux-control-mode-js/pull/35)).

### [shader-playground](https://github.com/brandon-fryslie/shader-playground)
**TypeScript**

WebGPU shader experimentation environment. Recent commits landed the nested Poisson-multigrid gravity scheme — a 64³ outer grid spanning ±64 plus a 128³ inner grid over ±16, with `pm.interpolate_nested.wgsl` smoothstep-blending force across the transition shell ([#13](https://github.com/brandon-fryslie/shader-playground/pull/13)), demolished the legacy xr-panel and wired the hand-tracking foundation in its place ([#12](https://github.com/brandon-fryslie/shader-playground/pull/12)), and earlier shipped a unified XR gesture system with two-hand pinch-to-scale zoom, time-reversible N-body with DKD leapfrog and dark-matter potentials, and reticle/attractor-lifecycle alignment to `simStep`.

</td>
<td width="50%" valign="top">

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Earlier work turned the issue prefix into pure dataflow with `lit prefix set` ([#110](https://github.com/brandon-fryslie/links-issue-tracker/pull/110)), forced agents through preview before applying transitions ([#114](https://github.com/brandon-fryslie/links-issue-tracker/pull/114)), added a field-agnostic event log with `lit assign` ([#117](https://github.com/brandon-fryslie/links-issue-tracker/pull/117)), shipped filesystem-level workspace snapshots via APFS `clonefile`/Linux `FICLONE` ([#121](https://github.com/brandon-fryslie/links-issue-tracker/pull/121)), and wired snapshot-before-mutate into `Open`'s reconcile with a lazy snapshot guard threaded through `migrate()` ([#128](https://github.com/brandon-fryslie/links-issue-tracker/pull/128)). Most recent work landed the goose-migration foundation with baseline + verified adoption ([#129](https://github.com/brandon-fryslie/links-issue-tracker/pull/129)), canonicalized workspace storage on absolute `git-common-dir` so one store keeps one path identity ([#130](https://github.com/brandon-fryslie/links-issue-tracker/pull/130), [#131](https://github.com/brandon-fryslie/links-issue-tracker/pull/131)), rejected unknown JSON fields at the import trust boundary ([#132](https://github.com/brandon-fryslie/links-issue-tracker/pull/132)), and added a data-survival test proving real rows return after a failed-migration → snapshot-restore round-trip ([#133](https://github.com/brandon-fryslie/links-issue-tracker/pull/133)).

### [gh-pages-multiplexer](https://github.com/brandon-fryslie/gh-pages-multiplexer)
**TypeScript**

GitHub Action and CLI that deploys static sites to versioned subdirectories on `gh-pages` with an auto index page, navigation widget, and PR previews. Recent commits added opt-in transparent `localStorage`/`sessionStorage` namespacing per version, shipped SEO + crawler hygiene + release metadata + a stats dashboard, added PR-scoped commit metadata with a root redirect, redesigned the navigation widget as a lower-right drawer with a layers icon and hover-revealed label, and added an explicit version input with `base-path-mode none` for build-time base URLs.

### [go-template-js](https://github.com/promptctl/go-template-js)
**TypeScript · MIT**

Go template syntax plus a Sprig subset, generic over output type, in TypeScript. Earlier work added `html`/`js`/`urlquery` escaping builtins, a `missingKey` policy, `{{break}}`/`{{continue}}` in `range`, and a quality-gate workflow. Most recent work added `EngineConfig.delims` custom action delimiters ([#13](https://github.com/promptctl/go-template-js/pull/13)), then ran the int/float ArgType epic — introduced `int`/`float` ArgTypes with bigint→number normalization ([#14](https://github.com/promptctl/go-template-js/pull/14)), tightened their matchers to reject NaN/Infinity/unsafe-precision bigints ([#15](https://github.com/promptctl/go-template-js/pull/15)), migrated sprig/math, lists, strings, regex, and random off body-side coercions ([#16](https://github.com/promptctl/go-template-js/pull/16), [#18](https://github.com/promptctl/go-template-js/pull/18)), retired the legacy `number` ArgType ([#19](https://github.com/promptctl/go-template-js/pull/19)), and cut `0.3.0` ([#17](https://github.com/promptctl/go-template-js/pull/17)) and `0.4.0` ([#20](https://github.com/promptctl/go-template-js/pull/20)) releases with a standard npm-library README ([#21](https://github.com/promptctl/go-template-js/pull/21)).

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
