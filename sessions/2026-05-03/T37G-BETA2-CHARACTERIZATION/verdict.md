# T37G-BETA2-CHARACTERIZATION verdict

**Verdict label:** `HALT_T37G_GATE_NOT_SATISFIED`

**Halt key fired:** `T37G_GATE_NOT_SATISFIED` (spec §4 / §A.1).

**Status:** HALTED.

---

## Gate

Per spec §GATES / §A.1, this prompt fires **only if** the prior session's
halt_log.json contains a halt key in

```
{T37_NEXT_SECTOR_BETA_NONZERO, T37E_NEXT_SECTOR_BETA_NONZERO}
```

The prompt names two candidate prior sessions:

* `siarc-relay-bridge/sessions/2026-05-02/T37-S2-EXTRACTION-POLYNOMIAL-AWARE/`
* `siarc-relay-bridge/sessions/2026-05-02/T37E-EXTENDED-RECURRENCE/`

## Observed prior halt keys

| session                              | halt keys                                                              | verdict label                              | gate match |
|--------------------------------------|------------------------------------------------------------------------|--------------------------------------------|------------|
| T37-S2-EXTRACTION-POLYNOMIAL-AWARE   | `T37_K_SENSITIVITY_DIVERGENT`, `T37_D_CONSISTENT_WITH_ZERO` (×4 reps each) | (no `Verdict label:` line in `verdict.md`) | NO         |
| T37E-EXTENDED-RECURRENCE             | (none)                                                                 | `T37E_PARTIAL_a_1_NULL_AT_HIGHER_PRECISION` | NO         |

Neither session produced a `*_NEXT_SECTOR_BETA_NONZERO` halt key. The
gate is not satisfied.

## Action

Per spec §4 / §A.1, Phases B-F (refined free-`beta_2` scan, partition
test, universality test, PSLQ probe, certificate) are **not run**.
Phase A's input-validation step is the entirety of this session.

## Files produced

* `t37g_runner.py`               — gate-check runner
* `halt_log.json`                — single halt entry, full prior-session survey
* `discrepancy_log.json`         — empty
* `unexpected_finds.json`        — empty
* `beta_2_per_rep.json`          — stub (not produced; gate halt)
* `beta_2_stability_grid.json`   — stub (not produced; gate halt)
* `beta_2_pslq_probe.json`       — stub (not produced; gate halt)
* `partition_test.json`          — stub (not produced; gate halt)
* `universality_test.json`       — stub (not produced; gate halt)
* `closed_form_test.json`        — stub (not produced; gate halt)
* `claims.jsonl`                 — 4 honest entries (see handoff §AEAL note)
* `handoff.md`                   — this session
* `rubber_duck_critique.md`      — gate-only checks
* `verdict.md`                   — this file

## Recommendation

If the operator wants T37G to fire, the prior pipeline (017c or 017e)
must first land a `*_NEXT_SECTOR_BETA_NONZERO` halt. As of 2026-05-02
the d=2 next-sector exponent `beta_2` has not been measured to fall
outside zero by >5 sigma in either prior session, so 017g has nothing
to characterise.
