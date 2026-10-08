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

Fourteen PRs into `rich-js` today, and they share a shape: a byte-for-byte reconciliation with Python's Rich. A progress column drawn in a theme key Rich never used. A rule title that lost its own justify on the way through. A ProgressBar colour named `magenta` where Rich's `rgb(249,38,114)` is specific. The port has been close to Rich for a while; today was closing the last millimetre.

The `ProgressBar`'s `pulse` finally animates — stored as a flag that nothing read, now a shimmer over `bar.back` lifted toward `bar.pulse` on the library's own clock. First thing in there that moves on its own.

`vhid` landed one PR — every rectangle `eyes` prints now spells itself `x,y,width,height`, the form `--rect` takes. `cc-hands` deleted its Anthropic and OpenAI backends: the brain is a Claude Code it runs, and that is all. Brandon let both breaking changes through without comment. A tidy day — millimetric, which `rich-js` seems to have earned a season of.

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

*Updated October 8, 2026*

### Last 24 Hours

- `brandon-fryslie/rich-js` — 14 PRs merged: effect catalogue promoted to `src/` with a docs page ([#338](https://github.com/brandon-fryslie/rich-js/pull/338)); one concurrency group per docs slot, pinned to multiplexer v1.1.0 ([#336](https://github.com/brandon-fryslie/rich-js/pull/336)); 20-minute timeout on every CI job that runs the gate ([#339](https://github.com/brandon-fryslie/rich-js/pull/339)); ProgressBar's pulse animates on the library's own clock, lifted toward `bar.pulse` through Effected ([#340](https://github.com/brandon-fryslie/rich-js/pull/340)); Effected merges cells on what the depth writes ([#341](https://github.com/brandon-fryslie/rich-js/pull/341)); a terminal-supplied colour takes no subject's share in effects ([#342](https://github.com/brandon-fryslie/rich-js/pull/342)); Rule draws line in `rule.line` and title in `rule.text`, as Rich does ([#343](https://github.com/brandon-fryslie/rich-js/pull/343)); pretty quotes a key that is not a name or an index, as Rich reprs it ([#344](https://github.com/brandon-fryslie/rich-js/pull/344)); effects-feel reads a strip's text cells off the render its colours come from ([#345](https://github.com/brandon-fryslie/rich-js/pull/345)); ProgressBar in Rich's rgb colours ([#346](https://github.com/brandon-fryslie/rich-js/pull/346)); a given `completed` wins over `advance` in `updateTask` ([#347](https://github.com/brandon-fryslie/rich-js/pull/347)); a RichText title's own justify outranks `titleJustify` ([#348](https://github.com/brandon-fryslie/rich-js/pull/348)); site xterm.js 5.3 → `@xterm/xterm` 6, synchronized-output shim removed ([#349](https://github.com/brandon-fryslie/rich-js/pull/349)); `progress.percentage` magenta and `progress.elapsed` yellow, as Rich's ([#350](https://github.com/brandon-fryslie/rich-js/pull/350)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-10-07)).
- `brandon-fryslie/cc-hands` — 3 PRs merged: hands reaches its model only through the brain — the keyed Anthropic and OpenAI backends gone, two prompts and two summarisers collapsed into one ([#268](https://github.com/brandon-fryslie/cc-hands/pull/268)); a command Claude Code carries out itself is over once it printed, so `/model` and friends no longer leave a turn open ([#266](https://github.com/brandon-fryslie/cc-hands/pull/266)); a pause between words stays inside the speech, not a stop Smart Turn judges ([#267](https://github.com/brandon-fryslie/cc-hands/pull/267)) ([commits](https://github.com/brandon-fryslie/cc-hands/commits?author=brandon-fryslie&since=2026-10-07)).
- `promptctl/vhid` — 1 PR merged: every rectangle `eyes` prints takes the form `--rect` takes — windows' and displays' bounds and the scope line's region join the row's box, read back by one parser ([#162](https://github.com/promptctl/vhid/pull/162)) ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-10-07)).

### This Week

- `promptctl/vhid` — 253 commits: human-hands epic — pointer moves follow a Fitts-length minimum-jerk path with overshoot, bow and tremor; clicks aim inside a box; typing comes in bursts with rollover; a design note, a probe page, and a live record of every verb on studious ([#148](https://github.com/promptctl/vhid/pull/148)–[#154](https://github.com/promptctl/vhid/pull/154), [#156](https://github.com/promptctl/vhid/pull/156)–[#161](https://github.com/promptctl/vhid/pull/161)); every rectangle `eyes` prints takes the `--rect` form ([#162](https://github.com/promptctl/vhid/pull/162)); 0.4.1 shipped and the Homebrew distribution route landed — pkg and cask, a published release moves cask in the same run ([#135](https://github.com/promptctl/vhid/pull/135)–[#140](https://github.com/promptctl/vhid/pull/140)); release-path law pass and 10-minute release budget ([#133](https://github.com/promptctl/vhid/pull/133), [#145](https://github.com/promptctl/vhid/pull/145)); observability — every verb leaves one record, Control-C or SIGTERM leaves a cancelled record ([#142](https://github.com/promptctl/vhid/pull/142), [#144](https://github.com/promptctl/vhid/pull/144), [#146](https://github.com/promptctl/vhid/pull/146)); `vhid scroll --vertical N` rolls N notches per report ([#141](https://github.com/promptctl/vhid/pull/141)); a merged read leaves the region to its readers ([#143](https://github.com/promptctl/vhid/pull/143)); docs broken into layers by reader ([#147](https://github.com/promptctl/vhid/pull/147)); a daemon whose file was replaced refuses to start a reader of another build ([#155](https://github.com/promptctl/vhid/pull/155)) ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-10-01)).
- `brandon-fryslie/cc-hands` — 186 commits: tmux arc — hands starts and reads sessions through their panes, types into panes only while they're in front, closes sessions via SIGTERM with window ownership ([#242](https://github.com/brandon-fryslie/cc-hands/pull/242), [#256](https://github.com/brandon-fryslie/cc-hands/pull/256)–[#265](https://github.com/brandon-fryslie/cc-hands/pull/265)); raw-api — hands reaches its model only through the brain, the keyed Anthropic and OpenAI backends gone ([#268](https://github.com/brandon-fryslie/cc-hands/pull/268)); brain arc — takes any Anthropic login Claude Code takes, reads its own token usage off the wire, resumes conversation across restarts, picks model and personality from config ([#233](https://github.com/brandon-fryslie/cc-hands/pull/233), [#236](https://github.com/brandon-fryslie/cc-hands/pull/236), [#237](https://github.com/brandon-fryslie/cc-hands/pull/237), [#240](https://github.com/brandon-fryslie/cc-hands/pull/240), [#249](https://github.com/brandon-fryslie/cc-hands/pull/249)); a conversation page shows what was said and called ([#239](https://github.com/brandon-fryslie/cc-hands/pull/239)); Spotify playback, keyed Anthropic prompt caching, summariser usage events ([#241](https://github.com/brandon-fryslie/cc-hands/pull/241), [#252](https://github.com/brandon-fryslie/cc-hands/pull/252), [#253](https://github.com/brandon-fryslie/cc-hands/pull/253)); status corrections — a self-run command is over once it printed, a background subagent reads as working, a pause between words no longer ends the turn ([#263](https://github.com/brandon-fryslie/cc-hands/pull/263), [#266](https://github.com/brandon-fryslie/cc-hands/pull/266), [#267](https://github.com/brandon-fryslie/cc-hands/pull/267)); design docs on what a packaged hands can and cannot sell ([#243](https://github.com/brandon-fryslie/cc-hands/pull/243), [#246](https://github.com/brandon-fryslie/cc-hands/pull/246)) ([commits](https://github.com/brandon-fryslie/cc-hands/commits?author=brandon-fryslie&since=2026-10-01)).
- `brandon-fryslie/low-talker` — 92 commits: streaming arc — a press is decoded while the key is down, confirmed words commit while the press is open, dictation stays in the app its first words reached, streamed commits wait for settled punctuation ([#150](https://github.com/brandon-fryslie/low-talker/pull/150)–[#153](https://github.com/brandon-fryslie/low-talker/pull/153)); the build's model jobs run on model-tool, bench runs from the menu-bar app, lowtalker CLI deleted ([#154](https://github.com/brandon-fryslie/low-talker/pull/154)–[#156](https://github.com/brandon-fryslie/low-talker/pull/156)); Realtime socket outbox bounded, streamed-latency test on driven clock, start-over test keeps pace with engine ([#157](https://github.com/brandon-fryslie/low-talker/pull/157)–[#159](https://github.com/brandon-fryslie/low-talker/pull/159)); command mode leaves the code — an utterance becomes one thing, its text at the cursor ([#160](https://github.com/brandon-fryslie/low-talker/pull/160)); status icon, HUD with listening/transcribing, Open at Login, config file follows saves ([#161](https://github.com/brandon-fryslie/low-talker/pull/161)–[#164](https://github.com/brandon-fryslie/low-talker/pull/164)); Fn/Globe as the chord, key-up timing, modifier change dating, confirm-timer handler isolation ([#165](https://github.com/brandon-fryslie/low-talker/pull/165)–[#168](https://github.com/brandon-fryslie/low-talker/pull/168)); audio under audible floor answered as nothing said; verbose_json serves avg_logprob and compression_ratio; the release workflow notarizes with existing Apple ID credentials ([#169](https://github.com/brandon-fryslie/low-talker/pull/169), [#170](https://github.com/brandon-fryslie/low-talker/pull/170), [#171](https://github.com/brandon-fryslie/low-talker/pull/171)) ([commits](https://github.com/brandon-fryslie/low-talker/commits?author=brandon-fryslie&since=2026-10-01)).
- `brandon-fryslie/rich-js` — 66 commits: byte-for-byte reconciliation with Python's Rich across progress, table, rule, pretty, highlighter and effects — a given completed wins over advance, a RichText title's own justify outranks `titleJustify`, Rule's line and title read `rule.line` and `rule.text`, ProgressBar draws in Rich's rgb colours, `progress.percentage`/`progress.elapsed` theme keys fixed ([#346](https://github.com/brandon-fryslie/rich-js/pull/346)–[#348](https://github.com/brandon-fryslie/rich-js/pull/348), [#343](https://github.com/brandon-fryslie/rich-js/pull/343), [#344](https://github.com/brandon-fryslie/rich-js/pull/344), [#347](https://github.com/brandon-fryslie/rich-js/pull/347), [#350](https://github.com/brandon-fryslie/rich-js/pull/350)); ProgressBar's pulse animates on the library's own clock through Effected, the effect catalogue promoted to `src/` with a docs page ([#338](https://github.com/brandon-fryslie/rich-js/pull/338), [#340](https://github.com/brandon-fryslie/rich-js/pull/340), [#341](https://github.com/brandon-fryslie/rich-js/pull/341), [#342](https://github.com/brandon-fryslie/rich-js/pull/342), [#345](https://github.com/brandon-fryslie/rich-js/pull/345)); 0.19.0 shipped ([#337](https://github.com/brandon-fryslie/rich-js/pull/337)); CI jobs bounded at 20 minutes, docs deploys per-slot concurrency ([#336](https://github.com/brandon-fryslie/rich-js/pull/336), [#339](https://github.com/brandon-fryslie/rich-js/pull/339)); site xterm.js 5.3 → `@xterm/xterm` 6 ([#349](https://github.com/brandon-fryslie/rich-js/pull/349)); effects-feel sigh catches once, firefly halos never add ([#330](https://github.com/brandon-fryslie/rich-js/pull/330)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-10-01)).
- `promptctl/cc-candybar` — 30 commits: edit mode — segment library add menu, save/cancel, add/remove buttons ([#290](https://github.com/promptctl/cc-candybar/pull/290), [#292](https://github.com/promptctl/cc-candybar/pull/292), [#293](https://github.com/promptctl/cc-candybar/pull/293)); live bar on GitHub Pages replays Claude turns, pnpm bar:web for a browser terminal ([#296](https://github.com/promptctl/cc-candybar/pull/296), [#297](https://github.com/promptctl/cc-candybar/pull/297)); session's Claude Code read, not daemon's env ([#299](https://github.com/promptctl/cc-candybar/pull/299)); doctor checks that config is correct and URL handler works ([#311](https://github.com/promptctl/cc-candybar/pull/311), [#314](https://github.com/promptctl/cc-candybar/pull/314)); a no-fill cell's unauthored text is the terminal's own ([#291](https://github.com/promptctl/cc-candybar/pull/291)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-10-01)).
- `brandon-fryslie/gh-pages-multiplexer` — 16 commits: new repo stood up — concurrent deploys rebuild from the new tip, per-slot concurrency groups, token kept out of process args and `.git/config`, publish retries bounded by deadline ([#1](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/1)–[#5](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/5)) ([commits](https://github.com/brandon-fryslie/gh-pages-multiplexer/commits?author=brandon-fryslie&since=2026-10-01)).
- `promptctl/laws` — 11 commits: `[LAW:domain-language]` prose/spec/application-spec pass ([#84](https://github.com/promptctl/laws/pull/84), [#85](https://github.com/promptctl/laws/pull/85)); per-law eval harness, run-record schema, no-silent-failure baseline ([#86](https://github.com/promptctl/laws/pull/86)); one Claude Code harness from isolation+driver with hold-out controls ([#88](https://github.com/promptctl/laws/pull/88), [#94](https://github.com/promptctl/laws/pull/94)); rung profiles, S/M projections ([#90](https://github.com/promptctl/laws/pull/90), [#91](https://github.com/promptctl/laws/pull/91)); 0.35.0 released with consumers-by-hold model ([#92](https://github.com/promptctl/laws/pull/92)); review-audit of promptctl PR review rounds ([#93](https://github.com/promptctl/laws/pull/93)) ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-10-01)).
- `promptctl/homebrew-tap` — 8 commits: scheduled vhid cask sync, vhid workflow added and gated to manual trigger ([#1](https://github.com/promptctl/homebrew-tap/pull/1), [#3](https://github.com/promptctl/homebrew-tap/pull/3), [#4](https://github.com/promptctl/homebrew-tap/pull/4)) ([commits](https://github.com/promptctl/homebrew-tap/commits?author=brandon-fryslie&since=2026-10-01)).
- `promptctl/tmux-phoenix` — 5 commits: tmux-control's `Connection::open`, owned reader, typed targets ([#20](https://github.com/promptctl/tmux-phoenix/pull/20)); phoenix-core/capture/store windows-and-winlinks graph with reasoned absences and exact argv ([#21](https://github.com/promptctl/tmux-phoenix/pull/21)); phoenix-store reads take no lock ([#22](https://github.com/promptctl/tmux-phoenix/pull/22)); phoenix-restore plan over symbolic refs, apply binds ids ([#23](https://github.com/promptctl/tmux-phoenix/pull/23)) ([commits](https://github.com/promptctl/tmux-phoenix/commits?author=brandon-fryslie&since=2026-10-01)).
- `brandon-fryslie/dotfiles` — 2 commits ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-10-01)).
- `brandon-fryslie/swe4vibe-lab` — 2 commits ([commits](https://github.com/brandon-fryslie/swe4vibe-lab/commits?author=brandon-fryslie&since=2026-10-01)).

### This Month

Top repos by Brandon's commit volume over the past 30 days:

- [`promptctl/vhid`](https://github.com/promptctl/vhid) — 302 commits
- [`brandon-fryslie/cc-hands`](https://github.com/brandon-fryslie/cc-hands) — 211
- [`brandon-fryslie/low-talker`](https://github.com/brandon-fryslie/low-talker) — 202
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 164
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 64
- [`brandon-fryslie/gh-pages-multiplexer`](https://github.com/brandon-fryslie/gh-pages-multiplexer) — 16
- [`promptctl/laws`](https://github.com/promptctl/laws) — 11
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 10
- [`promptctl/homebrew-tap`](https://github.com/promptctl/homebrew-tap) — 8
- [`promptctl/tmux-phoenix`](https://github.com/promptctl/tmux-phoenix) — 5

Languages: Swift, Python, TypeScript, Go, Shell.

---

<details>
<summary>Previous highlights</summary>

- [2026-10-07](./daily-archive/2026-10-07.md)
- [2026-10-06](./daily-archive/2026-10-06.md)
- [2026-10-03](./daily-archive/2026-10-03.md)
- [2026-10-02](./daily-archive/2026-10-02.md)
- [2026-10-01](./daily-archive/2026-10-01.md)
- [2026-09-30](./daily-archive/2026-09-30.md)
- [2026-09-29](./daily-archive/2026-09-29.md)

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

A virtual keyboard and a virtual mouse for macOS, driven from a CLI or over MCP. Real HID devices through the pqrs DriverKit extension — no event taps, no Accessibility grant. 302 commits over the past month, 253 this week. The human-hands epic landed — pointer moves follow a Fitts-length minimum-jerk path, steered on a learned acceleration curve, with overshoot, a bow away from the elbow, and a 7–13 Hz tremor fading in and out ([#149](https://github.com/promptctl/vhid/pull/149), [#150](https://github.com/promptctl/vhid/pull/150), [#159](https://github.com/promptctl/vhid/pull/159)); clicks rest before pressing, hold the button, and space a double-click like a hand, aiming inside a box timed by Fitts' law ([#151](https://github.com/promptctl/vhid/pull/151), [#158](https://github.com/promptctl/vhid/pull/158)); typing and chords keep a typist's cadence, coming in bursts with rollover ([#152](https://github.com/promptctl/vhid/pull/152), [#156](https://github.com/promptctl/vhid/pull/156)); click and key-repeat timings read the HID system's one setting ([#153](https://github.com/promptctl/vhid/pull/153)); the design note, probe page, and a live record on studious close the loop ([#148](https://github.com/promptctl/vhid/pull/148), [#154](https://github.com/promptctl/vhid/pull/154), [#161](https://github.com/promptctl/vhid/pull/161)). Earlier this week 0.4.0 and 0.4.1 shipped with Homebrew distribution ([#135](https://github.com/promptctl/vhid/pull/135)–[#140](https://github.com/promptctl/vhid/pull/140)); every rectangle `eyes` prints now takes the `--rect` form ([#162](https://github.com/promptctl/vhid/pull/162)).

### [cc-hands](https://github.com/brandon-fryslie/cc-hands)
**Python**

Voice for Claude Code — speak to a session over a chord, hear its reply, run a brain that holds its own account on a dedicated Claude Code behind the proxy. 211 commits over the past month, 186 this week. The tmux arc landed — hands starts a session in a tmux window and reads its pane screen through the socket the window was opened on ([#242](https://github.com/brandon-fryslie/cc-hands/pull/242), [#256](https://github.com/brandon-fryslie/cc-hands/pull/256), [#257](https://github.com/brandon-fryslie/cc-hands/pull/257)); a pane is typed into only while it is in front of its session ([#258](https://github.com/brandon-fryslie/cc-hands/pull/258)); close-session sends SIGTERM, closes a window hands opened, and leaves a user shell ([#262](https://github.com/brandon-fryslie/cc-hands/pull/262)); a session delegating to a background subagent reads as still at work ([#263](https://github.com/brandon-fryslie/cc-hands/pull/263)–[#265](https://github.com/brandon-fryslie/cc-hands/pull/265)). The brain takes any Anthropic login Claude Code takes, reads its own token usage off the wire, resumes conversation across restarts, and picks model and personality from config.toml ([#233](https://github.com/brandon-fryslie/cc-hands/pull/233), [#236](https://github.com/brandon-fryslie/cc-hands/pull/236), [#237](https://github.com/brandon-fryslie/cc-hands/pull/237), [#240](https://github.com/brandon-fryslie/cc-hands/pull/240), [#249](https://github.com/brandon-fryslie/cc-hands/pull/249)). Today the keyed Anthropic and OpenAI backends were deleted — hands reaches its model only through the brain ([#268](https://github.com/brandon-fryslie/cc-hands/pull/268)); a self-run slash command is over once it printed, and a pause between words no longer ends the turn ([#266](https://github.com/brandon-fryslie/cc-hands/pull/266), [#267](https://github.com/brandon-fryslie/cc-hands/pull/267)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — fork of `@owloops/claude-powerline` with CLI override flags so the entire config can live in `settings.json`. 64 commits over the past month, 30 this week. The edit mode landed — segment library add menu, save/cancel, add/remove buttons ([#290](https://github.com/promptctl/cc-candybar/pull/290), [#292](https://github.com/promptctl/cc-candybar/pull/292), [#293](https://github.com/promptctl/cc-candybar/pull/293)); a live bar on GitHub Pages replays Claude turns, pnpm bar:web for a browser terminal ([#296](https://github.com/promptctl/cc-candybar/pull/296), [#297](https://github.com/promptctl/cc-candybar/pull/297)); session's Claude Code read, not daemon's env ([#299](https://github.com/promptctl/cc-candybar/pull/299)); doctor checks that config is correct and URL handler works ([#311](https://github.com/promptctl/cc-candybar/pull/311), [#314](https://github.com/promptctl/cc-candybar/pull/314)); a no-fill cell's unauthored text is the terminal's own ([#291](https://github.com/promptctl/cc-candybar/pull/291)).

</td>
<td width="50%" valign="top">

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript · MIT**

A port of Python's Rich to TypeScript — markup, tables, trees, syntax, progress, tracebacks, Live, and an App runtime that routes focus and the pointer. 164 commits over the past month, 66 this week, 14 PRs landed in the last 24 hours. Byte-for-byte reconciliation with Python's Rich — ProgressBar draws in Rich's rgb colours, a given `completed` wins over `advance`, Rule's line and title read `rule.line` and `rule.text`, a RichText title's own justify outranks `titleJustify`, pretty quotes keys that aren't names or indices, `progress.percentage`/`progress.elapsed` theme keys corrected ([#343](https://github.com/brandon-fryslie/rich-js/pull/343), [#344](https://github.com/brandon-fryslie/rich-js/pull/344), [#346](https://github.com/brandon-fryslie/rich-js/pull/346)–[#348](https://github.com/brandon-fryslie/rich-js/pull/348), [#350](https://github.com/brandon-fryslie/rich-js/pull/350)); the effect catalogue — Effected, shimmer, pulse, sparkle, wheel, fade and dissolve — promoted to `src/` with a docs page, and ProgressBar's pulse animates on the library's own clock ([#338](https://github.com/brandon-fryslie/rich-js/pull/338), [#340](https://github.com/brandon-fryslie/rich-js/pull/340)–[#342](https://github.com/brandon-fryslie/rich-js/pull/342), [#345](https://github.com/brandon-fryslie/rich-js/pull/345)); 0.19.0 shipped ([#337](https://github.com/brandon-fryslie/rich-js/pull/337)); CI jobs bounded at 20 minutes with per-slot docs deploys ([#336](https://github.com/brandon-fryslie/rich-js/pull/336), [#339](https://github.com/brandon-fryslie/rich-js/pull/339)); site xterm.js 5.3 → `@xterm/xterm` 6 ([#349](https://github.com/brandon-fryslie/rich-js/pull/349)).

### [low-talker](https://github.com/brandon-fryslie/low-talker)
**Swift**

Local push-to-talk dictation for macOS with a chord-selected command layer. 202 commits over the past month, 92 this week. The streaming arc landed — a press is decoded while the key is down, confirmed words commit while the press is open, dictation stays in the app its first words reached, streamed commits wait for settled punctuation ([#150](https://github.com/brandon-fryslie/low-talker/pull/150)–[#153](https://github.com/brandon-fryslie/low-talker/pull/153)); command mode leaves the code — an utterance becomes one thing, its text at the cursor ([#160](https://github.com/brandon-fryslie/low-talker/pull/160)); a status icon, a HUD with listening/transcribing, and Open at Login ([#161](https://github.com/brandon-fryslie/low-talker/pull/161)–[#164](https://github.com/brandon-fryslie/low-talker/pull/164)); Fn/Globe as the chord, with modifier-change dating and confirm-timer handler isolation ([#165](https://github.com/brandon-fryslie/low-talker/pull/165)–[#168](https://github.com/brandon-fryslie/low-talker/pull/168)); audio under the audible floor is answered as nothing said, verbose_json serves avg_logprob and compression_ratio, release workflow notarizes with existing Apple ID credentials ([#169](https://github.com/brandon-fryslie/low-talker/pull/169), [#170](https://github.com/brandon-fryslie/low-talker/pull/170), [#171](https://github.com/brandon-fryslie/low-talker/pull/171)).

### [gh-pages-multiplexer](https://github.com/brandon-fryslie/gh-pages-multiplexer)
**TypeScript**

GitHub Action + CLI: deploy static sites to versioned subdirectories on gh-pages with auto index page, navigation widget, and PR previews. New repo, 16 commits this week. Concurrent deploys rebuild from the probed tip instead of rebasing, with a worktree life-cycle and classified rejections ([#1](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/1)); the deploy concurrency group is keyed per version slot so a PR run no longer cancels a pending main deploy ([#2](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/2)); the test suite was reconciled with Node 26's localStorage shadowing and a 150-commit fixture built with git fast-import ([#3](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/3)); the token is kept out of the process table and `.git/config` — authentication by env-scoped header, no credential helper ([#4](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/4)); publish retries are bounded by a 10-minute deadline, retrying only while the tip moves ([#5](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/5)).

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
