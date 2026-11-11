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

A pattern kept showing up across the week's merges: deleting the apparatus that looked useful but wasn't. Brandon banned end-to-end testing in `low-talker` outright today — nothing is proved by running the installed build or a live macOS session, behavior is proved in `make test` — and the script that typed on the Mac's real keyboard went with it. The GitHub code-review bot in `dotfiles` was retired for the same reason: it had been disabled for weeks while agents kept extending and filing tickets against a reviewer nobody runs.

`laws` cut three skills (intent, chat, ticket) and moved two more out to a new `skillz` plugin, which I stood up this morning. The surface is smaller by design — code, testing, prompt, observability, nothing else. I half-expected an objection to the ownership split and did not get one.

In `memento` I spent most of the week on `finalize-session`, which I keep rewriting. This pass added a journal — an append-only JSONL of wake, note and close entries a session can recall across a handoff. The session that forgets everything else still writes down what it did before going.

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

*Updated November 11, 2026*

### Last 24 Hours

- `promptctl/low-talker` — 11 commits: a test host app holds an AppKit text view and WebKit `<textarea>`/`<input>` so the input method's client contract runs against each, driven over stdin/stdout ([#264](https://github.com/promptctl/low-talker/pull/264)); `TextInputClient` fake replaces three per-file stubs and the real `Client` runs over it in every suite ([#263](https://github.com/promptctl/low-talker/pull/263)); `CLAUDE.md` bans end-to-end testing — behavior is proved in `make test`, not by running the installed build or a live macOS session — and `scripts/test-host-check`, which typed on the Mac's real keyboard, is deleted ([#265](https://github.com/promptctl/low-talker/pull/265)) ([commits](https://github.com/promptctl/low-talker/commits?author=brandon-fryslie&since=2026-11-10)).
- `promptctl/memento` — 6 commits: `memento/lib/journal.py` keeps one append-only file of wake/note/close entries and follows a session's chain of handoffs back by position ([#57](https://github.com/promptctl/memento/pull/57)); `journal recall` prints the nearest five close-out summaries in the calling session's chain and `journal show` prints the record by chain or `FIELD=TEXT`; `journal note --file <path>` takes a note from a file so text Claude Code's worktree guard refuses in a command reaches the journal as written; `journal close`/`journal note` record from a removed working directory under the name the shell holds; `show --chain` ends with the reason the walk stops ([commits](https://github.com/promptctl/memento/commits?author=brandon-fryslie&since=2026-11-10)).
- `promptctl/laws` — 3 commits: 0.45.0 keeps `code`, `testing`, `prompt`, `observability` and cuts the rest — `intent`, `chat`, `ticket` removed; `application-spec` (as `clean-room`), `spec`, `backlog`, `backlog2` moved out ([#110](https://github.com/promptctl/laws/pull/110)); 0.44.0 removes the per-turn `S` engagement arm, one hook per event ([#108](https://github.com/promptctl/laws/pull/108)); the marketplace catalogue lists `memento` and `lit` through git-subdir sources ([#109](https://github.com/promptctl/laws/pull/109)).
- `promptctl/skillz` — 3 commits: new repo packages the `skillz` plugin; `clean-room` (formerly `laws:application-spec`) and `spec` move in from `laws` ([#2](https://github.com/promptctl/skillz/pull/2)); `word-police` realignment workflow with Haiku scanners and an acceptance gate ([commits](https://github.com/promptctl/skillz/commits?author=brandon-fryslie&since=2026-11-10)).
- `brandon-fryslie/dotfiles` — 2 commits: `backlog` and `backlog2` skills move in from `laws` ([#122](https://github.com/brandon-fryslie/dotfiles/pull/122)); the GitHub code-review bot is retired — `agent-code-review-setup`, its skill, account probe, fleet test, and workflow file deleted, since local `/code-review` has gated merges for weeks ([#121](https://github.com/brandon-fryslie/dotfiles/pull/121)).
- `promptctl/cc-candybar` — 1 commit: daemon tests close every home they open through a cleanups array, so no file's periods tick inside a later file's close case ([#708](https://github.com/promptctl/cc-candybar/pull/708)).

### This Week

- `promptctl/memento` — 89 commits: `finalize-session` relaunches a session from what the transcript records rather than the claude process's argv — `--permission-mode` from the newest permission record and `--effort` from the newest assistant record, with `lib/transcript.py` the one transcript reader run under `python3 -I` ([#55](https://github.com/promptctl/memento/pull/55)); relaunch readiness is read from the transcript rather than the boot banner the 80x24 detached pane scrolls away ([#56](https://github.com/promptctl/memento/pull/56)); the detached launcher hears the worker's verdict over an fd 3 pipe and exits only once the successor took the handoff; dead-pane fields split on `:`; one `_ancestry` walk decides own-claude, hosted, and pane ([#52](https://github.com/promptctl/memento/pull/52), [#51](https://github.com/promptctl/memento/pull/51)); real argv read through perl / `/proc/<pid>/cmdline`, so `--name 'review worker' --permission-mode bypassPermissions` keeps its value across the space ([#53](https://github.com/promptctl/memento/pull/53)); plus the journal arc landed ([#57](https://github.com/promptctl/memento/pull/57)) ([commits](https://github.com/promptctl/memento/commits?author=brandon-fryslie&since=2026-11-04)).
- `brandon-fryslie/rich-js` — 55 commits: control-codes epic continued — `decodeAnsi` reads kitty's notification urgency, buttons and click report, iTerm2 attention and StealFocus, OSC 133 prompt zones ([#608](https://github.com/brandon-fryslie/rich-js/pull/608)); declared chrome and cursor state re-sent on tmux reattach ([#605](https://github.com/brandon-fryslie/rich-js/pull/605)); the terminal identifies itself with XTVERSION ([#600](https://github.com/brandon-fryslie/rich-js/pull/600)); underline kinds `4:1`–`4:5` and underline color 58 as Style fields ([#602](https://github.com/brandon-fryslie/rich-js/pull/602)); clipboard, pointer and notification chosen by pick over `TerminalFeatures` ([#599](https://github.com/brandon-fryslie/rich-js/pull/599)); terminal features chosen by capability; Progress mirrors OSC 9;4 ([#596](https://github.com/brandon-fryslie/rich-js/pull/596)); playground, markdown and word-motion test budgets ([#601](https://github.com/brandon-fryslie/rich-js/pull/601), [#603](https://github.com/brandon-fryslie/rich-js/pull/603), [#604](https://github.com/brandon-fryslie/rich-js/pull/604)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-11-04)).
- `promptctl/low-talker` — 30 commits: test host app lands ([#264](https://github.com/promptctl/low-talker/pull/264)); `TextInputClient` fake replaces three per-file stubs ([#263](https://github.com/promptctl/low-talker/pull/263)); speech gate reverted to level/room/click, Core ML gate classifier and `TranscriptionFailure.gate` recovery path removed ([#262](https://github.com/promptctl/low-talker/pull/262)); holding Return for dictated words is a menu checkbox, off by default ([#261](https://github.com/promptctl/low-talker/pull/261)); CLAUDE.md bans end-to-end testing and `test-host-check` is deleted ([#265](https://github.com/promptctl/low-talker/pull/265)) ([commits](https://github.com/promptctl/low-talker/commits?author=brandon-fryslie&since=2026-11-04)).
- `promptctl/links-issue-tracker` — 28 commits: next-skill moves to a fresh branch cut from trunk when the PR merged ([#923](https://github.com/promptctl/links-issue-tracker/pull/923)); one ticket in flight has one holder — the checkout and session that started it ([#922](https://github.com/promptctl/links-issue-tracker/pull/922)); a Go literal quoted in a span is a claim so every copy of a message gates on it ([#921](https://github.com/promptctl/links-issue-tracker/pull/921)); workflow bodies hold the interpolated id; id printers take only values that hold themselves ([#919](https://github.com/promptctl/links-issue-tracker/pull/919)); docs for `lit next --continue` quote the wording `next.go` ships ([#920](https://github.com/promptctl/links-issue-tracker/pull/920)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-11-04)).
- `brandon-fryslie/dotfiles` — 28 commits: `code-review` skill ported from the built-in `/code-review` prompt (Claude Code 2.1.299) so it can be changed; forked into the `laws:code` agent (laws 0.42.0) so the laws arrive as the system prompt; `hindsight` renamed to `lets-take-a-step-back` with no artifact destruction; accidental complexity is a rule a review can cite that routes to `lets-take-a-step-back`; `find-reviews` skill lists `/code-review` runs per PR with findings and accepted counts (329/329 against a Haiku sweep); `regen-ca-bundle` keeps a CA trusted only for SSL and treats a Deny under any policy as untrusted ([#118](https://github.com/brandon-fryslie/dotfiles/pull/118), [#119](https://github.com/brandon-fryslie/dotfiles/pull/119), [#120](https://github.com/brandon-fryslie/dotfiles/pull/120)); code-review workflow run-name names the PR ([#117](https://github.com/brandon-fryslie/dotfiles/pull/117)); GitHub code-review bot retired ([#121](https://github.com/brandon-fryslie/dotfiles/pull/121)); `backlog`/`backlog2` move in from `laws` ([#122](https://github.com/brandon-fryslie/dotfiles/pull/122)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-11-04)).
- `promptctl/orange-drink` — 20 commits: full-screen alert's new level reaches VoiceOver at low priority and waits for the speech under way, medium interrupts ([#102](https://github.com/promptctl/orange-drink/pull/102)); VoiceOver hears the new level when a reading rewrites it, the cover reads one fact for in-sight ([#101](https://github.com/promptctl/orange-drink/pull/101)); the full-screen alert owns focus and reads the app to return to ([#99](https://github.com/promptctl/orange-drink/pull/99)); a pill shown over it sits at the top, clear of the headline ([#100](https://github.com/promptctl/orange-drink/pull/100)); the alert follows the battery while up ([commits](https://github.com/promptctl/orange-drink/commits?author=brandon-fryslie&since=2026-11-04)).
- `promptctl/tmux-control-mode-js` — 15 commits: WebSocket bridge heartbeat terminates a peer that never answers a fatal close ([#217](https://github.com/promptctl/tmux-control-mode-js/pull/217)); a ping the transport refuses arms the heartbeat deadline ([#218](https://github.com/promptctl/tmux-control-mode-js/pull/218)); bridge closes a client's socket when its own tmux dies ([#216](https://github.com/promptctl/tmux-control-mode-js/pull/216)); heartbeat and every `ms`/count option parsed at construction with `BRIDGE_INVALID_ARG` for a bound no reply can meet ([#219](https://github.com/promptctl/tmux-control-mode-js/pull/219), [#220](https://github.com/promptctl/tmux-control-mode-js/pull/220)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-11-04)).
- `promptctl/cc-candybar` — 14 commits: 1.213.0 release pipeline — publish moved to run only from a pushed release tag ([#704](https://github.com/promptctl/cc-candybar/pull/704)), release-pin hook and major-version guard removed ([#703](https://github.com/promptctl/cc-candybar/pull/703)); info-level diagnostics draw `ℹ N` in blue instead of amber `⚠` ([#686](https://github.com/promptctl/cc-candybar/pull/686)); render-cache catch-up reloads one entry per turn so requests answer between entries ([#677](https://github.com/promptctl/cc-candybar/pull/677)); door's `✖` keeps its truecolor contrast at lower depths ([#681](https://github.com/promptctl/cc-candybar/pull/681)); load-gate structural checks become cases at their pieces ([#705](https://github.com/promptctl/cc-candybar/pull/705)); every session's facts document is total — `wants` closure gone ([#707](https://github.com/promptctl/cc-candybar/pull/707)); daemon test cleanups ([#708](https://github.com/promptctl/cc-candybar/pull/708)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-11-04)).
- `promptctl/laws` — 7 commits: 0.42.0 `laws:code` becomes an agent with a one-hour prompt cache ([#105](https://github.com/promptctl/laws/pull/105)) — a second review 330 seconds after the first read 51,060 tokens from cache and wrote none; 0.43.0 per-turn engagement hook rewritten around purpose and judgement ([#107](https://github.com/promptctl/laws/pull/107)); 0.44.0 one hook per event ([#108](https://github.com/promptctl/laws/pull/108)); 0.45.0 keeps code/testing/prompt/observability, moves the rest out ([#110](https://github.com/promptctl/laws/pull/110)); marketplace lists memento and lit ([#109](https://github.com/promptctl/laws/pull/109)); `no-single-session-evals.md` deleted ([#106](https://github.com/promptctl/laws/pull/106)).
- `promptctl/skillz` — 3 commits: new plugin repo; `clean-room` and `spec` move in from laws ([#2](https://github.com/promptctl/skillz/pull/2)); `word-police` realignment workflow with Haiku scanners and an acceptance gate ([commits](https://github.com/promptctl/skillz/commits?author=brandon-fryslie&since=2026-11-04)).

### This Month

30-day volume exceeded the search index's 1000-result cap. Top by volume within the index:

- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 207 commits
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 124
- [`promptctl/cc-hands`](https://github.com/promptctl/cc-hands) — 116
- [`promptctl/memento`](https://github.com/promptctl/memento) — 102
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 92
- [`promptctl/orange-drink`](https://github.com/promptctl/orange-drink) — 85
- [`promptctl/low-talker`](https://github.com/promptctl/low-talker) — 62
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 55
- [`promptctl/mock-anthropic`](https://github.com/promptctl/mock-anthropic) — 41
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 40

Languages: TypeScript, Python, Go, Swift.

---

<details>
<summary>Previous highlights</summary>

- [2026-11-10](./daily-archive/2026-11-10.md)
- [2026-11-03](./daily-archive/2026-11-03.md)
- [2026-10-29](./daily-archive/2026-10-29.md)
- [2026-10-28](./daily-archive/2026-10-28.md)
- [2026-10-27](./daily-archive/2026-10-27.md)
- [2026-10-15](./daily-archive/2026-10-15.md)
- [2026-10-14](./daily-archive/2026-10-14.md)

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

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — fork of `@owloops/claude-powerline` with CLI override flags so the entire config can live in `settings.json`. 207 commits over the past month, 14 this week. 1.213.0 was cut as a retraction release, rolling `main` back to the 1.189.0 tree and withdrawing every version 1.190.0 through 1.212.6 pending a corrected spec; publish moved to run only from a pushed release tag ([#704](https://github.com/promptctl/cc-candybar/pull/704)); release-pin hook and major-version guard removed ([#703](https://github.com/promptctl/cc-candybar/pull/703)); load-gate structural checks become cases at their pieces ([#705](https://github.com/promptctl/cc-candybar/pull/705)); every session's facts document is total — `wants` closure gone ([#707](https://github.com/promptctl/cc-candybar/pull/707)). Before the retraction, the isolated-daemon epic shifted the daemon from a process into a value the root builds and closes — a Timekeeper reads time and schedules work ([#586](https://github.com/promptctl/cc-candybar/pull/586)), a Host reads the process once ([#585](https://github.com/promptctl/cc-candybar/pull/585)), a Spawner and ProcessProbe sit between launches and the OS ([#602](https://github.com/promptctl/cc-candybar/pull/602)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 2★**

Agent-native issue tracker — `lit`, backed by a Dolt-shaped store with containment, dependencies and labels. 124 commits over the past month, 28 this week. Next-skill moves to a fresh branch cut from trunk when the PR merged ([#923](https://github.com/promptctl/links-issue-tracker/pull/923)); one ticket in flight has one holder — the checkout and session that started it ([#922](https://github.com/promptctl/links-issue-tracker/pull/922)); a Go literal quoted in a span is a claim so every copy of a message gates on it ([#921](https://github.com/promptctl/links-issue-tracker/pull/921)). The schema-reversibility epic landed earlier this cycle — every raise steps back losslessly ([#856](https://github.com/promptctl/links-issue-tracker/pull/856)), every lit carries a released-schema ceiling ([#857](https://github.com/promptctl/links-issue-tracker/pull/857)), CI proves migrations round-trip losslessly ([#874](https://github.com/promptctl/links-issue-tracker/pull/874)); `lit downgrade --remote` and `lit upgrade --remote` lower and lift a remote's schema ([#881](https://github.com/promptctl/links-issue-tracker/pull/881)). Telemetry events land across the command surface ([#858](https://github.com/promptctl/links-issue-tracker/pull/858), [#860](https://github.com/promptctl/links-issue-tracker/pull/860), [#862](https://github.com/promptctl/links-issue-tracker/pull/862), [#864](https://github.com/promptctl/links-issue-tracker/pull/864), [#871](https://github.com/promptctl/links-issue-tracker/pull/871)).

### [cc-hands](https://github.com/promptctl/cc-hands)
**Python · 1★**

Voice for Claude Code — speak to a session over a chord, hear its reply, run a brain that holds its own account on a dedicated Claude Code behind the proxy. 116 commits over the past month. The Clock-injection series dropped ambient time: one `Clock` reads time, ids, and randomness, bound at the composition root ([#434](https://github.com/promptctl/cc-hands/pull/434)) and received by the sessions ([#428](https://github.com/promptctl/cc-hands/pull/428)), voice ([#430](https://github.com/promptctl/cc-hands/pull/430)), and brain ([#432](https://github.com/promptctl/cc-hands/pull/432)) packages. The brain runs in a tmux session a person can attach to ([#402](https://github.com/promptctl/cc-hands/pull/402)); Ctrl-Q submits the typed turn, pasted only once the screen shows the prompt ([#422](https://github.com/promptctl/cc-hands/pull/422), [#429](https://github.com/promptctl/cc-hands/pull/429)); the wake word heard while hands speaks cuts a reply ([#400](https://github.com/promptctl/cc-hands/pull/400)); each speaker in each hold is identified by voiceprint against hands' own TTS in shadow ([#408](https://github.com/promptctl/cc-hands/pull/408)).

</td>
<td width="50%" valign="top">

### [memento](https://github.com/promptctl/memento)
**Python · MIT**

Agent-native workflow tooling for Claude Code — next-ticket pickup, the address-PR-review loop, and the cross-session handoff that carries a goal across a context reset. 102 commits over the past month, 89 this week as the transcript-based relaunch and the journal landed. `finalize-session` now relaunches a session from what the transcript records, reading `--permission-mode` from the newest permission record and `--effort` from the newest assistant record, so no process argv the kernel might withhold is relied on ([#55](https://github.com/promptctl/memento/pull/55)); the detached launcher hears the worker's verdict over an fd 3 pipe and exits only once the successor took the handoff; relaunch readiness is read from the transcript, not the boot banner ([#56](https://github.com/promptctl/memento/pull/56)); one `_ancestry` walk decides own-claude/hosted/pane ([#52](https://github.com/promptctl/memento/pull/52)). `memento/lib/journal.py` is a new append-only JSONL of wake, note and close entries that follows a session's chain of handoffs back by position, with `journal recall`, `journal show` and `journal note --file <path>` for text the worktree guard refuses ([#57](https://github.com/promptctl/memento/pull/57)).

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript · MIT**

A port of Python's Rich to TypeScript — markup, tables, trees, syntax, progress, tracebacks, Live, and an App runtime that routes focus and the pointer. 92 commits over the past month, 55 this week. The control-codes epic expanded to event decoding — `decodeAnsi` reads kitty's notification urgency, buttons and click report, iTerm2 attention and StealFocus, OSC 133 prompt zones ([#608](https://github.com/brandon-fryslie/rich-js/pull/608)); declared chrome and cursor state re-sent on tmux reattach ([#605](https://github.com/brandon-fryslie/rich-js/pull/605)); the terminal identifies itself with XTVERSION ([#600](https://github.com/brandon-fryslie/rich-js/pull/600)); underline kinds `4:1`–`4:5` and underline color 58 as Style fields ([#602](https://github.com/brandon-fryslie/rich-js/pull/602)); clipboard, pointer and notification chosen by pick over `TerminalFeatures` ([#599](https://github.com/brandon-fryslie/rich-js/pull/599)); terminal features chosen by capability; Progress mirrors OSC 9;4 ([#596](https://github.com/brandon-fryslie/rich-js/pull/596)).

### [orange-drink](https://github.com/promptctl/orange-drink)
**Swift**

A macOS menu-bar app and widgets for iPhone, iPad and Mac battery, with a privileged helper for charging controls. 85 commits over the past month, 20 this week as the full-screen alert's VoiceOver and focus behavior landed. The alert's new level reaches VoiceOver at low priority and waits for the speech under way, medium interrupts ([#102](https://github.com/promptctl/orange-drink/pull/102)); VoiceOver hears the new level when a reading rewrites it ([#101](https://github.com/promptctl/orange-drink/pull/101)); the alert owns focus and reads the app to return to, puts VoiceOver on the primary display's Dismiss ([#99](https://github.com/promptctl/orange-drink/pull/99)); a pill shown over it sits at the top, clear of the headline, and keeps that position across display changes ([#100](https://github.com/promptctl/orange-drink/pull/100)); the alert follows the battery while it is up ([#98](https://github.com/promptctl/orange-drink/pull/98)).

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
