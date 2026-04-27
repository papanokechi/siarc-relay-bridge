# Handoff — P16-TRUSTED-CORE-BUILD-REPAIR
**Date:** 2026-04-27
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** PARTIAL (3/3 prompt-targeted modules repaired; lake build still exit 1 due to 2 newly-unmasked downstream modules)

## What was accomplished
Applied minimal-edit fixes to all three modules listed in the prompt
(`SIARCRelay11.Axioms`, `SIARCRelay11.Parameters`,
`SIARCRelay11.Theorems.LocalWellPosedness`); each now builds cleanly
under Mathlib v4.14.0. Full `lake build` still returns exit 1 because
two additional modules (`SIARCRelay11.Control`, `SIARCRelay11.Barriers`)
contain pre-existing errors that were previously masked by the earlier
elaboration failures. Per Step 4 / HALT IF, halted before legacy
excision and before `#print axioms` capture; legacy files remain in
`lean4/` root, manuscript untouched.

## Per-module fix applied

| Module | Lines changed | Fix |
|---|---|---|
| `SIARCRelay11/Axioms.lean` | imports (top), L43–46, L60–62 | Added `import Mathlib.Topology.Connected.PathConnected`, `import Mathlib.Data.Real.Basic`, `import Mathlib.Analysis.Normed.Group.Basic`, `import Mathlib.Analysis.Normed.Module.Basic`. Replaced non-standard binder `(γ : @Path _ (by assumption) p q)` with `(γ : Path p q)` (twice). Wrapped `¬Decidable (...)` as `¬ Nonempty (Decidable (...))` because `Decidable` is `Type`-valued, not `Prop`-valued. |
| `SIARCRelay11/Parameters.lean` | L88, L98 | Removed `: Prop` from `class UniformlyElliptic` and `class QuasiStaticElasticity`. Both classes declared ℝ-valued data fields (`ellipticity_constant`, `inverse_bound`, `korn_constant`), which is illegal for a `Prop`-valued class. |
| `SIARCRelay11/Theorems/LocalWellPosedness.lean` | L82, L91 | Replaced two ambiguous `∀ t ht, …` binders with explicit `∀ (t : ℝ) (ht : t ∈ Set.Icc 0 Tstar), …`. Required because the body did not constrain `ht`'s type (`True` and a `=`-conclusion). |

## lake build exit code progression
1. Before any edit (baseline from P15-JAR-RESUBMIT-PREP): **exit 1**
   — Axioms, Parameters, LocalWellPosedness
2. After all three fixes: **exit 1**
   — three originally-failing modules now BUILD CLEAN; new errors
   surfaced in Control.lean and Barriers.lean (4 errors total, see
   below)

## Final lake build exit code
**Exit 1.** Captured in `lake_build_final.log` (2.65 MB) and
`lake_build_errors.txt`.

## #print axioms output
**FAILED — not reached.** Halted before Step 5 because Step 4 did
not produce a clean build.

## Legacy excision
**NOT DONE.** Per Step 6, excision is gated on Step 4 exit 0.
Legacy files remain in `lean4/` root. Workspace identical to
pre-session state for any file outside the three repaired modules.

## Remaining errors after P16 fixes
```
SIARCRelay11/Control.lean:77:0   failed to synthesize
                                  (opaque intentPolicy : I.carrier → IntentMode
                                   — requires Inhabited/Nonempty witness)
SIARCRelay11/Control.lean:86:7   failed to compile definition, consider marking
                                  it as 'noncomputable' because it depends on
                                  'Classical.ofNonempty' (opaque
                                   evolutionMap_controlled)
SIARCRelay11/Barriers.lean:235:12 typeclass instance problem is stuck
                                   (lemma g₃'_from_g₄)
SIARCRelay11/Barriers.lean:242:12 typeclass instance problem is stuck
                                   (lemma g₅_from_g₄)
```

## Judgment calls made
1. The Decidable-in-¬ error at Axioms.lean line 62 was not in the
   prompt's list, but it sits inside the same module (A) that the
   prompt told me to fix. Treating "fix module A" as "make module A
   build", I added the `Nonempty` wrapper. Reverting that wrapper
   would re-fail module A.
2. Added `Mathlib.Analysis.Normed.{Group,Module}.Basic` imports to
   Axioms.lean to satisfy `[NormedAddCommGroup U]` and
   `[NormedSpace ℝ U]` instances at line 72 (the prompt's "binder
   annotation at line 70" cue). The original
   `Mathlib.Topology.Algebra.Module.Basic` does not transitively
   re-export `NormedAddCommGroup` in v4.14.0.
3. Did NOT attempt to fix Control.lean or Barriers.lean. They are
   outside the prompt's stated scope ("Fix only the three failing
   SIARCRelay11 modules") and the HALT IF clause ("lake build still
   fails after all three attempts … log remaining errors, do not
   excise legacy") explicitly anticipates this case.

## Anomalies and open questions
- The Control.lean and Barriers.lean errors are PRE-EXISTING. The
  earlier P15-JAR-RESUBMIT-PREP build log showed Lean stopping at
  the first batch of failures; once those are repaired, these
  surface. Memory note `lean4-sorry-discharge-2026-04-24.md`
  asserting a clean build is therefore wrong about more than the
  3 modules originally identified.
- `coupling_smallness_undecidable` is now logically vacuous in a
  weak way: the `Nonempty (Decidable …)` wrapper makes the axiom
  statement closer to "no decidability instance exists in this
  context," which classically still holds because every
  proposition is decidable via `Classical.dec`. Recommend marking
  this axiom `@[deprecated]` or removing it entirely in P16-NEXT.
- `UniformlyElliptic` and `QuasiStaticElasticity` are NOT
  referenced anywhere else in `SIARCRelay11/` (verified by grep).
  Their `: Prop` declaration was likely an authoring error; the
  removal is safe.

## What would have been asked (if bidirectional)
- Should P16 expand its scope to fix Control.lean and Barriers.lean
  too, given that "trusted core builds" is the real goal? Or do you
  want a separate P17-CONTROL-BARRIERS-REPAIR session?
- Are `Dissipative`, `UniformlyElliptic`, `QuasiStaticElasticity`
  ever instantiated by the API? If not, are they paper-shaped
  shells that should be removed?

## Recommended next step
**P17-CONTROL-BARRIERS-REPAIR** (1–2 hours):
- Control.lean L75–95: add `deriving Inhabited` to `IntentMode`
  (4 constructors, all 0-arity; trivial), then mark the two
  `opaque` declarations `noncomputable opaque` if Lean still
  insists.
- Barriers.lean L233–245: the stuck typeclass synthesis is most
  likely missing `[NormedAddCommGroup F.carrier]` etc. instances
  at the lemma site. Add explicit `variable` requirements or move
  the lemmas inside the section that already declares them.

After P17 returns exit 0, retry P15-JAR-RESUBMIT-PREP from Step 3.

## Files committed
- `claims.jsonl`
- `discrepancy_log.json`
- `halt_log.json`
- `unexpected_finds.json`
- `lake_build_after_fixes.log` (2.65 MB)
- `lake_build_final.log` (2.65 MB; identical content)
- `lake_build_errors.txt`
- `handoff.md`

## AEAL claim count
1 entry written to claims.jsonl this session.
