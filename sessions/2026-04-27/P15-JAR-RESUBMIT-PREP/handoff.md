# Handoff — P15-JAR-RESUBMIT-PREP — **HALTED**
**Date:** 2026-04-27
**Agent:** GitHub Copilot (VS Code)
**Status:** HALTED at Step 3 (lake build failure)

## Halt summary

Per the prompt's HALT condition ("If `lake build` exit non-0: report
errors and HALT"), execution stopped after Step 3. The legacy excision
in Steps 1–2 was completed, then **reverted** to leave the workspace
in its original pre-session state, because the `lake build` failure is
unrelated to the excision and the workspace would otherwise be left
half-converted.

## Step 1–2 results (excision; subsequently reverted)

Files moved to `lean4/legacy/` (then moved back after halt):
- `Axioms.lean`, `Barriers.lean`, `Bundles.lean`, `Control.lean`,
  `Controllability.lean`, `Invariance.lean`,
  `LocalWellPosedness.lean`, `Operators.lean`, `Stability.lean`,
  `StateSpace.lean` (10 files)
- `RelayV2_MinimalModel.lean`, `RelayV2_Relay{1,2,3,5,6,7,8,9,10,11,12,13,14,15}_*.lean` (15 files)
- **Total: 25 files moved**

Files reported as missing: none (all listed files were present).

After Step 2, the `lean4/` root contained only `lakefile.lean` and
`SIARCRelay11.lean` (plus the `SIARCRelay11/` subdirectory and the
moved `legacy/`). After halt, all 27 `.lean` files were restored to
the `lean4/` root.

## Step 3 result — `lake build` failed (exit 1)

`lake --version`: Lake 5.0.0-410fab7 (Lean 4.14.0). Toolchain pinned
to `leanprover/lean4:v4.14.0` matches `lean-toolchain`. Mathlib
required at `v4.14.0`. `.lake/` directory exists (Mathlib already
fetched).

### Failed targets (3)

```
- SIARCRelay11.Axioms
- SIARCRelay11.Parameters
- SIARCRelay11.Theorems.LocalWellPosedness
```

### Error excerpt (`lake_build_errors.txt`)

```
SIARCRelay11/Axioms.lean:43:20  unknown identifier 'Path'
SIARCRelay11/Axioms.lean:44:16  unknown identifier 'ℝ'
SIARCRelay11/Axioms.lean:44:29  unknown identifier 'Path'
SIARCRelay11/Axioms.lean:58:9   unknown identifier 'ℝ'
SIARCRelay11/Axioms.lean:59:23  unknown identifier 'ℝ'   (×3)
SIARCRelay11/Axioms.lean:70:19  invalid binder annotation, type is not a class instance
SIARCRelay11/Parameters.lean:90:2   failed to generate projections for 'Prop' structure, field 'ellipticity_constant' is not a proof
SIARCRelay11/Parameters.lean:101:2  failed to generate projections for 'Prop' structure, field 'inverse_bound' is not a proof
SIARCRelay11/Theorems/LocalWellPosedness.lean:82:9  failed to infer binder type
SIARCRelay11/Theorems/LocalWellPosedness.lean:82:7  failed to infer binder type
```

Full log: `lake_build.log` (~2.6 MB).

### Root cause analysis

The errors are **inside the `SIARCRelay11/` trusted-core namespace**,
NOT in the legacy files we moved. Confirmation: I read
`SIARCRelay11/Axioms.lean` lines 1–15 — it imports only
`Mathlib.Topology.Basic` and `Mathlib.Topology.Algebra.Module.Basic`,
but uses `Path` (lives in `Mathlib.Topology.Connected.PathConnected`)
and `ℝ` (lives in `Mathlib.Data.Real.Basic`) at lines 43–59. These are
**missing imports** that pre-date this session. The file has never
elaborated against Mathlib `v4.14.0` in its current state.

The `Parameters.lean` errors ("failed to generate projections for
'Prop' structure, field is not a proof") indicate a `Prop`-vs-`Type`
mix-up in a structure declaration — also pre-existing.

The `LocalWellPosedness.lean:82` "failed to infer binder type" is a
typeclass-resolution failure, also pre-existing.

### Critical implication

**The P15 manuscript's claim that `SIARCRelay11/` is a "0-sorry trusted
core" is not currently verifiable**, because the namespace **does not
build at all**. JAR's reviewer almost certainly observed this same
build failure in addition to the (separately reported) `sorry` count
in legacy files.

This is more serious than the original P15-LEGACY-TRIAGE conclusion.
P15-LEGACY-TRIAGE assumed `SIARCRelay11/` was buildable; that
assumption was never tested. **The Option A path (excise + cover
letter) cannot proceed until the trusted-core build is repaired.**

## Steps not executed (halted)

- Step 4 (capture `#print axioms`) — impossible without successful build
- Step 5 (locate manuscript) — not reached
- Step 6 (write `manuscript_R2.tex`) — not reached
- Step 7 (compile PDF) — not reached
- Step 8 (cover letter) — not reached

## Anomalies and open questions

1. **Pre-existing trusted-core build failure.** `SIARCRelay11.Axioms`,
   `SIARCRelay11.Parameters`, and
   `SIARCRelay11.Theorems.LocalWellPosedness` have type-check errors
   against Mathlib v4.14.0. When was this last verified to build?
2. **Memory note `lean4-sorry-discharge-2026-04-24.md` reported "0
   sorry, builds clean".** That note is now contradicted by direct
   observation. Either the note was based on a different toolchain, a
   different Mathlib version, or the audit was incomplete.
3. **Self-report mismatch.** `SIARCRelay11/TrustedBoundary.lean:251`
   claims "0 sorrys in entire project (Relay 24: 7 sorry → 5 opaque +
   2 axiom)". The 0-sorry count is now confirmed only at the
   syntactic level (grep); the *semantic* claim that the trusted core
   elaborates to a `MasterCertificate` term is **untested** because
   the namespace doesn't build.
4. **The `axiom holonomy_nonlocal` declaration on
   `SIARCRelay11/Axioms.lean:43` even uses `@Path _ (by assumption) p
   q`** — the `by assumption` term-level tactic in a binder is highly
   unusual and likely indicates a hand-written placeholder that was
   never elaborated.

## Recommended next step

**P16-TRUSTED-CORE-BUILD-REPAIR**: do not attempt JAR resubmission
until the trusted-core build is green. Concrete subtasks:

1. Add missing imports to `SIARCRelay11/Axioms.lean`:
   - `import Mathlib.Topology.Connected.PathConnected` (for `Path`)
   - `import Mathlib.Data.Real.Basic` (for `ℝ`)
2. Audit `SIARCRelay11/Parameters.lean` lines 85–105 for
   `Prop`-vs-`Type` mismatches (likely a `class` vs `structure`
   confusion or a field declared with a non-`Prop` type inside a
   `Prop` structure).
3. Inspect `SIARCRelay11/Theorems/LocalWellPosedness.lean` line 82 for
   ambiguous binders.
4. Re-run `lake build` to confirm the trusted-core compiles.
5. Capture `#print axioms` for the four guarantee theorems.
6. Only then proceed with P15-JAR-RESUBMIT-PREP.

Estimated effort: **1–3 days** for an experienced Lean 4/Mathlib
developer; longer if the `Parameters.lean` `Prop` issue requires
restructuring.

## Workspace state at halt

- `lean4/` root: 27 `.lean` files (original count, restored).
- `lean4/legacy/` directory: removed.
- `lean4/_lake_build.log`, `lean4/_lake_build_errors.txt`: created
  during this session; **not removed** (they are useful diagnostics).
- `siarc-relay-bridge/sessions/2026-04-27/P15-JAR-RESUBMIT-PREP/`:
  contains `lake_build.log`, `lake_build_errors.txt`, `handoff.md`,
  `claims.jsonl`, `halt_log.json`, `discrepancy_log.json`,
  `unexpected_finds.json`.

## Files committed

- `handoff.md`
- `claims.jsonl`
- `lake_build.log`
- `lake_build_errors.txt`
- `halt_log.json` (one entry: pre-existing trusted-core build failure)
- `discrepancy_log.json`
- `unexpected_finds.json`

## AEAL claim count
1 entry written to claims.jsonl (submission-prep, halted).
