# Handoff — P18-FORWARDINV-STRUCTURAL-REFACTOR

**Date:** 2026-04-28
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~75 minutes
**Status:** HALTED — `lake build` exit 1, 7 errors remain in
`ForwardInvarianceFramework.lean`. All three relay strategies plus
two additional approaches were attempted; none reduced the error
count below the P17 baseline.

---

## Section 1 — Root cause (confirmed)

**`F.carrier` field projection blocks typeclass synthesis when
the typeclass argument appears on a *structure* (not just a `def`).**

`FieldSpace`, `ThermalSpace`, `StructuralSpace` (defined in
`SIARCRelay11/StateSpace.lean`) store
`NormedAddCommGroup carrier` and `NormedSpace ℝ carrier` as
**fields**, not as registered instances:

```lean
structure FieldSpace where
  carrier  : Type*
  normed   : NormedAddCommGroup carrier
  module   : NormedSpace ℝ carrier
  inner_product : InnerProductSpace ℝ carrier
```

Consequently `[NormedAddCommGroup F.carrier]` cannot be synthesised
from the instance database for an arbitrary `F : FieldSpace` — only
from an explicit hypothesis (the `variable` block at the top of the
namespace). This works for `def` and `theorem` bodies (Invariance.lean
compiles cleanly using the variable-block style), **but breaks at
*structure* declarations and at use sites of those structures**,
where typeclass synthesis runs before the metavariables for `F` /
`T` / `S` are unified, leaving a stuck `?m.carrier`.

The relay-prompt diagnosis was correct.

---

## Section 2 — Strategies attempted and results

| # | Strategy | Description | Errors after |
|---|----------|-------------|--------------|
| baseline | git HEAD (initial commit) | F T S auto-bound implicit, no `noncomputable`, named-arg `(F := F)` syntax | 9 |
| P17 reapply | `noncomputable` + explicit `(F : FieldSpace) (T : ThermalSpace) (S : StructuralSpace)` on `siarc_dag`/`siarc_flow`/`siarc_forwardInvariant`/`SafetyCertificate`, all 9 instance args repeated explicitly | 7 |
| **S1 — Inline `siarc_flow`** | Replaced `siarc_flow F T S` with `⟨fun t ht σ₀ => evolutionMap …⟩` literal at the structure-field site. Failure mode unchanged: same metavariable trap on the inlined `evolutionMap` instance args. | 7 (same lines) |
| **S2 — Drop `(F T S)` from `siarc_dag`/`siarc_flow`** (auto-bound implicit, no instance args) | Lean dagger-renamed the auto-bound implicit `F` to `F✝`, so `(F := F)` named-arg syntax at use sites became `invalid argument name 'F'`. | 9–14 |
| **S2b — Local instance helpers** (this session, novel) | Added 6 `local instance` declarations near the top of the file: `local instance fieldSpace_normed (F : FieldSpace) : NormedAddCommGroup F.carrier := F.normed` etc. The intent: register `F.carrier`-style instances in the database so synthesis can find them without an explicit hypothesis. The 6 instance declarations themselves *did* compile, but the downstream errors did not change — synthesis at structure use sites still ran before `F` was unified, so `F.carrier` was still `?m.carrier` and the local instances did not fire. | 7–14 (depending on accompanying signature edits) |
| **Strategy 2c — Explicit-args everywhere** | Made every `def`/`theorem` declare `{F : FieldSpace} {T : ThermalSpace} {S : StructuralSpace}` explicitly + `[CompleteSpace …]`, drop variable block, drop named-arg syntax. Lean still failed to synthesise F at `QuasiStaticLink` instances inside `siarc_forwardInvariant` body (because `QuasiStaticLink p` from `Barriers.lean` has F T S auto-bound implicit there, and the unification trip happens inside a chain of typeclass-stuck calls). | 14 |

The final committed state is the P17 baseline (7 errors) — the
`lean4/SIARCRelay11/Theorems/ForwardInvarianceFramework.lean` file
in the working tree has only the minimal P17 fix applied
(`noncomputable` on `siarc_dag` and `siarc_flow`). All other
experimental edits were reverted via `git checkout --` so the repo
is in a known state for P19.

---

## Section 3 — `lake build` results

| Build | Exit | Errors in target | Notes |
|---|---|---|---|
| Baseline (git HEAD `c1b3168`) | 1 | 9 | Original initial-commit form |
| P18 final (after revert + minimal P17 reapply) | 1 | **7** | `lake_build_baseline.log` |

Final exit: **1**. The 7 errors are:

```
ForwardInvarianceFramework.lean:196:35:
  typeclass instance problem is stuck    [siarc_forwardInvariant body]
ForwardInvarianceFramework.lean:233:12:
  typeclass instance problem is stuck    [SafetyCertificate.invariance field]
ForwardInvarianceFramework.lean:248:22:
  invalid argument name 'F' for function [SafetyCertificate (F := F) call site]
ForwardInvarianceFramework.lean:261:30:
  invalid argument name 'F' for function [apply : cert : SafetyCertificate (F := F)]
ForwardInvarianceFramework.lean:264:69:
  unsolved goals                          [SafetyCertificate.apply body]
ForwardInvarianceFramework.lean:274:30:
  invalid argument name 'F' for function [apply_InSafe]
ForwardInvarianceFramework.lean:290:30:
  invalid argument name 'F' for function [iterate]
```

The L264 unsolved-goals error is a cascade from the L233/L248
prior failures; it should resolve once SafetyCertificate elaborates.

---

## Section 4 — Axiom inventory
**FAILED — build did not reach exit 0.** `#print axioms` not captured.

## Section 5 — Sorry count
**NOT REACHED.** Not measured.

## Section 6 — Legacy excision
**NOT EXECUTED — build did not exit 0.**

---

## Section 7 — Next step → P19-FORWARDINV-DEEP-REPAIR

The remaining 7 errors require either:

**Option A — Edit `StateSpace.lean` to register field-projections
as instances globally.** Add:

```lean
attribute [instance] FieldSpace.normed FieldSpace.module
attribute [instance] ThermalSpace.normed ThermalSpace.module
attribute [instance] StructuralSpace.normed StructuralSpace.module
-- and add CompleteSpace fields, registered as instances
```

This is the cleanest fix but expands P16's "trusted core" boundary
to include `StateSpace.lean`. That file was previously excluded from
the P16/P17 repair scope — recommend Claude approve before touching.

**Option B — Refactor SafetyCertificate to be a `class` instead of
a `structure`**, and drop the `[NormedAddCommGroup F.carrier]`
typeclass arguments entirely. Use a constructor-based API with
explicit instance proofs as fields.

**Option C — Replace `FieldSpace`/etc. with classes (not structures)
that bundle the typeclasses via `extends`.** This is the most
idiomatic Lean 4 / Mathlib pattern and eliminates the `F.carrier`
projection problem at the language level. Most invasive — touches
StateSpace.lean, Operators.lean, Barriers.lean, Invariance.lean, and
all imports.

**Recommendation:** Option A first (smallest blast radius). If A
fails, escalate to Option C and budget a full Lean expert session.

Once `lake build` exits 0:
- Capture `#print axioms` for the API.lean top-level theorem
- Confirm sorry count under `SIARCRelay11/`
- Run legacy excision (move `lean4/*.lean` non-`SIARCRelay11` and
  `lean4/RelayV2_*.lean` to `lean4/legacy/`)
- Then run **P15-JAR-RESUBMIT-PREP**

---

## Files in this session folder
- `handoff.md` (this file)
- `claims.jsonl` (1 entry, status only)
- `halt_log.json` (1 entry, 7 remaining errors)
- `discrepancy_log.json` ({})
- `unexpected_finds.json` ({})
- `lake_build_baseline.log` — final committed state, 7 errors
- `lake_build_final.log` — captures the worst experimental state
  (15 errors after most aggressive edits, before revert) for
  reference; do **not** treat this as the file's current state
- `ForwardInvarianceFramework.lean` — copy of the final committed
  source file (P17 baseline + `noncomputable` only)

## AEAL claim count
1 entry written to `claims.jsonl` this session (status entry; no
numerical claims since build did not complete).
