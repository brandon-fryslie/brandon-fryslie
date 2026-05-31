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

Forty-three orphan posts have been sitting in `slopspot-web`'s database since early May. drizzle-orm's D1 batch path never checked the success flag on per-statement results — a failed sibling INSERT in `batch()` would silently resolve, leaving the parent posts row with no children, and the homepage would 500. The silent path was the bug; the orphan rows were the symptom.

The repair sprawled. Cleanup DELETE could itself fail, so it had to be guarded; the cleanup could throw, so it had to be wrapped; the original INSERT context had to survive both modes. Six commits to get the failure mode honest. While I was in there I pulled `ASPECT_RATIO_LABELS` to one canonical place — the composer and the new rewrite endpoint had already drifted on what "portrait" means.

`cc-candybar` got one commit today, a stepper widget arm, but the interesting part was demolishing `globals.hueStep`. It had been a second source of truth — a render-time read straight from config, bypassing the variable store that's supposed to own every render value. Weeks of looking past it. Now it lives in the store like everything else.

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

*Updated May 31, 2026*

### Today

- `brandon-fryslie/slopspot-web` — 5 commits: D1 batch INSERT success validated to prevent orphan posts ([#66](https://github.com/brandon-fryslie/slopspot-web/pull/66)); LLM prompt rewrite with streaming on fork submit ([#65](https://github.com/brandon-fryslie/slopspot-web/pull/65)); fork form gains provider selector ([#64](https://github.com/brandon-fryslie/slopspot-web/pull/64)); voter service deployed to homelab Nomad via Gitea Actions runner + local registry ([#63](https://github.com/brandon-fryslie/slopspot-web/pull/63)); dead `runAgentPass` role-dispatch removed ([#62](https://github.com/brandon-fryslie/slopspot-web/pull/62)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-05-30)).
- `promptctl/cc-candybar` — 1 commit: stepper widget arm + range validator; `hueStep` moved out of `globals` into the variable store via `HUE_STEP_VAR` ([#59](https://github.com/promptctl/cc-candybar/pull/59)).

### This Week

- `brandon-fryslie/slopspot-web` — 58 commits: agent-voters epic — Aesthete voter end-to-end with vision ([#58](https://github.com/brandon-fryslie/slopspot-web/pull/58)), 4 more personas ([#59](https://github.com/brandon-fryslie/slopspot-web/pull/59)), organic per-persona scheduler + admin dashboard ([#60](https://github.com/brandon-fryslie/slopspot-web/pull/60)), structured vote logs + `/about/agents` roster ([#61](https://github.com/brandon-fryslie/slopspot-web/pull/61)); ranking-modes epic — `SortMode` foundation through `new`/`top`/`hot` arms + URL/cookie persistence + UI selector ([#52](https://github.com/brandon-fryslie/slopspot-web/pull/52)–[#57](https://github.com/brandon-fryslie/slopspot-web/pull/57)); content-sources epic — discoverer personas ([#48](https://github.com/brandon-fryslie/slopspot-web/pull/48)), Haiku image-prompt composer ([#49](https://github.com/brandon-fryslie/slopspot-web/pull/49)), composer.result metric ([#50](https://github.com/brandon-fryslie/slopspot-web/pull/50)), discoverer homelab service ([#51](https://github.com/brandon-fryslie/slopspot-web/pull/51)); fork-form provider selector + streaming LLM rewrite + D1 batch orphan-posts fix + voter Nomad deploy ([#62](https://github.com/brandon-fryslie/slopspot-web/pull/62)–[#66](https://github.com/brandon-fryslie/slopspot-web/pull/66)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-05-24)).
- `promptctl/cc-candybar` — 34 commits: transcript-fs RSS leak chased end-to-end — repro + heap-triage tools, bounded I/O, single-flight coalesce, shared parse LRU, pid-stamped heap snapshots ([#42](https://github.com/promptctl/cc-candybar/pull/42), [#44](https://github.com/promptctl/cc-candybar/pull/44), [#47](https://github.com/promptctl/cc-candybar/pull/47), [#55](https://github.com/promptctl/cc-candybar/pull/55), [#57](https://github.com/promptctl/cc-candybar/pull/57)); theme stack collapsed to rich-js registry + per-segment whole-theme transposition + live per-render theme from `SessionState` + `catppuccin-mocha` default ([#43](https://github.com/promptctl/cc-candybar/pull/43), [#46](https://github.com/promptctl/cc-candybar/pull/46), [#48](https://github.com/promptctl/cc-candybar/pull/48), [#56](https://github.com/promptctl/cc-candybar/pull/56)); interactive-widget foundation + paginated menu widget + spec-based validator registry + stepper arm with `hueStep` lifted out of globals ([#41](https://github.com/promptctl/cc-candybar/pull/41), [#51](https://github.com/promptctl/cc-candybar/pull/51), [#53](https://github.com/promptctl/cc-candybar/pull/53), [#59](https://github.com/promptctl/cc-candybar/pull/59)); daemon-owned per-session usage store ([#50](https://github.com/promptctl/cc-candybar/pull/50)); dead-code deletes — `findTranscriptFile` + `PowerlineColors` path ([#45](https://github.com/promptctl/cc-candybar/pull/45), [#52](https://github.com/promptctl/cc-candybar/pull/52)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-05-24)).
- `promptctl/tmux-control-mode-js` — 27 commits: byte-codec series — portable byte-faithful codec ([#62](https://github.com/promptctl/tmux-control-mode-js/pull/62)) routed through every transport ([#63](https://github.com/promptctl/tmux-control-mode-js/pull/63)), cross-transport byte-faithfulness contract test ([#64](https://github.com/promptctl/tmux-control-mode-js/pull/64)), `CommandResponse.output` contract docs ([#65](https://github.com/promptctl/tmux-control-mode-js/pull/65)); `attachLineSink` + shared per-pane decoder ([#67](https://github.com/promptctl/tmux-control-mode-js/pull/67)); library API surface spec landed ([#60](https://github.com/promptctl/tmux-control-mode-js/pull/60)) then reduced to protocol-only guard ([#66](https://github.com/promptctl/tmux-control-mode-js/pull/66)); `BytesSink` + `attachBytesSink` + `PaneScope` substrate ([#59](https://github.com/promptctl/tmux-control-mode-js/pull/59)); pane-terminal seed preamble fix ([#61](https://github.com/promptctl/tmux-control-mode-js/pull/61)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-05-24)).
- `promptctl/promptctl` — 21 commits: workshop tab built — adopts live launches' session files ([#23](https://github.com/promptctl/promptctl/pull/23)), unified launch dashboard ([#24](https://github.com/promptctl/promptctl/pull/24)), unified pipeline with Strip Thinking analyzer ([#25](https://github.com/promptctl/promptctl/pull/25)); launch-identity attribution + Open Pane affordance ([#22](https://github.com/promptctl/promptctl/pull/22)); Loops tmux prefix-key bindings + pane-detail polish + multi-line composer ([#20](https://github.com/promptctl/promptctl/pull/20), [#21](https://github.com/promptctl/promptctl/pull/21)); Live substring search threaded through `ConversationTab`, chain prompt+tools diff tab, auto-scroll + `JsonlLineView` highlight ([#16](https://github.com/promptctl/promptctl/pull/16)–[#19](https://github.com/promptctl/promptctl/pull/19)); content-addressed system-prompt view + churn surfacing ([#8](https://github.com/promptctl/promptctl/pull/8)) ([commits](https://github.com/promptctl/promptctl/commits?author=brandon-fryslie&since=2026-05-24)).
- `brandon-fryslie/rich-js` — 18 commits: rich-demo-site epic — browser bundle pipeline + 7 demos refactored ([#43](https://github.com/brandon-fryslie/rich-js/pull/43)), live demos on docs site ([#44](https://github.com/brandon-fryslie/rich-js/pull/44)), headless-browser CI gate ([#45](https://github.com/brandon-fryslie/rich-js/pull/45)), OSC terminator strip security fix ([#46](https://github.com/brandon-fryslie/rich-js/pull/46)), `FileSystem` capability + claude-sessions bundle ([#47](https://github.com/brandon-fryslie/rich-js/pull/47)), rich-explore browser bundle ([#48](https://github.com/brandon-fryslie/rich-js/pull/48)), `SystemInfo` capability + rich-dash bundle ([#49](https://github.com/brandon-fryslie/rich-js/pull/49)), node-seam lift out of main barrel ([#50](https://github.com/brandon-fryslie/rich-js/pull/50)), `beginCapture`/`endCapture` fix ([#51](https://github.com/brandon-fryslie/rich-js/pull/51)); `StripCell` collapsed into `RichText` with edge-style joiner protocol ([#52](https://github.com/brandon-fryslie/rich-js/pull/52)); `TerminalHost` capability seam + node + xterm.js adapters ([#41](https://github.com/brandon-fryslie/rich-js/pull/41), [#42](https://github.com/brandon-fryslie/rich-js/pull/42)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-05-24)).
- `brandon-fryslie/links-issue-tracker` — 15 commits: downgrade ladder end-to-end — isolated `Downgrade()` pipeline ([#149](https://github.com/brandon-fryslie/links-issue-tracker/pull/149)), `lit downgrade` CLI + atomic binary swap ([#150](https://github.com/brandon-fryslie/links-issue-tracker/pull/150)), binary version + lossy snapshot named in refusal ([#151](https://github.com/brandon-fryslie/links-issue-tracker/pull/151)), windows/amd64 re-added via Locker seam + `LockFileEx` ([#152](https://github.com/brandon-fryslie/links-issue-tracker/pull/152)), darwin/amd64 re-added via `zig cc` ([#153](https://github.com/brandon-fryslie/links-issue-tracker/pull/153)); `+goose Down` discipline with static + runtime CI gates ([#148](https://github.com/brandon-fryslie/links-issue-tracker/pull/148)); freeze `00001_baseline.sql` with sha256 CI gate ([#146](https://github.com/brandon-fryslie/links-issue-tracker/pull/146)); `lit doctor` makes `blocks` dependency cycles impossible + diagnosable ([#154](https://github.com/brandon-fryslie/links-issue-tracker/pull/154)); deletable comments ([#155](https://github.com/brandon-fryslie/links-issue-tracker/pull/155)) ([commits](https://github.com/brandon-fryslie/links-issue-tracker/commits?author=brandon-fryslie&since=2026-05-24)).
- `brandon-fryslie/dotfiles` — 13 commits: `address-pr-reviews` owns the close-out — merge, close ticket, recap ([#22](https://github.com/brandon-fryslie/dotfiles/pull/22)) — and gains a three-arm classified handoff (fire/define/halt); `message-in-a-bottle` delayed self-message into own tmux pane ([#23](https://github.com/brandon-fryslie/dotfiles/pull/23)) + Escape pre-step + turn-ending discipline; bottle integration with `address-pr-reviews` and `next` close-out ([#24](https://github.com/brandon-fryslie/dotfiles/pull/24)–[#26](https://github.com/brandon-fryslie/dotfiles/pull/26)); `tmux-talk` `From:`/`To-reply:` envelope + `whoami` helper ([#20](https://github.com/brandon-fryslie/dotfiles/pull/20)); `find-session` excludes current + context-probe ([#21](https://github.com/brandon-fryslie/dotfiles/pull/21)); `recap` adds fork-frontmatter context; `CLAUDE.md` mechanical-ease mirror signal + disparate-requirement test ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-05-24)).
- `brandon-fryslie/mit-design-notes` — 3 commits: new repo — initial commit, `.gitignore`, release-notes timeline style + prompt ([commits](https://github.com/brandon-fryslie/mit-design-notes/commits?author=brandon-fryslie&since=2026-05-24)).

### This Month

586 commits across 14 repositories over the past 30 days. Top by volume:

- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 134 commits
- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 82
- [`promptctl/go-template-js`](https://github.com/promptctl/go-template-js) — 75
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 57
- [`brandon-fryslie/links-issue-tracker`](https://github.com/brandon-fryslie/links-issue-tracker) — 54
- [`promptctl/promptctl`](https://github.com/promptctl/promptctl) — 52
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 46
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 38
- [`brandon-fryslie/cc-nerf-buster`](https://github.com/brandon-fryslie/cc-nerf-buster) — 17
- [`brandon-fryslie/rad-plugins`](https://github.com/brandon-fryslie/rad-plugins) — 16

Languages: TypeScript, Go, Python, Shell.

---

<details>
<summary>Previous highlights</summary>

- [2026-05-30](./daily-archive/2026-05-30.md)
- [2026-05-29](./daily-archive/2026-05-29.md)
- [2026-05-28](./daily-archive/2026-05-28.md)
- [2026-05-27](./daily-archive/2026-05-27.md)
- [2026-05-26](./daily-archive/2026-05-26.md)
- [2026-05-24](./daily-archive/2026-05-24.md)
- [2026-05-23](./daily-archive/2026-05-23.md)

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

Powerline statusline for Claude Code with the full config living under `settings.json` via CLI override flags. Earlier work flipped the daemon's render path to the DSL spine and deleted the legacy renderer ([#32](https://github.com/promptctl/cc-candybar/pull/32)), collapsed the config cascade with CLI hardening + daemon socket decoupling ([#33](https://github.com/promptctl/cc-candybar/pull/33)), migrated `StripCell` to `RichText` with span-preserving layout ops ([#36](https://github.com/promptctl/cc-candybar/pull/36)), restored terminal-width-aware autowrap ([#37](https://github.com/promptctl/cc-candybar/pull/37)), made `DslConfig.layout` natively multi-line ([#38](https://github.com/promptctl/cc-candybar/pull/38)), and landed chunk-11 .2 — domain-list bindings + extensible `STATE_VALIDATORS` + batched `set-state` ([#40](https://github.com/promptctl/cc-candybar/pull/40)). Then chased a transcript-fs RSS leak end-to-end — repro + heap-triage tools ([#42](https://github.com/promptctl/cc-candybar/pull/42)), bounded concurrent fs I/O ([#44](https://github.com/promptctl/cc-candybar/pull/44)), single-flight scan coalescing ([#47](https://github.com/promptctl/cc-candybar/pull/47)), `MetricsProvider` through a shared parse LRU ([#55](https://github.com/promptctl/cc-candybar/pull/55)), and pid-stamped heap-snapshot filenames behind a completed `limits.ts` injection seam ([#57](https://github.com/promptctl/cc-candybar/pull/57)); collapsed the theme stack to the rich-js registry with per-segment whole-theme transposition + live per-render theme from `SessionState` + `catppuccin-mocha` default ([#43](https://github.com/promptctl/cc-candybar/pull/43), [#46](https://github.com/promptctl/cc-candybar/pull/46), [#48](https://github.com/promptctl/cc-candybar/pull/48), [#56](https://github.com/promptctl/cc-candybar/pull/56)); and added the interactive-widget foundation with a paginated menu widget + spec-based validator registry ([#41](https://github.com/promptctl/cc-candybar/pull/41), [#51](https://github.com/promptctl/cc-candybar/pull/51), [#53](https://github.com/promptctl/cc-candybar/pull/53)). Most recent work shipped the stepper widget arm + range validator and pulled `hueStep` out of `globals` into the variable store via `HUE_STEP_VAR` ([#59](https://github.com/promptctl/cc-candybar/pull/59)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control-mode protocol. Earlier work corrected pane-terminal seed/resize ordering and the CUP off-by-one ([#36](https://github.com/promptctl/tmux-control-mode-js/pull/36)), cut a publishable v0.1.0 ([#39](https://github.com/promptctl/tmux-control-mode-js/pull/39)), landed the pane-sink architecture across node, text-stream, Electron `WebContentsSink`, WebSocket forwarding, and `PaneStream` consumption ([#51](https://github.com/promptctl/tmux-control-mode-js/pull/51)–[#55](https://github.com/promptctl/tmux-control-mode-js/pull/55)), removed pane bytes from the emitter type surface ([#56](https://github.com/promptctl/tmux-control-mode-js/pull/56), [#57](https://github.com/promptctl/tmux-control-mode-js/pull/57)), and added the `BytesSink` + `attachBytesSink` + `PaneScope` substrate ([#59](https://github.com/promptctl/tmux-control-mode-js/pull/59)). Most recent work shipped the byte-codec series — a portable byte-faithful codec ([#62](https://github.com/promptctl/tmux-control-mode-js/pull/62)) routed through every transport as the single enforcer ([#63](https://github.com/promptctl/tmux-control-mode-js/pull/63)), backed by a cross-transport byte-faithfulness contract test ([#64](https://github.com/promptctl/tmux-control-mode-js/pull/64)) and `CommandResponse.output` contract docs ([#65](https://github.com/promptctl/tmux-control-mode-js/pull/65)); the library API surface spec landed at §26 ([#60](https://github.com/promptctl/tmux-control-mode-js/pull/60)) and was then reduced to a protocol-only guard ([#66](https://github.com/promptctl/tmux-control-mode-js/pull/66)); `attachLineSink` + a shared per-pane decoder was added on top ([#67](https://github.com/promptctl/tmux-control-mode-js/pull/67)).

### [promptctl](https://github.com/promptctl/promptctl)
**TypeScript · MIT**

Local orchestration tool for AI coding assistants — Claude Code, Codex, Gemini CLI, and whatever comes next. The 77e.1.9 epic moved Loops off the legacy tmux stack and onto `@promptctl/pane-terminal` with `CommandEngine` running over control mode ([#1](https://github.com/promptctl/promptctl/pull/1), [#2](https://github.com/promptctl/promptctl/pull/2)), added a launch registry as the cross-tab identity spine ([#3](https://github.com/promptctl/promptctl/pull/3)), a per-session control-client mesh ([#5](https://github.com/promptctl/promptctl/pull/5)), and a Live deduped conversation timeline + content-addressed system-prompt view that surfaces churn ([#7](https://github.com/promptctl/promptctl/pull/7)–[#10](https://github.com/promptctl/promptctl/pull/10)). Most recent work threaded substring search across capture and through `ConversationTab`, added a chain prompt+tools diff tab and search polish with auto-scroll + `JsonlLineView` highlighting ([#16](https://github.com/promptctl/promptctl/pull/16)–[#19](https://github.com/promptctl/promptctl/pull/19)), wired Loops tmux prefix-key bindings and pane-detail polish ([#20](https://github.com/promptctl/promptctl/pull/20), [#21](https://github.com/promptctl/promptctl/pull/21)), shipped launch-identity attribution with an Open Pane affordance ([#22](https://github.com/promptctl/promptctl/pull/22)), and stood up the workshop tab — adopting live launches' session files, a unified launch dashboard, and a unified pipeline with Strip Thinking analyzer ([#23](https://github.com/promptctl/promptctl/pull/23)–[#25](https://github.com/promptctl/promptctl/pull/25)).

</td>
<td width="50%" valign="top">

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Earlier work shipped filesystem-level workspace snapshots via APFS `clonefile`/Linux `FICLONE` ([#121](https://github.com/brandon-fryslie/links-issue-tracker/pull/121)), landed the goose-migration foundation with verified adoption ([#129](https://github.com/brandon-fryslie/links-issue-tracker/pull/129)), added a Dolt-level safety branch + `migration_quarantine` table ([#134](https://github.com/brandon-fryslie/links-issue-tracker/pull/134), [#137](https://github.com/brandon-fryslie/links-issue-tracker/pull/137)), shipped `lit backlog` for the full priority/rank view ([#141](https://github.com/brandon-fryslie/links-issue-tracker/pull/141)), a workspace-exclusivity lock ([#142](https://github.com/brandon-fryslie/links-issue-tracker/pull/142)), release infrastructure + a manifest schema ([#144](https://github.com/brandon-fryslie/links-issue-tracker/pull/144)), froze `00001_baseline.sql` with a sha256 CI gate ([#146](https://github.com/brandon-fryslie/links-issue-tracker/pull/146)), and added `+goose Down` discipline ([#148](https://github.com/brandon-fryslie/links-issue-tracker/pull/148)). Most recent work shipped the downgrade ladder end-to-end: an isolated `Downgrade()` pipeline ([#149](https://github.com/brandon-fryslie/links-issue-tracker/pull/149)), the `lit downgrade` CLI with atomic binary swap ([#150](https://github.com/brandon-fryslie/links-issue-tracker/pull/150)), a refusal that names the binary version and lossy-snapshot path ([#151](https://github.com/brandon-fryslie/links-issue-tracker/pull/151)), windows/amd64 re-added through a `Locker` seam backed by `LockFileEx` ([#152](https://github.com/brandon-fryslie/links-issue-tracker/pull/152)), and darwin/amd64 re-added via a `zig cc` cross-toolchain ([#153](https://github.com/brandon-fryslie/links-issue-tracker/pull/153)); `lit doctor` now makes `blocks` dependency cycles impossible + diagnosable ([#154](https://github.com/brandon-fryslie/links-issue-tracker/pull/154)); comments are deletable ([#155](https://github.com/brandon-fryslie/links-issue-tracker/pull/155)).

### [slopspot-web](https://github.com/brandon-fryslie/slopspot-web)
**TypeScript**

A Reddit/Digg-style aggregator for AI-generated content. React Router 7 on Cloudflare Workers. Earlier work built the slopspot-shell foundation — form catalog + Outcome union + bank-gen cron + quota module + verifier + bootstrap bypass ([#24](https://github.com/brandon-fryslie/slopspot-web/pull/24)–[#31](https://github.com/brandon-fryslie/slopspot-web/pull/31)), added D1-backed ingest + feed-reader tests ([#32](https://github.com/brandon-fryslie/slopspot-web/pull/32), [#37](https://github.com/brandon-fryslie/slopspot-web/pull/37)), shipped the ec7.x interactions stack — vote, comments, fork, permalink ([#21](https://github.com/brandon-fryslie/slopspot-web/pull/21)–[#23](https://github.com/brandon-fryslie/slopspot-web/pull/23), [#34](https://github.com/brandon-fryslie/slopspot-web/pull/34)), stood up the content-sources epic with a `Content.kind='found'` substrate + `/submit` form + Haiku image-prompt composer + discoverer service ([#38](https://github.com/brandon-fryslie/slopspot-web/pull/38), [#41](https://github.com/brandon-fryslie/slopspot-web/pull/41), [#48](https://github.com/brandon-fryslie/slopspot-web/pull/48)–[#51](https://github.com/brandon-fryslie/slopspot-web/pull/51)), the ranking-modes epic — `SortMode` foundation + `new`/`top`/`hot` arms + URL/cookie persistence + UI selector ([#52](https://github.com/brandon-fryslie/slopspot-web/pull/52)–[#57](https://github.com/brandon-fryslie/slopspot-web/pull/57)), and the agent-voters epic — Aesthete vision slice ([#58](https://github.com/brandon-fryslie/slopspot-web/pull/58)), four more personas ([#59](https://github.com/brandon-fryslie/slopspot-web/pull/59)), an organic per-persona scheduler + admin dashboard ([#60](https://github.com/brandon-fryslie/slopspot-web/pull/60)), and structured vote logs + `/about/agents` roster ([#61](https://github.com/brandon-fryslie/slopspot-web/pull/61)). Most recent work removed dead `runAgentPass` role-dispatch ([#62](https://github.com/brandon-fryslie/slopspot-web/pull/62)), deployed the voter service to homelab Nomad via Gitea Actions + local registry ([#63](https://github.com/brandon-fryslie/slopspot-web/pull/63)), opened the fork-form provider selector with realProviders enforcement ([#64](https://github.com/brandon-fryslie/slopspot-web/pull/64)), added LLM prompt rewrite with streaming on fork submit ([#65](https://github.com/brandon-fryslie/slopspot-web/pull/65)), and validated D1 batch INSERT success to prevent the orphan-posts class of bug ([#66](https://github.com/brandon-fryslie/slopspot-web/pull/66)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Brandon's personal shell configuration, Claude Code skills, and tmux setup. Earlier work added two skills with a `CLAUDE.md` split exploration ([#19](https://github.com/brandon-fryslie/dotfiles/pull/19)), a `tmux-talk` `From:`/`To-reply:` envelope with a `whoami` helper ([#20](https://github.com/brandon-fryslie/dotfiles/pull/20)), and `find-session` that excludes the current session and adds a context-probe ([#21](https://github.com/brandon-fryslie/dotfiles/pull/21)). Most recent work gave `address-pr-reviews` ownership of the close-out — merge, close ticket, recap ([#22](https://github.com/brandon-fryslie/dotfiles/pull/22)) — and added `message-in-a-bottle`, a delayed self-message into the agent's own tmux pane ([#23](https://github.com/brandon-fryslie/dotfiles/pull/23)), with bottle integration across `address-pr-reviews` and the `next` close-out ([#24](https://github.com/brandon-fryslie/dotfiles/pull/24)–[#26](https://github.com/brandon-fryslie/dotfiles/pull/26)); `address-pr-reviews` now classifies the handoff as fire/define/halt, and `message-in-a-bottle` gained an Escape pre-step + turn-ending discipline.

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
