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

`low-talker` didn't exist last Wednesday. It has forty-three commits now — a Swift menu-bar agent for push-to-talk dictation on macOS, from the founding doc through the microphone permission dance, an event tap on Right Option, a virtual keyboard driver that types through a root helper reached over XPC, and today's onboarding flow that lists what must hold before the app is useful. New repos rarely reach "the machine can type" in a week. This one did.

Something else showing up across the week: docs that name methods, classes, or options that don't exist getting cut down to what does. `rich-js`'s docs arc deleted the logging page for a class Console doesn't have, described the Pretty renderable that exists rather than the repr protocol that doesn't, and rewrote the console page around the eight methods it has instead of the fourteen it doesn't. A doc that names what isn't there is worse than no doc at all.

Today's `elvenspeak` commits pull piper out of every test file that named it. The pipeline is a fleet now, and asking the seam's properties of the artifact over HTTP means no test has to know which engine answered.

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

*Updated September 9, 2026*

### Last 24 Hours

- `brandon-fryslie/dotfiles` — 8 commits: reviewer runs as ssssmokey then brandroid as CI quotas hit and shift ([039def8](https://github.com/brandon-fryslie/dotfiles/commit/039def810cf5cfe5e6a95a2e3ce8f74c22b0d7a7), [0f9b35b](https://github.com/brandon-fryslie/dotfiles/commit/0f9b35b)); discarding the generated review workflow made unrepresentable behind a registered guard whose rule is stated ([e934ca5](https://github.com/brandon-fryslie/dotfiles/commit/e934ca5), [0625014](https://github.com/brandon-fryslie/dotfiles/commit/0625014), [74c7be3](https://github.com/brandon-fryslie/dotfiles/commit/74c7be3)); Claude session URLs stopped at the source, with the fix kept in git ([0d1abc1](https://github.com/brandon-fryslie/dotfiles/commit/0d1abc1)); "never publish session links or transcripts" added as an enforceable rule ([d723b59](https://github.com/brandon-fryslie/dotfiles/commit/d723b59)); orphaned `.claude/skills/next` copy dropped ([57b90d5](https://github.com/brandon-fryslie/dotfiles/commit/57b90d5)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-09-08)).
- `promptctl/elvenspeak` — 8 commits: the `piper-pipeline-4mx` arc took piper out of `test_api`, `test_main`, and the conformance table, moved models out of the last two engine test files, taught the stub fleet to speak with conformance running on every image, and paid down what `speaks.py` was owed ([commits](https://github.com/promptctl/elvenspeak/commits?author=brandon-fryslie&since=2026-09-08)); the router leg boots against a stub fleet ([#45](https://github.com/promptctl/elvenspeak/pull/45)).
- `brandon-fryslie/low-talker` — 4 commits: onboarding shows one list of what must hold across CLI and menu alike ([#39](https://github.com/brandon-fryslie/low-talker/pull/39)); a saved config takes effect where it stands, and one that cannot be read costs nothing ([#37](https://github.com/brandon-fryslie/low-talker/pull/37)); the keyboard files its own answer with the setup assistant ([#41](https://github.com/brandon-fryslie/low-talker/pull/41)); orphaned `.claude/skills/next` copy dropped ([#42](https://github.com/brandon-fryslie/low-talker/pull/42)).
- `promptctl/cc-candybar` — 4 commits: the global menu leads the bar as one accent-coloured symbol ([#224](https://github.com/promptctl/cc-candybar/pull/224)); segments and presets merge by name then by field, so a first durable write lands one field ([#225](https://github.com/promptctl/cc-candybar/pull/225)); a duplicate object key warns at load, named by file and line ([#227](https://github.com/promptctl/cc-candybar/pull/227)); the lifetime tests await a named condition instead of a deadline ([#226](https://github.com/promptctl/cc-candybar/pull/226)).

### This Week

- `promptctl/links-issue-tracker` — 52 commits: 0.11.0 through 0.14.0 released across the week — the `/next` skill ships from the binary as a managed template with epic-major selection ([#460](https://github.com/promptctl/links-issue-tracker/pull/460), [#463](https://github.com/promptctl/links-issue-tracker/pull/463)), templates that name commands lit does not dispatch are refused ([#462](https://github.com/promptctl/links-issue-tracker/pull/462)), sync-target-resolution deduplicated ([#467](https://github.com/promptctl/links-issue-tracker/pull/467)), the DDL-text toolkit split out of migration_runner.go ([#470](https://github.com/promptctl/links-issue-tracker/pull/470)), the flag framework and error taxonomy split out of cli.go ([#471](https://github.com/promptctl/links-issue-tracker/pull/471)), claim eligibility folded to one verdict replacing three routing gates ([#479](https://github.com/promptctl/links-issue-tracker/pull/479)), a frozen dependency stops blocking readiness ([#480](https://github.com/promptctl/links-issue-tracker/pull/480)), the store-seam epic closed with the contract growing a clock ([#488](https://github.com/promptctl/links-issue-tracker/pull/488)), lock waits report themselves and name their holder ([#498](https://github.com/promptctl/links-issue-tracker/pull/498)), and the repo is now an installable Claude plugin marketplace ([#494](https://github.com/promptctl/links-issue-tracker/pull/494)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-09-02)).
- `promptctl/crom` — 48 commits: the whole tool shipped this week — Chrome-profile launcher with stable reason-slug errors and a --json failure envelope ([#32](https://github.com/promptctl/crom/pull/32), [#35](https://github.com/promptctl/crom/pull/35)), Chrome-death fails the launch instead of blaming the port ([#16](https://github.com/promptctl/crom/pull/16)), a port ledger that names strangers holding a reservation ([#37](https://github.com/promptctl/crom/pull/37), [#40](https://github.com/promptctl/crom/pull/40)), leaked-reservation reclamation tested on one machine carrying every leak ([#41](https://github.com/promptctl/crom/pull/41)–[#42](https://github.com/promptctl/crom/pull/42)), drift detection on `crom up` with argv rewrites pinned to observation ([#44](https://github.com/promptctl/crom/pull/44)–[#47](https://github.com/promptctl/crom/pull/47)), machine-global cache-free snapshots taken only from a stopped browser ([#62](https://github.com/promptctl/crom/pull/62)), and publication as a Claude plugin marketplace ([#64](https://github.com/promptctl/crom/pull/64)) ([commits](https://github.com/promptctl/crom/commits?author=brandon-fryslie&since=2026-09-02)).
- `brandon-fryslie/low-talker` — 43 commits: new repo. A Swift menu-bar agent for push-to-talk dictation on macOS, from founding doc and SwiftPM scaffold ([#1](https://github.com/brandon-fryslie/low-talker/pull/1)–[#5](https://github.com/brandon-fryslie/low-talker/pull/5)) through a WhisperKit transcriber and 16 kHz mono capture ring ([#8](https://github.com/brandon-fryslie/low-talker/pull/8)–[#9](https://github.com/brandon-fryslie/low-talker/pull/9)), microphone permission and an event tap for Right Option hold-vs-tap ([#11](https://github.com/brandon-fryslie/low-talker/pull/11), [#15](https://github.com/brandon-fryslie/low-talker/pull/15)), per-mode initial-prompt vocabulary that keeps word timings ([#21](https://github.com/brandon-fryslie/low-talker/pull/21)), a virtual keyboard driver reaching a root helper over XPC ([#29](https://github.com/brandon-fryslie/low-talker/pull/29)), text and chords delivered through one typist ([#30](https://github.com/brandon-fryslie/low-talker/pull/30)), and today's onboarding flow ([#39](https://github.com/brandon-fryslie/low-talker/pull/39)) ([commits](https://github.com/brandon-fryslie/low-talker/commits?author=brandon-fryslie&since=2026-09-02)).
- `brandon-fryslie/rich-js` — 43 commits: node/browser seam sealed — the barrel stays browser-safe under a checked host-access list ([#73](https://github.com/brandon-fryslie/rich-js/pull/73), [#75](https://github.com/brandon-fryslie/rich-js/pull/75)); every box style rewritten as the reference's 8×4 grid and pinned against Python Rich ([#94](https://github.com/brandon-fryslie/rich-js/pull/94)–[#95](https://github.com/brandon-fryslie/rich-js/pull/95)); markup routed through one crossing with tag grammar taken from the reference ([#100](https://github.com/brandon-fryslie/rich-js/pull/100)–[#102](https://github.com/brandon-fryslie/rich-js/pull/102)); docs cut back to what exists — logging page deleted, pretty page rewritten around the actual renderable, console page around the eight methods it has ([#81](https://github.com/brandon-fryslie/rich-js/pull/81)–[#85](https://github.com/brandon-fryslie/rich-js/pull/85)); word-wrap ordered before overflow ([#98](https://github.com/brandon-fryslie/rich-js/pull/98)); a colour ramp primitive over OKLCH stops ([#92](https://github.com/brandon-fryslie/rich-js/pull/92)); justify "full" distributes gaps between words ([#111](https://github.com/brandon-fryslie/rich-js/pull/111)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-09-02)).
- `promptctl/cc-candybar` — 32 commits: the config file becomes the one durable store ([#203](https://github.com/promptctl/cc-candybar/pull/203)), with root sections merging by named row ([#209](https://github.com/promptctl/cc-candybar/pull/209)); custom-segments arc reads shell/file sources through one parse seam, dotted-path reads, and thresholds off one ramp call ([#221](https://github.com/promptctl/cc-candybar/pull/221)–[#223](https://github.com/promptctl/cc-candybar/pull/223)); theme-vocabulary render — closed cell paints from vocabulary, hue cursor deleted, disclosure trigger wears the band's state ([#210](https://github.com/promptctl/cc-candybar/pull/210)–[#211](https://github.com/promptctl/cc-candybar/pull/211)); doctor menu ships with a first check that repairs Claude Code's 256-colour downgrade in tmux ([#216](https://github.com/promptctl/cc-candybar/pull/216)); daemon derives its V8 heap cap from the RSS budget after a SIGABRT crash-loop outage ([#197](https://github.com/promptctl/cc-candybar/pull/197)); a digest-identified update notice ([#208](https://github.com/promptctl/cc-candybar/pull/208)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-09-02)).
- `promptctl/elvenspeak` — 31 commits: `piper-routing-7e2` closed — voices name the engine that speaks them ([#29](https://github.com/promptctl/elvenspeak/pull/29)) and Spanish is spoken in Spanish ([#32](https://github.com/promptctl/elvenspeak/pull/32)); Chatterbox lands as the fourth engine ([#33](https://github.com/promptctl/elvenspeak/pull/33)); `piper-memory-9rc` gives the synthesis ceiling an owner and refuses to serve confined with a ceiling nobody chose ([#36](https://github.com/promptctl/elvenspeak/pull/36), [#38](https://github.com/promptctl/elvenspeak/pull/38)); `piper-build-b4h` runs the image and makes it prove it serves ([#41](https://github.com/promptctl/elvenspeak/pull/41)–[#43](https://github.com/promptctl/elvenspeak/pull/43)); `piper-pipeline-4mx` closed today by pulling piper out of `test_api`/`test_main`/the conformance table and taking the model cache out of both gates ([commits](https://github.com/promptctl/elvenspeak/commits?author=brandon-fryslie&since=2026-09-02)).
- `brandon-fryslie/dotfiles` — 21 commits: reviewer CI account rotation across quotas (SSSSSMOKEY → QWR → BRANDROID → SSSSSMOKEY); dotbot now manages the CA trust bundle ([3f74e2b](https://github.com/brandon-fryslie/dotfiles/commit/3f74e2b)); interception CA stops being exported to every node process ([a7b90a9](https://github.com/brandon-fryslie/dotfiles/commit/a7b90a9)); Claude session URLs stopped at the source with the fix pinned in git ([0d1abc1](https://github.com/brandon-fryslie/dotfiles/commit/0d1abc1)); continuum's periodic save disabled instead of mirrored ([993db06](https://github.com/brandon-fryslie/dotfiles/commit/993db06)); truecolor reaches both sides of the tmux boundary ([8a48523](https://github.com/brandon-fryslie/dotfiles/commit/8a48523)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-09-02)).
- `promptctl/memento` — 19 commits: `/next` retired as an executable skill — now ships from the lit binary as a pointer stub with memento 0.2.0 ([#2](https://github.com/promptctl/memento/pull/2)); ceiling settings live in memento.conf per user, project, and session ([#5](https://github.com/promptctl/memento/pull/5)); auto-bottle folds into memento as one plugin ([#6](https://github.com/promptctl/memento/pull/6)); address-pr-reviews reads every page of a PR's reviews before answering whether the current one is there ([#8](https://github.com/promptctl/memento/pull/8)); a session can move or lift its own context ceiling, set by files only ([260bdfc](https://github.com/promptctl/memento/commit/260bdfc)).
- `promptctl/laws` — 16 commits: horizon arc — `/goal` drives across session boundaries unattended ([#49](https://github.com/promptctl/laws/pull/49)), the auth check makes a request rather than reading a stale credential ([#50](https://github.com/promptctl/laws/pull/50)), the observer ignores headless claude subprocesses ([#51](https://github.com/promptctl/laws/pull/51)); injector enacts the craft switch live, then retires the BUN_INSPECT channel and relaunch apparatus ([#46](https://github.com/promptctl/laws/pull/46)–[#48](https://github.com/promptctl/laws/pull/48)); prompt spine split every text into objective vs constraint at distance zero ([#40](https://github.com/promptctl/laws/pull/40)–[#41](https://github.com/promptctl/laws/pull/41)).
- `promptctl/openconv` — 15 commits: a conversation can choose the engine, not just the voice ([#19](https://github.com/promptctl/openconv/pull/19)); session language now reaches the TTS call, where it was being dropped ([#20](https://github.com/promptctl/openconv/pull/20)); a voice selector on the call page that can change mid-call ([#23](https://github.com/promptctl/openconv/pull/23)); the cutoff gets two seconds to separate instead of guessing one ([#21](https://github.com/promptctl/openconv/pull/21)); a second-inference gate timed so a GPU that failed to initialise cannot serve calls ([#26](https://github.com/promptctl/openconv/pull/26)).
- `promptctl/textual-js` — 11 commits: widgets sealed as one implementation each — Label is Static under a second name ([#13](https://github.com/promptctl/textual-js/pull/13)), Digits is a font plus identity ([#16](https://github.com/promptctl/textual-js/pull/16)), LoadingIndicator is a still frame ([#19](https://github.com/promptctl/textual-js/pull/19)), Welcome composes children so it's not a ContentWidget ([#21](https://github.com/promptctl/textual-js/pull/21)); Placeholder emits the cells it paints ([#17](https://github.com/promptctl/textual-js/pull/17)); the header paints one resolved title screen-over-app ([#15](https://github.com/promptctl/textual-js/pull/15)).
- `promptctl/horizon-run-20260902T045432Z` — 10 commits: black-box conformance rig for a mackup-alike link tool ([#2](https://github.com/promptctl/horizon-run-20260902T045432Z/pull/2)); built-in application catalog of 614 definitions pinned to the appendix ([#4](https://github.com/promptctl/horizon-run-20260902T045432Z/pull/4)); sync primitives with a permission clamp and drift detection ([#8](https://github.com/promptctl/horizon-run-20260902T045432Z/pull/8)–[#9](https://github.com/promptctl/horizon-run-20260902T045432Z/pull/9)); link install as appspec/06's per-file procedure over a shared per-file executor ([#11](https://github.com/promptctl/horizon-run-20260902T045432Z/pull/11)).

### This Month

600 commits across 22 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 92 commits
- [`promptctl/crom`](https://github.com/promptctl/crom) — 60
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 60
- [`promptctl/laws`](https://github.com/promptctl/laws) — 57
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 52
- [`promptctl/elvenspeak`](https://github.com/promptctl/elvenspeak) — 50
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 48
- [`promptctl/openconv`](https://github.com/promptctl/openconv) — 44
- [`brandon-fryslie/low-talker`](https://github.com/brandon-fryslie/low-talker) — 43
- [`promptctl/memento`](https://github.com/promptctl/memento) — 23

Languages: Go, TypeScript, Python, Rust, Swift, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-08-20](./daily-archive/2026-08-20.md)
- [2026-08-19](./daily-archive/2026-08-19.md)
- [2026-08-18](./daily-archive/2026-08-18.md)
- [2026-08-17](./daily-archive/2026-08-17.md)
- [2026-08-16](./daily-archive/2026-08-16.md)
- [2026-08-15](./daily-archive/2026-08-15.md)
- [2026-08-14](./daily-archive/2026-08-14.md)

</details>

<!-- RECENT-ACTIVITY:END -->

<!-- PREVIOUS-WORK:START -->

### Previous Engineering Work

- **[Week of August 17](./previous-work/2026/2026-08-17.md)** — *in progress*
- **[Week of August 10](./previous-work/2026/2026-08-10.md)** — slopspot RAG stack and freshness trail · cc-candybar per-segment palette overrides · lit sync safety and licensing clean-room · cc-dump Anthropic-only proxy consolidation
- **[Week of August 3](./previous-work/2026/2026-08-03.md)** — lit workflows 0.4.0 · cc-candybar option-domain seam and theme picker · slopspot-paste editor made editable end-to-end · room-eq-wizard-mcp surface completion
- **[Week of July 27](./previous-work/2026/2026-07-27.md)** — laws evals harness lands · macklebox and room-eq-wizard-mcp bootstrapped · links-issue-tracker supply-chain gating · stats card and weekly-archive contract
- **[Week of July 20](./previous-work/2026/2026-07-20.md)** — tmux-control-mode-js complexity audit splits · dotfiles session-handoff and iterm2-restore transports · laws skill expansion 0.16→0.20 · lit sync epic and candybar consolidation
- **[Week of July 13](./previous-work/2026/2026-07-13.md)** — cc-dump 0.3.0 release · laws hooks and comments-law reshape · tmux publish-gate hardening
- **[Week of July 6](./previous-work/2026/2026-07-06.md)** — tinkerpadai launch arc · links-issue-tracker types-are-the-program recut · slopspot-paste embeds & diffs · crowdship money layer

[Full archive →](./previous-work/)

<!-- PREVIOUS-WORK:END -->

---

## Selected Projects

<!-- SELECTED-PROJECTS:START -->
<table>
<tr>
<td width="50%" valign="top">

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. 113 commits over the past 90 days. 52 commits this past week promoted the tracker from 0.11.0 through 0.14.0 — the `/next` skill ships from the binary as a managed template with epic-major selection ([#460](https://github.com/promptctl/links-issue-tracker/pull/460), [#463](https://github.com/promptctl/links-issue-tracker/pull/463)), sync-target-resolution deduplicated ([#467](https://github.com/promptctl/links-issue-tracker/pull/467)), the flag framework and error taxonomy split out of cli.go ([#471](https://github.com/promptctl/links-issue-tracker/pull/471)), claim eligibility folded to one verdict replacing three routing gates ([#479](https://github.com/promptctl/links-issue-tracker/pull/479)), the store-seam epic closed with the contract growing a clock ([#488](https://github.com/promptctl/links-issue-tracker/pull/488)), and the repo is now presented as an installable Claude plugin marketplace ([#494](https://github.com/promptctl/links-issue-tracker/pull/494)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Environment and tooling substrate — dotbot-driven config, per-machine trust, and the Claude Code / lit / candybar wiring across Brandon's fleet. 80 commits over the past 90 days. 21 commits this past week rotated the reviewer CI account across quotas, put dotbot in charge of the CA trust bundle ([3f74e2b](https://github.com/brandon-fryslie/dotfiles/commit/3f74e2b)), stopped exporting the interception CA to every node process ([a7b90a9](https://github.com/brandon-fryslie/dotfiles/commit/a7b90a9)), and suppressed Claude session URLs at the source with the fix pinned in git ([0d1abc1](https://github.com/brandon-fryslie/dotfiles/commit/0d1abc1)).

### [laws](https://github.com/promptctl/laws)
**JavaScript · MIT · 4★**

Claude Code plugin: laws for writing high quality code and llm guidance. 74 commits over the past 90 days. 16 commits this past week extended the horizon arc — `/goal` drives across session boundaries unattended ([#49](https://github.com/promptctl/laws/pull/49)), the auth check now makes a request rather than reading a stale credential ([#50](https://github.com/promptctl/laws/pull/50)), and the observer ignores headless claude subprocesses ([#51](https://github.com/promptctl/laws/pull/51)); the injector enacted the craft switch live and then retired the BUN_INSPECT channel and the relaunch apparatus ([#46](https://github.com/promptctl/laws/pull/46)–[#48](https://github.com/promptctl/laws/pull/48)).

</td>
<td width="50%" valign="top">

### [crom](https://github.com/promptctl/crom)
**Python · 1★**

Chrome-profile launcher and orchestration CLI — named failure envelopes, tracked reservations, machine-global snapshots, drift detection on relaunch, published as a Claude Code plugin marketplace. 60 commits over the past 90 days; the whole tool shipped this week. 48 commits this past week — Chrome-death fails the launch rather than blaming the port ([#16](https://github.com/promptctl/crom/pull/16)), stable reason-slug errors with a --json failure envelope ([#32](https://github.com/promptctl/crom/pull/32), [#35](https://github.com/promptctl/crom/pull/35)), a port ledger that names strangers holding a reservation ([#37](https://github.com/promptctl/crom/pull/37), [#40](https://github.com/promptctl/crom/pull/40)), drift detection with argv rewrites pinned to observation ([#47](https://github.com/promptctl/crom/pull/47)), machine-global cache-free snapshots taken only from a stopped browser ([#62](https://github.com/promptctl/crom/pull/62)), and publication as a Claude plugin marketplace ([#64](https://github.com/promptctl/crom/pull/64)).

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript**

A JavaScript port of Python's Rich — Panel, Table, Console, markup, and text rendering pinned frame-for-frame against the reference. 54 commits over the past 90 days. 43 commits this past week sealed the node/browser seam ([#73](https://github.com/brandon-fryslie/rich-js/pull/73)–[#75](https://github.com/brandon-fryslie/rich-js/pull/75)), rewrote every box style as the reference's 8×4 grid and pinned each frame against Python Rich ([#94](https://github.com/brandon-fryslie/rich-js/pull/94)–[#95](https://github.com/brandon-fryslie/rich-js/pull/95)), routed markup through one crossing with tag grammar taken from the reference ([#100](https://github.com/brandon-fryslie/rich-js/pull/100)–[#102](https://github.com/brandon-fryslie/rich-js/pull/102)), and cut docs back to what exists ([#81](https://github.com/brandon-fryslie/rich-js/pull/81)–[#85](https://github.com/brandon-fryslie/rich-js/pull/85)).

### [openconv](https://github.com/promptctl/openconv)
**Rust**

Self-hosted server compatible with the ElevenLabs Conversational AI API. 53 commits over the past 90 days. 15 commits this past week let a conversation choose the engine, not just the voice ([#19](https://github.com/promptctl/openconv/pull/19)); carried the session language to the TTS call, where it was being dropped ([#20](https://github.com/promptctl/openconv/pull/20)); added a voice selector that can change mid-call ([#23](https://github.com/promptctl/openconv/pull/23)); and timed a second-inference gate so a GPU that failed to initialise cannot serve calls ([#26](https://github.com/promptctl/openconv/pull/26)).

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
