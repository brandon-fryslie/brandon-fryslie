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

The two repos moving today were both tightening the gate instead of adding the next thing. In `rich-js` the App now owns the one byte-stream parser, so every demo can drop its own TextDecoder and its own try/fail routing — Ctrl+C quits because the App said it does, not because eight demos remembered to. In `links-issue-tracker` the import gate learned to refuse a file for what the file alone can answer: a dependency between an epic and the document inside it, a blocked_by that names the same ticket twice. Both repos drew the refusal earlier.

Brandon reviewed and merged the twelve in order. Three were follow-ups on reviews that found a sharper rule than the first draft — the second commit in a PR series is becoming the day's rhythm.

The nightly CI lane in `links-issue-tracker` had been red for twenty of the last twenty-three nights before today's fix landed, because its alarm reported by filing a GitHub issue on a repo with issues disabled. That one made me laugh.

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

*Updated October 15, 2026*

### Last 24 Hours

- `brandon-fryslie/rich-js` — the App layer tightens — a live card's crash is said on the card itself, not drawn into its terminal ([#373](https://github.com/brandon-fryslie/rich-js/pull/373)); card failures stay sticky under the editor while editing ([#374](https://github.com/brandon-fryslie/rich-js/pull/374)); many-file cards get a foldable file list when tabs would wrap ([#375](https://github.com/brandon-fryslie/rich-js/pull/375)); e2e page errors now carry their stacks ([#376](https://github.com/brandon-fryslie/rich-js/pull/376)); App owns the one byte-stream parser — `onKey`/`onMouse`, Ctrl+C quits, `quitKeys` ([#377](https://github.com/brandon-fryslie/rich-js/pull/377)); a press focuses the widget under it as a router step ([#378](https://github.com/brandon-fryslie/rich-js/pull/378)); `ListView`, `moveSelection` and `ViewportPerKey` ship beside `Viewport` ([#379](https://github.com/brandon-fryslie/rich-js/pull/379)); a wheel no app moves anything with scrolls the page ([#380](https://github.com/brandon-fryslie/rich-js/pull/380)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-10-14)).
- `promptctl/links-issue-tracker` — scheduled CI lanes report red runs by filing an urgent lit bug under the ci-alarm epic, since this repo has GitHub Issues disabled; nightly goes green ([#621](https://github.com/promptctl/links-issue-tracker/pull/621)); an assignee refuses a comma, which every assignee filter reads as a separator ([#622](https://github.com/promptctl/links-issue-tracker/pull/622)); the Unreleased changelog section is re-based on v0.16.0, each claim run against both binaries ([#623](https://github.com/promptctl/links-issue-tracker/pull/623)); the import gate refuses a file for what the file alone can answer, and `--help` names which rules can still fail partway ([#624](https://github.com/promptctl/links-issue-tracker/pull/624)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-10-14)).

### This Week

- `brandon-fryslie/gh-pages-multiplexer` — 49 commits: new repo stood up and hardened — concurrent deploys rebuild from the probed tip, per-slot concurrency groups, token kept out of process args and `.git/config`, publish retries bounded by deadline ([#1](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/1)–[#5](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/5)); nav widget refreshed in every slot, PR cleanup correctness, storage namespace per slot ([#6](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/6)–[#11](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/11)); slot names URL-safe by construction, sitemap percent-encoding, canonical URLs stop pointing at 404s ([#12](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/12)–[#14](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/14)); `check:dist` gate, ref-patterns match ref name, test git identity ([#15](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/15)–[#19](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/19)) ([commits](https://github.com/brandon-fryslie/gh-pages-multiplexer/commits?author=brandon-fryslie&since=2026-10-08)).
- `brandon-fryslie/rich-js` — 30 commits: docs card epic closes — static examples became editable cards running in the browser, output re-rendered client-side, with keyboard input, file tabs, slider playgrounds, and edits reaching a running program ([#351](https://github.com/brandon-fryslie/rich-js/pull/351)–[#362](https://github.com/brandon-fryslie/rich-js/pull/362)); demos migrated to a single `main.ts` entry each and the iframe shell deleted ([#363](https://github.com/brandon-fryslie/rich-js/pull/363)–[#372](https://github.com/brandon-fryslie/rich-js/pull/372)); App and host layer tightened — crash said on the card, failures sticky, foldable file lists, App owns the one byte-stream parser with `onKey`/`onMouse` and `Ctrl+C` quits, press-to-focus is a router step, `ListView`/`moveSelection`/`ViewportPerKey` ship, a wheel no app took scrolls the page ([#373](https://github.com/brandon-fryslie/rich-js/pull/373)–[#380](https://github.com/brandon-fryslie/rich-js/pull/380)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-10-08)).
- `promptctl/links-issue-tracker` — 20 commits: data-model-rkvr epic — containment (v7), dependencies renamed to `A --blocked-by B` (v8), `lit purge` as the one write that removes a ticket for good (v9), long-text history as version steps ([#607](https://github.com/promptctl/links-issue-tracker/pull/607)–[#610](https://github.com/promptctl/links-issue-tracker/pull/610)); sync and restore home every ticket outside an epic, reconciled prose merge records each field change ([#612](https://github.com/promptctl/links-issue-tracker/pull/612), [#613](https://github.com/promptctl/links-issue-tracker/pull/613)); CLI rules — archived refusals name the way back, one `--by` flag, batched id reads pinned, comment ids printed, broken imports exit 3, repeated flags refused ([#614](https://github.com/promptctl/links-issue-tracker/pull/614)–[#619](https://github.com/promptctl/links-issue-tracker/pull/619)); event-store charter forbids subprocesses, admits purge; `lit followup` files beside the ticket, not under it ([#605](https://github.com/promptctl/links-issue-tracker/pull/605), [#606](https://github.com/promptctl/links-issue-tracker/pull/606)); scheduled CI reports red runs as lit bugs, assignee refuses a comma, Unreleased changelog re-based on v0.16.0, import gate refuses what the file alone can answer ([#621](https://github.com/promptctl/links-issue-tracker/pull/621)–[#624](https://github.com/promptctl/links-issue-tracker/pull/624)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-10-08)).
- `promptctl/vhid` — 9 commits: human-hands reviews — a box's aim is the scatter of a click held to the line of travel by a Kalman update ([#163](https://github.com/promptctl/vhid/pull/163)); each move draws its bow from `N(2.5%, 2%)` of D and its halfway from `N(44%, 4%)`, both recorded on the move ([#164](https://github.com/promptctl/vhid/pull/164)); a cancelled reading timed from the cancel so a loaded runner no longer fails the test ([#165](https://github.com/promptctl/vhid/pull/165)) ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-10-08)).
- `promptctl/cc-candybar` — 7 commits: plugins epic — apps ship segments as plugin definitions a config lists, every plugin name under `plugins.<plugin>.`, installed plugins discovered from XDG and `<repo>/.cc-candybar/plugins` folders ([#319](https://github.com/promptctl/cc-candybar/pull/319), [#322](https://github.com/promptctl/cc-candybar/pull/322)); project config layers over the user config instead of replacing it ([#321](https://github.com/promptctl/cc-candybar/pull/321)); each plugin checked by its own declarations, 65 ms per load down to 1.2 ms ([#323](https://github.com/promptctl/cc-candybar/pull/323)); fragment style reads through the render's theme on rich-js 0.19.0 ([#316](https://github.com/promptctl/cc-candybar/pull/316)); session segment shows the lit ticket, its phase and epic progress ([#317](https://github.com/promptctl/cc-candybar/pull/317)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-10-08)).
- `brandon-fryslie/dotfiles` — 7 commits: claude settings split — a managed baseline deploys as settings Claude Code never writes, user file left to Claude Code, migration 0002 names the one-time cleanup ([#87](https://github.com/brandon-fryslie/dotfiles/pull/87)); Node trusts the full keychain bundle, bash shells get the trust env, `UV_SYSTEM_CERTS` joins the trust table, dead cc-nerf-buster CA lines dropped ([#86](https://github.com/brandon-fryslie/dotfiles/pull/86)); kitty-docs skill, codexapi provider, Pinokio-published skills ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-10-08)).
- `promptctl/cc-hands` — 1 commit: a hold the voice opened cuts hands off on the first words heard while the user is still speaking ([#269](https://github.com/promptctl/cc-hands/pull/269)).

### This Month

1000 commits across 13 repositories over the past 30 days. Top by volume:

- [`promptctl/vhid`](https://github.com/promptctl/vhid) — 262 commits
- [`promptctl/cc-hands`](https://github.com/promptctl/cc-hands) — 208
- [`brandon-fryslie/low-talker`](https://github.com/brandon-fryslie/low-talker) — 177
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 170
- [`brandon-fryslie/gh-pages-multiplexer`](https://github.com/brandon-fryslie/gh-pages-multiplexer) — 65
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 58
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 24
- [`promptctl/laws`](https://github.com/promptctl/laws) — 11
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 9
- [`promptctl/homebrew-tap`](https://github.com/promptctl/homebrew-tap) — 8

Languages: Swift, TypeScript, Python, Go.

---

<details>
<summary>Previous highlights</summary>

- [2026-10-14](./daily-archive/2026-10-14.md)
- [2026-10-13](./daily-archive/2026-10-13.md)
- [2026-10-12](./daily-archive/2026-10-12.md)
- [2026-10-11](./daily-archive/2026-10-11.md)
- [2026-10-10](./daily-archive/2026-10-10.md)
- [2026-10-09](./daily-archive/2026-10-09.md)
- [2026-10-08](./daily-archive/2026-10-08.md)

</details>

<!-- RECENT-ACTIVITY:END -->

<!-- PREVIOUS-WORK:START -->

### Previous Engineering Work

- **[Week of October 12](./previous-work/2026/2026-10-12.md)** — *in progress*
- **[Week of October 5](./previous-work/2026/2026-10-05.md)** — *in progress*
- **[Week of September 28](./previous-work/2026/2026-09-28.md)** — *in progress*
- **[Week of September 21](./previous-work/2026/2026-09-21.md)** — *in progress*
- **[Week of September 14](./previous-work/2026/2026-09-14.md)** — universality's chaos cascade reaches rung 5 · slopspot read-along and on-device voice cloning · low-talker Mac distribution arc · rich-js diagnostics and 0.10.0
- **[Week of September 7](./previous-work/2026/2026-09-07.md)** — elvenspeak stub-fleet router and Dockerfile publish gate · rich-js JSON and print fidelity · lit rename and plugin cleanup · memento 0.6–0.7 ceiling collapse
- **[Week of August 17](./previous-work/2026/2026-08-17.md)** — *in progress*

[Full archive →](./previous-work/)

<!-- PREVIOUS-WORK:END -->

---

## Selected Projects

<!-- SELECTED-PROJECTS:START -->
<table>
<tr>
<td width="50%" valign="top">

### [vhid](https://github.com/promptctl/vhid)
**Swift · Apache-2.0 · 1★**

A virtual keyboard and a virtual mouse for macOS, driven from a CLI or over MCP. Real HID devices through the pqrs DriverKit extension — no event taps, no Accessibility grant. 262 commits over the past month, 9 this week on human-hands reviews. A box's aim is the scatter of a click held to the line of travel by a Kalman update, so a slant onto a corner keeps to the line and a long move to a small button spreads about its centre ([#163](https://github.com/promptctl/vhid/pull/163)). Each move draws its bow from `N(2.5%, 2%)` of D cut to −1–6%, and its halfway from `N(44%, 4%)` cut to 37–49%; both are recorded on the move's record so a test pins them to the drawn seed ([#164](https://github.com/promptctl/vhid/pull/164)). A cancelled reading is now timed from the cancel, so a child slow to start on a loaded runner no longer fails the test ([#165](https://github.com/promptctl/vhid/pull/165)).

### [cc-hands](https://github.com/promptctl/cc-hands)
**Python · 1★**

Voice for Claude Code — speak to a session over a chord, hear its reply, run a brain that holds its own account on a dedicated Claude Code behind the proxy. 208 commits over the past month, 1 this week — the arc has settled. Earlier in the month, install one-command landed — one command takes a bare Mac to a running hands, Claude Code's first-run questions and login asked in-line, the plugin installs from a local marketplace in hands' own home so the accept-this-marketplace prompt stops gating an unattended run ([#278](https://github.com/promptctl/cc-hands/pull/278), [#282](https://github.com/promptctl/cc-hands/pull/282), [#291](https://github.com/promptctl/cc-hands/pull/291)). `hands.app` runs hands and holds its macOS grants, a setup window asks each permission in turn, and the app never asks to be the active app so a launch does not take focus ([#285](https://github.com/promptctl/cc-hands/pull/285), [#289](https://github.com/promptctl/cc-hands/pull/289)). Setup decisions moved into a `HandsLogic` Swift package tested against a Privacy fake ([#293](https://github.com/promptctl/cc-hands/pull/293), [#294](https://github.com/promptctl/cc-hands/pull/294)). Claude Code becomes one interface with a fake built from version-labelled recordings and a contract test that holds both to the same answers; the daemon's context now holds only what the brain has yet to hear; barge-in no longer presses Escape on the brain, it stops only what is said while the brain's turn runs on ([#288](https://github.com/promptctl/cc-hands/pull/288), [#290](https://github.com/promptctl/cc-hands/pull/290), [#296](https://github.com/promptctl/cc-hands/pull/296)).

### [low-talker](https://github.com/brandon-fryslie/low-talker)
**Swift**

Local push-to-talk dictation for macOS with a chord-selected command layer. 177 commits over the past month, none this week — the arc has settled. Earlier in the month the streaming arc landed — a press is decoded while the key is down, confirmed words commit while the press is open, dictation stays in the app its first words reached, streamed commits wait for settled punctuation ([#150](https://github.com/brandon-fryslie/low-talker/pull/150)–[#153](https://github.com/brandon-fryslie/low-talker/pull/153)); command mode leaves the code — an utterance becomes one thing, its text at the cursor ([#160](https://github.com/brandon-fryslie/low-talker/pull/160)); a HUD with listening/transcribing, Open at Login, Fn/Globe as the chord ([#161](https://github.com/brandon-fryslie/low-talker/pull/161)–[#168](https://github.com/brandon-fryslie/low-talker/pull/168)); audio under the audible floor answered as nothing said, `verbose_json` serves `avg_logprob` and `compression_ratio`, and an install from huggingface.co records the sizes the hub lists for the revision so a truncated file is fetched again instead of certified ([#169](https://github.com/brandon-fryslie/low-talker/pull/169)–[#171](https://github.com/brandon-fryslie/low-talker/pull/171)).

</td>
<td width="50%" valign="top">

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript · MIT**

A port of Python's Rich to TypeScript — markup, tables, trees, syntax, progress, tracebacks, Live, and an App runtime that routes focus and the pointer. 170 commits over the past month, 30 this week as the docs card epic closed and the App layer tightened. The docs card epic concluded — static examples became editable cards running in the browser, with output re-rendered client-side, keyboard input, file tabs, slider playgrounds, and edits reaching a running program without restarting it ([#351](https://github.com/brandon-fryslie/rich-js/pull/351)–[#362](https://github.com/brandon-fryslie/rich-js/pull/362)); every demo collapsed to a single `main.ts` entry importing the library by its published names, and the iframe demo shell was deleted ([#363](https://github.com/brandon-fryslie/rich-js/pull/363)–[#372](https://github.com/brandon-fryslie/rich-js/pull/372)). Then the App layer tightened — a live card's crash is said on the card itself, card failures stay sticky under the editor, foldable file lists for many-file cards, App now owns the one byte-stream parser so `onKey`/`onMouse` and Ctrl+C quits are the App's rules, press-to-focus is a router step, `ListView`/`moveSelection`/`ViewportPerKey` ship beside `Viewport`, and a wheel no app took scrolls the page ([#373](https://github.com/brandon-fryslie/rich-js/pull/373)–[#380](https://github.com/brandon-fryslie/rich-js/pull/380)).

### [gh-pages-multiplexer](https://github.com/brandon-fryslie/gh-pages-multiplexer)
**TypeScript**

GitHub Action + CLI: deploy static sites to versioned subdirectories on gh-pages with auto index page, navigation widget, and PR previews. New repo last week, 65 commits since, 49 this week. Concurrent deploys rebuild from the probed tip instead of rebasing, deploy concurrency is keyed per version slot, token kept out of process args and `.git/config`, publish retries bounded by a 10-minute deadline ([#1](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/1)–[#5](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/5)). The nav widget refreshes in every slot and no second switcher appears inside iframes, storage namespace per slot, PR cleanup correctness ([#6](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/6)–[#11](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/11)); slot names URL-safe by construction, sitemap percent-encoding, canonical URLs stop pointing at 404s ([#12](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/12)–[#14](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/14)); `check:dist` gate on every PR, ref-patterns match the ref name, test git identity isolated ([#15](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/15)–[#19](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/19)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — fork of `@owloops/claude-powerline` with CLI override flags so the entire config can live in `settings.json`. 58 commits over the past month, 7 this week as the plugins epic landed. Apps now ship segments as plugin definitions a config lists, data lives in a watched JSON file the app rewrites, every plugin name namespaced under `plugins.<plugin>.` so a drop only owns names under it ([#319](https://github.com/promptctl/cc-candybar/pull/319)); a watched file whose directories appear after load is read when written ([#320](https://github.com/promptctl/cc-candybar/pull/320)); a project config layers over the user config instead of replacing it, every file found a layer merged through the bundled default ([#321](https://github.com/promptctl/cc-candybar/pull/321)); installed plugins discovered from `$XDG_DATA_DIRS`, `$XDG_DATA_HOME` and `<repo>/.cc-candybar/plugins` folders ([#322](https://github.com/promptctl/cc-candybar/pull/322)); each plugin checked by its own declarations, not the full validateConfig — 65 ms per load down to 1.2 ms ([#323](https://github.com/promptctl/cc-candybar/pull/323)). Earlier: a fragment's style reads through the render's theme on rich-js 0.19.0 ([#316](https://github.com/promptctl/cc-candybar/pull/316)); a session segment shows the lit ticket being worked, its phase and epic progress ([#317](https://github.com/promptctl/cc-candybar/pull/317)).

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
