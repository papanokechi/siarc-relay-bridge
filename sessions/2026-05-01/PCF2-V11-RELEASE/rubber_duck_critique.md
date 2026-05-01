# Rubber-duck critique — PCF-2 v1.1 draft

**Date:** 2026-05-01
**Reviewer (rubber duck):** GitHub Copilot, self-critique pass on PCF-2 v1.1
**Source:** `tex/submitted/pcf2_program_statement.tex`, 14 pp, 0 errors,
0 undefined refs (compile log: pass 3 clean).

---

## 1. Is Conjecture B4's wording precise enough?

**Status:** Mostly yes, with one caveat the human author should review.

The statement
> "for every degree-d PCF (1, b) of generic type in scope … log|δ_n| =
>  -A n log n + α n − β log n + γ + o(1) (n→∞), with A = 2d"

is sharp in the variable that matters (A) and properly relegates α, β, γ
to free constants. The phrase "of generic type in scope" inherits the
hypothesis of Definition `def:Delta3` (irreducible Z-primitive) plus
"the regularity hypotheses of PCF-1 v1.3 §5" — but PCF-1 v1.3 §5
is the section housing Theorem 5 itself, so the back-reference is
cyclic in flavour. **Recommend** a one-sentence list of the three
explicit hypotheses (irreducible, Z-primitive, no exceptional
indicial resonance) inline in §`sec:B4` if a referee asks. For the
v1.1 program-statement level this is acceptable as written — the
purpose is to record the conjecture, not to prove it — and the
hypothesis-tightening can defer to a future PCF-2 results paper.

A second concern: the statement is silent on **uniformity in n** of
the o(1) error term. PCF-1 v1.3 Theorem 5 gives an explicit big-O bound;
B4 here is stated only as a leading-order asymptotic. A future quartic
extension (op:b4-degree-d) should match PCF-1's level of explicitness
and quote a uniform constant.

## 2. Is the 50-row table too dense to print?

**Status:** Borderline acceptable as `\scriptsize`; landscape was
considered and rejected.

The table is reproduced via `\input{../../sessions/2026-05-01/
PCF2-SESSION-C1/wkb_cubic_harvest_v2.tex}`, which uses `\scriptsize`.
With `[ht]` placement and 50 rows × 8 columns, the table fits on a
single page in pass 3 (no overflow warnings; the pdflatex log shows
only the standard `'h' float specifier changed to 'ht'` cosmetic
advisory). Page count went from 11 (v1.0) to 14 (v1.1), with the
table consuming approximately one page on its own.

**Formatting choice:** kept the existing `\scriptsize` + portrait
layout because (a) the content fits without overflow, (b) introducing
`rotating` for a single landscape table inflates the preamble for
marginal benefit, and (c) Zenodo readers prefer continuous portrait
flow. **If a journal referee asks for finer typesetting**, the cleanest
upgrade is splitting the table into two halves (rows 1–25 and 26–50)
rather than going landscape — `\midrule` already supplies the natural
split point.

## 3. Is `op:d2-anomaly` phrased as a genuine open problem?

**Status:** Yes, with a near-miss.

The two named hypotheses are operational:
- **(a)** "The d=2 split is a low-degree artefact (indicial-root
  resonance) and B4 (unsplit) holds for all d ≥ 3."
- **(b)** "The d=2 split is governed by an invariant that becomes
  vacuous or constant at d=3."

Both are **falsifiable by the same experiment**: a quartic harvest
analogous to Sessions B+C1 (op:b4-degree-d). Hypothesis (a) predicts
A = 8 unsplit at d=4; hypothesis (b) is consistent with either a
split or unsplit d=4 outcome and would be confirmed only if the
*controlling invariant* is identified. So (a) is the cleaner test
and the problem statement ties it explicitly to op:b4-degree-d.

**Near-miss:** the parenthetical "a candidate is the parity of the
analytic-rank component of Δ in the indicial expansion" in
hypothesis (b) is a plausible but unsupported guess. **Recommend**
either backing it up with a citation in a future revision or
softening to "an as-yet-unidentified invariant"; for v1.1 it stands
because (b) is presented as an alternative framing, not as the
primary claim.

## 4. Is the B4' falsification subsection honest about the negative
   result?

**Status:** Yes; the subsection deliberately avoids overclaiming.

The text reads "**not** … as a 'publishable counterexample'; we
claim only that B4' has been ruled out as a candidate refinement of
B4." This is the correct framing: B4' was a refined hypothesis
internal to the SIARC working notes (its first appearance was in
Session B's draft of `session_B_results.tex`), not a published
external claim. The negative result is appropriately filed as
near-miss-class evidence in the AEAL chain (§"AEAL note") and is
not promoted to a stand-alone result.

A second honesty check: the subsection acknowledges that the
catalogue's coefficient window may be too narrow to expose a finer
splitting invariant ("[a finer cubic invariant] in a way the present
catalogue's coefficient window cannot detect"). This is faithful to
the empirical reality and avoids the trap of "absence of evidence is
evidence of absence" at the wrong epistemic level.

**Minor**: The label `conj:B4prime` in `\begin{conjecture}[B4', FALSIFIED at d=3]` is correct, but the rendered theorem-style "Conjecture (B4', FALSIFIED at d=3)" environment will appear in the document's Conjecture counter, alongside B1, B2, B3, B3iv, B4. A reader scanning the conjecture list will see a numbered, falsified conjecture, which is exactly the AEAL methodology's intended visibility. No change recommended.

## 5. Other notes

- **Bibliography:** the PCF-1 bib entry was upgraded from "v1.2" to
  "v1.3"; concept DOI 10.5281/zenodo.19934553 is preserved (Zenodo
  concept DOIs auto-resolve to the latest version once v1.3 is
  uploaded). No new bib entries were strictly required since the C1
  inserts cite via prose (bridge URLs in plain `\texttt{...}`)
  rather than `\cite{...}`.
- **Existing label clash resolved:** the v1.0 label `conj:B4` (which
  pointed to "B₃ part (iv): Painlevé-hierarchy reduction") was
  renamed `conj:B3iv`; the new B4 (sharp WKB) takes the freed
  `conj:B4` slot. Two `\ref{conj:B4}` call-sites in the risk register
  and the "Why this matters" section were updated accordingly. No
  semantic shift in those passages.
- **Page count** (14 pp) sits comfortably inside the [10, 16] target.
- **Title block** now displays "Version 1.1" as a sub-line below the
  title, plus `(v1.1)` in `\date{}`. Consistent with the v1.3 update
  pattern of PCF-1.

## 6. Halt-condition check

- LaTeX compile: 3 pdflatex passes, 0 errors, 0 undefined refs. ✓
- Page count: 14 pp ∈ [10, 16]. ✓
- All A2/B/C1 handoffs present in `siarc-relay-bridge/sessions/
  2026-05-01/`. ✓
- 50-row table fits in 1 page in `\scriptsize`, no overflow. ✓
- No halt condition triggered.
