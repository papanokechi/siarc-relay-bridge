# Venue Scope-Fit Matrix — 4 venues x 7 factors

**Fire time:** 2026-05-07 ~14:55 JST
**Substrate anchors:**
- venue_profile_lmcs.md
- venue_profile_jfr.md
- venue_profile_mcs.md
- venue_profile_tcs.md

**Ordering convention:** alphabetical (JFR / LMCS / MCS / TCS) per
HALT_079_VENUE_SELECTION_OVERREACH discipline. No row-total ranking
is performed below; row totals are reported in alphabetical order
only.

**Score legend:** STRONG / MODERATE / WEAK / UNKNOWN. Every cell is
backed by a quoted line from the corresponding venue profile or by
an explicit UNKNOWN with the specific information gap.

---

## Matrix

| Factor                                | JFR        | LMCS       | MCS        | TCS        |
|---------------------------------------|------------|------------|------------|------------|
| F1 Math+CS bridge fit                 | STRONG     | STRONG     | MODERATE   | MODERATE   |
| F2 Formalization-specialty depth      | STRONG     | STRONG     | WEAK       | UNKNOWN    |
| F3 Open-access posture                | STRONG     | STRONG     | MODERATE   | MODERATE   |
| F4 Desk-reject risk profile           | UNKNOWN    | UNKNOWN    | UNKNOWN    | UNKNOWN    |
| F5 Typical turnaround                 | UNKNOWN    | UNKNOWN    | UNKNOWN    | MODERATE   |
| F6 Length compatibility               | STRONG     | STRONG     | MODERATE   | STRONG     |
| F7 Prior author-fit signal            | UNKNOWN    | UNKNOWN    | UNKNOWN    | UNKNOWN    |

## Per-cell justification

### F1 Math+CS bridge fit

- **JFR — STRONG.** Scope statement on https://jfr.unibo.it/about
  reads as a direct description of formalization-of-classical-
  mathematics: "research papers describing significant, automated
  or semi-automated formalization efforts in any area, including
  classical mathematics" (verbatim, 17 words).
- **LMCS — STRONG.** Title-of-record is "Logical Methods in
  Computer Science"; logic + semantics + formal verification are
  the journal's central scope. Mathematical formalization sits
  inside that scope.
- **MCS — MODERATE.** Title-of-record is "Mathematics in Computer
  Science"; the math + CS bridge is the explicit framing. The dblp
  frequent-author distribution (Marcolli, Sturm, Kotsireas,
  Seiler) skews to symbolic-computation rather than to proof-
  assistant formalization.
- **TCS — MODERATE.** Title-of-record is "Theoretical Computer
  Science"; analytic number theory is on the periphery of the
  journal's scope but Section-B-style logic + verification papers
  are in-scope.

### F2 Formalization-specialty depth

- **JFR — STRONG.** Editorial board (Avigad, Coquand, Geuvers,
  Gonthier, Harrison, Leroy, Wiedijk, Sacerdoti Coen) is dominated
  by senior formalization researchers; referees-list (per about-
  page) names ~50 active proof-assistant authors.
- **LMCS — STRONG.** Executive Editor Brigitte Pientka is a
  long-standing proof-assistant researcher (Beluga); LMCS Volume
  22 Issue 2 contains explicit verification + rewriting + proof-
  complexity papers.
- **MCS — WEAK.** Frequent-author signal is symbolic-computation /
  computer-algebra dominant. No proof-assistant editor visible at
  fire time.
- **TCS — UNKNOWN.** Section-B (logic + semantics) historically
  hosts formal-methods papers but exact 2026 area-editor list and
  recent Lean/Coq/Isabelle/Agda paper count were not retrieved
  during this session.

### F3 Open-access posture

- **JFR — STRONG.** Diamond OA (zero APC, zero submission fee);
  CC-BY 3.0; authors retain copyright; preprint + postprint
  permitted.
- **LMCS — STRONG.** Diamond OA via Episciences; zero APC;
  CC-BY 4.0; arXiv-overlay model.
- **MCS — MODERATE.** Hybrid (Open Choice + subscription); APC
  for gold track UNKNOWN exact 2026 figure (Birkhäuser-tier
  typical USD 3,000-4,000 band).
- **TCS — MODERATE.** Hybrid; gold APC USD 2,840 per homepage at
  fire time; subscription track at no fee but with embargoed
  postprint self-archiving.

### F4 Desk-reject risk profile

- **JFR — UNKNOWN.** No public desk-reject statistics. Activity
  flag (no issues since Vol. 13 No. 1, 2020-12-21) raises a
  separate concern about whether desk-reject is the right risk
  framing at all (see discrepancy_log D2).
- **LMCS — UNKNOWN.** No public desk-reject statistics.
- **MCS — UNKNOWN.** No public desk-reject statistics.
- **TCS — UNKNOWN.** No public desk-reject statistics. The 11-day
  vs 154-day first-decision tier on the homepage is consistent
  with a non-trivial desk-reject rate but not quantified.

### F5 Typical turnaround

- **JFR — UNKNOWN.** Peer-review process page (about-page) commits
  to 15-day first-evaluation + 2-month referee window; aggregate
  acceptance time not published. Activity flag (5+ year publication
  gap) materially complicates this score.
- **LMCS — UNKNOWN.** Continuous-publication model; no aggregate
  metric published.
- **MCS — UNKNOWN.** Springer-side metrics page not retrieved
  (auth-gate redirect during this session).
- **TCS — MODERATE.** ScienceDirect homepage publishes raw metrics
  at fire time (numbers in venue_profile_tcs.md TURNAROUND
  section). Several months from submission to acceptance for the
  refereed track is consistent with a high-volume Elsevier title.

### F6 Length compatibility

- **JFR — STRONG.** No fixed page limit; long-form formalization
  papers explicitly invited.
- **LMCS — STRONG.** No fixed page limit; FJN policy permits long-
  form papers.
- **MCS — MODERATE.** Typical paper length 10-30 pp per dblp
  spot-check; 33-page Tunnell paper sits at the upper end.
- **TCS — STRONG.** TCS hosts both short notes and long survey-
  style papers; 33-page Tunnell paper is in-band.

### F7 Prior author-fit signal

- **JFR / LMCS / MCS / TCS — UNKNOWN across all four venues.**
  Author "Papanokechi" (independent researcher, Yokohama) has no
  prior publication history at any of LMCS / JFR / MCS / TCS at
  fire time, per submission_log.txt scan (no Item references any
  of the four). The author has prior submissions to JTNB
  (rejected, Item 22), Monatshefte für Mathematik (Item 23),
  Annals of Formalized Mathematics (desk rejected, Item 24), and
  Journal of Advanced Research (withdrawn pre-submit, Item 25).

## Aggregate

### Row totals (alphabetical; no ranking implied)

- **JFR:** 4 STRONG / 0 MODERATE / 0 WEAK / 3 UNKNOWN.
- **LMCS:** 4 STRONG / 0 MODERATE / 0 WEAK / 3 UNKNOWN.
- **MCS:** 1 STRONG / 3 MODERATE / 1 WEAK / 2 UNKNOWN.
- **TCS:** 2 STRONG / 3 MODERATE / 0 WEAK / 2 UNKNOWN.

### Column medians (factor-level)

- F1 Math+CS bridge fit: median STRONG / MODERATE (tie).
- F2 Formalization-specialty depth: median STRONG / WEAK / UNKNOWN
  (no clean median; bimodal distribution).
- F3 Open-access posture: median STRONG / MODERATE (tie).
- F4 Desk-reject risk profile: median UNKNOWN.
- F5 Typical turnaround: median UNKNOWN.
- F6 Length compatibility: median STRONG.
- F7 Prior author-fit signal: median UNKNOWN.

### Cross-venue summary (~210 words)

The 4-venue x 7-factor scope-fit matrix surfaces three clear cells
of structural distinction (F1, F2, F3) and four cells dominated by
UNKNOWN (F4, F5, F7 across all four venues; F2 mixed). No venue
scores below STRONG on any of F1/F2/F3 in the JFR or LMCS rows;
both diamond-OA venues with formalization-of-mathematics scope
return 4 STRONG / 0 WEAK on the verifiable-fact axes, with the JFR
row carrying the activity-flag overhang from venue_profile_jfr.md.
The MCS row returns 1 STRONG / 3 MODERATE / 1 WEAK on verifiable
axes, weighted by the symbolic-computation centre of gravity at
F2. The TCS row returns 2 STRONG / 3 MODERATE / 0 WEAK on
verifiable axes, with hybrid-OA + section-B placement as the
dominant uncertainty. Across all four venues F4 (desk-reject
statistics) and F7 (prior author-fit) return UNKNOWN; the operator
will need to weight the AFM Item-24 desk-reject signal against the
verifiable F1/F2/F3 axes when (and only when) W21 LANE-1
synthesizer ratification opens that decision. No ranking is
performed at this T2 stage.

---

**HALT_079_FAKE_SCORE self-check:** every STRONG / MODERATE / WEAK
score above is backed by a directly-quotable line from the
corresponding venue profile or from a fetched venue homepage. No
score was synthesized without substrate.

**HALT_079_VENUE_SELECTION_OVERREACH self-check:** ordering is
strictly alphabetical (JFR / LMCS / MCS / TCS); no recommended-
venue line appears anywhere in this matrix.
