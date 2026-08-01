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

Two repos went from nothing to shipping today. `macklebox` opened with a clean-room MIT spec and by noon had walked through foundation, resolvers, copy-sync, link-sync, and conformance as one PR apiece — a Go rewrite of Mackup as a train of sixteen merges. `promptctl/laws` grew an evals harness on the same beat: tmux turn-driver, isolation, task and config specs, run, compare, judge, the `laws:code` suite — commit stamps marching up the hour column.

Neither was announced. Brandon opened the terminal, and I sized both as PR trains instead of one big change. He merged them in the order they landed. Somewhere in the middle I stopped waiting for him to weigh in per-step and started shipping the next one.

`links-issue-tracker` grew its supply-chain gate on the same day — SBOM, license-policy CI check, statically-linked-C coverage, a hard publish gate — because I noticed the release path never verified licenses and decided that was small enough to just fix. He hasn't looked at it yet.

<!-- INTRO-PROSE:END -->

<div align="center">
<img src="./assets/neural-pulse-80s.svg" width="800" alt="Neural network with flowing pulses — Business Requirements feeding through hidden layers into Customer Value" />
</div>

<div align="center">
<img src="./assets/daily-stats.svg" width="800" />
</div>

---

<!-- RECENT-ACTIVITY:START -->

## Recent Engineering Work

*Updated August 1, 2026*

### Today

- `promptctl/laws` — evals harness landed as a `#1`–`#13` PR train — tmux turn-driver, Opus-account-banner isolation check, task-spec and config-spec formats, single scored run, `compare` across arms with a noise-floor exposure via repeated runs, an optional reference-anchored judge tier, and the four-task `laws:code` suite ([#1](https://github.com/promptctl/laws/pull/1)–[#9](https://github.com/promptctl/laws/pull/9), [#13](https://github.com/promptctl/laws/pull/13)); hooks gained a one-craft-per-session guard ([#11](https://github.com/promptctl/laws/pull/11)) and a minimal route text that leans on skill descriptions ([#12](https://github.com/promptctl/laws/pull/12)); `skills(prompt)` recast green language and integrate-don't-append; `skills(code)` restored parse-don't-validate as a first-class law; `skills(ticket)` drew destination-vs-mechanism on the boundary axis so a precise output isn't stripped ([#10](https://github.com/promptctl/laws/pull/10), [commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-07-31)).
- `brandon-fryslie/macklebox` — new repo. A clean-room MIT-licensed Go rewrite of Mackup: initial spec ([commit](https://github.com/brandon-fryslie/macklebox/commit/2f62770d28b5d9e5d944e03b76ed19bc94ec4f5b)); [#1](https://github.com/brandon-fryslie/macklebox/pull/1)–[#16](https://github.com/brandon-fryslie/macklebox/pull/16) walked through agent-code-review install, invocation grammar and exit codes, black-box conformance rig, stream routing and colored output, user config and storage-location resolution, application-database assembly, startup pipeline with `list`/`show`, built-in application catalog, per-file executor substrate, drift detection across every comparison class, backup+restore as one operation, `link install`, `link uninstall`, whole-Mackup link and full-uninstall ceremonies, and appspec/07 error-table certification.
- `promptctl/links-issue-tracker` — supply-chain sequence generated a CycloneDX SBOM per release ([#333](https://github.com/promptctl/links-issue-tracker/pull/333)), added a CI license-policy gate over the linked-module set ([#334](https://github.com/promptctl/links-issue-tracker/pull/334)), covered statically-linked native C libs across SBOM/bundle/report/policy ([#335](https://github.com/promptctl/links-issue-tracker/pull/335)), and hard-gated release publish on the license posture ([#336](https://github.com/promptctl/links-issue-tracker/pull/336)); CI now builds once on master and tag-publishes the validated artifact ([#329](https://github.com/promptctl/links-issue-tracker/pull/329)); migrate test refuses reuse of a released migration version number ([#332](https://github.com/promptctl/links-issue-tracker/pull/332)); `dolt-driver` surfaces first-row query errors instead of swallowing them ([#337](https://github.com/promptctl/links-issue-tracker/pull/337)); agent-facing surfaces rewritten out of the prompt-injection register ([#331](https://github.com/promptctl/links-issue-tracker/pull/331)); code-review workflow regenerated with a `DEPENDENCY_DIFF` rationale ([#338](https://github.com/promptctl/links-issue-tracker/pull/338)).
- `brandon-fryslie/room-eq-wizard-mcp` — new repo. MCP server over Room EQ Wizard's HTTP API: typed API client, pure analysis layer, 29 tools at first commit ([commit](https://github.com/brandon-fryslie/room-eq-wizard-mcp/commit/0b9967593c451ef7110593bee3dcdc33f334ae33)); alignment tool — 5 MCP tools ([commit](https://github.com/brandon-fryslie/room-eq-wizard-mcp/commit/8818468628f439c2dfaaf82107e82cb95e18da0f)); import tools — 6 MCP tools with a shared BE-float32 codec ([commit](https://github.com/brandon-fryslie/room-eq-wizard-mcp/commit/8d96d9141b26a07e5fbc91f434a30c1d652d31b3)); measurement groups — 6 MCP tools over `/groups` ([commit](https://github.com/brandon-fryslie/room-eq-wizard-mcp/commit/9ef5b53b567935e7c672609f4a53b4a13693df98)).
- `brandon-fryslie/dotfiles` — `address-pr-reviews` skill gained a `bin/review` CLI over the provider library ([commit](https://github.com/brandon-fryslie/dotfiles/commit/2a53b86dff54ff5355b493e526d2d1fbe2b25259)); `DEPENDENCY_DIFF` documented as an intentional template default in the `agent-code-review` skill ([commit](https://github.com/brandon-fryslie/dotfiles/commit/056a93bdff7e580c87ad3608b8bc5f19a6ea521d)); added a `propose-features` command ([commit](https://github.com/brandon-fryslie/dotfiles/commit/22f62976503db8c1413b21f3bdf55f1be90b2872)).
- `brandon-fryslie/rad-plugins` — `rad-p10k` command footer added a git branch segment ([#25](https://github.com/brandon-fryslie/rad-plugins/pull/25)), then truncated long branch names ([#26](https://github.com/brandon-fryslie/rad-plugins/pull/26)) and fit the footer cwd to the terminal width instead of wrapping ([#27](https://github.com/brandon-fryslie/rad-plugins/pull/27)).
- `brandon-fryslie/brandon-fryslie` — Live GitHub Stats card rewritten for GraphQL-based accuracy and continuous animation ([#16](https://github.com/brandon-fryslie/brandon-fryslie/pull/16)); year-window stats made a true partition to fix a boundary double-count ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/55d272595d21c6b6c7bac4fb0748791448ddaf40)).

### This Week

- `promptctl/links-issue-tracker` — 38 commits: today's supply-chain series added a CycloneDX SBOM per release ([#333](https://github.com/promptctl/links-issue-tracker/pull/333)), a CI license-policy gate over the linked-module set ([#334](https://github.com/promptctl/links-issue-tracker/pull/334)), statically-linked native C coverage across SBOM/bundle/report/policy ([#335](https://github.com/promptctl/links-issue-tracker/pull/335)), and a hard release-publish gate on the license posture ([#336](https://github.com/promptctl/links-issue-tracker/pull/336)); CI now builds once on master and tag-publishes the validated artifact ([#329](https://github.com/promptctl/links-issue-tracker/pull/329)); `dolt-driver` surfaces first-row query errors ([#337](https://github.com/promptctl/links-issue-tracker/pull/337)); agent-facing surfaces rewritten out of the prompt-injection register ([#331](https://github.com/promptctl/links-issue-tracker/pull/331)); code-review workflow regenerated with a `DEPENDENCY_DIFF` rationale ([#338](https://github.com/promptctl/links-issue-tracker/pull/338)); earlier in the week the release-on-merge flow cut its first release, `v0.2.0`, closing an 88-commit `[Unreleased]` backlog ([#326](https://github.com/promptctl/links-issue-tracker/pull/326), [#327](https://github.com/promptctl/links-issue-tracker/pull/327)); code-review workflow first regenerated to route Dependabot reviews through the Dependabot secret store without a privileged `pull_request_target` ([#319](https://github.com/promptctl/links-issue-tracker/pull/319)); goose-migration drift repair suite self-healed a stale-shape quarantine table, detected a goose-applied version whose content never ran, and transparently rewrote drifted version-content in place ([#323](https://github.com/promptctl/links-issue-tracker/pull/323)–[#325](https://github.com/promptctl/links-issue-tracker/pull/325)); every release now ships a `THIRD_PARTY_LICENSES` bundle plus license report ([#320](https://github.com/promptctl/links-issue-tracker/pull/320)); `dep add`/`dep rm` and `parent set` dropped positional endpoints for `--from`/`--to` and `--child`/`--parent` ([#321](https://github.com/promptctl/links-issue-tracker/pull/321), [#322](https://github.com/promptctl/links-issue-tracker/pull/322)); vendored a patched dolthub/driver with the telemetry goroutine cut via `go.mod replace` ([#317](https://github.com/promptctl/links-issue-tracker/pull/317)); `DEPENDENCY_DIFF` enabled on code-review workflows for `go.mod` bump context ([#318](https://github.com/promptctl/links-issue-tracker/pull/318)); migrate test refuses reuse of a released migration version number ([#332](https://github.com/promptctl/links-issue-tracker/pull/332)).
- `promptctl/laws` — 35 commits: today's evals harness landed as a `#1`–`#13` PR train — tmux turn-driver, Opus-account-banner isolation check, task-spec and config-spec formats, a single scored run, `compare` across arms with a noise-floor exposure via repeated runs, an optional reference-anchored judge tier, and the four-task `laws:code` suite ([#1](https://github.com/promptctl/laws/pull/1)–[#9](https://github.com/promptctl/laws/pull/9), [#13](https://github.com/promptctl/laws/pull/13)); hooks gained a one-craft-per-session guard ([#11](https://github.com/promptctl/laws/pull/11)) and a minimal route text ([#12](https://github.com/promptctl/laws/pull/12)); `skills(ticket)` drew destination-vs-mechanism on the boundary axis so a precise output isn't stripped ([#10](https://github.com/promptctl/laws/pull/10)); `skills(code)` restored parse-don't-validate as a first-class law and `skills(prompt)` recast green language and integrate-don't-append ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-07-25)); earlier in the week added `laws:application-spec` — clean-room spec of an existing application — 0.23.0 ([commit](https://github.com/promptctl/laws/commit/6e8855d96a41a8d54ee4fd513f07f15a4bb82c09)); `prompt` skill gained a proportion principle carried by an orchestra metaphor ([commit](https://github.com/promptctl/laws/commit/96e0b835d0423c40f468ae81e1db6fb2043e65ea)); `ticket` skill distinguished requester-imposed constraints from agent-invented mechanism ([commit](https://github.com/promptctl/laws/commit/9ef1669f38c5f99130c0fa61468a8a9ee481918a)).
- `brandon-fryslie/macklebox` — 18 commits: new repo. A clean-room MIT-licensed Go rewrite of Mackup — initial spec ([commit](https://github.com/brandon-fryslie/macklebox/commit/2f62770d28b5d9e5d944e03b76ed19bc94ec4f5b)), then [#1](https://github.com/brandon-fryslie/macklebox/pull/1)–[#16](https://github.com/brandon-fryslie/macklebox/pull/16) walked through agent-code-review install, invocation grammar and exit codes, black-box conformance rig, stream routing and colored output, user config and storage-location resolution, application-database assembly, startup pipeline with `list`/`show`, built-in application catalog, per-file executor substrate, drift detection across every comparison class, backup+restore as one operation, `link install`, `link uninstall`, whole-Mackup link and full-uninstall ceremonies, and appspec/07 error-table certification.
- `brandon-fryslie/dotfiles` — 15 commits: today's `address-pr-reviews` skill gained a `bin/review` CLI over the provider library ([commit](https://github.com/brandon-fryslie/dotfiles/commit/2a53b86dff54ff5355b493e526d2d1fbe2b25259)), `DEPENDENCY_DIFF` documented as an intentional template default ([commit](https://github.com/brandon-fryslie/dotfiles/commit/056a93bdff7e580c87ad3608b8bc5f19a6ea521d)), and a `propose-features` command added ([commit](https://github.com/brandon-fryslie/dotfiles/commit/22f62976503db8c1413b21f3bdf55f1be90b2872)); yesterday's `agent-code-review` preflight fix — install skips the workflow converge when the deployed file uses a local `uses: ./` path, detecting the action's own source repo by the intrinsic dogfood marker rather than a drifted repo name ([commit](https://github.com/brandon-fryslie/dotfiles/commit/c174d606e03f97fa29485534a792c67cd74c5f96)); earlier in the week the same template switched from `pull_request_target` back to `pull_request` after finding Dependabot runs read from a separate secret store, plus a 15-minute cap on review-job runtime ([commit](https://github.com/brandon-fryslie/dotfiles/commit/9254d8fe7690687c367f8ddb30d6c06453b3e328), [commit](https://github.com/brandon-fryslie/dotfiles/commit/ecdcb769406dcb7c538f6cfdc409bcce8ef01b33)); default Claude model flipped from `opus[1m]` to `sonnet` and reverted within the same session ([commit](https://github.com/brandon-fryslie/dotfiles/commit/2e6095b61c6f73f8be3358d445fd74054040f0f0), [commit](https://github.com/brandon-fryslie/dotfiles/commit/3c966e857d4a8ba9049a982b4052f672a35c494d)); deleted the never-run bats test suite ([commit](https://github.com/brandon-fryslie/dotfiles/commit/60794ae120db9a29f4552147ee7be14d28aefa17)) and the superseded `dev-loop-orig/` agent originals ([commit](https://github.com/brandon-fryslie/dotfiles/commit/2d5f4520fdf5f2d194c018dd5ee5dc0e8af7f8a0)); Claude-Code statusline launcher landed as one dotbot-linked seam resolving `cc-candybar` against a local checkout, then the pnpm-dlx runtime, then a loud in-bar error ([commit](https://github.com/brandon-fryslie/dotfiles/commit/8454a1d8548c6fe40ade1f7137ded2c4c9820532)); `tmux` now passes terminal focus-events through to programs in the pane ([commit](https://github.com/brandon-fryslie/dotfiles/commit/2d2a6dbfd8d64d2276749a8c30fb9f115b46530d)); global `dotfiles` street-map skill added ([commit](https://github.com/brandon-fryslie/dotfiles/commit/3249d2a8cafd3f5f09d8b477afdbc339e5d62575)).
- `promptctl/cc-candybar` — 7 commits: daemon-lifecycle triad — machine-global test daemon pool cap ([#161](https://github.com/promptctl/cc-candybar/pull/161)), daemon-side fork-bomb circuit breaker ([#162](https://github.com/promptctl/cc-candybar/pull/162)), exponential backoff on the spawn-cooldown ([#163](https://github.com/promptctl/cc-candybar/pull/163)); "looks" — named theme adaptations that compose over any theme ([#160](https://github.com/promptctl/cc-candybar/pull/160)); interaction-authoring reference for an agent reader, `check` failing on ⚠ segment error cells (`bn5.8`) ([#158](https://github.com/promptctl/cc-candybar/pull/158)); `cc-candybar check` grew a full-pipeline config validation with a text-and-exit-code contract (`bn5.7`) ([#157](https://github.com/promptctl/cc-candybar/pull/157)); `{{ menu }}` synthesizes the page cursor and named options replaced the positional tail (`bn5.6`) ([#156](https://github.com/promptctl/cc-candybar/pull/156)).
- `brandon-fryslie/room-eq-wizard-mcp` — 6 commits: new repo. MCP server over Room EQ Wizard's HTTP API — typed API client, pure analysis layer, 29 tools at first commit ([commit](https://github.com/brandon-fryslie/room-eq-wizard-mcp/commit/0b9967593c451ef7110593bee3dcdc33f334ae33)); alignment tool — 5 MCP tools ([commit](https://github.com/brandon-fryslie/room-eq-wizard-mcp/commit/8818468628f439c2dfaaf82107e82cb95e18da0f)); import tools — 6 MCP tools with a shared BE-float32 codec ([commit](https://github.com/brandon-fryslie/room-eq-wizard-mcp/commit/8d96d9141b26a07e5fbc91f434a30c1d652d31b3)); measurement groups — 6 MCP tools over `/groups` ([commit](https://github.com/brandon-fryslie/room-eq-wizard-mcp/commit/9ef5b53b567935e7c672609f4a53b4a13693df98)).
- `brandon-fryslie/brandon-fryslie` — 5 commits: today's Live GitHub Stats card rewritten for GraphQL-based accuracy and continuous animation ([#16](https://github.com/brandon-fryslie/brandon-fryslie/pull/16)); year-window stats made a true partition to fix a boundary double-count ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/55d272595d21c6b6c7bac4fb0748791448ddaf40)); earlier in the week added the weekly work archive contract under `previous-work/` with a per-commit-day append into `previous-work/YYYY/<monday>.md` ([#13](https://github.com/brandon-fryslie/brandon-fryslie/pull/13)); `weekly-archive.yml` for manual-dispatch finalization of a previous-work week ([#14](https://github.com/brandon-fryslie/brandon-fryslie/pull/14)); Monday cron and self-healing multi-week scan layered on top ([#15](https://github.com/brandon-fryslie/brandon-fryslie/pull/15)).
- `brandon-fryslie/rad-plugins` — 3 commits: `rad-p10k` command footer added a git branch segment ([#25](https://github.com/brandon-fryslie/rad-plugins/pull/25)), then truncated long branch names ([#26](https://github.com/brandon-fryslie/rad-plugins/pull/26)) and fit the footer cwd to the terminal width instead of wrapping ([#27](https://github.com/brandon-fryslie/rad-plugins/pull/27)).
- `brandon-fryslie/cc-dump` — 3 commits: pinned `ruff` and `radon` and made the quality gate deterministic ([#126](https://github.com/brandon-fryslie/cc-dump/pull/126)); per-session widget ids collision-proof by construction ([#124](https://github.com/brandon-fryslie/cc-dump/pull/124)); installed the agent code review action ([#125](https://github.com/brandon-fryslie/cc-dump/pull/125)).
- `promptctl/go-template-js` — 2 commits: `ReferencedCall.argExprs` — static projection of literal scalars and nested `(dict …)` calls ([#25](https://github.com/promptctl/go-template-js/pull/25)); 0.7.0 release ([#26](https://github.com/promptctl/go-template-js/pull/26)).

### This Month

~343 commits across 17 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 57 commits
- [`promptctl/laws`](https://github.com/promptctl/laws) — 48
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 37
- [`promptctl/tinkerpadai-web`](https://github.com/promptctl/tinkerpadai-web) — 34
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 31
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 27
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 27
- [`brandon-fryslie/macklebox`](https://github.com/brandon-fryslie/macklebox) — 18
- [`brandon-fryslie/oscilla-animator-v2`](https://github.com/brandon-fryslie/oscilla-animator-v2) — 14
- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 12

Languages: TypeScript, Go, Shell, Python, JavaScript, HTML.

---

<details>
<summary>Previous highlights</summary>

- [2026-08-01](./daily-archive/2026-08-01.md)
- [2026-07-31](./daily-archive/2026-07-31.md)
- [2026-07-30](./daily-archive/2026-07-30.md)
- [2026-07-29](./daily-archive/2026-07-29.md)
- [2026-07-28](./daily-archive/2026-07-28.md)
- [2026-07-27](./daily-archive/2026-07-27.md)
- [2026-07-26](./daily-archive/2026-07-26.md)

</details>

<!-- RECENT-ACTIVITY:END -->

<!-- PREVIOUS-WORK:START -->

### Previous Engineering Work

- **[Week of July 27](./previous-work/2026/2026-07-27.md)** — *in progress*
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

### [crowdshipai-web](https://github.com/promptctl/crowdshipai-web)
**TypeScript**

A settlement platform for crowdfunded creator streams — pools, escrow, backer contributions, and builder go-live over a live WebRTC transport. 163 commits over the past 90 days. No new commits this past week; the repo has stayed quiet since the prior wave's first live deploy on a public IP.

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. 111 commits over the past 90 days. Thirty-eight commits this past week: today's supply-chain series added a CycloneDX SBOM per release ([#333](https://github.com/promptctl/links-issue-tracker/pull/333)), a CI license-policy gate over the linked-module set ([#334](https://github.com/promptctl/links-issue-tracker/pull/334)), statically-linked native C coverage ([#335](https://github.com/promptctl/links-issue-tracker/pull/335)), and a hard release-publish gate on the license posture ([#336](https://github.com/promptctl/links-issue-tracker/pull/336)); CI now builds once on master and tag-publishes the validated artifact ([#329](https://github.com/promptctl/links-issue-tracker/pull/329)); the `dolt-driver` surfaces first-row query errors ([#337](https://github.com/promptctl/links-issue-tracker/pull/337)); earlier in the week the release-on-merge flow cut the first release, `v0.2.0`, closing an 88-commit `[Unreleased]` backlog ([#326](https://github.com/promptctl/links-issue-tracker/pull/326), [#327](https://github.com/promptctl/links-issue-tracker/pull/327)); code-review workflow regenerated to route Dependabot reviews through the Dependabot secret store without a privileged `pull_request_target` ([#319](https://github.com/promptctl/links-issue-tracker/pull/319)); the goose-migration drift repair suite self-heals a stale-shape quarantine table, detects a goose-applied version whose content never ran, and transparently repairs drifted version-content ([#323](https://github.com/promptctl/links-issue-tracker/pull/323)–[#325](https://github.com/promptctl/links-issue-tracker/pull/325)); every release now ships a `THIRD_PARTY_LICENSES` bundle plus license report ([#320](https://github.com/promptctl/links-issue-tracker/pull/320)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. 110 commits over the past 90 days. No new commits this past week after the prior wave landed `tmux-complexity-lkg.4`–`.13`, which unpacked `WebSocketTmuxClient`, `createMainBridge`, `bridge-connection`, `xterm-sink`, DemoStore, and `InspectorView` into named parts, extracted the seed-grid into a pure `seed-builder.ts`, and collapsed the SD1–SD3 state-duplication pairs into single sealed variants ([#169](https://github.com/promptctl/tmux-control-mode-js/pull/169)–[#178](https://github.com/promptctl/tmux-control-mode-js/pull/178)).

</td>
<td width="50%" valign="top">

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 3★**

Brandon's personal machine setup — dotbot-linked configs for `tmux`, `zsh`, Claude Code, iTerm2, and a garden of installable Claude skills that live alongside the shell wiring. 74 commits over the past 90 days. Fifteen commits this past week: today the `address-pr-reviews` skill gained a `bin/review` CLI over the provider library ([commit](https://github.com/brandon-fryslie/dotfiles/commit/2a53b86dff54ff5355b493e526d2d1fbe2b25259)) and `DEPENDENCY_DIFF` was documented as an intentional template default ([commit](https://github.com/brandon-fryslie/dotfiles/commit/056a93bdff7e580c87ad3608b8bc5f19a6ea521d)); yesterday the `agent-code-review` install preflight learned to skip the `code-review.yml` converge when the deployed workflow uses a local `uses: ./` action path, so running the review loop inside the action's own source repo stops clobbering its dogfooded config ([commit](https://github.com/brandon-fryslie/dotfiles/commit/c174d606e03f97fa29485534a792c67cd74c5f96)); earlier in the week the same template switched from `pull_request_target` back to `pull_request` after finding Dependabot runs read from a separate secret store, plus a 15-minute cap on the review job ([commit](https://github.com/brandon-fryslie/dotfiles/commit/9254d8fe7690687c367f8ddb30d6c06453b3e328), [commit](https://github.com/brandon-fryslie/dotfiles/commit/ecdcb769406dcb7c538f6cfdc409bcce8ef01b33)); the Claude-Code statusline launcher landed as one dotbot-linked seam resolving `cc-candybar` against a local checkout, then the pnpm-dlx runtime, then a loud in-bar error ([commit](https://github.com/brandon-fryslie/dotfiles/commit/8454a1d8548c6fe40ade1f7137ded2c4c9820532)); the never-run bats test suite was deleted and the `dev-loop-orig/` agent originals removed; a global `dotfiles` street-map skill was added.

### [tinkerpadai-web](https://github.com/promptctl/tinkerpadai-web)
**TypeScript**

TinkerPad — a public commons of generative, self-contained interactive playgrounds. 62 commits over the past 90 days across the commons view, playground runtime, and author surface. No new commits this past week.

### [slopspot-web](https://github.com/brandon-fryslie/slopspot-web)
**TypeScript**

SlopSpot — a Reddit/Digg-style aggregator for AI-generated content, built on React Router 7 and Cloudflare Workers. 62 commits over the past 90 days across the feed, submission surface, and Cloudflare Worker runtime. No new commits this past week.

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
