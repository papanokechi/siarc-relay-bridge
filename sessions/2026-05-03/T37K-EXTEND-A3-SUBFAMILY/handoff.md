# Handoff — T37K-EXTEND-A3-SUBFAMILY
**Date:** 2026-05-03
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~30 minutes
**Status:** COMPLETE

## What was accomplished
Selected a third A=3 PCF representative (alpha=2, beta=0, gamma=2,
delta=0, epsilon=1; Delta_b=-16) by parametric enumeration with
tie-break on `dist_to_midpoint(-15.5)` then on `|sum of integer
params|`. Derived its Birkhoff a_n recurrence at dps=300, N=2000.
Ran the 017c-style two-stage windowed fit on K_lead in {22, 25, 28}
× W1 in {(800,1200), (800,1500), (800,1800)} (9 configs). Tested the
candidate A=3 sub-family relation (2A)^2 * a_1 = 4*Delta_b - 9 (i.e.
36*a_1 = 4*Delta_b - 9 at A=3). The relation fails: measured
a_1 = -17/4 = -153/36 versus predicted -73/36; residual -20/9
(absolute value 2.22...). Per-rep [1, a_1] PSLQ confirms the
rational a_1 = -17/4 at tol=1e-30 with HARD HYGIENE matching at
tol=1e-12. The 12-atom basis PSLQ surfaced only a basis-trivial
identity (1 - 1/2 - 36*(1/72) = 0, with coefficient zero on a_1),
which the artefact filter correctly downgrades.

## A=3 sub-family relation outcome
**Verdict: T37K_RELATION_FALSIFIED**

The two-point fit (V_quad at Delta_b=-11, QL15 at Delta_b=-20) was
a coincidence. With the third A=3 rep at Delta_b=-16, the relation
36*a_1 = 4*Delta_b - 9 predicts a_1 = -73/36 = -2.0278, while the
measured value is a_1 = -17/4 = -4.25 (clean per-rep rational,
PSLQ-confirmed at tol=1e-30, denominator 4 not 36). G20 catalogue
stands as discrete; no A=3 sub-family closed form via the
(2A)^2*a_1 = 4*Delta_b - 9 ansatz.

## Key numerical findings
* Third A=3 rep selected: (alpha, beta, gamma, delta, epsilon) =
  (2, 0, 2, 0, 1); Delta_b = -16; |sum| = 5; non-degenerate
  3-term recurrence; A_computed = 3 cross-validated; script
  `t37k_runner.py`.
* a_1 median (60-digit cap) = `-4.25` exactly (to >= 50 digits);
  envelope half-range = `3.78e-51` across the 9-config grid;
  K_lead in {22,25,28}, W1 in {(800,1200),(800,1500),(800,1800)};
  script `t37k_runner.py` at dps=300, N=2000.
* Per-rep PSLQ on [1, a_1] returns relation [17, 4] at tol=1e-30,
  i.e. a_1 = -17/4 with HARD HYGIENE at tol=1e-12 matching;
  script `t37k_runner.py`.
* Predicted a_1 from relation = (4*(-16) - 9) / 36 = -73/36
  = -2.0278; residual = a_1 - predicted = -20/9 = -2.222...;
  |residual| > 1e-3 ⇒ relation falsified (not in indeterminate
  band); script `t37k_runner.py`.
* 12-atom-basis PSLQ relation at tol=1e-30 = `[1, 0, -1, 0, 0, 0,
  0, 0, 0, 0, -36, 0]` (basis-trivial identity 1 - 1/2 - 36*(1/72)
  = 0; coefficient zero on a_1); same relation at tol=1e-12;
  artefact filter (a_1_coef == 0) classifies as not a relation
  involving a_1.
* Cross-rep consistency: 4*Delta_b - 36*a_1 - 9 evaluated at each
  A=3 rep — V_quad gives 0 (algebraic), QL15 gives 0 (algebraic),
  third rep gives `+80` (= -64 + 153 - 9). Relation does not
  hold as a global integer identity across the three A=3 reps.

## Judgment calls made
* PSLQ alternate-relation criterion was tightened to require
  **nonzero coefficient on the a_1 atom** in the 12-atom basis.
  Without this filter, the basis-trivial identity 1 - 1/2 -
  36*(1/72) = 0 (which PSLQ finds first at tol=1e-30 because the
  basis contains rank-deficient atoms) would have been mislabelled
  as `T37K_ALTERNATE_RELATION`. Documented in
  `rubber_duck_critique.md` §(e).
* Selected (alpha=2, beta=0, gamma=2, delta=0, epsilon=1) over the
  alternative (alpha=2, beta=1, gamma=2, delta=0, epsilon=1) at
  Delta_b=-15. Both have `dist_to_midpoint = 0.5`; the 017k §A.2
  tie-break selected smallest `|sum|` = 5 (vs 6). The chosen rep
  has alpha=2, contrasting with V_quad and QL15 (both alpha=3),
  which is desirable as a falsification probe across alpha
  strata.

## Anomalies and open questions
* **Three-rep linear ansatz curiosity (Claude review).** The three
  A=3 measurements `(alpha, Delta_b, 36*a_1)` =
  `{(3,-11,-53), (3,-20,-89), (2,-16,-153)}` are exactly fit by
  the 3-parameter form `36*a_1 = -249 + 4*Delta_b + 80*alpha`.
  This is degenerate by counting (3 points, 3 parameters) and
  therefore not elevatable. If a fourth A=3 rep with novel
  (alpha, Delta_b) (e.g. alpha=1 at Delta_b ∉ {-11, -16, -20}, or
  alpha=4) returns 36*a_1 = -249 + 4*Delta_b + 80*alpha to >= 30
  digits, the ansatz becomes an A=3 sub-family closed form
  candidate (with 1 spare degree of freedom). Otherwise, the
  three-point linear relation is also a coincidence and the A=3
  stratum is genuinely discrete in (alpha, Delta_b). Recorded in
  `unexpected_finds.json`.
* **Denominator stratification.** V_quad and QL15 (both alpha=3)
  have a_1 with denominator 36; the third rep (alpha=2) has
  denominator 4. The denominator may track alpha (e.g. denom = some
  function of alpha). Worth checking if the (alpha=1, alpha=4)
  candidates from the linear-ansatz falsification probe report
  denominators that fit a denom(alpha) rule.
* **alpha-dependence detected.** The original (2A)^2*a_1 =
  4*Delta_b - 9 ansatz was alpha-blind; the falsification at
  alpha=2 is consistent with the picture that a_1 carries
  non-trivial alpha-dependence beyond the implicit Delta_b =
  beta^2 - 4*alpha*gamma route. Any future closed-form ansatz on
  the A=3 stratum must explicitly carry alpha (or a function
  thereof) as an argument, not just Delta_b and A.

## What would have been asked (if bidirectional)
* Should the 3-parameter ansatz `36*a_1 = -249 + 4*Delta_b +
  80*alpha` be elevated as the next candidate closed form despite
  being interpolation-degenerate, or held as a curiosity until a
  fourth rep falsifies it (rule of four for 3-parameter linear
  forms)?
* Is alpha=1 or alpha=4 the more informative falsifier? alpha=4
  doubles the alpha range (3, 2 -> 4) and would test whether the
  c2 coefficient (80 in the current fit) holds at alpha=4. alpha=1
  fills in below alpha=2 and tests the same.
* For the QL09 anomaly (a_1 = 0 at A=4, Delta_b=1), is a similar
  "rule of three" extension warranted on the A=4 side? At present
  A=4 has only QL05 (a_1=31/4) and QL09 (a_1=0); a third A=4 rep
  with novel Delta_b would mirror the 017k extension on the
  positive-Delta_b side.

## Recommended next step
Compose **T37L-EXTEND-A3-FOURTH-REP**: select a fourth A=3 rep
with `alpha ∈ {1, 4}` (or a new value distinct from {2, 3}) and
Delta_b not in {-11, -16, -20}. Two natural candidates from
parametric enumeration:
- alpha=1, beta=0, gamma=4, delta=0, epsilon=1 → Delta_b=-16
  (collision; not allowed)
- alpha=1, beta=0, gamma=3, delta=0, epsilon=1 → Delta_b=-12
- alpha=1, beta=0, gamma=5, delta=0, epsilon=1 → Delta_b=-20
  (collision; not allowed)
- alpha=4, beta=0, gamma=2, delta=0, epsilon=1 → Delta_b=-32
- alpha=4, beta=0, gamma=1, delta=0, epsilon=1 → Delta_b=-16
  (collision; not allowed)

Test the 3-parameter linear ansatz `36*a_1 = -249 + 4*Delta_b +
80*alpha` against the new rep at >= 30-digit precision. If it
fails, the A=3 stratum is genuinely discrete in (alpha, Delta_b)
and any closed form requires more than 3 atoms. If it holds, the
ansatz is a candidate sub-family relation with one spare degree
of freedom (4 reps fitting a 3-parameter law).

## Files committed
* `t37k_runner.py`
* `third_A3_rep_selection.json`
* `rep_crossvalidation.json`
* `recurrence_third_A3_rep.csv`
* `a_1_third_A3_rep_fit.json`
* `subfamily_relation_test.json`
* `cross_rep_consistency.json`
* `subfamily_certificate.md`
* `verdict.json`
* `verdict.md`
* `halt_log.json` (empty)
* `discrepancy_log.json` (empty)
* `unexpected_finds.json`
* `claims.jsonl` (15 entries)
* `rubber_duck_critique.md`
* `runner.stdout.log`
* `handoff.md` (this file)

## AEAL claim count
15 entries written to `claims.jsonl` this session (target was >= 14).
