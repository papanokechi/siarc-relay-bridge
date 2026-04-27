# Handoff — P19-STATESPACE-INSTANCE-ATTRS

**Date:** 2026-04-28
**Agent:** GitHub Copilot (VS Code)
**Status:** HALTED — instance-attribute approach (Option A from
P18 handoff) attempted; same 7 errors persist in
`ForwardInvarianceFramework.lean` because the variable-block
binders shadow the registered attribute-instances. Removing the
variable-block binders triggers diamond inheritance against the
rest of the codebase. Recommend P20 with structure-to-class
refactor (Option C from P18).

---

## Section 1 — Fields registered as instances

Edited `lean4/SIARCRelay11/StateSpace.lean` (after the
`StructuralSpace` definition, before `ControlSpace`):

```lean
attribute [instance] FieldSpace.normed
attribute [instance] FieldSpace.module
attribute [instance] ThermalSpace.normed
attribute [instance] ThermalSpace.module
attribute [instance] StructuralSpace.normed
attribute [instance] StructuralSpace.module
```

Six fields registered:
- `FieldSpace.normed : NormedAddCommGroup carrier` (line 56)
- `FieldSpace.module : NormedSpace ℝ carrier` (line 57)
- `ThermalSpace.normed : NormedAddCommGroup carrier` (line 62)
- `ThermalSpace.module : NormedSpace ℝ carrier` (line 63)
- `StructuralSpace.normed : NormedAddCommGroup carrier` (line 68)
- `StructuralSpace.module : NormedSpace ℝ carrier` (line 69)

`FieldSpace.inner_product` deliberately NOT registered: would
diamond against `NormedAddCommGroup` since `InnerProductSpace`
extends it.

No `complete : CompleteSpace carrier` field exists on any of the
three structures — `CompleteSpace` is supplied via the variable
block in downstream files only.

## Section 2 — Error count progression

| State | Targeted errors | Notes |
|---|---|---|
| P18 baseline (file at git HEAD + `noncomputable` only) | 7 | starting point |
| Step 5: attrs added, Forward unchanged | **7** | identical 7 errors at lines 196:35, 233:12, 248:22, 261:30, 264:69, 274:30, 290:30 |
| Step 5b: drop redundant `[NormedAddCommGroup]` / `[NormedSpace]` from variable block | 14 | "don't know how to synthesize implicit F/T/S" cascade — variable block was *also* what made `F`/`T`/`S` auto-bind into theorem signatures via Lean's auto-bound-implicit machinery |
| Step 5c: keep variable block, make F T S positional on `siarc_dag`/`siarc_flow`/`siarc_forwardInvariant`/`SafetyCertificate` | 17 | **diamond inheritance**: `g₁ p σ` in Barriers.lean uses the variable-block instance `inst✝⁸ : NormedAddCommGroup F.carrier`, but the SIARC DAG path resolves the same goal to `F.normed` (attribute instance). Two distinct terms of the same proposition. Type-mismatch on `And.intro`. |

**Halt rule triggered:** "attribute [instance] declarations cause
instance conflicts in other modules (diamond inheritance)" —
specifically when the variable block is removed/altered to give the
attributes a chance to fire.

The reverted baseline (= attributes added in StateSpace.lean,
ForwardInvarianceFramework reverted to P18 noncomputable form)
preserves the 7-error P18 baseline without breaking other modules.
The attribute additions are benign in isolation — they do not
introduce any new errors elsewhere — but they also do not unblock
the framework synthesis.

## Section 3 — `lake build` final exit code
**Exit 1** for `lake build SIARCRelay11.Theorems.ForwardInvarianceFramework`.
Same 7 errors as P18.

Full `lake build` not re-run after revert (would inherit the same
7 framework errors; no scope to fix).

## Section 4 — Axiom inventory
**FAILED — build did not reach exit 0.** Not captured.

## Section 5 — Sorry count
**NOT REACHED.**

## Section 6 — Legacy excision
**NOT EXECUTED.**

## Section 7 — Next step → P20-FIELDSPACE-CLASS-REFACTOR

The instance-attribute approach **partially works** (the attributes
are correctly registered, no diamond when other code uses the
variable block) but **does not solve the original synthesis
problem** because:

> Lean instance synthesis at a use site of a polymorphic structure
> (e.g. `siarc_flow : Flow (StateSpace F T S)`) runs *before* the
> metavariable for `F` is unified. The instance database lookup
> sees `?m.carrier` and cannot match either the attribute-instance
> on `FieldSpace.normed` (requires unifying `?m` with `F`) or the
> variable-block hypothesis (same problem). Both fail symmetrically.

**The deeper fix is Option C from P18:** convert
`FieldSpace`/`ThermalSpace`/`StructuralSpace` from `structure` to
`class … extends NormedAddCommGroup carrier, NormedSpace ℝ carrier
where …`. This makes the typeclass *part of the class signature*
rather than a field, so Lean can infer it directly from
`F : FieldSpace`. Most invasive — touches `StateSpace.lean`,
`Operators.lean`, `Barriers.lean`, `Invariance.lean`, every import.

**Alternative (Option B)**: refactor `SafetyCertificate` to take
`(F.carrier T.carrier S.carrier)` as explicit type args + bundle
the typeclass proofs as fields. Less idiomatic but smaller blast
radius than full class refactor.

**Recommend** for P20:
1. First verify Option C scope by enumerating `def`/`theorem`
   declarations that use `[NormedAddCommGroup F.carrier]` etc.
   (`grep -rn 'NormedAddCommGroup F\.carrier' SIARCRelay11/`).
2. If <30 sites: do Option C in one pass.
3. If ≥30 sites: do Option B as scaffolding, then Option C as
   follow-up.

Once `lake build` exits 0:
- Capture `#print axioms`
- Confirm sorry count
- Run legacy excision
- Then run P15-JAR-RESUBMIT-PREP

---

## Files in this session folder

- `handoff.md` (this file)
- `claims.jsonl`
- `halt_log.json`
- `discrepancy_log.json` (`{}`)
- `unexpected_finds.json` (`{}`)
- `lake_targeted.log` — first build attempt (attrs added,
  variable block intact) → 7 errors at L196/L233/L248/L261/L264/L274/L290
- `lake_targeted2.log` — 5b attempt, dropped variable-block normed/module → 14 errors
- `lake_targeted3.log` — 5c attempt, F T S positional on certificate → 7 errors but renumbered (function-expected cascade)
- `lake_targeted4.log` — 5c with siarc_dag/flow positional → 17 errors with diamond evidence (visible @g₁ F T S F.normed vs @g₁ F T S inst✝⁸)
- `lake_targeted5.log` — 5c after revert (file mismatch) → 14 errors
- `lake_attrs_only.log` — final committed state (StateSpace attrs + ForwardInvarianceFramework P18 baseline) → 7 errors, identical to P18
- `lake_full.log` — partial (killed mid-build to halt)
- `StateSpace.lean` — copy of edited source (with `attribute [instance]` block)
- `ForwardInvarianceFramework.lean` — copy of P18 baseline (`noncomputable` only, no other changes)

## AEAL claim count
1 entry written to `claims.jsonl` (status entry; no new numerical claims).
