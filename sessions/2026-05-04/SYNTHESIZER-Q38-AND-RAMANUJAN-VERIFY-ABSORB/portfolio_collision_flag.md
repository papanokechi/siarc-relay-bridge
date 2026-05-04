# Portfolio collision flag — Item 17 (Meinardus / G-01 Law) vs Item 23 (P1 PCF rational-contamination)

**Surfaced by:** synthesizer-Claude 2026-05-04 ~21:40 JST
**Status:** DEFERRED for arbitration (Item 17 venue selection
            owns this resolution; cross-domain inventory pass
            required)

## The collision risk

PCF-1 v1.3 (Item 23, P1 PCF rational-contamination) is queued
for Ramanujan Journal as primary target per the 3-decision
close-out 2026-05-04 ~19:11 JST. The 2026-05-04 ~21:40 JST
synthesizer-Claude Track 2 verification pass upgraded this
recommendation to STRONG.

In parallel, Item 17 (Ratio Universality / Meinardus / G-01
Law) was desk-rejected by Acta Arithmetica 2026-05-04 ~19:16
JST and now needs a resubmission target. **Ramanujan Journal's
named scope hits the Meinardus content directly:**

| Item 17 content | Ramanujan Journal named scope |
| --- | --- |
| Meinardus-class partition function asymptotics | "Hyper-geometric and basic hyper-geometric series (q-series)" |
| Partition / G-01 Law content | "Partitions, compositions and combinatory analysis" |
| Asymptotic expansion + universality | "Circle method and asymptotic formulae" |

Synthesizer-Claude observed: "**The Meinardus / G-01 paper may
actually be a stronger Ramanujan Journal candidate than PCF-1**
— partition theory is more central to the journal's identity
than continued-fraction transcendence."

If both Item 23 (PCF-1) and Item 17 (Meinardus) target Ramanujan
Journal as primary, that creates a simultaneous-submission
anti-pattern at the same venue from the same author. The
synthesizer flagged this as the same anti-pattern previously
observed for IJNT, JTNB, and MathComp (where the operator
deliberately spaced submissions to avoid two parallel-active
papers at same venue).

## Historical Ramanujan Journal entry (Item 14)

Item 14 (paper4_takeuchi PSL₂(ℤ) 4-tier) was submitted to
Ramanujan Journal earlier this round and **rejected 2026-04-29
(desk, no reviewer comments; Sub ID 5448b2ad)**. This is in the
record but does NOT count toward the parallel-active count
because it is closed.

The collision risk is specifically Item 23 + Item 17 both being
**parallel-active** at Ramanujan Journal.

## Resolution paths

The Item 17 venue selection task is logged separately as SQL
todo `ratio-universality-meinardus-g01-resubmit-target-decision`
and is deferred per RACI (cross-domain partition-function
asymptotics, not degree-2 PCF analysis; needs its own inventory
pass).

When that inventory runs, the relevant question is:

**Q-CLAUDE-?? (deferred):** of {PCF-1 (Item 23), Item 17
(Meinardus / G-01 Law)}, which one targets Ramanujan Journal
and which one targets a different venue?

Possible orderings (decision-tree skeleton):
1. **PCF-1 first → Ramanujan, Item 17 → other venue**
   - Honors the synthesizer 2026-05-04 ~19:11 JST close-out
     decision (PCF-1 → Ramanujan primary)
   - Item 17 needs a partition-theory-friendly alternative;
     candidates: J. Number Theory (Gallagher), IJNT (already
     holds Item 24), Adv Math, Math Z, Israel J Math, Trans
     AMS, Bull AusMS
   - Risk: PCF-1 may not be Ramanujan's strongest topic-fit
     (synthesizer's framing: partition theory is closer to
     journal identity than CF transcendence)

2. **Item 17 first → Ramanujan, PCF-1 → other venue**
   - Honors the synthesizer's "stronger candidate" framing
   - PCF-1 needs an alternative; candidates per the 5-venue
     analysis from FAA-DESK-REJECTION-RECORD: JTNB, IJNT, Bull
     AusMS, RMJM
   - Risk: re-litigates the 2026-05-04 ~19:11 JST close-out
     decision; would need synthesizer authorization to revise

3. **Sequential — PCF-1 first, Item 17 waits for PCF-1 verdict**
   - Avoids parallel-active at same venue
   - Cost: Item 17 sits in queue until PCF-1's ~3-day median
     turnaround resolves
   - Reasonable if Ramanujan Journal turnaround is short
     (synthesizer-verified at 3-day median)

4. **Both parallel** (anti-pattern; not recommended)
   - Synthesizer-flagged anti-pattern matching prior IJNT /
     JTNB / MathComp avoidance pattern
   - Default-rejected unless operator + synthesizer have
     specific reason to override

## SQL state

- `ratio-universality-meinardus-g01-resubmit-target-decision`
  (pending) — Item 17 venue selection; cross-domain inventory
  required
- `pcf1-meinardus-ramanujan-portfolio-collision-arbitration`
  (NEW — to be inserted) — synthesizer-side; resolves which
  of {PCF-1, Item 17} → Ramanujan Journal vs alternate; gates
  on Item 17 cross-domain venue inventory

## Recommendation (synthesizer-Claude position)

> "That's a strategic decision for later, not now. Just flagging."

Per the synthesizer's own framing: surface and defer.

No agent action requested in this audit deposit beyond
recording the flag for synthesizer + operator arbitration.
