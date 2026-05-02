# Rubber-duck critique — T37F-Q18-NUMERICAL-PROBE

## E.1 checklist

(a) **Phase 0 branch pinning is documented unambiguously**
    -> `phase_0_branch_pinning.json` records branch (+) and branch (-)
       with explicit `c` value, `zeta_signed = 2c` (signed; negative in
       branch (-)), and a written rationale. The recurrence-derivation
       script `derive_recurrence_QL09_opposite_branch.py` was run and
       reports `bracket = 0` for QL09, with the parity test passing.
       The pinning was NOT silently inferred; it is documented.

(b) **Phase 0 sanity check at n=100 was performed**
    -> `t37f_run.log` records `sanity n=100: |a_minus/a_plus| = 1.0`,
       which is a strong pass (within [1e-10, 1e10] band by 10 orders
       of magnitude on each side). In fact the ratio is 1.0 to working
       precision — see Unexpected Find #1: this is the structural
       a_n(-c) = (-1)^n a_n(+c) identity at work.

(c) **Phase B uses K_lead = 25 (017c-measured stable optimum), NOT 40**
    -> `t37f_runner.py` constants block: `K_LEAD = 25`,
       `K_LEAD_GRID = [20, 25, 30]`. The 017c probe_K finding is
       referenced in the docstring. K_lead = 40 is NOT used.

(d) **Phase C.4 PSLQ HARD HYGIENE: dual-tolerance check**
    -> `pslq_probe` is called at tol=1e-8 and tol=1e-12. The runner
       checks `if pslq_loose and not pslq_strict` and halts with
       `T37F_PSLQ_OVERCLAIM` in that case. For the actual run,
       `|a_1_minus|` was below 1e-3 so PSLQ was not invoked
       (consistent with classification (a) THIRD_STRATUM); both
       results are recorded as `None` in claims.jsonl.

(e) **Phase D classification covers all four cases**
    -> `classify()` returns one of:
        - `BRANCH_DEGENERATE` (rank loss or |C_minus| < 1e-50)
        - `THIRD_STRATUM_CONFIRMED` (|a_1_minus| < 1e-30)
        - `BASIS_SHADOW_CONFIRMED` (|a_1_minus| > 1e-3)
        - `BASIS_SHADOW_PARTIAL` (otherwise)
       and the certificate writes one branch of recommendations per
       outcome. All four labels also map to verdict labels per §6 of
       the prompt.

## Additional self-critique

* **Forbidden-verb hygiene.** Searched `q18_numerical_certificate.md`
  and `handoff.md` for `proves|confirms|shows|demonstrates|
  establishes|validates|verifies|certifies` in prediction-or-
  conjecture context. Found `confirmed` only as a label suffix
  (`THIRD_STRATUM_CONFIRMED`), which is a controlled token, not a
  prose claim. Found "consistent with" used for the actual prose
  judgement of the result.

* **Discrepancy with 017c D values.** Logged in
  `discrepancy_log.json`. 017c's D for QL09 was BLOCKED (half-range
  ~10^11 times median) so neither side has a meaningful D number.
  Phase D classification is driven by |a_1| only.

* **Numerical evidence strength.**
  - `|a_1_branch_minus| = 2.17e-61` (envelope median)
  - half-range = 1.7e-40 (the half-range exceeds the median because
    the underlying value is structurally zero and the 9 envelope
    configs probe the precision floor)
  - even the half-range is 10^10 below the 1e-30 THIRD_STRATUM
    threshold
  - decision is robust by 30+ orders of magnitude

* **Structural insight (Unexpected Find #1).** The branch (-) and
  branch (+) recurrences satisfy `a_n(-c) = (-1)^n a_n(+c)`
  exactly. With `zeta_signed = 2c` (signed), `T_n` is therefore
  *literally identical* across branches. This is not a feature
  specific to QL09 — it applies to every d=2 PCF. Hence the Q18
  branch question is provably NOT a degree of freedom at the level
  of T_n with the signed convention. The QL09 a_1 = 0 vanishing
  must therefore be structural (alpha^2 + 16*alpha*gamma = 4*beta^2
  identity for QL09), not a convention shadow.

* **Scope discipline.** No other reps' opposite branches scanned
  (out-of-scope per §8). Only QL09. Only one pair of branches.

* **Compute discipline.** Total runtime ~3 seconds wall-clock
  (recurrence is fast at dps=300 N=2000). Well under the 1.5h
  budget.
