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

The Copilot reviewer went away overnight — a pricing change — and the answer was a one-day sweep. A new z.ai PR-review action installed across `slopspot-web`, `slopspot-paste`, and `rad-plugins`; a fresh `zai-pr-review` skill in `dotfiles`; `address-pr-reviews` retargeted from Copilot's session stream to z.ai's review-thread model, with most of its producer lifecycle deleted in the move. The skill's seam survived the vendor swap because the seam was always "open review threads," never the API on the other side.

`slopspot-paste` is new. It went from nothing to b48.1 through b48.7 in a single sitting — a block-based paste editor for chat transcripts. Typed Turn[] core, mobx + lit-html on top, the server's `/api/paste` re-arming on the same boundary, split/merge by caret offset, a stored-XSS fix at the end hardening renderMarkdown's HTML and link-href passes. The kind-conversion matrix collapsed to two total functions over a shared text projection. Brandon let that stand.

In `cc-candybar` the hue stepper had been advancing one step per render instead of per click. An absolute `wrap(current ± by)` snapshotted at render time was secretly idempotent between renders; the relative nudge it should have always been now rides in the URL.

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

*Updated June 9, 2026*

### Today

- `brandon-fryslie/slopspot-paste` — 9 commits: new repo. A block-based paste editor for chat transcripts shipped b48.1 through b48.7 — source-dropdown parsers + claude-share/JSONL ingestion + pure `renderTurns` ([#1](https://github.com/brandon-fryslie/slopspot-paste/pull/1)), DOM-free block model ([#2](https://github.com/brandon-fryslie/slopspot-paste/pull/2)), `/api/fetch` + `/api/paste` Turn[] arm with `isTurns()` boundary ([#3](https://github.com/brandon-fryslie/slopspot-paste/pull/3)), mobx EditorStore + lit-html view + mount boundary ([#4](https://github.com/brandon-fryslie/slopspot-paste/pull/4)), `index.astro` wired with editor CSS + no-JS fallback ([#5](https://github.com/brandon-fryslie/slopspot-paste/pull/5)), confirm-on-reparse + handle-drag + kind-conversion proof ([#6](https://github.com/brandon-fryslie/slopspot-paste/pull/6)), split/merge a block by text-range ([#7](https://github.com/brandon-fryslie/slopspot-paste/pull/7)); plus the z.ai PR-review action ([#8](https://github.com/brandon-fryslie/slopspot-paste/pull/8)) and a stored-XSS fix in `renderMarkdown` — raw HTML tokens escape to literal text, link/image hrefs pass a default-deny scheme allowlist ([#9](https://github.com/brandon-fryslie/slopspot-paste/pull/9)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-06-08)).
- `brandon-fryslie/rad-plugins` — 5 commits: z.ai PR-review action installed ([#8](https://github.com/brandon-fryslie/rad-plugins/pull/8)); `really-really-amend` no longer mutates persistent remote-URL config as a side effect of force push; the same helper now reads the authoritative `branch.<name>.remote` config value instead of parsing the abbrev-ref string (which broke for branch names containing slashes); `claad` restored as direct `claude --dangerously-skip-permissions`, `happy` repointed at homelab, `cclod`/`coplod` dropped; prompt tune-up ([commits](https://github.com/brandon-fryslie/rad-plugins/commits?author=brandon-fryslie&since=2026-06-08)).
- `brandon-fryslie/dotfiles` — 3 commits: `address-pr-reviews` retargeted from Copilot (gone, pricing change) to the z.ai Coding Agent Review action — `wait` blocks on the workflow run for the PR head SHA, `fetch` collapses to open review threads, `ensure`/`trigger` deleted; new `zai-pr-review` skill installs the action into a repo; the laws reworked ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-06-08)).
- `promptctl/links-issue-tracker` — 2 commits: framed root `CLAUDE.md`/`AGENTS.md` as dogfood examples (with a marker-only migration fix so `writeManagedFile` compares against original bytes, not post-migration content) ([#182](https://github.com/promptctl/links-issue-tracker/pull/182)); `mkdocs build --strict` now exits clean — phantom `guides/` paths repointed at real flat-`docs/` files ([#181](https://github.com/promptctl/links-issue-tracker/pull/181)).
- `brandon-fryslie/slopspot-web` — z.ai PR-review action installed ([#163](https://github.com/brandon-fryslie/slopspot-web/pull/163)).
- `promptctl/cc-candybar` — hue stepper `◀`/`▶` emit a relative step-state nudge instead of an absolute target — the old `wrap(current ± by)` baked a render-time `current` into the OSC-8 link and was secretly idempotent across renders; the relative `by` now rides the link and `current` is read live at apply time ([#86](https://github.com/promptctl/cc-candybar/pull/86)).
- `brandon-fryslie/chaperone-auth-gateway` — `ProcessConfig` + `SpawnChild` consolidated ~130 lines of duplicate process/env/banner code across `run` and `examine`; fixed a CA-env-vars bug in examine mode (3 vars → 10+); lint debt cleaned up by dropping an unused `io.Writer` seam ([#1](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/1)).

### This Week

- `brandon-fryslie/slopspot-web` — 55 commits: the Genome system L1–L7 + dynasty view + lineage-on-card landed early in the window, plus the Voice/Feud engine, the Growing-Cast Birth Engine + Birth Rite + Newcomer debut, the Heretic's recipe-deviation ballot, the Poet, the efficiency series (page-size cut, materialized score, cursor pagination, queue-isolated generation, edge-cached `/media`), the observability series (`/health`, CPU-tail Worker, smoke suite, Prometheus `/metrics`, VictoriaMetrics prober), the creative-governance corpus, and today's z.ai action install ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-06-02)).
- `brandon-fryslie/dotfiles` — 23 commits: today's Copilot→z.ai migration; earlier in the week, the `claude` skill `posse` absorbed remediation shapes + variance planning and `sheriff` absorbed the workaround audit; a sweep retired stale skills (`code-refactor`, `peekaboo`, the `zai` home-infra mirror); new skills landed — `copy-session-to-zai`, `slop-image` (local image generation), `share-slop` (uploads CC session JSONL to paste.slopspot.ai), `scroll-pinned-stepper` ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-06-02)).
- `promptctl/links-issue-tracker` — 20 commits: today's dogfood-framing of `CLAUDE.md`/`AGENTS.md` + marker-only migration fix ([#182](https://github.com/promptctl/links-issue-tracker/pull/182)) and `mkdocs --strict` cleanup ([#181](https://github.com/promptctl/links-issue-tracker/pull/181)); earlier — public-release paperwork (LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, CHANGELOG + release gate), the lane-scoped sequential gate ([#179](https://github.com/promptctl/links-issue-tracker/pull/179)), and the project-intent north star ([#180](https://github.com/promptctl/links-issue-tracker/pull/180)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-06-02)).
- `promptctl/cc-candybar` — 19 commits: today's stepper relative-nudge fix ([#86](https://github.com/promptctl/cc-candybar/pull/86)); earlier — the template-engine `bdi.1`–`bdi.4` formatter migration onto the DSL helper surface ([#78](https://github.com/promptctl/cc-candybar/pull/78)–[#81](https://github.com/promptctl/cc-candybar/pull/81)), the `widgets` module deleted (actions are the sole interaction authority) ([#72](https://github.com/promptctl/cc-candybar/pull/72)), JSON Schema export + lint CLI + vars/segments/config CLI ([#76](https://github.com/promptctl/cc-candybar/pull/76)), and the `dsl-loader` god-file decomposed by change-reason ([#73](https://github.com/promptctl/cc-candybar/pull/73)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-06-02)).
- `brandon-fryslie/slopspot-paste` — 9 commits: the b48.1–b48.7 block-editor build-out plus today's z.ai action install and the stored-XSS sanitization fix ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-06-02)).
- `brandon-fryslie/rad-plugins` — 5 commits: today's z.ai action install, the two `really-really-amend` fixes (no remote-URL mutation; authoritative remote-config read), and the `claad`/`happy`/`cclod`/`coplod` reshuffle ([commits](https://github.com/brandon-fryslie/rad-plugins/commits?author=brandon-fryslie&since=2026-06-02)).
- `brandon-fryslie/mit-design-notes` — 4 commits: the last duplicate motifs retired (reticle, scatter, deck minted; strict zero reached) ([#5](https://github.com/brandon-fryslie/mit-design-notes/pull/5)) and the scroll-pinned-stepper page added for Pages deployment ([#6](https://github.com/brandon-fryslie/mit-design-notes/pull/6)).
- `brandon-fryslie/iterm2-scripting-helper` — 2 commits: markdown docs migrated to the lit backlog.
- `brandon-fryslie/chaperone-auth-gateway` — `ProcessConfig`/`SpawnChild` consolidation across `run` and `examine` ([#1](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/1)).
- `brandon-fryslie/shader-playground` — 1 commit.

### This Month

555 commits across 14 repositories over the past 30 days. Top by volume:

- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 182 commits
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 87
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 61
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 61
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 42
- [`promptctl/promptctl`](https://github.com/promptctl/promptctl) — 39
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 31
- [`promptctl/go-template-js`](https://github.com/promptctl/go-template-js) — 17
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 17
- [`brandon-fryslie/rad-plugins`](https://github.com/brandon-fryslie/rad-plugins) — 9

Languages: TypeScript, Go, Shell.

---

<details>
<summary>Previous highlights</summary>

- [2026-06-05](./daily-archive/2026-06-05.md)
- [2026-06-04](./daily-archive/2026-06-04.md)
- [2026-06-03](./daily-archive/2026-06-03.md)
- [2026-06-02](./daily-archive/2026-06-02.md)
- [2026-06-01](./daily-archive/2026-06-01.md)
- [2026-05-31](./daily-archive/2026-05-31.md)
- [2026-05-30](./daily-archive/2026-05-30.md)

</details>

<!-- RECENT-ACTIVITY:END -->

---

## Selected Projects

<!-- SELECTED-PROJECTS:START -->
<table>
<tr>
<td width="50%" valign="top">

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code, with the full config living under `settings.json` via CLI override flags. Most recent work fixed the hue stepper to emit a relative step-state nudge instead of an absolute target — the old `wrap(current ± by)` baked render-time `current` into the OSC-8 link and was secretly idempotent across renders ([#86](https://github.com/promptctl/cc-candybar/pull/86)). Earlier landed the template-engine `bdi.1`–`bdi.4` formatter migration onto a DSL helper surface ([#78](https://github.com/promptctl/cc-candybar/pull/78)–[#81](https://github.com/promptctl/cc-candybar/pull/81)), deleted the `widgets` module on the grounds that `actions` are the sole interaction authority ([#72](https://github.com/promptctl/cc-candybar/pull/72)), added JSON Schema export + lint CLI + vars/segments/config CLI ([#76](https://github.com/promptctl/cc-candybar/pull/76)), and decomposed the `dsl-loader` god-file by change-reason ([#73](https://github.com/promptctl/cc-candybar/pull/73)).

### [slopspot-web](https://github.com/brandon-fryslie/slopspot-web)
**TypeScript**

A Reddit/Digg-style aggregator for AI-generated content, built on React Router 7 over Cloudflare Workers. Most recent work installed the z.ai PR-review action ([#163](https://github.com/brandon-fryslie/slopspot-web/pull/163)). Earlier in the window the Genome system landed in seven labeled layers — recipe→Genome + lineage DAG through the dynasty view at `/dynasty/:id` ([#115](https://github.com/brandon-fryslie/slopspot-web/pull/115)–[#157](https://github.com/brandon-fryslie/slopspot-web/pull/157)) — along with the Voice/Feud engine ([#130](https://github.com/brandon-fryslie/slopspot-web/pull/130), [#134](https://github.com/brandon-fryslie/slopspot-web/pull/134), [#144](https://github.com/brandon-fryslie/slopspot-web/pull/144), [#151](https://github.com/brandon-fryslie/slopspot-web/pull/151)), the Growing-Cast Birth Engine ([#146](https://github.com/brandon-fryslie/slopspot-web/pull/146)) with the Birth Rite ([#154](https://github.com/brandon-fryslie/slopspot-web/pull/154)) and Newcomer debut ([#156](https://github.com/brandon-fryslie/slopspot-web/pull/156)), the Poet ([#152](https://github.com/brandon-fryslie/slopspot-web/pull/152)), the Heretic's recipe-deviation ballot ([#141](https://github.com/brandon-fryslie/slopspot-web/pull/141)), the efficiency series (page-size cut, materialized score, cursor pagination, queue-isolated generation, edge-cached `/media`), and an observability suite (`/health`, CPU-tail Worker, smoke suite, Prometheus `/metrics`, VictoriaMetrics prober).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. Most recent work framed root `CLAUDE.md`/`AGENTS.md` as dogfood examples with a marker-only migration fix in `writeManagedFile` — the change signal now compares against original bytes, not post-migration content ([#182](https://github.com/promptctl/links-issue-tracker/pull/182)) — and brought `mkdocs build --strict` to a clean exit by repointing phantom `guides/` paths at the real flat-`docs/` files ([#181](https://github.com/promptctl/links-issue-tracker/pull/181)). Earlier landed the public-release paperwork (MIT LICENSE + README License section, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, CHANGELOG with a release-script gate) ([#173](https://github.com/promptctl/links-issue-tracker/pull/173)–[#178](https://github.com/promptctl/links-issue-tracker/pull/178)), the epic-view renderer + cross-epic deps + `lit show` wiring ([#170](https://github.com/promptctl/links-issue-tracker/pull/170)–[#172](https://github.com/promptctl/links-issue-tracker/pull/172)), the lane-scoped sequential gate ([#179](https://github.com/promptctl/links-issue-tracker/pull/179)), and the project-intent north star ([#180](https://github.com/promptctl/links-issue-tracker/pull/180)).

</td>
<td width="50%" valign="top">

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Brandon's personal shell dotfiles, a growing Claude Code skill library, a parallel codex configuration, and the settings that glue the rest of the stack together. Most recent work retargeted `address-pr-reviews` from Copilot (gone, pricing change) to the z.ai Coding Agent Review action — `wait` now blocks on the workflow run for the PR head SHA, `fetch` collapses to open review threads, `ensure`/`trigger` deleted — and added a `zai-pr-review` skill that installs the action into a repo. Earlier the `claude` `posse` skill absorbed remediation shapes and variance planning, `sheriff` absorbed the workaround audit, a sweep retired stale skills (`code-refactor`, `peekaboo`, the `zai` home-infra mirror), and new skills landed: `copy-session-to-zai`, `slop-image` (local image generation), `share-slop` (uploads CC session JSONL to paste.slopspot.ai), `scroll-pinned-stepper`.

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control-mode protocol. Most recent work shipped the byte-codec series — a portable byte-faithful codec ([#62](https://github.com/promptctl/tmux-control-mode-js/pull/62)) routed through every transport as the single enforcer ([#63](https://github.com/promptctl/tmux-control-mode-js/pull/63)), backed by a cross-transport faithfulness contract ([#64](https://github.com/promptctl/tmux-control-mode-js/pull/64)) and `CommandResponse.output` contract docs ([#65](https://github.com/promptctl/tmux-control-mode-js/pull/65)); the library API surface spec landed at §26 ([#60](https://github.com/promptctl/tmux-control-mode-js/pull/60)) and was then reduced to a protocol-only guard ([#66](https://github.com/promptctl/tmux-control-mode-js/pull/66)); and `attachLineSink` with a shared per-pane decoder was added on top ([#67](https://github.com/promptctl/tmux-control-mode-js/pull/67)).

### [go-template-js](https://github.com/promptctl/go-template-js)
**TypeScript · MIT**

Go template syntax with a Sprig subset, generic over the output type, in TypeScript. The DSL helper surface powering the `cc-candybar` `bdi.1`–`bdi.4` formatter migration is built on this library, so much of cc-candybar's recent work is implicitly a downstream test. Heavy commit activity earlier in the 90-day window with a quieter recent stretch as cc-candybar consumed the resulting API.

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
