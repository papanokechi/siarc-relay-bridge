# arXiv submission runbook — SIARC Umbrella v2.0

**Source-of-truth Zenodo record:** 10.5281/zenodo.19965041 (record id 19965041, version 2.0).
**Pack location on bridge:** `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_siarc_umbrella_v2.0/`
**arXiv classification:** primary `math.HO`, cross-list `(none)`.
**Page count:** 12 pp.
**Operator-action gate per Rule 2:** the agent does *not* submit on behalf
of the operator.  This runbook is the operator's checklist.

---

## Step 0 — Prerequisites

1. arXiv account (operator's existing account; ORCID-verified preferred
   per arXiv's first-time-submitter expediting rule).
2. **Endorsement REQUIRED** for first-time submitter to math.HO.  math.HO is part of the math endorsement cluster.  Once the operator has obtained a single positive endorsement in any math.* category (e.g. math.NT via PCF-1 v1.3 in record #2), subsequent submissions in math.HO typically inherit the cluster's endorsement privileges for that operator (per current arXiv help text); operator confirms via the in-flight submission widget at submission time.  No math.HO-specific endorsement template was emitted by 034 (spec §3.D.1 limited Phase D to math.NT records only).
3. Bridge pack hash-verified vs Zenodo (PASS in 034 PHASE A.2;
   see `pack_hash_match_table.md` for md5 + SHA-256 + size + page count).

---

## Step 1 — File attachments (in order)

Upload to arXiv submission "Add Files" widget in this order:

```
sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_siarc_umbrella_v2.0/main.tex                         # primary TeX source
sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_siarc_umbrella_v2.0/00README.txt                          # bridge provenance + pack readme
sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_siarc_umbrella_v2.0/abstract.txt                          # one-paragraph abstract verbatim
sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_siarc_umbrella_v2.0/main.pdf                          # PDF alternate-source (arXiv auto-compile fallback)
```

The compressed pack tarball `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_siarc_umbrella_v2.0/siarc_umbrella_v2.0.tar.gz` is *not* uploaded directly
(arXiv auto-tars after acceptance); it is preserved on the bridge as the
canonical immutable mirror artefact.

---

## Step 2 — arXiv classification

```
Primary:    math.HO
Cross-list: (none)
```

Cross-list rationale:
  (none)

---

## Step 3 — Metadata fields (paste verbatim)

- **Title:** An Arithmetic Stratification of Polynomial Continued Fractions — v2.0 (Modular-Discriminant Framing)
- **Authors:** papanokechi (Independent Researcher, Yokohama, Japan)
- **Abstract:** *paste contents of `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_siarc_umbrella_v2.0/abstract.txt`* — first paragraph
  reproduced below for convenience:

> This paper is a program statement, not a results paper. It is the v2.0 revision of the SIARC umbrella program statement, refactoring the v1 (April 2026) framing around a cross-degree invariant triple \bigl(\Delta_d(b),\ \PetN{\Delta}(\tau_b),\ \xi_0(b)\bigr) that emerged from the SIARC stack between v1 and v2. The triple combines the polynomial discriminant of the denominator polynomial b (the dis…  (full text in `abstract.txt`)

- **Comments:** "12 pages.  Mirror of Zenodo record 10.5281/zenodo.19965041."
- **Report-no:** *(none — SIARC nondefault)*
- **DOI:** 10.5281/zenodo.19965041
- **License:** CC-BY-4.0  (matches Zenodo; arXiv supports CC-BY-4.0 from
  the standard license dropdown).

---

## Step 4 — arXiv web-form sequence

1. https://arxiv.org/submit  →  **Start new submission**.
2. Choose category — primary `math.HO`, then click **Add another**
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

- Note the assigned arXiv ID under Item 1 of
  `tex/submitted/submission_log.txt`.
- Operator action on Zenodo: edit record 19965041's
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
