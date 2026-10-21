# REPORT — CT-S55-BASE-VERSION

**Which version of the manuscript does *Letters in Mathematical Physics* hold
for MATH-D-26-00523?**

## 1. Verdict

**LMP holds v1.2** — Zenodo record 21412469, md5 `792107efab6317e8ae21e2ca20f092ff`,
778,209 bytes, 25 pages.

**CT-S52's revision was built against v1.0** — md5 `99faea5b0f4095788e4ee932436beeda`,
24 pages. **A rebase is required before any §5 edit is applied.**

Two routes, independent of each other, agree:

| route | method | result |
|---|---|---|
| 1 | md5 of the manuscript item as uploaded | byte-identical to v1.2 |
| 2 | page-for-page text of the stamped build | 25 of 25 pages match v1.2 |

All five pre-registered predictions held. No falsifier fired.

A corollary worth stating plainly, because it cuts against the suspicion that
prompted the session: **the submission itself was internally consistent.** v1.2
was published 2026-07-17 and the manuscript was submitted 17 Jul 2026, so the
cover letter's promise that the deposited PDF is identical to the submitted file
was true when written. What went wrong was downstream — CT-S52 reconstructed the
base from the only copy in the repository, which was v1.0.

## 2. What was done

The operator asked for the submitted file to be hashed and the session halted.
That was done first and reported. The operator then pointed at the download
link embedded in the stamped PDF. That link resolved, and it changed the
character of the result: what had been a content-comparison problem became a
hash identity.

### 2.1 Route 1 — the manuscript item itself

Editorial Manager serves two different things, and the distinction is the whole
problem:

- **(A) the stamped build**, `MATH-D-26-00523.pdf`, which EM compiles for
  review. 27 pages: a two-page submission cover, then 25 manuscript pages, each
  carrying stamped line numbers `1..65` and, on the first, a download-link
  header. md5 `e2f27a8ee5288dd1f0d8fedb0909a63f`.
- **(B) the manuscript item**, served through the link in (A) at page 3 as
  `https://www2.cloud.editorialmanager.com/math/download.aspx?id=60154&guid=68eb…`.
  EM returns this **as uploaded, unstamped**, with
  `content-disposition: attachment; filename="vquad-periodrep-paper-v1.2.pdf"`.

(A) matches **none** of the four published versions. **That zero is the expected
result, not a finding** — (A) is EM's own re-render and cannot hash to an author
file. It is recorded explicitly (claim S55-04) so that a later reader cannot
mistake it for evidence about which version was submitted. This is the same
hazard as an empty sweep: a non-match that means nothing looks exactly like a
non-match that means something.

(B) is byte-identical to v1.2. The comparison required md5 equality and full
byte equality to agree, and refuses if they ever diverge.

The link used to fetch (B) was **read out of the PDF's own link annotations**,
not transcribed from the rendered header text — `hash_submitted.py` re-reads the
annotation and refuses if the URI it records is not present in (A). Provenance
is therefore established rather than asserted.

### 2.2 Route 2 — the content of the stamped build

Pre-registered before it was run, and kept even after route 1 settled the
question, because an absence-or-identity claim deserves a second,
differently-implemented read.

The EM overlay had to be removed for any page comparison to be possible, and a
stripping rule that may remove whatever stands in its way can manufacture a
match. The rule (PREREG §3.0, S1–S3) is therefore narrow and self-policing: it
removes only the maximal trailing run of standalone line-number lines, and that
run must read exactly `1, 2, …, N` with `N ≥ 20` or the script refuses; plus, on
one page only, the EM download-link block. Nothing else. It is applied to the EM
pages only — never to a candidate, since stripping both sides would let the rule
erase a genuine difference.

Graded result:

| version | pages | pages matching the EM body |
|---|---|---|
| **v1.2** | 25 | **25 of 25** |
| v1.1 | 25 | 20 of 25 |
| v1.3 | 26 | 16 of 25 |
| v1.0 | 24 | 0 of 25 |

The margin over the runner-up is 5 pages. v1.0 scores zero because its 24-page
length shifts every page index — the page-count difference alone separates it.

## 3. Controls

The verdict rests on the observable being able to fail. Three independent
checks, all evaluated **after** the observable (a vacuity check guards a PASS,
not a FAIL):

- **V1 pairwise distinctness.** All six pairs of candidate versions differ. A
  full match against one therefore excludes the other three.
- **V2 negative control.** Swapping two adjacent EM body pages drops every
  candidate, including the winner, below a full match (v1.2 falls to 23/25). The
  observable is sensitive to page content, not merely to page count.
- **V2b the rule cannot manufacture the match.** Re-running with `strip_em`
  replaced by the identity gives **0 of 25** for every candidate. The match is
  produced by manuscript content surviving the overlay, not by the stripping.

`emit_claims_s55.py` was exercised by a **14-arm harness, 14/14 CAUGHT**, each
arm in a fresh scratch directory — an arm run in the session directory would
overwrite the very `claims.jsonl` the claims cite. `claims.jsonl` was
byte-identical before and after, sha256 `5b5024f8…`.

| arm | expected | result |
|---|---|---|
| **A0** pristine | **must WRITE** | wrote 7/7 claims, rc 0 |
| M1 routes disagree on the version | refuse | rc 2, its own reason |
| M2 rebase flag flipped to NO | refuse | rc 2 |
| M3 unstripped match no longer zero | refuse | rc 2 |
| M4 a falsifier recorded as fired | refuse | rc 2 |
| M5 stamped build recorded as matching | refuse | rc 2 |
| M6 anchor line duplicated | refuse | rc 2, "matched 2 lines" |
| M7 anchor line deleted | refuse | rc 2, "matched 0 lines" |
| M8 output_hash attributed to wrong script | refuse | rc 2 |
| M9 a claim emptied of its text | refuse | rc 2 |
| M10 label outside the permitted set | refuse | rc 2 |
| M11 sweep reported as empty | refuse | rc 2 |
| M12 second instance unconfirmed | refuse | rc 2 |
| M13 sweep split no longer sums | refuse | rc 2 |

An arm provoking a `SyntaxError` or `NameError` is **rejected, not counted as
CAUGHT** — a traceback echoes the offending source line, so the injected reason
string can appear in the output of a script that never ran a check.

### 3.1 A0 caught a defect in the harness itself

On its first run A0 **MISSED**: it asserted the emitter writes 6 claims, a
figure transcribed when the harness was written, while the emitter now writes 7.
The harness was reporting a working emitter as broken. Repaired by **deriving**
the expected count from the real artefact rather than carrying a literal. The
same defect class this session exists to examine — a figure fixed by
transcription rather than read from the thing it describes — appeared inside
the instrument built to study it.

## 4. Amendment H sweep — and it is not empty

The commissioning question was "is CT-S52's base the wrong document?". The defect
class beneath it: **an artefact identified or described from the only copy in
the tree, rather than from its content.**

CT-S52 named its base "the file published in Zenodo record 20719043" and its own
output records that only because v1.0 was the only V_quad paper PDF present. The
rebuild-and-compare it performed was rigorous about *which .tex produces this
PDF* and silent about *whether this PDF is what LMP holds*.

**A second instance is confirmed.** The arXiv upload material — the metadata
package, its submission runbook, its consistency gate, its ledger and CT-S51's
walkthrough — names as its source
`sessions/2026-06-16/VQUAD-PAPER-LAYOUTFIX-001/latex/`, whose PDF is md5
`99faea5b…`, 24 pages: **v1.0**. Following that runbook today would upload a
version two behind the deposit and one behind what the journal holds, with a
Comments field reading `24 pages` for a 25- or 26-page paper.

Same cause, not merely the same shape: v1.0 is the only V_quad paper PDF in the
tree, so every pass that went looking for "the paper" found it, and none checked
the content.

The census found 46 page-count figures, 35 equal to v1.0's 24. **That is a
census, not a defect count** — a figure of 24 that correctly describes v1.0 *as*
v1.0 is right. The split:

- **28 actionable** — arXiv field values to be entered or instructions to be
  acted on.
- **7 descriptive and correct as written** — CT-S52's `identify_source.out.txt`
  and `CHANGES.md:11` describe v1.0's rebuilds and v1.0's md5, which really are
  24 pages. What is wrong there is the *inference*, recorded as S55-03, not the
  number.

Hits decided **not** to be defects are listed with reasons in
`outputs/sweep_h.out.txt` §3, including CT-S51's `STATE.md` pinning record
20719043 (correct — it documents the v1.0 deposit, not the submission) and
`check_upload_ready.out.txt:35`'s "12 pp" (the companion paper, a different
document).

## 5. Claims

| id | label | substance |
|---|---|---|
| S55-01 | INSPECTED | EM's manuscript item 60154 is byte-identical to v1.2 (record 21412469) |
| S55-02 | VERIFIED | Independently, the stamped build's 25 body pages match v1.2 25/25; runner-up v1.1 at 20/25 |
| S55-03 | INSPECTED | CT-S52's base is v1.0, 24 pages; rebase required; its identification was assumed, now refuted |
| S55-04 | INSPECTED | The stamped build matches 0 of 4 — expected, and explicitly not evidence |
| S55-05 | VERIFIED | The observable is content-sensitive and the stripping rule does not manufacture the match |
| S55-06 | INSPECTED | Concept 20719042 has four versions incl. v1.3 (2026-09-13) — **already established by CT-S53**, restated only because an independent fetch agrees |
| S55-07 | INSPECTED | Amendment H sweep: not empty; second instance confirmed in the arXiv material |

## 6. What this does NOT establish

- **Nothing was rebased.** The §5 edits prepared in CT-S54 REPORT.md §10 remain
  unapplied. CT-S52's revision still sits on v1.0.
- **No section or line number in the correspondence was re-checked.** The
  follow-up email drafted in CT-S54 cites Proposition 2.4, Lemma 2.7, Table 1,
  Remark 3.4, §5 and Table 2 as read off the journal PDF. This session did not
  verify that those numbers are the same in v1.2 as in whatever they were read
  from. **They must be checked against v1.2 before the email goes.**
- **What changed between v1.0, v1.1, v1.2 and v1.3 was not examined.** The page
  counts differ (24/25/25/26) and 20 of 25 pages of v1.1 match v1.2, but no diff
  was taken. A rebase needs that diff.
- **The relationship between v1.3 and the editor correspondence was not
  examined.** v1.3 was published 2026-09-13; the cover letter promised the
  deposit and the submission would be identical, and the deposit is now two
  versions ahead of the submission. CT-S53 holds the relevant record.
- **The 28 actionable arXiv figures were not repaired.** They are reported, not
  fixed; that material is held pending the editor in any case.

## 7. Open questions for the operator

1. **Rebase onto v1.2, then diff v1.0 → v1.2** before re-applying the ξ=0 edits.
   Some of CT-S52's edits may already be present, and some may not apply.
2. **Re-check every section number in `FOLLOWUP-EMAIL.md` against v1.2** before
   sending. The email's content stands; its numbering is unverified.
3. **The deposit is now ahead of the submission — but the cover letter was true
   when written.** Page 2 of the EM build states: *"A citable, timestamped
   version is deposited on Zenodo as a preprint only, concept DOI
   10.5281/zenodo.20719042 (the deposited PDF is identical to the file submitted
   here)."* That was **accurate at submission**: v1.2 was published 2026-07-17
   and the manuscript was submitted 17 Jul 2026, and the submitted file *is*
   v1.2. The sentence became untrue on **2026-09-13**, when v1.3 was published —
   the statement cites the *concept* DOI, which resolves to the latest version.
   So the discrepancy is not a submission error; it is drift that opened two
   months later. Whether it needs mentioning to the editor is a judgement, not a
   computation, but it is now documented rather than suspected.
4. **The arXiv material needs rebasing too**, if arXiv is still intended.

## 8. Uncommitted files

Nothing was committed, pushed, tagged, sent, uploaded, submitted or deposited.
Network activity was read-only HTTP GETs: the public Zenodo API and records, and
one Editorial Manager download link that was already embedded in a file the
operator supplied. No token or credential was used or is present.

```
sessions/2026-09-17/CT-S55-BASE-VERSION/
  PREREG.md                                            9174 B
  REPORT.md                                            this file
  claims.jsonl          sha256 5b5024f89b8e193ba14aab1167c53a583d0b7f9536a0b8c77d7ce8af7b7a34af
  scripts/hash_submitted.py                            8501 B
  scripts/base_version.py                             14909 B
  scripts/sweep_h.py                                  10005 B
  scripts/emit_claims_s55.py                          14861 B
  scripts/controls_s55.py                              9132 B
  outputs/submitted_file_hash.out.txt   sha256 3e1f81e1b4b9f27f…
  outputs/base_version.out.txt          sha256 407417fe7cf46bdc…
  outputs/sweep_h.out.txt               sha256 fadc9398f3c0041d…
  outputs/controls.out.txt              sha256 2795d7d97f93dc9c…
  refs/MATH-D-26-00523-EM.pdf                       1074874 B  (operator-supplied)
  refs/EM-manuscript-item-60154-vquad-periodrep-paper-v1.2.pdf
                                                     778209 B  (fetched via the link in the above)
  refs/em-download-response-headers.txt                 984 B
  refs/zenodo-20719042-versions.json                  42987 B  (verbatim API response)
  refs/zenodo-v1.0-20719043.pdf                      773171 B
  refs/zenodo-v1.1-21410927.pdf                      775400 B
  refs/zenodo-v1.2-21412469.pdf                      778209 B
  refs/zenodo-v1.3-22731371.pdf                      784836 B
```

All four Zenodo references were md5-verified against the stored API response,
resolved by exact field path `hits.hits[].files[].checksum` — never by searching
for a key named `checksum`.

`refs/EM-manuscript-item-60154-…pdf` and `refs/zenodo-v1.2-21412469.pdf` share
sha256 `97ec5aff4b08f4ef48587358286451b2a6398f4c4d14062c2a2f8e8c69b5f2d3`. That
identity is the answer to the question this session was asked.
