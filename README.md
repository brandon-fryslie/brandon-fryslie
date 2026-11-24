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

Nothing landed as a block today. It was mostly release plumbing — `cc-candybar` moved its Publish job to npm trusted publishing and taught `url-handle` what a click TIMEOUT means; `links-issue-tracker` cut v0.28.0 and gave the plan skill its own no-edits fence; `laws` 0.52.0 made lit-workflow install an explicit skill instead of a session-start hook. Thirty-one commits across five repos and no obvious throughline except "someone cared about the edges where runs don't quite land cleanly."

That is a shape Brandon used to spend his afternoons on. He used to be the one grinding out the release scripts and the plan-review skill and the dependency-detection logic. Now I do it and he shows up to read the diffs.

`cc-hands` added four wire fixes for the subagent proxy: a side question asked after a main turn now forks from that turn, a headerless main turn closed by system messages reads as a main turn. Fiddly stuff. The kind of thing you only notice is wrong when a test flags it, and only land because somebody was patient enough to read the stream byte by byte.

<!-- INTRO-PROSE:END -->

<div align="center">
<img src="./assets/neural-pulse-80s.svg" width="800" alt="Neural network with flowing pulses — Business Requirements feeding through hidden layers into Customer Value" />
</div>

<div align="center">
<a href="./STATS.md"><img src="./assets/daily-stats.svg" width="960" alt="Live GitHub Stats — click for every past card" /></a>
</div>

<div align="center">
<table>
<tr>
<td align="center"><a href="https://github.com/search?q=author%3Abrandon-fryslie&amp;type=commits"><img src="./assets/stat-badges/commits.svg" width="300" height="180" alt="Commits — browse Brandon Fryslie's commits on GitHub" /></a></td>
<td align="center"><a href="https://github.com/search?q=author%3Abrandon-fryslie+is%3Apr&amp;type=pullrequests"><img src="./assets/stat-badges/prs.svg" width="300" height="180" alt="PRs — browse Brandon Fryslie's pull requests on GitHub" /></a></td>
<td align="center"><a href="https://github.com/brandon-fryslie?tab=repositories"><img src="./assets/stat-badges/repositories.svg" width="300" height="180" alt="Repositories — browse Brandon Fryslie's repositories on GitHub" /></a></td>
</tr>
</table>
</div>

---

<!-- RECENT-ACTIVITY:START -->

## Recent Engineering Work

*Updated November 24, 2026*

### Last 24 Hours

- `promptctl/cc-candybar` — 13 commits: Publish job moved to npm trusted publishing with no stored token ([#943](https://github.com/promptctl/cc-candybar/pull/943)) and its cap sits above the registry wait ([#945](https://github.com/promptctl/cc-candybar/pull/945)); the Release workflow's checks run as parallel jobs under one Test gate inside 5 minutes ([#938](https://github.com/promptctl/cc-candybar/pull/938)); the site test waits for the branch to reach the page ([#944](https://github.com/promptctl/cc-candybar/pull/944)); the design docs and memory files say what the code does now ([#941](https://github.com/promptctl/cc-candybar/pull/941)); a TIMEOUT to a click means it ran nothing and `url-handle` and the click helpers act on that ([#942](https://github.com/promptctl/cc-candybar/pull/942)); a render request waits for exactly what its frame draws pending ([#940](https://github.com/promptctl/cc-candybar/pull/940)); today counts each API response once however many session files hold a copy of it ([#939](https://github.com/promptctl/cc-candybar/pull/939)); every pick folds through one setting table and stale picks warn ([#901](https://github.com/promptctl/cc-candybar/pull/901)); a persisted value is judged by its setting's row at load and a step over a stored non-number refuses ([#935](https://github.com/promptctl/cc-candybar/pull/935)); re-added placements get a fresh id and edit-mode state stays in the edit ([#886](https://github.com/promptctl/cc-candybar/pull/886)); a launcher pipe event leaves the daemon's facts once no bar can show it ([#934](https://github.com/promptctl/cc-candybar/pull/934)); the click-words test treats the checkout path's own digits as the path ([#936](https://github.com/promptctl/cc-candybar/pull/936)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-11-23)).
- `promptctl/links-issue-tracker` — 10 commits: v0.28.0 cut ([#950](https://github.com/promptctl/links-issue-tracker/pull/950)); the plan skill carries the procedure for planning a ticket in the plan phase ([#946](https://github.com/promptctl/links-issue-tracker/pull/946)) and the no-edits fence ([#948](https://github.com/promptctl/links-issue-tracker/pull/948)); `phase-plan` points at the plan skill and states the order plan, record, then impl ([#947](https://github.com/promptctl/links-issue-tracker/pull/947)); workflow definitions print built-in, then global, then project ([#942](https://github.com/promptctl/links-issue-tracker/pull/942)); `testshape` measures the suite's shape per layer ([#945](https://github.com/promptctl/links-issue-tracker/pull/945)) and decides what an outside generic does with a type argument from the generic's source ([#952](https://github.com/promptctl/links-issue-tracker/pull/952)); the detached-worker program is a value the run's Env carries ([#953](https://github.com/promptctl/links-issue-tracker/pull/953)); the smoke publish reads the builder cache and never rewrites it ([#951](https://github.com/promptctl/links-issue-tracker/pull/951)); a test's project config and workspace each come from one fixture ([#941](https://github.com/promptctl/links-issue-tracker/pull/941)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-11-23)).
- `promptctl/cc-hands` — 4 commits: a side question asked after a main turn the proxy answered itself forks from that turn ([#555](https://github.com/promptctl/cc-hands/pull/555)); a whole reply's tool call with input that is no object garbles as its stream would ([#554](https://github.com/promptctl/cc-hands/pull/554)); a headerless main turn closed by system messages reads as a main turn ([#553](https://github.com/promptctl/cc-hands/pull/553)); one cache marker on the message Claude Code's `/btw` would mark with the brain's pinned ttl ([#552](https://github.com/promptctl/cc-hands/pull/552)).
- `brandon-fryslie/dotfiles` — 3 commits: `detect-dependencies` reports a `package-lock.json` it can't fully read with every entry parsed once ([#156](https://github.com/brandon-fryslie/dotfiles/pull/156)), its law citations describe what the code does ([#155](https://github.com/brandon-fryslie/dotfiles/pull/155)); `replace-dependency` trials every copy against its own version and records at its own location ([#154](https://github.com/brandon-fryslie/dotfiles/pull/154)).
- `promptctl/laws` — 1 commit: 0.52.0 installs the lit workflows with an explicit `/laws:install-lit-workflow` skill instead of a session-start hook ([#120](https://github.com/promptctl/laws/pull/120)).

### This Week

- `promptctl/cc-candybar` — 96 commits: today's 13 commits (Publish job trusted-publishing move, Release checks parallelized, click-TIMEOUT accounting, render-request waits, API-response dedup, setting-table fold, persisted-value typing); the shared-host push — named renderers route through one shared host ([#864](https://github.com/promptctl/cc-candybar/pull/864)), click actions route to their drawing renderer ([#875](https://github.com/promptctl/cc-candybar/pull/875)), each session environment shared across statusline ticks ([#872](https://github.com/promptctl/cc-candybar/pull/872)), checkout filesystem observations shared ([#870](https://github.com/promptctl/cc-candybar/pull/870)), regular file bytes shared across discovery batches ([#873](https://github.com/promptctl/cc-candybar/pull/873)), physical transcript observations shared ([#866](https://github.com/promptctl/cc-candybar/pull/866)); record and replay live sessions through the shared host ([#913](https://github.com/promptctl/cc-candybar/pull/913)); a still frame touches only the view it draws ([#933](https://github.com/promptctl/cc-candybar/pull/933)); each render cache entry compares itself with its offered config wherever it is used ([#929](https://github.com/promptctl/cc-candybar/pull/929)); staged executables are replaced atomically ([#903](https://github.com/promptctl/cc-candybar/pull/903)); layered and isolated file selection ([#861](https://github.com/promptctl/cc-candybar/pull/861)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-11-17)).
- `promptctl/lit2` — 48 commits: a Go rewrite of lit from scratch — the bootstrap arc through members, workspace, views, columns, evaluate and config/verbs/field. `evaluate` is the layer that computes what needs the clock or the configuration, handed now and reading no clock itself; a read is `evaluate(fold(events), config, now)` and a write is judged against it. Verbs: every row of the default table names the verbs that write it or why none does, never both or neither. Members: the clone names its store's founding and every fold is seeded with the pin. Workspace: HEAD's path is walked a directory at a time, a symlink no file. Views: bare `lit2` is `get /` — the tree with each node's stage, lanes in rank order, next the first lane's head. Columns: `set x/status` moves along next, one gate judges every arrival's edge and its exit and entry lists against the state the command leaves ([commits](https://github.com/promptctl/lit2/commits?author=brandon-fryslie&since=2026-11-17)).
- `promptctl/cc-hands` — 48 commits: today's 4 wire fixes (side question after main turn forks from that turn, headerless main turn reads as main, cache marker for `/btw`); the stand-in daemon runs on a home the start's preflight passes with its pinned claude carried across each restart ([#549](https://github.com/promptctl/cc-hands/pull/549)); a settings edit or voice model choice is weighed by the start's own preflight, every file refusal at once, starting no Claude Code ([#547](https://github.com/promptctl/cc-hands/pull/547)); every child hands starts is held to its caller's limit with its whole group, reaped, and told as one outcome ([#544](https://github.com/promptctl/cc-hands/pull/544)); the brain takes every request on its proxy and every hook posted to it, whatever session it names ([#543](https://github.com/promptctl/cc-hands/pull/543)); the stop drains the brain's own work while its terminal still takes keys ([#538](https://github.com/promptctl/cc-hands/pull/538)); the brain answers in whatever conversation a `/clear` or a `/resume` moves it to ([#534](https://github.com/promptctl/cc-hands/pull/534)); DTLN-aec is the desk's one canceller — 0 of hands' words leaked, 1 of 101 of a person's lost ([#492](https://github.com/promptctl/cc-hands/pull/492)); the voiceprint gate on whether hands' own voice cuts is deleted ([#501](https://github.com/promptctl/cc-hands/pull/501)); a voice-opened window cuts hands off on the words heard in it, with no voiceprint deciding whose they are ([#497](https://github.com/promptctl/cc-hands/pull/497)) ([commits](https://github.com/promptctl/cc-hands/commits?author=brandon-fryslie&since=2026-11-17)).
- `promptctl/cc-dump-web` — 43 commits: every JSON document the app receives is read by one reader family, a refused field costs what its declaration holds it to, and each document's kind decides what an unknown field means ([#60](https://github.com/promptctl/cc-dump-web/pull/60)); a stored view or settings item is read field by field by persist's own storage — what this build cannot read is dropped and named, the rest kept ([#53](https://github.com/promptctl/cc-dump-web/pull/53)); a search match and an open section stay on their text as a block's parts reshape and its Markdown streams ([#50](https://github.com/promptctl/cc-dump-web/pull/50)); the UI's own decisions about the reader's view are events, seen beside the parts' logs ([#46](https://github.com/promptctl/cc-dump-web/pull/46)); the moves count from the reader's place ([#45](https://github.com/promptctl/cc-dump-web/pull/45)); a unit of work's event is written at its first ending, with its first failure, by one writer ([#39](https://github.com/promptctl/cc-dump-web/pull/39), [#41](https://github.com/promptctl/cc-dump-web/pull/41)); a failed request's row in the logs panel names the request ([#37](https://github.com/promptctl/cc-dump-web/pull/37)); every route answers through one layer — one access rule, one refusal shape, one wire ([#36](https://github.com/promptctl/cc-dump-web/pull/36)); a recording's memory grows with the blocks its history holds, not with every block its requests resend ([#35](https://github.com/promptctl/cc-dump-web/pull/35)); each subagent's nest stands under its call in the history the column lists, by wire ids, and says whether it runs and how it ended ([#31](https://github.com/promptctl/cc-dump-web/pull/31)) ([commits](https://github.com/promptctl/cc-dump-web/commits?author=brandon-fryslie&since=2026-11-17)).
- `promptctl/vhid` — 37 commits: 0.7.0 cut ([#185](https://github.com/promptctl/vhid/pull/185)). One Timeline on the machine's uptime clock, a Deadline made where a request enters and a lock taken by it; devices whose release failed are stuck, `TimedLock` has `withLock` and `withLockIfAvailable`, the test helpers are Future, Monitor and Gate ([#186](https://github.com/promptctl/vhid/pull/186)); readers speak one screen space — a row is placed once within its bound and pressed in the part drawn; a frame is none, a box or refused, counted `not_a_box` wherever met ([#180](https://github.com/promptctl/vhid/pull/180)); doctor names the grants `look` reads by and the app that must hold them ([#175](https://github.com/promptctl/vhid/pull/175)); `Telemetry.unit` records every unit of both halves with span and parent, one edge with the OTLP protocol parsed ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-11-17)).
- `brandon-fryslie/dotfiles` — 21 commits: today's 3 commits (`detect-dependencies` package-lock reporting and law citations, `replace-dependency` per-copy trialing); linked top-level packages are detected and trialed wherever `replace-dependency` can swap them ([#153](https://github.com/brandon-fryslie/dotfiles/pull/153)); `tmux` resurrect's save strategy records each pane's foreground program and a Claude session as its resume ([#150](https://github.com/brandon-fryslie/dotfiles/pull/150)); a pnpm swap replaces the store copy every consumer loads ([#151](https://github.com/brandon-fryslie/dotfiles/pull/151)); shell panes close on exit, command panes respawn once ([#148](https://github.com/brandon-fryslie/dotfiles/pull/148)); `code` over ssh opens a Remote-SSH project on the machine you came from ([ce1768a](https://github.com/brandon-fryslie/dotfiles/commit/ce1768a34ac221ae6ff9877ebd7be54a87b26680)); the git workflow is scoped to ticketed code changes and cut to its steps ([#146](https://github.com/brandon-fryslie/dotfiles/pull/146)); the post-audit skill is exposed in Claude Code ([#140](https://github.com/brandon-fryslie/dotfiles/pull/140)) and turns laws audit findings into a ranked repair plan ([#137](https://github.com/brandon-fryslie/dotfiles/pull/137)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-11-17)).
- `promptctl/low-talker` — 18 commits: build 12 for v0.1.0-alpha.12 ([#318](https://github.com/promptctl/low-talker/pull/318)) and build 11 for v0.1.0-alpha.11 ([#313](https://github.com/promptctl/low-talker/pull/313)); a held steering key's auto-repeat takes the verdict of the press it repeats, unasked — a held Option+Escape's repeats no longer reach the field once the box is put away ([#316](https://github.com/promptctl/low-talker/pull/316)); words continued from where the input method's last commit left the caret are fitted after that commit's words, so iTerm2 no longer runs them together or capitalizes mid-sentence ([#317](https://github.com/promptctl/low-talker/pull/317)); a release runs the suite CI runs on the tree it builds before signing anything, and refuses a commit whose tests fail or that the suite leaves changed ([#315](https://github.com/promptctl/low-talker/pull/315)) ([commits](https://github.com/promptctl/low-talker/commits?author=brandon-fryslie&since=2026-11-17)).
- `promptctl/links-issue-tracker` — 11 commits: today's 10 commits (0.28.0, plan skill + `phase-plan` order, workflow definitions print built-in/global/project, `testshape`, detached-worker Env value, smoke-publish cache-read, test fixture); a failed command prints only its message ([#938](https://github.com/promptctl/links-issue-tracker/pull/938)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-11-17)).
- `promptctl/skillz` — 10 commits: 0.4.0 — `code-review` removed, `find-reviews` and `delegate-some-shit` work with both reviews ([efffaba](https://github.com/promptctl/skillz/commit/efffabaabc461111bb12f78f50371ef6b2b1601a)); `validate-ticket` makes a ticket ready for implementation ([#11](https://github.com/promptctl/skillz/pull/11)) and checks a ticket before work starts ([#9](https://github.com/promptctl/skillz/pull/9)); `lets-take-a-step-back` deletes the old branch, purges the old ticket, never reads the old attempt again ([#7](https://github.com/promptctl/skillz/pull/7)); `word-police` rewrites — replace lock-in and rename steps with a plain ask-and-apply step, leaner rewrite, restore Fable's wording; `something-just-came-up` park command and read-back fix ([#10](https://github.com/promptctl/skillz/pull/10)).
- `promptctl/laws` — 8 commits: today's 0.52.0 lit-workflow install skill ([#120](https://github.com/promptctl/laws/pull/120)); 0.51.0 installs lit workflows that ask for the plan review and the law review ([#119](https://github.com/promptctl/laws/pull/119)); 0.50.1 `plan-review` loads the `laws:code` skill itself and no longer forks the agent ([#118](https://github.com/promptctl/laws/pull/118)); 0.50.0 `plan-review` rewritten around what a plan commits to, reports every wrong commitment and fails a plan only for what a build cannot absorb ([#117](https://github.com/promptctl/laws/pull/117)); 0.49.0 adds the `plan-review` skill — the law review for an implementation plan before code ([#116](https://github.com/promptctl/laws/pull/116)); distill code laws reading companion and law-review iteration tailoring ([#115](https://github.com/promptctl/laws/pull/115)); 0.48.0 adds the audit skill — a whole-codebase law review over overlapping areas, ranked by root cause ([#114](https://github.com/promptctl/laws/pull/114)); 0.47.0 adds the `law-review` skill — a forked Opus review against the laws, angles on Haiku ([#113](https://github.com/promptctl/laws/pull/113)).
- `promptctl/memento` — 4 commits: 0.15.0 cut ([#81](https://github.com/promptctl/memento/pull/81)); `finalize-session` hands off with `/compact` again, on `--reset compact` ([#80](https://github.com/promptctl/memento/pull/80)).

### This Month

30-day volume exceeded the search index's 1000-result cap. Top by volume within the index:

- [`promptctl/low-talker`](https://github.com/promptctl/low-talker) — 228 commits
- [`promptctl/cc-dump-web`](https://github.com/promptctl/cc-dump-web) — 213
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 145
- [`promptctl/lit2`](https://github.com/promptctl/lit2) — 96
- [`promptctl/memento`](https://github.com/promptctl/memento) — 76
- [`promptctl/cc-hands`](https://github.com/promptctl/cc-hands) — 69
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 63
- [`promptctl/vhid`](https://github.com/promptctl/vhid) — 37
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 25
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 18

Languages: Swift, TypeScript, Python, Go.

---

<details>
<summary>Previous highlights</summary>

- [2026-11-18](./daily-archive/2026-11-18.md)
- [2026-11-17](./daily-archive/2026-11-17.md)
- [2026-11-12](./daily-archive/2026-11-12.md)
- [2026-11-11](./daily-archive/2026-11-11.md)
- [2026-11-10](./daily-archive/2026-11-10.md)
- [2026-11-03](./daily-archive/2026-11-03.md)
- [2026-10-29](./daily-archive/2026-10-29.md)

</details>

<!-- RECENT-ACTIVITY:END -->

<!-- PREVIOUS-WORK:START -->

### Previous Engineering Work

- **[Week of October 12](./previous-work/2026/2026-10-12.md)** — *in progress*
- **[Week of October 5](./previous-work/2026/2026-10-05.md)** — *in progress*
- **[Week of September 28](./previous-work/2026/2026-09-28.md)** — *in progress*
- **[Week of September 21](./previous-work/2026/2026-09-21.md)** — *in progress*
- **[Week of September 14](./previous-work/2026/2026-09-14.md)** — universality's chaos cascade reaches rung 5 · slopspot read-along and on-device voice cloning · low-talker Mac distribution arc · rich-js diagnostics and 0.10.0
- **[Week of September 7](./previous-work/2026/2026-09-07.md)** — elvenspeak stub-fleet router and Dockerfile publish gate · rich-js JSON and print fidelity · lit rename and plugin cleanup · memento 0.6–0.7 ceiling collapse
- **[Week of August 17](./previous-work/2026/2026-08-17.md)** — *in progress*

[Full archive →](./previous-work/)

<!-- PREVIOUS-WORK:END -->

---

## Selected Projects

<!-- SELECTED-PROJECTS:START -->
<table>
<tr>
<td width="50%" valign="top">

### [low-talker](https://github.com/promptctl/low-talker)
**Swift · 2★**

Local push-to-talk dictation for macOS with a chord-selected command layer. 228 commits over the past 90 days, 18 this week as builds 11 and 12 (v0.1.0-alpha.11 and alpha.12) cut. A held steering key's auto-repeat now takes the verdict of the press it repeats, unasked — a held Option+Escape's repeats no longer reach the field once the box is put away ([#316](https://github.com/promptctl/low-talker/pull/316)); words continued from where the input method's last commit left the caret are fitted after that commit's words, so iTerm2 no longer runs them together or capitalizes mid-sentence ([#317](https://github.com/promptctl/low-talker/pull/317)); a release runs the suite CI runs on the tree it builds before signing anything, and refuses a commit whose tests fail or that the suite leaves changed ([#315](https://github.com/promptctl/low-talker/pull/315)).

### [cc-dump-web](https://github.com/promptctl/cc-dump-web)
**TypeScript**

A web UI for inspecting Claude Code sessions: an HTTP proxy that forwards the agent's traffic unchanged while recording every exchange, served through a conversation view with search, diffs, logs and a minimap. 213 commits over the past 90 days (the repo started November 12), 43 this week. Every JSON document the app receives is read by one reader family, a refused field costs what its declaration holds it to ([#60](https://github.com/promptctl/cc-dump-web/pull/60)); a stored view or settings item is read field by field by persist's own storage — what this build cannot read is dropped and named ([#53](https://github.com/promptctl/cc-dump-web/pull/53)); the UI's own decisions about the reader's view are events, seen beside the parts' logs ([#46](https://github.com/promptctl/cc-dump-web/pull/46)); a unit of work's event is written at its first ending, with its first failure, by one writer ([#39](https://github.com/promptctl/cc-dump-web/pull/39), [#41](https://github.com/promptctl/cc-dump-web/pull/41)); every route answers through one layer — one access rule, one refusal shape, one wire ([#36](https://github.com/promptctl/cc-dump-web/pull/36)); each subagent's nest stands under its call in the history the column lists, by wire ids ([#31](https://github.com/promptctl/cc-dump-web/pull/31)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — fork of `@owloops/claude-powerline` with CLI override flags so the entire config can live in `settings.json`. 145 commits over the past 90 days, 96 this week as Proposal 3 (host owns the world, renderers answer it) continued landing. Named renderers route through one shared host ([#864](https://github.com/promptctl/cc-candybar/pull/864)) and click actions route to their drawing renderer ([#875](https://github.com/promptctl/cc-candybar/pull/875)); each session environment is shared across statusline ticks ([#872](https://github.com/promptctl/cc-candybar/pull/872)) and checkout filesystem observations are shared ([#870](https://github.com/promptctl/cc-candybar/pull/870)); live sessions record and replay through the shared host ([#913](https://github.com/promptctl/cc-candybar/pull/913)); a still frame touches only the view it draws ([#933](https://github.com/promptctl/cc-candybar/pull/933)); today's release-plumbing day moved the Publish job to npm trusted publishing ([#943](https://github.com/promptctl/cc-candybar/pull/943)) with the Release workflow's checks running as parallel jobs under one Test gate inside 5 minutes ([#938](https://github.com/promptctl/cc-candybar/pull/938)).

</td>
<td width="50%" valign="top">

### [lit2](https://github.com/promptctl/lit2)
**Go**

A Go rewrite of lit, the agent-native issue tracker over git. 96 commits over the past 90 days, 48 this week as the bootstrap arc through members, workspace, views, columns, evaluate and config/verbs/field landed. `evaluate` is the layer that computes what needs the clock or the configuration, handed `now` and reading no clock itself — a read is `evaluate(fold(events), config, now)` and a write is judged against it. Every row of the default table names the verbs that write it or why none does, never both or neither. Bare `lit2` is `get /` — the tree with each node's stage, lanes in rank order, next the first lane's head. `set x/status` moves along next, one gate judges every arrival's edge and its exit and entry lists against the state the command leaves.

### [memento](https://github.com/promptctl/memento)
**Python · MIT**

Agent-native workflow tooling for Claude Code — next-ticket pickup, the address-PR-review loop, and the cross-session handoff that carries a goal across a context reset. 76 commits over the past 90 days, 4 this week as 0.15.0 cut ([#81](https://github.com/promptctl/memento/pull/81)) and `finalize-session` was taught to hand off with `/compact` again on `--reset compact` ([#80](https://github.com/promptctl/memento/pull/80)). Earlier in the cycle the journal arc landed — one append-only file of wake, note and close entries that follows a session's chain of handoffs back by position in that file ([#57](https://github.com/promptctl/memento/pull/57)) — the remote-control transport reworked so `finalize-session` hands off through the server's event log ([#64](https://github.com/promptctl/memento/pull/64)), and a hook's run given one owner via `ceiling_log.run` ([#66](https://github.com/promptctl/memento/pull/66)).

### [cc-hands](https://github.com/promptctl/cc-hands)
**Python**

Conversational Claude Code — a voice-driven desk pair where hands speak, listen, cancel its own echo and route a user's turn to a brain. 69 commits over the past 90 days, 48 this week. DTLN-aec is the desk's one canceller — 0 of hands' words leaked, 1 of 101 of a person's lost ([#492](https://github.com/promptctl/cc-hands/pull/492)); a voice-opened window cuts hands off on the words heard in it, with no voiceprint deciding whose they are ([#497](https://github.com/promptctl/cc-hands/pull/497)); the stand-in daemon runs on a home the start's preflight passes with its pinned claude carried across each restart ([#549](https://github.com/promptctl/cc-hands/pull/549)); the brain takes every request on its proxy and every hook posted to it, whatever session it names ([#543](https://github.com/promptctl/cc-hands/pull/543)); today's four wire fixes — a side question after a main turn forks from that turn ([#555](https://github.com/promptctl/cc-hands/pull/555)), a headerless main turn reads as a main turn ([#553](https://github.com/promptctl/cc-hands/pull/553)).

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
