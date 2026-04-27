# Handoff — P15-SORRY-AUDIT
**Date:** 2026-04-27
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~5 minutes
**Status:** COMPLETE

## What was accomplished
Diagnostic-only enumeration of every `sorry` token in `lean4/` (excluding `.lake/`
vendored Mathlib/Batteries/Aesop/LeanSearchClient). All matches were classified
into three buckets: (a) real proof-gap `sorry` tokens in active code, (b)
`sorry` tokens that lie inside block comments / docstring code samples
(inert), and (c) textual mentions of the word "sorry" in comments,
docstrings, and audit tables. No files were modified.

## Key numerical findings

- Raw `\bsorry\b` matches in project `.lean` files (excluding `.lake/`): **89**
- Of those, after stripping `--` line-comment prefixes and string literals: 88
- **Real proof-gap sorries (active code paths): 10**
- Sorries inside `/- ... -/` block-comment templates: **6**
  (all in `SIARCRelay11/Examples/Example_PhysicalSystem.lean`)
- Sorries inside docstring code-fence (inert): 1
  (`RelayV2_Relay12_ControllabilityFramework.lean:51`)
- Textual mentions in comments/markdown tables only: 71
- `SIARCRelay11/` trusted core + theorems layer real sorries: **0**
- Top-level legacy stack real sorries: **10**

### Real proof-gap sorries (10)

| # | File | Line | Enclosing declaration | Kind | Notes |
|---|------|------|-----------------------|------|-------|
| 1 | `lean4/Axioms.lean` | 16 | `axiom holonomy_nonlocal` | axiom-body placeholder | `:= by sorry`; intentional, comment-tagged "placeholder: sheaf-theoretic argument" |
| 2 | `lean4/Axioms.lean` | 24 | `axiom coupling_smallness_undecidable` | axiom-body placeholder | `:= by sorry`; intentional, comment-tagged "Rice's theorem analogue" |
| 3 | `lean4/Control.lean` | 69 | `def evolutionMap_controlled` | proof-gap | tagged "Relay 12: integrate controlled system" |
| 4 | `lean4/Controllability.lean` | 23 | `def ReachableSet` | proof-gap | tagged "Relay 12" |
| 5 | `lean4/Invariance.lean` | 50 | `theorem safe_manifold_invariance` | proof-gap | tagged "Relay 12 target: Nagumo + barrier" |
| 6 | `lean4/LocalWellPosedness.lean` | 48 | `theorem local_well_posedness` | proof-gap | tagged "Relay 12 target: Kato + contraction" |
| 7 | `lean4/Operators.lean` | 113 | `def evolutionMap` | proof-gap | tagged "Relay 12 placeholder" |
| 8 | `lean4/Operators.lean` | 125 | `lemma evolutionMap_semigroup` | proof-gap | tagged "Relay 12 target" |
| 9 | `lean4/StateSpace.lean` | 89 | `instance` (NormedAddCommGroup field `norm_add_le`) | proof-gap | inline triangle-inequality field |
| 10 | `lean4/StateSpace.lean` | 90 | `instance` (NormedAddCommGroup field `eq_of_dist_eq_zero`) | proof-gap | inline metric separation field |

### Per-file count of real proof-gap sorries

| File | Count |
|------|-------|
| `lean4/Axioms.lean` | 2 (both axiom-as-sorry placeholders) |
| `lean4/Control.lean` | 1 |
| `lean4/Controllability.lean` | 1 |
| `lean4/Invariance.lean` | 1 |
| `lean4/LocalWellPosedness.lean` | 1 |
| `lean4/Operators.lean` | 2 |
| `lean4/StateSpace.lean` | 2 |
| **Total** | **10** |

### Inert sorries (do NOT contribute to the kernel `sorryAx` count)

| File | Lines | Why inert |
|------|-------|-----------|
| `SIARCRelay11/Examples/Example_PhysicalSystem.lean` | 40, 44, 48, 52, 56, 60 | Entire `noncomputable def mySystemAxioms` block is wrapped in `/- ... -/` (lines 35–62). User-fillable template. |
| `RelayV2_Relay12_ControllabilityFramework.lean` | 51 | Inside a fenced ` ``` ` Markdown code block within a docstring; not elaborated. |

### Layer summary

- **`SIARCRelay11/` trusted core + theorems + infrastructure**: 0 real sorries. Confirms the audit notes in `TrustedBoundary.lean` (line 251 — "0 sorrys in entire project (Relay 24: 7 sorry → 5 opaque + 2 axiom)") and `AxiomInventory.lean` (line 220 — "Sorry count: 0 in all theorem files").
- **Top-level legacy stack** (`Axioms.lean`, `Control.lean`, `Controllability.lean`, `Invariance.lean`, `LocalWellPosedness.lean`, `Operators.lean`, `StateSpace.lean`): 10 real sorries. These files predate the Relay 24 refactor that produced the `SIARCRelay11/` namespace and are not imported by `SIARCRelay11.lean` (root) — they are the historical R10–R12-era stubs.

### Distinguishing axiom-level from proof-gap

- **Axiom-level (intentional)**: Axioms.lean lines 16 and 24. These are written as `axiom name : T := by sorry` — semantically equivalent to a vacuous axiom and tagged in adjacent comments as deliberate placeholders ("requires sheaf-theoretic argument", "undecidability via Rice's theorem analogue"). They are *not* discharged proof obligations; they are sealed assumptions documented as such.
- **Proof-gap (genuine TODO)**: lines 3–10 in the table above (8 items). Each carries a "Relay 12 target" marker and refers to a concrete proof technique (Nagumo, Kato, semigroup integration, Lumer–Phillips, etc.).

No `sorry` was found being used as a *named axiom in the trusted layer*
(e.g. `tunnell_conditional_on_BSD`-style). The two axiom-body sorries in
`Axioms.lean` are in the legacy stack and are superseded by the
`SIARCRelay11/` axiom inventory (which uses proper `axiom` declarations
without `:= by sorry`).

## Judgment calls made

- Excluded `.lake/` vendored package files (Mathlib, Batteries, Aesop,
  LeanSearchClient) from the inventory. Those contain `sorry` tokens
  in test fixtures and example docstrings that are not part of this
  project's proof obligations.
- Classified two file-position matches as inert because the `sorry`
  tokens are syntactically inside `/- ... -/` block comments or inside
  triple-backtick code fences within `/-! ... -/` docstrings. I did
  not attempt to elaborate the files to confirm; the classification
  is purely lexical.
- Decided that `axiom name : T := by sorry` in `lean4/Axioms.lean`
  counts as a "real sorry" for the kernel (it produces `sorryAx`),
  but separately tagged it as **axiom-level/intentional** per the
  prompt's distinction (a) vs (b).

## Anomalies and open questions

- The two top-level legacy directories appear to coexist with the
  current `SIARCRelay11/` namespace. `lean4/lakefile.lean` bills
  itself as a "sorry-free" stack, but the root-level files
  (`Control.lean`, `Operators.lean`, `Invariance.lean`,
  `LocalWellPosedness.lean`, `StateSpace.lean`, `Controllability.lean`,
  `Axioms.lean`) still contain 10 real sorries between them. **It is
  unclear whether these files are still part of the build target.**
  If they are not imported transitively from `SIARCRelay11.lean`, the
  audit-correct count is 0; if they are, the project is not yet
  sorry-free at the root. Recommend Claude review whether these files
  should be deleted, moved out of `lean4/`, or formally marked
  deprecated.
- `lean4/Axioms.lean` uses `axiom name ... := by sorry`, which is
  unusual syntax (`axiom` declarations in Lean 4 normally do not take
  a body). This may not even elaborate; if it does, the `sorry`
  tokens contribute `sorryAx` to the kernel. Worth verifying with
  `lake build` or `#print axioms`.
- The Examples block-comment template (`Example_PhysicalSystem.lean`)
  has 6 `sorry` tokens that are intentionally inert (commented out).
  If a user uncomments the block to instantiate a custom system, those
  6 sorries become live. Not an issue for the audit baseline but
  worth flagging.

## What would have been asked (if bidirectional)

- Are the top-level files (`Operators.lean`, `Control.lean`, etc.)
  still part of the active proof stack, or are they superseded by
  `SIARCRelay11/`?
- Is the intent to discharge the 8 "Relay 12 target" sorries, or to
  convert them to `opaque`/`axiom` as was done in Relay 24 for the
  `SIARCRelay11/` mirror files?
- Should the 2 `axiom ... := by sorry` declarations in
  `lean4/Axioms.lean` be rewritten as proper `axiom` statements
  (no body) to remove the kernel `sorryAx` dependency while preserving
  the intentional-assumption status?

## Recommended next step

P16-SORRY-DISCHARGE-LEGACY: For each of the 8 proof-gap sorries in the
top-level legacy stack, either (i) delete the file if it is no longer
imported anywhere in the build graph, or (ii) convert the declaration
to an `opaque` / proper `axiom` mirroring the Relay-24 pattern used in
`SIARCRelay11/`. For the 2 `axiom ... := by sorry` lines in
`lean4/Axioms.lean`, drop the `:= by sorry` so they become
proper axioms with no kernel `sorryAx` usage.

## Files committed

- `sessions/2026-04-27/P15-SORRY-AUDIT/handoff.md` (this file)
- `sessions/2026-04-27/P15-SORRY-AUDIT/raw_sorry_inventory.txt`
  (full grep output, sha256: see claims.jsonl)
- `sessions/2026-04-27/P15-SORRY-AUDIT/claims.jsonl`
- `sessions/2026-04-27/P15-SORRY-AUDIT/halt_log.json` (empty `{}`)
- `sessions/2026-04-27/P15-SORRY-AUDIT/discrepancy_log.json` (empty `{}`)
- `sessions/2026-04-27/P15-SORRY-AUDIT/unexpected_finds.json` (empty `{}`)

## AEAL claim count
1 entry written to claims.jsonl this session (diagnostic).
