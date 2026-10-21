# PREREG — CT-S37-DRAFT-B (Group B: §3 local data, §4 the moduli space)

Written before `scripts/draft_check.py` was run. `scripts/claim_index.py` is a
read-only index over the corpus and was run during input gathering; it computes
nothing about the drafted prose.

## Hypothesis

H: Every claim id cited in `section3.tex` and `section4.tex` resolves to a
claim in the corpus, is not superseded, and carries in the prose exactly the
epistemic label that claim currently carries in its `claims.jsonl` record.

## Observable

`scripts/draft_check.py` extracts, from each drafted `.tex` file, every pair
(claim id, asserted label), where the asserted label is the nearest preceding
`\textbf{LABEL}` with LABEL in the corpus label vocabulary
{PROVEN, VERIFIED, STRUCTURAL, CONJECTURED, INSPECTED}. For each pair it
reports one of:

- `OK` — id resolves, not superseded, label matches;
- `UNRESOLVED` — no such id in the corpus, under either the literal id or the
  `CT-` prefixed alias;
- `SUPERSEDED` — the record carries a structured `superseded_by`;
- `MISMATCH` — the corpus label differs from the label asserted in the prose;
- `ALIAS` — resolved only via the `CT-` prefix (reported, not failed).

The exit code is 0 only if there are zero UNRESOLVED, zero SUPERSEDED and zero
MISMATCH.

## Falsifier, with a numeric threshold

The check FAILS, and the session halts and reports, if

  (UNRESOLVED + SUPERSEDED + MISMATCH) > 0.

Threshold: zero. No tolerance. Fixed before the first run and not revised
afterwards.

## Control required by the task

One deliberately wrong label must be caught. This is implemented as a mutant
suite, `scripts/mutants_draft_check.py`, not as a single arm, and each arm must
be CAUGHT **for the stated reason**:

- an arm is CAUGHT only if the checker exits non-zero AND its output names the
  mutated claim id AND the output contains no `Traceback`, `SyntaxError` or
  `NameError`;
- an arm that exits non-zero because the checker crashed is reported MISSED.

Arms (all drawn from labels and ids that do **not** appear beside the mutated
citation in the unmutated text, so that no arm can be rejected merely because
the checker consults its own constant list):

1. `S4-03` relabelled PROVEN → CONJECTURED (label the corpus never uses for it);
2. `S16-01` relabelled INSPECTED → PROVEN (the upgrade P0 forbids);
3. `S6-C16` relabelled STRUCTURAL → VERIFIED;
4. `S16-04` relabelled STRUCTURAL → INSPECTED;
5. a cited id replaced by `S4-99`, which does not exist (UNRESOLVED arm);
6. a cited id replaced by `S4-01`, which exists and self-declares superseded
   (supersession arm);
7. `CT-S9-PVPARAMS-C005` replaced by its alias-stripped form
   `S9-PVPARAMS-C005` (must resolve, and must be REPORTED as an alias);
8. `section3.tex` truncated to zero bytes (reader-integrity arm: the checker
   must refuse, not report "0 problems").

## Vacuity pre-check

The observable must move when the data it is about moves. Two directions:

(i) **Sensitivity.** Arms 1–6 change the prose and must change the verdict from
    PASS to FAIL. If any arm leaves the verdict at PASS, the observable is
    insensitive to the hypothesis and the session halts.

(ii) **Non-vacuity of the reader.** Before reporting any count, the checker
     asserts, for each drafted file: it decodes as UTF-8; it contains the
     non-ASCII sentinel `é ö ±`; it is at least 4000 bytes; it contains at
     least 4 `\subsection{`; and it yields at least 15 (id, label) pairs.
     These are **bounds**, not exact fingerprints, so that a legitimate edit to
     the prose cannot fire them before the pairs are examined. Arm 8 exercises
     this guard.

## Pre-registered expectation

Recorded before the first run so that the outcome can be scored against it:
the drafted prose is expected to PASS, and the `S9-PVPARAMS` → `CT-S9-PVPARAMS`
alias is expected to be REPORTED but not to fail the run, since the drafts
use the corpus form. If instead a MISMATCH appears, that is a finding about the
draft and is to be reported, not silently repaired.

## Known non-falsifiers, declared in advance

- Corpus-wide parse noise (unparseable lines in three 2026-04/2026-05 sessions)
  and 84 duplicate bare claim ids in 2026-05 sessions are **pre-existing**,
  predate every `CT-S*` session, and are out of scope. They are reported, not
  repaired.
- A claim whose free text merely mentions "superseded" is **not** treated as
  superseded. Only a structured `superseded_by` field fails the run. Text hits
  are surfaced as warnings for adjudication.
- Group A (§0, §2) is undrafted. §3 and §4 do not depend on it, but the task's
  premise that "sections already drafted are inputs" is unmet for Group A and
  this is reported rather than worked around.

---

## AMENDMENT (post-hoc, recorded because a threshold proved ill-posed)

Written AFTER the first two runs of `scripts/draft_check.py` and before the
run that produced the reported verdict. Nothing in the falsifier changed.

**What was pre-registered.** The reader-integrity non-vacuity bound required at
least 15 (id, label) pairs per drafted file.

**What happened.** `section3.tex` yields 45 pairs. `section4.tex` yields 12.
Twelve is the true number of citations in a correctly drafted section: §4 is a
reading section resting on nine distinct claims, three of them cited more than
once. The bound therefore fired on correct prose, which is precisely the
fingerprint failure a non-vacuity bound exists to avoid — a bound must
distinguish an empty or unreadable file from a real one, not encode a guess at
how many citations a section ought to contain.

**What changed.** `MIN_PAIRS` narrowed from 15 to 5 per file, with a new
group-level bound `MIN_PAIRS_TOTAL = 30`. The original value, the observed
values and this reason are recorded here and in REPORT.md.

**Boundary mutant added in the same edit.** Arm `M9` reduces `section4.tex` to
exactly four citations while leaving its byte count and subsection count
untouched, so that only the narrowed bound can fire. `M9` must be CAUGHT. This
is the same handling applied to N5 and N7 in CT-S35: narrowed post-hoc,
boundary mutant added in the same edit, both caught, and disclosed rather than
presented as the original design.

**The falsifier was not touched.** It remains
(UNRESOLVED + SUPERSEDED + MISMATCH) > 0, threshold zero.

## SECOND FINDING FROM THE SAME FAILURE

The first run also exposed a defect in the checker rather than in the prose.
The claim-id pattern was
`(?:CT-)?S\d+[A-Z]*-[A-Z]*\d+(?:-[A-Z]+\d+)*`, which requires each segment to
end in digits. `CT-S9-PVPARAMS-C005` has the segment `PVPARAMS`, which does
not, so **every** `CT-S9-PVPARAMS-*` citation was silently dropped: eight in
§3 and three in §4. The checker would have reported PASS while never having
examined eleven of the fifty-seven citations. It surfaced only because the
reader-integrity bound fired and the pair counts were read. Repaired to
`(?:CT-)?S\d+[A-Z]*(?:-[A-Z0-9]+)+`; the counts moved 37 → 45 and 9 → 12,
which is the evidence that the repair changed what is examined.
