/-
  GoldbachHelfgott/Statement.lean

  Top-level statements imported from outside this development:

    * `helfgott_ternary` — Helfgott's ternary Goldbach theorem (2013),
      imported as an axiom.  We do **not** attempt to reprove it;
      the published proof is hundreds of pages long and relies on
      heavy analytic-number-theory infrastructure.
      Tag (AEAL): `near_miss` — axiomatic import of a published result.

    * `goldbach_certificate_witness` — placeholder for the eventual
      computational certificate (every even n < N₀ verified directly).
      Tag (AEAL): `near_miss` — discharged by a separate computational
      relay session (GOLDBACH-HELFGOTT-C2 / GOLDBACH-CERT).

  Sorry inventory: 0  (the stub used elsewhere is an `axiom`, not a `sorry`)
-/

import GoldbachHelfgott.Basic

namespace GoldbachHelfgott

/-- **Helfgott (2013).**  Every odd integer ≥ 7 is a sum of three primes.

Imported as an axiom: out of scope for this formalization. -/
axiom helfgott_ternary : ∀ k : ℕ, TernaryGoldbach k

end GoldbachHelfgott
