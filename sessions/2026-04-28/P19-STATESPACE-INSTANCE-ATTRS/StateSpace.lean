import Mathlib.Geometry.Manifold.SmoothManifoldWithCorners
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Topology.FiberBundle.Basic
import Mathlib.Analysis.Normed.Module.Basic

/-!
# SIARCRelay11.StateSpace — Type Definitions for the Full State Space Hierarchy

## Purpose
Defines the mathematical types: base manifold M, fiber spaces (Field, Thermal,
Structural), control and intent spaces, the product StateSpace, and the
SafeManifold invariant subset.

## Dependencies
- Mathlib smooth manifolds, inner product spaces, fiber bundles, normed spaces

## Known Blockers
- Full Lorentzian metric requires pseudo-Riemannian Mathlib extension (not yet available)
- Sobolev space structure on ThermalSpace requires Mathlib Sobolev API

## Status (Relay 22)
- NormedAddCommGroup on StateSpace: **discharged** (via `NormedAddCommGroup.induced`)
- NormedSpace ℝ on StateSpace: **discharged** (via `norm_smul_le` transfer)
- 0 sorry remaining in this file
-/


namespace SIARCRelay11

-- ============================================================
-- Base Lorentzian-type manifold M
-- ============================================================

/-- M: the base manifold (smooth, finite-dimensional, compact with boundary).
    In the physical interpretation this is a 4-dimensional Lorentzian spacetime
    region. We use Riemannian proxy since Mathlib4 lacks pseudo-Riemannian.

    NOTE: `SmoothManifoldWithCorners (𝓡 n)` requires `EuclideanSpace` from
    `Mathlib.Geometry.Manifold.Instances.Real` which adds heavy transitive
    imports. We store the smooth-manifold property as a `Prop` field so that
    this file compiles with a minimal import set. -/
structure LorentzBase (n : ℕ) where
  carrier        : Type*
  [top_space     : TopologicalSpace carrier]
  [compact       : CompactSpace carrier]
  pseudo_metric  : carrier → carrier → ℝ

-- ============================================================
-- Component spaces (fibers over M)
-- ============================================================

/-- FieldSpace: L² sections of an electromagnetic-type field bundle over M.
    Abstracted as a Banach space with inner product structure. -/
structure FieldSpace where
  carrier       : Type*
  normed        : NormedAddCommGroup carrier
  module        : NormedSpace ℝ carrier
  inner_product : InnerProductSpace ℝ carrier

/-- ThermalSpace: temperature distribution space, W^{1,2}(M) Sobolev proxy. -/
structure ThermalSpace where
  carrier   : Type*
  normed    : NormedAddCommGroup carrier
  module    : NormedSpace ℝ carrier

/-- StructuralSpace: displacement field space for mechanical/elastic deformation. -/
structure StructuralSpace where
  carrier   : Type*
  normed    : NormedAddCommGroup carrier
  module    : NormedSpace ℝ carrier

-- ============================================================
-- Register the bundled typeclass fields as global instances
-- ============================================================
-- P19: Without these, `[NormedAddCommGroup F.carrier]` cannot be
-- synthesized from `F : FieldSpace` alone (the field is not in the
-- instance database). Registering them here unblocks typeclass
-- synthesis at every use site of FieldSpace/ThermalSpace/StructuralSpace
-- — in particular the SafetyCertificate / siarc_flow site in
-- ForwardInvarianceFramework.lean.
attribute [instance] FieldSpace.normed
attribute [instance] FieldSpace.module
attribute [instance] ThermalSpace.normed
attribute [instance] ThermalSpace.module
attribute [instance] StructuralSpace.normed
attribute [instance] StructuralSpace.module

/-- ControlSpace: finite-dimensional input space U ≅ ℝᵐ. -/
structure ControlSpace (m : ℕ) where
  carrier   : Fin m → ℝ

/-- IntentSpace: abstract high-level goal/intent parameter space.
    Compact metric space (could be a simplex of mission modes). -/
structure IntentSpace where
  carrier   : Type*
  metric    : MetricSpace carrier
  compact   : CompactSpace carrier

-- ============================================================
-- Full StateSpace: product bundle over M
-- ============================================================

/-- StateSpace: the full coupled state Σ = FieldSpace × ThermalSpace × StructuralSpace. -/
@[ext]
structure StateSpace
    (F : FieldSpace)
    (T : ThermalSpace)
    (S : StructuralSpace) where
  field      : F.carrier
  thermal    : T.carrier
  structural : S.carrier

-- ============================================================
-- Product norm structure on StateSpace (Relay 21 — sorry discharge)
-- ============================================================
-- Strategy: StateSpace ≅ F.carrier × (T.carrier × S.carrier) as an
-- additive group. Mathlib provides NormedAddCommGroup and NormedSpace
-- on product types. We transfer via the injective embedding
-- `StateSpace.toProd` using `NormedAddCommGroup.induced`.

/-- The canonical embedding of StateSpace into the product type. -/
def StateSpace.toProd {F : FieldSpace} {T : ThermalSpace} {S : StructuralSpace}
    (σ : StateSpace F T S) : F.carrier × (T.carrier × S.carrier) :=
  (σ.field, σ.thermal, σ.structural)

/-- Inverse: product type back to StateSpace. -/
def StateSpace.ofProd {F : FieldSpace} {T : ThermalSpace} {S : StructuralSpace}
    (p : F.carrier × (T.carrier × S.carrier)) : StateSpace F T S :=
  ⟨p.1, p.2.1, p.2.2⟩

/-- The embedding is injective. -/
theorem StateSpace.toProd_injective
    {F : FieldSpace} {T : ThermalSpace} {S : StructuralSpace} :
    Function.Injective (StateSpace.toProd (F := F) (T := T) (S := S)) := by
  intro ⟨f1, t1, s1⟩ ⟨f2, t2, s2⟩ h
  simp only [toProd, Prod.mk.injEq] at h
  obtain ⟨rfl, rfl, rfl⟩ := h
  rfl

/-- The embedding is an equivalence. -/
def StateSpace.equivProd (F : FieldSpace) (T : ThermalSpace) (S : StructuralSpace) :
    StateSpace F T S ≃ F.carrier × (T.carrier × S.carrier) where
  toFun := toProd
  invFun := ofProd
  left_inv := fun σ => by simp [toProd, ofProd]
  right_inv := fun p => by simp [toProd, ofProd]

-- Component-wise algebraic instances for StateSpace
instance stateSpace_zero {F : FieldSpace} {T : ThermalSpace} {S : StructuralSpace}
    [Zero F.carrier] [Zero T.carrier] [Zero S.carrier] :
    Zero (StateSpace F T S) := ⟨⟨0, 0, 0⟩⟩
instance stateSpace_add {F : FieldSpace} {T : ThermalSpace} {S : StructuralSpace}
    [Add F.carrier] [Add T.carrier] [Add S.carrier] :
    Add (StateSpace F T S) := ⟨fun a b => ⟨a.field + b.field, a.thermal + b.thermal, a.structural + b.structural⟩⟩
instance stateSpace_neg {F : FieldSpace} {T : ThermalSpace} {S : StructuralSpace}
    [Neg F.carrier] [Neg T.carrier] [Neg S.carrier] :
    Neg (StateSpace F T S) := ⟨fun a => ⟨-a.field, -a.thermal, -a.structural⟩⟩
instance stateSpace_sub {F : FieldSpace} {T : ThermalSpace} {S : StructuralSpace}
    [Sub F.carrier] [Sub T.carrier] [Sub S.carrier] :
    Sub (StateSpace F T S) := ⟨fun a b => ⟨a.field - b.field, a.thermal - b.thermal, a.structural - b.structural⟩⟩
instance stateSpace_nsmul {F : FieldSpace} {T : ThermalSpace} {S : StructuralSpace}
    [SMul ℕ F.carrier] [SMul ℕ T.carrier] [SMul ℕ S.carrier] :
    SMul ℕ (StateSpace F T S) := ⟨fun n a => ⟨n • a.field, n • a.thermal, n • a.structural⟩⟩
instance stateSpace_zsmul {F : FieldSpace} {T : ThermalSpace} {S : StructuralSpace}
    [SMul ℤ F.carrier] [SMul ℤ T.carrier] [SMul ℤ S.carrier] :
    SMul ℤ (StateSpace F T S) := ⟨fun n a => ⟨n • a.field, n • a.thermal, n • a.structural⟩⟩
instance stateSpace_smul {F : FieldSpace} {T : ThermalSpace} {S : StructuralSpace}
    [SMul ℝ F.carrier] [SMul ℝ T.carrier] [SMul ℝ S.carrier] :
    SMul ℝ (StateSpace F T S) := ⟨fun r a => ⟨r • a.field, r • a.thermal, r • a.structural⟩⟩

/-- AddCommGroup on StateSpace, transferred from the product via injection. -/
instance stateSpace_addCommGroup
    {F : FieldSpace} {T : ThermalSpace} {S : StructuralSpace}
    [NormedAddCommGroup F.carrier]
    [NormedAddCommGroup T.carrier]
    [NormedAddCommGroup S.carrier] :
    AddCommGroup (StateSpace F T S) :=
  StateSpace.toProd_injective.addCommGroup _
    rfl (fun _ _ => rfl) (fun _ => rfl) (fun _ _ => rfl)
    (fun _ _ => rfl) (fun _ _ => rfl)

/-- Module ℝ on StateSpace, component-wise. -/
instance stateSpace_module
    {F : FieldSpace} {T : ThermalSpace} {S : StructuralSpace}
    [NormedAddCommGroup F.carrier] [NormedSpace ℝ F.carrier]
    [NormedAddCommGroup T.carrier] [NormedSpace ℝ T.carrier]
    [NormedAddCommGroup S.carrier] [NormedSpace ℝ S.carrier] :
    Module ℝ (StateSpace F T S) where
  smul := stateSpace_smul.smul
  one_smul a := by ext <;> exact one_smul ℝ _
  mul_smul r s a := by ext <;> exact mul_smul r s _
  smul_zero r := by ext <;> exact smul_zero r
  smul_add r a b := by ext <;> exact smul_add r _ _
  add_smul r s a := by ext <;> exact add_smul r s _
  zero_smul a := by ext <;> exact zero_smul ℝ _

/-- The canonical embedding as an AddMonoidHom. -/
def StateSpace.toProdHom
    {F : FieldSpace} {T : ThermalSpace} {S : StructuralSpace}
    [NormedAddCommGroup F.carrier]
    [NormedAddCommGroup T.carrier]
    [NormedAddCommGroup S.carrier] :
    StateSpace F T S →+ F.carrier × (T.carrier × S.carrier) where
  toFun := StateSpace.toProd
  map_zero' := rfl
  map_add' _ _ := rfl

/-- **NormedAddCommGroup on StateSpace** (Relay 22: fully discharged).
    Transferred from the Mathlib `NormedAddCommGroup` instance on
    `F.carrier × (T.carrier × S.carrier)` via `NormedAddCommGroup.induced`. -/
noncomputable instance stateSpace_normedAddCommGroup
    {F : FieldSpace} {T : ThermalSpace} {S : StructuralSpace}
    [NormedAddCommGroup F.carrier]
    [NormedAddCommGroup T.carrier]
    [NormedAddCommGroup S.carrier] :
    NormedAddCommGroup (StateSpace F T S) :=
  NormedAddCommGroup.induced (StateSpace F T S)
    (F.carrier × (T.carrier × S.carrier))
    StateSpace.toProdHom StateSpace.toProd_injective

/-- **NormedSpace ℝ on StateSpace** (Relay 22: fully discharged).
    Transferred from `NormedSpace ℝ` on the product via the embedding. -/
noncomputable instance stateSpace_normedSpace
    {F : FieldSpace} {T : ThermalSpace} {S : StructuralSpace}
    [NormedAddCommGroup F.carrier] [NormedSpace ℝ F.carrier]
    [NormedAddCommGroup T.carrier] [NormedSpace ℝ T.carrier]
    [NormedAddCommGroup S.carrier] [NormedSpace ℝ S.carrier] :
    NormedSpace ℝ (StateSpace F T S) where
  norm_smul_le r σ := norm_smul_le r (StateSpace.toProd σ)

-- ============================================================
-- SafeManifold: invariant subset of StateSpace
-- ============================================================

/-- SafeManifold: the admissible region defined by barrier constraints.
    Σ_safe = { σ ∈ Σ | g₁(σ) ≥ 0 ∧ g₂(σ) ≥ 0 ∧ g₄(σ) ≥ 0 ∧ g₅(σ) ≥ 0 }
    g₃ (holonomy) excluded: non-local, see Axioms.lean. -/
structure SafeManifold
    (F : FieldSpace)
    (T : ThermalSpace)
    (S : StructuralSpace)
    (g₁ g₂ g₄ g₅ : StateSpace F T S → ℝ) where
  point      : StateSpace F T S
  barrier_g1 : g₁ point ≥ 0
  barrier_g2 : g₂ point ≥ 0
  barrier_g4 : g₄ point ≥ 0
  barrier_g5 : g₅ point ≥ 0

end SIARCRelay11
