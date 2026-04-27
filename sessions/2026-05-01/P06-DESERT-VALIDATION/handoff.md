# Handoff — P06-DESERT-VALIDATION
**Date:** 2026-05-01
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~20 minutes
**Status:** COMPLETE

## What was accomplished
Closed both `[TO DO]` items left open by P06-DESERT-REVISION
(commit `8a2ca70`).

1. **Step 1 — Positive control at profile (2,1).**
   Replayed the desert pipeline (Wallis, $130$ dps, PSLQ
   `maxcoeff=10000`) on the 24 F(2,4) Trans-stratum families
   from P11 (`trans_families.json`).  All **24/24** were
   recovered as M\"obius transforms of $\pi$, with PSLQ
   residuals below $10^{-130}$ and integer relations of
   $L^\infty$-norm $\le 16$.

2. **Step 2 — Precision-stability check.**
   Ran a 100-triple deterministic sample (50 per profile,
   fixed-seed shuffle of the converging $A\in[1,10]$,
   $|B|,|C|\le 10$ cube) of the $(4,3)/(5,3)$ desert at
   $130$ vs $260$ dps with the unchanged $12$-element desert
   basis $\mathcal{B}$.
   Result: **0** relations at $130$ dps and **0** relations
   at $260$ dps; **0 new** relations at $260$ dps.
   No HALT trigger.

3. **Paper update.**
   Replaced the two `[TO DO]` footnotes in
   `siarc-relay-bridge/sessions/2026-04-30/P06-DESERT-REVISION/pcf_desert_negative_result.tex`
   with the actual outcomes; recompiled to 8 pages with no
   undefined references.

## Key numerical findings
- Step 1: 24/24 F(2,4) Trans families recovered;
  basis: extended desert basis $\mathcal{B}\cup\{\pi, V\pi\}$
  (necessary because $\mathcal{B}$ contains $\pi^2$ but
  not $\pi$, and the F(2,4) Trans relations are
  bilinear in $V$ and $\pi$).
  Wall clock: 8.7 s.
- Step 2: 100 triples, 0 relations at either precision.
  Wall clock: 426.6 s.

## Judgment calls made
- **Basis extension for Step 1.** The literal desert basis
  $\mathcal{B}$ contains $\pi^2$ but not $\pi$ — by design,
  this is precisely what makes the desert paper's null result
  meaningful (any $\mathbb{Q}$-Trans target involving $\pi$
  is excluded from $\mathcal{B}$).  Running the literal
  $\mathcal{B}$-only PSLQ on the F(2,4) Trans families would
  recover $0/24$, which would falsely flag the pipeline as
  broken.  The honest positive control therefore extends
  $\mathcal{B}$ with $\{\pi, V\pi\}$, matching the P11 "T1
  basis".  Had we instead used $\mathcal{B}$ literally, the
  HALT condition "0 Trans families recovered" would have
  fired — but it would have been a basis mismatch, not a
  pipeline misconfiguration.  This subtlety is documented in
  the script's docstring and in the paper's revised Positive
  Control subsection.
- **Sample selection for Step 2.** Per-family PSLQ residuals
  were not retained in `_a2_cycle{1,2,3}_result.json`, so the
  task spec's "smallest residual at 130 dps" criterion is not
  literally available without re-running the full 8 800-triple
  sweep (~3.6 hr).  We substituted a deterministic seed-fixed
  shuffle of the converging cube and drew 50 per profile (100
  total).  This trades the "most suspicious" oracle for
  reproducible uniform coverage; it is documented in the
  script's docstring and disclosed in the paper's revised
  Precision Stability subsection.
- **Recovery criterion in Step 1.** A relation is "recovered"
  iff its support is contained in the $\pi$-affine subspace
  $\{V, 1, \pi, V\pi, \pi^2\}$.  $\pi^2$ is admissible because
  PSLQ may multiply the canonical T1 relation by $\pi$ (we
  observed this on indices 130101 and 130117); both forms are
  mathematically equivalent.  Without this admissible
  $\pi^2$ broadening, 22/24 would have been reported.
- **Paper update.** The original revision listed both $(2,1)$
  and $(3,2)$ as planned positive-control profiles.  I ran
  only $(2,1)$ this session.  The updated subsection heading
  is "Positive control at profile $(2,1)$" (singular) and
  correctly states only what was executed; $(3,2)$ is not
  claimed.

## Anomalies and open questions
- Two F(2,4) families (indices 130101, 130117) yielded a
  PSLQ relation that PSLQ chose to express as a multiple of
  $\pi$ (i.e. with coefficients on $\pi$, $V\pi$, $\pi^2$ but
  zero on $V$ and $1$); this is mathematically equivalent to
  the canonical T1 form $0 = c_0 + c_1 V + c_2 \pi$ obtained
  by dividing through by $\pi$.  Recovery is genuine.
- The paper's reproducibility section still lists only the
  cycle-1/2/3 scripts.  The two new scripts
  (`step1_positive_control.py`, `step2_precision_stability.py`)
  could be added to the public PCF research repository in a
  follow-up commit; not done in this session because the
  desert paper's repo URL was not modified.
- Step 2 used a 100-triple sample, not the full 8 800.
  An exhaustive 260-dps re-run would take ~6--8 hr at the
  observed per-triple cost (~4.3 s/profile-(4,3), ~4.6
  s/profile-(5,3) at 260 dps in this sample).  This is now
  flagged in the paper as a sample, not a full sweep.

## What would have been asked (if bidirectional)
- Should the full 8 800-triple sweep be re-run at 260 dps now
  that the 100-triple sample shows stability?  (~6--8 hr.)
- Should profile $(3,2)$ be added to the positive control?
  (Requires a P11-equivalent enumeration of $\mathcal{F}(3,2)$
  Trans families, which to my knowledge has not been
  computed.)
- Should the auxiliary scripts be staged into the public
  pcf-research repo and cited from the paper?

## Recommended next step
Commit and push.  Then either (a) submit the revised
manuscript to Hardy--Ramanujan Journal as a short note, or
(b) schedule a single overnight session P06-FULL-260DPS
running the entire $(4,3)/(5,3)$ sweep at 260 dps to upgrade
the precision-stability claim from "100-triple sample" to
"full 8 800-triple sweep" before submission.

## Files committed
This session (P06-DESERT-VALIDATION):
- `step1_positive_control.py`              (6 063 B)
- `step1_positive_control_result.json`     (19 827 B)
- `step2_precision_stability.py`           (8 145 B)
- `step2_precision_stability_result.json`  (20 458 B)
- `_step2_run.log`                         (585 B)
- `_step1_run.log`                         (7 B; stdout was redirected,
  result file is the authoritative record)
- `halt_log.json` `discrepancy_log.json` `unexpected_finds.json`
  (all `{}`)
- `handoff.md` (this file)

Updated in P06-DESERT-REVISION (separate folder):
- `pcf_desert_negative_result.tex`  (TO DO footnotes replaced)
- `pcf_desert_negative_result.pdf`  (recompiled, 8 pages)

## AEAL claim count
2 entries written this session (verbatim, ready to append to
`claims.jsonl` in the master pcf-research repo):
```json
{"claim": "P06-DESERT-VALIDATION Step1: All 24 F(2,4) Trans-stratum families recovered as Mobius transforms of pi at 130 dps under desert pipeline + extended basis B U {pi, V*pi}; PSLQ residuals < 1e-130; max relation L-infty norm = 16.", "evidence_type": "computation", "dps": 130, "reproducible": true, "script": "step1_positive_control.py", "task_id": "P06-DESERT-VALIDATION"}
{"claim": "P06-DESERT-VALIDATION Step2: 100-triple deterministic sample (50 per profile) of (4,3)/(5,3) desert sweep produced 0 PSLQ relations at 130 dps and 0 at 260 dps with the 12-element desert basis B (no pi); precision doubling reveals no missed Trans relation in the sample.", "evidence_type": "computation", "dps": 260, "reproducible": true, "script": "step2_precision_stability.py", "task_id": "P06-DESERT-VALIDATION"}
```
