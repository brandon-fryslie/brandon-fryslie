# ❌ SVG Interactivity on GitHub - What Doesn't Work

GitHub's security model strips almost all interactivity from SVGs. Here's what gets removed:

---

## 1. JavaScript (Completely Stripped)

```xml
<!-- THIS DOES NOT WORK -->
<svg xmlns="http://www.w3.org/2000/svg">
  <script>
    // All JavaScript is removed by GitHub's sanitizer
    alert('This will never run');
  </script>
  
  <circle cx="50" cy="50" r="30" fill="blue"
          onclick="alert('Clicked!')"/>  <!-- Event handler removed -->
</svg>
```

**Result:** All `<script>` tags and inline event handlers are stripped.

---

## 2. CSS :hover (Context Issue)

```xml
<!-- THIS PROBABLY DOESN'T WORK -->
<svg xmlns="http://www.w3.org/2000/svg">
  <style>
    .hoverable { fill: blue; }
    .hoverable:hover { fill: red; }  <!-- Won't work in <img> context -->
  </style>
  
  <circle class="hoverable" cx="50" cy="50" r="30"/>
</svg>
```

**Why it fails:** GitHub embeds SVGs as `<img>` tags, which creates an isolated context. CSS pseudo-classes like `:hover` don't penetrate the image boundary.

---

## 3. Links (Security Concern)

```xml
<!-- THIS DOES NOT WORK -->
<svg xmlns="http://www.w3.org/2000/svg">
  <a href="https://example.com">
    <text x="10" y="20">Click me</text>  <!-- Link stripped -->
  </a>
</svg>
```

**Result:** All `<a>` tags are removed for security (phishing prevention).

---

## 4. Form Inputs (No User Input)

```xml
<!-- THIS DOES NOT WORK -->
<svg xmlns="http://www.w3.org/2000/svg">
  <foreignObject width="200" height="50">
    <input type="text"/>  <!-- foreignObject removed -->
  </foreignObject>
</svg>
```

**Result:** `<foreignObject>` and all HTML form elements are stripped.

---

## 5. SMIL Click Events (Unclear)

```xml
<!-- THIS MIGHT NOT WORK -->
<svg xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="30" fill="blue">
    <set attributeName="fill" to="red" begin="click"/>  <!-- May not work -->
  </circle>
</svg>
```

**Status:** SMIL supports `begin="click"`, but GitHub's `<img>` context may prevent event delivery.

---

## 6. CSS :target (Direct View Only)

```xml
<!-- THIS ONLY WORKS IF SVG IS VIEWED DIRECTLY -->
<svg xmlns="http://www.w3.org/2000/svg">
  <style>
    #state1 { display: block; }
    #state2 { display: none; }
    
    #state1:target { display: none; }
    #state2:target { display: block; }
  </style>
  
  <g id="state1">
    <text x="10" y="20">State 1</text>
  </g>
  <g id="state2">
    <text x="10" y="20">State 2</text>
  </g>
</svg>
```

**Why it fails:** This only works when the SVG is viewed directly at URLs like `file.svg#state2`. When embedded in a README, the fragment identifier doesn't reach the SVG.

---

## 7. Mouse Position Tracking (No Access)

```xml
<!-- THIS DOES NOT WORK -->
<!-- There's no way to read mouse coordinates without JavaScript -->
```

**Result:** Complete impossibility without JS.

---

## ⚠️ The Core Problem

GitHub embeds SVGs like this:

```html
<!-- In the rendered README -->
<img src="https://raw.githubusercontent.com/.../your.svg"/>
```

This `<img>` embedding means:
1. **No DOM access** - The SVG is in an isolated context
2. **No event bubbling** - Mouse events don't reach the SVG
3. **No pseudo-classes** - `:hover`, `:focus`, `:active` don't work
4. **No fragments** - `#hash` URLs don't affect embedded images

---

## 🔒 Why So Restrictive?

**Security.** SVGs can contain:
- JavaScript that steals cookies
- Phishing links disguised as GitHub UI
- Resource exhaustion attacks
- Privacy-invading tracking pixels

GitHub's sanitizer removes ALL potentially dangerous features.

---

## ✅ What DOES Work

Only **time-based** and **self-contained** animations:

1. **CSS `@keyframes`** - Timed animations
2. **SMIL `<animate>`** - Timed property changes
3. **SMIL `<animateTransform>`** - Timed transformations
4. **Filters** - `feTurbulence`, gradients, etc.
5. **CSS transitions** - But only for time-based state changes

Everything is **deterministic** and **non-interactive**.

---

## 💡 Workarounds (Limited)

### 1. External Hosted SVG with Full Features

Host an interactive SVG on your own server, then link to it:

```markdown
[See Interactive Demo](https://your-site.com/interactive.svg)
```

The external SVG can have full JS/interactivity, but users must click to visit.

### 2. Multiple Static Frames

Create multiple versions showing different states:

```markdown
## Hover States

Normal:
![Normal State](./normal.svg)

Hovered:
![Hover State](./hovered.svg)

Clicked:
![Clicked State](./clicked.svg)
```

Users imagine the interaction.

### 3. Animated "Hover" Effect

Simulate hover by having elements pulse/highlight automatically:

```xml
<style>
  .pseudo-hover {
    animation: highlight 3s ease-in-out infinite;
  }
  @keyframes highlight {
    0%, 80%, 100% { fill: blue; }
    90% { fill: red; }  /* "Hover" moment */
  }
</style>
```

---

## 📊 Feature Comparison

| Feature | Allowed? | Works on GitHub? | Reason |
|---------|----------|------------------|--------|
| `<script>` | ❌ No | No | Security |
| `onclick=""` | ❌ No | No | Security |
| `:hover` CSS | ⚠️ Maybe | No* | Context isolation |
| `<a href>` | ❌ No | No | Phishing prevention |
| SMIL `begin="click"` | ⚠️ Maybe | No* | Context isolation |
| CSS animations | ✅ Yes | Yes | Safe |
| SMIL animations | ✅ Yes | Yes | Safe |
| Filters | ✅ Yes | Yes | Safe |

\* Technically allowed in SVG spec, but GitHub's `<img>` context prevents them from working.

---

## 🎯 Bottom Line

**You cannot get user input in GitHub SVGs.**

The only "interaction" possible is:
1. **Time-based** - Animations that happen automatically
2. **Pseudo-random** - Patterns that feel unpredictable
3. **Visual tricks** - Simulating interaction through animation

For true interactivity, you need:
- External hosting with full features
- Link users to a live demo
- Use GitHub Pages or CodePen for interactive versions

---

*This is a hard limitation, not a challenge to overcome. GitHub's security model is intentionally restrictive.*

*Last updated: 2026-01-29*
