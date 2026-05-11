# Runbook Addendum — Zenodo "New version" IsNewVersionOf Auto-population Quirk

**Date**: 2026-05-11 09:06 JST
**Parent slot**: 167 (bridge SHA `8d1f426`)
**Trigger**: operator-side observation at umbrella v2.2 Phase B step 2 fire-time
**Severity**: HIGH (operator runbook correctness; would cause schema-violating deposit if uncorrected)

---

## Observation

Operator clicked "New version" from `https://zenodo.org/records/19965041` (umbrella v2.0) and Zenodo auto-populated the `IsNewVersionOf` row with `10.5281/zenodo.19885550` — which is the umbrella **v1.0 version-DOI** (the ORIGINAL deposit in the chain), NOT `10.5281/zenodo.19965041` (v2.0 version-DOI = immediate predecessor).

## Cross-validation

Verified against the live PCF-2 v1.4 record (`https://zenodo.org/records/20114315`, deposited 2026-05-11):

```
isNewVersionOf       10.5281/zenodo.19963298 (publication-preprint)   ← PCF-2 v1.3 (IMMEDIATE predecessor)
isSupplementTo       10.5281/zenodo.19931635 (publication-preprint)
cites                10.5281/zenodo.19931635 (publication-preprint)
isSupplementTo       10.5281/zenodo.19885549 (publication-preprint)
cites                10.5281/zenodo.19885549 (publication-preprint)
```

PCF-2 v1.4 IsNewVersionOf points to v1.3 (`19963298`), NOT v1.0 (`19936298`). The operator at PCF-2 v1.4 deposit time successfully achieved the schema-compliant immediate-predecessor target. This confirms:

1. Zenodo's auto-population behavior for IsNewVersionOf = points to chain's FIRST version (the original deposit), NOT immediate predecessor.
2. The operator MUST manually edit the auto-populated value to comply with slot 160 schema v1 §Layer 1: *"IsNewVersionOf MUST target the **immediate predecessor's** version-DOI on both sides."*
3. This is a known-feasible operator workflow.

## Corrected Phase B step 2 (supersedes `operator_runbook.md` step 2)

**Replace step 2 in the slot 167 operator runbook with the following:**

> **2. Confirm and correct IsNewVersionOf auto-population**:
>    - Scroll to Related-identifiers section in new draft.
>    - Zenodo will auto-populate one row: `IsNewVersionOf` → `10.5281/zenodo.19885550`. This is the umbrella v1.0 version-DOI (chain origin), **NOT** the immediate predecessor v2.0.
>    - **Manually edit this value**: change `19885550` → `19965041` (umbrella v2.0 version-DOI = immediate predecessor of v2.2 per slot 160 schema v1).
>    - Verify the corrected row reads: `IsNewVersionOf` → `10.5281/zenodo.19965041` (Publication / Preprint).
>    - **HALT if Zenodo prevents the edit** (would indicate a Zenodo platform change; trigger re-consultation).
>    - **HALT if the auto-populated value is anything other than `19885550`** (e.g., `19885549` concept-DOI; would indicate a Zenodo schema change).

## Why slot 160 schema v1 prefers immediate predecessor over chain-origin

Slot 160 `locked_schema_v1.md` line 31 (verbatim):
> "**`IsNewVersionOf` is the documented exception**: it is by definition a version-to-version relation and MUST target the **immediate predecessor's version-DOI** on both sides."

Rationale (implicit in schema):
- The DataCite IsNewVersionOf relation type is intended as a direct version-to-version link (forms a doubly-linked list across versions).
- Chain-origin pointing (Zenodo's auto-populate default) collapses the version graph topology — every version points to v1.0 instead of forming the chain v1.0 ← v2.0 ← v2.2.
- The PCF-2 v1.0..v1.4 chain (5 versions) preserves the doubly-linked structure: each version IsNewVersionOf its immediate predecessor.
- This matches the slot 160 schema's reading of DataCite vocabulary semantics.

## Updated halt conditions for Phase B

Append to `operator_runbook.md` Halt conditions:

- **H6** (NEW): Phase B step 2 — Zenodo auto-populated IsNewVersionOf value is anything other than `10.5281/zenodo.19885550` (e.g., `19885549` concept-DOI or some other identifier) → halt + investigate (potential Zenodo schema change).
- **H7** (NEW): Phase B step 2 — Zenodo UI does not permit editing the auto-populated value → halt + re-consult (would indicate a Zenodo platform restriction not previously observed).

## Status

**This addendum is operative**: any future operator-side fire of `operator_runbook.md` MUST apply this correction to Phase B step 2. The original runbook step 2 in `operator_runbook.md` is hereby SUPERSEDED by the text in this addendum.

A follow-up bridge fire (slot 168+ optional) may consolidate this addendum into the runbook proper; for now, both files travel together in slot 167.

## Logged as

- **UF-167-4** (HIGH; OPERATOR-RUNBOOK-CORRECTNESS): see `unexpected_finds.json` addendum below.
- No new discrepancy entry: the slot 167 runbook step 2 was wrong-as-written but no operator action took an incorrect path (caught at fire-time observation by operator).

---

## Appendix — UF-167-4 entry (to be merged into `unexpected_finds.json` if a slot 167 amendment commit happens)

```json
{
  "id": "UF-167-4",
  "severity": "HIGH",
  "category": "OPERATOR-RUNBOOK-CORRECTNESS",
  "summary": "Slot 167 operator_runbook.md Phase B step 2 incorrectly assumed Zenodo's 'New version' workflow auto-populates IsNewVersionOf with the IMMEDIATE PREDECESSOR's version-DOI (e.g., v2.0 = 19965041 for an umbrella v2.2 new version from v2.0 page). Operator observation 2026-05-11 09:06 JST: Zenodo actually auto-populates with the CHAIN-ORIGIN's version-DOI (e.g., v1.0 = 19885550), NOT immediate predecessor. Operator must MANUALLY EDIT the auto-populated value to comply with slot 160 schema v1 §Layer 1 (immediate-predecessor target).",
  "impact": "If uncorrected, umbrella v2.2 deposit would have published with IsNewVersionOf → 19885550 (v1.0), violating slot 160 schema v1 §Layer 1 rule. Caught at fire-time by operator visual inspection. Cross-validated against PCF-2 v1.4 live record which correctly shows IsNewVersionOf → 19963298 (v1.3 immediate predecessor), confirming the manual-edit step is a known-feasible operator workflow.",
  "recommendation": "Operator runbook Phase B step 2 MUST instruct operator to (a) observe Zenodo's auto-population value (19885550 expected), (b) manually edit to 19965041 (v2.0 immediate predecessor), (c) verify. Apply correction per RUNBOOK_ADDENDUM_ZENODO_AUTO_POPULATE.md (this file).",
  "first_observed": "2026-05-11 09:06 JST (operator Phase B step 2 fire-time visual inspection)",
  "status": "RESOLVED-VIA-ADDENDUM"
}
```

---

**End of `RUNBOOK_ADDENDUM_ZENODO_AUTO_POPULATE.md`.**
