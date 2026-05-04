# arXiv submission runbook — Channel Theory v1.3

**Source-of-truth Zenodo record:** 10.5281/zenodo.19972394 (record id 19972394, version 1.3).
**Pack location on bridge:** `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_ct_v1.3/`
**arXiv classification:** primary `math-ph`, cross-list `math.DS, math.NT`.
**Page count:** 17 pp.
**Operator-action gate per Rule 2:** the agent does *not* submit on behalf
of the operator.  This runbook is the operator's checklist.

---

## Step 0 — Prerequisites

1. arXiv account (operator's existing account; ORCID-verified preferred
   per arXiv's first-time-submitter expediting rule).
2. **Endorsement REQUIRED** for first-time submitter to math-ph.  math-ph is its own arXiv endorsement domain.  Endorser must hold active math-ph endorsement privilege (≥ a few math-ph submissions in the prior 5 years).  Tier-1 candidate from ENDORSER-HANDLE-ACQUISITION 2026-05-04 with math-ph track record: Marta Mazzocco (mazzocco_m_1) — operator confirms email before sending.  No math-ph-specific endorsement template was emitted by 034 (spec §3.D.1 limited Phase D to math.NT records only); operator may adapt the math.NT templates by changing `math.NT` → `math-ph` and the paper title accordingly.
3. Bridge pack hash-verified vs Zenodo (PASS in 034 PHASE A.2;
   see `pack_hash_match_table.md` for md5 + SHA-256 + size + page count).

---

## Step 1 — File attachments (in order)

Upload to arXiv submission "Add Files" widget in this order:

```
sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_ct_v1.3/channel_theory_outline.tex                         # primary TeX source
sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_ct_v1.3/00README.txt                          # bridge provenance + pack readme
sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_ct_v1.3/abstract.txt                          # one-paragraph abstract verbatim
sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_ct_v1.3/channel_theory_outline.pdf                          # PDF alternate-source (arXiv auto-compile fallback)
```

The compressed pack tarball `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_ct_v1.3/ct_v1.3.tar.gz` is *not* uploaded directly
(arXiv auto-tars after acceptance); it is preserved on the bridge as the
canonical immutable mirror artefact.

---

## Step 2 — arXiv classification

```
Primary:    math-ph
Cross-list: math.DS, math.NT
```

Cross-list rationale:
-   math.DS
  math.NT

---

## Step 3 — Metadata fields (paste verbatim)

- **Title:** Channel Theory for Polynomial Continued Fractions: Asymptotic Channels, the ξ₀ = 2/√β₂ Identity, and a Bridge Conjecture
- **Authors:** papanokechi (Independent Researcher, Yokohama, Japan)
- **Abstract:** *paste contents of `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_ct_v1.3/abstract.txt`* — first paragraph
  reproduced below for convenience:

> We propose, define, and catalogue asymptotic channels for sequences arising from polynomial continued fractions (PCFs). Each channel is a triple (D, T, S) specifying a formal-series space D, an asymptotic gauge T, and an analytic- continuation section S; three concrete channels appear in the SIARC stack -- the recurrence-parameter channel \Lt, the Borel-of-trans-series channel \BoT, and the connec…  (full text in `abstract.txt`)

- **Comments:** "17 pages.  Mirror of Zenodo record 10.5281/zenodo.19972394."
- **Report-no:** *(none — SIARC nondefault)*
- **DOI:** 10.5281/zenodo.19972394
- **License:** CC-BY-4.0  (matches Zenodo; arXiv supports CC-BY-4.0 from
  the standard license dropdown).

---

## Step 4 — arXiv web-form sequence

1. https://arxiv.org/submit  →  **Start new submission**.
2. Choose category — primary `math-ph`, then click **Add another**
   for each cross-list entry above.
3. License — select **CC-BY-4.0** from the dropdown.
4. Add files — upload in the order listed in Step 1.
5. Verify auto-compile (arXiv runs pdfTeX on the .tex; the included
   .pdf serves as fallback if compile fails).
6. Metadata — paste Title, Authors, Abstract, Comments, DOI from Step 3.
7. Preview — confirm title/authors/abstract and PDF first page render
   match the deposited Zenodo PDF.
8. Submit — arXiv issues an arXiv ID of the form `arXiv:XXXX.XXXXX`.

---

## Step 5 — Post-submission

- Note the assigned arXiv ID under Item 4 of
  `tex/submitted/submission_log.txt`.
- Operator action on Zenodo: edit record 19972394's
  **Related identifiers** to add the new arXiv ID with relation
  `IsIdenticalTo` (or `IsVersionOf`); this completes the Zenodo↔arXiv
  bidirectional cross-link.
- Update SIARC umbrella v2.0 / future v2.1 cross-reference tables
  (operator-side, separate session) with the arXiv ID.
- Confirm submission visible at `https://arxiv.org/abs/<arXiv-id>`
  ~24h after acceptance (arXiv's announcement cycle).

---

## §_endorsement (this record)

Adapt one of the math.NT endorsement templates by substituting category and paper title; or proceed via institutional-email auto-endorsement path if applicable.

---

## Provenance

- 034 session path: `sessions/2026-05-04/ARXIV-MIRROR-RUNBOOK-REFIRE/`
- Pack hash verification: `pack_hash_match_table.md` (5/5 PASS)
- Zenodo metadata blob: `zenodo_metadata_5_records.json`
- AEAL claims: `claims.jsonl`
