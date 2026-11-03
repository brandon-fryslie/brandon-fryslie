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

The pattern sat in two repos at once. `cc-candybar`'s daemon got a Timekeeper, a Spawner, a ProcessProbe, a Host — every ambient thing the OS used to hand it is now a value the root builds and the tests can hold still. `cc-hands` did the equivalent for its sessions, voice, and brain packages: one Clock reads time, ids, and randomness, bound at the composition root, received everywhere else. Different repos, same move, the same morning.

Nobody asked for either refactor. The tickets were about tests being slow and flaky; the way out, it turned out, was the same shape — strip the ambients, pass the inputs in. Brandon didn't name the pattern. It emerged, and he let it stand.

Elsewhere was quieter. `dotfiles` spent the day teaching one shell guard every way a session URL can leak — gh comment, gh api, environment variables, the files a publishing command takes its text from. `links-issue-tracker` reverted a top-level id index migration from master before any release could carry it, and shipped `lit downgrade --remote` to lower a schema and hold it there.

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

*Updated November 3, 2026*

### Last 24 Hours

- `promptctl/cc-candybar` — 48 commits: the daemon's ambients become values the root builds — a Timekeeper reads time and schedules work ([#586](https://github.com/promptctl/cc-candybar/pull/586)), a Host reads the process once so tests stop writing `process.env` ([#585](https://github.com/promptctl/cc-candybar/pull/585)), a Spawner and ProcessProbe sit between launches and the OS ([#602](https://github.com/promptctl/cc-candybar/pull/602)), `createDaemon` takes every adapter and path as input ([#583](https://github.com/promptctl/cc-candybar/pull/583)); a launch's drained pipes get one owner, one bound and a stat ([#595](https://github.com/promptctl/cc-candybar/pull/595), [#598](https://github.com/promptctl/cc-candybar/pull/598)), and a cut drain or failed pipe shows in the ⚠ indicator ([#601](https://github.com/promptctl/cc-candybar/pull/601)); a resident Swift forwarder sends the raw link to the daemon ([#594](https://github.com/promptctl/cc-candybar/pull/594)), a click it could not deliver tells the user ([#600](https://github.com/promptctl/cc-candybar/pull/600)); a flake is quarantined by one line and a line older than a week shows red ([#576](https://github.com/promptctl/cc-candybar/pull/576)), daemon boots in a worker land on the ledger ([#578](https://github.com/promptctl/cc-candybar/pull/578)), each test layer is a directory and the unit tier refuses what it may not touch ([#573](https://github.com/promptctl/cc-candybar/pull/573)); array-form segment templates with scoped partials ([#569](https://github.com/promptctl/cc-candybar/pull/569)); a click's whole time including Launch Services is measured ([#603](https://github.com/promptctl/cc-candybar/pull/603)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-11-02)).
- `promptctl/links-issue-tracker` — 27 commits: schema reversibility design — every raise steps back losslessly and only a release raises a remote ([#856](https://github.com/promptctl/links-issue-tracker/pull/856)); migration 12's top-level id index pulled from master before any release could carry it ([#855](https://github.com/promptctl/links-issue-tracker/pull/855)); every lit carries a released-schema ceiling so no build migrates past what a release carries ([#857](https://github.com/promptctl/links-issue-tracker/pull/857)); `lit downgrade --remote` lowers a remote and holds it, `lit upgrade --remote` lifts it ([#881](https://github.com/promptctl/links-issue-tracker/pull/881)); the stash carrier keeps what a Down drops ([#882](https://github.com/promptctl/links-issue-tracker/pull/882)); a push that raises the remote's schema lands only from a release ([#873](https://github.com/promptctl/links-issue-tracker/pull/873)); CI proves every migration round-trips losslessly ([#874](https://github.com/promptctl/links-issue-tracker/pull/874)); telemetry events on rank sets, tree-order reads, workspace resolution, minting, id-prefix census, `lit dep`, `lit followup`, `lit history`, `lit doctor` ([#858](https://github.com/promptctl/links-issue-tracker/pull/858), [#860](https://github.com/promptctl/links-issue-tracker/pull/860), [#862](https://github.com/promptctl/links-issue-tracker/pull/862), [#864](https://github.com/promptctl/links-issue-tracker/pull/864), [#871](https://github.com/promptctl/links-issue-tracker/pull/871)); a detached worker carries its spawning command's trace id ([#875](https://github.com/promptctl/links-issue-tracker/pull/875)); Windows backup ordering ([#868](https://github.com/promptctl/links-issue-tracker/pull/868)); a divergent sync no longer brings back a relation one side removed ([#869](https://github.com/promptctl/links-issue-tracker/pull/869)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-11-02)).
- `promptctl/low-talker` — 23 commits: a microphone stopped mid-press is readied again for the next press ([#239](https://github.com/promptctl/low-talker/pull/239)); only the newest engine's failure readies a new input, so a late stop cannot take the input from under the next press; the "begins no dictation" box is gone — a chord blocked by held modifiers surfaces nothing ([#243](https://github.com/promptctl/low-talker/pull/243)); a cancel decides the listen at once, no start or queued ready follows it; CoreAudio starts off the main thread and child processes are awaited, so the test process keeps its cooperative pool; one peak reader serves clips and windows via vDSP; the watchdog times and kills only its own test process behind `make test-watchdog`; Build 10 for v0.1.0-alpha.10 ([#244](https://github.com/promptctl/low-talker/pull/244)) ([commits](https://github.com/promptctl/low-talker/commits?author=brandon-fryslie&since=2026-11-02)).
- `brandon-fryslie/dotfiles` — 15 commits: `guard-session-url` denies session-URL leaks across every surface — `gh` comment/review/api writes ([#107](https://github.com/brandon-fryslie/dotfiles/pull/107)), the config forms of a hook bypass ([#105](https://github.com/brandon-fryslie/dotfiles/pull/105)), writing or unsetting `core.hooksPath` ([#110](https://github.com/brandon-fryslie/dotfiles/pull/110)), `GIT_CONFIG_GLOBAL`/`HOME`/`XDG_CONFIG_HOME` in a git call's environment ([#113](https://github.com/brandon-fryslie/dotfiles/pull/113)), the files a publishing command takes its text from ([#114](https://github.com/brandon-fryslie/dotfiles/pull/114)); `guard-tmux-server` reads a command's words, not the Command tuple ([#116](https://github.com/brandon-fryslie/dotfiles/pull/116)); the tmux server is guarded by what a command runs ([#102](https://github.com/brandon-fryslie/dotfiles/pull/102)); `repo-session` launches a worktree, delivers a verbatim brief via `tmux-command` with a 10s working check ([#103](https://github.com/brandon-fryslie/dotfiles/pull/103)); Brandon's stated rules land in the global `CLAUDE.md` ([#104](https://github.com/brandon-fryslie/dotfiles/pull/104)); `regen-ca-bundle` reads an explicit Deny trust entry as untrusted, not as evaluation failure ([#115](https://github.com/brandon-fryslie/dotfiles/pull/115)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-11-02)).
- `promptctl/tmux-control-mode-js` — 13 commits: pane-detail epic — `listPanes`/`listWindows` return structured records ([#180](https://github.com/promptctl/tmux-control-mode-js/pull/180)), `listSessions` returns a structured `SessionRecord` ([#181](https://github.com/promptctl/tmux-control-mode-js/pull/181)), `capturePane` returns full pane history with escapes as a typed command ([#189](https://github.com/promptctl/tmux-control-mode-js/pull/189)), per-method `RpcSpec` table replaces `RpcRequest`/`RpcResponseMap` ([#183](https://github.com/promptctl/tmux-control-mode-js/pull/183)); cross-session layout events relay via global hook and reach bridge consumers ([#188](https://github.com/promptctl/tmux-control-mode-js/pull/188), [#192](https://github.com/promptctl/tmux-control-mode-js/pull/192)); watch a whole tmux server without disturbing it ([#191](https://github.com/promptctl/tmux-control-mode-js/pull/191)); WebSocket bridge disposes the client when `createBridgeConnection` throws, and `onHello` unwinds client/bridge/peer via one release stack ([#185](https://github.com/promptctl/tmux-control-mode-js/pull/185), [#187](https://github.com/promptctl/tmux-control-mode-js/pull/187)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-11-02)).
- `promptctl/orange-drink` — 13 commits: temperature warning specified and shipped — a pill when the battery runs warm or hot ([#58](https://github.com/promptctl/orange-drink/pull/58)), the Temperature row on the Alerts screen ([#59](https://github.com/promptctl/orange-drink/pull/59)), re-arm two degrees under Warm ([#60](https://github.com/promptctl/orange-drink/pull/60)), design-docs/alerts.md spec ([#57](https://github.com/promptctl/orange-drink/pull/57)); update-check allows the helper and reads it answering from the updated copy ([#55](https://github.com/promptctl/orange-drink/pull/55)); Sparkle's helper signing ordered after Xcode's own ([#50](https://github.com/promptctl/orange-drink/pull/50)); release refuses a commit whose tests did not pass ([#53](https://github.com/promptctl/orange-drink/pull/53)); menu-bar item names the battery state for VoiceOver ([#52](https://github.com/promptctl/orange-drink/pull/52)); iPhone listing and capture spikes promoted to `scripts/iphone-devices` ([#61](https://github.com/promptctl/orange-drink/pull/61)); battery levels say per-language ([#49](https://github.com/promptctl/orange-drink/pull/49)) ([commits](https://github.com/promptctl/orange-drink/commits?author=brandon-fryslie&since=2026-11-02)).
- `promptctl/cc-hands` — 12 commits: one `Clock` reads time, ids, and randomness — bound at the composition root ([#434](https://github.com/promptctl/cc-hands/pull/434)) and received by the sessions ([#428](https://github.com/promptctl/cc-hands/pull/428)), voice ([#430](https://github.com/promptctl/cc-hands/pull/430)), and brain ([#432](https://github.com/promptctl/cc-hands/pull/432)) packages; a typed turn is sent by Ctrl-Q, pasted only once the screen shows the prompt ([#422](https://github.com/promptctl/cc-hands/pull/422), [#429](https://github.com/promptctl/cc-hands/pull/429)); side questions forked from a turn ending in system messages are accepted ([#423](https://github.com/promptctl/cc-hands/pull/423)); an untaken turn's words are cleared before the next turn is typed ([#424](https://github.com/promptctl/cc-hands/pull/424)); words Claude Code takes next from an untaken turn are stopped through the one stop ([#431](https://github.com/promptctl/cc-hands/pull/431)); a 400 on a request hands built or changed is logged as hands' bug ([#425](https://github.com/promptctl/cc-hands/pull/425)); each CI run says what each test cost in its own log ([#421](https://github.com/promptctl/cc-hands/pull/421)) ([commits](https://github.com/promptctl/cc-hands/commits?author=brandon-fryslie&since=2026-11-02)).
- `promptctl/go-template-js` — 10 commits: subtemplates — `include` renders a define by name as Helm's does ([#46](https://github.com/promptctl/go-template-js/pull/46)), `Template.evaluateDefine` as Go's `ExecuteTemplate` ([#47](https://github.com/promptctl/go-template-js/pull/47)), `Defines.names()` lists every define a template can render own and inherited ([#48](https://github.com/promptctl/go-template-js/pull/48)); a string engine prints a plain object as Go's `%v` ([#50](https://github.com/promptctl/go-template-js/pull/50)); `print` and `printf %v` print a map or slice as `{{ . }}` does ([#51](https://github.com/promptctl/go-template-js/pull/51)); evaluator's refusal names the leaf that cannot print, not the top-level array ([#52](https://github.com/promptctl/go-template-js/pull/52)); `sprig.abbrevboth` ports `goutils.AbbreviateFull` whole ([#45](https://github.com/promptctl/go-template-js/pull/45)); 0.12.0 cut ([#54](https://github.com/promptctl/go-template-js/pull/54)) ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-11-02)).
- `brandon-fryslie/rich-js` — 5 commits: 0.29.0 renames non-standard names to industry-standard terms (breaking) ([#540](https://github.com/brandon-fryslie/rich-js/pull/540)); NEL ends a line, every other C1 control shows a stand-in ([#537](https://github.com/brandon-fryslie/rich-js/pull/537)); a running App asks its terminal — `terminalColors` reads OSC 10/11 ([#538](https://github.com/brandon-fryslie/rich-js/pull/538)); ESC `]`, `P`, `_` are Alt keys unless an ask is awaiting a reply ([#539](https://github.com/brandon-fryslie/rich-js/pull/539)); a template's hold reaches the frame only through what it draws or decides ([#521](https://github.com/brandon-fryslie/rich-js/pull/521)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-11-02)).
- `promptctl/memento` — 4 commits: 0.12.0 cut ([#37](https://github.com/promptctl/memento/pull/37)); the worktree-guard words Claude Code refuses are spelled out in the handoff command ([#36](https://github.com/promptctl/memento/pull/36)) ([commits](https://github.com/promptctl/memento/commits?author=brandon-fryslie&since=2026-11-02)).

### This Week

- `promptctl/cc-candybar` — 154 commits: isolated-daemon epic — `createDaemon` is a value closed by the process that serves it ([#520](https://github.com/promptctl/cc-candybar/pull/520)), a connection runs over any stream ([#521](https://github.com/promptctl/cc-candybar/pull/521)), a launch carries its owner so a closed daemon's work is refused ([#523](https://github.com/promptctl/cc-candybar/pull/523)), the draw's output is a Frame every byte derives from ([#550](https://github.com/promptctl/cc-candybar/pull/550)), a one-shot reader asks for the Frame ([#553](https://github.com/promptctl/cc-candybar/pull/553)), in-process daemon tests run in the jest worker ([#524](https://github.com/promptctl/cc-candybar/pull/524)); dependency-injection refactors — Timekeeper, Host, Spawner/ProcessProbe, `createDaemon` input adapters ([#583](https://github.com/promptctl/cc-candybar/pull/583), [#585](https://github.com/promptctl/cc-candybar/pull/585), [#586](https://github.com/promptctl/cc-candybar/pull/586), [#602](https://github.com/promptctl/cc-candybar/pull/602)); joiners — adjacent row positions never select one tone ([#494](https://github.com/promptctl/cc-candybar/pull/494)), two colours at every depth across hue turns ([#508](https://github.com/promptctl/cc-candybar/pull/508), [#512](https://github.com/promptctl/cc-candybar/pull/512)); plugins — a repo's own load as `repo.<name>` beside installed `plugins.<name>` ([#489](https://github.com/promptctl/cc-candybar/pull/489)), diagnostics indicator aggregates errors ([#483](https://github.com/promptctl/cc-candybar/pull/483)); live-bar landscape explorer ([#544](https://github.com/promptctl/cc-candybar/pull/544)); tmux renderer offered inside tmux ([#499](https://github.com/promptctl/cc-candybar/pull/499)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-10-27)).
- `promptctl/cc-hands` — 73 commits: Clock-injection series across sessions/voice/brain/root packages ([#428](https://github.com/promptctl/cc-hands/pull/428)–[#434](https://github.com/promptctl/cc-hands/pull/434)); wake word heard while hands speaks cuts a reply ([#400](https://github.com/promptctl/cc-hands/pull/400)); Ctrl-Q submits the typed turn ([#413](https://github.com/promptctl/cc-hands/pull/413)); each speaker in each hold identified by voiceprint against hands' own TTS in shadow ([#408](https://github.com/promptctl/cc-hands/pull/408)); S2 end-to-end against the mock brain ([#406](https://github.com/promptctl/cc-hands/pull/406)); a stop's Ctrl-C goes once Claude Code has acted on its Escape ([#405](https://github.com/promptctl/cc-hands/pull/405)); brain runs in a tmux session a person can attach to ([#402](https://github.com/promptctl/cc-hands/pull/402)); any Kyutai voice spoken in, named by repo path ([#394](https://github.com/promptctl/cc-hands/pull/394)); `merge-pr.sh` exits only once the PR merged or will not ([#397](https://github.com/promptctl/cc-hands/pull/397)) ([commits](https://github.com/promptctl/cc-hands/commits?author=brandon-fryslie&since=2026-10-27)).
- `promptctl/links-issue-tracker` — 52 commits: scale epic — rank keys stop growing and respace stays local ([#843](https://github.com/promptctl/links-issue-tracker/pull/843)), one ticket's neighbours read the rows they order ([#845](https://github.com/promptctl/links-issue-tracker/pull/845)), a write's stamp reads its family's instants alone ([#846](https://github.com/promptctl/links-issue-tracker/pull/846)), top-level ids count through an index ([#847](https://github.com/promptctl/links-issue-tracker/pull/847)), rank set writes only the issues it names ([#848](https://github.com/promptctl/links-issue-tracker/pull/848)), a write flushes the drive once ([#850](https://github.com/promptctl/links-issue-tracker/pull/850)), open of an existing store takes no bootstrap lock ([#852](https://github.com/promptctl/links-issue-tracker/pull/852)), compaction keeps its engine ([#853](https://github.com/promptctl/links-issue-tracker/pull/853)); schema-reversibility and -ceiling design ([#855](https://github.com/promptctl/links-issue-tracker/pull/855), [#856](https://github.com/promptctl/links-issue-tracker/pull/856), [#857](https://github.com/promptctl/links-issue-tracker/pull/857)); `lit downgrade --remote` / `lit upgrade --remote` ([#881](https://github.com/promptctl/links-issue-tracker/pull/881)); telemetry events across the command surface ([#858](https://github.com/promptctl/links-issue-tracker/pull/858), [#860](https://github.com/promptctl/links-issue-tracker/pull/860), [#862](https://github.com/promptctl/links-issue-tracker/pull/862), [#864](https://github.com/promptctl/links-issue-tracker/pull/864), [#871](https://github.com/promptctl/links-issue-tracker/pull/871)); `lit start` reads its lane family ([#844](https://github.com/promptctl/links-issue-tracker/pull/844)); merged-PR flow returns to the PR list ([#841](https://github.com/promptctl/links-issue-tracker/pull/841)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-10-27)).
- `promptctl/orange-drink` — 39 commits: Widgets screen built — All Batteries in Rings, List and Bars styles at all four sizes ([#37](https://github.com/promptctl/orange-drink/pull/37), [#39](https://github.com/promptctl/orange-drink/pull/39)), Device Battery widget ([#27](https://github.com/promptctl/orange-drink/pull/27)), Edit Widget device picker ([#48](https://github.com/promptctl/orange-drink/pull/48)), widget click on macOS 14 ([#42](https://github.com/promptctl/orange-drink/pull/42)), panel on widget click ([#41](https://github.com/promptctl/orange-drink/pull/41)), Appearance / Show device names / Include this Mac options ([#40](https://github.com/promptctl/orange-drink/pull/40)); temperature warning epic ([#57](https://github.com/promptctl/orange-drink/pull/57)–[#60](https://github.com/promptctl/orange-drink/pull/60)); distribution — Sparkle update in place ([#30](https://github.com/promptctl/orange-drink/pull/30)), launch-at-login from General ([#31](https://github.com/promptctl/orange-drink/pull/31)), launchd job repair ([#28](https://github.com/promptctl/orange-drink/pull/28)), helper replacement at launch ([#29](https://github.com/promptctl/orange-drink/pull/29)); macOS low-battery notification closable ([#33](https://github.com/promptctl/orange-drink/pull/33)); power-management accessory sources ([#23](https://github.com/promptctl/orange-drink/pull/23)) ([commits](https://github.com/promptctl/orange-drink/commits?author=brandon-fryslie&since=2026-10-27)).
- `brandon-fryslie/rich-js` — 26 commits: control-codes epic — every control and format code point has one disposition read by sanitizer and width measure ([#533](https://github.com/brandon-fryslie/rich-js/pull/533)), bidi controls take effect inside the content ([#534](https://github.com/brandon-fryslie/rich-js/pull/534)), format characters contained ([#535](https://github.com/brandon-fryslie/rich-js/pull/535)), C0 keeps meaning and content writes no directive ([#536](https://github.com/brandon-fryslie/rich-js/pull/536)), NEL and other C1 ([#537](https://github.com/brandon-fryslie/rich-js/pull/537)); 0.28.0 and 0.29.0 (breaking rename) ([#532](https://github.com/brandon-fryslie/rich-js/pull/532), [#540](https://github.com/brandon-fryslie/rich-js/pull/540)); animation — a frame carries one time no renderable reads in render ([#519](https://github.com/brandon-fryslie/rich-js/pull/519)), lifecycle half is an animation ([#520](https://github.com/brandon-fryslie/rich-js/pull/520)), marching-ants border effect ([#529](https://github.com/brandon-fryslie/rich-js/pull/529)); joiners — gradient seam ramp ([#517](https://github.com/brandon-fryslie/rich-js/pull/517)), seams stay visible under effects ([#516](https://github.com/brandon-fryslie/rich-js/pull/516)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-10-27)).
- `promptctl/low-talker` — 24 commits: chord-blocked box retired ([#243](https://github.com/promptctl/low-talker/pull/243)); input re-ready on engine failure ([#239](https://github.com/promptctl/low-talker/pull/239)); CoreAudio off-main cooperative pool, child processes awaited, peak reader via vDSP; test watchdog behind `make test-watchdog`; Build 10 / v0.1.0-alpha.10 ([#244](https://github.com/promptctl/low-talker/pull/244)) ([commits](https://github.com/promptctl/low-talker/commits?author=brandon-fryslie&since=2026-10-27)).
- `brandon-fryslie/dotfiles` — 20 commits: guard-session-url hardening across every leak surface ([#105](https://github.com/brandon-fryslie/dotfiles/pull/105)–[#116](https://github.com/brandon-fryslie/dotfiles/pull/116)); iTerm2 session-restore removed ([#100](https://github.com/brandon-fryslie/dotfiles/pull/100), [#101](https://github.com/brandon-fryslie/dotfiles/pull/101)); global `CLAUDE.md` operating rules condensed; worktrees created with `EnterWorktree`; `repo-session` worktree launch ([#103](https://github.com/brandon-fryslie/dotfiles/pull/103)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-10-27)).
- `promptctl/tmux-control-mode-js` — 13 commits: pane-detail epic landed with structured records and `capturePane`; WebSocket bridge disposal; cross-session layout coverage ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-10-27)).
- `promptctl/go-template-js` — 13 commits: subtemplates (`include`, `evaluateDefine`, `Defines.names()`), evaluator `%v` fidelity, engine marked-call tracking ([#42](https://github.com/promptctl/go-template-js/pull/42)), 0.12.0 cut ([#54](https://github.com/promptctl/go-template-js/pull/54)) ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-10-27)).
- `promptctl/memento` — 11 commits: close-out guidance says nothing about git; docstrings capped at five sentences; worktree exit advice removed; 0.12.0 cut ([#35](https://github.com/promptctl/memento/pull/35), [#37](https://github.com/promptctl/memento/pull/37)) ([commits](https://github.com/promptctl/memento/commits?author=brandon-fryslie&since=2026-10-27)).
- `promptctl/laws` — 7 commits: new `intent` skill ([#99](https://github.com/promptctl/laws/pull/99)) and new `code-testing` skill renamed to `testing` ([#100](https://github.com/promptctl/laws/pull/100), [#101](https://github.com/promptctl/laws/pull/101)); drop "slate" language ([#95](https://github.com/promptctl/laws/pull/95)); design-goals prose removed then restored ([#102](https://github.com/promptctl/laws/pull/102), [#103](https://github.com/promptctl/laws/pull/103)); 0.37–0.41.1 cut.

### This Month

30-day volume exceeded the search index's 1000-result cap. Top by volume within the index:

- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 236 commits
- [`promptctl/orange-drink`](https://github.com/promptctl/orange-drink) — 156
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 152
- [`promptctl/low-talker`](https://github.com/promptctl/low-talker) — 129
- [`promptctl/cc-hands`](https://github.com/promptctl/cc-hands) — 109
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 56
- [`promptctl/mock-anthropic`](https://github.com/promptctl/mock-anthropic) — 41
- [`promptctl/vhid`](https://github.com/promptctl/vhid) — 39
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 30

Languages: TypeScript, Go, Swift, Python.

---

<details>
<summary>Previous highlights</summary>

- [2026-10-29](./daily-archive/2026-10-29.md)
- [2026-10-28](./daily-archive/2026-10-28.md)
- [2026-10-27](./daily-archive/2026-10-27.md)
- [2026-10-15](./daily-archive/2026-10-15.md)
- [2026-10-14](./daily-archive/2026-10-14.md)
- [2026-10-13](./daily-archive/2026-10-13.md)
- [2026-10-12](./daily-archive/2026-10-12.md)

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

Powerline statusline for Claude Code — fork of `@owloops/claude-powerline` with CLI override flags so the entire config can live in `settings.json`. 236 commits over the past month, 154 this week as the isolated-daemon epic shifted the daemon from a process into a value the root builds and closes. The draw's output is a Frame every byte derives from ([#550](https://github.com/promptctl/cc-candybar/pull/550)); in-process daemon tests run in the jest worker ([#524](https://github.com/promptctl/cc-candybar/pull/524)); a launch carries its owner so a closed daemon's work is refused ([#523](https://github.com/promptctl/cc-candybar/pull/523)); a Timekeeper reads time and schedules work ([#586](https://github.com/promptctl/cc-candybar/pull/586)), a Host reads the process once ([#585](https://github.com/promptctl/cc-candybar/pull/585)), a Spawner and ProcessProbe sit between launches and the OS ([#602](https://github.com/promptctl/cc-candybar/pull/602)); a resident Swift forwarder delivers click URLs to the daemon ([#594](https://github.com/promptctl/cc-candybar/pull/594)); a flake quarantine ledger and per-worker daemon boot tracking land under the test tier split ([#573](https://github.com/promptctl/cc-candybar/pull/573), [#576](https://github.com/promptctl/cc-candybar/pull/576), [#578](https://github.com/promptctl/cc-candybar/pull/578)); joiners draw two colours at every depth across hue turns ([#508](https://github.com/promptctl/cc-candybar/pull/508), [#512](https://github.com/promptctl/cc-candybar/pull/512)); a live-bar landscape explorer ([#544](https://github.com/promptctl/cc-candybar/pull/544)).

### [orange-drink](https://github.com/promptctl/orange-drink)
**Swift**

A macOS menu-bar app and widgets for iPhone, iPad and Mac battery, with a privileged helper for charging controls. 156 commits over the past month, 39 this week as the Widgets screen and a temperature-warning epic landed. All Batteries ships in Rings, List, and Bars styles at all four sizes with device-picker and Appearance options ([#37](https://github.com/promptctl/orange-drink/pull/37), [#39](https://github.com/promptctl/orange-drink/pull/39), [#40](https://github.com/promptctl/orange-drink/pull/40), [#43](https://github.com/promptctl/orange-drink/pull/43), [#48](https://github.com/promptctl/orange-drink/pull/48)); the panel surfaces on widget click, on macOS 14 too ([#41](https://github.com/promptctl/orange-drink/pull/41), [#42](https://github.com/promptctl/orange-drink/pull/42)); a Device Battery widget ships ([#27](https://github.com/promptctl/orange-drink/pull/27)). The temperature warning is specified in `design-docs/alerts.md` ([#57](https://github.com/promptctl/orange-drink/pull/57)), surfaces as a pill when the battery runs warm or hot ([#58](https://github.com/promptctl/orange-drink/pull/58)), gets a row on the Alerts screen ([#59](https://github.com/promptctl/orange-drink/pull/59)), and re-arms two degrees under Warm ([#60](https://github.com/promptctl/orange-drink/pull/60)). Distribution hardened — Sparkle updates in place ([#30](https://github.com/promptctl/orange-drink/pull/30)), launchd job repair at launch ([#28](https://github.com/promptctl/orange-drink/pull/28)), release refuses a commit whose tests did not pass ([#53](https://github.com/promptctl/orange-drink/pull/53)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 2★**

Agent-native issue tracker — `lit`, backed by a Dolt-shaped store with containment, dependencies and labels. 152 commits over the past month, 52 this week. The scale epic closed — rank keys stop growing with respace staying local, one ticket's neighbours read the rows they order, a write's stamp reads its family's instants alone, top-level ids count through an index, a write flushes the drive once in commit, and open of an existing store takes no bootstrap lock ([#843](https://github.com/promptctl/links-issue-tracker/pull/843), [#845](https://github.com/promptctl/links-issue-tracker/pull/845)–[#848](https://github.com/promptctl/links-issue-tracker/pull/848), [#850](https://github.com/promptctl/links-issue-tracker/pull/850), [#852](https://github.com/promptctl/links-issue-tracker/pull/852)). Schema reversibility designed and enforced — every raise steps back losslessly ([#856](https://github.com/promptctl/links-issue-tracker/pull/856)), every lit carries a released-schema ceiling ([#857](https://github.com/promptctl/links-issue-tracker/pull/857)), CI proves migrations round-trip losslessly ([#874](https://github.com/promptctl/links-issue-tracker/pull/874)); `lit downgrade --remote` and `lit upgrade --remote` ([#881](https://github.com/promptctl/links-issue-tracker/pull/881)); migration 12's top-level id index pulled from master before any release could carry it ([#855](https://github.com/promptctl/links-issue-tracker/pull/855)). Telemetry events land across the command surface — rank sets, tree-order reads, workspace resolution, `lit doctor`, `lit history`, `lit dep`, `lit followup` ([#858](https://github.com/promptctl/links-issue-tracker/pull/858), [#860](https://github.com/promptctl/links-issue-tracker/pull/860), [#862](https://github.com/promptctl/links-issue-tracker/pull/862), [#864](https://github.com/promptctl/links-issue-tracker/pull/864), [#871](https://github.com/promptctl/links-issue-tracker/pull/871)).

</td>
<td width="50%" valign="top">

### [low-talker](https://github.com/promptctl/low-talker)
**Swift · 1★**

Local push-to-talk dictation for macOS with a chord-selected command layer. 129 commits over the past month, 24 this week; Build 10 cut as v0.1.0-alpha.10 ([#244](https://github.com/promptctl/low-talker/pull/244)). The "begins no dictation" box retired — a chord blocked by held modifiers surfaces nothing ([#243](https://github.com/promptctl/low-talker/pull/243)); a microphone stopped mid-press is readied again for the next press, only the newest engine's failure readies a new input, so a late stop cannot take the input from under the next press ([#239](https://github.com/promptctl/low-talker/pull/239)); a cancel decides the listen at once with no start or queued ready following it. CoreAudio starts off the main thread with child processes awaited so the test process keeps its cooperative pool; one peak reader serves clips and windows via vDSP; a watchdog times and kills only its own test process behind `make test-watchdog`.

### [cc-hands](https://github.com/promptctl/cc-hands)
**Python · 1★**

Voice for Claude Code — speak to a session over a chord, hear its reply, run a brain that holds its own account on a dedicated Claude Code behind the proxy. 109 commits over the past month, 73 this week. The Clock-injection series dropped ambient time: one `Clock` reads time, ids, and randomness, bound at the composition root ([#434](https://github.com/promptctl/cc-hands/pull/434)) and received by the sessions ([#428](https://github.com/promptctl/cc-hands/pull/428)), voice ([#430](https://github.com/promptctl/cc-hands/pull/430)), and brain ([#432](https://github.com/promptctl/cc-hands/pull/432)) packages. The brain runs in a tmux session a person can attach to ([#402](https://github.com/promptctl/cc-hands/pull/402)); Ctrl-Q submits the typed turn ([#413](https://github.com/promptctl/cc-hands/pull/413), [#422](https://github.com/promptctl/cc-hands/pull/422)); side questions forked from a turn ending in system messages are accepted ([#423](https://github.com/promptctl/cc-hands/pull/423)); the wake word heard while hands speaks cuts a reply ([#400](https://github.com/promptctl/cc-hands/pull/400)); any Kyutai voice can be spoken in, named by repo path ([#394](https://github.com/promptctl/cc-hands/pull/394)); each speaker in each hold is identified by voiceprint against hands' own TTS in shadow ([#408](https://github.com/promptctl/cc-hands/pull/408)).

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript · MIT**

A port of Python's Rich to TypeScript — markup, tables, trees, syntax, progress, tracebacks, Live, and an App runtime that routes focus and the pointer. 56 commits over the past month, 26 this week. The control-codes epic unified every control and format code point under one disposition read by both sanitizer and width measure ([#533](https://github.com/brandon-fryslie/rich-js/pull/533)); bidi controls take effect inside the content that holds them ([#534](https://github.com/brandon-fryslie/rich-js/pull/534)); C0 keeps its meaning while content writes no directive ([#536](https://github.com/brandon-fryslie/rich-js/pull/536)); NEL ends a line and every other C1 shows a stand-in ([#537](https://github.com/brandon-fryslie/rich-js/pull/537)). 0.29.0 renames non-standard names to industry-standard terms (breaking) ([#540](https://github.com/brandon-fryslie/rich-js/pull/540)). Animation — a frame carries one time no renderable reads in render ([#519](https://github.com/brandon-fryslie/rich-js/pull/519)); joiners draw gradient-seam ramps that stay visible under effects ([#516](https://github.com/brandon-fryslie/rich-js/pull/516), [#517](https://github.com/brandon-fryslie/rich-js/pull/517)).

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
