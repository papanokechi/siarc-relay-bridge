# Stage 0 — Source staging and integrity

Slot: `sessions/2026-06-16/VQUAD-PAPER-CORRECTIONS-001/`
Parent (pristine, NOT modified): `sessions/2026-06-15/VQUAD-PERIODREP-PAPER-001/`
Date: 2026-06-16. HEAD at task start: `e207b33` (VQUAD-COLDREAD-001 committed).

## 0.1 Sources copied into the slot
From `VQUAD-PERIODREP-PAPER-001/latex/` and `.../sections/`:
- `latex/build.py`, `latex/preamble.tex`, `latex/vquad-periodrep-paper.tex`, `latex/vquad-periodrep-paper.pdf`
- `sections/section-1.md` … `section-8.md`, `sections/section-9-references.md`

`work/` created for scratch.

## 0.2 Integrity check (verified BEFORE any edit)
Pre-corrections provenance pins (re-confirmed post-edit; the `.tex`/`.pdf` are retained, not regenerated this slot):

| Artifact | SHA-256 | Matches |
|---|---|---|
| copied `.tex` | `BD59D7448022C8C3822A4CFCDDEE4638528159B7650DE06CF5200F16B09C0BA7` | parent `.tex` == cold-read bundle `.tex` |
| copied `.pdf` | `359D1172AF3F867F4349CF4776A222813A855CD354BC78C0B68CCFB0026C702B` | pre-corrections pin `359d1172…` (cold-read) |

The copied `.tex` equals the parent `.tex` byte-for-byte; since `build.py` regenerates the `.tex`
deterministically from `preamble.tex` + the section fragments, this proves the copied sources are
identical to the parent at copy time.

## 0.3 Canonical corrections spec
`sessions/2026-06-16/VQUAD-COLDREAD-001/corrections-list.md` read in full. It is canonical; where the
task-prompt summary conflicts, corrections-list.md wins. Two conflicts found and flagged (see
`corrections-applied.md` §Conflicts and `claims.jsonl`).

## Build architecture (critical)
`latex/build.py` **generates** `latex/vquad-periodrep-paper.tex` by concatenating
`preamble.tex` (rstrip) + per-section `% ===== section-N.md =====` markers + each
`sections/section-{1..8}.md` + `section-9-references.md` + `\end{document}`, then runs
`pdflatex` ×2 with `SOURCE_DATE_EPOCH` (default `1718409600`) and the preamble byte-repro guards
(`\pdfinfoomitdate=1`, `\pdftrailerid{}`, `\pdfsuppressptexinfo=-1`).

**Consequence:** corrections were applied to the `.md` fragments and `preamble.tex`, **never** to the
generated `.tex` (which `build.py` overwrites in Stage 4). The retained `.tex`/`.pdf` are the
pre-corrections provenance artifacts only.

Notable placements (not where the cold-read line numbers naively suggest):
- Abstract (L-3) and `\thanks` (L-4) live in **`preamble.tex`**, not `section-1.md`.
- `eq:C-skeleton`/`eq:bridge` (H-1 candidate, intro) are in `section-1.md`; the `§4.3 "The constants"`
  H-1 candidate is in `section-4.md`.

## Per-file change manifest (edited copy vs pristine parent)
| File | State | diff-lines |
|---|---|---|
| `latex/preamble.tex` | EDITED (L-3, L-4) | 3 |
| `sections/section-1.md` | UNCHANGED (H-1 draft-only) | 0 |
| `sections/section-2.md` | EDITED (M-3 ack, L-5) | 10 |
| `sections/section-3.md` | UNCHANGED | 0 |
| `sections/section-4.md` | UNCHANGED (H-1 §4.3 location, draft-only) | 0 |
| `sections/section-5.md` | EDITED (M-1, M-2) | 8 |
| `sections/section-6.md` | EDITED (L-2) | 6 |
| `sections/section-7.md` | EDITED (M-3 §7.4, L-1 §7.1) | 19 |
| `sections/section-8.md` | UNCHANGED | 0 |
| `sections/section-9-references.md` | EDITED (M-4, M-3, L-1 bibitems) | 41 |

`section-1.md` and `section-4.md` UNCHANGED is the mechanical proof that **H-1 was not inserted**
(it is drafted only, pending the Stage-3 operator halt).
