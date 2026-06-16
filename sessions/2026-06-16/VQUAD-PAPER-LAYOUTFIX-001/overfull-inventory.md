# overfull-inventory.md — VQUAD-PAPER-LAYOUTFIX-001 Stage 1.3 / 1.4

Text-block measure = **5.5 in ≈ 396.3 pt** (letterpaper, 1.5 in margins).
Diagnostic build: `\overfullrule` + grep `Overfull \hbox` in
`vquad-periodrep-paper.log`. Original log preserved as `_ORIGINAL_build.log`
(rebuilt from pristine CORRECTIONS-001 sources; that build reproduces
`4ca12a35…` exactly, so this inventory is the true baseline).

## BEFORE — complete list (20 overfull hboxes), generated-`.tex` line numbers
| # | over-width (pt) | location | nature |
|--:|--:|---|---|
| 1 | 35.66 | line 276 (`align*` q-polys) | display: `q_2 =` expanded **and** factored on one row |
| 2 | 3.70 | 387–392 | paragraph w/ inline `\texttt{…\_…}` |
| 3 | 31.49 | line 405 (display) | local-exponents `\[…\]`, multi-clause |
| 4 | 96.14 | 631–637 | paragraph w/ long `\texttt{…\_…}` script name |
| 5 | 22.91 | line 712 (display) | §4.3 wide decimal constants |
| 6 | 32.47 | 743–750 | paragraph w/ `\texttt{…\_…}` |
| 7 | 103.34 | 804–810 | paragraph w/ long `\texttt{…\_…}` |
| 8 | 95.49 | line 849 (display) | `eq:methodB-chain` multi-step equality |
| 9 | 28.25 | 849–856 | paragraph adjacent to the chain |
| 10 | 43.75 | 870–877 | paragraph w/ `\texttt{…\_…}` |
| 11 | 55.43 | 912–922 | paragraph w/ `\texttt{…\_…}` |
| 12 | 24.46 | line 946 | display / inline-wide |
| 13 | 1.74 | 993–997 | paragraph (marginal) |
| 14 | 52.31 | 1191–1196 | paragraph w/ `\texttt{…\_…}` |
| 15 | 1.24 | 1198–1199 | paragraph (marginal) |
| 16 | 16.89 | 1201–1205 | paragraph w/ `\texttt{…\_…}` |
| 17 | **152.86** | line 1232 | **A.3 `array{ll}`**: col-2 width pinned to ξ₀'s 17-digit entry on every row |
| 18 | 72.33 | 1263–1278 | §6 motive-datum `\[…\]` multi-clause |
| 19 | 25.43 | 1263–1278 | methods `tabular` (4 columns) |
| 20 | 102.77 | 1263–1278 | methods `tabular` row |

Over-widths span **1.24 → 152.86 pt** — *not* a single uniform offset, so this is
**not** a paper-size mismatch (a mismatch would shift every box by ~the same amount).

## CLASSIFICATION — MIX (global breaking + local wide displays)
Two root mechanisms:

1. **Unbreakable monospace script/file names** (`\texttt{stage4a_methodA_v2.py}`,
   `holonomic_recognition_q3.py`, `stage4_methodA_results.json`, …). `\texttt`
   underscores carry **no breakpoint**, so the token cannot wrap → runs off the
   right edge. Affects boxes #2,4,6,7,10,11,14,16 (and the small marginal ones
   #13,15 are tight justification). **Layer: global** — `\emergencystretch` +
   a breakable `\_`.

2. **Intrinsically-wide display math / one wide table** that exceed 396 pt even
   when set alone: #1 (q-poly row), #3 (local exponents), #5 (§4.3 constants),
   #8 (methodB chain), #17 (A.3 array — the 152.86 pt extreme), #18 (§6 datum),
   #19/#20 (methods table). **Layer: local** — insert an aligned break, or set
   the block at `\small`/`\footnotesize`, or de-array A.3.

## Proposed fix layers (preference order, per brief Stage 2.1)
- **(a) global, first:** `\emergencystretch=3em` + redefine `\_` to append
  `\allowbreak`. Content-preserving (glyph unchanged; only an invisible breakpoint
  added). Cleared **20 → 7**.
- **(b) local, second:** for the 7 wide displays/table, add aligned line-breaks or
  shrink to `\small`/`\footnotesize`; de-array A.3 → `aligned`. Cleared **7 → 0**.

No geometry/paper-size change is warranted (the diagnosis is unambiguous: the
spread of over-widths and the correct, matching paper sizes rule it out).

## AFTER — 0 overfull hboxes (success criterion met). See `build-result.md`.
