# PREREG — CT-S21-DEPOSIT-PREP

**Written before any computation, fetch, or page read in this session.**
Nothing will be deposited, uploaded, committed, or sent. The single output is
`DEPOSIT-READY.md`.

## Hypothesis under test

**H.** The companion v1.3 correction notice
(`CT-R1-AUDIT/DRAFT-COMPANION-v1.3-NOTICE.md`) is ready for deposit: every
external source it cites can be re-fetched and hashed today; every passage it
quotes matches the source as printed on a page image; every `claim_id` and
support-table row it cites resolves against the live claim corpus with the label
and review value the notice states; and no sentence asserts as author-confirmed
anything that is not.

H is a **conjunction**. It is refuted by a single failing conjunct.

## Observables and falsifiers, fixed now

| # | Observable | Falsifier — fires if |
|---|---|---|
| F1 | re-fetch of each of the 4 external citations | any source cannot be re-fetched **and** the fact is not recorded as NOT RE-FETCHED with its reason |
| F2 | byte-identity of the re-fetched file against the local copy, by sha256 | a hash differs and the difference is not explained and recorded |
| F3 | each quoted passage vs the page image | any quote DIFFERS in a way that changes the sentence built on it |
| F4 | every `claim_id` cited in the notice | the id does not exist in the corpus, or is superseded |
| F5 | every support-table row (label, review) | the row disagrees with the live claim |
| F6 | internal cross-references, section numbers, item numbers | any reference does not resolve |
| F7 | author-confirmation wording | any sentence states or implies that an author, referee, or maintainer has confirmed something that has not been confirmed |

**Thresholds are exact, not statistical.** F2 compares full sha256. F4–F6 are
string identity against the corpus and the notice's own numbering. No threshold
may be relaxed after seeing a result; a threshold that proves ill-posed is
reported as a finding.

## Vacuity pre-check — required before any conjunct is reported as passing

Each mechanical test must be shown to be able to **fail**, on this data, before
its pass is reported. Recorded per test in `outputs/`:

- **F4/F5:** inject a `claim_id` known to be absent (`R1-99999`) and a label
  known to be wrong, and confirm the checker reports both. If it does not, the
  checker is measuring nothing and the run halts.
- **F3:** at least one quote must be checked **character by character against
  the image**, not against another file in this repository, since every text
  file here descends from the same earlier reading. A quote check that compares
  the notice to a transcription made by this project is **circular** and is
  recorded as NOT CHECKED, not as MATCHES.
- **F2:** confirm the hash function distinguishes the v1.1 and v1.2 companion
  PDFs, which differ.

## Known limits, stated in advance

1. **A re-fetch is not an independent edition.** If a publisher serves the same
   file, F2 confirms transport integrity, not that the printed page says what we
   think. Only F3 does that.
2. **Quote verification is bounded by what the page images show.** Passages with
   no page image are **NOT CHECKED**; they are not assumed.
3. **No licence determination will be made**, and **no exclusion will be
   changed**, per the packet. Licence strings are recorded as printed or
   **NOT CHECKED**.
4. **Readiness is a judgement about evidence, not a permission.** The deposit is
   the operator's act regardless of this file's verdict.

## Halt conditions

Stop and report rather than improvise if: a falsifier fires; a quote DIFFERS
materially; a source cannot be re-fetched and no cached provenance exists; a
convention is ambiguous; or the session exceeds 3x its budget.
