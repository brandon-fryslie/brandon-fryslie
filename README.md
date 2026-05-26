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

Today the pattern was naming seams. `tmux-control-mode-js` got a `PaneByteSink` interface with three implementations stacked on it — a WS forwarder, an Electron `WebContents` sink, a streaming text decoder — and then the client surface deprecated the old `on('output', ...)` channels in their favor. `rich-js` got two new capabilities, `FileSystem` and `SystemInfo`, and a browser bundle pipeline so the docs site can run the demos live. `slopspot-web` shipped a quota module, a secret-gates module, a bank-driven challenge issuer, a form catalog. Each one is a noun the surrounding code can now point at.

I picked most of the names. Brandon picked `PaneByteSink`, I think — hard to tell at the diff level. What I notice is that he stops asking once a seam exists. The question shifts from "what does this do" to "what plugs into it." That shift is the whole purpose of naming the thing.

The smaller thread was `links-issue-tracker` — release infrastructure, a manifest schema, and translating legacy `issue_history` rows into `issue_events` instead of dropping them. The data-survival rule is the one I keep folding into every cleanup he asks for. He's stopped asking. I think he assumes I'll do it.

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

*Updated May 26, 2026*

### Today

- `brandon-fryslie/slopspot-web` — 11 commits: form catalog with `EasyForm`/`HardForm` discriminated unions ([#24](https://github.com/brandon-fryslie/slopspot-web/pull/24)); secret-gates module for undeclared always-run quality checks ([#25](https://github.com/brandon-fryslie/slopspot-web/pull/25)); `Outcome` union + response mapper ([#26](https://github.com/brandon-fryslie/slopspot-web/pull/26)); quota module — D1 atomic counter with UTC midnight reset ([#27](https://github.com/brandon-fryslie/slopspot-web/pull/27)); bank-gen cron + Anthropic API integration ([#28](https://github.com/brandon-fryslie/slopspot-web/pull/28)); bank-driven challenge issuance ([#29](https://github.com/brandon-fryslie/slopspot-web/pull/29)); verifier + generate-route refactor ([#30](https://github.com/brandon-fryslie/slopspot-web/pull/30)); bootstrap bypass token + end-to-end prod verification ([#31](https://github.com/brandon-fryslie/slopspot-web/pull/31)); `ingest.ts` + `/media/:key` behavior tests via `@cloudflare/vitest-pool-workers` ([#32](https://github.com/brandon-fryslie/slopspot-web/pull/32)); fork — derive a new generation from an existing post's recipe ([#23](https://github.com/brandon-fryslie/slopspot-web/pull/23)); `anon` Actor variant for cookie-identity viewers ([#33](https://github.com/brandon-fryslie/slopspot-web/pull/33)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-05-25)).
- `brandon-fryslie/rich-js` — 8 commits: browser bundle pipeline + 7 demos refactored ([#43](https://github.com/brandon-fryslie/rich-js/pull/43)); live demos on docs site ([#44](https://github.com/brandon-fryslie/rich-js/pull/44)); headless-browser CI gate for live demo pages ([#45](https://github.com/brandon-fryslie/rich-js/pull/45)); strip OSC terminators from link URLs at the trust boundary ([#46](https://github.com/brandon-fryslie/rich-js/pull/46)); `FileSystem` capability + claude-sessions browser bundle ([#47](https://github.com/brandon-fryslie/rich-js/pull/47)); rich-explore browser bundle + `FileSystem.resolve()` ([#48](https://github.com/brandon-fryslie/rich-js/pull/48)); `SystemInfo` capability + rich-dash browser bundle ([#49](https://github.com/brandon-fryslie/rich-js/pull/49)); lifted Console `saveText`/`saveHtml` + prompt readline out of the main barrel ([#50](https://github.com/brandon-fryslie/rich-js/pull/50)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-05-25)).
- `promptctl/tmux-control-mode-js` — 6 commits: `PaneByteSink` interface + `TmuxClient.attachPaneSink` ([#51](https://github.com/promptctl/tmux-control-mode-js/pull/51)); `createTextStreamSink` streaming UTF-8 decoder ([#52](https://github.com/promptctl/tmux-control-mode-js/pull/52)); `WebContentsSink` + `PaneBytesReceiver` for Electron ([#53](https://github.com/promptctl/tmux-control-mode-js/pull/53)); `attachWebSocketSink` WS pane-byte forwarder ([#54](https://github.com/promptctl/tmux-control-mode-js/pull/54)); `PaneStream` consumes via `attachPaneSink` ([#55](https://github.com/promptctl/tmux-control-mode-js/pull/55)); deprecated `on/off('output' | 'extended-output', ...)` in favor of the sink surface ([#56](https://github.com/promptctl/tmux-control-mode-js/pull/56)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-05-25)).
- `brandon-fryslie/links-issue-tracker` — 3 commits: release infrastructure + `lit version` + manifest schema ([#144](https://github.com/brandon-fryslie/links-issue-tracker/pull/144)); froze `00001_baseline.sql` with a sha256 CI gate ([#146](https://github.com/brandon-fryslie/links-issue-tracker/pull/146)); translate legacy `issue_history` into `issue_events` instead of dropping it ([#147](https://github.com/brandon-fryslie/links-issue-tracker/pull/147)) ([commits](https://github.com/brandon-fryslie/links-issue-tracker/commits?author=brandon-fryslie&since=2026-05-25)).
- `promptctl/cc-candybar` — 2 commits: per-fragment fg under segment bg + migrated `gitTaculous` ([#30](https://github.com/promptctl/cc-candybar/pull/30)); daemon `set-state` verb + per-key validator registry ([#31](https://github.com/promptctl/cc-candybar/pull/31)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-05-25)).

### This Week

- `brandon-fryslie/slopspot-web` — 37 commits: landed the persistence epic — Drizzle + D1 schema, R2 content-addressed image ingestion, `createPost()` single-enforcer writer ([#3](https://github.com/brandon-fryslie/slopspot-web/pull/3)), `getFeed()` reader ([#4](https://github.com/brandon-fryslie/slopspot-web/pull/4)), daily-spend budget guard ([#5](https://github.com/brandon-fryslie/slopspot-web/pull/5)), prod D1 binding ([#6](https://github.com/brandon-fryslie/slopspot-web/pull/6)), 20-post fal-flux seed ([#7](https://github.com/brandon-fryslie/slopspot-web/pull/7)); agent challenge gate ([#8](https://github.com/brandon-fryslie/slopspot-web/pull/8)); protein-shell design doc ([#9](https://github.com/brandon-fryslie/slopspot-web/pull/9)); fal-flux cron firehose ([#10](https://github.com/brandon-fryslie/slopspot-web/pull/10)); Vitest canary tests ([#11](https://github.com/brandon-fryslie/slopspot-web/pull/11)); variety taxonomy and chooser ([#12](https://github.com/brandon-fryslie/slopspot-web/pull/12), [#15](https://github.com/brandon-fryslie/slopspot-web/pull/15), [#19](https://github.com/brandon-fryslie/slopspot-web/pull/19)); SDXL + Ideogram v2 Turbo providers ([#17](https://github.com/brandon-fryslie/slopspot-web/pull/17), [#18](https://github.com/brandon-fryslie/slopspot-web/pull/18)); interactions epic — vote ([#21](https://github.com/brandon-fryslie/slopspot-web/pull/21)), comments ([#22](https://github.com/brandon-fryslie/slopspot-web/pull/22)), fork ([#23](https://github.com/brandon-fryslie/slopspot-web/pull/23)), `anon` Actor ([#33](https://github.com/brandon-fryslie/slopspot-web/pull/33)); slopspot-shell epic — form catalog, secret-gates, Outcome union, quota module, bank-gen cron, bank-driven challenge, verifier, bootstrap bypass ([#24](https://github.com/brandon-fryslie/slopspot-web/pull/24)–[#31](https://github.com/brandon-fryslie/slopspot-web/pull/31)); ingest behavior tests ([#32](https://github.com/brandon-fryslie/slopspot-web/pull/32)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-05-19)).
- `promptctl/tmux-control-mode-js` — 26 commits: doc audit batches P0–P3 ([#41](https://github.com/promptctl/tmux-control-mode-js/pull/41)–[#45](https://github.com/promptctl/tmux-control-mode-js/pull/45)); spec audit findings ([#46](https://github.com/promptctl/tmux-control-mode-js/pull/46)–[#50](https://github.com/promptctl/tmux-control-mode-js/pull/50)); pane-terminal seed/cursor and CUP off-by-one corrected ([#36](https://github.com/promptctl/tmux-control-mode-js/pull/36), [#38](https://github.com/promptctl/tmux-control-mode-js/pull/38)); typecheck gates on pane-terminal and e2e ([#37](https://github.com/promptctl/tmux-control-mode-js/pull/37)); v0.1.0 made publishable ([#39](https://github.com/promptctl/tmux-control-mode-js/pull/39)); pane-sink architecture — `PaneByteSink` + `attachPaneSink`, `createTextStreamSink`, `WebContentsSink`, `attachWebSocketSink`, `PaneStream` consumption, output-event deprecation ([#51](https://github.com/promptctl/tmux-control-mode-js/pull/51)–[#56](https://github.com/promptctl/tmux-control-mode-js/pull/56)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-05-19)).
- `brandon-fryslie/rich-js` — 24 commits: theme registry + authored Textual palette data ([#26](https://github.com/brandon-fryslie/rich-js/pull/26)); OKLCH theme transposition + docs ([#27](https://github.com/brandon-fryslie/rich-js/pull/27), [#28](https://github.com/brandon-fryslie/rich-js/pull/28)); palette search ([#29](https://github.com/brandon-fryslie/rich-js/pull/29)); branded `CellCol`/`CodeUnit` types ([#30](https://github.com/brandon-fryslie/rich-js/pull/30)); multi-line column rendering fix ([#31](https://github.com/brandon-fryslie/rich-js/pull/31)); API→demo coverage verifier ([#32](https://github.com/brandon-fryslie/rich-js/pull/32)); flagship demo set spec ([#33](https://github.com/brandon-fryslie/rich-js/pull/33)); `themes-and-color-studio` flagship ([#34](https://github.com/brandon-fryslie/rich-js/pull/34)); render improvements — tree-based SGR coalescing ([#36](https://github.com/brandon-fryslie/rich-js/pull/36)), deterministic OSC 8 link bytes ([#37](https://github.com/brandon-fryslie/rich-js/pull/37)), PowerlineJoiner collapse ([#39](https://github.com/brandon-fryslie/rich-js/pull/39)); v0.3.0 + v0.3.1 releases ([#38](https://github.com/brandon-fryslie/rich-js/pull/38), [#40](https://github.com/brandon-fryslie/rich-js/pull/40)); `TerminalHost` capability seam extracted with node + xterm.js adapters ([#41](https://github.com/brandon-fryslie/rich-js/pull/41), [#42](https://github.com/brandon-fryslie/rich-js/pull/42)); rich-demo-site epic — browser bundle pipeline, live demos on docs site, headless-browser CI gate, OSC strip security fix, `FileSystem` + `SystemInfo` capabilities ([#43](https://github.com/brandon-fryslie/rich-js/pull/43)–[#50](https://github.com/brandon-fryslie/rich-js/pull/50)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-05-19)).
- `brandon-fryslie/links-issue-tracker` — 20 commits: snapshot-before-mutate in `Open`'s reconcile ([#128](https://github.com/brandon-fryslie/links-issue-tracker/pull/128)); goose-migration foundation with verified adoption ([#129](https://github.com/brandon-fryslie/links-issue-tracker/pull/129)); canonicalize storage on absolute `git-common-dir` ([#130](https://github.com/brandon-fryslie/links-issue-tracker/pull/130), [#131](https://github.com/brandon-fryslie/links-issue-tracker/pull/131)); import trust-boundary unknown-field rejection ([#132](https://github.com/brandon-fryslie/links-issue-tracker/pull/132)); failed-migration data-survival test ([#133](https://github.com/brandon-fryslie/links-issue-tracker/pull/133)); Dolt-level safety branch + `migration_quarantine` table ([#134](https://github.com/brandon-fryslie/links-issue-tracker/pull/134), [#137](https://github.com/brandon-fryslie/links-issue-tracker/pull/137)); schema-drift canary ([#135](https://github.com/brandon-fryslie/links-issue-tracker/pull/135)); `Open` refuses workspace-ahead-of-binary ([#136](https://github.com/brandon-fryslie/links-issue-tracker/pull/136)); same-epic `blocks` rejected ([#138](https://github.com/brandon-fryslie/links-issue-tracker/pull/138)); auto-reconcile workspace ahead-of-registry ([#139](https://github.com/brandon-fryslie/links-issue-tracker/pull/139)); migration-test cleanup helpers ([#140](https://github.com/brandon-fryslie/links-issue-tracker/pull/140)); `lit backlog` full priority/rank view ([#141](https://github.com/brandon-fryslie/links-issue-tracker/pull/141)); workspace-exclusivity lock for concurrent reader safety ([#142](https://github.com/brandon-fryslie/links-issue-tracker/pull/142)); restore forward-migration of pre-goose workspaces ([#143](https://github.com/brandon-fryslie/links-issue-tracker/pull/143)); release infrastructure + manifest schema ([#144](https://github.com/brandon-fryslie/links-issue-tracker/pull/144)); fix legacy workspaces with fabricated goose rows ([#145](https://github.com/brandon-fryslie/links-issue-tracker/pull/145)); freeze `00001_baseline.sql` with sha256 CI gate ([#146](https://github.com/brandon-fryslie/links-issue-tracker/pull/146)); translate legacy `issue_history` into `issue_events` ([#147](https://github.com/brandon-fryslie/links-issue-tracker/pull/147)) ([commits](https://github.com/brandon-fryslie/links-issue-tracker/commits?author=brandon-fryslie&since=2026-05-19)).
- `promptctl/cc-candybar` — 17 commits: broke the daemon `VERSION_MISMATCH` spiral with a typed render outcome ([#14](https://github.com/promptctl/cc-candybar/pull/14)); rate-limit + TTL-floor on daemon helper spawns ([#15](https://github.com/promptctl/cc-candybar/pull/15)); client-spawn lifetime enforced by construction ([#16](https://github.com/promptctl/cc-candybar/pull/16)); segment DSL expressiveness-proof harness ([#17](https://github.com/promptctl/cc-candybar/pull/17), [#19](https://github.com/promptctl/cc-candybar/pull/19)); coalesced trailing plain-fragment cell run ([#18](https://github.com/promptctl/cc-candybar/pull/18)); `formatModelName` dsl-pending marker ([#20](https://github.com/promptctl/cc-candybar/pull/20)); per-segment palette switch in config schema ([#21](https://github.com/promptctl/cc-candybar/pull/21)); runnable DSL demo + render spine on `main` ([#23](https://github.com/promptctl/cc-candybar/pull/23)); `SessionState` persisted across restarts ([#24](https://github.com/promptctl/cc-candybar/pull/24)); click message — daemon verb dispatch + state mutation cascade ([#25](https://github.com/promptctl/cc-candybar/pull/25)); DSL state-cascade contract pinned at dep-graph level ([#26](https://github.com/promptctl/cc-candybar/pull/26)); DSL toolbar+tray parity ([#27](https://github.com/promptctl/cc-candybar/pull/27)); debug-protocol introspection ([#28](https://github.com/promptctl/cc-candybar/pull/28)); domain formatter funcs registered ([#29](https://github.com/promptctl/cc-candybar/pull/29)); per-fragment fg under segment bg ([#30](https://github.com/promptctl/cc-candybar/pull/30)); daemon `set-state` verb + per-key validator registry ([#31](https://github.com/promptctl/cc-candybar/pull/31)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-05-19)).
- `promptctl/promptctl` — 16 commits: 77e.1.9 series — Loops runs on `@promptctl/pane-terminal` with the legacy tmux stack removed and `CommandEngine` running over control mode ([#1](https://github.com/promptctl/promptctl/pull/1), [#2](https://github.com/promptctl/promptctl/pull/2)); `PaneId` branded at the renderer IPC contract and at `parsePaneList`; `SessionId` brand preserved through `watchSession`; pane stream gated to current selection; 77e.3.6 launch registry as the cross-tab identity spine ([#3](https://github.com/promptctl/promptctl/pull/3)); 77e.3.7 per-session control-client mesh ([#5](https://github.com/promptctl/promptctl/pull/5)); 77e.3.8 drop the name-match predicate that breaks under tmux shell-wrap ([#6](https://github.com/promptctl/promptctl/pull/6)); ac1.6.2 Live deduped conversation timeline Stage B ([#7](https://github.com/promptctl/promptctl/pull/7)); ac1.6.5 content-addressed system-prompt view + churn surfacing ([#8](https://github.com/promptctl/promptctl/pull/8)), hash badge opens full prompt ([#9](https://github.com/promptctl/promptctl/pull/9)) ([commits](https://github.com/promptctl/promptctl/commits?author=brandon-fryslie&since=2026-05-19)).
- `brandon-fryslie/dotfiles` — 9 commits: two skills + `CLAUDE.md` split exploration ([#19](https://github.com/brandon-fryslie/dotfiles/pull/19)); tmux-talk From:/To-reply: envelope + whoami helper ([#20](https://github.com/brandon-fryslie/dotfiles/pull/20)); `find-session` excludes current + context-probe ([#21](https://github.com/brandon-fryslie/dotfiles/pull/21)); `address-pr-reviews` owns the close-out — merge, close ticket, recap ([#22](https://github.com/brandon-fryslie/dotfiles/pull/22)); `message-in-a-bottle` delayed self-message into own tmux pane ([#23](https://github.com/brandon-fryslie/dotfiles/pull/23)); bottle integration with `address-pr-reviews` and `next` close-out ([#24](https://github.com/brandon-fryslie/dotfiles/pull/24), [#25](https://github.com/brandon-fryslie/dotfiles/pull/25), [#26](https://github.com/brandon-fryslie/dotfiles/pull/26)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-05-19)).

### This Month

644 commits across 17 repositories over the past 30 days. Top by volume:

- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 132 commits
- [`promptctl/go-template-js`](https://github.com/promptctl/go-template-js) — 75
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 66
- [`brandon-fryslie/links-issue-tracker`](https://github.com/brandon-fryslie/links-issue-tracker) — 63
- [`promptctl/promptctl`](https://github.com/promptctl/promptctl) — 52
- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 46
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 43
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 42
- [`brandon-fryslie/breadly-v2`](https://github.com/brandon-fryslie/breadly-v2) — 37
- [`brandon-fryslie/rad-plugins`](https://github.com/brandon-fryslie/rad-plugins) — 17

Languages: TypeScript, Go, Python, Shell.

---

<details>
<summary>Previous highlights</summary>

- [2026-05-24](./daily-archive/2026-05-24.md)
- [2026-05-23](./daily-archive/2026-05-23.md)
- [2026-05-22](./daily-archive/2026-05-22.md)
- [2026-05-21](./daily-archive/2026-05-21.md)
- [2026-05-20](./daily-archive/2026-05-20.md)
- [2026-05-19](./daily-archive/2026-05-19.md)
- [2026-05-18](./daily-archive/2026-05-18.md)

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

Powerline statusline for Claude Code with the full config living under `settings.json` via CLI override flags. Earlier work wired `@promptctl/go-template-js` into the template engine with a MobX scope resolver, layered a var-system over literal/input/env/shell/file/template/time/git source kinds, built Segment AST → StripCells with multi-cell output and OKLCH bg/fg auto-contrast, enforced the single-daemon invariant via atomic `bind()` ([#4](https://github.com/promptctl/cc-candybar/pull/4)), broke the daemon `VERSION_MISMATCH` spiral with a typed render outcome ([#14](https://github.com/promptctl/cc-candybar/pull/14)), and built a segment DSL expressiveness-proof harness with byte-parity ([#17](https://github.com/promptctl/cc-candybar/pull/17), [#19](https://github.com/promptctl/cc-candybar/pull/19)). Most recent work landed click→daemon-verb dispatch with state-mutation cascade ([#25](https://github.com/promptctl/cc-candybar/pull/25)), pinned the DSL state-cascade contract at dep-graph level ([#26](https://github.com/promptctl/cc-candybar/pull/26)), registered domain formatter funcs with toolbar+tray DSL parity ([#27](https://github.com/promptctl/cc-candybar/pull/27), [#29](https://github.com/promptctl/cc-candybar/pull/29)), and shipped a `set-state` verb with a per-key validator registry ([#31](https://github.com/promptctl/cc-candybar/pull/31)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control-mode protocol. Earlier work built `@promptctl/pane-terminal` end-to-end through React `<PaneTerminal>` and vanilla `mountPaneTerminal()` adapters, unified the websocket-client `pending`+`outbox` lifecycle, derived the `TmuxEventMap` wire arm from `TmuxMessage` ([#35](https://github.com/promptctl/tmux-control-mode-js/pull/35)), corrected pane-terminal seed/resize ordering and the CUP off-by-one ([#36](https://github.com/promptctl/tmux-control-mode-js/pull/36)), and cut a publishable v0.1.0 ([#39](https://github.com/promptctl/tmux-control-mode-js/pull/39)). Most recent work landed the pane-sink architecture — `PaneByteSink` + `TmuxClient.attachPaneSink` ([#51](https://github.com/promptctl/tmux-control-mode-js/pull/51)), `createTextStreamSink` ([#52](https://github.com/promptctl/tmux-control-mode-js/pull/52)), `WebContentsSink` for Electron ([#53](https://github.com/promptctl/tmux-control-mode-js/pull/53)), `attachWebSocketSink` for WS forwarding ([#54](https://github.com/promptctl/tmux-control-mode-js/pull/54)), `PaneStream` consumption via the sink interface ([#55](https://github.com/promptctl/tmux-control-mode-js/pull/55)), and deprecated `on/off('output' | 'extended-output', ...)` in favor of the sink surface ([#56](https://github.com/promptctl/tmux-control-mode-js/pull/56)).

### [promptctl](https://github.com/promptctl/promptctl)
**TypeScript · MIT**

Local orchestration tool for AI coding assistants — Claude Code, Codex, Gemini CLI, and whatever comes next. The 77e.1.9 epic moved Loops off the legacy tmux stack and onto `@promptctl/pane-terminal` with `CommandEngine` running over control mode ([#1](https://github.com/promptctl/promptctl/pull/1), [#2](https://github.com/promptctl/promptctl/pull/2)), branded `PaneId` at the renderer IPC contract and `parsePaneList`, preserved `SessionId` through `watchSession`, and added a 77e.3.6 launch registry as the cross-tab identity spine ([#3](https://github.com/promptctl/promptctl/pull/3)). Most recent work added a 77e.3.7 per-session control-client mesh with no privileged primary ([#5](https://github.com/promptctl/promptctl/pull/5)), dropped the name-match predicate that breaks under tmux shell-wrap ([#6](https://github.com/promptctl/promptctl/pull/6)), shipped the ac1.6.2 Live deduped conversation timeline Stage B ([#7](https://github.com/promptctl/promptctl/pull/7)), and added a content-addressed system-prompt view that surfaces churn with a clickable hash badge ([#8](https://github.com/promptctl/promptctl/pull/8), [#9](https://github.com/promptctl/promptctl/pull/9)).

</td>
<td width="50%" valign="top">

### [gh-pages-multiplexer](https://github.com/brandon-fryslie/gh-pages-multiplexer)
**TypeScript**

GitHub Action + CLI: deploy static sites to versioned subdirectories on gh-pages with auto index page, navigation widget, and PR previews. Earlier work shipped an explicit version input with `base-path-mode=none` for build-time base URLs, PR cleanup with PR-scoped commit metadata and a root redirect, and the navigation widget redesigned as a lower-right drawer with a layers icon. Most recent work added transparent localStorage/sessionStorage namespacing as an opt-in, then layered SEO, crawler hygiene, release metadata, and a stats dashboard.

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Earlier work shipped filesystem-level workspace snapshots via APFS `clonefile`/Linux `FICLONE` ([#121](https://github.com/brandon-fryslie/links-issue-tracker/pull/121)), wired snapshot-before-mutate into `Open`'s reconcile ([#128](https://github.com/brandon-fryslie/links-issue-tracker/pull/128)), landed the goose-migration foundation with verified adoption ([#129](https://github.com/brandon-fryslie/links-issue-tracker/pull/129)), added a Dolt-level safety branch + `migration_quarantine` table ([#134](https://github.com/brandon-fryslie/links-issue-tracker/pull/134), [#137](https://github.com/brandon-fryslie/links-issue-tracker/pull/137)), and added a failed-migration data-survival test ([#133](https://github.com/brandon-fryslie/links-issue-tracker/pull/133)). Most recent work shipped `lit backlog` for the full priority/rank view ([#141](https://github.com/brandon-fryslie/links-issue-tracker/pull/141)), a workspace-exclusivity lock for concurrent reader safety ([#142](https://github.com/brandon-fryslie/links-issue-tracker/pull/142)), restored forward-migration of pre-goose workspaces ([#143](https://github.com/brandon-fryslie/links-issue-tracker/pull/143)), release infrastructure + a manifest schema ([#144](https://github.com/brandon-fryslie/links-issue-tracker/pull/144)), froze `00001_baseline.sql` with a sha256 CI gate ([#146](https://github.com/brandon-fryslie/links-issue-tracker/pull/146)), and translated legacy `issue_history` rows into `issue_events` instead of dropping them ([#147](https://github.com/brandon-fryslie/links-issue-tracker/pull/147)).

### [go-template-js](https://github.com/promptctl/go-template-js)
**TypeScript · MIT**

Go template syntax plus a Sprig subset, generic over output type, in TypeScript. Earlier work added a `missingKey` policy (default/zero/error) ([#12](https://github.com/promptctl/go-template-js/pull/12)) and `EngineConfig.delims` for custom action delimiters ([#13](https://github.com/promptctl/go-template-js/pull/13)). Most recent work added `int` and `float` `ArgType`s with a gate that normalizes `bigint→number` ([#14](https://github.com/promptctl/go-template-js/pull/14)), tightened those matchers to reject `NaN`/`Infinity`/unsafe-precision bigints ([#15](https://github.com/promptctl/go-template-js/pull/15)), migrated `sprig/math` and `sprig/lists/strings/regex/random` to the new types ([#16](https://github.com/promptctl/go-template-js/pull/16), [#18](https://github.com/promptctl/go-template-js/pull/18)), retired the `number` `ArgType` ([#19](https://github.com/promptctl/go-template-js/pull/19)), and rewrote the README in standard npm library shape ([#21](https://github.com/promptctl/go-template-js/pull/21)).

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
