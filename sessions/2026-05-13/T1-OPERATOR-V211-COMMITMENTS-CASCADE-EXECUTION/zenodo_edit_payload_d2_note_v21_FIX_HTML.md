# Zenodo Edit FIX-PASS — D2-NOTE v2.1 addendum rendering correction

**Date:** 2026-05-13 ~15:38 JST
**Target record:** D2-NOTE v2.1 (`10.5281/zenodo.20015923`)
**Prior Edit:** 2026-05-13 15:37:22 UTC (description-only; no new version DOI minted)
**Status:** 🟡 OPERATOR FIX-EDIT PENDING

---

## §1 — Why a fix-pass is needed

The first Edit pass (operator-executed 2026-05-13 ~15:37 JST) successfully
appended the addendum text content to the description, but three rendering
issues are visible on the public record:

1. Date placeholder `2026-05-DD` never replaced with `2026-05-13`.
2. The `###` Markdown heading marker renders as literal `### S154 Compliance Addendum...` text rather than as a bold/large heading.
3. The `**...**` Markdown bold markers render as literal `**Mathematical-content vs...**` text rather than as bold.

Root cause: Zenodo's description field accepts **HTML, not Markdown**.
Pasting raw Markdown causes each paragraph to be wrapped in `<p>...</p>`
by Zenodo's sanitizer, but the inline Markdown delimiters survive
as plain text.

Apologies for the wrong-format payload in §3 of the prior file
(`zenodo_edit_payload_d2_note_v21.md`). This file replaces it for the
fix-pass.

---

## §2 — Browser steps for operator

1. Navigate to `https://zenodo.org/records/20015923` while logged in as the
   record owner.
2. Click **Edit** (top-right of record header).
3. Scroll to the **Description** field.
4. **Locate the addendum** — find the line that begins:
   ```
   ### S154 Compliance Addendum (added 2026-05-DD via Zenodo Edit; per
   ```
5. **Select** from `### S154 Compliance Addendum` through the end of the
   description (everything from the Markdown-broken heading down to the
   final companion-artefact citation). Delete this selection.
6. Place cursor at the end of the AI Disclosure paragraph (just after
   "...takes full responsibility for the content of this article.").
7. Paste the HTML block from §3 verbatim. The cursor should be in HTML
   mode (most Zenodo editors accept raw HTML in the description field).
8. Click **Save Draft**.
9. Review the rendered preview; confirm:
   - The `S154 Compliance Addendum` heading renders as a styled heading (`<h3>`)
   - Three bold sub-labels render as bold (`<strong>`)
   - The date reads `2026-05-13` not `2026-05-DD`
   - Three companion-DOI links render as `<a href="https://doi.org/...">` (clickable)
10. Click **Publish** (this should NOT mint a new version DOI; description-only
    edits typically don't trigger versioning).

---

## §3 — HTML replacement payload

Copy everything BETWEEN the BEGIN PAYLOAD and END PAYLOAD markers below:

```
=== BEGIN PAYLOAD ===

<hr>

<h3>S154 Compliance Addendum (added 2026-05-13 via Zenodo Edit; per slot 154 verdict bridge HEAD 4761392 / slot 186 runbook)</h3>

<p>This record was deposited 2026-05-04, before the S154 compliance amendment overlay was introduced (slot 154 verdict 2026-05-10; slot 186 runbook 2026-05-11). The following clarifications are added retrospectively for governance-trail completeness:</p>

<p><strong>Mathematical-content vs formalization tooling-state firewall (per discrepancy D-153-3).</strong> The results in this note concern the Borel-singularity radius for polynomial continued fractions and lie wholly within the M1-M9 mathematical-content axis. They make no claims about the state of any Lean-4 formalization of these results; the M10 formalization tooling-state axis is documented separately at <a href="https://github.com/papanokechi/wallis-pcf-lean4">github.com/papanokechi/wallis-pcf-lean4</a> with a SCOPE.md document declaring an OPTIONAL UPLIFT pathway and a 2026-08-02 report deadline.</p>

<p><strong>M8b sub-leading Stokes constant caveat.</strong> This note's universality claims pertain to the Borel-singularity radius (a topological / analytic-continuation invariant) and not to sub-leading Stokes constants. The M8b sub-leading constant analysis carries a PERMANENT_RESIDUAL caveat documented in bridge session T1-SYNTH-M8B-RATIFICATION-CASCADE-ABSORPTION-130R; readers interested in Stokes-constant universality should consult that source rather than this note.</p>

<p><strong>Reproduction note.</strong> This is a 6-page summary/announcement note; the underlying computations are reproduced in companion artefacts: PCF-1 v1.3 (<a href="https://doi.org/10.5281/zenodo.19937196">10.5281/zenodo.19937196</a>), PCF-2 v1.4 (<a href="https://doi.org/10.5281/zenodo.20114315">10.5281/zenodo.20114315</a>), and Umbrella v2.2 (<a href="https://doi.org/10.5281/zenodo.20114861">10.5281/zenodo.20114861</a>).</p>

=== END PAYLOAD ===
```

Payload length: ≈2.1 KB (well under Zenodo description-field limit).

---

## §4 — Differences from the prior (broken) payload

| Element | Prior payload | This payload |
|---|---|---|
| Format | Markdown (`### ...`, `**bold**`, `---`) | HTML (`<h3>`, `<strong>`, `<hr>`) |
| Date | `2026-05-DD` placeholder | Hardcoded `2026-05-13` (the canonical Edit date) |
| Companion DOIs | Plain text | `<a href="https://doi.org/...">` clickable links |
| GitHub repo URL | Plain text `github.com/papanokechi/...` | `<a href="https://github.com/...">` clickable link |
| Section break | Triple `---` rules | Single `<hr>` at top only |

---

## §5 — Verification checklist for operator post-Publish

After Publish, verify on the Zenodo public page:

- [ ] Date in heading reads `2026-05-13`, not `2026-05-DD`
- [ ] "S154 Compliance Addendum" heading renders larger/bolder than body text
- [ ] Three sub-section labels render as bold (no literal `**`)
- [ ] No `###` or `**` characters appear anywhere in the addendum text
- [ ] `github.com/papanokechi/wallis-pcf-lean4` is a clickable link
- [ ] Three companion DOIs (PCF-1 / PCF-2 / Umbrella) are clickable links
- [ ] Horizontal rule visible above the addendum heading
- [ ] No new version DOI minted; record DOI remains `10.5281/zenodo.20015923`
- [ ] Concept DOI remains `10.5281/zenodo.19996689`

---

## §6 — Fallback / abort criteria

1. **Zenodo strips `<a>` tags** (sanitizer too aggressive). Fallback: re-Edit
   with plain-text DOIs (no `<a>` wrapper); still use `<h3>`, `<strong>`,
   `<hr>` for structure.
2. **Zenodo strips `<h3>` tags**. Fallback: use `<p><strong>` for the
   heading instead.
3. **Description field is in WYSIWYG mode only** (no HTML toggle visible).
   Manual fix: select the broken `### S154...` text, apply heading style via
   toolbar; select each `**...**` substring, apply bold via toolbar; manually
   replace `2026-05-DD` text with `2026-05-13`.
4. **Edit somehow mints a new version DOI**. No problem; record both the
   old (`20015923`) and new version DOIs. The concept DOI (`19996689`)
   remains stable. Update the SQL close note with both.

---

## §7 — Post-fix-Edit follow-up actions

1. SQL close: `UPDATE todos SET status='done' WHERE id='opportunistic-option-c-d2-note-edit';`
   (closing on successful fix-Edit; the broken-render Edit doesn't count as
   "done" since the rendering issues defeat the purpose of formal section labels.)
2. Optional bridge follow-up slot
   `T2-EXECUTOR-M1-D2-NOTE-S154-ADDENDUM-FIX-LANDED` if operator wants a
   tracked audit-trail entry. Otherwise SQL update only.

---

**End fix-Edit payload.**
