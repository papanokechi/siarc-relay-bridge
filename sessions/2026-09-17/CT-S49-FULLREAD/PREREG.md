# PREREG — CT-S49-FULLREAD

Written **before** `scripts/check_read_findings.py` existed.

## 0. What this session is, and what it is not

This is the **end-to-end read**: the paper taken as a document rather than
checked section by section. It was commissioned on the explicit ground that
*"a person reading is worth more than any instrument"*, and that judgement is
accepted here without qualification.

**This session does not substitute for that read.** What it does is a
continuous read of all fifteen source files in order, followed by a mechanical
confirmation of every finding against the source. It is an instrument-assisted
read, and its output is a **list of candidates for a human reader**, not a
verdict on the document.

The reason for the confirmation step is the standing hazard: *a reader that
invents a defect fails like one that misses it, worse if acted on.* A read
produces prose observations, which are exactly the kind of finding that cannot
be reproduced later. So every observation is reduced to a **decidable question
about the bytes of the source** before it is reported, and any observation that
cannot be so reduced is reported as an **impression** and labelled
`CONJECTURED`.

## 1. Hypothesis

The paper contains defects of a class that no instrument used in this run could
have caught: **cross-file inconsistencies of statement**. Every prior pass
checked one section, one citation, or one formula. None compared what §1
promises against what §7 does, or what §9 disclaims against what Appendix A
reports.

## 2. Observable

For each finding, a **positive predicate over the source files** — a phrase
present, a phrase absent, a symbol used where another was declared, two
attributions that differ. Each is resolved to `file:line`.

## 3. Falsifiers

- **F1.** If a phrase reported as *absent* is in fact present anywhere in the
  fifteen files, that finding is withdrawn. Threshold: exact match after
  whitespace normalisation, so a line-wrapped occurrence counts as present.
  *(S48-06 was this hazard; the needle is wrap-tolerant by construction.)*
- **F2.** If a phrase reported as *present* is not at the `file:line` given,
  the finding is withdrawn.
- **F3.** If a symbol reported as *undeclared in §1* is in fact declared there,
  the finding is withdrawn.

## 4. Vacuity pre-check

The read's hazard is **manufacturing** findings, so the controls guard the
positive direction:

- **V1.** Every "absent" predicate is paired with a phrase that **is** present,
  which must be found. A reader that finds nothing must be distinguishable from
  a document that contains nothing.
- **V2.** Every "present" predicate is paired with a near-miss variant that
  must **not** be found, so a needle loose enough to wrap is not loose enough
  to match anything.
- **V3.** The file set is resolved **positively**: `section5.tex` must hash to
  `af25048b9b62a6f4…`, the digest CT-S47 verified, so the tree being read is
  the tree that was checked. *(S44-16's rule: name the corpus, resolve it by a
  marker.)*

If any control fails, the affected finding is reported as **uninterpretable**
rather than as a defect.

## 5. Advance prediction

I expect the read to find between four and twelve reportable items, most of
them **notation and cross-reference drift** rather than mathematics, because
every mathematical display has now been routed and checked. The most likely
place for a *substantive* find is the **boundary between a section drafted
early and one drafted late** — specifically §9 and Appendix B, which were
written before the formula pass existed and which contain standing disclaimers
about it.

If that prediction is right it is worth little: it names a class, not an item.
It is recorded so that a find *outside* that class is visible as a surprise.

## 6. Scope limit

**Nothing is repaired in this session.** No `.tex` file is edited. The output
is a list with evidence, for the operator to rule on. Severity assessments are
judgement and are labelled `CONJECTURED`; the underlying facts are `INSPECTED`.
