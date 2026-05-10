# Amendment diff — slot 163+164 combined DOI-correction amendment-overlay

**Targets:** 2 LANDED post-slot-160 amendment-overlay artefacts (slot 160 `locked_schema_v1.md` + slot 161 `amended_description_block.md`).
**Edit pattern:** Single string substitution `19885550` → `19885549` (umbrella v1.0 version-DOI → umbrella concept-DOI).
**Edit count:** 5 line changes total (3 in Target A schema + 2 in Target B PCF-2 v1.4 block).
**Ground truth:** Zenodo native version-listing UI sidebar (operator paste 2026-05-10 21:43:37 JST) + doi.org STEP 0.4 pre-resolve cited from slot 162 audit (bridge SHA `9271d74`).
**Authority:** slot 162 `DOI_CORRECTION_AUDIT.md` §1.1; slot 162 D-162-1 HIGH discrepancy.

---

## Edit A1 — `locked_schema_v1_corrected.md` line 20

```diff
@@ -18,5 +18,5 @@ schema (Anchor deposits table)
 | PCF-1 | `10.5281/zenodo.19931635` | yes (next version) |
 | PCF-2 | `10.5281/zenodo.19936297` | yes (v1.4 onward) |
-| Umbrella | `10.5281/zenodo.19885550` | yes (v2.3 onward) |
+| Umbrella | `10.5281/zenodo.19885549` | yes (v2.3 onward) |
 | Channel Theory | `10.5281/zenodo.19941678` | yes (next version) |
 | D2-NOTE | `10.5281/zenodo.19996689` | yes (next version) |
```

**Authority:** Umbrella concept-DOI per Zenodo sidebar paste 2026-05-10 21:43:37 JST: "Cite all versions? You can cite all versions by using the DOI 10.5281/zenodo.19885549."

## Edit A2+A3 — `locked_schema_v1_corrected.md` lines 40+41

```diff
@@ -38,6 +38,6 @@ ### Reference row pattern (PCF-2 v1.4 instance, 5 rows)
 IsNewVersionOf  10.5281/zenodo.19963298    PCF-2 v1.3 (version-DOI; exception)
 IsSupplementTo  10.5281/zenodo.19931635    PCF-1 concept
 Cites           10.5281/zenodo.19931635    PCF-1 concept
-IsSupplementTo  10.5281/zenodo.19885550    Umbrella concept
-Cites           10.5281/zenodo.19885550    Umbrella concept
+IsSupplementTo  10.5281/zenodo.19885549    Umbrella concept
+Cites           10.5281/zenodo.19885549    Umbrella concept
 ```
```

**Authority:** Concept-DOI discipline per slot 160 schema v1 §Discipline ("IsSupplementTo / Cites / IsDocumentedBy / References MUST target concept-DOIs, not version-DOIs"). Umbrella concept = `19885549`, NOT `19885550`.

## Edit B1+B2 — `amended_description_block_corrected.md` lines 138+139

```diff
@@ -136,6 +136,6 @@ ### Related identifiers (paste each row into the Zenodo `Related identifiers` table)
 | `IsSupplementTo` | `10.5281/zenodo.19931635` (PCF-1 concept)    | Publication   | Cubic extension of the PCF-1 framework (degree-2 progenitor)      |
 | `Cites`          | `10.5281/zenodo.19931635` (PCF-1 concept)    | Publication   | PCF-1 v1.3 §5 d=2 split (sole known anomaly to Conjecture B4)     |
-| `IsSupplementTo` | `10.5281/zenodo.19885550` (Umbrella concept) | Publication   | PCF-2 v1.4 supplements the SIARC umbrella program (Option α' deposit cascade per slot 157 §Q4b) |
-| `Cites`          | `10.5281/zenodo.19885550` (Umbrella concept) | Publication   | Umbrella program-statement carrier (axis-coverage cross-references) |
+| `IsSupplementTo` | `10.5281/zenodo.19885549` (Umbrella concept) | Publication   | PCF-2 v1.4 supplements the SIARC umbrella program (Option α' deposit cascade per slot 157 §Q4b) |
+| `Cites`          | `10.5281/zenodo.19885549` (Umbrella concept) | Publication   | Umbrella program-statement carrier (axis-coverage cross-references) |
 
 (Operator: when umbrella v2.2 and picture-chain v1.20+ are deposited, their PCF-2-v1.4 cross-link rows go onto **their** records, not this one. PCF-2 v1.4's record only points back to the PCF-1 concept DOI and to the PCF-2 v1.3 prior version.)
```

**Authority:** Concept-DOI discipline per slot 160 schema v1 §Discipline. The (slot 161) parenthetical at line 141 is non-DOI-bearing and out of slot 163+164 scope (UF-161-1 still applies; not amended here).

---

## Outside the diff (deliberately preserved)

- Target A §Q1c IsNewVersionOf exception text (preserves `19965041` umbrella v2.0 version-DOI as the documented exception target; correct as-is).
- Target B §1 Deposit metadata + §5 manual checklist (inherited from slot 137 baseline; UF-162-1-class residuals; out of slot 163+164 scope per anti-edit 4 inheritance).
- Slot 162 `amended_description_block.md` (already correct via slot 162 fire; out of scope).
- All other LANDED predecessors (immutable).

---

## Bytes changed

| Target | Lines edited | Bytes net | Hash before | Hash after |
|---|---|---|---|---|
| `locked_schema_v1_corrected.md` | 3 (lines 20, 40, 41) | 0 (1-digit substitution; no length change) | `b0b1b325efac…` (origin) | (post-edit hash captured in claims.jsonl I5) |
| `amended_description_block_corrected.md` | 2 (lines 138, 139) | 0 (1-digit substitution; no length change) | `aa56a04311…` (origin) | (post-edit hash captured in claims.jsonl I4) |

Total: 5 line changes; 0 bytes net (single-digit `0` → `9` substitution; length preserved).

---

**End of amendment_diff.md.**
