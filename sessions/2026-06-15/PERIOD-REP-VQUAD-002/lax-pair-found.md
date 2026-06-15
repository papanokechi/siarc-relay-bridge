# Stage 1 — G-LAX pre-investigation: CONFIRMED-ABSENT

**Chain:** PERIOD-REP-VQUAD-002 · **Stage:** 1 · **Date:** 2026-06-15
**Verdict:** **G-LAX confirmed-absent** — no explicit V_quad Lax pair / rank-2
linear (isomonodromy) ODE exists anywhere in the corpus.

> Strengthening Condition 1 requires checking whether a located Lax pair already
> determines the algebraicity of ω before running the Borel–Padé fallback. It
> does **not** exist; Stage 3 (fallback) is therefore required.

## 1.1 Search performed (this probe, fresh)

| # | Scope | Pattern | Result |
|---|-------|---------|--------|
| A | whole repo `project-fingerprint/` | `Lax\|associated linear (problem\|system)\|isomonodrom(ic\|y)` | hits only in **prose / future-work** contexts (no matrix) |
| B | `sectorial/vquad_stokes_resurgence/` | `\bLax\b\|associated linear\|isomonodrom\|linear system\|2x2 system` | 5 hits, **all** Jimbo–Miwa references or the "missing step" flag |
| C | `sectorial/vquad_stokes_resurgence/` | `dPsi\|Lax\|\begin{pmatrix}\|A_0\|A_1\|Theta_\infty\|rank-2` | **0** matrix/ODE hits (only Γ-function lines, `\relax`) |

**Key corpus lines (sourced):**
- `sectorial/vquad_stokes_resurgence/note_stokes_2piK.tex:326` — "coincides with the
  Jimbo–Miwa **isomonodromic** …" (reference to the literature problem, not a
  constructed V_quad Lax pair).
- `sectorial/vquad_stokes_resurgence/note_stokes_2piK.tex:345` — "establishing (P2)
  is an **isomonodromy** [problem]" — explicitly framed as *open/future work*.
- `sectorial/vquad_stokes_resurgence/claims_stokes_2piK.jsonl:8` (claim `VQS-2piK-8`)
  — lists "identification … with the Jimbo–Miwa isomonodromy connection-formula
  Stokes multiplier" as a **MISSING STEP**, not an executed computation.
- `files/EBR-II-paper.md:59–61` — the V_quad linear problem is described only **in
  words**: "order-2 Heun type, four singular points (p=4), connection datum
  σ_conn transcendental in the accessory parameter."

## 1.2 Corroboration with the parent probe

The parent probe reached the identical conclusion independently:
- `PERIOD-REP-VQUAD-001/vquad-linear-system.md:10–17` — "**No explicit Lax pair /
  linear ODE for V_quad is present in the corpus.** … literature-derived /
  CONJECTURAL-for-V_quad, not corpus-verified."
- `PERIOD-REP-VQUAD-001/data-inventory.json:136–139` (gap `G-LAX`) — "NO explicit
  Lax pair / rank-2 linear ODE for V_quad's Painlevé V exists in the corpus."

## 1.3 Disposition impact

- **No located Lax pair ⇒ no shortcut to algebraicity.** Stage 3 (Borel–Padé +
  exact holonomic recognition over ℚ(√3)) is the operative test.
- The *only* Lax/linear-ODE that exists in the corpus is the **EBR / D8⁽¹⁾**
  sibling (cc3 order-4 Borel operator `L`), which is a **distinct ODE** ("same
  flavour but not the same integral", `data-inventory.json` EBR-CC3-TEMPLATE
  L73) and cannot be specialised to V_quad.

**Status:** G-LAX = **confirmed-absent** (fresh search + parent corroboration).
Proceed to Stage 2.
