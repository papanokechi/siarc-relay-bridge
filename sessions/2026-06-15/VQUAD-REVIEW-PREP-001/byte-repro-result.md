# Byte-reproducibility verification — VQUAD-PERIODREP-PAPER-001

**Outcome: BYTE-REPRO VERIFIED.** Two independent builds produced a byte-identical PDF (identical SHA-256). No fix needed.

## Method

Per the task (Phase B), the committed paper was built twice in succession from
`sessions/2026-06-15/VQUAD-PERIODREP-PAPER-001/latex/`, each build cleaning all
intermediates first and running `pdflatex` twice (for cross-references):

```
# Build N (PowerShell translation of the task's rm/cp):
Remove-Item -Force *.aux,*.log,*.out,vquad-periodrep-paper.pdf
pdflatex -interaction=nonstopmode vquad-periodrep-paper.tex   # pass 1
pdflatex -interaction=nonstopmode vquad-periodrep-paper.tex   # pass 2
Copy-Item vquad-periodrep-paper.pdf buildN.pdf
```

Engine: MiKTeX `pdflatex` (`C:\Users\shkub\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe`).
Comparison: `Get-FileHash -Algorithm SHA256`.

Note: the dual-build was run **without** `SOURCE_DATE_EPOCH` set — i.e. the raw
`pdflatex` invocation from the task, not via `build.py`. This is the stricter
test (it exercises the preamble guards alone).

## Result

| Build | SHA-256 | Bytes | Pages |
|-------|---------|-------|-------|
| build1.pdf | `359D1172AF3F867F4349CF4776A222813A855CD354BC78C0B68CCFB0026C702B` | 698730 | 23 |
| build2.pdf | `359D1172AF3F867F4349CF4776A222813A855CD354BC78C0B68CCFB0026C702B` | 698730 | 23 |

**MATCH = YES** (identical SHA-256, identical byte length). Wall time for the
full 4-pass sequence: ~10 s (warm MiKTeX cache).

## Why it is reproducible (root cause = preamble guards, not the env var)

The committed `latex/preamble.tex` carries the three pdfTeX reproducibility guards:

```
\pdfinfoomitdate=1        % omit /CreationDate, /ModDate
\pdftrailerid{}           % empty /ID trailer (else time+random seeded)
\pdfsuppressptexinfo=-1   % suppress embedded pdfTeX/source banner
```

These suppress every wall-clock- and randomness-derived field in the PDF, so the
output is timestamp-independent **without** needing `SOURCE_DATE_EPOCH`. Confirmed
empirically two ways:

1. The two raw builds above (different wall-clock instants) are byte-identical.
2. The freshly raw-built `vquad-periodrep-paper.pdf` is byte-identical to the
   version already staged in git (which `build.py` produced *with*
   `SOURCE_DATE_EPOCH=1718409600`): after the rebuild, `git status` showed the
   staged PDF as `A ` (added, no unstaged modification), i.e. working tree == index.
   So the env var is redundant given the guards; both paths yield the same bytes.

## Consequence for the Zenodo deposit

No `build.py` change is required for byte-reproducibility. The deposit PDF can be
regenerated bit-for-bit by anyone with the same MiKTeX/pdfTeX major version using
either `build.py` or a bare `pdflatex` ×2. `byte-repro-fix-proposal.md` was **not**
written because no fix is needed (Phase B.3 path not taken).

Caveat (standard, not a defect): byte-identity is guaranteed across runs on the
**same pdfTeX engine build**; a different TeX distribution/version may relayout or
re-encode and produce a different hash. For the deposit, pin the engine version in
the reproducibility statement (already noted in the paper slot's
`reproducibility-statement.md`).

## Hygiene

The transient `build1.pdf`, `build2.pdf` and `*.aux/*.log/*.out` produced by this
check were deleted from the paper slot's `latex/` directory afterwards. The paper
slot returned to its exact pre-check staged state: **21 staged files, 0 untracked,
0 modified** (verified via `git status --short`).
