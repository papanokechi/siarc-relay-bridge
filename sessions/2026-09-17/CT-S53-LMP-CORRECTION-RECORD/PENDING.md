# CT-S53 — PENDING: required data not supplied

**Status: the record has NOT been written.** The recorder refused, which is the
correct outcome, not a failure.

## What is missing

The instruction that opened this session says "I will paste it" and gives the
date as `<date sent>`. Neither arrived. Two things are required and this agent
cannot obtain either — it has no mail access and will not reconstruct an email
it did not see.

| Needed | Where it goes | Format |
|---|---|---|
| **The email text exactly as sent** | `email/email_as_sent.txt` | plain text, verbatim, no reflowing |
| **The date it was sent** | `email/META.json` | `{"date_sent": "YYYY-MM-DD", "via": "Editorial Manager Send E-mail"}` |

Then run:

```
python scripts\record_correction.py
```

It writes `claims.jsonl` (5 claims, all labelled `INSPECTED`) and
`outputs/record.out.txt`, and hashes the email text. Current state:

```
REFUSED: email\email_as_sent.txt does not exist. The operator must paste the
email text exactly as sent; this agent has no mail access and will not
reconstruct it.
```

## A third thing that needs your eye

**Item 4's "two alternatives" are not in anything this session produced.**
CT-S52's `CORRECTIONS-FOR-REFEREES.md` states item 4 in a single resolved
form — ξ = 0 is not apparent, it carries a logarithm — because Part A settled
it. There are no bracketed alternatives in that file. So either the email was
adapted before sending, or it came from a different draft. The recorder reads
the question off the pasted text rather than guessing: it reports `RESOLVED`,
`UNRESOLVED` (with the bracketed spans printed), or `NOT LOCATABLE`. It will
not pick one for you.

## What was verified while waiting

These did not need the email and are checked against primary sources.

### 1. The Zenodo concept id is right, and the "not updated" claim is checkable

Read from the Zenodo REST API, not assumed from the record number:

- record **20719043** → `doi 10.5281/zenodo.20719043`, **`conceptdoi
  10.5281/zenodo.20719042`**. The operator's concept id is correct.

Four versions exist under that concept:

| Record | Version | Published |
|---|---|---|
| 20719043 | 1.0 | 2026-06-16 |
| 21410927 | 1.1 | 2026-07-17 |
| 21412469 | 1.2 | 2026-07-17 |
| 22731371 | **1.3** | **2026-09-13** |

Nothing has been published since 2026-09-13, eight days before this recording.
So "not updated pending the editor's reply" is supportable **if the email was
sent on or after 2026-09-13**. If it was sent earlier, the claim is false as
stated and the recorder refuses — this arm was tested with a planted date of
2026-08-01 and fired, naming v1.3 as the conflict.

### 2. The submission record exists and matches

`submission_log.txt` item 42: *An explicit exponential-period representation of
the V_quad connection coefficient*, Letters in Mathematical Physics (Springer
Nature, Editorial Manager), **Submission ID MATH-D-26-00523**, submitted
**17 Jul 2026**, Under Review since 2026-07-28. Courtesy-query horizon
~2026-11-17.

### 3. A finding that bears directly on the correction — please read

**The CT-S52 revision was built against v1.0. LMP is unlikely to be holding
v1.0.**

CT-S52 identified "the submitted PDF" as Zenodo record 20719043 — v1.0,
md5 `99faea5b…`, 24 pages — because that is the **only** V_quad paper PDF in
the repository. I have now confirmed that v1.1, v1.2 and v1.3 are **not in the
tree at all**:

| Version | md5 | In repo? |
|---|---|---|
| v1.0 | `99faea5b0f4095788e4ee932436beeda` | **yes** |
| v1.1 | `7feaf94c05a1815a9e8a0ea04561f834` | no |
| v1.2 | `792107efab6317e8ae21e2ca20f092ff` | no |
| v1.3 | `943545955c2951a9592759862230e46a` | no |

LMP received the manuscript on **17 Jul 2026** — the same day **v1.1 and v1.2
were both published**. That makes v1.2 the most plausible thing the editor is
holding, and v1.0 the least plausible.

This cannot be settled from the repository: item 42 of the submission log
records the submitted file as
`[OPERATOR-SUPPLY — manuscript build as submitted; MD5/SHA-256 not recorded at
submission time]`. The hash was never captured, so there is nothing to compare
against. The log itself flags this record as the *unrecorded-submission* class.

**Why it matters here.** CT-S52's line numbers, section numbers, the claim
"24 → 26 pages", and the statement that all existing citation numbers are
preserved are all relative to v1.0. If the editor is holding v1.2, those
specifics may not line up with the manuscript in front of them — and the
corrections themselves may be partly redundant, since v1.3 (2026-09-13) came
after the CT-R1 audit and may already hedge the D₅⁽¹⁾ identification.

**Nothing has been changed on the basis of this.** It is reported for a
decision. The concrete question: *which version did LMP receive?* If it was not
v1.0, the CT-S52 revision should be rebased before anything further is sent,
and the sent email's item-by-item references should be checked against the
version the editor actually holds.

## Controls

The recorder was exercised in a scratch directory outside this session, with a
positive baseline that had to **write** — a harness in which every arm refuses
is indistinguishable from one in which every arm works.

| Arm | Expected | Result |
|---|---|---|
| **A0** complete fixture | writes 5 claims, exit 0 | **wrote**, exit 0 |
| M1 `date_sent` = `<date sent>` | refuse | exit 2, "placeholder, not a date" |
| M2 `date_sent` in the future | refuse | exit 2 |
| M3 `date_sent` = 2026-08-01 (before v1.3) | refuse | exit 2, names v1.3 as CONFLICT |
| M4 empty email file | refuse | exit 2 |
| M5 bracketed alternatives present | exit 0, state `UNRESOLVED` | reported 2 spans, `UNRESOLVED` |

Each arm refused for its **own** reason, not a shared one. The scratch directory
was removed; this session's `claims.jsonl` was never written by any arm.

## Governance

Nothing sent, deposited, uploaded, submitted or committed. No earlier session's
record was edited — CT-S52 and every prior session are untouched. The Zenodo
record was read through the public API only.
