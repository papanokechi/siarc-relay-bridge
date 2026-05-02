# Handoff — T1-BIRKHOFF-TRJITZINSKY-LITREVIEW

**Date:** 2026-05-02
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~3.5 hours (literature synthesis, no numerical pipeline)
**Status:** COMPLETE (Phase-1 deliverables delivered; Phase 2 deferred to a separate relay)

## What was accomplished

Phase-1 KEYSTONE deliverable: a literature-derived bracket on the SIARC
amplitude exponent $A$ for the polynomial-continued-fraction stratum at
$d \ge 3$, classified into one of the four gap types, with an
AEAL-honest triangulation against the SIARC empirical / theoretical-
prediction record (PCF-2 v1.3, CT v1.3 H4, Theory-Fleet aggregator).
The seven research deliverables (`bt1933_theorem_extraction.md`,
`descendants_synthesis_matrix.{tsv,md}`, `gap_proposition_for_d_ge_3.md`,
`aeal_triangulation.md`, `bibliography_pass1.bib`,
`recommended_next_phase_t1.md`) plus AEAL `claims.jsonl` (17 entries)
and the standard halt / discrepancy / unexpected-finds logs constitute
the Phase-1 corpus. **No proof attempt was made**; Phase 2 is
specified as a downstream relay `T1-BIRKHOFF-PHASE2-LIFT-LOWER`.

## Key numerical findings

* Literature-derivable bracket (Wasow-normalisation reading, paraphrased
  from Wasow 1965 §X.3 + Birkhoff 1911):
  $A \in [\psi_{\mathrm{lower}}(d),\ \psi_{\mathrm{upper}}(d)] = [d,\ 2d]$
  for $d \ge 3$. Provenance: `gap_proposition_for_d_ge_3.md` §3.
* Gap type: **GAP_TYPE_C** ($\psi_{\mathrm{lower}}(d) < 2d =
  \psi_{\mathrm{upper}}(d)$). B4 sits at the literature upper bound;
  Phase 2's task is the lower-bound lift.
* SIARC empirical record (cited from PCF-2 v1.3 / SESSION-T2 verdict.md;
  no re-execution): $A_{\mathrm{fit}} - 2d \in [-10^{-2}, +10^{-2}]$
  on $110/110$ cubic + quartic families at the relevant tail-window
  precision, and $\rho(\log\|\Delta\|_{\mathrm{Pet}}, A_{\mathrm{fit}}
  - 6) = +0.638$ at $n = 50$, $p_{\mathrm{Bonf}} = 8.6 \times 10^{-6}$.
  These narrow $A$ at $d \in \{3, 4\}$ to a sub-percent neighbourhood
  of $2d$, inside the literature bracket.

## Judgment calls made

1. **Wasow-normalisation reading** (Q3 §3). The agent could not pin
   from secondary sources alone whether SIARC's $A$ matches Wasow
   1965's $\sigma$ or Adams 1928's $2\sigma$ Newton-polygon-slope
   normalisation. The agent took the **Wasow reading** as the working
   hypothesis (consistent with all five secondary sources used:
   Wasow 1965, Wimp–Zeilberger 1985, Immink 1984, Sauzin 2016,
   Loday-Richaud 2016) and explicitly flagged the alternative as a
   major-halt branch in the Phase-2 verdict labels. *Logged as D-05.*
2. **Braaksma reference resolution** (Q2 row vi). The relay prompt
   cites "Braaksma 1991+ … Compositio 100"; the agent could not verify
   a Braaksma paper in Compositio Math vol 100 with the given title.
   The closest title match is Ann. Inst. Fourier 42 (1992), 517–540;
   the agent uses that as the principal reference and includes the
   J. Diff. Eqs. 92 (1991) paper as the linear-meromorphic companion.
   *Logged as D-03.*
3. **Year/volume corrections** for Birkhoff 1930 → 1911 and Immink
   1991+ → 1984 (LNM 1085). *Logged as D-01, D-02.*
4. **Did NOT auto-rewrite** Theory-Fleet H1's verdict label
   `B4_PROVED_AT_d≥3_RESIDUE_AT_d=2` (per relay DO-NOT clause). The
   Phase-1 reading that this label is heuristic-grade rather than
   theorem-grade is logged as D-04 in `unexpected_finds.json` for
   Claude / human-reviewer arbitration.

## Anomalies and open questions

**This is the most important section of the handoff.**

The Phase-1 deliverables surface five substantive items the operator
should review before Phase 2 launches:

* **A-01.** **Normalisation-match ambiguity (D-05).** Without primary-
  source consultation of B–T 1933 / Adams 1928 / Wasow 1965 §X.3, the
  agent cannot pin whether the SIARC ansatz $A$ corresponds to
  Wasow's $\sigma$ or Adams's $2\sigma$. The Q3 GAP_TYPE_C
  classification depends on the Wasow reading; under the Adams reading
  the bracket would shift to $[d/2, d]$ and B4 would be **outside**
  the literature upper bound, which is a Phase-2 major-halt branch.
  This must be resolved before Phase 2's target theorem statement can
  be finalised.
* **A-02.** **H1 verdict-label inconsistency (D-04).** The Phase-1
  reading is that B–T 1933 + descendants **predict / are consistent
  with** $A = 2d$ at $d \ge 3$ but do **not** rigorously establish
  it without the SIARC-specialisation argument decomposed in Q3 §5
  (sub-claims P2.1, P2.2, P2.3). H1's `B4_PROVED_AT_d≥3` label is
  heuristic-grade. Claude / the human reviewer should decide whether
  to amend H1's label and the umbrella v2.0 main.tex line 295
  ("extends $A = 2d$ to all $d$ via the Birkhoff–Trjitzinsky
  asymptotic theory") to use the permitted phrasing
  ("predicted by / consistent with the Birkhoff–Trjitzinsky theory").
* **A-03.** **Braaksma reference verification (D-03).** The "Compositio
  100" cite in the relay prompt could not be verified; the closest
  match is Ann. Inst. Fourier 42 (1992). If the operator intended a
  third Braaksma paper (e.g. a Compositio Math paper the agent
  missed), the Phase-2 dependency list may need an update.
* **A-04.** **Resonance-locus content of P2.2.** The Phase-2 sub-claim
  P2.2 (formal-exponent extremality / no resonance cancellation)
  requires an arithmetic argument on the discriminant axis
  $\Delta_d(b)$ that is **not** in any of the post-1933 sources
  consulted in Phase 1. The PCF-2 v1.3 / SESSION-T2 modular-discriminant
  axis finding ($\rho = +0.638$ on the residual $\delta = A_{
  \mathrm{fit}} - 6$) is **sub-leading** and orthogonal to the
  leading-$A$ resonance question, but the **same** modular-arithmetic
  machinery may be the appropriate framework. This linkage needs a
  separate scoping pass before Phase 2.
* **A-05.** **Definition of $A_{\mathrm{PCF}}(b)$ in PCF-1 v1.3 §2 /
  PCF-2 v1.3 §2.1.** The agent did not directly read PCF-1 v1.3 §2
  (which carries the canonical SIARC normalisation of the recurrence
  and the ansatz $\log|\delta_n| = -A n \log n + \cdots$). A primary-
  source pass on PCF-1 v1.3 §2 by the operator (or by a follow-up
  agent with PCF-1 v1.3 access) is the cheapest way to resolve A-01.

## What would have been asked (if bidirectional)

Primary-literature items the agent could not fully access, and what
specifically was needed from each:

* **B–T 1933 (Acta Math 60).** *Needed:* the precise statement of
  Theorems 1 and 2 in the original B–T normalisation; the exact
  form of the "rank stratification" hypothesis; the explicit
  formal-exponent calculation for the second-order rational-coefficient
  case (which is the SIARC PCF stratum). *Without this:* the
  normalisation match (A-01) is unresolved.
* **Adams 1928 (Trans. AMS 30).** *Needed:* the explicit second-order
  formal-exponent formula in Adams's normalisation, to compare
  against the Wasow §X.3 polynomial-coefficient bound and pin
  whether the SIARC $A$ matches Wasow's $\sigma$ or Adams's
  $2\sigma$.
* **Wasow 1965 §X.2–§X.3.** *Needed:* §X.3's exact statement of the
  polynomial-coefficient slope bound, including the precise
  normalisation; §X.4's resonance-correction enumeration. *Without
  this:* Q3 §3's $\psi_{\mathrm{upper}}(d) = 2d$ is a high-confidence
  paraphrase, not a theorem-grade citation.
* **Immink 1984 LNM 1085 §II.3.** *Needed:* the precise Borel-1
  summability statement, including the Gevrey order and the sectorial
  parameters; §II.4's resonant-case treatment.
* **Braaksma 1991/1992 §1.** *Needed:* the multisummability statement
  for fractional-rank cases; whether the "Compositio 100" cite in the
  relay prompt corresponds to a real paper or is a typo for the
  1992 Ann. Inst. Fourier paper.

Borderline cases in Q3 where the bracket depends on a paraphrased
secondary source:

* **B-01.** $\psi_{\mathrm{upper}}(d) = 2d$ depends on the
  Wasow-normalisation match; paraphrased from Wasow 1965 §X.3 and
  Wimp–Zeilberger 1985 §2.
* **B-02.** $\psi_{\mathrm{lower}}(d) = d$ depends on the same
  normalisation match applied to Birkhoff 1911 Thm 4; paraphrased
  from Wasow 1965 §X.2.

Inconsistencies between Theory-Fleet H1 and Phase-1 reading:

* **C-01.** H1 verdict label `B4_PROVED_AT_d≥3` (heuristic-grade in
  Phase-1's reading; should be downgraded to `B4_FORMAL_PROVED_AT_d≥3`
  or `B4_HEURISTIC_AT_d≥3` with the rigorous content gated on
  Phase 2's lower-bound lift). H1's own `Access caveat` admits
  primary B–T 1933 was not opened; Phase-1's reading is consistent
  with that caveat.

## Recommended next step

**Operator action (low effort, high value):** Resolve A-05 (PCF-1
v1.3 §2 normalisation read) and A-01 (Wasow vs Adams normalisation)
by a focused primary-literature pass — institutional library access
to Wasow 1965 §X.2–§X.3 and Adams 1928 §1 plus a careful read of
PCF-1 v1.3 §2.

**Next relay:** `T1-BIRKHOFF-PHASE2-LIFT-LOWER` per
`recommended_next_phase_t1.md`, **conditional on** A-01 being
resolved in favour of the Wasow reading. If the resolution is the
Adams reading, the Phase-2 specification must be reformulated and a
separate halt-recovery relay is needed.

## Files committed

Under `siarc-relay-bridge/sessions/2026-05-02/T1-BIRKHOFF-TRJITZINSKY-LITREVIEW/`:

* `bt1933_theorem_extraction.md` (Q1)
* `descendants_synthesis_matrix.tsv` (Q2)
* `descendants_synthesis_matrix.md` (Q2)
* `gap_proposition_for_d_ge_3.md` (Q3)
* `aeal_triangulation.md` (Q4)
* `bibliography_pass1.bib`
* `recommended_next_phase_t1.md`
* `claims.jsonl` (17 AEAL entries)
* `halt_log.json` (empty)
* `discrepancy_log.json` (empty + pointer to `unexpected_finds.json`)
* `unexpected_finds.json` (D-01..D-05)
* `handoff.md` (this file)
* `verdict.md`

## AEAL claim count

**17** entries written to `claims.jsonl` this session (target $\ge 15$):
T1-LIT-01..05 (bibliographic facts), T1-LIT-06..10 (theorem-statement
paraphrases with provenance), T1-LIT-11..14 (gap-proposition
derivations + classification), T1-LIT-15..17 (AEAL triangulation
findings for E1, E2, E3).

## Epistemic-language scan result

Phase-G2 scan (PowerShell `Select-String` regex
`\b(shows|confirms|proves|demonstrates|establishes|verifies|established|verified|proved|confirmed|shown|demonstrated)\b`,
case-insensitive) was run on every Phase-1 deliverable. Two
genuine context-(iii) usages in `gap_proposition_for_d_ge_3.md` lines
29–30 (PCF-2 v1.3 cubic/quartic harvest "verified") were rewritten
to "supported". All remaining occurrences fall into safe categories:
context (i) (refereed-rigorous theorems of B–T, Turrittin, Wasow,
Immink, Braaksma, Costin, Loday-Richaud), explicitly negated /
*FALSE*-marked misattribution discussion, conditional verdict-label
semantics in tables, or scan-self-check meta-discussion. The scan
**passes**.
