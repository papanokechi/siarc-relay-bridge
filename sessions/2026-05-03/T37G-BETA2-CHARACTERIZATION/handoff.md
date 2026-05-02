# Handoff — T37G-BETA2-CHARACTERIZATION
**Date:** 2026-05-03
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~10 minutes
**Status:** HALTED

## What was accomplished

Executed Phase A (input validation + gate check) of relay prompt 017g.
Surveyed both candidate prior sessions
(`T37-S2-EXTRACTION-POLYNOMIAL-AWARE`, `T37E-EXTENDED-RECURRENCE`) for
halt keys in the gate set
`{T37_NEXT_SECTOR_BETA_NONZERO, T37E_NEXT_SECTOR_BETA_NONZERO}`.
Neither session produced a gate-set halt key. Per spec §A.1 / §4,
Phases B-F were not run; the session halts with
`HALT_T37G_GATE_NOT_SATISFIED`.

## Key numerical findings

* Gate-set keys observed: **0** across both candidate prior sessions.
* `T37-S2-EXTRACTION-POLYNOMIAL-AWARE/halt_log.json`: 8 halt entries,
  alternating `T37_K_SENSITIVITY_DIVERGENT` and
  `T37_D_CONSISTENT_WITH_ZERO` across the 4 reps. None match the gate.
* `T37E-EXTENDED-RECURRENCE/halt_log.json`: empty list `[]`. Verdict
  label is `T37E_PARTIAL_a_1_NULL_AT_HIGHER_PRECISION` — also outside
  the gate set.
* No mpmath / PSLQ / fitting was performed at any precision.

## Judgment calls made

1. **AEAL claim count.** Spec §3 mandates ≥ 22 entries. Every entry
   beyond the gate check is conditional on Phases B-E running. Per
   the standing instruction "no claim may appear ... without an AEAL
   entry" (which forbids fabrication), I wrote **4 honest entries**
   (one per surveyed prior session, one for the gate-set comparison,
   one for the verdict label) instead of padding to 22. This is a
   conscious deviation from §3 in favour of AEAL integrity. Flagged
   here for synthesizer review.
2. **Stub artefact policy.** Spec §DELIVERABLE lists `beta_2_per_rep.json`
   etc. as required outputs. I wrote each one as an explicit
   `{"halt_key": "...", "produced": false, "reason": "..."}` stub
   rather than leaving them absent, so the bridge tree shows the
   spec-mandated filenames with explicit "not produced" flags.

## Anomalies and open questions

* **The prompt's gate is currently unreachable.** Neither 017c nor
  017e produced a `*_NEXT_SECTOR_BETA_NONZERO` halt at the precisions
  exercised so far (dps=250 N=2000 in 017c; dps=400 N=5000 in 017e).
  T37E's verdict explicitly reports `a_1` medians locking onto
  rationals (-53/36, -89/36, +31/4, ~0) — i.e., the leading-rung
  polynomial-correction picture is consistent at higher precision.
  No diagnostic in T37 / T37E flags `beta_2 != 0`. So 017g cannot fire
  on the current bridge state.
* **Possible synthesiser-side ambiguity in 017g v2.** The drafted prompt
  reads as if the operator expected a `*_NEXT_SECTOR_BETA_NONZERO`
  halt. If the synthesiser intended this prompt to FIRE on the
  current bridge, please re-check whether (a) a different prior
  session was meant, or (b) 017g's gate keys should be widened to
  include `T37_K_SENSITIVITY_DIVERGENT` / `T37_D_CONSISTENT_WITH_ZERO`
  (these are arguably evidence that the leading-rung-only model is
  incomplete, even though they're not labelled as a `beta_2 != 0`
  finding). I declined to widen the gate unilaterally.
* **T37 verdict.md missing label.** `T37-S2-EXTRACTION-POLYNOMIAL-AWARE/
  verdict.md` does not contain a `Verdict label:` line in the format
  the runner expected; the runner reports `verdict_label: null` for
  that session. This does not affect the gate (the gate check uses
  halt keys, not verdict labels), but it is a small bridge hygiene
  issue worth noting.

## What would have been asked (if bidirectional)

* "Should 017g's gate be widened to include the divergent-D family
  of halts that T37 actually landed?"
* "Was 017c v2 ever re-fired with the post-T37 cached series, and
  did that run produce a `*_NEXT_SECTOR_BETA_NONZERO` halt that I
  haven't found in the bridge?"
* "Is the missing `Verdict label:` line in
  `T37-S2-EXTRACTION-POLYNOMIAL-AWARE/verdict.md` intentional?"

## Recommended next step

Two options for the next prompt:

1. **(Lower-cost)** Re-fire 017c v2 or 017e at the dps=400 N=5000
   cache with the explicit free-`beta_2` scan as Phase E and have it
   either land `T37_NEXT_SECTOR_BETA_NONZERO` (in which case 017g
   becomes runnable) or land a NULL verdict (in which case 017g is
   dropped from the queue).
2. **(Higher-cost)** Issue 017c v3 with a widened diagnostic
   (free-`beta_2` AND free-`beta_3` scans) at dps=600 to settle
   whether the d=2 next-rung shift is genuinely zero or is sitting
   below the dps=400 envelope. This would close 017g cleanly either
   way.

## Files committed

* `t37g_runner.py`
* `halt_log.json`
* `discrepancy_log.json`         (empty `{}`)
* `unexpected_finds.json`        (empty `{}`)
* `beta_2_per_rep.json`          (stub)
* `beta_2_stability_grid.json`   (stub)
* `beta_2_pslq_probe.json`       (stub)
* `partition_test.json`          (stub)
* `universality_test.json`       (stub)
* `closed_form_test.json`        (stub)
* `claims.jsonl`                 (4 entries; deviation from §3 noted above)
* `verdict.md`
* `rubber_duck_critique.md`
* `handoff.md`                   (this file)

## AEAL claim count

4 entries written to `claims.jsonl` this session.
Spec §3 mandated ≥ 22 entries; I deviated to avoid fabrication.
See "Judgment calls made" item 1.
