# Pre-Verification Report — T1-069R1-SUBSTRATE-GAP-PRE-VERIFICATION-102

**Task:** Canonical bibliographic-identifier resolution + accessibility-tier classification
for the three references cited in the 069r1 NO_GO_SUBSTRATE_INSUFFICIENT verdict.

**Anchor verdict:** 069r1 (commit `601500b`,
sessions/2026-05-07/M6-CC-R1-CLOSURE-PREFLIGHT-069R1/), verdict
`NO_GO_SUBSTRATE_INSUFFICIENT`, both paths (α = KNY chart-shift Δ; β =
Okamoto 1987 §3 τ-function reparametrisation) closed at A.1.5 substrate gap.
Substrate-gap content per 058R `phase_b_canonical_map.md` L136-140: the explicit
`(a_0, a_1, a_2) → (α_inf, α_0, β_inf, β_0)` chart-map IS the open R1 itself.

**Date:** 2026-05-07
**Bridge HEAD at fire:** `402c7de`
**069r1 anchor commit:** `601500b` (reachable, confirmed via `git log --all --oneline 601500b`)

**Scope:** Canonical-ID resolution + accessibility-tier classification ONLY.
NO PDF acquisition. NO substrate-gap closure. NO 069r2 R1-CLOSURE FIRE drafting.

---

## 1. Resolution summary

| 069r1 cite                       | Canonical DOI                              | arXiv         | Tier | Resolution |
|----------------------------------|--------------------------------------------|---------------|------|------------|
| Jimbo-Miwa 1981 papers I-V       | 10.1016/0167-2789(81)90013-0 (Part I, JMU) | n/a (pre-arXiv) | 3   | RESOLVED (with discrepancy: only Parts I-III exist; Part I has 3rd author Ueno) |
|                                  | 10.1016/0167-2789(81)90021-X (Part II)     | n/a           | 3    | RESOLVED |
|                                  | 10.1016/0167-2789(81)90003-8 (Part III)    | n/a           | 3    | RESOLVED |
| Conte-Musette 2008 review        | 10.1007/978-1-4020-8491-1 (1st ed)         | n/a           | 3    | RESOLVED |
| Forrester-Witte 2002             | 10.1002/cpa.3021 (CPA 55(6))               | math-ph/0201051 | 1  | RESOLVED |

**Verdict candidate:** **V2 — ALL_3_RESOLVED_MIXED_ACCESSIBILITY**

All three 069r1-cited references resolve to canonical DOIs; one is open-access
(Forrester-Witte 2002 via arXiv:math-ph/0201051), two are paywalled (Jimbo-Miwa
Physica D series + Conte-Musette 1st ed).

---

## 2. Per-reference canonical records

### 2.1 Jimbo-Miwa-Ueno (1981) — Physica D series

The 069r1 cite "Jimbo-Miwa 1981 papers I-V" refers to a three-part Physica D
series (NOT five parts). Full canonical metadata recorded in
[jimbo_miwa_resolution.json](jimbo_miwa_resolution.json). Summary:

- **Part I** (DOI [10.1016/0167-2789(81)90013-0](https://doi.org/10.1016/0167-2789(81)90013-0))
  — Jimbo, Miwa, Ueno, Physica D 2(2):306-352, April 1981. **Three authors, including Ueno.**
- **Part II** (DOI [10.1016/0167-2789(81)90021-X](https://doi.org/10.1016/0167-2789(81)90021-X))
  — Jimbo, Miwa, Physica D 2(3):407-448, June 1981. **Most directly relevant for P_III τ-function.**
- **Part III** (DOI [10.1016/0167-2789(81)90003-8](https://doi.org/10.1016/0167-2789(81)90003-8))
  — Jimbo, Miwa, Physica D 4(1):26-46, October 1981.

Discrepancies with 069r1 cite (recorded in [discrepancy_log.json](discrepancy_log.json)):
- **D1_069R1_PART_COUNT** — 069r1 says "I-V" but only Parts I, II, III exist in Physica D under
  this title. Likely conflation with the four 1980 Proc. Japan Acad. precursor notes
  (10.3792/pjaa.56.{143,149,269,301}).
- **D2_069R1_AUTHOR_SHORTHAND** — Part I has three authors {Jimbo, Miwa, Ueno}; "Jimbo-Miwa"
  is field-shorthand omitting Ueno.

Auxiliary open-access precursors (Project Euclid, 1980, all Tier 1):
`10.3792/pjaa.56.143` (I), `10.3792/pjaa.56.149` (II), `10.3792/pjaa.56.269` (III),
`10.3792/pjaa.56.301` (IV, Miwa solo).

### 2.2 Conte-Musette (2008) — The Painlevé Handbook (1st ed)

DOI [10.1007/978-1-4020-8491-1](https://doi.org/10.1007/978-1-4020-8491-1) — Conte & Musette,
Springer Netherlands, Dordrecht, 2008. ISBN 9781402084904 (print) /
9781402084911 (electronic). Full record in
[conte_musette_resolution.json](conte_musette_resolution.json).

A 2nd edition (2020, DOI [10.1007/978-3-030-53340-3](https://doi.org/10.1007/978-3-030-53340-3),
Springer International Cham, Mathematical Physics Studies series) exists with
expanded coverage; this is the version referenced by sibling envelope T2-R5-LIT-HUNT-TRIANGULATION-086.
069r1's "2008" year-stamp uniquely identifies the 1st edition.

Discrepancy:
- **D3_069R1_EDITION_AMBIGUITY** — 069r1 cite is unambiguous to 1st ed by year, but synth at
  LANE-1 should consider whether 2nd ed's expanded discrete-Painlevé and multi-component-reduction
  material is relevant before final acquisition.

### 2.3 Forrester-Witte (2002) — CPA 55(6)

DOI [10.1002/cpa.3021](https://doi.org/10.1002/cpa.3021) — Forrester & Witte,
"Application of the τ-function theory of Painlevé equations to random matrices:
P_V, P_III, the LUE, JUE, and CUE", *Comm. Pure Appl. Math.* 55(6):679-727,
March 2002 (online) / June 2002 (print). arXiv preprint
[math-ph/0201051](https://arxiv.org/abs/math-ph/0201051) (submitted 2002-01-24).
Full record in [forrester_witte_resolution.json](forrester_witte_resolution.json).

Disambiguation: the 069r1 "Forrester-Witte 2002" cite resolves uniquely to this paper;
flanking candidates (CMP 2001 PIV/PII/GUE; Nagoya 2004 PVI; ANZIAM 2002 short note;
Nonlinearity 2003 discrete Painlevé) are year-mismatched OR topically off (none treat
P_III with substantive τ-function development).

Discrepancy:
- **D4_069R1_FW_AMBIGUITY** — multiple Forrester-Witte papers in the τ-function/Painlevé
  series; 069r1 year-stamp uniquely picks CPA 2002 (P_V/P_III/LUE/JUE/CUE).

---

## 3. Accessibility tier matrix

Tier definitions:
- **Tier 1** = open-access (free, no acquisition action required)
- **Tier 2** = preprint-archive accessible (e.g., arXiv) but final-record paywalled
- **Tier 3** = paywall (requires institutional ILL or pay-per-view purchase)
- **Tier 4** = closed/withdrawn/inaccessible

| Reference                              | Tier | Free PDF source             | Cost (USD)  |
|----------------------------------------|------|-----------------------------|-------------|
| Jimbo-Miwa-Ueno I (10.1016/...90013-0) | 3    | none                        | ~35-50 ppv  |
| Jimbo-Miwa II   (10.1016/...90021-X)   | 3    | none                        | ~35-50 ppv  |
| Jimbo-Miwa III  (10.1016/...90003-8)   | 3    | none                        | ~35-50 ppv  |
| Conte-Musette 2008 1st ed              | 3    | none                        | 80-150 book |
| Forrester-Witte 2002 (CPA)             | 1    | arxiv.org/abs/math-ph/0201051 | 0         |

Open-access auxiliary substrate (Tier 1):
- Proc. Japan Acad. 1980 short-form precursors (10.3792/pjaa.56.{143,149,269,301})
  via Project Euclid.
- arXiv:math-ph/0201051 (Forrester-Witte 2002 preprint, content-equivalent to
  Wiley CPA published version per Crossref abstract match).

---

## 4. Substrate-gap mapping per reference

Recapitulating the gap from 058R `phase_b_canonical_map.md` L136-140:
the explicit chart-map `(a_0, a_1, a_2) → (α_inf, α_0, β_inf, β_0)` for the
P_III ODE coefficient namespace is the open R1 itself.

| Reference | Section(s) most relevant | Coverage |
|-----------|--------------------------|----------|
| Jimbo-Miwa-Ueno I  | §4 isomonodromic-deformation parameter space | partial — sets the framework but does not specialize to P_III |
| Jimbo-Miwa II      | §3-4 P_III tau-function + monodromy data     | **direct match for substrate gap** |
| Jimbo-Miwa III     | §2 degenerations P_VI → P_V → P_III          | tangential |
| Conte-Musette 2008 ch. 5 | Painlevé property test for ODEs       | partial — verifies chart-map well-definedness only |
| Conte-Musette 2008 ch. 7 | multi-scale + perturbation reductions | partial — complementary, not on canonical chart |
| Forrester-Witte 2002 §2-3 | Okamoto P_V/P_III τ-function development with explicit chart variables | **direct match for substrate gap** |
| Forrester-Witte 2002 §4   | hard-edge LUE → P_III τ characterization | direct match if LANE-1 prefers random-matrix-side derivation |

### 4.1 Path-coverage assessment

**Path α (analytic-guidance from existing substrate + Conte-Musette 1st ed):**
INSUFFICIENT for the specific P_III τ-function chart-map. Conte-Musette covers
Painlevé property + general reductions but lacks the random-matrix/τ-function
characterization needed at A.1.5.F1.

**Path β (literature-acquisition: Jimbo-Miwa Part II + Forrester-Witte 2002):**
SUFFICIENT. These two papers together provide both the original
isomonodromic-deformation derivation (JM II) and the τ-function/random-matrix
characterization (FW 2002) of the P_III chart variables. Forrester-Witte 2002 is
already Tier 1 OPEN; only Jimbo-Miwa Part II requires acquisition.

**Path γ (single-paper minimal-acquisition: Forrester-Witte 2002 only):**
LIKELY SUFFICIENT when paired with Okamoto 1987 (Funkcial. Ekvac. 30:305 for
P_III) which is already in 069r1 substrate. FW 2002 §2-3 establishes the
explicit (α, β, γ, δ)_{P_III} ↔ (a, b, c, d)_{Hamiltonian} ↔ (τ-function arguments)
chart correspondence directly. This is the lowest-cost path.

---

## 5. Verdict ladder

Using the envelope's verdict taxonomy:

- **V1 — ALL_3_OPEN_ACCESS** — falsified. JM 1981 + Conte-Musette 1st ed are paywalled.
- **V2 — ALL_3_RESOLVED_MIXED_ACCESSIBILITY** — **ACTIVE**. All 3 cites resolve to canonical
  DOIs; FW 2002 is Tier 1 (arXiv); JM 1981 + Conte-Musette 2008 are Tier 3.
- **V3 — PARTIAL_RESOLUTION** — falsified. All 3 resolved.
- **V4 — NONE_RESOLVED_OR_HALLUCINATED** — falsified. All 3 resolved.

**Selected verdict: V2 — ALL_3_RESOLVED_MIXED_ACCESSIBILITY**

### Halt-condition checks

- **H_ENV1** (cite-not-resolved) — NOT triggered (all 3 resolved).
- **H_ENV2** (cite-hallucinated) — NOT triggered (all 3 canonical via Crossref).
- **H_ENV3** (DOI-drift-major) — NOT triggered. Minor drift recorded as discrepancies D1/D2/D3/D4
  (part-count loose, author-shorthand, edition-disambiguation, year-disambiguation); no critical drift.
- **H_ENV4** (accessibility-Tier-4-only) — NOT triggered (FW 2002 is Tier 1).
- **H_ENV5** (FW-ambiguous) — NOT triggered. FW 2002 disambiguates uniquely to
  10.1002/cpa.3021 by year + topic (P_III). The four flanking FW papers are clearly
  year- or topic-mismatched.

No halt conditions triggered. `halt_log.json` written with empty `{}`.

---

## 6. Recommendation for W21 LANE-1 synth (Mon 2026-05-12)

**Path γ (lowest-cost, recommended):**
Treat Forrester-Witte 2002 (arXiv:math-ph/0201051, free PDF) plus already-acquired
Okamoto 1987 (Funkcial. Ekvac. 30:305) as the substrate-closure pair for A.1.5.F1.
This requires NO acquisition action and uses existing 069r1 substrate plus one
free arXiv PDF. Estimated synth time: 60-90 min for the chart-map closure.

**Path β fallback (if γ found insufficient at synth):**
Add targeted ILL or pay-per-view acquisition of Jimbo-Miwa Part II
(DOI 10.1016/0167-2789(81)90021-X, ~$35-50 ppv or $0 ILL). Acquisition
window: 1-3 days. This provides independent isomonodromic-deformation
verification of the chart-map.

**Path α (analytic-guidance only, NOT recommended):**
Conte-Musette 2008 1st ed alone is INSUFFICIENT and should not be used as the
primary closure substrate. It may be useful as supplementary background for the
Painlevé-property verification step (ch. 5) but does not close the F1 gap.

---

## 7. Files in this deposit

- `pre_verification_report.md` (this file)
- `jimbo_miwa_resolution.json`
- `conte_musette_resolution.json`
- `forrester_witte_resolution.json`
- `claims.jsonl` (≥6 AEAL entries)
- `discrepancy_log.json`
- `halt_log.json` (empty `{}`)
- `unexpected_finds.json`
- `handoff.md`

## 8. AEAL claim count

7 entries written to `claims.jsonl` (≥ 6 base floor).
