# layout-fixes-applied.md — VQUAD-PAPER-LAYOUTFIX-001 Stage 2

**Discipline: LAYOUT ONLY.** Every fix below changes line-breaking, alignment, or
font *size* only. No digit, symbol, word, or equation was altered. Proven in
`build-result.md` Stage 3.4 (character-multiset diff: only ±ASCII-hyphen, 0 other
chars).

## A. GLOBAL — `latex/preamble.tex` (cleared 20 → 7)
Inserted after the byte-reproducible guards (kept intact):
```latex
% --- layout only (LAYOUTFIX-001): break long monospace file/script names and
%     relieve tight justification. No content/character changes. ---
\emergencystretch=3em
\makeatletter
\let\vquadorigunderscore\_
\renewcommand{\_}{\vquadorigunderscore\allowbreak}
\makeatother
```
- `\emergencystretch=3em` — last-resort glue so TeX can set a few stubborn lines
  without overflowing. Pure justification relief.
- breakable `\_` — appends an **invisible** `\allowbreak` *after* the underscore
  glyph. The underscore character is unchanged; only a permitted breakpoint is
  added, so long monospace names (`stage4a_methodA_v2.py`, `holonomic_recognition_q3.py`,
  …) may wrap at `_`. `\_` is text-mode only (math subscripts use bare `_`), so the
  redefinition cannot touch any equation.

## B. LOCAL — display/table reflow (cleared 7 → 0). Source `.md` files only.

1. **section-2.md — `align*` q-polynomials** (the persistent 35.66 pt box).
   `q_1` and `q_2` each had the *expanded* polynomial and its *factored* form on a
   single aligned row. Added an aligned continuation line so the `=` factored form
   starts a new line:
   ```
   q_2(z)&=(-36+24\sqrt3)z^2+(-12+8\sqrt3)z^3+(-12+8\sqrt3)z^4\\
         &=4(2\sqrt3-3)\,z^2\,(z^2+z+3).
   ```
   (`\;=\;` → `\\` + `&=`: same `=` and the same factor string; only the position
   of the line break and the alignment change.) Same for `q_1`.

2. **section-2.md — local-exponents `\[…\]`** wrapped in `gathered`; one `\qquad`
   → `\\` (stack the clauses instead of running them across one line).

3. **section-4.md — `eq:constants` (§4.3 wide decimals)** wrapped in `{\small … }`
   (display font follows surrounding text size). Digits unchanged.

4. **section-5.md — `eq:methodB-chain`** `equation` → `equation`+`split` (two `&`,
   one `\\`) so the multi-step equality wraps at `=`.

5. **section-5.md — methods `tabular` (4 cols)** wrapped in `{\footnotesize … }`.

6. **section-6.md — motive-datum `\[…\]`** wrapped in `gathered`; one `\qquad` → `\\`.

7. **section-8.md — A.3 `array{ll}` → `aligned`** (the 152.86 pt extreme).
   Root cause: `{ll}` reserves column-2 width = the **widest** entry (ξ₀'s 17-digit
   decimal) for **every** row. Converted to a single-alignment `aligned` (mirroring
   §4.3), value appended inline via `\qquad`, wrapped in `{\small … }`. ξ₀'s exact
   `\rvert K` spacing and all digits preserved.

## C. p4-factor check (Stage 2.3) — NOT a typo
`eq:p4-factor` reads
`p_4(\xi)=\frac{210276+9720\sqrt3}{418501}\,\xi\bigl(\xi+\tfrac{2}{\sqrt3}\bigr)`.
The `\sqrt3` scope is correct: the factor is `ξ(ξ + 2/√3)`, consistent with
`ξ₀ = 2/√3` and the singular locus `{0, −2/√3, ∞}` (eq. (10)). **No math typo →
no HALT.** Left unchanged.

## Confirmation
No content character changed in any edit above. The only mechanisms used are:
aligned line-breaks (`\\`, `&`), inner math environments (`split`/`gathered`/
`aligned`), font-size scopes (`\small`/`\footnotesize`), and an invisible
`\allowbreak` after `\_`. Load-bearing proof in `build-result.md` §3.4.
