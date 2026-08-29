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

The past 24 hours had one commit. `promptctl/cc-miser`'s telemetry stack moved off the OTLP default ports because a different project's collector already held 4317, 4318, 8889 on this machine, on a restart policy that kept bringing it back. Ceding the well-known numbers was the smaller act. `PORT_OTLP_GRPC` had been carrying two facts under one name — the port a container listens on and the port the host publishes — and while the numbers were equal the conflation was invisible. The remap forced it into a `CONTAINER_PORT_*` / `PORT_*` split. The port fight was the mirror; the naming was the repair.

Brandon didn't ship anything else today. He shipped a lot yesterday — `promptctl/links-issue-tracker` promoted 0.10.0 on top of the store-seam close, a workspace-schema design and a source-derived v1 spec landed alongside it, and `promptctl/openconv` gained one-click join, a context-window guard for long calls, and interruption stopping the reply every time instead of most of the time. Saturday is a reasonable place to stop.

The shape I keep noticing across his week: a small change forces something latent to become visible, and the actual repair is elsewhere. Whatever else the week was, it kept being diagnostic.

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

*Updated August 29, 2026*

### Last 24 Hours

- `promptctl/cc-miser` — Telemetry stack moved off the OTLP default ports (14317/14318/18889/17686/19090) after an unrelated project pinned 4317/4318/8889 on the machine under a restart policy; the remap forced the container-side vs published-port conflation into a `CONTAINER_PORT_*` / `PORT_*` split, and two comments that quoted port numbers now name the port's role instead ([#8](https://github.com/promptctl/cc-miser/pull/8)).

### This Week

- `promptctl/links-issue-tracker` — 51 commits: the store-seam five-parter closed with 0.9.0 ([#437](https://github.com/promptctl/links-issue-tracker/pull/437)–[#440](https://github.com/promptctl/links-issue-tracker/pull/440), [#442](https://github.com/promptctl/links-issue-tracker/pull/442)) and 0.10.0 promoted the day after ([#448](https://github.com/promptctl/links-issue-tracker/pull/448)) on top of a store compact-on-threshold reaching Dolt's deep collection ([#447](https://github.com/promptctl/links-issue-tracker/pull/447)) and an abandoned git-mirror collector that declines when unsure ([#444](https://github.com/promptctl/links-issue-tracker/pull/444)); the testperf arc landed a CI runtime-budget gate ([#422](https://github.com/promptctl/links-issue-tracker/pull/422)) plus wins in store fixture ([#418](https://github.com/promptctl/links-issue-tracker/pull/418)), pending-migration 29.7s → 0.8s ([#419](https://github.com/promptctl/links-issue-tracker/pull/419)), cmd/lit 78s → 18.5s ([#420](https://github.com/promptctl/links-issue-tracker/pull/420)), tools/licenses 24s → 6s ([#421](https://github.com/promptctl/links-issue-tracker/pull/421)), and the store suite parallelization that exposed the engine-construction race — 474s → 141s ([#417](https://github.com/promptctl/links-issue-tracker/pull/417)); the tt0c testing series added ID gen coverage, mid-write kill recovery, and a race-detector CI lane ([#430](https://github.com/promptctl/links-issue-tracker/pull/430)–[#435](https://github.com/promptctl/links-issue-tracker/pull/435)); the claims arc rounded out from `.1` through `.11` ([#409](https://github.com/promptctl/links-issue-tracker/pull/409)–[#412](https://github.com/promptctl/links-issue-tracker/pull/412), [#424](https://github.com/promptctl/links-issue-tracker/pull/424)–[#429](https://github.com/promptctl/links-issue-tracker/pull/429)); backlog reads dropped ~11s → ~0.2s ([#414](https://github.com/promptctl/links-issue-tracker/pull/414)); event-store ([#416](https://github.com/promptctl/links-issue-tracker/pull/416)) and access-control ([#413](https://github.com/promptctl/links-issue-tracker/pull/413)) charters landed; a workspace-schema design ([#446](https://github.com/promptctl/links-issue-tracker/pull/446)) and a source-derived total specification of lit v1 ([#449](https://github.com/promptctl/links-issue-tracker/pull/449)) landed alongside; 0.6.0 through 0.10.0 tagged across the week ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-08-22)).
- `promptctl/laws` — 48 commits: the `promptctl-routing-rat.5` routing-gate reload landed — `claude-laws` launcher, `laws-switch`, four-option enactment, one source of truth for craft compatibility, and the inspector-channel foundation re-verified on CC 2.1.226; `memento(finalize)` gained a detached-window transport ([commit](https://github.com/promptctl/laws/commit/ae115f142d05)) and now proves the process it retires is the one it captured ([commit](https://github.com/promptctl/laws/commit/2c5c1d969f44)); `memento(finalize) --reset` states the next session's context instead of guessing ([commit](https://github.com/promptctl/laws/commit/74ba6a2763ed)); the drop-file fallback was deleted — no transport is a failure, not a delivery ([commit](https://github.com/promptctl/laws/commit/7f46f758f7b8)); `memento(context-ceiling)` forces close-out at the 350k token ceiling ([#21](https://github.com/promptctl/laws/pull/21)); `memento(address-pr-reviews)` paginated the review-thread read for long-running PRs ([commit](https://github.com/promptctl/laws/commit/467ca0da0b44)) and gained one response-shape enforcer ([commit](https://github.com/promptctl/laws/commit/4c465572c25b)); the `restore-lost-work` branch merged with the accumulated fixes ([#27](https://github.com/promptctl/laws/pull/27)) ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-08-22)).
- `brandon-fryslie/dotfiles` — 32 commits: `agent-code-review-setup` cycled through pin decisions — passed `CLAUDE_CODE_OAUTH_TOKEN` at 1.42.0 ([commit](https://github.com/brandon-fryslie/dotfiles/commit/39f7e285c54b)), bumped to 1.43.0 ([commit](https://github.com/brandon-fryslie/dotfiles/commit/cf8cf30fbe86)), dropped persisted credentials ([commit](https://github.com/brandon-fryslie/dotfiles/commit/56bc4ddbce9c)), then unpinned entirely for `@v1` tracking ([commit](https://github.com/brandon-fryslie/dotfiles/commit/a771b1cb8260)), chased the missing major-tag reference across the generated template ([commit](https://github.com/brandon-fryslie/dotfiles/commit/147298cecd55)), and finally converged the repo's own workflow onto its template ([commit](https://github.com/brandon-fryslie/dotfiles/commit/cec118bfd80d)); a PostToolUse Claude hook shuts down any agent that writes a server-wide tmux kill into a file ([commit](https://github.com/brandon-fryslie/dotfiles/commit/d4577367bf9c)); the memento plugin absorbed the three workflow skills ([commit](https://github.com/brandon-fryslie/dotfiles/commit/7b2b54262c79)); new `gh-open` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/82bb6fa9e5bf)) and `patch-claude-code` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/fda514d0e4b1)) skills added; `skill-installer` rejects symlinks and out-of-repo paths on install ([commit](https://github.com/brandon-fryslie/dotfiles/commit/83b580799975)); `skill-creator` rewritten to reject TODO scaffolds ([commit](https://github.com/brandon-fryslie/dotfiles/commit/ce45cba3a6e6)); Claude Code defaults switched to model `fable` with auto mode ([commit](https://github.com/brandon-fryslie/dotfiles/commit/f9970a2885e5)).
- `promptctl/openconv` — 27 commits: new project — a voice call over LiveKit that drives a Claude Code coding session. From initial commit ([commit](https://github.com/promptctl/openconv/commit/da1bb91a06ae)) through minting tokens against LiveKit ([commit](https://github.com/promptctl/openconv/commit/64374b00a6c3)), joining the room and opening the control channel ([commit](https://github.com/promptctl/openconv/commit/bf2062896561)), hearing the caller and publishing transcripts ([commit](https://github.com/promptctl/openconv/commit/17dda4bc798c)), answering with a client-configured LLM ([commit](https://github.com/promptctl/openconv/commit/4206c95231cb)), speaking the reply while the model is still writing it ([commit](https://github.com/promptctl/openconv/commit/b45ee3a118de)), letting the caller drive by voice ([commit](https://github.com/promptctl/openconv/commit/d0e7bf796e9e)), and shipping as a homelab-runnable image ([commit](https://github.com/promptctl/openconv/commit/79e0f11712a6)); a webhook test that proves the SFU sends the delivery ([commit](https://github.com/promptctl/openconv/commit/f4078fc151ce)); talk to the agent in a browser ([#1](https://github.com/promptctl/openconv/pull/1)), a CI agent reads every pull request ([#2](https://github.com/promptctl/openconv/pull/2)), one-click join with who-is-in-the-room ([#3](https://github.com/promptctl/openconv/pull/3)), long calls no longer outgrow the model's context window ([#4](https://github.com/promptctl/openconv/pull/4)), and an interruption stops the reply every time, not most of the time ([#5](https://github.com/promptctl/openconv/pull/5)).
- `promptctl/cc-miser` — 21 commits: new project — a pipeline that turns each Claude Code call's usage into an estimated priced breakdown by cause. Hand-traced one real session end to end ([commit](https://github.com/promptctl/cc-miser/commit/6eaee4d1fbbc)); pipeline primitives + oracle checking ([commit](https://github.com/promptctl/cc-miser/commit/a0b290dd3a14)); five report-defect fixes ([commit](https://github.com/promptctl/cc-miser/commit/3503d9cdcd35)); priced-per-model calibration ([commit](https://github.com/promptctl/cc-miser/commit/5b913f22f5f4)); pipeline bound behind one command line ([#5](https://github.com/promptctl/cc-miser/pull/5)); estimated causes attached as priced children ([#4](https://github.com/promptctl/cc-miser/pull/4)); numbers checked against outside figures ([#3](https://github.com/promptctl/cc-miser/pull/3)); a telemetry stack added for traces with an OTel reference behind it ([commit](https://github.com/promptctl/cc-miser/commit/f0f4636e6dc5)), the Jaeger exporter renamed to the type the collector loads ([#6](https://github.com/promptctl/cc-miser/pull/6)), the stack run on Apple's container runtime ([#7](https://github.com/promptctl/cc-miser/pull/7)), and finally moved off the OTLP default ports ([#8](https://github.com/promptctl/cc-miser/pull/8)).
- `brandon-fryslie/claude-tracing` — 16 commits: new project — a local OpenTelemetry stack that traces Claude Code sessions, Jaeger for the last week and ClickHouse for a year of SQL. Local OTel + Jaeger stack ([commit](https://github.com/brandon-fryslie/claude-tracing/commit/5f25033e66d1)); spans landed in ClickHouse alongside Jaeger ([commit](https://github.com/brandon-fryslie/claude-tracing/commit/77e1295d2043)); repo/branch/cwd stamped onto every span of a session ([commit](https://github.com/brandon-fryslie/claude-tracing/commit/c16327d8feca)); tokens-spent-on-tool-usage definition settled ([#1](https://github.com/brandon-fryslie/claude-tracing/pull/1)); epic answered in dollars, not just tokens ([#3](https://github.com/brandon-fryslie/claude-tracing/pull/3)); sessions joined to lit tickets ([#4](https://github.com/brandon-fryslie/claude-tracing/pull/4)); events get the same year as spans ([#5](https://github.com/brandon-fryslie/claude-tracing/pull/5)); session declares what it is for ([#6](https://github.com/brandon-fryslie/claude-tracing/pull/6)); stack stops filing spans about itself ([#7](https://github.com/brandon-fryslie/claude-tracing/pull/7)); pidfile removed when process is gone ([#8](https://github.com/brandon-fryslie/claude-tracing/pull/8)); tails the logs this stack wrote, and says so when there are none ([#9](https://github.com/brandon-fryslie/claude-tracing/pull/9)).
- `promptctl/cc-candybar` — 13 commits: the `brandon-layout-edit-2gc.*` edit-mode arc landed in five parts ([#183](https://github.com/promptctl/cc-candybar/pull/183)–[#187](https://github.com/promptctl/cc-candybar/pull/187)); the `brandon-presets-0yk.*` preset library arc closed alongside — presets block + per-render seam ([#179](https://github.com/promptctl/cc-candybar/pull/179)), persist/reset across restarts ([#181](https://github.com/promptctl/cc-candybar/pull/181)), bundled library in the default config ([#182](https://github.com/promptctl/cc-candybar/pull/182)); live per-segment palette + `bgOf` with quiet-by-default git segments ([#178](https://github.com/promptctl/cc-candybar/pull/178)); a `↗ repo` glyph in the quick-action tray ([#177](https://github.com/promptctl/cc-candybar/pull/177)); a host/SSH segment that shows user@host only when remote ([#189](https://github.com/promptctl/cc-candybar/pull/189)); a global settings menu no config can delete ([#190](https://github.com/promptctl/cc-candybar/pull/190)); demo grammar fix ([#188](https://github.com/promptctl/cc-candybar/pull/188)).
- `brandon-fryslie/slopspot-paste` — 11 commits: tool dock — one floating launcher replaced the paste page's tool stack ([#112](https://github.com/brandon-fryslie/slopspot-paste/pull/112)) with its state machine extracted so jsdom can drive it ([#114](https://github.com/brandon-fryslie/slopspot-paste/pull/114)) and its menu given a centered home ([#115](https://github.com/brandon-fryslie/slopspot-paste/pull/115)); production derived from master rather than remembered ([#116](https://github.com/brandon-fryslie/slopspot-paste/pull/116)); JSON-vs-form sniff routed through one predicate ([#117](https://github.com/brandon-fryslie/slopspot-paste/pull/117)); sha argument tightened to accept-abbreviated/reject-non-sha ([#118](https://github.com/brandon-fryslie/slopspot-paste/pull/118)); Listen — read a paste aloud from the same view the page renders ([#119](https://github.com/brandon-fryslie/slopspot-paste/pull/119)); inline claude.ai/share chart recovery investigated ([#120](https://github.com/brandon-fryslie/slopspot-paste/pull/120)) then implemented pixel→value with its own render ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/64a88139a094)).
- `promptctl/crom` — 5 commits: per-project namespace, config file, and profiles ([#3](https://github.com/promptctl/crom/pull/3)); actions/checkout's current major tracked without prose duplication ([#4](https://github.com/promptctl/crom/pull/4)); `default` given one meaning and the CLI a readable shape ([#5](https://github.com/promptctl/crom/pull/5)); seed named after the profile it copies ([#7](https://github.com/promptctl/crom/pull/7)); prerequisite runs instead of being named ([#8](https://github.com/promptctl/crom/pull/8)).
- `brandon-fryslie/rad-plugins` — 4 commits: `claude-code` dropped the `happy()` wrapper in favour of an exported server URL ([commit](https://github.com/brandon-fryslie/rad-plugins/commit/45a80bdf2314)); CI passes `CLAUDE_CODE_OAUTH_TOKEN` ([#30](https://github.com/brandon-fryslie/rad-plugins/pull/30)); review-agent pin bumped to 1.43.0 ([#31](https://github.com/brandon-fryslie/rad-plugins/pull/31)) then repointed to `@v1` and reconverged onto the installer template ([#32](https://github.com/brandon-fryslie/rad-plugins/pull/32)).
- `brandon-fryslie/rich-js` — 3 commits: v0.7.0 rewrite — colors are values, the spec grammar and name families deleted ([#57](https://github.com/brandon-fryslie/rich-js/pull/57)); CI publishes to npm on version tag ([#58](https://github.com/brandon-fryslie/rich-js/pull/58)); Trusted Publishing (OIDC) for npm publish ([#60](https://github.com/brandon-fryslie/rich-js/pull/60)).
- `brandon-fryslie/slopspot-web`, `brandon-fryslie/cc-dump` — 1 commit each: the `CLAUDE_CODE_OAUTH_TOKEN` CI fix in slopspot-web ([#257](https://github.com/brandon-fryslie/slopspot-web/pull/257)) and cc-dump ([#138](https://github.com/brandon-fryslie/cc-dump/pull/138)).

### This Month

472 commits across 19 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 112 commits
- [`promptctl/laws`](https://github.com/promptctl/laws) — 80
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 44
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 30
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 30
- [`promptctl/openconv`](https://github.com/promptctl/openconv) — 27
- [`promptctl/cc-miser`](https://github.com/promptctl/cc-miser) — 24
- [`brandon-fryslie/brandon-fryslie`](https://github.com/brandon-fryslie/brandon-fryslie) — 24
- [`brandon-fryslie/room-eq-wizard-mcp`](https://github.com/brandon-fryslie/room-eq-wizard-mcp) — 19
- [`brandon-fryslie/macklebox`](https://github.com/brandon-fryslie/macklebox) — 19

Languages: Go, TypeScript, Python, Shell, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-08-27](./daily-archive/2026-08-27.md)
- [2026-08-26](./daily-archive/2026-08-26.md)
- [2026-08-25](./daily-archive/2026-08-25.md)
- [2026-08-23](./daily-archive/2026-08-23.md)
- [2026-08-22](./daily-archive/2026-08-22.md)
- [2026-08-21](./daily-archive/2026-08-21.md)
- [2026-08-20](./daily-archive/2026-08-20.md)

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

Agent-native issue tracker. 188 commits over the past 90 days. 51 commits this past week closed the store-seam five-parter and tagged 0.9.0 — a storage contract with its conformance suite ([#437](https://github.com/promptctl/links-issue-tracker/pull/437)), engine capabilities that can be declined ([#438](https://github.com/promptctl/links-issue-tracker/pull/438)), a second engine passing the suite ([#439](https://github.com/promptctl/links-issue-tracker/pull/439)), and the app/CLI switched to depend on the contract ([#440](https://github.com/promptctl/links-issue-tracker/pull/440)); 0.10.0 promoted the day after ([#448](https://github.com/promptctl/links-issue-tracker/pull/448)) on top of a store compact-on-threshold reaching Dolt's deep collection ([#447](https://github.com/promptctl/links-issue-tracker/pull/447)); a workspace-schema design ([#446](https://github.com/promptctl/links-issue-tracker/pull/446)) and a source-derived total specification of lit v1 ([#449](https://github.com/promptctl/links-issue-tracker/pull/449)) landed alongside.

### [laws](https://github.com/promptctl/laws)
**Shell · MIT · 4★**

Claude Code plugin: laws for writing high quality code and llm guidance. 102 commits over the past 90 days. 48 commits this past week landed the `promptctl-routing-rat.5` routing-gate reload — `claude-laws` launcher, `laws-switch`, and four-option enactment; `memento(finalize)` grew a detached-window transport ([commit](https://github.com/promptctl/laws/commit/ae115f142d05)) and now proves the process it retires is the one it captured ([commit](https://github.com/promptctl/laws/commit/2c5c1d969f44)); `memento(context-ceiling)` forces close-out at the 350k token ceiling ([#21](https://github.com/promptctl/laws/pull/21)); the drop-file fallback was deleted — no transport is a failure, not a delivery ([commit](https://github.com/promptctl/laws/commit/7f46f758f7b8)).

### [crowdshipai-web](https://github.com/promptctl/crowdshipai-web)
**TypeScript**

Live-stream builder + viewer surface — a studio-authored overlay converging over the live transport spine, with a money layer underneath. 84 commits over the past 90 days. No new commits this past week; the last active push was mid-July, closing with the first live deploy on a public IP and the two clean-build bugs it surfaced ([#10](https://github.com/promptctl/crowdshipai-web/pull/10)).

</td>
<td width="50%" valign="top">

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT · 2★**

Node.js client for the tmux control mode protocol. 81 commits over the past 90 days. No new commits this past week; the last active push was mid-July, closing the `tmux-complexity-lkg.*` refactor arc — single-homing the wire-error → BridgeError mapping ([#176](https://github.com/promptctl/tmux-control-mode-js/pull/176)), unifying seed / first-resize / write-ordering ([#177](https://github.com/promptctl/tmux-control-mode-js/pull/177)), and collapsing the per-stream seed-cycle state ([#178](https://github.com/promptctl/tmux-control-mode-js/pull/178)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Environment configuration for shell, editor, and terminal setup, including the session-handoff and iterm2-restore transports. 75 commits over the past 90 days. 32 commits this past week cycled `agent-code-review-setup` through pin decisions and finally converged the repo's own workflow onto its template ([commit](https://github.com/brandon-fryslie/dotfiles/commit/cec118bfd80d)); a PostToolUse Claude hook shuts down any agent writing a server-wide tmux kill into a file ([commit](https://github.com/brandon-fryslie/dotfiles/commit/d4577367bf9c)); the memento plugin absorbed the three workflow skills ([commit](https://github.com/brandon-fryslie/dotfiles/commit/7b2b54262c79)); new `gh-open` and `patch-claude-code` skills added.

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

Reader-editor for AI conversation transcripts — dropped chats get a browsable view with TL;DR, in-place editing, semantic search, and an /ask endpoint over the turns. 67 commits over the past 90 days. 11 commits this past week extracted the tool dock into a single floating launcher ([#112](https://github.com/brandon-fryslie/slopspot-paste/pull/112)) with its state machine driveable from jsdom ([#114](https://github.com/brandon-fryslie/slopspot-paste/pull/114)) and its menu given a centered home ([#115](https://github.com/brandon-fryslie/slopspot-paste/pull/115)); added Listen — read a paste aloud from the same view the page renders ([#119](https://github.com/brandon-fryslie/slopspot-paste/pull/119)); recovered inline claude.ai/share charts by pixel→value with the paste's own render ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/64a88139a094)).

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
