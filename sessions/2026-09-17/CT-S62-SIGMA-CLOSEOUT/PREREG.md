# PREREG — CT-S62-SIGMA-CLOSEOUT

Written 2026-09-21, **before** running `scripts/check_sigma_closeout.py`.

## Situation

A rejection letter from SIGMA arrived 2026-09-21 ~20:06 JST, 112 days after
the 2026-06-01 direct-email submission recorded at `submission_log.txt`
section A Item 37. The task is to close the record out.

Two prior findings are at stake, both from CT-S61:

- **S61-14 / S61-15** held that receipt was UNCONFIRMED and that SIGMA's
  two-working-day resend remedy had fallen due and not been fired. A decision
  letter can only exist if the paper arrived, so these must be superseded.
- **S61-17** held that the manuscript was under consideration at two venues
  at once, breaching SIGMA's own criteria. A terminal verdict at SIGMA closes
  that from one side.

## Hypotheses, observables, falsifiers

**H1 — the closeout makes Item 37 terminal.**
Observable: the count of ACTIVE section-A items, computed by importing
`make_active_snapshot.py`'s *own* `TERMINAL_V` matcher and `field()` reader
(not a fresh regex written for this session), applied to an **in-memory copy**
of the log with the proposed edit spliced in. The log on disk is not touched.
Falsifier: the active count fails to fall from 4 to exactly 3, or Item 37 is
found already terminal before the edit.

**H2 — the letter is attributable to Item 37.**
Observable: the number of section-A items whose Status names SIGMA.
Falsifier: not exactly 1. If 0 or ≥2, HALT — the letter cannot be attributed
by content and the operator must attribute it from the mailbox.

**H3 — the proposed wording is read correctly by every scanner that will
read it.** The four scanners in `deposit-A076227\out\` share a `TERMINAL`
regex. CT-S61 found it matches the bare word `accepted`, so a Status line
saying "1 reviewer(s) that has accepted" silently killed a live record.
Observable: each scanner's own `TERMINAL` applied to the proposed Status and
Verdict text. Falsifier: the proposed text is read terminal for a reason
other than the rejection — i.e. a word other than `rejected` triggers it.

**H4 — the concurrent-submission situation is changed but NOT resolved.**
Observable: whether Item 36 (The Ramanujan Journal) still carries a
non-terminal verdict, and which manuscript version it holds.
Falsifier for "resolved": if Item 36 is non-terminal, the paper is still live
somewhere and the closeout is one-sided. This is expected to fire; it is
recorded as a finding, not as a failure.

## Vacuity pre-check (run before the result is read)

The H1 observable must be shown to MOVE with the data it is about:

- **(i)** splice a *non-terminal* verdict ("PENDING — awaiting editorial
  acknowledgement") into Item 37 and confirm the active count stays **4**;
- **(ii)** splice the *proposed rejection* verdict and confirm it becomes
  **3**.

If (i) also gives 3, the observable is insensitive to the verdict text and
the test is vacuous — HALT. If (ii) gives 4, the proposed wording does not
close the record — HALT and rewrite the wording.

A further anti-vacuity guard, from CT-S61's own near-miss: every extracted
field is asserted non-trivial (`len > 30`) before it is tested, because a
regex that silently extracts the empty string returns a confident, wrong
negative that is indistinguishable from a real one.

## Thresholds

Fixed before running. Active count before = 4 (from
`CT-S61/outputs/active_snapshot.txt`, derived from log sha256
`70f814b926a5fd67a761bbebe19b5474db69b440e7e3f2340624c79029897433`). Active
count after the proposed edit = 3. Items naming SIGMA = 1. Controls required
to fire = all.

## What this session will NOT do

- It will **not** edit `submission_log.txt`. The record is the operator's;
  this session produces a paste-ready block and proves what it does.
- It will **not** send, reply to, or acknowledge anything.
- It will **not** record a substantive reason for the rejection. The letter
  gives a standing screening formula; treating it as a mathematical judgement
  would be inventing a finding.
- It will **not** re-open or re-run any CT-S61 check; superseded claims are
  superseded by new claims, never edited.
