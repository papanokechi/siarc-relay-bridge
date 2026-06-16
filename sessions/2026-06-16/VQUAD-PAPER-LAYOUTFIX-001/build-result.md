# build-result.md — VQUAD-PAPER-LAYOUTFIX-001 Stage 3

## Build
- Driver: `latex/build.py` (concatenate `preamble.tex` + `sections/section-*.md`
  → `vquad-periodrep-paper.tex`; `pdflatex × 2`; `SOURCE_DATE_EPOCH=1718409600`).
- Errors: **0**. Pages: **24** (unchanged from 24).
- Undefined refs/citations: **0** (all `\ref`/`\cite` resolve).
- Underfull \hbox: 8 (informational loose lines from `\emergencystretch`; **no
  clipping** — underfull never overruns the margin). Acceptable.

## Overfull hboxes — the success criterion
| | count |
|---|--:|
| BEFORE (baseline `4ca12a35…`) | **20** |
| AFTER global fix (preamble) | 7 |
| AFTER local display/table fixes | **0** |

`Get-Content vquad-periodrep-paper.log | Select-String 'Overfull \hbox'` → **0 matches.**

## New PDF pins (supersede `4ca12a35…` / `028a1a5d…`)
| | value |
|---|---|
| **SHA-256** | `33f339edd17c5405bfd24a85ba1a5df65aeeb836e25fb525d778599aa7ba3eea` |
| **MD5** | `99faea5b0f4095788e4ee932436beeda` |
| bytes | 773171 |
| pages | 24 |
| OLD SHA-256 | `4ca12a35d655df2227a9e1740e60b39c2e6cabef6a1942c74307cd43849582fe` |
| OLD MD5 | `028a1a5d9e10a3a9487596f6db3e6a38` |
| OLD bytes | 714771 |

## Byte-reproducibility
Independent build from a **pristine temp dir** (fresh copy of `preamble.tex` +
`build.py` + `sections/`) produced the **identical** SHA-256
`33f339ed…`. → byte-reproducible: **TRUE**.

## Stage 3.3 — wrong-venue (Gate 2.2) on the NEW PDF
Extracted text (pypdf, 63713 chars). Forbidden tokens **absent**:
`Compositio`, `AAECC`, `ETNA`, `Comptes Rendus`, `Crelle`, `Journal of Number
Theory`, `Mathematika`. `Symbolic Comput` **present** = the legitimate Kovacic /
J. Symbolic Computation citation, **not** a venue leak. **Gate 2.2: PASS.**

## Stage 3.4 — content-unchanged proof (load-bearing AEAL)
Method: extract full text of OLD (`OLD-vquad-periodrep-paper-4ca12a35.pdf`) and NEW
PDFs (pypdf); strip all whitespace; compare. Then the airtight, order-independent
test — **character-multiset (Counter) diff** of the whitespace-stripped streams.

- Whitespace-stripped lengths: OLD 54177, NEW 54175 (Δ = −2).
- **Character-multiset diff (NEW − OLD): exactly one character differs in count —
  ASCII hyphen `U+002D` by −2. ZERO other characters differ (no digit, letter,
  Greek, or math operator changes count).**
- The −2 hyphens are **line-end hyphenation**: reflow moved where lines break, so 4
  optional end-of-line hyphens vanished and 2 appeared (net −2). The words
  themselves (`corresponding`, `Numerically`, `rational`, `singularity`,
  `coefficient`, `computational`) are intact and present identically in both.
- The 46 raw `difflib` blocks (see `_textdiff_report.txt`) are all reflow furniture:
  (i) page running-heads re-extracting at shifted stream offsets across reflowed
  page breaks (each a paired delete+insert of an identical string), (ii) the §3.2
  "Rapid decay" proposition + its figure swapping extraction order (character-
  identical, just moved), (iii) the `holonomic_recognition_q3.py` script name now
  splitting at `_` across a page break (intact, `q3.py,` fragment paired), and
  (iv) the 6 line-end hyphens above.

**TEXT DIFF = REFLOW-ONLY: YES.** No content (digit/symbol/word/equation) changed.

## Gate verdicts
- Overfull = 0 ✅
- 0 LaTeX errors, refs resolve, 24pp ✅
- Byte-reproducible (pristine temp) ✅
- Wrong-venue (Gate 2.2) PASS ✅
- Content-diff reflow-only (multiset: −2 hyphen, 0 other) ✅
- p4 factor correct (not a typo) ✅

**HALT GATE: CLEARED.** No content change, no residual overfull, p4 not a typo →
safe to ship the new PDF and cascade.
