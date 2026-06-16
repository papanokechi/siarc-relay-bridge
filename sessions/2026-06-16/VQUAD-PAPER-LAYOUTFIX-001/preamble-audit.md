# preamble-audit.md — VQUAD-PAPER-LAYOUTFIX-001 Stage 1.2

Source: `latex/preamble.tex` (copied from CORRECTIONS-001 `d4fc87a`; the copy
reproduces the overflowing PDF `4ca12a35…` byte-for-byte → correct starting point).

## documentclass + options
```
\documentclass[11pt,reqno]{amsart}
```
- Class: **amsart** (AMS article). Base size **11pt**, equation numbers right (`reqno`).
- No paper size in the class options → amsart default `letterpaper` (8.5×11 in).

## Geometry / text block
```
\usepackage[letterpaper,margin=1.5in]{geometry}
```
- Paper: **letterpaper** (matches the class default — *no a4/letter mismatch*).
- Margins: **1.5 in** all round → text block width = 8.5 − 2·1.5 = **5.5 in ≈ 396.3 pt**.
- This is a *narrow* measure (amsart default would be wider), but it is internally
  consistent: the class paper size, the geometry paper size, and the pdflatex output
  paper size all agree on letterpaper. **No paper-size mismatch.**

## pdflatex output paper size
- `build.py` invokes `pdflatex` with no `-output-paper-size` override and no
  `\pdfpagewidth`/`\pdfpageheight` in the preamble → output paper size = letterpaper
  (driven by `geometry`). Confirmed: the produced PDF is 612×792 pt (US Letter).
- → **the multi-page overflow is NOT a letter-vs-a4 geometry mismatch.**

## Line-breaking / justification controls (BEFORE fix)
| control | present? | note |
|---|---|---|
| `\usepackage{microtype}` | **yes** (line 5) | protrusion/expansion already on |
| `\tolerance` | not set | TeX default 200 |
| `\hbadness` | not set | default |
| `\emergencystretch` | **not set** | ← no last-resort stretch for tight lines |
| `\sloppy` / `sloppypar` | not used | |
| breakable `\_` (monospace underscore) | **no** | `\texttt{a_b_c.py}` has **no** breakpoints |

## Byte-reproducible build guards (must be preserved)
```
\pdfinfoomitdate=1
\pdftrailerid{}
\pdfsuppressptexinfo=-1
```
Build via `build.py`: concatenate `preamble.tex` + `sections/section-*.md`
→ `vquad-periodrep-paper.tex`, then `pdflatex × 2` with `SOURCE_DATE_EPOCH`
default `1718409600`. Reproduces `4ca12a35…`.

## Audit conclusion
The two missing controls — **`\emergencystretch`** and a **breakable underscore** —
are the global levers. Geometry/paper size are correct and are *not* the cause; the
overflow is a MIX of (a) unbreakable monospace `\texttt{…\_…}` script names and
(b) intrinsically-wide display equations / one wide 4-column table. See
`overfull-inventory.md` for the classified evidence.
