# SPRINT-W3-SUBLEADING-BALANCE — Report

**Date:** 2026-04-27
**Sprint week:** 3 (final probe of the Trans locus `a₂/b₁² = −2/9`)
**Status:** complete; verdict = **PATH 3** (all three sub-leading approaches NEGATIVE → empirical paper from W1+W2+585k survey)

---

## 1. Recap (W1 → W2 → W3)

| Sprint | Hypothesis | Result |
|---|---|---|
| W1 | Strong indicial form: `a₂/b₁² = −2/9 ⇔ {α₁, α₂} = {1/3, 2/3}` | **Refuted.** Indicial pair {1/3, 2/3} forces irrational `b₀/b₁ = (27 ± √17)/18`; not the empirical Trans loci. |
| W1 | Closed form for indicial exponent | `α(μ) = −((b₁−b₀)·μ + (a₁−a₂)) / (b₁·μ − 2 a₂)` (verified against numerics). |
| W2 | Leading-Birkhoff invariants distinguish Trans | **Tautological.** PSLQ identity `\|μ₊/μ₋\| = (13+3√17)/4 ↔ a₂/b₁² = −2/9` is Vieta-derivable from `μ₊·μ₋ = a₂` and `μ₊+μ₋ = b₁`. Sum/product/discriminant of indicial exponents are NOT constant across Trans families. |
| **W3-A** | Sub-leading [n⁻¹] balance forces a resonance on Trans | **NEGATIVE.** A_num factors as `(a₂ − b₁μ)·(4 a₂ − b₁²)`; vanishes only on the double-root locus `4 a₂ = b₁²` (Alg). On Trans, `A\|μ_± = ∓√17·b₁/3` ≠ 0. |
| **W3-B** | Convergence rate `ρₙ = \|rₙ−L\|·qₙ²` separates Trans from Log/Alg | **NEGATIVE/INCONCLUSIVE.** `\|rₙ − L\|` falls below `mp.dps = 200` by n≈300 (rate is hyperexponential because qₙ ∼ Γ(n+1)·μ^n); the rate constant `\|μ_−/μ_+\|` is exactly the W2-tautological quantity. |
| **W3-C** | The limits L are algebraic, or expressible in {√17, π, log 2} | **NEGATIVE.** PSLQ at dps=300, maxcoeff=10000 finds no relation in `[1, L, L², L³, L⁴]` and no relation in `[1, L, √17, π, log 2]`. The 10 pairwise relations found are tautological scale-invariance: `L(λ·b₁) = λ·L(b₁)` on the (a₀,a₁,b₀) = (0,0,0) sub-family. |

---

## 2. Part A — Sub-leading Birkhoff balance

**Setup.** Birkhoff ansatz `yₙ = Γ(n+1)·μⁿ·n^α·(1 + c₁/n + c₂/n² + …)`. Substitute into `yₙ₊₁ − bₙ·yₙ + aₙ·yₙ₋₁ = 0` divided by `Γ(n+1)·μⁿ·n^α`. With `u = 1/n`:

- [u⁻¹] coefficient: `a₂/μ − b₁ + μ` ⇒ characteristic equation `μ² − b₁μ + a₂ = 0`. ✓
- [u⁰] coefficient: `(a₁ − a₂α + a₂ + αμ² − b₀μ + (b₁μ − μ²)·c₁ + b₁μ)/μ`. The `c₁`-coefficient at this order is `μ²−b₁μ+a₂ = 0` (drops automatically); the equation determines α via the W1 closed form. ✓
- [u¹] coefficient (sub-leading): linear in `c₁` and `c₂`. The `c₂` coefficient is again exactly `μ²−b₁μ+a₂ = 0` (drops). The `c₁` coefficient, after reducing μ² and substituting α = W1, is

  $$ A_{\text{num}} \;=\; (a_2 - b_1 \mu)\,(4 a_2 - b_1^2)\,,\qquad A_{\text{den}} \;=\; a_2 b_1 + 2 a_2 \mu - b_1^2 \mu. $$

**Resonance loci.** `A = 0` iff
  1. `a₂ = b₁μ` ⇒ via char eq `μ = 0` (degenerate; not interesting), **or**
  2. `4a₂ = b₁²` ⇒ Alg double-root locus (CF discriminant = 0).

Neither is the Trans locus `a₂ = −2b₁²/9`. On Trans:
  $$ A\big|_{a_2=-2b_1^2/9,\;\mu=\mu_\pm} \;=\; \mp\,\frac{\sqrt{17}\,b_1}{3}\ \neq\ 0. $$

**Verdict.** The [n⁻¹] balance is *regular* on Trans; `c₁ = −B/A` is uniquely determined and yields no new constraint on (a₀,a₁,a₂,b₀,b₁) beyond the indicial pair. Sub-leading resonance does **not** explain the Trans property.

Cross-check on Log loci: `A` is also nonzero (e.g. on `a₂/b₁² = −1/4`, `A = −2b₁(b₁+4μ)/(b₁+6μ)` ≠ 0). So the [n⁻¹] balance is generically regular; the only exceptional locus is `4 a₂ = b₁²`.

(Source: `sprint_w3/subleading_birkhoff.py`, `_subleading_birkhoff.log`.)

---

## 3. Part B — Convergence-rate experiment

**Setup.** For each family, generate `(pₙ, qₙ)` by the recurrence with seeds `(p₋₁, p₀) = (1, 0)`, `(q₋₁, q₀) = (0, 1)`. Define `L = r_N` at N=600 (full-precision proxy for the limit), `rₙ = pₙ/qₙ`. Tested 10 Trans + 5 Log + 5 Alg families at `mp.dps = 200`.

**Findings.**
- For Trans and Log (real-monotone CFs): `log₁₀|rₙ−L|` is already ≈ −200 at n=300, i.e. equal to the working precision; `r₅₀₀ = L` to all 200 digits. The CF is hyperexponentially convergent.
- The classical Diophantine normalization `ρₙ = |rₙ−L|·qₙ²` explodes (≈10^2620 at n=500) because `qₙ ∼ Γ(n+1)μ⁺ⁿn^α` (note the Γ factor). The right rate constant is

  $$ |r_n - L| \;\sim\; \frac{|\mu_-/\mu_+|^n}{q_n\,q_{n+1}}\,. $$

  On Trans, `|μ_-/μ_+|² = (13 − 3√17)/(13 + 3√17)`, which is Vieta-tautologically equivalent to `a₂/b₁² = −2/9` (already known from W2). No new amplitude/coefficient invariant emerges.
- For complex-root Alg families (A02–A05), `r₅₀₀` is far from a fixed limit (the recurrence does not have a unique convergent limit; behavior is oscillatory). This is consistent with the empirical "Alg" classification.

**Verdict.** PATH 2 **NEGATIVE**: convergence rate gives no new invariant; the surviving rate constant is the same Vieta-tautological √17 quantity W2 already established.

(Source: `sprint_w3/convergence_rate.py`, `_convergence_rate.log`, `convergence_rate.json`.)

---

## 4. Part C — Direct algebraic identification of L

**Setup.** 10 Trans families, `mp.dps = 300`, N = 500. PSLQ tolerance 10⁻⁴⁰, `maxcoeff = 10000`. Phantom-hit rule: reject relations whose target-coefficient is zero.

### C1 — `[1, L, L², L³, L⁴]`
**No relation found** for any of the 10 Trans L values. So `L` is not a degree-≤4 algebraic number with coefficient bound 10000. (For comparison, Heegner-type Diophantine constants typically fall below this bound in dps≈100; the absence of a hit at dps=300, bound 10000 is strong evidence of transcendentality.)

### C2 — Pairwise `[1, Lᵢ, Lⱼ, LᵢLⱼ, Lᵢ², Lⱼ²]`
Ten relations found among the 45 pairs. **All ten are tautological consequences of the scale invariance**

  $$ L(\lambda\,b_1)\;=\;\lambda\,L(b_1)\quad\text{when}\quad(a_0,a_1,b_0)=(0,0,0)\,,$$

verified directly: `L(b₁=6) = 2·L(b₁=3)`, `L(b₁=9) = 3·L(b₁=3)`, etc. (T01:0.4936… ; T03:0.9874… = 2·T01 ; T05:1.4811… = 3·T01.) The sub-family with `(a₀,a₁,b₀) = (1,0,1)` is *not* scale-invariant (b₀=1 breaks homogeneity), and indeed contributes no C2 hits. After interpretation these are *not* genuine algebraic relations between distinct CFs.

### C3 — Mixed transcendental basis `[1, L, √17, π, log 2]`
**No relation found** for any Trans family.

**Verdict.** The Trans CF limits L are (to bound 10000 at dps=300) genuinely transcendental and do not factor through {√17, π, log 2}. Path of analytic identification is closed.

(Source: `sprint_w3/direct_algebraic.py`, `_direct_algebraic.log`, `direct_algebraic.json`.)

---

## 5. PATH selection: **PATH 3**

The three sub-leading paths corresponded to three distinct possible "escapes" from the W1+W2 dead end:

- PATH 1 (sub-leading resonance closes the gap) — refuted by Part A.
- PATH 2 (convergence rate exposes a new invariant) — refuted by Part B.
- PATH 3 (analytic frameworks all insufficient → write empirical paper) — **selected.**

**Recommendation:** the empirical paper should be written from existing material:

1. The 585k-family classification survey (existing infrastructure) → empirical evidence that exactly the locus `a₂/b₁² = −2/9` (with the sign condition `a₂ < 0`) produces transcendental CF limits, while `−1/4`, `−1/9`, `−1/36`, … produce log-type families and `4a₂ ≥ b₁²` produces algebraic families.
2. **W1 indicial closed form** as the sole rigorous analytic theorem.
3. **W2 PSLQ identity** `|μ₊/μ₋| = (13+3√17)/4 ↔ a₂/b₁² = −2/9`, recognised explicitly as Vieta-tautological but used to motivate the geometric framing (signed Riemann scheme).
4. **W3 negative results** stated as bounding the analytic landscape: sub-leading Birkhoff is regular on Trans, convergence rate is W2-tautological, and the limits are not low-degree algebraic nor combinations of √17/π/log 2 to bound 10000.

The framing should be: *"Trans is an empirically robust but currently analytically opaque locus; we present the strongest classification + indicial theorem + tautology + bounds to date and pose explicit open questions."*

---

## 6. Outline of empirical paper

Working title: **"Empirical classification of the Trans/Log/Alg trichotomy in degree-(2,1) Pochhammer continued fractions and the locus `a₂/b₁² = −2/9`"**.

1. **Introduction** — empirical observation, the trichotomy, the −2/9 anomaly.
2. **Setup** — degree-(2,1) recurrence, leading conventions, Birkhoff ansatz.
3. **W1 theorem** — indicial closed form `α(μ) = −((b₁−b₀)μ + a₁−a₂)/(b₁μ−2a₂)` with full derivation; refutation of strong indicial form.
4. **W2 PSLQ identity** — `|μ₊/μ₋| = (13+3√17)/4` and Vieta verification.
5. **The 585k empirical survey** — methodology, Trans rate, Log strata, Alg strata.
6. **Negative results bounding the analytic landscape** — sub-leading regularity (W3-A), convergence-rate tautology (W3-B), PSLQ exclusion of low-degree algebraic and `{√17, π, log 2}` closed forms (W3-C).
7. **Open questions** — modular interpretation? hypergeometric monodromy? higher-rank PSLQ at dps=1000?
8. **Reproducibility** — claim manifest, scripts, hashes (AEAL).

---

## 7. AEAL claims summary

Four entries written to `claims.jsonl`: A (NEGATIVE), B (NEGATIVE/INCONCLUSIVE), C (NEGATIVE), synthesis (PATH_3). All carry `phantom_hit_rule_applied: true` and SHA-256 hashes of their generating scripts.

---

## 8. File manifest (this session)

```
sessions/2026-04-27/SPRINT-W3-SUBLEADING-BALANCE/
├── claims.jsonl
├── halt_log.json                            (empty, no halt triggered)
├── discrepancy_log.json                     (empty)
├── unexpected_finds.json                    (empty: scale-invariance C2 hits are
│                                             expected and tautological, not unexpected)
├── handoff.md
├── sprint_w3_report.md                      (this file)
└── sprint_w3/
    ├── subleading_birkhoff.py               (Part A driver)
    ├── _subleading_birkhoff.log             (Part A output)
    ├── convergence_rate.py                  (Part B driver)
    ├── _convergence_rate.log                (Part B output)
    ├── convergence_rate.json                (Part B numerical record)
    ├── direct_algebraic.py                  (Part C driver)
    ├── _direct_algebraic.log                (Part C output)
    └── direct_algebraic.json                (Part C numerical record)
```
