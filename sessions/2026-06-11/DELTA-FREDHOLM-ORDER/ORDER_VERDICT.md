# ORDER_VERDICT.md — Phase A verdict

**Session:** DELTA-FREDHOLM-ORDER · Phase A (entire order & Hadamard genus of R∞)
**Object:** R∞(λ) = Σ_{S sparse ⊆ {2,3,…}} ∏_{i∈S} λ u_i = Σ_n a_n λ^n,
with u_i = 1/(b(i−1) b(i)), b(k) = A k² + B k + C (degree d; running family (A,B,C)=(1,0,1), d=2).
**Companion certified value:** δ(1,0,1) = log R∞(1) = 0.123857194360626392728504989702590840967579545852296568213131…

**Discipline:** falsification-first. The draft's "order ≤ 1/(2d), genus 0" was to be TESTED, not confirmed.
Two independent routes (power-series coefficient decay; eigenvalue convergence exponent) were required to
agree, backed by by-hand bounds, with PROVEN / STRUCTURAL / VERIFIED / CONJECTURED graded separately.

---

## A4.0 Headline verdict

| Quantity | Value | Grade |
|---|---|---|
| Entire order ρ | **ρ = 1/(2d)**  (= **1/4** for d=2) | STRUCTURAL (by-hand bound) + VERIFIED-numerical (two routes) |
| Hadamard genus | **p\* = 0** | STRUCTURAL (rests only on Σuₙ < ∞) |
| Hadamard product | **R∞(λ)² = ∏_k (1 + λ s_k²)**, no exponential factor | STRUCTURAL |
| Theorem-4 hypothesis S < 1 | **unconditional on the integer family** A,C≥1,B≥0 (uniform S ≤ 1/6; max S=0.1307 at (1,0,1)); conditional for general real b ((0.01,0,1): S=6.84) | STRUCTURAL (uniform bound) + VERIFIED + falsified-universality |

**The draft's "order ≤ 1/(2d), genus 0" is CORRECT and is UPGRADEABLE from an inequality to the equality
ρ = 1/(2d).** The genus-0 claim is confirmed. No downstream claim is overturned on order/genus; the only
correction needed is (i) tighten "≤ 1/(2d)" → "= 1/(2d)" and remove the draft's exponential-factor
placeholder in the Hadamard product, and (ii) restate the Theorem-4 S<1 line as unconditional on the
integer family (uniform S ≤ 1/6), conditional for general real b. Details and paste-ready text below.

---

## A1 — Coefficient route (power-series order)

`order_coefficients.py` (dps 220) computes a_n exactly (positive recurrence P_m = P_{m−1} + λ u_m P_{m−2},
λ-degree tracking; all contributions positive ⇒ no cancellation), Richardson-extrapolated in the truncation
parameter h = 1/M^{2d−1} (= 1/M³ for d=2 — see GOTCHA 1), then fits the Hadamard order-from-coefficients law

  log(1/a_n) ~ 2d · n log n + O(n)   ⟺   ρ = limsup n log n / log(1/a_n) = 1/(2d).

Primary estimator: direct 4-parameter least squares L_n = c₂·ln(n!) + c₁·n + c₀·ln n + c, reading c₂ → 2d.

| family | d | 2d (direct LS) | ρ = 1/(2d) |
|---|---|---|---|
| (1,0,1) | 2 | **4.0029** | **0.2498** |
| (1,0,5) | 2 | 4.003 | 0.2498 |
| (1,3,2) | 2 | 4.00 | 0.250 |
| b=k+1   | 1 | 2.0075 | 0.498 |
| b=k³+1  | 3 | 6.00 | 0.167 |

Output: `out/order_coefficients_result.json`
sha256 `17db7b85e8347f0df2788a9842056bcf47b27c71c016932e9f21111c6cb94fc2`.

## A1 cross-check — Eigenvalue route (convergence exponent)

`eigenvalue_route.py`: R∞(λ)² = ∏_k(1 + λ s_k²), {s_k} = positive spectrum of the Jacobi operator T
(zero diagonal, off-diagonal √u_{j+1}; P0 convention). The canonical product's order = convergence exponent
of its zeros λ_k = −1/s_k², i.e. ρ_prod = inf{ t : Σ s_k^{2t} < ∞ } = 1/p when s_k² ~ c k^{−p}.
Curvature-corrected log–log fit (log s_k = −d log k + c₀ + c₁/k + c₂/k²):

| family | d_corr | p_corr = 2d_corr | ρ_prod = 1/p |
|---|---|---|---|
| (1,0,1) | **1.9997** | 3.9993 | **0.2500** |
| (1,0,5) | 2.0011 | 4.0022 | 0.2499 |
| (1,3,2) | 1.9997 | 3.9993 | 0.2500 |
| b=k+1   | 0.9999 | 1.9999 | 0.5000 |
| b=k³+1  | 2.9992 | 5.9985 | 0.1667 |

Output: `out/eigenvalue_route_result.json`
sha256 `119fa513b90d8ffa41862a91334e1b971b9cb069a65374eceaf3dad876da32a3`.

**A1 vs A1-cross-check agreement (the required evidence):** for (1,0,1) the coefficient route gives
ρ = 0.2498 and the eigenvalue route gives ρ_prod = 0.2500; both → 1/4. Agreement holds across d = 1, 2, 3.
The two routes are independent (one reads the power-series coefficients, the other the operator spectrum),
so their agreement is the falsification-surviving evidence for ρ = 1/(2d).

## A2 — Genus

Zeros of R∞(λ)² are λ_k = −1/s_k². Genus p\* = smallest integer with Σ_k |1/λ_k|^{p\*+1} = Σ_k s_k^{2(p\*+1)} < ∞.
Already at p\* = 0: Σ_k s_k² = Tr T² = S = Σ_{n≥2} u_n < ∞ (trace-class). Numerically
Σ s_k² (spectral) = 0.13066962 matches S = Σ u_n (direct) = 0.13066962 to 8 digits ⇒ the spectral sum is the
trace and converges. Hence **genus p\* = 0**, and the Hadamard factorisation carries **no exponential factor**:

  **R∞(λ)² = ∏_{k≥1} (1 + λ s_k²).**

Grade: STRUCTURAL — rests only on Σuₙ < ∞ (trace-class T²), which is independent of the sharp order.

## A3 — Rigorous bounds (by hand), graded separately from the sharp order

Let u_i ~ i^{−2d} (since b(k) ~ A k^d_poly with poly-degree giving u_i = 1/(b(i−1)b(i)) ~ A^{−2} i^{−2d};
"d" here is the entire-order index 2d = 2·polydeg, polydeg = 2 for the running quadratic b).

- **LOWER (ρ ≥ 1/(2d)), elementary.** a_n ≥ T_n := ∏_{k=1}^n u_{2k}, the single dominant sparse term on the
  no-two-consecutive index set {2,4,…,2n}. With u_{2k} ~ (2k)^{−2d}: log(1/T_n) ~ 2d·n log n, so
  ρ = limsup n log n / log(1/a_n) ≥ 1/(2d). **PROVEN-by-hand** (one inequality, elementary).

- **UPPER (ρ ≤ 1/(2d)), via the canonical product.** a_n ≤ e_n := the elementary-symmetric coefficient,
  i.e. the coefficient of λ^n in ∏_{i≥2}(1 + λ u_i) (drops the sparsity constraint, an overcount). That
  product is a canonical product whose order equals the convergence exponent of its zeros {−1/u_i}, namely
  inf{ t : Σ u_i^t < ∞ } = 1/(2d) (because u_i ~ i^{−2d}). By the standard canonical-product / Hadamard
  theorem, the entire function Σ e_n λ^n has order 1/(2d), so a_n ≤ e_n forces ρ ≤ 1/(2d). **STRUCTURAL**
  (cites the standard canonical-product order theorem; not re-proved here).

  Trivial slack bound for entire-ness: a_n ≤ (Σ_i u_i)^n / n! = S^n/n! ⇒ Σ a_n λ^n is dominated by exp(S|λ|),
  so R∞ is entire of order ≤ 1 unconditionally. (Stated as the cheap rigorous floor; the sharp bound above
  pulls it down to 1/(2d).)

- **Conclusion.** ρ = 1/(2d) is bracketed by two by-hand bounds (lower elementary, upper via canonical
  product). The **equality** (vs strict <) and the precise constant are corroborated by the eigenvalue
  convergence exponent (zeros λ_k = −1/s_k², s_k ~ k^{−d_poly}) — VERIFIED-numerical. Grades: rigorous
  bracket = PROVEN-by-hand (lower) + STRUCTURAL (upper); sharp value ρ = 1/(2d) = VERIFIED-numerical
  (two agreeing routes). It is NOT reported as PROVEN-machine-checked.

**A1-vs-A3 self-consistency:** the by-hand bracket [1/(2d), 1/(2d)] (A3) brackets exactly the numerically
fitted ρ = 0.2498 / 0.2500 (A1, both routes). Consistent. ✔

---

## Theorem-4 soft spot — S = Σ_{n≥2} u_n < 1

`thm4_S.py` (dps 80, analytic tail).

- **Rigorous telescoping bound (PROVEN-by-hand).** Since
  u_k = 1/(b(k−1)b(k)) = [1/(b(k)−b(k−1))]·(1/b(k−1) − 1/b(k)) and b(k)−b(k−1) = A(2k−1)+B ≥ 3A+B for k≥2
  (the gap is increasing), summing the telescope gives
  **S ≤ 1/((3A+B)·b(1)) = 1/((3A+B)(A+B+C)).**
  Hence a clean **sufficient condition for S < 1: (3A+B)(A+B+C) > 1.**

- **Running family (1,0,1):** S = 0.130669618987432469653… (matches the P0 certified value to 22 digits,
  |S−S_P0| = 5.2e-22), bound 1/((3)(2)) = 1/6 ≈ 0.1667 ≥ S ✔, sufficient product = 6 > 1 ✔. S < 1 with a
  factor-~8 margin.

- **Other families:** (1,0,5) S=0.0336, (1,3,2) S=0.0217, (2,1,3) S=0.0181 — all < 1, all certified by the
  sufficient condition.

- **Falsification (important):** S < 1 is **NOT universal**. Degenerate small-leading-coefficient triples
  violate it: (A,B,C) = (0.01, 0, 1) gives **S = 6.844 > 1** (sufficient product = 0.0303 < 1, so the bound
  correctly declines to certify it). So S < 1 is not a universal property of all degree-2 b; it must be
  *scoped*, not merely caveated (next bullet).

- **Integer-regime resolution (the scoping, not just a caveat).** On the integer lattice the note actually
  studies — A,C ∈ ℤ≥1, B ∈ ℤ≥0 — the bound is *uniform*: (3A+B) ≥ 3 and (A+B+C) ≥ 2, so
  (3A+B)(A+B+C) ≥ 6 and **S ≤ 1/6 < 1 unconditionally**. Verified over the 125-triple grid A,C∈{1..5},
  B∈{0..4}: every S ≤ 1/6, and the **maximum S = 0.1307 is attained at the running family (1,0,1)** — the
  extremal lattice point. Theorem 4 is therefore stated **unconditionally on the integer family** (uniform
  S ≤ 1/6) and **conditionally — (3A+B)(A+B+C) > 1 — for general real b**, with (0.01,0,1) the genuine
  out-of-regime failure.

Output: `out/thm4_S_result.json` sha256 `33eb39329951a3b5226cdc9ae33aafb4509a51574b53ae934d6dc59f7935f4ee`.

---

## Corrected Proposition 5 (paste-ready)

> **Proposition 5 (entire order and genus).** The function R∞(λ) = Σ_{S} ∏_{i∈S} λ u_i, the sum taken over
> finite sparse (no two consecutive) subsets S ⊆ {2, 3, …} with u_i = 1/(b(i−1) b(i)) and b a degree-2
> polynomial with b(k) ~ A k² (k → ∞), is entire of order ρ = 1/(2d) with d = 2, i.e. **ρ = 1/4**, and of
> **genus 0**. Equivalently, writing {s_k} for the positive spectrum of the associated Jacobi operator T,
>
>   **R∞(λ)² = ∏_{k≥1} (1 + λ s_k²),**
>
> a genus-0 Hadamard product with no exponential factor, convergent because Σ_k s_k² = Tr T² = S < ∞.
>
> *Bounds.* The lower bound ρ ≥ 1/4 follows from the single dominant sparse term ∏_{k≤n} u_{2k} (indices
> 2,4,…,2n), giving log(1/a_n) ~ 4 n log n. The upper bound ρ ≤ 1/4 follows from a_n ≤ e_n, the coefficients
> of the canonical product ∏_{i≥2}(1 + λ u_i), whose order equals the convergence exponent inf{t : Σ u_i^t <
> ∞} = 1/4 of its zeros. The sharp equality ρ = 1/4 is confirmed numerically by two independent routes
> (coefficient decay and the s_k² ~ k^{−4} eigenvalue convergence exponent), which agree to three digits.

(For general polynomial degree d_poly the statement reads ρ = 1/(2 d_poly); the running family has d_poly = 2.)

### Downstream sentences to change in delta_fredholm_note.md (Phase-B B0 edit list)

1. **Abstract** — wherever it says "order at most 1/(2d)": change to "order exactly 1/(2d) (= 1/4), genus 0".
2. **Status block (four-class)** — order: VERIFIED-numerical + STRUCTURAL bracket; genus: STRUCTURAL;
   the rigorous ρ ≤ 1 floor: PROVEN-by-hand. Do NOT grade the sharp ρ = 1/4 as PROVEN.
3. **Proposition 5 body** — replace with the paste-ready text above; **delete any "× (exponential factor)"
   / "(…)" placeholder** in the Hadamard product (genus 0 ⇒ none).
4. **Theorem 4 line** — DONE (B0). Stated **unconditionally on the integer family** A,C≥1,B≥0 via the
   uniform bound S ≤ 1/6 (since (3A+B)(A+B+C) ≥ 6); **conditionally** via (3A+B)(A+B+C) > 1 for general real
   b; Remark records (0.01,0,1): S ≈ 6.84 as the out-of-regime failure. Telescoping bound + grid check
   (125 integer triples, max S at (1,0,1)) back it.
5. **Any sentence asserting Prop 5 / Theorem 4 are PROVEN** — they are STRUCTURAL/VERIFIED; only Lean
   Theorems 1 & 2 (T_DET, T_COMB) are PROVEN-machine-checked.

---

## Four-class grade per piece

- ρ ≤ 1 (entire): **PROVEN-by-hand** (a_n ≤ Sⁿ/n!).
- ρ ≥ 1/(2d) (lower): **PROVEN-by-hand** (dominant sparse term).
- ρ ≤ 1/(2d) (upper): **STRUCTURAL** (canonical-product order theorem, cited).
- ρ = 1/(2d) sharp value: **VERIFIED-numerical** (two agreeing independent routes, dps 220 / curvature-corrected spectral fit).
- genus p\* = 0: **STRUCTURAL** (Σ s_k² = S < ∞).
- Hadamard product no exp factor: **STRUCTURAL** (follows from genus 0).
- S ≤ 1/((3A+B)(A+B+C)): **PROVEN-by-hand** (telescoping).
- S ≤ 1/6 uniform on the integer family A,C≥1,B≥0: **PROVEN-by-hand** (bound denominator ≥ 6, extremum at (1,0,1)) + **VERIFIED** (125-triple grid).
- S(1,0,1) = 0.1307 < 1: **VERIFIED** (matches P0 to 22 digits).
- S < 1 universal: **FALSIFIED** (counterexample (0.01,0,1)).

**Gate A4 PASS:** A1 (coeff) and A1-cross-check (eigenvalue) agree; A1 numeric brackets sit inside the A3
by-hand bracket; self-consistent. Phase B may proceed.
