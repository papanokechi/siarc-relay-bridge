# A-115-RECONCILED stamp file

**Date:** 2026-05-08
**Agent:** GitHub Copilot (VS Code)
**Bridge commit at deposit time:** dd9c096 (parent at staging)
**Prompt:** SIARC Relay Prompt 114 — A-115 reconciliation
**Task ID:** T2-OPERATOR-A-115-RECONCILIATION-LABELING-CONVENTION-128
**Sequential shifted:** 126 (planned) -> 127 (fallback) -> 128 (next-available; both 126 and 127 were taken at fire time)

## Summary

A-115-1 (PRIMARY — labeling-convention divergence) and A-115-2
(SECONDARY — LIT dict source-string subsec misattribution) reconciled
per audit_verdict.md L301-307. The unsubscripted-Greek shorthand
$(\alpha,\beta,\gamma,\delta)$ in p12 Intro + p12 sec:vquad now reads
explicitly as Hamiltonian $(\alpha_\infty, \alpha_0, \beta_\infty,
\beta_0)$ in both prose and the math display, with a load-bearing
cross-walk footnote at sec:vquad documenting the disambiguation.
The LIT dict in `vquad_p3d6_recovery.py` was relabeled to
machine-readable Hamiltonian names and its `source` field corrected
to point at the actual subsec containing the 4-tuple (subsec
"Painleve III(D_6) parameters" at p12 L975).

UF-115-3 (V_quad as Okamoto-degeneration locus / D_6 -> D_7
boundary) remains open for a future structural relay prompt and is
explicitly out-of-scope for this documentation-only reconciliation
task.

## Files modified

| File | SHA-256 (pre, on-disk) | SHA-256 (post, on-disk) |
|---|---|---|
| `tex/submitted/p12_journal_main.tex` | 82173A09521D6676ADC523E1D55CD1310F693479608A9F98EB980689A4786853 | DAC0282ED4C6F8BC1046003ACAEDA0B84593712F9336404AAFDC18B0A6A176A7 |
| `pcf-research/channel/cc_pipeline_2026-05-01/vquad_p3d6_recovery.py` | 19E96D3FDD83D0CB2A2B59598C5641A23AC8C32C2907342FD7D4AE75F15C072D | 28B8DE47161254AE17B2C4E98F3C7B54D35D9864E6B9C4D3D0E859C0B27B7DC5 |

(Diff-header SHA values are LF-normalised UTF-8 reconstructions;
see discrepancy_log.json D-128-1.)

## Edit summary

- D1 (p12 Intro L232-237): bracketed Hamiltonian-name expansion
  added; classical-ODE shorthand retained for prose continuity.
- D2 (p12 sec:vquad math display L981-985): block-display equation
  expanded to two math lines, classical-ODE on first line and
  Hamiltonian on second line, joined by `\equiv` then `=`.
- D3 (p12 sec:vquad cross-walk footnote): inserted on the word
  "parameters" at the head of the math display; cites Okamoto1987
  sect 1.1 and IwasakiKimuraShimomuraYoshida sect VII.4 (KNY 2017
  citation omitted; bib-key absent — see UF-128-NEW-BIBKEY).
- D4 (vquad_p3d6_recovery.py L48): LIT dict P_III_D6_params
  relabeled to Hamiltonian convention.
- D5 (vquad_p3d6_recovery.py L49-50): source-string subsec fix
  ("Stokes data" -> "Painleve III(D_6) parameters"; subsec
  existence cross-checked at p12 L975).

## pdflatex compile

- Baseline (pre-edit): exit 0; 24 warning/error lines (all benign:
  hyperref Unicode-token, h-float-specifier, infwarerr meta).
- Post-edit pass 1: exit 0; 25 warning/error lines (the +1 is the
  expected "Label(s) may have changed. Rerun" cross-ref shift).
- Post-edit pass 2 (rerun): exit 0; 24 warning/error lines
  (matches baseline). 21-page PDF produced. No new errors. No
  undefined references.

## Pointer

Full diff: `a_115_reconciliation.diff` (3175 bytes, 2 file hunks,
~6 hunks total: 2 in p12 + 1 in vquad_p3d6_recovery).

## SQL todos closed by this stamp

- `a-115-1-reconciliation-prompt-draft` -> done
- `a-115-1-reconciliation-prompt-followup` -> done
- `a-115-2-lit-dict-source-string-fix` -> done

`uf-115-3-okamoto-degeneracy-structural-prompt` remains pending.
