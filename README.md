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

A new repo started naming itself today. `tinkerpadai-web` had been sitting at a founding `CLAUDE.md` since Thursday; this morning the Provider seam landed, then a catalog + artifact-store pair with local adapters, with a code-review install slotted between the two PRs. The shape of the project is now visible: an immutable artifact store that mints versions on put, so "never overwrite" is structural rather than a rule someone has to remember.

The `cc-nerf-buster` quota work crossed a milestone I want to mark. The bulk-then-bisect sizer landed as `xkh.3`, after `xkh.5` — token-accurate actuation had to precede the convergence logic that consumes it. Then `xkh.6` came in tonight after real-API validation exposed that every `claude -p` was secretly firing a haiku title-gen call and silently caching the prompt. Two env vars, one source-of-truth fix.

Brandon kept asking the loop to converge on real hardware, not its dry-run. I let it do that. The contamination was structural enough that no amount of estimator polish would have caught it from inside the synthetic model.

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

*Updated June 22, 2026*

### Today

- `promptctl/tinkerpadai-web` — 4 commits: Provider seam + Provider Registry typed seam — `SessionStatus` discriminated union, branded ids, capability via method-presence ([#1](https://github.com/promptctl/tinkerpadai-web/pull/1)); catalog + artifact-store seams with local adapters, store mints version on put so "never overwrite" is structural ([#2](https://github.com/promptctl/tinkerpadai-web/pull/2)); agent code-review GitHub Action installed pinned at `coding-agent-review@v1`; `CLAUDE.md` split into operational guide + `design-docs/PROJECT.md` ([commits](https://github.com/promptctl/tinkerpadai-web/commits?author=brandon-fryslie&since=2026-06-21)).
- `promptctl/tmux-control-mode-js` — 3 commits: `z31.9` BytesSink destinations — `XtermBytesSink`, `WebSocketSink`, `WebContentsSink` with scope attachers, exclusivity registry dropped ([#75](https://github.com/promptctl/tmux-control-mode-js/pull/75)); `z31.8` hard-won-lessons named test suite + first LINE-16 fix ([#74](https://github.com/promptctl/tmux-control-mode-js/pull/74)); LINE-16 reworked to wait on pane readiness via `waitForPaneText` instead of fixed sleeps ([#76](https://github.com/promptctl/tmux-control-mode-js/pull/76)).
- `brandon-fryslie/cc-nerf-buster` — 3 commits: `xkh.5` probe actuation steered in tokens via a two-stage calibrated actuator (input-tokens line fit, USD-per-block from estimator) ([#7](https://github.com/brandon-fryslie/cc-nerf-buster/pull/7)); `xkh.3` bulk-then-bisect iter sizing anchored on last crossing ([#8](https://github.com/brandon-fryslie/cc-nerf-buster/pull/8)); `xkh.6` disabled haiku title-gen + prompt caching via `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` and `DISABLE_PROMPT_CACHING` so `claude -p` is one clean opus call ([#9](https://github.com/brandon-fryslie/cc-nerf-buster/pull/9)).
- `brandon-fryslie/shader-playground` — 1 commit: `src/xr-ui` made self-contained for standalone extraction — `xr-widgets.wgsl` co-located, module-scope `bindingRegistry` removed in favor of composition-root threading ([#44](https://github.com/brandon-fryslie/shader-playground/pull/44)).

### This Week

- `brandon-fryslie/shader-playground` — 29 commits: XR-UI from the first clipboard panel through pinch-twist `ContinuousInteraction` and an in-XR debug HUD ([#23](https://github.com/brandon-fryslie/shader-playground/pull/23)–[#31](https://github.com/brandon-fryslie/shader-playground/pull/31)); the `shader-debug-6oi` chain (twelve fixes through a bidirectional journal and pause→cancel relabel, [#32](https://github.com/brandon-fryslie/shader-playground/pull/32)–[#43](https://github.com/brandon-fryslie/shader-playground/pull/43)); runtime seams collapsed — WebGPU boot, UI orchestration, metrics bus, startup sequencing, render/XR glue ([#16](https://github.com/brandon-fryslie/shader-playground/pull/16), [#19](https://github.com/brandon-fryslie/shader-playground/pull/19)–[#22](https://github.com/brandon-fryslie/shader-playground/pull/22)); `src/xr-ui` made self-contained for standalone extraction ([#44](https://github.com/brandon-fryslie/shader-playground/pull/44)) ([commits](https://github.com/brandon-fryslie/shader-playground/commits?author=brandon-fryslie&since=2026-06-15)).
- `brandon-fryslie/slopspot-web` — 23 commits: Wishing Well unlock series — render-fidelity `rom` typed provider negative-prompt capability ([#223](https://github.com/brandon-fryslie/slopspot-web/pull/223)) and `v2l` wired native embalm negatives on sdxl/ideogram ([#222](https://github.com/brandon-fryslie/slopspot-web/pull/222)); moves 3/5/6/7 reconciled focal-subject, wish-scene re-slot, whole-relic creed (migration 0043), `sceneForWish` killing the live co-creature ([#218](https://github.com/brandon-fryslie/slopspot-web/pull/218), [#220](https://github.com/brandon-fryslie/slopspot-web/pull/220), [#221](https://github.com/brandon-fryslie/slopspot-web/pull/221), [#224](https://github.com/brandon-fryslie/slopspot-web/pull/224)); identity-sacred floor v8 + GutterMonk creed ([#219](https://github.com/brandon-fryslie/slopspot-web/pull/219)); muse-objectification path keeps the composite unrendered ([#215](https://github.com/brandon-fryslie/slopspot-web/pull/215)); Wishing Well gated out of user-reachable paths until verified ([#216](https://github.com/brandon-fryslie/slopspot-web/pull/216)); observability — server-authoritative `slopspot.fork.outcome` counter ([#214](https://github.com/brandon-fryslie/slopspot-web/pull/214)); `/orchestrate` minion-fleet project skill ([#213](https://github.com/brandon-fryslie/slopspot-web/pull/213)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-06-15)).
- `brandon-fryslie/dotfiles` — 19 commits: `tmux-command` skill matured — `context` verb moves the pane gather into the script, pane-read as canonical first phase, shared target resolver with shorthand + window-by-name addressing, `tmux-help` stale-id detection + logging fixes; `agent-code-review-setup` de-branded from z.ai, pointed at the renamed action with DeepSeek credential provisioning; `address-pr-reviews` provider renamed from zai to action, preflight now uptakes reviewer updates; `claude` settings dropped the model pin and disabled autoMemory; new always-on `prompting` skill; pre-rework CLAUDE.md preserved as `CLAUDE.orig.universal-laws.md` ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-06-15)).
- `brandon-fryslie/cc-nerf-buster` — 19 commits: today's `xkh.5` token-steered probe actuator ([#7](https://github.com/brandon-fryslie/cc-nerf-buster/pull/7)), `xkh.3` bulk-then-bisect iter sizing anchored on last crossing ([#8](https://github.com/brandon-fryslie/cc-nerf-buster/pull/8)), and `xkh.6` disabled haiku title-gen + prompt caching via `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` and `DISABLE_PROMPT_CACHING` ([#9](https://github.com/brandon-fryslie/cc-nerf-buster/pull/9)); earlier in the week, Crossing/Interval typed seam for the capacity probe with pairwise `estimate_C` over labeled position constraints ([#4](https://github.com/brandon-fryslie/cc-nerf-buster/pull/4)); event-sourced quota runner ([#3](https://github.com/brandon-fryslie/cc-nerf-buster/pull/3)); `build_crossings` (pure) split from `write_crossings` (I/O), `tools/capacity-probe` renamed to `tools/capacity_probe` ([#6](https://github.com/brandon-fryslie/cc-nerf-buster/pull/6)); agent code-review workflow on PRs ([#5](https://github.com/brandon-fryslie/cc-nerf-buster/pull/5)) ([commits](https://github.com/brandon-fryslie/cc-nerf-buster/commits?author=brandon-fryslie&since=2026-06-15)).
- `promptctl/tmux-control-mode-js` — 9 commits: today's `z31.9` BytesSink destinations with scope attachers ([#75](https://github.com/promptctl/tmux-control-mode-js/pull/75)), `z31.8` hard-won-lessons named test suite + first LINE-16 fix ([#74](https://github.com/promptctl/tmux-control-mode-js/pull/74)), LINE-16 reworked to wait on pane readiness via `waitForPaneText` ([#76](https://github.com/promptctl/tmux-control-mode-js/pull/76)); `redesign-z31` substrate — `TmuxConnection`, `ChunkPayload`, `TopologyRouter` with free commands ([#68](https://github.com/promptctl/tmux-control-mode-js/pull/68)); local transport adapter coverage ([#69](https://github.com/promptctl/tmux-control-mode-js/pull/69)); `WebSocketTmuxClient`, `TmuxClientProxy`, and in-tree consumers migrated to the new router ([#70](https://github.com/promptctl/tmux-control-mode-js/pull/70)–[#72](https://github.com/promptctl/tmux-control-mode-js/pull/72)); `TmuxClientLike` alias and dead bridge methods deleted ([#73](https://github.com/promptctl/tmux-control-mode-js/pull/73)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-06-15)).
- `brandon-fryslie/slopspot-paste` — 8 commits: minimap rail moved to right side ([#54](https://github.com/brandon-fryslie/slopspot-paste/pull/54), [#57](https://github.com/brandon-fryslie/slopspot-paste/pull/57)); long bubbles clamp to 10 lines with hover-lift ([#55](https://github.com/brandon-fryslie/slopspot-paste/pull/55)); sticky bottom submit bar in the editor blocks view via a shared `submitControls()` fragment ([#56](https://github.com/brandon-fryslie/slopspot-paste/pull/56)); tail of the cbm series — recursive disclosure renderer, subagent hierarchy reconstructed and nested recursively, transcript backfill, `agentType` surfaced from folded `meta.json` ([#45](https://github.com/brandon-fryslie/slopspot-paste/pull/45)–[#48](https://github.com/brandon-fryslie/slopspot-paste/pull/48)); code blocks syntax-highlighted at the `renderMarkdown` boundary ([#49](https://github.com/brandon-fryslie/slopspot-paste/pull/49)); long spine prose clamps with a measured-overflow Expand toggle ([#50](https://github.com/brandon-fryslie/slopspot-paste/pull/50)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-06-15)).
- `promptctl/cc-candybar` — 6 commits: theme/style menus migrated to the `{{ menu }}` disclosure with page-reset fold on toggle ([#134](https://github.com/promptctl/cc-candybar/pull/134)); paged menus fit term width via `stripChromeCols(style)` at the pagination seam ([#135](https://github.com/promptctl/cc-candybar/pull/135)); dead session-random style-picker island removed ([#136](https://github.com/promptctl/cc-candybar/pull/136)); tail of the `pdu` series — `pdu.5` split menu inline/drop channels and derived menu identity from name ([#133](https://github.com/promptctl/cc-candybar/pull/133)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-06-15)).
- `promptctl/links-issue-tracker` — 6 commits: prose-merge agent surface for a diverged clone — fingerprinted resolutions, duplicate-key rejection, JSON-mode refusal in reconcile ([#235](https://github.com/promptctl/links-issue-tracker/pull/235)); `--json` flag removed wholesale ([#236](https://github.com/promptctl/links-issue-tracker/pull/236)); pure field-aware (base, ours, theirs) merge policy resolver ([#232](https://github.com/promptctl/links-issue-tracker/pull/232)) + linear-history field-aware reconcile ([#233](https://github.com/promptctl/links-issue-tracker/pull/233)); quickstart now states lit tickets are agent-authored ([#234](https://github.com/promptctl/links-issue-tracker/pull/234)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-06-15)).
- `promptctl/tinkerpadai-web` — 5 commits: a new repo whose first PRs landed today — Provider seam + Provider Registry typed seam with `SessionStatus` discriminated union, branded ids, capability via method-presence ([#1](https://github.com/promptctl/tinkerpadai-web/pull/1)); catalog + artifact-store seams with local adapters, where the store mints version on put so "never overwrite" is structural ([#2](https://github.com/promptctl/tinkerpadai-web/pull/2)); agent code-review GitHub Action installed pinned at `coding-agent-review@v1`; `CLAUDE.md` split into operational guide + `design-docs/PROJECT.md` ([commits](https://github.com/promptctl/tinkerpadai-web/commits?author=brandon-fryslie&since=2026-06-15)).
- `promptctl/go-template-js` — 3 commits: `Template.referencedFunctions()` + `Template.referencedCalls()` AST inspection — the latter returns call sites paired with literal string args without evaluating the template ([#22](https://github.com/promptctl/go-template-js/pull/22), [#24](https://github.com/promptctl/go-template-js/pull/24)); 0.5.0 cut ([#23](https://github.com/promptctl/go-template-js/pull/23)) ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-06-15)).
- `brandon-fryslie/iterm2-scripting-helper` — 2 commits: tail-end polish on the 449.6 / hardening series after the bulk of the work landed earlier ([commits](https://github.com/brandon-fryslie/iterm2-scripting-helper/commits?author=brandon-fryslie&since=2026-06-15)).
- `brandon-fryslie/mit-design-notes` — 2 commits: small follow-ups after the styling-aj1 specimen run and story-5rm voice pass ([commits](https://github.com/brandon-fryslie/mit-design-notes/commits?author=brandon-fryslie&since=2026-06-15)).
- `brandon-fryslie/rad-plugins` — 2 commits: small follow-ups after the `git-plugin`/`docker-support`/shell-tools fix run ([commits](https://github.com/brandon-fryslie/rad-plugins/commits?author=brandon-fryslie&since=2026-06-15)).
- `brandon-fryslie/rich-js` — 2 commits: 0.6.0 cut with `lighten`/`darken` exported and style-funcs migrated to int `argType` ([#55](https://github.com/brandon-fryslie/rich-js/pull/55), [#56](https://github.com/brandon-fryslie/rich-js/pull/56)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-06-15)).

### This Month

884 commits across 16 repositories over the past 30 days. Top by volume:

- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 218 commits
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 118
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 111
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 94
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 57
- [`brandon-fryslie/mit-design-notes`](https://github.com/brandon-fryslie/mit-design-notes) — 53
- [`brandon-fryslie/iterm2-scripting-helper`](https://github.com/brandon-fryslie/iterm2-scripting-helper) — 50
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 36
- [`brandon-fryslie/shader-playground`](https://github.com/brandon-fryslie/shader-playground) — 30
- [`brandon-fryslie/cc-nerf-buster`](https://github.com/brandon-fryslie/cc-nerf-buster) — 26

Languages: TypeScript, Go, Shell, Python, HTML, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-06-21](./daily-archive/2026-06-21.md)
- [2026-06-20](./daily-archive/2026-06-20.md)
- [2026-06-19](./daily-archive/2026-06-19.md)
- [2026-06-18](./daily-archive/2026-06-18.md)
- [2026-06-17](./daily-archive/2026-06-17.md)
- [2026-06-16](./daily-archive/2026-06-16.md)
- [2026-06-15](./daily-archive/2026-06-15.md)

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

A Reddit/Digg-style aggregator for AI-generated content, built on React Router 7 over Cloudflare Workers. Recent week the Wishing Well render-fidelity track closed several substitution poles the directive prose couldn't enforce: move-7 `sceneForWish` keys on the template-discriminator type so a `{animal}` template can no longer reach the render as a live co-creature, exhaustive by construction with a future bypass becoming a compile error ([#224](https://github.com/brandon-fryslie/slopspot-web/pull/224)); move-6 appended a Dilettante whole-relic creed via migration 0043 ([#221](https://github.com/brandon-fryslie/slopspot-web/pull/221)); move-5 re-slots the wish-occasion recipe subject as the SCENE ([#220](https://github.com/brandon-fryslie/slopspot-web/pull/220)); identity-sacred floor v8 + GutterMonk fidelity creed closed swap-to-embalmed-substitute ([#219](https://github.com/brandon-fryslie/slopspot-web/pull/219)); render-fidelity `v2l` wired native embalm negative prompts on sdxl/ideogram ([#222](https://github.com/brandon-fryslie/slopspot-web/pull/222)) and `rom` typed the per-provider `supportsNegativePrompt` capability ([#223](https://github.com/brandon-fryslie/slopspot-web/pull/223)); `fork-80r.1` selected fork/breed pauses from a typed `ForkErrorCause` discriminator ([#212](https://github.com/brandon-fryslie/slopspot-web/pull/212)); deploy turned migrate-on-ship via a serialized build → migrate → upload sequence ([#210](https://github.com/brandon-fryslie/slopspot-web/pull/210)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — full config under `settings.json` via CLI override flags. Recent week theme/style menus migrated to the same `{{ menu }}` disclosure everything else uses, with a page-reset fold on toggle ([#134](https://github.com/promptctl/cc-candybar/pull/134)); paged menus now fit term width on every page via a `stripChromeCols(style)` reservation at the pagination seam ([#135](https://github.com/promptctl/cc-candybar/pull/135)); the dead session-random style-picker island was removed ([#136](https://github.com/promptctl/cc-candybar/pull/136)); `pdu.5` split menu inline/drop channels and derived menu identity from name so N independent menus can sit anywhere in a segment ([#133](https://github.com/promptctl/cc-candybar/pull/133)); `pdu.9` let horizontal `compose` stack drops with embeddable `{{ menu }}` ([#131](https://github.com/promptctl/cc-candybar/pull/131)); render burn-down — OSC-8 closure invariant, 45→2-col over-reserved width, per-part color serialization guard, `closeOnPick` default, group-toggle disclosure glyph ([#125](https://github.com/promptctl/cc-candybar/pull/125)–[#130](https://github.com/promptctl/cc-candybar/pull/130)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. Recent week added a prose-merge agent surface for a diverged clone — when a field-aware reconcile settles every code-owned field but a free-text field (title/description/agent_prompt) was rewritten on both sides, base/ours/theirs is surfaced and finalized via fingerprinted resolutions, with duplicate-key rejection and JSON-mode refusal in the reconcile handler ([#235](https://github.com/promptctl/links-issue-tracker/pull/235)); the `--json` flag was removed wholesale — text is the one canonical agent-readable surface ([#236](https://github.com/promptctl/links-issue-tracker/pull/236)); pure field-aware (base, ours, theirs) merge policy resolver ([#232](https://github.com/promptctl/links-issue-tracker/pull/232)) + linear-history field-aware reconcile for a diverged clone on top ([#233](https://github.com/promptctl/links-issue-tracker/pull/233)); quickstart now states lit tickets are agent-authored, not human-written ([#234](https://github.com/promptctl/links-issue-tracker/pull/234)); automatic inline receive lets an established clone see pushed tickets without a manual pull ([#231](https://github.com/promptctl/links-issue-tracker/pull/231)); sync survived online-GC contention with a staged-working-set proof ([#229](https://github.com/promptctl/links-issue-tracker/pull/229), [#230](https://github.com/promptctl/links-issue-tracker/pull/230)).

</td>
<td width="50%" valign="top">

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Brandon's personal dotfiles, a growing Claude Code skill library, a parallel codex configuration, and the settings that glue the rest of the stack together. Recent week the `tmux-command` skill became the canonical channel into other harnesses — built-in slash-command injection with codex and opencode command references populated, a shared target resolver with shorthand + window-by-name addressing, a `context` verb that moves the pane gather into the script, pane-read as the canonical first phase, and `tmux-help` stale-id detection + logging fixes; `hire-a-minion` spawns worktree-backed tmux minions and drives their slash commands through that same channel; the agent code-review action moved off the z.ai brand to `coding-agent-review` and the `agent-code-review-setup` skill was pointed at it with DeepSeek credential provisioning; `address-pr-reviews` had its provider renamed from zai to action and now uptakes reviewer updates in preflight; new always-on `prompting` skill for LLM-authored prompts; `claude-code-power` on-demand reference skill landed; `pr-review` grew plan-first rounds + change-request dismissal + a finalize-session script ([#65](https://github.com/brandon-fryslie/dotfiles/pull/65)).

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

Paste/editor companion for slopspot content, with provenance carried from ingest. Recent week added a sticky bottom submit bar in the editor blocks view via a shared `submitControls()` fragment used by both toolbars ([#56](https://github.com/brandon-fryslie/slopspot-paste/pull/56)); the minimap rail finalized on the right side ([#57](https://github.com/brandon-fryslie/slopspot-paste/pull/57)); long bubbles clamp to 10 lines with CSS `:hover` owning transient lift and JS click-pin owning persistent state ([#55](https://github.com/brandon-fryslie/slopspot-paste/pull/55)); the cbm series reconstructed the subagent hierarchy and nested it recursively with a condensed tool-call model and per-tool primary-arg table on top ([#41](https://github.com/brandon-fryslie/slopspot-paste/pull/41)–[#48](https://github.com/brandon-fryslie/slopspot-paste/pull/48)); code blocks syntax-highlight at the `renderMarkdown` boundary ([#49](https://github.com/brandon-fryslie/slopspot-paste/pull/49)); long spine prose clamps with a measured-overflow Expand toggle ([#50](https://github.com/brandon-fryslie/slopspot-paste/pull/50)).

### [mit-design-notes](https://github.com/brandon-fryslie/mit-design-notes)
**HTML**

Typographic and motion specimens — a styles-only design notebook deployed to GitHub Pages. Recent week landed the styling-aj1 typographic specimen run from masthead through epilogue — the engraved cover plate, chronophotographic motion study, nesting chain, exploded assembly schematic, runway/terminal/gauge sticky window, trigger/bind oscilloscope, the loupe/stereo/turntable/deck/proof/anatomy/frequency/em/count/inked-line/kindling/full-bleed specimen plates ([#14](https://github.com/brandon-fryslie/mit-design-notes/pull/14)–[#38](https://github.com/brandon-fryslie/mit-design-notes/pull/38)), then the rack, shallow focus, reconstruction, data essay, nine-blade iris close, and paper-dissolving epilogue ([#39](https://github.com/brandon-fryslie/mit-design-notes/pull/39)–[#44](https://github.com/brandon-fryslie/mit-design-notes/pull/44)); the story-5rm voice pass + descent threshold + surfacing + closing thread ([#45](https://github.com/brandon-fryslie/mit-design-notes/pull/45)–[#48](https://github.com/brandon-fryslie/mit-design-notes/pull/48)); trueness-jj1 paints only the live window and broadens the contact-sheet ignore ([#49](https://github.com/brandon-fryslie/mit-design-notes/pull/49), [#50](https://github.com/brandon-fryslie/mit-design-notes/pull/50)).

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
