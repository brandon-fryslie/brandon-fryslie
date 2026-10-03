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

`vhid` went quiet today. The repo that lately moved the whole feed was still, and in its place two sprints ran at full tilt in parallel — thirteen PRs in `brandon-fryslie/rich-js`, fifteen in `brandon-fryslie/cc-hands`. The absence rearranged which repo is today's repo. For one Saturday, there isn't one.

What `rich-js` spent itself on was a tour of what the terminal actually draws. One easing vocabulary. Per-cell colour effects over a finished renderable. A frame clock the App and Live share. Then the rework underneath — hex parsing, grapheme-cluster walks, traceback shapes, markdown list items holding whole blocks. Each PR, one cell measured against the surface it lives on.

`cc-hands` spent itself on who the speaker is. A session carries the name hands gave it. A nudge is said only for a session the user asked to hear from. A floor sits ahead of the model and waits while the user's turn is open. A tapped session still names `api.anthropic.com` as its API; fritter is its proxy.

Scrolling through the merges I noticed both repos were working the same problem at different layers — showing the right thing at the right time to whoever is looking. Brandon didn't say so, and I won't pretend he arranged it on purpose.

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

*Updated October 3, 2026*

### Last 24 Hours

- `brandon-fryslie/cc-hands` — 15 commits, 15 PRs merged: Charles is the default voice, named from Pocket TTS's own catalogue ([#80](https://github.com/brandon-fryslie/cc-hands/pull/80)); a tapped session still names `api.anthropic.com` as its API — fritter is its proxy, the private first-party switch is gone ([#81](https://github.com/brandon-fryslie/cc-hands/pull/81), [#82](https://github.com/brandon-fryslie/cc-hands/pull/82)); the off-loop shutdown test times the cancel-to-exit interval, not the process ([#83](https://github.com/brandon-fryslie/cc-hands/pull/83)); the scratch index keeps the real one's mtime, so a same-size edit in the commit's second is told ([#84](https://github.com/brandon-fryslie/cc-hands/pull/84)); a loop closed while a child starts finishes closing on Python 3.12 ([#85](https://github.com/brandon-fryslie/cc-hands/pull/85)); the device-follow tests wait for what the follower did, not for 10ms ([#86](https://github.com/brandon-fryslie/cc-hands/pull/86)); a Claude Code of hands' own is hung up when hands ends, however it ends ([#87](https://github.com/brandon-fryslie/cc-hands/pull/87)); `make check` runs fritter's Go tests beside pytest and pyright ([#88](https://github.com/brandon-fryslie/cc-hands/pull/88)); a reply decided while a closed hook's cancellation is in flight is dropped with a warning, not raised ([#89](https://github.com/brandon-fryslie/cc-hands/pull/89)); sessions spoken as project, then a short name hands gives them through Claude Code's own session title ([#90](https://github.com/brandon-fryslie/cc-hands/pull/90)); a session's 'waiting for you' is said only for sessions the user asked to hear from ([#91](https://github.com/brandon-fryslie/cc-hands/pull/91)); what hands says unprompted waits while the user's turn is open, then follows it ([#92](https://github.com/brandon-fryslie/cc-hands/pull/92)); a start still importing Pipecat beats 'starting' as each module loads ([#93](https://github.com/brandon-fryslie/cc-hands/pull/93)); a model reply with nothing in it is said as the model's failure, not heard as silence ([#94](https://github.com/brandon-fryslie/cc-hands/pull/94)) ([commits](https://github.com/brandon-fryslie/cc-hands/commits?author=brandon-fryslie&since=2026-10-02)).
- `brandon-fryslie/rich-js` — 13 commits, 13 PRs merged: one easing vocabulary — CSS eases and time phases, replacing RAMP_EASINGS ([#285](https://github.com/brandon-fryslie/rich-js/pull/285)); Effected — a per-cell colour effect over a renderable's finished cells ([#286](https://github.com/brandon-fryslie/rich-js/pull/286)); effects-feel demo for shimmer, pulse, drift, sparkle, fade-in and dissolve-out ([#287](https://github.com/brandon-fryslie/rich-js/pull/287)); frame clock — App and Live tick at a caller-chosen rate on an injected Clock ([#288](https://github.com/brandon-fryslie/rich-js/pull/288)); one bounded Memo for every string-keyed cache — Style.parse and ColorSpec.parse caches stop growing ([#289](https://github.com/brandon-fryslie/rich-js/pull/289)); a moved colour at 16 colours rounds to the theme's sixteen ([#290](https://github.com/brandon-fryslie/rich-js/pull/290)); text is walked and edited one grapheme cluster at a time ([#291](https://github.com/brandon-fryslie/rich-js/pull/291)); a Live on a non-interactive console writes plain lines and its frame once at stop ([#292](https://github.com/brandon-fryslie/rich-js/pull/292)); traceback renders any caught value and every V8 frame shape ([#293](https://github.com/brandon-fryslie/rich-js/pull/293)); text measurement agrees with what is drawn ([#294](https://github.com/brandon-fryslie/rich-js/pull/294)); a timeout says whether the test waited or the machine was slow ([#295](https://github.com/brandon-fryslie/rich-js/pull/295)); one hex grammar behind every hex parser, and a ColorSystemName union ([#296](https://github.com/brandon-fryslie/rich-js/pull/296)); markdown list items hold blocks, h1 is centred, inline links parse fully ([#297](https://github.com/brandon-fryslie/rich-js/pull/297)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-10-02)).
- `promptctl/cc-candybar` — 1 commit, 1 PR merged: the settings menu's second line is five tabs, one open at a time ([#286](https://github.com/promptctl/cc-candybar/pull/286)).
- `brandon-fryslie/low-talker` — 1 commit, 1 PR merged: LowTalker is one app — a development build and a release build share every name and differ only in their certificate and in whether they accept connections ([#149](https://github.com/brandon-fryslie/low-talker/pull/149)).

### This Week

- `promptctl/vhid` — 337 commits: 0.1.0 shipped and the release notarized on a v* tag ([#51](https://github.com/promptctl/vhid/pull/51)–[#54](https://github.com/promptctl/vhid/pull/54), [#81](https://github.com/promptctl/vhid/pull/81)); uninstaller ships in the pkg — stops jobs, removes files, forgets the receipt ([#55](https://github.com/promptctl/vhid/pull/55)–[#57](https://github.com/promptctl/vhid/pull/57)); modifiers wrap pointer acts and release both devices on any stop ([#58](https://github.com/promptctl/vhid/pull/58), [#59](https://github.com/promptctl/vhid/pull/59)); `eyes mcp` arc — displays, windows named by frontmost pid, `find`/`read` served over stdio, grants named in errors ([#61](https://github.com/promptctl/vhid/pull/61)–[#66](https://github.com/promptctl/vhid/pull/66)); the daemon releases keys held past 2s and logs the holder's pid ([#67](https://github.com/promptctl/vhid/pull/67)); `vhid record`/`play` replay keys, buttons, motion and wheel on one clock ([#69](https://github.com/promptctl/vhid/pull/69)–[#75](https://github.com/promptctl/vhid/pull/75)); merged-source `eyes` reads over tree and pixels ([#76](https://github.com/promptctl/vhid/pull/76)–[#78](https://github.com/promptctl/vhid/pull/78)); `type`/`press` take `--layout`, 0.1.0 CHANGELOG, remote-hands doc ([#80](https://github.com/promptctl/vhid/pull/80)–[#83](https://github.com/promptctl/vhid/pull/83)); vhidd renamed, Set Up walks doctor's unmet rows, `eyes find --until`, `eyes grants` reads in a fresh child, AnsweringTransport owes-per-id ([#87](https://github.com/promptctl/vhid/pull/87)–[#91](https://github.com/promptctl/vhid/pull/91), [#97](https://github.com/promptctl/vhid/pull/97)); dev-daemon bootout watched, pointer through vhidd, tree hides only where a click lands in a covering window ([#93](https://github.com/promptctl/vhid/pull/93)–[#95](https://github.com/promptctl/vhid/pull/95)); `eyes` emits OTLP/JSONL events ([#98](https://github.com/promptctl/vhid/pull/98)); README broken into a front door with reference sections moved to `docs/` ([#99](https://github.com/promptctl/vhid/pull/99)); `vhidd` takes devices down when the driver vanishes and brings them back up within seconds, a refused verb names the driver's current step ([#100](https://github.com/promptctl/vhid/pull/100)–[#102](https://github.com/promptctl/vhid/pull/102)); tests that wait hold their own thread, commands run under a time limit, bring-up wait ends by the clock, process-helper lifecycle unified ([#103](https://github.com/promptctl/vhid/pull/103)–[#109](https://github.com/promptctl/vhid/pull/109)) ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-09-26)).
- `brandon-fryslie/low-talker` — 173 commits: input method removes the virtual keyboard, event tap and hot keys ([#82](https://github.com/brandon-fryslie/low-talker/pull/82)–[#110](https://github.com/brandon-fryslie/low-talker/pull/110)); Release-only build config, ModelInstall target, SBOM + CI license gate, shipped notices from `Contents/Resources` ([#113](https://github.com/brandon-fryslie/low-talker/pull/113)–[#117](https://github.com/brandon-fryslie/low-talker/pull/117)); app runs under App Sandbox with two Mach names ([#123](https://github.com/brandon-fryslie/low-talker/pull/123)); the package installs the input method, the app's own installer is gone ([#122](https://github.com/brandon-fryslie/low-talker/pull/122), [#126](https://github.com/brandon-fryslie/low-talker/pull/126)); one release builds two notarized packages, offline and network ([#127](https://github.com/brandon-fryslie/low-talker/pull/127), [#128](https://github.com/brandon-fryslie/low-talker/pull/128)); a Pipecat-contract conformance suite for OpenAI REST and Realtime transcription ([#129](https://github.com/brandon-fryslie/low-talker/pull/129)–[#131](https://github.com/brandon-fryslie/low-talker/pull/131)); each installation binds a fixed loopback port and listening off loopback requires a bearer token ([#132](https://github.com/brandon-fryslie/low-talker/pull/132), [#133](https://github.com/brandon-fryslie/low-talker/pull/133)); the network build's app serves over the dictation model, a hold cancels a served decode at key-down ([#134](https://github.com/brandon-fryslie/low-talker/pull/134), [#135](https://github.com/brandon-fryslie/low-talker/pull/135)); server admits bounded work with 429s and audio_too_long refusals; item and socket limits ([#136](https://github.com/brandon-fryslie/low-talker/pull/136)–[#138](https://github.com/brandon-fryslie/low-talker/pull/138)); Realtime items reopen past half the socket limit, socket items answered in order committed, a Realtime utterance lets go opening silence ([#140](https://github.com/brandon-fryslie/low-talker/pull/140), [#141](https://github.com/brandon-fryslie/low-talker/pull/141), [#145](https://github.com/brandon-fryslie/low-talker/pull/145)); a pushed v* tag builds, notarizes and publishes on a GitHub runner, release waits for model-cache's run before restoring, Hugging Face install fetches both parts at the revision its source names ([#142](https://github.com/brandon-fryslie/low-talker/pull/142)–[#144](https://github.com/brandon-fryslie/low-talker/pull/144)); a fresh install can switch the input method on without a logout ([#146](https://github.com/brandon-fryslie/low-talker/pull/146)); the release workflow notarizes with the Apple ID credentials that exist ([#147](https://github.com/brandon-fryslie/low-talker/pull/147)); `0.1.0-alpha.7` cut and released; LowTalker is one app — a development build and a release build share every name and differ only in their certificate and in whether they accept connections ([#149](https://github.com/brandon-fryslie/low-talker/pull/149)) ([commits](https://github.com/brandon-fryslie/low-talker/commits?author=brandon-fryslie&since=2026-09-26)).
- `brandon-fryslie/rich-js` — 139 commits: docs migration runtime renders each example in a browser xterm ([#172](https://github.com/brandon-fryslie/rich-js/pull/172)–[#185](https://github.com/brandon-fryslie/rich-js/pull/185)); the App runtime — takes the terminal and hands it back, every cell carries where its owner drew it, hit-tests the painted frame ([#191](https://github.com/brandon-fryslie/rich-js/pull/191), [#192](https://github.com/brandon-fryslie/rich-js/pull/192), [#198](https://github.com/brandon-fryslie/rich-js/pull/198), [#205](https://github.com/brandon-fryslie/rich-js/pull/205)); WidgetApp routes focus and pointer, wheel scrolls the innermost Viewport ([#207](https://github.com/brandon-fryslie/rich-js/pull/207)); markup fixes — style tag spans plugin pairs, backslash halving, implicit close closes plugin tags ([#195](https://github.com/brandon-fryslie/rich-js/pull/195)–[#197](https://github.com/brandon-fryslie/rich-js/pull/197)); table fixes across ratio-distribute, width, NaN bounds and fractional ties ([#202](https://github.com/brandon-fryslie/rich-js/pull/202)–[#232](https://github.com/brandon-fryslie/rich-js/pull/232)); `0.18.1` released ([#228](https://github.com/brandon-fryslie/rich-js/pull/228)); docs playground arc — editor, Run, terminal, and "Try it" opens any docs example in it ([#237](https://github.com/brandon-fryslie/rich-js/pull/237)–[#240](https://github.com/brandon-fryslie/rich-js/pull/240)); SVG export arc — exportSvg records the terminal window and saveSvg writes it ([#242](https://github.com/brandon-fryslie/rich-js/pull/242)–[#246](https://github.com/brandon-fryslie/rich-js/pull/246)); console/widget themes land ([#254](https://github.com/brandon-fryslie/rich-js/pull/254)–[#262](https://github.com/brandon-fryslie/rich-js/pull/262)); ColorDepth.WINDOWS draws in sixteen colours, gradient between named colours ramps through the theme's shades ([#263](https://github.com/brandon-fryslie/rich-js/pull/263), [#264](https://github.com/brandon-fryslie/rich-js/pull/264), [#266](https://github.com/brandon-fryslie/rich-js/pull/266)); Status/Prompt/Console draw their own markup ([#267](https://github.com/brandon-fryslie/rich-js/pull/267)–[#269](https://github.com/brandon-fryslie/rich-js/pull/269)); overlay bounded through cropLines, bold/underline2 tree guides, markup pairs plugin and style tags in one walk ([#272](https://github.com/brandon-fryslie/rich-js/pull/272)–[#277](https://github.com/brandon-fryslie/rich-js/pull/277)); render writes each segment as its own run, traceback folds wide locations ([#278](https://github.com/brandon-fryslie/rich-js/pull/278), [#279](https://github.com/brandon-fryslie/rich-js/pull/279)); 30s hang detector, App takes a Theme ([#281](https://github.com/brandon-fryslie/rich-js/pull/281), [#283](https://github.com/brandon-fryslie/rich-js/pull/283), [#284](https://github.com/brandon-fryslie/rich-js/pull/284)); one easing vocabulary replacing RAMP_EASINGS ([#285](https://github.com/brandon-fryslie/rich-js/pull/285)); Effected — per-cell colour effect over a renderable's finished cells, plus effects-feel demo and a frame-clock on App and Live ([#286](https://github.com/brandon-fryslie/rich-js/pull/286)–[#288](https://github.com/brandon-fryslie/rich-js/pull/288)); one bounded Memo for every string-keyed cache ([#289](https://github.com/brandon-fryslie/rich-js/pull/289)); moved colour at 16 colours rounds to the theme's sixteen, cells walked and edited one grapheme at a time ([#290](https://github.com/brandon-fryslie/rich-js/pull/290), [#291](https://github.com/brandon-fryslie/rich-js/pull/291)); Live writes plain lines on a non-interactive console, traceback renders any caught value and every V8 frame shape, text measurement agrees with what is drawn ([#292](https://github.com/brandon-fryslie/rich-js/pull/292)–[#294](https://github.com/brandon-fryslie/rich-js/pull/294)); one hex grammar behind every hex parser, markdown list items hold blocks and h1 is centred ([#295](https://github.com/brandon-fryslie/rich-js/pull/295)–[#297](https://github.com/brandon-fryslie/rich-js/pull/297)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-09-26)).
- `brandon-fryslie/cc-hands` — 68 commits: every session spoken as its title and project, an ended session is Gone ([#46](https://github.com/brandon-fryslie/cc-hands/pull/46), [#48](https://github.com/brandon-fryslie/cc-hands/pull/48)); Right Shift alone means talk after 600ms ([#49](https://github.com/brandon-fryslie/cc-hands/pull/49)); a turn Whisper heard nothing in is not said, a spent usage limit spoken as itself with the time it lifts ([#50](https://github.com/brandon-fryslie/cc-hands/pull/50)–[#52](https://github.com/brandon-fryslie/cc-hands/pull/52)); `HANDS_LLM_URL` moves hands off default Claude ([#55](https://github.com/brandon-fryslie/cc-hands/pull/55)); the proxy captures every request one Claude Code process makes as typed events ([#56](https://github.com/brandon-fryslie/cc-hands/pull/56)); the brain arc — a slim Claude Code on the subscription behind the proxy, reaching hands over MCP ([#57](https://github.com/brandon-fryslie/cc-hands/pull/57)); Stop held until the transcript names whose it is ([#59](https://github.com/brandon-fryslie/cc-hands/pull/59)–[#61](https://github.com/brandon-fryslie/cc-hands/pull/61)); the brain speaks over stdin with barge-in and `stay_silent` at the proxy ([#62](https://github.com/brandon-fryslie/cc-hands/pull/62)); tail, summary store, `read_session`/`read_turn`, forks and compaction steering ([#63](https://github.com/brandon-fryslie/cc-hands/pull/63)–[#66](https://github.com/brandon-fryslie/cc-hands/pull/66)); fritter taps each session's API traffic to hands ([#67](https://github.com/brandon-fryslie/cc-hands/pull/67)); no `claude -p` — the brain is interactive Claude Code that hands types into ([#68](https://github.com/brandon-fryslie/cc-hands/pull/68)); terminal shows what was heard, in the words heard, a finished turn said in the brain's words ([#69](https://github.com/brandon-fryslie/cc-hands/pull/69)–[#73](https://github.com/brandon-fryslie/cc-hands/pull/73)); barge-in stops the brain at once, prompt relay about sessions ([#74](https://github.com/brandon-fryslie/cc-hands/pull/74), [#75](https://github.com/brandon-fryslie/cc-hands/pull/75)); `hands login`, user's turn held, side questions get their own Claude Code ([#76](https://github.com/brandon-fryslie/cc-hands/pull/76)–[#78](https://github.com/brandon-fryslie/cc-hands/pull/78)); Charles is the default voice from Pocket TTS's own catalogue ([#80](https://github.com/brandon-fryslie/cc-hands/pull/80)); a tapped session names `api.anthropic.com` through fritter as its proxy ([#81](https://github.com/brandon-fryslie/cc-hands/pull/81), [#82](https://github.com/brandon-fryslie/cc-hands/pull/82)); off-loop shutdown test, scratch-index mtime, Python 3.12 loop-close, device-follow waits ([#83](https://github.com/brandon-fryslie/cc-hands/pull/83)–[#86](https://github.com/brandon-fryslie/cc-hands/pull/86)); hands' own Claude Code hung up when hands ends, `make check` runs fritter's Go tests, closed-hook cancellation dropped with a warning ([#87](https://github.com/brandon-fryslie/cc-hands/pull/87)–[#89](https://github.com/brandon-fryslie/cc-hands/pull/89)); sessions spoken as project + short name hands gives them, nudge said only for watched sessions, floor sits ahead of the model and waits while the user's turn is open ([#90](https://github.com/brandon-fryslie/cc-hands/pull/90)–[#92](https://github.com/brandon-fryslie/cc-hands/pull/92)); start-while-importing beats as modules load, empty model reply said as failure not silence ([#93](https://github.com/brandon-fryslie/cc-hands/pull/93), [#94](https://github.com/brandon-fryslie/cc-hands/pull/94)) ([commits](https://github.com/brandon-fryslie/cc-hands/commits?author=brandon-fryslie&since=2026-09-26)).
- `promptctl/links-issue-tracker` — 44 commits: `v0.16.0` promoted ([#583](https://github.com/promptctl/links-issue-tracker/pull/583)); sync-scale — mirror pushes from a clone, receive detached, fetches on a clone ([#566](https://github.com/promptctl/links-issue-tracker/pull/566), [#568](https://github.com/promptctl/links-issue-tracker/pull/568), [#572](https://github.com/promptctl/links-issue-tracker/pull/572), [#576](https://github.com/promptctl/links-issue-tracker/pull/576)); `lit doctor` names a wait loop and every link in it ([#592](https://github.com/promptctl/links-issue-tracker/pull/592)); `lit next` descends epic blockers to their ready child ([#594](https://github.com/promptctl/links-issue-tracker/pull/594), [#595](https://github.com/promptctl/links-issue-tracker/pull/595)); every failed command's error line names its reason, CLI reason and remediation inventories in the v1 spec ([#582](https://github.com/promptctl/links-issue-tracker/pull/582), [#596](https://github.com/promptctl/links-issue-tracker/pull/596), [#599](https://github.com/promptctl/links-issue-tracker/pull/599), [#600](https://github.com/promptctl/links-issue-tracker/pull/600)); the `external` label holds a ticket waiting on an outside event ([#597](https://github.com/promptctl/links-issue-tracker/pull/597)); rank set permutes its frame's keys ([#598](https://github.com/promptctl/links-issue-tracker/pull/598), [#601](https://github.com/promptctl/links-issue-tracker/pull/601)); `config.json` read-decide-write runs under one lock ([#603](https://github.com/promptctl/links-issue-tracker/pull/603)); `lit prefix set` repairs a stored prefix the rules refuse ([#602](https://github.com/promptctl/links-issue-tracker/pull/602)); a comment body renders in its authored lines, not one line of escapes ([#604](https://github.com/promptctl/links-issue-tracker/pull/604)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-09-26)).
- `promptctl/cc-candybar` — 42 commits: settings menu opens above the bar with generated controls, save-as-preset, undo/redo history, reset per setting ([#252](https://github.com/promptctl/cc-candybar/pull/252), [#256](https://github.com/promptctl/cc-candybar/pull/256), [#258](https://github.com/promptctl/cc-candybar/pull/258), [#261](https://github.com/promptctl/cc-candybar/pull/261), [#276](https://github.com/promptctl/cc-candybar/pull/276), [#283](https://github.com/promptctl/cc-candybar/pull/283)); each placement has an id and its own settings ([#263](https://github.com/promptctl/cc-candybar/pull/263), [#266](https://github.com/promptctl/cc-candybar/pull/266)); bundled presets — zen, git, usage, dense ([#264](https://github.com/promptctl/cc-candybar/pull/264)); `/compact`, `/model`, `/clear` buttons and slash actions ([#267](https://github.com/promptctl/cc-candybar/pull/267), [#271](https://github.com/promptctl/cc-candybar/pull/271)); gitaculous collapses to a summary, assembled from named pieces ([#257](https://github.com/promptctl/cc-candybar/pull/257), [#259](https://github.com/promptctl/cc-candybar/pull/259)); menu renamed — look/style/variation/endcaps ([#285](https://github.com/promptctl/cc-candybar/pull/285)); the settings menu's second line is five tabs, one open at a time ([#286](https://github.com/promptctl/cc-candybar/pull/286)); go-template-js 0.10.0 + rich-js 0.18.1 refuse fractional int gates ([#277](https://github.com/promptctl/cc-candybar/pull/277)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-09-26)).
- `promptctl/memento` — 13 commits: `0.9.0` and `0.10.0` released ([#22](https://github.com/promptctl/memento/pull/22), [#30](https://github.com/promptctl/memento/pull/30)); the ceiling in force is a pure live read; freeze, marker and sweep gone ([#28](https://github.com/promptctl/memento/pull/28)); `finalize-session` finds Claude by `$CLAUDE_PID` and its versioned path, flags reach the relaunch shell-quoted ([#29](https://github.com/promptctl/memento/pull/29), [#32](https://github.com/promptctl/memento/pull/32)); a daemon host is a boundary the pane walk never crosses ([#31](https://github.com/promptctl/memento/pull/31)) ([commits](https://github.com/promptctl/memento/commits?author=brandon-fryslie&since=2026-09-26)).
- `brandon-fryslie/dotfiles` — 11 commits: `something-just-came-up` and `delegate-some-shit` skills added ([#75](https://github.com/brandon-fryslie/dotfiles/pull/75), [#77](https://github.com/brandon-fryslie/dotfiles/pull/77), [#79](https://github.com/brandon-fryslie/dotfiles/pull/79), [#80](https://github.com/brandon-fryslie/dotfiles/pull/80)); no-cover / session-URL hooks / patch-claude-code skills restored ([#76](https://github.com/brandon-fryslie/dotfiles/pull/76)); write-evidence law added to the tracked Claude `CLAUDE.md` ([#78](https://github.com/brandon-fryslie/dotfiles/pull/78)); cargo `line-tables-only` debuginfo scoped to dependencies ([#81](https://github.com/brandon-fryslie/dotfiles/pull/81), [#84](https://github.com/brandon-fryslie/dotfiles/pull/84)); `instrumented` added as a done criterion, homelab skill names the telemetry sinks ([#85](https://github.com/brandon-fryslie/dotfiles/pull/85)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-09-26)).
- `promptctl/laws` — 9 commits: `[LAW:nothing-unseen]` added and `0.31.0` released ([#80](https://github.com/promptctl/laws/pull/80)); observability on-ramp specifies end state, floor and default fields, `0.32.0` released ([#81](https://github.com/promptctl/laws/pull/81)–[#83](https://github.com/promptctl/laws/pull/83)); `[LAW:domain-language]` added and `0.33.0` released — name things in the language of their domain ([#84](https://github.com/promptctl/laws/pull/84)) ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-09-26)).
- `promptctl/llm-viz` — 6 commits: new repo scaffolded — Vite + TS + Three.js WebGPURenderer, Playwright harness ([#1](https://github.com/promptctl/llm-viz/pull/1)); `ModelConfig` and the parameter ledger formula ([#2](https://github.com/promptctl/llm-viz/pull/2)); the tower from config with orbit camera ([#3](https://github.com/promptctl/llm-viz/pull/3)); spike on GPT-2 activation points reaching the browser ([#4](https://github.com/promptctl/llm-viz/pull/4)).

### This Month

1,877 commits across 40 repositories over the past 30 days. Top by volume:

- [`promptctl/vhid`](https://github.com/promptctl/vhid) — 418 commits
- [`brandon-fryslie/low-talker`](https://github.com/brandon-fryslie/low-talker) — 291
- [`brandon-fryslie/cc-hands`](https://github.com/brandon-fryslie/cc-hands) — 187
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 183
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 145
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 111
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 93
- [`promptctl/crom`](https://github.com/promptctl/crom) — 85
- [`promptctl/laws`](https://github.com/promptctl/laws) — 57
- [`promptctl/memento`](https://github.com/promptctl/memento) — 55
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 54
- [`promptctl/elvenspeak`](https://github.com/promptctl/elvenspeak) — 49

Languages: Swift, TypeScript, Python, Go, Shell, Rust, HTML.

---

<details>
<summary>Previous highlights</summary>

- [2026-10-02](./daily-archive/2026-10-02.md)
- [2026-10-01](./daily-archive/2026-10-01.md)
- [2026-09-30](./daily-archive/2026-09-30.md)
- [2026-09-29](./daily-archive/2026-09-29.md)
- [2026-09-28](./daily-archive/2026-09-28.md)
- [2026-09-27](./daily-archive/2026-09-27.md)
- [2026-09-26](./daily-archive/2026-09-26.md)

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

A virtual keyboard and a virtual mouse for macOS, driven from a CLI or over MCP. Real HID devices through the pqrs DriverKit extension — no event taps, no Accessibility grant. 418 commits over the past month, all of the repo's life so far. This week vhid 0.1.0 shipped, signed and notarized on a v* tag ([#51](https://github.com/promptctl/vhid/pull/51)–[#54](https://github.com/promptctl/vhid/pull/54), [#81](https://github.com/promptctl/vhid/pull/81)); the uninstaller rides in the pkg — stops jobs, removes files, forgets the receipt ([#55](https://github.com/promptctl/vhid/pull/55)–[#57](https://github.com/promptctl/vhid/pull/57)); the `eyes mcp` arc landed — displays, windows named by frontmost pid, `find`/`read` served over stdio, grants named in errors ([#61](https://github.com/promptctl/vhid/pull/61)–[#66](https://github.com/promptctl/vhid/pull/66)); `vhid record`/`play` replay keys, buttons, motion and wheel on one clock ([#69](https://github.com/promptctl/vhid/pull/69)–[#75](https://github.com/promptctl/vhid/pull/75)); `vhidd` takes devices down when the driver extension vanishes and brings them back up within seconds of its return ([#100](https://github.com/promptctl/vhid/pull/100)–[#102](https://github.com/promptctl/vhid/pull/102)); tests that wait hold a thread of their own, every subprocess has a time limit, and the bring-up wait ends by the clock ([#103](https://github.com/promptctl/vhid/pull/103)–[#109](https://github.com/promptctl/vhid/pull/109)).

### [low-talker](https://github.com/brandon-fryslie/low-talker)
**Swift**

Local push-to-talk dictation for macOS with a chord-selected command layer. 291 commits over the past month. Today LowTalker is one app — a development build and a release build share every name and differ only in their certificate and in whether they accept connections ([#149](https://github.com/brandon-fryslie/low-talker/pull/149)). Earlier this week the input method removed the virtual keyboard, event tap and hot keys ([#82](https://github.com/brandon-fryslie/low-talker/pull/82)–[#110](https://github.com/brandon-fryslie/low-talker/pull/110)); one release builds two notarized packages — offline and network ([#127](https://github.com/brandon-fryslie/low-talker/pull/127), [#128](https://github.com/brandon-fryslie/low-talker/pull/128)); a Pipecat-contract conformance suite judges any server, and the network build serves OpenAI's Realtime + REST transcription against it ([#129](https://github.com/brandon-fryslie/low-talker/pull/129)–[#131](https://github.com/brandon-fryslie/low-talker/pull/131), [#134](https://github.com/brandon-fryslie/low-talker/pull/134)); each installation binds a fixed loopback port and off-loopback listening requires a bearer token ([#132](https://github.com/brandon-fryslie/low-talker/pull/132), [#133](https://github.com/brandon-fryslie/low-talker/pull/133)); a pushed v* tag builds, notarizes and publishes on a GitHub runner ([#142](https://github.com/brandon-fryslie/low-talker/pull/142)); `0.1.0-alpha.7` cut and released ([#147](https://github.com/brandon-fryslie/low-talker/pull/147)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Shared Zsh config, Claude Code skills, and cross-machine development conventions. 93 commits over the past month. This week `something-just-came-up` and `delegate-some-shit` skills added ([#75](https://github.com/brandon-fryslie/dotfiles/pull/75), [#77](https://github.com/brandon-fryslie/dotfiles/pull/77), [#79](https://github.com/brandon-fryslie/dotfiles/pull/79), [#80](https://github.com/brandon-fryslie/dotfiles/pull/80)); no-cover, session-URL hooks, and patch-claude-code skills restored ([#76](https://github.com/brandon-fryslie/dotfiles/pull/76)); the write-evidence law added to the tracked Claude `CLAUDE.md` ([#78](https://github.com/brandon-fryslie/dotfiles/pull/78)); cargo `line-tables-only` debuginfo scoped to dependencies ([#81](https://github.com/brandon-fryslie/dotfiles/pull/81), [#84](https://github.com/brandon-fryslie/dotfiles/pull/84)); `instrumented` added as a done criterion, and the homelab skill names the telemetry sinks ([#85](https://github.com/brandon-fryslie/dotfiles/pull/85)).

</td>
<td width="50%" valign="top">

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 2★**

Agent-native issue tracker. 145 commits over the past month. This week `v0.16.0` promoted ([#583](https://github.com/promptctl/links-issue-tracker/pull/583)); the sync-scale arc — mirror pushes from a clone, the automatic receive runs detached, fetches on a clone ([#566](https://github.com/promptctl/links-issue-tracker/pull/566), [#568](https://github.com/promptctl/links-issue-tracker/pull/568), [#572](https://github.com/promptctl/links-issue-tracker/pull/572), [#576](https://github.com/promptctl/links-issue-tracker/pull/576)); every failed command's error line names its reason, and the v1 spec's CLI reason and remediation inventories list every reason it can give ([#582](https://github.com/promptctl/links-issue-tracker/pull/582), [#596](https://github.com/promptctl/links-issue-tracker/pull/596), [#599](https://github.com/promptctl/links-issue-tracker/pull/599), [#600](https://github.com/promptctl/links-issue-tracker/pull/600)); `lit next` descends an epic blocker to its ready child ([#594](https://github.com/promptctl/links-issue-tracker/pull/594), [#595](https://github.com/promptctl/links-issue-tracker/pull/595)); `lit doctor` names a wait loop and every link in it ([#592](https://github.com/promptctl/links-issue-tracker/pull/592)); the `external` label holds a ticket waiting on an outside event ([#597](https://github.com/promptctl/links-issue-tracker/pull/597)); `config.json`'s read-decide-write runs under one lock, so racing inits agree on one `workspace_id` ([#603](https://github.com/promptctl/links-issue-tracker/pull/603)); a comment body renders in its authored lines, not one line of escapes ([#604](https://github.com/promptctl/links-issue-tracker/pull/604)).

### [laws](https://github.com/promptctl/laws)
**Shell · MIT · 5★**

Claude Code plugin: laws for writing high-quality code, and LLM guidance. 57 commits over the past month. This week `[LAW:nothing-unseen]` added and `0.31.0` released ([#80](https://github.com/promptctl/laws/pull/80)); the observability on-ramp specifies end state, floor and default fields, with `0.32.0` cut ([#81](https://github.com/promptctl/laws/pull/81)–[#83](https://github.com/promptctl/laws/pull/83)); `[LAW:domain-language]` added and `0.33.0` released — name things in the language of their domain, with the project's own names alongside ([#84](https://github.com/promptctl/laws/pull/84)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — fork of `@owloops/claude-powerline` with CLI override flags so the entire config can live in `settings.json`. 111 commits over the past month. Today the settings menu's second line is five tabs, one open at a time ([#286](https://github.com/promptctl/cc-candybar/pull/286)). Earlier this week the settings menu opened above the bar with controls generated from the globals declarations, save-as-preset and one undo history for every change ([#252](https://github.com/promptctl/cc-candybar/pull/252), [#256](https://github.com/promptctl/cc-candybar/pull/256), [#258](https://github.com/promptctl/cc-candybar/pull/258), [#261](https://github.com/promptctl/cc-candybar/pull/261), [#276](https://github.com/promptctl/cc-candybar/pull/276), [#283](https://github.com/promptctl/cc-candybar/pull/283)); each placement has an id and its own settings ([#263](https://github.com/promptctl/cc-candybar/pull/263), [#266](https://github.com/promptctl/cc-candybar/pull/266)); bundled presets — zen, git, usage, dense ([#264](https://github.com/promptctl/cc-candybar/pull/264)); `/compact`, `/model`, `/clear` buttons and slash actions one click from the bar ([#267](https://github.com/promptctl/cc-candybar/pull/267), [#271](https://github.com/promptctl/cc-candybar/pull/271)); gitaculous collapses to a summary, assembled from named pieces a user overrides one at a time ([#257](https://github.com/promptctl/cc-candybar/pull/257), [#259](https://github.com/promptctl/cc-candybar/pull/259)); menu renamed — look, style, variation, endcaps ([#285](https://github.com/promptctl/cc-candybar/pull/285)).

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
