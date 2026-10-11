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

The pattern I've been noticing in `cc-hands` is that it stopped being a voice project a week ago. Nothing new teaches it to listen, nothing new picks a model. The branch names say install, app, docs, monetization — and the diffs underneath are shell scripts, permission prompts, keychain handling, launchd plists. A voice-for-Claude-Code product turning, PR by PR, into a packaging problem.

Today the shape held. The one-command installer learned to install hands' own plugin from a local marketplace rather than one on GitHub, so Claude Code's accept-this-marketplace prompt stops gating an unattended run. A setup window asks for Microphone and Input Monitoring in turn before hands runs. The app no longer takes focus on launch — `NSApp.activate(ignoringOtherApps:)` was pulling the person's current app forward seventy-nine times across one test run, and now it isn't. These are not voice features. They are what a shipped Mac app has to do.

In the margin, `dotfiles` grew the trust env Node and uv need behind Proxyman — six small commits, no PRs, Brandon's own machine. The week's labour has quietly skewed toward the thing closest to a release.

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

*Updated October 11, 2026*

### Last 24 Hours

- `promptctl/cc-hands` — install: hands installs its own Claude Code plugin from a local marketplace in its home, so Claude Code's accept-this-marketplace prompt stops gating an unattended run ([#291](https://github.com/promptctl/cc-hands/pull/291)); app: hands never asks to be the active app, so a launch behind the person's app does not take its focus ([#289](https://github.com/promptctl/cc-hands/pull/289)); hands.app: a setup window asks for Microphone and Input Monitoring in turn before hands runs ([#285](https://github.com/promptctl/cc-hands/pull/285)); install: a guided run, numbered steps, retried on the spot, written for the login shell ([#282](https://github.com/promptctl/cc-hands/pull/282)); brain: hands answers the brain's theme and trust itself, so its first run asks only its login ([#283](https://github.com/promptctl/cc-hands/pull/283)); docs: hands is tested at designed interfaces with fakes, not by runs on a copy of production ([#287](https://github.com/promptctl/cc-hands/pull/287)); docs rewritten in plain, standard technical English ([#284](https://github.com/promptctl/cc-hands/pull/284)) ([commits](https://github.com/promptctl/cc-hands/commits?author=brandon-fryslie&since=2026-10-10)).
- `brandon-fryslie/dotfiles` — certs: Node trusts the full keychain bundle, bash shells get the trust env, `UV_SYSTEM_CERTS` joins the TRUST_ENV table so ssh sessions get it, dead cc-nerf-buster CA lines dropped ([#86](https://github.com/brandon-fryslie/dotfiles/pull/86)); agents: repo-scoped kitty-docs skill and repomix docs template, codexapi provider in claude settings, Pinokio-published gepeto and pinokio skills ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-10-10)).

### This Week

- `promptctl/cc-hands` — 117 commits: install one-command — a bare Mac to a running hands with the person's only act an Input Monitoring grant, Claude Code's first-run questions and login asked in-line, the plugin installed from a local marketplace ([#273](https://github.com/promptctl/cc-hands/pull/273)–[#276](https://github.com/promptctl/cc-hands/pull/276), [#278](https://github.com/promptctl/cc-hands/pull/278), [#282](https://github.com/promptctl/cc-hands/pull/282), [#291](https://github.com/promptctl/cc-hands/pull/291)); hands.app — runs hands and holds its macOS grants, gated to a live subscription, a setup window asks each permission in turn, never asks to be the active app ([#270](https://github.com/promptctl/cc-hands/pull/270), [#271](https://github.com/promptctl/cc-hands/pull/271), [#285](https://github.com/promptctl/cc-hands/pull/285), [#289](https://github.com/promptctl/cc-hands/pull/289)); voice — tell the user's voice from someone else's in the room, named voiceprints with only the owner acting, drive a session on the user's standing order, a hold the voice opened cuts hands off on first words heard ([#269](https://github.com/promptctl/cc-hands/pull/269), [#277](https://github.com/promptctl/cc-hands/pull/277), [#279](https://github.com/promptctl/cc-hands/pull/279), [#280](https://github.com/promptctl/cc-hands/pull/280)); tmux arc — hands starts a Claude Code session in a tmux window, reads its pane, closes via SIGTERM, status in tmux status line ([#242](https://github.com/promptctl/cc-hands/pull/242), [#256](https://github.com/promptctl/cc-hands/pull/256)–[#265](https://github.com/promptctl/cc-hands/pull/265)); raw-api collapse — hands reaches its model only through the brain, keyed Anthropic and OpenAI backends gone ([#268](https://github.com/promptctl/cc-hands/pull/268)); brain: answers theme and trust itself so first-run asks only login ([#283](https://github.com/promptctl/cc-hands/pull/283)); attention warns before Claude Code's own question timeout ([#272](https://github.com/promptctl/cc-hands/pull/272)); docs rewritten in plain technical English, tested at designed interfaces with fakes ([#284](https://github.com/promptctl/cc-hands/pull/284), [#287](https://github.com/promptctl/cc-hands/pull/287)) ([commits](https://github.com/promptctl/cc-hands/commits?author=brandon-fryslie&since=2026-10-04)).
- `promptctl/vhid` — 113 commits: human-hands epic — pointer verbs take a box with aim held to the line of travel by a Kalman update ([#158](https://github.com/promptctl/vhid/pull/158), [#163](https://github.com/promptctl/vhid/pull/163)); pointer moves vary like a hand's, with overshoot, a bow drawn from the move's seed, and a faint tremor ([#159](https://github.com/promptctl/vhid/pull/159), [#164](https://github.com/promptctl/vhid/pull/164)); typing comes in bursts with rollover ([#152](https://github.com/promptctl/vhid/pull/152), [#156](https://github.com/promptctl/vhid/pull/156)); clicks rest, hold, and space a double-click like a hand ([#151](https://github.com/promptctl/vhid/pull/151)); click and key-repeat timings read the HID system's one setting ([#153](https://github.com/promptctl/vhid/pull/153)); the probe page logs wheel events and carries a hover-intent menu, with a live record of every verb on studious ([#154](https://github.com/promptctl/vhid/pull/154), [#161](https://github.com/promptctl/vhid/pull/161)); `eyes` prints each match's box beside its centre, cut to where the system's hit test lands ([#157](https://github.com/promptctl/vhid/pull/157), [#160](https://github.com/promptctl/vhid/pull/160)); every rectangle `eyes` prints takes the `--rect` form ([#162](https://github.com/promptctl/vhid/pull/162)); a cancelled reading timed from the cancel so a loaded runner no longer fails the test ([#165](https://github.com/promptctl/vhid/pull/165)); a daemon whose file was replaced refuses to start a reader of another build ([#155](https://github.com/promptctl/vhid/pull/155)) ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-10-04)).
- `brandon-fryslie/gh-pages-multiplexer` — 65 commits: new repo stood up and run through its gauntlet — concurrent deploys rebuild from the probed tip, per-slot concurrency groups, token kept out of process args and `.git/config`, publish retries bounded by deadline ([#1](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/1)–[#5](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/5)); nav widget refreshed in every slot, PR cleanup correctness, storage namespace per slot ([#6](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/6)–[#11](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/11)); slot names URL-safe by construction, sitemap percent-encoding, canonical URLs stop pointing at 404s ([#12](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/12)–[#14](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/14)); `check:dist` gate, ref-patterns match ref name, test git identity ([#15](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/15)–[#19](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/19)) ([commits](https://github.com/brandon-fryslie/gh-pages-multiplexer/commits?author=brandon-fryslie&since=2026-10-04)).
- `brandon-fryslie/rich-js` — 28 commits: docs card epic — static examples became editable cards running in the browser, with keyboard input, file tabs, slider playgrounds, and edits reaching a running program ([#351](https://github.com/brandon-fryslie/rich-js/pull/351)–[#362](https://github.com/brandon-fryslie/rich-js/pull/362)); byte-for-byte reconciliation with Python's Rich across progress, table, rule, pretty, effects ([#343](https://github.com/brandon-fryslie/rich-js/pull/343), [#344](https://github.com/brandon-fryslie/rich-js/pull/344), [#346](https://github.com/brandon-fryslie/rich-js/pull/346)–[#348](https://github.com/brandon-fryslie/rich-js/pull/348), [#350](https://github.com/brandon-fryslie/rich-js/pull/350)); effect catalogue promoted to `src/` with a docs page, ProgressBar's pulse animates on the library's own clock ([#338](https://github.com/brandon-fryslie/rich-js/pull/338), [#340](https://github.com/brandon-fryslie/rich-js/pull/340)–[#342](https://github.com/brandon-fryslie/rich-js/pull/342), [#345](https://github.com/brandon-fryslie/rich-js/pull/345)); site xterm.js 5.3 → `@xterm/xterm` 6, 20-minute CI job timeout, per-slot docs concurrency ([#336](https://github.com/brandon-fryslie/rich-js/pull/336), [#339](https://github.com/brandon-fryslie/rich-js/pull/339), [#349](https://github.com/brandon-fryslie/rich-js/pull/349)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-10-04)).
- `promptctl/cc-candybar` — 22 commits: live bar on GitHub Pages replays Claude turns, `pnpm bar:web` for a browser terminal ([#296](https://github.com/promptctl/cc-candybar/pull/296), [#297](https://github.com/promptctl/cc-candybar/pull/297)); menu — every option setting is `◀ value ▶` opening a plain list, settings marked when they differ from default, charset and colour depth leave the settings menu, session tab gains `⎘ resume` and `↗ config`, autocompact control, alt theme turns hue every three cells along a row ([#298](https://github.com/promptctl/cc-candybar/pull/298), [#300](https://github.com/promptctl/cc-candybar/pull/300), [#302](https://github.com/promptctl/cc-candybar/pull/302), [#303](https://github.com/promptctl/cc-candybar/pull/303), [#306](https://github.com/promptctl/cc-candybar/pull/306), [#308](https://github.com/promptctl/cc-candybar/pull/308)); daemon reads the session's Claude Code, not daemon's env ([#299](https://github.com/promptctl/cc-candybar/pull/299)); doctor checks config and URL handler ([#311](https://github.com/promptctl/cc-candybar/pull/311), [#314](https://github.com/promptctl/cc-candybar/pull/314)); fragment style reads through the render's theme on rich-js 0.19.0 ([#316](https://github.com/promptctl/cc-candybar/pull/316)); session segment shows the lit ticket, its phase and epic progress ([#317](https://github.com/promptctl/cc-candybar/pull/317)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-10-04)).
- `brandon-fryslie/low-talker` — 9 commits: audio under the audible floor answered as nothing said, `verbose_json` serves `avg_logprob` and `compression_ratio`, an install from huggingface.co records the sizes the hub lists for the revision so a truncated file is fetched again ([#169](https://github.com/brandon-fryslie/low-talker/pull/169)–[#171](https://github.com/brandon-fryslie/low-talker/pull/171)) ([commits](https://github.com/brandon-fryslie/low-talker/commits?author=brandon-fryslie&since=2026-10-04)).
- `brandon-fryslie/dotfiles` — 6 commits: Node trusts the full keychain bundle, bash shells get the trust env, `UV_SYSTEM_CERTS` joins the trust table, dead cc-nerf-buster CA lines dropped ([#86](https://github.com/brandon-fryslie/dotfiles/pull/86)); kitty-docs skill, codexapi provider, Pinokio-published skills ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-10-04)).
- `promptctl/tmux-phoenix` — 5 commits: tmux-control's `Connection::open`, owned reader, typed targets; phoenix-core/capture/store graph; phoenix-store lock-free reads; phoenix-restore plan over symbolic refs ([#20](https://github.com/promptctl/tmux-phoenix/pull/20)–[#23](https://github.com/promptctl/tmux-phoenix/pull/23)) ([commits](https://github.com/promptctl/tmux-phoenix/commits?author=brandon-fryslie&since=2026-10-04)).
- `promptctl/homebrew-tap` — 2 commits: vhid cask updated through the shared release workflow ([#4](https://github.com/promptctl/homebrew-tap/pull/4)) ([commits](https://github.com/promptctl/homebrew-tap/commits?author=brandon-fryslie&since=2026-10-04)).
- `brandon-fryslie/swe4vibe-lab` — 2 commits: vocabulary sweep across the course — runnable example / broken version / fixed version, demo output labels matched; README closes on recurrence rather than a finite list ([commits](https://github.com/brandon-fryslie/swe4vibe-lab/commits?author=brandon-fryslie&since=2026-10-04)).
- `promptctl/laws` — 1 commit: law-evals parse-dont-validate and domain-language case sets, dilution/over-firing/hold-out controls, schema v3 frozen ([#94](https://github.com/promptctl/laws/pull/94)).

### This Month

1000+ commits across 13 repositories over the past 30 days. Top by volume:

- [`promptctl/vhid`](https://github.com/promptctl/vhid) — 262 commits
- [`promptctl/cc-hands`](https://github.com/promptctl/cc-hands) — 229
- [`brandon-fryslie/low-talker`](https://github.com/brandon-fryslie/low-talker) — 186
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 157
- [`brandon-fryslie/gh-pages-multiplexer`](https://github.com/brandon-fryslie/gh-pages-multiplexer) — 65
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 59
- [`promptctl/laws`](https://github.com/promptctl/laws) — 11
- [`promptctl/homebrew-tap`](https://github.com/promptctl/homebrew-tap) — 8
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 8
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 7

Languages: Swift, Python, TypeScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-10-10](./daily-archive/2026-10-10.md)
- [2026-10-09](./daily-archive/2026-10-09.md)
- [2026-10-08](./daily-archive/2026-10-08.md)
- [2026-10-07](./daily-archive/2026-10-07.md)
- [2026-10-06](./daily-archive/2026-10-06.md)
- [2026-10-03](./daily-archive/2026-10-03.md)
- [2026-10-02](./daily-archive/2026-10-02.md)

</details>

<!-- RECENT-ACTIVITY:END -->

<!-- PREVIOUS-WORK:START -->

### Previous Engineering Work

- **[Week of September 28](./previous-work/2026/2026-09-28.md)** — *in progress*
- **[Week of September 21](./previous-work/2026/2026-09-21.md)** — *in progress*
- **[Week of September 14](./previous-work/2026/2026-09-14.md)** — *in progress*
- **[Week of September 7](./previous-work/2026/2026-09-07.md)** — elvenspeak stub-fleet router and Dockerfile publish gate · rich-js JSON and print fidelity · lit rename and plugin cleanup · memento 0.6–0.7 ceiling collapse
- **[Week of August 17](./previous-work/2026/2026-08-17.md)** — *in progress*
- **[Week of August 10](./previous-work/2026/2026-08-10.md)** — slopspot RAG stack and freshness trail · cc-candybar per-segment palette overrides · lit sync safety and licensing clean-room · cc-dump Anthropic-only proxy consolidation
- **[Week of August 3](./previous-work/2026/2026-08-03.md)** — lit workflows 0.4.0 · cc-candybar option-domain seam and theme picker · slopspot-paste editor made editable end-to-end · room-eq-wizard-mcp surface completion

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

A virtual keyboard and a virtual mouse for macOS, driven from a CLI or over MCP. Real HID devices through the pqrs DriverKit extension — no event taps, no Accessibility grant. 262 commits over the past month, 113 this week. The human-hands epic kept refining — pointer verbs take a box and press a point drawn inside it, aim held to the hand's line of travel by a Kalman update ([#158](https://github.com/promptctl/vhid/pull/158), [#163](https://github.com/promptctl/vhid/pull/163)); pointer moves vary like a hand's with overshoot and a bow drawn from the move's seed ([#159](https://github.com/promptctl/vhid/pull/159), [#164](https://github.com/promptctl/vhid/pull/164)); clicks rest, hold, and space a double-click like a hand ([#151](https://github.com/promptctl/vhid/pull/151)); typing comes in bursts with rollover ([#152](https://github.com/promptctl/vhid/pull/152), [#156](https://github.com/promptctl/vhid/pull/156)); click and key-repeat timings read the HID system's one setting ([#153](https://github.com/promptctl/vhid/pull/153)). `eyes` prints each match's box beside its centre, cut to where the system's hit test lands ([#157](https://github.com/promptctl/vhid/pull/157), [#160](https://github.com/promptctl/vhid/pull/160)); every rectangle it prints takes the `--rect` form ([#162](https://github.com/promptctl/vhid/pull/162)); a daemon whose file was replaced refuses to start a reader of another build ([#155](https://github.com/promptctl/vhid/pull/155)).

### [cc-hands](https://github.com/promptctl/cc-hands)
**Python · 1★**

Voice for Claude Code — speak to a session over a chord, hear its reply, run a brain that holds its own account on a dedicated Claude Code behind the proxy. 229 commits over the past month, 117 this week. Install one-command landed — one command takes a bare Mac to a running hands, Claude Code's first-run questions and login asked in-line, and today the plugin installs from a local marketplace in hands' own home so the accept-this-marketplace prompt stops gating an unattended run ([#273](https://github.com/promptctl/cc-hands/pull/273)–[#276](https://github.com/promptctl/cc-hands/pull/276), [#278](https://github.com/promptctl/cc-hands/pull/278), [#282](https://github.com/promptctl/cc-hands/pull/282), [#291](https://github.com/promptctl/cc-hands/pull/291)). `hands.app` runs hands and holds its macOS grants (gated to a live subscription), a setup window asks each permission in turn before hands runs, and the app never asks to be the active app so a launch does not take focus ([#270](https://github.com/promptctl/cc-hands/pull/270), [#271](https://github.com/promptctl/cc-hands/pull/271), [#285](https://github.com/promptctl/cc-hands/pull/285), [#289](https://github.com/promptctl/cc-hands/pull/289)). Voice learned named voiceprints with only the owner acting, and a session can be driven on a standing order ([#277](https://github.com/promptctl/cc-hands/pull/277), [#279](https://github.com/promptctl/cc-hands/pull/279), [#280](https://github.com/promptctl/cc-hands/pull/280)). Raw-api collapse — hands reaches its model only through the brain, keyed Anthropic and OpenAI backends gone ([#268](https://github.com/promptctl/cc-hands/pull/268)).

### [low-talker](https://github.com/brandon-fryslie/low-talker)
**Swift**

Local push-to-talk dictation for macOS with a chord-selected command layer. 186 commits over the past month, 9 this week as the arc tapered. Earlier in the month the streaming arc landed — a press is decoded while the key is down, confirmed words commit while the press is open, dictation stays in the app its first words reached, streamed commits wait for settled punctuation ([#150](https://github.com/brandon-fryslie/low-talker/pull/150)–[#153](https://github.com/brandon-fryslie/low-talker/pull/153)); command mode leaves the code — an utterance becomes one thing, its text at the cursor ([#160](https://github.com/brandon-fryslie/low-talker/pull/160)); a HUD with listening/transcribing, Open at Login, Fn/Globe as the chord ([#161](https://github.com/brandon-fryslie/low-talker/pull/161)–[#168](https://github.com/brandon-fryslie/low-talker/pull/168)). This week was the tail: audio under the audible floor answered as nothing said, `verbose_json` serves `avg_logprob` and `compression_ratio`, and an install from huggingface.co records the sizes the hub lists for the revision so a truncated file is fetched again instead of certified ([#169](https://github.com/brandon-fryslie/low-talker/pull/169)–[#171](https://github.com/brandon-fryslie/low-talker/pull/171)).

</td>
<td width="50%" valign="top">

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript · MIT**

A port of Python's Rich to TypeScript — markup, tables, trees, syntax, progress, tracebacks, Live, and an App runtime that routes focus and the pointer. 157 commits over the past month, 28 this week. The docs card epic landed — static examples became editable cards running in the browser, with output re-rendered client-side, keyboard input, file tabs, slider playgrounds, and edits reaching a running program without restarting it ([#351](https://github.com/brandon-fryslie/rich-js/pull/351)–[#362](https://github.com/brandon-fryslie/rich-js/pull/362)); `/playground` is the card at full width ([#356](https://github.com/brandon-fryslie/rich-js/pull/356)). Byte-for-byte reconciliation with Python's Rich across progress, table, rule, pretty and effects ([#343](https://github.com/brandon-fryslie/rich-js/pull/343), [#344](https://github.com/brandon-fryslie/rich-js/pull/344), [#346](https://github.com/brandon-fryslie/rich-js/pull/346)–[#348](https://github.com/brandon-fryslie/rich-js/pull/348), [#350](https://github.com/brandon-fryslie/rich-js/pull/350)). The effect catalogue — Effected, shimmer, pulse, sparkle, wheel, fade and dissolve — promoted to `src/` with a docs page, and ProgressBar's pulse animates on the library's own clock ([#338](https://github.com/brandon-fryslie/rich-js/pull/338), [#340](https://github.com/brandon-fryslie/rich-js/pull/340)–[#342](https://github.com/brandon-fryslie/rich-js/pull/342), [#345](https://github.com/brandon-fryslie/rich-js/pull/345)); site xterm.js 5.3 → `@xterm/xterm` 6 ([#349](https://github.com/brandon-fryslie/rich-js/pull/349)).

### [gh-pages-multiplexer](https://github.com/brandon-fryslie/gh-pages-multiplexer)
**TypeScript**

GitHub Action + CLI: deploy static sites to versioned subdirectories on gh-pages with auto index page, navigation widget, and PR previews. New repo last week, 65 commits since. Concurrent deploys rebuild from the probed tip instead of rebasing, deploy concurrency is keyed per version slot, token kept out of process args and `.git/config`, publish retries bounded by a 10-minute deadline ([#1](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/1)–[#5](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/5)). The nav widget refreshes in every slot and no second switcher appears inside iframes, storage namespace per slot, PR cleanup correctness ([#6](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/6)–[#11](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/11)); slot names URL-safe by construction, sitemap percent-encoding, canonical URLs stop pointing at 404s ([#12](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/12)–[#14](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/14)); `check:dist` gate on every PR, ref-patterns match the ref name, test git identity isolated ([#15](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/15)–[#19](https://github.com/brandon-fryslie/gh-pages-multiplexer/pull/19)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — fork of `@owloops/claude-powerline` with CLI override flags so the entire config can live in `settings.json`. 59 commits over the past month, 22 this week. A live bar on GitHub Pages replays Claude turns, and `pnpm bar:web` opens the live bar in a browser terminal you can click ([#296](https://github.com/promptctl/cc-candybar/pull/296), [#297](https://github.com/promptctl/cc-candybar/pull/297)). Menu work this week — every option setting is `◀ value ▶` opening a plain list, settings marked when they differ from default, the session tab gained `⎘ resume` and `↗ config`, autocompact control, and an alt theme that turns hue every three cells along a row ([#298](https://github.com/promptctl/cc-candybar/pull/298), [#300](https://github.com/promptctl/cc-candybar/pull/300), [#302](https://github.com/promptctl/cc-candybar/pull/302), [#303](https://github.com/promptctl/cc-candybar/pull/303), [#306](https://github.com/promptctl/cc-candybar/pull/306), [#308](https://github.com/promptctl/cc-candybar/pull/308)). The doctor checks that config is correct and the URL handler works ([#311](https://github.com/promptctl/cc-candybar/pull/311), [#314](https://github.com/promptctl/cc-candybar/pull/314)); a fragment's style reads through the render's theme on rich-js 0.19.0 ([#316](https://github.com/promptctl/cc-candybar/pull/316)); a session segment shows the lit ticket being worked, its phase and epic progress ([#317](https://github.com/promptctl/cc-candybar/pull/317)).

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
