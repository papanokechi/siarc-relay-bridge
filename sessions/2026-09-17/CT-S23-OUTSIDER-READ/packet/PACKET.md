# Membership of a quadratic-recurrence connection in a Painlevé V isomonodromic family

*Assembled mathematical content. Statements, definitions, proofs and numerical
results only.*

Page images supplied with this document:

- `pages/vdps_p2634.png`, `p2635.png`, `p2636.png`, `p2637.png`
  (van der Put & Saito, *Moduli spaces for linear differential equations and the
  Painlevé equations*, Ann. Inst. Fourier **59** (2009) no. 7, 2611–2667),
  including **Table 2.1** on p. 2635.
- `pages/jimbo_p1152.png`.

---

## 1. The sequence and its growth

Let `b(n) = Σ_{k=0}^{d} β_k n^k` be a polynomial of degree `d ≥ 1` with
`b(k) ≠ 0` for all `k ≥ 1`, and define

    Q_n = b(n) Q_{n-1} + Q_{n-2},     Q_{-1} = 0,  Q_0 = 1.

Write `r_n = Q_n / ∏_{k=1}^{n} b(k)`.

**Proposition 1.** `r_n` converges for every such `b`, with no hypothesis on the
limit, and `r_∞ − r_n = O(n^{−(2d−1)})`.

**Proposition 2.** If `b(n) > 0` for all `n ≥ 1` then `r_n` is strictly
increasing with `r_n ≥ 1`; hence `r_∞ ≥ 1 > 0`.

Write `r_1, …, r_d` for the roots of `b`. Assume

- **(A1)** the roots are distinct and none is a non-negative integer;
- **(A3)** `r_∞ := lim_n Q_n / ∏_{k=1}^{n} b(k)` exists and is **nonzero**.

**Proposition 3.** Under (A1) and (A3),

    Q_n = r_∞ · β_d^n · [ ∏_i Γ(n+1−r_i) / Γ(1−r_i) ] · (1 + o(1)),

and consequently

    Q_n / Γ(dn+1) ~ K · (β_d/d^d)^n · n^s,
      s = β_{d−1}/β_d + (d−1)/2,
      K = r_∞ · (2π)^{(d−1)/2} · d^{−1/2} / ∏_{i=1}^{d} Γ(1 − r_i).

The step to the asymptotic form uses `r_∞ − r_n = O(1/n)`, which Proposition 1
supplies for every `d ≥ 1`.

**Proposition 4.** Under (A1) and (A3),
`lim |Q_n/(dn)!|^{1/n} = |β_d|/d^d`. Hence `Σ Q_n w^n/(dn)!` has radius
`d^d/|β_d|` in `w`, i.e.

    ξ₀ = d / |β_d|^{1/d}     in the variable ζ = w^{1/d}.

This is proved without Gamma asymptotics. At `d = 2` it returns `ξ₀ = 2/√β₂`.

**The candidate Borel-plane exponent** is `ρ_d = −s − 1 = −(d+1)/2 −
β_{d−1}/β_d`. At `d = 2` this is `−3/2 − β₁/β₂`.

### 1.1 Numerical confirmation of `s` at `d = 4`

Computed with mpmath at dps ≥ 60, `n` up to 20000, `Q_n` renormalised at each
step with `log|Q_n|` tracked, fitted as
`log c_n = s log n + C + a₁/n + a₂/n² + …` through at least three Richardson
levels.

Eight quartic representatives were used, six of them with sign-changing `b`.
All eight have `r_∞ ≠ 0`, in the range `0.9241–1.0795`, with `N/2`-vs-`N`
agreement of 28.8–30.5 digits.

The measured `s` matched `β_{d−1}/β_d + (d−1)/2` for all eight. A vacuity
pre-check was run in both directions: varying `β_0 … β_{d−2}` with `β_d, β_{d−1}`
held fixed left `s` unmoved within fit error, and varying `β_{d−1}` moved `s` as
predicted.

### 1.2 The case of interest

For the polynomial with `β₂ = 3, β₁ = 1` (`d = 2`):

    ξ₀ = 2/√3 = 1.15470053837925152901829756100391491129520350254025…
    r_∞ = 1.0166044410585109363370972132676576869179835143890…

`r_∞` is confirmed to 2317.8 digits by agreement between two independent
extrapolations. A PSLQ probe over the basis
`{r_∞, 1, π, √3, Γ(1/3), Γ(2/3), log 2, log 3, |Γ(1−r₁)|, …}` returned **no
relation**; `r_∞` is a numerically-known constant only.

### 1.3 Two constants that must not be conflated

For this object there are two formal solutions with actions `c_± = ±2/√β₂`.

    ξ₀ = |c_±|        = 2/√3        (the action of a single formal solution)
    ζ* = |c₊ − c₋|    = 2ξ₀ = 4/√3  (the action difference)

These are **different objects**, not the same singularity in different
variables. `ξ₀` is a characteristic root, obtained from the Newton polygon; it
is not defined as a Borel radius. Any germ coefficient extracted from `K` is
stated against `ξ₀` and must not be attached to `ζ*`.

The amplitude at `ξ₀` is `A = K·Γ(s+1)`, with exponent `−(s+1) = ρ_d`.

**Naming prohibition, used throughout.** `K` is the amplitude at `ξ₀ = 2/√3`.
`S_{ζ*}` is the Stokes constant at the action difference `ζ* = 2ξ₀ = 4/√3`.
They are a factor of 2 apart in the action and neither name is ever used for the
other.

---

## 2. Three objects, two equivalence classes

Three distinct objects have been referred to under one name. They have different
formal types.

| Object | Description | Katz multiset | Table 2.1 row |
|---|---|---|---|
| **A** | the series `Σ Qₙ zⁿ` | `(1/2, −, 1/2)` | PIII(D₈); quadratic cover in the PIII(D₆) row |
| **B** | `L_φ` | `(0,0,1)` | PV / `D̃₅` |
| **C** | the ODE of §3 | `(0,0,1)` | PV / `D̃₅` |

**Proposition 5.** `B` and `C` are projectively equivalent under `z ↦ 1/x`:
their trace-free normal forms are identically equal. Writing the scalar equation
as `A W'' + A′ W' + C W = 0` with `A = 3x²+x+1`, both normal potentials are

    r(x) = (12x⁴ + 4x³ + 4x² + 11) / (4(3x²+x+1)²),

and the inversion carries `B`'s singular points `(−1 ± i√11)/2` exactly onto
`C`'s `(−1 ± i√11)/6`. They are **not the same operator**: their printed forms
differ by the rank-1 twist `A^{−1/2}`, which alters the trace by `−dlog A ≠ 0`.
`B`'s row is read from its trace-free normal form, which inversion alone
reaches.

So the three names label **two** classes: `A`, and the class `{B, C}`.

### 2.1 Seven conditions on any use of Table 2.1

1. **All row matches are necessary conditions only.** Table 2.1 is captioned
   *"Classification of Families"* and p. 2634 sets it up for *"a local family
   `M(u)` of differential modules, represented by a matrix equation `d/dz +
   A(z,u)` where `A(z,u)` is a 2×2-matrix with trace 0"*. It classifies families
   of rank-2 trace-free connections, not individual scalar operators.
2. The PIII(D₆) match for `A`'s cover is at **special** parameters.
3. The `D̃₅` label belongs, at most, to `B` and `C`.
4. The provenance of any earlier PIII(D₆) label is not established here.
5. **`A`'s row is one of exactly two exceptional rows.** On p. 2634, immediately
   before the table:

   > "For a differential module `M` corresponding to one of the types, the
   > strong Hilbert-Riemann problem has a positive answer, **except possibly for
   > `(1/2, −, 1/2)` and `(−, −, 5/2)`** […] For these two types we only consider
   > the modules `M(u)` for which the strong Riemann–Hilbert problem does have a
   > positive answer."

   `(1/2, −, 1/2)` is `A`'s type. The row is restricted to modules satisfying an
   additional condition, which has not been checked for `A`.
6. There is an unbridged scalar-to-connection gap for `A`.
7. **`dim P = 0` for the PIII(D₈) row** means the family has no free parameters
   in the authors' sense. On p. 2634 `P` is *"a space of parameters `P` […]
   consisting of traces or eigenvalues of the matrices involved in the
   construction of `R`"*, and on p. 2635 *"`R → P` is a family of affine cubic
   surfaces"* — so `P` is the base of a cubic-surface fibration on the monodromy
   side. Immediately after the table the source writes: *"We will also describe
   the corresponding **one-dimensional families of differential modules
   `M(t)`**."* The table's `r(t)` column is a Katz-invariant column for a
   singular point named `t`, present only when the singular set contains one.
   The letter `t` therefore does two different jobs on that page.

---

## 3. System C

Set

    s_± = (−1 ± i√11)/6,     δ = −i√11/3,     x(z) = s_₊ + δz.

**System C** is the scalar equation `y'' + P_C y' + Q_C y = 0` with

    P_C = δ(6x + 1)/(3x² + x + 1),
    Q_C = δ²(−x²)/(3x² + x + 1).

Its normal potential is the `r(x)` of Proposition 5. Under `x = s_₊ + δz` the
poles are **only** at `z = 0, 1`, both double with coefficient `−1/4`, and there
is **no apparent singularity**. At infinity

    r_z = −11/27 + (i√11/27)/z + …

---

## 4. The moduli space

For a type-`(0,0,1)` module the strong Riemann–Hilbert problem has a positive
answer (§3.2, p. 2637). The module is

    d/dz + A₀/z + A₁/(z−1) + A_∞,

with `A₀, A₁` trace-zero constant matrices, `A_∞ = (t/2)·diag(−1,1)`, `t ∈ C*`,
`det A_i = −θ_i²/4`, and singular points normalised to `0, 1, ∞`.

**No semisimplicity hypothesis and no non-resonance hypothesis appear.** p. 2636
defines resonance as an eigenvalue difference in `Z∖{0}`, and treats resonance
and reducibility as sources of *singularities of the monodromy space*: such
modules are inside the space, not excluded from it.

The explicit family `(4.1)` of p. 2655 is, with `D(z) = z(z−1)` and
`A = [[a, b], [c, −a]]`:

    a = p + ½(−2qt + t − θ_∞)(z − q) − ½ t (z − q)²

    b = −( z·( (p + ½(q−1)q t)² − θ₁²/4
             + (q−1)(θ₀²/4 − θ₁²/4 − q θ_∞²/4) ) )/q
        − ( (q−1)(p + ½((q−1)q t − θ₀ + q θ_∞))
                 (p + ½((q−1)q t + θ₀ + q θ_∞)) )/q

    c = −(z − q)/(q − 1)

with the system `y' = N y`, `N = −A/D`.

**A typo in the printed source.** On p. 2655 the first square in `b(z)` prints
`(p + ½(q−1)q)²`, with no `t`, while the second term carries `(q−1)q t`. Tested
against the source's own constraint `det A(1) = −θ₁²/4`:

| reading | `det A(0) = −θ₀²/4` | `det A(1) = −θ₁²/4` |
|---|---|---|
| as printed | holds | **nonzero remainder** |
| `(p + ½(q−1)q t)²` | holds | **holds identically** |

`det A(0)` does not discriminate; `det A(1)` does. The corrected reading is used
throughout.

Separately, the prose statement that `θ_∞` is the `(1,1)` entry of `A₀+A₁` does
not hold for the printed family: the entry is `−θ_∞/2`. Nothing below relies on
it.

The chart is `U₀ ≅ C × (C∖{0,1})`, coordinates `(p, q)` with `q ∉ {0,1}`. On
`U₀ × (C∖{0})` the foliation given by the 2-form

    Ω = dp∧dq/(q(q−1)) − dH_V ∧ dt

coincides with the foliation given by isomonodromy (p. 2656), with flow `(4.4)`
and Hamiltonian `H_V` `(4.5)`.

---

## 5. Membership of System C

### 5.1 The time invariant

Under `x = s_₊ + δz`, System C's expansion at infinity gives `t²/4 = −11/27`,
hence

    t = ∓ 2i√33/9.

This is the time invariant of the framework — the scale of the irregular type at
`∞` — computed from the configuration.

### 5.2 Local data

A probe on three exact draws fixes the dictionary: the double-pole coefficients
are `(θ₀²−1)/4` and `(θ₁²−1)/4`, and `R(∞) = t²/4` (3 of 3 each). The naive
`1/z` entry `tθ_∞/2` **failed all three draws**; the data give `t(θ_∞+1)/2`.
Those draws double as the vacuity control, since they carry `θ₀ ≠ 0` and the
observable reports it.

Hence `θ₀ = θ₁ = 0`, so `A₀, A₁` are nilpotent and nonzero — non-semisimple
local data, with a log term. The eigenvalue difference is `0 ∉ Z∖{0}`, so this is
not resonance in the source's sense; and §3.2 imposes no semisimplicity
condition in any case.

### 5.3 Irreducibility

Riccati test `w' + w² = r`, exactly. All poles are simple; the residues at `s_±`
satisfy `A² − A = −1/4`, so `A = 1/2`; `w` is bounded at `∞` with `c₀² = 1/3`;
matching `r₁ = −1/9` forces `n = −1 ∓ √3/18`, irrational, hence not a
non-negative integer. Contradiction. **System C is irreducible**, and does not
sit on the classical Riccati locus.

### 5.4 The point

The overdetermined solve — five coefficient equations plus `b₁ = 0` in four
unknowns — is **consistent**, with two branches:

| | `t` | `θ_∞` | `q` | `p` |
|---|---|---|---|---|
| 1 | `−2i√33/9` | `−2 − √3/9` | `≈ 0.5 + 0.8123 i` | `≈ 0.4649 i` |
| 2 | `+2i√33/9` | `−2 + √3/9` | `≈ 0.5 − 25.6278 i` | `≈ 396.2089 i` |

Exactly, on branch 1:

    p   = 5i(−28151758571√33 + 48874838016√11)/4086468672
    q   = 1/2 + (−457937√11 i + 281700√33 i)/122408
    t   = −2√33 i/9
    θ_∞ = −2 − √3/9,   θ₀ = θ₁ = 0

Verified by re-substitution into the **general** formula for the normal
potential, not the reduced closed form used to derive it: the difference
simplifies to `0` identically, with worst relative residual over five points at
dps 60 of `5.8e-56` and `7.0e-61`. `b₁ = 0`, and `q ∉ {0,1}`, so the point lies
in `U₀`.

`θ_∞ = −2 ∓ √3/9`, not the `−1 ∓ √3/9` the generic dictionary predicts: the
`t(θ_∞+1)/2` entry was derived for non-constant `b`, and the `b′/b` term shifts
the behaviour at `∞` by one when `b₁ = 0`. The double-pole entries at `z = 0, 1`
are untouched, since `b`'s zero lies elsewhere, so `θ₀ = θ₁ = 0` stands.

### 5.5 Consequence

All hypotheses are satisfied; the point lies in `U₀`; `q(q−1) ≠ 0` and `t ≠ 0`
there, so the vector field `(4.4)` is regular at it and **exactly one leaf passes
through**. Since Painlevé V is the isomonodromy foliation on that space, System C
lies on a PV isomonodromic leaf.

---

## 6. The normalisation is exact, not projective

The matching of §5 is of *normal potentials*, which is blind to a rank-1 twist.
The following removes that caveat.

**Proposition 6.** A rank-1 twist acts by `A ↦ A + λI` and changes the trace by
`2λ`, so `tr(A + λI) = 0` has the unique solution `λ = −tr(A)/2`: within the
orbit of one connection under rank-1 twists, the trace-free member is unique.

**Proposition 7 (a converse fails).** Trace-freeness alone does **not** single
out a representative of a projective class. Take `L = d − 1/(2z)` over `C(z)`:

| | | |
|---|---|---|
| `L ⊗ L = d − 1/z` | **trivial** | witness `w = z`, and `2f + w′/w = 0` exactly |
| `L` itself | **non-trivial** | the residue of `f` at `0` is `−1/2 ∉ Z`, so `f` is not the logarithmic derivative of a rational function |

So a non-trivial 2-torsion rank-1 module exists. Tensoring a trace-free module by
it preserves both the projective class and triviality of the determinant. Hence a
projective class can contain more than one trace-free module up to isomorphism.

**Proposition 8 (the decisive comparison).** A second-order operator is
determined by the **pair** `(P, Q)` in `∂² + P∂ + Q`. The normal potential
`R = P²/4 + P′/2 − Q` is blind to a rank-1 twist; the pair is not.

| | `P` | `Q` |
|---|---|---|
| System C in `z` | `(2z−1)/(z(z−1))` | `(22z²−22z−2i√11 z+5+i√11)/(54z(z−1))` |
| family at `(p,q,t,θ_∞)` | identical | identical |

Both differences vanish identically, with worst relative residual `0` over five
points at dps 60. **The two differential modules are isomorphic** — not merely
projectively isomorphic.

Two vacuity controls, both assertions: perturbing `q` by `10⁻³` makes the
comparison report a non-zero difference, so the test can reject a wrong point;
and an operator with the **same `R` but different `P`** is separated by the
`(P,Q)` test and not by `R`.

**Why it works out.** `3x² + x + 1 = 3(x−s₊)(x−s₋) = 3δ²·z(z−1) = 3δ²D`, so
System C's own Wronskian coefficient is `P_C = δ(6x+1)/(3x²+x+1) = D′/D`; the
family's is `P = D′/D − b′/b`, equal to `D′/D` exactly when `b` is constant, i.e.
when `b₁ = 0` — the condition the match already forced. The two objects carry the
same rank-1 twist.

**Open.** Since trace-freeness alone is insufficient, what is the correct sharper
hypothesis under which a projective class has a unique representative in the
normalised form? A 2-torsion twist shifts local exponents by `½`, but individual
local exponents depend on the lattice, so whether the normalisation "local
exponents `±θ_i/2`" excludes such twists needs an argument not given here. The
membership result does not depend on it.

---

## 7. Which scalar reduction

A rank-2 first-order system `Y' = N Y` does not determine a single scalar
second-order ODE. Eliminating either component gives

    P_b = −(n₁₁+n₂₂) − n₁₂′/n₁₂,      P_c = −(n₁₁+n₂₂) − n₂₁′/n₂₁,
    P_b − P_c = d/dz log(n₂₁/n₁₂),

exactly; and under the common denominator of §4 this is `d/dz log(c/b)`.
The route difference `d/dz log(n₂₁/n₁₂)` is convention-free; identifying
`n₂₁/n₁₂` with `c/b` uses the fact that §4 divides *both* off-diagonal entries by
the same `D`. The orientation is **b-route minus c-route**.

At the point of §5.4, over `Q(i,√3,√11)`:

| difference | exact | numeric, dps 40 |
|---|---|---|
| `P_b − P_C` | 0 | `2.0e-177` |
| `Q_b − Q_C` | 0 | `2.5e-175` |
| `P_c − P_C` | `−1/(z−q)` | `1.45` |
| `Q_c − Q_C` | nonzero | `8.1` |

The c-route residual is exactly `−1/(z−q)`, the simple zero of
`c(z) = −(z−q)/(q−1)` at `q`, which the gauge relation predicts. Note `−1/(z−q)`
has no zero in `z`, so a comparison against the c-route returns "mismatch" at
every sample point, at every parameter value.

**At infinity.** On the branch with rate `+t/2` the eigenvector is `e₁ + O(1/z)`,
so the first component carries exponent `θ_∞/2` with no shift for any `θ_∞`;
System C demands `−1 − √3/18`, forcing `θ_∞ = −2 − √3/9`, residual 0 at dps 40.
The subdominant branch is then predicted from `ord_∞(N₁₂) = 2` and matches.
Since `P_b ≡ P_C` and `Q_b ≡ Q_C` identically, agreement of every local datum
follows; this is corroboration by a second route, not an independent constraint.

**Two unsound routes, recorded.** (i) Keeping `θ_∞` symbolic inside the scalar
reduction and reading its heads at `z = ∞` is unsound: `deg_z b` drops from 1 to
0 at exactly the printed `θ_∞`, so the head coefficients are discontinuous
precisely at the point of interest. (ii) Treating `μ(+) − μ(−)` as
gauge-invariant between the system and a scalar reduction is false here: the two
branches carry different powers of `z`, `0` and `−2`. Route (ii) returned
"inconsistent" and would have reported `θ_∞ = √3/9` — wrong by exactly the
shift, 2. It was caught by an arithmetic control: the two scalar exponents must
sum to `−P₁`; they summed to `−1` against System C's `−2`.

---

## 8. Monodromy, Stokes data, and verification of the leaf

### 8.1 Setting

The comparison quantities are `x₁, x₂, x₃`. The quantities `a₀, a₁` are
excluded, being identically `2` under unipotent local monodromy (`θ₀ = θ₁ = 0`
gives `s₁ = s₂ ≡ 2`).

`e₁` is the formal solution with exponential factor `e^{+tz/2}`, `e₂` the one
with `e^{−tz/2}`. The residual gauge is exactly `G_m = diag(c,1)`, under which
`d₁, d₂, d₃` are invariant. The comparison quantities are therefore canonical
once the eigen-lines are labelled.

The branch cut and sector labelling at `∞` are fixed in advance, with Stokes rays
`arg z = ±π/2`. Analytic continuation is by Taylor-block continuation with
continuous `log z`; the formal solution at the irregular rank-1 point is
optimally truncated with an exact residual.

The convention — base point side, orientation of the two small loops,
orientation of the loop at `∞`, and the pairing of the source's matrices with the
loop generators — is **not chosen**. A finite candidate set of 16 is declared
together with four conditions, and **exactly one** candidate is required to
satisfy all four; zero, or two or more, is a halt.

### 8.2 Known-answer control

The solver was smoke-tested on an Euler system against `exp(2πiM)` — `5.07e-59`
at dps 60 — then run against Kummer's equation against closed forms.

Three facts emerged and are stated because they constrain the setup.

1. **Kummer's companion system is not trace-free**: `tr B = 1 − b/z`, so
   `det M₀ = e^{−2πib} ≠ 1` and an `SL₂` factorisation cannot apply. The
   trace-free gauge `Ñ = N − ½ tr(N) I` moves `L` to `diag(b/2−a, a−b/2)` and
   gives `tr M₀ = 2cos(πb)`, `det M₀ = 1`.
2. **`M_∞` must be the clockwise big circle.** The counterclockwise circle is
   homotopic to `γ₀` itself.
3. For any unimodular `M` with `M₁₁ ≠ 0`, `(1+f₁f₂)/α − M₂₂` equals
   `(1 − det M)/m₁₁` and **vanishes identically** — so that identity is not a
   test. It is replaced by computing the two Stokes matrices separately and
   requiring each to be unipotent and triangular in *opposite* triangles, plus
   the factorisation identity.

A further identity, derived from a `diag·lower·upper` ordering, has trace
`α + (1+f₁f₂)/α`, whereas the factorisation actually computed is
`e^{2πiL}·S_{2π}(upper)·S_π(lower)`, with trace `α(1+f₁f₂) + α⁻¹`. The two differ
by `(α − α⁻¹)f₁f₂`. In the corrected form it is a **dependent** restatement of
three other checks and is not independent evidence.

**Result: 32 of 32 checks pass** at both parameter values `(a,b) = (1/3, 5/7)`
and `(2/5+3i/10, 11/10−i/5)`, at ≥ 35 digits, individual checks landing at
44–151 digits.

**Consequence carried forward:** because `M_∞` is the clockwise loop, `α` is
`e^{−2πiL₁₁}`, not `e^{+2πiL₁₁}`.

### 8.3 System C at `t₀`

At the point of §5.4 on branch 1: `det A₀ = det A₁ = 0` exactly;
`A_∞ = (t/2)diag(−1,1)` to 121 digits; `(A₀+A₁)₁₁ = −θ_∞/2`; and

    L₁₁ = θ_∞/2 exactly,  hence  α = e^{iπθ_∞}  in closed form.

Two checks on the truncated formal series, neither a magnitude bound: the
residual sits at the **minimal term** of the series (observed ratio 1.29 against
a bound `N³`), and it decays at the predicted Gevrey rate `e^{−|t|R}` between
`R = 160` and `R = 140` — observed `1.028e-11` against a predicted `8.163e-12`,
ratio 1.259.

On `|z| = R` the factor `e^{Λz}` has modulus `e^{±|t|R}` with `|t|R = 204.25`, a
one-sided dynamic range of `10^{88.6}`; forward integration contaminates the
recessive column at that level. This is inherent to the path and not removable by
rescaling.

**Exactly one convention of the sixteen passes all four conditions** —
base point to the right, small loops counterclockwise, `M_∞` clockwise, and the
source's `M₁` paired with `γ₁` — with

    ‖M₀M₁M_∞ − I‖ = 2.44e-105,
    tr − 2 = 2.1e-190 and 1.3e-190,
    α and shape at 1.9e-91 and 5.4e-113,
    cubic 1.17e-111.

The other 15 fail, several on `α` alone (`0.327`, `2.27`, `2.34`).

**The comparison quantities at `t₀`**, error bar `8.49e-105` from step halving
(`h = ρ/4` vs `ρ/8`, 273 vs 487 steps), not from a single run's internal
estimate:

```
x₁ = -3.4791908904110720783362611334763347 - 1.0850135702764914087402902784335110 i
x₂ =  5.0274753770206575050513601616191382 + 2.3656209874946766465307178962989066 i
x₃ =  1.9725752524636335304002661101339216            (imaginary part 4.7e-113)
α  =  0.8227296571200546517827584488045268 + 0.5684328555732130672602017927956251 i
f₁ = -3.3348223479737981505682497583139139 + 0.9702273755626692946689592593960931 i
f₂ = -0.0594481783485879912289472592033449 - 0.0730538755916226118669832209758999 i
```

`α = e^{+iπ√3/9} = e^{−iπθ_∞}`; `|α| = 1` and `|arg α| = π√3/9`.

The fibre through System C **is** a singular cubic surface — the point sits on
two resonance divisors, `s₁ = s₂ = 2` — but the point itself is a **smooth**
point of that surface: `∇F = (1.523, 1.523, 21.240)` in modulus,
`max|∇F| = 21.24`. The coordinates therefore retain first-order sensitivity.

### 8.4 Sensitivity of the observable

Perturbing `(q,p)` off the leaf, holding `t` and `θ` fixed — the perturbed points
remain in the `(0,0,1)` family, since `det A₀ = det A₁ = 0` hold identically in
`(p,q)`:

| direction | `max|Δx_i|` at `10⁻⁶` | ratio `(10⁻⁶)/(10⁻⁸)` |
|---|---|---|
| `q` | `8.686e-6` | `99.99978` |
| `p` | `2.639e-5` | `99.99956` |

Both ten orders above the `10⁻¹⁵` floor, both ratios first order. The observable
can see leaf membership.

### 8.5 Transport along the leaf

Painlevé V `(4.2)` with `θ₀ = θ₁ = 0` — the middle term of `dp/dt` then vanishes
identically and is dropped, not approximated — transported by Taylor series in
`s = t − t₀` from exact recurrences, with no finite differences anywhere, to
`t₁ = t₀ + ε`.

Controls, all assertions that can fail:

- two constructions of `A(z)` sharing no code agree to 201 digits;
- the Taylor series satisfies the PV system at `t₁`: residuals `2.4e-201` and
  `8.3e-202`;
- one step of size `ε` agrees with two steps of `ε/2` to 200 digits;
- **discrimination**: the same transport with a deliberately wrong vector field
  (the constant `2θ_∞ − 2` dropped from `dp/dt`) moves the trace coordinates by
  `0.0383`.

| `ε` | worst coordinate agreement |
|---|---|
| `10⁻³` | **90.81 digits** |
| `10⁻⁴` | **91.83 digits** |
| `10⁻⁵` | **92.83 digits** |

Agreement to ~91 digits against a threshold of 30.

**On the residual.** The ratios are `10.430` and `10.034` — linear in `ε` over
two decades. Raising the working precision from 200 to 320 digits leaves the
agreement figures and their ratio **identical to every printed figure**, while
every precision-limited control improves by about 120 digits:

| quantity | dps 200 | dps 320 |
|---|---|---|
| `max|A_sympy − A_mpmath|` | `1.02e-201` | `2.65e-321` |
| `‖M₀M₁M_∞ − I‖` at `t₁` | `1.20e-105` | `5.57e-225` |
| cubic residual at `t₁` | `3.96e-112` | `7.13e-232` |
| `|x₃(t₁) − x₃(t₀)|` | `2.35e-113` | `3.30e-233` |
| PV residual at `t₁` | `2.45e-201` | `1.26e-321` |
| **`α` residual** | **`1.834e-91`** | **`1.834e-91`** |

Two values at a round-off floor cannot reproduce to seven significant figures
across a 120-digit change in precision. The residual is therefore systematic and
deterministic. The one quantity that does not move is the `α` residual, which is
the optimal-truncation floor `e^{−|t|R}` with `|t|R = 204.25`, i.e. `10^{−88.7}`
— a property of `R`, not of the arithmetic precision. The mechanism for the
`O(ε)` behaviour is that the truncation error is a smooth function `E(t)` of the
point, so the transported difference is `|E(t₁) − E(t₀)| ≈ |E′(t₀)|·ε`.

**Scope of the conclusion.** What is confirmed is that the linear system built
from `(q(t₀), p(t₀))` lies on the PV leaf **as seen by the trace coordinates
`x₁, x₂, x₃`, under the one convention of sixteen that passed the declared
four-condition test** — and that convention is a *result*, obtained by an
overdetermined test declared before any number was computed, not an assumption
carried into it. Three further qualifications belong with that sentence: the
observable is `(x₁,x₂,x₃)` and not the full monodromy representation; the check
is at one point of one branch, along one direction in `t`, at three step sizes;
and this is confirmation at a stated precision, not a proof.

### 8.6 The second branch

The solution of §5.4 is a sign pair.

**Proposition 9.** Branches 1 and 2 are related by the Galois automorphism `σ` of
`Q(√3, √11)` with `σ(√3) = −√3`, `σ(√11) = +√11` (hence `σ(√33) = −√33`), which
maps `t, θ_∞, q, p` term by term, each difference simplifying to exactly `0`.
They are **not** complex conjugates: `conj(q₁) ≠ q₂` and `conj(p₁) ≠ p₂`.

That symmetry is algebraic and the monodromy is transcendental in the matrix
entries, so `σ` does not act on the analytic continuation: it transfers the
location argument but carries no information about the Stokes data. Branch 2 was
therefore computed in full.

| | branch 1 | branch 2 |
|---|---|---|
| `t` | `−2√33 i/9` | `+2√33 i/9` |
| unique convention (of 16) | `right\|ccw\|infcw\|10` | `right\|cw\|infccw\|01` |
| `x₁` | `−3.47919089041107…−1.08501357028 i` | `+5.02747537702066…+2.36562098749 i` |
| `x₂` | `+5.02747537702066…+2.36562098749 i` | `−3.47919089041107…−1.08501357028 i` |
| `x₃` | `1.97257525246363353040…` | identical |
| `α` | `0.82272965712005…+0.56843285557 i` | identical |
| agreement | `90.81` / `91.83` digits | `90.82` / `91.84` digits |

The winning convention is the exact mirror in all three flags, which is what
`t → −t` should do to an orientation-dependent Stokes geometry; and it is a
result of the branch-2 test, not an assumption carried over. The trace
coordinates are the same multiset with `x₁ ↔ x₂` swapped and `x₃, α` identical,
so the two branches sit at the same point of the character variety up to the
relabelling the mirrored convention induces.

**A structural route to that last statement was attempted and fails.** Both
branches carry their finite singular points at `z = 0` and `z = 1` with
`θ₀ = θ₁ = 0`, so `φ(z) = 1 − z` exchanges them and fixes `∞`; and
`D(1−z) = (1−z)(−z) = z² − z = D(z)` exactly.

**Proposition 10.** Since `A` is traceless, `det` is the only constant-gauge
invariant, so a constant gauge `G` with `A₂(z) = −G A₁(φ(z)) G⁻¹` forces the
scalar condition `P₂(z) = P₁(φ(z))` with `P := a² + bc`.

Tested symbolically against four candidate maps:

| `φ` | `max|coeff|` of `P₂ − P₁∘φ` |
|---|---|
| identity | `3.83454` |
| `z ↦ 1−z` | `0.415740` |
| coefficient conjugation | `0.415740` |
| conjugation ∘ `z ↦ 1−z` | `3.83454` |

Zero of four vanish, against a positive control — `σ(P₁) − P₂`, a known-true
identity of the same radical complexity — which returns exactly `0`. **No
constant-gauge analytic equivalence exists.** A `z`-dependent gauge is untested:
it would shift the trace by `(log det G)′`, so the traceless-implies-det-only
argument does not apply to it.

---

## 9. The Stokes constant at `ζ*`

In the native normalisation, with the convention `leading B[Φ] = 1`:

```
  C      = 8.127336795495072367112578732023583182264542722338793…
  S_{ζ*} = 2πi C = 51.0655631399546622698316746099456615679204103033104… i
  ζ*     = 4/√3
```

`C` is trusted to 100 digits. Two independently stored copies agree on their
first 251 characters.

**A first search space was degenerate and its negative is void.** Over the basis
`[log C, log 2, log 3, log π, log Γ(1/3), log Γ(1/6), 1]`, PSLQ returned — for
`C` and for all three decoys alike — the relation

    −2 log 2 + 3 log 3 − 3 log π + 12 log Γ(1/3) − 6 log Γ(1/6) = 0,

whose coefficient on `log C` is **zero**. The cause is that Legendre duplication
at `z = 1/6` together with reflection at `1/3` gives

    Γ(1/6) = 2^{2/3} √3 Γ(1/3)² / (2√π),      residual 1.69e-80.

So the search never tested `C`: the decoys were rejected because the search
returned a `C`-free relation, not because the space discriminates. That result is
**void, not negative**.

**In the corrected space** `{2, 3, π, Γ(1/3)}`, shown independent by a
degeneracy pre-check run on the basis with the target removed: **no** relation

    C = ± 2^a 3^b π^c Γ(1/3)^d e^f

exists with `|coeff| ≤ 10⁶`, `1 ≤ |m| ≤ 12` and cost `≤ 40`, against `C` known
to 100 digits.

This is a negative over a stated space, and is not a statement that no closed
form exists.

---

## 10. What is not established

- Membership is confirmed **at a stated numerical precision**, for the trace
  coordinates `x₁, x₂, x₃`, at one point of each branch, along one direction in
  `t`. It is not a proof.
- The `ρ` of §1 is an exponent in `ζ`; whether it is the same object as an
  indicial exponent in `u = √z` is not shown here.
- Whether object `A` lies in any such family is untouched.
- The sharper hypothesis of §6 is not supplied.
- The `z`-dependent gauge of §8.6 is untested.
- No closed form for `r_∞` and none for `C`, over the stated bases only.
