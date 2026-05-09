# Phase B.5 pdflatex compile log — slot 137

**Session**: T2-EXECUTOR-PCF2-V14-M7-V0-AMENDMENT-PREP-137
**Date**: 2026-05-09
**Source under compile**: `tex/submitted/pcf2_program_statement_v14.tex`
**Build environment**: `pdflatex -interaction=nonstopmode`, MiKTeX/TeX Live (workspace-installed)
**Working directory at compile**: `tex/submitted/`
**External \input{} resolution**: workspace-root junction `sessions` → `siarc-relay-bridge\sessions` (created in-fire to resolve 4 `\input{../../sessions/...}` directives that were broken by default in the bare working tree). The junction is reversible (`Remove-Item sessions`); the deposit-time arxiv-pack form flattens these inputs.

## Baseline (G7 — v1.3 reference compile)

| Metric                        | Value                                                                 |
|-------------------------------|-----------------------------------------------------------------------|
| Source                        | `pcf2_program_statement.tex` (75,098 B, 1450 lines)                   |
| pass-1 exit code              | 0                                                                     |
| pass-2 exit code              | 0                                                                     |
| Errors                        | 0 (the single `^!` hit at `pcf2_program_statement.log` L497 is a benign font-name spillover from an Underfull-hbox box-content trace inside the existing v1.3 prose `(R1\!\to\!R1.1\!\to\!R1.2\!\to\!R1.3\!\to\!T2)`, not a fatal error; pass-2 exit 0 + PDF produced is consistent with A3 PASS) |
| Undefined references          | 0                                                                     |
| **W_pre (warnings, all-cat)** | **39**                                                                |
|   Underfull hbox/vbox         | 14                                                                    |
|   Overfull hbox/vbox          | 12                                                                    |
|   LaTeX Warning               | 3                                                                     |
|   Package Warning             | 10                                                                    |
| PDF pages                     | 22                                                                    |
| PDF size                      | 558,151 B                                                             |
| PDF SHA-256 (16-char prefix)  | A92D5D03103E3A8D                                                      |

## Final (Phase B.5 — v1.4 compile)

| Metric                        | Value                                                                 |
|-------------------------------|-----------------------------------------------------------------------|
| Source                        | `pcf2_program_statement_v14.tex` (80,244 B, 1537 lines)               |
| pass-1 exit code              | 0                                                                     |
| pass-2 exit code              | 0                                                                     |
| Errors (`^! `)                | 0                                                                     |
| Undefined references          | 0                                                                     |
| **W_post (warnings, all-cat)**| **44**                                                                |
|   Underfull hbox/vbox         | 14 (Δ = +0)                                                           |
|   Overfull hbox/vbox          | 17 (Δ = +5)                                                           |
|   LaTeX Warning               | 3 (Δ = +0)                                                            |
|   Package Warning             | 10 (Δ = +0)                                                           |
| PDF pages                     | 23 (Δ = +1 vs v1.3 baseline)                                          |
| PDF size                      | 636,049 B                                                             |
| PDF SHA-256 (16-char prefix)  | 471DC7C7EBF8BD4F                                                      |
| Source SHA-256 (16-char prefix)| 0CF4E7DC90C1AC2A                                                     |
| Diff SHA-256 (16-char prefix) | 30371C2EBD9885B1                                                      |
| Diff: +lines / -lines         | +107 / -25                                                            |
| Diff size                     | 10,486 B                                                              |

## Acceptance criteria A1–A8 outcomes

| #  | Criterion                                                                                       | Outcome | Notes                                                                                                                                |
|----|-------------------------------------------------------------------------------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------|
| A1 | pdflatex pass-1 exit code 0                                                                     | PASS    | exit 0                                                                                                                               |
| A2 | pdflatex pass-2 exit code 0                                                                     | PASS    | exit 0                                                                                                                               |
| A3 | 0 errors at pass-2                                                                              | PASS    | 0 hits on `^! ` (corrected regex with trailing space; the looser `^!` regex triggered on a font-name spillover in box-content trace) |
| A4 | 0 undefined references at pass-2                                                                | PASS    | 0                                                                                                                                    |
| A5 | W_post ≤ W_pre + 12 (44 ≤ 39 + 12 = 51)                                                         | PASS    | Δ = +5 (5 new Overfull hbox; minor cosmetic)                                                                                         |
| A6 | PDF page count change ≤ +3 (Δ = +1)                                                             | PASS    | 22 → 23                                                                                                                              |
| A7 | All 3 substrate SHAs (`e857172`, `7f93b9e`, `5f9db69`) appear verbatim in v1.4 source body      | PASS    | hits = 3 / 3 / 1                                                                                                                     |
| A8 | `(SOFT-BRANCH; HARD-BRANCH-PENDING)` appears verbatim ≥ 3 times in body prose                   | PASS    | 4 hits at L58 / L134 / L998 / L1001                                                                                                  |

All 8 acceptance criteria PASS.

## ANTI-CONFLATION post-edit scan (per §3.3)

```powershell
git --no-pager diff --no-index --unified=0 pcf2_program_statement.tex pcf2_program_statement_v14.tex |
  Select-String -Pattern '^\+[^+].*(5\.978|7\.954)'
```

Result: **0 hits** in agent-NEW added lines. The intended-exclusion clause "the M4 V0 numerical content (cubic / quartic A_fit residuals) is unrelated to the M7 V0 j=0 PSLQ closure and is not cited here" appears in the amended `op:j-zero-amplitude-h6` block but does not contain the literal numerical strings `5.978` / `7.954`, so the diff-restricted scan returns clean. Inherited v1.3 §sec:B4 mentions of `5.978` / `7.954` (8 occurrences in the v1.3 body) appear as unchanged context lines and are correctly excluded.

## FV (forbidden-verb) scan on agent-NEW added lines

Verb list scanned: `proves`, `confirms`, `establishes`, `demonstrates`, `shows`, `validates`, `corroborates`, `verifies`, `certifies`, `settles`, `discharges`, `ratifies`.

Result: **0 hits** in agent-NEW added lines (case-insensitive).

Inherited v1.3 prose containing FV-list verbs (e.g., `op:finer-cubic-split` block "absorbs" / etc.) is grandfathered under the slot 116 J2 / 075 J2 / 098 J3 / 121 / 123 verb-list-as-data + inherited-prose exemption pattern.

## Per-warning category breakdown (W_post = 44; for operator-side cosmetic v1.5 cleanup, if desired)

- 14 Underfull hbox/vbox warnings (carried over from v1.3 baseline; same count Δ = 0)
- 17 Overfull hbox/vbox warnings (12 carried over from v1.3 baseline + 5 new from v1.4 added prose; the new occurrences are mostly long URLs / wide math expressions in the new `\paragraph{v1.4 closure (soft branch).}` block — minor cosmetic; would be addressed by `\sloppy` or `\linebreak` insertions in a future cleanup pass)
- 3 LaTeX Warning (carried over; "Reference may have changed" type, expected for cross-references)
- 10 Package Warning (carried over; mostly hyperref / microtype info-class)

A5 NOTE_137_WARNCOUNT_HIGH was **not** triggered (44 ≤ 51 allowance).

## Diff summary

```
b_amendment_v14.diff : 10,486 B
  +lines : 107
  -lines :  25
```

Edit-pass coverage:
- Edit pass 1 (title v1.3 → v1.4): 1 block edited
- Edit pass 2 (date + abstract addendum): 1 block edited (8-line abstract addendum block + date line)
- Edit pass 3 (op:j-zero-amplitude-h6 body, CRITICAL): 1 block replaced (~26 lines → ~95 lines)
- Edit pass 4 (cross-references): 2 status-update parenthetical lines added (at sec:R1-finer-split synthesis + at op:finer-cubic-split successor sentence)
- Edit pass 5 (bibliography): no-op (no new bibitems; per §2.6 expectation)
- Edit pass 6 (amendment log paragraph "What changed between v1.3 and v1.4"): 1 paragraph added (adapted to paper's existing `\noindent\textit{...}\;\;` style — the v1.3 source uses this convention rather than `\paragraph{...}` for "What is new in v1.X" series; structural consistency preferred over the prompt-literal `\paragraph{}` form)
- Edit pass 7 (companion-papers / position-in-stack table): no-op (no per-version companion table in v1.3 source)

Total: 5 productive edits + 2 no-ops = 7 edit passes coverage.

## Operator-side runbook prerequisites

The 4 `\input{../../sessions/...}` directives in the v1.3/v1.4 source bind to a workspace-root `sessions` directory. At deposit time, the operator should either:

1. Use the arxiv-pack flattened form (`siarc-relay-bridge/sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf2_v1.3/pack/`) as the canonical Zenodo-deposit source bundle, regenerating the equivalent for v1.4 by running the same flatten procedure on `pcf2_program_statement_v14.tex`; **or**
2. Recreate the workspace-root `sessions` junction at deposit time (operator preference).

Slot 137's `pcf2_program_statement_v14.pdf` was produced via path 2 (junction) and is artifact-equivalent to what the flatten path would produce.
