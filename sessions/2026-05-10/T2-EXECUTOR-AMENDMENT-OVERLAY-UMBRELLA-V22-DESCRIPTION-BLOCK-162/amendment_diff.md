# Slot 162 — amendment-overlay diff (slot 135 baseline → slot 162 amended block)

**Baseline:** `siarc-relay-bridge/sessions/2026-05-09/T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135/zenodo_v22_description_block.md` at bridge SHA `887981bf51860550a05ff949f0145c1687623689`.
**Amended overlay:** `amended_description_block.md` in this slot's folder.
**Edits applied:** 3 (Edit 1 / Edit 2 / Edit 3).
**Scope:** §4 Layer 1 re-paint + §2.5 insertion + §7 footer addition. §1, §2, §3, §5, §6 preserved per anti-edit 4.

The diff is for human audit; the baseline file at `887981b` is NOT modified (LANDED bridge artefacts are immutable). The slot 135 baseline persists as-is at its commit; slot 162 produces a parallel `amended_description_block.md` that an operator can copy-paste at Zenodo deposit time.

---

## Edit 1 — §4 Layer 1 table re-paint (8 rows → 11 rows; concept-DOI discipline + paired pattern + GitHub-URL-row removed)

**Locate:** §4 "Companion-paper cross-link metadata" table (lines 47-56 in baseline).

```
--- a/zenodo_v22_description_block.md   (slot 135 baseline / 887981b)
+++ b/amended_description_block.md       (slot 162 overlay)
@@ §4 Companion-paper cross-link metadata @@
-| Relation            | Identifier                                                          | Description                                                  |
-|---------------------|---------------------------------------------------------------------|--------------------------------------------------------------|
-| `IsNewVersionOf`    | `10.5281/zenodo.19885550` (concept DOI)                            | umbrella v1 / v2.0 (v2.1 internal staging; not deposited)     |
-| `IsSupplementTo`    | `10.5281/zenodo.19937196` (PCF-1 v1.3)                             | Companion paper PCF-1 v1.3                                    |
-| `IsSupplementTo`    | `10.5281/zenodo.19963298` (PCF-2 v1.3 — REPLACE WITH v1.4 IF v1.4 IS DEPOSITED FIRST PER CASCADE-132 §3.1 UNANIMOUS OPTION α) | Companion paper PCF-2 (v1.3 or v1.4)                          |
-| `IsSupplementTo`    | `10.5281/zenodo.19951331` (Channel Theory v1.2)                    | Companion paper CT v1.2                                        |
-| `IsSupplementTo`    | `10.5281/zenodo.19915689` (T2B v3.0)                               | Companion paper T2B v3.0                                       |
-| `IsSupplementTo`    | `(picture-chain v1.20+ DOI; TO_BE_ASSIGNED at slot 136 deposit)`   | Picture-chain v1.20+                                          |
-| `IsCitedBy`         | `(submission_log Item 12 series 2; if applicable)`                 | Operator splice at deposit time                                |
-| `Cites` (bridge)    | `https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-09/T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135/` | Bridge session for this fire (substrate-prep)                  |
+| Relation            | Identifier (DOI)                                          | Resource type | Description                                                                |
+|---------------------|-----------------------------------------------------------|---------------|----------------------------------------------------------------------------|
+| `IsNewVersionOf`    | `10.5281/zenodo.19965041` (Umbrella v2.0 version-DOI)     | Publication   | This v2.2 supersedes v2.0 (v2.1 internal staging only; not deposited)      |
+| `IsSupplementTo`    | `10.5281/zenodo.19931635` (PCF-1 concept)                 | Publication   | Companion paper PCF-1 (degree-2 progenitor of the SIARC series)            |
+| `Cites`             | `10.5281/zenodo.19931635` (PCF-1 concept)                 | Publication   | Companion paper PCF-1 (paired schema v1 §Layer 1 row)                      |
+| `IsSupplementTo`    | `10.5281/zenodo.19936297` (PCF-2 concept)                 | Publication   | Companion paper PCF-2 (cubic / degree-3 extension)                         |
+| `Cites`             | `10.5281/zenodo.19936297` (PCF-2 concept)                 | Publication   | Companion paper PCF-2 (paired schema v1 §Layer 1 row)                      |
+| `IsSupplementTo`    | `10.5281/zenodo.19941678` (Channel Theory concept)        | Publication   | Companion paper Channel Theory (formal asymptotic-channels framework)      |
+| `Cites`             | `10.5281/zenodo.19941678` (Channel Theory concept)        | Publication   | Companion paper Channel Theory (paired schema v1 §Layer 1 row)             |
+| `IsSupplementTo`    | `10.5281/zenodo.19783311` (T2B concept)                   | Publication   | Companion paper T2B (Trans-Stratum dichotomy; degree-(2,1) integer PCFs)   |
+| `Cites`             | `10.5281/zenodo.19783311` (T2B concept)                   | Publication   | Companion paper T2B (paired schema v1 §Layer 1 row)                        |
+| `IsSupplementTo`    | `(picture-chain v1.20+ concept; TO_BE_RESOLVED post slot-136-deposit)` | Publication   | Companion picture-chain v1.20+ (program-tier visual carrier)               |
+| `Cites`             | `(picture-chain v1.20+ concept; TO_BE_RESOLVED post slot-136-deposit)` | Publication   | Companion picture-chain v1.20+ (paired schema v1 §Layer 1 row)             |
```

**Notes:**
- 5 version-DOI references replaced with concept-DOI equivalents per schema v1 §Layer 1 paired-pattern (umbrella `19885550` → not in this table; PCF-1 `19937196` → `19931635`; PCF-2 `19963298` → `19936297`; CT `19951331` → `19941678`; T2B `19915689` → `19783311`).
- 5 paired `IsSupplementTo` + `Cites` rows added per schema v1 §Layer 1 paired-pattern (1 pair per program-tier companion: PCF-1 / PCF-2 / CT / T2B / picture-chain).
- 1 row dropped: `IsCitedBy` submission_log row (operator may re-add at deposit time as a deposit-time-resolved row).
- 1 row dropped: `Cites` (bridge) GitHub URL row (per schema v1 §References anti-rule / slot 160 §Q1b + UF-160-2; SHA citations stay in Description-body prose only).
- 1 row corrected: `IsNewVersionOf` target `19885550` → `19965041` per schema v1 §Q1c (umbrella v2.0 version-DOI is the v2.2 predecessor; the previously-cited `19885550` is umbrella v1.0 version-DOI, mislabeled as concept-DOI in baseline; see DOI_CORRECTION_AUDIT.md).
- Net row count: 8 → 11 (+3 net: -2 dropped + 5 paired companion rows added).

---

## Edit 2 — Insert §2.5 axis-coverage table (12 rows: M1–M12)

**Locate:** between current §2 "Version-difference description text" (lines 25-33; including the "Expanded variant" subsection) and §3 "Picture-chain v1.20+ deposit accompaniment note" (line 35).

```
--- a/zenodo_v22_description_block.md   (slot 135 baseline / 887981b)
+++ b/amended_description_block.md       (slot 162 overlay)
@@ between §2 and §3 @@
+
+## §2.5 M1–M12 program-axis coverage (snapshot at Umbrella v2.2 deposit time)
+
+| Axis | Status | Primary substrate |
+|---|---|---|
+| M1 | external | D2-NOTE concept `10.5281/zenodo.19996689` |
+| M2 | tabled (RULE 1) | — |
+| M3 | tabled (RULE 1) | — |
+| M4 | closed (V0; folded) | bridge cascade `5f9db69` (cascade 106) |
+| M5 | tabled (RULE 1) | — |
+| M6.CC | closed (retired into Channel Theory) | Channel Theory concept `10.5281/zenodo.19941678` |
+| M7 | closed (V0; folded) | bridge cascade `7f93b9e` (cascade 123) |
+| M8a | closed (V0; folded) | bridge cascade `cb429e1` (cascade 127R) |
+| M8b | closed (V0; folded) | bridge cascade `74c5630` (cascade 130R; d≥3 caveat in Umbrella v2.3 Appendix C iii) |
+| M9 | partial | bridge cascade `b9aa881` (slot 136 picture v1.20+) |
+| M10 | partial | Lean sorry discharge work-stream; SAFE phrasing in Umbrella v2.3 Appendix C ii |
+| M11 | tabled (RULE 1) | — |
+| M12 | tabled (RULE 1) | — |
+
+The axis-coverage table follows the SIARC v1 schema locked by slot 160 verdict (siarc-relay-bridge cascade `012736f`); status vocabulary and atomic listing are normative. Bridge cascade SHAs are content-addressed persistent identifiers; URLs may decay if the `siarc-relay-bridge` repository is renamed but SHAs remain recoverable from any clone.
+
+**Per-deposit semantics**: Umbrella v2.2 absorbs the V0-closure cascade via the v2.2 §Closure Cascade and Bridge Provenance amendment (cf. §2 "Expanded variant" above). The 4 V0-closed axes (M4, M7, M8a, M8b) and the M6.CC retirement are program-tier provenance for the Umbrella program statement, not new mathematical content; this is the semantic distinction between Umbrella v2.2 (provenance-tier amendment) and Umbrella v2.3 (mathematical content amendment, F6-blocked on D-156-1).
```

**Notes:** 12 data rows (M1, M2, M3, M4, M5, M6.CC, M7, M8a, M8b, M9, M10, M11, M12) — note M6.CC is the canonical M6 row name (M6 base axis is retired-into-CT) and M11+M12 are tabled, so 12 axis rows = full M1–M12 coverage. Status vocabulary {external, closed (V0; folded), closed (retired into Channel Theory), partial, tabled (RULE 1)} matches slot 160 schema v1 atomic listing. Bridge cascade SHAs are 7-char short-hash cited as content-addressed identifiers.

---

## Edit 3 — Add §7 schema authority footer

**Locate:** below §6 "RULE 1 lift gate" (line 79; end of file). The new §7 is the final section.

```
--- a/zenodo_v22_description_block.md   (slot 135 baseline / 887981b)
+++ b/amended_description_block.md       (slot 162 overlay)
@@ after §6 RULE 1 lift gate; before "End of" line @@
+
+## §7 Schema authority
+
+The §4 related-identifier row pattern (11 rows: 1 `IsNewVersionOf` + 5×2 paired `IsSupplementTo` + `Cites` for each program-tier companion target) and the §2.5 M1–M12 axis-coverage table format follow the SIARC v1 Zenodo metadata schema locked by slot 160 verdict (`T1-SYNTH-M1-M12-ZENODO-RELATION-EXPRESSION-SCHEMA-160`, bridge SHA `012736f`, 2026-05-10). Concept-DOI vs version-DOI discipline: cross-links target concept-DOIs; `IsNewVersionOf` is the documented exception (version-to-version relation; targets v2.0 version-DOI `19965041`).
+
+**DOI correction note**: the Umbrella concept-DOI was corrected during slot 162 pre-flight from `10.5281/zenodo.19885550` to `10.5281/zenodo.19885549`. The umbrella program is a single Zenodo concept (`19885549` = the "Cite all versions" DOI per Zenodo native version-listing UI 2026-05-10) with two versions: v1.0 = version-DOI `19885550` (Apr 29 2026); v2.0 = version-DOI `19965041` (May 2 2026). The previously-cited `19885550` was a version-DOI mislabeled as a concept-DOI; the umbrella v2.2 deposit creates a new version (v2.2) within the existing concept `19885549`. See `DOI_CORRECTION_AUDIT.md` in this slot's bridge folder for the full propagation scope and recommended slot 163+ amendment-overlays.
+
+The §1 "Concept DOI" cell and §5 step 1 of this amended block preserve the slot 135 baseline `10.5281/zenodo.19885550` per slot 162 §4 anti-edit 4 (single-deliverable scope: only §4 + §2.5 + §7 are touched). At Zenodo deposit time, the operator must instead visit `10.5281/zenodo.19885549` for the "New version" workflow.
```

**Notes:** schema authority cited as slot 160 bridge SHA `012736f` (verified ancestor of `origin/main` at slot 162 STEP 0.2 pre-flight; full 40-char `012736f121b2859ac3d782206ca0261f1332b31e`). DOI correction note enumerates the version-DOI vs concept-DOI distinction. The "DOI correction note" paragraph is the I5-permitted location for the wrong-context quoted `19885550` value (single quoted occurrence in §7; not in §4 anywhere).

---

## Edit summary

| Edit | Section | Type | Lines (baseline) → Lines (amended) |
|---|---|---|---|
| Edit 1 | §4 Layer 1 table | REPLACE 8 rows → 11 rows | 47-56 → corresponding §4 in amended |
| Edit 2 | §2.5 axis-coverage | INSERT new section | (none) → between §2 and §3 in amended |
| Edit 3 | §7 schema authority | INSERT new section | (none) → after §6 in amended |

3 concrete edits applied. §1 Deposit metadata, §2 Version-difference description text + Expanded variant, §3 Picture-chain accompaniment note, §5 Operator deposit checklist, §6 RULE 1 lift gate text are all unchanged per anti-edit 4 (only §4 + §2.5 + §7 are touched).

**End of amendment_diff.md.**
