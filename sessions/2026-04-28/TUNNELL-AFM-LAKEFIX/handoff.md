# Handoff — TUNNELL-AFM-LAKEFIX
**Date:** 2026-04-28
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~10 minutes
**Status:** COMPLETE

## What was accomplished
Filled all four placeholders in `tunnell_afm_R1.tex` (copied to `tunnell_afm_R2.tex`):
Lean version, Mathlib version, GitHub URL, Zenodo DOI. Recompiled to a clean
12-page PDF (exit 0, 490,183 bytes, two pdflatex passes). Wrote AFM cover letter,
claims/halt/discrepancy/unexpected logs, and committed to bridge repo (no push).

## Key numerical findings
- Source: `siarc-relay-bridge/sessions/2026-04-27/TUNNELL-AFM-REVISION/tunnell_afm_R1.tex` (46673 B, 2026-04-27 18:45:36)
- Placeholders remaining after fill: **0** (verified via `Select-String` on `\[INSERT|\[GITHUB|\[ZENODO|\[FILL|\[PLACEHOLDER`)
- pdflatex pass 1 exit: 0
- pdflatex pass 2 exit: 0
- PDF: **12 pages, 490,183 bytes**
- tex SHA-256: `91546b54974e25a4cf54a13ca71fa75380f0c5ed3c0efa421c6ccac2333d8bb9`

## Placeholder fills (line numbers in R2)
All four placeholders were colocated in the `\subsection*{Reproducibility}` block.
Replacement was applied as a single contiguous edit; resulting positions:

| # | Token | Replaced with | Line in R2 |
|---|---|---|---|
| 1 | `[INSERT VERSION FROM lean-toolchain]` | `leanprover/lean4:v4.14.0` | 790 |
| 2 | `[INSERT HASH]` (Mathlib commit) → release `v4.14.0` | `v4.14.0` (sentence rephrased: "Mathlib release") | 791 |
| 3 | `[GITHUB-REPO-URL]` | `https://github.com/papanokechi/tunnell-cnp-lean4` | 788 |
| 4 | `[ZENODO-DOI-PLACEHOLDER]` | `https://doi.org/10.5281/zenodo.19834824` | 794 |

## Step 8 verification grep (`zenodo.19834824|tunnell-cnp-lean4|v4\.14\.0`)
```
788  \url{https://github.com/papanokechi/tunnell-cnp-lean4}.
790  \texttt{leanprover/lean4:v4.14.0}
791  and Mathlib release \texttt{v4.14.0}.  To verify: clone the
794  \url{https://doi.org/10.5281/zenodo.19834824}.
```

## Judgment calls made
- The prompt's prescribed sentence text uses "Mathlib release `v4.14.0`" (not "Mathlib commit"). The R1 source said "Mathlib commit `[INSERT HASH]`". I followed the prompt verbatim and rephrased to "Mathlib release". This is a minor wording change consistent with using a release tag rather than a SHA.
- Author name in cover letter: extracted from `\author{Papanokechi\thanks{...}}` (line 77 of tex) — used "Papanokechi" as signature.

## Anomalies and open questions
None detected.

## What would have been asked (if bidirectional)
None.

## Recommended next step
papanokechi to submit manually at https://afm.episciences.org with:
- `tunnell_afm_R2.pdf` (main manuscript)
- `tunnell_afm_R2_coverletter.txt` (cover letter)
- `formal/CongruentStubs.lean` (supplementary, from the GitHub repo)

## Files committed
- `sessions/2026-04-28/TUNNELL-AFM-LAKEFIX/tunnell_afm_R2.tex`
- `sessions/2026-04-28/TUNNELL-AFM-LAKEFIX/tunnell_afm_R2.pdf`
- `sessions/2026-04-28/TUNNELL-AFM-LAKEFIX/tunnell_afm_R2_coverletter.txt`
- `sessions/2026-04-28/TUNNELL-AFM-LAKEFIX/_pdflatex_pass1.log`
- `sessions/2026-04-28/TUNNELL-AFM-LAKEFIX/_pdflatex_pass2.log`
- `sessions/2026-04-28/TUNNELL-AFM-LAKEFIX/claims.jsonl`
- `sessions/2026-04-28/TUNNELL-AFM-LAKEFIX/halt_log.json`
- `sessions/2026-04-28/TUNNELL-AFM-LAKEFIX/discrepancy_log.json`
- `sessions/2026-04-28/TUNNELL-AFM-LAKEFIX/unexpected_finds.json`
- `sessions/2026-04-28/TUNNELL-AFM-LAKEFIX/handoff.md`

## AEAL claim count
1 entry written to `claims.jsonl` this session.
