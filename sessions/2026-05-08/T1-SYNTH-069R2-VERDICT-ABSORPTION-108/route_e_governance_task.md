# Route E governance task — operator-side parallel-track

**Status**: TIER-A action per `cascade_plan.md`
**Owner**: operator (papanokechi)
**Synth turn required**: NO (operator-side authoring only)
**Blocker**: nothing (no-regret action; binding regardless of which of Routes A/B/C/D ultimately lands GO)
**Estimated effort**: ~1-2 hours operator-time depending on whether the rename is trivial relabel or non-trivial additive-shift-included
**Triggered by**: 069r2 verdict QB.3 = Y_RENAME_REQUIRED (decisive non-deferred finding)

## Why this work is binding

Per the 069r2 §5 verdict packet QB.3 reasoning:

> EXCERPT 1 is direct: Okamoto 1987 uses (η_∞, η_0, θ_∞, θ_0) and the project's (α_∞, α_0, β_∞, β_0) is "a project-side rename adopted in CT v1.3 §3.5 rewrite." Therefore Okamoto §3 does not surface the project's (α, β) form; the rename is a separate step. This makes Route E precondition binding for Route B (and equally for Routes A, C, D).

Whatever closes M6.CC R1, the closure substrate will be derived in some literature parametrisation ((η, θ) for Okamoto-side; (a_0, a_1, a_2) for KNY-side; possibly something else for FW). To compose with the project's CT v1.3 §3.5 (α, β) namespace, an explicit rename derivation must exist.

## Scope of authoring

CT v1.3 §3.5 currently adopts the (α_∞, α_0, β_∞, β_0) namespace as a project-side rename of Okamoto's (η_∞, η_0, θ_∞, θ_0). The current state of the rename derivation in §3.5 is unknown to the agent — it may already exist as an explicit derivation, or it may be a footnote / parenthetical / "by the standard rename" reference without explicit equations.

The operator-side governance work is to:

1. **Locate the current rename text in CT v1.3 §3.5.** Identify whether it is:
   - (a) An explicit derivation with displayed equations
   - (b) A parenthetical or footnote pointing to a standard reference
   - (c) Implicit / not present

2. **If (b) or (c)**: author an explicit derivation. The derivation should consist of:
   - A statement of the four equations defining each (α, β) parameter in terms of (η, θ)
   - A justification / citation showing where this rename originates (a known standard rename in the Painlevé literature, OR a project-internal choice)
   - If the rename includes ANY additive or affine shift (beyond pure relabel), explicit display of the shift terms

3. **−1/3 null-sum offset check.** The 069r2 verdict Anomaly 2 + 3 noted that V_quad's image (1/6, 0, 0, −1/2) violates Okamoto's α_∞ + α_0 + β_∞ + β_0 = 0 by exactly −1/3. This is plausibly a structural feature of the rename (additive-shift-included) rather than a residual gap. The operator's authoring should explicitly address whether the rename produces a constant additive shift of −1/3 in the null-sum, OR whether the −1/3 originates elsewhere (Hamiltonian expansion, integration constant, etc.).

4. **Symbol collision check.** Per 058R phase_b5 (verdict EXCERPT 2): the project namespace has TWO (α, β)-tuples — Okamoto-derived (α_∞, α_0, β_∞, β_0) and the P_III ODE coefficients (α, β, γ, δ). The §3.5 rename derivation should explicitly disambiguate these two namespaces (e.g., subscripting, alternative letter, or explicit "Okamoto (α, β)" / "P_III ODE (α, β, γ, δ)" disambiguation in §3.5 prose).

## Output deliverable

A revised CT v1.3 §3.5 sub-section (or new §3.5.x sub-sub-section) with:
- Title: e.g., "Rename derivation: Okamoto (η, θ) → project (α, β)"
- Four displayed equations defining the rename
- Justification (1-2 paragraphs) covering origin, relabel-vs-shift status, and −1/3 offset accounting
- Symbol collision disambiguation note

If the rename turns out to be pure relabel with no additive shift (ROUTE_E_TRIVIAL per QE), the deliverable can be lighter weight — a single displayed paragraph with the four relabel equations.

If the rename turns out to include an additive shift (ROUTE_E_NONTRIVIAL_REQUIRED per QE), the deliverable should be more substantial and likely require some computation to identify the shift.

## After completion

When the operator-authored §3.5 rename derivation is complete:

1. Bridge-deposit the revised §3.5 text as a new bridge session (e.g., `T1-OPERATOR-CT-V13-S35-RENAME-DERIVATION-NNN`).
2. Update SQL todos: mark `069r2-route-e-governance-parallel-track` → done.
3. The substrate-paste round 1 (TIER-B per cascade_plan) can use the just-authored §3.5 rename text as the fourth excerpt — saving the operator a re-trip.

## SQL todo

A new SQL todo `069r2-route-e-governance-parallel-track` is inserted (description: "operator-side authoring of CT v1.3 §3.5 (η,θ)→(α,β) rename derivation; binding for Route E precondition; no-regret parallel-track per 069r2 verdict QB.3 = Y_RENAME_REQUIRED").

This todo can run in parallel with substrate-paste-round-1 preparation (TIER-B). Order recommendation: do this Route E work FIRST so its output can feed directly into the round-1 paste as the fourth excerpt.
