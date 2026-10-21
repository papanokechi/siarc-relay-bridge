# PREREG — CT-S22-STOKES

Written **before any solver code exists** in this session, per P0 and per the
operator's Stage 0 instruction. Nothing in this file may be changed after a
number has been seen; if a threshold proves ill-posed that is **a finding to
report, not a number to adjust**, and the correct framing in that case is that
*the observable was underspecified*, not that the bound was too tight.

Session: `sessions/2026-09-17/CT-S22-STOKES/`
Date: 2026-09-19
Predecessor gap: `S16-15` (CT-S16 `REPORT.md` §6) — the pre-registered step-3(b)
falsifier was never run. **Its 30-digit threshold is carried over unchanged.**

---

## 0. The question

CT-S16 established, at label STRUCTURAL, that System C is a point of van der
Put–Saito's chart `U₀` of the moduli space `M_{t,λ}` for the `(0,0,1)` row, that
the isomonodromy vector field is regular there, and therefore that exactly one
Painlevé V leaf passes through it. What was **not** done is the thing that would
make the leaf statement VERIFIED rather than inferred: exhibit the deformation
and check that the monodromy and Stokes data are actually constant along it.

**Hypothesis H.** Transporting `(q,p)` along the PV flow (4.2) from `t₀` to
`t₁ = t₀ + ε` and rebuilding the linear system from `(q(t₁), p(t₁), t₁)`
produces a connection with the **same** analytic data as at `t₀`.

**Observable.** The van der Put–Saito trace coordinates `(x₁, x₂, x₃)` of §3.2.1
(p.2629) and §3.2.2 (p.2630) — see §3 below.

**Falsifier, threshold fixed now.** Disagreement of any of `x₁, x₂, x₃` beyond
**30 significant digits** at either `ε`. Anything less is a FAIL.

**Scope of a failure, pre-declared.** A failure falsifies **this construction**
— the normal-form match, the located point, the flow integration, or the Stokes
solver — and **not** membership in general. The verdict must say so in those
words.

---

## 1. Sources, and what is taken from where

All read from the local PDF `refs/vdPS-arXiv-0902.1702v5.pdf`
(sha256 `1d4be8e4526f6ca834506a976a6ffc999e9659acc2da08753b87e1f59d006e47`),
by **looking at rendered page images**, per the `S16-17` rule. Journal page =
PDF page + 2609.

| datum | source | status |
|---|---|---|
| family `(4.1)`: `A = z(z−1)(A_∞ + A₀/z + A₁/(z−1)) = [[a,b],[c,−a]]` | p.2655 | read this session |
| `A_∞ = (t/2)·diag(−1,1)`, `det A_i = −θᵢ²/4`, exponents `±(tz+θ_∞)/2` at ∞ | p.2629 §3.2 | read this session |
| `M₁M₂M_∞ = 1`; `M_∞ = diag(α,α⁻¹)·[[1,0],[f₁,1]]·[[1,f₂],[0,1]]` | p.2629 §3.2.1 | read this session |
| `s₁ = tr M₁`, `s₂ = tr M₂`, `s₃ = α`; `d₃ := b₁c₂+d₁d₂−s₂d₁−s₁d₂+s₁s₂+s₃` | p.2629 | read this session |
| `xᵢ = dᵢ`; cubic `F = 0` | p.2630 | read this session |
| PV flow `(4.2)` | p.2655 | read this session |
| the point `(p,q,t,θ_∞)`, `θ₀ = θ₁ = 0` | CT-S16 `outputs/pq_solution.txt`, `REPORT.md` §4 | carried in |
| the `b(z)` typo: first term is `(p+½(q−1)qt)²`, not `(p+½(q−1)q)²` | CT-S16 §2 | carried in, **re-corroborated** |

**Re-corroboration of the typo, new this session.** On the same page 2655 the
matrix `B₁` prints the corresponding entry **with** the `t`:
`(p + ½(q−1)qt)² − θ₁²/4 + (q−1)(…)`. The paper therefore contradicts itself on
one page, and the reading CT-S16 adopted from `det A(1) = −θ₁²/4` is the one
`B₁` also uses. This is recorded as corroboration, not as a new result.

**A convention the paper states and the printed family does not satisfy.**
p.2629 says "`θ_∞` is the (1,1) entry of `A₀+A₁`". CT-S16 §2 found the printed
family gives `−θ_∞/2` instead. This session does **not** rely on the prose: every
quantity is computed from the matrix `A(z)` itself. The discrepancy is used only
as a **signed cross-check** (§4, control C-5).

---

## 2. Geometry: base point, loops, orientation, cuts, sectors, rays

Fixed now, in full, so that no choice is made after seeing a number.

### 2.1 The connection and its horizontal sections

The module is `d/dz + A(z)` with `A(z) = A_∞ + A₀/z + A₁/(z−1)`, so a
fundamental matrix of **horizontal sections** satisfies

> `Y′(z) = −A(z) Y(z)`,  `B(z) := −A(z)`.

`B_∞ = −A_∞ = diag(t/2, −t/2)`. Column 1 therefore carries `e^{+tz/2}` and
column 2 carries `e^{−tz/2}`.

**Basis labelling at ∞ (fixes the residual ambiguity).** `V_q` and `V_{−q}` are
the two formal eigen-lines. We declare

> `e₁` := the formal solution with exponential factor `e^{+tz/2}` (first
> coordinate), `e₂` := the one with `e^{−tz/2}` (second coordinate).

The remaining gauge freedom is exactly `G_m = diag(c,1)` (p.2629), under which
`d₁, d₂, d₃` are invariant. **So once `e₁/e₂` are labelled as above, the
comparison quantities are canonical.** This is the basis-and-normalisation
question the operator required to be settled before any code: it is settled by
(i) the eigen-line labelling above and (ii) the `G_m`-invariance of `dᵢ`.

### 2.2 Branch cut, sectors, Stokes rays

The exponential difference is `q(z) = t z`. At `t₀ = −2i√33/9` we have
`arg t₀ = −π/2`, `|t₀| = 2√33/9 = 1.27656947…`.

- **Singular (Stokes) directions**: `t z ∈ ℝ`, i.e.
  **`d₊ : arg z = +π/2`** (`t z ∈ ℝ_{>0}`) and
  **`d₋ : arg z = −π/2`** (`t z ∈ ℝ_{<0}`).
- **Anti-Stokes directions** (`Re(tz) = 0`): `arg z = 0` and `arg z = π`.
- **Branch cut for `z^L`**: the **negative real axis**, `arg z ∈ (−π, π]`,
  principal branch of `log z`.
- **Reference direction for summation**: `d₀ : arg z = 0`, which is a regular
  direction (it is anti-Stokes, not singular). All formal solutions are
  optimally truncated on this ray and on the rays `arg z = ±π/2 ± π/4`.
- **Sector labelling**: `S_k` is the open sector bisected by
  `arg z = k·π/2`, `k = 0,1,2,3`, of opening `π`. Each contains exactly one
  singular direction on its boundary pair; consecutive `S_k` overlap.

These are the **named Stokes rays**: `d₊ = +π/2`, `d₋ = −π/2`. Two of them,
as required for Katz rank 1 (`2r = 2`).

### 2.3 Base point and loop generators

- **Base point** `z* = R` on the positive real axis (`arg z* = 0 = d₀`), with
  `R` chosen so that `|t z*| ≥ 120`. At `t₀` this means `R ≥ 94.0`; we fix
  **`R = 160`**, giving `|t z*| = 204.25` and optimal-truncation error
  `O(e^{−204}) ≈ 10^{−88.7}`, i.e. **58 orders below the threshold**.
- **Orientation**: all loops **counterclockwise** (positive).
- `γ₁` (around `z = 1`): from `z*` straight along the positive real axis to
  `1 + r`, once ccw around `1` at radius `r = 1/4`, straight back.
- `γ₀` (around `z = 0`): from `z*` along the positive real axis to `1 + r`,
  then over `z = 1` by the **upper** semicircle of radius `r`, on to `z = r`,
  once ccw around `0` at radius `r`, and back by the same route.
- `γ_∞`: the full ccw circle `|z| = R` from `z*` to `z*`.
- **Composition convention**: continuation along `γ` sends a fundamental matrix
  `Y ↦ Y·M_γ`; for the concatenation "`γ` then `δ`" the matrix is `M_γ M_δ`.

**The ordering/orientation ambiguity is resolved by a pre-declared
overdetermined test, not by choosing.** There are finitely many candidate
conventions (order of the two loops, sign of orientation, left/right action:
8 combinations). We declare *now* that the admissible convention is the one —
**and there must be exactly one** — satisfying **all** of:

1. `‖M₀ M₁ M_∞ − I‖ < 10⁻³⁰`;
2. `tr M₀ = tr M₁ = 2` and `M₀ ≠ I ≠ M₁` (forced by `θ₀ = θ₁ = 0`);
3. `M_∞` has the exact shape `[[α, αf₂],[α⁻¹f₁, α⁻¹(1+f₁f₂)]]` with the `α`
   **independently** predicted in §4 C-5;
4. the cubic `F(x₁,x₂,x₃,s₁,s₂,s₃) = 0` of p.2630 holds to `< 10⁻³⁰`.

If **more than one** convention passes all four, or if **none** does, that is a
HALT: the convention is genuinely ambiguous and the session reports it rather
than picking. This procedure is pre-registered precisely so that resolving the
bookkeeping by test cannot be mistaken for fitting.

---

## 3. The comparison quantities

Per p.2630, `xᵢ = dᵢ`, where `Mⱼ = [[aⱼ,bⱼ],[cⱼ,dⱼ]]`:

- `x₁ := d₁` — the `(2,2)` entry of `M₀` (vdPS's `M₁`, the loop around `z = 0`);
- `x₂ := d₂` — the `(2,2)` entry of `M₁` (vdPS's `M₂`, the loop around `z = 1`);
- `x₃ := d₃ = b₁c₂ + d₁d₂ − s₂d₁ − s₁d₂ + s₁s₂ + s₃`.

Written `(x, y, z)` in the operator's packet; `z` is not used for the
coordinate anywhere in this session, to avoid collision with the independent
variable. **The three comparison quantities are `x₁, x₂, x₃`.**

**`a₀` and `a₁` are excluded, and here is why in one line.** With
`θ₀ = θ₁ = 0` the local monodromies at `z = 0, 1` are unipotent and `≠ I`
(CT-S16, carried in from `R1-83`/C1), so `s₁ = tr M₀ ≡ 2` and
`s₂ = tr M₁ ≡ 2` **identically, for every point of the leaf and for every
nearby connection with the same local exponents**. A quantity that is
constrained to a constant cannot discriminate, so including it in the
comparison would manufacture two free passes. They are therefore **excluded
from the observable and retained only as control C-3.**

**A consequence that must be recorded before it is measured.** p.2630 states
that the fibre `π⁻¹(p)` acquires singular points exactly when `p` lies on one of
the five divisors `s₁ = ±2`, `s₂ = ±2`, `R₁ = 0`, the first four corresponding
to **resonance**. Our point has `s₁ = s₂ = 2` and so lies on **two** of them.
The fibre through System C is therefore a **singular** cubic surface. Whether
our point is itself a singular point of that surface is computable: it is iff
`∂F/∂x₁ = ∂F/∂x₂ = ∂F/∂x₃ = 0` there. **Pre-registered: this gradient is
computed and reported in Stage 2 whatever its value**, because if it vanishes
the coordinates lose first-order sensitivity and Stage 3 is the only thing that
would reveal it.

With `s₁ = s₂ = 2` and `s₃ = α` the cubic control reads

> `F = x₁x₂x₃ + x₁² + x₂² − (2+2α)x₁ − (2+2α)x₂ − αx₃ + α² + 4α + 1 = 0`.

---

## 4. Method, and the controls that can fail

### 4.1 Integration method and step control

- **Analytic continuation**: Taylor-series stepping of `Y′ = B(z)Y` in the form
  `z(z−1)Y′ = −N(z)Y` with `N` the polynomial matrix `[[a,b],[c,−a]]` of `(4.1)`.
  Writing `w = z − z₀`, `P(w) = (w+z₀)(w+z₀−1) = p₀ + p₁w + p₂w²` and
  `N(z₀+w) = n₀ + n₁w + n₂w²`, the coefficients obey

  > `Y_{k+1} = −[ (n₀ + p₁k)Y_k + (n₁ + p₂(k−1))Y_{k−1} + n₂Y_{k−2} ] / (p₀(k+1))`,

  which is exact and needs `p₀ = z₀(z₀−1) ≠ 0`, i.e. steps never land on a
  singular point.
- **Step control**: at `z₀` let `ρ = min(|z₀|, |z₀−1|)`. Step length
  `h = ρ/4`; series order `K` chosen so `(h/ρ)^K = 4^{−K} < 10^{−(dps+10)}`.
  **Error is estimated by halving**: the entire pipeline is run at `h = ρ/4`
  and again at `h = ρ/8`, and the reported error is the difference. A single
  run's internal truncation estimate is **not** accepted as the error bar —
  that is the operator's explicit Stage 2 requirement.
- **Working precision**: `dps = 120` throughout, i.e. 90 guard digits over the
  30-digit threshold.
- **Formal solution at ∞**: `Y_f = F(z) z^L e^{Λz}`, `Λ = diag(t/2, −t/2)`,
  `F = I + Σ_{k≥1}F_k z^{−k}`, `L = diag` part of `B₁ = −(A₀+A₁)`, obtained by
  the standard recurrence; **the truncated series is substituted back into the
  ODE and the residual checked to be of the expected order** (control C-0).
  Truncation at the optimal order `N ≈ |t z|`.

### 4.2 Controls, all of them assertions that can fail

CT-S16 §7 lost a whole result to `irreducibility.py`, which returned a verdict
with no test performed. Every control below is an `assert`, and each is
**checked against a value known before the run**:

- **C-0** truncated formal series satisfies the ODE to the expected order.
- **C-1** `M₀M₁M_∞ = I` to `10⁻³⁰`.
- **C-2** `det Mⱼ = 1` for `j = 0,1,∞`.
- **C-3** `tr M₀ = tr M₁ = 2` and neither is `I`.
- **C-4** `M_∞` has the triangular×diagonal shape of p.2629, i.e.
  `α := (M_∞)_{11}`, `f₂ := (M_∞)_{12}/α`, `f₁ := α(M_∞)_{21}`, and the
  remaining entry reproduces `α⁻¹(1+f₁f₂)`.
- **C-5** `α = e^{2πi L₁₁} = e^{iπθ_∞}` — **predicted in closed form before the
  run** from `θ_∞ = −2 − √3/9`, giving `α = e^{−iπ√3/9}`, `|α| = 1`.
- **C-6** the cubic `F = 0`.
- **C-7** the two step sizes agree to better than the threshold.

C-5 and C-6 are the load-bearing ones: neither is reachable by a solver that is
silently computing the wrong object.

### 4.3 Stage 1 — the known-answer control, and its closed form

Solver correctness is established **before** System C is touched, on Kummer's
equation `zw″ + (b−z)w′ − aw = 0`, whose companion system
`Y′ = [[0,1],[a/z, 1−b/z]]Y` has a regular singular point at `0` and an
irregular point of Katz rank 1 at `∞` — the same local structure as the
`(0,0,1)` family, with `Λ = diag(0,1)` after the constant gauge
`T = [[1,1],[0,1]]` and `L = diag(−a, a−b)`.

**Closed-form targets, fixed now:**

- `tr M₀ = 1 + e^{−2πib}` and `det M₀ = e^{−2πib}` — exact, from the Frobenius
  exponents `0` and `1−b`. Basis-independent, hence directly comparable.
- formal monodromy at ∞ `= diag(e^{−2πia}, e^{2πi(a−b)})`.
- `M₀M_∞ = I`, hence `tr(γ̂·St₂·St₁) = 1 + e^{+2πib}`.
- the individual Stokes multipliers: obtained from the exact connection between
  the Frobenius basis at `0` and the `U`-basis at `∞`. **This connection is not
  quoted from memory**: it is verified in-session, numerically at `dps ≥ 40`,
  against `mpmath.hyperu` and `mpmath.hyp1f1`, which are an implementation
  independent of every line of code in this session. If that verification fails,
  the session HALTS and reports the formula as unavailable rather than adjusting
  it.

**FALSIFIER (Stage 1).** Agreement with the closed forms below **35 significant
digits**, at either of the two parameter values

> `(a,b) = (1/3, 5/7)` and `(a,b) = (2/5 + 3i/10, 11/10 − i/5)`,

chosen generic: `b ∉ ℤ`, `a ∉ ℤ`, `a − b ∉ ℤ`, so no resonance and no
degeneration. **On failure the session does not proceed to Stage 2.** The
control is kept as a regression test and re-run after every later change to the
solver.

---

## 5. Stage 3 — the vacuity pre-check, and what makes it fire

Run **before** the leaf transport of Stage 4, never after.

**Procedure.** Perturb the point off the leaf: `(q, p) → (q + δ, p)` and
`(q, p) → (q, p + δ)` at `δ = 10⁻⁶` and `δ = 10⁻⁸`, holding `t = t₀` and
`θ` fixed, rebuild `A(z)` from `(4.1)`, and recompute `(x₁,x₂,x₃)`.

**Required outcome.** Each coordinate must move by **≫ 10⁻³⁰**; concretely the
pre-registered requirement is

> `max_i |Δxᵢ| > 10⁻¹⁵` at `δ = 10⁻⁶`, and the response must be **first order**:
> the ratio of `max_i|Δxᵢ|` at `δ = 10⁻⁶` to that at `δ = 10⁻⁸` must lie in
> `[50, 200]` (a decade-squared change in `δ` against a linear response is
> `100`; the window admits a factor `2` of curvature).

**What makes it fire.** Either (i) `max_i|Δxᵢ| ≤ 10⁻¹⁵` at `δ = 10⁻⁶` — the
observable cannot see a perturbation ten thousand million times larger than the
threshold, so a 30-digit agreement in Stage 4 would be agreement about nothing;
or (ii) the ratio falls outside `[50,200]`, which would mean the response is not
first order and the sensitivity claim is not what it appears to be.

**If it fires the whole test is void and the session HALTS and says so.** No
Stage 4 number is reported in that case, because a falsifier that cannot fail is
not evidence. This is the direct descendant of the `S16-11` defect.

**Note on `s₁ = s₂ = 2`.** Because the fibre is singular (§3), the possibility
that the coordinates degenerate is not hypothetical here; it is the specific
reason this pre-check is not a formality.

---

## 6. Stage 4 — leaf transport

- Integrate PV `(4.2)` with `θ₀ = θ₁ = 0` in `t` from `t₀` to `t₁ = t₀ + ε`
  along the straight segment, by Taylor series of the vector field (series
  arithmetic in `mpmath`, order fixed so the tail is `< 10⁻(dps−10)`).
- **Two values a decade apart**: `ε = 10⁻³ · t₀/|t₀|` and `ε = 10⁻⁴ · t₀/|t₀|`
  (i.e. along `t₀`'s own direction, so the segment stays on the ray through the
  origin and no movable pole is approached tangentially).
- Rebuild `A(z)` at `(q(t₁), p(t₁), t₁)` from `(4.1)` and recompute `x₁,x₂,x₃`
  **by the same pipeline**, including all controls C-0…C-7.
- **PASS**: `|xᵢ(t₁) − xᵢ(t₀)| < 10⁻³⁰` for all three, at both `ε`, **and** the
  residual scales as expected in `ε` — since the true residual is zero, what is
  required is that neither `ε` shows a residual above threshold and that the
  observed residual does **not** grow like a positive power of `ε`, which would
  indicate a real drift rather than round-off.
- **FAIL**: anything else, with the scope sentence of §0 attached verbatim.

---

## 7. Stage 5 — `S_{ζ*}` (separate pre-registration required)

Not run in this session unless Stages 1–4 all pass, and then only under its own
PREREG entry.

**Naming prohibition, carried from CT-S3B (`REPORT.md`, `DERIVATION.md`) and
restated here because the two are a factor of 2 apart in the action:**

> **`K` is the amplitude at `ξ₀`. `S_{ζ*}` is the Stokes constant at the action
> difference `ζ* = 2ξ₀`. These are different objects. Neither name may be used
> for the other at any point, in code, in output, or in prose.**

Any script in this session that defines a variable named `K` or `S_zeta` must
carry the object's definition in a comment on the same line.

---

## 8. Halt conditions

P0's four, plus:

- Stage 1 falsifier fires (below 35 digits) → **do not proceed to Stage 2**.
- Stage 3 vacuity fires → **void, halt, report**.
- The convention test of §2.3 admits zero or ≥ 2 conventions → **halt**.
- The `mpmath` cross-check of the Kummer connection formula fails → **halt**,
  report the formula as unavailable.
- Any control C-0…C-7 fails at Stage 2 → **halt**; a Stokes solver that cannot
  reproduce `α` in closed form is not computing the Stokes data.
- Runtime beyond 3× budget.

## 9. Labels, fixed now

- Page quotations: **INSPECTED**.
- Stage 1 agreement with closed forms: **VERIFIED** (at stated dps, with
  residual).
- Stage 2 trace coordinates: **VERIFIED**.
- Stage 3 sensitivity: **VERIFIED**.
- Stage 4 leaf constancy: **VERIFIED** — and *only* VERIFIED. A 30-digit
  numerical agreement is **not** a proof that the leaf through System C is the
  PV leaf; it is a numerical check at a stated precision. The membership
  statement of CT-S16 §5 remains **STRUCTURAL**, and remains up to a rank-1
  twist. **No label may be raised because Stage 4 passes.**

## 10. Prohibitions

No commits, pushes, tags, PRs, deposits, uploads, submissions or emails.
Nothing outside `sessions/2026-09-17/CT-S22-STOKES/` is modified; files from
earlier sessions are read, and copied if needed, never edited.
Symbolic equality is established by simplifying the difference to zero **and** a
high-precision numeric check — never by `==` on unevaluated radicals.
Every script reads back what it wrote.
