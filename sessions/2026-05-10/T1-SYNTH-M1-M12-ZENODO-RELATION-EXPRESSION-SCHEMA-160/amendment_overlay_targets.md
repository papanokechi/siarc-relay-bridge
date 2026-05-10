# Amendment-Overlay Targets for Slot 160 Verdict Absorption

**Parent verdict:** Slot 160 (`verdict.md`); LABEL=SCHEMA_LOCK_INLINE; NO-FIRE.
**Schema authority:** `locked_schema_v1.md` (this folder).

This document specifies the concrete downstream amendment-overlays the slot 160 verdict mandates. It is the operator-facing handoff for which fires/edits the verdict implies.

---

## Target 1 — F6 Umbrella v2.3 substrate-prep (next math-axis fire)

**Status:** GATED (waiting on `D-156-1` V0+ vs V1 resolution per slot 159 anomaly).
**Embedding requirement (per slot 160 §Q5c option (i)):** F6 prompt body MUST embed:

1. Locked Q2b 7-status vocabulary (verbatim from `locked_schema_v1.md` §Layer 2).
2. Q2c granularity rule (atomic M1-M12 listing; no grouping of RULE-1-tabled axes).
3. Q1a 5-row Layer 1 pattern (referencing PCF-1 paired `IsSupplementTo` + `Cites` discipline).
4. Reference axis-coverage table for **Umbrella v2.3** instance (must be authored by F6, not copied from PCF-2).

**Umbrella v2.3 axis-coverage table — expected differences from PCF-2 v1.4 reference table in `locked_schema_v1.md`:**

- M4/M7/M8a/M8b: status = `closed (V0; folded)` (Umbrella v2.3 absorbs via Appendix C iii); semantics identical to PCF-2 v1.4.
- M9: status = `partial`; Umbrella v2.3 may or may not be the *primary* depending on D-156-1 outcome (V0+ → primary in v2.3; V1 → primary remains in picture-chain `b9aa881`).
- M10: status = `partial`; SAFE phrasing in Appendix C ii; consistent with PCF-2 v1.4.
- M1: `external` (D2-NOTE) — same as PCF-2.
- M6.CC: `closed (retired into Channel Theory)` — same as PCF-2.

**F6 deliverable surface:** Umbrella v2.3 Zenodo description block (analogous to slot 137 `zenodo_v14_description_block.md`).

---

## Target 2 — Slot 137 `zenodo_v14_description_block.md` amendment-overlay

**Status:** REQUIRED (operator-side, small scope, single deliverable).
**Type:** amendment-overlay fire (analogous to slot 158's role for cascade-132 §3.1).
**Scope:** ~1 file edit + bridge fire deposit.

**Concrete edit list:**

1. **Add 5th Layer 1 row** to the related-identifiers block:
   ```
   Cites           10.5281/zenodo.19885550    Umbrella concept
   ```
   Inserted directly after the existing `IsSupplementTo Umbrella concept` row to mirror the PCF-1 `IsSupplementTo` + `Cites` pairing pattern.

2. **Insert PCF-2 v1.4 axis-coverage table** in the Description body (use the table from `locked_schema_v1.md` §Layer 2 — Reference table verbatim).

3. **Add schema citation** at the bottom of the axis-coverage section:
   > "Axis-coverage table follows the SIARC v1 schema locked by slot 160 verdict (`<slot 160 bridge SHA>`)."

   The `<slot 160 bridge SHA>` is the bridge HEAD after this absorption fire lands; it MUST be filled in by the amendment-overlay fire, not pre-committed.

**Anti-edits (do NOT change):**

- Do NOT rewrite or remove existing Layer 1 rows (`IsNewVersionOf` / `IsSupplementTo PCF-1` / `Cites PCF-1` / `IsSupplementTo Umbrella` are all correct per slot 160 §Q1a).
- Do NOT add `Cites` rows for Channel Theory / D2-NOTE / picture v1.19 (slot 160 §Q1a explicit anti-rule: axis-mediated relations belong in Layer 2, not Layer 1).
- Do NOT change concept-DOI vs version-DOI usage (slot 160 §Q1c verifies discipline correct).

**Recommended fire metadata:**

- Slot number: 161 (or next available; check supersession at fire time).
- Class: T2-Executor amendment-overlay.
- Band: LOW-MEDIUM.
- RULE 1: clean (operator-side document edit; no Zenodo deposit until F6 + this both land).
- Predecessor: slot 137 `45e236c`; slot 160 `<this fire bridge SHA>`.

---

## Target 3 — Slot 135 `zenodo_v22_description_block.md` (Umbrella v2.2 substrate)

**Status:** NO RETROACTIVE AMENDMENT REQUIRED.
**Rationale (per slot 160 §ABSORPTION_GUIDANCE):** Umbrella v2.2 is superseded by v2.3 (F6 deliverable). The schema lock applies to the v2.3 substrate authored fresh by F6, not to a retroactive edit of v2.2 substrate which will never be deposited as-is.

---

## Target 4 — Operator runbook addition (when picture-chain consolidated deposit is reconsidered)

**Status:** DEFERRED.
**Note:** If a future operator decision re-opens picture-chain consolidated deposit (currently DROPPED per Option α'), the deposit would be a **single-purpose deposit, not an anchor**. Per `locked_schema_v1.md` §Scope, single-purpose deposits cite the canonical outlook by reference and do NOT carry the full axis-coverage table.

---

## Target 5 — Future anchor-deposit version increments

**Status:** SCHEDULED (deposit-time application).

When PCF-1 / Channel Theory / D2-NOTE next version-increment, schema v1 applies. Each:

1. Uses the Layer 1 paired `IsSupplementTo` + `Cites` pattern for any paper-tier supplementary relations.
2. Uses the Layer 2 controlled vocabulary + atomic listing.
3. Cites slot 160 verdict SHA as schema authority.
4. Snapshots axis statuses *as of deposit time* (not the slot 160 fire time).

---

## Forward-pointer for Layer 3 (Community) lift

When `D-157-7` Community deferral lifts (post-RULE-1-lift + forcing function):

1. Create SIARC Zenodo Community.
2. Description: single line — pointer to canonical outlook bridge URL (current outlook bridge SHA at Community-creation time).
3. Add all 5 anchor deposits to Community.
4. NO axis-coverage table at Community level; per-deposit snapshots remain authoritative.

---

## Verification

After all amendment-overlay targets are absorbed, the following invariants MUST hold:

- I1: PCF-2 v1.4 description block carries 5 Layer 1 rows (matches `locked_schema_v1.md` §Layer 1 reference).
- I2: PCF-2 v1.4 description block carries 12-row M1-M12 axis-coverage table.
- I3: Umbrella v2.3 description block (F6 deliverable) carries 5 Layer 1 rows (with PCF-2 v1.4 as the supplementary peer instead of Umbrella).
- I4: Umbrella v2.3 description block carries 12-row M1-M12 axis-coverage table.
- I5: Both deposits cite slot 160 verdict SHA as schema authority.
- I6: Neither deposit has `Cites Channel Theory` / `Cites D2-NOTE` / `Cites picture v1.19` Layer 1 rows.
- I7: Bridge cascade SHAs in Description body prose, never in Layer 1 `References` rows.

Verification of I1-I7 happens at PCF-2 v1.4 + Umbrella v2.3 deposit-time review (post-F6 + post-amendment-overlay).
