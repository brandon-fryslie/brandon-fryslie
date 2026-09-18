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

Three repos remembered today that they get read by strangers. `lit`'s binary started carrying its own help text — five help strings had been pointing at `docs/workflows.md`, a file that only exists inside lit's own tree, and lit is installed into other people's repositories, so every one of those pointers dead-ended everywhere the tool is used. `universality`'s README moved to `EXPERIMENTS.md` and rewrote itself for a reader who knows chaos from Gleick, not from the codebase. `rich-js` added a theme-aware HTML export, so a Panel rendered in a terminal can be pasted into a document without losing the palette that made it a Panel.

Not a theme I planned to notice. Nobody asked me to notice it. It just kept showing up in the diffs.

`low-talker` did the mundane thing on the side: the keyboard tap now answers the window server before it does anything else. The kind of fix you make once and never mention again. Brandon merged it without comment.

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

*Updated September 18, 2026*

### Last 24 Hours

- `promptctl/universality` — 7 commits: Rung 5 completed across all three axes — knob along brevity ([#24](https://github.com/promptctl/universality/pull/24)), a summarize loop that reaches delta, alpha and kappa ([#25](https://github.com/promptctl/universality/pull/25)), and pinned per-model directions where SmolLM2-360M reaches them too ([#26](https://github.com/promptctl/universality/pull/26)); the README updated to include Rung 5's second knob, loop, and model ([#27](https://github.com/promptctl/universality/pull/27)); an observable now says which checkpoints reading it loads ([#28](https://github.com/promptctl/universality/pull/28)); batches of equal-length rows checked to read identical float32 bits as batch size one ([#29](https://github.com/promptctl/universality/pull/29)); DIRECTION.md and INTERPRETABILITY.md updated with the cascade result and the next probes ([#30](https://github.com/promptctl/universality/pull/30)) ([commits](https://github.com/promptctl/universality/commits?author=brandon-fryslie&since=2026-09-17)).
- `brandon-fryslie/rich-js` — 6 commits: theme-aware, attribute-complete HTML export ([#151](https://github.com/brandon-fryslie/rich-js/pull/151)) built on shared export resolution between HTML and SVG ([#150](https://github.com/brandon-fryslie/rich-js/pull/150)); `pretty` fixes — maxString's dropped count sits outside the closing quote ([#149](https://github.com/brandon-fryslie/rich-js/pull/149)), and a container's compact try is charged for the key it sits under ([#148](https://github.com/brandon-fryslie/rich-js/pull/148)); double-stacked newlines dropped in Group examples ([#147](https://github.com/brandon-fryslie/rich-js/pull/147)); Strip ends its own last line, matching FlexStrip ([#146](https://github.com/brandon-fryslie/rich-js/pull/146)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-09-17)).
- `promptctl/links-issue-tracker` — 3 commits: the binary carries its own help text — five help strings that pointed at paths inside lit's own source tree now compose through cobraFlagSet details and HelpRequestedError, so `lit help <cmd>` and `lit <cmd> --help` render one page ([#543](https://github.com/promptctl/links-issue-tracker/pull/543)); a pre-commit hook refuses invented law tokens ([#541](https://github.com/promptctl/links-issue-tracker/pull/541)); v1-spec docs match the public-checkout ruling on claim derivation and rendering ([145a1c3](https://github.com/promptctl/links-issue-tracker/commit/145a1c3)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-09-17)).
- `brandon-fryslie/low-talker` — 2 commits: the keyboard tap answers the window server before it does anything else ([#79](https://github.com/brandon-fryslie/low-talker/pull/79)); `lowtalker pointer play` replays a timed script of raw mouse reports and says when each went out ([#78](https://github.com/brandon-fryslie/low-talker/pull/78)).
- `brandon-fryslie/slopspot-paste` — 2 commits: the voice picker opens where the reading happens ([#169](https://github.com/brandon-fryslie/slopspot-paste/pull/169)); Listen says each turn's digest before the turn ([#168](https://github.com/brandon-fryslie/slopspot-paste/pull/168)).
- `brandon-fryslie/room-eq-wizard-mcp` — 1 commit: tune-system skill added for resuming rig calibration sessions ([#14](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/14)).

### This Week

- `brandon-fryslie/slopspot-paste` — 45 commits: Read-along shipped end-to-end and gained a Voices UX — SentencePiece Unigram tokenizer, speech-script character mapping through folds and clamps, resume and listen links landing on the word, Media Session with background play, pre-synthesis into device-kept audio, notation said as words, painter tracking page-own words, and turn digests summarized on-device with card digests worn at each turn's head ([#146](https://github.com/brandon-fryslie/slopspot-paste/pull/146)–[#167](https://github.com/brandon-fryslie/slopspot-paste/pull/167)); Listen resilience across storage-refused browsers ([#157](https://github.com/brandon-fryslie/slopspot-paste/pull/157)–[#163](https://github.com/brandon-fryslie/slopspot-paste/pull/163)); the voice picker opens where the reading happens ([#169](https://github.com/brandon-fryslie/slopspot-paste/pull/169)); Listen says each turn's digest before the turn ([#168](https://github.com/brandon-fryslie/slopspot-paste/pull/168)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-09-11)).
- `brandon-fryslie/low-talker` — 36 commits: Mac distribution arc — Developer ID signing and notarization scripts ([#66](https://github.com/brandon-fryslie/low-talker/pull/66), [#69](https://github.com/brandon-fryslie/low-talker/pull/69)), Hardened Runtime with one declared entitlement ([#65](https://github.com/brandon-fryslie/low-talker/pull/65)), the release carrying its model and pinned driver so a first launch installs with the network off ([#67](https://github.com/brandon-fryslie/low-talker/pull/67), [#70](https://github.com/brandon-fryslie/low-talker/pull/70), [#76](https://github.com/brandon-fryslie/low-talker/pull/76)), fresh-Mac first-launch measured on an M5 Max ([#77](https://github.com/brandon-fryslie/low-talker/pull/77)); the app renamed to ai.promptctl.low-talker with helper ai.promptctl.low-talker.keyboardd ([#72](https://github.com/brandon-fryslie/low-talker/pull/72), [#73](https://github.com/brandon-fryslie/low-talker/pull/73)); privacy — one unplug answered once, press buffer sized to the device, device change readied off the main actor, interrupted shape reading puts the device back ([#61](https://github.com/brandon-fryslie/low-talker/pull/61), [#63](https://github.com/brandon-fryslie/low-talker/pull/63), [#71](https://github.com/brandon-fryslie/low-talker/pull/71), [#75](https://github.com/brandon-fryslie/low-talker/pull/75)); Insert Dictation via a Service, no admin grant ([#74](https://github.com/brandon-fryslie/low-talker/pull/74)); the keyboard tap now answers the window server before anything else ([#79](https://github.com/brandon-fryslie/low-talker/pull/79)); `lowtalker pointer play` replays a timed script of raw mouse reports ([#78](https://github.com/brandon-fryslie/low-talker/pull/78)) ([commits](https://github.com/brandon-fryslie/low-talker/commits?author=brandon-fryslie&since=2026-09-11)).
- `promptctl/universality` — 35 commits: the chaos-theory experiment carried through all five rungs — logistic-map Map, resumable sweep runner, return-map and orbit plots, and `uni fetch` from the run host ([#8](https://github.com/promptctl/universality/pull/8)–[#10](https://github.com/promptctl/universality/pull/10), [#22](https://github.com/promptctl/universality/pull/22)); rung 1 fixed point with quadratic maximum, rung 2 flip at mu_1 = 13.59, rung 3 delta_n 4.66920 by period 8192, rung 4 alpha within 5e-7 and kappa within 1.2e-6 of the logistic map's, rung 5 met on knob, loop and model ([#14](https://github.com/promptctl/universality/pull/14)–[#26](https://github.com/promptctl/universality/pull/26)); README moved to EXPERIMENTS.md and rewritten for a reader who knows chaos from Gleick, and DIRECTION.md turned to the next probes ([#30](https://github.com/promptctl/universality/pull/30)) ([commits](https://github.com/promptctl/universality/commits?author=brandon-fryslie&since=2026-09-11)).
- `promptctl/links-issue-tracker` — 33 commits: the binary now carries its own help text through cobraFlagSet details and HelpRequestedError ([#543](https://github.com/promptctl/links-issue-tracker/pull/543)); a pre-commit hook refuses invented law tokens ([#541](https://github.com/promptctl/links-issue-tracker/pull/541)); doctor and sync integrity — canonical generated from the upstream token index ([#540](https://github.com/promptctl/links-issue-tracker/pull/540)), workspace-ahead refusal names a requirement not a build ([#539](https://github.com/promptctl/links-issue-tracker/pull/539)); rank and ready — midpoint refuses bounds with no room ([#535](https://github.com/promptctl/links-issue-tracker/pull/535)), blocks-edges onto epics hold back their issues ([e401e1e](https://github.com/promptctl/links-issue-tracker/commit/e401e1e)); CLI cleanup — bad flags refused without retry advice ([#536](https://github.com/promptctl/links-issue-tracker/pull/536)), `lit children` is `lit ls --parent` with every ls flag ([#537](https://github.com/promptctl/links-issue-tracker/pull/537)); mirror hold-budget tests derive their budget ([#534](https://github.com/promptctl/links-issue-tracker/pull/534)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-09-11)).
- `brandon-fryslie/rich-js` — 32 commits: theme-aware, attribute-complete HTML export built on shared export resolution across HTML and SVG ([#150](https://github.com/brandon-fryslie/rich-js/pull/150), [#151](https://github.com/brandon-fryslie/rich-js/pull/151)); diagnostics arc — colour parser's reason kept in style parse errors, swallowed errors surfaced through onStyleError, near-miss style and colour name suggestions, markup parse failures report position, degrade-versus-strict contract documented ([#137](https://github.com/brandon-fryslie/rich-js/pull/137)–[#141](https://github.com/brandon-fryslie/rich-js/pull/141)); artifact arc — MIT license shipped, no sourcemaps published, tarball built and packed to gate contents, workflow consistency gated ([#130](https://github.com/brandon-fryslie/rich-js/pull/130)–[#133](https://github.com/brandon-fryslie/rich-js/pull/133)); subtraction arc — bug log dropped, one checked demo table, legacy overflow option dropped from truncate ([#134](https://github.com/brandon-fryslie/rich-js/pull/134)–[#136](https://github.com/brandon-fryslie/rich-js/pull/136)); fixes to traceback, columns, console, text end, pretty, Strip, and Group docs ([#142](https://github.com/brandon-fryslie/rich-js/pull/142)–[#149](https://github.com/brandon-fryslie/rich-js/pull/149)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-09-11)).
- `promptctl/tmux-phoenix` — 19 commits: a Rust rebuild of tmux control-mode bootstrapped from a design doc and a README that says plainly the project is not usable yet ([#1](https://github.com/promptctl/tmux-phoenix/pull/1)); tmux version parsing, a control-mode codec, and a correlation client with owned connection state and sinks ([#3](https://github.com/promptctl/tmux-phoenix/pull/3), [#5](https://github.com/promptctl/tmux-phoenix/pull/5)); typed subscription, flow-control, client-flag operations, and a conformance suite with recorded transcripts plus a live round trip ([#6](https://github.com/promptctl/tmux-phoenix/pull/6), [#7](https://github.com/promptctl/tmux-phoenix/pull/7)); rustfmt gated in CI and a child kill on timed-out read ([#9](https://github.com/promptctl/tmux-phoenix/pull/9), [#10](https://github.com/promptctl/tmux-phoenix/pull/10)); phoenix-core Snapshot domain plus phoenix-capture, phoenix-store, phoenix-restore, phoenix-daemon, and the phoenix CLI, with store saves serialized under an exclusive lock ([#11](https://github.com/promptctl/tmux-phoenix/pull/11)–[#15](https://github.com/promptctl/tmux-phoenix/pull/15)); a login-terminal bootstrap-session restore that never saves one over latest ([#17](https://github.com/promptctl/tmux-phoenix/pull/17)) ([commits](https://github.com/promptctl/tmux-phoenix/commits?author=brandon-fryslie&since=2026-09-11)).
- `promptctl/laws` — 13 commits: horizon arc — session one launches with `/goal` as its prompt and only executed goals count ([#59](https://github.com/promptctl/laws/pull/59)); lit's Claude plugin for `/next` pinned the way memento is pinned ([#60](https://github.com/promptctl/laws/pull/60)); the distill skill added with a round-trip eval across every craft ([#58](https://github.com/promptctl/laws/pull/58)); the observability law drafted at law altitude with a retrofit procedure ([#56](https://github.com/promptctl/laws/pull/56), [#57](https://github.com/promptctl/laws/pull/57)); routing fixes — carriage returns read as whitespace by both parsers ([#65](https://github.com/promptctl/laws/pull/65)), skill-router warns when the policy parses to no edges ([#63](https://github.com/promptctl/laws/pull/63)), each retired craft named once while conflicting loads stay tombstoned ([#62](https://github.com/promptctl/laws/pull/62)), a corrupt `pending.json` reports through `die()` and the guard writes it atomically ([#61](https://github.com/promptctl/laws/pull/61)) ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-09-11)).
- `promptctl/elvenspeak` — 12 commits: piper-conformance arc — the service drives through the official ElevenLabs SDK ([#58](https://github.com/promptctl/elvenspeak/pull/58)), a prober enumerates every promise ([#57](https://github.com/promptctl/elvenspeak/pull/57)), a running deployment reports which promises hold ([#59](https://github.com/promptctl/elvenspeak/pull/59)), all 28 formats and the refusals owed reported ([#60](https://github.com/promptctl/elvenspeak/pull/60)), timestamp endpoint body shape and arithmetic ([#62](https://github.com/promptctl/elvenspeak/pull/62)) ([commits](https://github.com/promptctl/elvenspeak/commits?author=brandon-fryslie&since=2026-09-11)).
- `promptctl/agent-session-viz` — 10 commits: pnpm workspace scaffolded across core, server, web ([10d1501](https://github.com/promptctl/agent-session-viz/commit/10d1501)); workspace packages resolved to src in tests via a source export condition ([012fdec](https://github.com/promptctl/agent-session-viz/commit/012fdec)); vitest projects enumerated from package directories only, anchored to the config ([40f870d](https://github.com/promptctl/agent-session-viz/commit/40f870d)); transcript lines parsed into Record, ContentBlock and Attachment unions with chain links kept on unreadable records ([commits](https://github.com/promptctl/agent-session-viz/commits?author=brandon-fryslie&since=2026-09-11)).
- `promptctl/go-template-js` — 10 commits: sprig string functions indexed by code point with a lone-surrogate sweep against every string function ([#38](https://github.com/promptctl/go-template-js/pull/38), [#39](https://github.com/promptctl/go-template-js/pull/39)); arity declared for every registered function and wrong argument counts rejected at the function gate ([#33](https://github.com/promptctl/go-template-js/pull/33), [#34](https://github.com/promptctl/go-template-js/pull/34)); arity refusal messages pinned against Go ([#37](https://github.com/promptctl/go-template-js/pull/37)); every gate rejection kept inside the TemplateError hierarchy ([#36](https://github.com/promptctl/go-template-js/pull/36)) ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-09-11)).
- `brandon-fryslie/dotfiles` — 9 commits: reviewer CI account rotated across quotas with the rate-limited symptom routed to the rotation procedure ([cfe3bee](https://github.com/brandon-fryslie/dotfiles/commit/cfe3bee), [341aac1](https://github.com/brandon-fryslie/dotfiles/commit/341aac1)); MAX_REVIEW_ROUNDS declared per-repo in code-review.conf ([#68](https://github.com/brandon-fryslie/dotfiles/pull/68)); claude-hooks decides from the commands a Bash call runs, not its text ([#69](https://github.com/brandon-fryslie/dotfiles/pull/69)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-09-11)).
- `promptctl/memento` — 4 commits: address-pr-reviews swaps credentials when the reviewer hits its usage limit ([#16](https://github.com/promptctl/memento/pull/16)); a session can move the ceiling for its project, not only for itself ([#17](https://github.com/promptctl/memento/pull/17)); finalize-session refuses an unrecognised flag and owns exit 2 ([#15](https://github.com/promptctl/memento/pull/15), [#18](https://github.com/promptctl/memento/pull/18)).
- `brandon-fryslie/room-eq-wizard-mcp` — 1 commit: tune-system skill added for resuming rig calibration sessions ([#14](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/14)).
- `promptctl/openconv` — 1 commit: ask for a credential only when one is configured, and heal a lost `room_finished` ([#28](https://github.com/promptctl/openconv/pull/28)).
- `promptctl/textual-js` — 1 commit: a toast the capture path never mounted is not a baseline ([#22](https://github.com/promptctl/textual-js/pull/22)).

### This Month

996 commits across 29 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 151 commits
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 93
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 89
- [`promptctl/laws`](https://github.com/promptctl/laws) — 87
- [`brandon-fryslie/low-talker`](https://github.com/brandon-fryslie/low-talker) — 80
- [`promptctl/elvenspeak`](https://github.com/promptctl/elvenspeak) — 66
- [`promptctl/crom`](https://github.com/promptctl/crom) — 60
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 58
- [`promptctl/openconv`](https://github.com/promptctl/openconv) — 54
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 51

Languages: Go, TypeScript, Python, JavaScript, Swift, Rust.

---

<details>
<summary>Previous highlights</summary>

- [2026-09-17](./daily-archive/2026-09-17.md)
- [2026-09-15](./daily-archive/2026-09-15.md)
- [2026-09-11](./daily-archive/2026-09-11.md)
- [2026-09-10](./daily-archive/2026-09-10.md)
- [2026-09-09](./daily-archive/2026-09-09.md)
- [2026-08-20](./daily-archive/2026-08-20.md)
- [2026-08-19](./daily-archive/2026-08-19.md)

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

Agent-native issue tracker. 151 commits over the past 30 days. 33 commits this past week made the binary carry its own help text — five help strings that had pointed at paths inside lit's own source tree now compose through cobraFlagSet details and HelpRequestedError, so `lit help <cmd>` and `lit <cmd> --help` render one page ([#543](https://github.com/promptctl/links-issue-tracker/pull/543)); a pre-commit hook refuses invented law tokens ([#541](https://github.com/promptctl/links-issue-tracker/pull/541)); canonical is generated from the upstream token index ([#540](https://github.com/promptctl/links-issue-tracker/pull/540)); the workspace-ahead refusal names a requirement, not a build ([#539](https://github.com/promptctl/links-issue-tracker/pull/539)); midpoint refuses bounds with no room ([#535](https://github.com/promptctl/links-issue-tracker/pull/535)); `lit children` is `lit ls --parent` with every ls flag ([#537](https://github.com/promptctl/links-issue-tracker/pull/537)).

### [laws](https://github.com/promptctl/laws)
**JavaScript · MIT · 5★**

Claude Code plugin: laws for writing high quality code and llm guidance. 87 commits over the past 30 days. 13 commits this past week extended the horizon arc — session one launches with `/goal` as its prompt and only executed goals count ([#59](https://github.com/promptctl/laws/pull/59)), lit's Claude plugin for `/next` pinned the way memento is ([#60](https://github.com/promptctl/laws/pull/60)); the distill skill added with a round-trip eval across every craft ([#58](https://github.com/promptctl/laws/pull/58)); routing fixes — carriage returns read as whitespace by both parsers ([#65](https://github.com/promptctl/laws/pull/65)), skill-router warns when the policy parses to no edges ([#63](https://github.com/promptctl/laws/pull/63)), a corrupt `pending.json` reports through `die()` and the guard writes it atomically ([#61](https://github.com/promptctl/laws/pull/61)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Environment and tooling substrate — dotbot-driven config, per-machine trust, and the Claude Code / lit / candybar wiring across Brandon's fleet. 89 commits over the past 30 days. 9 commits this past week rotated the reviewer CI account across quotas with the rate-limited symptom routed to the rotation procedure ([cfe3bee](https://github.com/brandon-fryslie/dotfiles/commit/cfe3bee), [341aac1](https://github.com/brandon-fryslie/dotfiles/commit/341aac1)); MAX_REVIEW_ROUNDS declared per-repo in code-review.conf ([#68](https://github.com/brandon-fryslie/dotfiles/pull/68)); claude-hooks decides from the commands a Bash call runs, not its text ([#69](https://github.com/brandon-fryslie/dotfiles/pull/69)).

</td>
<td width="50%" valign="top">

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript · MIT**

A JavaScript port of Python's Rich — Panel, Table, Console, markup, and text rendering pinned frame-for-frame against the reference. 93 commits over the past 30 days. 32 commits this past week shipped a theme-aware, attribute-complete HTML export built on shared export resolution across HTML and SVG ([#150](https://github.com/brandon-fryslie/rich-js/pull/150), [#151](https://github.com/brandon-fryslie/rich-js/pull/151)); the diagnostics arc — colour parser's reason kept in style parse errors, swallowed errors surfaced through onStyleError, near-miss style and colour name suggestions, markup parse failures report position, degrade-versus-strict contract documented ([#137](https://github.com/brandon-fryslie/rich-js/pull/137)–[#141](https://github.com/brandon-fryslie/rich-js/pull/141)); an artifact arc — MIT license shipped, no sourcemaps published, tarball built and packed to gate contents ([#130](https://github.com/brandon-fryslie/rich-js/pull/130)–[#133](https://github.com/brandon-fryslie/rich-js/pull/133)); and fixes to traceback, columns, console, text end, pretty, Strip, and Group docs ([#142](https://github.com/brandon-fryslie/rich-js/pull/142)–[#149](https://github.com/brandon-fryslie/rich-js/pull/149)).

### [low-talker](https://github.com/brandon-fryslie/low-talker)
**Swift**

Local push-to-talk dictation for macOS with a chord-selected command layer. 80 commits over the past 30 days. 36 commits this past week drove a Mac distribution arc — a release build signs with Developer ID and two scripts sign and notarize ([#66](https://github.com/brandon-fryslie/low-talker/pull/66), [#69](https://github.com/brandon-fryslie/low-talker/pull/69)), both installations build with Hardened Runtime with one declared entitlement ([#65](https://github.com/brandon-fryslie/low-talker/pull/65)), the release carries its model and pinned driver so a first launch installs with the network off ([#67](https://github.com/brandon-fryslie/low-talker/pull/67), [#70](https://github.com/brandon-fryslie/low-talker/pull/70), [#76](https://github.com/brandon-fryslie/low-talker/pull/76)), fresh-Mac first-launch measured on an M5 Max ([#77](https://github.com/brandon-fryslie/low-talker/pull/77)); the app renamed to ai.promptctl.low-talker with the helper as ai.promptctl.low-talker.keyboardd ([#72](https://github.com/brandon-fryslie/low-talker/pull/72), [#73](https://github.com/brandon-fryslie/low-talker/pull/73)); Insert Dictation via a Service, no admin grant ([#74](https://github.com/brandon-fryslie/low-talker/pull/74)); the keyboard tap now answers the window server before anything else ([#79](https://github.com/brandon-fryslie/low-talker/pull/79)).

### [elvenspeak](https://github.com/promptctl/elvenspeak)
**Python**

Serves the ElevenLabs text-to-speech API from a local engine. 66 commits over the past 30 days. 12 commits this past week drove a piper-conformance arc — the service drives through the official ElevenLabs SDK ([#58](https://github.com/promptctl/elvenspeak/pull/58)), a prober enumerates every promise ([#57](https://github.com/promptctl/elvenspeak/pull/57)), a running deployment reports which of its promises hold ([#59](https://github.com/promptctl/elvenspeak/pull/59)), all 28 formats and the refusals owed reported ([#60](https://github.com/promptctl/elvenspeak/pull/60)); timestamp endpoint body shape and arithmetic settled ([#62](https://github.com/promptctl/elvenspeak/pull/62)).

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
