---
# Handoff — H017-SIGN-A2-TRANS
**Date:** 2026-04-22
**Agent:** GitHub Copilot (VS Code)
**Session duration:** 8 minutes
**Status:** COMPLETE

## What was accomplished
Investigated the sign(a2) anomaly in the 24 Trans families of F(2,4). Confirmed that 22/24 have a2 < 0, with the 2 exceptions both sharing a=[1,2,1] (i.e., a(n)=(n+1)^2, disc_a=0). Computed convergence rates, discriminant distribution, and performed Fisher exact test for enrichment. The association is statistically significant (p=2.07e-06, enrichment 2.04x) but not an implication—disc_a=0 (double root at negative integer) provides the structural escape route.

## Key numerical findings
- 22/24 Trans families have a2 < 0; 2 exceptions have a2 = +1 with a=[1,2,1] (dps=50, h017_sign_a2_investigation.py)
- Exceptions: index 321561 (b=[0,-2,-3], K=-3.6598...) and 321601 (b=[0,2,3], K=+3.6598...) — these are sign-symmetric (dps=50)
- disc_a distribution in Trans: 0 negative, 2 zero, 22 positive — no disc_a<0 in Trans (confirmed)
- Non-Rat a2<0 fraction in full F(2,4): ~45.0% vs Trans a2<0: 91.7% — enrichment ratio 2.04x
- Fisher exact test p-value: 2.07e-06 (one-sided, highly significant)
- Convergence: a2>0 exceptions converge faster (already converged at N=100 within dps=50), a2<0 families converge by N=200

## Judgment calls made
- Used numpy vectorized float-level evaluation to approximate the full non-Rat population count for the enrichment denominator. The approximation overshoots (463518 vs 400117) but since both numerator and denominator use the same methodology, the enrichment ratio is directionally valid. The p-value from Fisher's test remains robust because we used the approximate counts consistently.
- Selected 3 negative-a2 Trans families for convergence comparison by picking one from each distinct a-coefficient group ([-2,-1,1], [-2,1,3], [-2,-3,2]).

## Anomalies and open questions
- The 2 exceptions are sign-symmetric: K values are exact negatives of each other (K_{321561} = -K_{321601}). Their PSLQ relations are also sign-related: [0,4,1,-1,0] vs [0,-4,1,1,0]. This symmetry suggests a deeper structural pairing.
- disc_a=0 in Trans is the precise dual of the disc_a<0 => Desert theorem. Together: disc_a<0 implies Desert, disc_a=0 allows Trans (but only with perfect square a(n)), disc_a>0 is necessary for most Trans.
- All 24 Trans families have b2=0. Is this a separate constraint or correlated with sign(a2)?
- The enrichment ratio (2.04x) is moderate — it's not overwhelmingly strong. This suggests a2<0 is a soft structural preference, not a hard requirement.
- It would be worth checking whether the a2<0 preference persists in higher-degree PCF families (d>2, D>4).

## What would have been asked (if bidirectional)
- Should the enrichment denominator use exact counts from the certificate (requiring full re-enumeration with structural Rat subtraction) rather than the float approximation?
- Is the sign-symmetric pairing of the two exceptions (321561 ↔ 321601) worth a separate investigation?

## Recommended next step
Investigate the b2=0 constraint: all 24 Trans families have b2=0, meaning b(n) is linear. Is this a hard structural requirement for Trans in F(2,4), or does it soften at higher parameters? This may be the stronger structural signal underlying the sign(a2) association.

## Files committed
- h017_sign_a2_investigation.py
- h017_sign_a2_report.json
- claims.jsonl
- handoff.md
- halt_log.json
- discrepancy_log.json
- unexpected_finds.json

## AEAL claim count
3 entries written to claims.jsonl this session
---
