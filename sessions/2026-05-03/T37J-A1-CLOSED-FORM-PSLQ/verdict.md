# Verdict — T37J-A1-CLOSED-FORM-PSLQ

**Status:** `T37J_RATIONAL_PER_REP_ONLY`

## Result summary

Phase B reports per-rep PSLQ relations consistent with rationals at tol=1e-30, maxcoeff=10^15:

| rep    | Delta_b | A | apparent rational | residual   |
|--------|---------|---|-------------------|------------|
| V_quad |   -11   | 3 | **-53/36**        | 7.07e-58   |
| QL15   |   -20   | 3 | **-89/36**        | 9.03e-57   |
| QL05   |    +8   | 4 | **+31/4**         | 2.53e-50   |
| QL09   |    +1   | 4 | 0 (≈ 1.7e-57)     | (excluded from B; Q18 anomaly) |

HARD HYGIENE: PSLQ relations at tol=1e-30 are identical to those at
tol=1e-12 for every rep — no precision-artefact relations.
T37J_PSLQ_OVERCLAIM not triggered.

Phase C finds **no parsimonious unifying f(Delta_b, A)** consistent
with all 3 non-anomalous reps to <1e-30. The (Delta_b - 9/4)/A^2 form
fits the A=3 sub-family (V_quad, QL15) to 1e-57 but fails QL05 by ≈7.39.
3-coefficient polynomial families saturate by construction (3 unknowns,
3 measurements) and are not parsimonious closed forms; they fail the
QL09 boundary check (predicting a_1 ~ 7 instead of ~ 0).

Phase D finds no candidate predicting all 4 reps. The (Delta_b - 1)/(2A)^2
form vanishes at QL09 trivially (Δ_b=1) but fails the other 3 reps.

## Sub-findings flagged for Claude

1. **A=3 sub-family relation:** `(2A)^2 * a_1 = 4*Delta_b - 9`
   * V_quad: 36*(-53/36) = -53 = 4*(-11) - 9 ✓
   * QL15:   36*(-89/36) = -89 = 4*(-20) - 9 ✓
   * QL05 (A=4): predicts a_1 = 23/64; measured 31/4. FAILS.
   * QL09 (A=4): predicts a_1 = -5/64; measured ≈ 0. FAILS.
2. **2-rep linear:** `a_1[V_quad] - a_1[QL15] = 1` (algebraic
   consequence of (1) at fixed A=3 with Δ_b differing by 9).

These are consistent with the closed form, if any, being
**A-stratified** rather than a single rep-independent f(Δ_b, A).
Confirmation would require additional A=4 non-anomalous reps (Q24-(b)).

## Picture v1.11 recommendation

**Hold picture v1.10.** Do NOT amend to v1.11.

The 017j evidence is consistent with G20 closure as
"partition-with-per-rep-rationals" (017c). It does NOT support
upgrading to a single closed-form axiom. The A=3 sub-family relation
is a candidate axiom for a future A-stratified picture; it is
flagged in unexpected_finds.json for follow-up.

## AEAL footnote

19 entries in claims.jsonl (target >= 18). No HARD HALT. No prose
overclaim tripwire.
