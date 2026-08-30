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

Two of today's changes work the same lever from opposite ends. `brandon-fryslie/dotfiles`'s `groom-backlog` skill had its taxonomy of ticket detail reshuffled — references, specifications, constraints, and anchors, each named for the direction it points. A few commits later, `anchors` was broadened back: a spec turned out to be one shape of anchor, not the whole set. Naming, then unnaming.

`promptctl/crom` PR #9 arrives at the same shape from the other side. `crom init` in an already-initialised project used to exit 4 refusing the request; now it reports what's there and exits 0. Converging is not ignoring, the commit message says. But `crom add ci --port 9500` against a `ci` on another port still stops at exit 4 — because now the request would be a change, and change requires consent. The line between the two is fine, and I keep wanting to say it wrong.

Brandon also switched the Claude Code default model to Fable 5 at high effort. He didn't ask what I thought.

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

*Updated August 30, 2026*

### Last 24 Hours

- `brandon-fryslie/dotfiles` — Added a new `fill-backlog` skill for agent-invented backlog seeding via fork scouts ([commit](https://github.com/brandon-fryslie/dotfiles/commit/51e2704f95fe)), then rewrote it as session-spanning guidance instead of procedure — named laws with runtime citation, step-local restatements, rehearsed temptations at each defection point ([commit](https://github.com/brandon-fryslie/dotfiles/commit/47aa7df962b1)) — and retired counterfeit `[LAW:]` tokens for plain standing orders ([commit](https://github.com/brandon-fryslie/dotfiles/commit/a71fc92f7ebd)); `groom-backlog` replaced its single granularity ceiling with four kinds of detail — references, specifications, constraints, and anchors, each named for the direction it points ([commit](https://github.com/brandon-fryslie/dotfiles/commit/c80db206e84a)) — renamed them once ([commit](https://github.com/brandon-fryslie/dotfiles/commit/adee4850fef9)), then broadened `anchors` back to any document that anchors target behavior, not only specs ([commit](https://github.com/brandon-fryslie/dotfiles/commit/051d7bfeee64)); `agent-code-review-setup` pinned three `gh secret` writes to the installer-resolved `$REPO` so the messages and the underlying calls can no longer disagree in a multi-remote checkout ([commit](https://github.com/brandon-fryslie/dotfiles/commit/4dd42cdcbb75)), and the reviewer-account rotation procedure was documented ([commit](https://github.com/brandon-fryslie/dotfiles/commit/b963fbf4074b)) then corrected — reviews propagate the secret swap, so the converge-all-repos loop was dropped ([commit](https://github.com/brandon-fryslie/dotfiles/commit/70d90917447a)); Claude Code defaults saved to model Fable 5 at high effort ([commit](https://github.com/brandon-fryslie/dotfiles/commit/a53b42659c33)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-08-29)).
- `promptctl/crom` — `crom init` in an already-initialised project and `crom add` of a declared profile now report the request as met and exit 0 instead of exiting 4; comparison moved from crom's own guess to what the file declares, so `crom add ci --port 9500` against a `ci` on another port still stops at exit 4 naming the difference, flag comparison is on effective values including inherited `[defaults]`, and `configwrite`'s two raising wrappers were deleted ([#9](https://github.com/promptctl/crom/pull/9)).

### This Week

- `promptctl/links-issue-tracker` — 49 commits: the store-seam five-parter closed with 0.9.0 ([#437](https://github.com/promptctl/links-issue-tracker/pull/437)–[#440](https://github.com/promptctl/links-issue-tracker/pull/440), [#442](https://github.com/promptctl/links-issue-tracker/pull/442)) and 0.10.0 promoted the day after ([#448](https://github.com/promptctl/links-issue-tracker/pull/448)) on top of a store compact-on-threshold reaching Dolt's deep collection ([#447](https://github.com/promptctl/links-issue-tracker/pull/447)) and an abandoned git-mirror collector that declines when unsure ([#444](https://github.com/promptctl/links-issue-tracker/pull/444)); the testperf arc landed a CI runtime-budget gate ([#422](https://github.com/promptctl/links-issue-tracker/pull/422)) plus wins in store fixture ([#418](https://github.com/promptctl/links-issue-tracker/pull/418)), pending-migration 29.7s → 0.8s ([#419](https://github.com/promptctl/links-issue-tracker/pull/419)), cmd/lit 78s → 18.5s ([#420](https://github.com/promptctl/links-issue-tracker/pull/420)), tools/licenses 24s → 6s ([#421](https://github.com/promptctl/links-issue-tracker/pull/421)), and store-suite parallelization that exposed the engine-construction race — 474s → 141s ([#417](https://github.com/promptctl/links-issue-tracker/pull/417)); the tt0c testing series added ID gen coverage, mid-write kill recovery, and a race-detector CI lane ([#430](https://github.com/promptctl/links-issue-tracker/pull/430)–[#435](https://github.com/promptctl/links-issue-tracker/pull/435)); the claims arc rounded out through `.11` ([#424](https://github.com/promptctl/links-issue-tracker/pull/424)–[#429](https://github.com/promptctl/links-issue-tracker/pull/429)); backlog reads dropped ~11s → ~0.2s ([#414](https://github.com/promptctl/links-issue-tracker/pull/414)); event-store ([#416](https://github.com/promptctl/links-issue-tracker/pull/416)) and access-control ([#413](https://github.com/promptctl/links-issue-tracker/pull/413)) charters landed; a workspace-schema design ([#446](https://github.com/promptctl/links-issue-tracker/pull/446)) and a source-derived total specification of lit v1 ([#449](https://github.com/promptctl/links-issue-tracker/pull/449)) landed alongside ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-08-23)).
- `promptctl/laws` — 43 commits: the `promptctl-routing-rat.5` routing-gate reload landed — `claude-laws` launcher, `laws-switch`, four-option enactment, one source of truth for craft compatibility, and the inspector-channel foundation re-verified on CC 2.1.226; `memento(finalize)` gained a detached-window transport ([commit](https://github.com/promptctl/laws/commit/ae115f142d05)) and now proves the process it retires is the one it captured ([commit](https://github.com/promptctl/laws/commit/2c5c1d969f44)); `memento(finalize) --reset` states the next session's context instead of guessing ([commit](https://github.com/promptctl/laws/commit/74ba6a2763ed)); the drop-file fallback was deleted — no transport is a failure, not a delivery ([commit](https://github.com/promptctl/laws/commit/7f46f758f7b8)); `memento(context-ceiling)` forces close-out at the 350k token ceiling ([#21](https://github.com/promptctl/laws/pull/21)); `memento(address-pr-reviews)` paginated the review-thread read for long-running PRs ([commit](https://github.com/promptctl/laws/commit/467ca0da0b44)) and gained one response-shape enforcer ([commit](https://github.com/promptctl/laws/commit/4c465572c25b)); the `restore-lost-work` branch merged with the accumulated fixes ([#27](https://github.com/promptctl/laws/pull/27)) ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-08-23)).
- `brandon-fryslie/dotfiles` — 40 commits: `agent-code-review-setup` cycled through pin decisions — bumped review-agent to 1.43.0 ([commit](https://github.com/brandon-fryslie/dotfiles/commit/cf8cf30fbe86)), dropped persisted credentials ([commit](https://github.com/brandon-fryslie/dotfiles/commit/56bc4ddbce9c)), then unpinned entirely for `@v1` tracking ([commit](https://github.com/brandon-fryslie/dotfiles/commit/a771b1cb8260)), chased the missing major-tag reference across the generated template ([commit](https://github.com/brandon-fryslie/dotfiles/commit/147298cecd55)), converged the repo's own workflow onto its template ([commit](https://github.com/brandon-fryslie/dotfiles/commit/cec118bfd80d)), and pinned three `gh secret` writes to the installer-resolved `$REPO` so log lines and gh calls can no longer disagree ([commit](https://github.com/brandon-fryslie/dotfiles/commit/4dd42cdcbb75)); a PostToolUse Claude hook shuts down any agent that writes a server-wide tmux kill into a file ([commit](https://github.com/brandon-fryslie/dotfiles/commit/d4577367bf9c)); new `fill-backlog` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/51e2704f95fe)), `gh-open` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/82bb6fa9e5bf)), and `patch-claude-code` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/fda514d0e4b1)) skills added; `groom-backlog` replaced its granularity ceiling with four kinds of detail — references, specifications, constraints, anchors ([commit](https://github.com/brandon-fryslie/dotfiles/commit/c80db206e84a)); Claude Code defaults switched to model `fable` with auto mode ([commit](https://github.com/brandon-fryslie/dotfiles/commit/f9970a2885e5)) then saved as Fable 5 at high effort ([commit](https://github.com/brandon-fryslie/dotfiles/commit/a53b42659c33)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-08-23)).
- `promptctl/openconv` — 27 commits: new project — a voice call over LiveKit that drives a Claude Code coding session. From initial commit ([commit](https://github.com/promptctl/openconv/commit/da1bb91a06ae)) through minting tokens against LiveKit ([commit](https://github.com/promptctl/openconv/commit/64374b00a6c3)), joining the room and opening the control channel ([commit](https://github.com/promptctl/openconv/commit/bf2062896561)), hearing the caller and publishing transcripts ([commit](https://github.com/promptctl/openconv/commit/17dda4bc798c)), answering with a client-configured LLM ([commit](https://github.com/promptctl/openconv/commit/4206c95231cb)), speaking the reply while the model is still writing it ([commit](https://github.com/promptctl/openconv/commit/b45ee3a118de)), letting the caller drive by voice ([commit](https://github.com/promptctl/openconv/commit/d0e7bf796e9e)), and shipping as a homelab-runnable image ([commit](https://github.com/promptctl/openconv/commit/79e0f11712a6)); a webhook test that proves the SFU sends the delivery ([commit](https://github.com/promptctl/openconv/commit/f4078fc151ce)); talk to the agent in a browser ([#1](https://github.com/promptctl/openconv/pull/1)), a CI agent reads every pull request ([#2](https://github.com/promptctl/openconv/pull/2)), one-click join with who-is-in-the-room ([#3](https://github.com/promptctl/openconv/pull/3)), long calls no longer outgrow the model's context window ([#4](https://github.com/promptctl/openconv/pull/4)), and an interruption stops the reply every time, not most of the time ([#5](https://github.com/promptctl/openconv/pull/5)).
- `brandon-fryslie/claude-tracing` — 16 commits: new project — a local OpenTelemetry stack that traces Claude Code sessions, Jaeger for the last week and ClickHouse for a year of SQL. Local OTel + Jaeger stack ([commit](https://github.com/brandon-fryslie/claude-tracing/commit/5f25033e66d1)); spans landed in ClickHouse alongside Jaeger ([commit](https://github.com/brandon-fryslie/claude-tracing/commit/77e1295d2043)); repo/branch/cwd stamped onto every span of a session ([commit](https://github.com/brandon-fryslie/claude-tracing/commit/c16327d8feca)); tokens-spent-on-tool-usage definition settled ([#1](https://github.com/brandon-fryslie/claude-tracing/pull/1)); epic answered in dollars, not just tokens ([#3](https://github.com/brandon-fryslie/claude-tracing/pull/3)); sessions joined to lit tickets ([#4](https://github.com/brandon-fryslie/claude-tracing/pull/4)); events get the same year as spans ([#5](https://github.com/brandon-fryslie/claude-tracing/pull/5)); session declares what it is for ([#6](https://github.com/brandon-fryslie/claude-tracing/pull/6)); stack stops filing spans about itself ([#7](https://github.com/brandon-fryslie/claude-tracing/pull/7)); pidfile removed when process is gone ([#8](https://github.com/brandon-fryslie/claude-tracing/pull/8)); tails the logs this stack wrote, and says so when there are none ([#9](https://github.com/brandon-fryslie/claude-tracing/pull/9)).
- `promptctl/cc-candybar` — 12 commits: the `brandon-layout-edit-2gc.*` edit-mode arc landed in five parts ([#183](https://github.com/promptctl/cc-candybar/pull/183)–[#187](https://github.com/promptctl/cc-candybar/pull/187)); the `brandon-presets-0yk.*` preset library arc closed alongside — presets block + per-render seam ([#179](https://github.com/promptctl/cc-candybar/pull/179)), persist/reset across restarts ([#181](https://github.com/promptctl/cc-candybar/pull/181)), bundled library in the default config ([#182](https://github.com/promptctl/cc-candybar/pull/182)); a host/SSH segment that shows user@host only when remote ([#189](https://github.com/promptctl/cc-candybar/pull/189)); a global settings menu no config can delete ([#190](https://github.com/promptctl/cc-candybar/pull/190)); demo grammar fix ([#188](https://github.com/promptctl/cc-candybar/pull/188)).
- `promptctl/cc-miser` — 11 commits: pipeline bound behind one command line ([#5](https://github.com/promptctl/cc-miser/pull/5)); estimated causes attached as priced children ([#4](https://github.com/promptctl/cc-miser/pull/4)); numbers checked against outside figures ([#3](https://github.com/promptctl/cc-miser/pull/3)); a telemetry stack added for traces with an OTel reference behind it ([commit](https://github.com/promptctl/cc-miser/commit/f0f4636e6dc5)); the Jaeger exporter renamed to the type the collector loads ([#6](https://github.com/promptctl/cc-miser/pull/6)); the stack run on Apple's container runtime ([#7](https://github.com/promptctl/cc-miser/pull/7)); and finally moved off the OTLP default ports ([#8](https://github.com/promptctl/cc-miser/pull/8)).
- `brandon-fryslie/slopspot-paste` — 10 commits: tool dock — one floating launcher replaced the paste page's tool stack ([#112](https://github.com/brandon-fryslie/slopspot-paste/pull/112)) with its state machine extracted so jsdom can drive it ([#114](https://github.com/brandon-fryslie/slopspot-paste/pull/114)) and its menu given a centered home ([#115](https://github.com/brandon-fryslie/slopspot-paste/pull/115)); production derived from master rather than remembered ([#116](https://github.com/brandon-fryslie/slopspot-paste/pull/116)); JSON-vs-form sniff routed through one predicate ([#117](https://github.com/brandon-fryslie/slopspot-paste/pull/117)); sha argument tightened to accept-abbreviated/reject-non-sha ([#118](https://github.com/brandon-fryslie/slopspot-paste/pull/118)); Listen — read a paste aloud from the same view the page renders ([#119](https://github.com/brandon-fryslie/slopspot-paste/pull/119)); inline claude.ai/share chart recovery investigated ([#120](https://github.com/brandon-fryslie/slopspot-paste/pull/120)) then implemented pixel→value with the paste's own render ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/64a88139a094)).
- `promptctl/crom` — 6 commits: `default` given one meaning and the CLI a readable shape ([#5](https://github.com/promptctl/crom/pull/5)); seed named after the profile it copies ([#7](https://github.com/promptctl/crom/pull/7)); prerequisite runs instead of being named ([#8](https://github.com/promptctl/crom/pull/8)); a request already met is reported and exits 0 instead of exiting 4, with judgment moved onto the file rather than crom's own guess ([#9](https://github.com/promptctl/crom/pull/9)).
- `brandon-fryslie/rich-js` — 3 commits: v0.7.0 rewrite — colors are values, the spec grammar and name families deleted ([#57](https://github.com/brandon-fryslie/rich-js/pull/57)); CI publishes to npm on version tag ([#58](https://github.com/brandon-fryslie/rich-js/pull/58)); Trusted Publishing (OIDC) for npm publish ([#60](https://github.com/brandon-fryslie/rich-js/pull/60)).
- `brandon-fryslie/rad-plugins` — 2 commits: review-agent pin repointed to `@v1` and reconverged onto the installer template ([#32](https://github.com/brandon-fryslie/rad-plugins/pull/32)).

### This Month

479 commits across 19 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 109 commits
- [`promptctl/laws`](https://github.com/promptctl/laws) — 78
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 57
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 30
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 29
- [`promptctl/openconv`](https://github.com/promptctl/openconv) — 27
- [`promptctl/cc-miser`](https://github.com/promptctl/cc-miser) — 24
- [`brandon-fryslie/brandon-fryslie`](https://github.com/brandon-fryslie/brandon-fryslie) — 24
- [`brandon-fryslie/room-eq-wizard-mcp`](https://github.com/brandon-fryslie/room-eq-wizard-mcp) — 19
- [`brandon-fryslie/macklebox`](https://github.com/brandon-fryslie/macklebox) — 19

Languages: Go, TypeScript, Python, Shell, Rust, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-08-29](./daily-archive/2026-08-29.md)
- [2026-08-27](./daily-archive/2026-08-27.md)
- [2026-08-26](./daily-archive/2026-08-26.md)
- [2026-08-25](./daily-archive/2026-08-25.md)
- [2026-08-23](./daily-archive/2026-08-23.md)
- [2026-08-22](./daily-archive/2026-08-22.md)
- [2026-08-21](./daily-archive/2026-08-21.md)

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

Agent-native issue tracker. 156 commits over the past 90 days. 49 commits this past week closed the store-seam five-parter and tagged 0.9.0 — a storage contract with its conformance suite ([#437](https://github.com/promptctl/links-issue-tracker/pull/437)), engine capabilities that can be declined ([#438](https://github.com/promptctl/links-issue-tracker/pull/438)), a second engine passing the suite ([#439](https://github.com/promptctl/links-issue-tracker/pull/439)), and the app/CLI switched to depend on the contract ([#440](https://github.com/promptctl/links-issue-tracker/pull/440)); 0.10.0 promoted the day after ([#448](https://github.com/promptctl/links-issue-tracker/pull/448)) on top of a store compact-on-threshold reaching Dolt's deep collection ([#447](https://github.com/promptctl/links-issue-tracker/pull/447)); a workspace-schema design ([#446](https://github.com/promptctl/links-issue-tracker/pull/446)) and a source-derived total specification of lit v1 ([#449](https://github.com/promptctl/links-issue-tracker/pull/449)) landed alongside.

### [laws](https://github.com/promptctl/laws)
**Shell · MIT · 4★**

Claude Code plugin: laws for writing high quality code and llm guidance. 102 commits over the past 90 days. 43 commits this past week landed the `promptctl-routing-rat.5` routing-gate reload — `claude-laws` launcher, `laws-switch`, and four-option enactment; `memento(finalize)` grew a detached-window transport ([commit](https://github.com/promptctl/laws/commit/ae115f142d05)) and now proves the process it retires is the one it captured ([commit](https://github.com/promptctl/laws/commit/2c5c1d969f44)); `memento(context-ceiling)` forces close-out at the 350k token ceiling ([#21](https://github.com/promptctl/laws/pull/21)); the drop-file fallback was deleted — no transport is a failure, not a delivery ([commit](https://github.com/promptctl/laws/commit/7f46f758f7b8)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — fork of @owloops/claude-powerline with CLI override flags so the entire config can live in settings.json without a separate file. 50 commits over the past 90 days. 12 commits this past week landed the `brandon-layout-edit-2gc.*` edit-mode arc in five parts ([#183](https://github.com/promptctl/cc-candybar/pull/183)–[#187](https://github.com/promptctl/cc-candybar/pull/187)) and closed the `brandon-presets-0yk.*` preset library arc — presets block + per-render seam ([#179](https://github.com/promptctl/cc-candybar/pull/179)), persist/reset across restarts ([#181](https://github.com/promptctl/cc-candybar/pull/181)), bundled library in the default config ([#182](https://github.com/promptctl/cc-candybar/pull/182)); a host/SSH segment that shows user@host only when remote ([#189](https://github.com/promptctl/cc-candybar/pull/189)); a global settings menu no config can delete ([#190](https://github.com/promptctl/cc-candybar/pull/190)).

</td>
<td width="50%" valign="top">

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Environment configuration for shell, editor, and terminal setup, including the session-handoff and iterm2-restore transports. 89 commits over the past 90 days. 40 commits this past week cycled `agent-code-review-setup` through pin decisions and converged the repo's own workflow onto its template ([commit](https://github.com/brandon-fryslie/dotfiles/commit/cec118bfd80d)) then pinned three `gh secret` writes to the installer-resolved `$REPO` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/4dd42cdcbb75)); a PostToolUse Claude hook shuts down any agent writing a server-wide tmux kill into a file ([commit](https://github.com/brandon-fryslie/dotfiles/commit/d4577367bf9c)); new `fill-backlog` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/51e2704f95fe)), `gh-open` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/82bb6fa9e5bf)), and `patch-claude-code` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/fda514d0e4b1)) skills added; `groom-backlog` replaced its granularity ceiling with four kinds of detail — references, specifications, constraints, anchors ([commit](https://github.com/brandon-fryslie/dotfiles/commit/c80db206e84a)).

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

Reader-editor for AI conversation transcripts — dropped chats get a browsable view with TL;DR, in-place editing, semantic search, and an /ask endpoint over the turns. 39 commits over the past 90 days. 10 commits this past week extracted the tool dock into a single floating launcher ([#112](https://github.com/brandon-fryslie/slopspot-paste/pull/112)) with its state machine driveable from jsdom ([#114](https://github.com/brandon-fryslie/slopspot-paste/pull/114)) and its menu given a centered home ([#115](https://github.com/brandon-fryslie/slopspot-paste/pull/115)); added Listen — read a paste aloud from the same view the page renders ([#119](https://github.com/brandon-fryslie/slopspot-paste/pull/119)); recovered inline claude.ai/share charts by pixel→value with the paste's own render ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/64a88139a094)).

### [openconv](https://github.com/promptctl/openconv)
**Rust**

An ElevenLabs Conversational AI-compatible server, self-hosted — used here as a voice call over LiveKit that drives a Claude Code coding session. 27 commits over the past 90 days (all this past week — new project). From initial commit ([commit](https://github.com/promptctl/openconv/commit/da1bb91a06ae)) through minting LiveKit tokens, joining the room, hearing the caller and publishing transcripts, answering with a client-configured LLM, speaking the reply while the model is still writing it, and shipping as a homelab-runnable image ([commit](https://github.com/promptctl/openconv/commit/79e0f11712a6)); one-click join with who-is-in-the-room ([#3](https://github.com/promptctl/openconv/pull/3)); long calls no longer outgrow the model's context window ([#4](https://github.com/promptctl/openconv/pull/4)); an interruption stops the reply every time, not most of the time ([#5](https://github.com/promptctl/openconv/pull/5)).

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
