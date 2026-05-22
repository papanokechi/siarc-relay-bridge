# M2-REFIRE — PARTIAL-HALT REPORT

**Bridge session:** `VALIDATED-ARITH-M2-REFIRE`
**Date:** 2026-05-22
**Work order:** `WORK ORDER -- MILESTONE 2 RE-FIRE: PRECISION-HARDENED CERTIFIED BOUND` (issued 2026-05-22 12:57 local)
**Verdict:** `INCOMPLETE` (gate did not pass; **no certified bound emitted**)
**Authority:** orchestrator `certified_bound_refire.py` → `k_stability_report.json`

---

## TL;DR

The M2-REFIRE K-stability gate did **NOT** pass. Both PSLQ discovery runs
(`dps=8640` and `dps=28712`) were initiated against the M1-certified ball
midpoints. In this session the `dps=8640` run was killed externally at
iter=3230 (an interruption, not a natural terminal state), and the
`dps=28712` run is still in flight at iter=308 with an estimated wall-clock
of hundreds of hours remaining.

Per the work-order's explicit escape clause:

> If the dps=28712 run cannot complete in the available budget, that is a
> PARTIAL-HALT: deposit the dps=8640 result + the checkpointed 28712 progress,
> report "K-stability gate INCOMPLETE — 28712 run unfinished", and do NOT
> emit a final M_certified. An honest "not done" beats a bound off a
> single dps.

No `M_certified` is in force. `theorem.json` top-level `M_certified` remains
`null` with `status=PENDING_M2_REFIRE`. The void record for the prior
`M_certified=91` (dps=2160 spurious termination) is preserved.

---

## Step-by-step record

### Step 0 — Void the prior result ✅ (was already in place)
- `theorem.json` top-level `M_certified`: `null`, `status`: `PENDING_M2_REFIRE`.
- `theorem.json.void_record`: holds the prior `M_certified=91`, marked VOID with
  reason `precision-starved spurious termination`, `superseded_by`: `M2-REFIRE`.
- M1-ball SHA256 reasserted in-session:
  - `M1_outputs/balls_P28712.json` = `4729ea6cc4c2d433cbcb44c6f210ba82e22d77f51753c86aedce9562449a1ccf` ✓
  - `M1_outputs/balls_P14356.json` = `378407d760627fd1dab5f3493d8e29037c63d76a4f92a066736b43238af03f54` ✓

### Step 1 — Hardened discovery oracle ✅
- `_refire_discovery.py` enforces `dps ∈ {8640, 28712}` (dps=2160 explicitly **banned**).
- Input vector is the M1-certified ball **midpoint** at `P_bits=28712`, **not** `mpmath.khinchin` (the prior trajectory-difference root cause).
- `maxcoeff = 10**70`, `maxsteps = 250_000` (generously above empirical K~29363).
- Verbose `pslq` stdout is line-buffered to disk so the iteration counter K is checkpointed continuously.

### Step 2a — Discovery runs

| run | dps | started UTC | last K logged | observation UTC | wall-clock elapsed | rate (iter/s) | terminal state |
|-----|-----|-------------|---------------|-----------------|--------------------|---------------|-----------------|
| d8640_P28712  | 8640  | 12:49:39 | 3230 | 15:40:07 (kill) | 10227 s | 0.32 (early) → 0.15 (steady) | `INTERRUPTED_PARTIAL` |
| d28712_P28712 | 28712 | 13:01:03 | 308  | 15:46:14 (deposit) | 10069 s | 0.031 | `IN_FLIGHT` (orphaned, still alive) |

Empirical neighborhood K~29363 (from the historical m32a cascade, retained as
an expectation only — *not* a target).

- The `d8640` worker process (PID 14280) was killed externally
  (interrupt_cause recorded as "KeyboardInterrupt external (terminal session
  reset)"). The salvaged checkpoint at `_refire_checkpoint_d8640_P28712.json`
  is explicitly labeled `INTERRUPTED_PARTIAL` and carries a `salvage_note`
  stating it is **not** a result and **does not** satisfy the gate.
- The `d28712` worker process (PID 26608, parent 18648) is **alive** at
  deposit time. Its parent (PPID 9476) is gone; the worker is orphaned and
  should continue running unattended.

### Step 2b — Candidate verification at ≥32768 bits
- **No candidates produced** by either run before the partial-halt.
- `candidate_log` in `k_stability_report.json` is empty.

### Step 2c — K-stability gate
- Orchestrator verdict: **`INCOMPLETE`** (`missing checkpoints for dps=[28712]`).
- `K_stable`: `null`.

### Step 3 — Certified bound derivation
- **NOT EXECUTED**. Gate did not pass. No `M_certified` produced.

### Step 4a — False-negative guard ✅
- Planted relation `[1,-1,1]` on basis `[π, π+1, 1]` was detected by the oracle and
  the bound machinery returned `M_certified=1 < √3` as required.
- `guard_pass: true` recorded in `k_stability_report.json`.

### Step 4b — Provenance trace
- `bound_provenance.json` from the (now VOID) earlier run is preserved as-is.
- No new provenance trace was emitted because no bound was emitted.

### Step 4c — Candidate-rejection log
- Empty (no candidates this run). The historical dps=2160 spurious-termination
  candidate remains documented in `halt_log_M2.json` (preserved as a
  methodological finding).

---

## Sanity check on the orchestrator machinery (executed)

`_refire_dryrun.py` was run inside this session to validate the certified-bound
machinery would behave correctly **if** the gate had passed:

- `arb_thm1_init_bound` on the M1 ball at `ctx.prec=32768` →
  `[1.000003058379838526957307262625875010636 +/- 1.85e-40]` → `floor = 1`.
- `arb_cor2_bound(K=29363)` →
  `[6664694780684395394919.015967382401788721 +/- 4.73e-19]` → `floor = 6664694780684395394919`
  (~6.66 × 10²¹, comfortably between the void `91` and the empirical heuristic `1.036e72`,
  i.e. inside the work-order's sanity band).
- `arb_floor_lower_endpoint([12345.678 ± 1e-30])` = `12345` ✓.
- `propagated_uncertainty_floor` on a small synthetic relation produces
  an Arb of radius ~10⁻⁸⁶⁶⁷ as expected from the M1 ball radii.

Conclusion: **the certified-bound code path is sound**. The reason no
`M_certified` is emitted is **purely** that the discovery oracle has not
produced two CONVERGED_NULL terminal states yet — the gate is the blocker,
not the bound math.

---

## Why the runtime was insufficient

The work-order acknowledged this risk verbatim:

> The dps=28712 PSLQ run is the EXPENSIVE step (prior 60-min budget was killed
> mid-run). Allocate a long budget.

Observed in-session steady-state rates:

- `dps=8640`: ~0.15 iter/s during the high-norm phase. Reaching K~29363 from
  cold start: ~54 wall-clock hours.
- `dps=28712`: ~0.031 iter/s observed. Reaching K~29363: ~263 wall-clock hours
  (~11 days), to first order. (Rate may stabilise or worsen as norms grow.)

These figures exceed any practical single agent-session budget.

---

## Operator next actions

1. **Let the `d28712` process run unattended.** It is orphaned but alive
   (worker PID 26608, parent 18648). It will produce
   `_refire_checkpoint_d28712_P28712.json` upon natural termination
   (CANCELLING via `norm_bound > maxcoeff` or RELATION found).
2. **Restart `d8640`** in a clean process that won't be killed by terminal
   cleanup. The previous worker (PID 14280) was killed prematurely; the
   `INTERRUPTED_PARTIAL` salvage is unusable for the gate.
3. **Re-invoke `python certified_bound_refire.py`** once both checkpoint JSONs
   exist with terminal-state ∈ {CONVERGED_NULL, RELATION_CANDIDATE}. The
   orchestrator handles candidate verification, the gate, and (on PASS) the
   bound derivation automatically. No code changes are required.
4. **Sanity expectation** (per work order Step 3): a passing gate with
   K~29363 yields `M_certified ~ 6.66 × 10²¹`. A bound near `91` or
   ≥ `1.036 × 10⁷²` would HALT and require recheck.

---

## Anti-laundering assertion

No certified bound was emitted from a single dps. No `dps=2160` artifact was
consumed. No `mpmath` real value entered any certified chain. The
`INTERRUPTED_PARTIAL` and `IN_FLIGHT` states are recorded honestly and the
gate verdict is `INCOMPLETE`. **An honest "not done" beats a bound off a
single dps.**

---

## Deliverables emitted by this session

| file | status | purpose |
|------|--------|---------|
| `theorem.json` | unchanged (already PENDING_M2_REFIRE; void_record preserved) | no certified bound in force |
| `k_stability_report.json` | new (orchestrator-emitted) | gate verdict INCOMPLETE; full state |
| `halt_log_M2_REFIRE.json` | **new** | formal partial-halt event record |
| `M2_REFIRE_REPORT.md` | **new** (this file) | human-readable summary |
| `claims.jsonl` | appended (pre + post + partial-halt actualise) | AEAL ledger |
| `_refire_checkpoint_d8640_P28712.log` | preserved | line-buffered K trace (killed at iter=3230) |
| `_refire_checkpoint_d8640_P28712.json` | preserved | salvage record |
| `_refire_checkpoint_d28712_P28712.log` | live (process still appending) | line-buffered K trace, mid-run |
| `_refire_checkpoint_d28712_P28712.json` | **not yet present** | will be written when d28712 terminates |

No `bound_provenance.json` update was emitted (no new bound to provenance-trace).
