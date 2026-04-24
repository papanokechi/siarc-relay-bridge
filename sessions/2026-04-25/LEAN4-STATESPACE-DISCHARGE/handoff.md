# Handoff — LEAN4-STATESPACE-DISCHARGE
**Date:** 2026-04-25
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~90 minutes
**Status:** COMPLETE

## What was accomplished
All build errors in `lean4/SIARCRelay11/StateSpace.lean` were fixed, achieving 0 errors and 0 sorries. The file now compiles cleanly with Lean 4.14.0 / Mathlib 4.14.0. Key fixes: replaced broken `AddCommGroup where` block (which caused opaque definitional equality failures) with `Function.Injective.addCommGroup` + 7 standalone component-wise instances; replaced `Function.Injective.normedAddCommGroup` (doesn't exist) with `NormedAddCommGroup.induced`; simplified `LorentzBase` to avoid `EuclideanSpace` import. Also fixed downstream `Operators.lean` by adding `noncomputable` to 8 `opaque` declarations.

## Key numerical findings
- StateSpace.lean: 0 errors, 0 sorries (was ~15 errors before)
- Operators.lean: 0 errors (was 6 errors from missing `noncomputable`)
- Bundles.lean: 0 errors (downstream, builds clean)
- Control.lean and Barriers.lean: blocked by pre-existing errors in Axioms.lean (not related to StateSpace changes)

## Judgment calls made
1. **Replaced `AddCommGroup where` with `Injective.addCommGroup`**: The explicit `where` block caused Lean4's definitional equality to become opaque, breaking all downstream `rfl` proofs. The injection-transfer approach avoids this entirely by delegating all axiom proofs to the product type.
2. **Simplified `LorentzBase`**: Removed `SmoothManifoldWithCorners (𝓡 n)` and `ChartedSpace (EuclideanSpace ℝ (Fin n))` fields because importing `Mathlib.Geometry.Manifold.Instances.Real` pulled in uncompiled Mathlib modules. Since `LorentzBase` is not used by `StateSpace` or any downstream file, this has zero impact on the proof chain.
3. **Added `noncomputable` to `opaque` declarations in Operators.lean**: The `NormedAddCommGroup.induced` instance is `noncomputable`, which propagated to downstream `opaque` declarations that internally use `Classical.ofNonempty`.

## Anomalies and open questions
1. **Pre-existing errors in Axioms.lean**: Unknown identifier `Path` (line 43) and related errors. These block Control.lean and Barriers.lean. Likely a missing import or Mathlib API change.
2. **Pre-existing errors in Parameters.lean**: "failed to generate projections for 'Prop' structure" — structure fields that are not proofs but are in a Prop-typed structure.
3. **Pre-existing errors in Theorems/LocalWellPosedness.lean**: "failed to infer binder type" at line 82.
4. **Instance diamond risk**: The standalone `Zero`/`Add`/etc. instances and the `AddCommGroup` derived from `Injective.addCommGroup` should be definitionally equal (since the latter is built from the former), but this has not been stress-tested in downstream theorem proofs that might synthesize the instances differently.
5. **`LorentzBase` simplification**: If any future file needs the smooth manifold structure on `LorentzBase`, the `EuclideanSpace` import issue will need to be resolved (either by precompiling that Mathlib module or restructuring imports).

## What would have been asked (if bidirectional)
1. Should `LorentzBase` be removed entirely rather than simplified, given it's unused?
2. Are the Axioms.lean / Parameters.lean / LocalWellPosedness.lean errors known issues or should they be fixed in this session?
3. Is there a preferred strategy for handling the `noncomputable` propagation from `NormedAddCommGroup.induced`?

## Recommended next step
Fix the pre-existing errors in `Axioms.lean` (unknown `Path` identifier — likely needs a Mathlib topology import or API migration) and `Parameters.lean` (Prop structure field issue), which will unblock `Control.lean`, `Barriers.lean`, and the full `lake build`.

## Files committed
- `sessions/2026-04-25/LEAN4-STATESPACE-DISCHARGE/StateSpace.lean` — fixed source file
- `sessions/2026-04-25/LEAN4-STATESPACE-DISCHARGE/Operators.lean` — fixed downstream file
- `sessions/2026-04-25/LEAN4-STATESPACE-DISCHARGE/claims.jsonl` — 6 AEAL entries
- `sessions/2026-04-25/LEAN4-STATESPACE-DISCHARGE/halt_log.json` — empty (no halt conditions)
- `sessions/2026-04-25/LEAN4-STATESPACE-DISCHARGE/discrepancy_log.json` — empty
- `sessions/2026-04-25/LEAN4-STATESPACE-DISCHARGE/unexpected_finds.json` — empty
- `sessions/2026-04-25/LEAN4-STATESPACE-DISCHARGE/handoff.md` — this file

## AEAL claim count
6 entries written to claims.jsonl this session
