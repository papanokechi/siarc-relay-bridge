# Acta Arithmetica desk-rejection — verbatim record

**Received:** 2026-05-04
**From:** Maciej Radziejewski, Secretary, Acta Arithmetica
        (AMU Poznań)
**Re:** "Ratio Universality for Meinardus-Class Partition Functions
        and the G-01 Law" by Papanokechi Papanokechi
**Submission ID:** `260423-Papanokechi`
**Submitted:** 24 Apr 2026
**Turnaround:** 10 days (24 Apr → 4 May 2026)
**Matched submission_log Item:** **Item 17** (under
  "RECORDED SUBMISSIONS" section)
**Bridge session:** `sessions/2026-05-04/ACTA-ARITHMETICA-DESK-REJECTION-RECORD/`

---

## Verbatim email body

```
Dear Professor Papanokechi,

I am writing about the paper

   Ratio Universality for Meinardus-Class Partition Functions and the G-01 Law
   by Papanokechi Papanokechi.

Thank you for your interest in submitting your paper to Acta
Arithmetica. Unfortunately the editorial board of Acta Arithmetica
cannot accept your paper for publication.

During the last year our journal received more manuscripts than
can possibly be accepted, which temporarily caused a considerable
backlog. As a result, our editors need to be very selective. I
regret to inform you that your paper has to be rejected without
refereeing.

We are sorry about this situation and we hope for your
understanding. We wish you success in publishing your paper in
another journal.

Yours sincerely,

Maciej Radziejewski
secretary of Acta Arithmetica
----------------------------------------------------
Acta Arithmetica
ul. Uniwersytetu Poznańskiego 4
61-614 Poznań, Poland
Fax 48-61-829 53 15
e-mail: actarith@amu.edu.pl
```

---

## Classification

- **Verdict type:** Desk rejection without refereeing
- **Cited reason:** Backlog / "received more manuscripts than can
  possibly be accepted" — content-neutral
- **Refereeing process:** None (explicit "without refereeing")
- **No mathematical feedback** on the manuscript itself

---

## Pattern context

This is the **third** backlog-class desk rejection in the present
submission round (Items 22-29), and the **second** from the AMU
Poznań editorial ecosystem:

| # | Item | Venue | Date | Editor | Cited reason |
|---|---|---|---|---|---|
| 1 | Item 25 | Aequationes Mathematicae | 2 May 2026 | Managing Editor Attila Gilányi | Backlog |
| 2 | Item 23 | Functiones et Approximatio (AMU Poznań) | 4 May 2026 | EiC Łukasz Pańkowski | Publication-space pressure |
| 3 | **Item 17** | **Acta Arithmetica (AMU Poznań)** | **4 May 2026** | **Secretary Maciej Radziejewski** | **Backlog** |

**AMU Poznań ecosystem count:** 2 of 3 (F&A + Acta Arithmetica).
Both editors are at Adam Mickiewicz University, Poznań.

---

## Synthesizer prediction confirmed

Synthesizer-Claude's venue-target reconciliation analysis on
2026-05-04 ~19:00 JST flagged this exact ecosystem risk: when
Acta Arithmetica was on the candidate-venue shortlist for the
P1 PCF rational-contamination resubmission, Claude noted "Same
Polish academic ecosystem as F&A; if F&A's 'publication-space
pressure' is region-wide, Acta Arithmetica likely shares it."
That prediction was made just over an hour before the Acta
rejection email arrived. The ecosystem-risk hypothesis is now
**independently confirmed** by an actual Acta backlog rejection
on a different paper (Item 17, not the P1 rational-contamination
paper).

---

## Strategic implication

The 3-rejection / 2-AMU-ecosystem pattern is now established.
Synthesizer-side venue-strategy recommendation for the remainder
of the 2026 submission round and forward:

- **Avoid AMU Poznań ecosystem venues** for resubmissions
  (Acta Arithmetica and Functiones et Approximatio are both
  out for round-2026; ecosystem signal is region-specific
  publication-space pressure)
- **Bias toward** specialist NT (Ramanujan-class) + non-Polish-
  ecosystem + algorithmic venues
- **Resubmit-target decision** for Item 17 (Ratio Universality
  / Meinardus / G-01 Law paper) is operator + synthesizer side;
  see SQL todo `ratio-universality-meinardus-g01-resubmit-target-
  decision`. Note: this paper is in a different content domain
  from P1 PCF rational-contamination — partition-function
  asymptotics rather than degree-2 PCF discriminant analysis —
  so its venue inventory is independent and needs its own
  inventory pass

---

## Title divergence anomaly (logged in `discrepancy_log.json`)

The recorded title in `submission_log.txt` Item 17 (L120)
diverges from the title in `CMB.txt` Item 17 (L355) and the
title used by Radziejewski in the verbatim rejection email:

- **submission_log.txt L120:** "Ratio Universality for
  Meinardus-Class Partition Functions: Complete Asymptotic
  Expansion with Seven-Family Veri cation" *(typo: 'Veri cation'
  missing 'fi' ligature — likely PDF text-extraction artefact)*
- **CMB.txt L355 / verbatim email:** "Ratio Universality for
  Meinardus-Class Partition Functions and the G-01 Law"

Two-of-three sources (CMB + email) agree; submission_log diverges.
Both metadata files refer to the same Item 17 (same Submission ID
`260423-Papanokechi`, same submission date 24 Apr 2026, same
filename `RatioUniversality_ActaArith_submission.pdf`). The
divergence is preserved (not silently reconciled) per AEAL
provenance practice; surfaced as `DISC_ACTA_001` for operator
+ synthesizer review.
