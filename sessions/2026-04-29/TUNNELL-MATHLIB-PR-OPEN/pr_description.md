# `Finset.card_even_of_involution` — Mathlib PR description

## Summary

Adds `Finset.card_even_of_involution` and two corollaries:

* `Finset.card_even_of_involution`: if `σ : α → α` maps `s : Finset α` into
  itself, is an involution on `s`, and has no fixed point in `s`, then
  `Even s.card`.
* `Finset.two_dvd_card_of_involution`: same conclusion phrased as `2 ∣ s.card`.
* `Finset.card_even_of_involutive`: convenience version when `σ` is a global
  `Function.Involutive`.

## Statement

```lean
theorem Finset.card_even_of_involution
    {α : Type*} [DecidableEq α]
    (s : Finset α) (σ : α → α)
    (hMem : ∀ x ∈ s, σ x ∈ s)
    (hInv : ∀ x ∈ s, σ (σ x) = x)
    (hFix : ∀ x ∈ s, σ x ≠ x) :
    Even s.card
```

## Motivation

This is the elementary combinatorial parity tool that powers orbit-pairing
arguments. It is used implicitly throughout Mathlib (sign-flip arguments in
matchings, orbit-counting in group actions, symmetrisation tricks), but
there is no clean library statement of it as far as we could find with a
local grep over `Mathlib/`.

The lemma arises naturally — and is currently re-proved in user code — in
the Lean 4 formalization of Tunnell's criterion for the Congruent Number
Problem (<https://github.com/papanokechi/tunnell-cnp-lean4>,
DOI 10.5281/zenodo.19834824). There the involution
`(x, y, z) ↦ (-x, -y, -z)` pairs the nonzero integer representations of
`n` by a positive-definite ternary quadratic form, hence their count is
even. The lemma itself involves no number theory and belongs upstream.

## Proof sketch

Strong induction on `s.card`:

1. If `s = ∅`, then `s.card = 0` is even.
2. Otherwise pick any `x ∈ s`. Then `σ x ∈ s` (by `hMem`) and `σ x ≠ x`
   (by `hFix`). The set `s' := (s.erase x).erase (σ x)` is a strict
   subset of `s` and inherits the three hypotheses (using that `σ` is an
   involution on `s` to verify `σ` maps `s'` into `s'`).
3. By the induction hypothesis `Even s'.card`, and
   `s.card = s'.card + 2`, so `Even s.card`.

## Hypothesis design

The three hypotheses are stated **pointwise on `s`** rather than as a
`Function.Involutive σ` global hypothesis. This is the strictly more useful
spelling because in practice the involution is often only defined or only
makes sense on the set itself (e.g. an involution on a finite group orbit
inside an infinite ambient type). A separate corollary
`Finset.card_even_of_involutive` is provided for the common case where the
involution is global.

## Location

`Mathlib.Data.Finset.Card` (or alternatively `Mathlib.Data.Fintype.Parity`,
since the latter is the natural home for parity facts about finite types).

## Dependencies

```lean
import Mathlib.Data.Finset.Card
import Mathlib.Algebra.Group.Even
import Mathlib.Logic.Function.Basic
```

No new dependencies are introduced.

## Compile verification

The standalone file at
`congruent-relay/mathlib-pr/CardEvenOfInvolution.lean` (126 lines)
compiles cleanly under Lean `v4.30.0-rc1` + Mathlib `v4.30.0-rc1`
(local toolchain at `lean/lean-toolchain`):

```
$ lake env lean CardEvenOfInvolution.lean
$ echo $?
0
```

## Closes

N/A (new addition).
