# Paper Profile [PROFILE-P1] — PCF-1 v1.3

**Session:** T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077
**Compiled:** 2026-05-07
**Source SHA-256 (16):** `82173A09521D6676` (TeX) / `EC7C1DD25D2B39E7` (PDF)
**Path:** `tex/submitted/p12_journal_main.tex` (72311 B, 1674 lines)

---

## B.1 Record metadata

- **Title:** "Complex Multiplication as a Transcendence Predicate for Degree-Two Polynomial Continued Fractions" (verbatim from `p12_journal_main.tex` L34-36; 17 words)
- **Concept DOI:** `10.5281/zenodo.19931635`
- **Version DOI:** `10.5281/zenodo.19937196` (per `portfolio_inventory.md` L40, SHA `25B4C96DC15A85A3`)
- **Page count (PDF estimate):** ~16 pp typeset (per 066 PCF1-V13-V_QUAD-ROW-REFRAMING handoff "16pp v1.3 source"; source 1674 lines AMS article)
- **Primary arXiv category:** `math.NT` (per portfolio inventory table row 2: "math.NT (math.CA)")
- **Cross-list categories:** `math.CA`
- **Submission status:** PUBLISHED on Zenodo (verdict in CMB.txt L29 "Published (Zenodo); arXiv endorsement requested 2026-05-04 (Zudilin)"); arXiv mirror PENDING ENDORSEMENT
- **AEAL claim count (paper-internal):** evidence ladder anchored across 30 degree-two families; ≥ 24 family-level data rows + 7-component schema + Conjecture A v5 with 4 parts; numeric-claim count is paper-substrate-level (no separate `claims.jsonl` per paper)

## B.2 Mathematical-result spine

**80-word summary [verbatim quote from abstract L72-99, 47 words]:**
> "We propose a transcendence predicate for degree-two polynomial continued fractions (PCFs), based on the sign of the balanced discriminant Δ = β² − 4αγ of the denominator polynomial b_n = αn² + βn + γ. Our central empirical contribution is a sharp dichotomy across thirty degree-two families."

**Key theorem labels (≤ 5 most-cited, verbatim labels only):**

- `thm:trans-closed` — "Trans-stratum closed form, Δ > 0" (proven side of the dichotomy; L450)
- `Conjecture A v5 part (i)` — "transcendence dichotomy" (L650)
- `Conjecture A v5 part (ii)` — "algebraic predicate" (L660)
- `Conjecture A v5 part (iii)` — Stokes-exponent (L927)
- `Conjecture A v5 part (iv)` — Painlevé-prototype (L936)

**Open conjectures or empirical claims (with AEAL-status):**

- Conjecture A v5 (i)–(iv): TIER-2-EMPIRICAL (30/30 families verified at dps 220, integer bound 10¹⁰; not theorem-proven on Δ < 0 side)
- Stokes-exponent diagnostic (S < 1 on all six Δ < 0 families): TIER-2-EMPIRICAL (220 dps; intra-field cross-check QL06 vs QL26 in ℚ(√−7))
- V_quad → P_III(D_6) reduction at (1/6, 0, 0, −1/2): TIER-1-CONFIRMED (cited from prior literature; recovered through Heun bridge in §6)
- Δ > 0 closed-form theorem (`thm:trans-closed`): TIER-1-CONFIRMED (proven; 24/24 Trans-stratum)

## B.3 Substrate dependency graph

**Cites (within the 6-record portfolio):**

- T2B v3.0 (Class A/B at d=2, the −2/9 + 1/4 ratio dichotomy)
- D2-NOTE v2.1 (Borel-radius identity ξ_0 = d/β_d^{1/d} at d=2 anchor; per 066 V_quad row reframing)
- CT v1.3 (V_quad → P_III(D_6) reduction recovered through CC channel)
- SIARC umbrella v2.0 (PCF-1 is the d=2 specialisation of the cross-degree invariant triple)
- PCF-2 v1.3 (PCF-2 is explicitly framed as the cubic extension of PCF-1)

**Cited by (within the 6-record portfolio):**

- PCF-2 v1.3 abstract L51-52: "PCF-1 established a sharp empirical dichotomy across 30 degree-two families..."
- CT v1.3 §Position L130-135: "the Stokes signal S(t)<1 measured in the recurrence-parameter channel for the six known Δ<0 degree-2 polynomial continued fractions (cite siarc_pcf1_v13, Sec. 5)"
- SIARC umbrella v2.0 abstract L60-62: "PCF-1 v1.3 (sharp WKB exponents at d=2 stratified by sgn(Δ_2))"
- D2-NOTE v2.1 §Setup L223 footnote: "[Remark 5.E] siarc_pcf1_v13" (the d=2 anomaly Galois bin out-of-scope marker)
- T2B v3.0 §Introduction: PCF-1 cited as the parent paper for Δ>0 / Δ<0 dichotomy framing

**Cross-reference matrix (6×6 boolean; row = cites, column = cited by):**

|  | P1 PCF-1 | P2 PCF-2 | P3 CT | P4 D2-NOTE | P5 T2B | P6 umbrella |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| P1 PCF-1 | — | ✓ | ✓ | ✓ | ✓ | ✓ |

(see `bundle_configuration_matrix.md` §C for the full 6×6 matrix.)

## B.4 Endorsement-fit summary

**[verbatim from `portfolio_inventory.md` row 2, 30 words]:**
> "PCF-1 v1.3 — Complex Multiplication as a Transcendence Predicate for Degree-2 PCFs. math.NT (math.CA). Zudilin H (math.NT primary). Mazzocco H (math.CA cross). Garoufalidis H (math.NT match). Anomalies: none."

3 of 3 Tier-1 endorsers rated H (HIGH) for PCF-1 v1.3. Zudilin
template send-ready at `sessions/2026-05-04/ZUDILIN-ENDORSEMENT-DRAFT-FINALIZE/`
per portfolio inventory L160. arXiv endorsement requested 2026-05-04
(CMB.txt L29).

---

End of P1 profile.
