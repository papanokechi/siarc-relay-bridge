# Handoff — T2-EXECUTOR-XI0-D3-CLOSURE-REPRODUCIBILITY-VERIFY
**Date:** 2026-05-13
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE — closure REPRODUCED bit-identically across 11 days

---

## What was accomplished

DECISION 3 option (a) from the 2026-05-13 morning triage envelope was
"M-A close ξ₀ d=3 directly [LOW energy ~1–2 hr]". Investigation
discovered the work was **already executed and AEAL-recorded on
2026-05-02** at bridge commit `e93458fb56e6c4dbe5e4ec2127d4a2c81cb35e9b`
("XI0-D3-DIRECT — close G2 at d=3 across 3 Galois bins; verdict
G2_CLOSED_AT_D3 at 80 algebraic digits"). The stale "open" status had
propagated through D2-NOTE v2.1 (drafted 2026-05-03, §6 (a)) and the
2026-05-12 strategic-landscape review without anyone cross-checking the
2026-05-02 bridge artefact.

Rather than retire the todo as a paper-only bookkeeping move, the agent
**re-ran `xi0_d3_runner.py` in this fresh session folder** to refresh the
AEAL trail and produce independent reproducibility evidence.

**Result:** all 9 output files (5 AEAL claims, 3 per-bin CSVs, 4 JSON
result/log files, 2 markdown summaries) are **bit-identical** with the
2026-05-02 run. SHA-256 of every output matches across the 11-day gap,
including the single bundle hash `ad76e44f…a188478`.

This is the strongest possible reproducibility certification short of
re-running on a third platform: same script, fresh Python process, same
mpmath 1.3.0 / sympy 1.14.0 stack, bit-identical IEEE-754 / mpmath
deterministic outputs.

## Key numerical findings

All reproduced from 2026-05-02 (no new science; bookkeeping closure):

- **Galois bin +_C3_real** (family 19, b(n) = n³ − 3n² + 1):
  algebraic 80.0 digits agreement; numerical N=1500 → 3.18 asymptotic
  digits; verdict AGREES.
- **Galois bin +_S3_real** (family 14, b(n) = n³ − 3n² − n + 1):
  algebraic 80.0 digits agreement; numerical N=1500 → 3.18 asymptotic
  digits; verdict AGREES.
- **Galois bin −_S3_CM** (family 50, b(n) = n³ − 2n² − 1):
  algebraic 80.0 digits agreement; numerical N=1500 → 3.35 asymptotic
  digits; verdict AGREES.
- **Aggregate verdict: G2_CLOSED_AT_D3** (3/3 bins AGREE).
- Coverage certificate: K = 3 Galois bins, one representative per bin
  selected by minimum-|α₂|+|α₁|+|α₀| (tie-break by family_id).

All claims at dps=80, output_hash `ad76e44fbbfc8e5b285bd916ed50e4844d37b789ac5ccdd73b9664815a188478`.

## Judgment calls made

1. **Reproducibility re-run vs paper-only retirement.** The path-of-least-
   resistance close would have been to flip the SQL todo to `done` citing
   e93458f without any new compute. The agent chose to invest ~5 minutes
   of compute on a re-run because (i) AEAL discipline calls for
   refreshing claims when revisiting prior work, (ii) the bit-identical
   match is a much stronger reproducibility statement than a pure
   bookkeeping retire, and (iii) the script self-validates against the
   cubic_family_catalogue and would have HALTED if the catalogue had
   drifted (it did not).

2. **Did not modify D2-NOTE v2.1 source.** Per `d2note_consistency.md`
   from the 2026-05-02 run, the closure does not require modifying
   D2-NOTE v2.1 source (which is in tex/submitted/ and RULE-1-blocked
   from re-release until M-axis full closure). The §6 (a) "what remains
   open" item should be retired in the eventual D2-NOTE v2.2 / v3 with a
   citation to the e93458f / this-fire pair. Flagged as a documentation
   sync opportunity, not executed.

3. **PowerShell hung at end of script execution (cosmetic).** The
   Python process completed in ~90 seconds (timestamps 8:10:54 →
   8:12:34) but the PowerShell session did not return control until
   stopped manually. Outputs were on disk and bit-identical with prior.
   Not a halt condition.

## Anomalies and open questions

1. **Strategic-landscape stale-status oversight (substantive but not
   load-bearing).** The 2026-05-12 night four-stream review treated
   op:xi0-d3-direct as "still open" without checking the 2026-05-02
   bridge artefact. The agent recommends adding a "supersession-gate
   pre-fire check" to all future Tier-1-substantive recommendations
   (analogous to the existing `prompt drafting discipline` stored
   memory). This is the third or fourth instance of this pattern in
   the corpus (058R Q2/Q4 supersession; 064 deg_a=0 row; W20 068
   absorption; now this).

2. **D2-NOTE v2.1 §6 (a) phrasing is now factually stale.** Verbatim
   text in d2_note_v2_1.tex L793-796:
   > "Direct numerical d = 3 Newton-polygon test on at least one cubic
   > representative per Galois bin, at dps = 80. Predicted runtime: 1–2
   > hours per bin."

   The work was already done before v2.1 was even drafted (2026-05-02
   → 2026-05-03). When D2-NOTE v2.2 fires (RULE-1-permitting), §6 (a)
   should be rewritten as "Direct numerical d = 3 Newton-polygon test:
   CLOSED at e93458f / 2026-05-02; 3/3 Galois bins AGREE at 80
   algebraic digits and ~3 numerical asymptotic digits at N=1500."

3. **Numerical agreement is only ~3 digits at N=1500.** The script
   notes this is asymptotic-extrapolation-bounded (O(1/N) subleading
   term in the ratio Q_N / Q_{N-1} / N^3 → α_3). The 80-digit algebraic
   agreement is the load-bearing closure; the numerical ladder is a
   sanity check that bounds the subleading-term magnitude. This is the
   same pattern as d=2 (proven analytically) and d=4 (empirical at
   ~80 digits via different ladder). Not a halt; bookkeeping note.

## What would have been asked (if bidirectional)

Q1: Operator, do you want a D2-NOTE v2.2 sync fire scheduled (RULE-1-
post-lift) that retires the §6 (a) "open" status? Or absorb that into
a larger v2.2 / v3 fire whenever M-axis V0 closure is complete?

Q2: With M-A ξ₀ d=3 now bookkeeping-closed, would you prefer to spend
the remaining morning energy on (b) S6 rejection-pattern retrospective
[~2-3 hr] or (c) triple-win M-C op:cc-median-resurgence-execute [~4-8
hr, mostly background compute]? Or shelve and pivot to verdict 208
Day-1 actions per DECISION 2?

## Recommended next step

**Operator-facing next step:** With M-A ξ₀ d=3 closed (via bookkeeping
+ reproducibility verification), recommend either:

- **HIGH-LEVERAGE pivot to Tier-1 (c):** triple-win M-C
  op:cc-median-resurgence-execute is the highest-leverage single
  execution in the landscape per the 2026-05-12 strategic review.
  Binary outcome (confirm OR falsify H4 ~40-digit pre-registered
  prediction). 4-8 hr mostly background compute. RULE-1-permits the
  EXECUTION (only release of the companion note is blocked).

- **MEDIUM-LEVERAGE pivot to Tier-1 (b):** S6 rejection-pattern
  retrospective per 2026-05-12 sharper-review highest-value diagnostic
  flag. 2-3 hr private foundational planning; no compute load.

- **LOW-DRAG pivot to DECISION 2:** If operator wants quick wins,
  ratify verdict 208 Day-1 scope (Carneiro endorsement send awaiting
  arXiv code; T2B math.NT framing decision; PCF-2 v1.3 / PCF-1 v1.3
  arXiv staging).

**Agent-facing next step:** None without operator decision. SQL todo
`gods-eye-view-M-A-xi0-d3-direct` should be flipped to `done` with
citation to e93458f + this fire.

## Files committed

- `xi0_d3_runner.py` (copied from 2026-05-02; unchanged source)
- `bin_representatives.json` (bit-identical with 2026-05-02)
- `newton_d3_results.json` (bit-identical with 2026-05-02)
- `borel_d3_results.json` (bit-identical with 2026-05-02)
- `xi0_d3_+_C3_real.csv` (bit-identical with 2026-05-02)
- `xi0_d3_+_S3_real.csv` (bit-identical with 2026-05-02)
- `xi0_d3_-_S3_CM.csv` (bit-identical with 2026-05-02)
- `xi0_d3_aggregate.md` (bit-identical with 2026-05-02)
- `d2note_consistency.md` (bit-identical with 2026-05-02)
- `claims.jsonl` (bit-identical with 2026-05-02; 5 AEAL claims)
- `halt_log.json` (empty)
- `discrepancy_log.json` (empty)
- `unexpected_finds.json` (empty)
- `handoff.md` (this file)
- `reproducibility_certificate.md` (next; the 11-day-gap hash-match
  evidence table)

## AEAL claim count

5 AEAL entries re-emitted in this fire (all bit-identical with
2026-05-02). No new claims; closure is reproducibility-certification
of prior closure.
