# Zenodo Edit FIX-PASS 2 — D2-NOTE v2.1 addendum WYSIWYG-escape issue

**Date:** 2026-05-13 ~15:43 JST
**Target record:** D2-NOTE v2.1 (`10.5281/zenodo.20015923`)
**Edit pass history:**
- Pass 1 (15:37 JST): Markdown payload → `###` and `**` rendered as literal text
- Pass 2 (15:42 JST): HTML payload pasted into WYSIWYG editor → tags escaped to `&lt;h3&gt;`, render as literal text
- Pass 3 (this file): switch to HTML source-view before paste, OR use API PUT

**Status:** 🟡 OPERATOR FIX-EDIT PENDING (third pass)

---

## §1 — Why both prior passes failed

Zenodo's description editor is a TinyMCE WYSIWYG widget. Pasted content
behaviour:

- **Markdown** is NOT rendered (the editor wraps text in `<p>` but leaves
  `###` and `**` as literal characters).
- **HTML pasted in WYSIWYG mode** is treated as plain text — angle brackets
  are escaped (`<` → `&lt;`), so HTML tags display as literal text.

The editor has a **source-code view toggle** that bypasses this. Pasting
HTML in source-code view causes it to be stored as actual HTML markup.
This is the canonical fix path.

---

## §2 — Preferred path: HTML source view in browser

### Steps

1. Open https://zenodo.org/records/20015923 → click **Edit**.
2. Scroll to the **Description** field.
3. Find the **toolbar icons** above the description text area. Look for:
   - An icon shaped like `</>` (angle brackets with a slash)
   - OR a button labeled "Source", "HTML", "View source", or "</>"
   - OR a "Tools" or "View" menu containing a source-code option
4. Click that icon — the editor should switch to a plain-text view showing
   the existing description's underlying HTML markup.
5. **Locate the broken addendum** in the source view. It will look like:
   ```
   <p>&lt;hr&gt;</p>
   <p>&lt;h3&gt;S154 Compliance Addendum (added 2026-05-13 via Zenodo Edit; ...
   ```
   (Note: in source view, the `&lt;` etc are the actual stored content.)
6. **Delete** that entire broken block (from `<p>&lt;hr&gt;</p>` through
   the last `&lt;/p&gt;` of the addendum).
7. **Paste** the clean HTML block from §3 of this file (verbatim, in source
   view — angle brackets stay as `<` not `&lt;`).
8. Click the source-view toggle again to switch back to WYSIWYG. The
   rendering should now show:
   - A horizontal rule
   - An H3 heading "S154 Compliance Addendum (added 2026-05-13...)"
   - Three bold sub-labels
   - Three clickable DOI links
9. **Save Draft** → review preview → **Publish**.

### If you can't find the source toggle

- Try clicking inside the description, then look at the rightmost toolbar
  buttons.
- Try the keyboard shortcut `Ctrl+Shift+H` or `Alt+0` (TinyMCE defaults).
- If still not visible, skip to §4 (WYSIWYG manual formatting) or §5 (API).

---

## §3 — Clean HTML payload for source view

Paste everything between BEGIN/END markers when in source view:

```
=== BEGIN PAYLOAD (paste in source view ONLY) ===

<hr>
<h3>S154 Compliance Addendum (added 2026-05-13 via Zenodo Edit; per slot 154 verdict bridge HEAD 4761392 / slot 186 runbook)</h3>
<p>This record was deposited 2026-05-04, before the S154 compliance amendment overlay was introduced (slot 154 verdict 2026-05-10; slot 186 runbook 2026-05-11). The following clarifications are added retrospectively for governance-trail completeness:</p>
<p><strong>Mathematical-content vs formalization tooling-state firewall (per discrepancy D-153-3).</strong> The results in this note concern the Borel-singularity radius for polynomial continued fractions and lie wholly within the M1-M9 mathematical-content axis. They make no claims about the state of any Lean-4 formalization of these results; the M10 formalization tooling-state axis is documented separately at <a href="https://github.com/papanokechi/wallis-pcf-lean4">github.com/papanokechi/wallis-pcf-lean4</a> with a SCOPE.md document declaring an OPTIONAL UPLIFT pathway and a 2026-08-02 report deadline.</p>
<p><strong>M8b sub-leading Stokes constant caveat.</strong> This note's universality claims pertain to the Borel-singularity radius (a topological / analytic-continuation invariant) and not to sub-leading Stokes constants. The M8b sub-leading constant analysis carries a PERMANENT_RESIDUAL caveat documented in bridge session T1-SYNTH-M8B-RATIFICATION-CASCADE-ABSORPTION-130R; readers interested in Stokes-constant universality should consult that source rather than this note.</p>
<p><strong>Reproduction note.</strong> This is a 6-page summary/announcement note; the underlying computations are reproduced in companion artefacts: PCF-1 v1.3 (<a href="https://doi.org/10.5281/zenodo.19937196">10.5281/zenodo.19937196</a>), PCF-2 v1.4 (<a href="https://doi.org/10.5281/zenodo.20114315">10.5281/zenodo.20114315</a>), and Umbrella v2.2 (<a href="https://doi.org/10.5281/zenodo.20114861">10.5281/zenodo.20114861</a>).</p>

=== END PAYLOAD ===
```

---

## §4 — Fallback A: WYSIWYG manual formatting (if no source toggle)

If the source-view toggle is missing, build the addendum using the
WYSIWYG toolbar buttons:

1. In WYSIWYG mode, **delete** the entire broken addendum (the block that
   starts `<hr>` and `<h3>S154 Compliance Addendum...` — all of it).
2. Place cursor at the end of the AI Disclosure paragraph.
3. Press **Enter** to start a new line/paragraph.
4. (Optional) Insert a horizontal rule via toolbar (often a `—` or `HR` icon).
5. Press Enter again. **Type or paste** the heading text *without any
   formatting characters*:
   ```
   S154 Compliance Addendum (added 2026-05-13 via Zenodo Edit; per slot 154 verdict bridge HEAD 4761392 / slot 186 runbook)
   ```
6. Select that line. In the WYSIWYG **paragraph-style dropdown** (often
   showing "Paragraph" or "Normal"), choose **Heading 3** (or H3).
7. Press Enter, then paste the body paragraph:
   ```
   This record was deposited 2026-05-04, before the S154 compliance amendment overlay was introduced (slot 154 verdict 2026-05-10; slot 186 runbook 2026-05-11). The following clarifications are added retrospectively for governance-trail completeness:
   ```
8. Press Enter, paste:
   ```
   Mathematical-content vs formalization tooling-state firewall (per discrepancy D-153-3). The results in this note concern...
   ```
   Then **select the first sentence ending in `(per discrepancy D-153-3).`**
   and click the **Bold** button (B).
9. Add a hyperlink: select `github.com/papanokechi/wallis-pcf-lean4`, click
   the **link icon** (often a chain), paste `https://github.com/papanokechi/wallis-pcf-lean4`, click OK.
10. Repeat for the M8b paragraph (bold the leading label).
11. Repeat for the Reproduction note paragraph (bold the leading label;
    add three DOI links).
12. **Save Draft → review → Publish.**

This is more tedious but bypasses any source-view absence.

---

## §5 — Fallback B: REST API PUT (operator with API token)

If you have a Zenodo personal access token (https://zenodo.org/account/settings/applications/),
the description can be updated directly via the API. This is the most
reliable path because it skips the WYSIWYG editor entirely.

### PowerShell snippet

```powershell
# Set your Zenodo API token (DO NOT commit this to git):
$ZenodoToken = "<your-personal-access-token>"

# Fetch the current record and its deposition ID:
$record = Invoke-RestMethod -Uri "https://zenodo.org/api/records/20015923"
$depositionId = 20015923  # same numeric ID

# Get the editable deposition (requires Edit permission on the record):
$dep = Invoke-RestMethod -Uri "https://zenodo.org/api/deposit/depositions/$depositionId" `
    -Headers @{Authorization = "Bearer $ZenodoToken"}

# Build the new description with the addendum appended.
# Start from the existing description, strip the prior broken addendum,
# then append the clean HTML block:
$current = $dep.metadata.description
# Locate where to truncate. The broken Pass-2 addendum starts at "<p>&lt;hr&gt;</p>"
# Adjust as needed by inspecting $current.
$cleanBase = $current -replace '<p>&lt;hr&gt;</p>.*$', ''

$addendum = @'
<hr>
<h3>S154 Compliance Addendum (added 2026-05-13 via Zenodo Edit; per slot 154 verdict bridge HEAD 4761392 / slot 186 runbook)</h3>
<p>This record was deposited 2026-05-04, before the S154 compliance amendment overlay was introduced (slot 154 verdict 2026-05-10; slot 186 runbook 2026-05-11). The following clarifications are added retrospectively for governance-trail completeness:</p>
<p><strong>Mathematical-content vs formalization tooling-state firewall (per discrepancy D-153-3).</strong> The results in this note concern the Borel-singularity radius for polynomial continued fractions and lie wholly within the M1-M9 mathematical-content axis. They make no claims about the state of any Lean-4 formalization of these results; the M10 formalization tooling-state axis is documented separately at <a href="https://github.com/papanokechi/wallis-pcf-lean4">github.com/papanokechi/wallis-pcf-lean4</a> with a SCOPE.md document declaring an OPTIONAL UPLIFT pathway and a 2026-08-02 report deadline.</p>
<p><strong>M8b sub-leading Stokes constant caveat.</strong> This note's universality claims pertain to the Borel-singularity radius (a topological / analytic-continuation invariant) and not to sub-leading Stokes constants. The M8b sub-leading constant analysis carries a PERMANENT_RESIDUAL caveat documented in bridge session T1-SYNTH-M8B-RATIFICATION-CASCADE-ABSORPTION-130R; readers interested in Stokes-constant universality should consult that source rather than this note.</p>
<p><strong>Reproduction note.</strong> This is a 6-page summary/announcement note; the underlying computations are reproduced in companion artefacts: PCF-1 v1.3 (<a href="https://doi.org/10.5281/zenodo.19937196">10.5281/zenodo.19937196</a>), PCF-2 v1.4 (<a href="https://doi.org/10.5281/zenodo.20114315">10.5281/zenodo.20114315</a>), and Umbrella v2.2 (<a href="https://doi.org/10.5281/zenodo.20114861">10.5281/zenodo.20114861</a>).</p>
'@

$newDescription = $cleanBase.TrimEnd() + "`n" + $addendum

# Build PUT payload (preserve other metadata fields verbatim):
$updatedMetadata = $dep.metadata
$updatedMetadata.description = $newDescription

$body = @{ metadata = $updatedMetadata } | ConvertTo-Json -Depth 10 -Compress

# PUT update:
Invoke-RestMethod -Uri "https://zenodo.org/api/deposit/depositions/$depositionId" `
    -Method PUT `
    -Headers @{Authorization = "Bearer $ZenodoToken"; "Content-Type" = "application/json"} `
    -Body $body

# Publish:
Invoke-RestMethod -Uri "https://zenodo.org/api/deposit/depositions/$depositionId/actions/publish" `
    -Method POST `
    -Headers @{Authorization = "Bearer $ZenodoToken"}
```

⚠️ **Caveats:**
- Edit-without-new-version requires Zenodo's "Edit" action which preserves the
  DOI; pass-1 and pass-2 confirm Zenodo allowed this. The API path used here
  may require the record to be in "draft" state via the deposit API.
- If the API returns 403 or refuses to edit, fall back to §2 or §4.
- DO NOT commit the API token to git. Use environment variable
  `$env:ZENODO_TOKEN` and read it at runtime.

---

## §6 — Verification checklist for operator post-Publish

After Publish, verify on the Zenodo public page (https://zenodo.org/records/20015923):

- [ ] **No `&lt;`, `&gt;`, or `&amp;`** visible anywhere in the addendum (would indicate HTML-escape bug returned)
- [ ] **No `###`, `**`, `<h3>`, `<strong>`** visible as literal text
- [ ] Date in heading reads `2026-05-13`
- [ ] "S154 Compliance Addendum" heading renders larger/bolder than body text
- [ ] Three sub-section labels render as bold (no literal `**` or `<strong>`)
- [ ] `github.com/papanokechi/wallis-pcf-lean4` is a clickable hyperlink
- [ ] Three companion DOIs are clickable hyperlinks
- [ ] Horizontal rule visible above the addendum heading
- [ ] Record DOI still `10.5281/zenodo.20015923` (no new version minted)
- [ ] Concept DOI still `10.5281/zenodo.19996689`

If any verification fails after pass-3, halt and escalate; do not run pass-4
without diagnosing the failure mode.

---

## §7 — Post-fix SQL close

```sql
UPDATE todos
SET status='done',
    description = description || ' | RESOLVED 2026-05-13 via fix-pass-3 Zenodo Edit on record 20015923; S154 addendum renders correctly; no new version DOI minted; v2.1 grandfathering preserved.'
WHERE id='opportunistic-option-c-d2-note-edit';
```

(Pending operator confirmation of pass-3 success.)

---

**End fix-pass-2 payload.**
