# Phase D — Verdict aggregation + numerical cross-check identification

**Session:** 058R CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE
**Phase D verdict:** **UPGRADE_V1_0_PARTIAL_NUMERICAL** (per spec §6
OUTCOME LADDER position 2 of 4).

---

## D.1 — Signal aggregation

| phase   | signal                          | basis                                                        |
|---------|---------------------------------|--------------------------------------------------------------|
| A       | A_VERIFIED                      | sympy re-derivation; H4 cross-check β = 0                    |
| B       | B_VERIFIED_STRUCTURAL           | KNY 2017 §8.5.17 closes R5 (Lax pair); Φ_symp Jacobian deferred |
| B.5     | B5_VERIFIED_WITH_CAVEAT         | Okamoto-Sakai cross-walk reconciled (W(B_2) ⊃ W((2A_1)^(1))) |
| C       | C_LITERATURE_UNIFORM            | 5/5 anchors PASS; SHA 6/6 spec §1 PRIMARY anchors PASS       |

**Aggregated: structural verdict UPGRADE_V1_0_PARTIAL_NUMERICAL.**

The candidate-UPGRADE_V1_0_FULL ladder rung requires **Phase D.2
numerical cross-check at ≥ 5 digits** between $M(C_{V})$ and BLMP
2024's canonical-form value, where $C_{V} = 8.12733679549507\ldots$ is
the V_quad-native Stokes amplitude (H4 measurement).

In 058R the numerical cross-check is **NOT executed** because:

1. The **Φ_symp Jacobian factor** $|\det J(\Phi_{\mathrm{symp}})|$
   acting on Stokes data depends on the explicit gauge transformation
   from V_quad's scalar-OGF Lax representation to the KNY 2017 §8.5.17
   2nd-order scalar Lax form $L_{1} y = 0$ (eq. 8.239). Constructing
   this gauge transformation symbolically is a **separate symbolic-
   computation cycle** (estimated 4–8 hr agent time) and not in scope
   for 058R's structural-closure mandate.

2. **BLMP 2024 does not provide a numerical Stokes constant for the
   V_quad parameter point.** BLMP 2024 §4–§5 give the structural
   parametrisation of the cubic-surface monodromy manifold via
   monodromy parameters $(e_{1}, e_{2}) \in (\mathbb{C}^{*})^{2}$
   (Definition 1.3, eq. 1.16), with the connection-matrix formula
   eq. 4.28 implicit. To extract a numerical Stokes constant for
   V_quad's specific parameter point requires:

   (a) explicit conversion of CT v1.3 §3.5 four-tuple
       $(\alpha_{\infty}, \alpha_{0}, \beta_{\infty}, \beta_{0}) =
       (1/6, 0, 0, -1/2)$ to KNY $(a_{0}, a_{1}, a_{2})$ with
       $a_{0}+a_{1}=1$ — residual R1, partially open (the four-tuple
       does not satisfy Okamoto's null-sum constraint, sums to
       $-1/3$; surfaced as anomaly D2);

   (b) evaluation of BLMP 2024 §4 connection-matrix integral for the
       specific KNY-side parameter point;

   (c) tracking the multiplicative factor $|\det J(\Phi_{\mathrm{symp}})|$
       from (1).

This is the **classical UPGRADE_V1_0_PARTIAL_NUMERICAL ladder rung**
per spec §6: "Phases A + B + B.5 + C all pass structurally; Phase
D.2 numerical cross-check unavailable (Barhoumi-Lisovyy 2024 provides
only structural monodromy data without numerical Stokes constants for
the specific parameter values)."

## D.2 — Numerical cross-check (DEFERRED, identification only)

The structural cross-check chain that would close UPGRADE_V1_0_FULL:

$$\underbrace{|C_{V_{\mathrm{quad}}}|}_{= 8.127336795\ldots\ \text{(H4)}} \;\;\xrightarrow{\;M^{*}\;}\;\;
   \underbrace{|S_{\zeta_{*}}^{\mathrm{can}}|}_{\text{= ?, BLMP 2024 §4}}.$$

The numerical Phase-D.2 follow-up session would compute
$|S_{\zeta_{*}}^{\mathrm{can}}|$ via:

1. Pull KNY 2017 §8.5.17 differential Lax form (eq. 8.239) at V_quad-
   parameter point $(a_{1}, a_{2})$ (after R1 closure).
2. Extract the leading Stokes constant from the connection problem
   for $L_{1} y = 0$ near $x = 0$ (irregular singularity rank 1).
3. Evaluate $|M^{*} C_{V}|$ where $M^{*}$ acts as $\lambda^{?} \cdot
   |\det J(\Phi_{\mathrm{symp}})|$ on the Stokes-data part of $C_{V}$
   (here $\lambda = 1/3$ from Phase B; the symplectic Jacobian factor
   is the open numerical residual).
4. Verify $|S_{\zeta_{*}}^{\mathrm{can}}| - |M^{*} C_{V}| < 10^{-N}$
   at $N \ge 5$ digits.

**This is NOT performed in 058R.** Identification only.

If this follow-up session lands UPGRADE_V1_0_FULL: M9 gating reduces
from {M4-with-formal-baseline-+-structural-roadmap, M6.CC} to
{M4-with-formal-baseline-+-structural-roadmap}; M6.CC ✅ closes;
G15 fully closed; G22 fully closed; op:cc-formal-borel residual
fully resolved.

If the follow-up session instead surfaces a structural inconsistency
(e.g., R1 non-closable or Φ_symp Jacobian non-existent in canonical
form), it triggers `HALT_M6_PHASE_B_CONSTRUCTION_INCOMPLETE` with
specific obstruction reported.

## D.3 — Halt aggregation (final scan)

| halt code                                        | trigger? | basis                                                |
|--------------------------------------------------|----------|------------------------------------------------------|
| HALT_M6_LITERATURE_NOT_LANDED                    | NO       | C.0 PASS 16/16                                       |
| HALT_M6_BIRKHOFF_SERIES_DRIFT                    | NO       | A_VERIFIED; β = 0 matches H4 to 107 dps              |
| HALT_M6_PHASE_B_CONSTRUCTION_INCOMPLETE          | NO       | KNY 2017 §8.5.17 closes R5 structurally              |
| HALT_M6_NORMALIZATION_INCONSISTENCY              | NO       | M composition internally consistent on relevant chart|
| HALT_M6_AFFINE_WEYL_MISMATCH                     | NO       | B5 cross-walk explicit (inclusion); D3 anomaly only  |
| HALT_M6_LITERATURE_DISAGREES_WITH_H4             | NO       | 5/5 anchors uniform with Phase A H4 substrate        |
| HALT_M6_STOKES_NUMERICAL_MISMATCH                | N/A      | D.2 numerical cross-check NOT executed (deferred)    |
| HALT_M6_BIBKEY_COLLISION                         | NO       | Phase 0.5: zero new bibkeys collide; CC-NOTE outline |

| 058R wrapper halt                                | trigger? | basis                                                |
|--------------------------------------------------|----------|------------------------------------------------------|
| HALT_058R_T1P2_NOT_LANDED                        | NO       | 051 LANDED at `9c75f65` with 10 AEAL T1P2B-A1..A10   |
| HALT_058R_PREFLIGHT_NO_GO                        | NO       | 057 LANDED at `9d6e801` with §5 = GO; 16/16 SHA PASS |
| HALT_058R_SPEC_DRIFT                             | NO       | 9 phase headers + 8 spec halts at expected line numbers; spec SHA `BE3F8FE9..F6E3319` |
| HALT_058R_M6_TOKEN_OVERREACH                     | NO       | STEP 4 sweep: zero bare-M6 in NEW prose (M6.CC + M6.H4 only) |
| HALT_058R_VERDICT_LADDER_DRIFT                   | NO       | Phase F verdict UPGRADE_V1_0_PARTIAL_NUMERICAL is ladder rung 2 of 4 |
| HALT_058R_058_DEPOSIT_MODIFIED                   | NO       | 058 halt deposit at `29f0646` bit-identical (P11 read-only check PASS) |
| HALT_058R_SPEC_AMENDMENT_REQUIRED                | NO       | spec body unchanged since deposit; no content amendment proposed |

**No halt triggered.**

---

## Phase D verdict

**UPGRADE_V1_0_PARTIAL_NUMERICAL** (spec §6 OUTCOME LADDER rung 2 of 4):

> Phases A + B + B.5 + C all pass structurally; Phase D.2 numerical
> cross-check unavailable (BLMP 2024 provides only structural
> monodromy data without numerical Stokes constants for the V_quad
> parameter point; explicit Φ_symp Jacobian factor requires a
> follow-up symbolic-computation session).

**M6.CC closure status:** STRUCTURAL (Phase B Φ_symp now constructible
via KNY 2017 §8.5.17, closing the long-standing R5 blocker from the
2026-05-02 partial session); NUMERICAL (Phase D.2 cross-check)
deferred to the follow-up session
`CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL` (recommended
P1 priority; estimated 4–8 hr agent runtime).

**G15 / G22 / op:cc-formal-borel status update:**

* G15 (Φ_symp residual on Okamoto §§Lax-pair) — **partial → mostly
  closed via KNY 2017 §8.5.17** (Φ_symp now structurally
  constructible; Jacobian numerical value is the open residual).
* G22 (V_quad → P_III(D_6) canonical-form normalization map at
  108-digit canonical-form precision NOT written out) — **partial**
  (structurally written out via M = Φ_symp ∘ Φ_shift ∘ Φ_resc;
  numerical evaluation deferred).
* op:cc-formal-borel residual — **partial** (closure-pending the
  Phase D.2 numerical cross-check).

**M9 gating impact:** With 058R UPGRADE_V1_0_PARTIAL_NUMERICAL,
M6.CC remains in PARTIAL state. M9 gating remains
{M4-with-formal-baseline-+-structural-roadmap, M6.CC-partial}; the
follow-up Phase-D-numerical session is the gating-clearing target.

---

## Phase D anomalies (also entered in `discrepancy_log.json`)

* **D1** [INFO] R1 (Okamoto-convention identification of CT v1.3 §3.5
  4-tuple) carry-forward open from 2026-05-02 partial session;
  058R does not modify CT v1.3 (out of scope).
* **D2** [INFO] CT v1.3 §3.5 4-tuple $(1/6, 0, 0, -1/2)$ does not
  satisfy Okamoto's $\alpha_{\infty}+\alpha_{0}+\beta_{\infty}+\beta_{0}=0$
  null-sum constraint (sums to $-1/3$); carry-forward from
  2026-05-02 partial session unchanged.
* **D3** [STRUCTURAL] Spec's "$W(D_{6})$" framing in Phase B.5 has
  no literature anchor; reconciled to $W((2A_{1})^{(1)})$ surface
  symmetry per Sakai 2001 / KNY 2017 §8.1.20. Cross-walk is
  inclusion, not quotient. Spec amendment recommendation in
  handoff §Recommended-next-step.
* **D4** [INFO] Okamoto 1987 does NOT contain the explicit 2x2
  Lax pair (anomaly emerged on reading; Okamoto 1987 §1 covers
  the Hamiltonian formulation, §2 the affine Weyl symmetry, §3
  τ-functions, §4 cylinder functions — no Lax pair). The Lax pair
  used in Phase B is from KNY 2017 §8.5.17 (slot 14, auxiliary).
  Spec C.1 use ("Okamoto 1987 §§Lax-pair input that requires the
  Okamoto §§Lax-pair input") is therefore re-anchored to
  KNY 2017 §8.5.17.

D3 and D4 together motivate **operator-side action item: spec
amendment v1.2** to update Phase B.5 framing and re-anchor the
Lax-pair source. See handoff §Recommended-next-step.
