# Sub-problem C / Stage 2 — Kovacic algorithm on L_φ (Galois group)

**Slot:** PERIOD-REP-VQUAD-003 · **Stage:** 2 · **Date:** 2026-06-15
**Status:** COMPLETE · **HALT GATE 2: PASS** · **G-KOVACIC closed**
**Scripts:** `scripts/stage2_kovacic.py`, `scripts/stage2b_symsquare.py`
→ `scripts/stage2_kovacic_results.json`

> **Result: the differential Galois group of L_φ over ℚ(√3)(z) is SL(2,ℂ).**
> Two independent methods agree. This **documents the V_quad paper's "SL(2) by exact
> Kovacic" claim** (gap G-KOVACIC, "confirmed-absent in corpus" at VQUAD-002, now executed).

---

## 1. Reduction to normal form

L_φ = q₂D² + q₁D + q₀ over ℚ(√3) (VQUAD-002 §4.0a). With a = q₁/q₂, b = q₀/q₂, the
substitution y = u·exp(−½∫a) gives **u″ = r u**, r = ¼a² + ½a′ − b. Exact computation:

> **r = (11z⁴/4 + z² + z + 3) / ( z⁴ (z⁴ + 2z³ + 7z² + 6z + 9) )**
> = (11z⁴ + 4z² + 4z + 12) / ( 4 z⁴ (z²+z+3)² ).

(The denominator factors as 4z⁴(z²+z+3)²; note q₂ = 4(2√3−3)z²(z²+z+3).)

### Pole / order data (decisive for Kovacic)

| point | type | pole order of r |
|---|---|---|
| z = 0 | **irregular** singular | **4** |
| z = (−1 ± i√11)/2 (roots of z²+z+3) | regular singular | **2** each |
| z = ∞ | ordinary/regular | o(∞) = deg den − deg num = 8 − 4 = **4** |

Leading Laurent coefficient of r at z = 0: **r ~ (1/3)·z⁻⁴**, so the coefficient is
**L₀ = 1/3 ≠ 0**. (This is what makes z=0 a genuine irregular point with two *distinct*
exponentials, used in Method 2.)

---

## 2. Method 1 — Kovacic case elimination

Kovacic's algorithm assigns the group to one of four cases. We eliminate 1, 2, 3:

### Case 3 (finite group A₄/S₄/A₅) — EXCLUDED
Necessary condition: every pole order ≤ 2 and o(∞) ≥ 2. **Violated**: z=0 has pole order
**4 > 2**. Rigorously excluded.

### Case 1 (reducible, group ⊆ Borel) — EXCLUDED
Case 1 holds **iff** the Riccati equation v′ = r − v² has a **rational** solution
(equivalently L_φ has a hyperexponential solution exp∫ω, ω ∈ ℚ̄(z)). Tested with sympy's
complete rational-Riccati solver (`solve_riccati`, b₀=r, b₁=0, b₂=−1, coefficients in
ℚ(√3)):

> **solve_riccati(...) = [ ]  (no rational solution).**

Rigorously excluded. (sympy's `solve_riccati` is a complete algorithm for *all* rational
solutions; it handled the √3 coefficients natively.)

### Case 2 (imprimitive/dihedral, G ⊆ N(T)) — EXCLUDED
Case 1∪2 holds **iff** the **symmetric square** L⊙² = D³ − 4rD − 2r′ has a rational
solution (a Galois-fixed quadric). Case 1 already excluded, so a rational solution of L⊙²
would mean Case 2. Searched with the ansatz

> f = N(z) / ( z⁸ (z²+z+3)⁴ ),  deg N ≤ 18,

(generous pole-order bounds at 0 and at the z²+z+3 block; growth ≤ z² at ∞). Splitting each
coefficient over the ℚ-basis {1, √3} gave a homogeneous linear system in **38 rational
unknowns**; its only solution is the **trivial** one. No rational solution → Case 2
excluded.

### Conclusion (Method 1)
Cases 1, 2, 3 all excluded ⟹ **Case 4: G(L_φ) = SL(2,ℂ).**

---

## 3. Method 2 — structural confirmation (independent of the Kovacic search)

This positive-generation argument does not rely on the exhaustive negative search of
Method 1, and serves as the required second-method cross-check.

1. **G ⊆ SL(2).** The reduced equation u″ = r u has no first-derivative term ⟹ the
   Wronskian of any solution basis is constant ⟹ det of the monodromy/Galois action is 1
   ⟹ G ⊆ SL(2,ℂ).
2. **Exponential torus 𝔾_m ⊆ G.** At z=0, r ~ (1/3)z⁻⁴ with L₀ = 1/3 ≠ 0 ⟹ Poincaré rank 1
   irregular singularity with the two exponential parts exp(±√L₀ / z) = exp(±(1/√3)/z),
   which are **distinct**. Distinct exponentials ⟹ the local exponential torus is the full
   diagonal maximal torus 𝔾_m ⊂ SL(2).
3. **An off-torus unipotent ∈ G.** The deposited Stokes constant **S = 2πK ≠ 0**
   (VQUAD-001; K verified to 58 digits) at this irregular point is the entry of a
   non-identity Stokes matrix, a unipotent element that does **not** lie in the torus.
4. **Generation.** A maximal torus together with a single non-trivial unipotent off it
   generate all of SL(2). With (1), **G = SL(2,ℂ).** ∎

---

## 4. HALT GATE 2

> Gate: halt if the two implementations disagree, or if the result contradicts V_quad's
> SL(2) claim.

* Method 1 (Kovacic case elimination) → **SL(2)**.
* Method 2 (trace-free + exponential torus + Stokes) → **SL(2)**.
* **Agreement: YES.** No contradiction with the V_quad paper's "SL(2) by exact Kovacic".

**HALT GATE 2: PASS.** The probe proceeds. The under-documented G-KOVACIC gap is now
**closed**: the Kovacic verdict is reconstructed explicitly and cross-checked.

---

## 5. Caveats (AEAL)

* Only one symbolic engine (sympy 1.14.0) was available — no Maple/Mathematica. The "second
  method" requirement is met by the **structurally independent** Method 2 rather than a
  second CAS. The two methods share no code path: Method 1 is a negative/exhaustive
  Riccati+symmetric-square search; Method 2 is a positive torus-generation argument from
  the deposited Stokes datum.
* The Case-2 symmetric-square search uses **bounded** pole orders (z⁸, (z²+z+3)⁴, deg N≤18).
  The bounds are generous relative to the local exponents; a solution of smaller pole order
  is representable inside them. The trivial-only nullspace is therefore decisive within
  these (documented) bounds.
* Geometric Galois group (over ℚ̄) is what Kovacic's case structure detects; it is invariant
  under √3 ↦ −√3, consistent with both determinations of the V_quad field.

## 6. Sourcing

* L_φ exact coefficients: VQUAD-002 `operator-verification.md` §4.0a.
* S = 2πK, K (58 digits): VQUAD-001 `numerical-check.md` T1; `stokes_2piK_results.json`.
* Kovacic algorithm & case/group dictionary: J. Kovacic, *J. Symbolic Comput.* 2 (1986)
  3–43; van der Put–Singer, *Galois Theory of Linear Differential Equations*, §4.3.
* Symmetric-square ⟺ quadric-fixing dictionary: van der Put–Singer §4.

**Verdict (Stage 2): G(L_φ) = SL(2,ℂ), two independent methods, HALT GATE 2 PASS.**
