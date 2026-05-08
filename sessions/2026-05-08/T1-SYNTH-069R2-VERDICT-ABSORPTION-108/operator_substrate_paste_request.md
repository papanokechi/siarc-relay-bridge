# Operator substrate-paste request — round 1 (post-069r2 verdict)

**Goal**: resolve QA + QB.1 + QB.4 + QE in a single Claude.ai web follow-up turn by pasting four named substrate excerpts.

**Synth instruction (from 069r2 §5 verdict packet caveat 1)**:
> Suggest a single follow-up substrate-paste turn rather than five separate ones. Minimum substrate to re-fire usefully: (i) FW abstract + TOC + §3 parameter definitions; (ii) KNY 2017 §8.5.17 H_D6^KNY explicit Hamiltonian display (eqs. 8.237–8.239); (iii) Okamoto 1987 §1 H_III explicit Hamiltonian display; (iv) CT v1.3 §3.5 (η,θ) → (α,β) rename equation(s).

---

## Paste structure for Claude.ai web follow-up turn

Suggested opening line for the operator's paste:

> Round-1 substrate-paste for 069r2 follow-up. Per your §5 caveat 1, here are the four named excerpts. Please re-fire QA, QB.1, QB.4, QE (and QB.2 derivatively). All other 069r2 envelope context still applies (Route A/B/C/D/E namespace, HALT-S1 through HALT-S6, Round-1 + Round-2 rubber-duck QA acknowledged).

Then four substrate blocks, in this order:

### Excerpt FW (for QB.1)

```
=== FW arXiv math-ph/0201051 (Forrester-Witte 2002, "Application of the τ-function theory of Painlevé equations to random matrices: P_VI, the JUE, CyUE, cJUE and scaled limits") ===

[OPERATOR: paste]
- abstract (full)
- TOC / section headings
- §3 P_III parameter definitions (specifically the equation(s) defining how FW parameterizes P_III, and any references to KNY (a_0, a_1, a_2) or to (η_∞, η_0, θ_∞, θ_0))

If §3 is not the relevant section (FW's organization may differ), paste whatever section defines FW's P_III parametrisation.
```

### Excerpt KNY (for QA)

```
=== Kajiwara-Noumi-Yamada 2017 §8.5.17 H_D6^KNY explicit Hamiltonian display ===

[OPERATOR: paste]
- equations 8.237–8.239 (the explicit (q, p, t) form of H_D6^KNY)
- any surrounding text defining the (a_0, a_1, a_2) parameter constraints (specifically the affine root sum a_0 + a_1 + a_2 = 1 if applicable)
- any explicit derivation showing how (q, p, t) variables relate to the underlying Painlevé III(D_6) ODE
```

### Excerpt Okamoto (for QA)

```
=== Okamoto 1987 §1 H_III explicit Hamiltonian display ===

[OPERATOR: paste]
- the explicit (q, p, t) form of H_III in Okamoto's parametrisation (η_∞, η_0, θ_∞, θ_0)
- any text defining each of the four parameters (η_∞, η_0, θ_∞, θ_0)
- the equation(s) showing how H_III relates to the Painlevé III ODE
- if available, any cross-reference Okamoto makes to JM 1981 or to other parametrisations (Witte, Forrester, etc.)
```

### Excerpt CT v1.3 §3.5 (for QE)

```
=== CT v1.3 §3.5 (η,θ) → (α,β) rename equation(s) — CURRENT STATE ===

[OPERATOR: paste from tex/submitted/control center/Channel_Theory_v1.3.tex (or the canonical CT v1.3 source)]
- the explicit equation(s) defining (α_∞, α_0, β_∞, β_0) in terms of Okamoto's (η_∞, η_0, θ_∞, θ_0)
- any surrounding text justifying the rename (whether pure relabel or including affine/additive shift)
- if the rename derivation does NOT yet exist as an explicit derivation in CT v1.3 §3.5, paste the section as-is and note "[NO EXPLICIT RENAME DERIVATION; PARALLEL-TRACK ROUTE E GOVERNANCE WORK PENDING]"
```

---

## Re-fire instructions (paste at end of operator's Claude.ai web turn)

> Re-fire scope: QA + QB.1 + QB.4 + QE (and QB.2 derivatively). Do NOT re-evaluate QB.3 (already Y_RENAME_REQUIRED, robust). QC remains N-A unless QA + QB.4 both land NO_GO. QD will be addressed in a separate round-2 substrate-paste turn (V_quad numerical-solution structure + (α,β) extraction operation spec).
>
> Watch-list per your §5 caveat 4: if FW excerpts reveal Sakai D_6 surface-type machinery as the chart-map mechanism (vs σ-form / Hamiltonian P_III), please flag ROUTE_FRAME_INCOMPLETE per HALT-S5 rather than fold into A–E. Vocabulary triggers: "Sakai D_6 surface", "surface-type machinery", "Mukai pair", "rational surface" / "blow-up" / "exceptional curve", W(D_6) extended affine Weyl group.
>
> Acceptance criterion to bake into whichever route lands GO: explicitly trace where the −1/3 null-sum offset (EXCERPT 4 anomaly D2) originates. This is per your §5 caveat 3.

---

## Operator-side tasks before paste

| Task | Notes |
|---|---|
| Acquire FW math-ph/0201051 PDF | OA on arXiv. URL: `https://arxiv.org/abs/math-ph/0201051`. Apply Bibliographic Pre-Verification rule (memory `Bibliographic identifier pre-verification`): confirm DOI/arXiv resolves to FW 2002 before extracting. |
| Acquire KNY 2017 PDF | Reference: Kajiwara-Noumi-Yamada, "Geometric Aspects of Painlevé Equations" J. Phys. A: Math. Theor. 50 (2017) 073001. Should be in operator local library. |
| Acquire Okamoto 1987 PDF | Reference: Okamoto, "Studies on the Painlevé equations III. Second and Fourth Painlevé equations P_II and P_IV" Math. Ann. 275 (1986) 221-255 (or §1 of the P_III paper, Funkcial. Ekvac. 30 (1987) 305-332 — operator picks which). |
| Locate CT v1.3 §3.5 in canonical source | `tex/submitted/Channel_Theory_v1.3.tex` or wherever the latest §3.5 (η,θ)→(α,β) rename text resides. |

## Estimated time: paste-prep + Claude.ai web turn ≈ 30 min operator + ~5 min synth turn.
