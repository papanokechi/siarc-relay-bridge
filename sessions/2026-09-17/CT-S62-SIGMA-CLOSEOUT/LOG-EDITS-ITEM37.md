# LOG-EDITS-ITEM37 — SIGMA closeout

GENERATED 2026-09-21 by scripts/check_sigma_closeout.py — do not hand-edit.
Built against submission_log.txt sha256 70f814b926a5fd67a761bbebe19b5474db69b440e7e3f2340624c79029897433
If that is not the log's current digest, regenerate rather than patch.

## What this edit does, proved

- Section-A active count **4 -> 3** (Item 37 leaves; 36, 39, 42 remain).
- Vacuity arm: a non-terminal verdict spliced in the same place leaves the count at 4, so the observable tracks the verdict text.
- All four scanners read the new Verdict as terminal, and on the word `REJECTED` — not on an incidental word, which is the CT-S61 `accepted` defect.
- `submission_log.txt` was NOT modified by this script; the edit was applied to an in-memory copy only.

## Practice ruling applied

Operator ruling 1 (2026-09-21): *"when a verdict is recorded, the Status line changes in the same edit"*. Both change here, together. The old Status is kept beneath as a dated `Status was:` line, so nothing is lost. Nothing else in the item is rewritten — the concurrent-submission flag is **appended to**, not edited, because it is evidence.

## Replace Item 37's `Status:` and `Submission ID:` lines with these four lines

```text
   Status: REJECTED by SIGMA 2026-09-21 at editorial screening, without refereeing — closed at this venue; manuscript free to reroute.
   Status was: [until 2026-09-21] Submitted to SIGMA (Symmetry, Integrability and Geometry: Methods and Applications) — direct email to editorial office (PDF route, per the editorial-office provision for independent researchers who cannot clear arXiv endorsement; cover letter discloses the Zenodo preprint)
   Submission ID: NONE — SIGMA issues no manuscript identifier: it is an arXiv overlay journal whose instructions direct authors to send the arXiv number, and this was the exceptional non-arXiv direct-email route. Superseded 2026-09-21: the previous reading "PENDING … awaiting editorial acknowledgement" awaited an identifier the journal does not issue. See CT-S61 claims S61-12, S61-13.
   Verdict: REJECTED 2026-09-21 by the SIGMA Editors, conveyed by Mrs. Vira Pobyzh, Executive Assistant — "not suitable for consideration in SIGMA as not of the standard required for publication in this journal". EDITORIAL SCREENING ONLY: the letter states the journal is "highly selective about papers for which to start the refereeing process", so no referees were assigned and there are no reports. No substantive reason was given; the formula is the journal's standing screening wording and is NOT a finding about the mathematics. Elapsed 112 days from submission (2026-06-01) to decision. DISPOSITION: paper is free at SIGMA; joins the redirect queue. RECEIPT QUESTION SETTLED: the decision proves the 2026-06-01 direct-email submission reached the editorial office, so SIGMA's two-working-day resend remedy (sigmajournal@gmail.com) is MOOT and must not be fired; this supersedes the "receipt UNCONFIRMED" reading of CT-S61 claims S61-14 and S61-15. Verbatim letter: sessions/2026-09-17/CT-S62-SIGMA-CLOSEOUT/email/sigma_decision_as_received.txt
```

## Append to the end of Item 37's CONCURRENT-SUBMISSION FLAG line

```text
 SUPERSEDED 2026-09-21 (text above retained verbatim): SIGMA rejected the manuscript at screening, so the SIGMA side of the concurrent-submission conflict is closed by the venue rather than by the withdrawal. The conflict is NOT resolved: §A Item 36 (The Ramanujan Journal) remains non-terminal with a reviewer assigned, so the manuscript is still live at one venue. The sentence above, "SIGMA becomes the sole live venue carrying the corrected v1.2", is now void in direction — if anything survives it is Ramanujan, and Ramanujan holds v1.0, NOT v1.2. The withdrawal must still complete, but its operative ground is no longer conflict-clearing (moot): it is that a reviewer is refereeing the superseded v1.0 build, which carries the withdrawn Stokes constant S=0.43770528 and Theorem 4.1 un-demoted. See CT-S62 claim S62-07.
```

## Acceptance test after pasting

```powershell
python sessions\2026-09-17\CT-S61-SNAPSHOT-AND-STATUS\scripts\make_active_snapshot.py
```

It must report **Active: 3** and must no longer list Item 37. Regenerate the pasted snapshot block at the same time — it carries the old log digest and is stale the moment this edit lands.

## Not included, deliberately

- No substantive reason for the rejection. The letter gives the journal's standing screening formula; recording it as a judgement on the mathematics would be inventing a finding.
- No change to Item 36. That is a separate decision and a live one — see REPORT.md §3.
- No change to §B Item 17, whose Zenodo row Item 37 already flags as STALE at v1.0. Still outstanding.

