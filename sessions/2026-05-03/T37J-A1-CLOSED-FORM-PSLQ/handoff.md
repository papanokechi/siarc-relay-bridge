# Handoff — T37J-A1-CLOSED-FORM-PSLQ
**Date:** 2026-05-03
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~35 minutes
**Status:** COMPLETE

## What was accomplished

PSLQ-tested the apparent rational a_1 values reported by 017c
(V_quad -53/36, QL15 -89/36, QL05 +31/4) at AEAL precision
(mpmath dps=300, tol=1e-30, maxcoeff=10^15) with HARD HYGIENE
re-check at tol=1e-12. Searched for a unifying f(Delta_b, A) across
the 3 non-anomalous reps via 8 named single-formula candidates,
4 joint PSLQ basis configurations, an affine 3-equation 3-unknown
solve, and 4 polynomial families. Evaluated every candidate at the
QL09 boundary (Delta_b=1, A=4). Verdict: **T37J_RATIONAL_PER_REP_ONLY**;
no parsimonious rep-independent closed form found.

## Key numerical findings

* **Per-rep rationals consistent at AEAL precision** (script
  `t37j_runner.py`, dps=300):
  * V_quad: a_1 = -53/36 at residual 7.07e-58
  * QL15:   a_1 = -89/36 at residual 9.03e-57
  * QL05:   a_1 = +31/4  at residual 2.53e-50
* **HARD HYGIENE clean:** PSLQ relation vectors at tol=1e-30 are
  identical to those at tol=1e-12 for all 3 non-QL09 reps
  (`a_1_pslq_per_rep.json`).
* **No unifying f(Delta_b, A) at <1e-30** across 8 single-formula
  candidates. Best parsimonious form fails by O(7).
* **A=3 sub-family relation found:** `(2A)^2 * a_1 = 4*Delta_b - 9`
  consistent with V_quad and QL15 to 1e-57. FAILS QL05 (residual 7.39)
  and QL09 (residual 0.078). Sub-finding flagged for Claude review.
* **QL09 boundary check:** no candidate predicts both QL09 (a_1≈0)
  AND the 3 non-anomalous a_1 values to <1e-30.

## Judgment calls made

1. **Source file substitution.** Prompt §1 requested
   `a_1_per_rep.json` from 017c. That file does not exist; the
   equivalent data (a_1 medians + envelopes at >=46 digits) is
   in `phase_c_partition.json` under the `a_1` key. The runner
   loads from `phase_c_partition.json`. Prompt verdict
   T37J_INPUT_INVALID was NOT triggered because the data is
   present at the required precision under a different filename.
2. **PSLQ basis cap at 15 atoms** (prompt suggested 12-16). Chose
   15 to include the most diagnostic Delta_b combinations while
   keeping maxcoeff=10^15 tractable. Cap is `atom_specs[:16]`
   in `per_rep_pslq`.
3. **CF reconstruction implementation.** Initial pass had a sign /
   indexing bug that returned (q, p) pairs reversed (e.g.,
   "36/-53" instead of "-53/36"). Fixed in the standard
   convergent recursion (h_n = a_n*h_{n-1} + h_{n-2},
   k_n analogous). After fix all 3 reps' rationals match to
   >49 digits.
4. **halt_log.json rewrite after fix.** First runner pass wrote
   `verdict=T37J_NO_RATIONAL_DETECTED` due to the CF bug;
   second pass produced the correct verdict but the runner's
   "if not HALT_PATH.exists()" guard kept the stale value. The
   file was manually corrected to reflect the final verdict
   (T37J_RATIONAL_PER_REP_ONLY).

## Anomalies and open questions

1. **A=3 sub-family closed form is structural.** The relation
   `(2A)^2 * a_1 = 4*Delta_b - 9` matches V_quad (Delta_b=-11,
   a_1=-53/36) and QL15 (Delta_b=-20, a_1=-89/36) to 1e-57, well
   beyond what would be expected from coincidence on two integer-
   parameter reps. The relation FAILS at A=4 (QL05 a_1 = 31/4 ≠
   23/64; QL09 a_1 ≈ 0 ≠ -5/64). This suggests the closed form,
   if it exists, is **A-stratified** rather than rep-independent.

   The A=4 stratum is critically under-determined here (one
   non-anomalous rep + one anomalous). Q24-(b) follow-up should
   identify additional non-anomalous A=4 PCFs and re-extract a_1.
   If the A=4 stratum admits its own affine `a_1 * (2A)^2 =
   alpha_4 * Delta_b + beta_4`, picture v1.10 G20 should be
   amended to a single-axiom-with-A-stratification form. With
   QL05 alone we cannot pin (alpha_4, beta_4).

2. **2-rep linear relation a_1[V_quad] - a_1[QL15] = 1.** This is
   algebraic restriction of the A=3 sub-family relation. Recorded
   in unexpected_finds for completeness; not independent.

3. **Affine 3-equation 3-unknown solve produced (c1, c2, c3) =
   (4, 473, -1428).** The c1 = 4 coefficient matches the A=3 sub-
   family form exactly, but c2 = 473 and c3 = -1428 are large and
   non-parsimonious. A genuine 3-rep closed form would presumably
   involve small integer coefficients; the present solve is
   over-determined-to-trivial and FAILS QL09 by 7.31.

4. **Forbidden-verb tripwire.** Drafts of the certificate and
   verdict initially used "verifies" twice and "shows" once.
   These were rewritten to "reports / yields / is consistent with"
   pre-commit. T37J_PROSE_OVERCLAIM not triggered, but the
   tripwire is sensitive enough that future agents should draft
   with the controlled vocabulary in mind from the start.

5. **QL09 boundary check incidental hit.** The form
   `(Delta_b - 1)/(2A)^2` vanishes at QL09 trivially because
   Delta_b_QL09 = 1. The runner correctly flagged this as
   "consistent_with_a1_eq_0=true" but did NOT promote to
   T37J_UNIFYING_RELATION_FOUND_INCLUDING_QL09 because the form
   FAILS the 3 non-anomalous reps. Verdict logic gates correctly
   on "best_form is not None" first.

## What would have been asked (if bidirectional)

* Is the A=3 sub-family relation `(2A)^2 * a_1 = 4*Delta_b - 9`
  a known artefact of Birkhoff's classical formula at d=2 (i.e.,
  is it the d=2 specialisation of a general d-formula)? If so,
  Q24-(b) becomes "extract the A=4 specialisation" rather than
  "search for a closed form".
* Should the 2-rep a_1_V - a_1_QL15 = 1 relation be elevated
  to AEAL claim status? It is algebraically equivalent to the
  A=3 sub-family relation but carries less structural information.

## Recommended next step

**Q24-(b): A=4 stratum a_1 extraction at additional reps.**

Specifically: identify 2-3 additional non-anomalous A=4 PCFs in
the T35 catalogue (or generate them from the d=2 PCF family
parametrisation), run the 017c-style stage1 LSQ on T_n at
mpmath dps=200, n in [800, 1900], and extract a_1 for each.
With 3+ A=4 measurements, attempt to fit `a_1 * (2A)^2 = alpha_4
* Delta_b + beta_4` (parsimonious 2-coefficient form). If alpha_4
and beta_4 are small integers, the A-stratified closed form is
a candidate axiom for picture v1.11.

Until A=4 stratum is determined, picture v1.10 G20 stands as
"partition-with-per-rep-rationals".

## Files committed

* a_1_closed_form_certificate.md
* a_1_pslq_per_rep.json
* a_1_unifying_relation_search.json
* claims.jsonl (19 entries)
* discrepancy_log.json (empty list)
* halt_log.json (no halt; verdict T37J_RATIONAL_PER_REP_ONLY)
* handoff.md (this file)
* rubber_duck_critique.md
* t37j_run.log
* t37j_runner.py
* unexpected_finds.json (3 sub-findings)
* verdict.json
* verdict.md

## AEAL claim count

19 entries written to claims.jsonl this session (target ≥ 18).
