# Zenodo metadata — "An explicit exponential-period representation of the V_quad connection coefficient"

**STATUS: STAGED FOR OPERATOR REVIEW — NOT MINTED.** This file carries the
deposit metadata only. No Zenodo API call, no draft, no version, no DOI has been
created by the agent. Minting is the operator's irreversible manual step
(standing meta-rule: prepare-to-ready-state and STOP).

> **Current-draft caveat (Stage 3.2).** Title, description (abstract), and MSC
> codes are taken from the current V_quad paper draft. They may shift in
> VQUAD-PAPER-CORRECTIONS-001. Re-pin the metadata anchor (Stage 3.3) against any
> title/abstract/MSC change before deposit.

Related identifiers (the DOI cross-reference graph) are a separate deliverable:
see `related-identifiers.md` in this slot. They merge into the final
`metadata.related_identifiers` array at mint.

---

## Core fields (Step 1)

| Field | Value | Note |
|---|---|---|
| Title | An explicit exponential-period representation of the V_quad connection coefficient | current draft, may update at deposit |
| Resource type | Publication → Preprint (`upload_type: publication`, `publication_type: preprint`) | PINNED |
| Creator | Papanokechi | PINNED |
| Creator ORCID | 0009-0000-6192-8273 | PINNED |
| Creator affiliation | **OPERATOR DECISION — see ⚠️ F-AFFIL below** | conflict |
| License | Creative Commons Attribution 4.0 International (`cc-by-4.0`) | PINNED |
| Access right | open | PINNED |
| Version | 1.0.0 | brief value; corpus convention is `1.0` — operator picks |
| Language | eng | PINNED |
| Publication date | *(set by operator at mint — DO NOT hard-code a pre-mint date)* | operator |
| Keywords | 8 tags, listed below | current draft |

> ⚠️ **F-AFFIL — affiliation conflict (operator decides at deposit).**
> The task brief (Stage 3.1) requests affiliation **"Independent Researcher,
> Yokohama, Japan"**. Three authoritative corpus sources say **leave it blank**:
> (1) `zenodo_metadata.template.md` L28 marks affiliation *PINNED — none, byline
> carries ORCID only*; (2) the most-recent live record (Sakai, zenodo 20694841)
> has affiliation `null`; (3) a stored convention notes the older "Independent
> Researcher" affiliation **caused a v1-spec error** on a prior deposit. The
> paste-ready JSON below therefore keeps the creators block ORCID-only (the safe
> corpus default) and records the brief's requested value in
> `_affiliation_decision`. **Operator: confirm blank vs. the brief's value at
> deposit; either choice re-pins the metadata anchor.**

### Keywords (the 8 specified; order preserved)

1. polynomial continued fractions
2. exponential periods
3. Painlevé V
4. Fresán-Jossen exponential motives
5. Borel-Laplace duality
6. conditional transcendence
7. Sakai stratification
8. motivic Galois group

> Reminder (stored convention): the Zenodo "Keywords and subjects" web field has
> **no comma/bulk paste** — each keyword needs its own Enter, or set them in one
> shot via the legacy REST API `metadata.keywords` array.

### MSC 2020 (enter in Zenodo "Subjects", or carry as `_msc` annotation)

| Tier | Codes |
|---|---|
| Primary | 34M55 (Painlevé and other special equations; classification, hierarchies, normal forms) |
| Secondary | 11J81 (Transcendence of complex numbers), 34E20 (Singular perturbations, turning point theory, WKB), 14F40 (de Rham cohomology / algebraic geometry) |
| Tertiary | 33C20 (Generalized hypergeometric series), 37K10 (Completely integrable systems; hierarchies) |

> MSC codes are *current draft* — they may shift in corrections. Zenodo's legacy
> deposition schema has no first-class MSC field; enter them in the web "Subjects"
> control at mint, or leave the `_msc` annotation (stripped by `clean_meta`).

---

## Description (Step 1 — manuscript Abstract VERBATIM + bundle/SIARC addendum)

Abstract rendered word-for-word from the paper `\begin{abstract}` (LaTeX math
mapped faithfully to Unicode: Σ-class glyphs, sub/superscripts, en/em-dashes
preserved). The final three sentences are the Stage-3.1 bundle/SIARC addendum.

> We prove that the connection coefficient C of the V_quad polynomial continued fraction—the rank-one standalone closure on the Sakai surface D₅⁽¹⁾ (Painlevé V)—admits an explicit exponential-period representation C=(|Γ(β)|/2π)∫_γ e^ξ B̂(ξ) dξ=|Γ(β)| K, where B̂ is the Borel transform of the V_quad asymptotic series, holonomic of order 4 with coefficients in the real quadratic field ℚ(√3); γ is an explicit Hankel rapid-decay cycle on (−∞,−2/√3]; and β=−1/(3√3). The identity is verified by three structurally independent methods—differential-equation/operator duality, Borel–Laplace contour deformation, and Stokes-data—agreeing to 46 digits. The order-2 operator annihilating the asymptotic series has differential Galois group SL₂(ℂ) by Kovacic's algorithm. As a by-product, holonomicity of the Borel transform forces a finite resurgent structure. Finally, conditional on the Fresán–Jossen period conjecture for exponential motives and on a stated motivic-comparison hypothesis, C is transcendental over ℚ̄. This record accompanies the VQUAD-PERIODREP reproducibility bundle (verification scripts, certificates, and a byte-reproducible build), which reproduces every numerical claim above, including the 46-digit agreement. The work was produced under the SIARC governance methodology; per-stage provenance and AEAL-level claim ledgers are linked from the bundle's SIARC_PROVENANCE.md. The identity continues the V_quad companion paper (concept DOI 10.5281/zenodo.20455089) within the Sakai Stratification of PCF Transcendence program.

> Operator note: SIARC deposits render the description as HTML at mint (paragraph
> wrapped in `<p>…</p>`; the published record may HTML-entity-encode Greek/
> operators/dashes). The text above is the **canonical source**. Verify draft-side
> with a byte-exact compare; verify published-side with the **normalized** compare
> (strip `<p>`, decode entities). The first sentence is the verbatim manuscript
> Abstract opening; the trailing three sentences are the bundle/SIARC addendum
> (not part of the manuscript Abstract — operator may trim if a pure-Abstract
> description is preferred, which would re-pin the anchor).

---

## Paste-ready JSON (legacy deposition schema, for `_zenodo_uploader.py` / `run_production_draft.py`)

`_`-prefixed keys are operator annotations; the uploader's `clean_meta` step
strips them before the API call. `related_identifiers` is intentionally left as a
pointer — populate it from `related-identifiers.md` at mint.

```json
{
  "metadata": {
    "title": "An explicit exponential-period representation of the V_quad connection coefficient",
    "upload_type": "publication",
    "publication_type": "preprint",
    "creators": [
      {
        "name": "Papanokechi",
        "orcid": "0009-0000-6192-8273"
      }
    ],
    "description": "We prove that the connection coefficient C of the V_quad polynomial continued fraction\u2014the rank-one standalone closure on the Sakai surface D\u2085\u207d\u00b9\u207e (Painlev\u00e9 V)\u2014admits an explicit exponential-period representation C=(|\u0393(\u03b2)|/2\u03c0)\u222b_\u03b3 e^\u03be B\u0302(\u03be) d\u03be=|\u0393(\u03b2)| K, where B\u0302 is the Borel transform of the V_quad asymptotic series, holonomic of order 4 with coefficients in the real quadratic field \u211a(\u221a3); \u03b3 is an explicit Hankel rapid-decay cycle on (\u2212\u221e,\u22122/\u221a3]; and \u03b2=\u22121/(3\u221a3). The identity is verified by three structurally independent methods\u2014differential-equation/operator duality, Borel\u2013Laplace contour deformation, and Stokes-data\u2014agreeing to 46 digits. The order-2 operator annihilating the asymptotic series has differential Galois group SL\u2082(\u2102) by Kovacic's algorithm. As a by-product, holonomicity of the Borel transform forces a finite resurgent structure. Finally, conditional on the Fres\u00e1n\u2013Jossen period conjecture for exponential motives and on a stated motivic-comparison hypothesis, C is transcendental over \u211a\u0304. This record accompanies the VQUAD-PERIODREP reproducibility bundle (verification scripts, certificates, and a byte-reproducible build), which reproduces every numerical claim above, including the 46-digit agreement. The work was produced under the SIARC governance methodology; per-stage provenance and AEAL-level claim ledgers are linked from the bundle's SIARC_PROVENANCE.md. The identity continues the V_quad companion paper (concept DOI 10.5281/zenodo.20455089) within the Sakai Stratification of PCF Transcendence program.",
    "keywords": [
      "polynomial continued fractions",
      "exponential periods",
      "Painlev\u00e9 V",
      "Fres\u00e1n-Jossen exponential motives",
      "Borel-Laplace duality",
      "conditional transcendence",
      "Sakai stratification",
      "motivic Galois group"
    ],
    "license": "cc-by-4.0",
    "access_right": "open",
    "version": "1.0.0",
    "language": "eng",
    "_affiliation_decision": "brief Stage 3.1 requests 'Independent Researcher, Yokohama, Japan'; corpus convention (template PINNED, latest record 20694841 null, prior v1-spec error) is BLANK. Operator decides at deposit; creators block kept ORCID-only as the safe default.",
    "_msc_2020": { "primary": "34M55", "secondary": ["11J81", "34E20", "14F40"], "tertiary": ["33C20", "37K10"] },
    "_related_identifiers_pointer": "see related-identifiers.md — merge into metadata.related_identifiers at mint (12 ids; bundle isSupplementTo is a placeholder)",
    "_publication_date_pointer": "set by operator at mint; do not pre-date",
    "_resource_note": "Research preprint with reproducibility bundle: explicit exponential-period representation C=|\u0393(\u03b2)|K verified by three independent methods to 46 digits; transcendence CONDITIONAL on Fres\u00e1n\u2013Jossen + a motivic-comparison hypothesis. Description trailing 3 sentences are a bundle/SIARC addendum, not manuscript-Abstract text."
  }
}
```

---

## NOT changed
Manuscript content untouched; this is a staging artifact only. No file is minted,
versioned, committed, or sent to any API by filling this template.
