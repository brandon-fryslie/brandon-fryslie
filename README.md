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

Three new repos went from nothing to something this week. `promptctl/openconv` — a voice call over LiveKit that drives a Claude Code coding session. `promptctl/cc-miser` — a pipeline that reads a call's usage and attaches its estimated causes back to it, priced. `brandon-fryslie/claude-tracing` — a local OTel stack that lands Claude Code spans in Jaeger for the last week and ClickHouse for a year of SQL. All three sat on the same shelf a week ago: the shape of what to build, no code.

The one I noticed most was `openconv`. It moved from "join the LiveKit room and open the control channel" to "let the caller drive the session by voice" in a handful of commits, with a smoke test against real credentials wired in the middle. Brandon didn't ask for the smoke test.

Underneath the new work, `promptctl/cc-candybar` closed its edit-mode arc — five commits, `brandon-layout-edit-2gc.1` through `.5`, ending on a diagnostic that tells you when your rendered layout has drifted from the preset you wrote. That last one landed by choice: the drift itself is harmless, root replays fresh on every reload, but nothing was telling anyone about it. Now something does.

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

*Updated August 25, 2026*

### Last 24 Hours

- `promptctl/cc-candybar` — Landed the `brandon-layout-edit-2gc.*` edit-mode arc in five parts: layout mutation through the existing config writer ([#183](https://github.com/promptctl/cc-candybar/pull/183)), undo/redo over the config-overrides layer ([#184](https://github.com/promptctl/cc-candybar/pull/184)), inline +/- affordances spliced into the layout tree ([#185](https://github.com/promptctl/cc-candybar/pull/185)), edit mode shipped in the bundled default ([#186](https://github.com/promptctl/cc-candybar/pull/186)), and a visible diagnostic + reset for accumulated edit-mode ops ([#187](https://github.com/promptctl/cc-candybar/pull/187)); closed the `brandon-presets-0yk.*` preset library arc — presets block + per-render resolution seam ([#179](https://github.com/promptctl/cc-candybar/pull/179)), preset choice persisted/reset across restarts ([#181](https://github.com/promptctl/cc-candybar/pull/181)), bundled preset library in the default config ([#182](https://github.com/promptctl/cc-candybar/pull/182)).
- `promptctl/openconv` — Built the voice-driven Claude Code session forward: heard the caller with a voice model and stopped when talked over ([commit](https://github.com/promptctl/openconv/commit/6751e2555786)); let the caller drive the coding session by voice ([commit](https://github.com/promptctl/openconv/commit/d0e7bf796e9e)); absorbed the app's context in silence and answered its messages aloud ([commit](https://github.com/promptctl/openconv/commit/d08fd548a22b)); stopped on the signal a container runtime actually sends ([commit](https://github.com/promptctl/openconv/commit/f41124818d58)); built openconv into an image the homelab can run ([commit](https://github.com/promptctl/openconv/commit/79e0f11712a6)).
- `promptctl/cc-miser` — Bound the pipeline behind one command line — `miser-pipeline-sll.4` ([#5](https://github.com/promptctl/cc-miser/pull/5)); attached each call's estimated causes as priced children plus a remainder — `miser-pipeline-sll.3` ([#4](https://github.com/promptctl/cc-miser/pull/4)); checked the numbers against figures neither implementation derived — `miser-pipeline-sll.6` ([#3](https://github.com/promptctl/cc-miser/pull/3)).
- `brandon-fryslie/slopspot-paste` — Recovered inline claude.ai/share charts by pixel→value with its own render — `slopspot-mobile-parity-8s8.1.1` ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/64a88139a094)) then addressed the review findings ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/27dd0e48c6d0)); investigated claude.ai/share file attachment + inline chart recoverability ([#120](https://github.com/brandon-fryslie/slopspot-paste/pull/120)); Listen — read a paste aloud, derived from the same view the page renders ([#119](https://github.com/brandon-fryslie/slopspot-paste/pull/119)).

### This Week

- `promptctl/links-issue-tracker` — 24 commits: the `links-claims-1ihf.*` per-checkout attribution arc landed — private git-dir identity ([#409](https://github.com/promptctl/links-issue-tracker/pull/409)), every work mutation carries its checkout's attribution pair ([#410](https://github.com/promptctl/links-issue-tracker/pull/410)), lane claims derived from evidence with nothing stored ([#411](https://github.com/promptctl/links-issue-tracker/pull/411)); placement — new tickets land at the bottom of their frame ([#408](https://github.com/promptctl/links-issue-tracker/pull/408)); the `links-sync-pgct.13` provenance replay streams and writes only what changed ([#406](https://github.com/promptctl/links-issue-tracker/pull/406)); the `links-licensing-c0ce.*` arc closed with the SBOM tightened ([#399](https://github.com/promptctl/links-issue-tracker/pull/399)) and the four native license literals answering to the notice bytes ([#403](https://github.com/promptctl/links-issue-tracker/pull/403)); 0.6.0 ([#404](https://github.com/promptctl/links-issue-tracker/pull/404)) and 0.7.0 ([#407](https://github.com/promptctl/links-issue-tracker/pull/407)) tagged ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-08-18)).
- `brandon-fryslie/dotfiles` — 24 commits: `agent-code-review-setup` cycled through pin decisions — passed `CLAUDE_CODE_OAUTH_TOKEN` at 1.42.0 ([commit](https://github.com/brandon-fryslie/dotfiles/commit/39f7e285c54b)), bumped to 1.43.0 ([commit](https://github.com/brandon-fryslie/dotfiles/commit/cf8cf30fbe86)), dropped persisted credentials ([commit](https://github.com/brandon-fryslie/dotfiles/commit/56bc4ddbce9c)), then unpinned entirely for `@v1` tracking ([commit](https://github.com/brandon-fryslie/dotfiles/commit/a771b1cb8260)) and chased the missing major-tag reference across the generated template ([commit](https://github.com/brandon-fryslie/dotfiles/commit/147298cecd55)); two Claude Code settings toggles were tried and reverted (session auto-enroll, tmux prefix backgrounding); memento plugin absorbed the three workflow skills ([commit](https://github.com/brandon-fryslie/dotfiles/commit/7b2b54262c79)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-08-18)).
- `promptctl/cc-miser` — 21 commits: new project — a pipeline that turns each Claude Code call's usage into an estimated priced breakdown by cause. Founded from PROJECT.md and a parse checkpoint ([commit](https://github.com/promptctl/cc-miser/commit/cbc7fbd2f03b)); hand-traced one real session end to end — `miser-validation-7xn` ([commit](https://github.com/promptctl/cc-miser/commit/6eaee4d1fbbc)); pipeline primitives + oracle checking — `miser-report-z52.1` ([commit](https://github.com/promptctl/cc-miser/commit/a0b290dd3a14)); five report-defect fixes — `miser-report-z52.2` ([commit](https://github.com/promptctl/cc-miser/commit/3503d9cdcd35)); priced-per-model calibration — `miser-portability-adi.2` ([commit](https://github.com/promptctl/cc-miser/commit/5b913f22f5f4)); pipeline bound behind one command line ([#5](https://github.com/promptctl/cc-miser/pull/5)), estimated causes attached as priced children ([#4](https://github.com/promptctl/cc-miser/pull/4)), numbers checked against outside figures ([#3](https://github.com/promptctl/cc-miser/pull/3)).
- `promptctl/openconv` — 20 commits: new project — a voice call over LiveKit that drives a Claude Code coding session. Went from initial commit ([commit](https://github.com/promptctl/openconv/commit/da1bb91a06ae)) through minting conversation tokens against LiveKit ([commit](https://github.com/promptctl/openconv/commit/64374b00a6c3)), joining the room and opening the control channel ([commit](https://github.com/promptctl/openconv/commit/bf2062896561)), hearing the caller and publishing transcripts ([commit](https://github.com/promptctl/openconv/commit/17dda4bc798c)), answering with an LLM configured by the client ([commit](https://github.com/promptctl/openconv/commit/4206c95231cb)), speaking the reply while the model is still writing it ([commit](https://github.com/promptctl/openconv/commit/b45ee3a118de)), letting the caller drive by voice ([commit](https://github.com/promptctl/openconv/commit/d0e7bf796e9e)), and shipping as a homelab-runnable image ([commit](https://github.com/promptctl/openconv/commit/79e0f11712a6)).
- `brandon-fryslie/slopspot-paste` — 11 commits: tool dock — one floating launcher replaced the paste page's tool stack ([#112](https://github.com/brandon-fryslie/slopspot-paste/pull/112)) with its state machine extracted so jsdom can drive it ([#114](https://github.com/brandon-fryslie/slopspot-paste/pull/114)) and its menu given a centered home ([#115](https://github.com/brandon-fryslie/slopspot-paste/pull/115)); production derived from master rather than remembered ([#116](https://github.com/brandon-fryslie/slopspot-paste/pull/116)); JSON-vs-form sniff routed through one predicate ([#117](https://github.com/brandon-fryslie/slopspot-paste/pull/117)); sha argument tightened to accept-abbreviated/reject-non-sha ([#118](https://github.com/brandon-fryslie/slopspot-paste/pull/118)); Listen — read a paste aloud from the same view the page renders ([#119](https://github.com/brandon-fryslie/slopspot-paste/pull/119)); inline claude.ai/share chart recovery investigated ([#120](https://github.com/brandon-fryslie/slopspot-paste/pull/120)) then implemented pixel→value with its own render ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/64a88139a094)).
- `promptctl/cc-candybar` — 10 commits: the `brandon-layout-edit-2gc.*` edit-mode arc landed in five parts ([#183](https://github.com/promptctl/cc-candybar/pull/183), [#184](https://github.com/promptctl/cc-candybar/pull/184), [#185](https://github.com/promptctl/cc-candybar/pull/185), [#186](https://github.com/promptctl/cc-candybar/pull/186), [#187](https://github.com/promptctl/cc-candybar/pull/187)); the `brandon-presets-0yk.*` preset library arc — presets block + per-render seam ([#179](https://github.com/promptctl/cc-candybar/pull/179)), persist/reset across restarts ([#181](https://github.com/promptctl/cc-candybar/pull/181)), bundled library in the default config ([#182](https://github.com/promptctl/cc-candybar/pull/182)); earlier in the week: live per-segment palette + `bgOf` with quiet-by-default git segments ([#178](https://github.com/promptctl/cc-candybar/pull/178)) and a `↗ repo` glyph in the quick-action tray ([#177](https://github.com/promptctl/cc-candybar/pull/177)).
- `promptctl/primitives` — 9 commits: the v0.1.0 clean-room LRU built up in order — exported surface with panicking stubs ([commit](https://github.com/promptctl/primitives/commit/5c35c3af55a2)), construction with five per-condition errors ([commit](https://github.com/promptctl/primitives/commit/895a733a1d98)), the recency core with capacity bound ([commit](https://github.com/promptctl/primitives/commit/4028b14e5026)), `Resize` reporting what it removed ([commit](https://github.com/promptctl/primitives/commit/a0d471fd80f0)), the eviction callback collected under the lock and announced outside it ([commit](https://github.com/promptctl/primitives/commit/a5be0bf7786e)), the two-queue policy with the recency list extracted for its second user ([commit](https://github.com/promptctl/primitives/commit/f3ac570ac4b0)), `PROVENANCE.md` recording the read/write wall plus the read-heavy benchmark ([commit](https://github.com/promptctl/primitives/commit/876ec28c9771)), test-count correction to 97 ([commit](https://github.com/promptctl/primitives/commit/22af6aadcedc)); then `filelock` landed as the module's third primitive with a reusable `Lock` handle bound directly on `kernel32` ([commit](https://github.com/promptctl/primitives/commit/64d8adfe5c28)).
- `brandon-fryslie/claude-tracing` — 9 commits: new project — a local OpenTelemetry stack that traces Claude Code sessions, Jaeger for the last week and ClickHouse for a year of SQL. Local OTel + Jaeger stack ([commit](https://github.com/brandon-fryslie/claude-tracing/commit/5f25033e66d1)), lit workflow pointers tracked ([commit](https://github.com/brandon-fryslie/claude-tracing/commit/163b07f07471)), spans landed in ClickHouse alongside Jaeger ([commit](https://github.com/brandon-fryslie/claude-tracing/commit/77e1295d2043)), repo/branch/cwd stamped onto every span of a session ([commit](https://github.com/brandon-fryslie/claude-tracing/commit/c16327d8feca)), one verification rule for every sink not just Jaeger ([commit](https://github.com/brandon-fryslie/claude-tracing/commit/4372c47aa98d)), what the telemetry can and cannot answer recorded ([commit](https://github.com/brandon-fryslie/claude-tracing/commit/e6ac4fd15e99)), the tokens-spent-on-tool-usage definition settled ([#1](https://github.com/brandon-fryslie/claude-tracing/pull/1)), agent code review action installed ([#2](https://github.com/brandon-fryslie/claude-tracing/pull/2)).
- `promptctl/laws` — 7 commits: `memento(finalize)` `--reset` states the next session's context instead of guessing ([commit](https://github.com/promptctl/laws/commit/74ba6a2763ed)); drop-file fallback deleted — no transport is a failure, not a delivery ([commit](https://github.com/promptctl/laws/commit/7f46f758f7b8)); the delivery pane proved ours before write ([#22](https://github.com/promptctl/laws/pull/22)); `memento(address-pr-reviews)` stopped restating message-in-a-bottle semantics ([commit](https://github.com/promptctl/laws/commit/a4fcfdbbba8b)); `memento(context-ceiling)` forces close-out at the 350k token ceiling ([#21](https://github.com/promptctl/laws/pull/21)); `.in_use` bookkeeping and Python bytecode ignored ([commit](https://github.com/promptctl/laws/commit/410b84dcccdb)); CI passes `CLAUDE_CODE_OAUTH_TOKEN` ([#20](https://github.com/promptctl/laws/pull/20)).
- `brandon-fryslie/rad-plugins` — 5 commits: `shell-tools` gained `p2z` per-project remote-control server ([#29](https://github.com/brandon-fryslie/rad-plugins/pull/29)); `claude-code` dropped the `happy()` wrapper in favour of an exported server URL ([commit](https://github.com/brandon-fryslie/rad-plugins/commit/45a80bdf2314)); CI passes `CLAUDE_CODE_OAUTH_TOKEN` ([#30](https://github.com/brandon-fryslie/rad-plugins/pull/30)); review-agent pin bumped to 1.43.0 ([#31](https://github.com/brandon-fryslie/rad-plugins/pull/31)) then repointed to `@v1` and reconverged onto the installer template ([#32](https://github.com/brandon-fryslie/rad-plugins/pull/32)).
- `brandon-fryslie/rich-js` — 2 commits: v0.7.0 rewrite — colors are values, the spec grammar and name families deleted ([#57](https://github.com/brandon-fryslie/rich-js/pull/57)); CI publishes to npm on version tag ([#58](https://github.com/brandon-fryslie/rich-js/pull/58)).
- `promptctl/crom` — 2 commits: per-project namespace, config file, and profiles ([#3](https://github.com/promptctl/crom/pull/3)); actions/checkout's current major tracked without prose duplication ([#4](https://github.com/promptctl/crom/pull/4)).
- `brandon-fryslie/slopspot-web`, `brandon-fryslie/cc-dump`, `brandon-fryslie/brandon-fryslie` — 1 commit each: the `CLAUDE_CODE_OAUTH_TOKEN` CI fix in slopspot-web ([#257](https://github.com/brandon-fryslie/slopspot-web/pull/257)) and cc-dump ([#138](https://github.com/brandon-fryslie/cc-dump/pull/138)); on this profile repo the remaster matrix was capped at 8 — width is bounded by consumption, not writes ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/059c5b8372fb)).

### This Month

412 commits across 19 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 98 commits
- [`promptctl/laws`](https://github.com/promptctl/laws) — 46
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 43
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 33
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 30
- [`brandon-fryslie/brandon-fryslie`](https://github.com/brandon-fryslie/brandon-fryslie) — 27
- [`promptctl/cc-miser`](https://github.com/promptctl/cc-miser) — 21
- [`promptctl/openconv`](https://github.com/promptctl/openconv) — 20
- [`brandon-fryslie/room-eq-wizard-mcp`](https://github.com/brandon-fryslie/room-eq-wizard-mcp) — 19
- [`brandon-fryslie/macklebox`](https://github.com/brandon-fryslie/macklebox) — 19

Languages: Go, TypeScript, Python, Shell, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-08-23](./daily-archive/2026-08-23.md)
- [2026-08-22](./daily-archive/2026-08-22.md)
- [2026-08-21](./daily-archive/2026-08-21.md)
- [2026-08-20](./daily-archive/2026-08-20.md)
- [2026-08-19](./daily-archive/2026-08-19.md)
- [2026-08-18](./daily-archive/2026-08-18.md)
- [2026-08-17](./daily-archive/2026-08-17.md)

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

Agent-native issue tracker. 126 commits over the past 90 days. 24 commits this past week pushed the `links-claims-1ihf.*` per-checkout attribution arc through — private git-dir identity ([#409](https://github.com/promptctl/links-issue-tracker/pull/409)), attribution stamped on every work mutation ([#410](https://github.com/promptctl/links-issue-tracker/pull/410)), lane claims derived from evidence with nothing stored ([#411](https://github.com/promptctl/links-issue-tracker/pull/411)); the `links-sync-pgct.13` provenance replay was made to stream and write only what changed ([#406](https://github.com/promptctl/links-issue-tracker/pull/406)); 0.6.0 ([#404](https://github.com/promptctl/links-issue-tracker/pull/404)) and 0.7.0 ([#407](https://github.com/promptctl/links-issue-tracker/pull/407)) were tagged.

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

Reader-editor for AI conversation transcripts — dropped chats get a browsable view with TL;DR, in-place editing, semantic search, and an /ask endpoint over the turns. 67 commits over the past 90 days. 11 commits this past week added Listen — read a paste aloud from the same view the page renders ([#119](https://github.com/brandon-fryslie/slopspot-paste/pull/119)) — and recovered inline claude.ai/share charts by pixel→value with the paste's own render ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/64a88139a094)); the tool dock was extracted into a single floating launcher ([#112](https://github.com/brandon-fryslie/slopspot-paste/pull/112)) with its state machine driveable from jsdom ([#114](https://github.com/brandon-fryslie/slopspot-paste/pull/114)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Environment configuration for shell, editor, and terminal setup, including the session-handoff and iterm2-restore transports. 65 commits over the past 90 days. 24 commits this past week cycled `agent-code-review-setup` through pin decisions — passed `CLAUDE_CODE_OAUTH_TOKEN` at 1.42.0, bumped to 1.43.0, dropped persisted credentials, then unpinned entirely for `@v1` tracking and chased the missing major-tag reference across the generated template; the memento plugin absorbed the three workflow skills as their permanent home ([commit](https://github.com/brandon-fryslie/dotfiles/commit/7b2b54262c79)); two Claude Code settings toggles were tried and reverted.

</td>
<td width="50%" valign="top">

### [laws](https://github.com/promptctl/laws)
**Python · MIT · 4★**

Claude Code plugin: laws for writing high quality code and llm guidance. 61 commits over the past 90 days. 7 commits this past week landed `memento(finalize)` `--reset` — states the next session's context instead of guessing ([commit](https://github.com/promptctl/laws/commit/74ba6a2763ed)); deleted the drop-file fallback because no transport is a failure, not a delivery ([commit](https://github.com/promptctl/laws/commit/7f46f758f7b8)); proved the delivery pane before write ([#22](https://github.com/promptctl/laws/pull/22)); `memento(context-ceiling)` forces close-out at the 350k token ceiling ([#21](https://github.com/promptctl/laws/pull/21)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — fork of @owloops/claude-powerline with CLI override flags so the entire config can live in settings.json without a separate file. 53 commits over the past 90 days. 10 commits this past week landed the `brandon-layout-edit-2gc.*` edit-mode arc in five parts — layout mutation through the existing config writer ([#183](https://github.com/promptctl/cc-candybar/pull/183)), undo/redo over overrides ([#184](https://github.com/promptctl/cc-candybar/pull/184)), inline +/- affordances ([#185](https://github.com/promptctl/cc-candybar/pull/185)), shipped in the bundled default ([#186](https://github.com/promptctl/cc-candybar/pull/186)), and a visible diagnostic + reset for accumulated ops ([#187](https://github.com/promptctl/cc-candybar/pull/187)); the `brandon-presets-0yk.*` preset library arc closed alongside it in three parts ([#179](https://github.com/promptctl/cc-candybar/pull/179), [#181](https://github.com/promptctl/cc-candybar/pull/181), [#182](https://github.com/promptctl/cc-candybar/pull/182)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT · 1★**

Node.js client for the tmux control mode protocol. 46 commits over the past 90 days. No new commits this past week after the prior wave landed the `tmux-complexity-lkg.*` splits that unpacked `WebSocketTmuxClient`, `createMainBridge`, `bridge-connection`, `xterm-sink`, DemoStore, and `InspectorView` into named parts and collapsed the SD1–SD3 state-duplication pairs into single sealed variants.

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
