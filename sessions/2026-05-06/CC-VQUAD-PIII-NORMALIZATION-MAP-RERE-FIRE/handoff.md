# Handoff — 058R-CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE

**Date:** 2026-05-06
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~150 minutes (single-shot 9-phase execution)
**Status:** COMPLETE (verdict UPGRADE_V1_0_PARTIAL_NUMERICAL)

---

## What was accomplished

Re-fired 058 (CC-VQUAD-PIII-NORMALIZATION-MAP) on top of bridge HEAD
`9d6e801` (post-057 landing) and executed the full 9-phase
canonical-form normalization map task. Constructed M = Φ_symp ∘
Φ_shift ∘ Φ_resc with Φ_resc PINNED at λ=1/3, Φ_shift PINNED MODULO
sign at t_0 = -4√3, and Φ_symp STRUCTURALLY CONSTRUCTIBLE via
KNY 2017 §8.5.17 (closing the long-standing R5 blocker from the
2026-05-02 partial session). All 4 verification phases pass
structurally (A_VERIFIED + B_VERIFIED_STRUCTURAL +
B5_VERIFIED_WITH_CAVEAT + C_LITERATURE_UNIFORM); numerical Phase D.2
cross-check |M^* C_V| =? |S_ζ_*^can| deferred to follow-up session
yielding **UPGRADE_V1_0_PARTIAL_NUMERICAL** verdict (spec §6 OUTCOME
LADDER rung 2 of 4). 058 halt deposit at original path remains
bit-identical (P11 read-only check PASS).

## Key numerical findings

- **β = 0** (Gevrey-1 logarithmic Borel branch) re-verified at the
  Birkhoff level via sympy in `phase_a_birkhoff_match.py`; matches
  H4 measurement to 107 dps (substrate). [Phase A]
- **|ζ_*| = 4/√3 = 2.30940107675850305803659512201...** Borel-plane
  partner-action distance, sympy-derived from characteristic
  equation 3C² - 4 = 0. [Phase A; matches T1P2B-A6 baseline at 30+ dps]
- **Φ_resc rescaling factor λ = 1/3** PINNED via reduction of
  `3C² - 4 = 0` to canonical `C² = 1`. [Phase B.1]
- **Φ_shift origin t_0 = -ζ_*/λ = -4√3 ≈ -6.92820323...** PINNED
  modulo a global sign convention. [Phase B.2]
- **Φ_symp STRUCTURALLY CONSTRUCTIBLE** via KNY 2017 §8.5.17
  eq. 8.237–8.239 (R5 closure event). Numerical Jacobian
  `|det J(Φ_symp)|` deferred (Phase D.2). [Phase B.3]
- **|C_V| = 8.127336795495072367...** at 107 dps (V_quad Stokes
  amplitude, H4 measurement, re-cited from 051). [Substrate]
- **Spec halts evaluated 8/8 — 0 triggered** (HALT_M6_STOKES_NUMERICAL_MISMATCH
  marked N/A because D.2 deferred). [halt_log.json]
- **Wrapper halts evaluated 7/7 — 0 triggered**. [halt_log.json]
- **AEAL claim count: 24** (6 substrate-gate + 18 NEW; floor was
  ≥16 NEW). [claims.jsonl]
- **STEP 4 M6.CC token sweep: PASS** (zero bare-M6 in NEW prose;
  only M6.CC + M6.H4 compounds appear).

## Judgment calls made

- **Phase E full pdflatex build deferred → outline-only TeX source.**
  Spec §6 explicitly marks Phase E "conditional, minimal outline" for
  the UPGRADE_V1_0_PARTIAL_NUMERICAL ladder rung. `cc_note_v1.tex`
  deposited as TeX source for Picture v19 inclusion; agent did NOT
  invoke pdflatex. (Rationale: full PDF build adds ~30 min agent
  time without changing the verdict.)
- **D2-NOTE v2.1 carry-forward citations for B-T 1933 and Wasow
  1965** rather than re-extracting verbatim from the PDFs. Per spec
  C.4 + C.5 directive ("carry-forward via D2-NOTE v2.1"), this is
  spec-mandated and not an autonomous decision; recording explicitly
  for transparency.
- **AEAL output_hash field for "process" claims** (e.g., 058R-Cprev1
  STEP 1 substrate inventory) bound to the prompt_spec_used.md SHA
  (`be3f8fe9...`) when no single deliverable file is the natural
  hash anchor. Alternative would have been omitting `output_hash`,
  but spec mandate "reproducible: true + output_hash: <sha256>"
  applies to all claims.
- **058R writes only to `sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE/`**
  (with `-RERE-FIRE` suffix) to preserve the canonical 058 halt
  deposit at the bare path.

## Anomalies and open questions

**THIS IS THE MOST IMPORTANT SECTION.** See
`discrepancy_log.json` for full detail; condensed list:

- **D1** [INFO]. R1 (Okamoto-convention identification of CT v1.3
  §3.5 four-tuple) carry-forward open from 2026-05-02 partial
  session; 058R does NOT modify CT v1.3 (out of scope).

- **D2** [INFO]. CT v1.3 §3.5 four-tuple
  $(α_∞, α_0, β_∞, β_0) = (1/6, 0, 0, -1/2)$ does not satisfy
  Okamoto's null-sum constraint
  $α_∞ + α_0 + β_∞ + β_0 = 0$ (sums to $-1/3$). Carry-forward
  from 2026-05-02 partial session unchanged. The follow-up
  Phase-D-Numerical session must reconcile this (e.g., via an
  additional shift in the (a_0, a_1, a_2) chart or via
  Okamoto §3 τ-function parametrisation).

- **D3** [STRUCTURAL — primary substantive finding]. Spec's
  "$W(D_6)$" framework for Phase B.5 has no literature anchor.
  BLMP 2024 + Sakai 2001 + KNY 2017 + Okamoto 1987 + NY 1998/2000
  all use: surface type $D_6^{(1)}$, symmetry type $(2A_1)^{(1)}$,
  Bäcklund group $W_a(B_2) = W_a(C_2)$. Sakai's $W((2A_1)^{(1)})$
  is the long-root index-2 subgroup of Okamoto's $W_a(B_2)$. The
  cross-walk is **inclusion** not quotient. **Recommends operator-side
  spec amendment v1.2.**

- **D4** [INFO]. Okamoto 1987 does NOT contain an explicit 2x2
  Lax pair (covers Hamiltonian / affine Weyl / τ-functions /
  cylinder functions in §§1–4, but no Lax pair). The Lax pair
  used in Phase B.3 is from KNY 2017 §8.5.17. Spec C.1 directive
  "Okamoto §§Lax-pair" is therefore re-anchored to KNY 2017
  §8.5.17. **Recommends operator-side spec amendment v1.2.**

- **D5** [INFO]. Φ_symp Jacobian numerical evaluation requires
  separate session (~4–8 h symbolic-computation cycle) to
  construct the explicit gauge transformation between V_quad's
  third-order scalar-OGF Lax representation and KNY's second-order
  scalar Lax form `L_1 y = 0` (eq. 8.239). 058R deferred this
  cleanly via UPGRADE_V1_0_PARTIAL_NUMERICAL verdict.

**Open questions for Claude (epistemic review side):**

1. Is the 058R **B5_VERIFIED_WITH_CAVEAT** verdict (Okamoto-Sakai
   inclusion cross-walk) acceptable for declaring G15 residual
   "MOSTLY CLOSED", or should a stricter long-root-subgroup-action
   compatibility check on the H4-measured Stokes data be added before
   M6.CC reaches UPGRADE_V1_0_FULL?

2. Should the operator-side spec amendment v1.2 (per D3 + D4) be
   triggered before firing the Phase-D-Numerical follow-up session,
   or can the Phase-D-Numerical session run on the existing v1.1
   spec body with the D3/D4 reconciliation noted in handoff?

3. In the Phase-D-Numerical follow-up, BLMP 2024 §4 connection-matrix
   formula (eq. 4.28) requires a specific KNY-side $(a_1, a_2)$
   parameter point. This depends on the R1 closure (D1). Should
   R1 be tackled in the same Phase-D-Numerical session or as a
   prior preflight?

## What would have been asked (if bidirectional)

- After Phase B.5 surfaced the spec/literature framing mismatch
  (W(D_6) vs W((2A_1)^(1)) ⊂ W_a(B_2)), the agent would have asked:
  **"Should I HALT here and request spec amendment v1.2, or proceed
  with B5_VERIFIED_WITH_CAVEAT and surface for review?"** Decision
  made autonomously: proceed with caveat verdict (since D3 is a
  notational not numerical issue, and the structural Bäcklund-symmetry
  chain is preserved under correct group-theoretic naming).

- After Phase B.3 confirmed KNY 2017 §8.5.17 closure of R5, the agent
  would have asked: **"Should the structural-only completion of
  Phase B trigger an immediate UPGRADE_V1_0_FULL verdict if the
  numerical D.2 step is independently believable, or strictly
  PARTIAL_NUMERICAL?"** Decision made autonomously: strict
  PARTIAL_NUMERICAL per spec §6 ("UPGRADE_V1_0_FULL requires
  Phase D.2 numerical cross-check at ≥5 digits").

- During Phase C, the agent would have asked: **"Should the verbatim
  ≤30-word quotes use mathematical-typeset macros (\$...\$) or stay
  in plaintext to match the spec convention?"** Decision made
  autonomously: $$ inline math used with sympy-style notation
  preserved (`e_1^2`, `\zeta_*`, etc.) for readability.

## Recommended next step

**P1 priority — fire follow-up relay
`CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL`** (working title).

**Scope.** Compute the numerical Phase D.2 cross-check at ≥5 digits:

$$ |M^{*} C_{V}| \;\overset{?}{=}\; |S_{\zeta_{*}}^{\mathrm{can}}|. $$

**Inputs.** This 058R bridge tree (`phase_b_canonical_map.md` Φ_symp
structural form; `phase_a_birkhoff_match.py` H4 substrate);
KNY 2017 §8.5.17 eq. 8.237–8.239 (Lax form `L_1 y = 0`);
BLMP 2024 §4 connection-matrix formula eq. 4.28; CT v1.3 §3.5
four-tuple (post-R1 closure).

**Estimated agent runtime.** 4–8 h (symbolic + numerical sympy/mpmath
work). If R1 (D1+D2 reconciliation) is tackled in the same session,
runtime extends to 6–10 h.

**Pre-conditions.** (a) Decide whether to fire spec amendment v1.2
(D3 + D4) before or after Phase-D-Numerical (operator-side decision,
not agent-decidable). (b) Decide whether R1 closure (D1+D2) is in
scope of Phase-D-Numerical or a prior preflight relay.

**P2 priority (parallelizable) — fire spec amendment v1.2 relay**
to update Phase B.5 framing (W(D_6) → W((2A_1)^(1)) ⊂ W_a(B_2)) and
re-anchor Phase B.3 Lax-pair source (Okamoto §§Lax-pair → KNY 2017
§8.5.17). Operator + Claude side activity (~10 min).

**P3 priority — defer Picture v19 update** until Phase-D-Numerical
lands and verdict reaches UPGRADE_V1_0_FULL. The current
`cc_note_v1.tex` outline is sufficient to record the structural M
construction as an interim deposit.

## Files committed

(See bridge tree
`sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE/`):

| file                                                         | size  | SHA256 prefix |
|--------------------------------------------------------------|-------|---------------|
| prompt_spec_used.md                                          | 52 K  | be3f8fe9      |
| phase_0_5_bibkey_preflight.md                                |       | 38a882a5      |
| phase_a_birkhoff_match.py                                    |       | 7b4dd763      |
| phase_a_birkhoff_match.log                                   |       | 67fdb960      |
| phase_a_birkhoff_match.md                                    |       | 413a3845      |
| phase_b_canonical_map.md                                     |       | f831f9bd      |
| phase_b5_affine_weyl_crosswalk.md                            |       | b9d4ffd2      |
| phase_c_literature_verification.md                           |       | f698415c      |
| phase_d_verdict.md                                           |       | 025e3672      |
| cc_note_v1.tex                                               |       | 9c1649dc      |
| claims.jsonl                                                 |       | (per-file)    |
| halt_log.json                                                |       | (per-file)    |
| discrepancy_log.json                                         |       | (per-file)    |
| unexpected_finds.json                                        |       | (per-file)    |
| handoff.md (this file)                                       |       | (per-file)    |

## AEAL claim count

**24 entries** written to `claims.jsonl` this session:
- 6 substrate-gate claims (058R-Cprev1..Cprev6) covering STEP 1
  inventory + P9/P10/P11 GATES + Phase 0.0 provenance + Phase 0.5
  bibkey preflight.
- 18 NEW computation claims (058R-C1..C18) covering baseline
  T1P2B-A1..A10 re-cite (C1) + Phase A re-derivation (C2-C3) +
  Phase B canonical-map construction (C4-C6) + Phase B.5 cross-walk
  (C7-C8) + Phase C literature anchoring (C9-C12) + Phase D verdict
  (C13-C15) + STEP 4 M6.CC token sweep (C16) + Phase E CC-NOTE outline
  (C17) + anomaly aggregation (C18).

**Floor satisfied:** spec STEP F floor "≥16 NEW + inherited" met
with 18 NEW claims.

---

## 058 → 058R re-fire commentary

058 originally fired on 2026-05-06 (bridge HEAD pre-`9d6e801`) and
halted at P7 GATE because 057 (CC-VQUAD-PIII-LITERATURE-PREFLIGHT)
had not landed at fire time — a fire-order race per
`058r-early-fire-decision-substrate-2026-05-06.md` and
`058-cc-vquad-piii-haltp7-2026-05-06.md`. The 058 halt deposit at
`sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP/` is preserved
bit-identical (P11 read-only check PASS).

058R fired on top of bridge `9d6e801` (post-057 landing) to the new
path `sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE/`
and successfully completed all 9 phases. The `-RERE-FIRE` suffix is
intentional (preserves the canonical 058 halt at the bare path);
operator may rename or merge after Phase-D-Numerical lands.

The single substantive structural finding from 058R (beyond the
expected M-construction): **the spec's "W(D_6)" framing is not
literature-anchored** (D3 anomaly above). This was reconciled to
W((2A_1)^(1)) ⊂ W_a(B_2) (Okamoto 1987 §2.1 + KNY 2017 §8.1.20)
without halting; the reconciliation is a notational not numerical
correction, and the structural Bäcklund-symmetry chain underlying
M's compatibility with the canonical-form is preserved.
