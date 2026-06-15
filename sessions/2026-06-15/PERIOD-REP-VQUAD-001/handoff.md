---
# Handoff — PERIOD-REP-VQUAD-001
**Date:** 2026-06-15
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~120 min
**Status:** COMPLETE

## What was accomplished
Ran the full 8-stage sub-problem-A scoping probe asking whether the V_quad
connection coefficient `C` admits a clean exponential-period representation
`C = ∫_γ e^{f} g dt` (Fresán–Jossen). Inventoried the V_quad resurgence/Sakai data
and the proven EBR cc3 exponential-period template; read the *authoritative*
Fresán–Jossen source (the **book** `expmot.pdf`, not an arXiv id — both suggested
ids are false); reconstructed the Painlevé-V linear problem (Jimbo–Miwa,
specialised to `θ_∞=2/√3, α=1/6`); proposed an explicit candidate `(X,f,ω,γ)`;
ran a high-precision numerical sanity check; checked the candidate against every
FJ axiom; and delivered the verdict. **Verdict: NEEDS-MORE-PROBE (favourable).**
No corpus material modified; no Zenodo deposit; ready-state git HELD for operator.

## Key numerical findings
- Bridge `C = |Γ(β)|·K`, `S = 2πK`, with `S/C = 2π/|Γ(β)|` **exact** (residual 0)
  (dps=240, script=`scripts/numcheck_period_rep.py` T1). `C = 0.43770528619353…`.
- Dominant **Borel singularity at `ξ₀ = 2/√3` to 95.6 digits**
  (`lim|a_n/a_{n+1}|·n`); sub-dominant relative drift `2.1e-5` over a decade of
  `n` ⇒ single isolated branch (dps=240, T2). Necessary—not sufficient—for `ω`
  algebraic.
- `S`, `C` are **not** low-height combinations of `√π`/single Γ-values
  (PSLQ null, dps=45, T3) ⇒ genuine higher period if any.
- `K = 0.07287810255186696412944236333…` (58 cross-stable digits); `S` matches
  the deposited anchor to 41.3 digits.

## Judgment calls made
- **Resolved the task's ambiguous "connection coefficient C"** to
  `C_Borel = |Γ(β)|·K` (the `Γ(branch)·amplitude` skeleton, matching EBR
  `κ=Γ(4/3)·A₀`), distinct from the Stokes `S=2πK` and from the δ growth constant.
- **Verdict = NEEDS-MORE-PROBE (not GO-WITH-COMPLICATION).** Reason: the
  unresolved item (`ω` algebraicity) is not a side-risk to carry but the *input*
  `ω` that B/C/D consume; the task forbids GO while any FJ axiom is UNCLEAR
  (axioms 3 and 6 are). Classed "favourable" because Stage-5 evidence predicts the
  follow-up resolves for the candidate.
- **Standing meta-rule HELD over the literal "git push origin main"** — prepared
  ready-state only (see below), as on EBR3-REVISION-001.

## Anomalies and open questions  *(MOST IMPORTANT)*
- **Task object/precision conflation (corrected, see `data-inventory.json` C1).**
  The prompt's "δ Fredholm verified to 65 digits (Zenodo 20624814)" cites a
  *correct* DOI (commit 50f9989 ties 20624814 to the pcf-delta Fredholm growth
  constant), but conflates two objects: δ = log R_∞ is the *growth constant*
  (convergent/classical), a **different object from `C`** (the divergent-series
  Stokes datum). **The 65-digit precision is δ's, not `C`'s: `C` is known to ~58
  digits (via K), `S` to ~41.** Also δ(1,0,1) is the `b_n=n²+1` family, **not**
  V_quad (= V(3,1,1)). Anyone scoping B/C/D on a "65-digit C" assumption is wrong.
- **The load-bearing gap is `ω` algebraicity (G-OMEGA).** V_quad sits on the
  *non-holonomic* WKB/Painlevé side; unlike EBR (holonomic order-4 `L`), it has
  **no explicit algebraic Borel operator**, and its **accessory parameter is
  transcendental** (EBR-II §5). This is *the* thing that could make the clean
  exponential-period form fail. The Borel single-branch evidence is encouraging
  but does **not** prove algebraicity.
- **No V_quad Lax pair or Kovacic execution is in the corpus** (gaps G-LAX,
  G-KOVACIC). The "SL(2) by exact Kovacic" claim is asserted, not located; the
  Stage-3 linear system is literature-derived (Jimbo–Miwa), not corpus-verified.
- **FJ has no arXiv id** — the book is the only source. The two suggested arXiv
  numbers are unrelated papers. Future relays must not cite them.
- The T1 bridge is, by construction, a *rewrite* of the same large-order data, so
  it is a consistency check, not an independent evaluation. The decisive
  independent test (a clean integral evaluating to `C`) **cannot be run until `ω`
  is built**.

## What would have been asked (if bidirectional)
1. By "connection coefficient C," do you mean the Stokes `S=2πK`, the Borel
   branch coefficient `C_Borel=|Γ(β)|·K` (assumed here), or σ_conn directly?
2. Is there an unpublished V_quad Lax pair / Kovacic worksheet I should use
   instead of reconstructing Jimbo–Miwa from the literature?
3. For the follow-up, prefer (a) Borel–Padé + holonomic recognition of `B[φ]`, or
   (b) direct isomonodromy/`G_M` construction?

## Recommended next step
Authorise **PERIOD-REP-VQUAD-002** (1–2 weeks): construct the explicit V_quad
algebraic Borel operator `L_V` (Borel–Padé of the in-hand `a_n` to order 1500 +
`ore_algebra`/`gfun` holonomic recognition; test the 2-instanton tower at
`2ξ₀,3ξ₀`) and decide whether `ω = B[φ]dξ` is algebraic over `ℚ(√3)`. Decision
gate: algebraic ⇒ upgrade A to **GO**, start B; provably non-algebraic ⇒ A is
**NO-GO (clean form)**, pivot to the relative/family period (verdict.md §7.5).

## Files committed
*(ready-state staged, NOT committed — operator runs git by hand)*
- data-inventory.json
- fresan-jossen-axioms.md
- vquad-linear-system.md
- candidate-data.md
- numerical-check.md
- fresan-jossen-compatibility.md
- verdict.md
- ledger.json
- claims.jsonl
- handoff.md
- scripts/numcheck_period_rep.py
- scripts/numcheck_period_rep_results.json

## AEAL claim count
22 entries written to claims.jsonl this session
---
