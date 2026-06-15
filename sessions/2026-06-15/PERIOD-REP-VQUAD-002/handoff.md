---
# Handoff — PERIOD-REP-VQUAD-002
**Date:** 2026-06-15
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~2 sessions (compaction-resumed)
**Status:** COMPLETE

## What was accomplished
Resolved the single blocker (G-OMEGA) left by PERIOD-REP-VQUAD-001. The V_quad
asymptotic series phi(z)=sum a_n z^n was shown to be **D-finite over Q(sqrt3)**
(unique minimal operator order 2, degree 4), and its Borel transform
B-hat(xi)=sum a_{m+1}/m! xi^m to be **holonomic order 4 over exactly Q(sqrt3)**
(operator L_V, singular locus {0, -2/sqrt3, infinity}). Because the candidate form
omega = B-hat(xi) dxi is therefore a section of a Q(sqrt3)-algebraic connection,
the Fresan-Jossen algebraicity axiom is **SATISFIED**. Stage-5 disposition
selection is mechanical: field exactly Q(sqrt3) => **outcome_GO_clean => sub-problem
A = GO**. The result was reached without a corpus Lax pair or Kovacic file (both
confirmed-absent); the exact Q(sqrt3) arithmetic was the lever.

## Key numerical findings
- a_n exactly in Q(sqrt3); exact Fraction-pair port reproduces deposited mpmath to
  rel **2.66e-120** at dps=120 (mpmath precision floor; the exact port is exact)
  (script=port_crosscheck.py)
- phi: unique minimal holonomic operator **order 2, degree 4** over Q(sqrt3); nullity
  pattern {1,3,5,7}(r=2) confirms uniqueness (script=holonomic_recognition_q3.py)
- B-hat: holonomic **order 4, degree 2** over Q(sqrt3); residual **identically zero**
  (exact algebraic, not numerical) over xi^0..xi^129 (script=extract_verify_operators.py)
- L_V leading coeff factors exactly: (210276+9720 sqrt3)/418501 * xi * (xi+2/sqrt3)
- Indicial exponents at -2/sqrt3 = {-(1+beta),0,1,2}, non-integer root
  **-(1+beta) = -1+sqrt3/9 = -0.8075499103** (beta=-1/(3 sqrt3)) (script=indicial_analysis.py)
- Borel-Pade dominant pole at **-1.1549 ≈ -2/sqrt3** on [20/20]..[40/40]
  (script=borel_pade_census.py)

## Judgment calls made
- **Stage 3 ran as the operative test** (not a fallback) because Stages 1-2
  confirmed G-LAX and G-KOVACIC absent in the corpus. The DO-NOT "run Stage 3 only
  if Stages 1/2 didn't resolve" was satisfied: they did not resolve algebraicity.
- **Exact Q(sqrt3) recognition over numerical PSLQ.** I hand-rolled a Q3 Fraction-pair
  field (no Sage/ore_algebra available) and did exact Gaussian-elimination nullspace.
  This yields an *algebraic* identity (residual identically 0), the gold standard for
  a field-determination claim — strictly stronger than the prompt's numeric <1e-100.
- **Reported the -xi0 sign refinement** rather than silently matching the parent's
  +xi0. The sign is a genuine finding (see Anomalies), not an error to hide.
- **Did NOT relitigate the SL(2)-Galois claim** (per task 2.3); only flagged the
  missing Kovacic-execution file as a corpus-organization issue.

## Anomalies and open questions
**[MOST IMPORTANT SECTION — flagged for Claude review]**

1. **SIGN: Borel singularity at -2/sqrt3, not +2/sqrt3 (anomaly A1-SIGN).** The
   parent located xi0=2/sqrt3 to 95.6 digits as a **modulus** (|a_n/a_{n+1}|*n ->
   2/sqrt3); the sign was never pinned. The a_n carry (-1)^{n+1} for n>=3, so
   b_m=a_{m+1}/m! ~ (-1)^m(+), putting the branch point on the **negative** real
   axis. This is bookkeeping, not algebra: it does NOT change the field and does
   NOT downgrade the verdict. But it **does** fix the geometry for sub-problem B —
   the rapid-decay thimble lies along arg xi = pi, and it aligns cleanly with the
   FJ e^{-f} convention (f = -xi, decay as xi -> -infinity). **Claude: confirm the
   parent's +xi0 in candidate-data.md is understood as a modulus before B is drafted.**

2. **G-LAX "absent" yet L_phi reconstructs the linear problem (anomaly A2).** No
   explicit Lax pair is deposited anywhere in project-fingerprint, yet the order-2
   L_phi over Q(sqrt3) IS the scalar/Schrodinger reduction of the V_quad PV linear
   problem (Riccati c=psi'/psi linearizes it). The corpus's "SL(2) by exact Kovacic"
   and EBR-II's "order-2 Heun, 4 singular points" are consistent with L_phi but the
   operator itself was never written down. **Corpus-organization flag:** the Galois
   claim rests on an un-deposited computation. Not relitigated here (per scope).

3. **No infinite resurgent tower (anomaly/bonus TOWER-1).** Holonomicity forces a
   finite singular locus {0,-xi0,infinity}, so there are NO singularities at
   2xi0,3xi0,... This **resolves** the open question the parent left at the (1/2)^n
   numerical floor: V_quad resurgence is a finite rank-4 connection, not a wild
   alien lattice. Worth a sentence in the eventual paper.

4. **Transcendence reconciliation (why GO is clean).** The transcendental PV
   accessory parameter lives in the *nonlinear* isomonodromy moduli (the Painleve
   transcendent y(t) is genuinely non-holonomic). The *linear* scalar reduction
   governing the asymptotic series is over Q(sqrt3). These are not in tension — but
   a careless reading of "PV is transcendental" could wrongly predict NO-GO. The
   paper must state this distinction explicitly.

## What would have been asked (if bidirectional)
- "The parent's xi0 is a modulus; I'm reporting the signed singularity at -2/sqrt3.
  Do you want candidate-data.md amended now, or carried as a correction into 003?"
  (I carried it as a documented refinement; no corpus edit, per governance.)
- "B-hat is order 4 over Q(sqrt3) but a *single* algebraic operator. Do you want me
  to also exhibit the full 2x2 Lax matrix M(t) now, or defer that to sub-problem C?"
  (Deferred to C; L_phi suffices for the algebraicity verdict.)

## Recommended next step
Open **PERIOD-REP-VQUAD-003** for sub-problem B (rapid-decay cycle formalization,
using the corrected -2/sqrt3 geometry and Hien's rapid-decay homology) and
sub-problem C (run Kovacic on the now-explicit L_phi to independently confirm SL(2);
compute the differential Galois group of L_V; symbolically verify
C = int_gamma e^{xi} B-hat(xi) dxi; state conditional transcendence under FJ
Conjecture 1.3.2). Tentative venue: Compositio Mathematica or JSC. Effort: B ~2-3 wk,
C ~2-4 wk. Do NOT draft the 003 prompt here — scope only (see final-verdict.md sec7.2).

## Files committed
- dispositions.json (Stage 0 HALT GATE)
- lax-pair-found.md (Stage 1, G-LAX confirmed-absent)
- kovacic-found.md (Stage 2, G-KOVACIC confirmed-absent)
- operator-verification.md (Stage 4, the technical heart)
- disposition-applied.md (Stage 5, mechanical GO_clean)
- fresan-jossen-recheck.md (Stage 6)
- final-verdict.md (Stage 7)
- ledger.json, claims.jsonl, handoff.md (Stage 8)
- scripts/holonomic_recognition_q3.py (+ _results.json)
- scripts/extract_verify_operators.py (+ operator_verification_results.json)
- scripts/indicial_analysis.py (+ indicial_results.json)
- scripts/borel_pade_census.py (+ borel_pade_results.json)

## AEAL claim count
16 entries written to claims.jsonl this session.
---
