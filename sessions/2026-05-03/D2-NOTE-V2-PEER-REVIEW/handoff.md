# Handoff — D2-NOTE-V2-PEER-REVIEW

**Date:** 2026-05-03
**Source:** Synthesizer chat 2026-05-03 17:21 JST
**Purpose:** Anchor the 5-reviewer peer-review consolidation of
D2-NOTE v2 (Zenodo concept 19996689 / version 19996690, deposited
2026-05-03) as AEAL-grade provenance for the v1.14 picture
references (§1, §24 amendment log) and the merged
D2-NOTE-V2-1-WASOW-FULL-CLOSURE relay (QS-2).

The body below is the verbatim consolidation document (reflowed
from chat into Markdown; all numbers, criteria scores, findings,
revision items, and arbitration questions preserved exactly).

---

## Synthesizer briefing — D2-NOTE v2 arXiv-relevance peer-review consolidation

**Artefact under review:** D2-NOTE v2 (Zenodo concept 19996689 /
version 19996690, 2026-05-03, 6 pp)
**Question to reviewers:** arXiv-relevance on a 1–10 scale, 8
criteria + composite + recommendation
**Reviewers:** 5 independent AI peer-reviewers, all primed with
the same anti-flattery guardrail (§4 of the prompt)
**Date of consolidation:** 2026-05-03 17:21 JST

---

### 1. Quantitative summary

| Reviewer            | C1 fit | C2 orig | C3 rigour | C4 self-cont | C5 cit | C6 endors | C7 mod | C8 value | Composite | Recommendation         |
|---------------------|:------:|:-------:|:---------:|:------------:|:------:|:---------:|:------:|:--------:|:---------:|------------------------|
| R1 (read source+bib) | 6      | 5       | 4         | 4            | 5      | 4         | 5      | 5        | 5         | REVISE_BEFORE_SUBMIT   |
| R2                   | 8      | 6       | 4         | 4            | 6      | 4         | 5      | 6        | 5         | SUBMIT_WITH_MINOR_FIXES|
| R3                   | 8      | 4       | 2         | 4            | 6      | 3         | 3      | 2        | 3         | REVISE_BEFORE_SUBMIT   |
| R4                   | 7      | 5       | 3         | 4            | 6      | 4         | 5      | 5        | 5         | REVISE_BEFORE_SUBMIT   |
| R5                   | 6      | 5       | 4         | 3            | 7      | 4         | 5      | 5        | 5         | REVISE_BEFORE_SUBMIT   |
| **Mean**             | 7.0    | 5.0     | 3.4 ⚠     | 3.8 ⚠        | 6.0    | 3.8 ⚠     | 4.6    | 4.6      | **4.6**   | —                      |
| **Median**           | 7      | 5       | 4         | 4            | 6      | 4         | 5      | 5        | **5**     | —                      |
| **Spread (max−min)** | 2      | 2       | 2         | 1            | 2      | 1         | 2      | 4        | 2         | —                      |

**Recommendation tally:** REVISE_BEFORE_SUBMIT × 4,
SUBMIT_WITH_MINOR_FIXES × 1, SUBMIT_AS_IS × 0,
RECONSIDER_VENUE × 0.

---

### 2. Convergent findings (≥4 of 5 reviewers agree)

**F1 — RIGOUR DEFICIT (C3 mean 3.4; all 5 score ≤ 4)**

This is the load-bearing weakness. Convergent diagnosis across all
5 reviewers:

- The "theorem-grade" claim is overstated for what the artefact
  actually contains.
- A finite symbolic identity-check at $d \in \{2,\ldots,10\}$ +
  citation of Wasow §19 Thm 19.1 + Birkhoff §2 Thm I does not
  constitute a uniform-in-$d$ proof.
- The implication chain from the cited foundation theorems to the
  closed form $\xi_0(b) = d / \beta_d^{1/d}$ is not written out.

R1 surfaced a mechanical, verifiable finding worth flagging to the
synthesizer specifically: the bibliography note in
`annotated_bibliography.bib` for `birkhoff1930formal` itself
states that "the Borel-summability content is treated in the
companion Birkhoff–Trjitzinsky 1933 paper, not in §§2–3 of this
1930 paper" — yet B–T 1933 is not cited in the body of
`d2_note_v2.tex`. This is the specific load-bearing gap: Wasow §19
gives sectorial asymptotic existence, not Borel summability, so
the leap to "Borel-singularity radius" is unanchored. R1 also
notes that §6(d) of the body explicitly flags the Newton-polygon ↔
Wasow shearing-exponent equivalence as still requiring a
literature reference.

**F2 — SELF-CONTAINMENT DEFICIT (C4 mean 3.8; 4 of 5 score ≤ 4)**

- 6 pp is too short for an artefact whose centrepiece is upgrading
  a conjecture to a theorem at all $d$.
- Critical content (proof of the $d=2$ proposition, $d=4$
  measurement, falsification of v1.1 candidate, definition of
  operator $B_d$) is delegated to non-peer-reviewed Zenodo
  deposits (PCF-1, PCF-2, CT v1.3).
- A reader without the SIARC ecosystem on hand cannot reconstruct
  either the setup or any of the proofs.

**F3 — ENDORSEMENT VIABILITY DEFICIT (C6 mean 3.8; all 5 score ≤ 4)**

- A typical mid-career math.NT or math.CA endorser would hesitate.
- Triple-flag pattern: theorem-grade overclaim + heavy
  self-citation to non-peer-reviewed Zenodo + classification
  mismatch.
- All reviewers identify "downgrade language" or "supply the
  proof" as the necessary fix.

**F4 — PRIMARY CLASSIFICATION MISMATCH (3 of 5 explicit)**

R1, R4, R5 explicitly recommend math.NT → math.CA primary, math.NT
cross-list. R2 says math.NT acceptable; R3 doesn't take a strong
stance. Strict reading of the artefact body (Newton-polygon /
Wasow shearing / Borel summation / asymptotics of formal series) —
there is no Diophantine, L-function, or arithmetic content beyond
$\beta_d > 0$.

---

### 3. Divergent findings

**D1 — Subject-matter fit (range 6–8)**

R1 + R5 score 6 (math.CA fit, math.NT mismatch); R2 + R3 score 8
(math.NT acceptable as headline); R4 scores 7 (broad scope
acceptable). The classification question is the primary axis of
disagreement.

**D2 — Timeliness / value-add (range 2–6, largest spread)**

R3 scores 2 ("the mathematical community rarely benefits from
fragmented 6-page isolation notes"); R2 scores 6 ("can save future
authors from hunting through SIARC materials"). The disagreement
is about whether a short standalone consolidation note is a
legitimate arXiv genre or an inappropriately fragmented
contribution.

**D3 — Recommendation severity**

4 of 5 reviewers say REVISE_BEFORE_SUBMIT (more substantive
revision); 1 reviewer (R2) says SUBMIT_WITH_MINOR_FIXES (lighter
touch). R3 is the most severe (composite 3, C8 timeliness 2,
"decline to endorse for math.NT today"). R2 is the most lenient.

---

### 4. Convergent revision items (proposed by ≥3 reviewers)

In rough order of impact:

| #     | Revision                                                                                                                                                            | Proposed by                                                | Effort                       |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|------------------------------|
| Rev-A | Cite Birkhoff–Trjitzinsky 1933 (or Loday-Richaud 2016 ch. 7, or Costin 2008 ch. 5) for the Borel-summability step that Wasow §19 alone does not give                | R1 (specific); R2, R4, R5 (implicit via "implication chain") | ~1 page + 1 bib entry        |
| Rev-B | Write out the uniform-in-$d$ Newton-polygon characteristic-polynomial computation as an explicit Lemma, replacing "by Phase A* symbolic derivation"                 | R1, R2, R3, R5                                             | ~1 page                      |
| Rev-C | Either (a) supply the full implication chain so "theorem" stands, or (b) downgrade headline to "supported conjecture (proven $d=2$, verified $d=4$, symbolic $d \le 10$)" | All 5                                                      | ≥1 paragraph; possibly title edit |
| Rev-D | Reclassify primary → math.CA, secondary → math.NT for the arXiv submission                                                                                          | R1, R4, R5                                                 | submission metadata only     |
| Rev-E | Expand to 10–12 pp with explicit definitions of $B_d$, $\xi_0$, the formal generating function setup, and the falsification context — enough to be reader-standalone | R3, R4, R5                                                 | ~4–6 pages                   |
| Rev-F | Add appendix listing computation logs and exact Zenodo file references (reproducibility recipe)                                                                     | R2, R3                                                     | ~1 page                      |
| Rev-G | Address the rank mapping $q = (d+2)/2$ and "$p = 2$ suffices for all $d \ge 2$" — derive or cite, do not assert                                                     | R1                                                         | ~½ page                      |
| Rev-H | Flag SIARC bridge-session and Zenodo self-deposits as non-peer-reviewed in-body (not just in the .bib note)                                                         | R1, R2, R3                                                 | text-cosmetic                |

Combined revision set is ≈ 4–7 pp of new technical content (Rev-A
+ Rev-B + Rev-G), plus structural changes (Rev-C, Rev-D), plus
optional self-containment expansion (Rev-E).

---

### 5. Arbitration questions for the synthesizer

The synthesizer's job is to convert the 5-reviewer consensus into
a single SIARC-program decision. Open questions:

**Q-S1 — Proof-grade verdict**

Given F1 (rigour deficit, all 5 score ≤4) and the specific R1
finding about the Birkhoff vs. B–T 1933 gap admitted in the
artefact's own bib note: should D2-NOTE v2's "Theorem 1.4"
actually be labelled a theorem in any SIARC-internal usage? The
synthesizer's verdict on this question feeds back into:

- Q20 closure status (currently PARTIALLY ANSWERED on the
  universality axis — does this peer-review feedback tip it back
  to STILL OPEN?)
- The strategic-picture v1.13 §1 row for D2-NOTE v2
  ("THEOREM-GRADE LANDED") — does that label survive?

**Q-S2 — arXiv-mirror sequencing**

Three plausible paths:

- Path A (revise-first): apply Rev-A + Rev-B + Rev-C + Rev-D as a
  D2-NOTE v2.1 republish on Zenodo (which produces a new version
  DOI under the same concept), then ship that v2.1 to arXiv. Time
  cost: ~1 working session.
- Path B (park-and-prioritize): keep D2-NOTE v2 as a Zenodo-only
  artefact (do not ship to arXiv), and instead prioritize a longer
  self-contained paper (PCF-3 / Borel-channel monograph) that
  absorbs the cross-degree identity as a section with a real
  proof. Time cost: ~weeks.
- Path C (downgrade-only): apply only Rev-C(b) — downgrade
  language to "supported conjecture" — and ship to arXiv as a
  short note. Time cost: ~1 hour. Endorsement risk remains (R3,
  R5 would still be cool on this).

The synthesizer should rank these against SIARC program
priorities. R3's view ("natural home is a section in a longer
monograph") is the most aggressive Path-B advocate.

**Q-S3 — Wasow synthesizer cross-link**

The peer-review identifies the same gap that prompt 7 in the v1.13
picture queue (Wasow synthesizer Q20 full-closure arbitration) was
already designed to settle. Should prompt 7 be merged with the
D2-NOTE revise loop, since they share the load-bearing question
(does Wasow §19 + Birkhoff §2 anchoring constitute proof, or is
B–T 1933 / Loday-Richaud / Costin needed)? If yes, the merged task
becomes "Wasow-synthesizer arbitration → produces verdict → feeds
D2-NOTE v2.1 revision."

**Q-S4 — Strategic-picture amendment**

Should the v1.13 picture be amended (creating v1.14) to:

- demote D2-NOTE v2 from "THEOREM-GRADE LANDED" to
  "SUPPORTED-CONJECTURE LANDED, peer-review identified rigour gap,
  revise pending" in §1 + §3 P-NP row?
- add an explicit §6 prompt-queue row for D2-NOTE-V2-1-REVISE?
- update the §23 amendment log with a sub-entry recording this
  peer-review consolidation?

A "no, defer to the synthesizer's verdict" answer is acceptable —
but the synthesizer should at least flag whether the v1.13 picture
needs an interim "peer review pending" annotation.

---

### 6. Recommendation routing (for the operator)

Based on the consensus, the most defensible operator-side action
sequence is:

1. Wait for synthesizer verdict on Q-S1 before making any public
   claim that D2-NOTE v2 is a theorem.
2. Hold the arXiv mirror prompt (queue prompt 4) until the
   synthesizer rules between Path A / B / C in Q-S2.
3. Fire prompt 7 (Wasow Q20 full-closure) — this is now a
   higher-priority dependency than originally scheduled (Q-S3
   rationale).
4. Optionally fire a v1.14 strategic-picture micro-revision (Q-S4)
   to capture the peer-review feedback in the AEAL trail before
   any further dispatches.

The peer-review composite of 5/10 with 4-of-5 REVISE recommendation
is not a "ship as-is" signal but is also not a "kill the artefact"
signal — it is a "the artefact is real but the headline outpaces
the content; revise and re-submit" signal. The exact revision
shape depends on the synthesizer's Q-S1 ruling.

---

### Appendix — Scoring conventions

- Composite calculation: 4 of 5 reviewers used arithmetic mean
  rounded to integer; R1 used mean rounded up by half a point on a
  candour-credit basis. Mean of composites = 4.6, median = 5,
  mode = 5.
- Anti-flattery calibration: all reviewers were exposed to §4 of
  the prompt naming five common AI-reviewer failure modes. R3 most
  aggressively internalized the calibration (composite 3, lowest);
  R2 least (composite 5 + SUBMIT_WITH_MINOR_FIXES, most lenient
  verdict).
- Independence: the 5 reviewers did not see each other's outputs.
  Convergence on F1 (all 5 score C3 ≤ 4) is therefore strong
  evidence, not artefact of a shared narrative.

---

End of consolidation. See `claims.jsonl` for AEAL provenance and
parent picture v1.14 §24 for synthesizer arbitration.
