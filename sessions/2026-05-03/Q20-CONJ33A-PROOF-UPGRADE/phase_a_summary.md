# Phase A Summary — Q20-CONJ33A-PROOF-UPGRADE

**Verdict signal:** `A_DIRECT_IDENTITY`

## A.1 — Quote of 012's argument

See `phase_a_handoff_quote.md`. The Newton-polygon argument
(slope-1/d edge, ansatz `f ~ exp(c/u)`, characteristic
polynomial `χ_d(c) = 0`, `|c| = d/β_d^{1/d}`) is recorded
verbatim from `xi0_d3_runner.py` lines 23–34 and from the
"W1 (structural triviality)" anomaly note in `handoff.md`,
which itself surfaces the Q20 question to the synthesizer.

## A.2 — Symbolic re-derivation (sympy, general d)

Script: `phase_a_symbolic_derivation.py`.  Run log:
`phase_a_run.log`.

(i) **Newton-polygon edge.** For
`L_d = 1 - z B_d(θ+1) - z²` with
`B_d(t) = β_d t^d + β_{d-1} t^{d-1} + ... + β_0`, the lattice
points of `L_d` at `z = 0` are

> {(0,0)} ∪ {(1, k) : 0 ≤ k ≤ d} ∪ {(2, 0)}

(in `(z-order, θ-order)` coordinates).  The single non-trivial
edge of the lower-left convex hull at `z = 0` is `E: (0,0) → (1, d)`,
of slope-1/d after the rescaling `z = u^d`, multiplicity 2.

(ii) **Characteristic polynomial along `E`.** With ansatz
`f ~ exp(c/u)`, `z = u^d`, `θ = (u/d) ∂_u`, the principal
balance comes from `(0,0)` and `(1,d)`:

> χ_d(c) = 1 + (−β_d) · (−c/d)^d
>        = 1 + (−1)^{d+1} (β_d / d^d) c^d.

(Coefficient `−β_d` at `(1,d)` is the leading-t-coefficient of
`B_d(t+1)`, which equals β_d · 1^d = β_d, picked up with the
`−z` sign in `L_d = 1 − z B_d(θ+1) − z²`.)

(iii) **Characteristic root.** Setting `χ_d(c) = 0`:

> c^d = (−1)^d · d^d / β_d
> |c|^d = d^d / β_d  (β_d > 0)
> **|c| = d / β_d^{1/d}** [direct algebraic identity, uniform in d]

(iv) **Borel-singularity radius.**

> ξ_0(b) = |c| = d / β_d^{1/d}   ∎

The derivation is uniform in `d` and uniform in
`(β_{d-1}, …, β_0)` (which contribute only to lower-order
edges and to subleading indicial / Birkhoff data — not to the
slope-1/d leading characteristic root).  No case split is
required.  This is the symbolic content of D2-NOTE v1's own
"Heuristic structural picture" subsection of §3
(see Phase B for the diff against the d=2 proof template).

## A.3 — Sanity checks at d ∈ {2, 3, 4}

All three pass at the symbolic level (sympy-exact); the
mpmath cross-check at dps=50 reports rel_error = 0 (well
below the prompt's 1e-15 threshold).

| d | β_d | max\|root\| | expected ξ_0 | rel_error | match |
|---|-----|------------|--------------|-----------|-------|
| 2 |  3  | 1.15470053837925152901829756100… | 2/√3   | 0       | ✅ |
| 3 |  1  | 3.0                                 | 3      | 0       | ✅ |
| 4 |  1  | 4.0                                 | 4      | 0       | ✅ |

Cross-references:
- d=2 (V_quad, β_2=3): matches PCF-1 v1.3 / Prompt-005 value
  `2/√3 ≈ 1.1547005383792515` to 250 digits.
- d=3 (β_3=1, all 3 cubic representatives in 012's run have
  α_3=1): matches 012's 80-digit verdict `G2_CLOSED_AT_D3`
  (`xi0_d3_+_C3_real.csv`, `xi0_d3_+_S3_real.csv`,
  `xi0_d3_-_S3_CM.csv` — algebraic agreement_digits = 80.0).
- d=4 (β_4=1): matches PCF2-SESSION-Q1 spread-0 verdict at
  8 quartic representatives (`session_Q1_results.tex` line 119).

No `HALT_Q20_PHASE_A_SANITY_FAIL`.

## Phase A verdict

**`A_DIRECT_IDENTITY`** — the closed form `ξ_0 = d / β_d^{1/d}`
emerges as a direct algebraic identity for all `d ≥ 2` from
the slope-1/d edge characteristic polynomial.  No case split.
The `(β_{d-1}, …, β_0)`-independence at the `ξ_0` level is
also uniform (those coefficients enter only the indicial /
Birkhoff layer, not the leading edge).
