# Sorry Inventory — GOLDBACH-HELFGOTT-C1

Build: `lake build GoldbachHelfgott` ⇒ **success** (684/684 jobs).
All five modules type-check; `#check` smoke-tests in `Main.lean`
print the expected signatures.

Three scope-bounded gaps are documented below.  None of them is a
hidden `sorry` in a theorem body — `sorry_1` is exposed as an
explicit hypothesis of the bridge theorem, `sorry_2` and `sorry_3`
are exposed as named `axiom`s.  This matches the
`congruent-relay` convention: every gap is visible at the type
level and tagged AEAL `near_miss`.

---

## sorry_1 — prime-splitting sub-claim  (RESEARCH TARGET)

**Location.** `Reduction.lean`, definition `TernaryToBinaryAbove`
and hypothesis `hsplit` of `goldbach_from_helfgott_and_cert`.

**Statement.**
```
def TernaryToBinaryAbove (N₀ : ℕ) : Prop :=
  ∀ n : ℕ, N₀ ≤ n → Even n → 4 ≤ n → ∃ p q, IsGoldbachPair p q n
```

**Why it is not a logical consequence of Helfgott alone.**
Given even `n ≥ N₀ ≥ 4`, decompose `n = 3 + (n-3)` with `n-3` odd
and (for `N₀ ≥ 10`) at least 7.  Helfgott gives primes `p, q, r`
with `p + q + r = n - 3`, hence
`n = 3 + p + q + r`.  This is a *quaternary* decomposition.
Collapsing 4 → 2 primes requires an extra ingredient that
Helfgott does not provide: e.g.

  (a) the existence of a triple `(p,q,r)` with `3 ∈ {p,q,r}` *and*
      one of the remaining two summing with the third to a
      Goldbach partner of 3, or
  (b) a Chen / Vinogradov style control of the smallest prime in
      a ternary representation.

`TernaryToBinaryAbove` is therefore the precise mathematical
content of the bridge in the high-`n` regime and is the deliverable
of future relay sessions.

**AEAL class.** `near_miss` (research target, not claimed solved).

**Discharge plan.** Investigated in subsequent relay session
(`GOLDBACH-HELFGOTT-CN-…`); independent of `sorry_2`.

---

## sorry_2 — computational certificate up to N₀

**Location.** `Certificate.lean`, axiom `goldbach_certificate_N₀`.

**Statement.**
```
axiom goldbach_certificate_N₀ : goldbach_verified_below N₀
-- where N₀ : ℕ := 100000
```

**Status.** Explicit scope boundary.  To be discharged by relay
session **GOLDBACH-HELFGOTT-C2** (computational verification),
either by `decide` over a hard-coded witness table, or by
reflection of an externally produced SAT/SMT certificate.

**AEAL class.** `near_miss` (deferred to dedicated session).

---

## sorry_3 — Helfgott's ternary Goldbach theorem

**Location.** `Statement.lean`, axiom `helfgott_ternary`.

**Statement.**
```
axiom helfgott_ternary : ∀ k : ℕ, TernaryGoldbach k
```

**Status.** Imported from the literature
(Helfgott, *The ternary Goldbach problem*, 2013).
Reproving it is explicitly out of scope per the relay prompt
(Searcher's-Fatigue guard).

**AEAL class.** `independently_verified` (published, peer-reviewed
result imported as axiom).

---

## Compilation evidence

```
$ lake build GoldbachHelfgott
✔ [679/684] Built GoldbachHelfgott.Basic
✔ [680/684] Built GoldbachHelfgott.Statement
✔ [681/684] Built GoldbachHelfgott.Certificate
✔ [682/684] Built GoldbachHelfgott.Reduction
ℹ [683/684] Built GoldbachHelfgott.Main
info: goldbach_conditional :
  TernaryToBinaryAbove N₀ → ∀ (n : ℕ), StrongGoldbach n
info: goldbach_from_helfgott_and_cert :
  ∀ (N₀ : ℕ), 4 ≤ N₀ →
    goldbach_verified_below N₀ → (∀ (k : ℕ), TernaryGoldbach k) →
    TernaryToBinaryAbove N₀ → ∀ (n : ℕ), StrongGoldbach n
Build completed successfully (684 jobs).
```

`grep -n "sorry" GoldbachHelfgott/*.lean` ⇒ no matches.
The three gaps above are all `axiom` declarations or named
hypotheses, surfaced at the type level.

---

## Convention alignment with `congruent-relay`

| Aspect                          | congruent-relay         | GOLDBACH-HELFGOTT-C1     |
|---------------------------------|-------------------------|--------------------------|
| Visible-axiom convention        | ✓ (Tunnell, BSD)        | ✓ (Helfgott, certificate)|
| Sorry count in theorem bodies   | 0                       | 0                        |
| Research target as named lemma  | ✓                       | ✓ (`TernaryToBinaryAbove`)|
| AEAL `near_miss` tagging        | ✓                       | ✓                        |
