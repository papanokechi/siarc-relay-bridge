# Phase D — Verdict aggregation

## Input verdict signals

| Phase | Signal                              | Source |
|-------|-------------------------------------|--------|
| A     | `A_DIRECT_IDENTITY`                  | `phase_a_summary.md` |
| B     | `B_TEMPLATE_PARAMETRIC` (Conj 3.3.A* scope) | `phase_b_summary.md` |
| B     | `B_MACHINERY_NEEDED at d ≥ 3` (Prop 3.3.A scope, ρ_d) | `phase_b_summary.md` |
| C     | `HALT_Q20_LITERATURE_MISSING`        | `phase_c_summary.md` |

## Aggregation

Per Q20 prompt §2 Phase D.1:

  UPGRADE_FULL ← A_DIRECT_IDENTITY ∧ B_TEMPLATE_PARAMETRIC
                 ∧ C_LITERATURE_UNIFORM

  UPGRADE_PARTIAL_d_LE_d* ← (...) ∧ (...) ∧
                  (C_LITERATURE_UNIFORM ∨
                   C_LITERATURE_BOUNDED_AT_d*)

  UPGRADE_REJECTED ← any of: A_SYMBOLIC_FAILS,
                  B_PROOF_BREAKS at d ≤ 3,
                  C_LITERATURE_BOUNDED_AT_d* with d* < 3

The Phase C signal here is `HALT_Q20_LITERATURE_MISSING`,
which is neither `C_LITERATURE_UNIFORM` nor
`C_LITERATURE_BOUNDED_AT_d*`.  Per Q20 prompt §4
HALT_Q20_LITERATURE_MISSING handler:

> Wasow / Adams / BT / Conte-Musette not in operator's
> library at Phase C start. Produce partial output
> (Phases A + B only); skip Phases C, D, E in original
> form. Output verdict UPGRADE_PARTIAL_PENDING_LITERATURE
> with explicit "Phase C deferred" note.

and §6 Outcome Ladder item 3:

> 3. UPGRADE_PARTIAL_PENDING_LITERATURE
>    → Phase C deferred; Phases A + B complete
>    → moderate outcome; resumable on G3b literature
>      acquisition.

## Phase D verdict

**`UPGRADE_PARTIAL_PENDING_LITERATURE`**

### Scope of the partial verdict

- Phase A.2 establishes the closed-form identity
  `ξ_0 = d / β_d^{1/d}` as a **direct algebraic identity**
  uniform in `d ≥ 2`, for the **leading characteristic
  root of L_d at the slope-1/d edge of its Newton polygon
  at z=0**.  This is sympy-exact and reproducible.
- Phase B.4 establishes that the d=2 proof template
  (D2-NOTE v1 Prop 3.3.A sketch / CT v1.3 Prop xi0 sketch)
  has a **clean parametric-in-d line-by-line replacement**
  for the ξ_0 components (L1–L6 + L9), reducing to the d=2
  proof at d=2.  L7 and L8 (ρ and a_k) are out of scope for
  Conj 3.3.A* and remain open for Prop 3.3.A's broader
  components.
- Phase C cannot verify, from primary sources, that the
  Newton-polygon-to-Borel-singularity bridge (Wasow §X.3 +
  B–T 1933) is uniformly stated at general d ≥ 2.  This is
  the literature gate, not a structural gate.

### What is NOT discharged (residual operator action)

1. Primary-source verification of Wasow §X.3 / Adams 1928 /
   Birkhoff 1930 / B–T 1933 at general d (as flagged in
   T1-BIRKHOFF-TRJITZINSKY-LITREVIEW PHASE 2).  Acquisition
   would discharge the Conj 3.3.A* upgrade to
   `UPGRADE_FULL` (for the ξ_0-only scope).
2. PCF-1 v1.3 §5 source-drift check (D2-NOTE v1 ↔ PCF-1
   v1.3 §5 statement comparison).  D2-NOTE v1 and CT v1.3
   §3.3.A internally agree; PCF-1 v1.3 §5 not in workspace.
   Light residual operator-side action.
3. Parametric-in-d ρ_d formula at d ≥ 3 (open per D2-NOTE
   v1 §3 last paragraph).  Independent of the literature
   gate.  Required for upgrading Prop 3.3.A in full
   (ρ statement); NOT required for upgrading Conj 3.3.A*
   in isolation.

## What this means for SIARC

- **G1** (algebraic ξ_0 identity at general d): structural
  evidence STRENGTHENED by Phase A.  Status remains
  `proven at d=2, verified at d∈{3,4}, conjectured at d≥5`
  (no change), but the **structural claim that the d=3
  proof generalizes** is now AEAL-anchored at the
  symbolic level (`A_DIRECT_IDENTITY`).
- **G2** (closed at d=3, per Prompt 012): unchanged.
- **M2** (Conj 3.3.A* upgrade decision): partial; UPGRADE_FULL
  conditional on T1 PHASE 2 literature acquisition for the
  ξ_0-only scope.
- **M9** (SIARC-MASTER-V0 gating): unchanged this session
  (M2 partial, not done).
- **CT v1.4 amendment recommendation:** add a
  "Conj 3.3.A* upgrade conditional on T1 PHASE 2" footnote
  to §3.3.A; cite Phase A symbolic derivation
  (`phase_a_symbolic_derivation.py`) as the structural
  uniformity anchor.
