# Results on the leaf verification

*Statements and numerical results.*

---

## Results

| # | statement |
|---|---|
| 1 | The solver reproduces Kummer's monodromy, formal and Stokes data against closed forms, 32/32 checks at ≥ 35 digits (44–151 observed), at both pre-registered parameter values. |
| 2 | Kummer's companion system is not trace-free, so the vdPS `SL₂` factorisation requires the trace-free gauge. |
| 3 | The ccw circle at ∞ is homotopic to `γ₀`; vdPS's `M_∞` is the **clockwise** loop, hence their `α` is `e^{−2πiL₁₁}`. |
| 4 | Check `A6a` as first written was algebraically vacuous: `(1+f₁f₂)/α − M₂₂` equals `(1 − det M)/m₁₁` and vanishes identically for any unimodular `M` with `M₁₁ ≠ 0`. |
| 5 | `A7` as first written used vdPS's `diag·lower·upper` ordering against a computed `diag·upper·lower` factorisation; the two differ by `(α − α⁻¹)f₁f₂`. The corrected identity is a dependent restatement of `A4a`+`A5`+`A6e`. |
| 6 | At the CT-S16 point the printed family satisfies `det A₀ = det A₁ = 0` exactly and `A_∞ = (t/2)diag(−1,1)`. |
| 7 | `(A₀+A₁)₁₁ = −θ_∞/2`, contradicting the prose of p. 2629. |
| 8 | `L₁₁ = θ_∞/2` exactly, hence `α = e^{±iπθ_∞}` in closed form with `|α| = 1`, `|arg α| = π√3/9`. |
| 9 | The truncated formal series' residual sits at the minimal term and decays at the Gevrey rate `e^{−|t|R}`. |
| 10 | PREREG §2.3's 8-element candidate set could not represent `γ₀γ₁ = γ_∞`; widened to 16 with the four conditions and the threshold unchanged. |
| 11 | Over the 16 candidates, exactly one satisfies all four PREREG §2.3 conditions: right action, small loops ccw, `M_∞` clockwise, vdPS `M₁ = γ₁`. |
| 12 | The trace coordinates of System C at `t₀` are `x₁, x₂, x₃` as tabulated, with error bar `8.49e-105` from step halving. |
| 13 | The point is a smooth point of the singular cubic fibre: `max|∇F| = 21.24`, non-zero. |
| 14 | The observable is sensitive to leaf membership: `max|Δx_i| ≈ 10⁻⁵` at `δ = 10⁻⁶`, first order, ratios `99.9998` and `99.9996`. |
| 15 | System C's point transports along PV with `x₁, x₂, x₃` constant to 90.8 and 91.8 digits at `ε = 10⁻³, 10⁻⁴`. Gap `S16-15` closed numerically. |
| 16 | The Stage-4 test discriminates: a wrong vector field moves the coordinates by `3.8e-2`. |
| 17 | Raising `dps` 200→320 leaves the agreement and its ratio unchanged to every printed figure while every dps-limited control improves by ~120 digits; over `ε = 10⁻³, 10⁻⁴, 10⁻⁵` the ratios are `10.430` and `10.034`. |
| 18 | Branch 2 of the CT-S16 sign pair (`t = +2√33i/9`) passes Stages 2, 3 and 4 independently: unique convention `right\|cw\|infccw\|01`, agreement `90.82`/`91.84` digits. |
| 19 | Branches 1 and 2 are related by the Galois automorphism `σ: √3 ↦ −√3, √11 ↦ √11` of `Q(√3,√11)`, which maps `t, θ_∞, q, p` term by term; they are not complex conjugates. |
| 20 | The two branches' trace coordinates are the same multiset with `x₁` and `x₂` interchanged and `x₃`, `α` identical; the winning convention is the exact mirror. |
| 21 | The Stage-5A search space was degenerate: `Γ(1/6) = 2^{2/3}√3 Γ(1/3)²/(2√π)`, so PSLQ returned that identity with zero coefficient on `log C` and never tested `C`. Stage 5A is VOID, not negative. |
| 22 | In the corrected space `{2, 3, π, Γ(1/3)}` — shown independent by a degeneracy pre-check — no relation `C = ± 2^a 3^b π^c Γ(1/3)^d e^f` exists with `|coeff| ≤ 10⁶`, `1 ≤ |m| ≤ 12`, cost `≤ 40`, against `C` known to 100 digits. |

## Numerical values

```
x₁ = -3.4791908904110720783362611334763347 - 1.0850135702764914087402902784335110 i
x₂ =  5.0274753770206575050513601616191382 + 2.3656209874946766465307178962989066 i
x₃ =  1.9725752524636335304002661101339216
α  =  0.8227296571200546517827584488045268 + 0.5684328555732130672602017927956251 i
```

```
C      = 8.127336795495072367112578732023583182264542722338793…
S_{ζ*} = 2πiC = 51.0655631399546622698316746099456615679204103033104… i
ζ*     = 4/√3
```

## Conclusion

The gap `S16-15` is closed numerically at the 30-digit threshold with ~60 digits
of margin, on both branches of the CT-S16 sign pair. Stage 5's closed-form
search returned a pre-registered negative result after its first search space was
found degenerate and void.
