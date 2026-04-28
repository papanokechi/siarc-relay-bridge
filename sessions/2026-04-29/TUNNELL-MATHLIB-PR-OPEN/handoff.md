# Handoff — TUNNELL-MATHLIB-PR-OPEN
**Date:** 2026-04-29
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~30 minutes
**Status:** COMPLETE

## What was accomplished
Extracted `card_even_of_involution` from `congruent-relay/formal/CongruentStubs.lean` and prepared a standalone, Mathlib-idiomatic Lean 4 file at `congruent-relay/mathlib-pr/CardEvenOfInvolution.lean`. Ported the proof to Mathlib master API, namespaced under `Finset`, added `two_dvd_card_of_involution` and `card_even_of_involutive` corollaries, and verified the file compiles cleanly against the local toolchain (Lean v4.30.0-rc1, Mathlib v4.30.0-rc1). PR description drafted.

## Key numerical findings
- Standalone file: **126 lines** (vs. ~75 in CongruentStubs; the increase is module header + docstring + two corollaries).
- `lake env lean CardEvenOfInvolution.lean` exit code: **0**.
- 0 sorry, 0 axioms, 0 warnings.

## Files produced

| Path | Lines | Purpose |
|---|---|---|
| `congruent-relay/mathlib-pr/CardEvenOfInvolution.lean` | 126 | Standalone Mathlib-ready file (canonical source) |
| Bridge: `CardEvenOfInvolution.lean` | 126 | Copy for review |
| Bridge: `pr_description.md` | — | PR description for GitHub |
| Bridge: `claims.jsonl` | 1 | AEAL claim |

## Compile result
```
$ cd lean
$ lake env lean CardEvenOfInvolution.lean
$ echo $LASTEXITCODE
0
```
Three iterations were required to align the original CongruentStubs proof with Mathlib master API (see "API drift" below).

## Generalization applied
1. **Namespaced** under `Finset` (was `Congruent`).
2. Added explicit module docstring describing the application context.
3. Renamed pointwise hypotheses to `hMem`, `hInv`, `hFix` for Mathlib idiom.
4. Added `Finset.two_dvd_card_of_involution` corollary (the form actually consumed by `solSetNZ_card_even` in CongruentStubs).
5. Added `Finset.card_even_of_involutive` convenience corollary for the common case where `σ` is a global `Function.Involutive`.
6. Kept the **pointwise** form as the primary statement, since that is the strictly more general spelling (matters for orbit-style applications on subsets of an infinite type).
7. No CNP-specific hypotheses were present; nothing was removed.

## API drift fixes during port
The original proof was written against an earlier Mathlib. Adjustments needed for v4.30.0-rc1:

| Original | Replacement | Reason |
|---|---|---|
| `import Mathlib.Algebra.Parity` | `import Mathlib.Algebra.Group.Even` | Module renamed in modern Mathlib |
| `Finset.strongInduction with \| ind` | `\| H` | Eliminator alt-name changed |
| `even.add_two` (chain-call) | explicit `obtain ⟨r, hr⟩ := heven'; exact ⟨r+1, by omega⟩` | `Even.add_two` not available |
| `Finset.ssubset_of_subset_of_ne` | `Finset.ssubset_iff_subset_ne.mpr ⟨_, _⟩` | Lemma renamed/removed |
| `Even.two_dvd` (chain-call) | `obtain ⟨r, hr⟩ := …; exact ⟨r, by omega⟩` | Method not present on `Exists`-based `Even` |
| `Nat.even_zero` | `⟨0, rfl⟩` | Constant absent under that name |

These are all mechanical adjustments; the proof structure (strong induction → erase pair → inherit hypotheses → IH gives `s'.card` even → `s.card = s'.card + 2`) is unchanged.

## PR description
See `pr_description.md` in this session directory. Key points:
- Title: `feat(Finset.Card): card_even_of_involution`
- Primary statement uses pointwise hypotheses for maximum reusability.
- Two corollaries (`two_dvd_card_of_involution`, `card_even_of_involutive`) ship with the same PR.
- No new dependencies; only `Finset.Card`, `Algebra.Group.Even`, `Logic.Function.Basic`.

## Anomalies and open questions
- **Toolchain mismatch (mild).** The relay prompt mentions target Lean v4.14.0, but the local Mathlib mirror is v4.30.0-rc1. The PR will go to `master` of `mathlib4`, which is the relevant target; we already verified compilation against a recent Mathlib. If `tunnell-cnp-lean4` is genuinely pinned to v4.14.0, the upstream lemma will need backport (or, more likely, the user will bump the Tunnell project's Mathlib pin once the PR is merged).
- **Membership claim.** No exact-name match found in the local Mathlib mirror, but the search was grep-only (`card_even_of`, `Involutive.*card`, `Even.*Finset.*card.*involution`, `2 ∣ s\.card`). Before opening the PR a contributor should also:
  - Check the latest `mathlib4` `master` (not the local pin).
  - Skim `Mathlib.Combinatorics.SimpleGraph.Matching` and `Mathlib.GroupTheory.Perm.Cycle.Type` for any near-equivalent stated as a special case.
  - Search Zulip / Mathlib4 PR queue for "involution even card".
  If a near-equivalent exists, the PR becomes a "weakening" or rename rather than new addition.
- **Stylistic choice for review.** I used a triple of pointwise hypotheses; reviewers may suggest `Set.InvOn σ σ s s` or wrapping into `Function.Involutive` via a `Subtype` instead. None of the alternatives change the proof body materially. The provided `card_even_of_involutive` corollary already addresses the global-involution case.
- **`[DecidableEq α]` requirement.** Kept because `Finset.erase` requires it. It is the standard idiom.

## What would have been asked (if bidirectional)
- "Should the Mathlib branch target `master` or a stable v4.x release branch?"
- "Do you want me to also draft a `Finset.card_orbit` style lemma for the analogous group-action case in the same PR, or keep this PR minimal and tight?"

## Estimated effort to open the PR
- Fork `mathlib4`, clone, run `lake exe cache get`: **~30 min**.
- Drop file into `Mathlib/Data/Finset/Card.lean` (append) or new file `Mathlib/Data/Finset/CardInvolution.lean` and update `Mathlib.lean` import index: **~15 min**.
- Run linters (`lake exe runLinter`, `lake build`): **~30 min**.
- Open PR, fill template using `pr_description.md`, link to Tunnell repo and DOI: **~15 min**.

**Total: ≤ 90 minutes** for a contributor with an existing Mathlib fork.

## Recommended next step
papanokechi reviews `pr_description.md` and `CardEvenOfInvolution.lean`,
approves, then Copilot:
1. Performs the master-branch grep to confirm absence (mandatory pre-PR check).
2. Adds the lemma to the appropriate Mathlib file in a fork.
3. Opens the PR with the description above.
4. Cites the resulting PR number in `tunnell_cpp_R1.tex` reproducibility / formalization section as evidence that the formalization yielded an upstream contribution.

## Files committed (this session)
- `handoff.md` (this file)
- `pr_description.md`
- `CardEvenOfInvolution.lean` (mirror of the canonical file in `congruent-relay/mathlib-pr/`)
- `claims.jsonl`
- `halt_log.json` (empty)
- `discrepancy_log.json` (empty)
- `unexpected_finds.json` (empty)

## AEAL claim count
1 entry written to `claims.jsonl` this session.
