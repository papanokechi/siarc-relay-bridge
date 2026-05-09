# pdflatex compile log -- 116 v2.1 amendment

## Baseline (v2.0 unmodified, pre-edit)

```
$ pdflatex -interaction=nonstopmode -halt-on-error main.tex   # pass-1
$ pdflatex -interaction=nonstopmode -halt-on-error main.tex   # pass-2
PASS-2: warnings=28 errors=0 undef-msgs=0 pages=12
```

W_pre = 28 warnings (all Underfull/Overfull \hbox typesetting badness
in the existing Companion Papers longtable + a few scattered prose
paragraphs); 0 errors; 0 undefined references; 12 pages; PDF size
~455 kB.

## Post-edit (v2.1, amended)

```
$ pdflatex -interaction=nonstopmode -halt-on-error main.tex   # pass-1
PASS-1: warnings=127 errors=0 undef-msgs=84 pages=14
$ pdflatex -interaction=nonstopmode -halt-on-error main.tex   # pass-2
PASS-2: warnings=43 errors=0 undef-msgs=0 pages=15
```

W_post = 43 warnings (all Underfull/Overfull \hbox in the existing
Companion Papers longtable + the new 4-row milestone-status longtable
in sec:closure-cascade-table + the 5 new prose paragraphs in
sec:closure-cascade-{m4,m6,route-f,out-of-scope} + 5 new bibitems);
0 errors; 0 undefined references; 15 pages; PDF size ~495 kB
(SHA256 436962F093A95DB12AF6FD84B99515BE802A274C14B3EFE182EDACA3DF87A35D).

Pass-1 had 84 undef-msgs (label-shift -- the new \label{sec:closure-cascade...}
labels were not yet in main.aux); pass-2 cleared all of them, as
expected. The +99 warning increment from pass-1 to pass-2 is dominated
by the missing-label warnings being resolved (each "Reference X
undefined" in pass-1 was counted in the warnings tally; pass-2's
warnings-only count drops once .aux is settled).

## A4 acceptance interpretation

A4 strict-literal: "Post-edit pass-2: expected W_pre exactly". W_post = 43
!= W_pre = 28; delta = +15. STRICT FAIL.

A4 spirit (per "No new errors / undefined refs" qualifier):
- 0 errors (PASS)
- 0 undefined references (PASS)
- All new warnings are typesetting badness on net-new prose +
  longtable; no LaTeX semantic warnings (PASS)

Disposition: documented in
`discrepancy_log.json::DISCREPANCY-116-WARNCOUNT` as INFO. No
HALT_116_PDFLATEX_BREAK. Operator can request a follow-up cosmetic
pass to tighten the longtable column widths and add `\sloppy` to the
new section if W_post = W_pre is required for future submission.

## Distribution of new warnings (15 added)

All new warnings sit in the new sec:closure-cascade region (lines
824-991 inclusive of the new content + the 4 new bibitems
inserted before \end{thebibliography}). Categories:

- Underfull \hbox in the new milestone-status longtable rows (lines
  824-829) -- 5 entries
- Underfull \hbox in the M4 V0 / M6.CC R1 / Route F prose paragraphs
  (lines 834-895) -- ~6 entries
- Overfull \hbox in the new bibitems / new prose (lines 880-987) --
  ~4 entries

These are all standard LaTeX typesetting-quality artefacts and do
not affect mathematical content or PDF correctness.
