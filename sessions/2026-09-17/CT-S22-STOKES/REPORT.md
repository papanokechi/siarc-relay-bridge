# CT-S22-STOKES — REPORT

Session `CT-S22-STOKES`, `sessions/2026-09-17/CT-S22-STOKES/`.
Staged packet: Stage 0 pre-registration, Stage 1 known-answer control, Stage 2
System C monodromy and Stokes data, Stage 3 vacuity pre-check, Stage 4 leaf
transport, Stage 5 `S_{ζ*}`.

**Outcome in one line.** Stages 0–5 completed; the gap `S16-15` is closed
numerically at the 30-digit threshold with ~60 digits of margin, on **both**
branches of the CT-S16 sign pair; Stage 5's closed-form search returned a
pre-registered **negative** result after its first search space was found
degenerate and void. Nothing was committed.

---

## 1. What was done

### Stage 0 — pre-registration

`PREREG.md` (18,995 B) was written **before any solver code existed**. It fixes
the base point, loop generators and orientation; the branch cut, sector
labelling and the two named Stokes rays `arg z = ±π/2`; the comparison
quantities `x₁, x₂, x₃` with the reason `a₀, a₁` are excluded; the integration
method and step control; the 30-digit threshold; and the Stage-3 vacuity
criterion with the condition that makes it fire.

Two items in it are load-bearing and were settled before any number was seen:

- **The basis and normalisation question.** `e₁` is the formal solution with
  exponential factor `e^{+tz/2}`, `e₂` the one with `e^{−tz/2}`; the residual
  gauge is exactly `G_m = diag(c,1)`, under which `d₁, d₂, d₃` are invariant.
  The comparison quantities are therefore canonical once the eigen-lines are
  labelled, which is why "30 digits" is a meaningful statement at all.
- **The convention is decided by an overdetermined test, not chosen.** §2.3
  declares a finite candidate set and four conditions, requires *exactly one*
  candidate to satisfy all four, and makes zero or two-or-more a HALT.

### Stage 1 — known-answer control on Kummer's equation

`scripts/solver.py` (Taylor-block continuation with continuous `log z`, formal
solution at an irregular rank-1 point, optimal truncation, exact residual) was
smoke-tested on an Euler system against `exp(2πiM)` — `5.07e-59` at dps 60 —
then run against Kummer's equation.

**The falsifier fired on the first run, and three defects were found.** They are
recorded here rather than quietly repaired, and `scripts/stage1_kummer.py` with
`outputs/stage1_kummer.out.txt` is **retained deliberately** as the record.

1. **Kummer's companion system is not trace-free.** `tr B = 1 − b/z`, so
   `det M₀ = e^{−2πib} ≠ 1` and the vdPS `SL₂` factorisation cannot apply.
   Fixed at the setup by the trace-free gauge `Ñ = N − ½tr(N)I`, which moves
   `L` to `diag(b/2−a, a−b/2)` and gives `tr M₀ = 2cos(πb)`, `det M₀ = 1`.
2. **`M_∞` must be the clockwise big circle.** The counterclockwise circle is
   homotopic to `γ₀` itself, so the first run was computing `M₀·M₀`.
3. **Check `A6a` was algebraically vacuous.** For any unimodular `M` with
   `M₁₁ ≠ 0`, `(1+f₁f₂)/α = M₂₂` is a tautology — it could not fail. This is the
   CT-S16 §7 family ("a step that cannot fail cannot be trusted to report
   failure") reappearing in a control written the same morning. Replaced by
   computing the two Stokes matrices **separately** and requiring each to be
   unipotent and triangular in *opposite* triangles — four non-automatic
   conditions each — plus the factorisation identity.

**A fourth item, a mis-derivation, was then found and corrected.** On the second
run 15 of 16 checks passed and `A7` failed by O(1). `A7` had been derived
in-session from vdPS's product shape `diag(α,α⁻¹)·lower·upper`, whereas the
factorisation this solver computes is `e^{2πiL}·S_{2π}(upper)·S_π(lower)` — the
**opposite order**, whose trace is `α(1+f₁f₂) + α⁻¹`, not `α + α⁻¹(1+f₁f₂)`.
The corrected expression was checked by hand against the printed `f₁, f₂` before
the code was touched. This is reported as **a mis-derivation corrected, not a
threshold tuned**: the target `tr = 2cos(πb)` is unchanged and was already
verified at 99 digits, so the corrected `A7` is a **dependent** restatement of
`A4a`+`A5`+`A6e` and is *not* independent evidence. It is retained because an
ordering error of exactly that kind is what it detects.

**Result: 32 of 32 checks pass, 0 fail**, at both pre-registered parameter
values `(a,b) = (1/3, 5/7)` and `(2/5+3i/10, 11/10−i/5)`, at ≥ 35 digits —
individual checks land at 44–151 digits (`outputs/stage1_kummer2_run3.out.txt`).

**A convention consequence carried forward.** Because `M_∞` is the clockwise
loop, vdPS's `α` is `e^{−2πiL₁₁}`, not `e^{+2πiL₁₁}`. This was *not* used to
pick a convention in Stage 2 — both signs were left inside the candidate set and
the §2.3 test decided.

### Stage 2 — System C at `t₀`

The family `(4.1)` of van der Put–Saito p.2655 was built at the CT-S16 point
(branch 1), with `b(z)` in the reading that **carries the `t`**.

- **C-A, the family's own constraints at the point**: `det A₀ = det A₁ = 0`
  *exactly*; `A_∞ = (t/2)diag(−1,1)` to 121 digits.
- `(A₀+A₁)₁₁ = −θ_∞/2`, **not** `θ_∞` — CT-S16's finding about the paper's prose
  reconfirmed at the numeric point, and not relied on anywhere.
- `L₁₁ = θ_∞/2` **exactly**, so `α = e^{iπθ_∞}` in closed form — the C-5
  prediction, confirmed before any monodromy was computed.

**C-0 was rewritten as a rate test.** The original form, `residual < k·e^{−N}`,
only tests the constant `k` and is precisely the sort of threshold that gets
tuned until it passes. It was replaced, before its value was used for anything,
by two checks that can fail: **C-0a** the residual sits at the *minimal term* of
the series (observed ratio 1.29, bound `N³`), and **C-0b** the residual decays at
the predicted Gevrey rate `e^{−|t|R}` between `R = 160` and `R = 140` — observed
`1.028e-11` against a predicted `8.163e-12`, ratio 1.259.

**The §2.3 convention test fired, and caught two further defects.**

4. **A defect in the pre-registration itself.** §2.3's enumeration tied the
   orientation of `γ_∞` to that of the two small loops, so it could not
   represent the relation that actually holds with the base point to the right
   of both punctures — `γ₀γ₁ = γ_∞(ccw)`, i.e. small loops ccw and the big loop
   inverted. No candidate among the 8 could satisfy condition 1 and none did
   (best `‖MMM−I‖ = 6.85`). The set was **widened to 16**. This is a widening of
   the *search*, not a loosening of the *test*: the four conditions and the
   `10⁻³⁰` threshold are unchanged, and uniqueness over the wider set is still
   required. Recorded as a pre-registration shortfall.
5. **A script defect.** The cubic was evaluated with a fixed `x₁ ← M₀`
   labelling regardless of the order flag, so the `"10"` candidates were being
   scored on an inconsistent pairing. `x₁` and `x₂` now follow the order flag,
   as the relation `M₁M₂M_∞ = I` requires.

6. **A reporting error, caught before the report was written.** The `α` branch
   was printed through a `"+"/"-"` flag whose mapping was inverted, so a correct
   `α` was described by the wrong closed form. The branch is now **computed and
   printed**, not labelled.

A further precision shortfall was diagnosed and fixed without touching any
pre-registered quantity. At dps 120, condition 1 reached only `1.5e-25`. The
cause is neither the convention nor the solver: on `|z| = R` the factor
`e^{Λz}` has modulus `e^{±|t|R}` with `|t|R = 204.25`, a one-sided dynamic range
of `10^{88.6}`, and forward integration contaminates the recessive column at
that level. It is inherent to the path and not removable by rescaling. **`R` was
not changed — it is pre-registered — and no threshold was changed.** Only the
working precision was raised, `120 → 200`, which cannot affect the answer.

**Result: exactly one convention passes all four conditions** —
`right | small loops ccw | M_∞ cw | vdPS M₁ = γ₁` — with `‖M₀M₁M_∞ − I‖ =
2.44e-105`, `tr − 2 = 2.1e-190` and `1.3e-190`, `α` and shape at `1.9e-91` and
`5.4e-113`, cubic `1.17e-111`. The other 15 fail, several of them on `α` alone
(`0.327`, `2.27`, `2.34`), so the test discriminates.

**The comparison quantities at `t₀`** (error bar `8.49e-105`, from step halving
`h = ρ/4` vs `ρ/8`, 273 vs 487 steps — **not** from a single run's internal
estimate):

```
x₁ = d₁ = -3.4791908904110720783362611334763347 - 1.0850135702764914087402902784335110 i
x₂ = d₂ =  5.0274753770206575050513601616191382 + 2.3656209874946766465307178962989066 i
x₃ = d₃ =  1.9725752524636335304002661101339216            (imaginary part 4.7e-113)
α  = s₃ =  0.8227296571200546517827584488045268 + 0.5684328555732130672602017927956251 i
f₁      = -3.3348223479737981505682497583139139 + 0.9702273755626692946689592593960931 i
f₂      = -0.0594481783485879912289472592033449 - 0.0730538755916226118669832209758999 i
```

`α = e^{+iπ√3/9} = e^{−iπθ_∞}`; `|α| = 1` and `|arg α| = π√3/9` are the content
of the C-5 prediction, and both are hit. The *sign* of the exponent is the
convention, fixed by the same clockwise `M_∞` that Stage 1's `A7` correction
identified.

**The pre-registered gradient, reported whatever its value.** The fibre through
System C *is* a singular cubic surface — the point sits on two resonance
divisors, `s₁ = s₂ = 2`. But the point itself is a **smooth** point of that
surface: `∇F = (1.523, 1.523, 21.240)` in modulus, `max|∇F| = 21.24`. The
coordinates therefore retain first-order sensitivity, and the risk this was
pre-registered to detect is **absent**.

### Stage 3 — vacuity pre-check

Run **before** Stage 4, as required, and run even though Stage 2's gradient had
already shown it would pass — a falsifier that is only run when it might fire is
not a falsifier.

Perturbing `(q,p)` off the leaf at `δ = 10⁻⁶` and `10⁻⁸`, holding `t` and `θ`
fixed (the perturbed points remain in the `(0,0,1)` family — asserted, since
`det A₀ = det A₁ = 0` hold identically in `(p,q)`):

| direction | `max|Δxᵢ|` at `10⁻⁶` | ratio `(10⁻⁶)/(10⁻⁸)` |
|---|---|---|
| `q` | `8.686e-6` | `99.99978` |
| `p` | `2.639e-5` | `99.99956` |

Both far above the `10⁻¹⁵` floor — ten orders above it and twenty-five above
the threshold — and both ratios textbook first order inside `[50, 200]`.
**PASS.** The observable can see leaf membership; the Stage-4 test is not
vacuous.

### Stage 4 — leaf transport

PV `(4.2)` with `θ₀ = θ₁ = 0` (the middle term of `dp/dt` then vanishes
identically and is dropped, not approximated), transported by Taylor series in
`s = t − t₀` from exact recurrences — no finite differences anywhere —
to `t₁ = t₀ + ε` at `ε = 10⁻³·t₀/|t₀|` and `10⁻⁴·t₀/|t₀|`.

Controls, all assertions that can fail:

- **C-T1** the mpmath and sympy constructions of `A(z)`, which share no code,
  agree to 201 digits.
- **C-T2** the Taylor series satisfies the PV system at `t₁`: residuals
  `2.4e-201` and `8.3e-202`.
- **C-T3** one step of size `ε` agrees with two steps of `ε/2` to 200 digits.
- **C-D, discrimination.** The same transport with a deliberately **wrong**
  vector field (the constant `2θ_∞ − 2` dropped from `dp/dt`) moves the trace
  coordinates by `0.0383`. Without this, a Stage-4 pass could have been a
  transport that barely moved.

| `ε` | worst coordinate agreement |
|---|---|
| `10⁻³` | **90.81 digits** |
| `10⁻⁴` | **91.83 digits** |

**PASS at both, with ~60 digits of margin over the 30-digit threshold.**

**The scope of the pass, stated for citation.** What Stage 4 confirms is that the
linear system built from `(q(t₀), p(t₀))` lies on the PV leaf **as seen by the
trace coordinates `x₁, x₂, x₃`, under the one convention of sixteen that passed
the PREREG §2.3 test** — and that convention is itself a *result of Stage 2*,
obtained by an overdetermined test declared before any number was computed, not
an assumption carried into it. Three further qualifications belong with that
sentence: the observable is `(x₁,x₂,x₃)` and not the full monodromy
representation (`a₀, a₁` are excluded because `s₁ = s₂ ≡ 2`, see §1 Stage 0);
the check is at one point of one branch, along one direction in `t`, at two step
sizes; and the label is VERIFIED, so this is confirmation at a stated precision
and not a proof.

On the scaling: the ratio of the two residuals is `10.43`, i.e. roughly linear
in `ε`. At the time of this run the two contributions could not be separated,
and an earlier draft of this section said both values "sit at the computation's
noise floor". **That was wrong**, and §2.0 item 2 records how it was settled:
the dps-320 rerun left these figures identical while every dps-limited control
improved by ~120 digits, so the residual is systematic, not round-off, and is
floored by the pre-registered `R` rather than by precision. A third `ε`
confirmed linearity over two decades. An earlier draft of the *script* also
asserted the residual does *not* scale with `ε`; that assertion was wrong too
and was corrected before the output became the record.

---

## 2. Claims, each with exactly one label

| id | claim | label |
|---|---|---|
| S22-01 | The solver reproduces Kummer's monodromy, formal and Stokes data against closed forms, 32/32 checks at ≥ 35 digits (44–151 observed), at both pre-registered parameter values. | VERIFIED |
| S22-02 | Kummer's companion system is not trace-free, so the vdPS `SL₂` factorisation requires the trace-free gauge. | STRUCTURAL |
| S22-03 | The ccw circle at ∞ is homotopic to `γ₀`; vdPS's `M_∞` is the **clockwise** loop, hence their `α` is `e^{−2πiL₁₁}`. | STRUCTURAL |
| S22-04 | Check `A6a` as first written was algebraically vacuous: `(1+f₁f₂)/α − M₂₂` equals `(1 − det M)/m₁₁` and vanishes identically for any unimodular `M` with `M₁₁ ≠ 0`. | PROVEN |
| S22-05 | `A7` as first written used vdPS's `diag·lower·upper` ordering (trace `α + (1+f₁f₂)/α`) against a computed `diag·upper·lower` factorisation (trace `α(1+f₁f₂) + 1/α`); the two differ by `(α − α⁻¹)f₁f₂`. The corrected identity is a **dependent** restatement of `A4a`+`A5`+`A6e`. | PROVEN |
| S22-06 | At the CT-S16 point the printed family satisfies `det A₀ = det A₁ = 0` exactly and `A_∞ = (t/2)diag(−1,1)`. | VERIFIED |
| S22-07 | `(A₀+A₁)₁₁ = −θ_∞/2`, contradicting the prose of p.2629. CT-S16's finding, reconfirmed at the numeric point. | VERIFIED |
| S22-08 | `L₁₁ = θ_∞/2` exactly, hence `α = e^{±iπθ_∞}` in closed form with `|α| = 1`, `|arg α| = π√3/9`. | VERIFIED |
| S22-09 | The truncated formal series' residual sits at the minimal term and decays at the Gevrey rate `e^{−|t|R}`. | VERIFIED |
| S22-10 | PREREG §2.3's 8-element candidate set could not represent `γ₀γ₁ = γ_∞`; widened to 16 with the four conditions and the threshold unchanged. | STRUCTURAL |
| S22-11 | Over the 16 candidates, **exactly one** satisfies all four PREREG §2.3 conditions: right action, small loops ccw, `M_∞` clockwise, vdPS `M₁ = γ₁`. | VERIFIED |
| S22-12 | The trace coordinates of System C at `t₀` are the `x₁, x₂, x₃` tabulated above, with error bar `8.49e-105` from step halving. | VERIFIED |
| S22-13 | The point is a **smooth** point of the (singular) cubic fibre: `max|∇F| = 21.24`, non-zero. | VERIFIED |
| S22-14 | The observable is sensitive to leaf membership: `max|Δxᵢ| ≈ 10⁻⁵` at `δ = 10⁻⁶`, first order, ratios `99.9998` and `99.9996`. | VERIFIED |
| S22-15 | System C's point transports along PV with `x₁, x₂, x₃` constant to **90.8 and 91.8 digits** at `ε = 10⁻³, 10⁻⁴`. Gap `S16-15` closed numerically. | VERIFIED |
| S22-16 | The Stage-4 test discriminates: a wrong vector field moves the coordinates by `3.8e-2`. | VERIFIED |
| S22-17 | Raising `dps` 200→320 leaves the Stage-4 agreement and its ratio **unchanged to every printed figure** while every dps-limited control improves by ~120 digits; over `ε = 10⁻³, 10⁻⁴, 10⁻⁵` the ratios are `10.430` and `10.034`. The residual is therefore a systematic `O(ε)` error, not round-off. | VERIFIED |
| S22-18 | Branch 2 of the CT-S16 sign pair (`t = +2√33i/9`) passes Stages 2, 3 and 4 independently: unique convention `right|cw|infccw|01`, agreement `90.82`/`91.84` digits. | VERIFIED |
| S22-19 | Branches 1 and 2 are related by the Galois automorphism `σ: √3 ↦ −√3, √11 ↦ √11` of `Q(√3,√11)`, which maps `t, θ_∞, q, p` term by term; they are **not** complex conjugates. | PROVEN |
| S22-20 | The two branches' trace coordinates are the same multiset with `x₁` and `x₂` **interchanged** and `x₃`, `α` identical; the winning convention is the exact mirror. | VERIFIED |
| S22-21 | The Stage-5A search space was **degenerate**: `Γ(1/6) = 2^{2/3}√3 Γ(1/3)²/(2√π)`, so PSLQ returned that identity with zero coefficient on `log C` and never tested `C`. Stage 5A is VOID, not negative. | PROVEN |
| S22-22 | In the corrected space `{2, 3, π, Γ(1/3)}` — shown independent by a degeneracy pre-check — **no** relation `C = ± 2^a 3^b π^c Γ(1/3)^d e^f` exists with `|coeff| ≤ 10⁶`, `1 ≤ |m| ≤ 12`, cost `≤ 40`, against `C` known to 100 digits. | VERIFIED |

**No label was raised because Stage 4 passed**, as PREREG §9 requires. S22-15 is
VERIFIED — a numerical agreement at a stated precision — and is **not** PROVEN.

### 2.0 The four follow-up items

**Item 4 — scope sentence.** Added to Stage 4 above.

**Item 2 — S22-17, settled, and in the opposite direction from the one
anticipated.** The instruction was: rerun at `dps 320`, and if the residual
still sits at the floor, record the scaling test as *precision-limited rather
than passed*. The rerun (`outputs/stage4_transport_dps320.out.txt`) returned

```
  eps = 1e-3:  agreement 90.8118 digits      <- identical to dps 200
  eps = 1e-4:  agreement 91.8301 digits      <- identical to dps 200
  ratio                    10.429999         <- identical to dps 200
```

while every quantity that *is* dps-limited improved by about 120 digits:

| quantity | dps 200 | dps 320 |
|---|---|---|
| `max|A_sympy − A_mpmath|` | `1.02e-201` | `2.65e-321` |
| `‖M₀M₁M_∞ − I‖` at `t₁` | `1.20e-105` | `5.57e-225` |
| cubic residual at `t₁` | `3.96e-112` | `7.13e-232` |
| `|x₃(t₁) − x₃(t₀)|` | `2.35e-113` | `3.30e-233` |
| PV residual at `t₁` | `2.45e-201` | `1.26e-321` |
| **`α` residual** | **`1.834e-91`** | **`1.834e-91`** |

The one quantity that did not move is the `α` residual — which is exactly the
optimal-truncation floor of the divergent formal solution at `∞`, `e^{−|t|R}`
with `|t|R = 204.25`, i.e. `10^{−88.7}`. It is a property of the
**pre-registered `R`**, not of the arithmetic precision, and no `dps` can
reduce it.

**Two values at a round-off noise floor cannot reproduce to seven significant
figures across a 120-digit change in precision.** These did. The residual is
therefore systematic and deterministic, not round-off.

A third `ε` was then run (`outputs/stage4_transport_eps3.out.txt`) — an
*addition* to PREREG §4's "two values a decade apart", never a relaxation, and
the `≥ 30` digit threshold was applied to all three:

```
  eps = 1e-3: 90.8118   eps = 1e-4: 91.8301   eps = 1e-5: 92.8316
  ratios:  (1e-3)/(1e-4) = 10.430     (1e-4)/(1e-5) = 10.034
```

Linear over two decades, and dps-independent. **The scaling test is recorded as
PASSED, not as precision-limited.** The mechanism is that the truncation error
is a smooth function `E(t)` of the point, so the transported difference is
`|E(t₁) − E(t₀)| ≈ |E′(t₀)|·ε` — `O(ε)` and independent of `dps`, which is what
is observed. That mechanism is stated as the *explanation*; what is claimed as
VERIFIED is the measured dps-independence and the two ratios.

This also corrects a sentence I had written into the Stage-4 verdict: that both
values "sit at the computation's noise floor". That was wrong, and the wording
has been replaced in `stage4_transport.py` with a statement of the observables
plus an explicit instruction that the cross-`dps` comparison is made here, in
the report, rather than asserted inside a single run.

**Item 3 — branch 2 was RUN, not inferred.** The CT-S16 solution is a sign
pair, `t = ∓2√33i/9`. Before running anything, the relation between the branches
was identified and proved (`scripts/branch_relation.py`): the Galois
automorphism `σ` of `Q(√3, √11)` with `σ(√3) = −√3`, `σ(√11) = +√11` (hence
`σ(√33) = −√33`) maps branch 1 to branch 2 term by term in all four of
`t, θ_∞, q, p`, each difference simplifying to exactly `0`. They are **not**
complex conjugates: `conj(q₁) ≠ q₂` and `conj(p₁) ≠ p₂`.

**That symmetry is algebraic, and the monodromy is transcendental in the
matrix entries. `σ` does not act on the analytic continuation.** It therefore
transfers the CT-S16 location argument but carries no information about the
Stokes data, and cannot substitute for a run. Branch 2 was run in full:

| | branch 1 | branch 2 |
|---|---|---|
| `t` | `−2√33i/9` | `+2√33i/9` |
| unique convention (of 16) | `right\|ccw\|infcw\|10` | `right\|cw\|infccw\|01` |
| `x₁` | `−3.47919089041107…−1.08501357028i` | `+5.02747537702066…+2.36562098749i` |
| `x₂` | `+5.02747537702066…+2.36562098749i` | `−3.47919089041107…−1.08501357028i` |
| `x₃` | `1.97257525246363353040…` | `1.97257525246363353040…` (identical) |
| `α` | `0.82272965712005…+0.56843285557i` | identical |
| Stage 3 ratios | `99.9998`, `99.9996` | `99.9952`, `99.9998` |
| Stage 4 agreement | `90.81` / `91.83` digits | `90.82` / `91.84` digits |

Two results worth stating separately.

1. **The winning convention is the exact mirror**, in all three flags: the
   small loops reverse, `M_∞` reverses, and the pairing flag swaps. This is
   what `t → −t` should do to an orientation-dependent Stokes geometry, and it
   is a *result of the branch-2 §2.3 test*, not an assumption carried over.
2. **The trace coordinates are the same multiset with `x₁ ↔ x₂` swapped**, and
   `x₃` and `α` are identical. So the two branches sit at the *same point* of
   the character variety up to the relabelling that the mirrored convention
   induces — which is the geometrically sensible outcome, and is evidence that
   both branches describe one leaf rather than two.

**A defect this exposed.** Stages 3 and 4 originally carried the branch-1
convention as a hard-coded string. Running branch 2 would have applied
`right|ccw|infcw|10` to a geometry where it is wrong. Both scripts now
**re-derive** the convention from the PREREG §2.3 test at their own baseline and
assert uniqueness (`S2.unique_convention`); the hard-coded constant is gone.

**A second defect this exposed.** The `α`-branch report in `stage2_systemC.py`
printed a *correct* `α` with a closed form whose `±√3/9` sign was hard-coded
from branch 1's `θ_∞ = −2 − √3/9`. On branch 2, where `θ_∞ = −2 + √3/9`, it
printed `e^{−iπ√3/9}` for a number whose argument is `+π√3/9`. The number was
right and the description was wrong — the same class as the filename defect and
the `doi`-key defect. Both halves of the string are now computed from
`alpha_pred`, with an assertion that `|arg α_pred| = π√3/9` so the label cannot
be unfounded. Stage 2 was re-run on **both** branches under the corrected code.

**Item 1 — Stage 5 is pre-registered, and has been run.** See §2.2.

### 2.2 Stage 5 — and a pre-registered search space that was itself defective

`PREREG-STAGE5.md` was written before any Stage-5 computation, fixing the
naming prohibition (`K` at `ξ₀`, `S_{ζ*}` at `2ξ₀` — never interchanged), the
trusted precision, the search space, the acceptance criterion, **and what a
negative result would look like**, since "no closed form found" is meaningless
against an unstated space.

Stage 5 does **not** recompute `S_{ζ*}`. A prior fire
(`sessions/2026-05-02/CC-MEDIAN-RESURGENCE-EXECUTE/`, reproduced bit-for-bit at
`sessions/2026-05-13/T2-EXECUTOR-…-VERIFY/`) already did, and those folders are
read-only here. From `S_zeta_star_digits.txt`, in **V_quad native**
normalisation, convention `leading B[Φ]=1`:

```
  C        = 8.127336795495072367112578732023583182264542722338793…
  S_{ζ*}   = 2πiC = 51.0655631399546622698316746099456615679204103033104… i
  ζ*       = 4/√3
```

The two stored copies agree on their first 251 characters. `D_trust` was fixed
at **100 digits** — below the fire's own `108.39` — because inter-window
agreement is a convergence measure, not an error bound.

**The Stage-5A run returned a result that looked like a clean negative and was
actually void.** PSLQ returned, for `C` and for all three decoys alike, the
identical relation

```
   −2·log2 + 3·log3 − 3·log π + 12·log Γ(1/3) − 6·log Γ(1/6) = 0,
```

whose coefficient on `log C` is **zero**. That is Legendre duplication at
`z = 1/6` combined with reflection at `1/3`:

```
   Γ(1/6)Γ(2/3) = 2^{2/3}√π Γ(1/3),   Γ(1/3)Γ(2/3) = 2π/√3
   ⟹  Γ(1/6) = 2^{2/3}√3 Γ(1/3)² / (2√π)        [residual 6.2e-61 at dps 60]
```

So `Γ(1/6)` was never independent of `{2, 3, π, Γ(1/3)}`, the pre-registered
basis was **degenerate**, and the search never tested `C` at all. Its "NOT
FOUND" line excluded nothing and is **withdrawn**.

**The Stage-5A vacuity pre-check did not catch this, and the reason matters.**
It required 3 decoys rejected and 1 control accepted; it got exactly that. But
the decoys were rejected *because PSLQ handed back a `C`-free relation*, not
because the space discriminates. **A check that passes for the wrong reason** —
the recurring defect of this entire run, here occurring inside a pre-check
written specifically to prevent it. The pre-check tested the space against
numbers; it never tested the space against itself.

`PREREG-STAGE5.md` was **not edited**. `PREREG-STAGE5B.md` was written as a
separate pre-registration, as §5 of the first file requires, with:

- `Γ(1/6)` **removed as redundant** — a strictly *smaller* space, so no closed
  form representable in the 5A space is lost, and this is a correction rather
  than the widening that §5 forbids without new pre-registration;
- **all bounds unchanged** (`|coeff| ≤ 10⁶`, `1 ≤ |m| ≤ 12`, cost `≤ 40`,
  `D_trust = 100`) — nothing loosened;
- a **new degeneracy pre-check** (§4.1): PSLQ on the constants with `log C`
  removed must return **no** relation. This is the falsifier 5A lacked;
- a rule that a decoy rejected only via an `m = 0` relation **does not count as
  a rejection** — it counts as a degeneracy and fires.

Stage 5B result (`outputs/stage5b_pslq.out.txt`): degeneracy pre-check **passed**
(no relation among `{2, 3, π, Γ(1/3), 1}` at any bound), all three decoys
rejected **on their own merits** (no relation returned at all), positive control
`C_k = 4π²/(3Γ(1/3))` **recognised** at cost `1.51`. Then:

> **NOT FOUND.** No relation `C = ± 2^a 3^b π^c Γ(1/3)^d e^f` with
> `|coeff| ≤ 10⁶`, `1 ≤ |m| ≤ 12`, digit cost `≤ 40`, against `C` known to 100
> decimal digits. No candidate was returned at any bound.

**This excludes that space. It is not evidence that `C` has no closed form**,
and says nothing about spaces containing other gamma values, other algebraic
irrationalities, polylogarithms, or `ζ(3)`. Label **VERIFIED** — a verified
statement about a search, not about `C`.

**The normalisation caveat, unresolved and load-bearing.** `C` is in V_quad
native normalisation. The `V_quad → P-III(D6)` map is recorded as OPEN in the
2026-05-13 handoff and is **not** closed here. Nothing in Stage 5 may be
compared with the Stage-1–4 quantities of this session, which live in the vdPS
sectorial basis of `PREREG.md` §2.1–§2.2. The basis is fixed on one side only,
and that is stated here rather than discovered later.


### 2.1 Two claims the corpus checker sent back

`check_invariants.py` rejected the first draft of `claims.jsonl` on two counts,
and was right on both.

- **Invariant 1(a): "no PROVEN claim rests on `file_inspection`".** S22-04 and
  S22-05 had been labelled PROVEN with a script and an output file but no proof
  in them. Rather than downgrade the label to fit the check, the proofs were
  supplied: `scripts/algebra_checks.py` establishes both by **simplify-to-zero
  in sympy plus an independent numeric arm**, and the claims now cite it.
  `(1+f₁f₂)/α − m₂₂` simplifies to `(1 − det M)/m₁₁`; the two orderings differ
  by `f₁f₂(α²−1)/α`. The numeric arm is the sharper half: at the Stage-1
  parameter values the wrong ordering misses `2cos(πb)` by **`0.9612`** while
  the corrected one holds to `1.15e-29` — which is the O(1) `A7` failure,
  reproduced exactly and independently of the solver.
- **Invariant 2: "every claim carries exactly one recognised label".** A
  provisional S22-18 carried the label `NOT DONE`. That is a **status, not an
  epistemic label**, and it has no place in the claim corpus. The entry was
  removed at the time, and Stage 5's then-unattempted state was recorded in
  prose instead. The identifier `S22-18` has since been **reused** for the
  branch-2 result, which carries a real label (VERIFIED); Stage 5 was
  subsequently pre-registered and run, and is reported in §2.2.

Final: **22 claims** (S22-01…S22-22; S22-18 reinstated with a real epistemic
label rather than the status word the checker refused). Corpus **448 claims in
23 files**, all five invariants OK.

---

### 2.3 S22-20: the structural route was attempted, and it failed

**Claims S22-23, S22-24. Script `scripts/branch_symmetry.py`, output
`outputs/branch_symmetry.out.txt`.**

Open question 2 asked for a derivation of S22-20 in place of a third run. The
proposed shape was: `σ` maps the branch-1 system to the branch-2 system, and
the construction is equivariant, so the `x₁ ↔ x₂` swap should follow
structurally. The attempt was made and is reported here because it **did not
close**.

**Why `σ` alone cannot be the argument.** `family_polys` is a polynomial in
`(p, q, t, θ_∞)` with *rational* coefficients, so `σ(A₁) = A₂` holds
automatically, entry by entry — it is not extra information. But `σ` is an
automorphism of a number field: it is **not continuous**, so it does not carry
solutions to solutions, and the monodromy entries are transcendental in the
coefficients. `σ` transports the CT-S16 *location* argument and no Stokes data.
To move monodromy one needs an **analytic** map.

**The candidate, and why it was the right one to try.** Both branches carry
their finite singular points at `z = 0` and `z = 1`, and `θ₀ = θ₁ = 0`, so the
two punctures are interchangeable as far as local data is concerned. The
involution `φ(z) = 1 − z` exchanges them and fixes `∞`. Its denominator is
already invariant — `D(1 − z) = (1 − z)(−z) = z² − z = D(z)`, exactly zero
(**S22-23, PROVEN**). An orientation-reversing puncture swap is precisely what
would produce `x₁ ↔ x₂` with `x₃` and `α` fixed, and precisely what would
mirror `right|ccw|infcw|10` into `right|cw|infccw|01`.

**The test is exact and needs no solver.** `A` is **traceless**, so its only
gauge invariant is `det A = −(a² + bc)/D²`. A constant gauge `G` with
`A₂(z) = −G A₁(1−z) G⁻¹` therefore *forces* the scalar identity

```
P₂(z) = P₁(1−z),        P(z) := a(z)² + b(z)c(z).
```

That is a necessary condition, testable symbolically. **It fails**, as do three
neighbouring candidates (**S22-24, PROVEN**):

| candidate `φ` | `max |coeff|` of `P₂ − P₁∘φ` |
|---|---|
| identity | `3.83454` |
| `z ↦ 1 − z` | `0.415740` |
| coefficient conjugation | `0.415740` |
| conjugation ∘ `z ↦ 1 − z` | `3.83454` |

Zero candidates pass. **No constant-gauge analytic equivalence exists.**

**The positive control is what makes this a result rather than a null.** Four
"nonzero" verdicts are exactly what a comparison pipeline returns when
`simplify` cannot zero nested radicals — the negative would then be void in the
same way Stage 5A was. So the script tests, *first*, a known-true identity of
the same radical complexity: `σ(P₁) − P₂`, which `branch_relation.py` proves is
identically zero. It returns `max |coeff| = 0` **exactly**, and the run is
gated on that assert. The negatives are therefore informative.

**That control immediately caught a defect in this script.** Its first version
implemented `σ` as `subs(sqrt(3), -sqrt(3))`. Sympy stores `sqrt(33)` as an
*atom*, so that substitution never touched it, and the map applied was not `σ`.
The control failed with `max |coeff| ≈ 1.3e5` — far too large to be a
simplification artefact — and the script halted instead of printing four
negatives obtained under a wrong control. The fix reuses `branch_relation.py`'s
`σ` verbatim, which routes `√33` through `A·B` first. **A control written to
validate the test caught an error in the test's own machinery**; without it the
run would have reported the same four negatives with no idea whether they meant
anything.

**Disposition.** The pre-declared falsifier fired, so the script stops rather
than searching further candidate maps — the space of maps is not pre-registered
and enlarging it after seeing a failure is the move this session has refused
twice already. `S22-20` **remains VERIFIED-numerical**. What is now excluded is
the constant-gauge route; a `z`-dependent gauge is untested and is recorded as
open question 2.

---

## 3. What was NOT established

- **`S_{ζ*}` was not recomputed, and no closed form was found.** Stage 5 read
  the stored value from the 2026-05-02 fire and searched a pre-registered
  space; the result is a **negative** one (S22-22), reported with the same
  prominence as a positive one. It excludes that space and nothing more.
- **The `V_quad → P-III(D6)` normalisation map remains OPEN.** `C` is in V_quad
  native normalisation. Nothing in Stage 5 is comparable with the Stage-1–4
  quantities of this session, which live in the vdPS sectorial basis. The basis
  is fixed on one side only.
- **The naming prohibition held.** `K` is the amplitude at `ξ₀`; `S_{ζ*}` is at
  the action difference `2ξ₀`. `K` was not computed, not fitted, and not used
  as a name for `S_{ζ*}` at any point, in code, output or prose.
- **No proof.** Stage 4 is a numerical isomonodromy check at one point, along
  one direction in `t`, at two step sizes. It is evidence that the constructed
  linear system lies on the PV leaf through `(q(t₀), p(t₀))`; it is not a proof
  of membership, and a failure would have falsified *this construction*, not
  membership in general.
- **No global statement about the leaf.** Transport was to `t₀ + ε` for small
  `ε` only. Nothing is claimed about the leaf away from a neighbourhood of `t₀`,
  or about monodromy of the PV solution itself. Both branches of the CT-S16
  sign pair have now been run, but each only near its own `t₀`.
- **The residual floor is not removable by precision.** It is set by the
  pre-registered `R` through `e^{−|t|R}`. Lowering it would require changing
  `R`, which is pre-registered and was not changed to buy accuracy.
- **The vdPS prose/formula contradiction is reconfirmed, not resolved.** The
  paper says `θ_∞ = (A₀+A₁)₁₁`; the printed family gives `−θ_∞/2`. This session
  computed everything from the matrix `A(z)` and never used the prose.
- **The `b(z)` typo is still a reading, not a correction by the authors.** The
  reading that carries the `t` is corroborated by `B₁` on the same page and by
  `det A(1) = −θ₁²/4`, and is the one used throughout. It remains an adopted
  reading of a self-contradictory page.

---

## 4. Open questions for the operator

All four follow-up items are **closed**; what remains are new questions they
opened.

1. **The residual floor is `R`-limited, and `R` is pre-registered.** S22-17 is
   settled: the residual is systematic, not round-off. But it is floored at
   `e^{−|t|R} ≈ 10^{−88.7}`, and the only way past that is a larger `R` —
   which changes a pre-registered quantity. If more than ~91 digits is ever
   wanted from this pipeline, that needs a *new* pre-registration fixing `R`,
   not an adjustment of this one.
2. **The two branches give one point, and the simplest structural argument for
   it is now REFUTED.** S22-20 is an observation from two runs: `x₁ ↔ x₂`,
   `x₃` and `α` identical, conventions mirrored. The natural derivation —
   pull back along `φ(z) = 1 − z`, which exchanges the punctures `0` and `1`
   and fixes `∞` — was tested in §2.3 and **fails**: the necessary determinant
   condition `P₂(z) = P₁(φ(z))` is nonzero for `φ` and for three neighbouring
   candidates. So no *constant*-gauge equivalence exists. What remains open is
   a **`z`-dependent** gauge, which this session did not test and which is a
   materially harder object. Until then S22-20 stays **VERIFIED-numerical**,
   and the report says so rather than leaning on the Galois relation, which
   (S22-19) carries location and not monodromy.
3. **Stage 5's negative result is only as interesting as its space.** S22-22
   excludes `{2, 3, π, Γ(1/3)}` at cost ≤ 40. The natural next spaces — adding
   `Γ(1/4)`/`Γ(1/12)`, or algebraic numbers of degree > 1 over `Q(√3)`, or
   `ζ(3)` and polylogarithms — each need their own pre-registration, and each
   needs its own degeneracy pre-check, since the gamma values are riddled with
   multiplicative relations. That is the lesson of S22-21 and it will recur.
4. **The `V_quad → P-III(D6)` normalisation map is now load-bearing.** It was
   an open residual before; Stage 5 makes it the thing that stops the stored
   `S_{ζ*}` from being comparable with anything computed in this session.
5. **The pre-registration shortfalls are now two of a kind (S22-10, S22-21).**
   Both were candidate/basis sets enumerated from a mental picture rather than
   derived — the loops from a picture instead of the relation in `π₁`, the
   constants from a list instead of a check for independence. The repair in
   both cases was the same: widen or correct the *search*, never the *test*,
   and add the falsifier that was missing. Deriving the set from the structure
   in the first place is the cheaper fix, and is the item worth carrying.

---

## 5. Uncommitted files

Nothing was committed, pushed, tagged, deposited or sent. All of the following
are uncommitted, under `sessions/2026-09-17/CT-S22-STOKES/`:

```
PREREG.md
PREREG-STAGE5.md                           (retained: the VOID search, §2.2)
PREREG-STAGE5B.md                          (the corrected search space)
P0-AMENDMENT.md                            (PROPOSED: basis degeneracy pre-check)
REPORT.md                                  (this file)
claims.jsonl
scripts/solver.py
scripts/test_solver.py
scripts/locate_traces.py
scripts/render_pages.py
scripts/stage1_kummer.py                   (retained: the record of a falsifier firing)
scripts/stage1_kummer2.py
scripts/stage2_systemC.py
scripts/stage3_vacuity.py
scripts/stage4_transport.py
scripts/branch_relation.py
scripts/branch_symmetry.py                 (§2.3: the refuted structural route)
scripts/gamma16_identity.py
scripts/stage5_pslq.py                     (retained: the degenerate-space run)
scripts/stage5b_pslq.py
scripts/algebra_checks.py
scripts/emit_claims.py
outputs/test_solver.out.txt
outputs/locate_traces.out.txt
outputs/render_pages.out.txt
outputs/stage1_kummer.out.txt              (retained)
outputs/stage1_kummer2.out.txt             (retained: 15/16, A7 failing)
outputs/stage1_kummer2_run3.out.txt        (32/32)
outputs/stage2_systemC_run1.out.txt        (retained: the 2.3 test firing, 0 of 8)
outputs/stage2_systemC_run2.out.txt        (retained: 0 of 16 at dps 120)
outputs/stage2_systemC.out.txt             (1 of 16, unique; branch 1)
outputs/stage2_systemC_b2.out.txt          (1 of 16, unique; branch 2, mirrored)
outputs/stage3_vacuity.out.txt
outputs/stage3_vacuity_b2.out.txt
outputs/stage4_transport.out.txt
outputs/stage4_transport_b2.out.txt        (branch 2)
outputs/stage4_transport_dps320.out.txt    (settles S22-17)
outputs/stage4_transport_eps3.out.txt      (three eps, two decades)
outputs/branch_relation.out.txt
outputs/branch_symmetry.out.txt            (0 of 4 candidates; control at 0)
outputs/gamma16_identity.out.txt
outputs/stage5_pslq.out.txt                (retained: the VOID run)
outputs/stage5b_pslq.out.txt               (the NOT FOUND result)
outputs/algebra_checks.out.txt
pages/vdps_p2629.png
pages/vdps_p2630.png
pages/vdps_p2631.png
refs/vdPS-arXiv-0902.1702v5.pdf            (copied from CT-S16, sha256 1d4be8e4…)
```
