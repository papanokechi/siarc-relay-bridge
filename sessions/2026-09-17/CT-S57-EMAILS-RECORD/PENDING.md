# CT-S57 — record of the author's corrections sent to the LMP editor

**Both emails were sent on 2026-09-21** (operator: *"both went out today"*), via
Editorial Manager's "Send E-mail" function, for submission **MATH-D-26-00523**,
*Letters in Mathematical Physics*.

**The first email is recorded.** `claims.jsonl` holds 5 claims, all labelled
`INSPECTED`. **The follow-up is now recorded too** — 7 further claims, also all
`INSPECTED`. See §4, and §5 for a finding about how its text arrived.

Nothing here was sent, deposited, uploaded, submitted or committed. CT-S53 and
every earlier session are **untouched**: its recorder was *copied* into this
session, not run in place.

---

## 1. The first email

| | |
|---|---|
| file | `email/email_as_sent.txt` |
| bytes | 2862 |
| sha256 | `9bdcd347505999fdfb269ca0b632b23d83c25245e55fac066f565cd29a0572a0` |
| date sent | 2026-09-21 |
| items | 4 |

The date is the **operator's statement**, not derived from any header this agent
has seen; it has no mail access and did not reconstruct any part of the text.

### Item 4 went out UNRESOLVED

The recorder reads this off the text rather than guessing. It found item 4
locatable and **two** bracketed alternative spans still present:

```
[If the log check finds no logarithms:]
[If logarithms are found:]
```

→ **UNRESOLVED — both alternatives were sent.**

### Zenodo confirms the "not updated" claim

Read from the API, concept `20719042`:

| Record | Version | Published |
|---|---|---|
| 20719043 | 1.0 | 2026-06-16 |
| 21410927 | 1.1 | 2026-07-17 |
| 21412469 | **1.2** — the version LMP holds | 2026-07-17 |
| 22731371 | 1.3 | 2026-09-13 |

Versions published after 2026-09-21: **0**. Latest is v1.3, unchanged since
2026-09-13. The claim that the record has deliberately not been updated pending
the editor's reply is therefore supportable as stated.

*(Zenodo returned HTTP 504 for roughly ten minutes earlier in this session, and
the recorder refused to write the F3 claim for exactly that period. An unchecked
"not updated" claim written as INSPECTED would later be indistinguishable from a
verified one.)*

---

## 2. Every object the email cites exists in the manuscript the editor holds

`scripts/email1_objects.py`, checked against the **rendered** v1.2 PDF
(md5 `792107efab6317e8ae21e2ca20f092ff`) — not the LaTeX source, because a
`\label` is not what an editor reads.

- **8/8** numbered objects: Theorems 1.1 and 1.2, Corollaries 1.3 and 1.4,
  Proposition 2.4, Lemma 2.7, Table 1, **Remark 3.4**.
- **3/3** sections: 1.1, 1.2, 7.1.
- **Discrimination:** "Remark 3.3" — v1.0's numbering, which CT-S52's edit tags
  carried — is **absent** from v1.2. Without this the check would pass against
  v1.0 too and could not tell the versions apart.
- Both reader controls fire.

So although the revision was originally built against the wrong base, the
**email's numbering is correct** against the copy the editor is reading.

---

## 3. A finding the operator should see

**One of the two alternatives the editor received is now known to be false.**

The first alternative reads:

> *"I have since verified directly that the Frobenius solutions at xi = 0 carry
> no logarithmic terms, so the conclusion stands; the argument needs this
> added."*

CT-S52's Part A found the opposite: ξ = 0 **does** carry a logarithm, and the
second alternative is the correct one. The editor is holding a message in which
a statement and its negation both appear, one of them false, with nothing
indicating which case holds.

The follow-up, sent the same day, states plainly which case holds. **No further
email is needed on this point.** It is recorded so the sequence stays legible,
and so that nobody reading the first email alone takes the first alternative at
face value.

---

## 4. The follow-up email — recorded

| | |
|---|---|
| file | `email/followup_as_sent.txt` |
| bytes | 2041 |
| sha256 | `75d41c372645b15731c785af3539b751a31481d884898048a13149d701ee1601` |
| date sent | 2026-09-21 |
| items | 4 and 5 |

Recorded by `scripts/record_followup.py` as **S57-F01 … S57-F07**, all
`INSPECTED`. The recorder reads each fact off the text rather than being told
it, and refuses rather than guessing.

### Item 4 went out RESOLVED

Read off the text as sent, not asserted:

- bracketed conditional alternatives remaining: **0**
- asserts ξ = 0 *"is not an apparent singularity"*: **yes**
- asserts *"one local solution carries a logarithm"*: **yes**

→ **RESOLVED — logarithm found.** This settles, on the editor's side, the
ambiguity §3 records in the first email, and settles it to the alternative
CT-S52's computation supports. The recorder is written to refuse if it finds
item 4 still unresolved here, since the follow-up exists to resolve it.

Numbered items found in the text: **[4, 5]** — it continues the first email's
numbering rather than restarting, as intended.

### Item 5

New in the follow-up. All three figures present in the text as sent: **8.84 ×
10⁻⁴⁶** (the collapsed comparison), **9.31 × 10⁻⁴⁶** (Method C's separate
comparison, unaffected), **3.7 × 10⁻⁴⁶** (the stream-extracted-amplitude
reconstruction of *S*, Method B's genuine independent check).

### Its objects also check out against v1.2

`scripts/email2_objects.py`, against the same rendered v1.2 PDF: **7/7**
numbered objects (Proposition 2.4, Lemma 2.7, Table 1, **Table 2**, Figure 1,
Remark 3.4, Corollary 1.3), both sections, and equation **(17)**. `Remark 3.3`
— v1.0's numbering — absent, so the check discriminates v1.2 from v1.0. All
four controls fire.

Two differences from the first email's check, both deliberate:

- **Sections are matched on their rendered title**, `1.3.Main results` and
  `5.Three verifications`, not on the bare numeral. "5" occurs on nearly every
  page of a 25-page paper, so a bare-numeral check passes whatever the PDF
  contains and is no evidence at all.
- **Step [0] checks the citation list against the email itself** before
  anything is looked for in the PDF. The list is hand-read, so it could name an
  object the email never cites — an error that would otherwise pass silently as
  a PASS.

Worth noting for the revision: §5's title in the version the editor holds is
**"Three verifications"**. That is the phrase item 5 corrects.

### Zenodo, re-checked at recording time

Versions published after 2026-09-21: **0**. Latest still v1.3 (record
22731371), 2026-09-13. Recorded as S57-F07.

---

## 5. Finding — the record went stale without anyone noticing

The follow-up's text was pasted **into `email/email_as_sent.txt`**, the file the
five existing claims hash, rather than into a new file. That single write left
the record describing a file that no longer existed:

| | bytes | sha256 |
|---|---|---|
| recorded | 2862 | `9bdcd347505999fd…` |
| on disk after the paste | 4917 | `779591818fceba63…` |

**All five claims were invalidated, and nothing in this session could have
noticed.** The recorder had already exited 0; a recorder cannot detect a write
that happens after it. This is the same class as CT-S56 finding (h): a recorded
hash goes stale on any later write, and only a check that re-reads both sides
*afterwards* can see it.

Two repairs, both in place:

**`scripts/split_emails.py`** separated the two emails at the byte level. It
refused on its first run: the split head came to 2860 bytes / `47291cdb…`
against the recorded 2862 / `9bdcd347…`. Rather than pad to fit, it now tries a
candidate set of line endings and accepts **only** the one the existing claims
already cite — `+ one CRLF`, 2862 bytes, `9bdcd347…`, byte-identical. The paste
had introduced 8 CRLFs where the record carries 1; the 14 surplus separator
bytes belong to neither email and were discarded. Reconstruction from memory
was never an option: *an email recorded from memory is not a record.*

**`scripts/verify_claims_s57.py`** is the check that was missing. It re-reads
`claims.jsonl` from disk, re-hashes every cited email file from disk, takes no
value from any recorder, and runs **last**. Run it again any time the email
files are touched.

Its own first version had the defect in miniature, and it is worth recording.
The five CT-S53 claims carry `email_sha256` but **no filename key**, and the
first version required both — so it printed `no email file cited -- skipped`
for exactly the five rows that had gone stale. *A check that skips the rows it
exists to protect is the defect wearing a different hat.* Repaired: a hash with
no filename is still decidable, because it either matches some email file on
disk or it matches none, and "none" is precisely staleness. It now checks
**12 of 12** claims.

Verified on the real defect, not a synthetic one — the historical combined file
replayed in a scratch tree:

| arm | state | exit |
|---|---|---|
| A0 | the record as it now stands | **0**, all 12 consistent |
| R1 | the 4917-byte combined file, no follow-up file | **1**, 16 problems, all five S53 claims STALE |

R1 initially exited 2 rather than 1 — the "control did not fire for every cited
file" refusal masked the finding, because *no* file had resolved. A verifier
must report what is wrong, not merely that its control was starved; that case
is now distinguished.

### A third instance of the same class, in the recorder's own logging

`record_followup.py` is idempotent by refusal: re-running it finds its seven
claim IDs already present and declines to append. But its refusal path wrote to
the **same** output file as its success path, so the idempotency re-run
destroyed the only log of the write that had produced the claims. *A refusal
must not overwrite the evidence of the run it is declining to repeat.*
Refusals now go to `record_followup.out.refused.txt`; confirmed by re-running
the refusal and checking the success log byte-unchanged.

The lost log was **reproduced, not reconstructed**: `claims.jsonl` was truncated
to its five original claims and the recorder re-run, and the result came back
byte-identical to the file it had produced before —
`12581E426347D199810BFB4CEE37ABBA6B23A12BDB7FE572495C61206E8C6C17` both times.
That is also the session's only direct evidence that the recorder is
deterministic.

---

## 6. Still required

Nothing in this session. Both emails are recorded, hashed, and verified against
the files on disk.

Outside it, unchanged: **the editor's reply**, and after it a v1.4 of concept
`20719042` matching whatever revision is accepted, its description stating
plainly that v1.2 was the version submitted to LMP.

---

## 7. Files

```
email/email_as_sent.txt          the first email, verbatim (2862 B, restored)
email/followup_as_sent.txt       the follow-up, verbatim (2041 B)
email/META.json                  date sent, channel, provenance of the date
claims.jsonl                     12 claims, all INSPECTED (5 + 7)
scripts/record_correction.py     copied from CT-S53, unmodified
scripts/record_followup.py       the follow-up recorder; appends, never rewrites
scripts/split_emails.py          separates the two; refuses unless part 1
                                 reproduces the recorded hash exactly
scripts/email1_objects.py        the first email's objects vs the v1.2 render
scripts/email2_objects.py        the follow-up's objects vs the v1.2 render
scripts/verify_claims_s57.py     post-hoc verifier -- RUN LAST
outputs/record.out.txt
outputs/record_followup.out.txt
outputs/record_followup.out.refused.txt
outputs/email1_objects.out.txt
outputs/email2_objects.out.txt
outputs/verify_claims_s57.out.txt
PENDING.md                       this file
```

Run order: `split_emails.py` → `record_followup.py` → `email2_objects.py` →
`verify_claims_s57.py`.

All uncommitted. Nothing sent, deposited, uploaded or submitted.
