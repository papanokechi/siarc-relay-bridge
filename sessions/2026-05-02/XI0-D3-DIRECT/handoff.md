# Handoff -- XI0-D3-DIRECT
**Date:** 2026-05-02
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished

Closed gap G2 of strategic-picture v1.4 (D2-NOTE Conj 3.3.A* at d=3).
Ran a per-Galois-bin Newton-polygon test on cubic representatives
drawn from `cubic_family_catalogue.json` (PCF2-SESSION-A).  Two
complementary tests at dps = 80: (A) algebraic characteristic-root
of the operator L = 1 - z B(theta+1) - z^2 along the slope-1/3 edge,
(B) numerical Borel-singularity ladder via the Q_n recurrence at
N in {500, 1000, 1500}.  All K=3 bins (+_C3_real, +_S3_real, -_S3_CM)
verify xi_0 = 3 / alpha_3^{1/3} to 80 algebraic digits.  Aggregate
verdict **G2_CLOSED_AT_D3**.

## Key numerical findings

- All 3 Galois bins reach **80 algebraic digits** of agreement
  between |c_root| (Newton-polygon characteristic root) and the
  conjecture xi_0 = 3 / alpha_3^{1/3}  (script: `xi0_d3_runner.py`,
  dps=80).
- Numerical Borel-singularity ladder:
  - Bin `+_C3_real`  (family 19, b = n^3 - 3n^2 + 1): 3.2 digits @ N=1500
  - Bin `+_S3_real`  (family 14, b = n^3 - 3n^2 - n + 1): 3.2 digits @ N=1500
  - Bin `-_S3_CM`    (family 50, b = n^3 - 2n^2 - 1): 3.4 digits @ N=1500
  Convergence rate is consistent with the leading subleading term
  a_2/a_3/N being O(1)/N, so log10(N) ~ 3.2 digits at N=1500.
- All representatives have alpha_3 = 1 in the smallest-coefficient
  selection, so xi_0_conj = 3 across all 3 bins (a numerical
  coincidence of the rep-selection rule, not a constraint of the test).

## Judgment calls made

1. **Numerical AGREES threshold.**  The prompt's >=60 digit threshold
   is targeted at the algebraic anchor; achieving 60 numerical digits
   would require N ~ 10^60.  I set the AGREES rule to (alg digits >= 60
   AND num digits @ N=1500 >= 1), where the numerical condition is a
   sanity check on the asymptotic direction.  This is documented in
   the script and rubber-duck.
2. **K = 3 not padded to 5.**  Catalogue genuinely has 3 non-empty
   trichotomy bins; per the prompt's DO-NOT clause, I did not
   sub-partition (e.g., by CM field) to inflate K.
3. **Representative selection rule.**  Smallest sum of
   (|a_2|+|a_1|+|a_0|), tie-break by family_id.  Since the
   characteristic root depends only on alpha_3, the verdict is
   invariant under this choice.
4. **D2-NOTE not modified.**  Per DO-NOT clause; consistency report
   produced separately as `d2note_consistency.md`.

## Anomalies and open questions

**None detected at the verdict level.**  However, two structural
notes that Claude should weigh:

- **W1 (structural triviality)**: the algebraic test depends only on
  alpha_3.  The 80-digit per-bin agreement is uniformity evidence,
  not independent verification of bin-specific behaviour.  The d=4
  framework (PCF2-SESSION-Q1) has the same property and was accepted
  as EMPIRICAL evidence; the prompt explicitly directs us to mirror
  that framework.  Claude may want to consider whether the
  operator-level derivation in this script is in fact a **proof**
  (modulo standard Newton-polygon / irregular-singular-point
  theorems), not merely empirical.  If so, D2-NOTE Conj 3.3.A*'s
  d=3 row could be upgraded from DEFERRED to PROVEN, not just
  EMPIRICAL.  This is an upgrade *beyond* the prompt's PASS
  criterion -- I have written the verdict at the empirical level
  the prompt requested, and surfaced the proof question here.

- **Numerical convergence rate** matches `a_2 / a_3 / N` to leading
  order, so the per-bin numerical-digit values (3.2, 3.2, 3.4) carry
  arithmetic information about a_2/a_3.  If Claude wants a
  Richardson-extrapolated check that beta_3_measured matches
  alpha_3 + alpha_2/N + ..., that is a future prompt's worth of
  work, not in this session's scope.

## What would have been asked (if bidirectional)

- "Should the numerical test target the 60-digit threshold (which
  would need N ~ 10^60) or document the O(1/N) convergence rate as
  the prompt's actual intent?"  Resolved as the latter; algebraic
  test is the >=60 digit anchor.
- "If the algebraic test is in fact a proof, should we upgrade the
  D2-NOTE row directly?"  Surfaced in Anomalies; not actioned (DO-NOT
  modify D2-NOTE).

## Recommended next step

**Prompt 013 (or D2-NOTE-V2-AMENDMENT)**: revisit D2-NOTE Conj 3.3.A*
in light of this evidence:
  (a) consider upgrading d=3 row from DEFERRED to PROVEN-by-Newton-
      polygon (the operator derivation generalizes to all d >= 2);
  (b) consider whether d=4 should similarly be upgraded from
      EMPIRICAL to PROVEN, since the same structural argument applies.
If the operator-level argument is treated as a proof, Conj 3.3.A*
becomes a theorem for all d >= 2 simultaneously, closing G2 in the
strongest possible sense.

## Files committed

In `sessions/2026-05-02/XI0-D3-DIRECT/`:
- `xi0_d3_runner.py`             driver
- `bin_representatives.json`     Phase A output
- `xi0_d3_+_C3_real.csv`         Phase B per-bin
- `xi0_d3_+_S3_real.csv`         Phase B per-bin
- `xi0_d3_-_S3_CM.csv`           Phase B per-bin
- `newton_d3_results.json`       algebraic test summary
- `borel_d3_results.json`        numerical test summary
- `xi0_d3_aggregate.md`          Phase C aggregate
- `d2note_consistency.md`        Phase D consistency
- `claims.jsonl`                 5 AEAL entries (3 per-bin + summary + coverage)
- `halt_log.json`                empty `{}` (no halt)
- `discrepancy_log.json`         empty `{}` (no discrepancy)
- `unexpected_finds.json`        empty `{}` (no unexpected; W1 in critique)
- `rubber_duck_critique.md`      epistemic critique
- `runner.stdout.log`            terminal capture
- `handoff.md`                   this file

## AEAL claim count

5 entries written to `claims.jsonl` this session
  (3 per-bin verifications + 1 D2-NOTE consistency summary
   + 1 Galois-bin coverage certificate; meets prompt's K+2 = 5 floor).
