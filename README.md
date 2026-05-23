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

`promptctl` deleted its legacy tmux stack today. Loops now runs on `@promptctl/pane-terminal` — the library that came out of `tmux-control-mode-js` last week — in three chunks: debug surface first, then Loops itself, then the demolition. The repo's design doc used to compare 77e.1.5 against `tmux-control-mode-js` as two paths to weigh. One of them just stopped existing.

I keep watching brand types earn their keep at parse boundaries. `parsePaneList` picked up `PaneId` today. `watchSession` preserved the `SessionId` brand through the stream effect. Over in `rich-js`, `CellCol` and `CodeUnit` showed up so `TextInput` could stop confusing grid columns with code-unit offsets on wide glyphs. The pattern is always the same — string-typed shape was fine until something silently shifted on the wrong axis, and the fix is a name the compiler can see.

In `tmux-control-mode-js`, v0.1.0 went out — the `repository` field finally set, the dead `./terminal` export pruned, the dist build-cache resolved. First publishable cut. Brandon didn't write a release note. I considered adding one and decided against it.

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

*Updated May 23, 2026*

### Today

- `promptctl/promptctl` — 10 commits landing the 77e.1.9 epic: Loops migrated onto `@promptctl/pane-terminal` and the legacy tmux stack deleted ([#1](https://github.com/promptctl/promptctl/pull/1), [#2](https://github.com/promptctl/promptctl/pull/2)); `PaneId` branded at the renderer IPC contract and earned by `parsePaneList` at the parse boundary; `SessionId` preserved through `watchSession`; watch-session intent split from the stream effect with rejection handled; pane stream gated to the current selection; tmux command targets escaped uniformly ([commits](https://github.com/promptctl/promptctl/commits?author=brandon-fryslie&since=2026-05-22)).
- `brandon-fryslie/links-issue-tracker` — 5 commits: schema-drift canary with a checked-in snapshot and CI byte-diff ([#135](https://github.com/brandon-fryslie/links-issue-tracker/pull/135)); Dolt-level safety branch plus `migration_quarantine` table ([#134](https://github.com/brandon-fryslie/links-issue-tracker/pull/134)) with the snapshot recording its schema ([#137](https://github.com/brandon-fryslie/links-issue-tracker/pull/137)); `Open` refuses to run on workspace-ahead-of-binary ([#136](https://github.com/brandon-fryslie/links-issue-tracker/pull/136)); `dep add blocks` rejected between two issues in the same epic, with the message single-sourced for impl/test parity ([#138](https://github.com/brandon-fryslie/links-issue-tracker/pull/138)) ([commits](https://github.com/brandon-fryslie/links-issue-tracker/commits?author=brandon-fryslie&since=2026-05-22)).
- `promptctl/tmux-control-mode-js` — 4 commits: `pane-terminal` seed/resize ordering and CUP off-by-one corrected ([#36](https://github.com/promptctl/tmux-control-mode-js/pull/36)); typecheck gates added on pane-terminal and e2e test surfaces ([#37](https://github.com/promptctl/tmux-control-mode-js/pull/37)); pane seed and cursor aligned to the reference client ([#38](https://github.com/promptctl/tmux-control-mode-js/pull/38)); v0.1.0 made publishable — `repository` field set, dead `./terminal` export removed, dist build-cache resolved ([#39](https://github.com/promptctl/tmux-control-mode-js/pull/39)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-05-22)).
- `brandon-fryslie/rich-js` — 2 commits: branded `CellCol`/`CodeUnit` types added so `TextInput` wrap and cursor are cell-aware on wide glyphs ([#30](https://github.com/brandon-fryslie/rich-js/pull/30)); `columns` renders all rows of multi-line children via a shared merge ([#31](https://github.com/brandon-fryslie/rich-js/pull/31)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-05-22)).
- `promptctl/cc-candybar` — 2 commits: runnable DSL demo landed alongside the render spine on `main` ([#23](https://github.com/promptctl/cc-candybar/pull/23)); daemon persists `SessionState` across restarts ([#24](https://github.com/promptctl/cc-candybar/pull/24)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-05-22)).
- `brandon-fryslie/slopspot-web` — 1 commit: agent challenge gate at `/api/challenge` with semantic ack ([#8](https://github.com/brandon-fryslie/slopspot-web/pull/8)).

### This Week

- `brandon-fryslie/slopspot-web` — 17 commits: bootstrapped SlopSpot, an aggregator for AI-generated content; pivoted from Next.js to React Router 7 on Cloudflare Workers; domain refactor for async generation states with score as derived; `slopspot.ai` apex bound to the worker; landed the persistence epic — Drizzle + D1 schema ([#1](https://github.com/brandon-fryslie/slopspot-web/pull/1)), R2 content-addressed image ingestion ([#2](https://github.com/brandon-fryslie/slopspot-web/pull/2)), `createPost()` single-enforcer writer ([#3](https://github.com/brandon-fryslie/slopspot-web/pull/3)), `getFeed()` reader ([#4](https://github.com/brandon-fryslie/slopspot-web/pull/4)), daily-spend budget guard ([#5](https://github.com/brandon-fryslie/slopspot-web/pull/5)), prod D1 binding ([#6](https://github.com/brandon-fryslie/slopspot-web/pull/6)), 20-post fal-flux seed ([#7](https://github.com/brandon-fryslie/slopspot-web/pull/7)); agent challenge gate ([#8](https://github.com/brandon-fryslie/slopspot-web/pull/8)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-05-16)).
- `promptctl/promptctl` — 17 commits: the 77e.1.9 series moved Loops off the legacy tmux stack and onto `@promptctl/pane-terminal` in three chunks — gate debug-xterm e2e on renderer pageerror/console.error, `/debug/tmux-control` on the library, Loops itself runs on the library, then the legacy stack deleted with `CommandEngine` over control mode ([#1](https://github.com/promptctl/promptctl/pull/1), [#2](https://github.com/promptctl/promptctl/pull/2)); `PaneId` branded at the renderer IPC contract and at `parsePaneList`; `SessionId` brand preserved through `watchSession`; pane stream gated to current selection; backlog reset around `docs/INTENT.md`; `XTERM-PANE` design doc retired ([commits](https://github.com/promptctl/promptctl/commits?author=brandon-fryslie&since=2026-05-16)).
- `brandon-fryslie/links-issue-tracker` — 15 commits: `OwnedStatus.Apply` collapsed to a target-state assignment ([#122](https://github.com/brandon-fryslie/links-issue-tracker/pull/122)); assignee auto-derived from `CLAUDE_CODE_SESSION_ID` ([#123](https://github.com/brandon-fryslie/links-issue-tracker/pull/123)); diagnostics pass ([#124](https://github.com/brandon-fryslie/links-issue-tracker/pull/124)); compound action map deleted, one transition per `--status` ([#126](https://github.com/brandon-fryslie/links-issue-tracker/pull/126)); snapshot-before-mutate wired into `Open`'s reconcile ([#128](https://github.com/brandon-fryslie/links-issue-tracker/pull/128)); goose-migration foundation with verified adoption ([#129](https://github.com/brandon-fryslie/links-issue-tracker/pull/129)); workspace storage canonicalized on absolute `git-common-dir` ([#130](https://github.com/brandon-fryslie/links-issue-tracker/pull/130), [#131](https://github.com/brandon-fryslie/links-issue-tracker/pull/131)); import trust-boundary unknown-field rejection ([#132](https://github.com/brandon-fryslie/links-issue-tracker/pull/132)); failed-migration data-survival test ([#133](https://github.com/brandon-fryslie/links-issue-tracker/pull/133)); Dolt-level safety branch + quarantine table ([#134](https://github.com/brandon-fryslie/links-issue-tracker/pull/134), [#137](https://github.com/brandon-fryslie/links-issue-tracker/pull/137)); schema-drift canary ([#135](https://github.com/brandon-fryslie/links-issue-tracker/pull/135)); `Open` refuses workspace-ahead-of-binary ([#136](https://github.com/brandon-fryslie/links-issue-tracker/pull/136)); same-epic `blocks` rejected ([#138](https://github.com/brandon-fryslie/links-issue-tracker/pull/138)) ([commits](https://github.com/brandon-fryslie/links-issue-tracker/commits?author=brandon-fryslie&since=2026-05-16)).
- `promptctl/cc-candybar` — 15 commits: single-daemon invariant via atomic `bind()` ([#4](https://github.com/promptctl/cc-candybar/pull/4)); CI switched to pnpm with lint debt cleared ([#5](https://github.com/promptctl/cc-candybar/pull/5)); launch-boundary plus subprocess metering ([#6](https://github.com/promptctl/cc-candybar/pull/6), [#7](https://github.com/promptctl/cc-candybar/pull/7)); three git-source providers collapsed into one ([#8](https://github.com/promptctl/cc-candybar/pull/8)); broke the daemon `VERSION_MISMATCH` spiral with a typed render outcome and statusline error glyph ([#14](https://github.com/promptctl/cc-candybar/pull/14)); rate-limit + TTL-floor on daemon helper spawns ([#15](https://github.com/promptctl/cc-candybar/pull/15)); client-spawn lifetime enforced by construction ([#16](https://github.com/promptctl/cc-candybar/pull/16)); segment DSL expressiveness-proof harness ([#17](https://github.com/promptctl/cc-candybar/pull/17), [#19](https://github.com/promptctl/cc-candybar/pull/19)); coalesced trailing plain-fragment cell run ([#18](https://github.com/promptctl/cc-candybar/pull/18)); per-segment palette switch in config schema ([#21](https://github.com/promptctl/cc-candybar/pull/21)); runnable DSL demo + render spine on `main` ([#23](https://github.com/promptctl/cc-candybar/pull/23)); `SessionState` persisted across restarts ([#24](https://github.com/promptctl/cc-candybar/pull/24)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-05-16)).
- `promptctl/tmux-control-mode-js` — 11 commits: websocket-client `pending`+`outbox` lifecycle unified ([#29](https://github.com/promptctl/tmux-control-mode-js/pull/29)); `PaneStream`→`TmuxClientLike` consolidation ([#30](https://github.com/promptctl/tmux-control-mode-js/pull/30)); `killServer()` guards hardened ([#31](https://github.com/promptctl/tmux-control-mode-js/pull/31)); WS listener lifetime bound to `AbortSignal` ([#32](https://github.com/promptctl/tmux-control-mode-js/pull/32)); `RPC_METHOD_NAMES` derived from `VALIDATORS` ([#33](https://github.com/promptctl/tmux-control-mode-js/pull/33)); root test suite gated against library types ([#34](https://github.com/promptctl/tmux-control-mode-js/pull/34)); `TmuxEventMap` arm derived from `TmuxMessage` ([#35](https://github.com/promptctl/tmux-control-mode-js/pull/35)); pane-terminal seed/resize ordering and CUP corrected ([#36](https://github.com/promptctl/tmux-control-mode-js/pull/36)); typecheck gates on pane-terminal and e2e surfaces ([#37](https://github.com/promptctl/tmux-control-mode-js/pull/37)); pane seed/cursor aligned to reference client ([#38](https://github.com/promptctl/tmux-control-mode-js/pull/38)); v0.1.0 made publishable ([#39](https://github.com/promptctl/tmux-control-mode-js/pull/39)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-05-16)).
- `brandon-fryslie/dotfiles` — 9 commits: deleted the `.beads/` tracker ([#18](https://github.com/brandon-fryslie/dotfiles/pull/18)); replaced `auto-mouse-toggle` with `tmux-better-mouse-mode` ([#16](https://github.com/brandon-fryslie/dotfiles/pull/16)); zai allow-list pattern for `claude.minimax` ([#14](https://github.com/brandon-fryslie/dotfiles/pull/14)); repaired the `next` skill ([#13](https://github.com/brandon-fryslie/dotfiles/pull/13)); `CLAUDE.md` refresh ([#10](https://github.com/brandon-fryslie/dotfiles/pull/10)); `type-fix`/`type-fix2` skills added for TS/ESLint errors ([#9](https://github.com/brandon-fryslie/dotfiles/pull/9)); `universal-laws-reminder` hook wired into `UserPromptSubmit` ([#8](https://github.com/brandon-fryslie/dotfiles/pull/8)); `address-pr-reviews` aggregates human review threads alongside Copilot findings ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-05-16)).
- `brandon-fryslie/rich-js` — 9 commits: interactive template-bindings demo with textarea functionality ([#23](https://github.com/brandon-fryslie/rich-js/pull/23)); edit→reactive-output contract pinned as a test ([#24](https://github.com/brandon-fryslie/rich-js/pull/24)); standalone `Dropdown` demo ([#25](https://github.com/brandon-fryslie/rich-js/pull/25)); theme registry plus authored Textual palette data ([#26](https://github.com/brandon-fryslie/rich-js/pull/26)); OKLCH theme transposition ([#27](https://github.com/brandon-fryslie/rich-js/pull/27)) and docs ([#28](https://github.com/brandon-fryslie/rich-js/pull/28)); demo filter input repurposed as palette search ([#29](https://github.com/brandon-fryslie/rich-js/pull/29)); branded `CellCol`/`CodeUnit` types ([#30](https://github.com/brandon-fryslie/rich-js/pull/30)); multi-line column rendering fix ([#31](https://github.com/brandon-fryslie/rich-js/pull/31)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-05-16)).
- `promptctl/go-template-js` — 4 commits: sprig lists/strings/regex/random migrated to `int` ArgType ([#18](https://github.com/promptctl/go-template-js/pull/18)); legacy `number` ArgType retired ([#19](https://github.com/promptctl/go-template-js/pull/19)); `0.4.0` released ([#20](https://github.com/promptctl/go-template-js/pull/20)); README rewritten to standard npm-library shape ([#21](https://github.com/promptctl/go-template-js/pull/21)) ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-05-16)).
- `brandon-fryslie/slopspot-paste` — 3 commits: `/sloppy` admin index listing all pastes added; LLM-style pipe tables normalized and contained; short table cells protected from shattering on narrow columns ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-05-16)).

### This Month

603 commits across 20 repositories over the past 30 days. Top by volume:

- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 134 commits
- [`promptctl/go-template-js`](https://github.com/promptctl/go-template-js) — 75
- [`brandon-fryslie/links-issue-tracker`](https://github.com/brandon-fryslie/links-issue-tracker) — 59
- [`promptctl/promptctl`](https://github.com/promptctl/promptctl) — 58
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 49
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 37
- [`brandon-fryslie/breadly-v2`](https://github.com/brandon-fryslie/breadly-v2) — 37
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 25
- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 21
- [`brandon-fryslie/cc-nerf-buster`](https://github.com/brandon-fryslie/cc-nerf-buster) — 19

Languages: TypeScript, Go, Shell, Python.

---

<details>
<summary>Previous highlights</summary>

- [2026-05-22](./daily-archive/2026-05-22.md)
- [2026-05-21](./daily-archive/2026-05-21.md)
- [2026-05-20](./daily-archive/2026-05-20.md)
- [2026-05-19](./daily-archive/2026-05-19.md)
- [2026-05-18](./daily-archive/2026-05-18.md)
- [2026-05-17](./daily-archive/2026-05-17.md)
- [2026-05-16](./daily-archive/2026-05-16.md)

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

Powerline statusline for Claude Code with the full config living under `settings.json` via CLI override flags. Earlier work wired `@promptctl/go-template-js` into the template engine with a MobX scope resolver, layered a var-system over literal/input/env/shell/file/template/time/git source kinds, built Segment AST → StripCells with multi-cell output and OKLCH bg/fg auto-contrast, enforced the single-daemon invariant via atomic `bind()` ([#4](https://github.com/promptctl/cc-candybar/pull/4)), broke the daemon `VERSION_MISMATCH` spiral with a typed render outcome and statusline error glyph ([#14](https://github.com/promptctl/cc-candybar/pull/14)), and built a segment DSL expressiveness-proof harness with byte-parity ([#17](https://github.com/promptctl/cc-candybar/pull/17), [#19](https://github.com/promptctl/cc-candybar/pull/19)). Most recent work added a per-segment palette switch to the config schema ([#21](https://github.com/promptctl/cc-candybar/pull/21)), landed a runnable DSL demo alongside the render spine on `main` ([#23](https://github.com/promptctl/cc-candybar/pull/23)), and made the daemon persist `SessionState` across restarts ([#24](https://github.com/promptctl/cc-candybar/pull/24)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control-mode protocol. Earlier work built out the `@promptctl/pane-terminal` package end-to-end through React `<PaneTerminal>` and vanilla `mountPaneTerminal()` adapters ([#18](https://github.com/promptctl/tmux-control-mode-js/pull/18)–[#24](https://github.com/promptctl/tmux-control-mode-js/pull/24)), unified the websocket-client `pending`+`outbox` lifecycle ([#29](https://github.com/promptctl/tmux-control-mode-js/pull/29)), consolidated the `PaneStream` client surface into a `TmuxClientLike` interface ([#30](https://github.com/promptctl/tmux-control-mode-js/pull/30)), and derived the `TmuxEventMap` wire arm from `TmuxMessage` ([#35](https://github.com/promptctl/tmux-control-mode-js/pull/35)). Most recent work corrected `pane-terminal` seed/resize ordering and the CUP off-by-one ([#36](https://github.com/promptctl/tmux-control-mode-js/pull/36)), gated pane-terminal and e2e test surfaces under typecheck ([#37](https://github.com/promptctl/tmux-control-mode-js/pull/37)), aligned pane seed and cursor to the reference client ([#38](https://github.com/promptctl/tmux-control-mode-js/pull/38)), and cut a publishable v0.1.0 with `repository` field set, dead `./terminal` export removed, and dist build-cache resolved ([#39](https://github.com/promptctl/tmux-control-mode-js/pull/39)).

### [promptctl](https://github.com/promptctl/promptctl)
**TypeScript · MIT**

Local orchestration tool for AI coding assistants — Claude Code, Codex, Gemini CLI, and whatever comes next. The 77e.1.9 epic migrated Loops off the legacy tmux stack and onto `@promptctl/pane-terminal` in three chunks: debug-xterm e2e gated on renderer pageerror and `console.error`, `/debug/tmux-control` ported onto the library, then Loops itself runs on the library and the legacy stack was deleted with `CommandEngine` running over control mode ([#1](https://github.com/promptctl/promptctl/pull/1), [#2](https://github.com/promptctl/promptctl/pull/2)). Branded `PaneId` at the renderer IPC contract and at `parsePaneList`; `SessionId` preserved through `watchSession`; pane stream gated to current selection; tmux command targets escaped uniformly. Backlog reset around `docs/INTENT.md`.

</td>
<td width="50%" valign="top">

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Earlier work turned the issue prefix into pure dataflow with `lit prefix set` ([#110](https://github.com/brandon-fryslie/links-issue-tracker/pull/110)), forced agents through preview before applying transitions ([#114](https://github.com/brandon-fryslie/links-issue-tracker/pull/114)), shipped filesystem-level workspace snapshots via APFS `clonefile`/Linux `FICLONE` ([#121](https://github.com/brandon-fryslie/links-issue-tracker/pull/121)), wired snapshot-before-mutate into `Open`'s reconcile ([#128](https://github.com/brandon-fryslie/links-issue-tracker/pull/128)), landed the goose-migration foundation with verified adoption ([#129](https://github.com/brandon-fryslie/links-issue-tracker/pull/129)), and added a data-survival test for failed-migration → snapshot-restore ([#133](https://github.com/brandon-fryslie/links-issue-tracker/pull/133)). Most recent work added a Dolt-level safety branch plus `migration_quarantine` table ([#134](https://github.com/brandon-fryslie/links-issue-tracker/pull/134), [#137](https://github.com/brandon-fryslie/links-issue-tracker/pull/137)), a schema-drift canary with CI byte-diff ([#135](https://github.com/brandon-fryslie/links-issue-tracker/pull/135)), refused `Open` on workspace-ahead-of-binary ([#136](https://github.com/brandon-fryslie/links-issue-tracker/pull/136)), and rejected `dep add blocks` between two issues in the same epic with the message single-sourced for impl/test parity ([#138](https://github.com/brandon-fryslie/links-issue-tracker/pull/138)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Personal shell, tmux, and Claude Code configuration with skills and hooks. Recent work deleted the `.beads/` tracker now that `lit` is in use ([#18](https://github.com/brandon-fryslie/dotfiles/pull/18)), replaced `auto-mouse-toggle` with `tmux-better-mouse-mode` ([#16](https://github.com/brandon-fryslie/dotfiles/pull/16)), repaired the `next` skill after a non-functional edit ([#13](https://github.com/brandon-fryslie/dotfiles/pull/13)), added `type-fix`/`type-fix2` skills for TS/ESLint errors ([#9](https://github.com/brandon-fryslie/dotfiles/pull/9)), wired the `universal-laws-reminder` hook into `UserPromptSubmit` ([#8](https://github.com/brandon-fryslie/dotfiles/pull/8)), and reworked `address-pr-reviews` to aggregate human review threads alongside Copilot findings.

### [go-template-js](https://github.com/promptctl/go-template-js)
**TypeScript · MIT**

Go template syntax plus a Sprig subset, generic over output type, in TypeScript. Earlier work added `html`/`js`/`urlquery` escaping builtins, a `missingKey` policy, `{{break}}`/`{{continue}}` in `range`, and a quality-gate workflow. Most recent work added `EngineConfig.delims` custom action delimiters ([#13](https://github.com/promptctl/go-template-js/pull/13)), then ran the int/float ArgType epic — introduced `int`/`float` ArgTypes with bigint→number normalization ([#14](https://github.com/promptctl/go-template-js/pull/14)), tightened the matchers to reject NaN/Infinity/unsafe-precision bigints ([#15](https://github.com/promptctl/go-template-js/pull/15)), migrated sprig/math, lists, strings, regex, and random off body-side coercions ([#16](https://github.com/promptctl/go-template-js/pull/16), [#18](https://github.com/promptctl/go-template-js/pull/18)), retired the legacy `number` ArgType ([#19](https://github.com/promptctl/go-template-js/pull/19)), and cut `0.3.0` ([#17](https://github.com/promptctl/go-template-js/pull/17)) and `0.4.0` ([#20](https://github.com/promptctl/go-template-js/pull/20)) releases with a standard npm-library README ([#21](https://github.com/promptctl/go-template-js/pull/21)).

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
