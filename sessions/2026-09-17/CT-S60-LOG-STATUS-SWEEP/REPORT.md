# REPORT — CT-S60-LOG-STATUS-SWEEP

**Task.** Sweep section A of `submission_log.txt` for entries whose `Status:`
line disagrees with their own `Verdict:` line. Read-only; report a list; repair
nothing.

**Result: exactly two — Item 13 (JDE) and Item 26 (JSC).** Both share one cause.
The JMP entry, specifically predicted to be a third, is **not** one — and it is
Item **35**, not Item 34.

---

## 1. What was swept

`submission_log.txt`, sha256 `70f814b9…29897433`, 450 188 B — byte-identical to
the copy CT-S59 read. Section A delimited from its `Recorded Submissions` header
to the first major block separator; §B (`Recorded Submissions (https://zenodo.org/)`)
confirmed to lie outside. **42 items**, numbered 1–42.

Span bounding follows the lesson the log already records against itself (the
2026-08-29 note under *Pre-submission Inquiries*): each record is bounded at the
next record's start **and** at the block separator, so the final record cannot
absorb the trailing block and inherit the wrong verdict. Controls confirm both.

`sweep_status_verdict.py` exit **1**, **9/9 controls fired**.
`check_active_counts.py` exit **1**, **3/3 controls fired**.

---

## 2. Why the answer is 2 and not 18

Most §A entries read `Status: Submitted to <venue>` with a terminal Verdict. That
is **not** a contradiction — there, `Status` names the *venue*, not the liveness.
A sweep that flagged them would have returned 18 hits, buried the 2 real ones,
and been worse than useless.

So `Status` is classified three ways, and the whole grid is reported rather than
just the flagged cell:

| cell | n | reading |
|---|---|---|
| **LIVE × TERMINAL** | **2** | **contradiction — the Item 13 class** |
| VENUE × TERMINAL | 16 | Status names the venue only; conventional |
| TERMINAL × TERMINAL | 23 | Status already updated; clean |
| LIVE × OPEN | 1 | genuinely live (Item 42, the LMP submission) |

Item 42 classifying LIVE × OPEN is the sanity check: the one entry that *should*
read as live does.

---

## 3. The two contradictions

### Item 13 — `JDEQ26-983`, Journal of Differential Equations
```
Status : Submitted to Journal of Differential Equations (active review)
Verdict: REJECTED 2026-05-27 by Qiudong Wang, Handling Editor ...
         (initial screening before refereeing; no referee reports)
```
Established in CT-S59; used here as a **positive control with known ground
truth**, so that a sweep which missed it would be detected as dead rather than
reported as clean.

### Item 26 — `JSCO-D-26-00112`, Journal of Symbolic Computation
```
Status : With Editor at Journal of Symbolic Computation (Elsevier; double-blind;
         active review) — Editor-in-Chief Dr. Josef Schicho assigned as handling
         editor 2026-05-19
Verdict: REJECTED 2026-06-15 by Josef Schicho, Editor-in-Chief, after peer review.
```
**New.** And materially different from Item 13: this one **was refereed**. Its
rejection carries scientific signal, where Item 13's — screening, no referees —
carries none. If that paper is being re-routed on the assumption that it is still
out for review, the assumption is four months stale and the referee outcome is
the more useful fact.

### One cause, not two accidents

Both Verdict lines carry `[CORRECTION RECORDED 2026-08-29 …]`. Both were part of
the same landed-but-not-recorded batch, and in both the correction was **appended
to `Verdict` while `Status` was left untouched**. That is a single process gap
with two victims, and it predicts that any future correction made the same way
will produce a third.

---

## 4. Two things that are NOT findings

Reported explicitly, because each would have been an invented defect.

**The JMP entry is clean — and is Item 35.** Item 34 is the Desert Conjecture
paper (TERMINAL × TERMINAL); the JMP paper is Item **35**, `JMP26-AR-01521`
(VENUE × TERMINAL). Neither is in the contradiction class.

> **Correction to my own earlier report.** CT-S59's `REPORT.md` §6 item 1 says
> "Item 34 (JMP)". That is wrong, and wrong in this session's own subject
> matter: I read a grep hit by *line proximity* instead of resolving the entry's
> span — a record identified by location rather than by content. CT-S59 is left
> unedited per append-only discipline; claim **S60-11** supersedes it.

**The stale-looking active-submission counts are honest.** Three
`Active journal submissions` counts exist (lines 1507, 2005, 2553). The two that
enumerate items list 5-of-5 and 3-of-3 entries now carrying terminal verdicts —
which looks damning until the dates are checked. Each is a **dated snapshot**
(2026-05-25 and 2026-05-26) and was true when written. `check_active_counts.py`
§[2] exists solely to make that check before the finding is reported; without it
these were two more invented defects.

The genuine hazard is weaker and different: **no snapshot newer than 2026-05-26
exists**, so a reader looking for the current active set finds a four-month-old
one whose three entries have all since been rejected. That is a missing record,
not a false one.

---

## 5. What was NOT established

- **Whether the Status lines *should* be repaired, and how.** The record is
  yours; append-only discipline may well mean the right fix is a dated
  superseding line rather than an edit. Not decided here.
- **Section B was not swept.** Only §A was in scope. §B entries have a different
  shape (`Status:` describes the Zenodo deposit, not a journal).
- **Pre-submission Inquiries was not swept**, though the log's own 2026-08-29
  note shows that block has had the same class of defect.
- **`scan_decided_not_fired.py` was not located** anywhere in the repo or the
  VSCode tree, though the log references it as existing and as having been fixed
  on 2026-08-29. Its relationship to this sweep is therefore unknown, and this
  sweep may duplicate or contradict it. **Worth resolving before either is
  trusted as the authority.**
- No claim here is about whether any verdict is *correct* — only about whether
  the record contradicts itself.

---

## 6. Open questions for the operator

1. **How should Item 13 and Item 26's `Status` lines read?** A dated superseding
   line preserves the append-only convention; an in-place edit is cleaner to
   read. Your call.
2. **Item 26 is the one with content.** It was rejected *after peer review* by
   the Editor-in-Chief. Were the referee comments retained? They are the only
   refereed signal in this batch.
3. **A current active-submissions snapshot.** One line, and it removes the
   navigational hazard in §4 permanently.
4. **Where is `scan_decided_not_fired.py`?** If it exists outside these trees it
   should be the authority here, not this script.

---

## 7. Claims

11 claims, `S60-01` … `S60-11`, all **INSPECTED**, in `claims.jsonl`
(sha256 `e95fb2dab12fdb58a3ebec3203231b6b584b37a157e41cc034106abbbb30a24a`).

The emitter **refused its own first run**: claim S60-04 asserted Item 34 was
classified `VENUE` when the output says `TERMINAL`, and the pre-write support
check caught it before anything reached disk. That refusal is why §4 above is
correct.

---

## 8. Uncommitted files

```
sessions/2026-09-17/CT-S60-LOG-STATUS-SWEEP/
  REPORT.md
  claims.jsonl                       11 claims, sha256 e95fb2da…30a24a
  scripts/sweep_status_verdict.py    run 1st
  scripts/check_active_counts.py     run 2nd
  scripts/emit_claims_s60.py         run 3rd; re-run refuses
  outputs/sweep_status_verdict.out.txt
  outputs/check_active_counts.out.txt
```

**`submission_log.txt` was not written to.** Its sha256 is unchanged from the
value CT-S59 read: `70f814b926a5fd67a761bbebe19b5474db69b440e7e3f2340624c79029897433`.
Nothing committed, sent, or deposited.
