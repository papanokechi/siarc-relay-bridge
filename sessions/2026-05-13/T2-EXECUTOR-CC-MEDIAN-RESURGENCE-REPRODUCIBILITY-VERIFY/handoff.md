# Handoff — T2-EXECUTOR-CC-MEDIAN-RESURGENCE-REPRODUCIBILITY-VERIFY
**Date:** 2026-05-13
**Agent:** GitHub Copilot (VS Code) — claude-opus-4.7-xhigh
**Session duration:** ~25 minutes (~09:01–09:25 JST including reads + rerun + writes)
**Status:** COMPLETE

## What was accomplished

D3(c) "Triple-win M-C op:cc-median-resurgence-execute" from the 2026-05-12 strategic-landscape morning triage hit the supersession-gate exactly like D3(a) did this morning: the bridge already contained `sessions/2026-05-02/CC-MEDIAN-RESURGENCE-EXECUTE/` with verdict `H4_EXECUTED_PASS_108_DIGITS` (commit `ed61428a13795ad1cf3f922959b36c213d7727fb`). All requested parameters (ζ*=4/√3, 5000 coefficients, dps=250) match the operative substrate. To close the stale-status bookkeeping with a fresh AEAL trail, `median_resurgence.py` was re-run in this session folder under Python 3.12.10 + mpmath 1.3.0. **7 of 8 output files reproduced with bit-identical SHA-256; the 8th (`phaseA_series.log`) differs only in `elapsed=Xs` decoration strings and matches in every numerical column.** The 1.3 MB `Qn_5000_dps250.csv` hashes bit-for-bit to `0b9e656f08b5b1dae67ebaffa5456e3625594b8e4c1904b4d0b2487ab30687cd` — the H4-A8 determinism claim is verified across the 11-day gap. This is the n=2 same-day instance of the supersession-gate pattern.

## Key numerical findings (all reproduced bit-identically from 2026-05-02)

- **Branch exponent β = 0** (logarithmic case — refinement, not contradiction, of the H4 "half-integer expected" pre-registration; β_M1, β_M2, β_M3 all ≤ 1.5e-107) — `claims.jsonl` H4-A2.
- **Stokes coefficient C = 8.1273367954950723671125787320235831822645427223388…** — `claims.jsonl` H4-A3.
- **S_{ζ*} = 0.0 + 51.0655631399546622698316746099456615679204103033…·i** (purely imaginary, V_quad NATIVE normalization) — `claims.jsonl` H4-A6.
- **Phase C ↔ Phase D cross-check digit agreement: 108.39 digits** (vs Theory-Fleet H4 pre-registered HIGH-confidence forecast 30–50, central 40 — **2.71× exceeds forecast**) — `claims.jsonl` H4-A7.
- **Verdict: `H4_EXECUTED_PASS_108_DIGITS`** — `verdict.md`.

## Audit-class assertions (this fire, for AEAL trail)

1. `median_resurgence.py` rerun at dps=250, N_MAX=5000 on 2026-05-13 produced `Qn_5000_dps250.csv` with SHA-256 `0b9e656f08b5b1dae67ebaffa5456e3625594b8e4c1904b4d0b2487ab30687cd` bit-identical to the 2026-05-02 reference (commit `ed61428`).
2. Stokes constants C and S_{ζ*} reproduced bit-identically; logarithmic β=0 case confirmed.
3. 7 of 8 output files reproduced with identical SHA-256; the 8th differs only in elapsed-time decoration and matches in every numerical column (see `discrepancy_log.json` D-MC-REPRO-1).
4. Determinism claim H4-A8 from the 2026-05-02 fire is verified across an 11-day gap on the same host with a fresh Python interpreter session.

(These audit assertions are not added to `claims.jsonl` because that file is the script-generated H4-A1..H4-A8 set reproduced verbatim from the original fire — D3(a) precedent.)

## Judgment calls made

- **Reproducibility-certification approach over paper-retirement.** Same pattern as this morning's D3(a) closure: rather than mark the SQL todo "done" by citation alone, re-run the script in a new bridge session folder and produce a `reproducibility_certificate.md` with explicit hash-match table. This creates fresh AEAL anchors for the G-A calibration-paper data point and forces a real test of the H4-A8 determinism claim.
- **Phase D residual NOT re-investigated.** The 2026-05-02 fire substituted a polynomial LSQ in 1/n at order 40 for the original local-Borel-germ cross-check (because the original collapsed to Phase C). The reproduction inherits this substitution. Operator decision on whether to revisit Phase D as a separate fire is deferred.
- **V_quad → P-III(D6) normalization map remains OPEN.** The 51.0655631399…i Stokes constant is in V_quad NATIVE normalization, not in P-III(D6)'s natural coordinates. The CC-VQUAD-PIII-NORMALIZATION-MAP follow-up (cf. 058R, 069 PERSIST chain) is out of scope for this fire. This residual is unchanged by today's verification.
- **PSLQ closed-form recognition of C = 8.1273367954…** deferred (CC-MEDIAN-RESURGENCE-PSLQ candidate). Not this fire's scope.
- **`claims_audit.jsonl` NOT created as a separate file.** The 4 audit-class assertions for this fire are captured in handoff.md "Audit-class assertions" section above + the `unexpected_finds.json` / `discrepancy_log.json` JSON anchors, mirroring D3(a)'s structure exactly.

## Anomalies and open questions

- **n=2 same-day supersession-gate evidence.** Both Tier-1 picks from the 2026-05-12 strategic-landscape recommendations (D3(a) M-A xi_0 d=3, D3(c) M-C median-resurgence) had been executed 2026-05-02 and carried "open" status into today's SQL todo list. The memory `Strategic-landscape / Tier-1 recommendation drafters must include 'prior-fire bridge search' step` (stored this morning after D3(a)) is now reinforced at n=2. Recommend a fresh memory or upvote noting today's double instance — this is no longer a single anomaly but an emerging pattern that the strategic-landscape review process should formally guard against in its drafting checklist. See `unexpected_finds.json` UF-MC-REPRO-1.

- **G-A AEAL calibration seed: H4 prediction-vs-execution datapoint preserved.** The triple-win envisioned the H4 forecast (30–50 central 40) vs actual outcome (108.39 digits, ratio 2.71×) as the seed data point for the G-A AEAL calibration paper. Today's verification preserves that pair with current hash anchors and a fresh bridge-commit citation. When G-A drafting begins (post-RULE-1-lift), this is datapoint #1: forecast band [30, 50], central 40, executed 108.39, ratio 2.71×, β prediction "half-integer expected" → actual β=0 (refinement, not contradiction). See `unexpected_finds.json` UF-MC-REPRO-3.

- **β=0 logarithmic refinement vs H4 "half-integer expected".** As documented in the 2026-05-02 handoff, this is a refinement: H4 did not pre-register a specific β value, only an expected family. The HALT_H4_PREDICTION_FALSIFIED condition did not trigger. This information remains a useful data point for G-A but is not a discrepancy.

- **`phaseA_series.log` SHA-256 differs by elapsed-time strings only.** Logged in `discrepancy_log.json` D-MC-REPRO-1 with full diff. Not a determinism violation — the determinism claim H4-A8 specifically named `Qn_5000_dps250.csv`, which matches bit-for-bit.

## What would have been asked (if bidirectional)

- Should the n=2 supersession-gate pattern memory be promoted from "prescient single instance" to "documented dominant failure mode of strategic-landscape recommendations"? Recommend yes.
- Is closed-form recognition of C = 8.1273367954…(via PSLQ against {π, log 2, log 3, log √5, ζ(3), …}) wanted as the next fire on the M-C arc, or should the V_quad → P-III(D6) normalization-map follow-up take priority?
- Should the G-A AEAL calibration paper draft scaffold be queued for post-RULE-1-lift, or is it premature to begin scaffolding?

## Recommended next step

Update strategic-landscape / Tier-1 picklist generation (or its drafter checklist) to mandate a `git log --grep=<op-name>` bridge pre-search before recommending any Tier-1 op as "open". Then proceed to **D4 (Journey-pivot Prompt 209 go/no-go)** and **D5 (Corpus-review a/b/c selection)** to clear the remaining morning-triage queue. The M-C arc's substantive open work (CC-VQUAD-PIII-NORMALIZATION-MAP and/or CC-MEDIAN-RESURGENCE-PSLQ) should be treated as fresh fires drafted from the 2026-05-02 handoff's "recommended next steps" section rather than re-entries of the executed `op:cc-median-resurgence-execute` op.

## Files committed

- `median_resurgence.py` (copied from 2026-05-02 source; 31284 bytes; mtime preserved)
- `Qn_5000_dps250.csv` (1318306 bytes; SHA-256 `0b9e656f…b30687cd` — MATCHES 2026-05-02)
- `claims.jsonl` (2641 bytes; H4-A1..H4-A8 script-output — MATCHES 2026-05-02)
- `verdict.md` (511 bytes; MATCHES 2026-05-02)
- `S_zeta_star_digits.txt` (1239 bytes; MATCHES 2026-05-02)
- `fit_branch_exponent.log` (3644 bytes; MATCHES 2026-05-02)
- `local_germ_crosscheck.log` (1312 bytes; MATCHES 2026-05-02)
- `stokes_extraction.log` (1253 bytes; MATCHES 2026-05-02)
- `phaseA_series.log` (cosmetic-only diff vs 2026-05-02; numerical content identical)
- `reproducibility_certificate.md` (full hash table)
- `unexpected_finds.json` (UF-MC-REPRO-1/2/3)
- `discrepancy_log.json` (D-MC-REPRO-1 — phaseA_series.log cosmetic diff)
- `halt_log.json` (`{}`)
- `handoff.md` (this file)

## AEAL claim count

8 entries in `claims.jsonl` (H4-A1..H4-A8 reproduced bit-identically from 2026-05-02 commit `ed61428`); 4 audit-class assertions captured in this handoff's "Audit-class assertions" section + `unexpected_finds.json` / `discrepancy_log.json` JSON anchors.
