# Zenodo upload runbook — D2-NOTE v2.0 (NEW concept DOI)

**Date prepared:** 2026-05-03
**Agent:** GitHub Copilot (VS Code), session Q20A-PHASE-C-RESUME (dispatch 4)
**Operator action required:** YES — operator executes the upload; agent has prepared all artefacts.

---

## 0. Critical decision: NEW upload, NOT New Version

> **CRITICAL.** This is a **NEW upload** on Zenodo, not a *New Version*.
>
> **Reason:** D2-NOTE v1.0 (drafted 2026-05-02 in session
> `sessions/2026-05-02/D2-NOTE-DRAFT/`) was **never deposited to Zenodo**.
> Evidence: (a) `submission_log.txt` has no D2-NOTE Item entry; (b)
> `RESUME_AFTER_REBOOT_20260502.txt` lists exactly five published Zenodo
> records (umbrella v2.0, PCF-1 v1.3, PCF-2 v1.3, CT v1.3, T2B v3.0) and
> D2-NOTE is not among them; (c) the v1 handoff explicitly states
> "D2-NOTE has no Zenodo DOI yet minted". v1 was superseded in-flight by
> v2 (the cross-degree theorem upgrade landed within ~24 h of v1's draft,
> via Q20a UPGRADE_FULL).
>
> Therefore D2-NOTE v2 is a fresh concept DOI: there is no predecessor
> record to chain. Use **"New upload"** on https://zenodo.org/uploads.
>
> **If operator finds an existing D2-NOTE record on Zenodo** (e.g. v1
> was deposited and the agent's records are stale): STOP, do not click
> Publish, and instead use "New Version" of the v1 concept; update §3
> below to add `IsNewVersionOf: 10.5281/zenodo.<v1-version-DOI>`.

---

## 1. Files to upload

From `siarc-relay-bridge/sessions/2026-05-03/Q20A-PHASE-C-RESUME/d2_note_v2/`
upload:

| File                          | Required | Purpose                                   |
|-------------------------------|----------|-------------------------------------------|
| `d2_note_v2.pdf`              | YES      | Main artefact (6 pp, 400 559 B)           |
| `d2_note_v2.tex`              | YES      | LaTeX source for reproducibility          |
| `annotated_bibliography.bib`  | YES      | Bibliography source                       |

Plus, from one level up at
`siarc-relay-bridge/sessions/2026-05-03/Q20A-PHASE-C-RESUME/`:

| File                | Required | Purpose                                              |
|---------------------|----------|------------------------------------------------------|
| `claims.jsonl`      | YES      | AEAL claim ledger (58 entries; covers Q20a + carry-forward) |

Do NOT upload: `*.aux`, `*.bbl`, `*.blg`, `*.log`, `*.out`, `*.toc`.
They are derivative LaTeX build artefacts and not committed to the
bridge anyway.

### 1.1 Pre-upload SHA-256 verification (run from the session directory)

```powershell
cd "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-03\Q20A-PHASE-C-RESUME"

Get-FileHash -Algorithm SHA256 `
    d2_note_v2\d2_note_v2.pdf, `
    d2_note_v2\d2_note_v2.tex, `
    d2_note_v2\annotated_bibliography.bib, `
    claims.jsonl | Format-Table Hash, Path
```

**Expected hashes** (verified 2026-05-03):

| File                              | SHA-256 (full)                                                       | Size (B) |
|-----------------------------------|----------------------------------------------------------------------|----------|
| `d2_note_v2.pdf`                  | `3496D5B6E0EAF992842CCFDAF3BF51AA0BEECB34C3F99E76391C876072E3DC09`   | 400 559  |
| `d2_note_v2.tex`                  | `823B82FE14A96DD986E35DF62B3076427A2A900F7B219C8CFDC8CECA3F2B6816`   | 21 192   |
| `annotated_bibliography.bib`      | `80D1A0BC82F47A88063D947EB56271426C1881136C35C352813347A23CD6DC80`   | 34 092   |
| `claims.jsonl` (58 entries)       | `1FD307498C6A0ACA898B760BB51C0CDA2C9033986D8F21A938AAC6A20BAF645D`   | 27 162   |

If any hash mismatches: STOP, re-pull from the bridge `main` branch
(commit `1642b24`) and re-verify. Do not upload a drifted artefact.

### 1.2 Page count + integrity sanity

```powershell
$env:PYTHONIOENCODING = "utf-8"
python -c "import pypdf; print('pages:', len(pypdf.PdfReader(r'd2_note_v2\d2_note_v2.pdf').pages))"
# Expected output: pages: 6
```

The O1 operator review (`o1_operator_review.md`) confirmed READY_FOR_DEPOSIT
on 2026-05-03; all 9 content checks PASS. See that report for the per-check
verdict trail.

---

## 2. Zenodo metadata (paste into the form)

**Resource type:** Publication → Preprint

**Title:**

> Newton-polygon universality of the Borel-singularity radius for polynomial continued fractions

**Authors:**

| # | Name                        | Affiliation                                    | ORCID                       |
|---|-----------------------------|------------------------------------------------|-----------------------------|
| 1 | Echizen Kubo, Mauricio      | Independent researcher, Yokohama, Japan        | (operator: paste your ORCID)|

**Publication date:** 2026-05-03
**Language:** English
**Version:** 2.0
**Communities:** the same set used for Channel Theory v1.3 / PCF-2 v1.3
(operator: e.g. siarc, or whatever standing community list you used on
those previous deposits).

**Description:** paste the contents of the `zenodo_description_d2_note_v2.txt`
file generated alongside this runbook (see §2.1 below). All `<!-- ... -->`
HTML-comment lines are hidden by Zenodo's renderer; paste the text as-is.

**Keywords** (12 — same nine as v1 plus three v2-specific):

```
Newton polygon
Borel summability
polynomial continued fractions
irregular singular point
universality
SIARC
PCF
xi_0
Wasow asymptotic existence
Birkhoff formal series
shearing transformation
cross-degree theorem
```

**License:** Creative Commons Attribution 4.0 International (same as
the rest of the SIARC v1.3 cohort).

**Funding / Grants:** none.

### 2.1 Generate the description text

The description for v2 is below; save it as
`zenodo_description_d2_note_v2.txt` in the session directory and paste
its contents into Zenodo's description field at upload time.

```
Newton-polygon universality of the Borel-singularity radius for
polynomial continued fractions: a 6-page consolidatory short note
(v2.0, 2026-05-03; supersedes the v1.0 draft of 2026-05-02 which was
never deposited).

Position. We isolate, as a single citable artefact, the cross-degree
identity ξ₀(b) = d / β_d^(1/d) for the leading Borel-plane singular
distance of the formal generating function f(z) = Σ Q_n z^n of a
polynomial continued fraction (1, b) of degree d with leading
coefficient β_d > 0. Version 2 upgrades the v1 status from
"proven at d=2 / verified at d=4 / conjectured for d ≥ 2" to a
theorem-grade statement covering all d ≥ 2 uniformly.

The upgrade rests on two new anchors:

(i) SIARC Phase A* extended sweep — a direct symbolic identity check
    at d ∈ {2, 3, ..., 10}, 18/18 pass at dps = 50, relative error
    < 1.6 × 10^-51 above d = 2, with byte-locked script SHA-256
    8e6f9eb…f7496 for phase_a_symbolic_derivation.py and
    06d87de…0ac277 for phase_a_star_extended_sweep.py (cf. SIARC
    bridge sessions/2026-05-03/Q20A-PHASE-C-RESUME/, claims.jsonl).

(ii) Wasow 1965 §19 (Theorem 19.1) and Birkhoff 1930 §2 — the
    uniform-in-q general-case asymptotic existence theorem, plus
    the uniform-in-n formal series existence at an irregular
    singular point of rank q. Wasow's q maps to PCF degree d via
    q = (d+2)/2, with §19.3's ramification substitution x = const · t^p
    handling fractional q (p = 2 suffices for all d ≥ 2). The
    Newton-polygon slope-1/d edge of (1) is recorded as the same
    object as Wasow's shearing exponent g_0 = 1/d in two notations.

Theorem 4.1 (cross-degree universality of ξ₀; upgrades Conj. 3.3.A*
of Channel Theory v1.3): for every PCF (1, b) in scope with deg b = d ≥ 2
and β_d > 0, the leading characteristic root of the irregular
singularity at z = 0 is ξ₀(b) = d / β_d^(1/d).

Tier discipline (carried forward from v1):
- PROVEN at d = 2 (Newton-polygon proof, CT v1.3 Prop. 3.3.A;
  PCF-1 v1.3 Theorem 5 §5).
- VERIFIED at d = 4 (PCF2-SESSION-Q1, dps = 80, spread 0 across 8
  quartic representatives).
- THEOREM-GRADE for all d ≥ 2 via Wasow §19 + Birkhoff §2 + Phase A*
  symbolic identity (NEW in v2).
- DEFERRED at d = 3 for direct Newton-polygon test (op:xi0-d3-direct;
  measurement-of-corroboration only — symbolic identity already in
  Phase A* sweep).

Out of scope. The β_d < 0 branch, the d = 2 anomaly Galois bin
(PCF-1 v1.3 Remark 5.E), and the d ≥ 11 case (not in Phase A* sweep
but covered by Wasow framework) are recorded as open in §5.

This note remains purely consolidatory: no new numerical pipeline is
run; the v2 contribution is the Phase A* d-sweep and the Wasow / Birkhoff
literature anchoring. The Wasow §19 and Birkhoff 1930 literature claims
are anchored by SHA-256-verified PDFs at the runbook-canonical literature
directory (Wasow PDF SHA f59d6835…a5fd, Birkhoff PDF SHA aeb5291e…2efa)
and by per-theorem AEAL claim entries.

References (DOI / bridge URL):
- Channel Theory v1.3: 10.5281/zenodo.19972394 (concept 10.5281/zenodo.19941678)
- PCF-1 v1.3: 10.5281/zenodo.19937196 (concept 10.5281/zenodo.19931635)
- PCF-2 v1.3: 10.5281/zenodo.19963298 (concept 10.5281/zenodo.19936297)
- SIARC umbrella v2.0: 10.5281/zenodo.19965041 (concept 10.5281/zenodo.19885549)
- Q20A-PHASE-C-RESUME bridge session:
  https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-03/Q20A-PHASE-C-RESUME/
- PCF2-SESSION-Q1 bridge session:
  https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-01/PCF2-SESSION-Q1/

Method. AEAL/SIARC v1.3 cohort multi-agent methodology. AI tools
(GitHub Copilot powered by Anthropic Claude Opus 4.7, and Anthropic
Claude) were used for prose drafting and consistency-checking; all
theorem statements, conjecture formulations, and editorial decisions
remain the author's. All numerical claims trace to exact computations
stored under sessions/2026-05-{01,03}/ on the SIARC bridge with AEAL
claim entries in claims.jsonl (58 entries total in the Q20A-PHASE-C-RESUME
session as of dispatch 4).

NOTE TO OPERATOR. This is a NEW concept DOI (D2-NOTE v1 was never
deposited; v2 is the first published version). Use "New upload" on
https://zenodo.org/uploads, not "New Version" of any other record.
```

---

## 3. Related Identifiers

Add the following entries (Resource type = Publication / Preprint
unless noted):

| Relation              | Identifier                                                                                                          | Note                                          |
|-----------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| References            | 10.5281/zenodo.19941678                                                                                              | Channel Theory concept (cite-all)             |
| References            | 10.5281/zenodo.19972394                                                                                              | Channel Theory v1.3 (canonical d=2 / d=4 / Conj.~3.3.A* source) |
| References            | 10.5281/zenodo.19931635                                                                                              | PCF-1 concept (cite-all)                      |
| References            | 10.5281/zenodo.19937196                                                                                              | PCF-1 v1.3 (d=2 baseline; Theorem 5 §5)       |
| References            | 10.5281/zenodo.19936297                                                                                              | PCF-2 concept (cite-all)                      |
| References            | 10.5281/zenodo.19963298                                                                                              | PCF-2 v1.3                                    |
| References            | 10.5281/zenodo.19885549                                                                                              | SIARC umbrella concept (cite-all)             |
| References            | 10.5281/zenodo.19965041                                                                                              | SIARC umbrella v2.0                           |
| Is documented by      | https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-03/Q20A-PHASE-C-RESUME/                 | Resource type: Other / Software (canonical AEAL anchor) |
| Is documented by      | https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-01/PCF2-SESSION-Q1/                     | Resource type: Other / Software (d=4 measurement) |
| Is documented by      | https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-02/D2-NOTE-DRAFT/                       | Resource type: Other / Software (v1 draft session — superseded but archived) |

Do **NOT** add any `IsNewVersionOf` relation. v1 was never deposited
(see §0). If operator confirms v1 *was* deposited after all, switch
the `IsNewVersionOf` to point at the v1 version DOI.

---

## 4. Upload procedure

1. Navigate to https://zenodo.org/uploads → click **New upload** (the
   green button on the dashboard, NOT the "New version" button next to
   any existing record).
2. Drag-and-drop the four files from §1 in this order
   (Zenodo uses the first-listed PDF as the default preview):
   - `d2_note_v2.pdf` first
   - `d2_note_v2.tex`
   - `annotated_bibliography.bib`
   - `claims.jsonl`
3. Fill in metadata per §2.
4. Add Related Identifiers per §3 (eight `References` rows + three
   `Is documented by` rows = 11 entries).
5. Click **Save** (draft).
6. **Before publishing:** click **Preview**, verify:
   - PDF preview opens at page 1, title visible: "CROSS-DEGREE
     UNIVERSALITY OF THE BOREL-SINGULARITY RADIUS FOR POLYNOMIAL
     CONTINUED FRACTIONS".
   - All 11 Related Identifier rows resolve (Zenodo shows green check
     or formatted text for each).
   - Description renders without raw HTML comments visible (the v2
     description has no `<!-- -->` blocks; check that paragraph breaks
     and DOI hyperlinks render correctly).
   - Keywords: 12 chips visible.
   - Resource type = Publication / Preprint.
7. Click **Publish**.

---

## 5. Post-publish capture

After Zenodo mints the DOIs, capture the following and append to
`claims.jsonl` as a new claim. Q20a's claim count will be 58 + 1 = 59.

```powershell
# Replace <CONCEPT> and <VERSION> with the minted IDs.
cd "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-03\Q20A-PHASE-C-RESUME"

$concept = "10.5281/zenodo.<CONCEPT>"
$version = "10.5281/zenodo.<VERSION>"
$ts = Get-Date -Format "yyyy-MM-ddTHH:mm:ssK"

$claim = [ordered]@{
  claim         = "D2-NOTE v2.0 published on Zenodo. Concept DOI $concept; version DOI $version; published $ts. PDF SHA-256 3496d5b6e0eaf992842ccfdaf3bf51aa0beecb34c3f99e76391c876072e3dc09 (matches Q20a Phase E build hash; should match Zenodo readback exactly). v1 superseded (never deposited; see runbook §0)."
  evidence_type = "file_inspection"
  dps           = $null
  reproducible  = $true
  script        = "Invoke-RestMethod https://zenodo.org/api/records/<VERSION>"
  output_hash   = "3496d5b6e0eaf992842ccfdaf3bf51aa0beecb34c3f99e76391c876072e3dc09"
}
$line = $claim | ConvertTo-Json -Compress
Add-Content -Path claims.jsonl -Value $line
```

Then verify the published PDF byte-identical to local:

```powershell
$ver = "<VERSION>"   # e.g. 19980000
$pub = "https://zenodo.org/records/$ver/files/d2_note_v2.pdf?download=1"
Invoke-WebRequest $pub -OutFile zenodo_readback_v2.pdf
$h = (Get-FileHash zenodo_readback_v2.pdf -Algorithm SHA256).Hash
Write-Host "Readback SHA-256: $h"
Write-Host "Expected         : 3496D5B6E0EAF992842CCFDAF3BF51AA0BEECB34C3F99E76391C876072E3DC09"
if ($h -ieq "3496D5B6E0EAF992842CCFDAF3BF51AA0BEECB34C3F99E76391C876072E3DC09") {
  Write-Host "MATCH" -ForegroundColor Green
  Remove-Item zenodo_readback_v2.pdf
} else {
  Write-Host "MISMATCH — do NOT trust upload" -ForegroundColor Red
}
```

If the readback hash mismatches, do NOT trust the upload; re-upload
from scratch (Zenodo does not allow file edits after publish — you
would have to publish a v2.0.1 to correct).

Then commit the appended `claims.jsonl` to the bridge:

```powershell
cd "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge"
git pull origin main
git add sessions/2026-05-03/Q20A-PHASE-C-RESUME/claims.jsonl
git commit -m "Q20A — append D2-NOTE v2 Zenodo deposit claim

Concept DOI 10.5281/zenodo.<CONCEPT>; version DOI 10.5281/zenodo.<VERSION>.
PDF SHA-256 readback verified.

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
git push origin main
```

---

## 6. Cross-system updates (post-publish)

After publication, the operator should:

1. **submission_log.txt:** add Item 19 = D2-NOTE v2.0 (concept DOI
   minted today). Use the existing Item 17 / 18 patches as the
   template; the next-prompt-queue file
   `tex/submitted/control center/prompt/001_submission_log_patch_item19.txt`
   may already be staged for this — coordinate with that prompt's
   spec. The agent who fires Prompt 001 will splice between Item 18
   (line 577) and the Note: block (line 579).
2. **Channel Theory v1.3 Zenodo metadata:** add a Related Identifier
   `IsCitedBy: 10.5281/zenodo.<D2-NOTE-V2-CONCEPT>` (post-publish
   metadata edit only; no new CT version). This makes the cite path
   bidirectional.
3. **PCF-1 v1.3 / PCF-2 v1.3 Zenodo metadata (optional):** consider
   adding `IsCitedBy: <D2-NOTE-V2-CONCEPT>` if those records cite the
   ξ₀ universality identity in their abstracts.
4. **SIARC umbrella v2.0 §4.4:** the next umbrella revision (v2.1)
   should cite D2-NOTE v2 as the canonical source for the ξ₀ axis,
   superseding the CT v1.3 Conj. 3.3.A* citation. No immediate
   action; queue for v2.1 dispatch.
5. **Bridge:** the master-conjecture-v0 P-NP axis claim (currently
   citing CT v1.3) should switch to citing D2-NOTE v2 concept once
   D2-NOTE v2 stabilises.
6. **CT v1.4 / v1.5:** if Q20a UPGRADE_FULL prompts a CT v1.4 narrative
   draft (separate todo `ct-v14-narrative-draft`), the v1.4 §3.3
   should treat Conj. 3.3.A* as Theorem 3.3.A* (or equivalent), citing
   D2-NOTE v2 [\cite{siarc_d2_note_v2}] as the proof source.

---

## 7. If anything fails

- **Upload page hangs / Zenodo 502:** retry once. If it still fails,
  save the draft and notify; do NOT click Publish on a partial upload.
- **Operator finds an existing D2-NOTE record on Zenodo:** STOP. Do
  not click Publish. Investigate whether v1 was deposited
  retroactively. If yes, abandon this "New upload" draft (delete it
  from Zenodo's drafts UI), and re-execute via "New Version" of the
  v1 record's concept; add `IsNewVersionOf: 10.5281/zenodo.<v1-version>`
  to the related identifiers.
- **DOI mints with an unexpected concept link** (e.g. Zenodo
  accidentally chains it as a New Version of an unrelated draft):
  contact Zenodo support; do NOT publish a corrective second version
  that would create a phantom predecessor.
- **PDF readback hash mismatch** (§5): treat as data loss; pull the
  record (Zenodo does not allow file edits after publish — you would
  have to publish a v2.0.1) and re-upload from the local source files.

---

## 8. Bridge URLs (post-publish)

After the post-publish AEAL claim is appended and pushed, the bridge
advertisements are:

```
BRIDGE: https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-03/Q20A-PHASE-C-RESUME/
CLAUDE_FETCH: https://raw.githubusercontent.com/papanokechi/siarc-relay-bridge/main/sessions/2026-05-03/Q20A-PHASE-C-RESUME/handoff.md
ZENODO (concept): https://doi.org/10.5281/zenodo.<D2-NOTE-V2-CONCEPT>
ZENODO (v2.0):    https://doi.org/10.5281/zenodo.<D2-NOTE-V2-VERSION>
```

---

## 9. Quick-reference checklist

```
[ ] Run §1.1 Get-FileHash; all four hashes match
[ ] Run §1.2 page count check; pypdf reports 6
[ ] Save zenodo_description_d2_note_v2.txt locally (§2.1)
[ ] Open https://zenodo.org/uploads → New upload (NOT New version)
[ ] Drag PDF, .tex, .bib, claims.jsonl in that order
[ ] Resource type = Publication / Preprint
[ ] Title, authors, ORCID, date 2026-05-03, version 2.0, language EN
[ ] Communities (siarc + standing list)
[ ] Description (paste §2.1 text)
[ ] 12 keywords (§2)
[ ] License CC-BY 4.0
[ ] 8 References + 3 Is documented by Related Identifiers (§3)
[ ] No IsNewVersionOf
[ ] Save → Preview → check 11 Related Identifiers + PDF preview + description render
[ ] Publish
[ ] Capture concept and version DOIs
[ ] Append claims.jsonl entry (§5)
[ ] Verify byte-identical readback (§5)
[ ] git commit + push (§5 footer)
[ ] Fire Prompt 001 (submission_log Item 19) once §1 prompt directory is recreated
[ ] (Optional) Add IsCitedBy on CT v1.3 metadata (§6 step 2)
```

End of runbook.
