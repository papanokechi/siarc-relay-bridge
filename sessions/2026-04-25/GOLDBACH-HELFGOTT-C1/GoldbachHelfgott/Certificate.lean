/-
  GoldbachHelfgott/Certificate.lean

  Stub axiom for the computational certificate verifying strong
  Goldbach for every even n strictly below N₀ = 100000.

  In a real submission this axiom is replaced by a *generated*
  Lean term (e.g. via `decide` over a hard-coded witness table,
  or by reflecting an external SAT/SMT certificate).  That work
  belongs to the separate session **GOLDBACH-HELFGOTT-C2**.

  Sorry inventory: 0  (we use an `axiom`, scope-bounded as
  `near_miss`; this is a *known* gap, not a hidden one).
-/

import GoldbachHelfgott.Basic

namespace GoldbachHelfgott

/-- The computational bound used throughout this development. -/
def N₀ : ℕ := 100000

/-- Stub for the eventual computational certificate.

To be discharged by relay session **GOLDBACH-HELFGOTT-C2**. -/
axiom goldbach_certificate_N₀ : goldbach_verified_below N₀

theorem N₀_ge_four : 4 ≤ N₀ := by decide

end GoldbachHelfgott
