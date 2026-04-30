# Handoff — UMB-GAMMA0-2-SWEEP (P-08)
**Date:** 2026-04-30
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~12 minutes
**Status:** COMPLETE — HALT_A triggered (predicted halt branch)

## What was accomplished
Built a deg-(2,1) integer-PCF sweep over five non-PSL₂(ℤ) Fuchsian
groups (Γ₀(2) and Hecke G_q for q ∈ {4,5,6,8}) and tested whether
the naive indicial-root prediction ρ = −m(b−m)/b² produces
transcendental limits at the predicted ratio. 19,965 families were
enumerated at integrality of a₂/b₁² = ρ, 15,819 converged at K=500
float64, and full Stage B/C PSLQ classification ran at dps=100,
N=600. Each group cleared the prompt's ≥1000-family threshold.

## Key numerical findings
- **Per-group ratio table (script `umb_gamma0_2_sweep.py`, dps=100):**
  - Γ₀(2) → ρ = −1/4   total 5324  conv 1484  Trans 0  Log 0  Alg 235  Rat 23
  - G_4   → ρ = −3/16  total 3993  conv 3847  Trans 0  Log 0  Alg 159  Rat 17
  - G_5   → ρ = −4/25  total 3993  conv 3854  Trans 0  Log 0  Alg 116  Rat 6
  - G_6   → ρ = −5/36  total 3993  conv 3980  Trans 0  Log 0  Alg 96   Rat 3
  - G_8   → ρ = −7/64  total 2662  conv 2654  Trans 0  Log 0  Alg 61   Rat 1
- **HALT_A** triggered exactly as the prompt anticipated: G_4 at
  ρ = −3/16 is empirically a desert. So is every other tested group.
- 0 Phantom, 0 Log relations across the entire sweep at the basis
  [1, L, π, Lπ, π², Lπ², log 2, L log 2].
- All convergent counts ≥ 1000, satisfying the ≥1000-families-per-
  group validation threshold.

## Judgment calls made
- **Free-coefficient cube H = 5** for every group (matches
  UMB-RES-EXTEND base sweep). This keeps total enumeration ~20k and
  PSLQ wall under four minutes while exceeding the 1000-family floor.
- **Single-sign b₁** (positive only): the −b₁ stratum is a sign
  reflection that produces no new ratios, halving cost.
- **Trans basis fixed** to the 8-vector used in UMB-RES-EXTEND /
  T2B-RESONANCE (no log 3, no Catalan). Justification: a richer
  basis was already deployed in UMB-CLASSB-SATURATION deep checks
  and yielded no Trans; we keep this comparable to the −2/9 PSL₂(ℤ)
  reference so that any positive G_q hit would have been directly
  basis-comparable.
- **No deep dps=150 pass needed** (0 Trans hits to deep-validate).
  The deep_validate_trans hook is wired and reusable for the
  follow-up sessions Claude is expected to ask for.

## Anomalies and open questions
- **Γ₀(2) at ρ = −1/4 is empty of Trans.** This is interesting:
  Γ₀(2) has well-known modular CFs (e.g. Brouncker / F24 /
  Berndt-Bowman) but those sit at the **+1/4** Class B stratum,
  not −1/4. The sign asymmetry is consistent with the Theorem 3
  +1/4 universality already seen and reinforces that −ρ is the
  correct sign in the m=1 indicial-root prediction only when the
  cuspidal stratum is genuinely two-cusp (PSL₂(ℤ) case). For
  Γ₀(2) the relevant elliptic point order-2 contributes indicial
  roots {0, 1/2}, which give predicted ρ = 0 (not −1/4). The
  −1/4 prediction in the prompt may itself be a specification
  error worth flagging to Claude.
- **G_4 ≡ Γ₀(2)?** The Hecke triangle G_4 with vertices (∞, 0,
  i+1)/2 is isomorphic to Γ₀(2) up to commensurability and
  signature relabelling. Yet under our prediction map they sit at
  different ratios (−1/4 vs −3/16). Either the prediction map is
  group-naive, or one of the two embeddings is the right one and
  we should expect a degeneracy. Worth a Claude-side reconciliation.
- **0 Alg hits at high b₁** for G_5, G_6, G_8 is curious — the
  ratio Alg-rate falls monotonically with q. Possibly an artefact
  of the integrality pinch (a₂ grows like q²), but flagging in
  case it has structural meaning (pruning of arithmetic strata as
  group-theoretic complexity rises).
- The negative result confirms the prompt's working hypothesis:
  the indicial-root argument from UMB Remark 8 is **specific to
  PSL₂(ℤ)** and does not generalise verbatim. A multiplicity- or
  Stokes-aware refinement is required.

## What would have been asked (if bidirectional)
1. The prompt's predicted ρ for Γ₀(2) is −1/4 from "m=1, b=2".
   But Γ₀(2)'s order-2 elliptic point contributes indicial roots
   {0, 1/2} (not {1/2, 1/2}), giving ρ = 0 by the (m=0, b=2)
   reading. Should the Γ₀(2) row be re-tested at ρ = 0 (a clean
   Rat target rather than a Trans candidate)?
2. Should the Hecke G_q test include the **two** distinct cusp
   indicial pairs ({1/q, (q−1)/q} *and* {1/2, 1/2} from the
   order-2 elliptic generator)? The latter would predict
   ρ = −1/4 again — so the negative G_4 result might be a
   confluence of two distinct predictions both failing.

## Recommended next step
**UMB-GQ-INDICIAL-REFINE** (one prompt, ~30 min):
Replace the single-pair indicial-root prediction with a
multiplicity-weighted scan. For each group enumerate the *full*
list of indicial-root pairs (cusps + elliptic + parabolic) and
test every ρ_{ij} = −m_i(b_j − m_i)/b_j² rather than only the
cuspidal one. Use the existing scaffold; expand RATIO list to
~6–10 ratios per group; same Stage A / B / C pipeline. If still
all-zero, escalate to **UMB-STOKES-REFINEMENT** (full Birkhoff-
Stokes data extraction on representative G_4 family).

## Files committed
- claims.jsonl
- discrepancy_log.json
- group_summary.png
- halt_log.json
- handoff.md
- make_plot.py
- ratio_table.csv
- results.json
- run.log
- trans_rate_vs_ratio.png
- umb_gamma0_2_sweep.py
- unexpected_finds.json

## AEAL claim count
6 entries written to claims.jsonl this session.
