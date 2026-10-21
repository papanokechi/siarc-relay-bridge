# SIGMA submission identifier — §A Item 37

**Question (operator, 2026-09-21): "help provide submission ID for SIGMA".**

**Answer: none exists, and none will be assigned.**

---

## Why

SIGMA is an **arXiv overlay journal**. Its submission instructions
(<https://sigma-journal.com/about.html#submit>, read 2026-09-21) say verbatim:

> "Please submit the paper to arXiv.org and **send the arXiv number** to
> editor@sigma-journal.com **or (in exceptional cases only)** you can send the
> zipped paper in TeX/LaTeX format directly to editor@sigma-journal.com (please
> include the PDF or PostScript file as well) **with an explanation why you
> prefer not to put the paper to arXiv**."

The **arXiv number is the identifier**. SIGMA issues no proprietary manuscript
ID. Item 37 went by the non-arXiv route, so no arXiv number exists, and
therefore no identifier exists.

`scripts/check_sigma_id.py` (exit 1, 8/8 controls) confirms on disk:

| | |
|---|---|
| B1 | No SIGMA-shaped manuscript ID anywhere in the log — **NONE** |
| B2 | Item 37 records `PENDING … awaiting editorial acknowledgement` |
| B3 | **No acknowledgement recorded, +112 days** |
| B4 | Sent as **PDF only**; the route asks for zipped TeX/LaTeX **plus** PDF |
| B5 | Cover letter frames the route as a contingency, not an exercised choice |

The record is therefore waiting for something that cannot arrive.

## The more serious point

SIGMA publishes a remedy for exactly this silence, and it has been available
and unfired for 112 days:

> "If the receipt of your paper is not acknowledged **within two working days**,
> please resend it to our alternative e-mail address **sigmajournal@gmail.com**"

Due ~2026-06-03. The most economical explanation of 112 days of silence on an
email-route submission is that **it never entered the queue** — indistinguishable
from the case where it was filtered. Receipt is **UNCONFIRMED**; the submission
should not be treated as live.

Two further gaps against the stated route, both from B4/B5:

- **PDF only.** `vquad_resurgence.pdf` (612,719 B) with no `.zip`/`.tex`.
- **No stated reason.** The cover letter says *"I understand from your office
  that should I encounter difficulty posting to arXiv, I may send the article
  PDF directly, and **I will follow that route if needed**."* That announces a
  possible future route; it is not the explanation SIGMA asks for. (It also
  implies prior correspondence with the office — if that exists, it is the only
  trace of this submission and should be located.)

## Blocking condition

SIGMA's criteria require papers be *"not published previously and **not under
consideration for publication in any other journal or book**."* The unconfirmed
Ramanujan withdrawal (Item 36, +112 days, a reviewer actively refereeing) means
the manuscript is formally under consideration at both venues **now**. Resolve
Ramanujan before re-firing SIGMA — see `REPORT.md` §3.

## Worth knowing

SIGMA is an **authorised arXiv proxy submitter** and "can also replace (or
submit) an article in the arXiv on behalf of the authors" (about.html#overlay).
Stated for accepted papers, but it means the arXiv endorsement barrier that has
been shaping venue strategy across this portfolio is not necessarily permanent.

---

## Paste-ready replacement — Item 37 `Submission ID:` line

```
   Submission ID: NONE — SIGMA is an arXiv overlay journal and assigns no proprietary
   manuscript ID; the arXiv number is the identifier (sigma-journal.com/about.html#submit,
   read 2026-09-21). This was a non-arXiv direct email submission, so no ID exists and none
   will be assigned. Reference this paper by title + submission date 2026-06-01.
   ⚠ NO ACKNOWLEDGEMENT received in 112 days. SIGMA's instructions require a resend to the
   alternative address sigmajournal@gmail.com if receipt is not acknowledged within TWO
   WORKING DAYS (due ~2026-06-03; never fired). Receipt is UNCONFIRMED — do not treat this
   submission as live until acknowledged. Sent as PDF only; the exceptional route asks for
   zipped TeX/LaTeX plus PDF and an explanation why not arXiv.
   Submission ID was: "PENDING — email submission; no portal/manuscript ID assigned yet;
   awaiting editorial acknowledgement" — corrected 2026-09-21; it awaited an identifier that
   SIGMA does not issue.
```

**Not applied.** `submission_log.txt` sha256 is unchanged at
`70f814b926a5fd67a761bbebe19b5474db69b440e7e3f2340624c79029897433`.

---

## The chase handle — which title

Verified by `scripts/check_title.py` (exit 1, 9/9 controls, claims S61-19..23).

The title of record is identical in all three places it is written — page 1 of
the submitted PDF (resolved by md5 `4d1e4d59072cad0db8edc86280af45a1`), the
body of the cover letter, and the log's `Title:` field:

> A non-classical Painlevé V transcendent from a quadratic polynomial
> continued fraction: surface classification and resurgent Stokes data

**The cover letter's Subject line, however, is truncated**, dropping
`: surface classification and resurgent Stokes data`. That subject line is how
the editorial office will have filed a direct-email submission, so:

- **search** sent mail and ask the office on the stem
  `A non-classical Painlevé V transcendent from a quadratic polynomial continued fraction`,
  with the date 1 June 2026 and ORCID 0009-0000-6192-8273;
- **quote** the full title of record in the message itself.

Searching on the full string would return nothing, which is indistinguishable
from a submission that never arrived — the very question still open here.
