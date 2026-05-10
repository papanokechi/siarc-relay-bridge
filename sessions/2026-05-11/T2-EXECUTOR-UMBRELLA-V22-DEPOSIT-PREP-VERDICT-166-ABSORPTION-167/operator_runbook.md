# Operator Runbook — Umbrella v2.2 Zenodo Deposit (slot 167; verdict-166-α1 9-row path)

**Authority**: slot 166 synth verdict V3 + slot 167 absorption refinements
**Target deposit**: SIARC Umbrella v2.2 (program statement provenance addendum)
**Target Zenodo concept**: `10.5281/zenodo.19885549`
**Expected version DOI**: TO_BE_ASSIGNED at deposit time
**Cascade-132 Step**: 2 of 3 (Step 1 = PCF-2 v1.4 LANDED 2026-05-11; Step 3 = picture-chain v1.20+ pending)
**Paste-source**: `amended_description_block_v2.md` (this slot 167 folder)

---

## Phase A — Pre-fire DOI sidebar verification

**Open each URL in a browser tab; verify the live Zenodo sidebar matches the expected concept-vs-version status before initiating the deposit.**

| # | DOI                                  | Expected sidebar state                                                                                          | Status |
|---|--------------------------------------|------------------------------------------------------------------------------------------------------------------|--------|
| 1 | `10.5281/zenodo.19931635` (PCF-1 concept) | Sidebar shows "Concept DOI" label; latest version block lists v1.3 = `19937196`                              | ☐ verify |
| 2 | `10.5281/zenodo.19936297` (PCF-2 concept) | Sidebar shows v1.4 = `20114315` as latest version (confirms cascade Step 1 landed; confirms `19936297` is concept, not v1.0) | ☐ verify |
| 3 | `10.5281/zenodo.19941678` (Channel Theory concept) | Concept-DOI label; latest version v1.3                                                                  | ☐ verify |
| 4 | `10.5281/zenodo.19783311` (T2B concept) | Concept-DOI label (anti-pattern flag: NOT `19783312` which would be v1.0 version-DOI); latest version v3.0      | ☐ verify |
| 5 | `10.5281/zenodo.19885549` (Umbrella concept) | Concept-DOI label; latest version v2.0 = `19965041`                                                       | ☐ verify |
| 6 | `10.5281/zenodo.19965041` (Umbrella v2.0 version-DOI) | Specific v2.0 page; this is the IsNewVersionOf target                                            | ☐ verify |

**Halt condition for Phase A**: if any sidebar shows a single-digit-substitution mismatch against the substrate (e.g., `19783311` resolves to v1.0 instead of concept), HALT and re-fire as I4 single-digit anti-pattern incident report.

---

## Phase B — Field-by-field paste sequence

1. **Initiate "New version" from umbrella v2.0 record (`19965041`)**:
   - Visit https://zenodo.org/records/19965041 (NOT the concept page; the v2.0 page specifically)
   - Verify the record shown is "An Arithmetic Stratification ... v2.0" by papanokechi
   - Click "New version" button (top-right of record page)
   - Zenodo will auto-populate IsNewVersionOf row in the new draft

2. **Confirm IsNewVersionOf auto-population**:
   - Scroll to Related-identifiers section in new draft
   - Verify the auto-populated row reads: `IsNewVersionOf` → `10.5281/zenodo.19965041` (Publication / Preprint)
   - **HALT if it instead shows `19885549` (concept-DOI)** — would indicate Zenodo schema change requiring re-consultation. The IsNewVersionOf exception targets the **immediate predecessor version-DOI**, not the concept.

3. **Update Title field**:
   - Replace v2.0 title with: `An Arithmetic Stratification of Polynomial Continued Fractions: Program Statement of the SIARC Series (v2.2: Full M-axis V0 Closure Series)`

4. **Update Version label**: `v2.2`

5. **Update Resource type**: `Publication / Preprint` (NOT "Working paper"; chain-consistent with PCF-2 v1.4 revision-4 state)

6. **Update Publication date**: May 2026 (or specific deposit-day date per operator preference)

7. **Update Description field** (paste from `amended_description_block_v2.md` §2 expanded variant + §2.1 γ2 footnote + §2.5 axis-coverage table; format as HTML or Markdown per Zenodo TinyMCE editor; see PCF-2 v1.4 revision-4 for HTML conversion precedent including TinyMCE artifacts that are functionally fine).

8. **Update Version notes field** (if a separate field exists): paste §2 short form ("v2.2 (May 2026): Consolidates full M-axis V0 closure series ...").

9. **Add 8 paired-row block to Related-identifiers** (deposit at 9 rows total = 1 auto-populated IsNewVersionOf + 8 paired):
   - Row 2: `IsSupplementTo` → `10.5281/zenodo.19931635` (Publication) — Companion paper PCF-1
   - Row 3: `Cites` → `10.5281/zenodo.19931635` (Publication) — Companion paper PCF-1 paired
   - Row 4: `IsSupplementTo` → `10.5281/zenodo.19936297` (Publication) — Companion paper PCF-2
   - Row 5: `Cites` → `10.5281/zenodo.19936297` (Publication) — Companion paper PCF-2 paired
   - Row 6: `IsSupplementTo` → `10.5281/zenodo.19941678` (Publication) — Companion paper Channel Theory
   - Row 7: `Cites` → `10.5281/zenodo.19941678` (Publication) — Companion paper Channel Theory paired
   - Row 8: `IsSupplementTo` → `10.5281/zenodo.19783311` (Publication) — Companion paper T2B
   - Row 9: `Cites` → `10.5281/zenodo.19783311` (Publication) — Companion paper T2B paired
   - **DO NOT** add picture-chain v1.20+ rows at this stage per slot 166 verdict α1.

10. **Verify Related-identifier row count = 9**. HALT if >9 or <9.

11. **Upload file**: `umbrella_v22.pdf` (513,333 bytes, SHA-256 `8da215bc6b1e4370a64eb3fe26db33c92058069f3da311a47d9c9a667e08efd9`).
    - Optionally also upload `umbrella_v22.tex` as supplementary file.
    - Pre-existing slot 135 deliverables at `siarc-relay-bridge/sessions/2026-05-09/T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135/`.

12. **Final pre-publish review**:
    - Scroll Related-identifiers, confirm zero rows contain placeholder text, bridge SHAs, or version-DOIs other than `19965041`.
    - Confirm no rows reference picture-chain v1.20+.
    - Confirm title + version label + resource type all reflect v2.2 state.

13. **Click "Save" then "Publish"**.

14. **Record the resulting version DOI** (will be of the form `10.5281/zenodo.NNNNNNNN`) for next-step bookkeeping.

---

## Phase C — Post-publish bookkeeping (within same operator session)

1. **Capture deposit metadata** to a follow-up bridge slot (slot 168 or operator-discretion):
   - Version DOI
   - Publication timestamp
   - Zenodo internal revision number (1 at fresh publish)
   - File-upload sidebar count (should be 1 PDF + optional TeX)

2. **Splice submission_log Item 12 series 2** (umbrella v2.2 entry) per pattern established by submission_log Item 11 series 2 (PCF-2 v1.4; slot 165). Operator fills the actual splice text post-publication. Splice template lives in slot 135 `submission_log_item12_splice.diff` (placeholder TBD).

3. **Update cross-link metadata** (Phase D in slot 162 baseline §5 step 11):
   - BibTeX entries in companion papers' source `.tex` referencing umbrella v2.2
   - Abstract DOI link in any HTML/web mirrors
   - Update slot 162 baseline status: amend `OPERATOR-PENDING` → `LANDED` via a follow-up bridge fire (NOT in-place edit to slot 162 itself).

---

## Phase D — Deferred post-publish Edit (when picture-chain v1.20+ lands)

**Trigger**: picture-chain v1.20+ Zenodo deposit is independently fired and its concept-DOI is minted.

**Action**: revisit the published umbrella v2.2 Zenodo record → "Edit metadata" → append 2 paired rows:
- `IsSupplementTo` → `<picture-chain v1.20+ concept-DOI>` (Publication) — Companion picture-chain v1.20+
- `Cites` → `<picture-chain v1.20+ concept-DOI>` (Publication) — Companion picture-chain v1.20+ paired

**Save**. NO DOI bump (metadata-only Edit per D2-NOTE v2.1 precedent 2026-05-04). Terminal Related-identifier row count: 11.

**Pre-flight check for Phase D fire**:
- UF-167-1 schema-ambiguity surface should be resolved before this Edit. If interpretation (B) of slot 160 §Layer 1 anti-rule is canonical, this Edit must NOT happen; terminal count stays at 9. Fire a confirmation consultation if a definitive resolution is desired before Edit.

---

## Halt conditions (summary)

- **H1**: Phase A sidebar verification single-digit-substitution mismatch → halt + I4 incident report.
- **H2**: Phase B step 2 IsNewVersionOf auto-population shows concept-DOI instead of version-DOI → halt + re-consult.
- **H3**: Phase B step 10 row count ≠ 9 → halt; do not retry with placeholder substitution.
- **H4**: Live PCF-2 v1.4 record (`20114315`) shows as withdrawn or draft during Phase B step 7 paste → halt; the §2.1 γ2 footnote becomes incorrect.
- **H5**: Any sidebar in Phase A shows a record-not-found error → halt + investigate.

---

**End of `operator_runbook.md` (slot 167 verdict-166-V3 absorption).**
