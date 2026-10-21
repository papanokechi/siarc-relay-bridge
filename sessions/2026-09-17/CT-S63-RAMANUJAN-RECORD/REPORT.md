# CT-S63-RAMANUJAN-RECORD — report

Session: `sessions/2026-09-17/CT-S63-RAMANUJAN-RECORD/`
Status: **HALTED on missing inputs.** Parts A, B.1, B.3, B.4 and C were not
executed. Part B.2 was executed and produced a result that changes the brief.

Nothing was sent, deposited, committed or uploaded. `submission_log.txt` is
byte-unchanged throughout, sha256
`70f814b926a5fd67a761bbebe19b5474db69b440e7e3f2340624c79029897433`.

---

## 1. What was asked, and what could be done

The brief was records-only, in three parts, with a hard precondition: *"If any
file is missing or a date is a placeholder, STOP and say which."*

| Part | Requires | Done |
|---|---|---|
| A.1 — hash and record four emails | the four email files | **No — none exists** |
| A.2 — record the portal state | a real observation date | **No — `<date>` placeholder** |
| A.3 — record that v1.0 is under review | nothing external | Held with A |
| B.1 — rewrite item 36 Status | three `<date>`s; ID ruling | **No — blocked** |
| B.2 — evidence for the 1 June date | nothing external | **Yes — §3 below** |
| B.3 — item 37 (SIGMA) terminal | closing date and outcome | Unblocked, held |
| B.4 — apply `STATUS-EDITS.md` | nothing external | Unblocked, held |
| C — sweep, snapshot, diff | B landing | **No — nothing to check** |

The full halt report, with the proposed filenames for the four emails, is
`MISSING-INPUTS.md`.

### 1.1 The three blockers

1. **All four Ramanujan email files are missing.** The tree holds three email
   artefacts — two LMP letters in `CT-S57-EMAILS-RECORD/email/` and the SIGMA
   decision in `CT-S62-SIGMA-CLOSEOUT/email/` — and none is Ramanujan. The
   `CT-S53.../email/` directory is empty. No file in the tree has a date in
   its name.
2. **Three literal `<date>` placeholders** remain in the Status text the brief
   asks to be written: "not completed as of `<date>`", "follow-ups sent
   `<date>`", and the observation date for the portal claim.
3. **The supplied portal ID contradicts the log.** The brief gives
   `0f62ace0-70fb-4d25-8fdc-6418ef25ed4e`. The log records that string as the
   value the *withdrawal email* carried, and
   `0f62ace0-70fb-4d25-8fdc-6418af25ad4e` as the portal-of-record value — and
   its entire 2026-08-29 "MECHANISM, IDENTIFIED" finding rests on that
   assignment. Writing the brief's value into item 36 would either correct a
   long-standing error or destroy the finding. **This needs the operator's
   ruling**, read character by character off the portal. See §4.

---

## 2. Claims

Eight claims, `S63-01` .. `S63-08`, all **INSPECTED**, in `claims.jsonl`
(sha256 `958018b0afe4090e8b5bc9eac900bb067bd1c2f75dffb773ff3c24bed2d1ab04`).
Each cites a script in this session and a hashed output file, and the emitter
validates its buffer before writing, re-hashing each cited output from disk
and refusing if any digest disagrees. Re-running it refuses (exit 2) to a
separate `.refused.txt`, leaving the success log intact.

| id | substance |
|---|---|
| S63-01 | The log's 1 June line asserts the date and cites no artefact |
| S63-02 | No Ramanujan email artefact in 12,317 files; transcripts excluded by rule |
| S63-03 | The search refuses on timeout rather than reporting an absence |
| S63-04 | The 2026-06-12 backup's date is corroborated by its own contents |
| S63-05 | That backup already carries the 2026-06-01 withdrawal event |
| S63-06 | …and already carries both ID forms and the mismatch flag |
| S63-07 | Therefore B.2's conditional has a failed antecedent |
| S63-08 | The first provenance test was ill-posed; recorded, not dropped |

---

## 3. The finding: part B.2's premise fails

The brief instructed: search for evidence of a 1 June request; **if not found,
correct the date to 2026-08-29 and record that 2026-06-01 was unsupported.**

Evidence was found. The conditional does not apply.

**What was found.** A backup of `submission_log.txt` at
`.copilot/session-state/79d95e76-…/files/log_backup_submission_log_20260612_191220.txt`
(352,019 B, sha256 `271350c6…`). Its stated date is corroborated three ways —
filename, filesystem mtime, and, decisively, its contents: it contains neither
`MATH-D-26-00523` (the LMP submission of 2026-07-28) nor anything dated
2026-08-29, both of which are in the live log.

That file already carries, at L772–775:

- the withdrawal event at **2026-06-01 ~16:14 JST**, its first 200 characters
  identical to the live log's;
- the portal-of-record ID `…af25ad4e`;
- the email's ID `…ef25ed4e`;
- the **`SUBMISSION-ID MISMATCH`** flag.

So the date was written down eleven days after the event and eleven weeks
before the discovery that the withdrawal had not landed. And the record is not
merely dated — it names *which identifier the withdrawal email carried* and
that it differed from the portal's. **A record of an email's identifier has no
function unless the email existed.**

**Scope, stated exactly.** This establishes that the action was recorded
contemporaneously and specifically. It is **not the email**. No sent item is on
disk; only the mailbox is dispositive. What it rules out is that 2026-06-01 was
back-filled, reconstructed or invented.

**Consequence.** Item 36 should carry **two** requests — 2026-06-01, which did
not land, and 2026-08-29, which restated it with the portal ID — which is what
the live log already says. Rewriting Status to "Withdrawal requested
2026-08-29" alone would delete a contemporaneously recorded action, and would
also delete the three-month gap, which is the substance of the complaint
against the journal.

### 3.1 The separate finding this leaves standing

S63-01 and S63-02 are unaffected and worth keeping: the log's 1 June line
**cites no artefact**, and no Ramanujan email exists anywhere on disk — unlike
the 2026-08-29 entry, which describes a reply sent to Springer JEO. What was
wrong was the inference from that absence to the date, not the absence.

---

## 4. Not established

- **That any Ramanujan email was sent.** Only the mailbox can show that. The
  absence search covered 12,317 files and refuses rather than under-reporting,
  but a sent item lives in a mail client, not the repo.
- **Which submission ID the portal shows.** Unresolved, and it blocks B.1.
- **Anything about the four emails in the brief**, their dates, subjects or
  recipients. None is on disk; none may be reconstructed.
- **Whether item 37 (SIGMA) may be marked terminal** — the SIGMA letter
  recorded in CT-S62 names no title, no ID and no date, so the closing date
  must come from the operator. (The rejection itself is evidenced; only its
  date is not.)

### 4.1 A method failure in this session, reported rather than buried

The first provenance test was **"a file written on D contains no date later
than D."** Run against a log that plans, it reported four violations —
2026-07-01, 2026-08-31, 2026-10-29, 2026-11-12 — and would have voided the
whole inference. Reading them showed all four are forward-looking: a parking
window, an ETNA deadline, a JTNB cooldown. The test conflated *mentions a later
date* with *was written later*, so against this input it could only ever fire.
It was replaced by an event-based test, not tuned, and the misfire is printed
in the script's own output.

A second, smaller one: I first listed the portal ID `…af25ad4e` as a
post-June marker. The log records it as captured at submit time on 2026-05-30,
so its presence in a June file proves nothing. Discarded on the record.

**No `PREREG.md` was written for this session.** The brief was records-only and
I did not expect to test a hypothesis; then B.2 turned into one, and its first
form was ill-posed in exactly the way pre-registration exists to catch. I am
not back-dating a PREREG. The honest statement is that the falsifier for the
replacement test was fixed before it was run, and that the first test's failure
was caught by reading its output rather than by design.

---

## 5. Open questions for the operator

1. **Which ID does the Ramanujan portal actually show?** Character by
   character. This blocks B.1 and decides whether the log's MECHANISM finding
   survives.
2. **The four emails** — export them from the portal's correspondence view or
   the mail client, with dates, and Part A can run as written.
3. **Does B.2's instruction still stand** now that its antecedent has failed?
   The recommendation is to keep 2026-06-01, cite the 2026-06-12 backup as its
   support, and record both requests.
4. **SIGMA's closing date** (the letter carries none) — then item 37 can be
   marked terminal from `LOG-EDITS-ITEM37.md`.
5. **Shall the two held edit sets be applied?** `LOG-EDITS-ITEM37.md`
   (CT-S62) and `STATUS-EDITS.md` (CT-S61, items 13 and 26). Part C's checks
   are meaningless until they land.

---

## 6. Uncommitted files in this session

```
MISSING-INPUTS.md
REPORT.md
claims.jsonl                              958018b0afe4090e8b5bc9eac900bb067bd1c2f75dffb773ff3c24bed2d1ab04
scripts/check_june01_withdrawal.py        bounded, refusing absence search
scripts/check_backup_provenance.py        9/9 controls
scripts/emit_claims_s63.py                exit 0; re-run exit 2
outputs/check_june01_withdrawal.out.txt   5/5 controls, 12,317 files
outputs/check_backup_provenance.out.txt   9/9 controls
outputs/emit_claims_s63.out.txt
outputs/emit_claims_s63.refused.txt
```

No file outside this session directory was created or modified.
