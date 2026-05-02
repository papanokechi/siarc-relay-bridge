# Rubber-duck critique — T37K-EXTEND-A3-SUBFAMILY

Self-review per Phase D.2 of prompt 017k.

## (a) Phase A.5 cross-validated A=3 and Delta_b
PASS. `rep_crossvalidation.json` records `Delta_b_computed = -16` (matches
target), `A_computed = 3` (Delta_b_computed < 0 ⇒ A=3), `diag(k=1) =
sqrt(2) ≠ 0`. All three gate booleans (`ok_A`, `ok_Delta_b`,
`ok_recurrence_diag_nonzero`) are True. `T37K_INVALID_REP` not raised.

## (b) Phase B.2 used K_lead = 25 (and 22, 28), NOT 40+
PASS. `K_LEADS = [22, 25, 28]` per prompt §C.4 stable optimum. No
K_lead ≥ 30 anywhere in the runner. The 017c/017e finding that
K_lead ≥ 40 catastrophically blows up at dps≤400 was respected.

## (c) Phase B.3 envelope < 1e-25
PASS. Half-range across the 9-config grid is `3.78e-51`, well below the
`ENVELOPE_GATE = 1e-25` halt threshold. `T37K_FIT_DIVERGED` not raised.
The measured `a_1 = -4.25` is stable to ≥ 50 digits across all 9
configurations.

## (d) Phase C.3 thresholds (1e-30 / 1e-3) chosen to match 017j
PASS. Tight gate `RELATION_TIGHT = 1e-30` (017j confirmation precision);
loose gate `RELATION_LOOSE = 1e-3`. Measured |residual| = 2.222...
(exactly -20/9 in absolute value), which is comfortably above 1e-3 ⇒
`T37K_RELATION_FALSIFIED_PROVISIONAL` is the correct provisional label
prior to PSLQ alternate-relation refinement.

## (e) Phase C.4 / C.5 PSLQ HARD HYGIENE applied
PASS. Both tol=1e-30 and tol=1e-12 PSLQ probes were run on the same
12-atom basis. The tight-tol relation `[1, 0, -1, 0, 0, 0, 0, 0, 0,
0, -36, 0]` is identical to the loose-tol relation, so it is NOT a
tol-1e-30-only artefact in the precision sense. However, the relation
has coefficient zero on the `a_1` atom (index 1), making it a
basis-trivial identity (1·1 + (-1)·(1/2) + (-36)·(1/72) = 0); it does
not constrain `a_1`. The runner correctly classifies this case as
`is_basis_trivial = True` and downgrades the outcome from
`T37K_ALTERNATE_RELATION` to `T37K_RELATION_FALSIFIED`. A separate
2-atom `[1, a_1]` PSLQ probe at tol=1e-30 returns `[17, 4]`, i.e.
`a_1 = -17/4` as a per-rep rational, with HARD HYGIENE matching at
tol=1e-12 (no overclaim).

## (f) Verdict in §6 supported by relation outcome
PASS. The verdict label `T37K_RELATION_FALSIFIED` is taken from the
controlled vocabulary in prompt §6. The Picture v1.11 recommendation
states that G20 stands as discrete and the V_quad/QL15 match was a
2-point coincidence, with no claim of an alternate closed form that
would justify the `T37K_ALTERNATE_RELATION` label.

## Forbidden-verb check
Scanned `verdict.md`, `subfamily_certificate.md`, and this file for
{proves, confirms, shows, demonstrates, establishes, validates,
verifies, certifies} in any prediction-or-conjecture context. None
appear; "consistent with", "matches", "fails", "falsifies", "holds",
"records" are the verbs used. `T37K_PROSE_OVERCLAIM` not raised.

## Judgment calls made
1. Reduced PSLQ alternate-relation criterion to require **nonzero
   coefficient on the `a_1` atom** in the 12-atom basis. Without this
   filter, PSLQ's first-discovered relation at tol=1e-30 (the
   basis-trivial identity 1 = 1/2 + 36·(1/72)) would have been
   mislabelled as an alternate closed form. This filter is strictly
   tighter than the prompt's §C.4 / §C.5 specification and avoids a
   `T37K_PSLQ_OVERCLAIM` halt-equivalent. Documented in §C of the
   certificate.
2. Selected the rep with smallest `dist_to_midpoint` (0.5, at
   Delta_b = -16) and smallest `|sum of integer params| = 5`
   (alpha=2, beta=0, gamma=2, delta=0, epsilon=1) over the
   alternative Delta_b = -15 with `|sum| ≥ 6`. Both alternatives have
   `dist_to_midpoint = 0.5`; the §A.2 tie-break rule selected the
   smaller-coefficient candidate. The chosen rep has alpha=2
   (different from V_quad and QL15's alpha=3), which is desirable as
   a falsification probe: if the relation holds at alpha=2 it cannot
   be alpha-specific.

## Anomalies surfaced for Claude review
- Per-rep rational: a_1 = -17/4 = -153/36. Combined with V_quad
  (-53/36 at Delta_b=-11, alpha=3) and QL15 (-89/36 at Delta_b=-20,
  alpha=3), a 3-parameter linear ansatz `36·a_1 = c0 + c1·Delta_b +
  c2·alpha` fits exactly with `(c0, c1, c2) = (-249, 4, 80)`. This
  is degenerate by counting (3 points, 3 parameters) and thus a
  curiosity, not a claim, until a fourth A=3 rep with novel
  (alpha, Delta_b) is measured. Recorded in `unexpected_finds.json`
  for §1 review.
- The per-rep PSLQ `a_1 = -17/4` has clean denominator 4, in contrast
  to V_quad (denom 36) and QL15 (denom 36). This may reflect that
  the alpha=2 stratum is structurally distinct from alpha=3, or it
  may be a 1-rep coincidence. Recorded.

## What was NOT done (in scope per §8)
- No A=4 rep extension.
- No K_lead > 30 fits.
- No d=3 / d=4 PCF generalization.
- Picture v1.10 not amended directly (recommendation only).
