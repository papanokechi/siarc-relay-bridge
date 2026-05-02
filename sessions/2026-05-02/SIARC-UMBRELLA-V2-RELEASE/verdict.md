# SIARC-UMBRELLA-V2-RELEASE verdict

**Verdict label:** `UMBRELLA_V2_BUILT_AND_STAGED`

**Status:** PARTIAL (build succeeds, metadata staged; awaits operator
Zenodo upload per Phase D).

## Summary

Phase A (surgical edits to `tex/submitted/umbrella_program_paper/main.tex`)
through Phase F (verdict, rubber-duck critique, AEAL claim chain) all
completed without halt. The v2.0 source absorbs the post-T2
cross-degree invariant triple framing, integrates the four sister
Zenodo records (PCF-1 v1.3, PCF-2 v1.3, Channel Theory v1.2,
standalone j-invariant note), refreshes the Open Problems list
(`op:finer-cubic-split` closed; eight new entries added including
`prob:b4-allD`, `op:j-zero-amplitude-h6`, `op:j-1728-wedge`,
`op:shallow-j-effect-d4`, `prob:modular-discriminant-stratification`,
`prob:Pk-cells-structure`, `prob:median-resurgence-extension`,
`op:chi-Phi-compatibility`), and extends the Companion Papers table
from 7 to 16 entries.

## Build numerics

| metric | value |
|---|---|
| pages | 12 (vs v1: 7) |
| `!` lines in `main.log` | 0 |
| missing citations | 0 |
| unresolved cross-references | 0 |
| overfull hboxes | 4 (cosmetic; longest 167 pt in bibliography URL line) |
| underfull hboxes | 0 critical |
| pdflatex passes | 3 (1 to settle TOC + bibliography, 2 to clear "Label(s) may have changed") |
| build wall-time | < 30 s per pass (commodity laptop) |

## Source / PDF artefact hashes

- v1 baseline backup: `sessions/2026-05-02/SIARC-UMBRELLA-V2-RELEASE/archive/main_v1_baseline.tex`
  - SHA-256: `0C630DE2524F809DC56F4DB099325779CB54897CF5C7D90EC7C435432711F407`
  - size: 20,909 bytes
- v2.0 source: `tex/submitted/umbrella_program_paper/main.tex`
  - SHA-256: `612F732EBE2D8BABF5EE6582C3D35D6B91F2CF2421D9A7778B3A17810DAC8EF0`
  - size: 44,935 bytes
- v2.0 PDF: `tex/submitted/umbrella_program_paper/main.pdf`
  - SHA-256: `24382421290318AE2A8FD8F22E3A0EC6953D738D35411C61E32C26E7BD8F2037`
  - size: 455,178 bytes
  - 12 pages

## Halt conditions checked

All halt conditions per `.github/copilot-instructions.md` and Phase B
acceptance criteria PASS:

- Build error count: 0 ✓
- Missing citations: 0 ✓
- Unresolved refs: 0 ✓
- Page count ≥ v1 (7): 12 ≥ 7 ✓
- §4 Cross-Degree Framing renders without symbol failures: ✓
  (`\HH = \mathfrak{H}` and `\PetN` macro both expand cleanly; `amssymb`
   loaded since v1)
- No v1 claim retracted: ✓ (all v1 conjectures, theorems, open problems
  preserved verbatim or refined-but-not-contradicted; refinements logged
  in `discrepancy_log.json` — empty since no actual contradictions)
- No `claim_id` collisions in `claims.jsonl`: ✓ (UMB-V2-A1 .. UMB-V2-A12)

## Recommendation

Operator: proceed with Phase D (Zenodo "New version" upload of
`tex/submitted/umbrella_program_paper/main.pdf` against existing umbrella
v1 row at concept DOI `10.5281/zenodo.19885550`); after publish, fire
follow-up session `SUBMISSION-LOG-PATCH-ITEM18` to fill the
`__VERSION_DOI__` placeholder in `submission_log_patch_item18.txt` and
append Item 18 to `tex/submitted/submission_log.txt`.
