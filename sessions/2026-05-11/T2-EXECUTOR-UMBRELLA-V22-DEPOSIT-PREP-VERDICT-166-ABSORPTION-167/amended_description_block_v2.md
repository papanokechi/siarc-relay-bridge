# Zenodo v2.2 description block — operator-side runbook (slot 167 verdict-166-absorption overlay)

**Session**: T2-EXECUTOR-UMBRELLA-V22-DEPOSIT-PREP-VERDICT-166-ABSORPTION-167 (parent slot 162 `9271d74`; overlay applies slot 166 synth verdict V1 = α1 + β1 + γ2)
**Date drafted**: 2026-05-11 (slot 167 overlay; based on slot 162 amended block 2026-05-11)
**Status**: OPERATOR-PENDING (Phase C+D unblocked post RULE 1 lift; claude-chat `bfcfd92` 2026-05-10)

This document is the operator-side runbook for the umbrella v2.2 Zenodo new-version deposit. The agent does NOT execute the Zenodo upload; this file pre-stages the description-block text and metadata fields for the operator to paste into the Zenodo new-version form. Slot 167 amends slot 162 to apply slot 166 synth verdict V1 = α1 (STRIP-AT-DEPOSIT for picture-chain v1.20+ Layer 1 rows) + β1 (KEEP cascade-132 Option α ordering) + γ2 (CHANGELOG-FOOTNOTE for deposit-time-pinning prose). See `synth_verdict_166.md` for the verdict capture and `slot_162_amendment_diff.unified` (in this folder) for the concrete edits.

---

## §1. Deposit metadata

| Field             | Value                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------------|
| Concept DOI       | `10.5281/zenodo.19885549` (true concept; corrected by slot 163-164 propagation) |
| Version DOI       | `TO_BE_ASSIGNED` (operator fills at deposit time)                                                             |
| Version label     | `v2.2`                                                                                                       |
| Version sequence  | v1 → v2.0 → **v2.2** (v2.1 internal staging only; not deposited; FIRST version-skip in SIARC umbrella series per UF-132-7 / UF-135-2) |
| Resource type     | Publication / Preprint                                                                                  |
| Title             | `An Arithmetic Stratification of Polynomial Continued Fractions: Program Statement of the SIARC Series (v2.2: Full M-axis V0 Closure Series)` |
| Author            | papanokechi                                                                                                  |
| Affiliation       | Independent researcher, Yokohama, Japan                                                                      |
| Date              | May 2026                                                                                                     |

> **Note (slot 167 amendment-overlay):** §1 "Concept DOI" cell uses the corrected concept-DOI `10.5281/zenodo.19885549` per slot 163-164 DOI correction (`b936eb0`). Slot 162 baseline preserved the original `19885550` (v1.0 version-DOI; mislabeled) per its single-deliverable scope; slot 167 propagates the correction here for operator paste-time clarity. Both deposit workflow (visit concept-DOI before "New version") and §5 step 1 are now consistent.
>
> **Note (Resource type):** slot 162 baseline listed "Working paper"; corrected to "Preprint" here to match PCF-2 v1.4 deposit (operator back-edited PCF-2 v1.4 Resource type from "Working paper" → "Preprint" at revision 4 of `20114315`, observed 2026-05-11). Chain consistency maintained.

## §2. Version-difference description text

To be pasted into the Zenodo new-version form's "Version notes" / "What's new" field. Adopts the cascade-132 §5.3 verbatim text:

> **v2.2 (May 2026):** Consolidates full M-axis V0 closure series (M4, M7, M8a, M8b) and M6.CC R1; supersedes v2.1 internal staging.

### Expanded variant (longer "Description" field; optional)

> The v2.2 revision of the SIARC umbrella program statement extends the v2.0 Closure Cascade and Bridge Provenance section (§\ref{sec:closure-cascade}) from 3 milestones to 6 milestones, adding the M-axis V0 ratification cascade triple landed 2026-05-09: M7 V0 (cubic / quartic borderline-anormal $A$ residual; soft-branch ratification at MEDIUM-HIGH; bridge SHA `7f93b9e`; (SOFT-BRANCH; HARD-BRANCH-PENDING)), M8a V0 (catalogue-wide Painlevé-test stratum labeling via the Conte–Musette necessary criterion; 60/60 LABELED uniformly; bridge SHA `cb429e1`; (ALG-TEST-SCALE; STOKES-DICHOTOMY-DELEGATED-TO-M8B)), and M8b V0 (numerical foreclosure of the laptop-feasible $|S_2|$ extraction at $d=2$; cross-provider dual-witness; bridge SHA `74c5630`; (NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD)). The v2.0 → v2.2 version sequence skips v2.1 (internal staging only at bridge `883dddf`, 2026-05-09) per the operative cascade-132 (`fd669d3`) PATH_B decision. All mathematical content, conjectures, open problems, and the cross-degree triple of §\ref{sec:triple} are unchanged from v2.0; v2.2 is a status / provenance addendum, not a content revision.

### §2.1 Deposit-time companion-artefact snapshot (verdict-166-γ2 footnote)

> **Companion artefact state at deposit time (2026-05-11 JST):** PCF-2 v1.4 (`10.5281/zenodo.20114315`, deposited 2026-05-11; cascade-132 Option α Step 1 landed), Channel Theory v1.3 (`10.5281/zenodo.19972394`, deposited 2026-05-02), T2B v3.0 (`10.5281/zenodo.19915689`, deposited 2026-04-30), PCF-1 v1.3 (`10.5281/zenodo.19937196`, deposited 2026-05-01). Picture-chain v1.20+ deposit pending (substrate-prep at bridge `b9aa881` 2026-05-09; concept-DOI not yet minted); cross-link rows to be spliced via post-publish Zenodo Edit upon picture-chain concept-DOI mint (separate work-stream; cascade-132 Option α Step 3).

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

**Operator decision at deposit time** (per slot 166 verdict β1 KEEP Option α; β3 fallback): omit this §3 note IF picture-chain v1.20+ deposit lags (the default under verdict α1 STRIP-AT-DEPOSIT); include IF picture-chain v1.20+ deposit lands same-day-paired (verdict β3 fallback path). The §2.1 γ2 footnote already conveys the deposit-time state ("Picture-chain v1.20+ deposit pending") regardless of which path is taken.

## §4. Companion-paper cross-link metadata

Per cascade-132 §3.4 cross-link discipline, slot 160 schema v1, and slot 166 verdict V2 (α1 STRIP-AT-DEPOSIT for picture-chain rows). To be added to the Zenodo "Related identifiers" section:

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

**Notes (slot 167 amendment scope, applying slot 166 verdict α1):**

- **Row count at deposit: 9 rows** (1 `IsNewVersionOf` + 4×2 paired `IsSupplementTo` + `Cites` for PCF-1, PCF-2, Channel Theory, T2B concept-DOIs). Picture-chain v1.20+ cross-link pair (2 rows) is **deferred to post-publish Zenodo Edit** per slot 166 verdict α1 (STRIP-AT-DEPOSIT) and V4 propagation rule, pending picture-chain v1.20+ concept-DOI mint (separate substrate-prep work-stream; cascade-132 Option α Step 3 = slot 136 successor; D2-NOTE v2.1 post-publish Edit precedent P4 establishes this is operator-normalized workflow).
- **Post-Edit terminal row count: 11 rows** (above 9 + picture-chain `IsSupplementTo` + `Cites` paired at concept-DOI granularity).
- Concept-DOI discipline (slot 160 schema v1 §Layer 1): `IsSupplementTo`/`Cites` target concept-DOIs; `IsNewVersionOf` is the documented exception (version-to-version relation; targets v2.0 version-DOI `19965041`).
- Umbrella v2.2 is the program-tier carrier; per schema v1 §Q1a anti-rule "in PCF-2 v1.4" qualifier-scope-limited interpretation inherited from slot 162 line 88, Channel Theory + T2B + picture-chain are program-tier paired companions for Umbrella (NOT axis-mediated siblings). All 5 (PCF-1, PCF-2, CT, T2B, picture-chain) carry paired Layer 1 rows; picture-chain pair deferred to post-publish Edit per α1. **Semantic ambiguity flagged at UF-167-1**: the qualifier-scope interpretation is slot 162's contribution, not slot 160 explicit text; before the post-publish Edit fires, operator may wish to fire a confirmation consultation if the schema v1 §Layer 1 anti-rule is read as generalizing to umbrella (in which case the picture-chain post-publish Edit would NOT happen; row-count terminal = 9, not 11).
- D2-NOTE is correctly excluded from Layer 1 because the D2-NOTE record is not yet a stable companion-paper for the Umbrella program statement deposit (D2-NOTE serves as M1 substrate in the Layer 2 axis-coverage table only).
- The baseline IsCitedBy submission_log row and `Cites` GitHub-URL row are REMOVED per schema v1 §References anti-rule (slot 160 §Q1b + UF-160-2); operator may re-add the submission_log row at deposit time as a deposit-time-resolved row.

## §5. Operator deposit checklist (Phase C — unblocked post RULE 1 lift; verdict-166-α1 9-row path)

When pasting into the Zenodo new-version form:

1. Visit the Zenodo concept DOI `10.5281/zenodo.19885549` (corrected concept; NOT `19885550` which is v1.0 version-DOI).
2. Click "New version".
3. Upload `umbrella_v22.pdf` (513,333 bytes, SHA-256 `8da215bc6b1e4370a64eb3fe26db33c92058069f3da311a47d9c9a667e08efd9`).
4. Optionally also upload `umbrella_v22.tex` source as supplementary file.
5. Update "Title" to the v2.2 form (see §1 above).
6. Update "Description" / "Version notes" with §2 text (including §2.1 deposit-time companion-artefact snapshot per γ2 footnote).
7. Add §4 related-identifier entries — **9 rows total** (1 IsNewVersionOf + 4 paired = 8). Picture-chain v1.20+ rows are NOT added at this step per slot 166 verdict α1.
8. Set publication date.
9. Click "Save" then "Publish".
10. Record the resulting version DOI in `zenodo_v22_deposit_log.md` (this folder; template TBD on operator-side fire).
11. Run the Phase D cross-link metadata edits (BibTeX, abstract DOI links, etc.) per `cross_link_update_log.md` (template TBD).
12. Splice submission_log Item 12 series 2 per `submission_log_item12_splice.diff` (template TBD; operator fills the actual splice text after Zenodo DOI is assigned).
13. **Post-publish Edit (deferred)**: when picture-chain v1.20+ Zenodo concept-DOI is minted (separate work-stream), revisit this umbrella v2.2 record → Edit metadata → append 2 paired rows (IsSupplementTo + Cites, picture-chain concept-DOI). Terminal row count: 11. NO DOI bump (metadata-only Edit per P4 D2-NOTE v2.1 precedent).

> **Note (slot 167 amendment-overlay):** step 1 corrects the slot 162 baseline `19885550` → `19885549` per slot 163-164 DOI correction propagation. The `19885550` value is the v1.0 version-DOI, which lives within concept `19885549` but is not itself the concept landing-page.

## §6. RULE 1 lift gate

Per cascade-132 §3.4 unanimous: RULE 1 lifts when **slots 135 + 136 + 137 land + post-M10**. **Status as of slot 167**: RULE 1 LIFTED 2026-05-10 via Path B documented-commitment lift (claude-chat empty marker commit `bfcfd92` "RULE 1 LIFTED -- math-axis closure complete via documented-commitment lift; admin work-streams unblocked"). Phase C + D Zenodo deposit + cross-link metadata + submission_log splice work-streams are unblocked. PCF-2 v1.4 Zenodo deposit (cascade Step 1) LANDED at `10.5281/zenodo.20114315` on 2026-05-11; umbrella v2.2 (cascade Step 2) is this slot 167's deposit target.

---

## §7 Schema authority

The §4 related-identifier row pattern (9 rows at deposit; 11 rows post-Edit terminal: 1 `IsNewVersionOf` + 5×2 paired `IsSupplementTo` + `Cites` for each program-tier companion target) and the §2.5 M1–M12 axis-coverage table format follow the SIARC v1 Zenodo metadata schema locked by slot 160 verdict (`T1-SYNTH-M1-M12-ZENODO-RELATION-EXPRESSION-SCHEMA-160`, bridge SHA `012736f`, 2026-05-10). Concept-DOI vs version-DOI discipline: cross-links target concept-DOIs; `IsNewVersionOf` is the documented exception (version-to-version relation; targets v2.0 version-DOI `19965041`).

**Verdict authority**: slot 166 synth verdict (Claude T1-Synth, 2026-05-11 08:19 JST) chose V1 = α1 (STRIP-AT-DEPOSIT for picture-chain rows; deposit at 9 rows; post-publish Edit to terminal 11) + β1 (KEEP cascade-132 Option α ordering; β3 same-day-pair as fallback) + γ2 (CHANGELOG-FOOTNOTE; see §2.1). See `synth_verdict_166.md` in this slot 167 folder for the full verdict packet.

**DOI correction note**: the Umbrella concept-DOI was corrected during slot 162 pre-flight from `10.5281/zenodo.19885550` to `10.5281/zenodo.19885549`; slot 167 propagates the correction inline (see §1 + §5 step 1). The umbrella program is a single Zenodo concept (`19885549` = the "Cite all versions" DOI per Zenodo native version-listing UI 2026-05-10) with two versions: v1.0 = version-DOI `19885550` (Apr 29 2026); v2.0 = version-DOI `19965041` (May 2 2026). The previously-cited `19885550` was a version-DOI mislabeled as a concept-DOI; the umbrella v2.2 deposit creates a new version (v2.2) within the existing concept `19885549`. See `siarc-relay-bridge/sessions/2026-05-11/T2-EXECUTOR-DOI-CORRECTION-OVERLAY-SCHEMA-V1-AND-PCF2-V14-AMENDED-BLOCK-163-164/DOI_CORRECTION_AUDIT.md` for the full propagation scope.

---

**End of amended_description_block_v2.md (slot 167 overlay of slot 162 baseline, applying slot 166 verdict α1 + β1 + γ2).**
