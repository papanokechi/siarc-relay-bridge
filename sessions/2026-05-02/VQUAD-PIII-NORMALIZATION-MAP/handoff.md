# Handoff --- VQUAD-PIII-NORMALIZATION-MAP

**Date:** 2026-05-02
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~75 minutes
**Status:** PARTIAL

## What was accomplished

Asked: write the explicit change-of-variables Φ that maps V_quad's
Stokes data to canonical `P_III(D_6)` Hamiltonian-form Stokes data,
in order to lift the H4-measured 108-digit alien amplitude `C` from
V_quad-native normalization into canonical-form normalization.

Delivered: V_quad's homogeneous scalar OGF ODE re-derived from the
recurrence symbolically (sympy-verified to exact rational/algebraic
coefficients), Newton-polygon slope 1/2 confirmed, characteristic
exponent c = ±2/√3 and secondary exponent ρ = -11/6 re-derived from
scratch, V_quad-native Hamiltonian written, the Φ_resc and Φ_shift
components of Φ pinned (modulo three documented residuals), and the
Φ_symp component documented as a clean residual blocker (R5)
requiring the Okamoto 1987 Lax pair.

Verdict reached: **G15_PARTIAL**. Φ_resc and Φ_shift pinned; Φ_symp
residual; numerical canonical-form value `C_can` *not* produced
(would require fabricating R2-R5, which the prompt's "Do NOT" clause
forbids).

## Key numerical findings

- V_quad scalar ODE: `3 z³ f''(z) + 10 z² f'(z) + (5z + z² − 1) f(z) = 0` (exact rational; `verify_vquad_ode.py`)
- Newton polygon at z=0: single edge slope 1/2 (rank-1/2 irregular singularity); exact
- Characteristic exponent: c = ±2/√3 (exact algebraic; `verify_vquad_ode.py`)
- Borel singular distance: ζ_* = 4/√3 (exact algebraic; agrees with Prompt 005 to 250 digits by reference, hash preserved)
- Secondary Birkhoff exponent: ρ = -11/6 (exact rational; `verify_vquad_ode.py`)
- Φ_resc parameter: λ = c_0²/4 = 1/3 (exact, R3-conditional)
- Φ_shift Jacobian on Stokes data: 1 (exact, affine-shift triviality)
- Φ_symp Jacobian: NOT computed (residual R5)
- C_can: NOT numerically computed in this session
- S_{ζ_*}^can: NOT numerically computed in this session

## Judgment calls made

1. **Verdict choice (PARTIAL vs HARD HALT for missing literature).** The prompt's "Do NOT fabricate" clause and its PARTIAL definition are in mild tension. I read PARTIAL as the prompt's intended landing for "two of three Φ-blocks pinned, one blocked by literature", and HARD HALT as reserved for the case where *no* progress is possible. Phase A and most of Phase C *were* possible; Phases D and the symplectic part of C were not. PARTIAL fits.

2. **Re-derive V_quad's scalar ODE rather than cite CT v1.3.** Phase A's symbolic re-derivation gives an independent reproducibility line for the AEAL chain, with a fresh sha256 hash, rather than citing the CT v1.3 200-digit numerical verification. This is slightly redundant but cheap and provides an independent check.

3. **Treat the (1/6, 0, 0, -1/2) constraint mismatch as informational, not a halt.** The four numbers do not sum to zero, contrary to the Okamoto constraint quoted in the relay-prompt brief. I logged this in `unexpected_finds.json` and as residual R1 in `phi_change_of_variables.tex` rather than raising `G15_NORMALIZATION_AMBIGUOUS`, because the mismatch reduces to a convention question (Okamoto-Sakai vs CT v1.3 internal convention) and CT v1.3 §3.5 itself has no numerical inconsistency.

4. **Do not fabricate σ_0 = 0 to produce a numerical C_can.** Setting σ_0 = 0 would let me write `C_can = (1/3)^(11/12) * J_symp * 8.127336795...`, which would be a single number (with J_symp also fabricated). The prompt forbids this. I documented the symbolic form only.

5. **Did not modify the CC-MEDIAN-RESURGENCE-EXECUTE session contents.** Referenced the H4 measurement by hash in canonical_S_zeta_star.txt and claims.jsonl, in compliance with the prompt's "Do NOT modify" clause.

## Anomalies and open questions

**THIS IS THE MOST IMPORTANT SECTION (per standing instructions).**

### Layer separation between V_quad's scalar ODE and `P_III(D_6)`

V_quad's OGF satisfies a *linear* second-order ODE whose
Hamiltonization is *quadratic in p* (linear Hamiltonian). The
canonical `P_III(D_6)` Hamiltonian quoted in the relay-prompt brief
is *quadratic in p but with non-trivial q-p coupling* --- a genuinely
nonlinear Hamiltonian on (q, p). These two Hamiltonians live at
**different layers** of the geometry:

- V_quad's scalar ODE = the **L-equation** of an isomonodromic Lax
  pair (linear, frozen at the V_quad parameter point);
- `P_III(D_6)` (q, p, t) Hamiltonian = the **isomonodromic
  deformation** of that L-equation (nonlinear, in coordinates that
  are monodromy data of the Lax pair).

CT v1.3 §3.5's framing "algebraic identity at Painlevé-class level
only" gestures at this layer separation but does not spell it out.
Spelling it out is the substantive structural conclusion of this
session.

**Implication:** Φ cannot be a direct change-of-variables on
(f, f', z); it must act on the Lax-pair monodromy variety. This is
what makes R5 (Okamoto's explicit Lax pair) the *primary* blocker,
and what the rubber-duck self-critique (§3) flags for Claude review.

### Okamoto-constraint mismatch

CT v1.3 §3.5's parameter point (1/6, 0, 0, -1/2) does not satisfy
α_∞ + α_0 + β_∞ + β_0 = 0 (it sums to -1/3). This is documented in
`unexpected_finds.json` and as residual R1 in
`phi_change_of_variables.tex`. Three interpretations are listed; no
selection is made without R1 resolution.

**Recommendation for Claude:** review whether CT v1.3 §3.5 should
clarify which parameter convention (Okamoto, Sakai, or internal) it
uses for the (1/6, 0, 0, -1/2) point. This may be a CT v1.4
amendment candidate, but I am explicitly *not* rewriting CT v1.3 in
this session (per "Do NOT" clause).

### Why no numerical Phase D

Producing a 50-digit C_can would require fixing R2 (canonical
trans-series prefactor σ_0), R3 (Stokes sign convention), and R5
(Φ_symp Jacobian factor). All three are pieces of Okamoto 1987 and
Conte-Musette ch. 7 not in the operator's library. Fabricating any
of them violates the prompt's "Do NOT fabricate parameter values"
clause.

## What would have been asked (if bidirectional)

1. *"Do you have local PDF access to Okamoto 1987 (Funkcial. Ekvac. 30:305-332) or Conte-Musette 2008 ch. 7? If yes, I can pull the explicit Lax pair and continue Phase C-D fully (estimated +2 hours). If no, PARTIAL is the correct landing."*

2. *"The CT v1.3 §3.5 parameter point (1/6, 0, 0, -1/2) does not satisfy the Okamoto α + α + β + β = 0 constraint. Is this a known convention difference (CT v1.3 internal vs Okamoto/Sakai), or should I treat it as a halt-class anomaly?"*

3. *"Should I push to compute the 'best-effort' C_can with placeholder σ_0 = 0 and J_symp = 1 to provide a numerical anchor for Claude to compare against the literature, even though the prompt forbids fabrication? My reading of the prompt is no, but the H4 result has been waiting for canonical-form lift since Prompt 005, and a flagged-placeholder may be more useful than no number at all."*

## Recommended next step

**Operator action:** acquire Okamoto 1987 §§2-3 (the explicit Lax
pair --- ~10 pages) and Conte-Musette 2008 ch. 7 §§7.3-7.4
(parameter conventions and trans-series tables --- ~25 pages) via
the existing G3b ILL/AMS workflow. Both are standard library items.

**Next prompt (estimated 2-4 hr runtime):** `VQUAD-PIII-NORM-MAP-CLOSE`,
hard-gated on R5 (Lax pair). Pin R1-R4 from the literature, write
Φ_symp explicitly from the Lax-pair gauge transform, compute J(Φ)
numerically, verify `S_{ζ_*}^can` against Lisovyy-Roussillon's
P_III connection-problem tables to ≥ 50 digits.

Alternative if the literature acquisition is slow: continue with
Prompt 010 (T3 Stokes-multiplier follow-up) and other independent
prompts (002, 006, 008, 011, 012); G15 closure is gated on R5, not
on time.

## Files committed

Located at `sessions/2026-05-02/VQUAD-PIII-NORMALIZATION-MAP/`:

- `verify_vquad_ode.py` --- Phase A symbolic check (sympy)
- `verify_vquad_ode.log` --- Phase A output (sha256: 9c6c7865...e451213)
- `_compute_hashes.py` --- helper for AEAL hashes
- `_hashes.json` --- sha256 of all deliverables
- `vquad_hamiltonian.tex` --- Phase A deliverable
- `pIII_canonical.tex` --- Phase B deliverable
- `phi_change_of_variables.tex` --- Phase C deliverable (verdict)
- `canonical_S_zeta_star.txt` --- Phase D output (symbolic-only)
- `literature_crosscheck.md` --- Phase E deliverable
- `claims.jsonl` --- 12 AEAL entries (4 exact, 5 derivation, 2 literature_gap, 1 audit)
- `halt_log.json` --- empty `{}` (no halt triggered)
- `discrepancy_log.json` --- empty `{}` (no discrepancy)
- `unexpected_finds.json` --- 2 entries (Okamoto-constraint mismatch + layer-separation insight)
- `rubber_duck_critique.md` --- self-review
- `handoff.md` --- this file

## AEAL claim count

**12** entries written to `claims.jsonl` this session
(prompt asked for ≥ 6; the additional 6 are the layer-separation
audit entry, the Φ_shift triviality entry, the explicit "C_can NOT
COMPUTED" entry, and three V_quad-native sanity-check entries that
provide the reproducibility chain for Phase A).
