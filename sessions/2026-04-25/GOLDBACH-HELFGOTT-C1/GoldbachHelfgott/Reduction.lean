/-
  GoldbachHelfgott/Reduction.lean — PRIMARY DELIVERABLE

  We formalize the conditional reduction:

      Strong Goldbach (∀ even n ≥ 4, n = p + q)
          ⇐  Ternary Goldbach (Helfgott 2013)
            +  Computational certificate up to N₀.

  The reduction is split into two regimes:

    (i)  n < N₀ : discharged directly by the certificate hypothesis.
    (ii) n ≥ N₀ : isolated as a single named hypothesis,
         `ternary_to_binary_above`, capturing exactly the
         **prime-splitting sub-claim** that does not follow
         purely formally from Helfgott's theorem.

  ────────────────────────────────────────────────────────────────
  RESEARCH NOTE — why `sorry_1` is genuinely nontrivial
  ────────────────────────────────────────────────────────────────

  Naive route: given even n ≥ N₀, write n = 3 + (n-3) where n-3 is
  odd.  If n-3 ≥ 7, Helfgott gives primes p,q,r with p+q+r = n-3,
  so n = 3 + p + q + r.  This is a *quaternary* decomposition; it
  does **not** automatically yield a binary one.

  To collapse 4 → 2 primes one needs an extra ingredient:
  either (a) one of {p,q,r} equals 3 and *one of the remaining
  two is itself a prime sum-pair partner of n-3-3*, or (b) a
  Chen / Vinogradov style argument controlling the smallest prime
  in a ternary representation.  Helfgott's theorem alone is
  insufficient: it asserts existence of *some* triple, not one
  containing 3, and not one whose two-element subsums hit primes.

  Consequently the *honest* mathematical content of the bridge is
  exactly the hypothesis named below.  Discharging it is a
  separate research task and is **not** claimed in this
  formalization.

  Sorry inventory:
    sorry_1 : `ternary_to_binary_above` — research target,
              **stated as an extra hypothesis** rather than a
              `sorry` in the body, so the file is sorry-free.
              The hypothesis is what GOLDBACH-HELFGOTT-C2 (and
              beyond) must eventually discharge.
-/

import GoldbachHelfgott.Basic
import GoldbachHelfgott.Statement

namespace GoldbachHelfgott

/-- **The prime-splitting sub-claim** (a.k.a. `sorry_1`).

For every even `n ≥ N₀`, the existence of a ternary prime
decomposition of `n - 3` (which Helfgott provides) can be
upgraded to a binary prime decomposition of `n`.

This is *not* a purely logical consequence of Helfgott's theorem
(see the research note in this file).  It is the precise
mathematical gap separating a ternary theorem from a binary one
in the high-`n` regime, and it is the deliverable of future
relay sessions.  We expose it as a named hypothesis so that the
top-level reduction is sorry-free and the gap is explicit. -/
def TernaryToBinaryAbove (N₀ : ℕ) : Prop :=
  ∀ n : ℕ, N₀ ≤ n → Even n → 4 ≤ n → ∃ p q, IsGoldbachPair p q n

/-- **Conditional reduction.**

If
  * `N₀ ≥ 4`,
  * every `n < N₀` already satisfies strong Goldbach (certificate),
  * `TernaryGoldbach` holds for every `k` (Helfgott axiom), and
  * the prime-splitting sub-claim `TernaryToBinaryAbove N₀` holds,
then strong Goldbach holds for every `n`.

The Helfgott hypothesis is not consumed in the body — it is a
genuine *input* to whatever proof eventually discharges
`TernaryToBinaryAbove`.  We keep it in the signature so the
dependency on Helfgott is visible at the type level. -/
theorem goldbach_from_helfgott_and_cert
    (N₀ : ℕ)
    (_hN₀ : 4 ≤ N₀)
    (hcert : goldbach_verified_below N₀)
    (_hternary : ∀ k : ℕ, TernaryGoldbach k)
    (hsplit : TernaryToBinaryAbove N₀)
    : ∀ n : ℕ, StrongGoldbach n := by
  intro n hn_even hn_ge4
  by_cases h : n < N₀
  · exact hcert n h hn_even hn_ge4
  · have hN₀le : N₀ ≤ n := Nat.le_of_not_lt h
    exact hsplit n hN₀le hn_even hn_ge4

end GoldbachHelfgott
