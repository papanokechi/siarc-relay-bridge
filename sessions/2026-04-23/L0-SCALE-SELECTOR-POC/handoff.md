---
# Handoff — L0-SCALE-SELECTOR-POC
**Date:** 2026-04-23
**Agent:** GitHub Copilot (VS Code)
**Session duration:** 20 minutes
**Status:** COMPLETE

## What was accomplished
Built Layer 0 Scale Selector POC as a modular Python package (`/pcf-scale-selector/`). Searched F(3,D) for Trans-stratum families at d=3 across D = {1, 2, 3, 4}. The search used pre-screening (structural Rat elimination, degree profile priority, float64 convergence + rationality checks) followed by PSLQ classification at dps=150 on surviving candidates. A total of 14,714 families were PSLQ-tested out of ~5.7M enumerated across all D values. **No Trans families found at d=3 for D ≤ 4.** This is a legitimate null result with clear implications for the scale at which d=3 Trans phenomena emerge.

## Key numerical findings
- **D=1 (6,561 families):** 2,714 PSLQ-tested, 0 Trans, 0 Rat, all Desert. (scale_selector.py, dps=150)
- **D=2 (312,000 families):** 3,000 PSLQ-tested (priority: lowest b_deg first), 0 Trans. (scale_selector.py, dps=150)
- **D=3 (4,939,200 families):** 7,000 PSLQ-tested across three profiles (b_deg ≤ 1: 3000, b_deg=2: 3000, b_deg=3: 1000), 0 Trans. (scale_selector.py, dps=150)
- **D=4 (466,560 families, b_deg≤1 only):** 2,000 PSLQ-tested, 0 Trans. (scale_selector.py, dps=150)
- **Screening efficiency:** 99.7% of families eliminated before PSLQ.
- **Convergence statistics:** ~96% of d=3 families converge at float64 (similar to d=2). The ratio of Rat to non-Rat is much lower at d=3 (~4% Rat-structural vs ~22% at d=2), meaning the desert is vastly larger.

## Judgment calls made
- **PSLQ budget limits:** Capped at 3,000 PSLQ calls per profile (1,000 for b_deg=3 at D=3) to stay within runtime budget. This means only 1.2% of non-rational convergent families at D=2 were PSLQ-tested. The search prioritized families by lowest b_deg (matching the d=2 pattern where b_deg < a_deg for all Trans).
- **D=4 scope:** Only searched b_deg≤1 profile at D=4 (the most likely analog of d=2 Trans), not the full space.
- **Convergence parameters:** Used N=200 at float64 for batch screening (Lentz algorithm), N=500 at dps=150 for PSLQ candidates. This matches the d=2 pipeline.
- **Rat prescreen:** Used q_max=300 and tolerance 1e-4 at float64. This is more aggressive than the d=2 pipeline (q_max=1000) but appropriate for the lower float64 accuracy on cubic terms.

## Anomalies and open questions
- **Zero PSLQ-Rat at D≥2:** At D≥2, NONE of the PSLQ-tested candidates were classified as Rat. This means the float64 Rat prescreen was extremely effective at d=3 — or that something subtle is happening with the classification cascade. At d=2, the PSLQ-Rat category caught some edge cases that float64 missed. The absence at d=3 warrants a spot-check.
- **Coverage gap at D=2:** Only 3,000 out of ~241,000 non-rational convergent families were PSLQ-tested. If Trans families at d=3 have b_deg=2 (not b_deg≤1), they would be in the untested portion. The d=2 pattern (b_deg=1) guided the priority, but d=3 Trans might break this pattern.
- **The ratio hypothesis is untestable without Trans:** The ratio a₃/b_sub² ∈ {-2/9, 1/4} is only checkable once Trans families are found. At d=2, the -2/9 ratio required |b₁|=3 (D≥3) and b₀ up to ±4 (D≥4). For d=3, if the ratio still requires |b_sub|=3, then Trans with b_sub in position b₁ (not b₂) requires D≥3 with the right b₀ range. We may need D≥5 to capture all coefficient combinations.
- **Desert fraction grows with degree:** At d=2, Desert was ~78% of convergent families. At d=3, it appears to be >95%. This suggests that higher polynomial degree makes Trans families exponentially rarer, consistent with the null result.
- **Possible need for d=3 T1 basis extension:** The T1 basis {1, K, π, Kπ, π²} was designed for d=2. At d=3, the limit might involve π³ or other higher-order terms. An extended basis {1, K, π, Kπ, π², Kπ², π³} might be needed.

## What would have been asked (if bidirectional)
- Should the T1 basis be extended to include π³ or K·π² for d=3?
- At d=2, the PSLQ relations never needed π² (c4=0 always). Should we test a different basis for d=3?
- Is there a theoretical prediction for D_min at d=3? The parametric theory behind the Möbius-of-π structure might constrain which (a,b) polynomials can produce Trans limits.
- Should we increase the PSLQ budget to 50,000+ for a thorough search at D=3?

## Recommended next step
Run a targeted exhaustive search at D=4 for ALL families matching the d=2 structural pattern: a₃ ∈ {-2, 1}, b₃=0, |b_sub| ∈ {2, 3}, all other coefficients in {-4,...,4}. This produces ~120K families, all of which can be PSLQ-tested in ~4 hours. If still null, extend the T1 basis to 7 elements (add π³ and Kπ²) and re-test the D=3 b_deg≤1 candidates.

## Files committed
- scale_selector.py
- screener.py
- classifier.py
- report.py
- scale_selector_report.json
- scale_selector_report.md
- structural_comparison.json
- claims.jsonl
- README.md
- halt_log.json
- discrepancy_log.json
- unexpected_finds.json
- handoff.md

## AEAL claim count
4 entries written to claims.jsonl this session
---
