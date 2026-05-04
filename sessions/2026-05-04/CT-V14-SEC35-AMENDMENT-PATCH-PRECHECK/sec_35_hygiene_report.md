# CT v1.4 §3.5 amendment — LaTeX hygiene + render dry-check

**Task:** CT-V14-SEC35-AMENDMENT-PATCH-PRECHECK
**Scope:** the inserted `\paragraph{Layer note (added v1.4).}`
block only (≈190 words; lines added by `sec_35_amendment.patch`).
**Method:** static syntax inspection on the proposed paragraph;
no `pdflatex` compile (out-of-scope per spec §6).

---

## D.1 — Bracket-balance check

| Construct                                    | Opens `{` | Closes `}` | Balance |
|----------------------------------------------|-----------|-----------|---------|
| `\paragraph{Layer note (added v1.4).}`       | 1         | 1         | OK      |
| `\cite{costin2008asymptotics,birkhofftrjitzinsky1932analytic,jimbomiwa1981monodromy}` | 1 | 1 | OK |
| `\emph{L-equation layer}`                    | 1         | 1         | OK      |
| `$e^{Q(x)}\,s(x)$` (superscript group)       | 1         | 1         | OK      |
| `\emph{isomonodromic-deformation layer}`     | 1         | 1         | OK      |
| `\Cref{thm:vquad-cc}`                        | 1         | 1         | OK      |
| `H_{III'}` (subscript group)                 | 1         | 1         | OK      |
| `\emph{not}`                                 | 1         | 1         | OK      |
| **TOTAL**                                    | **8**     | **8**     | **OK**  |

`\begin{...}` / `\end{...}` introduced: **0**. No new
environments. **PASS.**

## D.2 — Forbidden-verb scan (per _RULES.txt §D)

Patterns scanned (case-insensitive substring) on the inserted
paragraph:

| Pattern                            | Hits | Notes                               |
|------------------------------------|------|--------------------------------------|
| `trivial`                          | 0    | —                                    |
| `obvious`                          | 0    | —                                    |
| `clearly`                          | 0    | —                                    |
| `easily seen to`                   | 0    | —                                    |
| `we claim`                         | 0    | —                                    |
| `it is clear that`                 | 0    | —                                    |
| `shows` (prediction/conjecture)    | 0    | Word absent.                         |
| `confirms` (prediction/conjecture) | 0    | Word absent.                         |
| `proves` (prediction/conjecture)   | 0    | Word absent.                         |
| `Wasow §X.3` (deprecated form)     | 0    | Wasow not cited in amendment.        |

The amendment uses neutral / observational verbs:
`is described`, `is satisfied by --- not equal to`,
`describes how the monodromy data deform`,
`is read as an identity`, `returns the deformation equation`.
These do not assert proof of an open conjecture or
falsifiable prediction; they characterise pre-existing,
literature-anchored definitions. **PASS.**

## D.3 — pdflatex compile

Out-of-scope per spec §6 (operator-side post-review).
**SKIPPED (by design).**

## D.4 — Other render-relevant observations

* The amendment uses the macro `\Vquad` and `\CC` — both are
  already defined and used pre-amendment in §3.5 (e.g.
  `\Vquad` at line 967, `\CC` at line 970, ct_v1.4_main.tex);
  no new macro needed.
* The amendment cites `\Cref{thm:vquad-cc}` (already defined
  in §3.3, ct_v1.4_main.tex line ~796–820) — cross-reference
  resolves on compile.
* Math expression `[\partial_x - X,\,\partial_\lambda - \Lambda] = 0`
  uses `\partial`, which is a standard built-in; no new
  package required.
* No `\label{}` introduced inside the new `\paragraph{}` —
  the paragraph is non-numbered and not back-referenced
  elsewhere (intentional; v1.4 amendment is a clarifying
  note, not a numbered statement).

## Verdict

`HYGIENE_DRY_CHECK_PASS` — bracket balance OK; no forbidden
verbs; no deprecated forms; no new macros / environments /
package dependencies introduced. Patch is render-clean
modulo pdflatex compile (operator-side post-review).
