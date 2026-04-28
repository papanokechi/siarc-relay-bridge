# Handoff — TUNNELL-MATHLIB-PR-CANDIDATE
**Date:** 2026-04-29
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished
Read `congruent-relay/formal/CongruentStubs.lean` in full (954 lines, 30+ theorems/defs/axioms). Inventoried every named declaration with section/line/role. Filtered against the five PR-quality criteria (general / not in Mathlib / no sorry / small / useful) and ranked the survivors. Wrote a draft Mathlib PR description for the top candidate.

## Key numerical findings
- 954 total lines, 680 substantive proof lines, 170 Mathlib bridging lines.
- 0 `sorry` in the file (the only escape hatch is the named axiom `tunnell_conditional_on_BSD`).
- 1 axiom, 2 opaque defs (`AlgebraicRank`, `AnalyticRank`).
- 5 candidates inspected; 1 strong candidate, 2 secondary candidates, 2 rejects.

## Inventory of named declarations

| Name | Kind | Line | Section | Role |
|---|---|---|---|---|
| `IsSquarefree` | def | 70 | §1 | bridging |
| `solSet` | def | 88 | §1 | substantive |
| `repCount` | def | 102 | §1 | substantive |
| `repCount_neg` | thm | 112 | §2 | substantive |
| `repCount_nonneg` | thm | 120 | §2 | substantive |
| `solSet_neg_x` | thm | 134 | §2 | substantive |
| `solSet_neg_y` | thm | 148 | §2 | substantive |
| `solSet_neg_z` | thm | 162 | §2 | substantive |
| `solSet_mono` | thm | 188 | §3a | substantive |
| `solSet_card_mono` | thm | 202 | §3a | substantive |
| `coord_bound_of_sum_eq` | thm | 213 | §3a | substantive (general) |
| `solSet_sufficient_bound` | thm | 234 | §3a | substantive |
| `solSet_stable` | thm | 253 | §3a | substantive |
| `repCount_stable` | thm | 269 | §3a | substantive |
| `natAbs_neg_eq` | thm | 283 | §3b | bridging (already in Mathlib) |
| `solSet_sign_symmetry` | thm | 290 | §3b | substantive |
| `solSet_origin` | thm | 318 | §3b | substantive |
| `solSet∞` | def | 333 | §3c | substantive |
| `solSet_sub_solSet∞` | thm | 339 | §3c | substantive |
| `solSet∞_bounded` | thm | 351 | §3c | substantive |
| `solSet∞_finite` | thm | 367 | §3c | substantive (general) |
| `solSet_eq_solSet∞` | thm | 384 | §3c | substantive |
| `solSet_neg_closed` | thm | 408 | §4 | substantive |
| `neg_ne_self_of_ne_zero` | thm | 418 | §4 | substantive |
| `orbit_pair_distinct` | thm | 433 | §4 | substantive |
| `negTriple` | def | 445 | §4 | substantive |
| `negTriple_involution` | thm | 451 | §4 | substantive |
| `negTriple_no_nonzero_fixpoint` | thm | 458 | §4 | substantive |
| `negTriple_mem_solSet` | thm | 467 | §4 | substantive |
| `solSetNZ` | def | 481 | §4 | substantive |
| **`card_even_of_involution`** | **thm** | **518** | **§4** | **substantive (fully general)** |
| `solSetNZ_card_even` | thm | 591 | §4 | substantive |
| `repCount_parity_split` | thm | 624 | §4 | substantive |
| `repCount_even_of_pos` | thm | 660 | §4 | substantive |
| `tunnellCounts` | def | 683 | counting | bridging |
| `isCongruentTunnell` | def | 698 | counting | bridging |
| `isCongruentTunnell_iff` | thm | 706 | counting | bridging |
| `inTunnellDomain` | def | 715 | counting | bridging |
| `tunnellCounts_cases` | thm | 721 | counting | substantive |
| `thetaCoeff` | def | 740 | §5 | bridging |
| `thetaCoeff_eq_repCount` | thm | 749 | §5 | bridging |
| `thetaCoeff_nonneg` | thm | 754 | §5 | bridging |
| `thetaCoeff_neg` | thm | 760 | §5 | bridging |
| `thetaCoeff_eq_solSet∞_card` | thm | 770 | §5 | substantive |
| `tunnellThetaCoeffs` | def | 798 | §5 | bridging |
| `tunnellThetaCoeffs_eq_tunnellCounts` | thm | 808 | §5 | bridging |
| `IsCongruentNumber` | def | 822 | §6 | substantive (CNP-specific) |
| `OnCurveEn` | def | 832 | §6 | substantive (CNP-specific) |
| `AlgebraicRank` / `AnalyticRank` | opaque | 845 | §6 | axiom-side |
| `BSD_for` | def | 861 | §6 | axiom-side |
| `tunnell_conditional_on_BSD` | axiom | 884 | §6 | axiom |
| `tunnell_forward` | thm | 894 | §6 | substantive |
| `tunnell_reverse_under_BSD` | thm | 904 | §6 | substantive |

## Ranked candidate table

Score components, each on 1–5 (PR complexity: 5 = SMALL, 1 = LARGE).

| # | Candidate | Generality | Completeness | Mathlib fit | PR complexity | **Total / 20** |
|---|---|---|---|---|---|---|
| 1 | **`card_even_of_involution`** | 5 | 5 | 5 | 5 | **20** |
| 2 | `coord_bound_of_sum_eq` | 3 | 4 | 4 | 5 | 16 |
| 3 | `solSet∞_finite` (generalized) | 4 | 4 | 4 | 3 | 15 |
| 4 | `neg_ne_self_of_ne_zero` (over `Int^n`) | 3 | 5 | 3 | 5 | 16 |
| 5 | `negTriple_involution` | 2 | 5 | 2 | 5 | 14 |

Ranking justifications:

- **#1 `card_even_of_involution`** — Pure `Finset` combinatorics. Zero number-theoretic content. Self-contained proof by strong induction (~75 lines including comments). Natural home: `Mathlib.Data.Finset.Card` or `Mathlib.Data.Fintype.Parity`. A brief grep over the local Mathlib mirror found no equivalent (`FixedPointFree.lean` exists but is restricted to group automorphisms). Useful for any combinatorial parity argument (orbit counting, sign-pairing, etc.).
- **#2 `coord_bound_of_sum_eq`** — General fact about positive-definite forms: `a > 0 ∧ a*v² ≤ t ∧ t ≥ 0 → |v| ≤ |t|`. Useful but very small; might be more naturally absorbed into a stronger lemma.
- **#3 `solSet∞_finite`** — Finiteness of integer solutions to a positive-definite ternary form. Genuinely useful for number theory but mildly CNP-flavoured (only ternary). Generalization to `n`-ary diagonal forms turns this from SMALL to MEDIUM.
- **#4 `neg_ne_self_of_ne_zero`** — Trivial in ℤⁿ; likely already implied by Mathlib's `neg_ne_self` infrastructure. Low marginal value.
- **#5 `negTriple_involution`** — Too narrow; would not be accepted as standalone.

**Recommended top candidate: `card_even_of_involution`** (20/20).

## Top candidate

### Statement
```lean
theorem card_even_of_involution [DecidableEq α]
    (s : Finset α) (f : α → α)
    (hf_mem : ∀ x ∈ s, f x ∈ s)
    (hf_inv : ∀ x ∈ s, f (f x) = x)
    (hf_fix : ∀ x ∈ s, f x ≠ x) :
    Even s.card
```

Located at lines 518–569 in `congruent-relay/formal/CongruentStubs.lean`.

### Why it is general
The statement and proof reference no number theory whatsoever — only `Finset`, `DecidableEq`, and `Even`. The hypotheses can be summarized as:

> `f` restricts to a fixed-point-free involution on `s`.

This is the textbook lemma that powers countless parity arguments: sign-pairing in quadratic-form orbit counting, group-action orbit lengths, matching theory, sum-symmetrisation tricks, etc.

### Generalization needed before PR
Minor. The version in `CongruentStubs.lean` already takes `f : α → α` — there is no CNP hypothesis to remove. Possible polish for upstream:

1. Phrase via `Function.Involutive` over a `Subtype s`, or accept `Set.InvOn f f s s` instead of three separate hypotheses, to match Mathlib idiom. Both spellings are acceptable; reviewers may suggest one.
2. State a companion form `2 ∣ s.card` (already a one-line corollary via `Even.two_dvd`).
3. Add a `Fintype` corollary: `∀ s : Finset α … → 2 ∣ Fintype.card s` if useful.
4. Drop the `[DecidableEq α]` requirement if possible by using `Finset.erase` with classical decidability, or keep it (it's idiomatic).

None of these affect the proof body materially.

### Draft PR description

```
Title: Finset.card_even_of_involution: even cardinality from a
       fixed-point-free involution

This PR adds `Finset.card_even_of_involution`, which states:

  Let `s : Finset α` and `f : α → α` such that `f` maps `s` into
  itself, is an involution on `s` (`f (f x) = x` for `x ∈ s`),
  and has no fixed points in `s` (`f x ≠ x` for `x ∈ s`). Then
  `Even s.card`.

Motivation: This is a foundational combinatorial parity tool that
is used implicitly all over Mathlib (orbit pairing, sign-flip
arguments, matchings) but has no clean library statement. It arises
naturally in the formalization of Tunnell's criterion for the
Congruent Number Problem
(github.com/papanokechi/tunnell-cnp-lean4),
where it powers the proof that the number of nonzero integer
representations of n by a positive-definite ternary quadratic form
is even, but the lemma itself is purely about Finsets.

The proof is a clean strong induction on `s.card`: pick any element
`x`, observe `f x ∈ s` and `f x ≠ x`, erase both, and apply the IH
to the smaller set.

Dependencies: only `Mathlib.Data.Finset.Basic`, `Mathlib.Algebra.Parity`.
Suggested location: `Mathlib.Data.Finset.Card`
                    (or `Mathlib.Data.Fintype.Parity`).
A `2 ∣ s.card` corollary is included.

Closes: N/A (new addition)
```

## Estimated effort to open the PR

- Polish + restate using `Function.Involutive` / `Set.InvOn`: 30–60 min.
- Add corollaries (`2 ∣ s.card`, `Fintype` form): 20 min.
- Move into a freshly-cloned Mathlib branch, lint, name in `mathlib_check`, run `lake build` for the touched file: 60–90 min.
- Write CHANGELOG entry, open PR: 15 min.

**Total: half a day** (≤ 4 hours) for an experienced Mathlib contributor; up to a day for someone unfamiliar with the Mathlib PR workflow.

## Anomalies and open questions
- **Did not run `lake build` against Mathlib4 to confirm absence.** The grep over `lean/.lake/packages/mathlib/Mathlib/**/*.lean` for patterns like `card_even_of`, `Involutive.*card`, `Even.*Finset.*card.*involution`, and `2 ∣ s\.card` found no exact match, but Mathlib evolves; before opening the PR the contributor should `grep` master and skim `Mathlib.Combinatorics.SimpleGraph.Matching` and `Mathlib.GroupTheory.Perm.Cycle` for any near-equivalent. If a subset/variant exists, this becomes a `weaken-hypothesis` PR rather than a new addition.
- The proof in `CongruentStubs.lean` uses `Finset.strongInduction` with a manual erase argument. Mathlib reviewers often prefer `Finset.induction_on'` + a custom step, or a quotient by the orbit relation. Either reformulation is acceptable but should be discussed with the reviewer.
- One minor stylistic item: the current proof opens `simp [s', Finset.mem_erase]` repeatedly. A reviewer may ask for `Finset.mem_erase_of_ne_of_mem` style instead.

## What would have been asked (if bidirectional)
- "Should the PR target Mathlib master, or a stable Mathlib release branch matching the v4.14.0 toolchain pinned by `tunnell-cnp-lean4`?"
- "Do we want the PR to also expose `solSetNZ_card_even` as a downstream corollary in `Mathlib.NumberTheory`, or keep that to the CPP paper only?"

## Recommended next step
Papanokechi reviews this handoff, confirms `card_even_of_involution` as the PR target, and authorizes Copilot to:
1. Fork mathlib4 (or use existing fork),
2. Add `Mathlib/Data/Finset/CardEvenInvolution.lean` (or extend `Mathlib/Data/Fintype/Parity.lean`),
3. Open a draft PR with the description above and link it in the CPP 2027 cover letter.

## Files committed
- `handoff.md` (this file)
- `claims.jsonl`
- `halt_log.json`
- `discrepancy_log.json`
- `unexpected_finds.json`
- `candidate_table.md`

## AEAL claim count
1 entry written to `claims.jsonl` this session.
