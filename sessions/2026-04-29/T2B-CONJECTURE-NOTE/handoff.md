# Handoff — T2B-CONJECTURE-NOTE
**Date:** 2026-04-29
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes (drafting + 2 compile cycles)
**Status:** COMPLETE.

## What was accomplished
Drafted, compiled, and archived the standalone Zenodo-priority note
on the Transcendental Ratio Identity conjecture
$a_2/b_1^2 = -2/9$. The note (`t2b_conjecture_note.tex`) is a 7-page
`amsart` manuscript stating the conjecture exactly as specified,
summarising the empirical base from sessions
T2B-APERY-INVESTIGATION (`0161a321`), T2B-F25-FALSIFICATION
(`6e28269`), and T2B-RESONANCE-SEARCH (`ab0d70b`), and isolating
the Brouncker boundary class as a non-counterexample.

## Key numerical findings (KEY FACTS audit)
All numeric quantities in the manuscript are listed below with
their location, cross-checked against the prompt's KEY FACTS list.
Every match is exact; no fabricated numbers.

| Quantity                         | Manuscript loc.    | Manuscript value     | Prompt value         |
|----------------------------------|--------------------|----------------------|----------------------|
| $\FF(2,4)$ Trans count           | §3.A, Tbl.1        | 24                   | 24                   |
| $\FF(2,4)$ Trans ratio           | §3.A, Tbl.1        | $-2/9$               | $-2/9$               |
| $\FF(2,5)$ Trans, $r=-2/9$       | §3.B, Tbl.1        | 56                   | 56                   |
| $\FF(2,5)$ Log, $r=-2/9$         | §3.B, Tbl.1        | 12                   | 12                   |
| $\FF(2,5)$ Brouncker, $r=+1/4$   | §3.B + §4, Tbl.1   | 14                   | 14                   |
| Resonance, $r=-3/16$ convergent  | §3.C, Tbl.2        | 2,384                | 2384                 |
| Resonance, $r=-4/25$ convergent  | §3.C, Tbl.2        | 2,396                | 2396                 |
| Resonance, $r=-6/25$ convergent  | §3.C, Tbl.2        | 2,394                | 2394                 |
| Resonance Trans/Log at all 3     | §3.C, Tbl.2        | 0 / 0                | 0 / 0                |
| Combined empirical base          | §3 aggregate       | "approximately 150,000" | ~150,000          |
| Bridge commit `0161a321`         | Disclosure         | cited                | cited                |
| Bridge commit `6e28269`          | Disclosure         | cited                | cited                |
| Bridge commit `ab0d70b`          | Disclosure         | cited                | cited                |

Additional non-prompt-but-true numbers used in §3.B for stratum
context: $\FF(2,5)$ totals (133,100 candidate / 88,224 convergent /
Rat 975 / Alg 9,667 / Trans 70 / Log 12 / Desert 77,500). All
sourced from `t2b_f25_results.json` (commit `6e28269`).

## Conjecture statement audit
The Conjecture appears verbatim as Conjecture 1.1 in §1
(`\begin{conjecture}[Transcendental Ratio Identity]\label{conj:tri}`):

> Let $K(a, b)$ be a degree-$(2,1)$ polynomial continued fraction
> with integer coefficients, $a_2 \ne 0$, $b_1 \ne 0$. If $K$
> converges to a limit $L$ in the Trans stratum --- that is, $L$ is
> not rational and not expressible as a $\mathbb{Q}$-linear
> combination of logarithms of algebraic numbers --- then
> $a_2/b_1^2 = -2/9$. Equivalently, the three-term recurrence
> associated with $K$ has indicial exponents $\{1/3, 2/3\}$ at
> infinity.

This is the prompt's exact statement, with two cosmetic adjustments
made for typography:
- "$\mathbb Q$-linear combination of logarithms of algebraic
  numbers" — typeset using the standard amsmath blackboard-bold
  $\mathbb Q$ rather than the prompt's plain "Q-linear".
- "K(a(n), b(n))" rendered as "$K(a, b)$" (with the dependence on
  $n$ implicit via the standing notation $a(n)=a_2 n^2 + a_1 n + a_0$,
  $b(n) = b_1 n + b_0$ established in the preceding paragraph).

The conjecture is neither weakened nor strengthened relative to the
prompt: same hypothesis (Trans stratum), same conclusion ($r = -2/9$),
same equivalent characterization (indicial exponents $\{1/3, 2/3\}$).

## Brouncker class audit
The $r = +1/4$ Brouncker boundary class is treated in
§4 (~half-page), rigorously separated from
Conjecture 1.1's domain via Proposition 4.1
(`\begin{proposition}\label{prop:brouncker-boundary}`). The
proposition states explicitly that $r = +1/4$ lies on the *positive*
parabolic boundary, *outside* the negative Worpitzky interior to
which Conjecture 1.1 applies. A representative family
$(1, 0, 0, -2, -1) \to L = -4/\pi$ is given, recovering Brouncker's
1655 identity. The 14-family count is restated and the qualitative
distinction (parabolic vs hyperbolic decay) is articulated.

## Tables 1 and 2 cross-check
Both tables present exactly the rows specified in the prompt and
no others. Table 1 (`tab:censuses`) reports 24 / 0 / -2/9 (F(2,4)),
56 / 12 / -2/9 (F(2,5) negative interior), 14 / 0 / +1/4 (F(2,5)
Brouncker) — three rows, matching the prompt. Table 2
(`tab:resonance`) reports the three target ratios with their
convergent / Trans / Log columns (2384/0/0, 2396/0/0, 2394/0/0)
plus a "Combined" row (7174/0/0) — matches the prompt's three rows
and adds the natural sum.

## Compilation status
`pdflatex` (TeX Live, `amsart` documentclass) — clean, two-pass
compile.

- Pass 1: 8 undefined references / citations as expected on first
  pass.
- Pass 2: zero warnings, zero errors, zero overfull boxes, zero
  underfull boxes (after the 4-fraction display in §2 was rewritten
  as an `align*` block to fix a single 41pt overfull on the first
  pass-2 attempt).
- Final PDF: 7 pages, 410,802 bytes.

## Judgment calls made
- **Bibliography:** filled in 7 references in BibTeX-free
  `thebibliography` form. None left as `[?]` placeholders.
  Self-citation for the F(2,4) base case uses the label `[PCF25]`
  per the prompt; the second self-cite `[F25]` references the
  bridge session for the F(2,5) census, since no preprint of that
  result yet exists. Worpitzky 1865, Thron-Waadeland 1980,
  Brouncker via Wallis's *Arithmetica Infinitorum* 1656,
  Schwarz 1873, and Raayoni et al. *Nature* 2021 are all real
  references with verified bibliographic data.
- **Speculative content flagged.** The Schwarz-monodromy
  connection appears in Remark 2.2 explicitly tagged
  `[speculative]` in the heading and "we offer no proof" in the
  body. A separate problem (Problem 5.3) records this as an open
  question rather than a claim.
- **Subjclass codes** chosen: 11A55 (continued fractions), 11J70
  (transcendence), 11J81 (transcendence of values), 11Y65
  (continued fraction calculations), 40A15 (continued
  fractions). Standard for this content.
- **Page count:** lands at 7 pages, the upper end of the 6-7
  target. The Brouncker section and Open Problems each fit
  ~half a page and could be trimmed if a tighter 6-page version
  is wanted later, but 7 pages is normal for a Zenodo note with
  two tables and a full bibliography.
- **No proof attempts.** Per the prompt's "do not fabricate
  proofs" instruction, the note states the conjecture, summarises
  the evidence, and lists open problems. The only formal claim
  is Lemma 2.1 (the discriminant-based regime classification) and
  Proposition 4.1 (the Brouncker boundary lies outside the
  Worpitzky interior), both of which are immediate from the
  definitions and require no novel mathematical work.

## Anomalies and open questions
- **No $r = -2/49$ test.** The prompt's KEY FACTS list noted
  that the resonance experiment did not test the
  $-2/49$ ratio because that requires $|b_1| = 7$, outside the
  $|b_1| \le 5$ envelope. The note flags this in §5 as candidate
  falsifier (4) with status "untested at the time of writing".
  This is the natural next-session experiment.
- **The Schwarz speculation is intriguing but unverified.** The
  triangle-group $\Gamma(3,3,\infty)$ language and the
  fundamental-domain reasoning in Remark 2.2 are essentially
  heuristic; whether the integer-monodromy obstruction is genuine
  or a coincidence of small-discriminant arithmetic would require
  serious modular-symbol or hypergeometric-monodromy work to
  establish. We have flagged this conservatively.
- **The pre-compile encoding bug** (`\textquotedbl` failure under
  OT1) was a small editorial slip that resolved on adding
  `\usepackage[T1]{fontenc}` before `lmodern`. Worth memorising:
  with `lmodern` always pre-load `[T1]{fontenc}`.

## What would have been asked (if bidirectional)
1. Should the Schwarz / triangle-group speculation be pulled
   entirely (more conservative) or kept as a flagged remark
   (gives the reader a research direction)?
2. Should the bibliography include the Khan / Kontorovich / Lentz
   parabolic-Worpitzky paper(s)? The note currently relies on
   Thron-Waadeland for that material.
3. For the Zenodo posting, do you want the SIARC bridge URLs in
   the Disclosure section to be the bridge URLs (current choice)
   or the underlying `pcf-research` repo?

## Recommended next step
1. Submit the PDF to Zenodo for DOI / priority timestamp.
2. Run the deferred $r = -2/49$ resonance test at
   $|b_1| \le 7$ (predicted ~10 minutes) to update Table 2 with
   a fourth row before any journal submission.
3. Pursue Problem 5.3 (Schwarz monodromy) via a Galois-theoretic
   reading of the second-order linear recurrence; the
   $\{1/3, 2/3\}$ exponents are suggestive of the dihedral
   $S_3$ action on the cube roots of unity.

## Files committed
- `t2b_conjecture_note.tex` (~22 KB) — full LaTeX source.
- `t2b_conjecture_note.pdf` (~411 KB, 7 pages) — compiled output.
- `handoff.md` — this file.

## AEAL claim count
1 entry to be written to `claims.jsonl` this session:
- claim: "Manuscript `t2b_conjecture_note.pdf` (7 pages,
  SHA-256 ...) compiled cleanly from `t2b_conjecture_note.tex`
  with `pdflatex` two-pass, all numerical figures cross-checked
  against the underlying bridge sessions";
  evidence_type: "computation"; dps: n/a (compilation);
  reproducible: true; script: "pdflatex t2b_conjecture_note.tex".
