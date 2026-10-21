# Paste-ready `Status:` replacements — §A Items 13 and 26

Per the operator's Ruling 1 (2026-09-21): *"Edit the Status lines in place … Rewrite
both to the terminal outcome and date, and keep the old text beneath as a dated
'was:' line so the history isn't lost."*

**These are proposals. This session did not modify `submission_log.txt`.**
Its sha256 is unchanged at
`70f814b926a5fd67a761bbebe19b5474db69b440e7e3f2340624c79029897433`.

Both Verdict lines are left **untouched** — they are evidence. Only the Status
line, whose single job is to be current, is rewritten.

---

## Item 13 — `JDEQ26-983`, Journal of Differential Equations

Replace **line 105**, currently:

```
   Status: Submitted to Journal of Differential Equations (active review)
```

with:

```
   Status: REJECTED 2026-05-27 — Journal of Differential Equations (initial screening, no referees). Paper is free; in the redirect queue. See Verdict for the decision email and grounds.
   Status was: "Submitted to Journal of Differential Equations (active review)" — stale from 2026-05-27 until corrected 2026-09-21; the 2026-08-29 correction updated Verdict only.
```

## Item 26 — `JSCO-D-26-00112`, Journal of Symbolic Computation

Replace **line 232**, currently:

```
   Status: With Editor at Journal of Symbolic Computation (Elsevier; double-blind; active review) — Editor-in-Chief Dr. Josef Schicho assigned as handling editor 2026-05-19
```

with:

```
   Status: REJECTED 2026-06-15 after peer review — Journal of Symbolic Computation (Editor-in-Chief Josef Schicho). HOLD: referee and editor comments are in the decision email and are NOT yet transcribed into this record; do not re-fire this paper until they are read. This is the programme's only refereed feedback.
   Status was: "With Editor at Journal of Symbolic Computation (Elsevier; double-blind; active review) — Editor-in-Chief Dr. Josef Schicho assigned as handling editor 2026-05-19" — stale from 2026-06-15 until corrected 2026-09-21; the 2026-08-29 correction updated Verdict only.
```

---

## The practice fix

The operator's own diagnosis: *"when a verdict is recorded, the Status line
changes in the same edit."* The 2026-08-29 batch appended to `Verdict` and left
`Status` alone; that is why both went stale, and it would have produced a third
the same way.

The standing check is
`CT-S60-LOG-STATUS-SWEEP/scripts/sweep_status_verdict.py` — run it whenever a
verdict is recorded. After the two edits above it should report **0**
`LIVE × TERMINAL` cells; that is the acceptance test for this edit.

Note it will *not* catch Item 36, whose Status and Verdict agree with each other
and are both wrong in the same direction. See `REPORT.md` §3.
