# Convention pin (Phase D) — JIMBO-MIWA-1981-II-ACQUISITION

Date: 2026-05-04
Status: PRIMARY-SOURCE NIA (Phase B all-routes-fail); transitive readback via
        BLMP 2024 §4.1 (slot 08).

================================================================
D.1 Direct primary-source readback (NIA)
================================================================

JM81 II PDF was not acquired in this session (all OA routes failed; see
route_probe_log.md). Direct §_LP / §_param readback is therefore not
performed in this task. Section D.2 below substitutes a transitive readback
via BLMP 2024 §4.1, which cites JM81 II as ref [24] and faithfully reproduces
the JM81 II Lax-pair construction with verbatim source attribution.

================================================================
D.2 Transitive readback via BLMP 2024 §4.1 (slot 08)
================================================================

Slot 08 file:
  tex/submitted/control center/literature/g3b_2026-05-03/
    08_barhoumi_lisovyy_miller_prokhorov_2024_pIII_D6.pdf
  SHA-256: 96C49CDD51B6C2A395CCD6CC3CB66BFFEB623643B1A2374DB3F203760F696BB3
  Size: 2,018,889 bytes; 77 pages.

BLMP reference [24] is verbatim (extracted from refs page via pypdf):
  "[24] Jimbo M., Miwa T., Monodromy preserving deformation of linear
   ordinary differential equations with ra- tional coefficients. II,
   Phys. D 2 (1981), 407-448."
=> BLMP [24] is exactly the acquisition target of this task.

BLMP §4.1 "Lax pair for Painlevé-III(D6)" (page 24, verbatim, ≤30-word
quote per Rule §D):

  Q1 (page 24, attribution):
    "Following Jimbo and Miwa [24], we use the fact that each Painlevé
     equation can be recast as an isomonodromic deformation condition for
     a 2x2 system of linear ODEs with rational coefficients."
    [27 words; primary attribution to JM81 II.]

  Q2 (page 24, equation 4.2 + 4.3 normalization):
    "After some normalization, the differential equation can be written
     in the form [eq 4.1-4.3] ... ϴ_∞ is a complex parameter and
     s = s(x), t = t(x), v = v(x), y = y(x)."
    [pp. 24-25, structurally close-paraphrase; one explicit named
     parameter ϴ_∞ at this stage.]

  Q3 (page 25, equation 4.6 — the parameter map):
    "denoting the constant value of I by ϴ_0, we arrive at (1.1) with
     parameters ϴ_0 = α/4, ϴ_∞ = 1 - β/4. (4.6)"
    [verbatim ≤30 words; this is the explicit two-parameter
     correspondence map: (α, β) ↔ (ϴ_0, ϴ_∞).]

  Q4 (page 25, monodromy interpretation):
    "The constants ϴ_0, ϴ_∞ can be naturally interpreted on the level
     of the 2x2 system (4.1)" — followed by formal-solution exponents
     ψ_formal^(∞) ~ exp(ix λ σ_3 / 2) λ^(-ϴ_∞ σ_3 / 2) and
     ψ_formal^(0) ~ exp(-i x λ^(-1) σ_3 / 2) λ^(ϴ_0 σ_3 / 2).
    [eqs 4.7-4.8; ϴ_0 and ϴ_∞ appear as the formal-monodromy exponents
     at the two irregular singular points λ=0 and λ=∞ respectively.]

================================================================
D.3 BLMP transitive convention pin (parameter labeling, JM81 II core)
================================================================

Per BLMP §4.1 "Following Jimbo and Miwa [24]":

  - JM81 II's Lax-pair construction for Painlevé-III(D6) introduces
    EXACTLY TWO core parameters denoted (ϴ_0, ϴ_∞), arising as the
    formal-monodromy exponents at the irregular singular points λ=0
    and λ=∞ of the 2x2 spectral system.

  - The map to the standard PIII(D6) coefficients (α, β) of equation
    (1.1) is:
        ϴ_0 = α/4,    ϴ_∞ = 1 - β/4    (BLMP eq 4.6)

  - Additional 2x2 monodromy data (Stokes multipliers s_1^∞, s_2^∞,
    s_1^0, s_2^0 and connection-matrix entries C_0∞^±) appear in BLMP
    §4.2-4.3 but are FUNCTIONS of (ϴ_0, ϴ_∞) and the moduli x.
    The CORE Lax-pair labeling is two-parameter.

================================================================
D.4 Comparison with CT v1.3 §3.5 4-tuple (1/6, 0, 0, -1/2)
================================================================

CT v1.3 §3.5 specifies a 4-tuple
  (α_∞, α_0, β_∞, β_0) = (1/6, 0, 0, -1/2).

Comparison with JM81 II (per BLMP transitive reading):

  - JM81 II core convention: (ϴ_0, ϴ_∞), TWO parameters, NOT a 4-tuple.
  - Symbol mismatch at the alphabet level: CT uses (α, β) doubly indexed
    by (∞, 0); JM81 II uses (ϴ) singly indexed by (0, ∞).
  - Cardinality mismatch: 4 vs. 2.
  - The JM81 II (ϴ_0, ϴ_∞) labeling is structurally identical to
    Okamoto 1987's W(B_2) 2-parameter convention (already pinned by
    OKAMOTO-1987-CONSTRAINT-PIN, 2026-05-04).

Provisional convention-pin verdict:
  CT v1.3 §3.5's 4-tuple (α_∞, α_0, β_∞, β_0) is consistent with
  neither (i) Jimbo-Miwa 1981 II's core 2-parameter (ϴ_0, ϴ_∞) Lax-pair
  labeling (per transitive reading via BLMP 2024 §4.1), nor (ii)
  Okamoto 1987's 2-parameter W(B_2) labeling (per the prior pin).
  This is consistent with the alternative-source hypothesis (Sakai 2001
  D_6 surface root-system convention) being the residual canonical
  candidate for the CT 4-tuple origin.

Caveats and limitations of transitive reading:
  (a) Without direct primary-source readback, we cannot rule out that
      JM81 II §_LP for sub-cases (e.g., the "P_III' " or "degenerate"
      sub-cases in JM81 II §3-§4) introduces additional parameter
      labels that BLMP 2024 §4.1 does not surface.
  (b) BLMP works specifically with the Painlevé-III(D6) generic case;
      JM81 II covers the full P_I-P_VI tableau and may use richer
      labeling per equation in the generic isomonodromic-deformation
      setup of JMU 1981 I (RIMS-319).
  (c) Direct verbatim verification (ILL acquisition recommended) is
      needed before declaring the convention pin closed at primary-
      source level.

================================================================
D.5 Cross-validation with BLMP §4.1 wording (per G17 anchor)
================================================================

The G17-LAYER-SEPARATION-LIT-ANCHOR (2026-05-04) Phase B.3 anchor
records BLMP 2024 §4.1 as quoting "after Jimbo-Miwa 1981 II" for the
Lax-pair construction. The current re-read of slot 08 page 24 confirms
the actual BLMP wording: "Following Jimbo and Miwa [24]". The G17
anchor's "after" phrasing is a paraphrase; the verbatim wording is
"Following ... [24]". This does not affect the convention-pin
conclusion: BLMP faithfully attributes the 2-parameter (ϴ_0, ϴ_∞)
Lax-pair construction to JM81 II.

================================================================
D.6 Outcome ladder mapping
================================================================

Spec ladder vs. session findings:

  - UPGRADE_JM81_ACQUIRED_CT_TUPLE_DIRECT_MATCH:
      not realized (acquisition NIA).
  - UPGRADE_JM81_ACQUIRED_CT_TUPLE_VIA_RELABELING:
      not realized (acquisition NIA).
  - UPGRADE_JM81_ACQUIRED_CT_TUPLE_NOT_FROM_JM81:
      provisionally consistent with BLMP transitive reading; cannot
      claim at "ACQUIRED" tier.
  - UPGRADE_JM81_NIA_ILL_RECOMMENDED_<library>:
      best fit at the AEAL-honest tier.
  - HALT_JM81_DIRECT_DISAGREES_WITH_BLMP:
      not triggered (BLMP transitive reading is internally consistent
      and aligned with the Okamoto 1987 pin; the CT 4-tuple is
      flagged as not-from-JM81-II by transitive reading, but BLMP
      and JM81 II do not disagree with each other).
  - HALT_JM81_TEXT_LAYER_BAD: n/a (no acquisition).
  - HALT_JM81_ALL_OA_ROUTES_FAIL: triggered as a sub-finding of
      Phase B; surfaced via the ILL recommendation.
  - HALT_JM81_PAYWALL_RULE_1: triggered for ScienceDirect (B.1);
      surfaced via the ILL recommendation.

Composite verdict (per AEAL honesty, see handoff §Verdict):
  UPGRADE_JM81_NIA_ILL_RECOMMENDED_RIMS_KYOTO
  with BLMP-TRANSITIVE-READING sub-finding indicating CT 4-tuple is
  NOT_FROM_JM81_II_CORE_CONVENTION (provisional pending direct
  primary-source verification).
