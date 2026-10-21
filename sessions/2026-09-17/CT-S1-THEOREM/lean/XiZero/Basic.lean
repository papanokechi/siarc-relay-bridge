/-
  XiZero.Basic — Lean 4 scoping skeleton for P4 Task B.

  Session: CT-S1-THEOREM.  Statement of part (i) of `theorem.tex`
  (Theorem `thm:radius`), with a proof skeleton carrying one `sorry`
  per gap.  THIS IS SCOPING ONLY: no gap is discharged here.

  Governance: this file is expected to build with `sorry` warnings.
  A `sorry`-free build is NOT claimed.
-/
import Mathlib

namespace XiZero

open Filter Polynomial
open scoped Topology Nat

/-! ## Setting -/

/-- The recurrence `Q n = b n * Q (n-1) + Q (n-2)`, with `Q (-1) = 0`, `Q 0 = 1`.
Shifting so that indices are natural numbers, `Q 1 = b 1`. -/
noncomputable def Q (b : ℕ → ℂ) : ℕ → ℂ
  | 0       => 1
  | 1       => b 1
  | (n + 2) => b (n + 2) * Q b (n + 1) + Q b n

/-- The dominant scale `B n = ∏_{k=1}^n b k`. -/
noncomputable def B (b : ℕ → ℂ) (n : ℕ) : ℂ := ∏ k ∈ Finset.Icc 1 n, b k

/-- `r n = Q n / B n`. -/
noncomputable def r (b : ℕ → ℂ) (n : ℕ) : ℂ := Q b n / B b n

/-- Hypothesis (A1): `b k ≠ 0` for every integer `k ≥ 1`. -/
def Nonvanishing (b : ℕ → ℂ) : Prop := ∀ k, 1 ≤ k → b k ≠ 0

/-! ## Proposition `prop:exists` — the limit always exists -/

/-- `r` satisfies `r n = r (n-1) + r (n-2) / (b (n-1) * b n)`.
Gap L1: pure algebra from `Q` and `B`, using (A1) to divide. -/
theorem r_rec (b : ℕ → ℂ) (hb : Nonvanishing b) (n : ℕ) (hn : 2 ≤ n) :
    r b n = r b (n - 1) + r b (n - 2) / (b (n - 1) * b n) := by
  sorry

/-- Existence of `r_∞`, unconditional given (A1) and `deg b = d ≥ 1`.
Gap L2: the three sub-steps of `prop:exists` — boundedness of `r`,
summability of `1 / |b (n-1) * b n|` (needs `|b n| ≥ c * n ^ d` eventually),
and absolute convergence of the telescoping series. -/
theorem exists_rinf (p : Polynomial ℂ) (hp : 1 ≤ p.natDegree)
    (hb : Nonvanishing fun k => p.eval (k : ℂ)) :
    ∃ L : ℂ, Tendsto (r fun k => p.eval (k : ℂ)) atTop (𝓝 L) := by
  sorry

/-- Proposition `prop:positive`: if `b n > 0` for all `n ≥ 1` then (H) holds.
Gap L3: induction showing `r` is real, strictly increasing, and `≥ 1`. -/
theorem rinf_ne_zero_of_pos (b : ℕ → ℂ)
    (hpos : ∀ k, 1 ≤ k → 0 < (b k).re ∧ (b k).im = 0)
    (L : ℂ) (hL : Tendsto (r b) atTop (𝓝 L)) : L ≠ 0 := by
  sorry

/-! ## Theorem `thm:radius` — part (i) -/

/-- **Step 2** of the proof: `‖B n / (n !) ^ d‖ ^ (1/n) → ‖β_d‖`.
Gap L4: `log ‖u k‖ = O(1/k)` and `∑_{k ≤ n} 1/k = O(log n)`; no Stirling. -/
theorem root_B_div_factorial_pow (p : Polynomial ℂ) (hp : 1 ≤ p.natDegree)
    (hb : Nonvanishing fun k => p.eval (k : ℂ)) :
    Tendsto (fun n : ℕ =>
        ‖B (fun k => p.eval (k : ℂ)) n / ((n ! : ℂ) ^ p.natDegree)‖ ^ ((1 : ℝ) / n))
      atTop (𝓝 ‖p.leadingCoeff‖) := by
  sorry

/-- **Step 3** of the proof: `((d * n)! / (n !) ^ d) ^ (1/n) → d ^ d`.
Purely combinatorial via the multinomial bounds
`d ^ (d * n) / (d * n + 1) ^ (d - 1) ≤ (d * n)! / (n !) ^ d ≤ d ^ (d * n)`.
Gap L5.  (Mathlib's `Stirling.factorial_isEquivalent_stirling` is an
alternative route, but the LaTeX proof deliberately avoids Stirling.) -/
theorem root_multinomial (d : ℕ) (hd : 1 ≤ d) :
    Tendsto (fun n : ℕ => (((d * n)! : ℝ) / ((n ! : ℝ) ^ d)) ^ ((1 : ℝ) / n))
      atTop (𝓝 ((d : ℝ) ^ d)) := by
  sorry

/-- **Theorem (i), the radius.**
`lim ‖Q n / (d * n)!‖ ^ (1/n) = ‖β_d‖ / d ^ d`, under (A1) and (H). -/
theorem radius (p : Polynomial ℂ) (hp : 1 ≤ p.natDegree)
    (hb : Nonvanishing fun k => p.eval (k : ℂ))
    (L : ℂ) (hL : Tendsto (r fun k => p.eval (k : ℂ)) atTop (𝓝 L)) (hL0 : L ≠ 0) :
    Tendsto (fun n : ℕ =>
        ‖Q (fun k => p.eval (k : ℂ)) n / ((p.natDegree * n)! : ℂ)‖ ^ ((1 : ℝ) / n))
      atTop (𝓝 (‖p.leadingCoeff‖ / (p.natDegree : ℝ) ^ p.natDegree)) := by
  -- Step 1: `Q n = r n * B n` and `‖r n‖ ^ (1/n) → 1`, using (H).
  -- Step 4: combine Steps 1-3.
  sorry

/-- **Step 5 / Corollary**: Cauchy-Hadamard restatement.
The Borel-type series `∑ Q n * w ^ n / (d * n)!` has radius `d ^ d / ‖β_d‖`.
Gap L6: transport `radius` through `FormalMultilinearSeries.radius_eq_liminf`
(confirmed present: `Mathlib/Analysis/Analytic/RadiusLiminf.lean`). -/
theorem borel_radius (p : Polynomial ℂ) (hp : 1 ≤ p.natDegree)
    (hb : Nonvanishing fun k => p.eval (k : ℂ))
    (L : ℂ) (hL : Tendsto (r fun k => p.eval (k : ℂ)) atTop (𝓝 L)) (hL0 : L ≠ 0) :
    Tendsto (fun n : ℕ =>
        (‖Q (fun k => p.eval (k : ℂ)) n / ((p.natDegree * n)! : ℂ)‖ ^ ((1 : ℝ) / n))⁻¹)
      atTop (𝓝 ((p.natDegree : ℝ) ^ p.natDegree / ‖p.leadingCoeff‖)) := by
  sorry

end XiZero
