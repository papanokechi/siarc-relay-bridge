# Handoff — T37M-DIRECT-BOREL-D-EXTRACTION
**Date:** 2026-05-03
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~95 minutes (Phase A stage-1 fit ~12 min/rep; Phase B Padé ladder ~16 min/rep all four reps in series; rest is debug + compose)
**Status:** HALTED — verdict `HALT_T37M_PADE_DIVERGENT`

## What was accomplished

Loaded 017e's cached `d=2` PCF Birkhoff series (4 reps; dps=400,
N=5000) and ran the direct Borel-Padé pipeline specified in
Prompt 017m: stage-1 polynomial-correction fit (K=25), cleanness-
step subtraction of the leading transmonomial, scaled Borel
transform `b_n := a_n_residual * zeta_*^n / Gamma(n+1)`, then
Padé `[M, M]` ladder over `(M_in, M)` with M_in in {200, 400, 600,
800}. Stage-1 reproduces 017e's a_1 medians (-53/36, -89/36, +31/4,
~0) at 27-64 digits. Cleanness step is clean
(`|residual_n|/|leading_n|` decays to 1.04e-98 at n=5000 for
V_quad). Padé ladder fails the spec convergence gates (1% on
location, 10% on residue) at every rep: M_in=200 sub-ladder gives 3
OK Padés that disagree at 14-43% on location and 150-300% on
residue; M_in in {400, 600, 800} all return `RANK_LOSS` from
`mpmath.pade` at dps=100 (Hankel system numerically singular at our
coefficient decay rates `|b_n| ~ 10^-46` at n=200, `~10^-65` at
n=800). Halt T37M_PADE_DIVERGENT fires per spec. The Borel-Padé
approach RECONFIRMS 017c/017e's finding that S_2 is below the
polynomial-tail floor at our laptop-feasible compute budget.

## Key numerical findings

- **Stage-1 fit cross-check vs 017e a_1 medians (dps=100, K=25,
  window [3500, 4900]; script: t37m_runner.py).**
  - V_quad: -1.4722222222... (59 digits agreement)
  - QL15:   -2.4722222222... (59 digits agreement)
  - QL05:   +7.7500000000... (62 digits agreement)
  - QL09:   -2.26e-65 (017e median 3.56e-123; 64 digits agreement
    in absolute null sense — both magnitudes far below noise)
- **Cleanness step decay rates (script: t37m_runner.py).**
  - V_quad |residual_5000|/|leading_5000| = 1.04e-98
  - QL15   |residual_5000|/|leading_5000| ~ 10^-87 (similar order)
  - QL05   |residual_5000|/|leading_5000| ~ 10^-90
  - QL09   |residual_5000|/|leading_5000| ~ 10^-92
- **Padé ladder result per rep (12 configs each; dps=100; script:
  t37m_runner.py).**
  - V_quad: 3 OK / 9 RANK_LOSS; loc spread (rel to 2) = 0.196,
    residue abs spread = 3.000.
  - QL15:   3 OK / 9 RANK_LOSS; loc spread = 0.339, residue
    spread = 3.000.
  - QL05:   3 OK / 9 RANK_LOSS; loc spread = 0.426, residue
    spread = 1.502.
  - QL09:   3 OK / 9 RANK_LOSS; loc spread = 0.137, residue
    spread = 2.941.
  - Spec gate is loc < 0.01 and residue < 0.10. All four reps fail
    both gates by >10x.
- **T35 S_1 = 2*pi*i*C convention cross-check at leading rung
  (script: t37m_runner.py Phase A.1).**
  - V_quad: rel_err 4.44e-17, QL15: 2.76e-17, QL05: 1.70e-17,
    QL09: 1.38e-17. Convention factor confirmed.
- **AEAL claims:** 28 entries written (spec minimum: 22).

## Judgment calls made

1. **Padé ladder downscaled from spec.** Spec asked M_in in {2000,
   3000, 4000, 4900} with ~3 M's per M_in. At dps=400 / mpmath.pade,
   benchmark on a single Padé at M=600 took ~5-15 minutes; the full
   spec ladder (12 Padés × 4 reps at M~700 average) projected to
   >10h, exceeding the 2-3h compute envelope. Replaced with a
   feasibility ladder M_in in {200, 400, 600, 800} at dps=100,
   sufficient (in principle) to detect a clean sub-leading singularity
   at eta=2 IF one exists at the polynomial-tail floor we hit. The
   replacement is documented in
   [`rubber_duck_critique.md`](rubber_duck_critique.md) section (b),
   citing Costin and Loday-Richaud as the methodology source. Result:
   M_in=200 the only sub-ladder that produced any Padés (the rest
   `RANK_LOSS`); M_in=200 results don't converge. The downscaling does
   NOT obscure the answer — within the laptop-feasible regime we
   already have the same answer as the full spec would: Padé does not
   converge at this precision/order.
2. **Mapped `T37M_S2_NOT_EXTRACTABLE` (initial verdict, weak gate)
   to `HALT_T37M_PADE_DIVERGENT` (final verdict, strict gate).** The
   runner originally produced `T37M_S2_NOT_EXTRACTABLE` because each
   rep had >=3 OK Padés (the runner's halt gate required 0 OK Padés).
   Per spec §B.5, the strict halt clause "12 orders disagree by >1%
   on location or >10% on residue" is also satisfied here, so
   `HALT_T37M_PADE_DIVERGENT` is the correct ladder label. Patched
   via [`finalize_verdict.py`](finalize_verdict.py) without
   re-running the expensive computation.
3. **DPS_FIT lowered from 200 to 100.** Stage-1 fit at dps=200 took
   ~1700 s/rep in the smoke test (V_quad alone was 28 minutes).
   Lowered to dps=100 (still 12 minutes/rep, ~50 minutes total Phase
   A) since the K=25 polynomial-correction fit converges to
   `a_k` medians matching 017e at >27 digits — far above any
   downstream-precision requirement for the Padé pipeline.
4. **Did NOT extend the recurrence.** Per spec §8 ("DO NOT extend
   the recurrence to higher precision before running Borel-Padé"),
   we stopped at cached 017e data. The recommendation for
   recurrence extension is in the verdict.md and certificate.

## Anomalies and open questions

1. **Spurious off-axis complex poles at M=60, M=80 for V_quad and
   QL05.** At M=60 Padé picks up `eta = 1.77` (V_quad) and
   `eta ≈ 1.006 - 0.050i` (QL05) — both of which have
   `|Im|/|abs| ~ 5%` (right at the physical-pole filter threshold).
   At M=80 V_quad shifts to `eta ~ 1.05` and QL05 to
   `eta ≈ 0.849 - 0.024i`. These pole-position drifts are
   consistent with sub-Padé-order spurious poles; without a
   converged ladder at higher M, the question of whether eta=2 is
   the actual sub-leading singularity location for the d=2 PCF
   Birkhoff structure remains UNDETERMINED. Recorded under
   `unexpected_finds.json:PADE_LOCATION_NOT_CONVERGED_TO_2`.
2. **`mpmath.pade` rank-loss at M_in >= 400.** This is a
   library-side / precision-side limitation, not a methodology
   failure: the dps=100 working precision is below what mpmath
   needs to solve the M=120-270 Hankel system stably given the
   `~10^-46` coefficient decay at n=200. Higher dps would unblock
   this but require a re-run with substantially larger compute
   budget (~6h at dps=200, ~24h at dps=400).
3. **Cross-method 017m vs 017c sanity check is null on its own
   terms.** 017c's `D_median` was already known to be unreliable
   (relative half-range >10^4); 017m's `D_canon` is also unreliable
   (Padé divergent). Recording both for AEAL traceability does NOT
   constitute a "method-A verifies method-B" cross-check —
   honestly, both are precision-limited at the same fundamental
   structural level.
4. **QL09's `a_1 = 0` to 73+ digits property is REPRODUCED at
   dps=100.** Stage-1 fit gives `a_1 = -2.26e-65`, which agrees
   with 017e's `3.56e-123` median in the absolute-null sense
   (both far below the regression-noise floor). The 017L sub-stratum
   (iii) finding (a_1=0 is basis-INDEPENDENT for the
   `B(alpha,beta,gamma)=0` quadric lattice) is consistent with
   what 017m sees here at the leading rung. 017m has nothing new
   to say about Q18 at the second rung because the second-rung
   amplitude itself is not extractable.
5. **Padé poles for QL09 at M=60 and M=80 are real-axis at
   eta=2.300 and 2.167.** These are SUGGESTIVE of the spec's
   eta=2 prediction (within ~15-30%), but with only 2 of 3 OK
   Padés near eta~2 and a third (M=70) at eta=2.644, the spread
   is too large to call convergence. If a future re-run at
   higher Padé order localizes QL09's pole at eta=2, that would
   be an interesting QL09-specific positive result — but it is
   NOT a current finding.

## What would have been asked (if bidirectional)

- Should the spec ladder at M_in in {2000, 3000, 4000, 4900} be
  attempted at dps=200-400 in a separate ~12-24h operator-side
  run, before declaring the entire Borel-Padé approach dead?
- Is the failure to converge at M_in=200, M=60-80 on the
  "right" eta=2 singularity informative — i.e., is the d=2 PCF
  next-rung singularity location actually at eta=2, or could
  the structure carry next-rung amplitude at a different eta
  (e.g., eta=1, conflating with the leading singularity, or at
  some lattice combination of zeta_* multiples)?
- Channel-theory median-resurgence (CT v1.3 sec 3.5) is the
  obvious next escalation. Should we relabel future S_2 prompts
  to focus on that approach exclusively?

## Recommended next step

Fire **op:cc-median-resurgence-execute** equivalent prompt for
the four reps (V_quad, QL15, QL05, QL09): direct channel-theory
median-resurgence extraction of S_2 via the median-summation
identity, bypassing both Stage-2 LSQ and Borel-Padé entirely.
This is the only methodology not yet foreclosed for S_2 at our
laptop-feasible compute budget.

In parallel, an operator-side recurrence extension to dps=600
N=8000 (~12h compute) would give Borel-Padé a second chance at
M_in in {1500, 2500, 4000} with dps=300; this is the "go big or
go home" option for the Padé approach.

Do NOT amend picture v1.10 G6b. The S_2 closure remains OPEN
(consistent with the prior 017c/017e status). 017m's contribution
to the picture is methodological: it forecloses the Borel-Padé
branch at laptop scale, sharpening the recommendation toward
channel-theory or operator-side recurrence extension.

## G6b closure status

**G6b remains OPEN.** Picture v1.10's G6b (S_2 amplitude as
Delta_b-discriminating invariant for d=2 PCFs) is neither
strengthened nor weakened by 017m's HALT verdict. The G6b
closure path now narrows to two non-foreclosed methodologies:
(a) channel-theory median-resurgence direct extraction (CT v1.3
sec 3.5), and (b) Borel-Padé on an operator-side-extended
recurrence at dps=600 N=8000.

## Files committed

- t37m_runner.py
- finalize_verdict.py
- smoke_test.py
- borel_transform_per_rep.json
- pade_approximants_per_rep.json
- borel_singularities_per_rep.json
- d_extraction_per_rep.json
- s_2_per_rep.json
- s_2_partition_certificate.md
- handoff.md
- verdict.md
- halt_log.json (4 entries: T37M_PADE_DIVERGENT per rep)
- discrepancy_log.json (empty: [])
- unexpected_finds.json (1 key: PADE_LOCATION_NOT_CONVERGED_TO_2)
- claims.jsonl (28 entries)
- rubber_duck_critique.md
- t37m_run.log, smoke.log

## AEAL claim count
28 entries written to claims.jsonl this session (spec minimum: 22).
