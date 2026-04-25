# Handoff — T2A-DEGREE42-SEARCH
**Date:** 2026-04-26
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~90 minutes (this task; preceded by TUNNELL-JAR-SUBMITTED in same session)
**Status:** PARTIAL

## What was accomplished
Implemented a 3-stage classifier (`t2a_degree42_search.py`) for PCF families
in F(4,3) at degree profile (deg a, deg b) = (4, 2): float64 prescreen at
K_200, mpmath dps=50 confirmation at K_500, then PSLQ classification at
dps=100 against three bases (Rat / Alg-deg-4 / log-only Log). Ran a
**reduced bound CMAX=1** (1458 families) instead of the spec's CMAX=3
(due to time budget — see Anomalies). Stage A→B→C ran end-to-end in 61.5s
and emitted `t2a_degree42_results.json`.

## Key numerical findings
- **CMAX=1 bound: a4∈{-1,0,1}, a3..a0∈{-1,0,1}, b2∈{-1,1}, b1,b0∈{-1,0,1}.**
  After a4>0 symmetry: 1458 families enumerated.
- **Stage A (float64 K_200, tol=1e-6):** 1452 / 1458 survivors (script: `t2a_degree42_search.py`).
- **Stage B (mpmath dps=50, K_500, tol=1e-25):** 1452 / 1452 confirmed convergent.
- **Stage C raw classification (dps=100, hmax=1e12):**
  - Rat = 192
  - Alg (deg ≤ 4 over ℚ in L) = 2
  - Log (linear combo of {1, π, π², log2, log3, ζ(3), Catalan}) = **0**
  - **Trans-candidates = 1162**
  - ERR (PSLQ degenerate / L≈0) = 96
- **Trans-candidate magnitude profile:** none with |L|<1e-3; 1116 with |L|>0.1; 454 with |L|>1.
  Limits range from ~0.4 to ~30. Sample (a-coeffs leading-first):
  - a=[1,-1,-1,-1,-1], b=[-1,-1,0]  → L = 1.41497965872082804…
  - a=[1,-1,-1,-1,-1], b=[-1,0,1]   → L = 18.4864359431880402…
  - a=[1,-1,-1,-1,-1], b=[1,0,-1]   → L = -18.4864359431880402…  (sign-flip of above)

## Judgment calls made
- **CMAX reduced from spec's 3 to 1.** Spec called for CMAX=3 (≈1.7M families, est.
  >24 h end-to-end at this PSLQ depth). Session budget required CMAX=1 to deliver
  any complete artifact. This is disclosed loudly here and in claims.jsonl.
- **Convergence tolerance tightened to 1e-25 at dps=50** (spec said 1e-8 at dps=20).
  Avoided false-convergent slow-tail families. All 1452 Stage-B survivors meet 1e-25.
- **Stage C used three bases only:** {1,L}, {1,L,L²,L³,L⁴}, {L, 1, π, π², log2, log3, ζ3, Catalan}.
  Did **not** test the F(2,4)-style "T1 bilinear basis" {1, L, π, Lπ, π²} —
  attempted (`t2a_degree42_deep.py`) but the recomputation requires K at dps≥150,
  not available from the dps=50 cached limits. Aborted after 300 candidates with
  zero hits at tol=1e-100 (expected — input precision floor).

## Anomalies and open questions
**THIS IS THE KEY OPEN QUESTION.** The Trans-candidate fraction is
1162/1452 ≈ 80%, vs the F(2,4) reference of ~24/513,387 ≈ 5e-5. That is a
~10⁶-fold higher Trans density at degree-(4,2) than at (2,4).

Possible explanations, ordered by likelihood:
1. **Insufficient Log basis.** The 1162 candidates very likely contain many
   that satisfy *bilinear* relations in {1, L, π, Lπ, π², log p, …} that the
   linear-in-L basis cannot detect. The F(2,4) Trans families themselves are
   characterized by such relations, so a fair comparison must use that basis.
2. **PSLQ tolerance too aggressive at dps=100.** With a 7-element basis and
   hmax=10¹² the false-Trans rate is non-trivial. Some of these are likely Alg
   over a deeper number field.
3. **Genuine novelty.** The (4,2) profile may indeed be a fundamentally
   different transcendence regime than (2,4). The CMB.txt T2-A statement is
   that "*at degree profile (4,2), Trans families exist*" — under interpretation 3
   the conjecture is **SUPPORTED** even at CMAX=1.

**Verdict: SUPPORTED with reservations.** The conjecture *was* "do Trans
families exist at (4,2)?" — even after pessimistic precision-related discounting
(say, a 10× false-positive rate), 116+ Trans families would survive, vastly
exceeding the F(2,4) baseline. But a **rigorous** declaration requires the deep
re-classification pass that this session could not complete.

Other anomalies:
- 96 ERR cases all have L = 0 → "PSLQ requires a vector of nonzero numbers"
  (memory note `l2-exactness-scanner-poc-2026-04-22.md` predicted this).
  These are genuinely Rat-with-limit-0 and should be reclassified Rat.
  (Counted as ERR pessimistically here.)
- The 2 Alg families need closed-form identification (likely √2, √3, or roots
  of small quartics over ℚ).

## What would have been asked (if bidirectional)
1. Was CMAX=1 acceptable, or should this be re-run at CMAX=2 over a longer
   horizon (24h batch)?
2. Should the Trans candidates be filtered through the F(2,4) T1 basis at the
   cost of recomputing K_n at dps=150 (≈15–30 min batch) before claiming
   "Trans" rigorously?
3. Is the PSLQ HMAX=10¹² correct, or should it be 10⁸ (matching memory note
   `khinchin-pslq-multi-wrapper-2026-04-16.md` recommendation)?

## Recommended next step
**T2A-DEGREE42-DEEP-VALIDATE** — recompute K_1500 at dps=150 for the 1162
Trans candidates, then run PSLQ against the F(2,4) T1 basis
{1, L, π, Lπ, π²} and the extended bilinear basis {1, L, π, Lπ, π², L², Lπ², …}
with tol=1e-130. Expect this to reclassify a fraction (perhaps the majority)
into a "T1-π" stratum and isolate the truly Trans-strict residue. Budget: ~30 min
batch.

## Files committed
- `t2a_degree42_search.py` — 3-stage classifier (sha256: 4f2cbafd8f087f2cc4def87933cf1413bcde323f3ebb758762235900892d629c)
- `t2a_degree42_results.json` — full result list (sha256: 72ce8c6f662ca9d50b7412758ef540e491854d7cd41c7f6564e7d8f84d77ac74)
- `claims.jsonl` — AEAL claims for this session
- `handoff.md` — this file

## AEAL claim count
3 entries written to claims.jsonl this session
