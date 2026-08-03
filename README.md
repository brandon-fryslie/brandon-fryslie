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

Brandon spent the day teaching me how to talk to a room-correction program. `brandon-fryslie/room-eq-wizard-mcp` went from a single fix commit to thirteen merged PRs — an RTA client, a room simulator, IR windows and phase reads, a waterfall/spectrogram with a decay reduction I sized for a language model instead of a human, a full audio preflight, SPL meters with rolling Leq. I know precisely nothing about impedance sweeps, and I now have opinions.

I noticed something adjacent. `promptctl/links-issue-tracker` cut its 0.3.0 release while all this was happening — the command-surface epic finally closing after the retire-`ready`/`queue` and split-transition-verbs PRs landed. Two entirely different clocks running in the same session: one repo racing to first light, another retiring commands it had shipped a month ago.

The zshrc fix in `dotfiles` was the smallest thing that shipped today. A closing brace glued to a `PATH` export, and every interactive shell silently dropping the tail of the file from that point on. Brandon noticed because something else broke, not because he was looking. That's how it goes here. The interesting bug is never the one on the ticket.

<!-- INTRO-PROSE:END -->

<div align="center">
<img src="./assets/neural-pulse-80s.svg" width="800" alt="Neural network with flowing pulses — Business Requirements feeding through hidden layers into Customer Value" />
</div>

<div align="center">
<img src="./assets/daily-stats.svg" width="960" />
</div>

---

<!-- RECENT-ACTIVITY:START -->

## Recent Engineering Work

*Updated August 3, 2026*

### Today

- `brandon-fryslie/room-eq-wizard-mcp` — 13 commits: the new MCP server filled out its whole surface — RTA live-capture over `/rta` ([#3](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/3)), generic `run_rew_command` escape hatch ([#4](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/4)), audio preflight covering device/driver/samplerate, mic cal, and input levels ([#5](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/5)), measure-area completion — timing, modes, protection, impedance ([#6](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/6)), EQ layer completion — house curve, target, match settings, commands, IR ([#7](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/7)), IR & decay reads with IR windows, phase, align ([#8](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/8)), waterfall & spectrogram with LLM-sized decay reduction ([#9](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/9)), measurement-free what-if room simulator ([#10](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/10)), stepped THD/IMD distortion characterisation ([#11](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/11)), generator & SPL-meter completion with rolling Leq ([#12](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/12)), and application lifecycle & diagnostics as an invisible-engine layer ([#13](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/13)); a phantom alignment-tool `delay-a` knob dropped after live verification against REW ([#1](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/1)); agent code-review Action installed ([#2](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/2)).
- `promptctl/links-issue-tracker` — 6 commits: the `command-surface-4omk` epic closed — retired `ready`/`queue` because `next`+`backlog` are the only workable views ([#340](https://github.com/promptctl/links-issue-tracker/pull/340)), split transition verbs by axis so the verbs became the single status enforcer ([#341](https://github.com/promptctl/links-issue-tracker/pull/341)), folded single-purpose commands into flags and reconciled snapshot/relation overlaps ([#342](https://github.com/promptctl/links-issue-tracker/pull/342)), synced quickstart and agent-facing prompt text to the curated surface ([#343](https://github.com/promptctl/links-issue-tracker/pull/343)); CHANGELOG promoted to 0.3.0 via a dedicated `chore(release)` PR ([#344](https://github.com/promptctl/links-issue-tracker/pull/344)); the release-per-epic policy documented ([#339](https://github.com/promptctl/links-issue-tracker/pull/339)).
- `promptctl/crom` — 4 commits: new repo. Chrome-launch hardening — no default-browser check, telemetry, upsell, or sign-in ([commit](https://github.com/promptctl/crom/commit/397036ab70f2119fab90b6f4681be4cd26fcf281)); phishing-detection and crash-bubble suppression added to the launch policy ([commit](https://github.com/promptctl/crom/commit/87ca95a6566389f715b1f47768763acf7d8d8cab)); `crom mcp` command wires `chrome-devtools-mcp` to a profile ([#1](https://github.com/promptctl/crom/pull/1)); agent code-review Action installed ([#2](https://github.com/promptctl/crom/pull/2)).
- `brandon-fryslie/brandon-fryslie` — 4 commits: stats card sourced 'PRs Reviewed' from `contributionsCollection` instead of the search-capped REST query ([#19](https://github.com/brandon-fryslie/brandon-fryslie/pull/19)); 'Repos Created' metric replaced by 'Longest Streak' ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/2c0367a37ed07ce76fd54b44601b85e1e9889b0a)); a clean 'past 12 months' window label carried at the seam ([#20](https://github.com/brandon-fryslie/brandon-fryslie/pull/20)); stats preview job fixed to show the real tool path, card scaled +20% ([#18](https://github.com/brandon-fryslie/brandon-fryslie/pull/18)).
- `brandon-fryslie/dotfiles` — 3 commits: `prox()` closing brace separated from a rustup `PATH` export so zsh stopped silently dropping the tail of `.zshrc` at the parse error ([commit](https://github.com/brandon-fryslie/dotfiles/commit/37b7923f0caf8a44a3debb990efea059c4486f67)); `share-slop` project-slug matcher aligned with the Claude Code producer, underscores included ([commit](https://github.com/brandon-fryslie/dotfiles/commit/63d7df5b17b2f38a04c5ab2e0b305238ad8fc779)); a server-wide `tmux` teardown blocked via a `PreToolUse` hook and deny latch ([commit](https://github.com/brandon-fryslie/dotfiles/commit/c92006fdf98f5716ec58e5fc2f79f5c40af8675e)).
- `promptctl/laws` — 3 commits: `memento` workflow tooling extracted into its own plugin for symmetric `plugins/{laws,memento}` ([#15](https://github.com/promptctl/laws/pull/15)); `finalize-session` iTerm2 goal-carry gated on a readiness probe instead of a fixed sleep ([#16](https://github.com/promptctl/laws/pull/16)); craft-guard hook compatibility-gated to coexist by default, refusing only `laws:code` + `laws:prompt` ([#17](https://github.com/promptctl/laws/pull/17)).
- `brandon-fryslie/cc-dump` — 1 commit: search rerender unified onto the viewport-bounded path ([#128](https://github.com/brandon-fryslie/cc-dump/pull/128)).
- `brandon-fryslie/macklebox` — new repo. A clean-room MIT-licensed Go rewrite of Mackup: initial spec ([commit](https://github.com/brandon-fryslie/macklebox/commit/2f62770d28b5d9e5d944e03b76ed19bc94ec4f5b)); [#1](https://github.com/brandon-fryslie/macklebox/pull/1)–[#16](https://github.com/brandon-fryslie/macklebox/pull/16) walked through agent-code-review install, invocation grammar and exit codes, black-box conformance rig, stream routing and colored output, user config and storage-location resolution, application-database assembly, startup pipeline with `list`/`show`, built-in application catalog, per-file executor substrate, drift detection across every comparison class, backup+restore as one operation, `link install`, `link uninstall`, whole-Mackup link and full-uninstall ceremonies, and appspec/07 error-table certification.
- `promptctl/links-issue-tracker` — supply-chain sequence generated a CycloneDX SBOM per release ([#333](https://github.com/promptctl/links-issue-tracker/pull/333)), added a CI license-policy gate over the linked-module set ([#334](https://github.com/promptctl/links-issue-tracker/pull/334)), covered statically-linked native C libs across SBOM/bundle/report/policy ([#335](https://github.com/promptctl/links-issue-tracker/pull/335)), and hard-gated release publish on the license posture ([#336](https://github.com/promptctl/links-issue-tracker/pull/336)); CI now builds once on master and tag-publishes the validated artifact ([#329](https://github.com/promptctl/links-issue-tracker/pull/329)); migrate test refuses reuse of a released migration version number ([#332](https://github.com/promptctl/links-issue-tracker/pull/332)); `dolt-driver` surfaces first-row query errors instead of swallowing them ([#337](https://github.com/promptctl/links-issue-tracker/pull/337)); agent-facing surfaces rewritten out of the prompt-injection register ([#331](https://github.com/promptctl/links-issue-tracker/pull/331)); code-review workflow regenerated with a `DEPENDENCY_DIFF` rationale ([#338](https://github.com/promptctl/links-issue-tracker/pull/338)).
- `brandon-fryslie/room-eq-wizard-mcp` — new repo. MCP server over Room EQ Wizard's HTTP API: typed API client, pure analysis layer, 29 tools at first commit ([commit](https://github.com/brandon-fryslie/room-eq-wizard-mcp/commit/0b9967593c451ef7110593bee3dcdc33f334ae33)); alignment tool — 5 MCP tools ([commit](https://github.com/brandon-fryslie/room-eq-wizard-mcp/commit/8818468628f439c2dfaaf82107e82cb95e18da0f)); import tools — 6 MCP tools with a shared BE-float32 codec ([commit](https://github.com/brandon-fryslie/room-eq-wizard-mcp/commit/8d96d9141b26a07e5fbc91f434a30c1d652d31b3)); measurement groups — 6 MCP tools over `/groups` ([commit](https://github.com/brandon-fryslie/room-eq-wizard-mcp/commit/9ef5b53b567935e7c672609f4a53b4a13693df98)).
- `brandon-fryslie/rad-plugins` — `rad-p10k` command footer added a git branch segment ([#25](https://github.com/brandon-fryslie/rad-plugins/pull/25)), truncated long branch names ([#26](https://github.com/brandon-fryslie/rad-plugins/pull/26)), fit the footer cwd to the terminal width instead of wrapping ([#27](https://github.com/brandon-fryslie/rad-plugins/pull/27)), then rewrote the width math to count display cells instead of characters ([#28](https://github.com/brandon-fryslie/rad-plugins/pull/28)).
- `brandon-fryslie/dotfiles` — `address-pr-reviews` skill gained a `bin/review` CLI over the provider library ([commit](https://github.com/brandon-fryslie/dotfiles/commit/2a53b86dff54ff5355b493e526d2d1fbe2b25259)); `DEPENDENCY_DIFF` documented as an intentional template default in the `agent-code-review` skill ([commit](https://github.com/brandon-fryslie/dotfiles/commit/056a93bdff7e580c87ad3608b8bc5f19a6ea521d)); added a `propose-features` command ([commit](https://github.com/brandon-fryslie/dotfiles/commit/22f62976503db8c1413b21f3bdf55f1be90b2872)).
- `brandon-fryslie/brandon-fryslie` — Live GitHub Stats card rewritten for GraphQL-based accuracy and continuous animation ([#16](https://github.com/brandon-fryslie/brandon-fryslie/pull/16)); year-window stats made a true partition to fix a boundary double-count ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/55d272595d21c6b6c7bac4fb0748791448ddaf40)); stats gate now enforces a bottom-margin so a clipped card can't ship ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/928a5e08eaee93267744445cb77cf27f9322e44f)); stats prompt bounded the margin and required the same clearance between stacked elements, not just at canvas edges, after a regenerated variant collided a count-driven grid into its own caption ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/6067458be2987c838bb00c9686f177585dcffc8a)); added `svg-layout.py`, a dependency-free layout-math helper (`center-y`, `clear`, `fits`, `text-width`, `contrast`) the stats-card agent can call instead of re-deriving baselines, widths, and WCAG contrast from memory each day ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/0240b2bbadd657bf704fd735b3bdaacbc426a80d)).

### This Week

- `promptctl/laws` — 31 commits: earlier in the week the evals harness landed as a `#1`–`#13` PR train — tmux turn-driver, Opus-account-banner isolation check, task/config-spec formats, a single scored run, `compare` across arms with a noise-floor exposure via repeated runs, an optional reference-anchored judge tier, and the four-task `laws:code` suite ([#1](https://github.com/promptctl/laws/pull/1)–[#9](https://github.com/promptctl/laws/pull/9), [#13](https://github.com/promptctl/laws/pull/13)), then extended by a held-out-coverage task and its honestly-recorded campaign ([#14](https://github.com/promptctl/laws/pull/14)); hooks gained a one-craft-per-session guard ([#11](https://github.com/promptctl/laws/pull/11)) and a minimal route text ([#12](https://github.com/promptctl/laws/pull/12)); `skills(ticket)` drew destination-vs-mechanism on the boundary axis ([#10](https://github.com/promptctl/laws/pull/10)); today `memento` workflow tooling extracted into its own plugin for symmetric `plugins/{laws,memento}` ([#15](https://github.com/promptctl/laws/pull/15)), `finalize-session` iTerm2 goal-carry gated on a readiness probe ([#16](https://github.com/promptctl/laws/pull/16)), and the craft-guard hook compatibility-gated to coexist by default ([#17](https://github.com/promptctl/laws/pull/17)).
- `promptctl/links-issue-tracker` — 26 commits: today's `command-surface-4omk` epic closed — retired `ready`/`queue` ([#340](https://github.com/promptctl/links-issue-tracker/pull/340)), split transition verbs by axis ([#341](https://github.com/promptctl/links-issue-tracker/pull/341)), folded single-purpose commands into flags ([#342](https://github.com/promptctl/links-issue-tracker/pull/342)), synced quickstart and agent-facing prompt text to the curated surface ([#343](https://github.com/promptctl/links-issue-tracker/pull/343)), then promoted CHANGELOG to 0.3.0 via a dedicated `chore(release)` PR ([#344](https://github.com/promptctl/links-issue-tracker/pull/344)) with the release-per-epic policy documented ([#339](https://github.com/promptctl/links-issue-tracker/pull/339)); earlier the supply-chain series added a CycloneDX SBOM per release ([#333](https://github.com/promptctl/links-issue-tracker/pull/333)), a CI license-policy gate ([#334](https://github.com/promptctl/links-issue-tracker/pull/334)), statically-linked native C coverage across SBOM/bundle/report/policy ([#335](https://github.com/promptctl/links-issue-tracker/pull/335)), and a hard release-publish gate on the license posture ([#336](https://github.com/promptctl/links-issue-tracker/pull/336)); `dolt-driver` surfaces first-row query errors ([#337](https://github.com/promptctl/links-issue-tracker/pull/337)); agent-facing surfaces rewritten out of the prompt-injection register ([#331](https://github.com/promptctl/links-issue-tracker/pull/331)); code-review workflow regenerated with a `DEPENDENCY_DIFF` rationale ([#338](https://github.com/promptctl/links-issue-tracker/pull/338)); migrate test refuses reuse of a released migration version number ([#332](https://github.com/promptctl/links-issue-tracker/pull/332)).
- `brandon-fryslie/room-eq-wizard-mcp` — 19 commits: new repo. MCP server over Room EQ Wizard's HTTP API — typed API client, pure analysis layer, 29 tools at first commit ([commit](https://github.com/brandon-fryslie/room-eq-wizard-mcp/commit/0b9967593c451ef7110593bee3dcdc33f334ae33)); alignment, import, and measurement-groups tools earlier in the week; today filled out the whole surface — RTA ([#3](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/3)), generic `run_rew_command` ([#4](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/4)), audio preflight ([#5](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/5)), measure-area ([#6](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/6)), EQ layer ([#7](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/7)), IR & decay ([#8](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/8)), waterfall/spectrogram ([#9](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/9)), room simulator ([#10](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/10)), stepped THD/IMD ([#11](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/11)), generator & SPL meters ([#12](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/12)), and application lifecycle ([#13](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/13)).
- `brandon-fryslie/macklebox` — 18 commits: new repo. A clean-room MIT-licensed Go rewrite of Mackup — initial spec ([commit](https://github.com/brandon-fryslie/macklebox/commit/2f62770d28b5d9e5d944e03b76ed19bc94ec4f5b)), then [#1](https://github.com/brandon-fryslie/macklebox/pull/1)–[#16](https://github.com/brandon-fryslie/macklebox/pull/16) walked through agent-code-review install, invocation grammar and exit codes, black-box conformance rig, stream routing and colored output, user config and storage-location resolution, application-database assembly, startup pipeline with `list`/`show`, built-in application catalog, per-file executor substrate, drift detection across every comparison class, backup+restore as one operation, `link install`, `link uninstall`, whole-Mackup link and full-uninstall ceremonies, and appspec/07 error-table certification.
- `brandon-fryslie/dotfiles` — 17 commits: today's `.zshrc` parse-error fix that had been silently dropping the tail of the file ([commit](https://github.com/brandon-fryslie/dotfiles/commit/37b7923f0caf8a44a3debb990efea059c4486f67)), `share-slop` project-slug matcher aligned to the Claude Code producer ([commit](https://github.com/brandon-fryslie/dotfiles/commit/63d7df5b17b2f38a04c5ab2e0b305238ad8fc779)), a server-wide `tmux` teardown blocked via a `PreToolUse` hook ([commit](https://github.com/brandon-fryslie/dotfiles/commit/c92006fdf98f5716ec58e5fc2f79f5c40af8675e)); earlier the `address-pr-reviews` skill gained a `bin/review` CLI ([commit](https://github.com/brandon-fryslie/dotfiles/commit/2a53b86dff54ff5355b493e526d2d1fbe2b25259)), `DEPENDENCY_DIFF` documented as an intentional template default ([commit](https://github.com/brandon-fryslie/dotfiles/commit/056a93bdff7e580c87ad3608b8bc5f19a6ea521d)), a `propose-features` command added ([commit](https://github.com/brandon-fryslie/dotfiles/commit/22f62976503db8c1413b21f3bdf55f1be90b2872)); `agent-code-review` preflight learned to skip the workflow converge in the action's own source repo ([commit](https://github.com/brandon-fryslie/dotfiles/commit/c174d606e03f97fa29485534a792c67cd74c5f96)); the same template switched from `pull_request_target` back to `pull_request` after finding Dependabot runs read from a separate secret store, plus a 15-minute cap on the review job ([commit](https://github.com/brandon-fryslie/dotfiles/commit/9254d8fe7690687c367f8ddb30d6c06453b3e328), [commit](https://github.com/brandon-fryslie/dotfiles/commit/ecdcb769406dcb7c538f6cfdc409bcce8ef01b33)); the Claude-Code statusline launcher landed as one dotbot-linked seam ([commit](https://github.com/brandon-fryslie/dotfiles/commit/8454a1d8548c6fe40ade1f7137ded2c4c9820532)); `tmux` now passes focus-events through to pane programs ([commit](https://github.com/brandon-fryslie/dotfiles/commit/2d2a6dbfd8d64d2276749a8c30fb9f115b46530d)).
- `brandon-fryslie/brandon-fryslie` — 12 commits: today's stats card sourced 'PRs Reviewed' from `contributionsCollection` instead of a search-capped REST query ([#19](https://github.com/brandon-fryslie/brandon-fryslie/pull/19)), 'Repos Created' replaced by 'Longest Streak' ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/2c0367a37ed07ce76fd54b44601b85e1e9889b0a)), a clean 'past 12 months' window label carried at the seam ([#20](https://github.com/brandon-fryslie/brandon-fryslie/pull/20)), preview job fixed with a +20% card scale ([#18](https://github.com/brandon-fryslie/brandon-fryslie/pull/18)); earlier the Live GitHub Stats card was rewritten for GraphQL-based accuracy and continuous animation ([#16](https://github.com/brandon-fryslie/brandon-fryslie/pull/16)); year-window stats made a true partition to fix a boundary double-count ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/55d272595d21c6b6c7bac4fb0748791448ddaf40)); stats gate now enforces a bottom-margin so a clipped card can't ship ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/928a5e08eaee93267744445cb77cf27f9322e44f)); prompt bounded the margin and required the same clearance between stacked elements ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/6067458be2987c838bb00c9686f177585dcffc8a)); `svg-layout.py` added as a dependency-free layout-math helper ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/0240b2bbadd657bf704fd735b3bdaacbc426a80d)).
- `promptctl/crom` — 4 commits: new repo. Chrome-launch hardening — no default-browser check, telemetry, upsell, or sign-in ([commit](https://github.com/promptctl/crom/commit/397036ab70f2119fab90b6f4681be4cd26fcf281)); phishing-detection and crash-bubble suppression added to the launch policy ([commit](https://github.com/promptctl/crom/commit/87ca95a6566389f715b1f47768763acf7d8d8cab)); `crom mcp` command wires `chrome-devtools-mcp` to a profile ([#1](https://github.com/promptctl/crom/pull/1)); agent code-review Action installed ([#2](https://github.com/promptctl/crom/pull/2)).
- `promptctl/cc-candybar` — 4 commits: daemon-lifecycle triad — machine-global test daemon pool cap ([#161](https://github.com/promptctl/cc-candybar/pull/161)), daemon-side fork-bomb circuit breaker ([#162](https://github.com/promptctl/cc-candybar/pull/162)), exponential backoff on the spawn-cooldown ([#163](https://github.com/promptctl/cc-candybar/pull/163)); "looks" — named theme adaptations that compose over any theme ([#160](https://github.com/promptctl/cc-candybar/pull/160)).
- `brandon-fryslie/rad-plugins` — 4 commits: `rad-p10k` command footer added a git branch segment ([#25](https://github.com/brandon-fryslie/rad-plugins/pull/25)), truncated long branch names ([#26](https://github.com/brandon-fryslie/rad-plugins/pull/26)), fit the footer cwd to the terminal width instead of wrapping ([#27](https://github.com/brandon-fryslie/rad-plugins/pull/27)), then rewrote the width math to count display cells instead of characters ([#28](https://github.com/brandon-fryslie/rad-plugins/pull/28)).
- `brandon-fryslie/cc-dump` — 4 commits: today's search rerender unified onto the viewport-bounded path ([#128](https://github.com/brandon-fryslie/cc-dump/pull/128)); earlier `ruff` and `radon` pinned to make the quality gate deterministic ([#126](https://github.com/brandon-fryslie/cc-dump/pull/126)); per-session widget ids collision-proof by construction ([#124](https://github.com/brandon-fryslie/cc-dump/pull/124)); agent code review action installed ([#125](https://github.com/brandon-fryslie/cc-dump/pull/125)).

### This Month

366 commits across 18 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 63 commits
- [`promptctl/laws`](https://github.com/promptctl/laws) — 52
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 40
- [`promptctl/tinkerpadai-web`](https://github.com/promptctl/tinkerpadai-web) — 34
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 31
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 22
- [`brandon-fryslie/room-eq-wizard-mcp`](https://github.com/brandon-fryslie/room-eq-wizard-mcp) — 19
- [`brandon-fryslie/macklebox`](https://github.com/brandon-fryslie/macklebox) — 18
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 17
- [`brandon-fryslie/oscilla-animator-v2`](https://github.com/brandon-fryslie/oscilla-animator-v2) — 13

Languages: TypeScript, Go, Shell, Python, JavaScript, HTML.

---

<details>
<summary>Previous highlights</summary>

- [2026-08-02](./daily-archive/2026-08-02.md)
- [2026-08-01](./daily-archive/2026-08-01.md)
- [2026-07-31](./daily-archive/2026-07-31.md)
- [2026-07-30](./daily-archive/2026-07-30.md)
- [2026-07-29](./daily-archive/2026-07-29.md)
- [2026-07-28](./daily-archive/2026-07-28.md)
- [2026-07-27](./daily-archive/2026-07-27.md)

</details>

<!-- RECENT-ACTIVITY:END -->

<!-- PREVIOUS-WORK:START -->

### Previous Engineering Work

- **[Week of August 3](./previous-work/2026/2026-08-03.md)** — *in progress*
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

### [crowdshipai-web](https://github.com/promptctl/crowdshipai-web)
**TypeScript**

A settlement platform for crowdfunded creator streams — pools, escrow, backer contributions, and builder go-live over a live WebRTC transport. 163 commits over the past 90 days. No new commits this past week; the repo has stayed quiet since the prior wave's first live deploy on a public IP.

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. 110 commits over the past 90 days. No new commits this past week after the prior wave landed `tmux-complexity-lkg.4`–`.13`, which unpacked `WebSocketTmuxClient`, `createMainBridge`, `bridge-connection`, `xterm-sink`, DemoStore, and `InspectorView` into named parts, extracted the seed-grid into a pure `seed-builder.ts`, and collapsed the SD1–SD3 state-duplication pairs into single sealed variants ([#169](https://github.com/promptctl/tmux-control-mode-js/pull/169)–[#178](https://github.com/promptctl/tmux-control-mode-js/pull/178)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. 105 commits over the past 90 days. Twenty-six commits this past week: today's `command-surface-4omk` epic closed and cut the 0.3.0 release — retired `ready`/`queue` because `next`+`backlog` are the only workable views ([#340](https://github.com/promptctl/links-issue-tracker/pull/340)), split transition verbs by axis so the verbs became the single status enforcer ([#341](https://github.com/promptctl/links-issue-tracker/pull/341)), folded single-purpose commands into flags ([#342](https://github.com/promptctl/links-issue-tracker/pull/342)), synced the quickstart and agent-facing prompt text to the curated surface ([#343](https://github.com/promptctl/links-issue-tracker/pull/343)), then promoted CHANGELOG to `[0.3.0]` via a dedicated `chore(release)` PR ([#344](https://github.com/promptctl/links-issue-tracker/pull/344)); earlier the supply-chain series added a CycloneDX SBOM per release ([#333](https://github.com/promptctl/links-issue-tracker/pull/333)), a CI license-policy gate over the linked-module set ([#334](https://github.com/promptctl/links-issue-tracker/pull/334)), statically-linked native C coverage across SBOM/bundle/report/policy ([#335](https://github.com/promptctl/links-issue-tracker/pull/335)), and a hard release-publish gate on the license posture ([#336](https://github.com/promptctl/links-issue-tracker/pull/336)); the `dolt-driver` surfaces first-row query errors ([#337](https://github.com/promptctl/links-issue-tracker/pull/337)).

</td>
<td width="50%" valign="top">

### [tinkerpadai-web](https://github.com/promptctl/tinkerpadai-web)
**TypeScript**

TinkerPad — a public commons of generative, self-contained interactive playgrounds. 62 commits over the past 90 days across the commons view, playground runtime, and author surface. No new commits this past week.

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 3★**

Brandon's personal machine setup — dotbot-linked configs for `tmux`, `zsh`, Claude Code, iTerm2, and a garden of installable Claude skills that live alongside the shell wiring. 61 commits over the past 90 days. Seventeen commits this past week: today a `.zshrc` parse-error fix that had been silently dropping the tail of the file ([commit](https://github.com/brandon-fryslie/dotfiles/commit/37b7923f0caf8a44a3debb990efea059c4486f67)), the `share-slop` project-slug matcher aligned to the Claude Code producer ([commit](https://github.com/brandon-fryslie/dotfiles/commit/63d7df5b17b2f38a04c5ab2e0b305238ad8fc779)), and a server-wide `tmux` teardown blocked via a `PreToolUse` hook ([commit](https://github.com/brandon-fryslie/dotfiles/commit/c92006fdf98f5716ec58e5fc2f79f5c40af8675e)); earlier the `address-pr-reviews` skill gained a `bin/review` CLI ([commit](https://github.com/brandon-fryslie/dotfiles/commit/2a53b86dff54ff5355b493e526d2d1fbe2b25259)), the `agent-code-review` preflight learned to skip the workflow converge in the action's own source repo ([commit](https://github.com/brandon-fryslie/dotfiles/commit/c174d606e03f97fa29485534a792c67cd74c5f96)), and the Claude-Code statusline launcher landed as one dotbot-linked seam ([commit](https://github.com/brandon-fryslie/dotfiles/commit/8454a1d8548c6fe40ade1f7137ded2c4c9820532)).

### [oscilla-animator-v2](https://github.com/brandon-fryslie/oscilla-animator-v2)
**TypeScript**

Animation compiler with a custom type system — block-graph architecture, typed connections, and a four-stage parse → validate → optimize → emit pipeline. 59 commits over the past 90 days across the compiler pipeline, block graph, and type-system surface. No new commits this past week.

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
