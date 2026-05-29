# Verdict — VQ-N1 (V_quad base-object surface reclassification)

**Verdict ID:** VQ-N1
**Created in:** Tier-1 synthesizer session (4-leg CLI relay, Opus 4.8)
**Persisted by:** VQ-N1-APPLY (Opus 4.8), 2026-05-29
**Substrate:** VQ-N1 verdict artifact (see `vq_n1_verdict.json`, full content preserved)
**Band:** MEDIUM

---

## Aggregate verdict

**LABEL:** RETRACT-AND-REPLACE (surface relabel)
**STATUS:** CLOSED
**CLAIM:** V_quad base object is **canonical doubly-degenerate PV** on the **Sakai D5⁽¹⁾** surface,
symmetry **W(A3⁽¹⁾) ≅ affine 𝔖₄**, generic / non-classical — **NOT** PIII(D6).

- Retracted: `V_quad = PIII(D6) transcendent`.
- Replacement: `V_quad = M11 of a generic non-classical doubly-degenerate PV transcendent on Sakai D5⁽¹⁾, symmetry W(A3⁽¹⁾)`.
- Underlying mathematics (V_quad = M11, isomonodromy, Stokes/Borel data, PSLQ-null) is **INTACT**; only the surface **label** was wrong.

This verdict clears **HALT_A1_BASE_UNCORRECTED** (FIRE-A1 dependency gate).

---

## Corrected classification

| field | value |
|---|---|
| equation | canonical fifth Painlevé (PV), doubly-degenerate |
| params (α,β,γ,δ) | (1/6, 0, 0, −1/2) — standard-form PV |
| Sakai surface | **D5⁽¹⁾** |
| symmetry | **W(A3⁽¹⁾) ≅ affine 𝔖₄** |
| orbit class | generic / non-classical (alcove-interior; θ_∞ = 2/√3 irrational; α = θ_∞²/8 = 1/6) |
| z=0 | ordinary, exponents {0,1}, no z^(1/2) ramification |
| finite sing. | two apparent Fuchsian points at z = (−1 ± i√11)/6, indices [0,0] |
| ∞ | rank-1 **unramified** irregular point, σ± = ±1/√3 |
| reduces to PIII? | **NO** |

**PIII exclusion:** δ = −1/2 ≠ 0 lies off the PV→PIII coalescence locus (DLMF 32.2.33 sends δ_PV → 0);
PIII(D7) further excluded because z=0 is ordinary with no z^(1/2) ramification.

---

## Evidence chain (4 legs)

1. **Surface anchor (ARGUED + DLMF 32.2(ii)):** literal params give PIII(D7) not D6; δ=−1/2 flagged as PV normalization.
   Citations verified: Sakai 2001 CMP 220:165-229; KNY 2017 JPhysA 50:073001; Jimbo 1982 PublRIMS 18:1137-1161;
   Okamoto 1987 Funkcial.Ekvac.30 (pages PENDING).
2. **Coalescence (ARGUED + DLMF 32.2.32-33):** (1/6,0,0,−1/2) has no finite PIII image (limit forces δ_PV→0, but δ=−1/2≠0)
   ⇒ genuine PV. Surface coords reproduce banked α = θ_∞²/8 = 1/6 exactly (fixes floating norm = 1/2).
3. **Tie-breaker (VERIFIED-FROM-FILE):** z=0 ordinary; two finite apparent-Fuchsian points; rank-1 unramified at ∞;
   finite Fuchsian monodromy; PIII NO_MATCH. No z^(1/2) ramification ⇒ D7 excluded, **D5⁽¹⁾ confirmed**.
4. **Closeout (VERIFIED-FROM-FILE):** S = 0.43770528073458051568, σ_conn = 0.060876890825462076805 to stored precision;
   ξ0 = 1.1547211828… is a 2.06e-5 NEAR-MISS to 2/√3 (xi_0_algebraic=false) — reinforces non-classicality, not an identity.

---

## Okamoto anomaly block — VERIFY-FIRST outcome: **DROPPED-UNCONFIRMED** (NOT load-bearing)

Phase-1 step-4 verification (VQ-N1-APPLY, against live DLMF 32.2):

- (1/6,0,0,−1/2) are DLMF **standard-form** PV parameters (α,β,γ,δ). DLMF 32.2(ii) confirms δ=−1/2 is the canonical PV
  normalization and δ=−1 the PIII normalization.
- The asserted "α+α+β+β=0" is an Okamoto **symmetric-form** (affine-root) constraint in **different coordinates**
  (DLMF 32.2(v) / Okamoto aᵢ parameters), not the standard-form quadruple. Applying a symmetric-form sum-constraint to
  standard-form coordinates is a **coordinate-category mismatch**; the "violation" is not well-posed as stated.
- The exact D6⁽¹⁾ symmetric-form constraint could **not** be confirmed from available sources (Okamoto 1987 page ref PENDING).

**Decision:** per the VERIFY-FIRST fallback, the Okamoto corroboration is **DROPPED** (not asserted unverified).
**Verdict impact:** NONE — PV/D5⁽¹⁾ stands on legs 1–4.

---

## Transcendence class — HEURISTIC

S is excluded from the Γ-Barnes closed-form class to 300+ dps by direct PSLQ; combined with alcove-interior
non-classicality, S is **expected** transcendental over that class. Stated as **conjecture**, not theorem. A full proof
needs a transcendence theorem for connection coefficients of generic non-classical PV transcendents at CM points
(currently nonexistent). Manuscripts must state this as conjecture.

---

## Supersede edges (recorded; history preserved, nothing deleted)

| superseded | date | disposition | pointer |
|---|---|---|---|
| VQUAD-PIII-NORMALIZATION-MAP | 2026-05-02 | WITHDRAWN-AND-REPLACED | `sessions/2026-05-02/VQUAD-PIII-NORMALIZATION-MAP/SUPERSEDED_BY_VQ-N1.json` |
| FRONTIER-A scope slot-189 | 2026-05-11 | SCOPE-INVALIDATED-PENDING-REBASE | `sessions/2026-05-11/T1-SYNTH-FRONTIER-A-RESCOPE-CONSULTATION-189/SCOPE_INVALIDATED_BY_VQ-N1.json` |

---

## Downstream (Phase 2 — STAGED ONLY, operator-gated; see handoff.md)

Tier-1 substantive (versioned-on-approval), Tier-2 Frontier-A re-base (D6→D5⁽¹⁾; danger object = Noumi-Yamada A3⁽¹⁾),
Tier-3 ledger hygiene (claims.jsonl L179 append-not-overwrite; index/log label fixes; folder rename LAST).
No downstream edits applied in this run.
