# Bundle Configuration Matrix [BUNDLE-B1..B5] — 077

**Session:** T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077
**Compiled:** 2026-05-07
**Scope:** Phase C inventory of the 5 bundle configurations enumerated
in spec §3. Per HALT_077_BUNDLE_SELECTION_OVERREACH, no bundle is
ranked, recommended, or argued against. Each row is an inventory
tag, not a verdict.

---

## C.0 — 6×6 cross-reference matrix (all records)

Boolean matrix; row "cites" column. ✓ = explicit cite/cross-link
present in source per profiles P1–P6 §B.3; — = no explicit
cross-link or self-row.

| cites \\ cited by | P1 PCF-1 | P2 PCF-2 | P3 CT | P4 D2-NOTE | P5 T2B | P6 umbrella |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| P1 PCF-1 | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| P2 PCF-2 | ✓ | — | ✓ | ✓ |   | ✓ |
| P3 CT | ✓ | ✓ | — | ✓ |   | ✓ |
| P4 D2-NOTE | ✓ | ✓ | ✓ | — |   | ✓ |
| P5 T2B | ✓ |   |   |   | — | ✓ |
| P6 umbrella | ✓ | ✓ | ✓ | ✓ | ✓ | — |

Density: 19/30 off-diagonal cells = ✓; 11/30 = blank. P5 T2B is
the most loosely coupled (5 in-edges, 2 out-edges); P6 umbrella
is most tightly coupled (5 in-edges, 5 out-edges, by design as
the program statement).

---

## [BUNDLE-B1] — PCF-stratification monograph

**Spec narrative spine:** "transcendence stratification of polynomial continued fractions"

| Dim | Value |
|---|---|
| C.1 Composition | PCF-1 v1.3 + PCF-2 v1.3 + T2B v3.0 |
| C.2 Estimated total page count | (16 + 22 + 8) × consolidation-factor; sum = 46 pp; consolidation-factor estimate 0.80–0.90 (intro/notation/refs merge); consolidated estimate ~37–41 pp |
| C.3 Primary arXiv category | `math.NT` (P1 + P2 primary; P5 cross-list math.NT; spine-weighted majority math.NT) |
| C.4 Candidate journals (3-5; length-tier compatibility note) | (a) Constructive Approximation (Springer; standard length tier 30–60 pp typeset, MEDIUM-fit); (b) International Mathematics Research Notices IMRN (Oxford UP; standard 25–40 pp typeset, MEDIUM-fit); (c) Journal of Number Theory (Elsevier; flexible length, MEDIUM-fit); (d) Acta Arithmetica (Polish Academy diamond OA; standard 20–40 pp, MEDIUM-fit, history caveat: P13 Ratio Universality desk-rejected from Acta Arithmetica 2026-05-04 per CMB.txt L30); (e) Journal de Théorie des Nombres de Bordeaux (centre-mersenne; flexible, history caveat: P11 hard-rejected at JTNB 2026-05-06 per CMB.txt L25) |
| C.5 Endorsement consolidation | math.NT primary endorsement (single Tier-1 candidate covers all three records: Zudilin per portfolio_inventory.md L31 "single math.NT endorsement also covers PCF-2 v1.3"); 1 distinct endorsement category required |
| C.6 AEAL composability tag | NEEDS-REWEAVE — three independent claims.jsonl ladders (PCF-1 30-family Δ-dichotomy at dps 220; PCF-2 Conjectures B_3(i)–(iv) + B4 at d∈{3,4} 110/110; T2B Theorem 1 + 2 + 3 + Completeness Conjecture). All three share the Δ-discriminant axis but at different degrees; reweave requires unifying notation (T2B uses (a₂, b₁) coefficients; PCF-1 uses (α, β, γ); PCF-2 uses (α₃, α₂, α₁, α₀)) |
| C.7 Workflow-lift tag | MEDIUM — no new theorems required; existing 3 record sources combine; bibliography union under T2B + PCF-1 + PCF-2 already overlaps (per portfolio cross-ref matrix); v1.0 Zenodo records remain immutable, B1 becomes a new monograph submission |

---

## [BUNDLE-B2] — Asymptotic-channels paper

**Spec narrative spine:** "asymptotic channels and the D2 formal-analytic separation"

| Dim | Value |
|---|---|
| C.1 Composition | CT v1.4 (post-G17-close) + D2-NOTE v2.1 |
| C.2 Estimated total page count | (~21 v1.4 + 9 D2-NOTE) × consolidation-factor; sum = 30 pp; consolidation-factor 0.80–0.85 (Newton-polygon proof material in D2-NOTE §3 already implicitly present in CT v1.3 §4); consolidated estimate ~25–27 pp |
| C.3 Primary arXiv category | `math-ph` (P3 primary math-ph; P4 primary math.CA crosslists math-ph; spine-weighted majority math-ph or math.CA) |
| C.4 Candidate journals (3-5) | (a) Asymptotic Analysis (IOS Press; ~30 pp typical, GOOD-fit per spec §0 "D2-NOTE v2.1 → Asymptotic Analysis" anchor); (b) Communications in Mathematical Physics (Springer; flexible, math-ph primary, MEDIUM-to-HIGH-fit); (c) Journal of Differential Equations (Elsevier; flexible, JDE history note: P10 Self-Adjoint ODEs Under review at JDE per CMB.txt L24, MEDIUM-fit); (d) Letters in Mathematical Physics (Springer; short-paper format, MEDIUM-fit); (e) Nonlinearity (IOP; flexible, history note: P08 Painlevé/V_quad Under review at Nonlinearity per CMB.txt L22, MEDIUM-fit) |
| C.5 Endorsement consolidation | math-ph primary endorsement (Mazzocco H per portfolio_inventory.md L42 + Garoufalidis H math.NT cross+resurgence cite); 1 distinct endorsement category math-ph; cross-list math.CA + math.NT requires no additional endorser per inventory L23 cross-listing note |
| C.6 AEAL composability tag | CLEAN — D2-NOTE v2.1 explicitly closes the Borel-summability layer for CT v1.3's xi0 conjecture (per D2-NOTE file header L18-21 "Birkhoff–Trjitzinsky 1933 §§4-6 cited as the Borel-summability layer"); the two records share the ξ_0 = d/β_d^{1/d} identity as central object; D2-NOTE proves d=2; CT v1.3 + D2-NOTE jointly verify d=4; both forward d=3 to `op:xi0-d3-direct`. CT v1.4 in-flight may further consolidate (G17 layer-separation per 2026-05-04 G17-LAYER-SEPARATION-LIT-ANCHOR session) |
| C.7 Workflow-lift tag | LOW-to-MEDIUM — CT v1.4 in-flight at `sessions/2026-05-03/CT-V14-NARRATIVE-DRAFT/` requires G17-close gate per spec §3.5; if G17 closes, B2 becomes IMMEDIATE; otherwise GATED-ON-G17 |

---

## [BUNDLE-B3] — Trans-stratum focus

**Spec narrative spine:** "Trans-stratum behavior in polynomial continued fractions"

| Dim | Value |
|---|---|
| C.1 Composition | PCF-2 v1.3 + T2B v3.0 |
| C.2 Estimated total page count | (22 + 8) × consolidation-factor; sum = 30 pp; consolidation-factor 0.85–0.90 (T2B's d=2 Trans-stratum extends to PCF-2's d=3 program-statement open conjectures); consolidated estimate ~25–27 pp |
| C.3 Primary arXiv category | `math.NT` (both records primary or cross math.NT; spine-weighted majority math.NT) |
| C.4 Candidate journals (3-5) | (a) Constructive Approximation (Springer; same MEDIUM-fit window as B1); (b) Acta Arithmetica (diamond OA, history caveat per B1 row); (c) Journal of Number Theory (Elsevier; flexible); (d) Annales de l'Institut Fourier (centre-mersenne diamond OA; flexible 30–60 pp); (e) Indagationes Mathematicae (Elsevier; history caveat: P-Rigidity Submitted INDAG-D-26-00112 per CMB.txt L33) |
| C.5 Endorsement consolidation | math.NT primary; same Zudilin/Garoufalidis Tier-1 H ratings as B1 minus PCF-1; 1 distinct category required |
| C.6 AEAL composability tag | CLEAN — T2B v3.0 d=2 Trans-stratum is the d=2 base case of PCF-2 v1.3's d=3 cubic Trans-stratum conjecture; T2B Completeness Conjecture and PCF-2 Conjecture B_3(i)–(iv) are degree-extension siblings on shared Δ-discriminant axis |
| C.7 Workflow-lift tag | LOW — both records are immutable Zenodo deposits; B3 is a focused 2-record monograph; bibliography union ~80% overlap |

---

## [BUNDLE-B4] — SIARC research-monograph

**Spec narrative spine:** "spectral and asymptotic structure of polynomial continued fractions: a unified framework"

| Dim | Value |
|---|---|
| C.1 Composition | umbrella v2.0 + PCF-1 v1.3 + PCF-2 v1.3 + CT v1.4 + D2-NOTE v2.1 + T2B v3.0 (all six) |
| C.2 Estimated total page count | (12 + 16 + 22 + 21 + 9 + 8) × consolidation-factor; sum = 88 pp; consolidation-factor 0.65–0.75 (umbrella's program-statement abstract becomes monograph introduction; cross-references collapse; bibliography union); consolidated estimate ~57–66 pp |
| C.3 Primary arXiv category | `math.NT` plus `math-ph` cross-list mandatory (3 of 6 records primary math.NT [P1, P2, P5 cross]; 2 of 6 primary math-ph or math.CA [P3, P4]; 1 of 6 primary math.HO [P6]); spine-weighted majority math.NT with math-ph + math.CA + math.HO cross-lists |
| C.4 Candidate journals (3-5) | (a) Memoirs of the AMS (long-form monograph 100–200 pp; LENGTH-FIT YES, prestige tier high); (b) Astérisque (SMF; long-form 100–300 pp; LENGTH-FIT YES); (c) Memoirs of the EMS (EMS Press diamond OA; long-form 80–150 pp; LENGTH-FIT YES); (d) Annales de l'Institut Fourier (centre-mersenne diamond OA; up to 60–80 pp typical); (e) Springer Lecture Notes in Mathematics (book series; LENGTH-FIT YES) |
| C.5 Endorsement consolidation | math.NT + math-ph primary plus math.CA cross + math.HO frame; 2 distinct endorsement categories required (math.NT via Zudilin + math-ph via Mazzocco); umbrella v2.0 cross-listing covers math.HO frame per portfolio inventory L38 "M (math.NT/math.GT/math.CA breadth)" |
| C.6 AEAL composability tag | NEEDS-REWEAVE — six independent ladders + umbrella's program-statement framing; substantial reweave to unify (a) Δ-discriminant notation across degrees, (b) Stokes-exponent vs ξ_0-Borel-radius vs Petersson-modular-discriminant axes, (c) Trans-stratum (d=2 T2B closed-form vs d=3 PCF-2 cubic-modular open vs general-d B4) |
| C.7 Workflow-lift tag | VERY-HIGH — full monograph rewrite + cross-record consistency audit + new bibliography union + new introduction + new conclusion; all 6 v1.0 Zenodo records remain immutable, B4 becomes new artefact |

---

## [BUNDLE-B5] — Status quo

**Spec narrative spine:** "each paper to its own venue (no bundling)"

| Dim | Value |
|---|---|
| C.1 Composition | 6 standalone records, each pinned to its current Zenodo DOI |
| C.2 Estimated total page count | 12 + 16 + 22 + 21 (CT v1.4 in-flight) or 17 (CT v1.3) + 9 + 8 = 84 (v1.4) or 80 (v1.3) pp aggregate; per-record page counts unchanged |
| C.3 Primary arXiv category | per-record: math.HO (P6), math.NT (P1, P2), math-ph (P3), math.CA (P4), math.HO (P5); 5 distinct primary-category combinations |
| C.4 Candidate journals (3-5 per record) | per-record stack (no bundle aggregation): P1 → math.NT venues per B1 row; P2 → math.NT or math-ph venues per B1 row; P3 → math-ph venues per B2 row; P4 → math.CA or Asymptotic Analysis per B2 row; P5 → math.NT or math.HO per B3 row; P6 → math.HO or `expositional` venues |
| C.5 Endorsement consolidation | 5 distinct endorsement categories required across the 6 records (math.HO frame for P6 + P5; math.NT for P1 + P2; math-ph for P3; math.CA for P4); per portfolio_inventory.md L23 cross-listing note, single math.NT endorsement covers P1 + P2 simultaneously, single math-ph endorsement covers P3 + cross-list of P2 |
| C.6 AEAL composability tag | CLEAN (each record independently composable; no inter-record consistency demand) |
| C.7 Workflow-lift tag | LOW — each record already on Zenodo; arXiv-mirror dispatch follows ARXIV-MIRROR-RUNBOOK 002 / 034 / 037 / 050 chain per portfolio inventory L218 |

---

## C.8 — Bundle composition coverage table

| Record | B1 | B2 | B3 | B4 | B5 |
|---|:-:|:-:|:-:|:-:|:-:|
| PCF-1 v1.3 | ✓ |   |   | ✓ | ✓ |
| PCF-2 v1.3 | ✓ |   | ✓ | ✓ | ✓ |
| CT v1.3 / v1.4 |   | ✓ |   | ✓ | ✓ |
| D2-NOTE v2.1 |   | ✓ |   | ✓ | ✓ |
| T2B v3.0 | ✓ |   | ✓ | ✓ | ✓ |
| umbrella v2.0 |   |   |   | ✓ | ✓ |

Per-bundle record-count: B1=3, B2=2, B3=2, B4=6, B5=6 (each as standalone).

---

## C.9 — Bundle-formation observations (inventory only)

[BUNDLE-OBS-1] B1 ∪ B2 covers 5 of 6 records (P1, P2, P3, P4, P5);
umbrella v2.0 (P6) is the residual. P6's program-statement
content overlaps with both B1 and B2 introductions.

[BUNDLE-OBS-2] B1 + B3 share PCF-2 v1.3 (P2) and T2B v3.0 (P5).
Mutual coverage requires a tie-break: B1 absorbs P2 + P5, OR
B3 absorbs P2 + P5; cannot both. Per HALT_077_BUNDLE_SELECTION_OVERREACH,
the tie-break is operator/synth scope.

[BUNDLE-OBS-3] B4 absorbs every record but is sized at the
monograph length tier (Memoirs of the AMS / Astérisque / EMS
Memoirs / Springer LNM) rather than the standard journal-article
tier of B1/B2/B3.

[BUNDLE-OBS-4] B5 (status quo) is structurally compatible with
any subset-bundling strategy: a partial bundle B1 may co-exist
with standalone-arXiv-mirror dispatch of P3/P4/P6 under B5.

[BUNDLE-OBS-5] CT v1.3 vs CT v1.4 distinction: B2 spec narrative
references "CT v1.4 (post-G17-close)". If G17-close is not landed
by W21 LANE-1 fire, B2 component reduces to CT v1.3 (canonical
Zenodo-published; SHA `59C5352795F8D63D`). In-flight CT v1.4
adds the G17 layer-separation narrative but is not yet Zenodo-deposited.

---

End of bundle configuration matrix.
