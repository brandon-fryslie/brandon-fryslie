# 🌲 Misty Forest Morning

A peaceful, atmospheric SVG scene reminiscent of the Kokiri Forest from Zelda: Ocarina of Time.

---

![Misty Forest Morning](./assets/misty-forest-morning.svg)

---

## 🎨 Scene Elements

### Depth Layers (Near to Far)
1. **Foreground** - Grass and reeds at water's edge
2. **Near trees** - Detailed trunks with foliage
3. **Mid-distance** - Silhouetted conifer trees
4. **Far mountains** - Layered peaks fading into mist
5. **Sky** - Gradient atmosphere

### Atmospheric Effects
- **Mist** - Using `feTurbulence` with animated frequency
- **Rain** - Gentle drops falling at varied speeds (2.7s - 3.8s)
- **Water ripples** - Expanding circles where rain hits
- **Depth blur** - Far objects more blurred than near

### Living Details
- **Fireflies** - 10 glowing insects at 3 depth levels
  - Far: Small (2px), dim
  - Mid: Medium (3px)
  - Near: Large (4px), bright
- **Movement** - Everything floats organically on prime duration cycles

---

## 🔧 3D Techniques Used

### 1. **Parallax Layering**
```css
@keyframes parallax-far { /* 8px movement, 40s */ }
@keyframes parallax-mid { /* 20px movement, 35s */ }
@keyframes parallax-near { /* 40px movement, 30s */ }
```
Layers move at different speeds creating depth perception.

### 2. **Atmospheric Perspective**
- Far mountains: `opacity: 0.4`, heavy blur
- Mid trees: `opacity: 0.6`, medium blur
- Near elements: `opacity: 0.9`, minimal blur

### 3. **Scale + Distance**
- Far fireflies: 2px radius
- Mid fireflies: 3px radius
- Near fireflies: 4px radius

### 4. **Layered Mist**
Two mist layers at different heights, each with 50-60s drift cycles, using fractal noise turbulence.

### 5. **Organic Animation**
- Fireflies: Prime durations (17s, 19s, 23s) = won't sync for hours
- Rain: Staggered delays create natural rhythm
- Ripples: Each has unique timing (2.3s - 3s)

---

## 🎭 Mood & Atmosphere

**Color Palette:**
- Sky: `#b8c5d6` → `#e8eef5` (cool morning blues)
- Mountains: `#8a9aa8` (soft gray-blue)
- Trees: `#3a4a3a`, `#4a6a5a` (muted forest greens)
- Water: `#5a7a8f` (reflective blue-gray)
- Fireflies: `#d4ff00` (soft yellow-green glow)

**Inspired by:**
- Japanese mountain forests (misty, serene)
- Kokiri Forest (Zelda OoT) - peaceful, magical
- Pacific Northwest rainforest mornings
- Studio Ghibli landscapes (soft, atmospheric)

---

## 🌧️ Rain Physics

Each rain drop:
- Starts slightly above viewport
- Falls 400px down
- Takes 2.7-3.8 seconds
- Staggered start times prevent uniformity
- Creates ripples on water surface

Ripples:
- Expand from 0 to 18-25px radius
- Fade from 60% to 0% opacity
- Each has unique timing
- Positioned where rain would naturally hit

---

## ✨ Firefly Behavior

**Movement patterns:**
3 unique keyframe animations simulate organic flight:
- Curved paths (using translate X/Y)
- Opacity flicker (0.3 - 1.0) mimics natural blinking
- No two fireflies share timing or path

**Depth cueing:**
- Size decreases with distance
- Glow intensity decreases with distance
- Movement speed same (they're insects, not affected by distance)
- Blur increases with distance

---

## 📐 Technical Stats

- **Total elements:** ~80 (optimized for performance)
- **Animation cycles:** 15+ unique timings
- **Filters used:** 5 (mist, blur at 3 depths, glow, water)
- **Layers:** 7 depth planes
- **File size:** 13.5 KB
- **No JavaScript** - Pure CSS/SMIL

---

## 🎯 Usage Ideas

Perfect for:
- GitHub profile header banner
- Project README header (nature/environmental projects)
- Meditation/wellness app documentation
- Game dev portfolio (showing atmospheric capability)
- Any project needing peaceful, zen aesthetics

---

## 🔗 Related Techniques

See also:
- [3D-GALLERY.md](./3D-GALLERY.md) - Learn the 3D techniques
- [RANDOMNESS-GUIDE.md](./RANDOMNESS-GUIDE.md) - Organic movement patterns
- [INTERACTIVITY-LIMITS.md](./INTERACTIVITY-LIMITS.md) - What's possible on GitHub

---

*A moment of peace in code. Watch the rain fall, the fireflies dance, the mist drift.*

*Created: 2026-01-29*
