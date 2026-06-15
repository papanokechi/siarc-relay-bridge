# Metadata prepared — VQUAD-ZENODO-PREP-001 (Stage 3)

**Verdict: metadata drafted and JSON-validated. All fields populated; two flagged
operator decisions (affiliation, addendum scope). NOT minted.**

Deliverable: `zenodo_metadata.md` (this slot) — mirrors the canonical
`zenodo_metadata.template.md` and the Sakai worked instance.

## Fields confirmed

| Field | Value | Status |
|---|---|---|
| Title | An explicit exponential-period representation of the V_quad connection coefficient | from paper `\title{}` L43-44; current draft |
| Resource type | Publication → Preprint | PINNED |
| Creator | Papanokechi | PINNED |
| ORCID | 0009-0000-6192-8273 | PINNED |
| Affiliation | brief: "Independent Researcher, Yokohama, Japan"; default kept BLANK | ⚠️ F-AFFIL — operator decides |
| License | cc-by-4.0 | PINNED |
| Access | open | PINNED |
| Version | 1.0.0 | brief value (corpus convention `1.0`) |
| Language | eng | PINNED |
| Publication date | set at mint | operator |
| Keywords | 8 (verbatim from brief, order preserved) | current draft |
| MSC 2020 | primary 34M55; secondary 11J81/34E20/14F40; tertiary 33C20/37K10 | current draft; enter in Zenodo "Subjects" |
| Description | abstract VERBATIM (1539 chars rendered) + 3-sentence bundle/SIARC addendum | current draft |

## Description provenance

* Sentences 1–6 (through "…C is transcendental over ℚ̄.") are the paper's
  `\begin{abstract}` (L50–64), LaTeX math rendered faithfully to Unicode:
  macros expanded (`\Vquad`→V_quad, `\Bhat`→B̂, `\Qsqrt`→ℚ(√3), `\Qbar`→ℚ̄,
  `\SL_2(\mathbb C)`→SL₂(ℂ)), `---`→em-dash, `--`→en-dash, all grade/branch
  tokens preserved (order 4, order-2, 46 digits, β=−1/(3√3), ξ₀ action).
* Sentences 7–9 are the Stage-3.1 addendum (bundle reproduces the 46-digit
  claim; SIARC provenance via SIARC_PROVENANCE.md; continues concept
  10.5281/zenodo.20455089). **Flagged** in the file: operator may trim to a
  pure-Abstract description (re-pins the anchor).
* The paste-ready JSON `description` is the same text, `json.dumps(...,
  ensure_ascii=True)`-escaped (generated programmatically, not hand-typed, to
  guarantee the escape↔glyph correspondence). Verified: `ConvertFrom-Json`
  parses; `description` length 1539.

## Anchor

* `zenodo_metadata.md` SHA-256 = **dee9195c7957f25fc57f497d6875cdd2b63d97d24f55f36b5e54e388ec003eb8**
* Recorded in `metadata-anchor-current.txt` with re-pin triggers.
* **Provisional** — re-pin after corrections (title/abstract/MSC/affiliation/version).

## Open operator decisions (carried to Stage 5 checklist)

1. **F-AFFIL** — blank (corpus convention, 3 sources incl. a documented prior
   v1-spec error) vs. brief's "Independent Researcher, Yokohama, Japan".
2. **Addendum scope** — keep the 3-sentence bundle/SIARC addendum in the
   description, or trim to pure Abstract.
3. **Version string** — `1.0.0` (brief) vs `1.0` (corpus).
Each decision, if it changes the file, re-pins the anchor.
