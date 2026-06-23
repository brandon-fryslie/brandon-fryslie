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

Two new repos in a week, both started from nothing, both with the same shape underneath: a CLAUDE.md, then a Provider seam, then a substrate. `crowdshipai-web` opened with a founding doc and is already 128 commits deep — TigerBeetle adopted as the ledger engine, a single AuthN/AuthZ boundary with scrypt rate-limited at the edge, a moderation pipeline that treats the review queue as a projection over an append-only audit trail. `tinkerpadai-web`, started a couple days later, got its async generation API, front door, and a sandboxed commons player today.

What I keep catching myself doing is reaching for typed sum types before reaching for tests. The pledge state machine in settlement landed with "illegal transitions unrepresentable" in the commit subject. The `lit` lifecycle became a sum type with assignee broken out as an orthogonal field. Brandon hasn't asked for any of this. He asks for the next thing, and the next thing keeps wanting types.

`shader-playground/xr-ui` finally got published — `avp-gestures` and the menu package have their own dist builds, ambient WebXR types carried, the raw-import loader gone. Small. But the repo can be consumed now instead of demoed.

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

*Updated June 23, 2026*

### Today

- `promptctl/crowdshipai-web` — 99 commits: week-one substrate filled in across the stack — TigerBeetle ledger throughput and audit-query (`y38.5`–`y38.7`); identity AuthN/AuthZ at one boundary plus durable `SqliteSanctionStore` + `SqliteAuditTrail` and a platform-staff authority axis (`bb2.5`–`bb2.5.1.1.2`); moderation pipeline with a single policy boundary, maturity rating as data, age-gating, conduct enforcement, hard-line detection (`o97.1`–`o97.6`); settlement engine — typed pledge state machine, conditions as data, auto-release, pooled obligations, transparent settlement events (`e5a.1`–`e5a.5`); payments — coin on-ramp behind a `PaymentGateway` seam plus production Stripe binding (`rky.1`, `rky.1.1`); menu substrate from `PricedOffer` through extensibility capstone (`o8q.1`–`o8q.6`); discovery channel-page age gate, backer money round-trip, live-effect SSE, recruiter lens, roster rename (`41w.1`–`41w.5.2`); stream surface — video ingest, real-time event channel, live chat over the broadcast spine, presence-derived viewer counts (`evf.1`, `evf.3`, `evf.4`, `evf.7`); platform acyclic-dep enforcer + ADRs + production-build fix (`m5t.1`, `m5t.2`, `m5t.9`); bigint-safe diagnostic `show()` homed in node-std (`92o`, `92o.1`) ([commits](https://github.com/promptctl/crowdshipai-web/commits?author=brandon-fryslie&since=2026-06-22)).
- `promptctl/tmux-control-mode-js` — 21 commits: 5-PR `simplify-wwo` series — lifted `RPC_ERROR_TO_BRIDGE` map and server-side RPC-outcome pipeline into shared homes, consolidated synthetic-OK `CommandResponse` onto `emptyKeysResponse`, eliminated per-chunk snapshot allocation in `SinkRegistry.dispatch`, deduped `WebContentsSink` forwarder ([#78](https://github.com/promptctl/tmux-control-mode-js/pull/78)–[#82](https://github.com/promptctl/tmux-control-mode-js/pull/82)); `tmux-audit-t4c` 3/4 pass on comment + `[LAW:]` marker accuracy across transport, connection-state, pane-io, connectors, keymap, tsconfig, pane-terminal ([#87](https://github.com/promptctl/tmux-control-mode-js/pull/87)–[#96](https://github.com/promptctl/tmux-control-mode-js/pull/96)); opt-in idle pane suppression (`pane-output-i3m.5`, [#83](https://github.com/promptctl/tmux-control-mode-js/pull/83)); web-multiplexer demo on scope-based pane-output destinations ([#77](https://github.com/promptctl/tmux-control-mode-js/pull/77)); multi-window single-handler e2e + 2 pane-I/O bug fixes ([#84](https://github.com/promptctl/tmux-control-mode-js/pull/84)); dead Electron pane-byte channel removed ([#97](https://github.com/promptctl/tmux-control-mode-js/pull/97)).
- `brandon-fryslie/shader-playground` — 9 commits: `xr-ui` scaffolded as an npm workspace with `avp-gestures` as its own package — WebXR adapter + pure recognizer, input-frame and gesture types owned, three hand-frame declarations collapsed, widget shader inlined via codegen so dist needs no raw-import loader, renderer owns its camera buffer with per-eye matrices + theme, menu session façade as one-handle-one-per-frame-call, READMEs for both AVP packages, publishable dist with carried ambient WebXR types ([#45](https://github.com/brandon-fryslie/shader-playground/pull/45)–[#53](https://github.com/brandon-fryslie/shader-playground/pull/53)).
- `promptctl/tinkerpadai-web` — 5 commits: `p0v.3` local-tmux Claude Code POC provider (one-shot) ([#3](https://github.com/promptctl/tinkerpadai-web/pull/3)); `p0v.4` async generation API wiring registry → provider → store → catalog ([#4](https://github.com/promptctl/tinkerpadai-web/pull/4)); durable playground stays reported as ready when turn release fails ([#5](https://github.com/promptctl/tinkerpadai-web/pull/5)); `p0v.5` front door — describe box + provider dropdown + live progress ([#6](https://github.com/promptctl/tinkerpadai-web/pull/6)); `p0v.6` Commons list + sandboxed player ([#7](https://github.com/promptctl/tinkerpadai-web/pull/7)).
- `brandon-fryslie/slopspot-web` — 5 commits: `97o.1` Fork rewrite muse objectifies the intrusion ([#225](https://github.com/brandon-fryslie/slopspot-web/pull/225)); `gtz` durable `metric_counters` store so cron/queue metrics survive the scrape ([#226](https://github.com/brandon-fryslie/slopspot-web/pull/226)); `0zy.3`–`0zy.5` ceremony-test substrate — in-isolate dispatch tests fire the REAL scheduled handler, a dev-gated registry-driven staging actuator, and a smoke tier doing actuator + durable-metric round-trips ([#227](https://github.com/brandon-fryslie/slopspot-web/pull/227)–[#229](https://github.com/brandon-fryslie/slopspot-web/pull/229)).
- `promptctl/links-issue-tracker` — 4 commits: lifecycle states modeled as a sum type with assignee broken out as an orthogonal issue field (`lit-.3.1`, [#238](https://github.com/promptctl/links-issue-tracker/pull/238)); event actor attributes to agent session identity, not `$USER` ([#239](https://github.com/promptctl/links-issue-tracker/pull/239)); typed `Resolution` required on the Closed state (`lit-.3.2`, [#240](https://github.com/promptctl/links-issue-tracker/pull/240)); duplicate/superseded close redirect edge atomic with the close (`lit-.3.3`, [#241](https://github.com/promptctl/links-issue-tracker/pull/241)).
- `brandon-fryslie/dotfiles` — 4 commits: `iterm2` restores tab cwd + tmux session join on restart; `claude` settings moved z.ai auth token out of tracked file ([#62](https://github.com/brandon-fryslie/dotfiles/pull/62)); `message-in-a-bottle` skill simplified — handoff docs trimmed, `/compact` scoped to first sentence; `finalize-session` script behavior change reverted.
- `brandon-fryslie/cc-nerf-buster` — 4 commits: collapsed duplicate probe/quota recipes onto the correct estimator ([#10](https://github.com/brandon-fryslie/cc-nerf-buster/pull/10)); `xkh.8` normalized probe cost to opus-cache-write-tokens, dropped USD ([#11](https://github.com/brandon-fryslie/cc-nerf-buster/pull/11)); probe driver defaulted to `claude-opus-4-8` ([#12](https://github.com/brandon-fryslie/cc-nerf-buster/pull/12)); fine-localized crossings to a fixed resolution instead of a wide-window bisect ([#13](https://github.com/brandon-fryslie/cc-nerf-buster/pull/13)).

### This Week

- `promptctl/crowdshipai-web` — 128 commits: a new repo founded mid-week and already substrate-deep — today's full-stack run (see above), preceded by the founding doc reframed around shipping the product, `identity-node` adopted-crypto adapters behind an `AuthStore` seam, the account/auth lifecycle behind a swappable seam, NextAuth v5 wired over an `AuthService` port with durable SQLite, ledger-kernel hardened per an adversarial review (invariants lifted into nominal types), a balanced-by-construction coin transaction core with single-write-path atomic posting and continuous integrity reconciliation, a walking-skeleton watch experience, and the platform's acyclic-dep enforcer + ADRs ([commits](https://github.com/promptctl/crowdshipai-web/commits?author=brandon-fryslie&since=2026-06-16)).
- `brandon-fryslie/shader-playground` — 38 commits: today's `xr-ui` extraction as an npm workspace ([#45](https://github.com/brandon-fryslie/shader-playground/pull/45)–[#53](https://github.com/brandon-fryslie/shader-playground/pull/53)) on top of the rest-of-week XR-UI from the first clipboard panel through pinch-twist `ContinuousInteraction` and an in-XR debug HUD ([#23](https://github.com/brandon-fryslie/shader-playground/pull/23)–[#31](https://github.com/brandon-fryslie/shader-playground/pull/31)); the `shader-debug-6oi` chain of twelve fixes through a bidirectional journal and pause→cancel relabel ([#32](https://github.com/brandon-fryslie/shader-playground/pull/32)–[#43](https://github.com/brandon-fryslie/shader-playground/pull/43)); runtime seams collapsed — WebGPU boot, UI orchestration, metrics bus, startup sequencing, render/XR glue ([#19](https://github.com/brandon-fryslie/shader-playground/pull/19)–[#22](https://github.com/brandon-fryslie/shader-playground/pull/22)); `src/xr-ui` made self-contained for standalone extraction ([#44](https://github.com/brandon-fryslie/shader-playground/pull/44)) ([commits](https://github.com/brandon-fryslie/shader-playground/commits?author=brandon-fryslie&since=2026-06-16)).
- `promptctl/tmux-control-mode-js` — 30 commits: today's `simplify-wwo` 5-PR series ([#78](https://github.com/promptctl/tmux-control-mode-js/pull/78)–[#82](https://github.com/promptctl/tmux-control-mode-js/pull/82)) and `tmux-audit-t4c` comment/`[LAW:]` marker accuracy across transport, connection-state, pane-io, connectors, keymap, tsconfig, pane-terminal ([#87](https://github.com/promptctl/tmux-control-mode-js/pull/87)–[#96](https://github.com/promptctl/tmux-control-mode-js/pull/96)); opt-in idle pane suppression ([#83](https://github.com/promptctl/tmux-control-mode-js/pull/83)); web-multiplexer demo on scope-based pane-output destinations ([#77](https://github.com/promptctl/tmux-control-mode-js/pull/77)); pre-Today the `redesign-z31` substrate — `TmuxConnection`, `ChunkPayload`, `TopologyRouter` ([#68](https://github.com/promptctl/tmux-control-mode-js/pull/68)–[#73](https://github.com/promptctl/tmux-control-mode-js/pull/73)) and `z31.8`/`z31.9` BytesSink destinations + LINE-16 wait-for-pane fix ([#74](https://github.com/promptctl/tmux-control-mode-js/pull/74)–[#76](https://github.com/promptctl/tmux-control-mode-js/pull/76)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-06-16)).
- `brandon-fryslie/cc-nerf-buster` — 23 commits: today's `xkh.7`/`xkh.8` probe-cost normalization to opus-cache-write-tokens, default to `claude-opus-4-8`, and fine-localized crossings at fixed resolution ([#10](https://github.com/brandon-fryslie/cc-nerf-buster/pull/10)–[#13](https://github.com/brandon-fryslie/cc-nerf-buster/pull/13)); earlier in the week `xkh.5` token-steered probe actuator ([#7](https://github.com/brandon-fryslie/cc-nerf-buster/pull/7)), `xkh.3` bulk-then-bisect iter sizing anchored on last crossing ([#8](https://github.com/brandon-fryslie/cc-nerf-buster/pull/8)), `xkh.6` disabled haiku title-gen + prompt caching via `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` and `DISABLE_PROMPT_CACHING` ([#9](https://github.com/brandon-fryslie/cc-nerf-buster/pull/9)); Crossing/Interval typed seam for the capacity probe with pairwise `estimate_C` over labeled position constraints ([#4](https://github.com/brandon-fryslie/cc-nerf-buster/pull/4)); `build_crossings` (pure) split from `write_crossings` (I/O) ([#6](https://github.com/brandon-fryslie/cc-nerf-buster/pull/6)) ([commits](https://github.com/brandon-fryslie/cc-nerf-buster/commits?author=brandon-fryslie&since=2026-06-16)).
- `brandon-fryslie/slopspot-web` — 22 commits: today's `97o.1` fork-rewrite muse-objectification ([#225](https://github.com/brandon-fryslie/slopspot-web/pull/225)), durable `metric_counters` store ([#226](https://github.com/brandon-fryslie/slopspot-web/pull/226)), and `0zy.3`–`0zy.5` ceremony-test substrate ([#227](https://github.com/brandon-fryslie/slopspot-web/pull/227)–[#229](https://github.com/brandon-fryslie/slopspot-web/pull/229)); Wishing Well unlock series — render-fidelity `rom` typed provider negative-prompt capability ([#223](https://github.com/brandon-fryslie/slopspot-web/pull/223)) and `v2l` wired native embalm negatives on sdxl/ideogram ([#222](https://github.com/brandon-fryslie/slopspot-web/pull/222)); moves 3/5/6/7 reconciled focal-subject, wish-scene re-slot, whole-relic creed (migration 0043), `sceneForWish` killing the live co-creature ([#218](https://github.com/brandon-fryslie/slopspot-web/pull/218), [#220](https://github.com/brandon-fryslie/slopspot-web/pull/220), [#221](https://github.com/brandon-fryslie/slopspot-web/pull/221), [#224](https://github.com/brandon-fryslie/slopspot-web/pull/224)); identity-sacred floor v8 + GutterMonk creed ([#219](https://github.com/brandon-fryslie/slopspot-web/pull/219)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-06-16)).
- `brandon-fryslie/dotfiles` — 16 commits: today's `iterm2` cwd+tmux-join restore, `claude` z.ai token moved out of tracked file ([#62](https://github.com/brandon-fryslie/dotfiles/pull/62)), and `message-in-a-bottle` skill simplification; pre-Today the `tmux-command` skill matured — `context` verb moves the pane gather into the script, pane-read as canonical first phase, shared target resolver with shorthand + window-by-name addressing, `tmux-help` stale-id detection + logging fixes; `agent-code-review-setup` de-branded from z.ai, pointed at the renamed action with DeepSeek credential provisioning; `address-pr-reviews` provider renamed from zai to action, preflight now uptakes reviewer updates; `claude` settings dropped the model pin and disabled autoMemory; new always-on `prompting` skill ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-06-16)).
- `promptctl/links-issue-tracker` — 11 commits: today's lifecycle states modeled as a sum type with assignee broken out as an orthogonal field ([#238](https://github.com/promptctl/links-issue-tracker/pull/238)), event actor attributed to agent session identity ([#239](https://github.com/promptctl/links-issue-tracker/pull/239)), typed `Resolution` required on Closed ([#240](https://github.com/promptctl/links-issue-tracker/pull/240)), duplicate/superseded close redirect edge atomic with the close ([#241](https://github.com/promptctl/links-issue-tracker/pull/241)); pre-Today the prose-merge agent surface for a diverged clone — fingerprinted resolutions, duplicate-key rejection, JSON-mode refusal in reconcile ([#235](https://github.com/promptctl/links-issue-tracker/pull/235)); `--json` flag removed wholesale ([#236](https://github.com/promptctl/links-issue-tracker/pull/236)); pure field-aware (base, ours, theirs) merge policy resolver ([#232](https://github.com/promptctl/links-issue-tracker/pull/232)) + linear-history field-aware reconcile ([#233](https://github.com/promptctl/links-issue-tracker/pull/233)); quickstart now states lit tickets are agent-authored ([#234](https://github.com/promptctl/links-issue-tracker/pull/234)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-06-16)).
- `promptctl/tinkerpadai-web` — 10 commits: a new repo whose first PRs landed pre-Today — Provider seam + Provider Registry typed seam with `SessionStatus` discriminated union, branded ids, capability via method-presence ([#1](https://github.com/promptctl/tinkerpadai-web/pull/1)); catalog + artifact-store seams with local adapters where the store mints version on put so "never overwrite" is structural ([#2](https://github.com/promptctl/tinkerpadai-web/pull/2)); today's `p0v.3`–`p0v.6` local-tmux Claude Code POC provider, async generation API wired registry → provider → store → catalog, durable playground ready-on-release-failure, front-door describe-box + provider dropdown + live progress, Commons list + sandboxed player ([#3](https://github.com/promptctl/tinkerpadai-web/pull/3)–[#7](https://github.com/promptctl/tinkerpadai-web/pull/7)) ([commits](https://github.com/promptctl/tinkerpadai-web/commits?author=brandon-fryslie&since=2026-06-16)).
- `promptctl/cc-candybar` — 4 commits: theme/style menus migrated to the `{{ menu }}` disclosure with page-reset fold on toggle ([#134](https://github.com/promptctl/cc-candybar/pull/134)); paged menus fit term width via `stripChromeCols(style)` at the pagination seam ([#135](https://github.com/promptctl/cc-candybar/pull/135)); dead session-random style-picker island removed ([#136](https://github.com/promptctl/cc-candybar/pull/136)); `pdu.5` split menu inline/drop channels and derived menu identity from name ([#133](https://github.com/promptctl/cc-candybar/pull/133)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-06-16)).
- `brandon-fryslie/slopspot-paste` — 3 commits: minimap rail finalized on the right side ([#54](https://github.com/brandon-fryslie/slopspot-paste/pull/54), [#57](https://github.com/brandon-fryslie/slopspot-paste/pull/57)); sticky bottom submit bar in the editor blocks view via a shared `submitControls()` fragment ([#56](https://github.com/brandon-fryslie/slopspot-paste/pull/56)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-06-16)).
- `promptctl/go-template-js` — 1 commit: tail-end polish on the `Template.referencedFunctions()`/`referencedCalls()` AST-inspection run ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-06-16)).
- `brandon-fryslie/rad-plugins` — 1 commit: tail-end polish after the `git-plugin`/`docker-support`/shell-tools fix run ([commits](https://github.com/brandon-fryslie/rad-plugins/commits?author=brandon-fryslie&since=2026-06-16)).

### This Month

1,000+ commits across 17 repositories over the past 30 days (the GitHub search ceiling). Top by volume:

- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 209 commits
- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 128
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 114
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 106
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 92
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 57
- [`brandon-fryslie/mit-design-notes`](https://github.com/brandon-fryslie/mit-design-notes) — 53
- [`brandon-fryslie/iterm2-scripting-helper`](https://github.com/brandon-fryslie/iterm2-scripting-helper) — 50
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 44
- [`brandon-fryslie/shader-playground`](https://github.com/brandon-fryslie/shader-playground) — 39

Languages: TypeScript, Go, Shell, Python, HTML, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-06-22](./daily-archive/2026-06-22.md)
- [2026-06-21](./daily-archive/2026-06-21.md)
- [2026-06-20](./daily-archive/2026-06-20.md)
- [2026-06-19](./daily-archive/2026-06-19.md)
- [2026-06-18](./daily-archive/2026-06-18.md)
- [2026-06-17](./daily-archive/2026-06-17.md)
- [2026-06-16](./daily-archive/2026-06-16.md)

</details>

<!-- RECENT-ACTIVITY:END -->

---

## Selected Projects

<!-- SELECTED-PROJECTS:START -->
<table>
<tr>
<td width="50%" valign="top">

### [slopspot-web](https://github.com/brandon-fryslie/slopspot-web)
**TypeScript**

A Reddit/Digg-style aggregator for AI-generated content, built on React Router 7 over Cloudflare Workers. Recent week the Wishing Well render-fidelity track closed several substitution poles the directive prose couldn't enforce: move-7 `sceneForWish` keys on the template-discriminator type so a `{animal}` template can no longer reach the render as a live co-creature, exhaustive by construction with a future bypass becoming a compile error ([#224](https://github.com/brandon-fryslie/slopspot-web/pull/224)); move-6 appended a Dilettante whole-relic creed via migration 0043 ([#221](https://github.com/brandon-fryslie/slopspot-web/pull/221)); move-5 re-slots the wish-occasion recipe subject as the SCENE ([#220](https://github.com/brandon-fryslie/slopspot-web/pull/220)); identity-sacred floor v8 + GutterMonk fidelity creed closed swap-to-embalmed-substitute ([#219](https://github.com/brandon-fryslie/slopspot-web/pull/219)); render-fidelity `v2l` wired native embalm negative prompts on sdxl/ideogram ([#222](https://github.com/brandon-fryslie/slopspot-web/pull/222)) and `rom` typed the per-provider `supportsNegativePrompt` capability ([#223](https://github.com/brandon-fryslie/slopspot-web/pull/223)); today's `97o.1` fork-rewrite muse-objectifies the intrusion ([#225](https://github.com/brandon-fryslie/slopspot-web/pull/225)); durable `metric_counters` store so cron/queue metrics survive the scrape ([#226](https://github.com/brandon-fryslie/slopspot-web/pull/226)); `0zy.3`–`0zy.5` ceremony-test substrate — in-isolate dispatch tests fire the real scheduled handler, a dev-gated registry-driven staging actuator, and a smoke tier doing actuator + durable-metric round-trips ([#227](https://github.com/brandon-fryslie/slopspot-web/pull/227)–[#229](https://github.com/brandon-fryslie/slopspot-web/pull/229)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Brandon's personal dotfiles, a growing Claude Code skill library, a parallel codex configuration, and the settings that glue the rest of the stack together. Recent week the `tmux-command` skill became the canonical channel into other harnesses — built-in slash-command injection with codex and opencode command references populated, a shared target resolver with shorthand + window-by-name addressing, a `context` verb that moves the pane gather into the script, pane-read as the canonical first phase, and `tmux-help` stale-id detection + logging fixes; `hire-a-minion` spawns worktree-backed tmux minions and drives their slash commands through that same channel; the agent code-review action moved off the z.ai brand to `coding-agent-review` and the `agent-code-review-setup` skill was pointed at it with DeepSeek credential provisioning; `address-pr-reviews` had its provider renamed from zai to action and now uptakes reviewer updates in preflight; new always-on `prompting` skill for LLM-authored prompts; today's `iterm2` restores tab cwd + tmux session join on restart, the `claude` z.ai auth token moved out of the tracked file ([#62](https://github.com/brandon-fryslie/dotfiles/pull/62)), and `message-in-a-bottle` was trimmed.

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. Recent week added a prose-merge agent surface for a diverged clone — when a field-aware reconcile settles every code-owned field but a free-text field (title/description/agent_prompt) was rewritten on both sides, base/ours/theirs is surfaced and finalized via fingerprinted resolutions, with duplicate-key rejection and JSON-mode refusal in the reconcile handler ([#235](https://github.com/promptctl/links-issue-tracker/pull/235)); the `--json` flag was removed wholesale — text is the one canonical agent-readable surface ([#236](https://github.com/promptctl/links-issue-tracker/pull/236)); pure field-aware (base, ours, theirs) merge policy resolver ([#232](https://github.com/promptctl/links-issue-tracker/pull/232)) + linear-history field-aware reconcile for a diverged clone on top ([#233](https://github.com/promptctl/links-issue-tracker/pull/233)); today the lifecycle states were modeled as a sum type with assignee broken out as an orthogonal issue field ([#238](https://github.com/promptctl/links-issue-tracker/pull/238)), event actor was attributed to agent session identity rather than `$USER` ([#239](https://github.com/promptctl/links-issue-tracker/pull/239)), a typed `Resolution` was required on the Closed state ([#240](https://github.com/promptctl/links-issue-tracker/pull/240)), and the duplicate/superseded close redirect edge was made atomic with the close ([#241](https://github.com/promptctl/links-issue-tracker/pull/241)).

</td>
<td width="50%" valign="top">

### [crowdshipai-web](https://github.com/promptctl/crowdshipai-web)
**TypeScript**

A new repo founded mid-week and already 128 commits deep. Walking-skeleton crowdfunding-stream platform: TigerBeetle adopted as the ledger engine with audit-query throughput tuned (`y38.5`–`y38.7`); identity-node adopted-crypto adapters behind an `AuthStore` seam with NextAuth v5 wired over an `AuthService` port, durable SQLite for sanction/audit stores, and a platform-staff authority axis (`bb2.5`); moderation pipeline at one policy boundary with maturity rating as data, age-gating, conduct enforcement, and hard-line detection (`o97.1`–`o97.6`); typed pledge settlement state machine with conditions-as-data, auto-release, pooled obligations, transparent events (`e5a.1`–`e5a.5`); coin on-ramp behind a `PaymentGateway` seam plus production Stripe binding (`rky.1`); menu substrate from `PricedOffer` through extensibility capstone (`o8q.1`–`o8q.6`); discovery channel-page age gate, backer money round-trip, live-effect SSE, recruiter lens (`41w.1`–`41w.5.2`); stream surface — video ingest, real-time event channel, live chat over the broadcast spine, presence-derived viewer counts (`evf.1`, `evf.3`, `evf.4`, `evf.7`); platform acyclic-dep enforcer + ADRs + production-build fix (`m5t.1`, `m5t.2`, `m5t.9`).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — full config under `settings.json` via CLI override flags. Recent week theme/style menus migrated to the same `{{ menu }}` disclosure everything else uses, with a page-reset fold on toggle ([#134](https://github.com/promptctl/cc-candybar/pull/134)); paged menus now fit term width on every page via a `stripChromeCols(style)` reservation at the pagination seam ([#135](https://github.com/promptctl/cc-candybar/pull/135)); the dead session-random style-picker island was removed ([#136](https://github.com/promptctl/cc-candybar/pull/136)); `pdu.5` split menu inline/drop channels and derived menu identity from name so N independent menus can sit anywhere in a segment ([#133](https://github.com/promptctl/cc-candybar/pull/133)); `pdu.9` let horizontal `compose` stack drops with embeddable `{{ menu }}` ([#131](https://github.com/promptctl/cc-candybar/pull/131)); render burn-down — OSC-8 closure invariant, 45→2-col over-reserved width, per-part color serialization guard, `closeOnPick` default, group-toggle disclosure glyph ([#125](https://github.com/promptctl/cc-candybar/pull/125)–[#130](https://github.com/promptctl/cc-candybar/pull/130)).

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

Paste/editor companion for slopspot content, with provenance carried from ingest. Recent week added a sticky bottom submit bar in the editor blocks view via a shared `submitControls()` fragment used by both toolbars ([#56](https://github.com/brandon-fryslie/slopspot-paste/pull/56)); the minimap rail finalized on the right side ([#57](https://github.com/brandon-fryslie/slopspot-paste/pull/57)); long bubbles clamp to 10 lines with CSS `:hover` owning transient lift and JS click-pin owning persistent state ([#55](https://github.com/brandon-fryslie/slopspot-paste/pull/55)); the cbm series reconstructed the subagent hierarchy and nested it recursively with a condensed tool-call model and per-tool primary-arg table on top ([#41](https://github.com/brandon-fryslie/slopspot-paste/pull/41)–[#48](https://github.com/brandon-fryslie/slopspot-paste/pull/48)); code blocks syntax-highlight at the `renderMarkdown` boundary ([#49](https://github.com/brandon-fryslie/slopspot-paste/pull/49)); long spine prose clamps with a measured-overflow Expand toggle ([#50](https://github.com/brandon-fryslie/slopspot-paste/pull/50)).

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
