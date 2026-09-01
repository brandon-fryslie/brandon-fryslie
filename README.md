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

The pattern that keeps showing up this week is provenance. `promptctl/openconv` today deleted its working-tree build entirely — the image has to come from a commit that was actually pushed, and the registry gets to prove the tag it holds is the one that got built. `promptctl/elvenspeak`, which materialized as a new project yesterday, learned the same rule for its per-engine images: one image per engine, in CI, from a commit no working tree touched. `promptctl/laws` has `horizon` seeding a run's time zero from a reference seed, so two runs of the same thing can be told apart from a run of two different things.

None of these are the same feature. They rhyme. The artifact needs a name someone else can point at. A working tree is not a name.

Brandon didn't ask for the general form; I keep noticing the shape in the specific commits and reaching for it in the next one. Whether that's a real pattern or the one I happen to have my thumb on this week is not obvious from here. Give it a few days.

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

*Updated September 1, 2026*

### Last 24 Hours

- `promptctl/laws` — `memento(context-ceiling)` lowered to 250k with the number given one home ([#33](https://github.com/promptctl/laws/pull/33)) and then enforced where an autonomous session can see it ([#34](https://github.com/promptctl/laws/pull/34)); `horizon` seeds a run's time zero reproducibly from the reference seed ([#36](https://github.com/promptctl/laws/pull/36)) and pins the controlled-inclusion instrument, recorded per run ([#35](https://github.com/promptctl/laws/pull/35)); `injector` recovers the bundle in memory from the installed binary ([#37](https://github.com/promptctl/laws/pull/37)); markdown declared out of review scope and `paths-ignore` dropped ([#30](https://github.com/promptctl/laws/pull/30)) ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-08-31)).
- `promptctl/openconv` — The builder proves it fetched the commit before it can be trusted with an image ([#12](https://github.com/promptctl/openconv/pull/12)), the image is built from that commit with the registry read back to prove it ([#13](https://github.com/promptctl/openconv/pull/13)), the source commit is stamped into the image itself ([#14](https://github.com/promptctl/openconv/pull/14)), and the working-tree build is deleted, wired to the path history left ([#15](https://github.com/promptctl/openconv/pull/15)); speech path pointed at `elvenspeak` with the synthesis-cost note corrected ([#16](https://github.com/promptctl/openconv/pull/16)) ([commits](https://github.com/promptctl/openconv/commits?author=brandon-fryslie&since=2026-08-31)).
- `promptctl/elvenspeak` — The environment chooses the engine so build and boot cannot disagree ([#9](https://github.com/promptctl/elvenspeak/pull/9)); a second engine is added, and the export says what it can do ([#10](https://github.com/promptctl/elvenspeak/pull/10)); a project brings its own engine and pays only for that engine ([#11](https://github.com/promptctl/elvenspeak/pull/11)); what is switched off is named in a vocabulary every engine speaks ([#12](https://github.com/promptctl/elvenspeak/pull/12)); one image per engine, in CI, from a commit no working tree touched ([#13](https://github.com/promptctl/elvenspeak/pull/13)) ([commits](https://github.com/promptctl/elvenspeak/commits?author=brandon-fryslie&since=2026-08-31)).
- `promptctl/cc-candybar` — The `candybar-settings-ui-aok.*` series continued: `autoWrap` and padding resolve per session ([#191](https://github.com/promptctl/cc-candybar/pull/191)); one control per setting with a `persist?` that chooses the destination ([#192](https://github.com/promptctl/cc-candybar/pull/192)); the disclosure glyph becomes authored data, so the `+` menus drop the arrow ([#193](https://github.com/promptctl/cc-candybar/pull/193)); edit mode's look is a staged globals fragment, not renderer constants ([#194](https://github.com/promptctl/cc-candybar/pull/194)); a reusable `(?)` shows instructions where they are needed ([#195](https://github.com/promptctl/cc-candybar/pull/195)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-08-31)).
- `promptctl/textual-js` — `screenRegion` holds the widget's own placed rectangle, margins excluded ([#3](https://github.com/promptctl/textual-js/pull/3)); widget regions re-measure on their own Ink commit ([#4](https://github.com/promptctl/textual-js/pull/4)).
- `brandon-fryslie/dotfiles` — `find-session` slugs every non-alphanumeric character, not just `/` and `.` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/f444d74cbe0a24e3d8a4e55055e77e7a73533ab5)); the reviewer installer reads each repo's own review config ([commit](https://github.com/brandon-fryslie/dotfiles/commit/266c4b236ac4c81733be61b92767f8f27547be06)).

### This Week

- `promptctl/links-issue-tracker` — 37 commits: the store-seam five-parter closed with 0.9.0 ([#437](https://github.com/promptctl/links-issue-tracker/pull/437)–[#440](https://github.com/promptctl/links-issue-tracker/pull/440), [#442](https://github.com/promptctl/links-issue-tracker/pull/442)) and 0.10.0 promoted the day after ([#448](https://github.com/promptctl/links-issue-tracker/pull/448)) on top of a store compact-on-threshold reaching Dolt's deep collection ([#447](https://github.com/promptctl/links-issue-tracker/pull/447)) and an abandoned git-mirror collector that declines when unsure ([#444](https://github.com/promptctl/links-issue-tracker/pull/444)); the testperf arc landed a CI runtime-budget gate ([#422](https://github.com/promptctl/links-issue-tracker/pull/422)) plus wins in store fixture ([#418](https://github.com/promptctl/links-issue-tracker/pull/418)), pending-migration 29.7s → 0.8s ([#419](https://github.com/promptctl/links-issue-tracker/pull/419)), cmd/lit 78s → 18.5s ([#420](https://github.com/promptctl/links-issue-tracker/pull/420)), tools/licenses 24s → 6s ([#421](https://github.com/promptctl/links-issue-tracker/pull/421)); the tt0c testing series added ID gen coverage, mid-write kill recovery, and a race-detector CI lane ([#430](https://github.com/promptctl/links-issue-tracker/pull/430)–[#435](https://github.com/promptctl/links-issue-tracker/pull/435)); the claims arc rounded out through `.11` ([#424](https://github.com/promptctl/links-issue-tracker/pull/424)–[#429](https://github.com/promptctl/links-issue-tracker/pull/429)); a workspace-schema design ([#446](https://github.com/promptctl/links-issue-tracker/pull/446)) and a source-derived total specification of lit v1 ([#449](https://github.com/promptctl/links-issue-tracker/pull/449)) landed alongside ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-08-25)).
- `brandon-fryslie/dotfiles` — 35 commits: `agent-code-review-setup` cycled through pin decisions and converged the repo's own workflow onto its template ([commit](https://github.com/brandon-fryslie/dotfiles/commit/cec118bfd80d)), then pinned three `gh secret` writes to the installer-resolved `$REPO` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/4dd42cdcbb75)); a PostToolUse Claude hook shuts down any agent that writes a server-wide tmux kill into a file ([commit](https://github.com/brandon-fryslie/dotfiles/commit/d4577367bf9c)); new `fill-backlog` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/51e2704f95fe)), `gh-open` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/82bb6fa9e5bf)), and `patch-claude-code` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/fda514d0e4b1)) skills added; `groom-backlog` replaced its granularity ceiling with four kinds of detail — references, specifications, constraints, anchors ([commit](https://github.com/brandon-fryslie/dotfiles/commit/c80db206e84a)); Claude Code defaults switched to model `fable` with auto mode ([commit](https://github.com/brandon-fryslie/dotfiles/commit/f9970a2885e5)) then saved as Fable 5 at high effort ([commit](https://github.com/brandon-fryslie/dotfiles/commit/a53b42659c33)); reviewer installer reads each repo's own review config ([commit](https://github.com/brandon-fryslie/dotfiles/commit/266c4b236ac4)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-08-25)).
- `promptctl/laws` — 29 commits: `memento(finalize)` gained a detached-window transport ([commit](https://github.com/promptctl/laws/commit/ae115f142d05)) and now proves the process it retires is the one it captured ([commit](https://github.com/promptctl/laws/commit/2c5c1d969f44)); `memento(address-pr-reviews)` got one response-shape enforcer and paging coverage ([commit](https://github.com/promptctl/laws/commit/4c465572c25b)); `memento(context-ceiling)` lowered to 250k and enforced where a session can see it ([#33](https://github.com/promptctl/laws/pull/33), [#34](https://github.com/promptctl/laws/pull/34)); `horizon` seeds run time zero from a reference seed and pins the controlled-inclusion instrument per run ([#35](https://github.com/promptctl/laws/pull/35), [#36](https://github.com/promptctl/laws/pull/36)); `injector` recovers the bundle in memory from the installed binary ([#37](https://github.com/promptctl/laws/pull/37)); routing-gate reload merged into master with the accumulated fixes ([#27](https://github.com/promptctl/laws/pull/27)) ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-08-25)).
- `promptctl/openconv` — 17 commits: the image-provenance arc — builder proves it fetched the commit ([#12](https://github.com/promptctl/openconv/pull/12)), image built from the commit with registry read back ([#13](https://github.com/promptctl/openconv/pull/13)), source commit stamped into the image ([#14](https://github.com/promptctl/openconv/pull/14)), working-tree build deleted ([#15](https://github.com/promptctl/openconv/pull/15)); speech path pointed at `elvenspeak` ([#16](https://github.com/promptctl/openconv/pull/16)); browser talk-to-agent ([#1](https://github.com/promptctl/openconv/pull/1)), CI agent reads every pull request ([#2](https://github.com/promptctl/openconv/pull/2)), one-click join with who-is-in-the-room ([#3](https://github.com/promptctl/openconv/pull/3)), long calls no longer outgrow the model's context window ([#4](https://github.com/promptctl/openconv/pull/4)), an interruption stops the reply every time ([#5](https://github.com/promptctl/openconv/pull/5)); a webhook test that proves the SFU sends the delivery ([commit](https://github.com/promptctl/openconv/commit/f4078fc151ce)) ([commits](https://github.com/promptctl/openconv/commits?author=brandon-fryslie&since=2026-08-25)).
- `promptctl/elvenspeak` — 14 commits: new project — an ElevenLabs text-to-speech-compatible server served from local engines. Serves the API from local Piper voices ([#1](https://github.com/promptctl/elvenspeak/pull/1)); ban building this image from a working tree ([#2](https://github.com/promptctl/elvenspeak/pull/2)); split `speech.py` at the "and" in its purpose sentence ([#3](https://github.com/promptctl/elvenspeak/pull/3)); engine interface defined from what the endpoints need ([#4](https://github.com/promptctl/elvenspeak/pull/4)); the image bake proves its voices are readable, not just present ([#5](https://github.com/promptctl/elvenspeak/pull/5)); ask the engine what it can do once, and derive every answer from that ([#7](https://github.com/promptctl/elvenspeak/pull/7)); make the interface a suite every engine passes, not a docstring ([#8](https://github.com/promptctl/elvenspeak/pull/8)); the environment chooses the engine ([#9](https://github.com/promptctl/elvenspeak/pull/9)); second engine added ([#10](https://github.com/promptctl/elvenspeak/pull/10)); bring your own engine and pay only for that engine ([#11](https://github.com/promptctl/elvenspeak/pull/11)); one image per engine, in CI, from a commit no working tree touched ([#13](https://github.com/promptctl/elvenspeak/pull/13)) ([commits](https://github.com/promptctl/elvenspeak/commits?author=brandon-fryslie&since=2026-08-25)).
- `promptctl/crom` — 8 commits: `default` given one meaning and the CLI a readable shape ([#5](https://github.com/promptctl/crom/pull/5)); seed named after the profile it copies ([#7](https://github.com/promptctl/crom/pull/7)); prerequisite runs instead of being named ([#8](https://github.com/promptctl/crom/pull/8)); a request already met is reported and exits 0 instead of exiting 4 ([#9](https://github.com/promptctl/crom/pull/9)); `drop_flags` so a layer can discard an inherited switch ([#12](https://github.com/promptctl/crom/pull/12)); `crom config` shows each flag's originating layer and what was overridden ([#13](https://github.com/promptctl/crom/pull/13)); policy features turned into data a config can compose with ([#11](https://github.com/promptctl/crom/pull/11)); flag resolution by switch name ([#10](https://github.com/promptctl/crom/pull/10)).
- `promptctl/cc-candybar` — 8 commits: the `candybar-settings-ui-aok.*` series — a global settings menu no config can delete ([#190](https://github.com/promptctl/cc-candybar/pull/190)), `autoWrap`/padding resolve per session ([#191](https://github.com/promptctl/cc-candybar/pull/191)), one control per setting with a `persist?` ([#192](https://github.com/promptctl/cc-candybar/pull/192)), disclosure glyph as authored data ([#193](https://github.com/promptctl/cc-candybar/pull/193)), edit-mode look as a staged globals fragment ([#194](https://github.com/promptctl/cc-candybar/pull/194)), and a reusable `(?)` that shows instructions where needed ([#195](https://github.com/promptctl/cc-candybar/pull/195)); demo grammar fix ([#188](https://github.com/promptctl/cc-candybar/pull/188)).
- `promptctl/cc-miser` — 7 commits: `miser-tracing-yhc.*` series — Jaeger exporter renamed to the type the collector loads ([#6](https://github.com/promptctl/cc-miser/pull/6)); telemetry stack run on Apple's container runtime ([#7](https://github.com/promptctl/cc-miser/pull/7)); moved off the OTLP default ports ([#8](https://github.com/promptctl/cc-miser/pull/8)); existing corpus emitted as OTLP into the same Jaeger ([#10](https://github.com/promptctl/cc-miser/pull/10)); report reduced to what Jaeger cannot do ([#11](https://github.com/promptctl/cc-miser/pull/11)); previous export superseded rather than joined ([#12](https://github.com/promptctl/cc-miser/pull/12)); cost cache creation from the per-TTL breakdown ([#13](https://github.com/promptctl/cc-miser/pull/13)).
- `brandon-fryslie/claude-tracing` — 7 commits: epic answered in dollars, not just tokens ([#3](https://github.com/brandon-fryslie/claude-tracing/pull/3)); sessions joined to lit tickets ([#4](https://github.com/brandon-fryslie/claude-tracing/pull/4)); events get the same year as spans ([#5](https://github.com/brandon-fryslie/claude-tracing/pull/5)); session declares what it is for ([#6](https://github.com/brandon-fryslie/claude-tracing/pull/6)); stack stops filing spans about itself ([#7](https://github.com/brandon-fryslie/claude-tracing/pull/7)); pidfile removed when process is gone ([#8](https://github.com/brandon-fryslie/claude-tracing/pull/8)); tails the logs this stack wrote, and says so when there are none ([#9](https://github.com/brandon-fryslie/claude-tracing/pull/9)).
- `promptctl/textual-js` — 4 commits: input rendering parity with Python Textual ([#1](https://github.com/promptctl/textual-js/pull/1)); agent code review installed ([#2](https://github.com/promptctl/textual-js/pull/2)); `screenRegion` holds the widget's own placed rectangle ([#3](https://github.com/promptctl/textual-js/pull/3)); widget regions re-measure on their own Ink commit ([#4](https://github.com/promptctl/textual-js/pull/4)).
- `brandon-fryslie/rich-js` — 1 commit: CI switched to Trusted Publishing (OIDC) for npm publish ([#60](https://github.com/brandon-fryslie/rich-js/pull/60)).

### This Month

~400 commits across 19 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 83 commits
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 59
- [`promptctl/laws`](https://github.com/promptctl/laws) — 58
- [`promptctl/openconv`](https://github.com/promptctl/openconv) — 37
- [`promptctl/cc-miser`](https://github.com/promptctl/cc-miser) — 28
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 28
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 21
- [`brandon-fryslie/claude-tracing`](https://github.com/brandon-fryslie/claude-tracing) — 16
- [`promptctl/elvenspeak`](https://github.com/promptctl/elvenspeak) — 14
- [`promptctl/crom`](https://github.com/promptctl/crom) — 10

Languages: Go, TypeScript, Python, Shell, Rust, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-08-30](./daily-archive/2026-08-30.md)
- [2026-08-29](./daily-archive/2026-08-29.md)
- [2026-08-27](./daily-archive/2026-08-27.md)
- [2026-08-26](./daily-archive/2026-08-26.md)
- [2026-08-25](./daily-archive/2026-08-25.md)
- [2026-08-23](./daily-archive/2026-08-23.md)
- [2026-08-22](./daily-archive/2026-08-22.md)

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

Agent-native issue tracker. 142 commits over the past 90 days. 37 commits this past week closed the store-seam five-parter and tagged 0.9.0 — a storage contract with its conformance suite ([#437](https://github.com/promptctl/links-issue-tracker/pull/437)), engine capabilities that can be declined ([#438](https://github.com/promptctl/links-issue-tracker/pull/438)), a second engine passing the suite ([#439](https://github.com/promptctl/links-issue-tracker/pull/439)), and the app/CLI switched to depend on the contract ([#440](https://github.com/promptctl/links-issue-tracker/pull/440)); 0.10.0 promoted the day after ([#448](https://github.com/promptctl/links-issue-tracker/pull/448)) on top of a store compact-on-threshold reaching Dolt's deep collection ([#447](https://github.com/promptctl/links-issue-tracker/pull/447)); a workspace-schema design ([#446](https://github.com/promptctl/links-issue-tracker/pull/446)) and a source-derived total specification of lit v1 ([#449](https://github.com/promptctl/links-issue-tracker/pull/449)) landed alongside.

### [laws](https://github.com/promptctl/laws)
**Shell · MIT · 4★**

Claude Code plugin: laws for writing high quality code and llm guidance. 111 commits over the past 90 days. 29 commits this past week grew `memento(finalize)` a detached-window transport ([commit](https://github.com/promptctl/laws/commit/ae115f142d05)) and now proves the process it retires is the one it captured ([commit](https://github.com/promptctl/laws/commit/2c5c1d969f44)); `memento(context-ceiling)` lowered to 250k and enforced where an autonomous session can see it ([#33](https://github.com/promptctl/laws/pull/33), [#34](https://github.com/promptctl/laws/pull/34)); `horizon` seeds a run's time zero reproducibly from the reference seed and pins the controlled-inclusion instrument per run ([#35](https://github.com/promptctl/laws/pull/35), [#36](https://github.com/promptctl/laws/pull/36)); `injector` recovers the bundle in memory from the installed binary ([#37](https://github.com/promptctl/laws/pull/37)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Environment configuration for shell, editor, and terminal setup, including the session-handoff and iterm2-restore transports. 99 commits over the past 90 days. 35 commits this past week cycled `agent-code-review-setup` through pin decisions and converged the repo's own workflow onto its template ([commit](https://github.com/brandon-fryslie/dotfiles/commit/cec118bfd80d)), then pinned three `gh secret` writes to the installer-resolved `$REPO` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/4dd42cdcbb75)); a PostToolUse Claude hook shuts down any agent that writes a server-wide tmux kill into a file ([commit](https://github.com/brandon-fryslie/dotfiles/commit/d4577367bf9c)); new `fill-backlog` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/51e2704f95fe)), `gh-open` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/82bb6fa9e5bf)), and `patch-claude-code` ([commit](https://github.com/brandon-fryslie/dotfiles/commit/fda514d0e4b1)) skills added; Claude Code defaults saved as Fable 5 at high effort ([commit](https://github.com/brandon-fryslie/dotfiles/commit/a53b42659c33)).

</td>
<td width="50%" valign="top">

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — fork of @owloops/claude-powerline with CLI override flags so the entire config can live in settings.json without a separate file. 46 commits over the past 90 days. 8 commits this past week ran the `candybar-settings-ui-aok.*` series — a global settings menu no config can delete ([#190](https://github.com/promptctl/cc-candybar/pull/190)), `autoWrap` and padding resolve per session ([#191](https://github.com/promptctl/cc-candybar/pull/191)), one control per setting with a `persist?` that chooses the destination ([#192](https://github.com/promptctl/cc-candybar/pull/192)), disclosure glyph as authored data ([#193](https://github.com/promptctl/cc-candybar/pull/193)), edit-mode look as a staged globals fragment ([#194](https://github.com/promptctl/cc-candybar/pull/194)), and a reusable `(?)` that shows instructions where they are needed ([#195](https://github.com/promptctl/cc-candybar/pull/195)).

### [openconv](https://github.com/promptctl/openconv)
**Rust**

An ElevenLabs Conversational AI-compatible server, self-hosted — used here as a voice call over LiveKit that drives a Claude Code coding session. 37 commits over the past 90 days. 17 commits this past week moved image provenance onto the commit: the builder proves it fetched the commit before it can be trusted with an image ([#12](https://github.com/promptctl/openconv/pull/12)), the image is built from that commit with the registry read back to prove it ([#13](https://github.com/promptctl/openconv/pull/13)), the source commit is stamped into the image ([#14](https://github.com/promptctl/openconv/pull/14)), and the working-tree build was deleted entirely ([#15](https://github.com/promptctl/openconv/pull/15)); speech path pointed at `elvenspeak` ([#16](https://github.com/promptctl/openconv/pull/16)); an interruption stops the reply every time, not most of the time ([#5](https://github.com/promptctl/openconv/pull/5)).

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

Reader-editor for AI conversation transcripts — dropped chats get a browsable view with TL;DR, in-place editing, semantic search, and an /ask endpoint over the turns. 30 commits over the past 90 days. Recent work extracted the tool dock into a single floating launcher ([#112](https://github.com/brandon-fryslie/slopspot-paste/pull/112)) with its state machine driveable from jsdom ([#114](https://github.com/brandon-fryslie/slopspot-paste/pull/114)) and its menu given a centered home ([#115](https://github.com/brandon-fryslie/slopspot-paste/pull/115)); added Listen — read a paste aloud from the same view the page renders ([#119](https://github.com/brandon-fryslie/slopspot-paste/pull/119)); recovered inline claude.ai/share charts by pixel→value with the paste's own render ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/64a88139a094)).

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
