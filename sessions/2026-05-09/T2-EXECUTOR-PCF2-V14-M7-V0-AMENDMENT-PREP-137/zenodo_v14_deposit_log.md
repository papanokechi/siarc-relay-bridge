# Zenodo deposit log — PCF-2 v1.4 (OPERATOR-PENDING template)

**Status**: TEMPLATE. To be filled by operator at the Zenodo new-version deposit step (Phase C, TABLED under RULE 1).

**Source**: T2-EXECUTOR-PCF2-V14-M7-V0-AMENDMENT-PREP-137 (slot 137)
**Deposit-ordering position**: FIRST in the M-axis V0 closure-series Zenodo session (per cascade-132 unanimous Option α). Slot 135 umbrella v2.2 deposits SECOND. Slot 136 picture-chain v1.20+ deposits THIRD.

---

## §1 Deposit metadata (OPERATOR FILLS)

| Field                                  | Value                                              |
|----------------------------------------|----------------------------------------------------|
| Deposit date / time (UTC)              | TBD                                                |
| Operator                               | papanokechi                                        |
| Zenodo concept DOI                     | `10.5281/zenodo.19936297`                          |
| Assigned v1.4 version DOI              | TBD                                                |
| Zenodo record URL                      | TBD                                                |
| Zenodo deposit-ID (numeric)            | TBD                                                |

## §2 Files uploaded (OPERATOR FILLS)

| Filename                         | Size (B) | SHA-256 (16-char prefix) | Verification |
|----------------------------------|----------|---------------------------|--------------|
| `pcf2_program_statement_v14.pdf` | 636,049  | `471DC7C7EBF8BD4F`        | TBD          |
| `pcf2_program_statement_v14.tex` | 80,244   | `0CF4E7DC90C1AC2A`        | TBD          |
| `b_amendment_v14.diff`           | 10,486   | `30371C2EBD9885B1`        | TBD          |

(Operator: if the source-bundle upload requires the 4 `\input{}` dependencies flattened in (per the deposit-time arxiv-pack flatten procedure), record the post-flatten source filename + size + SHA here as well.)

## §3 Related-identifiers row record (OPERATOR FILLS post-deposit)

| Relation         | Identifier (DOI)                          | Status      |
|------------------|-------------------------------------------|-------------|
| `IsNewVersionOf` | `10.5281/zenodo.19963298` (PCF-2 v1.3)    | TBD         |
| `IsSupplementTo` | `10.5281/zenodo.19931635` (PCF-1 concept) | TBD         |
| `Cites`          | `10.5281/zenodo.19931635` (PCF-1 concept) | TBD         |

## §4 Sidebar cross-check (operator paste-verifies at deposit time)

Per slot 116 J2 three-way mismatch precedent, the operator paste-verifies the PCF-2 Zenodo sidebar and records:

- [ ] Concept DOI on the PCF-2 page sidebar = `10.5281/zenodo.19936297`
- [ ] PCF-2 v1.3 version DOI on the page sidebar matches `19963298` (the bare numeric used in `zenodo_v14_description_block.md`)
- [ ] PCF-1 concept DOI on the PCF-1 page sidebar = `10.5281/zenodo.19931635` (cross-link target)

If any sidebar value contradicts the substrate-supplied DOI: HALT deposit, surface as discrepancy `D-137-5-MED`, and re-fire substrate cross-check before proceeding.

## §5 Post-deposit follow-on actions

1. [ ] Capture assigned v1.4 version DOI from Zenodo confirmation page.
2. [ ] Update `cross_link_update_log.md` (sibling template) with the v1.4 version DOI.
3. [ ] Splice `submission_log_v14_splice.diff` into `tex/submitted/submission_log.txt`.
4. [ ] Splice the freshly assigned v1.4 version DOI into umbrella v2.2's `zenodo_v22_description_block.md` `IsSupplementTo` row (slot 135 substrate at `sessions/2026-05-09/T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135/`); then proceed to umbrella v2.2 deposit (Option α step 2).
5. [ ] When picture-chain v1.20+ substrate-prep is fired (slot 136), splice the v1.4 version DOI into its description block as well.

## §6 Notes

(Operator-fillable free-form notes section.)
