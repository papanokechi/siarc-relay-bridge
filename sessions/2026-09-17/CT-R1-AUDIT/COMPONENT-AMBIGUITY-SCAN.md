# Component-ambiguity scan (operator review #17)

**Question.** CT-S18 failed because the packet did not say *which* scalar
reduction of a rank-2 system to compare. Is any existing claim about B, C or
their normal forms ambiguous in the same way?

**Method.** `scan_component_ambiguity.py` over all 21 live `claims.jsonl`
(backups excluded). It flags claims that assert an identity or comparison
between scalar operators, then checks whether the text pins down which
reduction is meant. Output: `outputs/component_ambiguity_scan.txt`,
sha256 `3646bf1999468aaa7fc8832859925f40746924dd30b14f8720e529d59d4eb3ef`.

30 claims compare or identify scalar operators; 10 pin the reduction explicitly;
20 were flagged for hand triage.

**A defect in the scan itself, found and fixed before triage.** The first run
flagged 71 of 74 as ambiguous, because the matching regex caught "companion" —
meaning the companion *paper* — and because the pinning regex missed
`first-component` (hyphenated) and `route 1`. A scan that flags almost
everything is not a scan; it reports the same thing as no scan at all. Both
regexes were tightened and the run repeated. Recorded because the first numbers
were briefly in hand and were meaningless.

## Triage of the 20

### Not exposed — no component choice exists (16)

`R1-74` `R1-76` `R1-77` `R1-82` `R1-83` `R1-87` `R1-89` `c06` `c11` `S6-C18`
`S17-05` `S19-004`, plus `S2-01` `S2-04` `S2-05` `S4-02`.

The operator's expectation was that the B≃C identity should be fine because it
was verified on `(P, Q)`. That is right, and the reason is stronger than the
test used: **B and C are given as scalar operators in the companion, not as
rank-2 systems.** A scalar second-order ODE has exactly one trace-free normal
form — the substitution removing the first-order term is canonical. So no choice
of component is available to get wrong. The ambiguity is created by *reduction
from* a system, and these claims never perform one.

The four `S2-*`/`S4-02` claims are the PCF growth-exponent work, matched only by
the phrase "scalar equation". Different domain entirely; no exposure.

### Exposed (2), and one borderline

* **`S18-010`** (CT-S18, PROVEN) — *"P_U0 - P_C = -1/(z-q), so it does not match
  P in admissible U_0."* This is the defective claim. Its computation is correct
  for the `c`-route; the inference is not. Already adjudicated by `S17-12`, which
  rejects the inference while accepting the computation. **A cold reader's claim
  file is not edited retrospectively** — the adjudication sits beside it.

* **`S16-14`** (CT-S16, STRUCTURAL) — the membership claim. It says System C
  *"is a point of the chart U_0"* without naming the reduction under which the
  match is asserted. The computation behind it used the first-component
  (`b`-route) reduction throughout, and `S17-10` and `S19-006` both confirm the
  match under that route specifically. So the claim is **true as intended and
  under-specified as written**. Clarified by appending `S16-R19-01` rather than
  editing it, per the record convention.

* **`S19-011`** (borderline, not exposed on inspection) — concerns the *local
  formal type* of System C's trace-free normal form. Local formal data at a
  singular point are invariants of the connection, not of a choice of cyclic
  vector, so no component ambiguity arises.

## Conclusion

**One live claim of mine was under-specified (`S16-14`), none were wrong.** The
B≃C family is immune for a structural reason rather than by luck. The defective
claim is the cold reader's, and it was already adjudicated.

The general rule extracted from this is P0's **sixth amendment**: a packet or
claim comparing scalar operators must name the component or the cyclic vector.
