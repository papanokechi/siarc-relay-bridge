/-
  GoldbachHelfgott/Main.lean

  Top-level assembly.  Combines:
    * `helfgott_ternary`            (Statement.lean,    axiom)
    * `goldbach_certificate_N₀`     (Certificate.lean,  axiom stub)
    * `TernaryToBinaryAbove N₀`     (Reduction.lean,    research hypothesis)
  to obtain conditional strong Goldbach.

  Sorry inventory: 0
-/

import GoldbachHelfgott.Basic
import GoldbachHelfgott.Statement
import GoldbachHelfgott.Reduction
import GoldbachHelfgott.Certificate

namespace GoldbachHelfgott

/-- **Conditional strong Goldbach.**

Given the prime-splitting hypothesis `TernaryToBinaryAbove N₀`
(the genuine research target — see `Reduction.lean`), strong
Goldbach holds for every natural number, with Helfgott's theorem
and the computational certificate up to `N₀ = 100000` as inputs. -/
theorem goldbach_conditional
    (hsplit : TernaryToBinaryAbove N₀) :
    ∀ n : ℕ, StrongGoldbach n :=
  goldbach_from_helfgott_and_cert
    (N₀ := N₀)
    N₀_ge_four
    goldbach_certificate_N₀
    helfgott_ternary
    hsplit

#check @goldbach_conditional
#check @goldbach_from_helfgott_and_cert
#check @TernaryToBinaryAbove
#check @StrongGoldbach
#check @TernaryGoldbach
#check @helfgott_ternary
#check @goldbach_certificate_N₀

end GoldbachHelfgott
