# MISSING-INPUTS — CT-S63-RAMANUJAN-RECORD

**HALTED before any edit to `submission_log.txt`.** The brief says: *"If any
file is missing or a date is a placeholder, STOP and say which."* Both
conditions are met. Nothing was sent, deposited, committed, or written to the
log. The log is byte-unchanged at sha256
`70f814b926a5fd67a761bbebe19b5474db69b440e7e3f2340624c79029897433`.

---

## 1. The four email files are not in the tree

The brief says *"the four email files above, verbatim, with their dates in
the filenames"* and *"do not reconstruct any of them"*. A full search of the
session tree finds **three** email files, none of them Ramanujan, and none
with a date in the filename:

| file | bytes | what it is |
|---|---|---|
| `CT-S57-EMAILS-RECORD/email/email_as_sent.txt` | 2862 | LMP corrections, items 1–4 |
| `CT-S57-EMAILS-RECORD/email/followup_as_sent.txt` | 2041 | LMP follow-up, items 4–5 |
| `CT-S62-SIGMA-CLOSEOUT/email/sigma_decision_as_received.txt` | 3343 | SIGMA rejection, recorded today |

`CT-S53-LMP-CORRECTION-RECORD/email/` exists but is **empty**.

So **all four Ramanujan emails are missing**. From the brief's own Part B.1,
they should be:

1. the **withdrawal request to JEO**, 2026-08-29;
2. the **JEO acknowledgement**, 2026-08-29;
3. the **follow-up to JEO**, date not given;
4. the **follow-up to the Editorial Office**
   (`ahamedreefan.tajudeen@springernature.com`), date not given.

Suggested drop location and naming, so the dates are in the filenames as the
brief requires:

```
sessions/2026-09-17/CT-S63-RAMANUJAN-RECORD/email/
  20260829_out_jeo_withdrawal_request.txt
  20260829_in_jeo_acknowledgement.txt
  <YYYYMMDD>_out_jeo_followup.txt
  <YYYYMMDD>_out_editorial_office_followup.txt
```

Paste each **verbatim**, and include the headers if the mail client will give
them — `Date:`, `From:`, `To:`, `Subject:`, `Message-ID:`. Part A.1 asks for
sender, recipient and subject per email; without headers those are
unquotable, and CT-S62 has just recorded one letter where exactly that gap
forced attribution by elimination instead of by quotation.

## 2. Three dates are literal placeholders

These appear in the brief as `<date>` and cannot be guessed:

| where | text |
|---|---|
| Part A.2 | "labelled as observed on **`<date>`** by the operator" |
| Part B.1 | "not completed as of **`<date>`**" |
| Part B.1 | "follow-ups sent **`<date>`** to JEO and to the Editorial Office" |

The portal state in Part A.2 is presumably observed **today, 2026-09-21** —
but the brief forbids reconstructing supplied inputs, and an observation date
written into the record from an assumption is the precise failure this
programme has been correcting all day. Please state it.

## 3. A contradiction in the supplied input — needs your ruling

This one matters more than the missing files, and must be settled before any
edit.

The brief supplies, as observed portal state:

> submission ID `0f62ace0-70fb-4d25-8fdc-6418ef25ed4e`

The log's Item 36 records the opposite assignment, twice, and builds a
finding on it:

- `Submission ID: 0f62ace0-70fb-4d25-8fdc-6418af25ad4e` — described as *"the
  portal-of-record value captured at submit time and is the authoritative
  one"*;
- the withdrawal email's `…6418ef25ed4e` — described as *"likely a
  transcription slip"*;
- and the 2026-08-29 verdict entry states as **MECHANISM, IDENTIFIED**: *"the
  2026-06-01 email quoted submission ID …6418ef25ed4e, which does not exist;
  the authoritative portal ID is …6418af25ad4e"* — i.e. the explanation of
  why the withdrawal never landed is that the email used `ef25ed4e`.

If the portal today shows **`ef25ed4e`**, then that whole mechanism is
inverted: the email quoted the ID the portal actually holds, the log's
recorded ID is the slip, and the reason the withdrawal did not complete is
**unknown**, not identified. That is a retraction, not a tidy-up.

Two possibilities, and I will not choose between them:

- **(a)** the portal shows `ef25ed4e` and the log's Submission ID line and its
  MECHANISM finding are both wrong;
- **(b)** the brief's line repeats the email's ID rather than the portal's,
  and the log stands.

Please re-read the portal ID character by character —
`…6418`**`af`**`25`**`ad`**`4e` versus `…6418`**`ef`**`25`**`ed`**`4e` — and
say which. Everything in Part B.1 about why the withdrawal stalled depends on
the answer.

## 4. Part B.3 is not blocked — the SIGMA evidence exists

The brief says *"Ask for the closing date and outcome if the log does not
already hold them; do not invent either."* The log does not hold them, but
they were obtained today from the decision letter itself and are already
recorded:

- **Outcome:** rejected at editorial screening, without refereeing.
- **Date:** 2026-09-21.
- **Evidence:** `CT-S62-SIGMA-CLOSEOUT/email/sigma_decision_as_received.txt`,
  sha256 `2887fa4b0c7e6f30dda3a85986eb5480db6501a6d3719a7b0dd9ac10ba6b30eb`,
  verbatim; claims S62-01..09.
- **Paste-ready edit:** `CT-S62-SIGMA-CLOSEOUT/LOG-EDITS-ITEM37.md`, generated
  and proven to move the active count 4 → 3 with a firing vacuity arm.

So Item 37 can be marked terminal on evidence whenever you choose to apply
it. It is held only by the general halt, not by a missing input.

## 5. Part B.4 is also unblocked, but held

`STATUS-EDITS.md` for Items 13 and 26 is prepared and needs no missing input.
It is **not applied**, because the halt is on the brief as a whole and
editing your canonical record while halted on the same file's other edits is
how a half-applied record happens. Say the word and it goes in, either alone
or together with Item 37.

## 6. What was done anyway

Part B.2 — *"search the log's own sources for any evidence of a 1 June
request"* — needs none of the missing inputs and is decidable now. It was
run read-only: `scripts/check_june01_withdrawal.py`, then
`scripts/check_backup_provenance.py`.

**Its premise failed.** The instruction was conditional — *if not found,
correct the date to 2026-08-29* — and evidence **was** found: a backup of
`submission_log.txt` dated 2026-06-12, whose date its own contents
corroborate, already carries the 2026-06-01 withdrawal event, both submission
ID forms, and the `SUBMISSION-ID MISMATCH` flag. So the date is
contemporaneously and specifically recorded, and must be cited rather than
overwritten. Full statement, with its scope limit, in `REPORT.md` §3.

This also bears on §3 above: the ID assignment the brief contradicts was on
the record by 2026-06-12, eleven weeks before the investigation that is said
to rest on it. That does not settle what the portal shows — only you can read
that — but it removes the possibility that the assignment was invented to fit
the finding.
