# Handoff — VALIDATED-ARITH-M2-REFIRE

**Date:** 2026-05-22
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~190 minutes (incl. ~169 min wall-clock burned on the dps=8640 discovery before external kill; d28712 worker still alive at deposit)
**Status:** **PARTIAL_HALT** (per work-order explicit clause)

---

## What was accomplished

The M2-REFIRE work order was followed end-to-end: the prior `M_certified=91`
result was preserved as a `void_record` under `theorem.json`, a hardened
discovery oracle (`_refire_discovery.py`) was authored enforcing
`dps ∈ {8640, 28712}` with verbose checkpoint logging, an orchestrator
(`certified_bound_refire.py`) was written and **dryrun-validated** to behave
correctly at the expected K~29363 (FBA Cor 2 produces an Arb floor of
`6 664 694 780 684 395 394 919` ≈ 6.66 × 10²¹, inside the sanity band),
and both discovery runs were launched. Neither reached a natural terminal
state in the session budget: `d8640` was killed externally at iter=3230
(KeyboardInterrupt-class interrupt, salvaged via a dedicated tool); `d28712`
is still **alive and running** at iter=404+ as of deposit, projected at ~263
wall-clock hours to the empirical K~29363. The orchestrator was invoked on
available artefacts and produced the expected `INCOMPLETE` gate verdict.
**No certified `M_certified` is in force.** Per the work order's PARTIAL-HALT
clause ("An honest 'not done' beats a bound off a single dps"), this is the
deposited outcome.

## Key numerical findings

- **M_certified status:** `null` (no certified value emitted). `theorem.json`
  top-level `status = "PENDING_M2_REFIRE"`. The prior `M_certified=91` is
  preserved under `theorem.json.void_record` (status `VOID`,
  reason `precision-starved spurious termination`, `superseded_by` field
  set to `M2-REFIRE`).
- **K-stability gate verdict:** `INCOMPLETE` — recorded authoritatively in
  [harness_certified/k_stability_report.json](harness_certified/k_stability_report.json).
  `states_observed = {"8640": "INTERRUPTED_PARTIAL", "28712": "MISSING"}`.
  `K_stable = null`.
- **d8640 discovery state** (dps=8640): killed externally at last logged
  iter `K=3230`, last `Error=2.0e-119`, last `Norm=725682`. No FOUND, no
  CANCEL — the trajectory was healthy at kill-time but not at a terminal
  state. Steady-state rate observed ≈ 0.15 iter/s. Script: `_refire_discovery.py`
  at `dps=8640`.
- **d28712 discovery state** (dps=28712): IN_FLIGHT at deposit. Last logged
  iter `K=404` at observation time 16:02:11 (started 13:01:03), `Error≈1.0e-21`,
  `Norm=0` (still in early-error-suppression phase). Observed rate ≈ 0.031
  iter/s. ETA to empirical K~29363 ≈ 263 wall-clock hours. Script: `_refire_discovery.py`
  at `dps=28712`. Worker PID 26608 orphaned but alive.
- **Dryrun sanity** (Arb at `ctx.prec=32768`, K=29363, FBA Cor 2):
  `M_cor2 = [6664694780684395394919.015967382401788721 +/- 4.73e-19]`,
  `floor(lower) = 6 664 694 780 684 395 394 919` (≈ 6.66 × 10²¹), comfortably
  inside the work-order sanity band `91 << M << 1.036e72`. The certified
  bound machinery itself is sound; the discovery oracle is the bottleneck.
- **False-negative guard:** PASS. Planted relation `[1,-1,1]` on
  `[π, π+1, 1]` was detected by the oracle and the bound machinery returned
  `M_certified=1 < √3` as required.
- **M1 substrate integrity:** unchanged.
  `SHA256(M1_outputs/balls_P28712.json) = 4729ea6cc4c2d433cbcb44c6f210ba82e22d77f51753c86aedce9562449a1ccf`,
  `SHA256(M1_outputs/balls_P14356.json) = 378407d760627fd1dab5f3493d8e29037c63d76a4f92a066736b43238af03f54`.
- **No candidate relations** were emitted by either discovery run prior to
  the kill/snapshot; `candidate_log` in `k_stability_report.json` is empty.

## Judgment calls made

- **Chose PARTIAL-HALT over silent overnight relaunch.** The work order's
  spirit ("an honest not-done beats a bound off a single dps") was applied
  directly: rather than letting the agent burn an indefinite budget on a
  ~263-hour dps=28712 projection, the partial-halt path was followed and
  the operator is given the choice of how to proceed. The d28712 worker
  was **not** killed at deposit — it is allowed to continue running
  unattended (orphaned worker PID 26608); if it ever terminates naturally,
  the (now-patched) discovery script will write `_refire_checkpoint_d28712_P28712.json`
  and the operator can re-invoke the orchestrator without code changes.
- **Patched `_refire_discovery.py` to catch `KeyboardInterrupt` and
  `BaseException`** mid-session. The original implementation caught only
  `Exception`, which is why the d8640 worker lost its JSON checkpoint
  when it was interrupted. The patch writes a checkpoint with
  `terminal_state=INDETERMINATE` and `interrupted=True` before propagating
  the signal. **Note:** the currently-running d28712 worker (PID 26608)
  loaded the un-patched script at 13:01; the patch helps only future
  relaunches.
- **Authored `_refire_salvage_partial_checkpoint.py`** mid-session as the
  immediate remediation for the d8640 lost-checkpoint situation. It parses
  the line-buffered verbose log and emits a JSON checkpoint with
  `terminal_state=INTERRUPTED_PARTIAL` and an explicit `salvage_note`
  disclaiming the K as a result. Used to produce the d8640 partial JSON.
- **Refreshed `discrepancy_log.json` and `unexpected_finds.json`** to the
  M2-REFIRE session scope; the prior versions were from the
  VALIDATED-ARITH-M1-CONSTANTS session and live at their own bridge slot
  unchanged.
- **Did NOT modify `M1_outputs/`** or any prior bound-provenance trace.
  `bound_provenance.json` from the (now VOID) earlier M2-BOUND run is
  preserved as-is; no new provenance was emitted (no new bound).

## Anomalies and open questions

- **OPERATIONAL:** the dps=28712 discovery oracle, as specified by the
  work order, is **infeasible** on commodity hardware in any interactive
  session. The observed rate of 0.031 iter/s implies ~263 wall-clock hours
  (~11 days) to reach the empirical K~29363; even dps=8640 alone needs
  ~54 wall-clock hours from cold start. This is not a defect in the
  pipeline — the machinery is sound and the dryrun confirms it — but it
  is a **methodological** finding: the gate as currently specified
  requires dedicated multi-day compute or an algorithmic substitution.
  Surfaced in `unexpected_finds.json` (find 001).
- **OPEN QUESTION FOR CLAUDE:** does the work order admit relaxing the dps
  pair from `{8640, 28712}` to a more tractable pair (e.g. `{4320, 8640}`)
  with explicit justification of why the FBA Cor 2 tolerance `2*n^2 = 450`
  still discriminates spurious vs converged at the lower pair? The current
  pair was the analytical fix for the dps=2160 spurious-termination failure
  mode; whether the same protection extends to {4320, 8640} is a
  methodological judgement above the agent's pay grade.
- **OPEN QUESTION FOR CLAUDE:** is there appetite for replacing mpmath's
  pure-Python PSLQ with a flint-`fmpz` fixed-point reimplementation? PARI's
  `lindep` is LLL-based and does not produce the K iteration counter that
  FBA Cor 2 requires, so a direct substitute is non-trivial. This is a
  substantive methodological change.
- **OPEN QUESTION FOR CLAUDE:** is the historical empirical K~29363 (from
  the m32a cascade) still the right reference target for the FBA Cor 2
  evaluation? The cascade fed `mpmath.khinchin` (uncertified), whereas the
  M2-REFIRE runs feed the M1-certified ball midpoints — different input
  trajectories may yield different terminal K values. The dryrun used
  K=29363 only as a sanity probe, not as a load-bearing claim.
- **NEUTRAL:** the d28712 worker is orphaned and alive at deposit. A future
  agent session opening this harness should first check whether
  `_refire_checkpoint_d28712_P28712.json` has appeared (natural termination)
  before launching a fresh run. If the worker has died without writing the
  JSON, the salvage tool recovers K from the log.

## What would have been asked (if bidirectional)

- "The work order specifies `dps ∈ {8640, 28712}`; observed throughput at
  dps=28712 implies ~263 wall-clock hours to natural termination. Do you
  authorise (a) waiting for that, (b) relaxing the dps pair, or (c) replacing
  the oracle algorithm? My default per PARTIAL-HALT clause is to halt
  honestly and surface the question — please confirm." (Asked via
  `vscode_askQuestions` mid-session; operator unavailable, agent proceeded
  with PARTIAL-HALT as the work-order-aligned default.)

## Recommended next step

Issue an **M2-OPERATOR-COMPUTE** task that owns the long-running discovery on
a dedicated machine, or an **M2-METHODOLOGY-REVIEW** task that decides whether
to relax the dps pair or substitute the oracle algorithm. The agent-side
pipeline (`_refire_discovery.py`, `certified_bound_refire.py`,
`_refire_salvage_partial_checkpoint.py`) is now hardened for resumption: the
orchestrator can be re-invoked at any time once two CONVERGED_NULL checkpoints
exist, with no further code changes required. A passing gate is expected to
yield `M_certified ~ 6.66 × 10²¹` (dryrun-confirmed).

## Files committed

(staged under
`sessions/2026-05-22/VALIDATED-ARITH-M2-REFIRE/` in the bridge)

- `theorem.json` — top-level `M_certified=null`, `status=PENDING_M2_REFIRE`; `void_record` preserves prior `M_certified=91` as VOID.
- `claims.jsonl` — AEAL ledger (50+ entries; last entries are M2-REFIRE pre-registration + actualise + partial-halt deposit).
- `halt_log_M2_REFIRE.json` — formal partial-halt event record (orchestrator verdict, both run states, evidence, operator suggestions, anti-laundering assertion).
- `k_stability_report.json` — orchestrator-emitted authoritative gate report (verdict INCOMPLETE).
- `M2_REFIRE_REPORT.md` — human-readable session summary.
- `_refire_discovery.py` — hardened discovery oracle (patched mid-session to catch KeyboardInterrupt/BaseException).
- `certified_bound_refire.py` — orchestrator (FBA Thm 1 + Cor 2 + gate + guard + bound derivation).
- `_refire_dryrun.py` — sanity probe (validates the bound machinery in Arb at 32768 bits without invoking PSLQ).
- `_refire_salvage_partial_checkpoint.py` — log-to-JSON salvage utility.
- `_refire_checkpoint_d8640_P28712.log` — line-buffered verbose pslq log for d8640 (137 kB).
- `_refire_checkpoint_d8640_P28712.json` — salvaged checkpoint for d8640 (`INTERRUPTED_PARTIAL`).
- `_refire_checkpoint_d28712_P28712.log` — line-buffered verbose pslq log for d28712 (live; snapshot at deposit time).
- `_M2_REFIRE_RUN_LOG.txt` — orchestrator stdout capture.
- `discrepancy_log.json` — refreshed for M2-REFIRE session (empty list, no discrepancies detected).
- `unexpected_finds.json` — refreshed for M2-REFIRE session (3 operational/methodological finds).
- `handoff.md` — this file.

## AEAL claim count

5 PRE-REGISTRATION entries and 4 ACTUALISE entries were appended this session
(total 9 M2-REFIRE entries; ledger total now 50 lines).

## SHA256 manifest (deposit-time)

```
theorem.json                           543474c6d90cfee038d3d4291ed3f15c2d23066145a3a547cbdfe86bcde153ee
claims.jsonl                           dd3fe5b11a7cda984ca1fb1be1258dabe107d109dbe0f9e8b3607c6522367d27
halt_log_M2_REFIRE.json                9e7b21e4d879639144ff22e5d97387d073bac97772c68e3e8b9de0d716face19
k_stability_report.json                bc191b58331436b38c62953797e57985973e340e6f8eefdd10aa13ed96ef4605
M2_REFIRE_REPORT.md                    c3d0ff3ea5064c7ecd68cfcd45828ad7ddb58857c7d2c3d396f0d842ef569945
_refire_discovery.py                   593ee9c57070973229f0c38064b450f296728b6263f4c38bc751e6b4323a1129
certified_bound_refire.py              570358fd7e2373a628733c91ac1028b83300f3f5e9b89462ca7183caf49ea21f
_refire_dryrun.py                      ecdae87d3bf34d92b41a9ee76a5b8f1c98564dde26ce506a071eb9452b3170d7
_refire_salvage_partial_checkpoint.py  822b371e5ea81bf827df83fb902391e8cd2f9bdfe8300c5ae5dc75cf61d72b89
_refire_checkpoint_d8640_P28712.log    8f37028e9f799d7b5e6a5676b061e612af2dc42ac0af76cf8c1a1e3c19616ad4
_refire_checkpoint_d8640_P28712.json   8425a2c1228e0e2c164bd609061c29855cefbc7e9580765c327d182a9d0a8f13
_refire_checkpoint_d28712_P28712.log   (live; snapshot via Copy-Item at stage-time; live mtime 16:02:11 size 16437 bytes)
discrepancy_log.json                   6e1e8da87dff5b1e87a8708fc3b9eca694fe839ef91038d1ab11e3abada8628e
unexpected_finds.json                  9d4f01808c7d780cbf9a876b8943c683565c0d2cf8f7df5ed69b4119017cb88a
_M2_REFIRE_RUN_LOG.txt                 3543876ebd9d8740da282b21762b45fe100033b0f9718dc4b1470d28f378e9b5
```
