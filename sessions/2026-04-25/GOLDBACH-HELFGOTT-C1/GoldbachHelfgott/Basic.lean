/-
  GoldbachHelfgott/Basic.lean
  Definitions for the strong/ternary Goldbach reduction formalization.

  Sorry inventory: 0
-/

import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Algebra.Ring.Parity
import Mathlib.Data.Finset.Basic

namespace GoldbachHelfgott

/-- A pair of primes summing to `n`. -/
def IsGoldbachPair (p q n : ℕ) : Prop :=
  Nat.Prime p ∧ Nat.Prime q ∧ p + q = n

/-- Strong (binary) Goldbach: every even `n ≥ 4` is a sum of two primes. -/
def StrongGoldbach (n : ℕ) : Prop :=
  Even n → n ≥ 4 → ∃ p q, IsGoldbachPair p q n

/-- A triple of primes summing to `k`. -/
def IsTernaryGoldbachTriple (p q r k : ℕ) : Prop :=
  Nat.Prime p ∧ Nat.Prime q ∧ Nat.Prime r ∧ p + q + r = k

/-- Ternary Goldbach (Helfgott 2013): every odd `k ≥ 7` is a sum of three primes. -/
def TernaryGoldbach (k : ℕ) : Prop :=
  Odd k → k ≥ 7 → ∃ p q r, IsTernaryGoldbachTriple p q r k

/-- A computational certificate covering all even `n` strictly below `N₀`. -/
def goldbach_verified_below (N₀ : ℕ) : Prop :=
  ∀ n : ℕ, n < N₀ → StrongGoldbach n

end GoldbachHelfgott
