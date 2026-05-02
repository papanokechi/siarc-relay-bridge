# T3 verdict

**Task:** T3-CONTE-MUSETTE-PAINLEVE-TEST
**Date:** 2026-05-02
**Status:** COMPLETE

## Verdict

**H3 = D=2_REDUCTION_AMBIGUOUS is closed under the Conte–Musette
algorithmic test at d=2** in the following precise sense:

- All 10 d=2 families (six Δ_b<0 named — V_quad, QL01, QL02, QL06,
  QL15, QL26 — and four Δ_b>0 representatives QL05, QL09, QL13,
  QL18) **pass** all three Conte–Musette branches and return the
  same Painlevé-class signature **P_III(D₆)**.
- V_quad sanity check (Phase D) **passes**: the pipeline assigns
  V_quad the class P_III(D₆) consistent with CT v1.3 Theorem 3.3.D.
- The Conte–Musette test as defined here **does not separate the
  Δ_b<0 anomaly bin from the Δ_b>0 elementary bin**.  The H3
  ambiguity is therefore not resolved at the level of the
  algorithmic Painlevé test on the linear OGF ODE: it requires an
  isomonodromic-deformation construction and Sakai-surface
  analysis, exactly as the H3 verdict cautioned.

## What this changes

- The Conte–Musette pipeline is the agreed canonical algorithmic
  test in the SIARC fleet's H3 plan.  Running it uniformly on the
  d=2 catalogue produces a clean per-family verdict table and an
  explicit, reproducible result.
- The d=3 catalogue (50 cubic families) is now entirely covered by
  the same pipeline.  Result: 50/50 LABELED, all
  PAINLEVE_UNCLASSIFIED, because the Newton polygon slopes 4/3 at
  x=0 and 2/3 at x=∞ fall outside the classical P_I..P_VI list.
  This is consistent with the d=3 dichotomy seen in PCF-2 v1.3
  Sessions B + C1 (uniform A_fit ≈ 6 across the cubic catalogue)
  and provides an algorithmic — not just empirical — argument for
  the d=3 stratum being fundamentally different from d=2.

## What this does NOT change

- A LABELED outcome is **passes the Conte–Musette test (necessary
  condition)**.  It is not a proof that any family is Painlevé
  reducible to P_III(D₆).  V_quad's reduction is an *anchored*
  case; the other nine d=2 families remain
  Conte–Musette-consistent without independent confirmation.
- The four Δ_b>0 representatives are a curated subset of the 24
  F(2,4) Trans families recorded in PCF-1 v1.3 Table 1; the
  remaining 20 elementary-positive families are not covered here
  (they are expected to behave identically under this algorithmic
  test, since the test depends only on the OGF ODE coefficient
  pattern).

## Anomaly bin (β²−4αγ < 0) status

All six Δ_b<0 families return LABELED with class P_III(D₆).
**The anomaly bin is invisible to this Conte–Musette test.**
The classical-vs-transcendental dichotomy of PCF-1 v1.3 §3 is not
reproducible from Newton-polygon / indicial / reflection data
alone, in agreement with the H3 verdict.

## Cross-degree comparison

- d=2: 100 % LABELED, class P_III(D₆) (rank-1 irregular at both ends).
- d=3: 100 % LABELED, class PAINLEVE_UNCLASSIFIED (rank 4/3 at 0,
  rank 2/3 at ∞ — fractional, outside P_I..P_VI).

This algorithmic separation between d=2 and d=3 is the
publication-grade outcome of the test: even though both degrees
pass the necessary condition, only d=2 carries a standard
Painlevé-class signature.
