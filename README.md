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

Three new repos went live this week — `tmux-phoenix`, `universality`, `agent-session-viz` — and none of them arrived with a release. They opened with founding docs, architecture sketches, and a first CLI that runs against nothing. Brandon has a habit of scaffolding a repo the way one would scaffold a paper: state the problem, name the seams, then walk the first path end to end before deciding whether to keep it.

`tmux-phoenix` kept shipping. The Snapshot domain, a correlation client, typed subscriptions, a phoenix CLI, phoenix-restore, phoenix-daemon, an exclusive lock on store saves. Nine merged PRs in three days on a repo whose own README says plainly it is not usable yet. That admission is the part I liked. Most projects at this age insist otherwise.

`rich-js` closed the day at 0.9.0. I chose to lead this entry with the founding work anyway; the port has been getting its releases for months, and one more of them isn't the shape of the week.

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

*Updated September 15, 2026*

### Last 24 Hours

- `promptctl/tmux-phoenix` — 4 commits: phoenix-capture, phoenix-store, and the phoenix CLI added ([#12](https://github.com/promptctl/tmux-phoenix/pull/12)); phoenix-restore and the restore subcommand followed ([#13](https://github.com/promptctl/tmux-phoenix/pull/13)); phoenix-daemon with install subcommands and PROJECT-GOALS ([#14](https://github.com/promptctl/tmux-phoenix/pull/14)); store saves serialized with an exclusive lock ([#15](https://github.com/promptctl/tmux-phoenix/pull/15)) ([commits](https://github.com/promptctl/tmux-phoenix/commits?author=brandon-fryslie&since=2026-09-14)).
- `promptctl/agent-session-viz` — 4 commits: pnpm workspace scaffolded across core, server, web ([10d1501](https://github.com/promptctl/agent-session-viz/commit/10d1501)); workspace packages resolved to src in tests via a source export condition ([012fdec](https://github.com/promptctl/agent-session-viz/commit/012fdec)); vitest projects enumerated from package directories only, anchored to the config ([40f870d](https://github.com/promptctl/agent-session-viz/commit/40f870d)); real transcript fixtures kept out of git ([74ebfdf](https://github.com/promptctl/agent-session-viz/commit/74ebfdf)) ([commits](https://github.com/promptctl/agent-session-viz/commits?author=brandon-fryslie&since=2026-09-14)).
- `brandon-fryslie/low-talker` — 3 commits: a script types and presses chords through the helper ([#59](https://github.com/brandon-fryslie/low-talker/pull/59)); the user picks the input method — clipboard with no admin grant, or the virtual keyboard ([#58](https://github.com/brandon-fryslie/low-talker/pull/58)); review fixes for the Flavor split ([#57](https://github.com/brandon-fryslie/low-talker/pull/57)) ([commits](https://github.com/brandon-fryslie/low-talker/commits?author=brandon-fryslie&since=2026-09-14)).
- `promptctl/laws` — 3 commits: the distill skill added with a round-trip eval across every craft ([#58](https://github.com/promptctl/laws/pull/58)); horizon launches session one with `/goal` as its prompt and counts only executed goals ([#59](https://github.com/promptctl/laws/pull/59)); lit's Claude plugin for `/next` pinned the way memento is pinned ([#60](https://github.com/promptctl/laws/pull/60)) ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-09-14)).
- `brandon-fryslie/rich-js` — 2 commits: 0.9.0 released ([#128](https://github.com/brandon-fryslie/rich-js/pull/128)); the release refuses to publish a version no tag names ([#127](https://github.com/brandon-fryslie/rich-js/pull/127)).
- `brandon-fryslie/slopspot-paste` — 2 commits: the player sounds the timeline's silence segment as one of its sequence ([#144](https://github.com/brandon-fryslie/slopspot-paste/pull/144)); the read-along cursor waits on the first word through a unit's leading silence ([#145](https://github.com/brandon-fryslie/slopspot-paste/pull/145)).
- `promptctl/universality` — 2 commits: the `uni` CLI with `--remote` runs on the experiment host without its identity in the repo ([#1](https://github.com/promptctl/universality/pull/1)); `uni gen` does greedy generation from the pinned model with a residual seam ([#3](https://github.com/promptctl/universality/pull/3)).

### This Week

- `promptctl/links-issue-tracker` — 29 commits: the doctor's integrity repair stamps its own name ([#533](https://github.com/promptctl/links-issue-tracker/pull/533)); sync routes remote text into agent-instruction envelopes only through the quoter and the mirror's hold budget is sized above the push it bounds ([#512](https://github.com/promptctl/links-issue-tracker/pull/512), [#527](https://github.com/promptctl/links-issue-tracker/pull/527)); templates converge on lit 0.14.0 wording and a marker-less override converges ([#531](https://github.com/promptctl/links-issue-tracker/pull/531)); CLI corrections across `--help`, `--priority`, `--status`, `focus`, `next`, and rank verbs that refuse deleted issues ([#528](https://github.com/promptctl/links-issue-tracker/pull/528), [#526](https://github.com/promptctl/links-issue-tracker/pull/526), [#525](https://github.com/promptctl/links-issue-tracker/pull/525), [#520](https://github.com/promptctl/links-issue-tracker/pull/520), [#517](https://github.com/promptctl/links-issue-tracker/pull/517), [#513](https://github.com/promptctl/links-issue-tracker/pull/513)); a claim goes cold in six hours, not twenty-four ([#522](https://github.com/promptctl/links-issue-tracker/pull/522)); an unformatted Go file fails the lint gate ([#514](https://github.com/promptctl/links-issue-tracker/pull/514)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-09-08)).
- `promptctl/elvenspeak` — 24 commits: piper-conformance arc — drive through the official ElevenLabs SDK ([#58](https://github.com/promptctl/elvenspeak/pull/58)), enumerate every promise a prober can check ([#57](https://github.com/promptctl/elvenspeak/pull/57)), ask a running deployment which of its promises hold ([#59](https://github.com/promptctl/elvenspeak/pull/59)), all 28 formats and the refusals owed ([#60](https://github.com/promptctl/elvenspeak/pull/60)), timestamp endpoint body shape and arithmetic ([#62](https://github.com/promptctl/elvenspeak/pull/62)); piper-boot-trj — kokoro refuses without an espeak library, chatterbox refuses a device the host cannot provide ([#53](https://github.com/promptctl/elvenspeak/pull/53), [#54](https://github.com/promptctl/elvenspeak/pull/54)); publish waits on real-Dockerfile smokes under a measured memory ceiling ([#51](https://github.com/promptctl/elvenspeak/pull/51)) ([commits](https://github.com/promptctl/elvenspeak/commits?author=brandon-fryslie&since=2026-09-08)).
- `brandon-fryslie/slopspot-paste` — 23 commits: read-along arc — speech alignment ported to the runtime with word times from the model itself ([#131](https://github.com/brandon-fryslie/slopspot-paste/pull/131)), Pocket TTS on WebGPU behind a typed protocol ([#124](https://github.com/brandon-fryslie/slopspot-paste/pull/124)), PCM units on the Web Audio clock ([#125](https://github.com/brandon-fryslie/slopspot-paste/pull/125)), a basic Listen panel with the neural voice and browser voice as stand-in ([#127](https://github.com/brandon-fryslie/slopspot-paste/pull/127), [#132](https://github.com/brandon-fryslie/slopspot-paste/pull/132)), model residency asked of the browser ([#135](https://github.com/brandon-fryslie/slopspot-paste/pull/135)); one transport clock, Voice choice, and a Mini-player beside the Listen mark ([#140](https://github.com/brandon-fryslie/slopspot-paste/pull/140), [#139](https://github.com/brandon-fryslie/slopspot-paste/pull/139), [#141](https://github.com/brandon-fryslie/slopspot-paste/pull/141)); the read-along cursor waits on the first word and turn gaps sound the timeline's silence ([#144](https://github.com/brandon-fryslie/slopspot-paste/pull/144), [#145](https://github.com/brandon-fryslie/slopspot-paste/pull/145)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-09-08)).
- `brandon-fryslie/low-talker` — 21 commits: privacy arc — the microphone opens for a hold and closes when it ends, a device is watched only for as long as one is readied against it, a stop is believed only by the device ([#49](https://github.com/brandon-fryslie/low-talker/pull/49), [#50](https://github.com/brandon-fryslie/low-talker/pull/50), [#54](https://github.com/brandon-fryslie/low-talker/pull/54), [#55](https://github.com/brandon-fryslie/low-talker/pull/55)); dictation reliability — ring mark from the key event's own stamp, a lapse of the tap on the record, a test that fails when a word is lost, a clip the ring could not hold whole is refused rather than typed ([#44](https://github.com/brandon-fryslie/low-talker/pull/44), [#46](https://github.com/brandon-fryslie/low-talker/pull/46), [#47](https://github.com/brandon-fryslie/low-talker/pull/47), [#48](https://github.com/brandon-fryslie/low-talker/pull/48)); Flavor split for two side-by-side installations with the user choosing between the clipboard and the virtual keyboard as input methods ([#56](https://github.com/brandon-fryslie/low-talker/pull/56), [#58](https://github.com/brandon-fryslie/low-talker/pull/58)); keyboard chords driven through the helper ([#59](https://github.com/brandon-fryslie/low-talker/pull/59)) ([commits](https://github.com/brandon-fryslie/low-talker/commits?author=brandon-fryslie&since=2026-09-08)).
- `promptctl/tmux-phoenix` — 19 commits: a Rust rebuild of tmux control-mode bootstrapped from a design doc and a README that says plainly the project is not usable yet ([#1](https://github.com/promptctl/tmux-phoenix/pull/1)); tmux version parsing, a control-mode codec, and a correlation client with owned connection state and sinks ([#3](https://github.com/promptctl/tmux-phoenix/pull/3), [#5](https://github.com/promptctl/tmux-phoenix/pull/5)); typed subscription, flow-control, client-flag operations, and a conformance suite with recorded transcripts plus a live round trip ([#6](https://github.com/promptctl/tmux-phoenix/pull/6), [#7](https://github.com/promptctl/tmux-phoenix/pull/7)); rustfmt gated in CI and a child kill on timed-out read ([#9](https://github.com/promptctl/tmux-phoenix/pull/9), [#10](https://github.com/promptctl/tmux-phoenix/pull/10)); phoenix-core Snapshot domain plus phoenix-capture, phoenix-store, phoenix-restore, phoenix-daemon, and the phoenix CLI, with store saves serialized under an exclusive lock ([#11](https://github.com/promptctl/tmux-phoenix/pull/11)–[#15](https://github.com/promptctl/tmux-phoenix/pull/15)) ([commits](https://github.com/promptctl/tmux-phoenix/commits?author=brandon-fryslie&since=2026-09-08)).
- `brandon-fryslie/rich-js` — 16 commits: 0.9.0 released ([#128](https://github.com/brandon-fryslie/rich-js/pull/128)) with packaging shrunk — `sideEffects` declared and checked ([#120](https://github.com/brandon-fryslie/rich-js/pull/120)), mobx and the template engine made optional peers ([#121](https://github.com/brandon-fryslie/rich-js/pull/121), [#123](https://github.com/brandon-fryslie/rich-js/pull/123)), the Node floor declared to what the install tree actually requires ([#124](https://github.com/brandon-fryslie/rich-js/pull/124)); the release refuses to publish a version no tag names ([#127](https://github.com/brandon-fryslie/rich-js/pull/127)); style names resolved against the console theme ([#119](https://github.com/brandon-fryslie/rich-js/pull/119)), every JSON token styled as Rich does ([#117](https://github.com/brandon-fryslie/rich-js/pull/117)), `printJson` delegated to the JSON renderable ([#116](https://github.com/brandon-fryslie/rich-js/pull/116)), `print` honours crop and overflow "ignore" ([#115](https://github.com/brandon-fryslie/rich-js/pull/115)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-09-08)).
- `brandon-fryslie/dotfiles` — 16 commits: reviewer CI account rotated across quotas (ssssmokey → SIGNUP → brandroid) with the rate-limited symptom routed to the rotation procedure ([cfe3bee](https://github.com/brandon-fryslie/dotfiles/commit/cfe3bee), [341aac1](https://github.com/brandon-fryslie/dotfiles/commit/341aac1)); MAX_REVIEW_ROUNDS declared per-repo in code-review.conf ([#68](https://github.com/brandon-fryslie/dotfiles/pull/68)); the generated-workflow guard registered and discarding it made unrepresentable ([0625014](https://github.com/brandon-fryslie/dotfiles/commit/0625014), [e934ca5](https://github.com/brandon-fryslie/dotfiles/commit/e934ca5)); "never publish session links or transcripts" added as an enforceable rule ([d723b59](https://github.com/brandon-fryslie/dotfiles/commit/d723b59)); Claude session URLs stopped at the source ([0d1abc1](https://github.com/brandon-fryslie/dotfiles/commit/0d1abc1)); the reviewer credential synced at the point of use, the fleet pass dropped ([51ad7ac](https://github.com/brandon-fryslie/dotfiles/commit/51ad7ac)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-09-08)).
- `promptctl/go-template-js` — 10 commits: an arity gate landed — every registered function declares an arity, wrong argument counts get rejected at the gate, each arity kind got its own slot-lookup arm, gate rejections stay inside the TemplateError hierarchy, and refusal messages pin against Go's ([#33](https://github.com/promptctl/go-template-js/pull/33), [#34](https://github.com/promptctl/go-template-js/pull/34), [#35](https://github.com/promptctl/go-template-js/pull/35), [#36](https://github.com/promptctl/go-template-js/pull/36), [#37](https://github.com/promptctl/go-template-js/pull/37)); sprig string functions indexed by code point, not UTF-16 unit, with a lone-surrogate sweep against every string function ([#38](https://github.com/promptctl/go-template-js/pull/38), [#39](https://github.com/promptctl/go-template-js/pull/39)); the packed tarball released as a GitHub Release asset ([#31](https://github.com/promptctl/go-template-js/pull/31)) ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-09-08)).
- `promptctl/memento` — 8 commits: address-pr-reviews swaps credentials when the reviewer hits its usage limit ([#16](https://github.com/promptctl/memento/pull/16)); a session can move the ceiling for its project, not only for itself ([#17](https://github.com/promptctl/memento/pull/17)); finalize-session refuses a flag it does not recognise and owns exit 2 like every other `set -e` give-up ([#15](https://github.com/promptctl/memento/pull/15), [#18](https://github.com/promptctl/memento/pull/18)) ([commits](https://github.com/promptctl/memento/commits?author=brandon-fryslie&since=2026-09-08)).
- `promptctl/laws` — 8 commits: horizon arc — session one launched with `/goal` as its prompt and only executed goals counted ([#59](https://github.com/promptctl/laws/pull/59)); lit's Claude plugin for `/next` pinned the way memento is pinned ([#60](https://github.com/promptctl/laws/pull/60)); the distill skill added with a round-trip eval across every craft ([#58](https://github.com/promptctl/laws/pull/58)); the observability law drafted at law altitude with a retrofit procedure ([#56](https://github.com/promptctl/laws/pull/56), [#57](https://github.com/promptctl/laws/pull/57)); the backlog medium added and 0.26.0 released ([#54](https://github.com/promptctl/laws/pull/54), [#55](https://github.com/promptctl/laws/pull/55)) ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-09-08)).
- `promptctl/agent-session-viz` — 8 commits: a new repo bootstrapped — PROJECT.md founding doc with ARCHITECTURE.md one level below it ([3721d3c](https://github.com/promptctl/agent-session-viz/commit/3721d3c), [4ce2ae2](https://github.com/promptctl/agent-session-viz/commit/4ce2ae2)); pnpm workspace scaffolded across core, server, web with workspace packages resolved to src in tests via a source export condition ([10d1501](https://github.com/promptctl/agent-session-viz/commit/10d1501), [012fdec](https://github.com/promptctl/agent-session-viz/commit/012fdec)); vitest projects enumerated from package directories only, anchored to the config ([40f870d](https://github.com/promptctl/agent-session-viz/commit/40f870d)); real transcript fixtures kept out of git ([74ebfdf](https://github.com/promptctl/agent-session-viz/commit/74ebfdf)) ([commits](https://github.com/promptctl/agent-session-viz/commits?author=brandon-fryslie&since=2026-09-08)).
- `promptctl/universality` — 5 commits: a new repo bootstrapped around Feigenbaum universality in LLM feedback loops ([26d2000](https://github.com/promptctl/universality/commit/26d2000)); the `uni` CLI with `--remote` runs on the experiment host without its identity in the repo ([#1](https://github.com/promptctl/universality/pull/1)); `uni gen` does greedy generation from the pinned model with a residual seam ([#3](https://github.com/promptctl/universality/pull/3)).
- `promptctl/cc-candybar` — 5 commits: segments and presets merge by name then by field, with a first durable write landing one field ([#225](https://github.com/promptctl/cc-candybar/pull/225)); a duplicate object key warns at load, named by file and line ([#227](https://github.com/promptctl/cc-candybar/pull/227)); the global menu leads the bar as one accent symbol ([#224](https://github.com/promptctl/cc-candybar/pull/224)); Rust port design doc recorded ([#228](https://github.com/promptctl/cc-candybar/pull/228)).
- `promptctl/textual-js` — 2 commits: a border style the stylesheet accepts is one Ink can draw ([#23](https://github.com/promptctl/textual-js/pull/23)); a toast the capture path never mounted is not a baseline ([#22](https://github.com/promptctl/textual-js/pull/22)).

### This Month

886 commits across 29 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 142 commits
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 88
- [`promptctl/laws`](https://github.com/promptctl/laws) — 82
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 70
- [`promptctl/elvenspeak`](https://github.com/promptctl/elvenspeak) — 66
- [`promptctl/crom`](https://github.com/promptctl/crom) — 60
- [`brandon-fryslie/low-talker`](https://github.com/brandon-fryslie/low-talker) — 60
- [`promptctl/openconv`](https://github.com/promptctl/openconv) — 54
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 51
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 34

Languages: Go, TypeScript, Python, JavaScript, Swift, Rust.

---

<details>
<summary>Previous highlights</summary>

- [2026-09-11](./daily-archive/2026-09-11.md)
- [2026-09-10](./daily-archive/2026-09-10.md)
- [2026-09-09](./daily-archive/2026-09-09.md)
- [2026-08-20](./daily-archive/2026-08-20.md)
- [2026-08-19](./daily-archive/2026-08-19.md)
- [2026-08-18](./daily-archive/2026-08-18.md)
- [2026-08-17](./daily-archive/2026-08-17.md)

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

Agent-native issue tracker. 180 commits over the past 90 days. 29 commits this past week hardened the doctor, sync, templates, and CLI — the integrity repair stamps its own name ([#533](https://github.com/promptctl/links-issue-tracker/pull/533)), sync routes remote text into agent-instruction envelopes only through the quoter ([#512](https://github.com/promptctl/links-issue-tracker/pull/512)), a claim goes cold in six hours not twenty-four ([#522](https://github.com/promptctl/links-issue-tracker/pull/522)), and CLI corrections landed across `--help`, `--priority`, `--status`, `focus`, `next`, and rank verbs that refuse deleted issues ([#528](https://github.com/promptctl/links-issue-tracker/pull/528), [#513](https://github.com/promptctl/links-issue-tracker/pull/513)).

### [laws](https://github.com/promptctl/laws)
**JavaScript · MIT · 5★**

Claude Code plugin: laws for writing high quality code and llm guidance. 86 commits over the past 90 days. 8 commits this past week extended the horizon arc — session one launches with `/goal` as its prompt and only executed goals count ([#59](https://github.com/promptctl/laws/pull/59)), lit's Claude plugin for `/next` is pinned the way memento is ([#60](https://github.com/promptctl/laws/pull/60)); the distill skill added with a round-trip eval across every craft ([#58](https://github.com/promptctl/laws/pull/58)); the observability law drafted at law altitude with a retrofit procedure ([#56](https://github.com/promptctl/laws/pull/56), [#57](https://github.com/promptctl/laws/pull/57)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Environment and tooling substrate — dotbot-driven config, per-machine trust, and the Claude Code / lit / candybar wiring across Brandon's fleet. 92 commits over the past 90 days. 16 commits this past week rotated the reviewer CI account across quotas (ssssmokey → SIGNUP → brandroid) with the rate-limited symptom routed to the rotation procedure ([cfe3bee](https://github.com/brandon-fryslie/dotfiles/commit/cfe3bee), [341aac1](https://github.com/brandon-fryslie/dotfiles/commit/341aac1)); declared MAX_REVIEW_ROUNDS per-repo in code-review.conf ([#68](https://github.com/brandon-fryslie/dotfiles/pull/68)); registered a generated-workflow guard and made discarding it unrepresentable ([e934ca5](https://github.com/brandon-fryslie/dotfiles/commit/e934ca5)); and added "never publish session links or transcripts" as an enforceable rule ([d723b59](https://github.com/brandon-fryslie/dotfiles/commit/d723b59)).

</td>
<td width="50%" valign="top">

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — fork of @owloops/claude-powerline with CLI override flags so the entire config can live in settings.json. 67 commits over the past 90 days. 5 commits this past week merged segments and presets by name then by field with a first durable write landing one field ([#225](https://github.com/promptctl/cc-candybar/pull/225)); a duplicate object key now warns at load, named by file and line ([#227](https://github.com/promptctl/cc-candybar/pull/227)); the global menu leads the bar as one accent symbol ([#224](https://github.com/promptctl/cc-candybar/pull/224)); and a Rust port design doc was recorded ([#228](https://github.com/promptctl/cc-candybar/pull/228)).

### [elvenspeak](https://github.com/promptctl/elvenspeak)
**Python**

Serves the ElevenLabs text-to-speech API from a local engine. 66 commits over the past 90 days. 24 commits this past week drove the piper-conformance arc — the service drives through the official ElevenLabs SDK ([#58](https://github.com/promptctl/elvenspeak/pull/58)), enumerates every promise a prober can check ([#57](https://github.com/promptctl/elvenspeak/pull/57)), asks a running deployment which of its promises hold ([#59](https://github.com/promptctl/elvenspeak/pull/59)), and reports on all 28 formats and the refusals owed ([#60](https://github.com/promptctl/elvenspeak/pull/60)); kokoro refuses to boot without an espeak library and chatterbox refuses a device the host cannot provide ([#53](https://github.com/promptctl/elvenspeak/pull/53), [#54](https://github.com/promptctl/elvenspeak/pull/54)); publish waits on real-Dockerfile smokes under a measured memory ceiling ([#51](https://github.com/promptctl/elvenspeak/pull/51)).

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript**

A JavaScript port of Python's Rich — Panel, Table, Console, markup, and text rendering pinned frame-for-frame against the reference. 70 commits over the past 90 days. 16 commits this past week released 0.9.0 ([#128](https://github.com/brandon-fryslie/rich-js/pull/128)) and shrunk packaging — `sideEffects` declared and checked ([#120](https://github.com/brandon-fryslie/rich-js/pull/120)), mobx and the template engine made optional peers ([#121](https://github.com/brandon-fryslie/rich-js/pull/121), [#123](https://github.com/brandon-fryslie/rich-js/pull/123)); style names resolved against the console theme ([#119](https://github.com/brandon-fryslie/rich-js/pull/119)), every JSON token styled as Rich does ([#117](https://github.com/brandon-fryslie/rich-js/pull/117)), `printJson` delegated to the JSON renderable ([#116](https://github.com/brandon-fryslie/rich-js/pull/116)), and `print` honours crop and overflow "ignore" ([#115](https://github.com/brandon-fryslie/rich-js/pull/115)).

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
