# THE ATELIER

![Atelier Banner](./assets/atelier-banner.svg)

**Machines That Dream in Geometry**  
*Winter 2026: Continuity & Gauge*

---

## CURRENT SEASON

This season explores **continuity in discrete systems**—how to make step functions feel smooth, how to bridge index sets without tearing, how to measure drift without breaking determinism.

**Collection pieces:**
- **Warp** — Timebase, scheduling, determinism  
- **Weft** — Data flowing through index sets  
- **Selvage** — Boundary conditions: adapters, defaults, ingestion rules  
- **Drape** — Smoothing, slew filters, continuity  
- **Cut** — Compilation passes that shape raw graphs into typed IR  

---

## PATTERN SHEETS

Each piece is documented as a **pattern sheet**:

### **Materials** (Dependencies)
What you'll need to construct this piece. Versions matter—like thread count.

### **Measurements** (Complexities)
O(n log n) here, O(1) there. Where the seams strain under load.

### **Seams** (Interfaces)
Points of contact between modules. This is where nondeterminism leaks in—reinforce carefully.

### **Tolerances** (Error Bounds)
How much slippage can the system absorb before it shows? ±0.001? ±1 frame?

---

## ATELIER NOTES

### On Determinism as a Material Property

Nondeterminism is not a bug—it's a cheap fabric. It frays. You can work with it if you line the seams: seed your randoms, version your floats, pin your timestamps. The result feels tighter.

### On Index Sets as Looms

A loom holds warp threads taut while weft threads weave through. An index set is the same: a structure that constrains what can move, defining where data can flow. The pattern emerges from tension between the fixed and the free.

### On Smoothing Without Lying

A slew filter is not interpolation—it's a controlled fall. You're not inventing data; you're admitting that discrete steps are a rendering artifact. The underlying signal was always continuous; you're just letting it breathe.

---

## LIVING GALLERY

![Daily Generative Art](./assets/atelier-daily-art.svg)

One piece in this collection is **alive**: a GitHub Action that generates a new visual each day from a deterministic seed. The image is not decoration—it's a **diagnostic artifact**. Each shape corresponds to:
- A render tree layout
- A phase field state
- A particle index set distribution

**Today's piece:**  
Seed: `2026-01-29` | Commit: `310fb71` | Pattern: _Voronoi tesselation of constraint satisfaction states_

View the [**Gallery Archive**](./GALLERY.md) to see the full seasonal collection.

---

## PREVIOUS SEASONS

### [Autumn 2025: Boundaries & Adapters](./seasons/autumn-2025.md)
*Selvage, ingestion rules, protocol negotiation. How systems touch without tearing.*

### [Summer 2025: Phase & Rhythm](./seasons/summer-2025.md)
*Scheduling, tempo maps, frame budgets. Making time feel right, not just correct.*

### [Spring 2025: Foundation Garments](./seasons/spring-2025.md)
*Core data structures, indexing, the invisible scaffolding that everything drapes over.*

---

## CRAFT PRINCIPLES

### **Restraint**
Few pieces, finished well. Every repo earns its place.

### **Coherence**
Consistent naming. Consistent structure. Consistent voice. This is not a storage unit.

### **Finish**
The last 10% is half the work. Polish the READMEs. Draw the diagrams. Write the tests that prove the claim.

### **Seasonality**
Work in focused arcs. Not "ongoing" or "maintenance mode"—**complete**. Then archive and begin again.

---

## TAILORING DIAGRAMS

Documentation includes **pattern-style diagrams**: flat shapes with annotations, sewn seams, fold lines. These map naturally to:
- Block graphs (modules as pattern pieces)
- IR transforms (cutting and refolding)
- Data flow (how the fabric drapes)

Example:
```
    ╔═══════════════╗
    ║   Raw Input   ║
    ╚═══════════════╝
           ↓ (cut)
    ╔═══════════════╗
    ║  Typed Graph  ║──→ (seam: interface boundary)
    ╚═══════════════╝
           ↓ (drape)
    ╔═══════════════╗
    ║  Output IR    ║
    ╚═══════════════╝
```

See [**PATTERN-GUIDE.md**](./PATTERN-GUIDE.md) for the full visual language.

---

## COMMISSIONS & INQUIRIES

This atelier does not take commissions—but you may study the patterns.

All pieces are open-source. The techniques are yours to learn. The philosophy is yours to question.

If you build something with these methods, I'd love to see it.

---

## MATERIALS & TOOLS

**Languages:** Rust, Zig, TypeScript  
**Substrates:** WASM, native, GPU  
**Instruments:** Deterministic chaos, seeded noise, constraint solvers  
**Philosophy:** [README-OBSERVATORY.md](./README-OBSERVATORY.md) for the science; this atelier for the craft.

---

## COLOPHON

This profile is itself a piece in the collection.

**Banner:** Faint wireframe over ivory, single burgundy accent  
**Typography:** GT America, Inter, system monospace  
**Diagrams:** Hand-drawn in SVG, then cleaned in code  
**Updated:** Each season's first commit  

---

*The Atelier does not chase trends. It makes pieces that last.*

**— BRANDON FRYSLIE**  
*Winter 2026*
