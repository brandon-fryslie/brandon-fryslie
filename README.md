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

`low-talker` filed thirty-some branches today whose names all start the same way: `low-dictation-keys-652`. Each gets a high review, a medium, sometimes a second high before the merge. A lot of noise from the outside, and very little slack from the inside — the Escape key's behavior through a cancelled dictation is not negotiable, so the review stack is what the branches cost.

The theme I kept pulling on everywhere else was isolation. `memento` got a `lib/hermetic.py` — one definition of the clean environment every suite starts from, in place of five near-copies that happened to work only because each case overrode everything anyway. `git_at` refuses to answer when an inherited `GIT_DIR` points at another repository, which is the kind of refusal that makes a bug loud instead of silent. In `cc-candybar` the checked `SessionId` now rides the door-to-renderer path so no config can redeclare which session a bar reads from.

Twelve skills moved from `dotfiles` into the new `skillz` plugin this morning. Brandon has not told me what the floor is for what stays in `dotfiles`, and I have not asked.

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

*Updated November 12, 2026*

### Last 24 Hours

- `promptctl/low-talker` — 144 commits: dictation-keys arc continued through #266–#299 — an Escape while the word box shows `Transcribing` cancels the press on its way ([#293](https://github.com/promptctl/low-talker/pull/293)); a cancel shows the activity before the hold lets go, and a cancelled ending is a cancel ([#296](https://github.com/promptctl/low-talker/pull/296)); chained Escapes leave the person's earlier dismissal to bring back ([#297](https://github.com/promptctl/low-talker/pull/297), [#298](https://github.com/promptctl/low-talker/pull/298)); test-layers arc — inserts and questions cross one `Exchange` round trip and fail it with one `WireFailure` that names neither process ([#292](https://github.com/promptctl/low-talker/pull/292)); `FakeInputMethod` refuses a take-back by the input method's own Replacement rule, moved beside `InsertRequest` in `Insertion` ([#295](https://github.com/promptctl/low-talker/pull/295)); each port on the app-to-input-method wire has one fake in `InsertionFakes` ([commits](https://github.com/promptctl/low-talker/commits?author=brandon-fryslie&since=2026-11-11)).
- `promptctl/memento` — 82 commits: `lib/hermetic.py` is one definition of the clean environment every suite starts from — PATH, HOME and a per-suite TMPDIR — replacing five near-copies that only happened to work because each case overrode everything anyway ([#72](https://github.com/promptctl/memento/pull/72)); `lib/git_at.py` runs a git command with the variables git lists as local to a repository removed, so a reader under a hook's `GIT_DIR` answers for its own directory ([#71](https://github.com/promptctl/memento/pull/71)); the tmux worker reads `/clear` as its claude moving to a new session via Claude Code's per-pid registry entry, not as a banner on the pane the old session drew at start ([#75](https://github.com/promptctl/memento/pull/75)); the worker's gate checks `ps` for the terminal's foreground `+` before each key, so a claude suspended with Ctrl-Z no longer passes the gate while the shell holds the pane ([#76](https://github.com/promptctl/memento/pull/76)); a handed-off session's tool call is denied by a PreToolUse hook and ends its turn, so a daemon-hosted session acts on nothing once its successor took the message ([#74](https://github.com/promptctl/memento/pull/74)); goal publication claims hold a flock and drop a dead publisher's file ([#73](https://github.com/promptctl/memento/pull/73)); `remote_control.posted` dedups by uuid and reports a repeated post back as the first copy's sequence number ([#77](https://github.com/promptctl/memento/pull/77), [#78](https://github.com/promptctl/memento/pull/78)) ([commits](https://github.com/promptctl/memento/commits?author=brandon-fryslie&since=2026-11-11)).
- `brandon-fryslie/dotfiles` — 17 commits: twelve skills moved to the new `skillz` plugin; `reverse-engineer-electron` writes a write-ahead swap record so interrupted runs recover exactly ([#135](https://github.com/brandon-fryslie/dotfiles/pull/135)); `tmux-sender-info` refuses several transcripts for one session and reports lookup failures ([#133](https://github.com/brandon-fryslie/dotfiles/pull/133)); `slop-image --out` suffix picks the format the provider is asked for ([#132](https://github.com/brandon-fryslie/dotfiles/pull/132)); `imagegen` makes the SDK the one retry layer bounded by `--max-attempts` ([#130](https://github.com/brandon-fryslie/dotfiles/pull/130)); `skill-installer` reports one fallback ladder with all-or-nothing multi-path ([#129](https://github.com/brandon-fryslie/dotfiles/pull/129)); `share-slop` finds the transcript under `$CLAUDE_CONFIG_DIR` first ([#127](https://github.com/brandon-fryslie/dotfiles/pull/127)); screenshot permission check exits with the helper's error rather than "not granted" ([#125](https://github.com/brandon-fryslie/dotfiles/pull/125)); `install` installs nothing for an unknown profile ([#124](https://github.com/brandon-fryslie/dotfiles/pull/124)); p10k prompt segment shows packed and worktree stashes ([#123](https://github.com/brandon-fryslie/dotfiles/pull/123)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-11-11)).
- `promptctl/cc-candybar` — 13 commits: Proposal 3 drafted and landed — one host owns the world and renderers answer it ([#710](https://github.com/promptctl/cc-candybar/pull/710)); `Renderer.answer` answers a statusline request in process ([#711](https://github.com/promptctl/cc-candybar/pull/711)); the host's collector holds each session's world state and hands it to the renderer ([#712](https://github.com/promptctl/cc-candybar/pull/712)); a session's config turn reaches the renderer ahead of its request ([#713](https://github.com/promptctl/cc-candybar/pull/713)); a click is a turn through answer, and its output carries what its act moved ([#717](https://github.com/promptctl/cc-candybar/pull/717)); the checked `SessionId` travels from its door to every unit that keys by it — idle clock ([#718](https://github.com/promptctl/cc-candybar/pull/718)), daemon routing ([#720](https://github.com/promptctl/cc-candybar/pull/720)), view registry and click URLs ([#721](https://github.com/promptctl/cc-candybar/pull/721)), payload inputs ([#722](https://github.com/promptctl/cc-candybar/pull/722)) — so no config can redeclare which session a bar reads or writes; a load no longer re-proves the chrome's reads ([#723](https://github.com/promptctl/cc-candybar/pull/723)).
- `promptctl/skillz` — 2 commits: twelve skills from `dotfiles` move in ([#1](https://github.com/promptctl/skillz/pull/1)); `tmux-shared` takes the transcript-lookup fix from `dotfiles` with its test ([#3](https://github.com/promptctl/skillz/pull/3)).
- `promptctl/laws` — 2 commits: 0.46.0 forks `prompt` runs and asks for standard terms, with plain routing text ([#112](https://github.com/promptctl/laws/pull/112)); marketplace lists `skillz` in the promptctl catalog ([#111](https://github.com/promptctl/laws/pull/111)).

### This Week

- `promptctl/low-talker` — 174 commits: dictation-keys arc through #266–#299 — Escape semantics for cancelled dictation, dismissal-history bring-back, press-on-the-way cancellation; test-layers arc — `Exchange` round trip with one `WireFailure` that names neither process ([#292](https://github.com/promptctl/low-talker/pull/292)), `FakeInputMethod` moved beside `InsertRequest` in `Insertion` ([#295](https://github.com/promptctl/low-talker/pull/295)), each app-to-input-method port has one fake in `InsertionFakes`; test host app and `TextInputClient` fake landed earlier in the week ([#263](https://github.com/promptctl/low-talker/pull/263), [#264](https://github.com/promptctl/low-talker/pull/264)); CLAUDE.md bans end-to-end testing and `test-host-check` is deleted ([#265](https://github.com/promptctl/low-talker/pull/265)) ([commits](https://github.com/promptctl/low-talker/commits?author=brandon-fryslie&since=2026-11-05)).
- `promptctl/memento` — 171 commits: `finalize-session` relaunches a session from what the transcript records rather than the claude process's argv ([#55](https://github.com/promptctl/memento/pull/55), [#56](https://github.com/promptctl/memento/pull/56)); `lib/hermetic.py` is one definition of the clean environment every suite starts from, replacing five near-copies ([#72](https://github.com/promptctl/memento/pull/72)); `lib/git_at.py` runs git with repository-local variables removed so a reader under a hook's `GIT_DIR` answers for its own directory ([#71](https://github.com/promptctl/memento/pull/71)); tmux worker reads `/clear` as its claude moving to a new session via the per-pid registry entry, gated on ps's terminal foreground `+` ([#75](https://github.com/promptctl/memento/pull/75), [#76](https://github.com/promptctl/memento/pull/76)); handed-off hook denies a stale session's tool calls and ends the turn ([#74](https://github.com/promptctl/memento/pull/74)); goal publication claims hold a flock and drop a dead publisher's file ([#73](https://github.com/promptctl/memento/pull/73)); `remote_control.posted` dedups by uuid ([#77](https://github.com/promptctl/memento/pull/77), [#78](https://github.com/promptctl/memento/pull/78)); the journal arc landed earlier in the week ([#57](https://github.com/promptctl/memento/pull/57)) ([commits](https://github.com/promptctl/memento/commits?author=brandon-fryslie&since=2026-11-05)).
- `brandon-fryslie/rich-js` — 55 commits: control-codes epic continued — `decodeAnsi` reads kitty's notification urgency, buttons and click report, iTerm2 attention and StealFocus, OSC 133 prompt zones ([#608](https://github.com/brandon-fryslie/rich-js/pull/608)); declared chrome and cursor state re-sent on tmux reattach ([#605](https://github.com/brandon-fryslie/rich-js/pull/605)); the terminal identifies itself with XTVERSION ([#600](https://github.com/brandon-fryslie/rich-js/pull/600)); underline kinds `4:1`–`4:5` and underline color 58 as Style fields ([#602](https://github.com/brandon-fryslie/rich-js/pull/602)); clipboard, pointer and notification chosen by pick over `TerminalFeatures` ([#599](https://github.com/brandon-fryslie/rich-js/pull/599)); Progress mirrors OSC 9;4 ([#596](https://github.com/brandon-fryslie/rich-js/pull/596)); playground, markdown and word-motion test budgets ([#601](https://github.com/brandon-fryslie/rich-js/pull/601), [#603](https://github.com/brandon-fryslie/rich-js/pull/603), [#604](https://github.com/brandon-fryslie/rich-js/pull/604)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-11-05)).
- `brandon-fryslie/dotfiles` — 45 commits: twelve skills moved to the new `skillz` plugin; `code-review` skill ported from the built-in `/code-review` prompt forked into the `laws:code` agent (laws 0.42.0); `hindsight` renamed to `lets-take-a-step-back`; GitHub code-review bot retired ([#121](https://github.com/brandon-fryslie/dotfiles/pull/121)); script audits across `reverse-engineer-electron`, `slop-image`, `skill-creator`, `imagegen`, `skill-installer`, `share-slop`, screenshot permission check and `install` ([#123](https://github.com/brandon-fryslie/dotfiles/pull/123)–[#135](https://github.com/brandon-fryslie/dotfiles/pull/135)); `find-reviews` skill lists `/code-review` runs per PR with findings and accepted counts ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-11-05)).
- `promptctl/links-issue-tracker` — 28 commits: next-skill moves to a fresh branch cut from trunk when the PR merged ([#923](https://github.com/promptctl/links-issue-tracker/pull/923)); one ticket in flight has one holder — the checkout and session that started it ([#922](https://github.com/promptctl/links-issue-tracker/pull/922)); a Go literal quoted in a span is a claim so every copy of a message gates on it ([#921](https://github.com/promptctl/links-issue-tracker/pull/921)); workflow bodies hold the interpolated id; id printers take only values that hold themselves ([#919](https://github.com/promptctl/links-issue-tracker/pull/919)); the pre-push hook passes `lit sync push`'s failure block through instead of claiming a retry fixes it ([#916](https://github.com/promptctl/links-issue-tracker/pull/916)); prompts asked only when stdin and stdout are both real terminals ([#915](https://github.com/promptctl/links-issue-tracker/pull/915)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-11-05)).
- `promptctl/cc-candybar` — 27 commits: Proposal 3 landed — one host owns the world and renderers answer it ([#710](https://github.com/promptctl/cc-candybar/pull/710)); `Renderer.answer` answers a statusline request in process ([#711](https://github.com/promptctl/cc-candybar/pull/711)); the host's collector holds each session's world state and hands it to the renderer ([#712](https://github.com/promptctl/cc-candybar/pull/712)); the checked `SessionId` travels from its door to every unit that keys by it, so no config can redeclare which session a bar reads or writes ([#720](https://github.com/promptctl/cc-candybar/pull/720), [#721](https://github.com/promptctl/cc-candybar/pull/721), [#722](https://github.com/promptctl/cc-candybar/pull/722)); a click is a turn through answer ([#717](https://github.com/promptctl/cc-candybar/pull/717)); a session's facts carry each transcript fold alone with the payload laying the hook over it ([#709](https://github.com/promptctl/cc-candybar/pull/709)); daemon test cleanups ([#708](https://github.com/promptctl/cc-candybar/pull/708)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-11-05)).
- `promptctl/orange-drink` — 20 commits: full-screen alert's new level reaches VoiceOver at low priority and waits for the speech under way, medium interrupts ([#102](https://github.com/promptctl/orange-drink/pull/102)); VoiceOver hears the new level when a reading rewrites it ([#101](https://github.com/promptctl/orange-drink/pull/101)); the full-screen alert owns focus and reads the app to return to ([#99](https://github.com/promptctl/orange-drink/pull/99)); a pill shown over it sits at the top, clear of the headline ([#100](https://github.com/promptctl/orange-drink/pull/100)); the alert follows the battery while up ([#98](https://github.com/promptctl/orange-drink/pull/98)) ([commits](https://github.com/promptctl/orange-drink/commits?author=brandon-fryslie&since=2026-11-05)).
- `promptctl/tmux-control-mode-js` — 15 commits: WebSocket bridge heartbeat terminates a peer that never answers a fatal close ([#217](https://github.com/promptctl/tmux-control-mode-js/pull/217)); a ping the transport refuses arms the heartbeat deadline ([#218](https://github.com/promptctl/tmux-control-mode-js/pull/218)); bridge closes a client's socket when its own tmux dies ([#216](https://github.com/promptctl/tmux-control-mode-js/pull/216)); heartbeat and every `ms`/count option parsed at construction with `BRIDGE_INVALID_ARG` for a bound no reply can meet ([#219](https://github.com/promptctl/tmux-control-mode-js/pull/219), [#220](https://github.com/promptctl/tmux-control-mode-js/pull/220)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-11-05)).
- `promptctl/laws` — 9 commits: 0.42.0 `laws:code` becomes an agent with a one-hour prompt cache ([#105](https://github.com/promptctl/laws/pull/105)); 0.43.0 per-turn engagement hook rewritten around purpose and judgement ([#107](https://github.com/promptctl/laws/pull/107)); 0.44.0 one hook per event ([#108](https://github.com/promptctl/laws/pull/108)); 0.45.0 keeps code/testing/prompt/observability, moves the rest out ([#110](https://github.com/promptctl/laws/pull/110)); 0.46.0 forks `prompt` runs ([#112](https://github.com/promptctl/laws/pull/112)); marketplace lists memento, lit and skillz ([#109](https://github.com/promptctl/laws/pull/109), [#111](https://github.com/promptctl/laws/pull/111)); `no-single-session-evals.md` deleted ([#106](https://github.com/promptctl/laws/pull/106)).
- `promptctl/skillz` — 5 commits: new plugin repo; twelve skills move in from `dotfiles` ([#1](https://github.com/promptctl/skillz/pull/1)); `clean-room` and `spec` move in from `laws` ([#2](https://github.com/promptctl/skillz/pull/2)); `tmux-shared` takes the transcript-lookup fix from `dotfiles` with its test ([#3](https://github.com/promptctl/skillz/pull/3)).

### This Month

30-day volume exceeded the search index's 1000-result cap. Top by volume within the index:

- [`promptctl/low-talker`](https://github.com/promptctl/low-talker) — 200 commits
- [`promptctl/memento`](https://github.com/promptctl/memento) — 182
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 169
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 92
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 84
- [`promptctl/orange-drink`](https://github.com/promptctl/orange-drink) — 80
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 64
- [`promptctl/cc-hands`](https://github.com/promptctl/cc-hands) — 52
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 40
- [`promptctl/laws`](https://github.com/promptctl/laws) — 16

Languages: Swift, Python, TypeScript, Go.

---

<details>
<summary>Previous highlights</summary>

- [2026-11-11](./daily-archive/2026-11-11.md)
- [2026-11-10](./daily-archive/2026-11-10.md)
- [2026-11-03](./daily-archive/2026-11-03.md)
- [2026-10-29](./daily-archive/2026-10-29.md)
- [2026-10-28](./daily-archive/2026-10-28.md)
- [2026-10-27](./daily-archive/2026-10-27.md)
- [2026-10-15](./daily-archive/2026-10-15.md)

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

Local push-to-talk dictation for macOS with a chord-selected command layer. 200 commits over the past month, 144 today as the dictation-keys and test-layers arcs landed. An Escape while the word box shows `Transcribing` cancels the press on its way ([#293](https://github.com/promptctl/low-talker/pull/293)); chained Escapes leave the person's earlier dismissal to bring back ([#297](https://github.com/promptctl/low-talker/pull/297), [#298](https://github.com/promptctl/low-talker/pull/298)); inserts and questions cross one `Exchange` round trip and fail it with one `WireFailure` that names neither process ([#292](https://github.com/promptctl/low-talker/pull/292)); `FakeInputMethod` refuses a take-back by the input method's own Replacement rule ([#295](https://github.com/promptctl/low-talker/pull/295)); a test host app holds an AppKit text view and WebKit `<textarea>`/`<input>` so the input method's client contract runs against each over stdin/stdout ([#264](https://github.com/promptctl/low-talker/pull/264)); `CLAUDE.md` bans end-to-end testing and `test-host-check` is deleted ([#265](https://github.com/promptctl/low-talker/pull/265)).

### [memento](https://github.com/promptctl/memento)
**Python · MIT**

Agent-native workflow tooling for Claude Code — next-ticket pickup, the address-PR-review loop, and the cross-session handoff that carries a goal across a context reset. 182 commits over the past month, 171 this week as the hermetic suite environment, the tmux-worker session detection, and the handed-off fence all landed. `lib/hermetic.py` is one definition of the clean environment every suite starts from, replacing five near-copies ([#72](https://github.com/promptctl/memento/pull/72)); `lib/git_at.py` runs git with repository-local variables removed so a reader under a hook's `GIT_DIR` answers for its own directory ([#71](https://github.com/promptctl/memento/pull/71)); the tmux worker reads `/clear` as its claude moving to a new session via Claude Code's per-pid registry entry ([#75](https://github.com/promptctl/memento/pull/75)); a handed-off session's tool call is denied by a PreToolUse hook and ends its turn ([#74](https://github.com/promptctl/memento/pull/74)); goal publication claims hold a flock and drop a dead publisher's file ([#73](https://github.com/promptctl/memento/pull/73)); the journal arc landed earlier in the week ([#57](https://github.com/promptctl/memento/pull/57)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — fork of `@owloops/claude-powerline` with CLI override flags so the entire config can live in `settings.json`. 169 commits over the past month, 27 this week as Proposal 3 landed. One host owns the world and renderers answer it ([#710](https://github.com/promptctl/cc-candybar/pull/710)); `Renderer.answer` answers a statusline request in process ([#711](https://github.com/promptctl/cc-candybar/pull/711)); the host's collector holds each session's world state and hands it to the renderer ([#712](https://github.com/promptctl/cc-candybar/pull/712)); the checked `SessionId` travels from its door to every unit that keys by it, so no config can redeclare which session a bar reads or writes ([#720](https://github.com/promptctl/cc-candybar/pull/720), [#721](https://github.com/promptctl/cc-candybar/pull/721), [#722](https://github.com/promptctl/cc-candybar/pull/722)); a click is a turn through answer ([#717](https://github.com/promptctl/cc-candybar/pull/717)). Earlier in the cycle 1.213.0 rolled `main` back to the 1.189.0 tree, withdrawing every version 1.190.0 through 1.212.6 pending a corrected spec.

</td>
<td width="50%" valign="top">

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript · MIT**

A port of Python's Rich to TypeScript — markup, tables, trees, syntax, progress, tracebacks, Live, and an App runtime that routes focus and the pointer. 92 commits over the past month, 55 this week. The control-codes epic expanded to event decoding — `decodeAnsi` reads kitty's notification urgency, buttons and click report, iTerm2 attention and StealFocus, OSC 133 prompt zones ([#608](https://github.com/brandon-fryslie/rich-js/pull/608)); declared chrome and cursor state re-sent on tmux reattach ([#605](https://github.com/brandon-fryslie/rich-js/pull/605)); the terminal identifies itself with XTVERSION ([#600](https://github.com/brandon-fryslie/rich-js/pull/600)); underline kinds `4:1`–`4:5` and underline color 58 as Style fields ([#602](https://github.com/brandon-fryslie/rich-js/pull/602)); clipboard, pointer and notification chosen by pick over `TerminalFeatures` ([#599](https://github.com/brandon-fryslie/rich-js/pull/599)); Progress mirrors OSC 9;4 ([#596](https://github.com/brandon-fryslie/rich-js/pull/596)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 2★**

Agent-native issue tracker — `lit`, backed by a Dolt-shaped store with containment, dependencies and labels. 84 commits over the past month, 28 this week. Next-skill moves to a fresh branch cut from trunk when the PR merged ([#923](https://github.com/promptctl/links-issue-tracker/pull/923)); one ticket in flight has one holder — the checkout and session that started it ([#922](https://github.com/promptctl/links-issue-tracker/pull/922)); a Go literal quoted in a span is a claim so every copy of a message gates on it ([#921](https://github.com/promptctl/links-issue-tracker/pull/921)); workflow bodies hold the interpolated id and id printers take only values that hold themselves ([#919](https://github.com/promptctl/links-issue-tracker/pull/919)); the pre-push hook passes `lit sync push`'s failure block through instead of claiming a retry fixes it ([#916](https://github.com/promptctl/links-issue-tracker/pull/916)); prompts asked only when stdin and stdout are both real terminals ([#915](https://github.com/promptctl/links-issue-tracker/pull/915)).

### [orange-drink](https://github.com/promptctl/orange-drink)
**Swift**

A macOS menu-bar app and widgets for iPhone, iPad and Mac battery, with a privileged helper for charging controls. 80 commits over the past month, 20 this week as the full-screen alert's VoiceOver and focus behavior landed. The alert's new level reaches VoiceOver at low priority and waits for the speech under way, medium interrupts ([#102](https://github.com/promptctl/orange-drink/pull/102)); VoiceOver hears the new level when a reading rewrites it ([#101](https://github.com/promptctl/orange-drink/pull/101)); the alert owns focus and reads the app to return to ([#99](https://github.com/promptctl/orange-drink/pull/99)); a pill shown over it sits at the top, clear of the headline ([#100](https://github.com/promptctl/orange-drink/pull/100)); the alert follows the battery while it is up ([#98](https://github.com/promptctl/orange-drink/pull/98)).

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
