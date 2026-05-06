# CC-VQUAD-PIII-NORMALIZATION-MAP — Synthesizer-Drafted Prompt Spec

**Session:** `CC-VQUAD-PIII-NORMALIZATION-MAP-PROMPT-SPEC`
**Date deposited:** 2026-05-04 (JST)
**Source:** PRE-DRAFT operator chat 2026-05-04 (Q35 ruling
  2026-05-04 + R5-OKAMOTO-NUMDAM-RETRY `SCENARIO B` disposition
  + v1.16 picture absorption + H4_PASS_108_DIGITS verdict)
**Purpose:** AEAL-anchor the CC-VQUAD-PIII-NORMALIZATION-MAP (M6
  closure) prompt spec at deposit time per the QS-2 / QS-3 /
  T1P2-DEPOSIT pattern, **before** the relay agent fires.

> **Chronology note (AEAL-honest):** This spec deposit is
> **pre-fire** (in contrast to the post-hoc `T1-BIRKHOFF-PHASE2-
> LIFT-LOWER-PROMPT-SPEC` deposit). The relay agent has **not**
> yet fired the spec at the time of this deposit. The spec is
> being deposited so the synthesizer (Claude) can perform critical-
> path QA review **before** operator dispatches the relay-prompt
> body into a fresh Copilot CLI session. The intended firing order
> is: (i) deposit (this) → (ii) synthesizer QA → (iii) amendments
> if needed → (iv) operator dispatches → (v) execution session
> opens at `sessions/<fire-date>/CC-VQUAD-PIII-NORMALIZATION-MAP/`.

---

## Verbatim spec body (intended for relay-agent dispatch)

```
TASK: CC-VQUAD-PIII-NORMALIZATION-MAP
TASK CLASS: relay agent invocation (AEAL-compliant)
PARALLEL-SAFE WITH: any task NOT touching M6 closure path
                    (parallel-safe with T1 Phase 3 / Wasow §X.3
                    OCR / QS-PCF2-AFIT readback per Q35 ruling)
COMPUTE: medium (~2-4 hr agent runtime; literature reading +
         symbolic map construction + Stokes-data cross-check +
         verdict drafting)

═══════════════════════════════════════════════════════════════
§0 CONTEXT
═══════════════════════════════════════════════════════════════

SIARC program critical path: SIARC-MASTER-V0 announcement (M9)
gates on {M4 = Conjecture B4 at d ≥ 3 proof-grade,
M6 = canonical-form Stokes constant at 30+ digits}.

Post-v1.16 picture state (2026-05-04):
  - M2 ✅ FULLY DONE (D2-NOTE v2.1 UPGRADE_FULL on Zenodo
    2026-05-04 ~07:00 JST; concept DOI 10.5281/zenodo.19996689,
    version DOI 10.5281/zenodo.20015923)
  - M4 status: PARTIAL with formal-baseline + structural
    roadmap (T1 Phase 2 verdict UPGRADE_PARTIAL_FORMAL_LEVEL,
    bridge 37c939f; T1 Phase 3 deferred to Tier 2 / v1.16
    cycle, parallel-safe with M6 per Q35 ruling)
  - M6 status: literature now SCENARIO B (R5-OKAMOTO-NUMDAM-
    RETRY 2026-05-04, bridge 872652b; 2 of 3 R5 sources
    acquired with verbose strengthened verification — slot 07
    Okamoto FE 30 P_III SHA 65294fbc, slot 08 Barhoumi-Lisovyy-
    Miller-Prokhorov 2024 SHA 96c49cdd; slot 09 Conte-Musette
    SCENARIO_C-substituted by slot 06 Costin 2008 ch. 5 SHA
    436c6c11)
  - M9 gating remains {M4-with-formal-baseline-+-structural-
    roadmap, M6}; this task closes the M6 leg
  - H4_PASS_108_DIGITS landed 2026-05-02 (bridge session
    sessions/2026-05-02/CC-MEDIAN-RESURGENCE-EXECUTE/):
      C = 8.127336795495072367112578732... (>= 108 digits)
      β = 0 (logarithmic Borel singularity, to >= 107 digits)
      S_{ζ*} = 2 π i C ≈ 51.06556313995466... i
      ALL VALUES IN V_QUAD NATIVE COORDINATES
  - Q35 ruling 2026-05-04 (synthesizer): M6 fires next, parallel-
    safe with T1 Phase 3 / Wasow §X.3 OCR; Phase B.5 W cross-walk
    is mandatory pre-step before Phase B canonical-map construction

This task is M6 closure: construct the explicit normalization map

  M : V_quad coordinates  -->  P_III(D_6) canonical Hamiltonian
                                 / Riemann-Hilbert form

so that the H4 measurement (Stokes data in V_quad native form)
transforms covariantly under M to canonical-form Stokes data, and
cross-checks against the Barhoumi-Lisovyy-Miller-Prokhorov 2024
P_III(D_6) Stokes/monodromy tables.

The output closes three picture-v1.16 gaps simultaneously:

  - G15 (Φ_symp residual on Okamoto 1987 §§Lax-pair) — closed
    by Phase B + B.5 + C.1
  - G22 (V_quad → P_III(D_6) canonical-form normalization
    map at 108-digit canonical-form precision NOT written
    out) — closed by Phase B + Phase D numerical cross-check
  - op:cc-formal-borel residual (Prompt 013 halted on this
    gate; refire pending Q21 path) — closes via Phase D
    UPGRADE_V1_0_FULL or UPGRADE_V1_0_PARTIAL_NUMERICAL

If M6 lands UPGRADE_V1_0_FULL: M9 gating reduces from {M4-with-
formal-baseline-+-structural-roadmap, M6} to {M4-with-formal-
baseline-+-structural-roadmap only}. Once T1 Phase 3 lands, M9 → {}
and SIARC-MASTER-V0 becomes announceable.

If M6 lands UPGRADE_V1_0_PARTIAL_*: gates are advanced (G15
fully closed, G22 partial, op:cc-formal-borel partial); M9
gating remains {M4, M6-partial}; refire path identified for
the residual.

If M6 HALTS: surfaces a structural gap; M6 stays partial; H4
verdict remains in V_quad native form only.

═══════════════════════════════════════════════════════════════
§1 ANCHOR FILES (preconditions; verify all present)
═══════════════════════════════════════════════════════════════

LITERATURE PDFs (under
tex/submitted/control center/literature/g3b_2026-05-03/;
verify hashes against SHA256SUMS.txt):

  Slot 01 — Birkhoff 1930 (Acta Math 54)
    Use: formal-series existence + uniqueness at irregular
         singular points (§§2-3); foundation for Phase A's
         V_quad formal Birkhoff series re-derivation
    PDF: 01_birkhoff_1930_acta54.pdf
    SHA prefix: aeb5291e

  Slot 03 — Birkhoff-Trjitzinsky 1933 (Acta Math 60)
    Use: Borel-summability machinery (§§4-6), already cited
         by D2-NOTE v2.1; provides the Borel-plane existence
         framework underlying Phase A's β = 0 logarithmic
         singularity at ζ* = 4/√3
    PDF: 03_birkhoff_trjitzinsky_1933_acta60.pdf
    SHA prefix: dcd7e3c6

  Slot 04 — Wasow 1965 (Dover, "Asymptotic Expansions for
                          Ordinary Differential Equations")
    Use: sectorial asymptotic existence (§19, Theorem 19.1,
         eq. 19.3); already cited by D2-NOTE v2.1 + T1 Phase 1
         + Phase 2; supplies the sector-by-sector structure
         the canonical-form map must respect
    PDF: 04_wasow_1965_dover.pdf
    SHA prefix: f59d6835

  Slot 06 — Costin 2008 ch. 5 ("Asymptotics and Borel
                                summability", CRC Press
                                Monographs 141)
    Use: general Stokes-phenomenon framing for ODEs at
         irregular singular points of fractional rank;
         SCENARIO_C substitute for Conte-Musette ch. 7
         (per A-01 verdict + R5 disposition)
    PDF: 06_costin_2008_chap5.pdf
    SHA prefix: 436c6c11

  Slot 07 — Okamoto 1987 ("Studies on the Painlevé equations
                            IV. Third Painlevé equation
                            P_III", Funkcialaj Ekvacioj 30,
                            305-332)
    Use: PRIMARY Lax pair anchor — canonical Hamiltonian
         normalization of P_III; W(B_2) affine-Weyl framework;
         §1 (Painlevé system, P_{III'} ↔ P_III, auxiliary
         Hamiltonian) + §2 (Transformation group of P_{III'},
         root system, Weyl group W of B_2 root system,
         realization of s_0 as canonical transformation)
    PDF: 07_okamoto_1987_painleve_III_FE30.pdf
    SHA prefix: 65294fbc
    (acquired via Kobe University FE direct URL per
     R5-OKAMOTO-NUMDAM-RETRY 2026-05-04)

  Slot 08 — Barhoumi-Lisovyy-Miller-Prokhorov 2024
            ("Painlevé-III Monodromy Maps Under the
              D_6 → D_8 Confluence and Applications to the
              Large-Parameter Asymptotics of Rational
              Solutions", SIGMA 20 (2024), 019)
    Use: PRIMARY Stokes data anchor — explicit P_III(D_6)
         monodromy maps in canonical normalization; W(D_6)
         affine-Weyl framework (Sakai-classification convention)
    PDF: 08_barhoumi_lisovyy_miller_prokhorov_2024_pIII_D6.pdf
    SHA prefix: 96c49cdd

H4 EXECUTION SESSION (under sessions/2026-05-02/
CC-MEDIAN-RESURGENCE-EXECUTE/):

  - handoff.md — full Phase A/B/C/D execution report
  - verdict.md — H4_EXECUTED_PASS_108_DIGITS
  - claims.jsonl — AEAL-anchored numerical findings
  - median_resurgence.py — script (closed-form four-term
                          recurrence; mpmath dps=250; n=5000)
  - S_zeta_star_digits.txt — full 108-digit C value

CT v1.3 / CT v1.4 NARRATIVE-DRAFT REFERENCES:

  - CT v1.3 §3.5 (algebraic-identity-DONE Painlevé-class level
    framing of V_quad ↔ P_III(D_6)); foundation for Phase A's
    formal-series re-derivation
  - CT v1.4 narrative-draft (in-flight; cite-only at deposit
    time; do not modify)

D2-NOTE v2.1 (Zenodo 10.5281/zenodo.20015923; PDF SHA
a8b6026a3453f901a0da68c3849a9d7d828138ca4622b8a3686b68f01d5ef74e):
citable artifact for the universality-radius-of-Borel-singularity
result this canonical-form normalization extends.

A-01 verdict handoff (sessions/2026-05-03/T1-A01-NORMALIZATION-
RESOLUTION/handoff.md): mu-units consistency Wasow / Birkhoff /
B-T / Adams (no factor-of-2 ambiguity at normalization level);
relevant for Phase B map construction.

v1.16 strategic picture (tex/submitted/control center/
picture_revised_20260503.md; SHA prefix 87e97357): strategic
context for M6 closure → M9 gating reduction.

R5-OKAMOTO-NUMDAM-RETRY handoff (sessions/2026-05-04/
R5-OKAMOTO-NUMDAM-RETRY/handoff.md, bridge 872652b): SCENARIO B
disposition + B_2/D_6 framework cross-walk caveat that motivates
Phase B.5.

═══════════════════════════════════════════════════════════════
§2 PHASES
═══════════════════════════════════════════════════════════════

PHASE 0.0 — provenance write-out (mandatory pre-step)
  Write the relay-prompt body verbatim to:
    sessions/<fire-date>/CC-VQUAD-PIII-NORMALIZATION-MAP/
      prompt_spec_used.md
  This anchors the exact spec the relay agent saw at fire time
  for AEAL provenance. Should be byte-identical to the body of
  this spec (modulo line-ending conversion, allowed).

PHASE 0.5 — bibkey collision preflight
  If Phase E drafts a citable artifact with a bibliography file
  (annotated_bibliography.bib or similar), verify any new
  bibkeys do not collide with existing entries in
  tex/submitted/control center/d2_note_v2_1/annotated_
  bibliography.bib (already present from D2-NOTE v2.1) or
  sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/
  annotated_bibliography.bib. If collision detected, halt with
  HALT_M6_BIBKEY_COLLISION and surface to operator for renaming.

PHASE A — formal Birkhoff series matching at z = 0
  Goal: re-derive (or cite) V_quad's formal Birkhoff series at
  z = 0 from CT v1.3 §3.5 framing; confirm the leading
  characteristic exponent matches H4's measurement.

  Method:
    A.1 — Set up the V_quad recurrence b_n = 3n^2 + n + 1 and
          its associated formal series y(z) = sum a_n z^{n+ξ}
          per Birkhoff 1930 §2 Theorem I (formal-series
          existence) using mu-units consistent with A-01
          verdict
    A.2 — Identify the leading characteristic exponent ξ_0 by
          Newton-polygon analysis of the recurrence's
          generating differential operator
    A.3 — Cross-check ξ_0 against H4 verdict (verdict.md):
          β = 0 (logarithmic Borel singularity; the leading
          alien amplitude C corresponds to ξ_0 in canonical
          form via Stokes phenomenon)
    A.4 — Cite CT v1.3 §3.5 algebraic identity (V_quad ↔
          Painlevé-class level identification) and D2-NOTE
          v2.1 universality result for Borel-singularity
          radius

  Verdict signal:
    - A_VERIFIED: ξ_0 derived consistently with H4
      measurement; V_quad formal series structurally aligned
      with CT v1.3 §3.5 framing
    - A_DRIFT: discrepancy with H4 measurement OR with CT
      v1.3 §3.5 framing → HALT_M6_BIRKHOFF_SERIES_DRIFT

  Output: phase_a_birkhoff_match.md (≤ 4 pp) +
          phase_a_birkhoff_match.py if any symbolic re-
          derivation was performed

PHASE B — canonical-form normalization map construction
  Goal: derive the explicit map M : V_quad coordinates →
  P_III(D_6) canonical Hamiltonian / Riemann-Hilbert form.

  This is the central technical task of M6.

  Sub-steps:
    B.1 — From Okamoto 1987 §1 (Painlevé system), extract the
          canonical Hamiltonian H_III for P_III(D_6) and its
          coordinate variables (q, p, t per Okamoto's
          convention)
    B.2 — From CT v1.3 §3.5, extract the algebraic identity
          mapping V_quad's z-coordinate to Okamoto's
          t-coordinate (and analogous y → q, y' → p mappings
          if applicable)
    B.3 — Construct the explicit map M as a composition:
          - Φ_resc (rescaling, λ = 1/3 from prior G15
            partial-closure work)
          - Φ_shift (shift, prior G15 partial-closure work)
          - Φ_symp (symplectic transformation; the part
            that requires the Okamoto §§Lax-pair input;
            this is the genuinely new part)
    B.4 — Verify M is bijective on the relevant chart
          (V_quad's chart at z = 0 ↔ P_III(D_6)'s chart at
          t corresponding to z = 0); compute Jacobian on
          formal series
    B.5 — Verify M respects the formal Birkhoff series
          structure: M takes V_quad's a_n z^{n+ξ_0} formal
          series to a P_III(D_6) formal series in the
          canonical Birkhoff form per Okamoto 1987 §1

  Verdict signal:
    - B_VERIFIED: M constructed explicitly; bijective on
      relevant chart; Jacobian non-degenerate; formal-series
      transformation respects Birkhoff structure
    - B_INCOMPLETE: M cannot be constructed because of a
      fundamental structural obstruction (e.g., V_quad's
      recurrence does not lift to any P_III(D_6) Hamiltonian
      flow on the available charts) → HALT_M6_PHASE_B_
      CONSTRUCTION_INCOMPLETE
    - B_INCONSISTENT: M is constructed but fails internal
      consistency (transition functions don't compose
      correctly, Jacobian degenerate where it shouldn't be,
      formal-series transformation produces extraneous
      logarithms or pole orders) → HALT_M6_NORMALIZATION_
      INCONSISTENCY

  Output: phase_b_canonical_map.md (≤ 6 pp) +
          phase_b_canonical_map.py (sympy / mpmath
          implementation of M)

PHASE B.5 — B_2 ↔ D_6 affine-Weyl cross-walk (mandatory
            pre-step per Q35 ruling 2026-05-04)
  Goal: establish the explicit cross-walk between Okamoto
  1987's W(B_2) affine-Weyl framework and Barhoumi-Lisovyy-
  Miller-Prokhorov 2024's W(D_6) framework BEFORE Phase B's
  canonical map is finalized. Without B.5, Phase B's map
  could end up subtly inconsistent with the modern Sakai-
  classification convention used in Phase C.

  Sub-tasks:
    B.5.1 — Read Okamoto 1987 §2 (Transformation group of
            P_{III'}, root system) and identify the W(B_2)
            affine-Weyl generators (typically s_0, s_1, s_2 —
            three generators for affine B_2). Record:
              - Each generator's action on Okamoto's
                parameter space (typically α, β-parameters
                of P_{III'})
              - The Coxeter / Dynkin diagram embedding
              - Page anchor + verbatim definition (≤ 30
                words)
    B.5.2 — Read Barhoumi-Lisovyy-Miller-Prokhorov 2024
            §_W (the section establishing W(D_6) action on
            canonical normalization) and identify the
            W(D_6) affine-Weyl generators (typically seven
            generators for affine D_6). Record:
              - Each generator's action on the modern
                parameter space (typically θ_∞, θ_0,
                θ_t-parameters per Sakai 2001)
              - The Coxeter / Dynkin diagram embedding
              - Page anchor + verbatim definition (≤ 30
                words)
    B.5.3 — Establish the explicit homomorphism /
            quotient between the two affine-Weyl framings.
            The expected structure is:
              W(D_6) affine  -->  W(B_2) affine
            via the surface-type classification of Sakai
            2001 (Painlevé III sits on a D_6^{(1)} / D_4
            surface in the Sakai classification; Okamoto's
            W(B_2) framing is a quotient by the confluence
            directions D_6 → D_8 that Barhoumi-Lisovyy 2024
            uses). The agent verifies:
              - The surjective homomorphism's kernel is the
                expected confluence-direction subgroup (or
                surface this if not)
              - Okamoto's parameters embed into the
                modern parameter space as the expected
                quotient image
              - The canonical-form normalization map M
                (Phase B output) respects both structures:
                M conjugates W(B_2) action on V_quad to
                the appropriate quotient of W(D_6) action
                on canonical P_III(D_6)
    B.5.4 — If a discrepancy surfaces (e.g., the expected
            homomorphism doesn't hold OR Phase B's map M
            doesn't respect the W structures), halt with
            HALT_M6_AFFINE_WEYL_MISMATCH and surface the
            specific algebraic gap. Do NOT silently force
            the structures to match.

  Verdict signal:
    - B5_VERIFIED: cross-walk explicit; M respects both
      structures; W(B_2) action compatible with quotient
      W(D_6) action
    - B5_MISMATCH: cross-walk fails or M does not respect
      the structures → HALT_M6_AFFINE_WEYL_MISMATCH

  Output: phase_b5_affine_weyl_crosswalk.md (≤ 4 pp) +
          phase_b5_affine_weyl_crosswalk.py if any symbolic
          generator-action verification was performed

PHASE C — literature anchoring
  Goal: anchor every load-bearing step of Phases A + B + B.5
  in literature with verbatim quotes (≤ 30 words per quote
  per hygiene), theorem/equation numbers, and page anchors.

  Sub-steps:
    C.0 gate — verify all 6 anchor PDFs at expected paths +
              SHA verification against
              tex/submitted/control center/literature/
              g3b_2026-05-03/SHA256SUMS.txt
              (PASS 11/11 expected; halt with HALT_M6_
              LITERATURE_NOT_LANDED if any slot fails)

    C.1 — Okamoto 1987 §1 (Painlevé system, Lax pair)
          PRIMARY Lax pair anchor for Phase B.1 + Phase B.3
          Φ_symp construction. Extract:
            - Theorem/equation number for the canonical
              Hamiltonian H_III definition
            - Verbatim ≤ 30-word statement of the canonical
              form
            - Page anchor (FE 30, 1987, pp. 305-332; the
              Kobe-U LaTeX-source PDF has its own
              page numbering — record both)

    C.2 — Barhoumi-Lisovyy-Miller-Prokhorov 2024 §Stokes
          PRIMARY Stokes data anchor for Phase D numerical
          cross-check. Extract:
            - Theorem/equation number for the explicit
              P_III(D_6) Stokes constants (or monodromy
              data table)
            - Verbatim ≤ 30-word statement
            - Page anchor (SIGMA 20 (2024), 019; preprint
              page numbering also acceptable)
            - Numerical value(s) of canonical-form Stokes
              constants if provided

    C.3 — Costin 2008 ch. 5 (general Stokes-phenomenon
          framing)
          Backup anchor (substitutes Conte-Musette per
          A-01 verdict). Extract verbatim quote stating the
          general Stokes-phenomenon transformation rule for
          ODEs at irregular singular points of fractional
          rank; ≤ 30 words; theorem/equation number; page
          anchor.

    C.4 — Birkhoff-Trjitzinsky 1933 §§4-6 (Borel
          summability)
          Carry-forward anchor (already used by D2-NOTE
          v2.1). Cite as foundation for Phase A's Borel-
          plane existence; do NOT re-extract verbatim
          quotes already in D2-NOTE v2.1's bibliography
          (cite by D2-NOTE v2.1's existing extraction).
          One short anchor sentence + page reference is
          sufficient.

    C.5 — Wasow 1965 §19 (Theorem 19.1, eq. 19.3)
          Carry-forward anchor. Cite as foundation for
          Phase B's sectorial structure; do NOT re-extract
          verbatim quotes already in D2-NOTE v2.1. One
          short anchor sentence + page reference.

  Verdict signal:
    - C_LITERATURE_UNIFORM: all 5 anchors uniform with
      Phases A + B + B.5; map M is well-anchored
    - C_LITERATURE_DISAGREES_AT_<source>: specific source
      contradicts Phase A/B/B.5 derivation OR contradicts
      H4 measurement → HALT_M6_LITERATURE_DISAGREES_WITH_H4
      (if H4 disagreement) OR surface for verdict-level
      review (if Phase A/B/B.5 disagreement)
    - C_LITERATURE_BOUNDED: anchor coverage is partial; M
      is only literature-anchored on a sub-chart of its
      domain → UPGRADE_V1_0_PARTIAL_LITERATURE in Phase D

  Output: phase_c_literature_verification.md (≤ 8 pp;
          one sub-section per C.1–C.5)

PHASE D — verdict aggregation + numerical cross-check
  Goal: combine Phase A + B + B.5 + C signals; perform the
  final numerical cross-check between M(H4) and Barhoumi-
  Lisovyy 2024 canonical-form Stokes constants.

  Sub-steps:
    D.1 — Aggregate signals:
          - A_VERIFIED + B_VERIFIED + B5_VERIFIED + C_
            LITERATURE_UNIFORM → candidate UPGRADE_V1_0_FULL
          - any phase failed structurally → HALT_M6_*
          - Phase verified but partial → candidate
            UPGRADE_V1_0_PARTIAL_*

    D.2 — Numerical cross-check (only if aggregate is
          UPGRADE_V1_0_FULL or UPGRADE_V1_0_PARTIAL):
          Apply the Phase B map M to the H4 measurement
          (C = 8.127336795... in V_quad native, dps=250)
          and obtain a canonical-form Stokes constant
          C_canonical = M*(C). Cross-check against Barhoumi-
          Lisovyy 2024's canonical-form value:
            (i) If Barhoumi-Lisovyy 2024 provides a numerical
                value for the relevant canonical-form Stokes
                constant: agreement to ≥ N digits where N is
                the precision they provide (typically 5-30
                digits, possibly more for symbolic-with-
                numerical-ZeroResidual claims)
            (ii) If Barhoumi-Lisovyy 2024 provides only an
                 algebraic-symbolic expression: numerically
                 evaluate that expression at the appropriate
                 parameter values and compare to C_canonical
                 at the precision available (expect at least
                 5 digits of agreement)
            (iii) If Barhoumi-Lisovyy 2024 provides only a
                  monodromy-matrix structure (no numerical
                  value or symbolic expression for the
                  specific parameter values): cross-check is
                  STRUCTURAL ONLY (verify the matrix structure
                  matches; numerical D.2 not applicable);
                  outcome is UPGRADE_V1_0_PARTIAL_NUMERICAL
                  (full structural match but numerical cross-
                  check unavailable)

          If numerical agreement is achieved: outcome
          UPGRADE_V1_0_FULL or UPGRADE_V1_0_PARTIAL_LITERATURE
          (depending on Phase C aggregate)

          If numerical disagreement at the available precision
          floor: HALT_M6_STOKES_NUMERICAL_MISMATCH (specific
          discrepancy investigated by re-checking Phase B map
          composition Φ_resc ∘ Φ_shift ∘ Φ_symp; possibly
          re-check Phase B.5 W cross-walk)

    D.3 — Halt aggregation:
          - HALT_M6_LITERATURE_NOT_LANDED (Phase C.0 gate)
          - HALT_M6_BIRKHOFF_SERIES_DRIFT (Phase A)
          - HALT_M6_PHASE_B_CONSTRUCTION_INCOMPLETE
            (Phase B fundamental obstruction)
          - HALT_M6_NORMALIZATION_INCONSISTENCY
            (Phase B internal inconsistency)
          - HALT_M6_AFFINE_WEYL_MISMATCH (Phase B.5)
          - HALT_M6_LITERATURE_DISAGREES_WITH_H4 (Phase C)
          - HALT_M6_STOKES_NUMERICAL_MISMATCH (Phase D.2)
          - HALT_M6_BIBKEY_COLLISION (Phase 0.5)

  Output: phase_d_verdict.md

PHASE E — D2-NOTE-style upgrade artifact (CC-NOTE v1.0,
          conditional on UPGRADE_V1_0_FULL or UPGRADE_V1_0_
          PARTIAL with acceptable residuals)
  Goal: draft a citable upgrade note that:
    E.1 — States the explicit V_quad → P_III(D_6) canonical-
          form normalization map M
    E.2 — Cites Phase A formal Birkhoff series + Phase B
          canonical map construction + Phase B.5 W cross-walk
    E.3 — Cites Phase C literature anchors (Okamoto 1987 + 
          Barhoumi-Lisovyy 2024 + Costin 2008 ch. 5 +
          Birkhoff-Trjitzinsky 1933 §§4-6 + Wasow 1965 §19)
    E.4 — Cites D2-NOTE v2.1 (Zenodo 10.5281/zenodo.20015923)
          and H4_PASS_108_DIGITS verdict (bridge session
          sessions/2026-05-02/CC-MEDIAN-RESURGENCE-EXECUTE/)

  Build clean with pdflatex passes 1, 2, 3 if drafted.

  Output: cc_note_v1.tex + cc_note_v1.pdf (if drafted)

  Note: a v1 draft can be 5-7 pp; full ~10-15 pp expansion
  is a separate task post-deposit.

PHASE F — handoff + AEAL claims
  Write handoff.md (full session report):
    - Verdict (Phase D output)
    - Phase A + B + B.5 + C summary tables
    - Phase D numerical cross-check details (specific digit
      counts for the numerical agreement / disagreement)
    - Anomalies noted
    - SHA-256 of all build artifacts
    - Bridge commit hash
    - Next-task recommendations

  Append AEAL claims to claims.jsonl (do NOT overwrite):
    - 1+ Phase A entries (formal Birkhoff series + leading
      exponent ξ_0 verification against H4)
    - 4+ Phase B entries (canonical map construction sub-
      steps B.1, B.2, B.3, B.4 / B.5 — note that B.4/B.5
      bookkeeping is intra-Phase-B; the four entries cover
      Φ_resc + Φ_shift + Φ_symp + Jacobian non-degeneracy)
    - 4+ Phase B.5 entries (W cross-walk B.5.1, B.5.2,
      B.5.3, and homomorphism verification)
    - 5+ Phase C entries (one verbatim anchor per source
      C.1, C.2, C.3, C.4, C.5)
    - 1+ Phase D verdict entry (numerical cross-check
      result with explicit digit count)
    - 1+ Phase E artifact provenance entry (if E ran)

  Total: ≥ 16 entries. Aim for higher if any sub-phase
  produces additional independently-verifiable findings.

  git commit + push.

═══════════════════════════════════════════════════════════════
§3 AEAL CLAIMS MINIMUM
═══════════════════════════════════════════════════════════════

Recommend ≥ 16 claims.jsonl entries as detailed in Phase F:
  - 1+ Phase A (formal Birkhoff series + ξ_0 verification)
  - 4+ Phase B (Φ_resc, Φ_shift, Φ_symp, Jacobian)
  - 4+ Phase B.5 (B.5.1, B.5.2, B.5.3, homomorphism check)
  - 5+ Phase C (one per literature source C.1–C.5)
  - 1+ Phase D verdict + numerical cross-check
  - 1+ Phase E artifact provenance (if E ran)

This is +2 over the prior baseline (T1 Phase 2's ≥ 14)
specifically to cover the new B.5 sub-tasks per Q35 ruling.

═══════════════════════════════════════════════════════════════
§4 HALT CONDITIONS
═══════════════════════════════════════════════════════════════

HALT_M6_LITERATURE_NOT_LANDED — any of the 6 anchor PDFs
  (slots 01/03/04/06/07/08) missing from
  tex/submitted/control center/literature/g3b_2026-05-03/
  OR fails SHA verification against SHA256SUMS.txt.
  Operator confirms acquisition workflow.

HALT_M6_AFFINE_WEYL_MISMATCH — Phase B.5 surfaces a genuine
  algebraic mismatch between W(B_2) (Okamoto 1987) and W(D_6)
  (Barhoumi-Lisovyy 2024) that cannot be reconciled by the
  expected Sakai-classification quotient homomorphism. Surface
  the specific algebraic gap. Do NOT silently force the
  structures to match.

HALT_M6_BIRKHOFF_SERIES_DRIFT — Phase A's formal Birkhoff
  series at z = 0 doesn't match V_quad's known structure from
  CT v1.3 §3.5 OR the leading characteristic exponent ξ_0
  doesn't match H4's measurement (β = 0, C = 8.127336795...).
  Investigate: possibly a normalization-convention mismatch
  between CT v1.3 and Birkhoff 1930 §2 Theorem I; check A-01
  verdict mu-units consistency.

HALT_M6_PHASE_B_CONSTRUCTION_INCOMPLETE — Phase B cannot
  construct the map M because of a fundamental structural
  obstruction (e.g., V_quad's recurrence does not lift to any
  P_III(D_6) Hamiltonian flow on the available charts; or
  Φ_symp requires an Okamoto-§§Lax-pair input the agent
  cannot extract from slot 07). Surface specific obstruction;
  may require operator-side reading of Sakai 2001 / additional
  literature.

HALT_M6_NORMALIZATION_INCONSISTENCY — Phase B's map M is
  constructed but fails internal consistency: transition
  functions don't compose correctly, Jacobian degenerate
  where it shouldn't be, formal-series transformation
  produces extraneous logarithms or pole orders.

HALT_M6_LITERATURE_DISAGREES_WITH_H4 — Phase C reading of
  Barhoumi-Lisovyy 2024 §Stokes (C.2) or Okamoto 1987
  §Painlevé-system (C.1) contradicts H4's measurement
  (β = 0 logarithmic; C = 8.127336795...). Surface specific
  contradiction.

HALT_M6_STOKES_NUMERICAL_MISMATCH — Phase D.2 numerical
  cross-check between M(H4) = C_canonical and Barhoumi-
  Lisovyy 2024's canonical-form value disagrees at the
  available precision floor. Re-check Phase B map composition
  Φ_resc ∘ Φ_shift ∘ Φ_symp; re-check Phase B.5 W cross-walk
  (the homomorphism may be at the wrong scale).

HALT_M6_BIBKEY_COLLISION — Phase 0.5 detects bibkey
  collision in any new bibliography entry. Surface to
  operator for renaming.

═══════════════════════════════════════════════════════════════
§5 FORBIDDEN-VERB HYGIENE
═══════════════════════════════════════════════════════════════

Per CT v1.4 / Q20a / T1 Phase 2 hygiene rules:
  - "trivial" / "trivially" / "obvious" / "clearly" — forbidden
    in artifact LaTeX (Phase E output); replace with explicit
    derivation or cite location
  - "easily seen to" — forbidden; replace with explicit
    derivation
  - "Wasow §X.3" — DEPRECATED per Q20a anomaly 4; use
    "Wasow §19 (Theorem 19.1, eq. 19.3)" or
    "Wasow §X.3 (Theorem 11.1)" depending on which result
    is cited (this M6 task primarily cites §19 by carry-
    forward from D2-NOTE v2.1)
  - "We claim" / "It is clear that" — forbidden; replace
    with explicit derivation or citation
  - "shows" / "confirms" / "proves" — forbidden in
    prediction-or-conjecture context (per T1 Phase 1 hygiene
    rule): a numerical match cross-check is "is consistent
    with" / "agrees to N digits with", NOT "confirms" /
    "proves"
  - Verbatim quotes from literature: ≤ 30 words per quote
    (per all prior cycles)

═══════════════════════════════════════════════════════════════
§6 OUTCOME LADDER
═══════════════════════════════════════════════════════════════

UPGRADE_V1_0_FULL — Phases A + B + B.5 + C + D all pass with
  full literature anchoring + numerical cross-check at the
  available precision floor. M6 ✅ closes; G15 fully closed;
  G22 fully closed; op:cc-formal-borel residual fully
  resolved. M9 gating reduces from {M4-with-formal-baseline-
  +-structural-roadmap, M6} to {M4-only}. Best-case outcome.

UPGRADE_V1_0_PARTIAL_NUMERICAL — Phases A + B + B.5 + C all
  pass structurally; Phase D.2 numerical cross-check
  unavailable (Barhoumi-Lisovyy 2024 provides only structural
  monodromy data without numerical Stokes constants for the
  specific parameter values). G15 fully closed; G22 partial
  (structurally closed, numerical cross-check not surfaced);
  op:cc-formal-borel partial. Refire path: extend Barhoumi-
  Lisovyy 2024 reading or acquire additional Stokes-data
  literature.

UPGRADE_V1_0_PARTIAL_LITERATURE — Phases A + B + B.5 pass;
  Phase C aggregate is C_LITERATURE_BOUNDED (anchor coverage
  partial: M is only literature-anchored on a sub-chart of
  its domain). G15 partial; G22 partial. Refire path: acquire
  Conte-Musette ch. 7 (currently SCENARIO_C-substituted by
  Costin) or extend Costin ch. 5 reading.

UPGRADE_V1_0_PARTIAL_PAGECOUNT — Phase E build at non-
  canonical page range (e.g., 4 pp instead of 5-7).
  Operator decides whether to deposit.

HALT_M6_* — see §4. Each halt produces a specific halt log
  + actionable next step.

═══════════════════════════════════════════════════════════════
§7 STANDING FINAL STEP
═══════════════════════════════════════════════════════════════

Per SIARC standing rule B5, output to chat (mandatory):

  BRIDGE: https://github.com/papanokechi/siarc-relay-bridge/
          tree/main/sessions/<fire-date>/CC-VQUAD-PIII-
          NORMALIZATION-MAP/

  CLAUDE_FETCH: https://raw.githubusercontent.com/papanokechi/
                siarc-relay-bridge/main/sessions/<fire-date>/
                CC-VQUAD-PIII-NORMALIZATION-MAP/handoff.md

  VERDICT: <one of UPGRADE_V1_0_FULL /
           UPGRADE_V1_0_PARTIAL_NUMERICAL /
           UPGRADE_V1_0_PARTIAL_LITERATURE /
           UPGRADE_V1_0_PARTIAL_PAGECOUNT /
           HALT_M6_LITERATURE_NOT_LANDED /
           HALT_M6_AFFINE_WEYL_MISMATCH /
           HALT_M6_BIRKHOFF_SERIES_DRIFT /
           HALT_M6_PHASE_B_CONSTRUCTION_INCOMPLETE /
           HALT_M6_NORMALIZATION_INCONSISTENCY /
           HALT_M6_LITERATURE_DISAGREES_WITH_H4 /
           HALT_M6_STOKES_NUMERICAL_MISMATCH /
           HALT_M6_BIBKEY_COLLISION>

  ANOMALIES: <numbered list if any>

  STRATEGIC_IMPLICATION: <verdict's effect on M9 gating,
                          G15 / G22 / op:cc-formal-borel
                          status, and SIARC-MASTER-V0
                          announce-readiness given current
                          M4 status>

  NUMERICAL_CROSS_CHECK_DIGITS: <if Phase D.2 ran, the
                                 explicit digit count of
                                 agreement between M(H4)
                                 and Barhoumi-Lisovyy 2024
                                 canonical-form Stokes
                                 value; otherwise N/A>

═══════════════════════════════════════════════════════════════
§8 OUT OF SCOPE
═══════════════════════════════════════════════════════════════

  - T1 Phase 3 (parallel-safe per Q35 ruling but separate
    task; closes M4-partial → M4-full; does NOT block M6
    deposit)
  - Modifying CT v1.3 / CT v1.4 / D2-NOTE v2.1 / PCF-1 v1.3 /
    PCF-2 v1.3 / umbrella v2.0 — read-only at this stage;
    M6's CC-NOTE v1.0 (Phase E) is a NEW citable artifact,
    not a modification of any existing artifact
  - Submitting CC-NOTE v1.0 (or any artifact) to arXiv,
    Zenodo, or any journal portal (per Rule 2; per
    SUBMISSION_LOG protocol; submission is a separate
    operator-side task post-deposit)
  - Generating any artifact requiring API key input (per
    Rule 1)
  - Conte-Musette ch. 7 acquisition (SCENARIO_C-accepted;
    substituted by Costin 2008 ch. 5 already in slot 06)
  - Adams 1928 acquisition (out of scope per A-01 verdict +
    R5 disposition)
  - Wasow §X.3 OCR (separate task; gated to T1 Phase 3 if
    Outcome A of QS-PCF2-AFIT)
  - PSLQ closed-form recognition of C_canonical (separate
    task CC-MEDIAN-RESURGENCE-PSLQ; gated on UPGRADE_V1_0_
    FULL outcome here)
  - Tier-2 deferred arbitrations (Q-CLAUDE-30-31, G17, Q21,
    Q22, Q23, Q24) — defer to v1.17 cycle
  - Speculating beyond what the literature anchors + H4
    measurement + CT v1.3 §3.5 framing explicitly support
```

---

## Synthesizer notes (Note 1–7)

Per the deposit-task spec §2.1 pattern, the synthesizer chat
ordinarily appends "Note 1–N" framing the spec. Notes 1–7
covering this M6 spec:

- **Note 1 (M9 critical-path framing):** captured in §0 CONTEXT.
  The post-v1.16 picture frames M9 gating as {M4-with-formal-
  baseline-+-structural-roadmap, M6}; this task closes the M6 leg.
  T1 Phase 3 closes the M4 leg in parallel per Q35 ruling.

- **Note 2 (literature-PDF SHA hashes + R5 SCENARIO B
  disposition):** captured in §1 ANCHOR FILES. All 6 anchor PDFs
  verified; SCENARIO B confirmed (slot 09 substituted by slot 06
  per A-01 verdict).

- **Note 3 (AEAL claims minimum):** captured in §3. Set to
  ≥ 16 (= 14 prior T1-Phase-2 baseline + 2 new B.5 sub-tasks).

- **Note 4 (Phase B.5 mandatory-pre-step):** captured in §2 Phase
  B.5 + §4 HALT_M6_AFFINE_WEYL_MISMATCH. The R5-OKAMOTO-NUMDAM-
  RETRY agent flagged the W(B_2) ↔ W(D_6) cross-walk as the
  largest blind-spot risk; B.5 makes it an explicit named phase
  rather than a discovered-mid-flight surprise.

- **Note 5 (forbidden-verb hygiene):** captured in §5. Carries
  forward all CT v1.4 / Q20a / T1 Phase 2 hygiene rules. Adds
  the "shows / confirms / proves in prediction-or-conjecture
  context" rule from T1 Phase 1 dossier.

- **Note 6 (numerical cross-check digit-floor framing):** captured
  in §2 Phase D.2 + §7 STANDING FINAL STEP NUMERICAL_CROSS_CHECK_
  DIGITS field. The H4 measurement is at 108 digits; Barhoumi-
  Lisovyy 2024 typically provides 5-30 digits or symbolic
  expressions; success threshold floats to "agreement at the
  available precision floor" rather than an absolute digit count
  (avoids producing HALT_M6_STOKES_NUMERICAL_MISMATCH spuriously
  when the literature value is only known to N < 30 digits).

- **Note 7 (out-of-scope, Tier-2 arbitration deferral):** captured
  in §8.

So Note 1–7 are structurally inlined into the spec body itself;
no separate notes-document is required for the relay-agent fire.

---

## QA review checklist for synthesizer

Before operator dispatches the relay-prompt body, the synthesizer
should verify:

- [ ] §§0–8 all present, in order, with the exact section markers
- [ ] §0 CONTEXT correctly frames M6 as {M4, M6} → {M4} M9-gating
      reduction (consistent with v1.16 picture state)
- [ ] §1 ANCHOR FILES lists all 6 anchor PDFs with correct SHA
      prefixes and correct SHA256SUMS.txt expected entries
- [ ] §2 Phase 0.0 + Phase 0.5 are pre-step gates, not main work
- [ ] §2 Phases A, B, B.5, C, D, E, F are all explicit with
      sub-steps and verdict signals
- [ ] §2 Phase B.5 sub-tasks B.5.1, B.5.2, B.5.3, B.5.4 are
      explicit and complete
- [ ] §2 Phase D.2 numerical cross-check has a "precision-floor
      floats" framing (so HALT_M6_STOKES_NUMERICAL_MISMATCH
      doesn't trigger spuriously when literature precision < 30
      digits)
- [ ] §3 AEAL minimum ≥ 16 entries with explicit Phase
      breakdown
- [ ] §4 HALT CONDITIONS has all 8 specific halt codes (operator's
      6 + 2 added: HALT_M6_PHASE_B_CONSTRUCTION_INCOMPLETE +
      HALT_M6_STOKES_NUMERICAL_MISMATCH); each is actionable
- [ ] §5 hygiene rules consistent with prior cycles (CT v1.4 /
      Q20a / T1 Phase 2 / T1 Phase 1 dossier)
- [ ] §6 OUTCOME LADDER has 4 UPGRADE rungs + reference to §4
      HALTS
- [ ] §7 STANDING FINAL STEP includes BRIDGE + CLAUDE_FETCH +
      VERDICT + ANOMALIES + STRATEGIC_IMPLICATION + new
      NUMERICAL_CROSS_CHECK_DIGITS field
- [ ] §8 OUT OF SCOPE explicitly excludes T1 Phase 3 (parallel-
      safe per Q35), all artifact modifications, all submission
      portals, all Tier-2 arbitrations
- [ ] No prediction-context "shows / confirms / proves" leaks
      through the spec body (✓ checked at draft time)

If any checklist item fails: synthesizer surfaces the specific
gap; agent re-drafts; deposit gets a v1.1 amendment block.

---

## Bridge anchors

- **Spec-deposit session (this):**
  `sessions/2026-05-04/CC-VQUAD-PIII-NORMALIZATION-MAP-PROMPT-SPEC/`
- **Execution session (TO BE OPENED at fire time):**
  `sessions/<fire-date>/CC-VQUAD-PIII-NORMALIZATION-MAP/`
- **Deposit pattern precedents (read for context):**
  - QS-2: `sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/`
    (75 KB synthesizer-drafted spec; cited Note 1–N pattern)
  - T1P2-DEPOSIT: `sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-
    LOWER-PROMPT-SPEC/` (22 KB spec; same QS-3 pattern; verdict
    UPGRADE_PARTIAL_FORMAL_LEVEL landed AFTER deposit was post-
    hoc-anchored)
- **Anchor execution sessions:**
  - H4: `sessions/2026-05-02/CC-MEDIAN-RESURGENCE-EXECUTE/`
    (verdict H4_EXECUTED_PASS_108_DIGITS)
  - A-01: `sessions/2026-05-03/T1-A01-NORMALIZATION-RESOLUTION/`
    (verdict A01_WASOW_READING_CONFIRMED)
  - R5-NUMDAM-RETRY: `sessions/2026-05-04/R5-OKAMOTO-NUMDAM-RETRY/`
    (outcome OUTCOME_R5RT_NUMDAM_ACQUIRED; SCENARIO B)

---

## Amendment block v1.1 — synthesizer QA absorption (2026-05-04 ~16:55 JST)

This amendment block records the synthesizer's pre-fire QA pass on the
verbatim spec body above (deposited 2026-05-04 ~07:00 JST). The QA
identified five localized patches needed to absorb the 033
SIARC-PRIMARY-W-HOMOMORPHISM-DERIVATION verdict (bridge `a9d34fd`)
which landed AFTER this spec was deposited but BEFORE the relay agent
fires it. Per the deposit-pattern at the head of this file (L876), this
amendment block is the documented mechanism for spec evolution between
deposit and fire — the amendments here are authoritative for the
relay-agent dispatch.

The verbatim spec body above is the v1.0 deposit. Amendments below are
v1.1. The relay agent dispatched at fire time should treat the v1.0
body AS AMENDED BY v1.1 below as the authoritative spec.

### Amendment v1.1.A — §0 CONTEXT additive bullet

After the L70 Q35-ruling bullet, insert:

> - 033 SIARC-PRIMARY-W-HOMOMORPHISM-DERIVATION verdict 2026-05-04
>   (bridge `a9d34fd`): Phase B.5 W cross-walk theorem-grade pre-closed
>   at INDEX-2 level; the agent cites this verdict rather than
>   re-deriving. Specifically: φ : W^aff(B_2) ↪ Aut(D_6^{(1)}) ⋉
>   W((2A_1)^{(1)}) is sympy-verified injective with image of index 2;
>   cokernel Z/2 generated by Bäcklund involution
>   π : (v_1, v_2) ↦ (−1 − v_1, v_2). Strict-isomorphism upgrade
>   pending 036 SIARC-OKAMOTO-1987-SEC3-SCAN.

### Amendment v1.1.B — §2 Phase B.5 substantive rewrite

The deposited B.5.3 + B.5.4 sub-tasks (L349–386) contain three
errors identified by the QA pass:

1. **L352 direction reversed.** Spec writes
   `W(D_6) affine → W(B_2) affine`. Reality (033): the map runs the
   other way — `W^aff(B_2) → Aut(D_6^{(1)}) ⋉ W((2A_1)^{(1)})`, and
   it is **injective** (kernel = {e}), not surjective with
   confluence-subgroup kernel.
2. **L352 target factor wrong.** Spec writes `W(B_2)` (finite);
   Okamoto §2.1 explicitly states **W^aff(B_2)** (affine). The image
   factor on the codomain side is **W((2A_1)^{(1)})**, not W(D_6).
3. **L354–358 Sakai-confluence narrative incorrect.** That was the
   synthesizer's *expected* picture; the actual cokernel is Z/2
   generated by π, which is a Bäcklund involution, not a confluence
   direction.

**B.5.1 + B.5.2 stay** (still useful as agent-side readback
verification of Okamoto §2 + Barhoumi-Lisovyy 2024 §_W generators).

**B.5.3 is REPLACED by B.5.3' (cite-and-verify):**

> B.5.3' — Cite-and-verify (replaces B.5.3 derivation work):
>   - Cite 033 SIARC-PRIMARY-W-HOMOMORPHISM-DERIVATION verdict
>     (bridge `a9d34fd`, session
>     `sessions/2026-05-04/SIARC-PRIMARY-W-HOMOMORPHISM-DERIVATION/`)
>     for the explicit homomorphism
>     φ : W^aff(B_2) ↪ Aut(D_6^{(1)}) ⋉ W((2A_1)^{(1)}).
>   - Re-run `verify_homomorphism.py` from 033's session locally to
>     confirm sympy reproduction of the 6 W^aff(B_2) defining
>     relations (regression check, not new derivation).
>   - Verify Phase B's canonical map M is consistent with φ's
>     injection direction (V_quad coords carry W^aff(B_2) action;
>     canonical P_III(D_6) form carries the larger Aut(D_6^{(1)}) ⋉
>     W((2A_1)^{(1)}) action; M intertwines them via φ).
>   - Record the INDEX-2 qualifier: M is correct up to the Bäcklund
>     involution π; π is a Sakai-side symmetry not seen by V_quad
>     coordinates.

**B.5.4 is REPLACED by B.5.4' (halt guard, downgraded from primary
halt path):**

> B.5.4' — HALT_M6_AFFINE_WEYL_MISMATCH retained as a *guard against
>   spec-execution drift* — i.e., if the local re-run of
>   `verify_homomorphism.py` disagrees with 033's recorded sympy
>   output, or if Phase B's M demonstrably fails to intertwine the
>   two actions, halt. **Expected to never fire post-033.**

**Replacement diagram for L350–358 (the wrong-direction L352):**

> Expected structure (post-033):
>
>     φ : W^aff(B_2)   ↪   Aut(D_6^{(1)}) ⋉ W((2A_1)^{(1)})
>          (Okamoto)         (Sakai / Barhoumi-Lisovyy 2024)
>
> with ker(φ) = {e}, [image : codomain] = 2, cokernel
> Z/2 = ⟨π⟩ where π : (v_1, v_2) ↦ (−1 − v_1, v_2) is the Bäcklund
> involution.
>
> Phase B's canonical map M intertwines:
>     M ∘ ρ_V = ρ_canonical ∘ φ ∘ (M restricted)
> for ρ_V the W^aff(B_2) action on V_quad and ρ_canonical the
> W^aff(D_6) action on canonical form.

### Amendment v1.1.C — §3 AEAL ≥ 16 floor (recompute, keep at ≥ 16)

With B.5.3 + B.5.4 collapsing from "4+ derivation entries" to "2+
readback entries" (B.5.1, B.5.2 only), the floor mechanically drops
to ≥ 14. **Replace L590** with:

> - 4+ Phase B.5 (B.5.1 readback, B.5.2 readback,
>   **B.5.3' citation provenance of 033 verdict + bridge SHA
>   `a9d34fd`**, **B.5.3' local sympy regression re-run of
>   `verify_homomorphism.py`**)

This keeps the floor at ≥ 16 and gives the AEAL log the
citation-provenance and reproducibility entries that were missing.

### Amendment v1.1.D — §4 HALT_M6_AFFINE_WEYL_MISMATCH note

L608–613 stays. **Append:**

> *Note (post-033): the underlying homomorphism is sympy-verified
> pre-fire at INDEX-2. This halt is retained as a regression guard;
> it should not fire under normal execution. If it does fire, the
> immediate diagnostic is `diff` of local `verify_homomorphism.py`
> output against 033's recorded sympy trace.*

### Amendment v1.1.E — §7 STANDING FINAL STEP STRATEGIC_IMPLICATION

Append to L744–748 STRATEGIC_IMPLICATION clause:

> ...and the INDEX-2 vs strict-isomorphism status of the
> Okamoto-Sakai W cross-walk in light of 036
> SIARC-OKAMOTO-1987-SEC3-SCAN outcome (when fired). If 036 returns
> UPGRADE_..._STRICT_ISOMORPHISM, M6's INDEX-2 qualifier on Phase
> B.5 promotes; if CONFIRM_..._INDEX2_FINAL, M6's INDEX-2 qualifier
> is final and π is treated as a Sakai-side-only Bäcklund
> involution.

### Amendment v1.1.F — Note 4 replacement

Replace L810–814 Note 4 with:

> Note 4 (Phase B.5 — pre-closed at deposit time): Drafted at v1.16
> picture state as "mandatory pre-step / largest blind-spot risk".
> As of 2026-05-04 bridge `a9d34fd`, theorem-grade closed via
> SIARC-PRIMARY derivation: φ injective, INDEX-2 image, cokernel
> Z/2 = ⟨π⟩. Phase B.5 in this spec is now a citation-and-
> regression-check step rather than a primary derivation.
> HALT_M6_AFFINE_WEYL_MISMATCH retained as guard.
> Strict-isomorphism vs INDEX-2-final status pending 036.

### Amendment v1.1.G — Checklist patches (L838–876)

- L851: change *"Phase B.5 sub-tasks B.5.1, B.5.2, B.5.3, B.5.4 are
  explicit and complete"* → *"B.5.1, B.5.2 readback-only; B.5.3'
  citation-and-regression; B.5.4' halt-guard"*.
- L857: AEAL minimum text unchanged (still ≥ 16); verify the
  Phase-breakdown text in §3 reflects v1.1.C above.
- **Add new line:** *"§0 CONTEXT cites bridge `a9d34fd` for 033
  verdict and references 036 strict-iso scan as future-dependent
  qualifier"*.

### Recommended fire chronology (per synthesizer QA)

Branch (β): **Fire 036 SIARC-OKAMOTO-1987-SEC3-SCAN first** (~1-2
hr literature scan, INDEPENDENT, no operator gate). Outcome
collapses M6's strategic-implication framing to one of two clean
states:

- 036 → UPGRADE_M6_PHASE_B5_TO_STRICT_ISOMORPHISM:
  M6 fires next with strict-iso framing in §0 + Phase B.5 +
  STRATEGIC_IMPLICATION; the v1.1.E qualifier collapses.
- 036 → CONFIRM_M6_PHASE_B5_INDEX2_FINAL:
  M6 fires next with INDEX-2-final framing; π is treated as
  Sakai-side-only.
- 036 → HALT_*: surface; reconsider M6 fire timing.

If operator prefers velocity over framing-sharpness, branch (α)
fire-M6-as-amended-now is also defensible — the v1.1.E qualifier
keeps the INDEX-2-vs-strict-iso outcome contingent on 036 firing
later.

### Amendment block status

This amendment block is itself AEAL-anchored. The amendments
described herein are authoritative for the relay-agent dispatch;
the v1.0 verbatim spec body above is preserved unmodified for
provenance.

If the relay agent is dispatched WITHOUT applying these amendments,
the Phase B.5 deliverables will produce a structurally-correct
verdict but with an incorrect homomorphism direction recorded in
the agent's claims — surface as HALT_M6_AFFINE_WEYL_MISMATCH or
as a discrepancy log entry against 033's bridge `a9d34fd`.

