# PREREG — CT-S59-JDE-THM61

**Honesty note, first.** This file was written *after* the first read, not
before it. The session began as a targeted file inspection (no computation),
and the reads were already under way when the record was opened. It is
recorded here rather than presented as a pre-registration it was not. The
thresholds below were not adjusted after seeing results, and the falsifiers
are stated in the form the scripts actually test.

## Hypothesis under test

The operator's, quoted:

> Poincaré–Perron proper assumes coefficients with finite limits, and PCF
> recurrences have b(n) → ∞. If Theorem 6.1 applies Poincaré–Perron directly
> to an un-normalised PCF recurrence, that's a misapplied theorem, not a bad
> citation — and a misapplied theorem in a paper under review is the kind of
> thing that does warrant telling the editor. If the recurrence is normalised
> to finite limits first, it's fine.

Two independent propositions are therefore on trial:

- **H1** — Theorem 6.1 applies Poincaré–Perron to the un-normalised PCF
  recurrence.
- **H2** — the paper is under review at the Journal of Differential Equations.

H2 is a premise, not a conclusion, and the instruction set depends on it. It is
checked because an unchecked premise is the cheapest place for a whole
conclusion to go wrong.

## Observables

| # | Observable | Source |
|---|---|---|
| O1 | the title and hypothesis of the environment rendered as "Theorem 6.1" | the as-submitted **PDF**, md5 `75ee5c4fcc3dc21668794d02daa23a93` |
| O2 | whether the text applies that theorem to `Q_{n+1} = b(n)Q_n + Q_{n-1}`, or declines to | TeX source sha256 `bb392b76…9153` **and** the render |
| O3 | the number of `\Cref`/`\ref`/`\autoref` to `thm:poincare-perron` | TeX source |
| O4 | the `Verdict:` line of the entry whose `Submission ID:` is `JDEQ26-983` | `submission_log.txt` |

O1 is read off the **render**, not inferred from `\newtheorem` counters, because
"Theorem 6.1" is a rendered number and inferring it would make the check a
restatement of my own count.

## Falsifiers, with thresholds

- **F1 (H1 confirmed → misapplication).** If the decline sentence
  "the Poincaré–Perron theorem does not apply directly" occurs **0 times** in
  the source, or **0 times** in the render, H1 is live and the finding is a
  misapplied theorem.
- **F2.** If O3 > 0, at least one cross-reference may be a proof step invoking
  Theorem 6.1, and each must be read individually before H1 can be dismissed.
- **F3 (premise).** If the `Verdict:` line begins `REJECTED`, H2 is false and
  instructions 1–2 of the brief, and the editor-notification branch of
  instruction 3, do not apply.
- **F4 (self-check).** If any control below fails to fire, no result in this
  session may be reported.

## Vacuity pre-check

Each detector must be shown able to return the other answer:

1. the theorem-title matcher must **not** match a fabricated title
   ("Riemann–Hilbert correspondence");
2. the decline matcher must **not** match a fabricated sentence
   ("does not apply obliquely");
3. the absent-`\bibitem` detector must return **present** for `/[Pp]erron/` and
   **absent** for `/[Kk]reuser/` in the same pass;
4. the hash check must fail on one perturbed byte;
5. the ligature-tolerant matcher must separate
   "convergent coefficients" (present) from "divergent coefficients" (absent);
6. the submission-ID lookup must find `JDEQ26-983` and not `JDEQ26-000`;
7. the stale-status detector must report **clean** on a status line that
   records a rejection.

Controls 5–7 were added *during* the session, 5 after the reader was caught
inventing a defect (below). That is recorded as an amendment, not backdated.

## Mid-session amendment — a reader defect, caught

The first run of `check_thm61.py` reported **4** findings. Two were mine:

- `pdftotext` on this build emits the `ffi`/`fi` ligatures as a **space**
  ("simpli ed form", "satis es"), so a literal search for
  "it requires convergent coefficients" reported it **absent** — verbally
  identical to what the check reports if the paper had really omitted its
  reason. This is the CT-S26 class exactly.
- the Birkhoff–Trjitzinsky bibitem regex used `[^\\]*?`, which cannot cross the
  `\emph{Acta Math.}` between the title and the year, so it reported
  `NOT FOUND` for an entry that is present.

Repaired by matching the source (authoritative, unligatured) *and* the render
with a ligature-tolerant pattern, and by allowing the bibitem regex to span
markup. Two further controls were added, one of which requires the matcher to
**recover a phrase the literal search provably misses in this render** — so the
tolerance cannot silently degrade to matching everything.

Both were invented defects, not missed ones. Neither reached the report.

## Out of scope

- No re-derivation of the paper's mathematics.
- No edit to `submission_log.txt` or to any earlier session.
- No email, deposit, or commit.
