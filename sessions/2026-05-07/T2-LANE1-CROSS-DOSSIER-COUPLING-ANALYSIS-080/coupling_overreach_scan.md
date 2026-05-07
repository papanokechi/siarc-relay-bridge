# Coupling-Overreach Scan — 080

**Phase:** H.3
**Tolerance:** 0 hits on overreach-pattern set in production
deliverables (D2-D12).

---

## §H.3.1 — Overreach-pattern set

Patterns flagged as overreach (asserting which option is
preferred / correct / obvious):

1. "preferred"  (positive ASSERTION-class)
2. "recommended"  (positive ASSERTION-class)
3. "obvious"  (positive ASSERTION-class)
4. "the right pick"
5. "correct"  (when applied to a pick decision)
6. "wrong"  (when applied to a pick decision)
7. "should be picked"
8. "should not be picked"
9. "should select" / "should choose" / "should prefer"
10. "the agent picks …" / "I pick …" / "I choose …"

A hit is ASSERTION-class overreach iff it is asserted as a
synth-side endorsement by agent voice (i.e., the pattern is not
embedded in a negation citation, a meta-policy disclaimer, or a
verbatim substrate citation).

---

## §H.3.2 — Scan results

Tooling: `grep_search` regex `\b(preferred|recommended|obvious|the right pick|correct|wrong|should be picked|should not be picked|should select|should choose)\b`.

### Pattern hits (all classified)

| # | Deliverable | Line | Match | Class | Pass/Fail |
|---:|---|---:|---|---|---|
| 1 | D6 dossier_decision_vector_078.md | (substrate citation) | "no default option declared, none preferred" | CITATION-class (verbatim 078 packet wording, negation framing) | PASS |
| 2 | D6 dossier_decision_vector_078.md | (substrate citation) | "any as 'the obvious / right' pair" | CITATION-class (negation framing inside `>` block) | PASS |
| 3 | D7 dossier_decision_vector_079.md | (substrate citation) | "alphabetically without recommended-pick" | CITATION-class (verbatim 079 packet wording, negation framing) | PASS |
| 4 | D7 dossier_decision_vector_079.md | (substrate citation) | "encode a recommended ordering. … does not order" | CITATION-class + FRAMING (negation citation + agent disclaimer) | PASS |
| 5 | D3-D7 various | (header citations) | "§Recommended next step" | HEADER-citation (handoff section header) | PASS (verb stem `recommend` is in section title; not an overreach assertion) |
| 6 | D12 absorption aid | (header citation) | "§Recommended next step" | HEADER-citation | PASS |

No ASSERTION-class overreach hits found.

### Patterns not detected

The following overreach patterns yield zero matches across all
production deliverables:

- "the right pick" — 0 matches
- "should be picked" / "should not be picked" — 0 matches
- "should select" / "should choose" / "should prefer" — 0 matches
- "I pick" / "I choose" / "I recommend" — 0 matches
- "the agent picks" / "the agent recommends" — 0 matches
- "correct" applied to a pick decision — 0 matches
- "wrong" applied to a pick decision — 0 matches

---

## §H.3.3 — Cross-check against decision-tree leaves

Per `decision_tree_skeleton.md` §E.1 META-policy: "this tree
does NOT mark any leaf as 'preferred' / 'obvious' / 'the right
pick' / 'default' / 'recommended'." Manual cross-check confirms:

- LANE-1.1 (4 leaves): no leaf flagged as preferred. PASS.
- LANE-1.2 (4 leaves): no leaf flagged as preferred. PASS.
- LANE-1.3 (10 leaves): no leaf flagged as preferred. PASS.
- LANE-1.4 (9 leaves): no leaf flagged as preferred. PASS.
- LANE-1.5 (7 leaves): no leaf flagged as preferred. PASS.

Cross-check: per-leaf annotations table (§E.2) — all entries
describe downstream coupling and dispatch only; no entry asserts
preference or correctness.

---

## §H.3.4 — Cross-check against amendment notes

Per `cross_dossier_amendment_notes.md` "Suggested LANE-1
disposition tag" field — "Suggested" is in the field-name only;
no individual note asserts which option synth should pick. The
disposition tags {UNGATE, HOLD, DEFER, TRIAGE} are advisory tags
on the note itself (whether to absorb / hold / defer / triage at
LANE-1), not synth-side option endorsements.

Note disposition-tag breakdown (§F.9): TRIAGE 5 / DEFER 1 /
UNGATE 1 / HOLD 1. Surfaced for synth weighing without asserting
a synth-side option ranking.

---

## §H.3.5 — Verdict

**Coupling-overreach scan: PASS.** 0 ASSERTION-class hits across
all 11 production deliverables. All matched patterns are
CITATION-class (verbatim substrate citations with negation
framing) or HEADER-class (verbatim handoff section header
citations).

End of `coupling_overreach_scan.md`.
