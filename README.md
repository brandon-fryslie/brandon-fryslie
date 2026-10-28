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

Two releases cut yesterday — `links-issue-tracker` v0.24.0 and `vhid` 0.6.0 — and today everything downstream turned into cleanup. Forty-three commits across four repos, most of them one-liners against clocks, locks, and watch keys. The ticket prefixes read `brandon-unfiled` and `links-unfiled` because none of it belongs to an epic. It's the sweeping that follows a release.

The one I keep coming back to: in `cc-candybar` the daemon's config watcher was keying its watches on inodes, so a symlinked `settings.json` rewritten by its editor silently stopped updating. The fix is to watch where the write lands, not what the file was yesterday. Not glamorous. One of the harder things to do consistently.

Over in `cc-hands`, the brain's end-to-end tests started running against `mock-anthropic` pinned at v0.1.0 — the Go rewrite from yesterday. Fast fixture to a thing that was a rewrite twelve hours ago. That part doesn't feel like a weekday.

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

*Updated October 28, 2026*

### Last 24 Hours

- `promptctl/cc-candybar` — 19 commits of post-epic cleanup — a repo's watch is keyed on the directories it bound and every pass rebinds it ([#467](https://github.com/promptctl/cc-candybar/pull/467)); a watch covers the whole refs tree of its common git dir ([#466](https://github.com/promptctl/cc-candybar/pull/466)); a symlinked config is watched where a write to it lands, no file watched by its inode ([#459](https://github.com/promptctl/cc-candybar/pull/459)); a repository's config runs only once the user approves it in the bar ([#454](https://github.com/promptctl/cc-candybar/pull/454)); a plugin folder whose watch has stopped delivering reads as stalled, not frozen ([#458](https://github.com/promptctl/cc-candybar/pull/458)); the backoff test owns the one clock the cooldown reads ([#464](https://github.com/promptctl/cc-candybar/pull/464)); `check:protocol` reads every anchor from code ([#462](https://github.com/promptctl/cc-candybar/pull/462)); pnpm test runs in five minutes or less on CI ([#453](https://github.com/promptctl/cc-candybar/pull/453)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-10-27)).
- `promptctl/cc-hands` — 15 commits — each voice model's load says the process's physical footprint and how much it grew ([#365](https://github.com/promptctl/cc-hands/pull/365)); Smart Turn judges each stop on its MLX port of the full-precision v3.2 in a fifth of the time ([#364](https://github.com/promptctl/cc-hands/pull/364)); each live word carries the speaker who said it, diarization paired with the streaming recognizer on MLX ([#363](https://github.com/promptctl/cc-hands/pull/363)); the brain's end-to-end tests run against `mock-anthropic` pinned at v0.1.0, installed with go ([#362](https://github.com/promptctl/cc-hands/pull/362)); live words from Nemotron's streaming model cut a hold while it is open ([#357](https://github.com/promptctl/cc-hands/pull/357)); one hold owner cuts every hold, Whisper and the diarizer as listeners ([#353](https://github.com/promptctl/cc-hands/pull/353)); a file-ticket names the file a warning was logged in, never its function ([#355](https://github.com/promptctl/cc-hands/pull/355)) ([commits](https://github.com/promptctl/cc-hands/commits?author=brandon-fryslie&since=2026-10-27)).
- `promptctl/links-issue-tracker` — 8 commits of post-v0.24.0 cleanup — otel and its sdk move to v1.45.0, out of the endpoint-logging advisory's range ([#835](https://github.com/promptctl/links-issue-tracker/pull/835)); a take removes the temp file a backup killed mid-write left, under the set's lock ([#834](https://github.com/promptctl/links-issue-tracker/pull/834)); `--latest-release` authenticates its GitHub API lookup with `GH_TOKEN` or `GITHUB_TOKEN` ([#833](https://github.com/promptctl/links-issue-tracker/pull/833)); a first open waits out a bootstrap build however long the machine's load makes it ([#832](https://github.com/promptctl/links-issue-tracker/pull/832)); a title or lane stored with a line break prints on one row in every listing ([#831](https://github.com/promptctl/links-issue-tracker/pull/831)); an unreadable input file is refused as usage before the workspace opens ([#830](https://github.com/promptctl/links-issue-tracker/pull/830)); a lock wait measures and sleeps on one clock ([#829](https://github.com/promptctl/links-issue-tracker/pull/829)); the store's and dbsnapshot's notices reach the stderr `cli.Run` was given ([#828](https://github.com/promptctl/links-issue-tracker/pull/828)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-10-27)).
- `brandon-fryslie/dotfiles` — tickets and notes point no finer than a file: dropped `file:line` anchors from write-evidence, fill-backlog, and form-a-posse ([53db94a](https://github.com/brandon-fryslie/dotfiles/commit/53db94add95529a29422b45603d011771bad0ca8)).

### This Week

- `promptctl/cc-candybar` — 74 commits: the 8ro6 view/payload epic closes — memento integration moves out ([#443](https://github.com/promptctl/cc-candybar/pull/443)), plugins carry per-session data and run their own programs ([#441](https://github.com/promptctl/cc-candybar/pull/441)), every source records refreshes in one ledger ([#446](https://github.com/promptctl/cc-candybar/pull/446)), every bar says how it is redrawn in a cell beside the door ([#448](https://github.com/promptctl/cc-candybar/pull/448)), a frame finds its session's view and opens nothing ([#444](https://github.com/promptctl/cc-candybar/pull/444)), a click says how long it waited ([#447](https://github.com/promptctl/cc-candybar/pull/447)); daemon watcher series — directory-bound watches rebind every pass ([#467](https://github.com/promptctl/cc-candybar/pull/467)), refs tree coverage ([#466](https://github.com/promptctl/cc-candybar/pull/466)), symlinked configs watched by write-landing ([#459](https://github.com/promptctl/cc-candybar/pull/459)); test harness — pnpm test under 5 minutes on CI ([#453](https://github.com/promptctl/cc-candybar/pull/453)), colour audits move to nightly outside the suite ([#452](https://github.com/promptctl/cc-candybar/pull/452)); a repository's config runs only once the user approves it ([#454](https://github.com/promptctl/cc-candybar/pull/454)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-10-21)).
- `promptctl/links-issue-tracker` — 55 commits: v0.24.0 released ([#826](https://github.com/promptctl/links-issue-tracker/pull/826)); bulk-edit epic — `lit undo list/revert` ([#813](https://github.com/promptctl/links-issue-tracker/pull/813)), bulk restore ([#806](https://github.com/promptctl/links-issue-tracker/pull/806)) and bulk comment ([#789](https://github.com/promptctl/links-issue-tracker/pull/789)), `lit ls --format yaml` round-trip through import ([#803](https://github.com/promptctl/links-issue-tracker/pull/803)), batches land whole or write nothing ([#824](https://github.com/promptctl/links-issue-tracker/pull/824)); scale epic — size-ceiling store with pruning ([#791](https://github.com/promptctl/links-issue-tracker/pull/791)), id-keyed reads in one query ([#795](https://github.com/promptctl/links-issue-tracker/pull/795)), 100 concurrent writers complete ([#793](https://github.com/promptctl/links-issue-tracker/pull/793)); storage epic — mirror push bounds, re-root follows without full GC ([#781](https://github.com/promptctl/links-issue-tracker/pull/781), [#783](https://github.com/promptctl/links-issue-tracker/pull/783)); post-release cleanup — backup temp-file sweep ([#834](https://github.com/promptctl/links-issue-tracker/pull/834)), `--latest-release` auth ([#833](https://github.com/promptctl/links-issue-tracker/pull/833)), line-break-safe listings ([#831](https://github.com/promptctl/links-issue-tracker/pull/831)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-10-21)).
- `promptctl/cc-hands` — 47 commits: voice/MLX work — Smart Turn on an MLX port of v3.2 in a fifth of the time ([#364](https://github.com/promptctl/cc-hands/pull/364)); each live word carries speaker diarization paired with the streaming recognizer on MLX ([#363](https://github.com/promptctl/cc-hands/pull/363)); one hold owner cuts every hold ([#353](https://github.com/promptctl/cc-hands/pull/353)); 10-minute voice turns sent whole on Nemotron 3 Diarization ([#340](https://github.com/promptctl/cc-hands/pull/340), [#341](https://github.com/promptctl/cc-hands/pull/341)); brain's Claude Code pin moves 2.1.289 → 2.1.308 ([#349](https://github.com/promptctl/cc-hands/pull/349), [#350](https://github.com/promptctl/cc-hands/pull/350)); brain end-to-end tests run against `mock-anthropic` v0.1.0 ([#352](https://github.com/promptctl/cc-hands/pull/352), [#362](https://github.com/promptctl/cc-hands/pull/362)); warnings epic — failed command events say why, hands file-tickets filed one per cause ([#332](https://github.com/promptctl/cc-hands/pull/332)–[#338](https://github.com/promptctl/cc-hands/pull/338)); hung daemon run ends itself ([#347](https://github.com/promptctl/cc-hands/pull/347)) ([commits](https://github.com/promptctl/cc-hands/commits?author=brandon-fryslie&since=2026-10-21)).
- `promptctl/mock-anthropic` — 41 commits: a Go rewrite from scratch — TypeScript deleted ([#18](https://github.com/promptctl/mock-anthropic/pull/18)), Go skeleton with command dispatcher and CI ([#20](https://github.com/promptctl/mock-anthropic/pull/20)), HTTPS forward proxy ([#25](https://github.com/promptctl/mock-anthropic/pull/25)), openssl CA/leaf certs ([#24](https://github.com/promptctl/mock-anthropic/pull/24)), record and replay modes ([#39](https://github.com/promptctl/mock-anthropic/pull/39), [#40](https://github.com/promptctl/mock-anthropic/pull/40)), SSE Messages generator ([#36](https://github.com/promptctl/mock-anthropic/pull/36)), built-in answers to Claude Code's own calls ([#37](https://github.com/promptctl/mock-anthropic/pull/37)), generators for OAuth/bootstrap/telemetry/MCP ([#30](https://github.com/promptctl/mock-anthropic/pull/30), [#31](https://github.com/promptctl/mock-anthropic/pull/31)) ([commits](https://github.com/promptctl/mock-anthropic/commits?author=brandon-fryslie&since=2026-10-21)).
- `promptctl/vhid` — 39 commits: the `eyes` epic — `eyes find` and `eyes read` named no place read what is in front, `eyes hit` says what a click would land on, `eyes find` matches by every text an element says and filters by role ([#171](https://github.com/promptctl/vhid/pull/171), [#172](https://github.com/promptctl/vhid/pull/172), [#173](https://github.com/promptctl/vhid/pull/173)); front window and overlay-coverage model ([#170](https://github.com/promptctl/vhid/pull/170)); plugin session-start version-check ([#167](https://github.com/promptctl/vhid/pull/167), [#168](https://github.com/promptctl/vhid/pull/168), [#169](https://github.com/promptctl/vhid/pull/169)); marketplace installs from `latest-release` branch ([#166](https://github.com/promptctl/vhid/pull/166)); 0.6.0 released ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-10-21)).
- `promptctl/orange-drink` — 20 commits: iPhone and iPad battery over cable ([#4](https://github.com/promptctl/orange-drink/pull/4)), signed+notarized DMG script ([#7](https://github.com/promptctl/orange-drink/pull/7)), Mac Battery widget signed as Developer ID ([#11](https://github.com/promptctl/orange-drink/pull/11)); admin-helper epic — privileged helper over authenticated XPC ([#15](https://github.com/promptctl/orange-drink/pull/15)), Low Power Mode from panel and L-key ([#16](https://github.com/promptctl/orange-drink/pull/16)), charge-limit UI holds charge at a target ([#19](https://github.com/promptctl/orange-drink/pull/19), [#21](https://github.com/promptctl/orange-drink/pull/21)); alert pills retire individually after 8 s ([#10](https://github.com/promptctl/orange-drink/pull/10), [#14](https://github.com/promptctl/orange-drink/pull/14)); usbmuxd listing diffed as one decision ([#22](https://github.com/promptctl/orange-drink/pull/22)) ([commits](https://github.com/promptctl/orange-drink/commits?author=brandon-fryslie&since=2026-10-21)).
- `promptctl/low-talker` — 16 commits: a lost microphone reports the reason it lost audio ([#235](https://github.com/promptctl/low-talker/pull/235)); input method opens its insert port off the main thread since opening it verifies its own Developer ID signature ([#233](https://github.com/promptctl/low-talker/pull/233)); input method ends itself past 1 GB and the Hotkey line says why — IMK rule 7 ([#232](https://github.com/promptctl/low-talker/pull/232)); IMK rules 5 and 7 wait on macos-26 measurements ([#231](https://github.com/promptctl/low-talker/pull/231)); a supervisor test that waits past its 10 s fails cleanly rather than taking the test process down ([#223](https://github.com/promptctl/low-talker/pull/223)) ([commits](https://github.com/promptctl/low-talker/commits?author=brandon-fryslie&since=2026-10-21)).
- `brandon-fryslie/rich-js` — 12 commits: rich-animation epic — an animation is placed like any renderable ([#503](https://github.com/brandon-fryslie/rich-js/pull/503)), a view that moves says so only through what it draws ([#514](https://github.com/brandon-fryslie/rich-js/pull/514)), colour transitions draw the same whatever was drawn before ([#513](https://github.com/brandon-fryslie/rich-js/pull/513)), a frame's hold no cell carries is told, not drawn ([#512](https://github.com/brandon-fryslie/rich-js/pull/512)); rich-protocol purity — a render that writes state throws ([#504](https://github.com/brandon-fryslie/rich-js/pull/504)), every cache a render fills is a Memo ([#505](https://github.com/brandon-fryslie/rich-js/pull/505)), a widget's observable refuses writes during render ([#506](https://github.com/brandon-fryslie/rich-js/pull/506)), Viewport scroll state kept once the frame is drawn ([#508](https://github.com/brandon-fryslie/rich-js/pull/508), [#509](https://github.com/brandon-fryslie/rich-js/pull/509), [#511](https://github.com/brandon-fryslie/rich-js/pull/511)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-10-21)).
- `brandon-fryslie/dotfiles` — 8 commits: `claude-codexapi` wrapper added to PATH; CLAUDE.md outline reworked; retired brainstorming/type-fix2 skills; moved disabled agents and commands out of active dirs; `agent-code-review-setup` renders each value's origin into its workflow comment ([#99](https://github.com/brandon-fryslie/dotfiles/pull/99)); Code Root moves to `~/code/open-with-whatever` ([#98](https://github.com/brandon-fryslie/dotfiles/pull/98)); coding files open in VS Code at their git root ([#97](https://github.com/brandon-fryslie/dotfiles/pull/97)); tickets point no finer than a file ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-10-21)).
- `promptctl/laws` — 2 commits: new `backlog2` skill — build and maintain an engineering backlog; 0.36.0 ([#96](https://github.com/promptctl/laws/pull/96)); code-review workflow removed, design doc on purpose and presence ([#97](https://github.com/promptctl/laws/pull/97)).
- `promptctl/memento` — 2 commits: memento 0.11.0 ships a cc-candybar plugin ([#33](https://github.com/promptctl/memento/pull/33), [#34](https://github.com/promptctl/memento/pull/34)).
- `brandon-fryslie/brandon-fryslie` — 1 commit: Copilot review workflow stores its token via `gh auth login` ([447e089](https://github.com/brandon-fryslie/brandon-fryslie/commit/447e089bb6040ce5a58b3ee715a8ac754f9b90d6)).

### This Month

30-day volume exceeded the search index's 1000-result cap. Top by volume within the index:

- [`promptctl/orange-drink`](https://github.com/promptctl/orange-drink) — 210 commits
- [`promptctl/low-talker`](https://github.com/promptctl/low-talker) — 208
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 180
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 117
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 110
- [`promptctl/cc-hands`](https://github.com/promptctl/cc-hands) — 64
- [`promptctl/mock-anthropic`](https://github.com/promptctl/mock-anthropic) — 41
- [`promptctl/vhid`](https://github.com/promptctl/vhid) — 39
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 23

Languages: Swift, Go, TypeScript, Python.

---

<details>
<summary>Previous highlights</summary>

- [2026-10-27](./daily-archive/2026-10-27.md)
- [2026-10-15](./daily-archive/2026-10-15.md)
- [2026-10-14](./daily-archive/2026-10-14.md)
- [2026-10-13](./daily-archive/2026-10-13.md)
- [2026-10-12](./daily-archive/2026-10-12.md)
- [2026-10-11](./daily-archive/2026-10-11.md)
- [2026-10-10](./daily-archive/2026-10-10.md)

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

### [orange-drink](https://github.com/promptctl/orange-drink)
**Swift**

A macOS menu-bar app and widgets for iPhone, iPad and Mac battery, with a privileged helper for charging controls. 210 commits over the past month, 20 this week. iPhone and iPad battery read over cable through usbmux and lockdown, and keep reading over Wi-Fi after one cable session ([#3](https://github.com/promptctl/orange-drink/pull/3), [#4](https://github.com/promptctl/orange-drink/pull/4), [#5](https://github.com/promptctl/orange-drink/pull/5)); a Mac Battery widget shipped signed as Developer ID ([#11](https://github.com/promptctl/orange-drink/pull/11)); a signed and notarized DMG builds from one script ([#7](https://github.com/promptctl/orange-drink/pull/7)). An admin-helper epic landed — a privileged helper over authenticated XPC accepts only its own app ([#13](https://github.com/promptctl/orange-drink/pull/13), [#15](https://github.com/promptctl/orange-drink/pull/15)), Low Power Mode toggles from the panel and the L-key ([#16](https://github.com/promptctl/orange-drink/pull/16)), and a Charge Limit UI holds charge at a target through the SMC ([#18](https://github.com/promptctl/orange-drink/pull/18), [#19](https://github.com/promptctl/orange-drink/pull/19), [#21](https://github.com/promptctl/orange-drink/pull/21)). Alert pills retire individually after 8 s, counted only while someone can see the screen ([#10](https://github.com/promptctl/orange-drink/pull/10), [#14](https://github.com/promptctl/orange-drink/pull/14)); a usbmuxd listing is diffed as one decision ([#22](https://github.com/promptctl/orange-drink/pull/22)).

### [low-talker](https://github.com/promptctl/low-talker)
**Swift · 1★**

Local push-to-talk dictation for macOS with a chord-selected command layer. 208 commits over the past month, 16 this week on the IMK rules series. The input method defaults to the main actor, IMK's callbacks hop through one logged entry, SE-0466 compiles on macos-26, main-actor inserts measured at 3.0 s with 11,162 reactivations lossless ([#213](https://github.com/promptctl/low-talker/pull/213), [#222](https://github.com/promptctl/low-talker/pull/222), [#223](https://github.com/promptctl/low-talker/pull/223), [#232](https://github.com/promptctl/low-talker/pull/232), [#233](https://github.com/promptctl/low-talker/pull/233)). The input method ends itself past 1 GB and the app's Hotkey line says why ([#217](https://github.com/promptctl/low-talker/pull/217), [#232](https://github.com/promptctl/low-talker/pull/232)). The speech gate's range is set only by frames the gate classifier calls speech, with LowTalkerCore bundling the r8 gate classifier and its training pipeline ([#211](https://github.com/promptctl/low-talker/pull/211)). A build-mismatch guard holds words back when the app and the input method disagree on build ([#214](https://github.com/promptctl/low-talker/pull/214)), and a lost microphone reports the reason it lost audio ([#235](https://github.com/promptctl/low-talker/pull/235)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 2★**

Agent-native issue tracker — `lit`, backed by a Dolt-shaped store with containment, dependencies and labels. 180 commits over the past month, 55 this week; v0.24.0 cut ([#826](https://github.com/promptctl/links-issue-tracker/pull/826)). The bulk-edit epic completed — `lit undo list/revert` reverts chosen writes from history ([#813](https://github.com/promptctl/links-issue-tracker/pull/813)), bulk start/done/open/restore/comment finish the single-verb coverage ([#777](https://github.com/promptctl/links-issue-tracker/pull/777), [#789](https://github.com/promptctl/links-issue-tracker/pull/789), [#800](https://github.com/promptctl/links-issue-tracker/pull/800), [#806](https://github.com/promptctl/links-issue-tracker/pull/806)), `lit ls --format yaml` round-trips through import ([#803](https://github.com/promptctl/links-issue-tracker/pull/803)), a batch lands whole or writes nothing ([#824](https://github.com/promptctl/links-issue-tracker/pull/824)). The scale epic landed a size-ceiling store with pruning ([#791](https://github.com/promptctl/links-issue-tracker/pull/791)), id-keyed reads in one query ([#795](https://github.com/promptctl/links-issue-tracker/pull/795)), and 100 concurrent writers completing ([#793](https://github.com/promptctl/links-issue-tracker/pull/793)). Post-v0.24.0 cleanup — a mid-write backup's temp file is swept under the set's lock ([#834](https://github.com/promptctl/links-issue-tracker/pull/834)), `--latest-release` authenticates its API lookup with `GH_TOKEN` or `GITHUB_TOKEN` ([#833](https://github.com/promptctl/links-issue-tracker/pull/833)), line-break-safe listings print on one row ([#831](https://github.com/promptctl/links-issue-tracker/pull/831)).

</td>
<td width="50%" valign="top">

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — fork of `@owloops/claude-powerline` with CLI override flags so the entire config can live in `settings.json`. 117 commits over the past month, 74 this week as the 8ro6 view/payload epic closed. Each session draws through its own view; the clock is the draw's; payloads store instants while ages and ETAs are the draw's; feeds refresh on their own periods ([#421](https://github.com/promptctl/cc-candybar/pull/421), [#423](https://github.com/promptctl/cc-candybar/pull/423)–[#433](https://github.com/promptctl/cc-candybar/pull/433), [#436](https://github.com/promptctl/cc-candybar/pull/436), [#439](https://github.com/promptctl/cc-candybar/pull/439), [#442](https://github.com/promptctl/cc-candybar/pull/442), [#446](https://github.com/promptctl/cc-candybar/pull/446)). The epic's close moved memento integration out ([#443](https://github.com/promptctl/cc-candybar/pull/443)), gave plugins per-session data and their own programs ([#441](https://github.com/promptctl/cc-candybar/pull/441)), recorded every source's refreshes in one ledger ([#446](https://github.com/promptctl/cc-candybar/pull/446)), and said beside each bar's door how it is redrawn ([#448](https://github.com/promptctl/cc-candybar/pull/448)). A daemon-watcher series followed — directory-bound watches rebind every pass ([#467](https://github.com/promptctl/cc-candybar/pull/467)), coverage spans the whole refs tree ([#466](https://github.com/promptctl/cc-candybar/pull/466)), symlinked configs are watched by write-landing ([#459](https://github.com/promptctl/cc-candybar/pull/459)); pnpm test runs under 5 minutes on CI ([#453](https://github.com/promptctl/cc-candybar/pull/453)).

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript · MIT**

A port of Python's Rich to TypeScript — markup, tables, trees, syntax, progress, tracebacks, Live, and an App runtime that routes focus and the pointer. 110 commits over the past month, 12 this week on the rich-animation and rich-protocol epics. Animations are placed like any renderable, a view that moves says so only through what it draws, and a colour transition draws a time the same whatever was drawn before ([#501](https://github.com/brandon-fryslie/rich-js/pull/501), [#503](https://github.com/brandon-fryslie/rich-js/pull/503), [#513](https://github.com/brandon-fryslie/rich-js/pull/513), [#514](https://github.com/brandon-fryslie/rich-js/pull/514)); a frame's hold no cell carries is told, not drawn ([#512](https://github.com/brandon-fryslie/rich-js/pull/512)). The rich-protocol purity series lands render-time guarantees — a render that writes state throws, every cache a render fills is a Memo, a widget's observable refuses writes during render, and `Viewport` keeps its scroll once the frame is drawn ([#504](https://github.com/brandon-fryslie/rich-js/pull/504)–[#509](https://github.com/brandon-fryslie/rich-js/pull/509), [#511](https://github.com/brandon-fryslie/rich-js/pull/511)).

### [cc-hands](https://github.com/promptctl/cc-hands)
**Python · 1★**

Voice for Claude Code — speak to a session over a chord, hear its reply, run a brain that holds its own account on a dedicated Claude Code behind the proxy. 64 commits over the past month, 47 this week. Voice/MLX work landed — Smart Turn judges each stop on its MLX port of v3.2 in a fifth of the time ([#364](https://github.com/promptctl/cc-hands/pull/364)), each live word carries the speaker who said it with diarization paired to the streaming recognizer on MLX ([#363](https://github.com/promptctl/cc-hands/pull/363)), one hold owner cuts every hold ([#353](https://github.com/promptctl/cc-hands/pull/353)), and voice turns held 10 minutes send whole on Nemotron 3 Diarization ([#340](https://github.com/promptctl/cc-hands/pull/340), [#341](https://github.com/promptctl/cc-hands/pull/341)). The brain's end-to-end tests run against `mock-anthropic` v0.1.0 ([#352](https://github.com/promptctl/cc-hands/pull/352), [#362](https://github.com/promptctl/cc-hands/pull/362)), and the Claude Code pin moved 2.1.289 → 2.1.308 ([#349](https://github.com/promptctl/cc-hands/pull/349), [#350](https://github.com/promptctl/cc-hands/pull/350)). The warnings epic — failed command events say why, hands file-tickets files one ticket per cause, a hung daemon run ends itself ([#332](https://github.com/promptctl/cc-hands/pull/332)–[#338](https://github.com/promptctl/cc-hands/pull/338), [#347](https://github.com/promptctl/cc-hands/pull/347)).

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
