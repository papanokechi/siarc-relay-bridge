# Sub-problem B / Stage 1.3 — Fresán–Jossen rapid-decay-class compatibility

**Slot:** PERIOD-REP-VQUAD-003 · **Stage:** 1.3 · **Date:** 2026-06-15
**Status:** COMPLETE

Fresán–Jossen (FJ) define the rapid-decay homology H₁^{rd}(X, M) of an exponential
D-module M = (algebraic connection) ⊗ E^{−f}. A cycle γ is **admissible** iff it satisfies
three conditions (FJ *Exponential Motives*; `fresan-jossen-axioms.md` this slot). We verify
each for our γ.

| FJ condition | Requirement | V_quad γ | Status |
|---|---|---|---|
| **(C1) finite-singularity integrability** | chain endpoints/boundary at the singular locus Z of M must give a convergent (locally L¹) integrand | branch point −ξ₀ with exponent −(1+β) > −1 ⇒ ∫ r^{−(1+β)} dr finite (Stage 1.2 §2) | **OK** |
| **(C2) rapid decay at ∞** | non-compact ends must run into directions where \|e^{−f}\| = \|e^{ξ}\| decays super-polynomially | both lips → −∞ along arg ξ = π, \|e^{ξ}\| = e^{−s} → 0 (Stage 1.2 §1) | **OK** |
| **(C3) closedness in H₁(X, Z; rd)** | γ is a relative cycle: ∂γ supported on Z ∪ {rapid-decay ∞}; the integrand df has no other critical-value contribution that would open the chain | ∂γ = {−ξ₀} ∪ {arg = π end at ∞}; f = −ξ has **no finite critical point** (df = −dξ ≠ 0); only the slope-1 irregular direction at ∞ contributes, captured by the rd end | **OK** |

---

## 1. (C1) Algebraic integrability at finite singularities

The only finite singularity of M crossed by γ is the regular-singular branch point −ξ₀ of
L_V (the point ξ = 0 is **apparent**, hence not a true singularity of the solution sheaf,
and is not on γ). The local exponent −(1+β) = −0.80754991… exceeds −1, so the singularity
is of **algebraic / tame** type with locally integrable integrand. FJ class this as a
"moderate" boundary point — the chain is allowed to end on it. ✔

## 2. (C2) Exponential decay at infinity along the cycle direction

FJ's rapid-decay condition is that along each non-compact branch the chain enters the
"region of rapid decay" R_f = { ξ : Re(f(ξ)) → +∞ } = { Re(−ξ) → +∞ } = { Re ξ → −∞ }.
Our rays do exactly this (arg ξ = π). The decay is genuinely exponential (e^{−s}),
stronger than the "faster than any polynomial" FJ minimum. ✔

## 3. (C3) Closedness / relative-cycle condition

A rapid-decay homology class must be a **relative** 1-cycle: its boundary may live only on
Z = Sing(M)_finite = {−ξ₀} together with the rapid-decay locus at ∞. We check there is no
*hidden* boundary:

* **f has no finite critical point.** f = −ξ ⇒ df = −dξ, nowhere zero on 𝔸¹. So there is
  no interior critical value at which the thimble could fail to close — the only critical
  direction is the irregular slope-1 direction at ∞, which is precisely the rapid-decay
  end. (Contrast: an f with a finite Morse critical point would require an additional
  Lefschetz thimble; here there is none.)
* **Single relevant Stokes direction.** L_V has slope 1 at ∞ with the dominant Borel
  singularity on arg = π (VQUAD-002 sign fix). The thimble wraps exactly that one cut; no
  second cut competes (the locus is finite — "no resurgent tower", VQUAD-002 bonus
  finding), so γ is a *single* well-defined relative class, not a sum over a lattice of
  alien directions.
* **Monodromy-consistent gluing.** The two lips carry determinations differing by
  e^{∓2πi(1+β)}; the clockwise γ_loop glues them into a closed relative chain (the loop
  contribution → 0 as ε → 0 because −(1+β) > −1). Hence ∂γ ⊆ Z ∪ {∞_{rd}}. ✔

---

## 4. Conclusion

γ satisfies **all three** FJ admissibility conditions and therefore defines a class

> **[γ] ∈ H₁^{rd}(𝔸¹_{ℚ(√3)}, M),  M = (L_V-module) ⊗ E^{ξ}.**

The pairing ⟨[γ], [B̂ dξ]_{dR}⟩ = ∫_γ e^{ξ} B̂ dξ is therefore a **bona-fide exponential
period** in the Fresán–Jossen sense, with the algebraicity of ω over ℚ(√3) supplied by
VQUAD-002 (GO_clean). The auxiliary FJ conditions flagged in `fresan-jossen-axioms.md`
(no finite critical locus competing; Hodge/decay boundary correctly placed) are the ones
verified above in (C3); they are the "easy-to-miss" conditions the eventual paper must
state explicitly. ∎

---

## 5. Sourcing

* FJ three-condition rapid-decay admissibility: `fresan-jossen-axioms.md` (this slot);
  FJ *Exponential Motives* (rapid-decay homology chapter).
* Apparent vs. true singularity at 0; finite locus / no resurgent tower; arg=π sign:
  VQUAD-002 `operator-verification.md` §4.0–4.2 and final-verdict.md.
* ω algebraic over ℚ(√3): VQUAD-002 `disposition-applied.md` (outcome_GO_clean).
* Integrability (−(1+β) > −1) and exponential end-decay: this slot Stages 1.2, 1.4.

**Verdict 1.3: γ is FJ-admissible (C1, C2, C3 all OK); ∫_γ e^{ξ} B̂ dξ is an exponential
period in the Fresán–Jossen sense.**
