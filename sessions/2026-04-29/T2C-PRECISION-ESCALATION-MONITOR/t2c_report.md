# T2C — Layer 5 Precision Escalation Monitor: Report

**Task:** T2C-PRECISION-ESCALATION-MONITOR
**Date:** 2026-04-29
**Agent:** GitHub Copilot (VS Code), .venv Python + mpmath
**Status:** COMPLETE with UNEXPECTED FINDING (logged, not halted)

---

## 1. Method

For every family `(a2, a1, a0, b1, b0)` the CF limit
`L = b(0) + a(1)/(b(1) + a(2)/(b(2) + ...))` is evaluated at
working precision `dps + 30` with adaptive depth (≥ 12·dps and grown
until two depths agree to `10^-(dps+10)`).

At each `dps ∈ {50, 100, 150, 200, 250, 300}` we run mpmath PSLQ on

```
B = { L, √2, √3, √5, √17, π, log2, ζ(3), 1 }
```

with tolerance `10^-(dps-5)` and `maxcoeff = 10^max(8,dps/10)`.

**Phantom-hit rule:** any returned relation with `L`-coefficient = 0
is REJECTED (its residual is then logged as the no-relation floor
`10^-dps`).

The residual `r(d)` is

* `|⟨rel, B⟩|` clipped from below at `10^-dps` if a non-phantom
  relation is accepted, otherwise
* `10^-dps` (the precision-limited tolerance — i.e. the limit
  successfully resisted identification at that dps).

Slope `m` of `log10(r(d))` vs `d` is computed by ordinary least squares.
Classification: `m < -0.8 → GENUINE`, `m > -0.2 → SPURIOUS`,
otherwise `AMBIGUOUS`.

In addition, an extended basis sweep at `dps = 300` is run with
`B' = {L, L², √17, π, log2, ζ(3), e, γ, 1}` (phantom rule: reject if
`L`- and `L²`-coefficients are both zero).

---

## 2. Per-family results (30 families)

| Family | Stratum | a2/b1² | Slope m | PSLQ-accept@all dps | Class |
|---|---|---|---|---|---|
| T01_116433 | Trans | -2/9 | -1.0000 | no | GENUINE |
| T02_116447 | Trans | -2/9 | -1.0000 | no | GENUINE |
| T03_118473 | Trans | -2/9 | -1.0000 | no | GENUINE |
| T04_118474 | Trans | -2/9 | -1.0000 | no | GENUINE |
| T05_118486 | Trans | -2/9 | -1.0000 | no | GENUINE |
| T06_118487 | Trans | -2/9 | -1.0000 | no | GENUINE |
| T07_130100 | Trans | -2/9 | -1.0000 | no | GENUINE |
| **T08_130101** | Trans | -2/9 | -1.0000 | **YES (closed form)** | GENUINE |
| T09_130102 | Trans | -2/9 | -1.0000 | no | GENUINE |
| T10_130116 | Trans | -2/9 | -1.0000 | no | GENUINE |
| **T11_130117** | Trans | -2/9 | -1.0000 | **YES (closed form)** | GENUINE |
| T12_130118 | Trans | -2/9 | -1.0000 | no | GENUINE |
| T13_143930 | Trans | -2/9 | -1.0000 | no | GENUINE |
| **T14_143931** | Trans | -2/9 | -1.0000 | **YES (closed form)** | GENUINE |
| T15_143932 | Trans | -2/9 | -1.0000 | no | GENUINE |
| T16_143933 | Trans | -2/9 | -1.0000 | no | GENUINE |
| T17_143934 | Trans | -2/9 | -1.0000 | no | GENUINE |
| T18_143948 | Trans | -2/9 | -1.0000 | no | GENUINE |
| T19_143949 | Trans | -2/9 | -1.0000 | no | GENUINE |
| T20_143950 | Trans | -2/9 | -1.0000 | no | GENUINE |
| **T21_143951** | Trans | -2/9 | -1.0000 | **YES (closed form)** | GENUINE |
| T22_143952 | Trans | -2/9 | -1.0000 | no | GENUINE |
| T23_321561 | Trans | +1/4 | -1.0000 | no | GENUINE |
| T24_321601 | Trans | +1/4 | -1.0000 | no | GENUINE |
| L01_log_p63 | Log | -1/36 | -1.0000 | no¹ | GENUINE |
| L02_log_n63 | Log | -1/36 | -1.0000 | no¹ | GENUINE |
| L03_log_p7  | Log | -1/49 | -1.0000 | no¹ | GENUINE |
| A01_1psqrt2 | Alg | (b1=0) | -1.0000 | YES (closed form) | GENUINE |
| A02_phi     | Alg | (b1=0) | -1.0000 | YES (closed form) | GENUINE |
| A03_1psqrt3 | Alg | (b1=0) | -1.0000 | YES (closed form) | GENUINE |

¹ Log limits `2/log(2)` are non-linear in `log(2)`; the linear-PSLQ
basis cannot detect them. This is correct behaviour, not a flaw.

---

## 3. Summary statistics

| Stratum | n | mean slope | std | min | max |
|---|---|---|---|---|---|
| Trans | 24 | −0.999999 | 4.6e-6 | −1.0000 | −0.99998 |
| Log   |  3 | −1.000000 | 0      | −1.0000 | −1.0000 |
| Alg   |  3 | −1.000000 | 0      | −1.0000 | −1.0000 |

**Separation gap (min Trans − max Log) = 0.0**

---

## 4. Separation analysis — IS slope a reliable Trans discriminator?

**No.** Across all 30 families the slope is essentially −1 because the
PSLQ residual saturates at the precision floor `10^-dps` whether or
not a true relation exists. The slope-only protocol therefore cannot
distinguish

* genuine Trans-hard limits (no algebraic identity of any order),
* closed-form Trans limits in `Q(π,1)` (e.g. T08, T11, T14, T21),
* algebraic limits (sqrt-of-rationals),

since all three drive the residual below `10^-dps` and our floor caps
them at exactly that level.

A truly **SPURIOUS** family — one where PSLQ returns an L-bearing
relation at low `dps` whose residual fails to shrink at higher `dps`
— **did not appear in this 30-family training set**. Slope can in
principle still detect such cases (residual would stay at, say,
`10^-40` regardless of dps, giving slope ≈ 0), but they are
rare/absent in the curated Trans/Log/Alg families.

**The discriminator that did fire is the *PSLQ-acceptance pattern
across dps***. Among the 24 Trans families:

* 20 / 24 produced **no L-bearing relation at any dps** in basis `B`
  — the genuine Trans-hard signature.
* 4 / 24 produced the **same L-bearing relation at every dps**
  (T08, T11, T14, T21) — these are not phantoms, they are exact
  closed forms in `Q(π, 1)` and are reported in §5.

A robust Layer-5 protocol must therefore record both `slope(r,dps)`
*and* `accept_at_each_dps`, with the dichotomy:

| `accept_at_each_dps` | `slope` | Classification |
|---|---|---|
| `[F]*6`            | ≈ −1 | **Trans-hard against B**           |
| `[T]*6`, same rel  | ≈ −1 | **Closed form against B** (transcendental but identifiable) |
| mixed (T at low, F at high) | flatter | **Spurious / phantom** |

---

## 5. PSLQ sweep at dps = 300 (extended basis)

Basis `B' = {L, L², √17, π, log2, ζ(3), e, γ, 1}`,
phantom rule: reject only if `rel[0]=rel[1]=0`.

* **24 Trans families tested.**
* **4 hits** (NOT 0 as the prompt expected — flagged as UNEXPECTED):

| Family | Coeffs `(a2,a1,a0,b1,b0)` | Identified relation | Closed form |
|---|---|---|---|
| T08_130101 | (−2,−1, 1,−3,−3) | `[-2,0, 0,-1,0,0,0,0,-2]` | `L = -(π+2)/2` |
| T11_130117 | (−2,−1, 1, 3, 3) | `[ 2,0, 0,-1,0,0,0,0,-2]` | `L =  (π+2)/2` |
| T14_143931 | (−2, 1, 3,−3,−3) | `[ 4,0, 0, 3,0,0,0,0, 4]` | `L = -(3π+4)/4` |
| T21_143951 | (−2, 1, 3, 3, 3) | `[-4,0, 0, 3,0,0,0,0, 4]` | `L =  (3π+4)/4` |

The four families pair up under `(b1,b0) → -(b1,b0)` sign flips, giving
`L → -L`. All four limits remain Lindemann–Weierstrass-transcendental
because π is, so they are correctly classified as Trans (NOT in the
Log or Alg strata). However, they are **not Trans-hard** in the sense
the prompt anticipated: they reduce to rational + rational·π.

**Conjecture status:** the Trans -2/9 conjecture (every Trans
limit at ratio -2/9, ≈585k convergent families, is transcendental)
is **NOT falsified**: closed forms in `Q(π)` are transcendental.
Only the auxiliary “Trans-hard against {1, √p, π, log2, ζ(3)}”
intuition is weakened — for 4 of 24 reference families.

---

## 6. Recommendation for Output B

**Add T2C as a short Appendix (≤ 1 page) to `trans_minus29_full.pdf`,
not as a Proposition.** Two findings drive this:

1. **Layer-5 protocol clarification:** the slope-of-residual statistic
   is *insufficient* on its own; the manuscript should report
   `(slope, accept_pattern)` jointly. This is a methodological
   refinement rather than a new theorem.
2. **Closed-form sub-family:** 4 of 24 reference Trans families admit
   π-rational identification. This deserves a sentence in the main
   text and a small sub-table in the appendix; it does NOT damage the
   stratum-membership conjecture but does refine the picture of
   internal structure within Trans -2/9.

Suggested LaTeX framing (drop-in paragraph for §5 / Appendix B):

> **Precision Escalation Monitor.** A Layer-5 validation supplements
> the four-layer pipeline of §3. For every candidate Trans limit, we
> compute `L` at `dps ∈ {50,100,150,200,250,300}`, run a PSLQ search
> against `{L, √2, √3, √5, √17, π, log 2, ζ(3), 1}` at each level, and
> record the joint statistic `(m, A)` where `m` is the slope of
> `log_{10}(\,r(d)\,)` versus `d` and `A ∈ \{F,T\}^6` is the
> per-`dps` PSLQ-acceptance vector after phantom-hit rejection. A
> family is declared **Trans-hard** iff `A = F^6`. Across the 24
> reference families of Theorem~\ref{thm:trans-29} this protocol
> isolates 20 families as Trans-hard and identifies the four
> exceptional families
> `(a, b) = ((-2,-1,1),(\pm 3,\pm 3))` and
> `((-2, 1, 3),(\pm 3, \pm 3))` whose limits reduce to
> `L \in \tfrac{1}{2}\,\mathbb{Q}(\pi)` (Appendix~B). All four
> remain transcendental by Lindemann–Weierstrass, so the Trans
> stratum at ratio `-2/9` is unchanged.

Estimated added length: 1 paragraph in §5, ½-page Appendix B with the
4-row identification table. No re-proof of any existing theorem
required.

---

## 7. Files

* `t2c/precision_escalation.py`
* `t2c/precision_escalation_results.json`
* `t2c/precision_escalation.log`
* `t2c/pslq_sweep_300.py`
* `t2c/pslq_sweep_300.json`
* `t2c/pslq_sweep_300.log`
* `t2c/t2c_report.md`  (this file)
* `t2c/claims.jsonl`
