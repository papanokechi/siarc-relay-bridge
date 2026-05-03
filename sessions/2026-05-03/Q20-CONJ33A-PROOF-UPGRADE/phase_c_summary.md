# Phase C Summary — Q20-CONJ33A-PROOF-UPGRADE

**Verdict signal:** `HALT_Q20_LITERATURE_MISSING`

## C.0 gate

Wasow 1965 §X.3, Adams 1928, Birkhoff 1930, and
Birkhoff–Trjitzinsky 1933 are all flagged in the
T1-BIRKHOFF-TRJITZINSKY-LITREVIEW (2026-05-02) handoff
as **needed-but-not-acquired** primary sources at the
operator side.  The operator has paraphrased / secondary-
source readings only.

Per Q20 prompt §4: halt at the gate with
`HALT_Q20_LITERATURE_MISSING`, produce partial output
(Phases A + B), skip the in-original-form Phases C / D / E,
and output verdict `UPGRADE_PARTIAL_PENDING_LITERATURE`.

## What this means

- Phase A's symbolic derivation (`A_DIRECT_IDENTITY`) is
  unaffected — it is sympy-proof of the leading-edge
  characteristic root identity at general d.
- Phase B's parametric-in-d diff (`B_TEMPLATE_PARAMETRIC`
  for ξ_0 only) is unaffected — it is a structural
  line-by-line walk of the d=2 proof template.
- The bridge from "leading characteristic root |c|" to
  "Borel-plane singular distance ξ_0" is the standard
  Newton-polygon-of-an-irregular-ODE theorem, which is
  textbook in Wasow §X.3 and parallel in B–T 1933 §§4–6.
  This is what Phase C would have verified explicitly at
  general d.  At paraphrase level, it is taken to hold
  uniformly in d, but this is **not** primary-source-
  confirmed.

## Conditional discharge

If the operator acquires Wasow 1965 §X.3, Adams 1928 §3,
Birkhoff 1930 §§2–3, and Birkhoff–Trjitzinsky 1933 §§4–6
(as recommended in T1 PHASE 2, see
`siarc-relay-bridge/sessions/2026-05-02/T1-BIRKHOFF-TRJITZINSKY-LITREVIEW/recommended_next_phase_t1.md`),
then Phase C can be re-run with M-tagged lines (L3, L8, and
the implicit Borel-summability link at L6) verified
directly.  Conditional on that verification giving
`C_LITERATURE_UNIFORM`, Q20 verdict UPGRADES to
`UPGRADE_FULL` for the **Conj 3.3.A* (ξ_0 only)** scope.

The broader Prop 3.3.A (ξ_0 + ρ + a_k) scope remains gated
on writing out the parametric-in-d ρ_d formula at d ≥ 3,
which is independent of the literature acquisition (per
D2-NOTE v1 §3 last paragraph).
