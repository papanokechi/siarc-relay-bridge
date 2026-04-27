# Handoff — SPRINT-W3-SUBLEADING-BALANCE
**Date:** 2026-04-27
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~80 minutes
**Status:** COMPLETE

## What was accomplished

Completed all three sub-leading probes of the Trans locus `a₂/b₁² = −2/9`. Part A (sub-leading Birkhoff [n⁻¹] balance), Part B (convergence-rate experiment over 20 families), and Part C (PSLQ algebraic identification of CF limits at dps=300, maxcoeff=10000) all returned **NEGATIVE** results. The verdict is **PATH 3**: write the empirical paper from the existing W1 indicial closed form, W2 PSLQ identity, the 585k-family classification survey, and the W3 negative results bounding the analytic landscape.

## Key numerical findings

- **Part A.** The c₁-coefficient at the [u¹] order of the Birkhoff cascade, after using the W1 indicial form, factors as `A_num = (a₂ − b₁μ)·(4 a₂ − b₁²)`. Vanishes only on the double-root locus `4 a₂ = b₁²` (Alg discriminant zero), NOT on the Trans locus. On Trans, `A|μ_± = ∓√17·b₁/3 ≠ 0`. (symbolic; script `subleading_birkhoff.py`.)
- **Part B.** For all 10 Trans families, `log₁₀|rₙ − L|` reaches −200 at n≈300 (mp.dps=200, N=600), i.e. CF is hyperexponentially convergent. The classical ρₙ = |rₙ−L|·qₙ² normalization is meaningless because qₙ ∼ Γ(n+1)μⁿ. The natural rate constant `|μ₋/μ₊|` is exactly the W2-tautological √17 quantity.
- **Part C.** No PSLQ relation found among `[1, L, L², L³, L⁴]` (maxcoeff=10000) for any of 10 Trans L-values; no relation against `[1, L, √17, π, log 2]`. Pairwise relations for the (a₀,a₁,b₀)=(0,0,0) sub-family are tautological linear scaling `L(λb₁) = λ·L(b₁)`. (mp.dps=300; script `direct_algebraic.py`.)

## Judgment calls made

- **Sub-leading expansion includes Γ(n+1).** The prompt's Birkhoff ansatz literally said `yₙ = μⁿ·n^α·(1 + c₁/n + …)`, but for degree-(2,1) coefficient recurrences `yₙ ∼ Γ(n+1)·μⁿ` is the correct leading order; without Γ(n+1) the [n⁻¹] balance is dimensionally mismatched. I used `yₙ = Γ(n+1)·μⁿ·n^α·(1+c₁/n+…)`.
- **Robust c₁ extraction.** The first symbolic pass used `expr.coeff(c1)` and incorrectly returned 0 because of how sympy distributed coefficients across a sum-with-rational-coefficients. Switched to `Poly(expr, c1, c2).coeff_monomial(c1)`, which gave the correct answer `(2a₂ − b₁μ + αb₁μ − b₀μ + …)/μ` and after reduction the factored form `A_num = (a₂ − b₁μ)(4a₂ − b₁²)`.
- **Picked rate-constant proxy `|μ_-/μ_+|` over a forced `|rₙ−L|·qₙ²` analysis.** Once `|rₙ−L|` collapses below mp.dps, the experiment reverts to the tautological characteristic-roots ratio. Increasing dps was deemed wasteful given that the rate is provably W2-tautological.
- **Treated Part C2 hits as tautological scale-invariance** (and logged in `unexpected_finds.json` as such, not as phantom hits). The L-coefficient is non-zero, but the relations are vacuous after inspection; this nuance is documented in the report and unexpected-finds log.

## Anomalies and open questions

- **Part C2 scale-invariance hits are a phantom-hit-rule blind spot.** The standard "L-coeff = 0" rule does not catch tautologies arising from continuous symmetry of the recurrence (here, b₁ → λb₁). In future sprints we may want a strengthened phantom rule that tests whether a relation persists under such symmetries.
- **Part B's "wrong normalization" issue.** The convergence rate `|rₙ−L|·qₙ²` is the appropriate Diophantine quantity for *continued fractions of irrationals* (where the partial quotients are O(1)), not for hyperexponential CFs with degree-(2,1) coefficients. A more thoughtful normalization, e.g. `|rₙ−L|·qₙ·qₙ₊₁` or `(|rₙ−L|·qₙ²)^{1/n}`, might give finite limits, but those reduce to `|μ_-/μ_+|` (Vieta-tautological).
- **Open analytic question (for Claude).** Is there a hypergeometric-monodromy or modular-curve interpretation that distinguishes `a₂/b₁² = −2/9` non-tautologically? W3 has now ruled out all standard Birkhoff-style routes, but higher-structure approaches (e.g. Riemann-scheme rigidity, Stokes data of the Birkhoff connection at infinity) remain unexamined.
- **Bound 10000 at dps 300 is moderate.** A rare possibility is that L is algebraic of degree ≤4 with coefficient bound > 10000. If Claude wants a stronger negative, repeat C1 at maxcoeff=10⁵ or 10⁶ (cost ≈ linear; safe to run).

## What would have been asked (if bidirectional)

1. *"Is the Birkhoff Γ(n+1) leading factor canonical, or do you want me to follow the prompt literally and accept that the [u⁻¹] balance won't close?"* — I went with the canonical analytical convention.
2. *"For Part C, do you want C2 'scale-invariance' relations counted as POSITIVE or filtered out as tautological?"* — I filtered them.
3. *"Should I increase dps to 600 and bound to 10⁶ for Part C1 to make the 'Trans is transcendental' claim stronger?"* — I did not, given the path-3 verdict; one upgrade run would suffice if Claude wants it.

## Recommended next step

**SPRINT-W4-EMPIRICAL-PAPER-DRAFT.** Begin drafting the empirical paper "Empirical classification of the Trans/Log/Alg trichotomy in degree-(2,1) Pochhammer continued fractions and the locus a₂/b₁² = −2/9" using the outline in `sprint_w3_report.md` §6. Inputs required:

- Existing 585k-family Trans/Log/Alg classification CSV (from prior survey infrastructure).
- W1 indicial closed form derivation (from W1 deliverables).
- W2 PSLQ identity script and output (from W2 deliverables).
- W3 negative-result section (from this session).

Optional pre-paper polish run: extend Part C1 to `maxcoeff = 10⁶` at dps=600 to harden the "Trans is transcendental" claim before submission.

## Files committed

```
sessions/2026-04-27/SPRINT-W3-SUBLEADING-BALANCE/
├── claims.jsonl
├── handoff.md
├── halt_log.json                      (empty)
├── discrepancy_log.json               (empty)
├── unexpected_finds.json              (logs scale-invariance C2 tautology)
├── sprint_w3_report.md
└── sprint_w3/
    ├── subleading_birkhoff.py         (Part A)
    ├── _subleading_birkhoff.log
    ├── convergence_rate.py            (Part B)
    ├── _convergence_rate.log
    ├── convergence_rate.json
    ├── direct_algebraic.py            (Part C)
    ├── _direct_algebraic.log
    └── direct_algebraic.json
```

## AEAL claim count

4 entries written to `claims.jsonl` this session: Part A (NEGATIVE), Part B (NEGATIVE/INCONCLUSIVE), Part C (NEGATIVE), synthesis (PATH_3).
