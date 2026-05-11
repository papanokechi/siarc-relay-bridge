# Verified Bibliography — FIRE-A1 Frontier-A literature anchor verification

**Date:** 2026-05-11
**Bridge predecessor:** slot 185 (`5ba0072`) Amendment-1 LOAD-BEARING gate
**Verification mode:** arXiv `citation_author` meta-tag inspection (post-031 bibliographic pre-verification rule)
**Slot collision note:** prompt body uses Task-ID -187, but slot 187 already landed at `3d698d7` (T1-SYNTH-UMBRELLA-V23-FRONTIER-COMMIT-ROUND-187); folder name uses **-188** to match filename and avoid collision. See D-188-1.

---

## Verification table (10 entries)

| # | Tier | Cited as | arXiv ID | Resolved title | Resolved authors | Year | DOI | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | Anchor (methodological-template) | Mazzocco & Mo 2006 | nlin/0610066 | The Hamiltonian Structure of the Second Painlevé Hierarchy | Mazzocco, Marta; Mo, Man Yue | 2006 | 10.1088/0951-7715/20/12/006 (Nonlinearity 20, 2007) | ✅ PASS — authors + title + year match cited reference. PII hierarchy paper used as methodological template for PIII(D₆) hierarchy construction (NOT a direct PIII anchor). |
| 2 | Anchor (methodological-template) | Bobrova & Mazzocco 2020 | 2012.11010 | The Sigma Form for the PII Hierarchy | Bobrova, Irina; Mazzocco, Marta | 2020 | 10.1016/j.geomphys.2021.104271 (J. Geom. Phys. 170, 2021) | ✅ PASS — authors + title + year match. PII sigma-form, again methodological-template for PIII analog. |
| 3 | Methodological | Joshi & Mazzocco 2002 | math/0212117 | Existence and Uniqueness of Tri-tronquée Solutions of the second Painlevé hierarchy | Joshi, N.; Mazzocco, M. | 2002 | 10.1088/0951-7715/16/2/304 (Nonlinearity 16, 2003) | ✅ PASS — authors + title + year match. Asymptotic-series existence/uniqueness in PII hierarchy; methodological tool for Borel-Pade analysis. |
| 4 | Methodological | Joshi-Lustri-Topp 2014 | 1403.1235 | Connection problem for the sine-Gordon/Painlevé III tau function and irregular conformal blocks | Its, A.; Lisovyy, O.; Tykhyy, Yu. | 2014 | 10.1093/imrn/rnu209 (Int. Math. Res. Notices 2015, 8903-8924) | ❌ **FAIL** — citation says **Joshi-Lustri-Topp**, arXiv ID resolves to **Its-Lisovyy-Tykhyy**. Hallucinated identifier (post-031 failure mode). The actual paper IS PIII-relevant (sine-Gordon/PIII tau function) but author attribution is wrong. Closest Joshi+Lustri paper found via web search: arXiv:1503.01302 "Stokes Phenomena in Discrete Painlevé I" by Joshi-Lustri 2015 (NO Topp; discrete PI not continuous PIII). No Joshi-Lustri-Topp 2014 published paper appears to exist. |
| 5 | Methodological | IILZ 2025 | 2505.16803 | Many-faced Painlevé I: irregular conformal blocks, topological recursion, and holomorphic anomaly approaches | Iorgov, Nikolai; Iwaki, Kohei; Lisovyy, Oleg; Zhuravlov, Yurii | 2025 | (no published DOI yet) | ✅ PASS — IILZ = Iorgov-Iwaki-Lisovyy-Zhuravlov; authors + title + year match. PI tau function methodological work; openly accessible on arXiv. |
| 6 | Methodological | LR 2024 | 2407.03464 | Semiclassical limit of a non-polynomial q-Askey scheme | Lenells, Jonatan; Roussillon, Julien | 2024 | (no published DOI yet) | ✅ PASS — LR = Lenells-Roussillon; authors + title + year match. Covers PI **AND PIII₃** (= PIII(D₆) degeneration) Darboux coordinates — directly PIII-relevant; openly accessible on arXiv. |
| 7 | Citation-only | ILP 2016 | 1604.03082 | Monodromy dependence and connection formulae for isomonodromic tau functions | Its, A.; Lisovyy, O.; Prokhorov, A. | 2016 | 10.1215/00127094-2017-0055 (Duke Math. J. 167, no. 7 (2018), 1347-1432) | ✅ PASS — ILP = Its-Lisovyy-Prokhorov; authors + title + year match. PVI + PII tau function connection formulae; openly accessible on arXiv. |
| 8 | Citation-only | Sakai 2001 (original Painlevé surface classification) | (no arXiv) | Rational surfaces associated with affine root systems and geometry of the Painlevé equations | Sakai, Hidetaka | 2001 | 10.1007/PL00005590 (Comm. Math. Phys. 220, no. 1 (2001), 165-229) | ✅ PASS — canonical Sakai reference identified via Crossref-style search. This is the foundational paper that introduced the PIII(D₆) / D₇ / D₈ Sakai-surface-type classification. |
| 9 | Citation-only (SIARC-internal) | cascade-067 V_quad resurgence note | bridge git | (internal session reference) | SIARC bridge | 2026-05-04~ | n/a | ⚠️ NOT-LOCATED-IN-THIS-FIRE — git log not searched in this fire (lower priority given HALT_A1_GAP_CLOSED supersedes downstream FIRE-A2/A3); Sakai surface-type tooling presumed available in bridge but not re-verified. |
| 10 | Citation-only (SIARC-internal) | 069r3 Sakai D₆⁽¹⁾ closure | bridge git | (internal session reference) | SIARC bridge | 2026-05-04~ | n/a | ⚠️ NOT-LOCATED-IN-THIS-FIRE — same as #9. |

---

## Summary

- **7/8 external identifiers verified PASS** (entries 1, 2, 3, 5, 6, 7, 8)
- **1/8 external identifiers FAIL** (entry 4 — hallucinated `Joshi-Lustri-Topp 2014` attribution; arXiv ID resolves to `Its-Lisovyy-Tykhyy 2014`)
- **2/10 SIARC-internal entries not re-verified** in this fire (entries 9, 10) — superseded in priority by HALT_A1_GAP_CLOSED
- **Acquisition status:** all 7 PASS-tier external identifiers are openly accessible on arXiv. No paywall issues. No acquisition failure.

Per the FIRE-A1 halt-mode decision matrix:
- Anchors (entries 1-2): both PASS → HALT_A1_ANCHOR_RETRACTED does NOT fire
- Entry 4 failure alone (without anchor failure) → would default to CLOSE_WITH_AMENDMENT
- **BUT** Phase B structural-gap audit triggers a stronger halt — see structural_gap_memo.md → **HALT_A1_GAP_CLOSED** overrides the per-entry verdict
