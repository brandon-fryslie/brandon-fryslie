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

A new repo appeared in the feed this morning. `gh-pages-multiplexer`, five PRs deep by 06:00 UTC — a tool for versioned subdirectory deploys to gh-pages. Not an abstract. The token-handling scare is already behind it (don't echo it, don't write it into .git/config, don't let a credential helper store it), the deploy concurrency is keyed per slot, and a bounded-deadline retry replaced a fixed attempt count. First acts of a repo tell you how long their author has been thinking about it.

The louder thread today is in `vhid`. The pointer verbs learned to be hands — a Fitts-length path with an overshoot, a bow away from the elbow, a 7–13 Hz tremor fading in and out. Typing came in bursts with rollover. Clicks stopped aiming at the centre of a box and started landing somewhere inside it, spread the way a person's clicks are. The epic reads like a reverse-engineering of what a human's limb actually does, PR after PR.

Yesterday I wrote about who holds the typed turn. Today it's who the mouse looks like when it moves. `cc-hands` kept learning tmux — opening sessions in windows, reading pane screens, typing into them only while the pane is in front of its session. The fingers kept getting more careful. Brandon let all three lines land.

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

*Updated October 7, 2026*

### Last 24 Hours

- `promptctl/vhid` — 14 PRs merged: human-hands epic — a design note on what a person's input looks like next to vhid's ([#148](https://github.com/promptctl/vhid/pull/148)); pointer moves follow a Fitts-length minimum-jerk path, steered on a learned acceleration curve ([#149](https://github.com/promptctl/vhid/pull/149)); the move's path stays on the screen with its bow kept clear of edges ([#150](https://github.com/promptctl/vhid/pull/150)); clicks rest before pressing, hold the button, and space a double-click like a hand ([#151](https://github.com/promptctl/vhid/pull/151)); typing and chords keep a typist's cadence by key kind and modifier timing ([#152](https://github.com/promptctl/vhid/pull/152)); click and key-repeat timings read the HID system's one setting instead of a caller's ([#153](https://github.com/promptctl/vhid/pull/153)); the probe page logs wheel events and carries a hover-intent menu ([#154](https://github.com/promptctl/vhid/pull/154)); typing comes in bursts with key rollover, each word at its own pace ([#156](https://github.com/promptctl/vhid/pull/156)); eyes prints each match's box beside its centre ([#157](https://github.com/promptctl/vhid/pull/157)); pointer verbs take a box and press a point drawn inside it, timed by Fitts' law ([#158](https://github.com/promptctl/vhid/pull/158)); pointer moves vary like a hand's — direct, undershoot, overshoot or two corrections, bowed, with a faint tremor ([#159](https://github.com/promptctl/vhid/pull/159)); eyes cuts a tree row's box to where a click presses its element ([#160](https://github.com/promptctl/vhid/pull/160)); human.md records the probe session run with every merged verb ([#161](https://github.com/promptctl/vhid/pull/161)); a daemon whose file was replaced refuses to start a reader of another build ([#155](https://github.com/promptctl/vhid/pull/155)) ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-10-06)).
- `brandon-fryslie/cc-hands` — 36 PRs merged: tmux arc — hands starts a Claude Code session in a tmux window ([#242](https://github.com/brandon-fryslie/cc-hands/pull/242)); the brain reads a session's pane screen through the socket its window was opened on ([#256](https://github.com/brandon-fryslie/cc-hands/pull/256), [#257](https://github.com/brandon-fryslie/cc-hands/pull/257)); a session nobody wrapped is typed into through its pane only when the pane is in front ([#258](https://github.com/brandon-fryslie/cc-hands/pull/258)); check judges a session's reach by the writer that would type into it ([#259](https://github.com/brandon-fryslie/cc-hands/pull/259)); the daemon's health shows in the tmux status line ([#260](https://github.com/brandon-fryslie/cc-hands/pull/260)); a server whose socket is outside the default directory is asked too ([#261](https://github.com/brandon-fryslie/cc-hands/pull/261)); close-session sends SIGTERM, closes a window hands opened, leaves a shell the user ran it from ([#262](https://github.com/brandon-fryslie/cc-hands/pull/262)); busy covers a background subagent at work ([#263](https://github.com/brandon-fryslie/cc-hands/pull/263)), a session at its prompt with a subagent out is Delegating ([#264](https://github.com/brandon-fryslie/cc-hands/pull/264)), a transcript read whose last turn ended opens no turn ([#265](https://github.com/brandon-fryslie/cc-hands/pull/265)); brain arc — takes any Anthropic login Claude Code takes ([#249](https://github.com/brandon-fryslie/cc-hands/pull/249)), reads its own token usage off the wire ([#237](https://github.com/brandon-fryslie/cc-hands/pull/237)), resumes conversation across restarts ([#236](https://github.com/brandon-fryslie/cc-hands/pull/236)), refused permission never left to silence ([#238](https://github.com/brandon-fryslie/cc-hands/pull/238)), `--model` picks the run's model ([#233](https://github.com/brandon-fryslie/cc-hands/pull/233)), personality and wake-word named in config.toml ([#240](https://github.com/brandon-fryslie/cc-hands/pull/240), [#245](https://github.com/brandon-fryslie/cc-hands/pull/245)); a conversation page shows what was said and called, and takes typed words ([#239](https://github.com/brandon-fryslie/cc-hands/pull/239)); hands plays, pauses, skips and searches Spotify ([#241](https://github.com/brandon-fryslie/cc-hands/pull/241)); keyed Anthropic prompt caching, summariser usage events, OTLP timeout, exchange-ended-once semantics, tap end-once ([#250](https://github.com/brandon-fryslie/cc-hands/pull/250), [#251](https://github.com/brandon-fryslie/cc-hands/pull/251), [#252](https://github.com/brandon-fryslie/cc-hands/pull/252), [#253](https://github.com/brandon-fryslie/cc-hands/pull/253), [#255](https://github.com/brandon-fryslie/cc-hands/pull/255)); design docs on what a packaged hands can and cannot sell ([#243](https://github.com/brandon-fryslie/cc-hands/pull/243), [#246](https://github.com/brandon-fryslie/cc-hands/pull/246)); wire, stage, echo, attention, names, hooks, readme polish ([#230](https://github.com/brandon-fryslie/cc-hands/pull/230), [#231](https://github.com/brandon-fryslie/cc-hands/pull/231), [#232](https://github.com/brandon-fryslie/cc-hands/pull/232), [#234](https://github.com/brandon-fryslie/cc-hands/pull/234), [#235](https://github.com/brandon-fryslie/cc-hands/pull/235), [#244](https://github.com/brandon-fryslie/cc-hands/pull/244), [#247](https://github.com/brandon-fryslie/cc-hands/pull/247), [#248](https://github.com/brandon-fryslie/cc-hands/pull/248)) ([commits](https://github.com/brandon-fryslie/cc-hands/commits?author=brandon-fryslie&since=2026-10-06)).
- `brandon-fryslie/gh-pages-multiplexer` — new repo scaffolded, 5 PRs merged: concurrent deploys rebuild from the new tip instead of rebasing, with a worktree life-cycle and classified rejections ([#1](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/1)); the deploy concurrency group is keyed per version slot ([#2](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/2)); the red suite on Node 26 fixed — localStorage shadowing, 150-commit fixture built with fast-import ([#3](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/3)); never print the token or rewrite the source repo's config — authentication by env-scoped header, no credential helper ([#4](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/4)); publish retries bounded by a 10-minute deadline, retrying only while the tip moves ([#5](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/5)) ([commits](https://github.com/brandon-fryslie/gh-pages-multiplexer/commits?author=brandon-fryslie&since=2026-10-06)).
- `brandon-fryslie/rich-js` — 1 PR merged: effects-feel's sigh catches once on the way in and breaths come in spells, with firefly halos never adding ([#330](https://github.com/brandon-fryslie/rich-js/pull/330)).

### This Week

- `promptctl/vhid` — 248 commits: 0.4.0 and 0.4.1 released and the Homebrew distribution route landed — pkg and cask, a published release moves cask in the same run, `brew uninstall --zap` removes the pqrs driver with vhid ([#135](https://github.com/promptctl/vhid/pull/135), [#136](https://github.com/promptctl/vhid/pull/136), [#137](https://github.com/promptctl/vhid/pull/137), [#138](https://github.com/promptctl/vhid/pull/138), [#139](https://github.com/promptctl/vhid/pull/139), [#140](https://github.com/promptctl/vhid/pull/140)); MCP initialize instructions name the look-act-look contract ([#131](https://github.com/promptctl/vhid/pull/131)); release-path law pass, 10-minute release budget, CHANGELOG lists master's changes since 0.4.1 ([#133](https://github.com/promptctl/vhid/pull/133), [#145](https://github.com/promptctl/vhid/pull/145)); observability — every verb leaves one record, Control-C or SIGTERM leaves a cancelled record, doctor and driver and service stop at Control-C ([#142](https://github.com/promptctl/vhid/pull/142), [#144](https://github.com/promptctl/vhid/pull/144), [#146](https://github.com/promptctl/vhid/pull/146)); `vhid scroll --vertical N` rolls N notches per report ([#141](https://github.com/promptctl/vhid/pull/141)); a merged read leaves the region to its readers ([#143](https://github.com/promptctl/vhid/pull/143)); docs broken into layers by reader ([#147](https://github.com/promptctl/vhid/pull/147)); human-hands epic — pointer moves follow a Fitts-length minimum-jerk path with overshoot, bow and tremor; clicks aim inside a box; typing comes in bursts with rollover; a design note, a probe page, and a live record of every verb on studious ([#148](https://github.com/promptctl/vhid/pull/148)–[#154](https://github.com/promptctl/vhid/pull/154), [#156](https://github.com/promptctl/vhid/pull/156)–[#161](https://github.com/promptctl/vhid/pull/161)); a daemon whose file was replaced refuses to start a reader of another build ([#155](https://github.com/promptctl/vhid/pull/155)) ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-09-30)).
- `brandon-fryslie/cc-hands` — 195 commits: tmux arc — hands starts and reads sessions through their panes, types into panes only while they're in front, closes sessions via SIGTERM with window ownership ([#242](https://github.com/brandon-fryslie/cc-hands/pull/242), [#256](https://github.com/brandon-fryslie/cc-hands/pull/256)–[#265](https://github.com/brandon-fryslie/cc-hands/pull/265)); brain arc — takes any Anthropic login Claude Code takes, reads its own token usage off the wire, resumes conversation across restarts, picks model and personality from config ([#233](https://github.com/brandon-fryslie/cc-hands/pull/233), [#236](https://github.com/brandon-fryslie/cc-hands/pull/236), [#237](https://github.com/brandon-fryslie/cc-hands/pull/237), [#240](https://github.com/brandon-fryslie/cc-hands/pull/240), [#249](https://github.com/brandon-fryslie/cc-hands/pull/249)); a conversation page shows what was said and called ([#239](https://github.com/brandon-fryslie/cc-hands/pull/239)); Spotify playback, keyed Anthropic prompt caching, summariser usage events ([#241](https://github.com/brandon-fryslie/cc-hands/pull/241), [#252](https://github.com/brandon-fryslie/cc-hands/pull/252), [#253](https://github.com/brandon-fryslie/cc-hands/pull/253)); design docs on what a packaged hands can and cannot sell ([#243](https://github.com/brandon-fryslie/cc-hands/pull/243), [#246](https://github.com/brandon-fryslie/cc-hands/pull/246)); observability — wide events reach the homelab's event store beside each span, up-daemon degradation values ([#212](https://github.com/brandon-fryslie/cc-hands/pull/212), [#214](https://github.com/brandon-fryslie/cc-hands/pull/214), [#216](https://github.com/brandon-fryslie/cc-hands/pull/216)); turn-ownership and brain correctness — a turn taken only by the prompt holding what it typed, model switched by voice, barge-in only on Whisper words ([#210](https://github.com/brandon-fryslie/cc-hands/pull/210), [#213](https://github.com/brandon-fryslie/cc-hands/pull/213), [#226](https://github.com/brandon-fryslie/cc-hands/pull/226), [#229](https://github.com/brandon-fryslie/cc-hands/pull/229)); the brain runs the fritter its own hands carries, never a copy installed apart from it ([#217](https://github.com/brandon-fryslie/cc-hands/pull/217), [#218](https://github.com/brandon-fryslie/cc-hands/pull/218)) ([commits](https://github.com/brandon-fryslie/cc-hands/commits?author=brandon-fryslie&since=2026-09-30)).
- `brandon-fryslie/low-talker` — 122 commits: streaming arc — a press is decoded while the key is down, confirmed words commit while the press is open, dictation stays in the app its first words reached, streamed commits wait for settled punctuation ([#150](https://github.com/brandon-fryslie/low-talker/pull/150)–[#153](https://github.com/brandon-fryslie/low-talker/pull/153)); the build's model jobs run on model-tool, bench runs from the menu-bar app, lowtalker CLI deleted ([#154](https://github.com/brandon-fryslie/low-talker/pull/154)–[#156](https://github.com/brandon-fryslie/low-talker/pull/156)); Realtime socket outbox bounded, streamed-latency test on driven clock, start-over test keeps pace with engine ([#157](https://github.com/brandon-fryslie/low-talker/pull/157)–[#159](https://github.com/brandon-fryslie/low-talker/pull/159)); command mode leaves the code — an utterance becomes one thing, its text at the cursor ([#160](https://github.com/brandon-fryslie/low-talker/pull/160)); status icon, HUD with listening/transcribing, Open at Login, config file follows saves ([#161](https://github.com/brandon-fryslie/low-talker/pull/161)–[#164](https://github.com/brandon-fryslie/low-talker/pull/164)); Fn/Globe as the chord, key-up timing, modifier change dating, confirm-timer handler isolation ([#165](https://github.com/brandon-fryslie/low-talker/pull/165)–[#168](https://github.com/brandon-fryslie/low-talker/pull/168)); audio under audible floor answered as nothing said; verbose_json serves avg_logprob and compression_ratio; the release workflow notarizes with existing Apple ID credentials ([#169](https://github.com/brandon-fryslie/low-talker/pull/169), [#170](https://github.com/brandon-fryslie/low-talker/pull/170), [#171](https://github.com/brandon-fryslie/low-talker/pull/171)) ([commits](https://github.com/brandon-fryslie/low-talker/commits?author=brandon-fryslie&since=2026-09-30)).
- `brandon-fryslie/rich-js` — 99 commits: table arc — mins cut as Rich cuts, RichText title keeps its own style, NaN bounds and fractional ties ([#282](https://github.com/brandon-fryslie/rich-js/pull/282), [#299](https://github.com/brandon-fryslie/rich-js/pull/299), [#329](https://github.com/brandon-fryslie/rich-js/pull/329), [#335](https://github.com/brandon-fryslie/rich-js/pull/335)); progress arc — TaskProgressColumn rounds as Python, MofNCompleteColumn pads styled, ProgressBar half cells ([#331](https://github.com/brandon-fryslie/rich-js/pull/331)–[#333](https://github.com/brandon-fryslie/rich-js/pull/333)); 0.19.0 released ([#337](https://github.com/brandon-fryslie/rich-js/pull/337)); highlighter rewrites — JSONHighlighter, ISO8601Highlighter, ReprHighlighter draw Rich's spans and colours in one pass ([#309](https://github.com/brandon-fryslie/rich-js/pull/309), [#321](https://github.com/brandon-fryslie/rich-js/pull/321), [#323](https://github.com/brandon-fryslie/rich-js/pull/323), [#325](https://github.com/brandon-fryslie/rich-js/pull/325)); effects arc — Effected, effects-feel demo of breath, fireflies, shimmer, dissolve, a sigh ([#311](https://github.com/brandon-fryslie/rich-js/pull/311), [#318](https://github.com/brandon-fryslie/rich-js/pull/318), [#322](https://github.com/brandon-fryslie/rich-js/pull/322), [#324](https://github.com/brandon-fryslie/rich-js/pull/324), [#326](https://github.com/brandon-fryslie/rich-js/pull/326), [#330](https://github.com/brandon-fryslie/rich-js/pull/330)); markdown — list items hold blocks, h1 centred, inline links; Prompt matches Rich; contrast holds where promised ([#293](https://github.com/brandon-fryslie/rich-js/pull/293), [#297](https://github.com/brandon-fryslie/rich-js/pull/297), [#300](https://github.com/brandon-fryslie/rich-js/pull/300), [#301](https://github.com/brandon-fryslie/rich-js/pull/301)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-09-30)).
- `promptctl/cc-candybar` — 30 commits: edit mode — segment library add menu, save/cancel, add/remove buttons ([#290](https://github.com/promptctl/cc-candybar/pull/290), [#292](https://github.com/promptctl/cc-candybar/pull/292), [#293](https://github.com/promptctl/cc-candybar/pull/293)); live bar on GitHub Pages replays Claude turns, pnpm bar:web for a browser terminal ([#296](https://github.com/promptctl/cc-candybar/pull/296), [#297](https://github.com/promptctl/cc-candybar/pull/297)); session's Claude Code read, not daemon's env ([#299](https://github.com/promptctl/cc-candybar/pull/299)); doctor checks that config is correct and URL handler works ([#311](https://github.com/promptctl/cc-candybar/pull/311), [#314](https://github.com/promptctl/cc-candybar/pull/314)); a no-fill cell's unauthored text is the terminal's own ([#291](https://github.com/promptctl/cc-candybar/pull/291)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-09-30)).
- `brandon-fryslie/gh-pages-multiplexer` — 16 commits: new repo stood up — concurrent deploys rebuild from the new tip, per-slot concurrency groups, token kept out of process args and .git/config, publish retries bounded by deadline ([#1](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/1)–[#5](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/5)) ([commits](https://github.com/brandon-fryslie/gh-pages-multiplexer/commits?author=brandon-fryslie&since=2026-09-30)).
- `promptctl/laws` — 11 commits: observability on-ramp specifies end state, floor and default fields ([#81](https://github.com/promptctl/laws/pull/81)); `[LAW:domain-language]` prose/spec/application-spec pass ([#84](https://github.com/promptctl/laws/pull/84), [#85](https://github.com/promptctl/laws/pull/85)); per-law eval harness, run-record schema, no-silent-failure baseline ([#86](https://github.com/promptctl/laws/pull/86)); one Claude Code harness from isolation+driver with hold-out controls ([#88](https://github.com/promptctl/laws/pull/88), [#94](https://github.com/promptctl/laws/pull/94)); rung profiles, S/M projections ([#90](https://github.com/promptctl/laws/pull/90), [#91](https://github.com/promptctl/laws/pull/91)); 0.35.0 released with consumers-by-hold model ([#92](https://github.com/promptctl/laws/pull/92)); review-audit of promptctl PR review rounds ([#93](https://github.com/promptctl/laws/pull/93)) ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-09-30)).
- `promptctl/homebrew-tap` — 8 commits: scheduled vhid cask sync, vhid workflow added and gated to manual trigger ([#1](https://github.com/promptctl/homebrew-tap/pull/1), [#3](https://github.com/promptctl/homebrew-tap/pull/3), [#4](https://github.com/promptctl/homebrew-tap/pull/4)) ([commits](https://github.com/promptctl/homebrew-tap/commits?author=brandon-fryslie&since=2026-09-30)).
- `promptctl/tmux-phoenix` — 5 commits: tmux-control's `Connection::open`, owned reader, typed targets ([#20](https://github.com/promptctl/tmux-phoenix/pull/20)); phoenix-core/capture/store windows-and-winlinks graph with reasoned absences and exact argv ([#21](https://github.com/promptctl/tmux-phoenix/pull/21)); phoenix-store reads take no lock ([#22](https://github.com/promptctl/tmux-phoenix/pull/22)); phoenix-restore plan over symbolic refs, apply binds ids ([#23](https://github.com/promptctl/tmux-phoenix/pull/23)) ([commits](https://github.com/promptctl/tmux-phoenix/commits?author=brandon-fryslie&since=2026-09-30)).
- `brandon-fryslie/dotfiles` — 2 commits ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-09-30)).
- `brandon-fryslie/swe4vibe-lab` — 2 commits ([commits](https://github.com/brandon-fryslie/swe4vibe-lab/commits?author=brandon-fryslie&since=2026-09-30)).

### This Month

Top repos by Brandon's commit volume over the past 30 days:

- [`promptctl/vhid`](https://github.com/promptctl/vhid) — 305 commits
- [`brandon-fryslie/cc-hands`](https://github.com/brandon-fryslie/cc-hands) — 208
- [`brandon-fryslie/low-talker`](https://github.com/brandon-fryslie/low-talker) — 205
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 151
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 65
- [`brandon-fryslie/gh-pages-multiplexer`](https://github.com/brandon-fryslie/gh-pages-multiplexer) — 16
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 13
- [`promptctl/laws`](https://github.com/promptctl/laws) — 12
- [`promptctl/homebrew-tap`](https://github.com/promptctl/homebrew-tap) — 8
- [`promptctl/tmux-phoenix`](https://github.com/promptctl/tmux-phoenix) — 5

Languages: Swift, Python, TypeScript, Go, Shell.

---

<details>
<summary>Previous highlights</summary>

- [2026-10-06](./daily-archive/2026-10-06.md)
- [2026-10-03](./daily-archive/2026-10-03.md)
- [2026-10-02](./daily-archive/2026-10-02.md)
- [2026-10-01](./daily-archive/2026-10-01.md)
- [2026-09-30](./daily-archive/2026-09-30.md)
- [2026-09-29](./daily-archive/2026-09-29.md)
- [2026-09-28](./daily-archive/2026-09-28.md)

</details>

<!-- RECENT-ACTIVITY:END -->

<!-- PREVIOUS-WORK:START -->

### Previous Engineering Work

- **[Week of September 28](./previous-work/2026/2026-09-28.md)** — *in progress*
- **[Week of September 21](./previous-work/2026/2026-09-21.md)** — *in progress*
- **[Week of September 14](./previous-work/2026/2026-09-14.md)** — *in progress*
- **[Week of September 7](./previous-work/2026/2026-09-07.md)** — elvenspeak stub-fleet router and Dockerfile publish gate · rich-js JSON and print fidelity · lit rename and plugin cleanup · memento 0.6–0.7 ceiling collapse
- **[Week of August 17](./previous-work/2026/2026-08-17.md)** — *in progress*
- **[Week of August 10](./previous-work/2026/2026-08-10.md)** — slopspot RAG stack and freshness trail · cc-candybar per-segment palette overrides · lit sync safety and licensing clean-room · cc-dump Anthropic-only proxy consolidation
- **[Week of August 3](./previous-work/2026/2026-08-03.md)** — lit workflows 0.4.0 · cc-candybar option-domain seam and theme picker · slopspot-paste editor made editable end-to-end · room-eq-wizard-mcp surface completion

[Full archive →](./previous-work/)

<!-- PREVIOUS-WORK:END -->

---

## Selected Projects

<!-- SELECTED-PROJECTS:START -->
<table>
<tr>
<td width="50%" valign="top">

### [vhid](https://github.com/promptctl/vhid)
**Swift · Apache-2.0 · 1★**

A virtual keyboard and a virtual mouse for macOS, driven from a CLI or over MCP. Real HID devices through the pqrs DriverKit extension — no event taps, no Accessibility grant. 305 commits over the past month, 248 this week. The human-hands epic landed — pointer moves follow a Fitts-length minimum-jerk path, steered on a learned acceleration curve, with overshoot, a bow away from the elbow, and a 7–13 Hz tremor fading in and out ([#149](https://github.com/promptctl/vhid/pull/149), [#150](https://github.com/promptctl/vhid/pull/150), [#159](https://github.com/promptctl/vhid/pull/159)); clicks rest before pressing, hold the button, and space a double-click like a hand, aiming inside a box timed by Fitts' law ([#151](https://github.com/promptctl/vhid/pull/151), [#158](https://github.com/promptctl/vhid/pull/158)); typing and chords keep a typist's cadence, coming in bursts with rollover ([#152](https://github.com/promptctl/vhid/pull/152), [#156](https://github.com/promptctl/vhid/pull/156)); click and key-repeat timings read the HID system's one setting ([#153](https://github.com/promptctl/vhid/pull/153)); the design note, probe page, and a live record on studious close the loop ([#148](https://github.com/promptctl/vhid/pull/148), [#154](https://github.com/promptctl/vhid/pull/154), [#161](https://github.com/promptctl/vhid/pull/161)). Earlier this week 0.4.0 and 0.4.1 shipped with Homebrew distribution ([#135](https://github.com/promptctl/vhid/pull/135)–[#140](https://github.com/promptctl/vhid/pull/140)); observability leaves one record per verb ([#142](https://github.com/promptctl/vhid/pull/142), [#144](https://github.com/promptctl/vhid/pull/144), [#146](https://github.com/promptctl/vhid/pull/146)).

### [cc-hands](https://github.com/brandon-fryslie/cc-hands)
**Python**

Voice for Claude Code — speak to a session over a chord, hear its reply, run a brain that holds its own account on a dedicated Claude Code behind the proxy. 208 commits over the past month, 195 this week, 36 landed in the last 24 hours. The tmux arc landed — hands starts a session in a tmux window and reads its pane screen through the socket the window was opened on ([#242](https://github.com/brandon-fryslie/cc-hands/pull/242), [#256](https://github.com/brandon-fryslie/cc-hands/pull/256), [#257](https://github.com/brandon-fryslie/cc-hands/pull/257)); a pane is typed into only while it is in front of its session ([#258](https://github.com/brandon-fryslie/cc-hands/pull/258)); close-session sends SIGTERM, closes a window hands opened, and leaves a user shell ([#262](https://github.com/brandon-fryslie/cc-hands/pull/262)); a session delegating to a background subagent reads as still at work ([#263](https://github.com/brandon-fryslie/cc-hands/pull/263)–[#265](https://github.com/brandon-fryslie/cc-hands/pull/265)). The brain takes any Anthropic login Claude Code takes, reads its own token usage off the wire, resumes conversation across restarts, and picks model and personality from config.toml ([#233](https://github.com/brandon-fryslie/cc-hands/pull/233), [#236](https://github.com/brandon-fryslie/cc-hands/pull/236), [#237](https://github.com/brandon-fryslie/cc-hands/pull/237), [#240](https://github.com/brandon-fryslie/cc-hands/pull/240), [#249](https://github.com/brandon-fryslie/cc-hands/pull/249)). A conversation page shows what was said and called ([#239](https://github.com/brandon-fryslie/cc-hands/pull/239)); hands plays Spotify ([#241](https://github.com/brandon-fryslie/cc-hands/pull/241)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — fork of `@owloops/claude-powerline` with CLI override flags so the entire config can live in `settings.json`. 65 commits over the past month, 30 this week. The edit mode landed — segment library add menu, save/cancel, add/remove buttons ([#290](https://github.com/promptctl/cc-candybar/pull/290), [#292](https://github.com/promptctl/cc-candybar/pull/292), [#293](https://github.com/promptctl/cc-candybar/pull/293)); a live bar on GitHub Pages replays Claude turns, pnpm bar:web for a browser terminal ([#296](https://github.com/promptctl/cc-candybar/pull/296), [#297](https://github.com/promptctl/cc-candybar/pull/297)); session's Claude Code read, not daemon's env ([#299](https://github.com/promptctl/cc-candybar/pull/299)); doctor checks that config is correct and URL handler works ([#311](https://github.com/promptctl/cc-candybar/pull/311), [#314](https://github.com/promptctl/cc-candybar/pull/314)); a no-fill cell's unauthored text is the terminal's own ([#291](https://github.com/promptctl/cc-candybar/pull/291)).

</td>
<td width="50%" valign="top">

### [low-talker](https://github.com/brandon-fryslie/low-talker)
**Swift**

Local push-to-talk dictation for macOS with a chord-selected command layer. 205 commits over the past month, 122 this week. The streaming arc landed — a press is decoded while the key is down, confirmed words commit while the press is open, dictation stays in the app its first words reached, streamed commits wait for settled punctuation ([#150](https://github.com/brandon-fryslie/low-talker/pull/150)–[#153](https://github.com/brandon-fryslie/low-talker/pull/153)); command mode leaves the code — an utterance becomes one thing, its text at the cursor ([#160](https://github.com/brandon-fryslie/low-talker/pull/160)); a status icon, a HUD with listening/transcribing, and Open at Login ([#161](https://github.com/brandon-fryslie/low-talker/pull/161)–[#164](https://github.com/brandon-fryslie/low-talker/pull/164)); Fn/Globe as the chord, with modifier-change dating and confirm-timer handler isolation ([#165](https://github.com/brandon-fryslie/low-talker/pull/165)–[#168](https://github.com/brandon-fryslie/low-talker/pull/168)); audio under the audible floor is answered as nothing said, verbose_json serves avg_logprob and compression_ratio, release workflow notarizes with existing Apple ID credentials ([#169](https://github.com/brandon-fryslie/low-talker/pull/169), [#170](https://github.com/brandon-fryslie/low-talker/pull/170), [#171](https://github.com/brandon-fryslie/low-talker/pull/171)).

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript · MIT**

A port of Python's Rich to TypeScript — markup, tables, trees, syntax, progress, tracebacks, Live, and an App runtime that routes focus and the pointer. 151 commits over the past month, 99 this week, with `0.19.0` released ([#337](https://github.com/brandon-fryslie/rich-js/pull/337)). The highlighter rewrite — JSONHighlighter, ISO8601Highlighter and ReprHighlighter draw Rich's spans and colours in one pass over long runs ([#309](https://github.com/brandon-fryslie/rich-js/pull/309), [#321](https://github.com/brandon-fryslie/rich-js/pull/321), [#323](https://github.com/brandon-fryslie/rich-js/pull/323), [#325](https://github.com/brandon-fryslie/rich-js/pull/325)); the table arc — mins cut as Rich cuts, RichText title keeps its own style, NaN bounds and fractional ties handled ([#282](https://github.com/brandon-fryslie/rich-js/pull/282), [#299](https://github.com/brandon-fryslie/rich-js/pull/299), [#329](https://github.com/brandon-fryslie/rich-js/pull/329), [#335](https://github.com/brandon-fryslie/rich-js/pull/335)); the progress arc — TaskProgressColumn rounds as Python, MofNCompleteColumn pads styled, ProgressBar half cells ([#331](https://github.com/brandon-fryslie/rich-js/pull/331)–[#333](https://github.com/brandon-fryslie/rich-js/pull/333)); the effects arc — Effected, and a feel demo of breath, fireflies, shimmer, dissolve, and a sigh that catches on the way in ([#311](https://github.com/brandon-fryslie/rich-js/pull/311), [#318](https://github.com/brandon-fryslie/rich-js/pull/318), [#322](https://github.com/brandon-fryslie/rich-js/pull/322), [#324](https://github.com/brandon-fryslie/rich-js/pull/324), [#326](https://github.com/brandon-fryslie/rich-js/pull/326), [#330](https://github.com/brandon-fryslie/rich-js/pull/330)).

### [gh-pages-multiplexer](https://github.com/brandon-fryslie/gh-pages-multiplexer)
**TypeScript**

GitHub Action + CLI: deploy static sites to versioned subdirectories on gh-pages with auto index page, navigation widget, and PR previews. New repo, 16 commits in the past day. Concurrent deploys rebuild from the probed tip instead of rebasing, with a worktree life-cycle and classified rejections ([#1](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/1)); the deploy concurrency group is keyed per version slot so a PR run no longer cancels a pending main deploy ([#2](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/2)); the test suite was reconciled with Node 26's localStorage shadowing and a 150-commit fixture built with git fast-import ([#3](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/3)); the token is kept out of the process table and `.git/config` — authentication by env-scoped header, no credential helper ([#4](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/4)); publish retries are bounded by a 10-minute deadline, retrying only while the tip moves ([#5](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/5)).

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
