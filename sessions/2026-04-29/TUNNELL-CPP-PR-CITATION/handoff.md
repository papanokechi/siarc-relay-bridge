# Handoff — TUNNELL-CPP-PR-CITATION
**Date:** 2026-04-29
**Agent:** GitHub Copilot (VS Code)
**Status:** COMPLETE

## What was accomplished
Added Mathlib PR #38609 citation to `tunnell_cpp_R1.tex`, producing `tunnell_cpp_R2.tex` and compiled `tunnell_cpp_R2.pdf`. Two citations inserted (Contributions itemize + Reproducibility paragraph). Both reference the lemma `Finset.card_even_of_involution` and link to the PR.

## Citation locations (in `tunnell_cpp_R2.tex`)
- **Contributions list** — new item 3 (after "Axiom-isolation architecture"):
  - lemma name appears at **line 144** (`\texttt{Finset.card\_even\_of\_involution}`)
  - PR hyperlink at **line 148** (`\href{...mathlib4/pull/38609}{PR~\#38609}`)
- **Reproducibility subsection**:
  - lemma name at **line 816**
  - PR hyperlink at **line 818**

## Build report
- pdflatex: 2 passes, both exit 0
- Output: `tunnell_cpp_R2.pdf`
- Pages: **12**
- Size: **492 643 bytes** (~481 KB)
- No unfixable errors; no fixes were required.

## Preamble note
`\usepackage{hyperref}` was already present (line 19) — no change needed for `\href`.

## Verification
```
Select-String -Path tunnell_cpp_R2.tex -Pattern '38609|card_even_of_involution'
```
Returned hits at lines 148 (Contributions PR ref), 818 (Reproducibility PR ref), plus pre-existing references to `card_even_of_involution` in Lean code listings (lines 956, 991). Combined with the escaped-underscore search, the lemma name is confirmed at lines 144 (new), 273 (pre-existing), 506 (pre-existing), 816 (new), 956 (pre-existing).

## Anomalies and open questions
None.

## Recommended next step
papanokechi submits `tunnell_cpp_R2.pdf` to **CPP 2027** when the call for papers opens. CPP 2027 is co-located with POPL 2027; deadline to be confirmed at <https://popl27.sigplan.org> when published.

## Files committed (this session)
- `tunnell_cpp_R2.tex`
- `tunnell_cpp_R2.pdf`
- `handoff.md`
- `claims.jsonl`
- `halt_log.json` (empty)
- `discrepancy_log.json` (empty)
- `unexpected_finds.json` (empty)

## AEAL claim count
1 entry written to `claims.jsonl` this session.
