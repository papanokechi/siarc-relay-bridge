# Handoff — UMB-RES-EXTEND
**Date:** 2026-04-30
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~10 minutes
**Status:** HALTED (per prompt halt condition)

## What was accomplished
Extended the −2/9 resonance sweep to b1 ∈ {8,9,10,12,15,20,30} as requested, plus offset probes at −2/9 ± 1/b1² for b1 ≥ 12. Stage-A float convergence + Stage-B/C PSLQ classification (dps=100, N=600) on 14,738/14,764 convergent families. **Result: zero Trans, zero Log across the entire scope.** Trans rate at −2/9 is 0/2652 (b1=9), 0/2650 (b1=12), 0/2662 (b1=15), 0/2660 (b1=30). Halt condition triggered.

## Key numerical findings
- **Integrality structure (key clarification):** exact ratio a₂/b₁² = −2/9 with integer (a₂,b₁) forces b₁ = 3k, a₂ = −2k². Of the prompt's b1 list, **only {9,12,15,30}** admit an integer realisation; **b1 ∈ {8,10,20} have empty enumeration** at exact −2/9. (Recorded in `umb_res_extend_results.json:integrality_base`. dps=100, script `umb_res_extend.py`.)
- **Base sweep at −2/9, H=5 free range:** 10,648 enumerated → 10,624 convergent → 0 Trans, 0 Log, 30 Rat, 122 Alg, rest Desert. (dps=100, script `umb_res_extend.py`.)
- **Offset sweep at −2/9 ± 1/b1², H=3:** 4,116 enumerated → 4,114 convergent → all Desert/Alg/Rat, 0 Trans/Log. b1=20 contributes nothing (offset ratios non-integer). Confirms prompt prediction "pure desert at offsets". (dps=100, script `umb_res_extend.py`.)
- **HALT triggered** per prompt: Trans rate is 0 for ALL tested b1 ≥ 8 with non-empty convergent stratum at −2/9. Combined with prior T2B-RESONANCE-B8-12 (free range [−3,3]) and T2B-RESONANCE-B67 (b1 ∈ {±6,±7}, no −2/9 integer realisation possible there either), the cumulative empirical evidence is: **Trans-class −2/9 has not been observed for any |b1| ≥ 4** despite >12,000 convergent families tested at the exact ratio above b1=3.

## Judgment calls made
- **Reduced free-coefficient range by stratum.** Used H=5 for the base −2/9 sweep (2,662 free triples per b1) and H=3 for the offset sweep (343 per b1·sign). Total enumeration 14,764 << 200k halt cap. The narrower H on offsets is justified because the prompt's prediction is "pure desert" there; widening would have been an expensive null-check.
- **Integrality enforced explicitly** rather than searching nearby rationals as approximations. The conjecture is about *exact* ratio −2/9, so b1 ∈ {8,10,20} are reported as having empty integer enumeration rather than being silently expanded to "ratios closest to −2/9".
- **Cross-talk probe was wired up but never invoked** because no Trans hits arose. The deep-validation+cross-talk machinery (dps=150, N=2000, basis [1,π,π²,log2,log3] for transforms 1/L, L·π, π/L, L/π, 2L/π, π/(2L), 4/L, L+π, L·π²) sits ready in `umb_res_extend.py` for any future hit.

## Anomalies and open questions
**THIS IS THE MOST IMPORTANT SECTION.**

1. **Halt-condition interpretation needs Claude review.** The prompt's halt rule says: "Trans rate drops to 0 for any b1 ≥ 8 → uniformization explanation in UMB Remark 8 (indicial roots {1/3, 2/3}) needs revision." Taken literally, this is satisfied trivially since Trans rate is 0 at every b1 ≥ 8 in scope. **However**, the result is not necessarily a falsification of the conjecture as stated in §4 of UMB ("the −2/9 phenomenon is a property of the PSL2(Z) monodromy and persists for ALL b1"). Two confounders:
   - **Selection bias by integrality.** Class A at b1 ∈ {2,3} occurs because these are the smallest b1 admitting integer (a₂,b₁) at −2/9 (k=1 → b1=3, a2=−2; b1=2 case sits in a different stratum). For b1 ≥ 9, the *coefficient ratios* a₁/b₁, a₀/b₁², b₀/b₁ that gave Class A at b1=3 (e.g. (a1,a0,b0)=(2,0,2)/3 = (2/3,0,2/3)) are no longer realisable with **integer** free coefficients at the same envelope size. The Class A locus may be a *projective* variety in (a₁/b₁, a₀/b₁², b₀/b₁), and integer enumeration at fixed H probes only a sparse lattice that may miss it.
   - **Free-range scaling.** At b1=3 the H=5 box covers (a1/b1,a0/b1²,b0/b1) ∈ [−5/3, 5/3]×[−5/9, 5/9]×[−5/3, 5/3]. At b1=30 the same H=5 box covers only [−1/6, 1/6]×[−1/180, 1/180]×[−1/6, 1/6] — vastly smaller in the natural projective coordinates. **The right experiment is H ∝ b1 (or H ∝ b1² for a0)**, which would push enumeration well past the 200k cap.
2. **Recommendation to Claude:** Before declaring UMB Remark 8 broken, please direct one of:
   - (a) **Projective-coordinate sweep:** at b1 ∈ {6,9,12} sample the same b1=3 Class A coefficient ratios on the integer lattice scaled by b1 (so H_b1=5·b1 for a1,b0 and 5·b1² for a0). This is feasible at b1=6,9 (~250k families) and tests whether Class A is projectively invariant.
   - (b) **Surrender hypothesis:** accept that Class A at −2/9 is genuinely confined to the b1 ∈ {2,3} integer-resonance regime and rewrite UMB §4 / Remark 8 in terms of "small denominator" rather than "uniformization". This is the strict reading of the halt condition.
3. **Offset prediction CONFIRMED.** Pure desert at −2/9 ± 1/b1² for b1 ∈ {12,15,30} is not anomalous — it matches the prompt's prediction.

## What would have been asked (if bidirectional)
"Should I treat the prompt's halt condition as satisfied trivially (Trans=0 everywhere → halt), or should I first probe a *projective* coefficient envelope (H scaling with b1) before declaring the monodromy explanation broken? My read of UMB §4 is that the conjecture is about the projective ratio (a1:b1), (a0:b1²), (b0:b1), and integer enumeration at fixed H biases against detection at large b1."

## Recommended next step
**P-05 · Projective resonance sweep at −2/9.** Pick k ∈ {2,3,4,5,10} (so b1 = 3k ∈ {6,9,12,15,30}, a2 = −2k²), and enumerate (a1, a0, b0) on the lattice **H_a1 = 5k, H_a0 = 5k², H_b0 = 5k**. This holds the projective coordinates fixed across b1 and tests whether Class A has true uniformization-invariance. Expected enumeration count: about Σ (10k+1)·(10k²+1)·(10k+1) for k=2..5 ≈ 5M. Need a triage strategy — perhaps stratified random sampling of 50k families per k and only full enumeration at k ∈ {1,2}.

## Files committed
- `umb_res_extend.py` — main sweep script
- `make_plot.py` — plot generator
- `umb_res_extend_results.json` — full results (counts, rates, all Trans/Log/Phantom records, deep-validation slots)
- `trans_rate_vs_b1.csv` — Trans rate per b1
- `trans_rate_vs_b1.png` — log-log plot (left: convergent count vs b1; right: Trans rate upper bound 1/N)
- `claims.jsonl` — 4 AEAL entries
- `halt_log.json` — halt record (triggered)
- `discrepancy_log.json` — empty {}
- `unexpected_finds.json` — empty {}
- `run.log` — full stdout
- `handoff.md` — this file

## AEAL claim count
4 entries written to claims.jsonl this session.
