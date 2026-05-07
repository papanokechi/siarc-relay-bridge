# Paper Profile [PROFILE-P5] — T2B v3.0

**Session:** T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077
**Compiled:** 2026-05-07
**Source SHA-256 (16):** `9BDD6A5D799BD8FE` (TeX) / `7AC8F204289409B5` (PDF)
**Path:** `tex/submitted/t2b_paper_draft_v5_withauthor.tex` (28635 B, 381 lines)

[NOTE-077-P5-1] Filename "v5_withauthor" reflects edit-history naming;
paper version is **3.0** per `\date{Version 3.0 \\ 2026-04-30}` header
at L18 verbatim. Both designators refer to the same artefact.

---

## B.1 Record metadata

- **Title:** "Two arithmetic classes of degree-(2,1) Trans-stratum continued fractions: a Birkhoff–Trjitzinsky / Gauss-continued-fraction dichotomy" (verbatim L11-12; 17 words)
- **Concept DOI:** `10.5281/zenodo.19783311` (per `portfolio_inventory.md` L44 verified across 3 sources; submission_log Item 10 L273 reads `19783311`)
- **Version DOI (v3.0):** `10.5281/zenodo.19915689`
- **Page count (PDF):** 8 pp typeset (pdf-regex /Type/Page count = 8)
- **Primary arXiv category:** `math.HO` (per portfolio inventory L44: "math.HO (math.NT)")
- **Cross-list categories:** `math.NT`
- **Submission status:** PUBLISHED on Zenodo (per CMB.txt portfolio table L31 "P-T2B | Trans -2/9 Conjecture | Zenodo | 10.5281/zenodo.19801038 | Published" — note CMB cites a different version DOI 19801038, surfaced D-077-4); per submission_log Item 10 L267-279 "Published on Zenodo (preprint, no journal review)"; "MM-01..MM-04 + UF-01 patches applied; coherent with UMB v3.0"
- **AEAL claim count (paper-internal):** 3 named theorems (Resonance family; Class A characterisation; Class B Stieltjes equivalence) + Completeness Conjecture; ~150,000 Class A families observed; 16 Brouncker-shape Class B families; 134,040 candidates at next BT integer-resonance locus a₂/b₁² = −3/16 returned zero hits

## B.2 Mathematical-result spine

**80-word summary [verbatim from abstract L21-28, 43 words; trailing clause paraphrased to honour HALT_077_QUOTE_LENGTH 50-word cap]:**
> "We study integer polynomial continued fractions (PCFs) of degree (2,1) — quadratic numerator, linear denominator — and their Trans-stratum: the convergent, generic-irrational subclass identified by exhaustive search in the SIARC programme. We show that the Trans-stratum partitions cleanly into exactly two arithmetic classes."

[Paraphrase of abstract L29-30, agent-authored, not a quote:]
The two classes are distinguished by the value of the structural
ratio `a_2 / b_1²`.

**Key theorem labels (≤ 5 most-cited, verbatim labels only):**

- `thm:resonance-family` — "Resonance family" (L137; Theorem 1)
- `thm:k2-stokes` — "Class A characterisation" (L186; Theorem 2)
- `thm:classB-stieltjes` — "Class B Stieltjes equivalence" (L232; Theorem 3)
- `conj:completeness` — "Completeness, T2B-revised" (L325)
- §6 "Empirical verification and the dichotomy" (L293; the 134,040-candidate desert sweep at k=3)

**Open conjectures or empirical claims (with AEAL-status):**

- Theorem 1 Resonance family (a₂/b₁² = −2/9 ↔ λ_+/λ_- = 2 integer-resonance): TIER-1-CONFIRMED (proven)
- Theorem 2 Class A characterisation (Stokes multiplier S_{12} ≠ 0 on locus → generic transcendental limits): TIER-1-CONFIRMED (Stokes-theoretic conditional theorem; "conditional" caveat on the Stokes-multiplier numerical step)
- Theorem 3 Class B Stieltjes equivalence (a₂/b₁² = +1/4 ↔ Pure-regime members are Stieltjes/Wallis transforms of Gauss CF for 4/π): TIER-1-CONFIRMED (proven)
- Saturation of the 16 Class B Brouncker-shape: TIER-3-OPEN (per Remark `rem:classB-saturation`)
- Completeness Conjecture (Trans-stratum at d=(2,1) exhausted by Class A + Class B): TIER-2-EMPIRICAL (134,040 candidates at k=3 yielded zero Trans-stratum families per L293-323)
- Off-orbit n/log(2) anchors at b1 ∈ {7, 10}: TIER-2-EMPIRICAL (044R + 044B; carried in T2B v3.0 narrative per CMB updates; see 044R/044B repo memory anchors)

## B.3 Substrate dependency graph

**Cites (within the 6-record portfolio):**

- PCF-1 v1.3 — Δ-discriminant dichotomy framing inherits from PCF-1's degree-2 dichotomy
- SIARC umbrella v2.0 — Trans-Stratum Conjecture in umbrella §5 L510 cites T2B-revised Completeness Conjecture verbatim
- D2-NOTE v2.1 — d=2 specialisation of cross-degree Borel-radius (Class A's BT characteristic equation λ² − b₁λ − a₂ = 0 is the d=2 Newton-polygon characteristic, related to D2-NOTE Lemma 3.1)
- CT v1.3 — Stokes mechanism in Class A (Stokes multiplier S_{12} on integer-resonance locus is the L_t no-go conjecture's d=2 Δ<0 zone)

**Cited by (within the 6-record portfolio):**

- SIARC umbrella v2.0 §5 (L503) "The Trans-Stratum Conjecture" — Trans-stratum two-class conjecture
- PCF-1 v1.3 §5 V_quad → P_III(D_6) reduction shares the −2/9 ↔ Δ=−11 prototype
- CMB.txt L1957 "alternative A_fit definition under PCF-2 v1.3"
- CMB.txt L1975 "upper-branch transition of PCF-1 v1.3 §6"

## B.4 Endorsement-fit summary

**[verbatim from `portfolio_inventory.md` row 5, 35 words]:**
> "T2B v3.0 — Two arithmetic classes of degree-(2,1) Trans-stratum continued fractions: a Birkhoff–Trjitzinsky / Gauss-continued-fraction dichotomy. math.HO (math.NT). Zudilin H (math.NT cross). Mazzocco M (Painlevé/asymptotic adjacency; math.NT cross-judgement plausible). Garoufalidis H (math.NT cross). Anomalies: none."

2 of 3 Tier-1 endorsers rated H; 1 rated M (Mazzocco). math.HO
primary may need cross-listing-out-strategy if a more specialised
venue is targeted; multi-category endorsement structurally easier
under cross-list rule.

---

End of P5 profile.
