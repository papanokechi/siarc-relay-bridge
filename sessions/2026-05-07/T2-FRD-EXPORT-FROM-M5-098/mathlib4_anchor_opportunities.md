# Mathlib4 anchor opportunities — M5 FRDs (relay 098 Phase E.E3)

**Generated:** 2026-05-07
**Scope:** For each FRD in [m5_frds.lean](m5_frds.lean), identify the
Mathlib4 module that would house the canonical version of the
underlying mathematical object, plus any candidate Mathlib4 PR
opportunity. This is the forward-link to M10 fires + Mathlib4
contributor papers.

This file does not perform live arXiv / DOI verification (none of
the M5 FRDs cite external bibliographic identifiers; per relay
spec the post-031 rule does not gate this fire). Mathlib4 module
paths are based on the Mathlib4 module organization at the time
of writing (Mathlib4 4.14.x; substantive paths may shift).

---

## Anchor table

| FRD | Lean object | Closest Mathlib4 anchor | Status |
|-----|-------------|-------------------------|--------|
| B1 | `VQuad` | None (project-specific structure) | NEW; no upstream candidate |
| B1 | `VQuad.aPoly` / `bPoly` | `Mathlib.Algebra.Polynomial.Eval` (`Polynomial.eval`) | use directly when proof bodies require polynomial evaluation lemmas |
| B2 | `Stratum` | None (project-specific tag) | NEW |
| B2 | `R` ratio | `Mathlib.Data.Rat.Defs` (`HDiv.hDiv`) | use directly |
| B3 | `indicialPoly` | `Mathlib.Algebra.Polynomial.Basic` (`Polynomial`) | refactor candidate; current encoding is `ℚ → ℚ` not `Polynomial ℚ` |
| B3 | `doubleRootCondition` | `Mathlib.Algebra.Polynomial.Roots` (`Polynomial.roots`) | use as predicate via root multiplicity |
| B3 | `indicialDiscriminant` | `Mathlib.Algebra.Polynomial.Discriminant` (if exists) or `Mathlib.RingTheory.Discriminant` | candidate Mathlib4 PR if quadratic discriminant lemma is missing |
| B4 | `StokesData` | None (project-specific) | NEW |
| B4 | `stratumOf` | None | inherently project-specific |
| B4 | `stokes` | `Mathlib.Analysis.Asymptotics.*` (Borel summation modules) | open Mathlib4 question; Borel-summability infrastructure is currently sparse in Mathlib4 |
| B5 | `zetaStar` | `Mathlib.NumberTheory.Cyclotomic.Basic` (algebraic numbers) or `Mathlib.Analysis.SpecificLimits.Normed` | algebraic real anchor |
| B6 | `PCFLimit` | `Mathlib.Algebra.ContinuedFractions.Basic` (existence) or `Mathlib.NumberTheory.ContinuedFractions.Basic` (depending on naming) | direct use; verify exact module path during M10-PROOF-DRAFT |
| B7 | `M8b_axis_residual_acceptance` | `Mathlib.Analysis.Asymptotics.Asymptotics` (asymptotic predicates) | statement-level only |
| B8 | `wallisStep` / `wallisP` | `Mathlib.Algebra.LinearRecurrence` (linear recurrence relations) | direct candidate; `Mathlib.Algebra.LinearRecurrence` provides the abstract framework |
| B9 | `SpecK` | None (project-specific 5-tuple) | NEW |

---

## Per-FRD Mathlib4 import recommendations

When `m5_frds.lean` is imported into a Lake-managed project, the
following Mathlib4 imports cover the per-FRD anchor needs:

```lean
-- Core (already in scaffold):
import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import Mathlib.Data.Rat.Defs

-- B1 / B3 polynomial layer:
import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Algebra.Polynomial.Eval

-- B6 continued fractions (verify exact module path):
-- import Mathlib.Algebra.ContinuedFractions.Basic
-- OR
-- import Mathlib.NumberTheory.ContinuedFractions.Basic

-- B8 linear recurrences:
import Mathlib.Algebra.LinearRecurrence

-- B5 algebraic numbers (when zetaStar body lands):
-- import Mathlib.NumberTheory.Cyclotomic.Basic
-- OR
-- import Mathlib.RingTheory.Algebraic
```

---

## Open Mathlib4 questions (for future M10 fires)

The following questions are out of scope for this relay but are
flagged as forward-pointers for the M10-PROOF-DRAFT fire:

1. **Continued-fraction module choice (B6).** Mathlib4 has had a
   continued-fraction layer since at least 4.0; its exact namespace
   has shifted (e.g. `GenContFract`, `ContinuedFraction`). The M10
   fire should verify the current path and choose between the
   abstract `GenContFract` and the more specific `SimpContFract`
   depending on whether the V_quad limit needs simple or
   generalized continued-fraction infrastructure.

2. **Borel-summability infrastructure (B4 + B7).** Mathlib4 currently
   does not have a robust Borel-summation API. A Mathlib4 PR
   contributing the Birkhoff-Trjitzinsky / Wimp-Zeilberger
   normal-case asymptotic-summation framework would be a substantial
   contribution; this is forward-pointed but NOT proposed in this
   fire.

3. **Discriminant of a quadratic over a commutative ring (B3).**
   Mathlib4's `Polynomial.discriminant` may or may not specialize
   cleanly to the quadratic case `a₁² - 4 a₂ a₀`. A small Mathlib4
   PR adding `Polynomial.discriminant_of_quadratic` would simplify
   B3's `doubleRootCondition` proof obligations.

4. **Algebraic-number subfield of ℝ (B5).** ζ_* = 4/√3 for V_quad
   is an algebraic real; Mathlib4 has `IsAlgebraic ℚ` but not a
   convenient embedding `(IsAlgebraic ℚ) → ℝ`. The M10 fire should
   choose between an explicit-real witness and an `IsAlgebraic`
   wrapper.

5. **Linear-recurrence Wallis specialization (B8).**
   `Mathlib.Algebra.LinearRecurrence` provides
   `LinearRecurrence` as a structure for constant-coefficient
   recurrences; the Wallis recurrence has *polynomial-in-n*
   coefficients, which falls outside this directly. The M10 fire
   may need to introduce `LinearRecurrenceWithPolynomialCoeffs` or
   use `Function.iterate` as a workaround.

---

## Mathlib4 PR opportunity summary

Of the 9 FRDs, **3** (B3 quadratic discriminant; B6 continued-fraction
module choice; B8 polynomial-coefficient linear recurrence) suggest
non-trivial Mathlib4 contributions. None are proposed in this
fire. They are forward-pointers for downstream M10-PROOF-DRAFT
fires.

The remaining 6 FRDs (B1, B2, B4, B5, B7, B9) do not require
Mathlib4 PRs; they are project-specific structures that consume
Mathlib4 anchors via existing modules.

---

## Bibliographic identifier audit

Per relay-098 PRE-VERIFICATION section:

> NEW arXiv / DOI identifiers cited in this fire: NONE.

This file does not cite external bibliographic identifiers. The
forward-link clause applies to M10-PROOF-DRAFT, which may cite
Mathlib4 contributor papers (e.g. for Borel-summability PRs); those
identifiers will require post-031 rule pre-verification at that
fire's draft time.

**Audit status for relay 098: N/A (no identifiers to pre-verify).**
