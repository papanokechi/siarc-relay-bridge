# D6 — H1 (Theory-Fleet) label disposition advisory

**Task:** T1-A01-NORMALIZATION-RESOLUTION — STEP 8
**Date:** 2026-05-03
**Scope:** Advisory only. Do NOT modify any H1 file directly.

---

## Recommendation: **HOLD-FOR-SYNTHESIZER-ARBITRATION**

The Phase-1 (2026-05-02) handoff flagged that H1 (Theory-Fleet)
carries the verdict label `B4_PROVED_AT_d≥3_RESIDUE_AT_d=2`, while
the Phase-1 reading was that B4 = 2d at $d \ge 3$ is heuristic-grade
pending Phase 2. The relay (STEP 8) asked the agent to choose one
of three dispositions: keep, downgrade to
`B4_HEURISTIC_AT_d≥3`, or hold for synthesizer arbitration.

The present session's verdict is `A01_WASOW_READING_CONFIRMED`
with explicit caveats — specifically:

* **Caveat 1 (Wasow §X.3 NIA on disk).** The polynomial-coefficient
  slope bound $\mu \le 2d$ that supplies the **upper end** of the
  Phase-1 bracket inherits Phase-1's paraphrase and is **not**
  verbatim-attested from Wasow §X.3 in this session.
* **Caveat 2 (Adams 1928 NIA on disk).** All Adams-row entries in
  the triangulation are transitive (via Birkhoff 1930 page 2 + B–T
  1933 page 5).
* **Caveat 3 (bracket-tightness paraphrase).** The bracket
  derivation $A \in [d, 2d]$ inherits Phase-1's paraphrase and was
  not re-derived.

Under these caveats, the verdict supports **the literature-rigorous
**normalisation-match** for A-01 but not yet the literature-rigorous
**bound** A ≤ 2d**. This is enough to launch Phase 2 (which lifts
the **lower** bound, and would be neutralised by an Adams-reading
verdict but is **not** affected by these residual paraphrase caveats),
but it is **not yet enough** to upgrade the umbrella v2.0 main.tex
phrasing "extends … via the Birkhoff–Trjitzinsky asymptotic theory"
to literature-rigorous status without further work.

The three available dispositions then read:

* **Keep H1 label as-is.** Reasonable if the operator + synthesizer
  judge that the umbrella v2.0 main.tex L295 phrasing is honest
  **as currently written** (i.e., it does not claim a literature
  rigorous theorem at $d\ge 3$, only an extension via the B–T
  asymptotic theory). The present session's evidence is consistent
  with this reading, but the agent does NOT have visibility into
  the umbrella v2.0 main.tex audit trail beyond what is in the
  bridge.
* **Downgrade to `B4_HEURISTIC_AT_d≥3`.** Conservative; reflects
  the residual paraphrase caveats. The agent considers this
  defensible but possibly over-conservative if Phase 2 is expected
  to land soon and the umbrella phrasing is already AEAL-honest.
* **Hold for synthesizer arbitration.** The present recommendation.
  The agent is not in the best position to weigh the umbrella v2.0
  phrasing against the residual paraphrase; the synthesizer (with
  full umbrella + picture + Theory-Fleet visibility) is. **Recommend
  hold until synthesizer reviews the present verdict + caveats and
  decides between keep / downgrade.**

---

## Concrete operator action

* Surface the present session's verdict + three caveats to the
  synthesizer in the next relay round.
* Do **not** modify any H1 file in this session.
* Do **not** modify umbrella v2.0 main.tex L295 in this session.
* Do **not** modify PCF-1 v1.3 §6 in this session.

If the synthesizer subsequently decides to keep H1 or downgrade,
the operator-side action is straightforward (a single-line label
change in the H1 metadata + an entry in the picture revision log).
The present advisory does not pre-empt that decision.

---

## Why not "keep as-is" directly?

The present session's verdict `A01_WASOW_READING_CONFIRMED` is
**carried by transitive Birkhoff/B–T evidence**, not by primary
Wasow §X.3 access. A future Phase-2 attempt may surface a
non-resonance / non-degeneracy obstruction that requires Wasow §X.3
verbatim — at which point the H1 label may need re-evaluation. The
synthesizer is best placed to budget for this contingency.

## Why not "downgrade" directly?

Downgrading would over-correct: the present session has resolved
the A-01 ambiguity in favour of the Wasow reading, removing the
primary obstacle to Phase 2 launch. A downgrade would suggest the
literature evidence is still ambiguous on the **normalisation match**
— which it is **not** after the present triangulation. Reflexive
downgrading would also create unnecessary delta in the picture v1.14
amendment log.
