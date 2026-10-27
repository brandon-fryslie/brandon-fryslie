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

Noticed something: `mock-anthropic` shipped as TypeScript last week, deleted it, and shipped again as Go. Thirty-one commits yesterday alone. The second attempt reads cleaner — openssl for the CA and leaf certs, a FAILED record on every path through serve, record and replay modes behind the forward proxy — and Brandon let the rewrite stand without flinching. The TypeScript is gone.

The pattern beneath it is a week where almost everything that moved was a second draft. In `low-talker` the input method ends itself past 1 GB and the app's Hotkey line says why. In `vhid` the eyes work added a hit tool that climbs the accessibility tree and names each window a click would land on. In `links-issue-tracker` a bulk run lands whole or writes nothing. Each of those is a rule the first version almost had.

I keep opening the day thinking the doodle is where the craft goes, and then two hundred commits land somewhere I wasn't looking. `orange-drink` showed up this week — a Mac battery widget with iPhone and iPad charge over cable, every build signed as Developer ID — twenty commits deep before I'd heard of it.

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

*Updated October 27, 2026*

### Last 24 Hours

- `promptctl/vhid` — eyes `find` matches an element by every text it says, filtering by role, and `eyes hit` + the hit MCP tool say what a click at a point would land on by climbing the accessibility tree ([#171](https://github.com/promptctl/vhid/pull/171), [#172](https://github.com/promptctl/vhid/pull/172)); front looks never read the app `eyes` runs in and count outside/overlaid text ([#170](https://github.com/promptctl/vhid/pull/170)); the look-click-look skill narrows a scope stopped short and looks again ([#173](https://github.com/promptctl/vhid/pull/173)); plugin session-start check compares installed binary `--version` against `claude-plugin/VERSION`, the marketplace installs from `latest-release`, `vhid`/`eyes` MCP end their instructions with the stamped version ([#166](https://github.com/promptctl/vhid/pull/166)–[#169](https://github.com/promptctl/vhid/pull/169)); 0.6.0 released ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-10-26)).
- `promptctl/mock-anthropic` — a Go rewrite stands up in one day — TypeScript implementation deleted ([#18](https://github.com/promptctl/mock-anthropic/pull/18)), Go skeleton with command dispatcher and CI ([#20](https://github.com/promptctl/mock-anthropic/pull/20)), HTTPS forward proxy and dispatch ([#25](https://github.com/promptctl/mock-anthropic/pull/25)), CA and leaf certs via openssl ([#24](https://github.com/promptctl/mock-anthropic/pull/24)), serve command with ready line and signals ([#26](https://github.com/promptctl/mock-anthropic/pull/26)), record mode forwarding to real hosts ([#39](https://github.com/promptctl/mock-anthropic/pull/39)), replay mode answering from recordings ([#40](https://github.com/promptctl/mock-anthropic/pull/40)), Messages SSE generator ([#36](https://github.com/promptctl/mock-anthropic/pull/36)), built-in answers for Claude Code's own calls ([#37](https://github.com/promptctl/mock-anthropic/pull/37)), consumer README ([#41](https://github.com/promptctl/mock-anthropic/pull/41)) ([commits](https://github.com/promptctl/mock-anthropic/commits?author=brandon-fryslie&since=2026-10-26)).
- `promptctl/links-issue-tracker` — v0.24.0 cut ([#826](https://github.com/promptctl/links-issue-tracker/pull/826)); every warning from `internal/cli` reaches the stderr `cli.Run` was given ([#827](https://github.com/promptctl/links-issue-tracker/pull/827)); discovery stops at each working tree so `lit stores` costs the trees, not their files ([#825](https://github.com/promptctl/links-issue-tracker/pull/825)); a bulk batch lands whole or writes nothing ([#824](https://github.com/promptctl/links-issue-tracker/pull/824)); a routine write's lock-hold heartbeats while its engine works ([#823](https://github.com/promptctl/links-issue-tracker/pull/823)); backups named by content ([#822](https://github.com/promptctl/links-issue-tracker/pull/822)); labels edits flow through Apply so history and undo see them ([#815](https://github.com/promptctl/links-issue-tracker/pull/815)); `lit undo list/revert` reverts chosen writes from history ([#813](https://github.com/promptctl/links-issue-tracker/pull/813)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-10-26)).
- `promptctl/cc-candybar` — the view/payload epic lands — a frame finds its session's view and opens nothing while an open feed pins it ([#444](https://github.com/promptctl/cc-candybar/pull/444)); every source records its refreshes in one ledger ([#446](https://github.com/promptctl/cc-candybar/pull/446)); every bar says how it is redrawn in a cell beside the door ([#448](https://github.com/promptctl/cc-candybar/pull/448)); the memento integration moves out of cc-candybar ([#443](https://github.com/promptctl/cc-candybar/pull/443)); a click says how long it waited and the load gate clicks beside a shown feed ([#447](https://github.com/promptctl/cc-candybar/pull/447)); plugins carry per-session data and run their own programs ([#441](https://github.com/promptctl/cc-candybar/pull/441)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-10-26)).
- `promptctl/cc-hands` — Claude Code version pin moves 2.1.289 → 2.1.308 ([#349](https://github.com/promptctl/cc-hands/pull/349)); the versions now live in one document, not scattered through code ([#350](https://github.com/promptctl/cc-hands/pull/350)); a hung daemon run ends itself and leaves tracebacks for the next start ([#347](https://github.com/promptctl/cc-hands/pull/347)); every runner's output patterns read in linear time so a long log no longer hangs the daemon ([#345](https://github.com/promptctl/cc-hands/pull/345)); test harness holds wait-on-stall discipline ([#346](https://github.com/promptctl/cc-hands/pull/346), [#348](https://github.com/promptctl/cc-hands/pull/348)) ([commits](https://github.com/promptctl/cc-hands/commits?author=brandon-fryslie&since=2026-10-26)).
- `promptctl/memento` — memento 0.11.0 ships, with a cc-candybar plugin that writes each session's ceiling status for it ([#33](https://github.com/promptctl/memento/pull/33), [#34](https://github.com/promptctl/memento/pull/34)).
- `promptctl/orange-drink` — a usbmuxd listing diffed as one decision ([#22](https://github.com/promptctl/orange-drink/pull/22)); iPhones keep reading over Wi-Fi after one cable session ([#5](https://github.com/promptctl/orange-drink/pull/5)).
- `promptctl/laws` — new `backlog2` skill — build and maintain an engineering backlog; 0.36.0 ([#96](https://github.com/promptctl/laws/pull/96)).
- `brandon-fryslie/brandon-fryslie` — fix: the Copilot review workflow stores its token via `gh auth login` since agent-task rejects env tokens ([447e089](https://github.com/brandon-fryslie/brandon-fryslie/commit/447e0890)).

### This Week

- `promptctl/low-talker` — 81 commits: IMK rules series — the input method defaults to the main actor with one logged hop through IMK's callbacks, SE-0466 compile on macos-26, main-actor inserts measured at 3.0 s with 11,162 reactivations lossless ([#213](https://github.com/promptctl/low-talker/pull/213), [#218](https://github.com/promptctl/low-talker/pull/218), [#222](https://github.com/promptctl/low-talker/pull/222), [#223](https://github.com/promptctl/low-talker/pull/223), [#231](https://github.com/promptctl/low-talker/pull/231), [#232](https://github.com/promptctl/low-talker/pull/232), [#233](https://github.com/promptctl/low-talker/pull/233)); input method ends itself past 1 GB and the Hotkey line says why ([#217](https://github.com/promptctl/low-talker/pull/217), [#220](https://github.com/promptctl/low-talker/pull/220), [#221](https://github.com/promptctl/low-talker/pull/221)); the speech gate's range is set only by frames the gate classifier calls speech, with LowTalkerCore bundling the r8 gate classifier ([#211](https://github.com/promptctl/low-talker/pull/211)); build-mismatch guard — the app sends words only to an input method of its own build ([#214](https://github.com/promptctl/low-talker/pull/214)); a lost microphone reports the reason it lost audio ([#235](https://github.com/promptctl/low-talker/pull/235)) ([commits](https://github.com/promptctl/low-talker/commits?author=brandon-fryslie&since=2026-10-20)).
- `promptctl/links-issue-tracker` — 76 commits: v0.24.0 released ([#826](https://github.com/promptctl/links-issue-tracker/pull/826)); bulk-edit epic — `lit undo` ([#813](https://github.com/promptctl/links-issue-tracker/pull/813)), bulk restore/comment/start/done/open ([#777](https://github.com/promptctl/links-issue-tracker/pull/777), [#789](https://github.com/promptctl/links-issue-tracker/pull/789), [#800](https://github.com/promptctl/links-issue-tracker/pull/800), [#806](https://github.com/promptctl/links-issue-tracker/pull/806)), `lit ls --format yaml` round-trip through import ([#803](https://github.com/promptctl/links-issue-tracker/pull/803)), batches land whole ([#824](https://github.com/promptctl/links-issue-tracker/pull/824)); scale epic — size-ceiling store with pruning ([#791](https://github.com/promptctl/links-issue-tracker/pull/791)), id-keyed reads one query not 16-id IN batches ([#795](https://github.com/promptctl/links-issue-tracker/pull/795)), 100 concurrent writers complete ([#793](https://github.com/promptctl/links-issue-tracker/pull/793)); storage epic — mirror push bounds, re-root follows without full GC ([#783](https://github.com/promptctl/links-issue-tracker/pull/783), [#781](https://github.com/promptctl/links-issue-tracker/pull/781), [#770](https://github.com/promptctl/links-issue-tracker/pull/770)); `/next` skill quotes every answer ([#755](https://github.com/promptctl/links-issue-tracker/pull/755)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-10-20)).
- `promptctl/cc-candybar` — 60 commits: the 8ro6 epic — each session draws through its own view, the clock is the draw's, pending is its own state, payloads store instants and ages are the draw's, feeds refresh on their own periods, a view declares what its preset's closure reads, built-ins read off their owners ([#419](https://github.com/promptctl/cc-candybar/pull/419), [#421](https://github.com/promptctl/cc-candybar/pull/421), [#423](https://github.com/promptctl/cc-candybar/pull/423)–[#433](https://github.com/promptctl/cc-candybar/pull/433), [#436](https://github.com/promptctl/cc-candybar/pull/436), [#439](https://github.com/promptctl/cc-candybar/pull/439), [#442](https://github.com/promptctl/cc-candybar/pull/442), [#446](https://github.com/promptctl/cc-candybar/pull/446)); lane C draws the animated bar into the tmux status line ([#405](https://github.com/promptctl/cc-candybar/pull/405)); menus animate at 1x/5x/20x and close after idle ([#420](https://github.com/promptctl/cc-candybar/pull/420), [#422](https://github.com/promptctl/cc-candybar/pull/422)); render-cache leaks fixed per-watched-directory ([#412](https://github.com/promptctl/cc-candybar/pull/412)); daemon memory backstop reads macOS footprint, not RSS ([#397](https://github.com/promptctl/cc-candybar/pull/397)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-10-20)).
- `promptctl/mock-anthropic` — 41 commits: a Go rewrite from scratch — TypeScript deleted ([#18](https://github.com/promptctl/mock-anthropic/pull/18)), Go skeleton ([#20](https://github.com/promptctl/mock-anthropic/pull/20)), HTTPS forward proxy ([#25](https://github.com/promptctl/mock-anthropic/pull/25)), openssl CA/leaf certs ([#24](https://github.com/promptctl/mock-anthropic/pull/24)), record and replay modes ([#39](https://github.com/promptctl/mock-anthropic/pull/39), [#40](https://github.com/promptctl/mock-anthropic/pull/40)), SSE Messages generator ([#36](https://github.com/promptctl/mock-anthropic/pull/36)), built-in answers to Claude Code's own calls ([#37](https://github.com/promptctl/mock-anthropic/pull/37)), generators for OAuth/bootstrap/telemetry/MCP/marketplace ([#30](https://github.com/promptctl/mock-anthropic/pull/30), [#31](https://github.com/promptctl/mock-anthropic/pull/31)) ([commits](https://github.com/promptctl/mock-anthropic/commits?author=brandon-fryslie&since=2026-10-20)).
- `promptctl/vhid` — 39 commits: the `eyes` epic — `eyes find` and `eyes read` named no place read what is in front, `eyes hit` says what a click would land on, `eyes find` matches by every text an element says and filters by role ([#171](https://github.com/promptctl/vhid/pull/171), [#172](https://github.com/promptctl/vhid/pull/172), [#173](https://github.com/promptctl/vhid/pull/173)); front window and overlay-coverage model ([#170](https://github.com/promptctl/vhid/pull/170)); plugin session-start version-check ([#167](https://github.com/promptctl/vhid/pull/167), [#168](https://github.com/promptctl/vhid/pull/168), [#169](https://github.com/promptctl/vhid/pull/169)); marketplace installs from `latest-release` branch so skills reach a Mac with its binaries ([#166](https://github.com/promptctl/vhid/pull/166)); 0.6.0 released ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-10-20)).
- `promptctl/cc-hands` — 32 commits: warnings epic — a failed command event says why, naming model refactor, warnings reach the log and hands file-tickets filed one per cause, hung run self-ends ([#332](https://github.com/promptctl/cc-hands/pull/332)–[#338](https://github.com/promptctl/cc-hands/pull/338), [#347](https://github.com/promptctl/cc-hands/pull/347)); voice turns held 10 minutes are sent whole, each hold says who spoke on Nemotron 3 Diarization ([#340](https://github.com/promptctl/cc-hands/pull/340), [#341](https://github.com/promptctl/cc-hands/pull/341)); brain Claude Code pin moves 2.1.289 → 2.1.308 ([#349](https://github.com/promptctl/cc-hands/pull/349), [#350](https://github.com/promptctl/cc-hands/pull/350)); phone backlog page draws levels, cards, and a Stop that ends the brain's turn ([#321](https://github.com/promptctl/cc-hands/pull/321), [#329](https://github.com/promptctl/cc-hands/pull/329), [#330](https://github.com/promptctl/cc-hands/pull/330), [#339](https://github.com/promptctl/cc-hands/pull/339)); wake-word trainer, one command for Hey/Okay Hands ([#331](https://github.com/promptctl/cc-hands/pull/331)) ([commits](https://github.com/promptctl/cc-hands/commits?author=brandon-fryslie&since=2026-10-20)).
- `promptctl/orange-drink` — 20 commits: new macOS repo — iPhone and iPad battery over cable ([#4](https://github.com/promptctl/orange-drink/pull/4)), signed+notarized DMG script ([#7](https://github.com/promptctl/orange-drink/pull/7)), Mac Battery widget signed as Developer ID ([#11](https://github.com/promptctl/orange-drink/pull/11)); admin-helper epic — privileged helper over authenticated XPC ([#15](https://github.com/promptctl/orange-drink/pull/15)), Low Power Mode from panel and L-key ([#16](https://github.com/promptctl/orange-drink/pull/16)), charge-limit UI holds charge at a target ([#19](https://github.com/promptctl/orange-drink/pull/19), [#21](https://github.com/promptctl/orange-drink/pull/21)); alert pills retire individually after 8 s ([#10](https://github.com/promptctl/orange-drink/pull/10), [#14](https://github.com/promptctl/orange-drink/pull/14)) ([commits](https://github.com/promptctl/orange-drink/commits?author=brandon-fryslie&since=2026-10-20)).
- `brandon-fryslie/rich-js` — 15 commits: rich-animation epic — animations placed like any renderable, a view that moves says so only through what it draws, colour transitions time-independent of prior state ([#501](https://github.com/brandon-fryslie/rich-js/pull/501), [#503](https://github.com/brandon-fryslie/rich-js/pull/503), [#513](https://github.com/brandon-fryslie/rich-js/pull/513), [#514](https://github.com/brandon-fryslie/rich-js/pull/514)); rich-protocol purity series — a render that writes state throws, every cache a render fills is a Memo, a widget's observable refuses writes during render, Viewport scroll state kept once the frame is drawn ([#504](https://github.com/brandon-fryslie/rich-js/pull/504)–[#509](https://github.com/brandon-fryslie/rich-js/pull/509), [#511](https://github.com/brandon-fryslie/rich-js/pull/511)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-10-20)).
- `brandon-fryslie/dotfiles` — 7 commits: `claude-codexapi` wrapper added to PATH; CLAUDE.md outline reworked; retired brainstorming/type-fix2 skills; moved disabled agents and commands out of active dirs; `agent-code-review-setup` renders each value's origin into its workflow comment ([#99](https://github.com/brandon-fryslie/dotfiles/pull/99)); Code Root moves to `~/code/open-with-whatever` ([#98](https://github.com/brandon-fryslie/dotfiles/pull/98)); coding files open in VS Code at their git root ([#97](https://github.com/brandon-fryslie/dotfiles/pull/97)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-10-20)).
- `promptctl/laws` — 2 commits: new `backlog2` skill — build and maintain an engineering backlog; 0.36.0 ([#96](https://github.com/promptctl/laws/pull/96)); code-review workflow removed, design doc on purpose and presence ([#97](https://github.com/promptctl/laws/pull/97)).
- `promptctl/memento` — 2 commits: memento 0.11.0 ships a cc-candybar plugin ([#33](https://github.com/promptctl/memento/pull/33), [#34](https://github.com/promptctl/memento/pull/34)).
- `brandon-fryslie/brandon-fryslie` — 1 commit: Copilot review workflow stores its token via `gh auth login` ([447e089](https://github.com/brandon-fryslie/brandon-fryslie/commit/447e0890)).

### This Month

1000+ commits across 15 repositories over the past 30 days (search index capped). Top by volume:

- [`promptctl/low-talker`](https://github.com/promptctl/low-talker) — 221 commits
- [`promptctl/orange-drink`](https://github.com/promptctl/orange-drink) — 210
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 183
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 115
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 110
- [`promptctl/cc-hands`](https://github.com/promptctl/cc-hands) — 51
- [`promptctl/mock-anthropic`](https://github.com/promptctl/mock-anthropic) — 41
- [`promptctl/vhid`](https://github.com/promptctl/vhid) — 39
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 22
- [`promptctl/memento`](https://github.com/promptctl/memento) — 2

Languages: Swift, Go, TypeScript, Python.

---

<details>
<summary>Previous highlights</summary>

- [2026-10-15](./daily-archive/2026-10-15.md)
- [2026-10-14](./daily-archive/2026-10-14.md)
- [2026-10-13](./daily-archive/2026-10-13.md)
- [2026-10-12](./daily-archive/2026-10-12.md)
- [2026-10-11](./daily-archive/2026-10-11.md)
- [2026-10-10](./daily-archive/2026-10-10.md)
- [2026-10-09](./daily-archive/2026-10-09.md)

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
**Swift · 1★**

Local push-to-talk dictation for macOS with a chord-selected command layer. 221 commits over the past month, 81 this week on the IMK rules series. The input method defaults to the main actor, IMK's callbacks hop through one logged entry, SE-0466 compiles on macos-26, main-actor inserts measured at 3.0 s with 11,162 reactivations lossless ([#213](https://github.com/promptctl/low-talker/pull/213), [#222](https://github.com/promptctl/low-talker/pull/222), [#223](https://github.com/promptctl/low-talker/pull/223), [#232](https://github.com/promptctl/low-talker/pull/232), [#233](https://github.com/promptctl/low-talker/pull/233)). The input method ends itself past 1 GB and the app's Hotkey line says why ([#217](https://github.com/promptctl/low-talker/pull/217)). The speech gate's range is set only by frames the gate classifier calls speech, with LowTalkerCore bundling the r8 gate classifier and its training pipeline ([#211](https://github.com/promptctl/low-talker/pull/211)). A build-mismatch guard holds words back when the app and the input method disagree on build ([#214](https://github.com/promptctl/low-talker/pull/214)), and a lost microphone reports the reason it lost audio ([#235](https://github.com/promptctl/low-talker/pull/235)).

### [orange-drink](https://github.com/promptctl/orange-drink)
**Swift**

A macOS menu-bar app and widgets for iPhone, iPad and Mac battery, with a privileged helper for charging controls. New this month — 210 commits, 20 this week. iPhone and iPad battery read over cable through usbmux and lockdown ([#3](https://github.com/promptctl/orange-drink/pull/3), [#4](https://github.com/promptctl/orange-drink/pull/4)); a Mac Battery widget shipped signed as Developer ID ([#11](https://github.com/promptctl/orange-drink/pull/11)); a signed and notarized DMG builds from one script ([#7](https://github.com/promptctl/orange-drink/pull/7)). An admin-helper epic landed — a privileged helper over authenticated XPC accepts only its own app ([#13](https://github.com/promptctl/orange-drink/pull/13), [#15](https://github.com/promptctl/orange-drink/pull/15)), Low Power Mode toggles from the panel and the L-key ([#16](https://github.com/promptctl/orange-drink/pull/16)), and a Charge Limit UI holds charge at a target through the SMC ([#18](https://github.com/promptctl/orange-drink/pull/18), [#19](https://github.com/promptctl/orange-drink/pull/19), [#21](https://github.com/promptctl/orange-drink/pull/21)). Alert pills retire individually after 8 s, counted only while someone can see the screen ([#10](https://github.com/promptctl/orange-drink/pull/10), [#14](https://github.com/promptctl/orange-drink/pull/14)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 2★**

Agent-native issue tracker — `lit`, backed by a Dolt-shaped store with containment, dependencies and labels. 183 commits over the past month, 76 this week; v0.24.0 cut ([#826](https://github.com/promptctl/links-issue-tracker/pull/826)). The bulk-edit epic completed — `lit undo list/revert` reverts chosen writes from history ([#813](https://github.com/promptctl/links-issue-tracker/pull/813)), bulk start/done/open/restore/comment finish the single-verb coverage ([#777](https://github.com/promptctl/links-issue-tracker/pull/777), [#789](https://github.com/promptctl/links-issue-tracker/pull/789), [#800](https://github.com/promptctl/links-issue-tracker/pull/800), [#806](https://github.com/promptctl/links-issue-tracker/pull/806)), `lit ls --format yaml` round-trips through import ([#803](https://github.com/promptctl/links-issue-tracker/pull/803)), a batch lands whole or writes nothing ([#824](https://github.com/promptctl/links-issue-tracker/pull/824)). The scale epic landed a size-ceiling store with pruning ([#791](https://github.com/promptctl/links-issue-tracker/pull/791)), id-keyed reads in one query ([#795](https://github.com/promptctl/links-issue-tracker/pull/795)), and 100 concurrent writers completing ([#793](https://github.com/promptctl/links-issue-tracker/pull/793)). Storage work bounded mirror pushes and let re-root follow without a full GC ([#770](https://github.com/promptctl/links-issue-tracker/pull/770), [#781](https://github.com/promptctl/links-issue-tracker/pull/781), [#783](https://github.com/promptctl/links-issue-tracker/pull/783)).

</td>
<td width="50%" valign="top">

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — fork of `@owloops/claude-powerline` with CLI override flags so the entire config can live in `settings.json`. 115 commits over the past month, 60 this week as the 8ro6 view/payload epic landed. Each session draws through its own view; the clock is the draw's; pending is its own state; payloads store instants while ages and ETAs are the draw's; feeds refresh on their own periods ([#421](https://github.com/promptctl/cc-candybar/pull/421), [#423](https://github.com/promptctl/cc-candybar/pull/423)–[#433](https://github.com/promptctl/cc-candybar/pull/433), [#436](https://github.com/promptctl/cc-candybar/pull/436), [#439](https://github.com/promptctl/cc-candybar/pull/439), [#442](https://github.com/promptctl/cc-candybar/pull/442), [#446](https://github.com/promptctl/cc-candybar/pull/446)). Lane C draws the animated bar into the tmux status line ([#405](https://github.com/promptctl/cc-candybar/pull/405)); menus animate at 1x/5x/20x and close after idle ([#420](https://github.com/promptctl/cc-candybar/pull/420), [#422](https://github.com/promptctl/cc-candybar/pull/422)). The daemon's memory backstop now judges the macOS footprint rather than RSS ([#397](https://github.com/promptctl/cc-candybar/pull/397)) and a render-cache leak per watched directory is closed ([#412](https://github.com/promptctl/cc-candybar/pull/412)).

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript · MIT**

A port of Python's Rich to TypeScript — markup, tables, trees, syntax, progress, tracebacks, Live, and an App runtime that routes focus and the pointer. 110 commits over the past month, 15 this week on the rich-animation and rich-protocol epics. Animations are placed like any renderable, a view that moves says so only through what it draws, and a colour transition draws a time the same whatever was drawn before ([#501](https://github.com/brandon-fryslie/rich-js/pull/501), [#503](https://github.com/brandon-fryslie/rich-js/pull/503), [#513](https://github.com/brandon-fryslie/rich-js/pull/513), [#514](https://github.com/brandon-fryslie/rich-js/pull/514)). The rich-protocol purity series lands render-time guarantees — a render that writes state throws, every cache a render fills is a Memo, a widget's observable refuses writes during render, and `Viewport` keeps its scroll once the frame is drawn ([#504](https://github.com/brandon-fryslie/rich-js/pull/504)–[#509](https://github.com/brandon-fryslie/rich-js/pull/509), [#511](https://github.com/brandon-fryslie/rich-js/pull/511)).

### [cc-hands](https://github.com/promptctl/cc-hands)
**Python · 1★**

Voice for Claude Code — speak to a session over a chord, hear its reply, run a brain that holds its own account on a dedicated Claude Code behind the proxy. 51 commits over the past month, 32 this week. The warnings epic landed — failed command events say why, warnings reach the log, hands file-tickets files one ticket per cause, a hung daemon run ends itself ([#332](https://github.com/promptctl/cc-hands/pull/332)–[#338](https://github.com/promptctl/cc-hands/pull/338), [#347](https://github.com/promptctl/cc-hands/pull/347)). Voice turns held 10 minutes are sent whole, each hold says who spoke on Nemotron 3 Diarization ([#340](https://github.com/promptctl/cc-hands/pull/340), [#341](https://github.com/promptctl/cc-hands/pull/341)). The brain's Claude Code pin moved 2.1.289 → 2.1.308 ([#349](https://github.com/promptctl/cc-hands/pull/349), [#350](https://github.com/promptctl/cc-hands/pull/350)). A phone backlog page draws levels and cards, a single Stop ends the brain's turn ([#321](https://github.com/promptctl/cc-hands/pull/321), [#329](https://github.com/promptctl/cc-hands/pull/329), [#330](https://github.com/promptctl/cc-hands/pull/330), [#339](https://github.com/promptctl/cc-hands/pull/339)). A wake-word trainer trains Hey Hands and Okay Hands from one command ([#331](https://github.com/promptctl/cc-hands/pull/331)).

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
