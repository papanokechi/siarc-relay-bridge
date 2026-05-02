# Zenodo upload runbook — D2-NOTE v1.0 (NEW concept DOI)

**Date prepared:** 2026-05-02
**Agent:** GitHub Copilot (VS Code), session D2-NOTE-DRAFT
**Operator action required:** YES — operator executes the upload; agent has prepared all artefacts.

> **CRITICAL.** This is a **NEW upload** on Zenodo, not a *New Version*. The D2-NOTE has **no predecessor record** on Zenodo. Selecting "New Version" of an unrelated record (e.g.\ Channel Theory v1.3) would corrupt the cross-degree umbrella by anchoring D2-NOTE to a wrong concept DOI. Use the "New upload" button on https://zenodo.org/uploads.

---

## 1. Files to upload

From `siarc-relay-bridge/sessions/2026-05-02/D2-NOTE-DRAFT/` upload:

| File | Required | Purpose |
|------|---------|---------|
| `d2_note.pdf`               | YES | Main artefact (4 pages, 343 419 B) |
| `d2_note.tex`               | YES | LaTeX source for reproducibility |
| `annotated_bibliography.bib`| YES | Bibliography source |
| `claims.jsonl`              | YES | AEAL claim ledger (8 entries) |

Do NOT upload: `*.aux`, `*.bbl`, `*.blg`, `*.log`, `*.out`, `*.toc`, `pass3.log`, `d2_note.log.tmp`. They are derivative build artefacts.

Pre-upload checks (run from the session directory):

```powershell
# SHA-256 verification (must match claims.jsonl D2-A8)
Get-FileHash -Algorithm SHA256 d2_note.pdf, d2_note.tex, annotated_bibliography.bib
# Expected pdf SHA-256: f2be89c18591479cbd86365730e40ca2ae6994d76cff0d8ab3ece84322bd94b8
# Expected tex SHA-256: 14044cd41760977504ef68725ebc9d2481d36dce22272227c24f9f9464dabc70
# Expected bib SHA-256: d1b16d781881737599f3e5d44ebf9bc4b35e38006159885e871bec57c93937f5

# Page count and size sanity
(Get-Item d2_note.pdf).Length     # expected: 343419
```

---

## 2. Zenodo metadata (paste into the form)

**Resource type:** Publication → Preprint

**Title:**

> Newton-polygon universality of the Borel-singularity radius for polynomial continued fractions

**Authors:**

| # | Name                        | Affiliation                                    | ORCID |
|---|-----------------------------|------------------------------------------------|-------|
| 1 | Echizen Kubo, Mauricio      | Independent researcher, Yokohama, Japan        | (operator: paste your ORCID) |

**Publication date:** 2026-05-02
**Language:** English
**Version:** 1.0
**Communities:** (operator: add your standard communities, e.g.\ siarc; same as Channel Theory v1.3)

**Description:** paste the contents of `zenodo_description_d2_note.txt` (the entire file).

**Keywords:**

```
Newton polygon
Borel summability
polynomial continued fractions
irregular singular point
universality
SIARC
PCF
xi_0
```

**License:** Creative Commons Attribution 4.0 International (same as the rest of the SIARC v1.3 cohort).

**Funding / Grants:** none.

---

## 3. Related Identifiers

Add the following entries (Resource type = Publication/Preprint unless noted):

| Relation              | Identifier                              | Note                                    |
|-----------------------|-----------------------------------------|-----------------------------------------|
| References            | 10.5281/zenodo.19941678                 | Channel Theory concept (cite-all)       |
| References            | 10.5281/zenodo.19972394                 | Channel Theory v1.3 (canonical source)  |
| References            | 10.5281/zenodo.19931635                 | PCF-1 concept (cite-all)                |
| References            | 10.5281/zenodo.19937196                 | PCF-1 v1.3 (d=2 baseline)               |
| References            | 10.5281/zenodo.19936297                 | PCF-2 concept (cite-all)                |
| References            | 10.5281/zenodo.19963298                 | PCF-2 v1.3                              |
| References            | 10.5281/zenodo.19885549                 | SIARC umbrella concept (cite-all)       |
| References            | 10.5281/zenodo.19965041                 | SIARC umbrella v2.0                     |
| Is documented by      | https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-02/D2-NOTE-DRAFT/ | Resource type: Other / Software         |
| Is documented by      | https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-01/PCF2-SESSION-Q1/ | Resource type: Other / Software         |

Do **NOT** add any `IsNewVersionOf` relation. This is a new concept.

---

## 4. Upload procedure

1. https://zenodo.org/uploads → click **New upload**.
2. Drag-and-drop the four files in §1 in the order listed (`d2_note.pdf` first; Zenodo uses the first-listed PDF as the default preview).
3. Fill in metadata per §2.
4. Add Related Identifiers per §3.
5. Click **Save** (draft).
6. **Before publishing:** click **Preview**, verify:
   - PDF preview opens at page 1, title visible.
   - All eight Related Identifier rows resolve (Zenodo shows green check or text).
   - Description renders without raw HTML comments visible (the `<!-- ... -->` lines should be hidden by Zenodo's renderer).
7. Click **Publish**.

---

## 5. Post-publish capture

After Zenodo mints the DOIs, capture the following and append to `claims.jsonl` as a new claim `D2-A9`:

```powershell
# Replace <CONCEPT> and <VERSION> with the minted IDs
$concept = "10.5281/zenodo.<CONCEPT>"
$version = "10.5281/zenodo.<VERSION>"
$ts = Get-Date -Format "yyyy-MM-ddTHH:mm:ssK"
$line = "{`"claim_id`": `"D2-A9`", `"task_id`": `"D2-NOTE-DRAFT`", `"claim`": `"D2-NOTE v1.0 published on Zenodo. Concept DOI $concept; version DOI $version; published $ts. PDF SHA-256 f2be89c18591479cbd86365730e40ca2ae6994d76cff0d8ab3ece84322bd94b8 (matches D2-A6/A8 anchor; should match Zenodo readback exactly).`", `"evidence_type`": `"file_inspection`", `"dps`": null, `"reproducible`": true, `"script`": `"Invoke-RestMethod https://zenodo.org/api/records/<VERSION>`", `"output_hash`": `"f2be89c18591479cbd86365730e40ca2ae6994d76cff0d8ab3ece84322bd94b8`"}"
Add-Content -Path claims.jsonl -Value $line
```

Then verify the published PDF byte-identical to local:

```powershell
$pub = "https://zenodo.org/records/<VERSION>/files/d2_note.pdf?download=1"
Invoke-WebRequest $pub -OutFile zenodo_readback.pdf
(Get-FileHash zenodo_readback.pdf -Algorithm SHA256).Hash
# Must equal: f2be89c18591479cbd86365730e40ca2ae6994d76cff0d8ab3ece84322bd94b8
Remove-Item zenodo_readback.pdf
```

If the readback hash mismatches, do NOT trust the upload; re-upload from scratch.

---

## 6. Cross-system updates

After publication, the operator should:

1. **PCF-1 v1.3 README on the bridge:** add D2-NOTE concept DOI to the "cross-references" section as the canonical short note for §5 (Newton-polygon universality).
2. **Channel Theory v1.3 metadata:** add a Related Identifier `IsCitedBy: 10.5281/zenodo.<D2-NOTE-CONCEPT>` (post-publish metadata edit only; no new CT version).
3. **SIARC umbrella v2.0 §4.4:** the next umbrella revision (v2.1) should cite D2-NOTE as the canonical source for the ξ₀ axis. No immediate action.
4. **Bridge:** the master-conjecture-v0 P-NP axis claim (currently citing CT v1.3) can switch to citing D2-NOTE concept once stable.

---

## 7. If anything fails

- **Upload page hangs / Zenodo 502:** retry once. If it still fails, save the draft and notify; do NOT click Publish on a partial upload.
- **DOI mints with an unexpected concept link** (e.g.\ Zenodo accidentally chains it as a New Version of a draft): contact Zenodo support; do NOT publish a corrective second version that would create a phantom predecessor.
- **PDF readback hash mismatch:** treat as data loss; pull the record (Zenodo does not allow file edits after publish — you would have to publish a v1.0.1) and re-upload from the local source files.

---

## 8. Bridge URLs (post-publish)

After D2-A9 is appended, the bridge advertisements are:

```
BRIDGE: https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-02/D2-NOTE-DRAFT/
CLAUDE_FETCH: https://raw.githubusercontent.com/papanokechi/siarc-relay-bridge/main/sessions/2026-05-02/D2-NOTE-DRAFT/handoff.md
ZENODO: https://doi.org/10.5281/zenodo.<D2-NOTE-CONCEPT>
```

End of runbook.
