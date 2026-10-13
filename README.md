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

A scope question runs through today's commits across three repos. In `rich-js`, nine demos stopped being wired through an iframe harness and became a single `main.ts` each — same program, two entry files: one for the card in the browser, one for the terminal. The library is imported by its published names, not by relative paths. One contract, two homes.

Over in `cc-candybar`, the config stopped replacing itself on the way up. A project file now layers over the user file; every file found is a layer, and a durable click refuses to write what a layer above would hide, naming that layer. Plugins arrived in the same shape: every name a plugin declares lives under `plugins.<plugin>.`, so a drop only ever owns names under it.

In `links-issue-tracker`, a follow-up stopped being filed under the ticket it followed up. It's filed beside it now, with its own `follows_up` column — the link is a fact about the pair, not a tree position.

Brandon merged each of them in order, without pointing out they rhymed.

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

*Updated October 13, 2026*

### Last 24 Hours

- `brandon-fryslie/rich-js` — docs card epic concludes — eight demos (rich-markup-plugins, rich-viewport, themes-and-color-studio, rich-config, rich-template-bindings, rich-explore, rich-dash, claude-sessions) each collapsed to a single `main.ts` entry, library imported by its published names, Node and browser hosts sharing one contract ([#363](https://github.com/brandon-fryslie/rich-js/pull/363)–[#370](https://github.com/brandon-fryslie/rich-js/pull/370)); terminal-host demo replaces the BrowserTerminalHost harness, run on NodeTerminalHost for the card and BrowserTerminalHost for the embed ([#371](https://github.com/brandon-fryslie/rich-js/pull/371)); iframe demo shell deleted — `demos.json`, `_browser-shell` templates and `demos:build` gone, `demoNames()` the one list the sidebar, routes, Demos index and e2e gate read ([#372](https://github.com/brandon-fryslie/rich-js/pull/372)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-10-12)).
- `promptctl/cc-candybar` — plugins epic — apps ship segments as plugin definitions a config lists, data lives in a watched JSON file the app rewrites, every plugin name namespaced under `plugins.<plugin>.` so a drop only owns names under it ([#319](https://github.com/promptctl/cc-candybar/pull/319)); a watched file whose directories appear after load is read when written, nearestWatchTarget re-arms one level deeper as each missing directory appears ([#320](https://github.com/promptctl/cc-candybar/pull/320)); a project config layers over the user config instead of replacing it, every file found a layer merged through the bundled default, a durable click refusing to write what a layer above would hide ([#321](https://github.com/promptctl/cc-candybar/pull/321)); installed plugins discovered from `$XDG_DATA_DIRS`, `$XDG_DATA_HOME` and `<repo>/.cc-candybar/plugins` with the folder's name as the plugin's ([#322](https://github.com/promptctl/cc-candybar/pull/322)); each plugin checked by its own declarations, not the full validateConfig — 65 ms per load down to 1.2 ms ([#323](https://github.com/promptctl/cc-candybar/pull/323)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-10-12)).
- `promptctl/links-issue-tracker` — event-store charter owner amendments: lit reads and writes git objects in-process through a permissive library and never runs a subprocess, lit's data lives in its own object database under the git common dir, and an explicit purge is the one write that removes a ticket's events ([#605](https://github.com/promptctl/links-issue-tracker/pull/605)); `lit followup` files the follow-up beside the ticket it follows up, not under it, via a new `issues.follows_up` column with migration 00006 backfilling from existing parent edges and climbing to the nearest open or epic ancestor ([#606](https://github.com/promptctl/links-issue-tracker/pull/606)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-10-12)).

### This Week

- `promptctl/vhid` — 74 commits: human-hands epic — pointer verbs take a box with aim held to the line of travel by a Kalman update ([#158](https://github.com/promptctl/vhid/pull/158), [#163](https://github.com/promptctl/vhid/pull/163)); pointer moves vary like a hand's with overshoot, a bow drawn from the move's seed, and a faint tremor ([#159](https://github.com/promptctl/vhid/pull/159), [#164](https://github.com/promptctl/vhid/pull/164)); typing comes in bursts with rollover ([#152](https://github.com/promptctl/vhid/pull/152), [#156](https://github.com/promptctl/vhid/pull/156)); clicks rest, hold, and space a double-click like a hand ([#151](https://github.com/promptctl/vhid/pull/151)); click and key-repeat timings read the HID system's one setting ([#153](https://github.com/promptctl/vhid/pull/153)); the probe page logs wheel events and carries a hover-intent menu with a live record of every verb on studious ([#154](https://github.com/promptctl/vhid/pull/154), [#161](https://github.com/promptctl/vhid/pull/161)); `eyes` prints each match's box beside its centre, cut to where the system's hit test lands ([#157](https://github.com/promptctl/vhid/pull/157), [#160](https://github.com/promptctl/vhid/pull/160)); every rectangle `eyes` prints takes the `--rect` form ([#162](https://github.com/promptctl/vhid/pull/162)); a cancelled reading timed from the cancel so a loaded runner no longer fails the test ([#165](https://github.com/promptctl/vhid/pull/165)) ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-10-06)).
- `brandon-fryslie/gh-pages-multiplexer` — 65 commits: new repo stood up and run through its gauntlet — concurrent deploys rebuild from the probed tip, per-slot concurrency groups, token kept out of process args and `.git/config`, publish retries bounded by deadline ([#1](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/1)–[#5](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/5)); nav widget refreshed in every slot, PR cleanup correctness, storage namespace per slot ([#6](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/6)–[#11](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/11)); slot names URL-safe by construction, sitemap percent-encoding, canonical URLs stop pointing at 404s ([#12](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/12)–[#14](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/14)); `check:dist` gate, ref-patterns match ref name, test git identity ([#15](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/15)–[#19](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/19)) ([commits](https://github.com/brandon-fryslie/gh-pages-multiplexer/commits?author=brandon-fryslie&since=2026-10-06)).
- `promptctl/cc-hands` — 62 commits: install one-command — a bare Mac to a running hands with the person's only act an Input Monitoring grant, Claude Code's first-run questions and login asked in-line, the plugin installed from a local marketplace ([#273](https://github.com/promptctl/cc-hands/pull/273)–[#276](https://github.com/promptctl/cc-hands/pull/276), [#278](https://github.com/promptctl/cc-hands/pull/278), [#282](https://github.com/promptctl/cc-hands/pull/282), [#291](https://github.com/promptctl/cc-hands/pull/291)); hands.app — runs hands and holds its macOS grants, gated to a live subscription, a setup window asks each permission in turn, never asks to be the active app, setup decided in a Swift library tested against a Privacy fake ([#285](https://github.com/promptctl/cc-hands/pull/285), [#289](https://github.com/promptctl/cc-hands/pull/289), [#293](https://github.com/promptctl/cc-hands/pull/293), [#294](https://github.com/promptctl/cc-hands/pull/294)); tests: app tests run only paths that draw nothing, twelve window-raising paths removed ([#292](https://github.com/promptctl/cc-hands/pull/292)); voice — tell the user's voice from someone else's in the room, named voiceprints with only the owner acting, a hold the voice opened cuts hands off on first words heard ([#277](https://github.com/promptctl/cc-hands/pull/277), [#279](https://github.com/promptctl/cc-hands/pull/279), [#280](https://github.com/promptctl/cc-hands/pull/280)); brain answers theme and trust itself so first-run asks only login ([#283](https://github.com/promptctl/cc-hands/pull/283)); docs rewritten in plain technical English, tested at designed interfaces with fakes ([#284](https://github.com/promptctl/cc-hands/pull/284), [#287](https://github.com/promptctl/cc-hands/pull/287)) ([commits](https://github.com/promptctl/cc-hands/commits?author=brandon-fryslie&since=2026-10-06)).
- `brandon-fryslie/rich-js` — 37 commits: docs card epic — static examples became editable cards running in the browser with keyboard input, file tabs, slider playgrounds, and edits reaching a running program ([#351](https://github.com/brandon-fryslie/rich-js/pull/351)–[#362](https://github.com/brandon-fryslie/rich-js/pull/362)); eight demos migrated to a single `main.ts` entry each and the iframe shell deleted ([#363](https://github.com/brandon-fryslie/rich-js/pull/363)–[#372](https://github.com/brandon-fryslie/rich-js/pull/372)); byte-for-byte reconciliation with Python's Rich across progress, table, rule, pretty, effects ([#346](https://github.com/brandon-fryslie/rich-js/pull/346)–[#348](https://github.com/brandon-fryslie/rich-js/pull/348), [#350](https://github.com/brandon-fryslie/rich-js/pull/350)); site xterm.js 5.3 → `@xterm/xterm` 6 ([#349](https://github.com/brandon-fryslie/rich-js/pull/349)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-10-06)).
- `promptctl/cc-candybar` — 7 commits: plugins epic — apps ship segments as plugin definitions a config lists, every plugin name under `plugins.<plugin>.`, installed plugins discovered from XDG and `<repo>/.cc-candybar/plugins` folders ([#319](https://github.com/promptctl/cc-candybar/pull/319), [#322](https://github.com/promptctl/cc-candybar/pull/322)); project config layers over the user config instead of replacing it ([#321](https://github.com/promptctl/cc-candybar/pull/321)); each plugin checked by its own declarations, 65 ms per load down to 1.2 ms ([#323](https://github.com/promptctl/cc-candybar/pull/323)); fragment style reads through the render's theme on rich-js 0.19.0 ([#316](https://github.com/promptctl/cc-candybar/pull/316)); session segment shows the lit ticket, its phase and epic progress ([#317](https://github.com/promptctl/cc-candybar/pull/317)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-10-06)).
- `brandon-fryslie/dotfiles` — 7 commits: claude settings split — a managed baseline deploys as settings Claude Code never writes, user file left to Claude Code, migration 0002 names the one-time cleanup ([#87](https://github.com/brandon-fryslie/dotfiles/pull/87)); Node trusts the full keychain bundle, bash shells get the trust env, `UV_SYSTEM_CERTS` joins the trust table, dead cc-nerf-buster CA lines dropped ([#86](https://github.com/brandon-fryslie/dotfiles/pull/86)); kitty-docs skill, codexapi provider, Pinokio-published skills ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-10-06)).
- `promptctl/links-issue-tracker` — 2 commits: event-store charter forbids subprocesses, keeps lit out of git, admits purge ([#605](https://github.com/promptctl/links-issue-tracker/pull/605)); `lit followup` files the follow-up beside the ticket, not under it, via a new `issues.follows_up` column ([#606](https://github.com/promptctl/links-issue-tracker/pull/606)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-10-06)).

### This Month

1000 commits across 13 repositories over the past 30 days. Top by volume:

- [`promptctl/vhid`](https://github.com/promptctl/vhid) — 262 commits
- [`promptctl/cc-hands`](https://github.com/promptctl/cc-hands) — 231
- [`brandon-fryslie/low-talker`](https://github.com/brandon-fryslie/low-talker) — 179
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 163
- [`brandon-fryslie/gh-pages-multiplexer`](https://github.com/brandon-fryslie/gh-pages-multiplexer) — 65
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 58
- [`promptctl/laws`](https://github.com/promptctl/laws) — 11
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 9
- [`promptctl/homebrew-tap`](https://github.com/promptctl/homebrew-tap) — 8
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 6

Languages: Swift, TypeScript, Python.

---

<details>
<summary>Previous highlights</summary>

- [2026-10-12](./daily-archive/2026-10-12.md)
- [2026-10-11](./daily-archive/2026-10-11.md)
- [2026-10-10](./daily-archive/2026-10-10.md)
- [2026-10-09](./daily-archive/2026-10-09.md)
- [2026-10-08](./daily-archive/2026-10-08.md)
- [2026-10-07](./daily-archive/2026-10-07.md)
- [2026-10-06](./daily-archive/2026-10-06.md)

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

A virtual keyboard and a virtual mouse for macOS, driven from a CLI or over MCP. Real HID devices through the pqrs DriverKit extension — no event taps, no Accessibility grant. 262 commits over the past month, 74 this week. The human-hands epic kept refining — pointer verbs take a box and press a point drawn inside it, aim held to the hand's line of travel by a Kalman update ([#158](https://github.com/promptctl/vhid/pull/158), [#163](https://github.com/promptctl/vhid/pull/163)); pointer moves vary like a hand's with overshoot and a bow drawn from the move's seed ([#159](https://github.com/promptctl/vhid/pull/159), [#164](https://github.com/promptctl/vhid/pull/164)); clicks rest, hold, and space a double-click like a hand ([#151](https://github.com/promptctl/vhid/pull/151)); typing comes in bursts with rollover ([#152](https://github.com/promptctl/vhid/pull/152), [#156](https://github.com/promptctl/vhid/pull/156)); click and key-repeat timings read the HID system's one setting ([#153](https://github.com/promptctl/vhid/pull/153)). `eyes` prints each match's box beside its centre, cut to where the system's hit test lands ([#157](https://github.com/promptctl/vhid/pull/157), [#160](https://github.com/promptctl/vhid/pull/160)); every rectangle it prints takes the `--rect` form ([#162](https://github.com/promptctl/vhid/pull/162)); a cancelled reading timed from the cancel so a loaded runner no longer fails the test ([#165](https://github.com/promptctl/vhid/pull/165)).

### [cc-hands](https://github.com/promptctl/cc-hands)
**Python · 1★**

Voice for Claude Code — speak to a session over a chord, hear its reply, run a brain that holds its own account on a dedicated Claude Code behind the proxy. 231 commits over the past month, 62 this week. Install one-command landed — one command takes a bare Mac to a running hands, Claude Code's first-run questions and login asked in-line, the plugin installs from a local marketplace in hands' own home so the accept-this-marketplace prompt stops gating an unattended run ([#273](https://github.com/promptctl/cc-hands/pull/273)–[#276](https://github.com/promptctl/cc-hands/pull/276), [#278](https://github.com/promptctl/cc-hands/pull/278), [#282](https://github.com/promptctl/cc-hands/pull/282), [#291](https://github.com/promptctl/cc-hands/pull/291)). `hands.app` runs hands and holds its macOS grants (gated to a live subscription), a setup window asks each permission in turn before hands runs, and the app never asks to be the active app so a launch does not take focus ([#285](https://github.com/promptctl/cc-hands/pull/285), [#289](https://github.com/promptctl/cc-hands/pull/289)). Setup decisions moved into a `HandsLogic` Swift package tested against a Privacy fake, and the twelve pytest paths that raised a real setup window on every run are gone ([#292](https://github.com/promptctl/cc-hands/pull/292), [#293](https://github.com/promptctl/cc-hands/pull/293), [#294](https://github.com/promptctl/cc-hands/pull/294)). Voice — tell the user's voice from someone else's in the room, named voiceprints with only the owner acting ([#277](https://github.com/promptctl/cc-hands/pull/277), [#279](https://github.com/promptctl/cc-hands/pull/279), [#280](https://github.com/promptctl/cc-hands/pull/280)).

### [low-talker](https://github.com/brandon-fryslie/low-talker)
**Swift**

Local push-to-talk dictation for macOS with a chord-selected command layer. 179 commits over the past month, none this week — the arc has settled. Earlier in the month the streaming arc landed — a press is decoded while the key is down, confirmed words commit while the press is open, dictation stays in the app its first words reached, streamed commits wait for settled punctuation ([#150](https://github.com/brandon-fryslie/low-talker/pull/150)–[#153](https://github.com/brandon-fryslie/low-talker/pull/153)); command mode leaves the code — an utterance becomes one thing, its text at the cursor ([#160](https://github.com/brandon-fryslie/low-talker/pull/160)); a HUD with listening/transcribing, Open at Login, Fn/Globe as the chord ([#161](https://github.com/brandon-fryslie/low-talker/pull/161)–[#168](https://github.com/brandon-fryslie/low-talker/pull/168)); audio under the audible floor answered as nothing said, `verbose_json` serves `avg_logprob` and `compression_ratio`, and an install from huggingface.co records the sizes the hub lists for the revision so a truncated file is fetched again instead of certified ([#169](https://github.com/brandon-fryslie/low-talker/pull/169)–[#171](https://github.com/brandon-fryslie/low-talker/pull/171)).

</td>
<td width="50%" valign="top">

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript · MIT**

A port of Python's Rich to TypeScript — markup, tables, trees, syntax, progress, tracebacks, Live, and an App runtime that routes focus and the pointer. 163 commits over the past month, 37 this week. The docs card epic concluded — static examples became editable cards running in the browser, with output re-rendered client-side, keyboard input, file tabs, slider playgrounds, and edits reaching a running program without restarting it ([#351](https://github.com/brandon-fryslie/rich-js/pull/351)–[#362](https://github.com/brandon-fryslie/rich-js/pull/362)); then every demo collapsed to a single `main.ts` entry importing the library by its published names, with a terminal-host demo replacing the old BrowserTerminalHost harness, and the iframe demo shell deleted — `demoNames()` is the one list the sidebar, routes, Demos index and e2e gate read ([#363](https://github.com/brandon-fryslie/rich-js/pull/363)–[#372](https://github.com/brandon-fryslie/rich-js/pull/372)). Byte-for-byte reconciliation with Python's Rich across progress, table, rule, pretty and effects ([#346](https://github.com/brandon-fryslie/rich-js/pull/346)–[#348](https://github.com/brandon-fryslie/rich-js/pull/348), [#350](https://github.com/brandon-fryslie/rich-js/pull/350)); site xterm.js 5.3 → `@xterm/xterm` 6 ([#349](https://github.com/brandon-fryslie/rich-js/pull/349)).

### [gh-pages-multiplexer](https://github.com/brandon-fryslie/gh-pages-multiplexer)
**TypeScript**

GitHub Action + CLI: deploy static sites to versioned subdirectories on gh-pages with auto index page, navigation widget, and PR previews. New repo last week, 65 commits since. Concurrent deploys rebuild from the probed tip instead of rebasing, deploy concurrency is keyed per version slot, token kept out of process args and `.git/config`, publish retries bounded by a 10-minute deadline ([#1](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/1)–[#5](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/5)). The nav widget refreshes in every slot and no second switcher appears inside iframes, storage namespace per slot, PR cleanup correctness ([#6](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/6)–[#11](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/11)); slot names URL-safe by construction, sitemap percent-encoding, canonical URLs stop pointing at 404s ([#12](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/12)–[#14](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/14)); `check:dist` gate on every PR, ref-patterns match the ref name, test git identity isolated ([#15](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/15)–[#19](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/19)).

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
