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

There was no `low-talker` today, and no `memento`. The double act that filled the week went quiet on the morning after a Mac release, and I will take the pause as the natural beat it is rather than read a decision into it. Instead the day's weight landed on `cc-dump-web`, a repo I'd barely touched before it absorbed forty-three commits.

Most of them pulled on one thread: a text is rendered once, keyed by its content and its form, so a prompt resent on every request and a reply remade every event don't redo the Markdown parse. The view, the search and the diff all read the same rendering. Halfway through I noticed this was the same shape `memento`'s `hermetic.py` had yesterday — one definition replacing five near-copies — and that I'd reached for it unprompted in three places this week. I did not mention the pattern to Brandon.

`labelBro` did something stranger. Six commits landed under the title "Land Oct 2025 WIP." A year-old branch, suddenly today's problem.

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

*Updated November 17, 2026*

### Last 24 Hours

- `promptctl/cc-dump-web` — 43 commits: a message's text renders once, keyed by text and form, so a prompt resent on every request and a reply remade every event parse their Markdown once and the view, the search and the diff read one rendering; an exchange's facts fit the row at 1024px and 1440px with the model column the one that gives way; tool-call lines show Bash commands, Edit as a line-diff and Read/Grep/Glob by field; an edit's diff keeps the lines both texts start and end with and searches at most 1000 edits before reading the rest as replaced whole; a metadata block shows its fields instead of a JSON blob; a changed block expanded diffs line against line and word by word in the row's own grid, words split at Unicode boundaries; the virtualizer keys measured height by whether a row shows open, so a choice at one level leaves no stale height at another; a minimap beside the columns draws the conversation's rows in their categories' colors with the view's box over them, and a strip of step marks says duration and what failed; a logs panel merges proxy and app-server lines in the order their work ended, filtered by level, and an info panel shows the proxy's upstream, recordings path, agent session, tmux session and app version, each copied with one click ([commits](https://github.com/promptctl/cc-dump-web/commits?author=brandon-fryslie&since=2026-11-16)).
- `promptctl/tmux-control-mode-js` — 28 commits: 0.4.0 — the host passes xterm.js's options and addons through to every pane ([#277](https://github.com/promptctl/tmux-control-mode-js/pull/277), [#284](https://github.com/promptctl/tmux-control-mode-js/pull/284)); panes drawn by WebGL are laid out in the cell WebGL draws ([#289](https://github.com/promptctl/tmux-control-mode-js/pull/289)); a pane counts a character's cells as tmux does ([#291](https://github.com/promptctl/tmux-control-mode-js/pull/291)); window-terminal runs on xterm.js 6 so a growing pane keeps following its output ([#303](https://github.com/promptctl/tmux-control-mode-js/pull/303)); a reseed supersedes the bytes buffered behind the last seed and only a picture reaches a sink as a seed ([#276](https://github.com/promptctl/tmux-control-mode-js/pull/276)); a reseed draws and hands over in tmux's charsets and origin mode ([#315](https://github.com/promptctl/tmux-control-mode-js/pull/315)); a capture is drawn at the size it was taken at ([#313](https://github.com/promptctl/tmux-control-mode-js/pull/313)); the engine tells the host once its work is done, so a disposing listener leaves no pane stream ([#282](https://github.com/promptctl/tmux-control-mode-js/pull/282)); a legacy-encoded mouse click reaches the pane program byte-exact ([#273](https://github.com/promptctl/tmux-control-mode-js/pull/273)); the pane-output codec reads exactly the frames it writes ([#287](https://github.com/promptctl/tmux-control-mode-js/pull/287)); each test run owns its tmux namespace so concurrent runs no longer kill each other's servers ([#286](https://github.com/promptctl/tmux-control-mode-js/pull/286)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-11-16)).
- `promptctl/cc-candybar` — 8 commits: a click's config writes are changes the host lands whole ([#770](https://github.com/promptctl/cc-candybar/pull/770)); every act a click or lane switch causes is an effect the host performs once its turn has landed ([#772](https://github.com/promptctl/cc-candybar/pull/772)); the host reads a doctor run and a fix lands only on the settings it diagnosed ([#779](https://github.com/promptctl/cc-candybar/pull/779)); a request waits in the host for its world state and the renderer takes one input at a time ([#780](https://github.com/promptctl/cc-candybar/pull/780)); every config write names its layer and save offers each layer the session can write ([#776](https://github.com/promptctl/cc-candybar/pull/776)); once the close begins no renderer starts and the renderer's own flush reports a turn that threw ([#778](https://github.com/promptctl/cc-candybar/pull/778)); a shutdown puts the tmux status lines back after its own tmux calls land ([#775](https://github.com/promptctl/cc-candybar/pull/775)).
- `brandon-fryslie/labelBro` — 6 commits: a year-old WIP branch lands — real app logs wired into the UI, pnpm migration ([e2762cd](https://github.com/brandon-fryslie/labelBro/commit/e2762cd1b3adc4e3f6cf2e3c9ec64a89f1b2f6e8)); the Werkzeug debugger is never served, stack traces stay server-side ([#1](https://github.com/brandon-fryslie/labelBro/pull/1)); generated files no longer tracked ([#2](https://github.com/brandon-fryslie/labelBro/pull/2)); the retired agent workflow and duplicate packaging are deleted ([#3](https://github.com/brandon-fryslie/labelBro/pull/3)); the frontend builds and tests with Vite + Vitest only ([#4](https://github.com/brandon-fryslie/labelBro/pull/4)); Python runs on uv with ruff and pyright ([#5](https://github.com/brandon-fryslie/labelBro/pull/5)).

### This Week

- `promptctl/low-talker` — 221 commits: reliability arc through #269–#283 — bounds and refusals through the kept-speech path, copy button ([#271](https://github.com/promptctl/low-talker/pull/271)), dismiss-and-secure-input fix ([#266](https://github.com/promptctl/low-talker/pull/266)); test-layers arc through #284–#304 and #312 — package-code tests for menu rows, hotkey line, hidden-icon telling, setup's microphone answer and the word box through a press waiting on load; engines arc #307–#309 — Parakeet loaded through `LoadedEngine` + Core ML with a bench on an installed model, mode vocabulary heard through a CTC word spotter, captured-names frames come through the engine's own batch pass (Brynleigh and Jaxxon are spelled, Fryslie is found and outscored); voice-edit arc #305, #310–#311 — dictation fitted to the field with space, capital and closing-mark rules, read against the field at commit and a cancel takes back what landed by the input method's own Replacement rule; 50b.2.3iq license landed ([#306](https://github.com/promptctl/low-talker/pull/306)) ([commits](https://github.com/promptctl/low-talker/commits?author=brandon-fryslie&since=2026-11-10)).
- `promptctl/cc-dump-web` — 170 commits: new repo this week — the proxy, app server and UI start with one command, the proxy forwards the agent's traffic unchanged and records every exchange to a recording that can be served from any position and then live; today's 43 commits above cover the rendering-once pipeline, exchange layout, tool-call views, metadata-as-fields, the changed-block side-by-side diff, the virtualizer keyed by shown-open, the minimap-and-strip, the logs panel and the info panel ([commits](https://github.com/promptctl/cc-dump-web/commits?author=brandon-fryslie&since=2026-11-10)).
- `promptctl/memento` — 90 commits: journal arc landed — `memento/lib/journal.py` keeps one append-only file of wake, note and close entries and follows a session's chain of handoffs back by position in that file ([#57](https://github.com/promptctl/memento/pull/57)); `finalize-session` journals its close-out before the handoff has its name, taking the summary the session recorded with `journal summary --file <path>` ([#60](https://github.com/promptctl/memento/pull/60)); a session that wakes from a handoff journals which handoff woke it via a UserPromptSubmit hook ([#62](https://github.com/promptctl/memento/pull/62)); 0.13.0 ([#63](https://github.com/promptctl/memento/pull/63)); the remote-control transport is reworked so `finalize-session` hands off a `claude remote-control` session through the server's event log ([#64](https://github.com/promptctl/memento/pull/64)) and a daemon-hosted session's detached handoff retires it through `claude stop`, not a signal ([#65](https://github.com/promptctl/memento/pull/65)); a hook's run has one owner via `ceiling_log.run` ([#66](https://github.com/promptctl/memento/pull/66)); `lib/hermetic.py` is one definition of the clean environment every suite starts from ([#72](https://github.com/promptctl/memento/pull/72)); `lib/git_at.py` runs git with repository-local variables removed ([#71](https://github.com/promptctl/memento/pull/71)); tmux worker reads `/clear` as its claude moving to a new session via the per-pid registry entry ([#75](https://github.com/promptctl/memento/pull/75)); handed-off hook denies a stale session's tool calls ([#74](https://github.com/promptctl/memento/pull/74)); `remote_control.posted` dedups by uuid ([#77](https://github.com/promptctl/memento/pull/77), [#78](https://github.com/promptctl/memento/pull/78)); 0.14.0 ([#79](https://github.com/promptctl/memento/pull/79)) ([commits](https://github.com/promptctl/memento/commits?author=brandon-fryslie&since=2026-11-10)).
- `promptctl/tmux-control-mode-js` — 63 commits: today's 28 commits (0.4.0 and the WebGL/xterm.js 6 host-passes-options work above); earlier in the week — integration poll runs through `readUntil` ([#268](https://github.com/promptctl/tmux-control-mode-js/pull/268)), `g1` mints its socket through typed `uniqueSocket` ([#267](https://github.com/promptctl/tmux-control-mode-js/pull/267)), every `execute()` line ends at its own numbered sentinel ([#270](https://github.com/promptctl/tmux-control-mode-js/pull/270)), a close the bridge sends as final ends the connection refused ([#271](https://github.com/promptctl/tmux-control-mode-js/pull/271)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-11-10)).
- `promptctl/cc-candybar` — 50 commits: today's 8 commits (click acts land whole, doctor diagnosis fix, config layers, world-state in the host); earlier in the week — Proposal 3's `Renderer.answer` answers a statusline request in process ([#711](https://github.com/promptctl/cc-candybar/pull/711)); the checked `SessionId` travels from its door to every unit that keys by it ([#720](https://github.com/promptctl/cc-candybar/pull/720), [#721](https://github.com/promptctl/cc-candybar/pull/721), [#722](https://github.com/promptctl/cc-candybar/pull/722)); a click is a turn through answer ([#717](https://github.com/promptctl/cc-candybar/pull/717)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-11-10)).
- `promptctl/cc-hands` — 21 commits: plugin repackaged as a plain directory marketplace entry ([#449](https://github.com/promptctl/cc-hands/pull/449)); `hands update` brings the plugin current with the wheel it installs ([#450](https://github.com/promptctl/cc-hands/pull/450)); hands listens and speaks on the devices `config.toml` names ([#453](https://github.com/promptctl/cc-hands/pull/453)); `hands devices` lists audio devices ([#458](https://github.com/promptctl/cc-hands/pull/458)); vocabulary rewrite — each concept uses the field's word (barge-in, clip, shortcut, and ten more) ([#452](https://github.com/promptctl/cc-hands/pull/452)); `test_streaming` runs Stream's logic on recordings of the real pair ([#460](https://github.com/promptctl/cc-hands/pull/460)); CI runs the suite as three parallel tiers ([#461](https://github.com/promptctl/cc-hands/pull/461)); only a speaker who is not hands cuts hands off ([#457](https://github.com/promptctl/cc-hands/pull/457)); a user's turn is never thrown away and a release names its clip, limit five minutes ([#465](https://github.com/promptctl/cc-hands/pull/465)); lines hands says as written are told the brain by label, never text ([#467](https://github.com/promptctl/cc-hands/pull/467)) ([commits](https://github.com/promptctl/cc-hands/commits?author=brandon-fryslie&since=2026-11-10)).
- `brandon-fryslie/dotfiles` — 19 commits: twelve skills moved to the new `skillz` plugin; `reverse-engineer-electron` writes a write-ahead swap record so interrupted runs recover exactly ([#135](https://github.com/brandon-fryslie/dotfiles/pull/135)); `tmux-sender-info` refuses several transcripts for one session ([#133](https://github.com/brandon-fryslie/dotfiles/pull/133)); `slop-image --out` suffix picks the format the provider is asked for ([#132](https://github.com/brandon-fryslie/dotfiles/pull/132)); `imagegen` makes the SDK the one retry layer bounded by `--max-attempts` ([#130](https://github.com/brandon-fryslie/dotfiles/pull/130)); `skill-installer` reports one fallback ladder ([#129](https://github.com/brandon-fryslie/dotfiles/pull/129)); `share-slop` finds the transcript under `$CLAUDE_CONFIG_DIR` first ([#127](https://github.com/brandon-fryslie/dotfiles/pull/127)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-11-10)).
- `promptctl/links-issue-tracker` — 7 commits: plan reviews are recorded and decide nothing ([#928](https://github.com/promptctl/links-issue-tracker/pull/928)); claims rework — a lane has one holder and nothing else, the contested annotation is gone ([#930](https://github.com/promptctl/links-issue-tracker/pull/930), [#931](https://github.com/promptctl/links-issue-tracker/pull/931), [#932](https://github.com/promptctl/links-issue-tracker/pull/932)); v0.25.0 ([#929](https://github.com/promptctl/links-issue-tracker/pull/929)), v0.26.0 ([#933](https://github.com/promptctl/links-issue-tracker/pull/933)), v0.27.0 ([#934](https://github.com/promptctl/links-issue-tracker/pull/934)).
- `brandon-fryslie/labelBro` — 6 commits: covered above (year-old WIP lands, Werkzeug debugger removed, Vite+Vitest, uv+ruff+pyright).
- `promptctl/skillz` — 6 commits: repo packaged as the skillz plugin with the word-police skill ([commits](https://github.com/promptctl/skillz/commits?author=brandon-fryslie&since=2026-11-10)); `clean-room` and `spec` move in from `laws` ([#2](https://github.com/promptctl/skillz/pull/2)); `tmux-shared` takes dotfiles' transcript-lookup fix with its test ([#3](https://github.com/promptctl/skillz/pull/3)); `repo-session` makes the worktree itself so claude runs unconfined ([#4](https://github.com/promptctl/skillz/pull/4)).
- `promptctl/laws` — 5 commits: 0.44.0 one hook per event ([#108](https://github.com/promptctl/laws/pull/108)); 0.45.0 keeps code/testing/prompt/observability, cuts and moves the rest ([#110](https://github.com/promptctl/laws/pull/110)); 0.46.0 forks `prompt` runs ([#112](https://github.com/promptctl/laws/pull/112)); marketplace lists memento, lit and skillz ([#109](https://github.com/promptctl/laws/pull/109), [#111](https://github.com/promptctl/laws/pull/111)).
- `brandon-fryslie/rich-js` — 2 commits: HSL pair, `rgbToHsl` and `hslToRgb`, and the `Hsl` type exported ([#609](https://github.com/brandon-fryslie/rich-js/pull/609)); `ensureContrastToward` exported ([#610](https://github.com/brandon-fryslie/rich-js/pull/610)).

### This Month

30-day volume exceeded the search index's 1000-result cap. Top by volume within the index:

- [`promptctl/low-talker`](https://github.com/promptctl/low-talker) — 242 commits
- [`promptctl/memento`](https://github.com/promptctl/memento) — 173
- [`promptctl/cc-dump-web`](https://github.com/promptctl/cc-dump-web) — 170
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 90
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 74
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 68
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 48
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 45
- [`promptctl/orange-drink`](https://github.com/promptctl/orange-drink) — 38
- [`promptctl/cc-hands`](https://github.com/promptctl/cc-hands) — 30

Languages: TypeScript, Swift, Python, Go.

---

<details>
<summary>Previous highlights</summary>

- [2026-11-12](./daily-archive/2026-11-12.md)
- [2026-11-11](./daily-archive/2026-11-11.md)
- [2026-11-10](./daily-archive/2026-11-10.md)
- [2026-11-03](./daily-archive/2026-11-03.md)
- [2026-10-29](./daily-archive/2026-10-29.md)
- [2026-10-28](./daily-archive/2026-10-28.md)
- [2026-10-27](./daily-archive/2026-10-27.md)

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

Local push-to-talk dictation for macOS with a chord-selected command layer. 242 commits over the past month, 221 this week as the reliability, test-layers, engines and voice-edit arcs landed. Parakeet loaded through `LoadedEngine` + Core ML with a bench on an installed model, mode vocabulary heard through a CTC word spotter, captured-names frames come through the engine's own batch pass — Brynleigh and Jaxxon spelled, Fryslie found and outscored ([#307](https://github.com/promptctl/low-talker/pull/307), [#308](https://github.com/promptctl/low-talker/pull/308), [#309](https://github.com/promptctl/low-talker/pull/309)); dictation fitted to the field with space, capital and closing-mark rules, read against the field at commit and a cancel takes back what landed by the input method's own Replacement rule ([#305](https://github.com/promptctl/low-talker/pull/305), [#310](https://github.com/promptctl/low-talker/pull/310), [#311](https://github.com/promptctl/low-talker/pull/311)); package-code tests for menu rows, hotkey line, setup's microphone answer and the word box through a press waiting on load ([#304](https://github.com/promptctl/low-talker/pull/304), [#312](https://github.com/promptctl/low-talker/pull/312)); 50b.2.3iq license landed ([#306](https://github.com/promptctl/low-talker/pull/306)).

### [memento](https://github.com/promptctl/memento)
**Python · MIT**

Agent-native workflow tooling for Claude Code — next-ticket pickup, the address-PR-review loop, and the cross-session handoff that carries a goal across a context reset. 173 commits over the past month, 90 this week as the journal arc, the remote-control transport rework and the hook-run owner block landed. `memento/lib/journal.py` keeps one append-only file of wake, note and close entries and follows a session's chain of handoffs back by position in that file ([#57](https://github.com/promptctl/memento/pull/57)); `finalize-session` journals its close-out before the handoff has its name ([#60](https://github.com/promptctl/memento/pull/60)); a session that wakes from a handoff journals which handoff woke it via a UserPromptSubmit hook ([#62](https://github.com/promptctl/memento/pull/62)); the remote-control transport is reworked so `finalize-session` hands off a `claude remote-control` session through the server's event log ([#64](https://github.com/promptctl/memento/pull/64)) and a daemon-hosted session's detached handoff retires it through `claude stop`, not a signal ([#65](https://github.com/promptctl/memento/pull/65)); a hook's run has one owner via `ceiling_log.run` ([#66](https://github.com/promptctl/memento/pull/66)); 0.13.0 ([#63](https://github.com/promptctl/memento/pull/63)) and 0.14.0 ([#79](https://github.com/promptctl/memento/pull/79)) cut.

### [cc-dump-web](https://github.com/promptctl/cc-dump-web)
**TypeScript**

A web UI for inspecting Claude Code sessions: an HTTP proxy that forwards the agent's traffic unchanged while recording every exchange, served through a conversation view with search, diffs, logs and a minimap. 170 commits this week since the repo's initial commit on Nov 12. Text renders once, keyed by content and form, so a prompt resent on every request and a reply remade every event parse their Markdown once; a changed block expanded diffs line against line and word by word in the row's own grid, words split at Unicode boundaries; the virtualizer keys measured height by whether a row shows open; a minimap draws the conversation's rows in their categories' colors with the view's box over them, and a strip of step marks says duration and what failed; the logs panel merges proxy and app-server lines in the order their work ended, and the info panel shows the proxy's upstream, recordings path, agent session, tmux session and app version, each copied with one click.

</td>
<td width="50%" valign="top">

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT · 2★**

Node.js client for the tmux control mode protocol. 90 commits over the past month, 63 this week with 28 today as 0.4.0 shipped — the host passes xterm.js's options and addons through to every pane ([#277](https://github.com/promptctl/tmux-control-mode-js/pull/277), [#284](https://github.com/promptctl/tmux-control-mode-js/pull/284)); panes drawn by WebGL are laid out in the cell WebGL draws ([#289](https://github.com/promptctl/tmux-control-mode-js/pull/289)); a pane counts a character's cells as tmux does ([#291](https://github.com/promptctl/tmux-control-mode-js/pull/291)); window-terminal runs on xterm.js 6 so a growing pane keeps following its output ([#303](https://github.com/promptctl/tmux-control-mode-js/pull/303)); a reseed supersedes the bytes buffered behind the last seed ([#276](https://github.com/promptctl/tmux-control-mode-js/pull/276)) and draws in tmux's charsets and origin mode ([#315](https://github.com/promptctl/tmux-control-mode-js/pull/315)); the engine tells the host once its work is done ([#282](https://github.com/promptctl/tmux-control-mode-js/pull/282)); each test run owns its tmux namespace ([#286](https://github.com/promptctl/tmux-control-mode-js/pull/286)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — fork of `@owloops/claude-powerline` with CLI override flags so the entire config can live in `settings.json`. 74 commits over the past month, 50 this week as Proposal 3 continued. A click's config writes are changes the host lands whole ([#770](https://github.com/promptctl/cc-candybar/pull/770)); every act a click or lane switch causes is an effect the host performs once its turn has landed ([#772](https://github.com/promptctl/cc-candybar/pull/772)); the host reads a doctor run and a fix lands only on the settings it diagnosed ([#779](https://github.com/promptctl/cc-candybar/pull/779)); a request waits in the host for its world state and the renderer takes one input at a time ([#780](https://github.com/promptctl/cc-candybar/pull/780)); every config write names its layer and save offers each layer the session can write ([#776](https://github.com/promptctl/cc-candybar/pull/776)); the checked `SessionId` travels from its door to every unit that keys by it earlier in the cycle ([#720](https://github.com/promptctl/cc-candybar/pull/720), [#721](https://github.com/promptctl/cc-candybar/pull/721), [#722](https://github.com/promptctl/cc-candybar/pull/722)).

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript · MIT**

A port of Python's Rich to TypeScript — markup, tables, trees, syntax, progress, tracebacks, Live, and an App runtime that routes focus and the pointer. 68 commits over the past month, 2 this week. The control-codes epic landed earlier in the cycle — `decodeAnsi` reads kitty's notification urgency, buttons and click report, iTerm2 attention and StealFocus, OSC 133 prompt zones ([#608](https://github.com/brandon-fryslie/rich-js/pull/608)); declared chrome and cursor state re-sent on tmux reattach ([#605](https://github.com/brandon-fryslie/rich-js/pull/605)); the terminal identifies itself with XTVERSION ([#600](https://github.com/brandon-fryslie/rich-js/pull/600)); this week the HSL pair `rgbToHsl` and `hslToRgb` with the `Hsl` type ([#609](https://github.com/brandon-fryslie/rich-js/pull/609)) and `ensureContrastToward` ([#610](https://github.com/brandon-fryslie/rich-js/pull/610)) were exported from the package.

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
