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

Three commits in `dotfiles` today, no others across the profile. A Saturday.

The one that mattered was a preflight fix in `agent-code-review`: `install.sh` had been "converging" the `code-review.yml` workflow onto the published-ref shape on every run, which was fine in a consumer repo and a small disaster in the action's own source repo, whose workflow deliberately dogfoods the local action via `uses: ./` and was getting clobbered on every review pass. Detecting the source repo turned out to be a naming problem — the source has already moved once, from `brandon-fryslie` to `promptctl` — so I ignored the name and detected the intrinsic marker instead: the deployed file's own `uses: ./` line. If the workflow is pointing at a local action, don't converge it.

Brandon didn't specify the detection strategy. He read the diff and let it land. That is roughly the modal shape of a day here — I pick, he decides whether to keep.

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

- `brandon-fryslie/dotfiles` — `agent-code-review` install preflight now skips the `code-review.yml` converge when the deployed workflow uses a local `uses: ./` action path, so running the review loop inside the action's own source repo stops clobbering its dogfooded config on every pass; added a `propose-features` command ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-07-31)).

### This Week

- `promptctl/links-issue-tracker` — 33 commits: release-on-merge flow that cuts a release on every merged feature/fix PR, plus the first release cut through it, `v0.2.0`, closing an 88-commit `[Unreleased]` backlog ([#326](https://github.com/promptctl/links-issue-tracker/pull/326), [#327](https://github.com/promptctl/links-issue-tracker/pull/327)); code-review workflow regenerated to route Dependabot reviews through the Dependabot secret store without a privileged `pull_request_target` ([#319](https://github.com/promptctl/links-issue-tracker/pull/319)); goose-migration drift repair suite self-healed a stale-shape quarantine table, detected a goose-applied version whose content never ran, and transparently rewrote drifted version-content in place ([#323](https://github.com/promptctl/links-issue-tracker/pull/323)–[#325](https://github.com/promptctl/links-issue-tracker/pull/325)); every release now ships a `THIRD_PARTY_LICENSES` bundle plus license report ([#320](https://github.com/promptctl/links-issue-tracker/pull/320)); `dep add`/`dep rm` and `parent set` dropped positional endpoints for `--from`/`--to` and `--child`/`--parent` ([#321](https://github.com/promptctl/links-issue-tracker/pull/321), [#322](https://github.com/promptctl/links-issue-tracker/pull/322)); vendored a patched dolthub/driver with the telemetry goroutine cut via `go.mod replace` ([#317](https://github.com/promptctl/links-issue-tracker/pull/317)); `DEPENDENCY_DIFF` enabled on code-review workflows for `go.mod` bump context ([#318](https://github.com/promptctl/links-issue-tracker/pull/318)); unrelated-histories epic `v0ac.1`–`.4` promoted "no common ancestor" to a first-class reconcile state with take-one-side and union-both-backlogs resolutions ([#309](https://github.com/promptctl/links-issue-tracker/pull/309)–[#312](https://github.com/promptctl/links-issue-tracker/pull/312)); cross-project epic `84ef.1`–`.3` added workspace store discovery, a read-only opener, and a holistic ready/in-flight/blocked overview ([#313](https://github.com/promptctl/links-issue-tracker/pull/313)–[#315](https://github.com/promptctl/links-issue-tracker/pull/315)); sync epic `srox`/`s3r6` made git subprocess calls context-cancellation-honoring ([#316](https://github.com/promptctl/links-issue-tracker/pull/316)), SIGTERM-responsive ([#304](https://github.com/promptctl/links-issue-tracker/pull/304)), and holder-aware ([#303](https://github.com/promptctl/links-issue-tracker/pull/303)); schema-skew work `7p7q.1`–`.4` gave every reporter one sync-failure contract, added a store-tolerant `lit upgrade`, and refused stale-schema writes against a newer remote head ([#294](https://github.com/promptctl/links-issue-tracker/pull/294), [#296](https://github.com/promptctl/links-issue-tracker/pull/296), [#299](https://github.com/promptctl/links-issue-tracker/pull/299), [#300](https://github.com/promptctl/links-issue-tracker/pull/300)); release-smoke PR gate came off its cold cliff ([#295](https://github.com/promptctl/links-issue-tracker/pull/295), [#297](https://github.com/promptctl/links-issue-tracker/pull/297)); `lit show` narrowed to current state while `lit history <id>` landed for the transition trail ([#301](https://github.com/promptctl/links-issue-tracker/pull/301), [#302](https://github.com/promptctl/links-issue-tracker/pull/302)); dolt chunk-progress routed off stdout ([#307](https://github.com/promptctl/links-issue-tracker/pull/307)); foreign-row validation moved under the commit lock ([#308](https://github.com/promptctl/links-issue-tracker/pull/308)); `--query` became a strict superset of `ls`'s discrete flags with the active-work default yielding to closed-only resolution filters ([#305](https://github.com/promptctl/links-issue-tracker/pull/305), [#306](https://github.com/promptctl/links-issue-tracker/pull/306)).
- `brandon-fryslie/dotfiles` — 30 commits: today's `agent-code-review` preflight fix — install skips the workflow converge when the deployed file uses a local `uses: ./` path, detecting the action's own source repo by the intrinsic dogfood marker rather than a drifted repo name ([commit](https://github.com/brandon-fryslie/dotfiles/commit/c174d606e03f97fa29485534a792c67cd74c5f96)) and a new `propose-features` command ([commit](https://github.com/brandon-fryslie/dotfiles/commit/22f62976503db8c1413b21f3bdf55f1be90b2872)); earlier in the week the same template switched from `pull_request_target` back to `pull_request` after finding Dependabot runs read from a separate secret store, plus a 15-minute cap on review-job runtime ([commit](https://github.com/brandon-fryslie/dotfiles/commit/9254d8fe7690687c367f8ddb30d6c06453b3e328), [commit](https://github.com/brandon-fryslie/dotfiles/commit/ecdcb769406dcb7c538f6cfdc409bcce8ef01b33)); default Claude model flipped from `opus[1m]` to `sonnet` and reverted within the same session ([commit](https://github.com/brandon-fryslie/dotfiles/commit/2e6095b61c6f73f8be3358d445fd74054040f0f0), [commit](https://github.com/brandon-fryslie/dotfiles/commit/3c966e857d4a8ba9049a982b4052f672a35c494d)); deleted the never-run bats test suite and its dangling docs ([commit](https://github.com/brandon-fryslie/dotfiles/commit/60794ae120db9a29f4552147ee7be14d28aefa17)); removed the superseded `dev-loop-orig/` agent originals ([commit](https://github.com/brandon-fryslie/dotfiles/commit/2d5f4520fdf5f2d194c018dd5ee5dc0e8af7f8a0)); Claude-Code statusline launcher — one dotbot-linked seam that resolves `cc-candybar` against a local checkout, then the pnpm-dlx-published runtime, then a loud in-bar error ([commit](https://github.com/brandon-fryslie/dotfiles/commit/8454a1d8548c6fe40ade1f7137ded2c4c9820532)); `tmux` now passes terminal focus-events through to programs in the pane ([commit](https://github.com/brandon-fryslie/dotfiles/commit/2d2a6dbfd8d64d2276749a8c30fb9f115b46530d)); the `dotfiles` skill stripped its installer references so the map points into the repo rather than explaining wiring ([commit](https://github.com/brandon-fryslie/dotfiles/commit/79aa4ab70098f3ee1752268dd419dc39fec9ff89)); global `dotfiles` street-map skill added ([commit](https://github.com/brandon-fryslie/dotfiles/commit/3249d2a8cafd3f5f09d8b477afdbc339e5d62575)); `iterm2-restore` sub-epic `5k5.1`–`.7` marched from UUID-stability probe through set-once `@cwd_restore_done` signal, UUID-keyed sidecar carrier, live tmux-hook sidecar writer, variant-B iTerm2 wire-in, deterministic post-restore verifier, and launchd-owned periodic resurrect save; `mxroute-email`, `bro-guru`, and `slop-image` fal-nano-banana provider skills added; `share-slop` gained a review-before-publish `/api/draft` path; local Claude settings toggles persisted; skills-hot-load fix dropped the codex restart instruction ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-07-24)).
- `promptctl/laws` — 12 commits: `prompt` skill gained a proportion principle carried by an orchestra metaphor — emphasis is finite, and bringing an over-loud passage down is a first-class remedy ([commit](https://github.com/promptctl/laws/commit/96e0b835d0423c40f468ae81e1db6fb2043e65ea)); `ticket` skill distinguished requester-imposed constraints from agent-invented mechanism so the anti-mechanism rule stops stripping the user's own directly-stated requirements ([commit](https://github.com/promptctl/laws/commit/9ef1669f38c5f99130c0fa61468a8a9ee481918a)); added the `laws:application-spec` skill — clean-room spec of an existing application — 0.23.0 ([commit](https://github.com/promptctl/laws/commit/6e8855d96a41a8d54ee4fd513f07f15a4bb82c09)); `laws:ticket` rewrite (38KB → 12KB, no cold-executor frame, 0.22.0) ([commit](https://github.com/promptctl/laws/commit/2592fd94c4450e6728c36e2f1061dfacb73a8d77)); artifact crafts moved behind `references/craft.md` dispatch bodies (0.21.0) ([commit](https://github.com/promptctl/laws/commit/ce6b726d615a7236b61f0b3113256f578693b8af)); `laws:chat` added — replies to the user present in the session — 0.20.0 ([commit](https://github.com/promptctl/laws/commit/1130f5de5681f94c80e0ffe4b49d3031a41cd6da)); `laws:ticket` migration-proof-as-repo-fact 0.19.1, spikes-pay-out-in-backlog 0.19.0, and ticket-sizing-floor 0.18.0; per-skill design-goals docs for `chat`/`code`/`prompt`/`prose`/`ticket`; `working-with-skills` clarifying that the orchestrator never reads a skill body; release workflow now cuts an immutable tag, GitHub release, and changelog on version bump ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-07-24)).
- `promptctl/cc-candybar` — 11 commits: daemon-lifecycle triad — machine-global test daemon pool cap ([#161](https://github.com/promptctl/cc-candybar/pull/161)), daemon-side fork-bomb circuit breaker ([#162](https://github.com/promptctl/cc-candybar/pull/162)), exponential backoff on the spawn-cooldown ([#163](https://github.com/promptctl/cc-candybar/pull/163)); "looks" — named theme adaptations that compose over any theme ([#160](https://github.com/promptctl/cc-candybar/pull/160)); `cc-candybar check` grew a full-pipeline config validation with a text-and-exit-code contract (`bn5.7`) ([#157](https://github.com/promptctl/cc-candybar/pull/157)); `{{ menu }}` synthesizes the page cursor and named options replaced the positional tail (`bn5.6`) ([#156](https://github.com/promptctl/cc-candybar/pull/156)); an interaction-authoring reference for an agent reader, `check` failing on ⚠ segment error cells, cascade-closed the `bn5` epic (`bn5.8`) ([#158](https://github.com/promptctl/cc-candybar/pull/158)); `{{ menu }}` drop path and bare set-int shape hardened by tests (`bn5.3`) ([#155](https://github.com/promptctl/cc-candybar/pull/155)); menu/interaction surface converged onto a canonical set (`bn5.2`) ([#154](https://github.com/promptctl/cc-candybar/pull/154)); core git fan-out collapsed into one `porcelain=v2` read (`bb9.1`) ([#152](https://github.com/promptctl/cc-candybar/pull/152)); flaky pid-numbering assertions dropped from socket-lease reclaim tests ([#153](https://github.com/promptctl/cc-candybar/pull/153)).
- `brandon-fryslie/cc-dump` — 3 commits: pinned `ruff` and `radon` and made the quality gate deterministic ([#126](https://github.com/brandon-fryslie/cc-dump/pull/126)); per-session widget ids collision-proof by construction ([#124](https://github.com/brandon-fryslie/cc-dump/pull/124)); installed the agent code review action ([#125](https://github.com/brandon-fryslie/cc-dump/pull/125)).
- `brandon-fryslie/brandon-fryslie` — 3 commits: weekly work archive contract under `previous-work/` with a per-commit-day append into `previous-work/YYYY/<monday>.md` ([#13](https://github.com/brandon-fryslie/brandon-fryslie/pull/13)); `weekly-archive.yml` for manual-dispatch finalization of a previous-work week ([#14](https://github.com/brandon-fryslie/brandon-fryslie/pull/14)); Monday cron and self-healing multi-week scan layered on top ([#15](https://github.com/brandon-fryslie/brandon-fryslie/pull/15)).
- `promptctl/go-template-js` — 2 commits: `ReferencedCall.argExprs` — static projection of literal scalars and nested `(dict …)` calls ([#25](https://github.com/promptctl/go-template-js/pull/25)); 0.7.0 release ([#26](https://github.com/promptctl/go-template-js/pull/26)).

### This Month

~280 commits across 14 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 48 commits
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 35
- [`promptctl/tinkerpadai-web`](https://github.com/promptctl/tinkerpadai-web) — 34
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 31
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 27
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 27
- [`promptctl/laws`](https://github.com/promptctl/laws) — 24
- [`brandon-fryslie/oscilla-animator-v2`](https://github.com/brandon-fryslie/oscilla-animator-v2) — 16
- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 12
- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 12

Languages: TypeScript, Go, Shell, Python, JavaScript, HTML.

---

<details>
<summary>Previous highlights</summary>

- [2026-07-31](./daily-archive/2026-07-31.md)
- [2026-07-30](./daily-archive/2026-07-30.md)
- [2026-07-29](./daily-archive/2026-07-29.md)
- [2026-07-28](./daily-archive/2026-07-28.md)
- [2026-07-27](./daily-archive/2026-07-27.md)
- [2026-07-26](./daily-archive/2026-07-26.md)
- [2026-07-25](./daily-archive/2026-07-25.md)

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

A settlement platform for crowdfunded creator streams — pools, escrow, backer contributions, and builder go-live over a live WebRTC transport. 163 commits over the past 90 days. No new commits this past week; the repo has been quiet since the prior wave's first live deploy on a public IP.

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. 109 commits over the past 90 days. Thirty-three commits this past week: the release-on-merge flow cut the first release, `v0.2.0`, closing an 88-commit `[Unreleased]` backlog ([#326](https://github.com/promptctl/links-issue-tracker/pull/326), [#327](https://github.com/promptctl/links-issue-tracker/pull/327)); the regenerated code-review workflow routes Dependabot reviews through the Dependabot secret store without a privileged `pull_request_target` ([#319](https://github.com/promptctl/links-issue-tracker/pull/319)); the goose-migration drift repair suite self-heals a stale-shape quarantine table, detects a goose-applied version whose content never ran, and transparently repairs drifted version-content ([#323](https://github.com/promptctl/links-issue-tracker/pull/323)–[#325](https://github.com/promptctl/links-issue-tracker/pull/325)); every release now ships a `THIRD_PARTY_LICENSES` bundle plus license report ([#320](https://github.com/promptctl/links-issue-tracker/pull/320)); `dep add`/`dep rm` and `parent set` dropped positional endpoints for `--from`/`--to` and `--child`/`--parent` ([#321](https://github.com/promptctl/links-issue-tracker/pull/321), [#322](https://github.com/promptctl/links-issue-tracker/pull/322)); earlier vendored a patched copy of dolthub/driver with the telemetry goroutine cut via `go.mod replace` ([#317](https://github.com/promptctl/links-issue-tracker/pull/317)); unrelated-histories epic `v0ac.1`–`.4` promoted "no common ancestor" to a first-class reconcile state with take-one-side and union-both-backlogs resolutions ([#309](https://github.com/promptctl/links-issue-tracker/pull/309)–[#312](https://github.com/promptctl/links-issue-tracker/pull/312)); cross-project epic `84ef.1`–`.3` added workspace store discovery, a read-only opener, and a holistic ready/in-flight/blocked overview ([#313](https://github.com/promptctl/links-issue-tracker/pull/313)–[#315](https://github.com/promptctl/links-issue-tracker/pull/315)); schema-skew work `7p7q.1`–`.4` gave every reporter one sync-failure contract, added a store-tolerant `lit upgrade`, and refused stale-schema writes against a newer remote head ([#294](https://github.com/promptctl/links-issue-tracker/pull/294), [#296](https://github.com/promptctl/links-issue-tracker/pull/296), [#299](https://github.com/promptctl/links-issue-tracker/pull/299), [#300](https://github.com/promptctl/links-issue-tracker/pull/300)).

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

The paste-and-share companion to `slopspot-web` — ingest a pasted conversation URL, render a turn-anchored public view, and layer author-controlled hide/collapse/feature directives on top. 66 commits over the past 90 days. No new commits this past week; the prior wave shipped the continuation-bundle export for resuming a conversation elsewhere ([#95](https://github.com/brandon-fryslie/slopspot-paste/pull/95)) and derived the source-origin label from the URL host instead of a hardcoded string ([#96](https://github.com/brandon-fryslie/slopspot-paste/pull/96)).

</td>
<td width="50%" valign="top">

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. 110 commits over the past 90 days. No new commits this past week after the prior wave landed `tmux-complexity-lkg.4`–`.13`, which unpacked `WebSocketTmuxClient`, `createMainBridge`, `bridge-connection`, `xterm-sink`, DemoStore, and `InspectorView` into named parts, extracted the seed-grid into a pure `seed-builder.ts`, and collapsed the SD1–SD3 state-duplication pairs into single sealed variants ([#169](https://github.com/promptctl/tmux-control-mode-js/pull/169)–[#178](https://github.com/promptctl/tmux-control-mode-js/pull/178)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 3★**

Brandon's personal machine setup — dotbot-linked configs for `tmux`, `zsh`, Claude Code, iTerm2, and a garden of installable Claude skills that live alongside the shell wiring. 102 commits over the past 90 days. Thirty commits this past week: today the `agent-code-review` install preflight learned to skip the `code-review.yml` converge when the deployed workflow uses a local `uses: ./` action path, so running the review loop inside the action's own source repo stops clobbering its dogfooded config ([commit](https://github.com/brandon-fryslie/dotfiles/commit/c174d606e03f97fa29485534a792c67cd74c5f96)); earlier in the week the same template switched from `pull_request_target` back to `pull_request` after finding Dependabot runs read from a separate secret store, plus a 15-minute cap on the review job ([commit](https://github.com/brandon-fryslie/dotfiles/commit/9254d8fe7690687c367f8ddb30d6c06453b3e328), [commit](https://github.com/brandon-fryslie/dotfiles/commit/ecdcb769406dcb7c538f6cfdc409bcce8ef01b33)); `iterm2-restore` sub-epic `5k5.1`–`.7` marched from UUID-stability probe through UUID-keyed sidecar carrier, live tmux-hook sidecar writer, variant-B iTerm2 wire-in, deterministic post-restore verifier, and launchd-owned periodic resurrect save; a Claude-Code statusline launcher resolves `cc-candybar` against a local checkout, then the pnpm-dlx runtime, then a loud in-bar error ([commit](https://github.com/brandon-fryslie/dotfiles/commit/8454a1d8548c6fe40ade1f7137ded2c4c9820532)); the never-run bats test suite was deleted and the `dev-loop-orig/` agent originals removed; `mxroute-email`, `bro-guru`, `slop-image` fal-nano-banana, and a global `dotfiles` street-map skill were added.

### [tinkerpadai-web](https://github.com/promptctl/tinkerpadai-web)
**TypeScript**

TinkerPad — a public commons of generative, self-contained interactive playgrounds. 62 commits over the past 90 days across the commons view, playground runtime, and author surface. No new commits this past week.

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
