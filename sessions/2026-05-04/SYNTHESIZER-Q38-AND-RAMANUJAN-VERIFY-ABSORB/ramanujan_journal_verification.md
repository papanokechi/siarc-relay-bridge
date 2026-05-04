# Ramanujan Journal — verified facts (synthesizer-Claude web-verification 2026-05-04 ~21:40 JST)

## Editorial leadership

| Role | Name | Affiliation | Tenure |
| --- | --- | --- | --- |
| Editor-in-Chief | Ken Ono | University of Virginia | 2024–present |
| Deputy Editor-in-Chief | Atul Dixit | IIT Gandhinagar | (current) |
| Founding Editor-in-Chief (emeritus) | Krishnaswami Alladi | (founding 1997, retired 2024) | 1997–2024 (~30 years) |

**Note on prior misattribution:** the agent stated in chat
2026-05-04 ~19:11 JST that "Berndt stepped down 2024" as the
EiC succession event for Ramanujan Journal. This was **factually
incorrect**. Berndt is on the editorial board but was never the
EiC. The actual succession is Alladi (founding 1997 → retired
2024) → Ono (2024 → present). Synthesizer-Claude surfaced this
correction during 2026-05-04 ~21:40 JST web-verification pass.

The Berndt error never propagated to any workspace file
(verified: grep `Berndt` across `tex/submitted/` + bridge
`sessions/2026-05-04/` returns no matches; the error was
chat-only).

Recorded as DISC_RAMANUJAN_001 in `discrepancy_log.json` of
this audit deposit.

## Editorial leadership signals (Ono-specific)

Ken Ono's research areas include:
- Number theory (general)
- Modular forms
- Partition theory
- Mock theta functions
- Continued-fraction transcendence (direct overlap with PCF-1
  v1.3 content)

This is described by synthesizer-Claude as "highly favorable for
PCF-1's content. ... His own research overlap with continued-
fraction transcendence work is direct."

The 2025 dedicated Special Collection honoring Alladi's 30 years
of service indicates the editorial transition was a planned
generational handover, not a crisis-driven turnover. Editorial
direction is stable.

## Submission-to-first-decision median

**~3 days** (per Springer-published journal statistic).

Comparison to recently-rejected venues this round:

| Venue | First-decision turnaround | Mode |
| --- | --- | --- |
| Aequationes Mathematicae | 3 days | Backlog desk-rejection (no refereeing) |
| Functiones et Approximatio | 9 days | "Publication-space pressure" desk-rejection (no refereeing) |
| Acta Arithmetica | 10 days | Backlog desk-rejection (no refereeing) |
| **Ramanujan Journal** | **~3 days median** | **All decisions (not just rejections)** |

Ramanujan Journal's 3-day median is for *all* decisions —
including those that go to refereeing and accept — which is
fundamentally different from the AMU Poznań ecosystem venues'
3-10 day windows that all resolved to backlog desk-rejection
without refereeing. The volume / backlog dynamic is structurally
distinct.

## AI-disclosure policy

- **Springer-wide policy**: AI-assisted manuscripts allowed
  with disclosure (well-established; multiple Springer-published
  AI-disclosure policy statements 2023-2025).
- **Ramanujan Journal-specific policy**: no journal-specific
  AI ban or restrictive variant surfaces in synthesizer's
  web-verification.
- **Authorial disclosure requirements** (standard):
    - conflicts of interest
    - funding sources
    - compliance with ethical standards

The project §11 standard AI-disclosure wording transfers cleanly
to a Ramanujan Journal cover letter.

## Publisher / ecosystem

- Publisher: Springer (Netherlands)
- EiC affiliation: University of Virginia (US)
- Deputy EiC affiliation: IIT Gandhinagar (India)
- Editorial board: international (verified)
- **No AMU Poznań / Polish ecosystem entanglement.** The
  journal is structurally outside the same-pattern risk class
  as F&A (AMU Poznań) and Acta Arithmetica (AMU Poznań).

## Topic-fit assessment for PCF-1 v1.3

| PCF-1 v1.3 content | Ramanujan Journal named scope area |
| --- | --- |
| Polynomial continued fractions | "Continued fractions" (explicitly listed) |
| Discriminant-sign transcendence predicate | "Diophantine analysis including irrationality and transcendence" (explicitly listed) |
| Number-theoretic dichotomy | "Number theory" (explicitly listed) |
| Asymptotic formulae | "Circle method and asymptotic formulae" (named area) |

**4-of-4 named scope hits.** Synthesizer-Claude characterized
this as "unusually clean topical alignment — three named scope
areas hit directly".

## Verdict on Strategy C (PCF-1 → Ramanujan Journal)

**Pre-verification (2026-05-04 ~19:11 JST close-out):** Strategy C
"tentative recommendation with editorial-transition hedge"
(based on incorrect Berndt-stepped-down framing).

**Post-verification (2026-05-04 ~21:40 JST):** Strategy C
**STRONG RECOMMENDATION WITH VERIFIED EVIDENCE**. Submission-
to-decision median (3 days), Ono-led editorial direction
favorable to PCF-1 content, scope alignment 4-of-4, ecosystem
distance from failed-pattern venues all point in the same
direction.

## Updated submission_log requirements

When the PCF-1 v1.3 Ramanujan Journal submission goes through,
the corresponding submission_log Item entry should record:

```
Target venue: Ramanujan Journal (Springer)
Editor-in-Chief: Ken Ono (University of Virginia, since 2024)
Deputy EiC: Atul Dixit (IIT Gandhinagar)
Publisher: Springer (Netherlands)
Expected first-decision turnaround: ~3 days median
AI-disclosure policy: Springer-standard allows-with-disclosure
Ecosystem risk: none identified (non-Polish, non-AMU)
```

## Standing-instruction note (carry-forward)

The "verify EiC succession before submission" check now formally
joins the SOP-BIBLIOGRAPHIC-VERIFICATION-APPEND standing rule.
Earlier today's chat-side Berndt error illustrated the cost of
skipping this verification: the agent's tentative-recommendation
framing was based on a misattribution. The synthesizer's
~21:40 JST verification pass corrected the misattribution and
upgraded the recommendation simultaneously.
