# Rubber-duck critique — T37J-A1-CLOSED-FORM-PSLQ

Internal pre-handoff sanity pass. Five gates from prompt §E.2.

## (a) Phase A.2 precision threshold (1e-30) verified?

YES. From `t37j_runner.py` (`precision_check`): for each non-QL09 rep,
ratio = envelope / |median| was computed and compared to 1e-30.

| rep    | envelope   | |median| | ratio       | < 1e-30? |
|--------|-----------|----------|-------------|----------|
| V_quad | 6.27e-48  | 1.4722   | ~4.3e-48    | YES      |
| QL15   | 2.39e-46  | 2.4722   | ~9.7e-47    | YES      |
| QL05   | 1.41e-40  | 7.75     | ~1.8e-41    | YES      |

QL09 was excluded by design. Gate PASSES; T37J_PRECISION_INSUFFICIENT
not triggered.

## (b) Phase B HARD HYGIENE (tol=1e-30 AND tol=1e-12) applied per rep?

YES. `per_rep_pslq` computes BOTH `rel_tol_1e-30` (with maxcoeff=1e15)
and `rel_tol_1e-12` (with maxcoeff=1e8). Output JSON includes the
`hygiene_flag_loose_only` field for each rep. For all 3 non-QL09
reps, the relation vector at tol=1e-30 is IDENTICAL to the vector
at tol=1e-12, so `hygiene_flag_loose_only = false`. No relation is
"only at the looser tolerance"; T37J_PSLQ_OVERCLAIM not triggered.

## (c) Phase C explored multiple functional forms, NOT just one?

YES. 8 explicit single-formula candidates were tested:
1. Delta_b/(2A)^2
2. (Delta_b - 1)/(2A)^2
3. Delta_b/A^2
4. Delta_b/(A*(A-1))
5. Delta_b/(4A)
6. Delta_b*A/(2A)^2
7. Delta_b/(A^2 - 1)
8. (Delta_b - 9/4)/A^2 (V_quad+QL15-derived)

Plus an affine 3-equation 3-unknown solve and 4 polynomial families.
All max-residuals reported in `a_1_unifying_relation_search.json`.

## (d) Phase D explicitly checks QL09 against any candidate f?

YES. `ql09_boundary` evaluates 6 named single-formula candidates,
the affine 3-eq solution, and 4 polynomial families at (Δ_b=1, A=4)
and computes `delta_vs_measured_a1` for each. Results recorded in
`a_1_unifying_relation_search.json` under `ql09_boundary`.

The (Delta_b - 1)/(2A)^2 form is the only candidate that vanishes
at QL09 within QL09's envelope, and it fails the 3 non-QL09 reps,
so it is NOT promoted to a unifying f.

## (e) Verdict in §6 supported by strongest match?

YES. The verdict ladder is:

* `T37J_UNIFYING_RELATION_FOUND_INCLUDING_QL09` — requires (i) some f
  with max-residual < 1e-30 across V_quad/QL15/QL05 AND (ii)
  consistency at QL09. Neither holds. NOT TRIGGERED.
* `T37J_UNIFYING_CLOSED_FORM_FOUND` — requires (i) only. Not held
  (best parsimonious f has max-residual >7). NOT TRIGGERED.
* `T37J_RATIONAL_PER_REP_ONLY` — requires per-rep rationals verified
  (Phase B) AND no unifying f (Phase C). HOLDS. TRIGGERED.

`T37J_RATIONAL_PARTIAL` and `T37J_NO_RATIONAL_DETECTED` are weaker
labels and would be selected only if some/all per-rep rationals
failed the tol=1e-30 check; all 3 passed.

Verdict choice is consistent with the ladder.

## Additional sanity checks

1. **Sign of A=3 sub-family relation:** verified by hand:
   * V_quad: 4*(-11) - 9 = -53 ✓
   * QL15: 4*(-20) - 9 = -89 ✓
2. **Sign of A=3 sub-family failure at A=4:**
   * QL05: predicted 4*8 - 9 = 23, so a_1 = 23/64 ≠ 31/4 = 496/64.
     Mismatch ratio 496/23 ≈ 21.6, structural and large.
3. **PSLQ basis rank:** the 15-atom basis includes 9 inverse-integers
   plus 4 Delta_b-derived atoms plus a_1 plus 1; no two atoms are
   integer-linearly identical at finite precision. T37J_RANK_LOSS
   not triggered.
4. **Forbidden-verb hygiene:** scanned the certificate, verdict, and
   handoff text for the controlled-vocabulary words {proves, confirms,
   shows, demonstrates, establishes, validates, verifies, certifies}
   (§5 of prompt 017j). Initial drafts of the certificate and verdict
   used "verifies" twice and "shows" once; both were rewritten to
   "reports / is consistent with / yields" prior to commit. Final
   prose contains none of the forbidden verbs in any prediction-or-
   conjecture context. T37J_PROSE_OVERCLAIM not triggered.

## Pre-flight conclusion

All 5 gates pass. Verdict T37J_RATIONAL_PER_REP_ONLY is supported
by §B (per-rep rationals at AEAL precision) and §C/§D (no parsimonious
unifying f). Two structural sub-findings flagged for Claude in
unexpected_finds.json. Picture v1.10 stands.
