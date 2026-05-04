# Dossier — Milestone Residual Gap Survey (M4 / M7 / M8b / M9)

## Front matter

- **Task ID:** MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9
- **Composed:** 2026-05-04
- **Verdict:** PARTIAL_RECON_DELIVERED — 4 sub-task matrices populated from on-disk
  literature corpus (slots 03 / 06 / 07 / 08 / 13 / 14 / 15 / 16 in
  `tex/submitted/control center/literature/g3b_2026-05-03/`) plus a small set
  of OA web probes. The dossier is reconnaissance only; no closure attempt is
  made for any of M4, M7, M8b, M9.
- **AEAL claim count:** 14 entries appended to this session's `claims.jsonl`.
- **Acquisition success rate (this session):** 0 acquired / 14 probed
  (web-fetch only; no new PDFs deposited; on-disk corpus reused).
- **Runtime profile:** ~45 min web-recon + on-disk verbatim extraction (single
  parallel pass; well under §0 ~3-4 hr budget).
- **Spec discrepancies surfaced:** 2 — (i) §1 anchor paths drifted from spec
  (Sakai slot 13 actual filename `13_sakai_1999_preprint_kyoto99_10.pdf`,
  KNY slot 14 actual `14_kajiwara_noumi_yamada_2017_geometric_aspects.pdf`;
  bridge handoff folders for T1 Phase 2 / T2.5d / T3 named differently from
  spec); (ii) three arXiv identifiers used as illustrative candidates during
  this researcher's web-probe sub-search resolved to unrelated
  physics / CS papers — same pattern as the 031 WITTE-FORRESTER hallucination
  finding. The spec § 5 sub-task C does not itself cite arXiv IDs (it cites
  Mazzocco / BLT / Iwaki by author + year only); the hallucinations came from
  this researcher's own probe attempts and have been recorded in
  `discrepancy_log.json` and dropped from the dossier rows.

---

## §A — M4 Residual (Sub-task A: post-Wasow §X.3 borderline-ansatz literature)

Per §3 schema. One row per candidate P1–P9.

### Row A.P1 — Costin 2008, "Asymptotics and Borel Summability" (CRC, monograph)

| Field | Value |
|---|---|
| Source | Costin, *Asymptotics and Borel Summability*, CRC Press, 2008. ISBN 9781584885078 |
| Acquisition route | On-disk slot 06 (`06_costin_2008_chap5.pdf` SHA-256 `436c6c11…6243289`, 1.4 MB, 258 pp; text-layer present, pypdf-extracted to `06_costin_2008_chap5.txt`, 13550 lines) |
| Text-layer status | OK (verified by Selesct-String pattern match on 12 distinct theorem labels in §4–§5) |
| Theorem(s) extracted | Theorem 4.147 (Borel summability for Gevrey-1 series under Phragmén–Lindelöf-type uniqueness); Theorem 5.11 (analytic structure of Borel transforms `Y_k = B ỹ_k` with explicit singular factorisation `Y₀±(z + lλⱼ) = ±[(±Sⱼ)ˡ (ln z)^{0,1} Y_{lej}(z)]^{(lmⱼ)} + B_{lj}(z)`); Theorem 5.26 (connection / Stokes formula `y = (C ± ½ S₁) e₁ x^{-β₁+1} e^{-xλ₁}(1 + o(1))` along γ±); Theorem 5.45 (transseries representation `y(x) = (L_φ B ỹ₀)(x) + Σ Cᵏ e^{-kx} (L_φ B ỹ_k)(x)` and `C(φ) = C(0+) − ½ Sβ` at φ = 0) |
| Non-resonance hypothesis | Verbatim p. 152 (Theorem 5.11 hypothesis): "for `l ∈ ℕ⁺` and small `z`, … the power of `ln z` is one iff `l β_j ∈ ℤ`"; non-resonance encoded in `k·β + l β_j − 1 ∉ ℤ` (eq. 5.14) |
| Non-degeneracy hypothesis | Verbatim p. 151 (eq. 5.13): `S_j = r_j Γ(β'_j) (A_{1,j})_j(0) = 0` is the explicit non-degeneracy obstruction for the j-th Stokes constant to vanish |
| Borderline-case (Wasow §X.4 sense) treatment | Costin §7.7d (Borel-plane localisation, p. 11187 of TXT) discusses "borderline region" where `(7.36) converges but barely so" — but at rank 1 only; **fractional-rank q ≥ 2 borderline-anormal case is not addressed** (verbatim search of "fractional rank" returns 0 hits in the 13550-line TXT) |
| Fit to SIARC PCF δ_n setting (Y / N / partial) | partial — Costin 2008 ch.5 covers the rank-1 generic case (M4 Phase 2 LIFT-LOWER baseline already absorbed this); the **fractional-rank q ≥ 2 borderline case relevant to PCF δ_n at d ≥ 3 is not present in this monograph** |
| NIA tag if any | none for Costin 2008 itself; the borderline-q≥2 sub-question is a NEGATIVE-FINDING tag inside Costin (search "fractional rank": 0 hits; search "borderline": 9 hits, all rank-1) |

### Row A.P2 — Loday-Richaud 2014, "Divergent Series, Summability and Resurgence II" (Springer LNM 2154)

| Field | Value |
|---|---|
| Source | Loday-Richaud, *Divergent Series, Summability and Resurgence II — Simple and Multiple Summability*, Springer LNM 2154, 2014. DOI 10.1007/978-3-319-29075-1 |
| Acquisition route | NOT_PROBED_THIS_SESSION (Springer LNM expected to hit Rule 1 SpringerLink auth-redirect, consistent with prior 029 / 030 finding for Sakai 2001 SpringerLink probe); operator-side ILL recommended for any future closure attempt |
| Text-layer status | NIA |
| Theorem(s) extracted | NIA |
| Non-resonance hypothesis | NIA |
| Non-degeneracy hypothesis | NIA |
| Borderline-case treatment | NIA |
| Fit | NIA |
| NIA tag | NIA_LNM2154_NOT_PROBED_THIS_SESSION |

### Row A.P3 — Braaksma 1992, "Multisummability of formal power series solutions of nonlinear meromorphic differential equations"

| Field | Value |
|---|---|
| Source | Braaksma, B. L. J., *Annales de l'Institut Fourier* 42(3), pp. 517-540 (1992). DOI 10.5802/aif.1301. NUMDAM URL `https://www.numdam.org/item/AIF_1992__42_3_517_0/` |
| Acquisition route | NUMDAM OA verified accessible (HTTP 200; Abstract + reference list extracted via web fetch; full PDF available at NUMDAM but not downloaded this session per per-session bandwidth discipline) |
| Text-layer status | abstract-only verified verbatim from NUMDAM landing page; full-text NIA (not deposited this session) |
| Theorem(s) extracted | Verbatim from NUMDAM abstract page: "In this paper a proof is given of a theorem of J. Écalle that formal power series solutions of nonlinear meromorphic differential equations are multisummable." |
| Non-resonance hypothesis | NIA (full text not extracted) |
| Non-degeneracy hypothesis | NIA |
| Borderline-case treatment | NIA — but title scope ("nonlinear meromorphic differential equations") covers the right ambient class; reference list cites Hukuhara 1937, Malgrange 1974, Ramis-Sibuya 1989, Sibuya 1990, Turrittin 1955, **Wasow 1976** (Dover reprint) confirming it is in the same Wasow-descendant family relevant to M4 Phase 3. Operator-side full-text deposit recommended for any future closure attempt. |
| Fit | partial-by-title-scope; full theorem statement NIA |
| NIA tag | NIA_BRAAKSMA_FULLTEXT_NOT_DEPOSITED_THIS_SESSION |

### Row A.P4 — Immink 1991/2008 (papers on q-difference / fractional rank)

| Field | Value |
|---|---|
| Source | Immink, G. K., several papers in *Funkcialaj Ekvacioj* / *J. Math. Anal. Appl.* / *Asymp. Anal.* during 1990s–2000s on Gevrey theory and multisummability for q-difference and irregular-rank ODEs |
| Acquisition route | NOT_PROBED_THIS_SESSION (no specific DOI / URL pinned in spec; Funkcialaj Ekvacioj on Project Euclid hits Rule 1 with security-check page on the URL probed; Kobe Math Seminar fallback returned HTTP 404) |
| Text-layer status | NIA |
| Theorem(s) | NIA |
| Non-resonance / non-degeneracy / borderline | NIA |
| Fit | NIA |
| NIA tag | NIA_IMMINK_NOT_PROBED_THIS_SESSION; supplementary tag NIA_FUNKCIALAJ_PROJECTEUCLID_AUTH_PAGE |

### Row A.P5 — Ramis-Sibuya 1996, "A new proof of multisummability of formal power series solutions of ODE"

| Field | Value |
|---|---|
| Source | Ramis, J.-P. and Sibuya, Y., *Funkcialaj Ekvacioj* 39, pp. 139-163 (1996) |
| Acquisition route | Project Euclid landing URL probed (`https://projecteuclid.org/journals/funkcialaj-ekvacioj/volume-39/issue-1/A-new-proof-of-multisummability-of-formal-power-series-solutions/`); response: "Additional security check is required" (Rule-1-class block); Kobe-U OA fallback URL returned HTTP 404 |
| Text-layer status | NIA |
| Theorem(s) | NIA verbatim; the existence of this paper is confirmed by independent reference in the Braaksma 1992 NUMDAM bibliography under different title (Ramis-Sibuya, *Hukuhara domains and fundamental existence and uniqueness theorems for asymptotic solutions of Gevrey type*, Asymp. Analysis 2 (1989), 39-94) — note: 1989 paper not 1996 paper, transcription discrepancy in spec §3 P5; flagged in `discrepancy_log.json` |
| Fit | partial-by-author-and-topic |
| NIA tag | NIA_RAMIS_SIBUYA_PROJECTEUCLID_SECURITY_CHECK |

### Row A.P6 — Sauzin 2015 (RIMS Kôkyûroku Bessatsu B61)

| Field | Value |
|---|---|
| Source | Sauzin, "Resurgent functions and splitting problems", RIMS Kôkyûroku Bessatsu B61 |
| Acquisition route | NOT_PROBED_THIS_SESSION (RIMS Kôkyûroku Bessatsu OA route not pinned in spec) |
| NIA tag | NIA_SAUZIN_NOT_PROBED |

### Row A.P7 — Balser 2000 (Springer LNM 1582)

| Field | Value |
|---|---|
| Source | Balser, *Formal Power Series and Linear Systems of Meromorphic ODE*, Springer LNM 1582, 2000 |
| Acquisition route | NOT_PROBED (Springer LNM expected Rule 1 auth-redirect) |
| NIA tag | NIA_BALSER_NOT_PROBED |

### Row A.P8 — Sternin-Shatalov 1996 (CRC)

| Field | Value |
|---|---|
| Source | Sternin and Shatalov, *Borel-Laplace Transform and Asymptotic Theory* (CRC) |
| Acquisition route | NOT_PROBED (publisher CRC; expected paywall) |
| NIA tag | NIA_STERNIN_SHATALOV_PAYWALL_EXPECTED |

### Row A.P9 — Écalle 1981–1985 trilogy *Les Fonctions Résurgentes*

| Field | Value |
|---|---|
| Source | Écalle, *Les Fonctions Résurgentes*, Tomes I, II (1981) and III (1985), Publ. Math. d'Orsay |
| Acquisition route | NOT_PROBED (Orsay 1981/1985 preprints not on standard OA platforms; operator-side ILL or direct request to author institution recommended) |
| NIA tag | NIA_ECALLE_TRILOGY_ILL_RECOMMENDED |

---

## §B — M7 Residual (Sub-task B: Chowla-Selberg / Γ(1/3) hard-branch)

### Row B.P1 — Chowla-Selberg 1949

| Field | Value |
|---|---|
| Source | Chowla, S. and Selberg, A., "On Epstein's Zeta-function (I)", *Journal für die reine und angewandte Mathematik (Crelle)* 227 (1967), pp. 86-110 — note that the standard citation 1949 in the spec is for the *Proceedings of the National Academy of Sciences* short note (Selberg-Chowla, PNAS 35 (1949) 371-374); the long Crelle paper appeared 1967 |
| Acquisition route | GDZ landing page for Crelle vol. 227 reached (`https://gdz.sub.uni-goettingen.de/id/PPN243919689_0227`); image-only viewer, no text-layer / PDF download in this session |
| Text-layer status | NIA — landing page is image-viewer only |
| Closed-form claim type (Γ(1/3) / Selberg integral / CM point / Other) | per standard reference (not extracted verbatim this session): closed-form evaluation of the Epstein zeta function for binary positive-definite quadratic forms with imaginary-quadratic discriminant, expressing it as a finite product of Γ-values × elementary factors |
| A=6 fit to PCF j=0 stratum | partial — the j=0 stratum is the equianharmonic CM point (lattice ℤ[ω] with ω = e^{2πi/3}); Chowla-Selberg gives `L(s, χ_{−3})` Γ(1/3) closures at this stratum, but does NOT directly state any A=6 PCF asymptotic constant; the connection PCF-A=6 ↔ Γ(1/3)-class would require a SIARC primary derivation, not literature citation |
| Verbatim theorem | NIA (image-only) |
| Bypasses 5-param-ansatz cap (Y / N / unclear) | unclear — the Γ(1/3)-class identity gives an algebraic / closed-form value, but linking it to A=6 in PCF formal-baseline language requires structural argument not present in Chowla-Selberg |
| NIA tag | NIA_CHOWLA_SELBERG_GDZ_IMAGE_ONLY |

### Row B.P2 — Selberg-Chowla 1967 follow-up

| Field | Value |
|---|---|
| Source | Selberg-Chowla, *J. Indian Math. Soc.* (1967) |
| Acquisition route | NOT_PROBED (J. Indian Math. Soc. backfile not on standard OA) |
| NIA tag | NIA_SELBERG_CHOWLA_INDIAN_NOT_PROBED |

### Row B.P3 — Borwein-Zucker 1992

| Field | Value |
|---|---|
| Source | Borwein, J. M. and Zucker, I. J., "Fast evaluation of the gamma function for small rational fractions using complete elliptic integrals of the first kind", *IMA J. Numer. Anal.* 12, pp. 519-526 (1992). DOI 10.1093/imanum/12.4.519 |
| Acquisition route | OUP academic.oup.com URL probed (`https://academic.oup.com/imajna/article-abstract/12/4/519/660193`); HTTP 403; DOI URL redirects to OUP article-lookup (also auth-gated) |
| Text-layer status | NIA |
| Closed-form claim | per standard reference: closed-form fast-converging series for `Γ(p/q)` for `q ∈ {1,2,3,4,6}` using AGM and complete elliptic integrals |
| A=6 fit | partial — gives Γ(1/3) closed-form route but no PCF A=6 statement |
| NIA tag | NIA_BORWEIN_ZUCKER_OUP_PAYWALL |

### Row B.P4 — Borwein-Borwein-Borwein 1989, *Pi and the AGM* (Wiley)

| Field | Value |
|---|---|
| Source | Borwein, J. M., Borwein, P. B., *Pi and the AGM*, Wiley (1987/1998 2nd ed.) — note the spec attributes "Borwein-Borwein-Borwein"; the canonical authorship is two Borweins |
| Acquisition route | NOT_PROBED (Wiley monograph; paywall expected) |
| NIA tag | NIA_BORWEIN_PI_AGM_PAYWALL_EXPECTED |

### Row B.P5–B.P9 — Aldea-Ohno 2018 / Yamamoto / Zudilin / Glaisher 1909 / Watson 1936 / Wan / Conrey / Borwein-Crandall

| Field | Value |
|---|---|
| Status | NOT_PROBED_THIS_SESSION — all of P5–P9 are author-or-year-only references in the spec without a specific DOI / URL; deep-probe deferred to a dedicated lit-hunt prompt |
| NIA tag | NIA_BR_P5_TO_P9_NOT_PROBED |

---

## §C — M8b Residual (Sub-task C: post-foreclosure structural literature)

### Row C.P1 — Costin 2008 ch.5 (alien derivatives + transseries connection)

| Field | Value |
|---|---|
| Source | Costin 2008 (slot 06; same source as Row A.P1) |
| Acquisition route | On-disk |
| Text-layer status | OK |
| Closed-form S_2 claim | Theorem 5.26 gives the **first** Stokes constant `S₁` in the connection formula; the **second** Stokes constant `S₂` would correspond to the second singularity at `2λ₁` in the Borel plane; Costin 2008 §5 / Theorem 5.11 (eq. 5.12) has a multi-singular analytic-structure formula `Y₀±(z + lλⱼ)` with `l ∈ ℕ⁺` covering `l ≥ 2`, but **the closed-form for the corresponding `S²ⱼ`-derived alien amplitude `S₂`** is not given as a single explicit formula — the structure is "the singularities at `lλⱼ` for `l ≥ 2` are derived from the `l = 1` singular data via convolution-product expansion". Verbatim search of "Stokes constant" returns 7 hits, all referencing `S` (1st only) and its decomposition; "second Stokes" returns 0 hits; "S_2" (alien-amplitude sense) returns 0 hits. |
| Connection-coefficient framework | Borel-Écalle resurgence + transseries (multi-instanton expansion) |
| Parameter regime fit to SIARC d=2 PCF dichotomy | partial — Costin 2008 covers nonlinear meromorphic ODE, which the d=2 PCF δ_n recurrence reduces to in formal scaling; but PIII(D_6) specifically is mentioned only in passing and the σ-form / τ-function language is absent |
| Verbatim theorem | Theorem 5.26 statement quoted verbatim in §A.P1 row above |
| Bypasses numerical extraction (Y / N / unclear) | unclear — gives a structural framework in which `S₂` is well-defined as the residue of a higher-fold convolution; but no closed-form rational / algebraic / transcendental evaluation is offered |

### Row C.P2 — BLMP 2024 (slot 08)

| Field | Value |
|---|---|
| Source | Barhoumi, Lisovyy, Miller, Prokhorov, "Asymptotics of Rational Solutions of Painlevé-III" (2024). On-disk slot 08 (`08_barhoumi_lisovyy_miller_prokhorov_2024_pIII_D6.pdf` SHA-256 `96c49cdd…f696bb3`, 2.0 MB, 77 pp; text-layer present, pypdf-extracted to `08_blmp_2024.txt`, 9030 lines). |
| Acquisition route | On-disk (slot 08) |
| Text-layer status | OK |
| Closed-form S_2 claim (Y / N / partial / NIA) | partial — Theorems 1.1 + 1.4 + 1.7 give explicit Riemann-Hilbert-problem characterisations of monodromy data `(α, β, x_1, x_2, x_3)` and Stokes-class parameters `(e_0, e_1, e_2, e_∞, η)` for both PIII(D_8) and PIII(D_6) cases. The monodromy data IS the Stokes-multiplier vector. Verbatim from Theorem 1.4 (line 451 ff.): "Let `u_0` be the solution of (1.1) corresponding to monodromy data `(α, β, x_1, x_2, x_3)` parametrized by generic monodromy parameters `(e_1, e_2)` using formulæ (consistent with (1.13)) `x_1 = e_1² (e_0² e_2² e_∞² (e_1² e_∞² − 1) (e_0² e_1² − 1) (e_0² e_1² − 1))^{−1/2} + …` (eq. 1.17–1.19)". |
| Connection-coefficient framework | RH problem (Riemann-Hilbert) with 2×2 jump matrices |
| Parameter regime fit to SIARC d=2 PCF dichotomy (β_R = 0; Δ_b dichotomy) | unclear — the RH parametrisation is in `(e_0, e_1, e_2, e_∞)`; pinning the SIARC `Δ_b` dichotomy onto an explicit constraint in the RH-parameter space would require a normalisation map (own-derivation; cf. bridge `T25E-VQUAD-PIII-NORM-MAP-CLOSE`); a literature-direct one-line citation does NOT exist in BLMP 2024 for the SIARC dichotomy |
| Verbatim theorem | T 1.4 hypothesis + (1.17)–(1.19) quoted in line 451–520 of `08_blmp_2024.txt`; full ~80-line statement omitted from this dossier for brevity |
| Bypasses numerical extraction | partial — RH analysis gives connection coefficients structurally; but pinning the second alien amplitude `S_2` for a specific normalisation (the SIARC d=2 PCF δ_n one) requires the normalisation map step which is the subject of M6 Phase B and currently INDEX-2 closed (036 verdict, 2026-05-04) |

### Row C.P3 — Mazzocco 2003-2010 (Painlevé connection formulas)

| Field | Value |
|---|---|
| Source | Mazzocco, M., several papers on Painlevé connection coefficients (PVI primarily; PIII cross-references) |
| Acquisition route | NOT_PROBED_DEEPLY_THIS_SESSION (Mazzocco was deprioritised to #3 endorsement reserve 2026-05-04 per spec; this sub-task is literature-only) |
| NIA tag | NIA_MAZZOCCO_NOT_DEEPLY_PROBED |

### Row C.P4 — Bonelli-Lisovyy-Tanzini 2017 / 2024 (τ-functions / gauge theory)

| Field | Value |
|---|---|
| Source | Bonelli, Lisovyy, Tanzini, several arXiv math-ph papers |
| Acquisition route | NOT_VERIFIED (general references known to exist; no specific arXiv ID stated in spec; this researcher's attempt to probe arXiv ID 2407.21184 / 2305.17839 / 1612.08719 / 1806.08398 returned **unrelated physics / CS papers** — pre-resolution gate per copilot-instructions Bibliographic ID Pre-Verification rule failed; same hallucination pattern as 031 WITTE-FORRESTER finding; recorded in `discrepancy_log.json`) |
| NIA tag | NIA_BLT_NO_VERIFIED_ID_THIS_SESSION |

### Row C.P5 — Iwaki-Saenz 2016 onward

| Field | Value |
|---|---|
| Source | Iwaki et al., quantum-curve / wall-crossing / resurgent-Painlevé arXiv math.CA + math-ph series |
| Acquisition route | NOT_PROBED_THIS_SESSION |
| NIA tag | NIA_IWAKI_NOT_PROBED |

### Row C.P6 — Iwaki et al. 2020-2024 (resurgent τ-function structure)

| Field | Value |
|---|---|
| Source | Iwaki et al. 2020-2024 series |
| Acquisition route | NOT_PROBED |
| NIA tag | NIA_IWAKI_2020_2024_NOT_PROBED |

### Row C.P7 — Clavier-Cournod 2024

| Field | Value |
|---|---|
| Source | Clavier-Cournod 2024 (resurgent second-Stokes-multiplier extraction; spec-by-author-and-year only) |
| Acquisition route | NOT_PROBED |
| NIA tag | NIA_CLAVIER_COURNOD_NOT_PROBED |

### Row C.P8 — Lisovyy-Roussillon 2017

| Field | Value |
|---|---|
| Source | Lisovyy, Roussillon, "On the connection problem for Painlevé III" (cited in the spec as "arXiv 1612.xxxxx" — partial ID); verified arXiv listing search via `https://arxiv.org/a/lisovyy_o_1` returned HTTP 404 (canonical author-page URL pattern not active) |
| Acquisition route | NOT_PROBED_DEEPLY_THIS_SESSION (canonical arXiv ID not pinned in spec, listing-search blocked) |
| NIA tag | NIA_LISOVYY_ROUSSILLON_NO_VERIFIED_ID |

### Row C.P9 — Jimbo-Miwa-Ueno 1981 + descendants

| Field | Value |
|---|---|
| Source | Jimbo, Miwa, Ueno, *Physica D* 2 (1981) 306-352 (general theory of monodromy preserving deformation) and Jimbo-Miwa, *Physica D* 2 (1981) 407-448 (Painlevé equations II). Cited at slot [12] of Sakai 1999 reference list (verified verbatim in slot 13 on-disk text). |
| Acquisition route | NOT_PROBED_THIS_SESSION (Physica D 1981 backfile expected to be paywalled at Elsevier; operator-side ILL recommended for any future closure attempt) |
| Coordinate-with note | Spec states "Slot 24 prompt slated; coordinate to avoid duplication" — this dossier does not duplicate slot 24's scope and only confirms the existence of the JMU-1981 reference in the on-disk Sakai 1999 bibliography (line at slot [12] in `13_sakai_1999_preprint_kyoto99_10.txt` references section). |
| NIA tag | NIA_JMU_1981_PHYSICA_D_PAYWALL_EXPECTED |

---

## §D — M9 Meta-Precedent (Sub-task D: research-program announcement protocol)

**STARTING-CONTEXT NOTE per spec §6 + AMENDMENT 1 / Q38.2:** This sub-task is
written assuming M6 closed at INDEX-2 final per the 036 SIARC-OKAMOTO-1987-SEC3-SCAN
verdict (2026-05-04) — cokernel `Z/2 = P^∨(B_2) / Q^∨(B_2) = centre Spin(5) = Sp(2)`.
The M9 partiality profile cross-cut in row R4 below treats M6 as ✅ CLOSED, not partial.

### Row R1 — Langlands 1967 letter to Weil

| Field | Value |
|---|---|
| Precedent | Langlands' letter to André Weil announcing what became known as the Langlands conjectures / functoriality |
| Year | January 1967 (handwritten; typed shortly after, January 1967, dated by Harish-Chandra cover note 16 January 1967) |
| Venue | Private letter (subsequently typed for circulation; later published 2015 in *Emil Artin and beyond---Class field theory and L-functions*, pp. 165-173) |
| Format | 17-page handwritten letter; private circulation |
| Partiality at announcement | 0 closed milestones / many partial / many open — verbatim from IAS author commentary (`https://publications.ias.edu/rpl/paper/43`): "Although the notion of functoriality had been introduced in the original letter to Weil, **there were few arguments apart from aesthetic ones to justify it.** So it was urgent to make a more cogent case." (RIDLE: aesthetic-justification-only at announcement time) |
| Caveat-framing (explicit / implicit / none) | implicit — letter did not present formal caveat catalogue; subsequent author-commentary surfaces the rough state. Verbatim from same IAS page: "The first letter was originally intended as a response to a question of Weil, …, but it began to take on a different shape as the possibility for verifying some simple consequences of an earlier letter, on what is now referred to as functoriality, presented itself." |
| Verbatim excerpt (≤ 200 words) | (above two passages, 91 words combined) |
| Cross-cut to SIARC M9 partiality profile | partial-fit — Langlands announced a research program at near-zero rigorous-confirmation level (aesthetic justification only); SIARC M9 profile is at the OPPOSITE end of the spectrum (six closed milestones M1/M2/M3/M5/M6/M8 + one numerical-foreclosure M8b + one partial-formal M4 + one soft-branch M7); a Langlands-mode announcement would be an over-aggressive precedent for SIARC M9 |

### Row R2 — Birch-Swinnerton-Dyer 1965 (BSD conjecture)

| Field | Value |
|---|---|
| Precedent | Birch and Swinnerton-Dyer, "Notes on elliptic curves II", *Crelle* 218 (1965) |
| Year | 1965 |
| Venue | Refereed journal (Crelle / J. reine angew. Math.) |
| Format | research article ~70 pp |
| Partiality | numerical-evidence-only at announcement; analytic-rank ↔ algebraic-rank statement formulated as conjecture |
| Caveat-framing | explicit (in the text — formulated as conjecture; numerical tables presented) |
| Verbatim excerpt | NIA — GDZ landing page for vol. 218 reached but image-only viewer; verbatim text not extracted this session |
| Cross-cut to SIARC M9 | partial-fit — single-conjecture announcement vs SIARC M9 multi-milestone; not the same announcement type |
| NIA tag | NIA_BSD_GDZ_IMAGE_ONLY |

### Row R3 — Iwasawa 1969 (main conjecture for cyclotomic fields)

| Field | Value |
|---|---|
| Precedent | Iwasawa, original announcement of the main conjecture, *Sûgaku* 16 (1969) and follow-up papers |
| Acquisition route | NOT_PROBED_THIS_SESSION (Sûgaku 1969 backfile not on common OA; operator-side ILL recommended) |
| NIA tag | NIA_IWASAWA_NOT_PROBED |

### Row R4 — Painlevé 1900 / Gambier 1910 (Painlevé classification origin)

| Field | Value |
|---|---|
| Precedent | Painlevé, *Acta Math.* 25 (1900) (irreducibility paper); Gambier, *Acta Math.* 33 (1910) (follow-up) |
| Year | 1900 / 1910 |
| Venue | Acta Mathematica |
| Format | research articles |
| Partiality | the Painlevé classification was announced as a multi-equation list with the property of "no movable critical points"; the irreducibility / transcendence properties of the six equations were OPEN at the announcement time and remained open for decades |
| Caveat-framing | implicit / classical-style |
| Verbatim excerpt | NOT_EXTRACTED_THIS_SESSION (Acta Math 25 / 33 OA via DigiZeitschriften / Mittag-Leffler archive expected, but not probed this session) |
| Cross-cut to SIARC M9 | strong-fit — the Painlevé program announced a structural classification with multiple OPEN sub-questions; structurally analogous to SIARC M9 announcing a multi-milestone program with one partial sub-target (M4) and one numerical foreclosure (M8b) |
| NIA tag | NIA_PAINLEVE_GAMBIER_ACTA_NOT_PROBED |

### Row R5 — Sakai 2001 (rational-surface Painlevé classification announcement)

| Field | Value |
|---|---|
| Precedent | Sakai, "Rational surfaces associated with affine root systems and geometry of the Painlevé equations", *Comm. Math. Phys.* 220 (2001) — based on the 1999 Kyoto preprint |
| Acquisition route | On-disk slot 13 (1999 preprint version, `13_sakai_1999_preprint_kyoto99_10.pdf` SHA-256 `ec1bbda3…aaf49ed6`, 514 KB; text-layer present, pypdf-extracted to `13_sakai_1999_preprint_kyoto99_10.txt`, ~3850 lines); SpringerLink published-2001 version paywalled (consistent with prior 029 / 030 finding) |
| Year | 1999 preprint / 2001 published |
| Venue | Kyoto Math Department preprint series → Comm. Math. Phys. |
| Format | research article ~58 pp |
| Partiality | classification framework presented as complete (8-fold surface-type list); discrete-Painlevé connection laid out programmatically; some sub-questions deferred to follow-up |
| Caveat-framing | explicit (Section structure laid out in introduction; sub-sections labelled as separate programs) |
| Verbatim excerpt (≤ 200 words) | From section 1 / introduction (line 3158–3210 of slot-13 TXT): "In Section 2 we motivate our construction on the example of a q-analog of the sixth Painlevé equation. … From the next Section 3, we forget about the differential/difference equations for a while and concentrate on surface theory. … In Section 4, we classify the surfaces and the anti-canonical divisors which satisfy our conditions. … In Section 7 we construct discrete Painlevé equations in terms of the Cremona action. We obtain the Painlevé differential equations by degenerating surfaces. We obtain, in particular, an 'elliptic' difference equation, which seems to be the most generic one (see § 7; 4)." (108 words) |
| Cross-cut to SIARC M9 partiality profile | strong-fit — Sakai announces a multi-component classification with explicit sub-section partition; SIARC M9 with M1/M2/M3/M5/M6/M8 ✅ + M4 partial + M7 soft + M8b numerically foreclosed has structurally similar "mostly-closed-with-explicit-residuals" character |

### Row R6 — Conte-Musette 2008/2020 monograph framing

| Field | Value |
|---|---|
| Precedent | Conte, Musette, *The Painlevé Handbook* (Springer, 2008; 2nd ed. 2020) — meta-framing of the Painlevé-test program as a coherent research program |
| Acquisition route | SpringerLink paywall (consistent with bridge prompt 030 CONTE-MUSETTE-CH7-FINAL-ACQUISITION-PROBE which also confirmed paywall on the same source) |
| NIA tag | NIA_CONTE_MUSETTE_MONOGRAPH_PAYWALL_PER_PROMPT_030 |

### Row R7 — Etingof-Schiffmann (variable years 2000s-2010s)

| Field | Value |
|---|---|
| Precedent | Etingof-Schiffmann program announcements on integrable systems |
| Acquisition route | NOT_PROBED_THIS_SESSION (no specific arXiv ID in spec) |
| NIA tag | NIA_ETINGOF_SCHIFFMANN_NOT_PROBED |

### Row R8 — Wiles 1995 / Taylor-Wiles 1995

| Field | Value |
|---|---|
| Precedent | Wiles, "Modular elliptic curves and Fermat's Last Theorem", *Ann. Math.* 141 (1995); Taylor-Wiles, "Ring-theoretic properties of certain Hecke algebras", *Ann. Math.* 141 (1995) |
| Year | 1995 |
| Venue | Annals of Mathematics |
| Format | full proof articles, NOT announcement-style |
| Partiality | many-closed-modular-results + one-final-theorem; a definitive-closure-paper rather than a research-program-announcement; **does NOT match the M9 announcement-format question**; included here only for completeness |
| Caveat-framing | explicit gap-and-fix structure (the original 1993 announcement, then the Taylor-Wiles 1995 fix, then the joint 1995 publication) |
| Cross-cut to SIARC M9 | weak-fit — proof-paper type, not announcement-paper type |

---

## §E — Cross-cut synthesizer-input matrix

Per §7 — compact summary line per milestone. **NO ranking, NO recommendation,
NO scheduling proposal.** Synthesizer territory.

| Milestone | What literature exists (positive findings, with row references) | What does not exist / is paywalled / is image-only / is not yet probed (negative + NIA findings) |
|---|---|---|
| **M4** (post-Wasow §X.3 borderline-anormal at fractional rank q ≥ 2) | Costin 2008 ch.5 (rank-1 baseline; theorem 5.11 / 5.26 / 5.45 explicit, on-disk slot 06); Braaksma 1992 NUMDAM (multisummability of nonlinear meromorphic ODE; full text exists at NUMDAM but not deposited this session) | NIA: Loday-Richaud 2014 (Springer paywall expected); Ramis-Sibuya Project Euclid security-check; Immink (no specific URL); Sauzin RIMS (not probed); Balser LNM 1582 (paywall expected); Sternin-Shatalov (CRC paywall); Écalle trilogy (Orsay 1981/1985 ILL-only). **The fractional-rank q ≥ 2 borderline-anormal case is not present in Costin 2008 ch.5** (verbatim search "fractional rank": 0 hits) — the gap is substantive, not just unprobed. |
| **M7** (Γ(1/3) hard-branch closure at j=0 stratum) | Chowla-Selberg 1949 / 1967 known-to-exist (GDZ image-only); Borwein-Zucker 1992 known-to-exist (OUP paywall); standard references give Γ(1/3) closed-form *evaluations* but not PCF-A=6 *identifications* | No literature anchor found in this session that bridges PCF formal-baseline-A to Γ(1/3) closure directly. The 5-param-ansatz cap that gates 006 (T2.5d AMBIGUOUS_AT_DPS8000 verdict 2026-05-02) is a numerical-method limit; bypassing it requires either (a) literature anchor connecting CM-point Γ-evaluation to PCF δ_n directly (not found this session) or (b) SIARC primary derivation. NIA on B.P5–B.P9 deeply. |
| **M8b** (Stokes-multiplier S_2 structural closure post-numerical-foreclosure) | Costin 2008 ch.5 (Theorems 5.11 / 5.26 / 5.45 cover rank-1 alien-amplitude structure in transseries language); BLMP 2024 slot 08 (Theorems 1.1 / 1.4 / 1.7 give Riemann-Hilbert characterisation of monodromy / Stokes data for PIII(D_8) and PIII(D_6)) | No closed-form S_2 alien-amplitude formula in either Costin or BLMP for the SIARC d=2 PCF dichotomy specifically (β_R = 0 universal at d=2; Δ_b dichotomy). Spec §5 P3–P9 references (Mazzocco / BLT / Iwaki / Clavier-Cournod / Lisovyy-Roussillon) NOT verified by deep probe this session; this researcher's own arXiv-ID guesses returned hallucinated unrelated papers (recorded in `discrepancy_log.json`). |
| **M9** (research-program announcement protocol; M6 ✅ INDEX-2 closed per 036) | Langlands 1967 letter (IAS verbatim author-commentary; aesthetic-justification-only at announcement time); Sakai 1999 / 2001 (on-disk slot 13; multi-component classification with explicit sub-section partition — strong-fit precedent); Painlevé 1900 / Gambier 1910 (strong-fit precedent by structural analogy; Acta Math NIA-not-probed) | NIA: BSD 1965 (GDZ image-only); Iwasawa 1969 (Sûgaku ILL); Conte-Musette monograph (Springer paywall per prompt 030); Etingof-Schiffmann (no specific URL). Wiles 1995 / Taylor-Wiles 1995 are **proof-papers**, not announcement-papers — does NOT match the M9 announcement-format question. |

---

## §F — Acquisition appendix

| Filename | SHA-256 | Size | Slot | Text-layer status |
|---|---|---|---|---|
| 03_birkhoff_trjitzinsky_1933_acta60.pdf | dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6 | 3411000 B | 03 | OK (pre-existing) |
| 04_wasow_1965_dover.pdf | f59d6835db58d2de59eab843b881b97106eee6c66e56bfce43de5788bbbaa5fd | 5557950 B | 04 | image-only-pypdf-detected (this dossier does not re-attempt OCR per spec §2 / prompt 019 owns scope) |
| 06_costin_2008_chap5.pdf | 436c6c115149052634b103a2ed3b460680ad38cd161897794d5eb1f2f6243289 | 1402505 B | 06 | OK; pypdf TXT 13550 lines; new TXT side-car `06_costin_2008_chap5.txt` written this session |
| 07_okamoto_1987_painleve_III_FE30.pdf | 65294fbca97e3ce1db0ea193dcd3048d9a2942db2ae6d435c9bdfacc2b78a43f | 6075525 B | 07 | OK (pre-existing TXT) |
| 08_barhoumi_lisovyy_miller_prokhorov_2024_pIII_D6.pdf | 96c49cdd51b6c2a395ccd6cc3cb66bffeb623643b1a2374db3f203760f696bb3 | 2018889 B | 08 | OK; pypdf TXT 9030 lines; new TXT side-car `08_blmp_2024.txt` written this session |
| 13_sakai_1999_preprint_kyoto99_10.pdf | ec1bbda3b77634e6def2a784d04947a0c9631bfade48c72aa0767b22aaf49ed6 | 526933 B | 13 | OK (pre-existing TXT) |

No new PDFs acquired this session — dossier is reconnaissance-of-existing-corpus
plus a small number of OA-landing-page web probes.

---

## §G — AEAL claims

See `claims.jsonl` (14 entries appended this session).
