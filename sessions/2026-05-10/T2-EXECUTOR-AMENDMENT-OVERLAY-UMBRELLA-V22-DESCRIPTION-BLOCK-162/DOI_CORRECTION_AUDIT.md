# DOI Correction Audit — Umbrella concept-DOI vs v1.0 version-DOI misclassification

**Discovered:** Slot 162 pre-flight (2026-05-10).
**Severity:** HIGH (substrate-citation contamination across multiple LANDED artefacts).
**Ground truth:** Zenodo native version-listing UI sidebar (operator pastes 2026-05-10 ~22:43 + ~22:50 JST: umbrella + T2B records) + doi.org live-resolution at slot 162 STEP 0.4.

## §1 Ground truth (Zenodo sidebar + doi.org-verified)

### §1.1 Umbrella record (single concept, two versions)

| DOI | Role | Resolves to |
|---|---|---|
| `10.5281/zenodo.19885549` | **CONCEPT-DOI** ("Cite all versions"; latest-resolving) | currently → v2.0 |
| `10.5281/zenodo.19885550` | **v1.0 VERSION-DOI** (within concept 19885549) | v1.0 (Apr 29, 2026) |
| `10.5281/zenodo.19965041` | **v2.0 VERSION-DOI** (within concept 19885549) | v2.0 (May 2, 2026) |

Source: Zenodo native version-listing UI sidebar (operator paste 2026-05-10 21:43:37 JST):
> Versions
> Version 2.0 — 10.5281/zenodo.19965041 — May 2, 2026
> Version 1.0 — 10.5281/zenodo.19885550 — Apr 29, 2026
> Cite all versions? You can cite all versions by using the DOI 10.5281/zenodo.19885549. This DOI represents all versions, and will always resolve to the latest one.

### §1.2 T2B record (single concept, three versions)

| DOI | Role | Resolves to |
|---|---|---|
| `10.5281/zenodo.19783311` | **CONCEPT-DOI** ("Cite all versions"; latest-resolving) | currently → v3.0 |
| `10.5281/zenodo.19783312` | **v1.0 VERSION-DOI** (within concept 19783311) | v1.0 (Apr 26, 2026) |
| `10.5281/zenodo.19801038` | **v2.0 VERSION-DOI** (within concept 19783311) | v2.0 (Apr 27, 2026) |
| `10.5281/zenodo.19915689` | **v3.0 VERSION-DOI** (within concept 19783311) | v3.0 (Apr 30, 2026) |

Source: Zenodo native version-listing UI sidebar (operator paste 2026-05-10 ~22:50 JST):
> Versions
> Version 3.0 — 10.5281/zenodo.19915689 — Apr 30, 2026
> Version 2.0 — 10.5281/zenodo.19801038 — Apr 27, 2026
> Version 1.0 — 10.5281/zenodo.19783312 — Apr 26, 2026
> Cite all versions? You can cite all versions by using the DOI 10.5281/zenodo.19783311. This DOI represents all versions, and will always resolve to the latest one.

### §1.3 Common contamination class

Both records exhibit the same **version-vs-concept misclassification** pattern: a v1.0 version-DOI was repeatedly written into LANDED artefacts and labeled "concept DOI", but the actual concept-DOI is a *separate* Zenodo identifier (the "Cite all versions" DOI from the native UI sidebar).

- Umbrella: `19885550` (v1.0 version-DOI) was mislabeled "concept DOI"; correct concept = `19885549`.
- T2B: `19783312` (v1.0 version-DOI) was mislabeled "concept DOI" in picture.md; correct concept = `19783311`. *Note*: schema v1 (`locked_schema_v1.md` slot 160) cites T2B concept correctly as `19783311`; the picture.md error did NOT propagate into schema v1 or slot 161 amended block.

The umbrella mislabeling is the more severe propagation (5+ LANDED bridge sessions); the T2B mislabeling is contained (1 LANDED artefact: picture.md line 158).

Even the umbrella v2.0 record's own description body perpetuates the umbrella misclassification ("v1 (April 2026, concept DOI 10.5281/zenodo.19885550) anchored the program..."; doi.org STEP 0.4 fetch 2026-05-11 confirmed verbatim) — this is wrong; `19885550` is v1.0's version-DOI, not a concept-DOI. Future umbrella v3.0+ revisions should fix this description text.

## §2 Propagation across LANDED bridge artefacts

Files citing umbrella DOI `19885550` and labeling it "concept DOI" (WRONG: `19885550` is v1.0 version-DOI; correct concept = `19885549`):

- `siarc-relay-bridge/sessions/2026-05-09/T1-EXECUTOR-116-UMBRELLA-V21-M9-V0-DEPOSIT-133/`: `umbrella_v21.tex`, `submission_log_item11_splice.diff`, `zenodo_v21_deposit_log.md`, `b_amendment.diff`, `discrepancy_log.json` (DISCREPANCY-116-CONCEPT-DOI INFO; the resolution heuristic was inverted), `unexpected_finds.json` (UF-116-CONCEPT-DOI-DRIFT INFO), `handoff.md`
- `siarc-relay-bridge/sessions/2026-05-09/T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135/`: `zenodo_v22_description_block.md` (§1 Concept DOI cell L15 + §4 Layer 1 IsNewVersionOf L49 + §5 step 1 L62), `umbrella_v22.tex`, `zenodo_v22_deposit_log.md`, `submission_log_item12_splice.diff`, `b_amendment_v22.diff`
- `siarc-relay-bridge/sessions/2026-05-09/T2-EXECUTOR-PCF2-V14-M7-V0-AMENDMENT-PREP-137/`: `pcf2_program_statement_v14.tex`
- `siarc-relay-bridge/sessions/2026-05-10/T1-SYNTH-M1-M12-ZENODO-RELATION-EXPRESSION-SCHEMA-160/`: `locked_schema_v1.md` (line 20 in §Anchor deposits §Reference table), `verdict.md`, `amendment_overlay_targets.md`, `unexpected_finds.json`
- `siarc-relay-bridge/sessions/2026-05-10/T2-EXECUTOR-AMENDMENT-OVERLAY-PCF2-V14-DESCRIPTION-BLOCK-161/`: `amended_description_block.md` (paired Umbrella IsSupplementTo + Cites rows; lines ~138-139), `amendment_diff.md`, `unexpected_finds.json`, `handoff.md`

Total: 5 distinct LANDED bridge sessions; ≥18 distinct files. (Slot 133 alone has 7 files; slot 135 has 5 files; slot 137 has 1 file; slot 160 has 4 files; slot 161 has 4 files. Net ≥21 files counting each artefact once.)

Files citing umbrella concept-DOI `19885549` correctly:

- `siarc-relay-bridge/sessions/2026-05-02/STRATEGIC-PICTURE-REVISED/picture.md` (lines 160 + 1073; the early authoritative registry)
- `siarc-relay-bridge/sessions/2026-05-09/T2-EXECUTOR-PICTURE-V120-M9-V0-AMENDMENT-PREP-136/picture_revised_20260507.md`

### §2.5 T2B propagation (separate, contained)

Files citing T2B DOI `19783312` and labeling it "concept DOI" (WRONG: `19783312` is v1.0 version-DOI; correct concept = `19783311`):

- `siarc-relay-bridge/sessions/2026-05-02/STRATEGIC-PICTURE-REVISED/picture.md` (line 158: "T2B v3.0 (channel theory bibliography) | `10.5281/zenodo.19915689` | `10.5281/zenodo.19783312` | — | published" — concept-DOI column has v1.0 version-DOI)

Files citing T2B concept-DOI `19783311` correctly:

- `siarc-relay-bridge/sessions/2026-05-10/T1-SYNTH-M1-M12-ZENODO-RELATION-EXPRESSION-SCHEMA-160/locked_schema_v1.md` (§Anchor deposits §Reference table)
- `siarc-relay-bridge/sessions/2026-05-10/T2-EXECUTOR-AMENDMENT-OVERLAY-PCF2-V14-DESCRIPTION-BLOCK-161/amended_description_block.md` (Layer 2 axis-coverage table inheritance)

The T2B mislabeling is contained to picture.md only; the schema-v1 + slot-161 chain has T2B concept-DOI correct from the start.

## §3 Why the wrong fork was picked

Slot 116 (2026-05-09) discovered the discrepancy and logged it as `DISCREPANCY-116-CONCEPT-DOI` INFO. The slot 116 resolution: *"Picture cross-walks and the tex source differ by exactly 1 (49 vs 50). This is most likely an OCR / typo class error in the picture spreadsheet that propagated."* This heuristic was wrong: picture.md is the early authoritative registry from 2026-05-02 (the day Umbrella v2.0 was deposited), and its `19885549` value is the actual umbrella concept-DOI (the "Cite all versions" DOI per Zenodo native UI). The tex-source `19885550` (likely originally pasted from v1.0's version-DOI URL when the v1.0 record was first deposited) was carried forward into v2.0 + v2.1 + v2.2 sources mislabeled as "concept DOI" rather than being updated to the actual concept `19885549`. Compounding factor: the v2.0 record's own description body also mislabels `19885550` as "concept DOI" of v1, providing apparent (but wrong) substrate confirmation for the tex-source value. (doi.org STEP 0.4 fetch 2026-05-11 verbatim: "v1 (April 2026, concept DOI 10.5281/zenodo.19885550) anchored the program...")

This is exactly the failure pattern the project memory `Bibliographic identifier pre-verification` (post-031 verdict) was designed to prevent — DOIs cited in deposit-runbook artefacts must be doi.org-verified before the relay prompt fires. Slot 162 STEP 0.4 doi.org pre-resolve mandate generalizes the lit-hunt-prompt rule to all amendment-overlay slots.

## §4 Recommended remediation slots

- **Slot 163** (recommended, LOW; T2-Executor): amendment-overlay against `locked_schema_v1.md` (slot 160 LANDED `012736f`) — single-line edit replacing `19885550` with `19885549` in the §Anchor deposits §Reference table umbrella row. Schema authority is the highest-leverage correction; downstream amendment-overlays will inherit the correct value. ~5-10 min agent work.
- **Slot 164** (recommended, LOW; T2-Executor): amendment-overlay against slot 161 `amended_description_block.md` (slot 161 LANDED `8906519`) — replace `19885550` with `19885549` in the 2 paired Umbrella IsSupplementTo + Cites rows. Optional: also produce a `slot_161_DOI_correction_notes.md` artefact with the diff summary. ~5-10 min agent work. Defer-or-combine: if slot 163 fires first, slot 164 can be tied in immediately afterward (combined slot 163+164 fire OK at LOW band).
- **Slot 165+** (optional, LOW): per-artefact corrections for the slot 133 / 135 / 137 tex-source files. These are pre-Zenodo source files; if the operator catches the DOI at deposit-time-paste (visit `19885549` instead of `19885550`), the source-file errors are recoverable at deposit time without retroactive amendment-overlay slots. Recommended path: bake the correction into the next-version source files as they are authored, NOT retroactive amendment-overlay slots.
- **Slot 165+ Picture.md T2B concept-DOI**: picture.md line 158 lists T2B concept = `19783312` (which is actually T2B v1.0 version-DOI per doi.org + Zenodo sidebar). Schema v1 + slot 161 use `19783311` (the correct T2B concept). No correction needed for schema-side. Picture.md may want a parallel correction in a future picture-chain amendment-overlay (rolled into slot 136 deposit-time review or a separate slot).
- **Umbrella v3.0 content cleanup** (future, when umbrella v3.0 is authored): the v2.0 Zenodo record's own description body perpetuates "v1 (April 2026, concept DOI 10.5281/zenodo.19885550)" — this typo should be fixed in the next-version umbrella source. Out of scope for slot 162.

## §5 Audit-trail summary

Bridge SHAs touched by this audit (read-only):
- `887981b` (slot 135 baseline; baseline cited verbatim in §4 of `amended_description_block.md`)
- `012736f` (slot 160 schema authority; cited as schema-amendment target in slot 163)
- `8906519` (slot 161 amended block; cited as content-amendment target in slot 164)

Bridge SHAs NOT touched (operator-pending; outside slot 162 scope):
- `887981b` itself (LANDED; immutable)
- `012736f` itself (LANDED; slot 163 to amend)
- `8906519` itself (LANDED; slot 164 to amend)

doi.org-resolutions cited (slot 162 STEP 0.4 pre-flight verified 2026-05-11):
- `https://doi.org/10.5281/zenodo.19885549` — Umbrella concept-DOI; resolves to "Published May 2, 2026 | Version 2.0 | This is the v2.0 revision of the SIARC umbrella program statement"
- `https://doi.org/10.5281/zenodo.19885550` — resolves to "Published April 29, 2026 | Version 1.0 | program statement... v1" — v1.0 version-DOI confirmed
- `https://doi.org/10.5281/zenodo.19965041` — Umbrella v2.0 version-DOI; resolves to "Published May 2, 2026 | Version 2.0" (same record as concept-DOI lookup)
- `https://doi.org/10.5281/zenodo.19931635` — PCF-1 concept-DOI; resolves to "Published May 1, 2026 | Version 1.3 | We propose a transcendence predicate for degree-two polynomial continued fractions..."
- `https://doi.org/10.5281/zenodo.19936297` — PCF-2 concept-DOI; resolves to "Published May 2, 2026 | Version 1.3 | PCF-2 (P13 in the SIARC stack), the cubic extension of PCF-1 (concept DOI 10.5281/zenodo.19931635; latest v1.3 = 10.5281/zenodo.19937196)" — PCF-2 body itself confirms PCF-1 concept-DOI correctly
- `https://doi.org/10.5281/zenodo.19941678` — Channel Theory concept-DOI; resolves to "Published May 2, 2026 | Version 1.3 | concept DOI 10.5281/zenodo.19941678, preserved across versions" — CT body confirms its own concept-DOI
- `https://doi.org/10.5281/zenodo.19783311` — T2B concept-DOI; resolves to "Published April 30, 2026 | Version 3.0 | Version 3.0 of the T2B preprint (Trans-Stratum dichotomy of degree-(2,1) integer PCFs, Class A vs Class B)"
- `https://doi.org/10.5281/zenodo.19996689` — D2-NOTE concept-DOI; resolves to "Published May 4, 2026 | Version 2.1 | D2-NOTE v2.1 (2026-05-03)... replacing v2 (concept 19996689 / version 19996690, 6pp)"

Zenodo native version-listing UI sidebar pastes (ground truth):
- Umbrella record sidebar — operator paste 2026-05-10 21:43:37 JST
- T2B record sidebar — operator paste 2026-05-10 ~22:50 JST

**End of DOI_CORRECTION_AUDIT.md.**
