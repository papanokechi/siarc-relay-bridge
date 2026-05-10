# PCF-2 v1.4 axis-coverage snapshot

**Schema authority:** Slot 160 (`T1-SYNTH-M1-M12-ZENODO-RELATION-EXPRESSION-SCHEMA-160`, bridge `012736f`).
**Snapshot context:** PCF-2 v1.4 Zenodo deposit description block, post-amendment-overlay slot 161 (bridge folder `T2-EXECUTOR-AMENDMENT-OVERLAY-PCF2-V14-DESCRIPTION-BLOCK-161`).
**Date:** 2026-05-10.
**Source:** byte-identical extraction from `amended_description_block.md` Edit 2 insertion.

---

**M1–M12 program-axis coverage (snapshot at PCF-2 v1.4 deposit time):**

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

---

## Citability

This snapshot is citable as a standalone artifact for the slot 160 schema-authority chain. Future anchor-deposit authoring (PCF-1 next version increment / Channel Theory next version increment / D2-NOTE next version increment / Umbrella v2.3 via F6 substrate-prep) MAY use this format as a copy-paste template, modifying only the per-anchor relation between the table's "primary substrate" column and the anchor's role (e.g., for M9 in Umbrella v2.3, the row would read `closed (V0+; primary)` or `closed (V1; primary)` depending on `D-156-1` resolution; PCF-2 v1.4 marks M9 as `partial` because its primary V0 substrate lives in picture-chain `b9aa881`).

## Verification

Per slot 161 §8 Invariant I7, this snapshot's table content is byte-identical to `amended_description_block.md` Edit 2 table content. Verification command (post-fire):

```powershell
$snap = Get-Content "axis_coverage_snapshot.md" | Select-String "^\| (M\d|Axis)" | ForEach-Object { $_.Line }
$amended = Get-Content "amended_description_block.md" | Select-String "^\| (M\d|Axis)" | ForEach-Object { $_.Line }
Compare-Object $snap $amended -CaseSensitive
```

(Empty output = byte-identical.)
