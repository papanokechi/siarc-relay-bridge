# Phase B.3–B.4 — Line-by-line diff of the d=2 proof
# against parametric-in-d replacement

Reference: D2-NOTE v1 Prop 3.3.A proof sketch (`d2_note.tex`
lines 197–226) and CT v1.3 Prop xi0 proof sketch
(`channel_theory_outline.tex` lines 521–540).  The two are
substantively identical; we use the D2-NOTE wording as the
canonical line-by-line basis.

For each line we mark:
- **U** = UNIVERSAL (works at general d without modification)
- **D** = D2-SPECIFIC (true at d=2, requires parametric replacement)
- **M** = MACHINERY (cites Wasow §X.3 / Adams 1928 / Birkhoff 1930
                     / Birkhoff–Trjitzinsky 1933; uniformity gated
                     on Phase C)

The Q20 conjecture (Conj 3.3.A*) is about **ξ_0 only**, not
about ρ or about a_k.  So D-lines that pertain *exclusively*
to ρ or a_k matter for upgrading Prop 3.3.A in full but **do
not** affect the upgradeability of Conj 3.3.A* in isolation.
Each line is annotated for both scopes.

---

## Line L1
**Original (d=2):** "The Newton polygon of the homogeneous
part of (eq:Lf) at `z = 0`, with `d = 2`, is read off from
the lattice points `{(0,0),(1,0),(1,1),(1,2),(2,0)}` (weight
= order of θ, height = order of z)."

**Class:** **D** (the lattice-point set lists exactly k =
0, 1, 2, which is d-dependent).

**Parametric-in-d replacement:** "The Newton polygon of the
homogeneous part of (eq:Lf) at `z = 0` is read off from the
lattice points `{(0,0)} ∪ {(1, k) : 0 ≤ k ≤ d} ∪ {(2, 0)}`."

**Reduces to L1 at d=2:** ✅ (gives `{(0,0),(1,0),(1,1),(1,2),
(2,0)}` exactly).

---

## Line L2
**Original (d=2):** "The lower convex hull has a single
non-trivial edge `(0,0) → (1,2)` of slope 1/2 and
multiplicity 2."

**Class:** **D** (slope = 1/2 is d-specific; "multiplicity 2"
refers to the two formal solutions at the irregular singular
point and is d-INDEPENDENT — order-2 ODE).

**Parametric-in-d replacement:** "The lower convex hull has a
single non-trivial edge `(0,0) → (1, d)` of slope 1/d and
multiplicity 2."

**Reduces to L1 at d=2:** ✅ (gives slope 1/2,
multiplicity 2).

**Verification at general d:** the lattice points
`{(0,0)} ∪ {(1, k): 0 ≤ k ≤ d} ∪ {(2,0)}` have lower-left
convex hull through `(0,0)` and `(1,d)` (since `(1,d)` lies
above all `(1, k<d)` and the segment `(0,0)–(1,d)` is below
all `(1, k<d)` because they sit at `x = 1, y = k < d` above
the line `y = d x`).  The `(2,0)` vertex is on the right
boundary and connects to `(1,d)` by an edge of slope `−d`,
which is not a left-side / `z=0` edge.  Phase A.2's
`newton_edge_d` function verifies this combinatorially.

---

## Line L3
**Original (d=2):** "...corresponding to a Gevrey-2-in-z
irregular singularity."

**Class:** **D** (Gevrey order = d).

**Parametric-in-d replacement:** "...corresponding to a
Gevrey-d-in-z irregular singularity."

**Reduces to L1 at d=2:** ✅.

**Justification at general d:** standard — Gevrey index of an
ODE with a slope-1/d edge of multiplicity m at z=0 is d (in
the z-variable); reduces to Gevrey-1 in `u = z^{1/d}`.  This
is the content of **Wasow §X.3** (or Adams 1928 §3 in the
difference setting).  **M-tagged** (gated on Phase C
literature verification).

---

## Line L4
**Original (d=2):** "Substituting `z = u²` and `θ = (u/2) ∂_u`,
the operator becomes Gevrey-1-in-u..."

**Class:** **D** (the substitution `z = u²` is d-specific;
the rescaling `θ = (u/2) ∂_u` is d-specific).

**Parametric-in-d replacement:** "Substituting `z = u^d` and
`θ = (u/d) ∂_u`, the operator becomes Gevrey-1-in-u..."

**Reduces to L1 at d=2:** ✅.

**Justification at general d:** straightforward chain rule —
if `z = u^d` then `dz/du = d u^{d-1}`, so
`u ∂_u = u · (d u^{d-1}) ∂_z = d z ∂_z = d θ`; hence
`θ = (1/d) u ∂_u`.  This is uniform in d.

---

## Line L5
**Original (d=2):** "...and the level-1/u trans-series ansatz
`f_±(u) = exp(c/u) · u^ρ · (1 + Σ_{k≥1} a_k u^k)` produces
the characteristic polynomial `χ(c) = 1 − (β_2/4) c²` at
leading order..."

**Class:** mixed: **U** for the ansatz form (level-1/u
trans-series — uniform in d after the `z = u^d` rescaling
brings the Gevrey index to 1); **D** for the explicit
characteristic polynomial.

**Parametric-in-d replacement:** "...and the level-1/u
trans-series ansatz `f_±(u) = exp(c/u) · u^ρ ·
(1 + Σ_{k≥1} a_k u^k)` produces the characteristic
polynomial
> χ_d(c) = 1 + (−1)^{d+1} (β_d / d^d) c^d
at leading order..."

**Reduces to L1 at d=2:** ✅ — at d=2,
`χ_2(c) = 1 + (−1)³ (β_2/4) c² = 1 − (β_2/4) c²`.

**Justification at general d:** this is the content of
**Phase A.2's symbolic derivation** (`phase_a_summary.md`,
verdict `A_DIRECT_IDENTITY`).  The principal balance picks
out the `(0,0)` and `(1, d)` lattice points; the `(2, 0)`
vertex contributes at order `u^{2d}` which is subleading.

---

## Line L6
**Original (d=2):** "...whose two roots are `c = ±2/√β_2`.
The positive root pins `ξ_0 = 2/√β_2`."

**Class:** **D** (explicit closed form at d=2).

**Parametric-in-d replacement:** "...whose modulus of any
non-zero root equals `d / β_d^{1/d}`.  This pins `ξ_0 = d /
β_d^{1/d}`."

**Reduces to L1 at d=2:** ✅ — at d=2 the two roots have
modulus `2/√β_2`, the positive real one is the root in
question.

**Justification at general d:** Phase A.2 closed form
`c^d = (−1)^d d^d / β_d`; all d roots have equal modulus
`d / β_d^{1/d}`; for `β_d > 0` and `d` odd there is one
real (negative) root, for `d` even there are two real
roots (`±d / β_d^{1/d}`); in all cases the **modulus**
equals `d / β_d^{1/d}`, which is the geometric content of
ξ_0 (the Borel-plane singular DISTANCE, a modulus).

**This is the line that closes Conj 3.3.A* at general d,
modulo M-tagged machinery.**

---

## Line L7
**Original (d=2):** "The u^1 coefficient of the trans-series
equation pins the indicial polynomial, giving
`ρ = −3/2 − β_1/β_2`."

**Class:** **D** (explicit ρ formula at d=2).

**Parametric-in-d replacement:** ❌ NOT WRITTEN OUT.  The
indicial polynomial at the irregular singular point in
`u = z^{1/d}` for general d is conjecturally a polynomial
of degree 2 in ρ (multiplicity 2 of the slope edge), but
the explicit ρ_d formula in terms of `(β_d, β_{d-1}, …)`
is **open even at d=3** per D2-NOTE v1 §3 last paragraph
("the indicial-polynomial analysis fixing the secondary
exponent ρ_d, and the Birkhoff recursion delivering the
formal coefficients a_k at d ≥ 3, are not written out
here and are open even at d = 3").

**Reduces to L1 at d=2:** N/A.

**Scope impact:**
- For **Conj 3.3.A* (ξ_0 only)** upgrade: **L7 IS NOT
  REQUIRED.**  ξ_0 is fixed at L6 (order u^0); ρ is
  determined at L7 (order u^1) and is independent of ξ_0.
- For **D2-NOTE v1 Prop 3.3.A (ξ_0 AND ρ)** upgrade: L7
  IS REQUIRED at general d.  This is OPEN.

---

## Line L8
**Original (d=2):** "The Birkhoff recursion for the `a_k`
then proceeds row-by-row in the `u^k` coefficient."

**Class:** **D** (explicit row-by-row recursion at d=2).

**Parametric-in-d replacement:** general "Birkhoff–Trjitzinsky
recursion for the `a_k` proceeds row-by-row in the `u^k`
coefficient."  At general d this is the standard B–T
algorithm output (Wasow §X.3 + B–T 1933).  **M-tagged**.

**Reduces to L1 at d=2:** ✅.

**Scope impact:**
- For **Conj 3.3.A***: not required.
- For **Prop 3.3.A (full ξ_0 + ρ + a_k)**: required, M-tagged.

---

## Line L9
**Original (d=2):** "The full computation, including the
worked V_quad example and the (α_1, α_0)-independence of
ξ_0, is [CT v1.3 §3.3 Worked Example]."

**Class:** **U** in the (α_1, α_0)-independence claim
(this is the structural Newton-polygon argument: the `(2,0)`
vertex contributes at order `u^{2d}` which is subleading
relative to ξ_0 at order `u^0`, so α_1, α_0 cannot enter
ξ_0).

**Parametric-in-d replacement:** "...the
(α_1, α_0)-independence of ξ_0 (the numerator polynomial
enters only at the `(2,0)` lattice vertex, which is at
order `u^{2d}` in the u-uniformised operator and so does
not reach ξ_0 at order `u^0`)..."

**Reduces to L1 at d=2:** ✅ at d=2, `2d = 4`.

---

## B.4 verdict signal

**For Conj 3.3.A* (ξ_0 only):** every D-line that pertains
to ξ_0 (L1, L2, L4, L5, L6) has a clean parametric-in-d
replacement that reduces to the d=2 line at d=2.  The
remaining D-lines (L7, L8) pertain to ρ and a_k respectively
and are **out of scope for Conj 3.3.A***.  No D-line is
left without a parametric-in-d replacement within the scope
of the conjecture.

**Verdict signal: `B_TEMPLATE_PARAMETRIC` for
Conj 3.3.A* upgrade scope (ξ_0 only).**

**For Prop 3.3.A (full ξ_0 + ρ statement) at general d:**
L7 has no parametric-in-d replacement available; the d≥3
indicial polynomial is open per D2-NOTE v1 §3.  Verdict
signal for this broader scope: `B_MACHINERY_NEEDED at
d ≥ 3` (specifically: explicit ρ_d formula).

**Machinery citations needed (M-tagged lines):**
- L3 (Gevrey index = d at slope-1/d edge): Wasow §X.3 or
  Adams 1928 §3
- L8 (Birkhoff recursion convergence at general d):
  Birkhoff–Trjitzinsky 1933 §§4–6, Wasow §X.3
- (Implicit at L6) Borel-singularity = exponential
  characteristic root for irregular ODEs: standard
  Borel summability theorem; Wasow §X.3 + Loday-Richaud.

These are the citations whose d-uniformity is gated on
Phase C.
