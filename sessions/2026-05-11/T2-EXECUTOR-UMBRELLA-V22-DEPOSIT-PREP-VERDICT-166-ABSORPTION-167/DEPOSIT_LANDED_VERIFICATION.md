# Deposit Landed — Umbrella v2.2 Zenodo Verification

**Date verified:** 2026-05-11 09:30 JST
**Live record:** https://zenodo.org/records/20114861
**Concept DOI:** 10.5281/zenodo.19885549 (resolves to latest)
**Version DOI:** 10.5281/zenodo.20114861 (v2.2 immutable)
**Revision:** 3 (operator made minor edits during draft)
**Status:** PUBLISHED · cascade-132 Option α Step 2 LANDED · 1 HIGH post-Edit required

---

## ✅ Field-by-field verification vs slot 167 spec

| Field | Expected (slot 167 spec) | Actual (live) | Status |
|---|---|---|---|
| Title | "An Arithmetic Stratification...Program Statement of the SIARC Series (v2.2: Full M-axis V0 Closure Series)" | matches verbatim | ✅ |
| Version | "2.2" | "2.2" | ✅ |
| Publication date | 2026-05-11 | 2026-05-11 | ✅ |
| Resource type | Preprint (publication/preprint) | Preprint (publication/preprint) | ✅ chain-consistent with PCF-2 v1.4 |
| License | cc-by-4.0 | cc-by-4.0 | ✅ |
| Access | open | open | ✅ |
| Creators | papanokechi (Independent Researcher) | papanokechi (Independent Researcher) | ✅ |
| Concept DOI | 19885549 | 19885549 | ✅ (slot 163-164 correction applied) |
| Files | umbrella_v22.pdf | umbrella_v22.pdf (513,333 B) + umbrella_v22.tex (63,815 B; source bonus) | ✅ |

## ✅ Related-identifiers — all 9 rows perfect per verdict 166 α1

| # | Relation | Target | Verdict spec | Live | Status |
|---|---|---|---|---|---|
| 1 | isNewVersionOf | 10.5281/zenodo.19965041 (v2.0 version-DOI) | ✓ immediate predecessor | ✓ | ✅ operator successfully edited Zenodo's auto-populated v1.0 (`19885550`) per RUNBOOK_ADDENDUM |
| 2 | isSupplementTo | 10.5281/zenodo.19931635 (PCF-1 concept) | paired | ✓ | ✅ |
| 3 | cites | 10.5281/zenodo.19931635 (PCF-1 concept) | paired | ✓ | ✅ |
| 4 | isSupplementTo | 10.5281/zenodo.19936297 (PCF-2 concept) | paired | ✓ | ✅ |
| 5 | cites | 10.5281/zenodo.19936297 (PCF-2 concept) | paired | ✓ | ✅ |
| 6 | isSupplementTo | 10.5281/zenodo.19941678 (CT concept) | paired | ✓ | ✅ |
| 7 | cites | 10.5281/zenodo.19941678 (CT concept) | paired | ✓ | ✅ |
| 8 | isSupplementTo | 10.5281/zenodo.19783311 (T2B concept) | paired | ✓ | ✅ |
| 9 | cites | 10.5281/zenodo.19783311 (T2B concept) | paired | ✓ | ✅ |

All 9 rows have `resource_type = publication-preprint`. ✅
Picture-chain v1.20+ rows (would have been #10 + #11) correctly STRIPPED per verdict α1 STRIP-AT-DEPOSIT; reserved for post-publish Edit per verdict V3 post-publish-action upon picture-chain concept-DOI mint.

## 🚨 D-167-3 (HIGH) — Description body anomaly

See `discrepancy_log.json`. **Operator pasted entire meta-document verbatim into Description field.** The Zenodo record currently displays:
- `# Zenodo-Clean Description Body — Umbrella v2.2 (slot 167 addendum)` (header)
- `**Date**: 2026-05-11 09:15 JST · **Parent slot**: 167 (bridge SHA 3f0377a)` (meta)
- `Part A — Plain-prose mirror` + `Part B — TinyMCE HTML-ready mirror` + `Part C — Diff log` (3-part wrapper)
- "Operator paste workflow" instructions
- `**End of ZENODO_CLEAN_DESCRIPTION_BODY.md.**`

**The actual umbrella description content IS embedded** (inside Part B's `<code>html</code>` fences) but TinyMCE rendered the code-fences as literal text rather than as live HTML.

### Fix path (~2 minutes)

1. Open https://zenodo.org/records/20114861 → "Edit" button (top right)
2. Scroll to Description field
3. Switch to source-view (Tools → Source code, or `<>` icon)
4. SELECT ALL existing content → DELETE
5. Open `ZENODO_DESCRIPTION_DROPIN_FIX.html` (this folder)
6. Copy ONLY the content between `<!-- BEGIN_PASTE -->` and `<!-- END_PASTE -->` markers
7. Paste into Zenodo Description source-view
8. Switch back to WYSIWYG → verify table renders, italics on A/S/d look right, blockquote indents §2.1
9. Save → Publish

**Zenodo behavior**: revision count bumps from 3 → 4. Version DOI `20114861` UNCHANGED. Concept DOI `19885549` UNCHANGED. This is a metadata-only Edit per D2-NOTE v2.1 precedent (2026-05-04).

## ⚠️ D-167-1 (MED) + D-167-2 (LOW) — PDF substrate corrigenda

See `discrepancy_log.json` for full detail. **PDF body** (umbrella_v22.tex line 851 + 849) contains cosmetic mismatches:
- Line 851: cites `19885550` (v1.0 version-DOI) as "concept" instead of `19885549`
- Line 849: cites Channel Theory v1.2 (`19951331`) instead of v1.3 (`19972394`)

**Both cosmetic-tier** — Zenodo machine-readable related-identifiers (correct) take precedence over PDF body for cross-reference resolution. Recommendation: fold corrections into Umbrella v2.3 (forthcoming mathematical-content revision) rather than rebuild + re-upload PDF now.

If operator wants pristine substrate-trail, the rebuild path is:
```
cd tex\submitted\umbrella_program_paper
# Edit umbrella_v22.tex lines 849, 851
pdflatex umbrella_v22.tex   # x2 for cross-refs
# Re-upload PDF via Zenodo Edit (metadata-only; no DOI bump)
```

Fold with the D-167-3 fix into one Edit session if pursued.

---

## Cascade-132 Option α deposit chain — 2/3 LANDED

- Step 1: PCF-2 v1.4 (`10.5281/zenodo.20114315`, 2026-05-11) ✅
- Step 2: Umbrella v2.2 (`10.5281/zenodo.20114861`, 2026-05-11) ✅ ← THIS DEPOSIT
- Step 3: Picture-chain v1.20+ (concept-DOI not yet minted; substrate-prep at bridge `b9aa881`) ⏳

Upon Step 3 landing:
- Splice 2 paired rows into Umbrella v2.2 record via post-publish Zenodo Edit (per verdict V3 post-publish action + V4 propagation rules)
- Verify reciprocal-citation completeness: Umbrella v2.2 terminal row count → 11; Picture-chain v1.20+ → contains paired `IsSupplementTo` + `Cites` → `10.5281/zenodo.19885549` (umbrella concept-DOI)

## RULE 1 lift gate status

Per the operator's 2026-05-09 ~11:17 JST instruction, admin/distribution work TABLED until M1-M12 mathematical/foundational closure complete. Hard SHA gate status:
- 4/4 hard SHAs met: 135 (`887981b`) + 136 (`b9aa881`) + 137 (`45e236c`) + 138 (`2b5b94e`)
- M10 resolution: still operator-pending (separate-axis V0 closure cascade mirroring 123/127R/130R 3-arc template, OR bundled with M9)

Step 2 deposit landing does NOT affect the gate; the gate is mathematical-axis-tier, not deposit-tier.

---

## Recommended operator action ordering

1. **NOW** (2 min) — Fix D-167-3 using `ZENODO_DESCRIPTION_DROPIN_FIX.html`
2. **Optional** (5 min) — Fold D-167-1 + D-167-2 PDF rebuild into the same Edit session if pristine substrate-trail desired
3. **Later** (operator gate) — Resolve M10 status taxonomy → RULE 1 lift → cascade-132 Option α Step 3 (picture-chain v1.20+ deposit)
4. **Final** — Post-publish Edit splice picture-chain rows into Umbrella v2.2 (11-row terminal state)
