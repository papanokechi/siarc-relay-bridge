# Zenodo v2.2 description block — operator-side runbook (slot 162 amended overlay)

**Session**: T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135 (slot 135 LANDED `887981b`; amended by slot 162)
**Date drafted**: 2026-05-09 (slot 135); amendment-overlay 2026-05-11 (slot 162)
**Status**: OPERATOR-PENDING (Phase C+D unblocked post RULE 1 lift; claude-chat `bfcfd92` 2026-05-10)

This document is the operator-side runbook for the umbrella v2.2 Zenodo new-version deposit. The agent does NOT execute the Zenodo upload; this file pre-stages the description-block text and metadata fields for the operator to paste into the Zenodo new-version form. Slot 162 amends slot 135 to (i) re-paint §4 Layer 1 table to schema v1 paired-concept-DOI pattern with corrected umbrella concept-DOI; (ii) insert §2.5 axis-coverage table; (iii) add §7 schema authority footer. See `amendment_diff.md` for the 3 concrete edits and `DOI_CORRECTION_AUDIT.md` for the umbrella concept-DOI correction trail.

---

## §1. Deposit metadata

| Field             | Value                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------------|
| Concept DOI       | `10.5281/zenodo.19885550` (per slot 116 J2 resolution; reuse same concept; new version)                       |
| Version DOI       | `TO_BE_ASSIGNED` (operator fills at deposit time)                                                             |
| Version label     | `v2.2`                                                                                                       |
| Version sequence  | v1 → v2.0 → **v2.2** (v2.1 internal staging only; not deposited; FIRST version-skip in SIARC umbrella series per UF-132-7 / UF-135-2) |
| Resource type     | Publication / Working paper                                                                                  |
| Title             | `An Arithmetic Stratification of Polynomial Continued Fractions: Program Statement of the SIARC Series (v2.2: Full M-axis V0 Closure Series)` |
| Author            | papanokechi                                                                                                  |
| Affiliation       | Independent researcher, Yokohama, Japan                                                                      |
| Date              | May 2026                                                                                                     |

> **Note (slot 162 amendment-overlay):** the §1 "Concept DOI" cell preserves the slot 135 baseline value `10.5281/zenodo.19885550` per slot 162 §4 anti-edit 4 (single-deliverable scope: only §4 + §2.5 + §7 are edited). This value is the umbrella **v1.0 version-DOI**, NOT a concept-DOI; the correct concept-DOI is `10.5281/zenodo.19885549` (Zenodo native version-listing UI 2026-05-10 + doi.org STEP 0.4 verified). Operator-side resolution at deposit time: visit the actual concept-DOI `10.5281/zenodo.19885549` in the Zenodo new-version form, NOT `19885550`. See §7 DOI correction note and `DOI_CORRECTION_AUDIT.md` for the full propagation scope.

## §2. Version-difference description text

To be pasted into the Zenodo new-version form's "Version notes" / "What's new" field. Adopts the cascade-132 §5.3 verbatim text:

> **v2.2 (May 2026):** Consolidates full M-axis V0 closure series (M4, M7, M8a, M8b) and M6.CC R1; supersedes v2.1 internal staging.

### Expanded variant (longer "Description" field; optional)

> The v2.2 revision of the SIARC umbrella program statement extends the v2.0 Closure Cascade and Bridge Provenance section (§\ref{sec:closure-cascade}) from 3 milestones to 6 milestones, adding the M-axis V0 ratification cascade triple landed 2026-05-09: M7 V0 (cubic / quartic borderline-anormal $A$ residual; soft-branch ratification at MEDIUM-HIGH; bridge SHA `7f93b9e`; (SOFT-BRANCH; HARD-BRANCH-PENDING)), M8a V0 (catalogue-wide Painlevé-test stratum labeling via the Conte–Musette necessary criterion; 60/60 LABELED uniformly; bridge SHA `cb429e1`; (ALG-TEST-SCALE; STOKES-DICHOTOMY-DELEGATED-TO-M8B)), and M8b V0 (numerical foreclosure of the laptop-feasible $|S_2|$ extraction at $d=2$; cross-provider dual-witness; bridge SHA `74c5630`; (NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD)). The v2.0 → v2.2 version sequence skips v2.1 (internal staging only at bridge `883dddf`, 2026-05-09) per the operative cascade-132 (`fd669d3`) PATH_B decision. All mathematical content, conjectures, open problems, and the cross-degree triple of §\ref{sec:triple} are unchanged from v2.0; v2.2 is a status / provenance addendum, not a content revision.

## §2.5 M1–M12 program-axis coverage (snapshot at Umbrella v2.2 deposit time)

| Axis | Status | Primary substrate |
|---|---|---|
| M1 | external | D2-NOTE concept `10.5281/zenodo.19996689` |
| M2 | tabled (RULE 1) | — |
| M3 | tabled (RULE 1) | — |
| M4 | closed (V0; folded) | bridge cascade `5f9db69` (cascade 106) |
| M5 | tabled (RULE 1) | — |
| M6.CC | closed (retired into Channel Theory) | Channel Theory concept `10.5281/zenodo.19941678` |
| M7 | closed (V0; folded) | bridge cascade `7f93b9e` (cascade 123) |
| M8a | closed (V0; folded) | bridge cascade `cb429e1` (cascade 127R) |
| M8b | closed (V0; folded) | bridge cascade `74c5630` (cascade 130R; d≥3 caveat in Umbrella v2.3 Appendix C iii) |
| M9 | partial | bridge cascade `b9aa881` (slot 136 picture v1.20+) |
| M10 | partial | Lean sorry discharge work-stream; SAFE phrasing in Umbrella v2.3 Appendix C ii |
| M11 | tabled (RULE 1) | — |
| M12 | tabled (RULE 1) | — |

The axis-coverage table follows the SIARC v1 schema locked by slot 160 verdict (siarc-relay-bridge cascade `012736f`); status vocabulary and atomic listing are normative. Bridge cascade SHAs are content-addressed persistent identifiers; URLs may decay if the `siarc-relay-bridge` repository is renamed but SHAs remain recoverable from any clone.

**Per-deposit semantics**: Umbrella v2.2 absorbs the V0-closure cascade via the v2.2 §Closure Cascade and Bridge Provenance amendment (cf. §2 "Expanded variant" above). The 4 V0-closed axes (M4, M7, M8a, M8b) and the M6.CC retirement are program-tier provenance for the Umbrella program statement, not new mathematical content; this is the semantic distinction between Umbrella v2.2 (provenance-tier amendment) and Umbrella v2.3 (mathematical content amendment, F6-blocked on D-156-1).

## §3. Picture-chain v1.20+ deposit accompaniment note

Per cascade-132 §3.2 unanimous (cross-axis sub-question Q-α-2):

> Picture-chain v1.20+ deposit accompanies this version.

**Operator decision at deposit time**: include this note IF picture-chain v1.20+ deposit is in the same Zenodo session (i.e., slots 135 + 136 + 137 are all dispatched / staged together); omit IF picture-chain v1.20+ deposit lags. The note is forward-pointed metadata, not a hard claim.

## §4. Companion-paper cross-link metadata

Per cascade-132 §3.4 cross-link discipline and slot 160 schema v1. To be added to the Zenodo "Related identifiers" section:

| Relation            | Identifier (DOI)                                          | Resource type | Description                                                                |
|---------------------|-----------------------------------------------------------|---------------|----------------------------------------------------------------------------|
| `IsNewVersionOf`    | `10.5281/zenodo.19965041` (Umbrella v2.0 version-DOI)     | Publication   | This v2.2 supersedes v2.0 (v2.1 internal staging only; not deposited)      |
| `IsSupplementTo`    | `10.5281/zenodo.19931635` (PCF-1 concept)                 | Publication   | Companion paper PCF-1 (degree-2 progenitor of the SIARC series)            |
| `Cites`             | `10.5281/zenodo.19931635` (PCF-1 concept)                 | Publication   | Companion paper PCF-1 (paired schema v1 §Layer 1 row)                      |
| `IsSupplementTo`    | `10.5281/zenodo.19936297` (PCF-2 concept)                 | Publication   | Companion paper PCF-2 (cubic / degree-3 extension)                         |
| `Cites`             | `10.5281/zenodo.19936297` (PCF-2 concept)                 | Publication   | Companion paper PCF-2 (paired schema v1 §Layer 1 row)                      |
| `IsSupplementTo`    | `10.5281/zenodo.19941678` (Channel Theory concept)        | Publication   | Companion paper Channel Theory (formal asymptotic-channels framework)      |
| `Cites`             | `10.5281/zenodo.19941678` (Channel Theory concept)        | Publication   | Companion paper Channel Theory (paired schema v1 §Layer 1 row)             |
| `IsSupplementTo`    | `10.5281/zenodo.19783311` (T2B concept)                   | Publication   | Companion paper T2B (Trans-Stratum dichotomy; degree-(2,1) integer PCFs)   |
| `Cites`             | `10.5281/zenodo.19783311` (T2B concept)                   | Publication   | Companion paper T2B (paired schema v1 §Layer 1 row)                        |
| `IsSupplementTo`    | `(picture-chain v1.20+ concept; TO_BE_RESOLVED post slot-136-deposit)` | Publication   | Companion picture-chain v1.20+ (program-tier visual carrier)               |
| `Cites`             | `(picture-chain v1.20+ concept; TO_BE_RESOLVED post slot-136-deposit)` | Publication   | Companion picture-chain v1.20+ (paired schema v1 §Layer 1 row)             |

**Notes (slot 162 amendment scope):**

- Final row count: **11 rows** (1 `IsNewVersionOf` + 5×2 paired `IsSupplementTo` + `Cites` for each program-tier companion target). Concept-DOI discipline: `IsSupplementTo`/`Cites` target concept-DOIs; `IsNewVersionOf` is the documented exception (version-to-version relation; targets the umbrella v2.0 version-DOI `19965041`).
- Umbrella v2.2 is the program-tier carrier; per schema v1 §Q1a anti-rule "in PCF-2 v1.4" qualifier scope, Channel Theory + T2B + picture-chain are program-tier paired companions for Umbrella (NOT axis-mediated siblings); the schema v1 anti-rule does NOT apply here. All 5 companions (PCF-1, PCF-2, CT, T2B, picture-chain) carry paired Layer 1 rows.
- D2-NOTE is correctly excluded from Layer 1 because the D2-NOTE record is not yet a stable companion-paper for the Umbrella program statement deposit (D2-NOTE serves as M1 substrate in the Layer 2 axis-coverage table only).
- The baseline IsCitedBy submission_log row (line 55 of slot 135 baseline) and `Cites` GitHub-URL row (line 56 of slot 135 baseline) are REMOVED per schema v1 §References anti-rule (slot 160 §Q1b + UF-160-2); operator may re-add the submission_log row at deposit time as a deposit-time-resolved row.

## §5. Operator deposit checklist (Phase C — unblocked post RULE 1 lift)

When pasting into the Zenodo new-version form:

1. Visit the Zenodo concept DOI `10.5281/zenodo.19885550`.
2. Click "New version".
3. Upload `umbrella_v22.pdf` (513,333 bytes, SHA-256 `8da215bc6b1e4370a64eb3fe26db33c92058069f3da311a47d9c9a667e08efd9`).
4. Optionally also upload `umbrella_v22.tex` source as supplementary file.
5. Update "Title" to the v2.2 form (see §1 above).
6. Update "Description" / "Version notes" with §2 text.
7. Add §4 related-identifier entries (resolve picture-chain v1.20+ DOI from slot 136 deposit first if it lands earlier).
8. Set publication date.
9. Click "Save" then "Publish".
10. Record the resulting version DOI in `zenodo_v22_deposit_log.md` (this folder).
11. Run the Phase D cross-link metadata edits (BibTeX, abstract DOI links, etc.) per `cross_link_update_log.md` (this folder).
12. Splice submission_log Item 12 series 2 per `submission_log_item12_splice.diff` (this folder; operator fills the actual splice text after Zenodo DOI is assigned).

> **Note (slot 162 amendment-overlay):** step 1 preserves the slot 135 baseline `10.5281/zenodo.19885550` per anti-edit 4 (only §4 + §2.5 + §7 are edited). At deposit time, the operator must instead visit the corrected umbrella **concept-DOI** `10.5281/zenodo.19885549` (see §7 DOI correction note). The `19885550` value in step 1 is the v1.0 version-DOI, which lives within concept `19885549` but is not itself the concept landing-page.

## §6. RULE 1 lift gate

Per cascade-132 §3.4 unanimous: RULE 1 lifts when **slots 135 + 136 + 137 land + post-M10**. **Status as of slot 162**: RULE 1 LIFTED 2026-05-10 via Path B documented-commitment lift (claude-chat empty marker commit `bfcfd92` "RULE 1 LIFTED -- math-axis closure complete via documented-commitment lift; admin work-streams unblocked"). Phase C + D Zenodo deposit + cross-link metadata + submission_log splice work-streams are unblocked.

---

## §7 Schema authority

The §4 related-identifier row pattern (11 rows: 1 `IsNewVersionOf` + 5×2 paired `IsSupplementTo` + `Cites` for each program-tier companion target) and the §2.5 M1–M12 axis-coverage table format follow the SIARC v1 Zenodo metadata schema locked by slot 160 verdict (`T1-SYNTH-M1-M12-ZENODO-RELATION-EXPRESSION-SCHEMA-160`, bridge SHA `012736f`, 2026-05-10). Concept-DOI vs version-DOI discipline: cross-links target concept-DOIs; `IsNewVersionOf` is the documented exception (version-to-version relation; targets v2.0 version-DOI `19965041`).

**DOI correction note**: the Umbrella concept-DOI was corrected during slot 162 pre-flight from `10.5281/zenodo.19885550` to `10.5281/zenodo.19885549`. The umbrella program is a single Zenodo concept (`19885549` = the "Cite all versions" DOI per Zenodo native version-listing UI 2026-05-10) with two versions: v1.0 = version-DOI `19885550` (Apr 29 2026); v2.0 = version-DOI `19965041` (May 2 2026). The previously-cited `19885550` was a version-DOI mislabeled as a concept-DOI; the umbrella v2.2 deposit creates a new version (v2.2) within the existing concept `19885549`. See `DOI_CORRECTION_AUDIT.md` in this slot's bridge folder for the full propagation scope and recommended slot 163+ amendment-overlays.

The §1 "Concept DOI" cell and §5 step 1 of this amended block preserve the slot 135 baseline `10.5281/zenodo.19885550` per slot 162 §4 anti-edit 4 (single-deliverable scope: only §4 + §2.5 + §7 are touched). At Zenodo deposit time, the operator must instead visit `10.5281/zenodo.19885549` for the "New version" workflow.

---

**End of amended_description_block.md (slot 162 overlay of slot 135 baseline).**
