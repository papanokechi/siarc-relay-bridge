# doi_resolution_probe.md — STEP 3

**Generated:** 2026-05-06 (Wed, W19)
**Method:** Per memory `Bibliographic identifier pre-verification`
(2026-05-04 SOP), each cited identifier resolved via Crossref API
(`https://api.crossref.org/works/<DOI>`) or arXiv abstract page
(`https://arxiv.org/abs/<arXiv-ID>`); HEAD request for the Kobe-U
direct-PDF URL. Resolved title + first author + journal/volume
compared to the cited reference.

**Important:** The CC-VQUAD-PIII spec §1 cites each anchor by
filename + SHA prefix + journal/volume/page only — it does NOT
embed DOI/arXiv identifiers in the spec body. The probes below
verify identifiers cited (a) inline in `SHA256SUMS.txt` notes
and (b) suggested in the 057 prompt body for verification. Per
SOP §scope, the probes here are *pre-fire* sanity checks for the
058 main relay; an identifier resolving to a different paper
than expected is flagged as anomaly even if not cited in the
spec proper.

---

## §A — Identifiers cited inline in SHA256SUMS.txt or pinned to known references

| ref | identifier | resolves to | match? |
|-----|------------|-------------|--------|
| Birkhoff 1930 (slot 01) | DOI **10.1007/bf02547522** (Crossref-canonical Acta Math entry) | "Formal theory of irregular linear difference equations" by Birkhoff George D., Acta Mathematica **54** (1930) pp. 205-246 | **YES** ✓ |
| Birkhoff-Trjitzinsky 1933 (slot 03) | DOI **10.1007/bf02398269** (Crossref-canonical Acta Math entry) | "Analytic theory of singular difference equations" by Birkhoff George D. & Trjitzinsky W. J., Acta Mathematica **60** (1933) pp. 1-89 | **YES** ✓ |
| Wasow 1965 (slot 04) | no DOI (1965 Interscience monograph; 1987/2018 Dover reprint ISBN 9780486495187); no Crossref entry surfaced for the Wasow book | identifier-level resolution N/A (book pre-dates Crossref); previously verified at acquisition time by title-page text extraction (SHA256SUMS.txt amendment 2026-05-03 — Chap IV §§10-15 + Chap V §§16-19 captured) | **N/A — non-DOI; re-confirmed via SHA + acquisition title-page** |
| Costin 2008 (slot 06) | DOI **10.1201/9781420070323** (Crossref book entry) | "Asymptotics and Borel Summability" by Costin Ovidiu, Chapman and Hall/CRC, 2008 | **YES** ✓ |
| Okamoto 1987 P_III (slot 07) | direct URL `http://fe.math.kobe-u.ac.jp/FE/FE_pdf_with_bookmark/FE21-30-en_KML/fe30-305-332/fe30-305-332.pdf` | HTTP 200; content-type=application/pdf; content-length=**6,075,525 bytes** (bit-exact to slot-07 PDF on disk: 6,075,525 bytes) — title-page text extracted at acquisition reads "Funkcialaj Ekvacioj, 30 (1987) 305-332 / Studies on the Painlevé Equations IV. / Third Painlevé Equation P_{III} / Kazuo OKAMOTO" (per SHA256SUMS.txt 2026-05-04 amendment) | **YES** ✓ |
| Barhoumi-Lisovyy-Miller-Prokhorov 2024 (slot 08) | arXiv **2307.11217** + DOI **10.3842/SIGMA.2024.019** | arXiv: "Painlevé-III Monodromy Maps Under the D_6→D_8 Confluence and Applications to the Large-Parameter Asymptotics of Rational Solutions" by Barhoumi, Lisovyy, Miller, Prokhorov; SIGMA 20 (2024) 019; Crossref DOI confirms same title + container "Symmetry, Integrability and Geometry: Methods and Applications" 2024 | **YES** ✓ |
| Sakai 1999 preprint (slot 13) — published 2001 | published-version DOI **10.1007/s002200100446** (slot 13 is the Kyoto preprint) | "Rational Surfaces Associated with Affine Root Systems and Geometry of the Painlevé Equations" by Sakai Hidetaka, Comm. Math. Phys. **220** (2001) pp. 165-229 | **YES** ✓ (preprint→published cross-reference; SHA256SUMS slot-13 note already documents this) |
| Kajiwara-Noumi-Yamada 2017 (slot 14) | arXiv **1509.08186** + Related DOI **10.1088/1751-8121/50/7/073001** | "Geometric Aspects of Painlevé Equations" by Kajiwara, Noumi, Yamada; J. Phys. A: Math. Theor. **50(7)** (2017) 073001; 168 pp. | **YES** ✓ |
| Noumi-Yamada 1998 (slot 15) | arXiv **math/9804132** + Related DOI **10.1007/s002200050502** | "Affine Weyl groups, discrete dynamical systems and Painleve equations" by Noumi, Yamada; CMP **199** (1998) 281-295; 16 pp. | **YES** ✓ |
| Noumi-Yamada 2000 (slot 16) | arXiv **math/0012028** + Related DOI **10.1142/9789812810199_0010** | "Birational Weyl group action arising from a nilpotent Poisson algebra" by Noumi, Yamada; MathPhys Odyssey 2001, Birkhäuser 2002, pp. 287-319; 31 pp. | **YES** ✓ |

§A aggregate: **9 PASS / 0 FAIL / 1 N/A (Wasow non-DOI)**.

---

## §B — Anomaly: 057-prompt-body suggested DOI for Birkhoff 1930 RESOLVES TO UNRELATED PAPER

The 057 relay prompt body §STEP 3 suggested (as a candidate for
verification) the DOI **10.1007/BF02547452** for "Birkhoff, G.D.
(1930). Formal theory of irregular linear difference equations.
Acta Math 54, 205-246." The prompt phrased this as "Project
Euclid DOI 10.1007/BF02547452 (or current equivalent)" — i.e.
flagged it as a candidate to be tested.

**Probe result (Crossref API):**
> 10.1007/BF02547452 → [1995] "Thermal studies and spectral
> characterization of the chelate of bis-(η5-cyclopentadienyl
> titanium(IV)) with salicylidene-4-methylaniline" by Mishra
> Virendra; Parmar D. S.; Joshi Virendra; Kaushik N. K.;
> Journal of Thermal Analysis vol. 45 pp. 1589-1596.

This is a known LLM failure mode (cf. memory `Bibliographic
identifier pre-verification` and 031 WITTE-FORRESTER-2010
verdict). The candidate DOI is one digit different from the
correct DOI (...7452 vs ...7522 — a transposition).

**Resolution:** Substituted with the Crossref-canonical DOI
**10.1007/bf02547522** (verified above in §A). The CC-VQUAD-PIII
spec §1 itself does NOT cite the wrong DOI — only filename + SHA
prefix `aeb5291e` + journal/volume citation "Acta Math 54, 205-
246" (which is correct). Therefore:

  - Spec citation → unaffected (no spec body modification needed).
  - 057-prompt-body candidate DOI → flagged as wrong; will be
    addressed by surfacing in handoff Anomalies + 058 go/no-go.
  - Anchor file integrity → confirmed by §A row 1 + §STEP 2 row 1
    (live SHA matches expected SHA aeb5291e).

This anomaly does **NOT** trigger HALT_057_DOI_HALLUCINATION on
the spec, because the spec does not cite the wrong DOI as an
acquisition target. The hallucinated DOI was in the 057 prompt
body itself and has been substituted for the canonical DOI in
this report.

---

## §C — Methodology notes

1. **Crossref API** used as the primary canonical-identifier
   source (DOI registry of record for Acta Math, SIGMA, CRC
   monograph, Comm. Math. Phys., J. Phys. A, etc.).
2. **arXiv abstract pages** consulted directly for arXiv IDs;
   abstract title + author list + journal-reference pulled.
3. **HEAD request** to the Kobe-U URL for slot 07 (since FE 30
   does not have a Crossref-indexed DOI; FE journal is not in
   Crossref); content-length match (6,075,525 bytes) is the
   bit-exact-size cross-check against the disk PDF.
4. **No new literature acquired** — all probes were read-only
   identifier resolution; no PDF download or modification.
5. **SHA256SUMS.txt unmodified** — confirmed by file's
   pre-/post- SHA-256 unchanged at
   `0518E111CFD408A3A04015FCE3D8278AF06226D0B7BD527361701FE5C8A0A190`.

---

## Aggregate

| group | PASS | FAIL | N/A | notes |
|-------|------|------|-----|-------|
| §A canonical identifier resolutions | 9 | 0 | 1 (Wasow) | all CC-VQUAD-anchored references resolve to the expected paper |
| §B 057-prompt suggested DOI | 0 | 1 | 0 | hallucinated DOI substituted with canonical |
| **TOTAL probed identifiers** | **9** | **1** | **1** | **9 PASS / 1 substituted (no spec dependency) / 1 non-DOI** |

**Result:** No HALT_057_DOI_HALLUCINATION condition for the spec
itself — every spec-cited reference resolves correctly via at
least one canonical identifier (Crossref, arXiv, or direct URL).
The single anomaly was a stray candidate DOI in the 057 prompt
body which has been substituted with the correct Crossref DOI;
this anomaly has zero effect on the CC-VQUAD-PIII spec's
literature-anchor closure.
