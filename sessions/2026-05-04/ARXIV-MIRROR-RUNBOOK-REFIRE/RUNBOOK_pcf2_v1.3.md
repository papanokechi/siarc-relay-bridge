# arXiv submission runbook — PCF-2 v1.3

**Source-of-truth Zenodo record:** 10.5281/zenodo.19963298 (record id 19963298, version 1.3).
**Pack location on bridge:** `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf2_v1.3/`
**arXiv classification:** primary `math.NT`, cross-list `math-ph`.
**Page count:** 22 pp.
**Operator-action gate per Rule 2:** the agent does *not* submit on behalf
of the operator.  This runbook is the operator's checklist.

---

## Step 0 — Prerequisites

1. arXiv account (operator's existing account; ORCID-verified preferred
   per arXiv's first-time-submitter expediting rule).
2. **Endorsement REQUIRED** (primary math.NT, first-time submitter).  See §_endorsement below; six populated templates were emitted by 034 (this record × three Tier-1 endorsers).  Operator personalises and sends one or more before the arXiv web-form submission can complete.  arXiv will issue a 6-character alphanumeric endorsement code once the operator starts a new submission in math.NT; that code is what the endorser enters at https://arxiv.org/auth/endorse.
3. Bridge pack hash-verified vs Zenodo (PASS in 034 PHASE A.2;
   see `pack_hash_match_table.md` for md5 + SHA-256 + size + page count).

---

## Step 1 — File attachments (in order)

Upload to arXiv submission "Add Files" widget in this order:

```
sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf2_v1.3/pcf2_program_statement.tex                         # primary TeX source
sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf2_v1.3/00README.txt                          # bridge provenance + pack readme
sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf2_v1.3/abstract.txt                          # one-paragraph abstract verbatim
sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf2_v1.3/pcf2_program_statement.pdf                          # PDF alternate-source (arXiv auto-compile fallback)
```

The compressed pack tarball `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf2_v1.3/pcf2_v1.3.tar.gz` is *not* uploaded directly
(arXiv auto-tars after acceptance); it is preserved on the bridge as the
canonical immutable mirror artefact.

---

## Step 2 — arXiv classification

```
Primary:    math.NT
Cross-list: math-ph
```

Cross-list rationale:
-   math-ph

---

## Step 3 — Metadata fields (paste verbatim)

- **Title:** PCF-2: A Program Statement for the Cubic Extension of the Δ-Discriminant Transcendence Predicate
- **Authors:** papanokechi (Independent Researcher, Yokohama, Japan)
- **Abstract:** *paste contents of `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf2_v1.3/abstract.txt`* — first paragraph
  reproduced below for convenience:

> This paper is a program statement, not a results paper. It frames PCF-2 (P13 in the SIARC stack), the cubic extension of PCF-1~\cite{Papanokechi2026PCF1} from degree-two polynomial continued fractions to degree-three. PCF-1 established a sharp empirical dichotomy across 30 degree-two families: the sign of the balanced discriminant \Delta_{2}=\beta^{2}-4\alpha\gamma predicts whether the limit of th…  (full text in `abstract.txt`)

- **Comments:** "22 pages.  Mirror of Zenodo record 10.5281/zenodo.19963298."
- **Report-no:** *(none — SIARC nondefault)*
- **DOI:** 10.5281/zenodo.19963298
- **License:** CC-BY-4.0  (matches Zenodo; arXiv supports CC-BY-4.0 from
  the standard license dropdown).

---

## Step 4 — arXiv web-form sequence

1. https://arxiv.org/submit  →  **Start new submission**.
2. Choose category — primary `math.NT`, then click **Add another**
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

- Note the assigned arXiv ID under Item 3 of
  `tex/submitted/submission_log.txt`.
- Operator action on Zenodo: edit record 19963298's
  **Related identifiers** to add the new arXiv ID with relation
  `IsIdenticalTo` (or `IsVersionOf`); this completes the Zenodo↔arXiv
  bidirectional cross-link.
- Update SIARC umbrella v2.0 / future v2.1 cross-reference tables
  (operator-side, separate session) with the arXiv ID.
- Confirm submission visible at `https://arxiv.org/abs/<arXiv-id>`
  ~24h after acceptance (arXiv's announcement cycle).

---

## §_endorsement (this record)

See `endorsement_template_pcf2_v1.3_zudilin.md`, `endorsement_template_pcf2_v1.3_mazzocco.md`, `endorsement_template_pcf2_v1.3_garoufalidis.md` (this session).

---

## Provenance

- 034 session path: `sessions/2026-05-04/ARXIV-MIRROR-RUNBOOK-REFIRE/`
- Pack hash verification: `pack_hash_match_table.md` (5/5 PASS)
- Zenodo metadata blob: `zenodo_metadata_5_records.json`
- AEAL claims: `claims.jsonl`
