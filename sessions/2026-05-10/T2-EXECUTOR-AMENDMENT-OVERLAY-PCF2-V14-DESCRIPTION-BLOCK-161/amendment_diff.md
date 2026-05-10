# Amendment diff — slot 137 baseline → slot 161 amended

**Baseline:** `siarc-relay-bridge/sessions/2026-05-09/T2-EXECUTOR-PCF2-V14-M7-V0-AMENDMENT-PREP-137/zenodo_v14_description_block.md` at bridge SHA `45e236c`.
**Amended:** `amended_description_block.md` (this folder).
**Schema authority:** Slot 160 verdict bridge `012736f`.
**Format:** unified-diff style, human-audit oriented (NOT machine-applied; baseline is immutable LANDED).

---

## Edit 1 — Layer 1 row count 3 → 5 (paired Umbrella rows)

```diff
@@ §2 Related identifiers (table body) @@
 | `IsNewVersionOf` | `10.5281/zenodo.19963298` (PCF-2 v1.3)    | Publication   | This v1.4 amendment supersedes v1.3                               |
 | `IsSupplementTo` | `10.5281/zenodo.19931635` (PCF-1 concept) | Publication   | Cubic extension of the PCF-1 framework (degree-2 progenitor)      |
 | `Cites`          | `10.5281/zenodo.19931635` (PCF-1 concept) | Publication   | PCF-1 v1.3 §5 d=2 split (sole known anomaly to Conjecture B4)     |
+| `IsSupplementTo` | `10.5281/zenodo.19885550` (Umbrella concept) | Publication   | PCF-2 v1.4 supplements the SIARC umbrella program (Option α' deposit cascade per slot 157 §Q4b) |
+| `Cites`          | `10.5281/zenodo.19885550` (Umbrella concept) | Publication   | Umbrella program-statement carrier (axis-coverage cross-references) |
```

**Authority:** slot 160 verdict §Q1a "Add `Cites 10.5281/zenodo.19885550 Umbrella concept` alongside the new `IsSupplementTo` row, mirroring the PCF-1 pattern (both `IsSupplementTo` and `Cites` for the same target). This is symmetric with row 2/3 and lossless."

**Discipline notes:**
- Both new rows target the Umbrella concept-DOI (`19885550`), NOT a version-DOI. Concept-DOI discipline preserved.
- Pattern mirrors rows 2-3 (PCF-1 paired).
- Note: column-width adjustment in the column-2 header row was applied (`Identifier (DOI)` column padded from 41 chars to 44 chars to accommodate the longer "(Umbrella concept)" annotation). No semantic change; this is a markdown rendering hygiene adjustment.

---

## Edit 2 — Layer 2 axis-coverage table inserted in Description markdown

```diff
@@ §2 Description markdown block (inside fenced ```markdown ... ``` block) @@
 **Companion documents**:
 - PCF-1 v1.3 (concept DOI `10.5281/zenodo.19931635`) — degree-2 progenitor.
 - Umbrella v2.2 (forthcoming, deposited second per cascade-132 Option α).
 - Picture-chain v1.20+ (forthcoming, deposited third per cascade-132 Option α).
+
+---
+
+**M1–M12 program-axis coverage (snapshot at PCF-2 v1.4 deposit time):**
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
 ```
```

**Authority:** slot 160 verdict §Q2a (anchor-deposits-carry-table) + §Q2b (locked 7-status vocabulary) + §Q2c (atomic M1-M12 listing).

**Discipline notes:**
- Inserted INSIDE the `\`\`\`markdown` fenced block (so it pastes verbatim into Zenodo's description field with markdown rendering preserved).
- Status values use the locked vocabulary verbatim (`closed (V0; folded)` / `closed (retired into Mx)` / `partial` / `external` / `tabled (RULE 1)`). No `not in scope` axes in this snapshot.
- Cascade SHAs cited in prose-tier (table cell text), NOT as Layer 1 References rows (per slot 160 §Q1b anti-rule).
- Atomic M1-M12 listing — RULE-1-tabled axes (M2, M3, M5, M11, M12) listed individually per §Q2c.

---

## Edit 3 — Schema authority citation footer

```diff
@@ §2 Related identifiers, after parenthetical operator note, before §2 Communities @@
 (Operator: when umbrella v2.2 and picture-chain v1.20+ are deposited, their PCF-2-v1.4 cross-link rows go onto **their** records, not this one. PCF-2 v1.4's record only points back to the PCF-1 concept DOI and to the PCF-2 v1.3 prior version.)
+
+**Schema authority**: the related-identifiers row pattern (5 rows; paired `IsSupplementTo` + `Cites` for each cross-link target) and the M1–M12 axis-coverage table format follow the SIARC v1 Zenodo metadata schema locked by slot 160 verdict (`T1-SYNTH-M1-M12-ZENODO-RELATION-EXPRESSION-SCHEMA-160`, bridge SHA `012736f`, 2026-05-10). Concept-DOI vs version-DOI discipline: cross-links target concept-DOIs; `IsNewVersionOf` is the documented exception (version-to-version relation; targets v1.3 version-DOI `19963298`).

 ### Communities
```

**Authority:** slot 160 amendment_overlay_targets.md Target 2 §3 ("Add schema citation at the bottom of the axis-coverage section: 'Axis-coverage table follows the SIARC v1 schema locked by slot 160 verdict (`<slot 160 bridge SHA>`).'"), expanded to also cite the row-pattern authority and concept-DOI discipline rule.

**Discipline notes:**
- Cites slot 160 by Task ID + bridge SHA + date — three independent identifiers for stable citation.
- Documents the IsNewVersionOf concept-DOI exception inline (per slot 160 §Q1c).

---

## Anti-edits applied (per slot 161 §4)

The following changes were CONSIDERED and DECLINED:

- **No** new rows for Channel Theory (`19941678`), D2-NOTE (`19996689`), or picture v1.19 — all axis-mediated, lives in Layer 2 (per slot 160 §Q1a anti-rule).
- **No** modification of §1 Concept-DOI / version-DOI taxonomy section.
- **No** modification of Title, Authors, Files-to-upload, §3 Post-deposit operator actions sections.
- **No** cascade-SHA References rows (per slot 160 §Q1b).
- **No** modification of the slot 137 baseline file at bridge `45e236c` (LANDED bridge artifact; immutable).
- **No** modification of any v1.3 mathematical content (max |δ_lin| = 3.09 × 10^{-23}; PSLQ 17-member basis; etc.) — preserved verbatim.
- **No** amendment of the parenthetical operator note at line 117 ("PCF-2 v1.4's record only points back to the PCF-1 concept DOI and to the PCF-2 v1.3 prior version") — this is now stale relative to the new 5-row pattern but flagged as `UF-161-2 LOW` for follow-up rather than amended inline (sticking strictly to slot 161 §3 prescribed 3 edits).

---

## Edit count

**Total edits applied: 3** (matches §8 Invariant I8 expectation).

## Byte delta summary

| Section | Baseline (45e236c) | Amended (slot 161) | Delta |
|---|---|---|---|
| Header status note | 1 sentence | 1 sentence + slot 161 amendment provenance addendum | +~150 chars |
| Description markdown axis-coverage table | absent | 12-row table + paragraph | +~1200 chars |
| Related identifiers table | 3 data rows | 5 data rows | +2 rows / +~250 chars |
| Schema authority footer | absent | 1 paragraph | +~500 chars |

(Approximate; not byte-precise. SHA-256 hashes of the two files are recorded in `claims.jsonl`.)
