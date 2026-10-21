# CT-S61 — active-submissions snapshot, the located scanner, and an open
# concurrent-submission window

Session: `sessions/2026-09-17/CT-S61-SNAPSHOT-AND-STATUS/`
Date: 2026-09-21 · read-only · **nothing committed, sent, or deposited**

Master log `submission_log.txt` sha256
`70f814b926a5fd67a761bbebe19b5474db69b440e7e3f2340624c79029897433`
— **unchanged**, verified before and after every script.

---

## 0. Headline

The task was two small items of record hygiene (Rulings 3 and 4). Generating the
snapshot surfaced something that outranks them:

> **The same manuscript is non-terminal at two journals today.** A withdrawal was
> requested from The Ramanujan Journal on 2026-06-01 to clear a
> simultaneous-submission conflict with SIGMA. It was never confirmed. As of the
> last portal check a reviewer had **accepted** and was refereeing. That is
> **+112 days**, and the record's own escalation dates (2026-09-01, 2026-09-12)
> passed unremarked.

No scanner reported it, for two independent reasons given in §3.

---

## 1. Ruling 4 — the scanner exists (supersedes CT-S60 §5)

`CT-S60-LOG-STATUS-SWEEP/REPORT.md` §5 states the tool "was not located". **That
is now false.** Per append-only discipline it is superseded by claim **S61-01**,
not edited.

`scan_decided_not_fired.py` is at `C:\LocalWork\deposit-A076227\out\`, with three
siblings I had not seen: `scan_stale_records.py`, `scan_fired_not_landed.py`,
`scan_submission_substrates.py`. It was found by content search after a
location-based search failed — the third time this run.

**The 2026-08-29 fix is real and verifiable.** The v1 backup is preserved, so
both versions were run against the current log:

| | v1 (superseded) | current |
|---|---|---|
| windows reported | 13, flat | 1 live + 12 moot |
| record attribution | none (one flat string) | per-record spans |
| JDE nudge window | reported live | correctly suppressed as moot |
| `--today` | hardcoded 2026-08-27 | parameter |

That reproduces the documented defect and its repair exactly. **INSPECTED.**

**The substantive point for CT-S60:** the scanner's liveness test is
`dead = TERMINAL(Verdict) or TERMINAL(Status)`. Because it is an **OR**, a record
whose Status and Verdict *disagree* is still marked dead on the strength of
either one. The scanner is therefore structurally blind to the Status/Verdict
contradiction class — so **CT-S60's sweep is complementary, not duplicative.**

`scan_stale_records.py` independently names items **13, 26 and 35** as its
calibration true positives, corroborating CT-S60's Item 34/35 correction from a
source I had not read. It currently **exits 2 with CALIBRATION FAILED**, correctly,
because the patch it anchors on has landed; by its own instruction the anchor now
needs updating. A tool that fails on every run is a tool that stops being run —
worth ten minutes.

## 2. Ruling 3 — the generated snapshot

`scripts/make_active_snapshot.py` → `outputs/active_snapshot.txt`. Derives the
active set from §A (active iff the Verdict line is not terminal), stamps the
generation date **and the sha256 of the log it was derived from**, so a later
reader can tell whether it still describes the current file. That is exactly what
the May snapshots could not do. 5/5 controls fired.

**42 items, 4 active** — independently matching `scan_stale_records.py`'s
"non-terminal records 4", a differently-implemented reader.

| Item | ID | Venue |
|---|---|---|
| 36 | `0f62ace0-…ad4e` | The Ramanujan Journal |
| 37 | PENDING (email) | SIGMA |
| 39 | EasyChair 262 | Reliable Computing |
| 42 | `MATH-D-26-00523` | **Letters in Math. Physics — the live one** |

Items 36 and 37 carry an **identical Title**.

## 3. The finding: Items 36 and 37

`scripts/check_item36_windows.py`, exit 1, **7/7 controls fired**.

This is **not** an undisclosed concurrent submission. The log discloses it fully
and the operator acted: a withdrawal was requested from Ramanujan the day after
the SIGMA submission. The defect is that the clearing action never completed and
nothing said so.

- **A1** Identical title, both non-terminal, two venues.
- **A2** Withdrawal requested 2026-06-01, **+112d**, unconfirmed. Portal check
  2026-08-29: "The editor has invited 1 reviewer(s)"; "There is 1 reviewer(s)
  that has accepted." A referee is working on a manuscript the author asked to
  withdraw, while the same manuscript is live at SIGMA.
- **A3 — why no scanner reported it.** `scan_decided_not_fired.py` suppressed
  Item 36 as *moot (record now terminal)* because its `TERMINAL` regex matched
  the word **`accepted`** — inside the sentence *"There is 1 reviewer(s) that
  has accepted."* The phrase that proves the manuscript is **most alive** is
  read as proof that it is finished. Confirmed against the raw field with the
  matcher's positive and negative controls both firing.
- **A4** The record's own `WATCH-1 2026-09-01` (+20d) and `WATCH-2 2026-09-12`
  (+9d) are overdue and match neither `PAT` nor anything else: `PAT` lists
  `escalation`, the text says `escalate`; WATCH-2 contains no trigger word.

So the failure is doubled: the record was suppressed at record level, and its
windows would have been missed at window level even if it had not been.

**The recurring shape.** Item 36's Verdict says its wording is *"deliberate so
the fired-but-not-landed scanner keeps firing until a dated confirmation
exists."* Wording chosen to keep one scanner firing silenced a different one. A
record cannot be tuned to its readers one at a time.

## 4. Claims

11 claims in `claims.jsonl`, all **INSPECTED** (file inspection and script
execution; no mathematical assertion). Emitter validates in-memory before
writing and refuses on re-run (exit 2).

## 5. What was NOT established

- Whether the Ramanujan withdrawal has since been confirmed. **The portal is the
  only authority and I cannot reach it.** Every date here is from the 2026-08-29
  portal check.
- Whether a decision has arrived by email for any of the 4 active items. No
  scanner can establish this — `scan_stale_records.py` says so of itself.
- Whether `scan_decided_not_fired.py`'s OR also *wrongly* kills records with
  terminal Status and open Verdict. Suspected, unverified, out of scope.
- Item 26's referee comments — not retrieved; operator-owned.

## 6. For the operator

1. **The Ramanujan window is the urgent item, not the Status lines.** Both
   venues prohibit simultaneous submission and the exposure grows daily. The
   record's own WATCH-1 said *"escalate to the editorial channel direct rather
   than the support desk, and do not escalate gently."* That was 20 days ago.
2. `STATUS-EDITS.md` has paste-ready replacements for Items 13 and 26, Verdict
   lines untouched. Acceptance test: `sweep_status_verdict.py` then reports 0
   `LIVE × TERMINAL`. **It will not catch Item 36** — there Status and Verdict
   agree with each other and are both wrong in the same direction.
3. Two one-line scanner repairs: drop `accepted` from `TERMINAL` (or require it
   to be verdict-initial), and add `escalate|WATCH-\d` to `PAT`.
4. Update `scan_stale_records.py`'s calibration anchor so it stops exiting 2.

## 7. Addendum — the SIGMA submission identifier (operator question)

Asked after the above: *"help provide submission ID for SIGMA."*
Full answer in `SIGMA-RECORD.md`; `scripts/check_sigma_id.py`, exit 1, 8/8
controls; claims S61-12..S61-18.

**There is no SIGMA submission ID and none will be assigned.** SIGMA is an arXiv
overlay journal and the arXiv number *is* the identifier; it issues no
proprietary manuscript ID. Item 37 took the non-arXiv email route, so no
identifier was ever created. Item 37's `PENDING … awaiting editorial
acknowledgement` awaits something that cannot arrive.

Three findings outrank the missing ID:

1. **Receipt is unconfirmed after 112 days.** SIGMA's instructions provide a
   remedy — resend to `sigmajournal@gmail.com` if receipt is not acknowledged
   **within two working days**. Due ~2026-06-03, never fired. The economical
   explanation of the silence is that the submission never entered the queue.
2. **The submission may not have met the route's terms**: logged as PDF-only
   where zipped TeX/LaTeX *plus* PDF is asked for, and the cover letter frames
   the route as a contingency (*"I will follow that route if needed"*) rather
   than giving the required reason for not using arXiv.
3. **SIGMA requires "not under consideration … in any other journal."** With the
   Ramanujan withdrawal unconfirmed (§3), that condition is breached now.

Also recorded: SIGMA is an authorised **arXiv proxy submitter**, so the arXiv
endorsement barrier shaping this portfolio's venue strategy may not be permanent.

Journal-policy quotations were read from <https://sigma-journal.com/about.html>
on 2026-09-21 and are marked `evidence_type: web_inspection`,
`reproducible: false`, with the URL and retrieval date — they are not
establishable by any script in this folder.

## 9. Addendum — which title (operator question)

With no submission ID issued (§7), the title is the only handle on item 37.
`scripts/check_title.py` — exit 1, **9/9 controls fired**, 1 finding.

**The title agrees everywhere it is written.** Resolved by content, not by
path: the PDF at md5 `4d1e4d59072cad0db8edc86280af45a1`, 612,719 B, is the
one the log records for item 37 — three files of that name exist in the tree
with three different digests. Its printed page-1 title, the title quoted once
in the cover letter's body, and the log's `Title:` field are identical
(S61-19, S61-20):

> A non-classical Painlevé V transcendent from a quadratic polynomial
> continued fraction: surface classification and resurgent Stokes data

**But that is not the string to search by.** The cover letter's *Subject*
line is truncated (S61-21):

```
Subject: Submission: A non-classical Painlevé V transcendent from a
         quadratic polynomial continued fraction
```

The subtitle `: surface classification and resurgent Stokes data` is absent.
The subject line is what an editorial office files a direct-email submission
under, so a search of sent mail — or a request to the office — phrased on the
full title would return nothing, and would look exactly like a submission
that never arrived. Given that receipt is already UNCONFIRMED at 112 days
(S61-15), that false negative is the expensive one.

**Answer (S61-22).** Two different strings for two different jobs:

| purpose | string |
|---|---|
| correspondence, and the log's `Title:` field | the full title above |
| searching sent mail / asking the office | the stem `A non-classical Painlevé V transcendent from a quadratic polynomial continued fraction`, plus 1 June 2026 and ORCID 0009-0000-6192-8273 |

Ligature note (S61-23): `pdftotext` on this build rendered this PDF's
ligatures correctly — a probe of the full extracted text found no dropped
ligatures other than the unrelated `2nd ed` — but the checks ran through a
ligature-tolerant matcher anyway, with its recovery and separation controls
both firing, so "not found" here cannot mean "my reader could not see it".

---

## 8. Uncommitted files

```
sessions/2026-09-17/CT-S61-SNAPSHOT-AND-STATUS/
  REPORT.md
  STATUS-EDITS.md
  SIGMA-RECORD.md
  claims.jsonl                          23 claims
  scripts/make_active_snapshot.py
  scripts/check_item36_windows.py
  scripts/check_sigma_id.py
  scripts/check_title.py
  scripts/emit_claims_s61.py
  scripts/emit_claims_s61b.py
  scripts/emit_claims_s61c.py
  outputs/active_snapshot.txt
  outputs/make_active_snapshot.out.txt
  outputs/check_item36_windows.out.txt
  outputs/check_sigma_id.out.txt
  outputs/check_title.out.txt
  outputs/emit_claims_s61.out.txt
  outputs/emit_claims_s61b.out.txt
  outputs/emit_claims_s61c.out.txt
  outputs/emit_claims_s61.refused.txt   (idempotency evidence)
  outputs/emit_claims_s61b.refused.txt  (idempotency evidence)
  outputs/emit_claims_s61c.refused.txt  (idempotency evidence)
```

Nothing outside this folder was written. `submission_log.txt` and the four
scanners in `deposit-A076227\out\` are byte-unchanged.
