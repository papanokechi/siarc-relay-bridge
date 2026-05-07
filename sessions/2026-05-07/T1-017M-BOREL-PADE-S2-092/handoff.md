# Handoff — T1-017M-BOREL-PADE-S2-092
**Date:** 2026-05-07
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~45 minutes (~88 s computation; rest is substrate readback + diagnostic build + deliverable composition)
**Status:** COMPLETE_PERMANENT_RESIDUAL

## What was accomplished

Executed relay 092's Borel-Padé exponential-asymptotics resummation of the 017m recurrence at dps=300 across the small-Padé regime (N,M ∈ {6, 8, 10, 12, 14, 16, 18}; 49 cells per rep, 196 cells total across V_quad / QL15 / QL05 / QL09). All 196 Padé approximants well-formed (no RANK_LOSS, no NO_POLE_NEAR_2 failures). Convergence-region detection: 0/84 adjacent (N,M) pairs reach the dps/4 = 75 digit threshold in any rep; best digits-of-agreement is 3.741 (V_quad). All four reps classify as `PERMANENT_RESIDUAL_G6b`. Aggregate M8b-axis verdict: `M8b_S2_PERMANENT_RESIDUAL_VIA_BOREL_PADE` (Phase D2 closure-by-residual-acceptance).

## Key numerical findings

- **Per-rep median |S_2 candidate| (dps=300, raw-series Borel-Padé):**
  V_quad 11.02 (rel half-range 2.14×; 7 N-rows × 7 M-cols stability table in `stability_table.md`).
  QL15 70.63 (rel half-range 3.95×).
  QL05 9.62 (rel half-range 76.85× — anomalously wide; D5).
  QL09 48.87 (rel half-range 10.08×).
- **Padé pole nearest u=2:** minimum across all 196 cells = 0.00537 (QL15 [16,14]); most cells have pole-distances in 0.3–0.7. A converged Padé would show monotonic shrinkage toward 0 as N+M grows; no such shrinkage observed.
- **Residue scaling:** at the (rare) cells where pole is near u=2, residues vary by 1–2 orders across adjacent (N,M) — no stable log-amplitude readable.
- **Implied |S_2|/|S_1| ratios across reps:** V_quad 0.216, QL15 0.526, QL05 1.091, QL09 1.281 — inconsistent across reps, further substantiating PERMANENT_RESIDUAL classification.
- **Comparison to 017L (T37E) LSQ baseline residual:** T37E reported rel half-range ~10^217 for Stage-2 D extraction. The present 092 Borel-Padé reports rel half-range 2.14–76.85 — approximately **215 orders of magnitude tighter** than LSQ baseline, yet still failing extraction threshold. Padé absence-of-convergence is a strictly stronger negative-result substrate.
- **Pade well-conditioning at small (N,M):** 196/196 OK cells across all reps. T37M's 9/12 RANK_LOSS per rep at M=200..800 confirms the small-(N,M) regime is the correct operating window for feasibility testing.

## Judgment calls made

1. **J1 — Interpretation of "017L" reference (D1).** 092 spec references "017L LSQ-residual recurrence substrate" (Phase A.P3, P5) but the prompt-archive shows the LSQ cascade as 017c → 017e (017m direct-Borel-Padé). Treated 017L as referring to T37E (extended-recurrence LSQ at dps=400/N=5000 with rel half-range ~10^217). Substrate location verified at `sessions/2026-05-02/T37E-EXTENDED-RECURRENCE/`.
2. **J2 — Raw vs leading-sector-subtracted Borel transform (D2).** 092 spec phase B1 says "formal Borel transform of the 017L asymptotic series (or its trans-series sector containing S_2)". Two methodologies plausible. T37M (2026-05-03) took the subtracted-high-order route and got RANK_LOSS. The present 092 fire deliberately took the raw-low-order route to provide an orthogonal negative-result substrate. The methodology is robust to choice (both fail).
3. **J3 — Stokes-constant magnitude convention (D3).** Padé approximants of real-coefficient series have real residues; T35's Stokes-imaginary factor `i` arises from the Borel-Laplace contour discontinuity, not from Padé. Reported "S_2 candidate" values are magnitudes (real); Im(S_2 candidate) is structurally zero across all 196 cells. For convergence detection magnitude is the right quantity. Documented for transparency.
4. **J4 — All-reps sweep (D4).** 092 phrases the task as "the M8b axis" (singular). 017m's deliverable is per-rep. Ran the sweep on all four reps and aggregated to a single M8b verdict via logical OR (any rep EXTRACTED → axis closed). All four reps PERMANENT_RESIDUAL → axis verdict PERMANENT_RESIDUAL.
5. **J5 — Spec halt-set self-check before Phase J writeup.** Explicitly verified all 5 spec halts (HALT_092_SUPERSEDED / NO_017L_SUBSTRATE / BOREL_PATHOLOGICAL / DPS_INSUFFICIENT / UNEXPECTED_POSITIVE) PASS with full rationale recorded in `halt_log.json`. PERMANENT_RESIDUAL_G6b is a verdict, not a halt — confirmed against the spec's Phase F note.

## Anomalies and open questions

1. **U1: Small-(N,M) Padé is well-conditioned at dps=300** — 196/196 OK cells across all reps, in stark contrast to T37M's 9/12 RANK_LOSS per rep. This validates 092's spec design choice (small-(N,M) = feasibility-test regime). May be useful for future Borel-Padé work generally.
2. **U2: Specific cells reach pole-distance 0.005 from u=2 but residues do not stabilise** — QL15 at (16,14) yields pole at distance 0.00537; (10,18) yields 0.04495; (12,18) yields 0.01997. Consistent with a Padé approximant **beginning** to resolve the sub-leading singularity. Forward-pointer: the **uncharted quadrant** is small-(N,M) Padé applied to the LEADING-SECTOR-SUBTRACTED residual (T37M's K=25 cleanness step + small-(N,M) instead of high-(N,M)). T37M did subtracted+high-order; 092 did raw+low-order; subtracted+low-order remains untested. Could be picked up in a future fire if M8b axis is ever revisited.
3. **U3: QL05 displays markedly wider |S_2| spread (76.85× rel half-range)** vs 2.14–10.08× for the other three reps. QL05 is the only `side='pos'` rep and the only one with `zeta_star = 4.0` exactly (vs irrationals for the others). Suggests Padé-fragility correlates with rep family (pos/neg side, integer/irrational zeta). Worth flagging if T2C precision-escalation monitor revisits QL05.
4. **U4: Stokes-convention `i` factor is a contour artifact, not a Padé output** — all 196 candidate-S_2 values have Im=0 to dps=300 by construction. T35's `S_1 = 2*pi*i*C` factor of `i` arises from the Borel-Laplace discontinuity around the cut. For a future fire that wants the genuine T35-convention S_2 (not just magnitude), one would need to integrate the Padé over a Stokes contour rather than read off pole residues.

5. **Open question for T1 Synth W21 cadence:** Given M8b axis closure-by-residual-acceptance is now numerically substantiated through three independent methodological lenses (017c LSQ, 017e extended LSQ, 017m subtracted-high-order Borel-Padé, 092 raw-low-order Borel-Padé — four lenses), is it appropriate to RETIRE M8b from the active-investigation portfolio and absorb the residual acceptance into the picture-v19 milestone schema? Or does the U2 forward-pointer (subtracted+low-order quadrant) warrant one more fire before retirement? **No agent-side decision recommended; LANE-1 W21 jurisdiction.**

## What would have been asked (if bidirectional)

- Confirmation that "M8b axis" is a single-rep concept vs an aggregate-over-reps concept (J4 documents the resolution but a synthesizer-side ratification would close it cleanly).
- Confirmation that the 017L → T37E identification (J1/D1) is correct, or whether there is a separate 017L prompt I should have located.
- Whether the U2 uncharted-quadrant fire (subtracted+low-order Padé) is worth scheduling, or whether four independent methodological negative results are sufficient to close M8b axis at PERMANENT_RESIDUAL.

## Recommended next step

If M8b axis is to be retired: dispatch a follow-up note absorbing the four-lens negative-result substrate into the picture-v19 milestone schema (similar in spirit to relay 067 BT-baseline-note follow-up). If M8b axis is held open: schedule a single fire of the subtracted+low-order Padé methodology (per U2) to close the orthogonal-quadrant gap. Either path is operator-side W21 dispatch.

## Files committed

- `borel_pade_s2_runner.py` — main computation runner (SHA-256 prefix `73819bd33cc26038`, 19616 B)
- `borel_pade_results.json` — full sweep results with per-cell pole locations, residues, S_2 candidates, convergence diagnostics (SHA-256 prefix `053a728ca9e41733`, 168813 B)
- `build_stability_table.py` — diagnostic-table generator (SHA-256 prefix `7d58f7a33d8ca7a2`, 7619 B)
- `stability_table.md` — Padé stability tables + divergence-pattern analysis per rep + aggregate interpretation (SHA-256 prefix `cb29db7d7ff1ca17`, 15253 B)
- `verdict.md` — verdict statement + method summary + classification rationale + comparison to 017L baseline + future-fire forward-pointer
- `claims.jsonl` — 15 AEAL entries (spec floor 5, suggested 7; 15 actual)
- `halt_log.json` — 0 halts triggered; 5 spec halts checked-and-passed with full rationale
- `discrepancy_log.json` — 5 non-blocking discrepancies (D1–D5) documented
- `unexpected_finds.json` — 4 unexpected finds (U1–U4) documented
- `run.log` — execution log from `borel_pade_s2_runner.py`
- `handoff.md` — this file

## AEAL claim count

15 entries written to `claims.jsonl` this session (spec minimum 5; suggested 7).
