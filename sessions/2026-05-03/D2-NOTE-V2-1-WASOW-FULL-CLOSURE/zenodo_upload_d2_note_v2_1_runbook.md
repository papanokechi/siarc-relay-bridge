# Zenodo upload runbook — D2-NOTE v2.1

**Deposit type:** New version on existing concept DOI

**Concept DOI (parent):** `10.5281/zenodo.19996689`

**Predecessor record (v2):** Zenodo record corresponding to
  `d2_note_v2.pdf` (SHA-256 `b9954d12bfe4f0c54351d9e87409c0d6870af6d53ff4904daf30e78e0e7ece66`),
  deposited 2026-05-03.

This runbook is a manual operator action. The agent does NOT
upload to Zenodo automatically.

## Step 1 — Open the v2 record

Navigate to https://doi.org/10.5281/zenodo.19996689 and follow
the redirect to the v2 deposit page.

Click the **"New version"** button. This creates a draft of v2.1
inheriting all metadata from v2.

## Step 2 — Replace files

Remove the v2 PDF and source attachments. Upload from
`sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/`:

| File | SHA-256 |
|---|---|
| `d2_note_v2_1.pdf` | `a8b6026a3453f901a0da68c3849a9d7d828138ca4622b8a3686b68f01d5ef74e` |
| `d2_note_v2_1.tex` | `840120e73534da8ef6a44fb977405fd2a8630219c4cf75a9acd7d8c75b388165` |
| `annotated_bibliography.bib` | `ba5baec01b46700ae48555a6e2569053884815325cbd1ca054c040827fb8fed7` |

Optional supplementary (recommended):

| File | Purpose |
|---|---|
| `claims.jsonl` | AEAL provenance (20 entries) |
| `phase_b_newton_polygon_lemma.md` | mechanical proof source for Lemma 3.1 |
| `phase_c3_bt1933_verification.md` | verbatim quote provenance for BT1933 §§4–6 |
| `phase_c_full_closure_synthesis.md` | full-closure synthesis |
| `phase_d_verdict.md` | build verdict |
| `phase_e_pdf_verification.md` | pypdf metadata + body verification |

## Step 3 — Update metadata

- **Title:** `Cross-degree universality of the Borel-singularity radius for polynomial continued fractions (v2.1)`
- **Version:** `2.1`
- **Publication date:** `2026-05-03`
- **Description:** paste the contents of `zenodo_description_d2_note_v2_1.txt` verbatim
- **Keywords:** `Newton polygon; Borel summability; polynomial continued fractions; irregular singular point; universality; Wasow; Birkhoff; Trjitzinsky; asymptotic expansion`
- **Resource type:** Publication → Preprint
- **Authors:** Papanokechi (ORCID 0009-0000-6192-8273), affiliation: Independent researcher, Yokohama, Japan
- **Communities:** keep all communities from v2
- **Related identifiers:** keep v2's; add `Is new version of` → `10.5281/zenodo.19996689`
- **License:** CC-BY 4.0 (match v2)

## Step 4 — Pre-publish QA

Operator check before clicking Publish:
- [ ] PDF preview renders 9 pages (FULL band)
- [ ] PDF Title metadata says `(v2.1)` (verified offline by pypdf)
- [ ] Author = Papanokechi (no PII tokens)
- [ ] Description contains "Birkhoff–Trjitzinsky 1933 §§4–6"
- [ ] Description contains "Newton-polygon characteristic-polynomial Lemma"
- [ ] All three primary files attached with matching SHA-256
- [ ] Concept DOI link in version stack shows v2 → v2.1

## Step 5 — Publish

Click **Publish**. Zenodo issues the v2.1 DOI and updates the
concept-DOI version stack. The v2.1 DOI is reserved at draft time
and finalised at publish.

## Step 6 — Post-publish

Record in this runbook:
- v2.1 DOI: `[OPERATOR FILL AFTER PUBLISH]`
- v2.1 record URL: `[OPERATOR FILL AFTER PUBLISH]`
- Publish timestamp: `[OPERATOR FILL AFTER PUBLISH]`

If the v2.1 DOI differs from the form `10.5281/zenodo.<n>` by
anything other than the n component, halt and inform Claude.

## Notes

- This is NOT a fresh deposit. Do not create a new concept DOI;
  always use "New version" on the existing one.
- Communities and ORCID linkage are inherited from v2 by default.
- If Zenodo flags the file SHA-256 as duplicate of any earlier
  version, halt and check whether the v2.1 PDF was somehow not
  rebuilt; the SHAs above are the canonical v2.1 anchors.
