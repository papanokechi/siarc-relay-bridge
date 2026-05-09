# Cross-link update log — picture-chain v1.20+ (slot 136)

**Status:** OPERATOR-PENDING — TABLED under RULE 1.
**Phase:** C+D (post RULE 1 lift; post-M10-status-resolution).
**Activates after:** slot 138+ orchestrates RULE 1 lift; operator-side Zenodo deposit window opens.

This file is a pre-staged template. The operator fills it at deposit time per cascade-132 §3.1 Option α deposit ordering.

---

## Deposit ordering (cascade-132 §3.1 unanimous Option α)

| Order | Substrate | Slot | Bridge SHA | Zenodo step |
|-------|-----------|------|-----------|-------------|
| 1 | PCF-2 v1.4 | 137 | `45e236c` | Deposit FIRST. Use slot 137's `zenodo_v14_description_block.md` for Zenodo form fields. Receive v1.4 version DOI. |
| 2 | Umbrella v2.2 | 135 | `887981b` | Deposit SECOND. Splice the v1.4 version DOI into umbrella v2.2 `IsSupplementTo` related-identifier per slot 135 `zenodo_v22_description_block.md` §4. Receive v2.2 version DOI. |
| 3 | Picture-chain v1.20+ | 136 | `<this-fire>` | Deposit THIRD. **Splice v1.4 + v2.2 version DOIs into picture-chain related-identifiers** per the worksheet below. Receive v1.20+ version DOI. |

---

## Picture-chain v1.20+ related-identifiers worksheet (operator fills)

The picture-chain v1.20+ Zenodo deposit description block should include:

```
[OPERATOR FILLS — picture-chain v1.20+ Zenodo description block goes here]
```

### Related-identifier splices (mandatory)

| Relationship | Identifier | Source slot |
|--------------|-----------|-------------|
| `IsSupplementedBy` | `10.5281/zenodo.<PCF-2 v1.4 version DOI>` (filled at step 1 above) | slot 137 |
| `IsSupplementedBy` | `10.5281/zenodo.<Umbrella v2.2 version DOI>` (filled at step 2 above) | slot 135 |
| `IsContinuationOf` | `10.5281/zenodo.<picture v1.19 version DOI>` (PICTURE-V19-CONSOLIDATED-DEPOSIT bridge `70d1a48`; 2026-05-06 ~12:13 JST) | (prior picture-chain) |

### BibTeX cross-link splices (mandatory)

| Target file | BibTeX entry to splice | Source DOI |
|-------------|-----------------------|-----------|
| (TBD: operator-side per BibTeX repo conventions) | `@misc{picture_v120plus_2026, ...}` | picture v1.20+ version DOI |

---

## Cross-link update steps (apply in this order)

1. **PCF-2 v1.4 cross_link (slot 137 cross_link_update_log).** Apply slot 137's cross-link updates first. Verify the v1.4 version DOI is operationally live at Zenodo before proceeding.
2. **Umbrella v2.2 cross_link (slot 135 cross_link_update_log).** Splice the v1.4 version DOI; apply slot 135's cross-link updates. Verify v2.2 version DOI is operationally live.
3. **Picture-chain v1.20+ cross_link (THIS file).** Splice both v1.4 + v2.2 version DOIs into picture-chain related-identifiers; apply BibTeX edits per the worksheet above.

---

## Submission_log splice ordering

Per slot 136 §6 step 5:

| Order | Submission_log item | Source slot |
|-------|---------------------|-------------|
| 1 | v1.4 splice (PCF-2) | slot 137 `submission_log_v14_splice.diff` |
| 2 | v2.2 splice (Umbrella) | slot 135 `submission_log_item12_splice.diff` |
| 3 | v1.20+ splice (Picture-chain) | THIS slot's `submission_log_v120plus_splice.diff` |

---

## RULE 1 lift gate (forward-pointed)

After all three Phase C+D cross_link updates land at Zenodo:

1. Cut `M1_M12_CLOSURE_OUTLOOK_<DATE>_POST_MATH.md` per RULE 1 §6 lift condition.
2. Lift RULE 1; admin window opens for M11 / M12 amendment orchestration.

---

**This file is pre-staged. Operator fills the worksheets at deposit time.**
