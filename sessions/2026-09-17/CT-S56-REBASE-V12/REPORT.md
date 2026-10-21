# REPORT — CT-S56-REBASE-V12

**Task.** Rebase the revision of MATH-D-26-00523 onto **v1.2**, the version
Letters in Mathematical Physics actually holds, and apply CT-S52's four items
plus a new item 5 on the independence of Methods B and C.

**Status.** Draft. Nothing committed, pushed, tagged, uploaded, submitted or
deposited. All files listed at the end are uncommitted.

---

## 1. What was done

| stage | script | result |
|---|---|---|
| 1 | `locate_source.py` | v1.2's source located, proven by byte-identical rebuild |
| 2 | `version_diff.py` | v1.0→v1.2 and v1.2→v1.3 diffed; all 19 CT-S52 edits apply |
| 3 | `apply_revision_v12.py` | 33 replacements, each matching exactly once |
| 3b | `build_check.py` | 27 pages, 0 TeX errors, 0 undefined references |
| 4 | `render_diff.py` | every rendered change attributable to items 1–5 |
| 4b | `locate_numbering.py` | edits located in v1.2's own numbering |
| 5 | `make_docs.py` | `CHANGES.md`, `CORRECTIONS-FOR-REFEREES.md` |
| — | `sweep.py` | Amendment H sweep; reproduces the original before-run byte-identically |
| — | `sweep_compare.py` | Amendment H sweep, before vs after (57 → 65) |
| — | `pattern_drift.py` | settles the `independent` vs `independen` question |
| — | `email_coverage.py` | revision checked against the emails **as sent** |
| — | `home_for_s56_01.py` | the submitted source given a home in the repo record |
| — | `verify_unchanged.py` | submitted artefacts byte-unchanged |
| — | `mutants_s56.py` | 9-arm control harness, A0 writes, 8/8 caught |
| — | `emit_claims_s56.py` → `verify_claims.py` | 23 claims, all verified against disk |

---

## 2. The finding that matters most

### The repository does not contain the source of the submitted paper.

The pre-registered gate asked whether any source in the tree rebuilds to v1.2.
**It failed.** Two candidates rebuilt *byte-identically* to **v1.0**, and nothing
scored above 0/25 pages against v1.2. Every July-dated session is absent; v1.1,
v1.2 and v1.3 were built from working directories under `C:\LocalWork` that were
never committed.

That negative is reported on its own, and is **not erased** by what followed.
The operator's halt condition — *if no source in the tree rebuilds to v1.2,
STOP and report* — fired exactly as written.

**The instrument was proven before the verdict was accepted.** v1.0 rebuilding
byte-identically is the positive control: without it, "nothing here builds to
v1.2" would be indistinguishable from "the build does not work here at all".

### The rescue came from applying Amendment H to this session's own scope.

The candidate list had been inherited from the phrasing of the instruction
("locate its LaTeX source … in the tree"). That is precisely the defect
Amendment H names: *a check whose scope was set by whoever reported the
problem, so the question "where else?" was never in scope and could never
fail.* Sweeping wider found `C:\LocalWork\vq-fix\src\base`, whose source
rebuilds byte-identically to v1.2 (`md5 792107ef…`). Sources for **all four**
published versions were then located and each confirmed by rebuild.

`PREREG.md` §12a records the widened candidate set, written **before** the
widened observable ran, and states explicitly that no threshold or rule changed.

---

## 3. Claims

All 24 are in `claims.jsonl`. **23 VERIFIED, 1 STRUCTURAL. None PROVEN** — the
emitter refuses the PROVEN label outright, since nothing here is machine-checked.

| id | label | substance |
|---|---|---|
| S56-01 | VERIFIED | the repo does not hold the submitted source |
| S56-02 | VERIFIED | v1.0 rebuilds byte-identically — the positive control |
| S56-03 | VERIFIED | v1.2's source found outside the repo, confirmed by rebuild |
| S56-04 | VERIFIED | v1.0→v1.2 is 3 hunks, +21/−3, journal boilerplate only |
| S56-05 | VERIFIED | all 19 CT-S52 replacements apply to v1.2, 0 broken |
| S56-06 | VERIFIED | 33 replacements, each matching exactly once |
| S56-07 | VERIFIED | bibliography 25→26, new entry last, numbering preserved |
| S56-08 | VERIFIED | 27 pages, 0 errors, 0 undefined references |
| S56-09 | VERIFIED | every rendered block attributable to items 1–5 |
| S56-10 | VERIFIED | all 33 replacements rendered; 11 substantive checks pass |
| S56-11 | VERIFIED | the reflow test passes controls in **both** directions |
| S56-12 | VERIFIED | exactly one stale tag: v1.2 has no "Remark 3.3" |
| S56-13 | VERIFIED | the automatic locator is a census, not an adjudicator |
| S56-14 | VERIFIED | every referee-facing number checked against the v1.2 render |
| S56-15 | VERIFIED | sweep 57→65, with the intended terms falling |
| S56-16 | VERIFIED | the "obtained twice" claim at v1.2 L424, now edited |
| S56-17 | VERIFIED | the revision's wording diverges from this paper's v1.3 |
| S56-18 | VERIFIED | submitted artefacts byte-unchanged |
| S56-19 | VERIFIED | control harness: A0 writes, 8/8 negative arms caught |
| S56-20 | VERIFIED | item 4's further correction: "obtained twice" had **zero** valid confirmations |
| S56-21 | VERIFIED | the narrow sweep pattern cannot see Method A's independence claim |
| S56-22 | VERIFIED | the submitted source has a home in the repo record, by content |
| S56-23 | **STRUCTURAL** | this session deleted its own evidence for the pattern-drift observation |
| S56-24 | VERIFIED | the new bibitem is the **companion's** v1.3, confirmed against the Zenodo API |

---

## 4. Instrument findings

These are defects in the *checking*, not in the paper. Each was caught by a
control, and each is recorded because an empty sweep and an absent sweep are
indistinguishable in a report that records only repairs.

**(a) The attributor could not tell "too short to decide" from "unexplained".**
The first run reported 20 unattributable blocks. All 20 were fragments —
hyphenation splits, re-split maths tokens, running headers. A block containing
no four-letter token scores 0% against every replacement, which is *identical*
to what a genuinely unexplained change scores. Repaired by stripping
headers/footers before diffing, merging fragments, and adding a decidable
reflow test. 177 raw blocks → 26; 25 attributed, 1 accounted exactly.

**(b) The reflow test was the dangerous one, so it is controlled both ways.**
A normaliser that stripped digits would make `8.84` and `3.69` compare equal and
would have reported item 5's central edit as mere pagination. Digits are
deliberately preserved, and the control asserts both that hyphenation *does*
collapse and that a changed figure *does not*.

**(c) The numbering locator invented an answer.** It located only 13 of 33 edits
and placed Theorem 1.1's text inside Proposition 3.2 — a *wrong number*, which
is worse than a miss and would have gone to referees. It was demoted to a
census. The decidable question was substituted instead: *does the object a tag
names exist in v1.2 at all?* That found exactly one stale tag.

**(d) The first mutant arm tested nothing.** M1 originally disabled the
`output_hash` check rather than corrupting the hash, and scored **MISSED** —
correctly. Disabling a guard on correct data shows only that the refusal path is
reachable. All eight negative arms now inject defects into the claim *data*.

**(e) The emitter's own hash check is vacuous in normal operation.** It compares
a hash it computed moments earlier with itself. `verify_claims.py` was added to
re-read both sides from disk, and on its first run it **failed** — the harness
had regenerated its output after the claims were written. A real firing, not a
synthetic one. The verifier is run *after* the emitter and its own output is
deliberately not claimed, since a self-citing verifier is circular.

**(f) One list, reconstructed in four places, disagreed with itself.** The L455
item-4 edit was added to the applier's `allreps` and to nothing else.
`make_docs.py`, `render_diff.py` and `locate_numbering.py` each rebuilt the list
independently as `s52 + FIVE`, so all three worked from 32 replacements while 33
were applied — and **`render_diff.py` still reported CLEAN**. An attributor
missing a replacement cannot say so; it can only attribute that rendered change
to something else, or not see it. The three reconstructions were replaced by a
single `apply_revision_v12.all_replacements()`, and `make_docs.py` now refuses
unless its parts account for the whole. The documents' stale "32" was caught not
by any of these but by the claims emitter's figure guard, which refused to write
a claim stating a number absent from its own cited output.

**(g) A sweep pattern whose inadequacy is invisible on the base.** `independent`
and the stem `independen` return the *identical 15 lines* on v1.2, so the choice
between them looked free. On the revision they differ by one line — and that
line is **Method A's independence claim**, precisely the claim item 5 exists to
restate. A check that cannot discriminate on the data you have is not thereby
adequate for the data you will have. The stem is now used for both runs; the
before-output is unaffected, byte for byte.

**(h) This session destroyed a piece of its own evidence.** The backup of the
original inline after-sweep was the only record that the two original runs used
different patterns. It was deleted in a tidy-up, in this same session, after the
observation had been made and before the claim citing it had been written; with
nothing committed it is unrecoverable. `verify_claims.py` did **not** catch this,
because the claim cited the *before*-sweep — the wrong file — and that file
hashed correctly. A hash check verifies that a cited file is intact; it cannot
verify that it is the file the claim actually rests on. The claim was rewritten
to what surviving files establish and the unverifiable part demoted to
STRUCTURAL and named as destroyed (S56-23). **Tidy-up is a write operation and
should run before claims are emitted, never after.**

---

## 5. Findings in the paper

**L455 — "Both statements are obtained twice, by a falling-factorial indicial
computation and by direct solution of the Frobenius recurrence."** Reported to
the operator as possibly a sixth correction; **ruled to fall inside item 4** and
now edited. The reasoning: the second route was run only at −ξ₀, so the
apparency statement at ξ = 0 had *zero* valid confirmations, not two. In the
revision the sentence was additionally **self-contradictory**, asserting
apparency three sentences after the corrected text states the logarithm. The
replacement says what each route covers. After the edit the term "twice" falls
to **0** occurrences. (S56-16, S56-20.)

**A second stale tag.** CT-S52's edit tags carry v1.0 numbering. Tag
"Cor 1.4 proof" names the wrong object — the apparency claim is in the proof of
**Corollary 1.3**. As with "Remark 3.3", the *tag* was wrong and the *edit*
landed correctly, because replacement matches on text, not on number. The sent
follow-up email says Corollary 1.3 and is **correct**.

### Left unedited, deliberately

**L587 — `% origin (apparent) and label`** — a stale LaTeX *comment*; the
rendered node correctly reads "(no cut)". Not edited: a comment edit is
invisible in the render, and the change set should map exactly to the five
items.

**Benign senses of "independent" left in place**, all read by hand:
"independently interesting" (L138), "independent of that construction" (L324),
"algebraically independent … Tannakian" (L1069), "Independently of
Fresán–Jossen" (L1147), the AI declaration's "independently verified" (L1285),
and Table 2's "Independent of" column header.

---

## 5a. The revision against the emails as sent

`email_coverage.py` checks the revision against what the follow-up actually
promised the editor — the reverse direction from every other check here, which
compare the revision against the *instructions*. All 15 commitments hold:

- **6/6** object numbers cited in the email exist in the revision (Proposition
  2.4, Lemma 2.7, Table 1, Figure 1, Remark 3.4, Corollary 1.3). An email citing
  an object the paper lacks is the worst defect available here, because the
  editor cannot check it.
- **7/7** assertions the email says are corrected are absent.
- **6/6** substantive replacements are present.
- Both reader controls fire.

The census of every surviving `apparen` (9) and `independen` (20) was then read
**by hand**, because the counts prove nothing: items 3–5 replace assertions with
discussion, so the words must survive. Every occurrence is corrective, benign,
or a table header. None is a surviving assertion.

---

## 6. What was NOT established

- **Not established: that the revision is ready to send.** It has never been
  read end to end as prose. Two items' worth of new text was written against a
  correction list, not composed.
- **Not established: Method A's independence.** It is *inferred*, not measured.
  The revision now says so rather than asserting it.
- **Not established: the L455 "obtained twice" claim**, in either direction.
- **Not established: that the other §5.1 independence claims hold.** Item 5
  restates every one of them to its measured basis, but only Method B's was
  actually tested (by CT-S54).
- **Not established: that CT-S54's `FOLLOWUP-EMAIL.md` section numbers are
  right.** This session verified the numbers *it* uses; the email was not
  re-checked against v1.2.
- **Not checked this session: the companion's v1.3 version DOI**
  `10.5281/zenodo.22831933` under concept `20455089`. Inherited from CT-S52 and
  not confirmed against the API. *A concept DOI is not a version DOI* — the
  distinction has bitten this corpus before.

---

## 7. Open questions for the operator

1. **The source of the submitted paper is not under version control.** Three of
   four published versions were built from uncommitted scratch directories. Any
   of them could be deleted without trace. **Ruling 3 applied**: v1.2's source
   is now copied to `submitted-source/MATH-D-26-00523/` with a content-derived
   marker (S56-22). v1.1 and v1.3's sources remain outside the tree — should
   they be imported too?
2. **The revision's wording will not match the published v1.3.** v1.3 already
   covers items 1 and 2, in *different words*, and covers neither 3, 4 nor 5.
   The cover letter promised deposit and submission would be identical. Keeping
   that promise means depositing a new version of concept `20719042` matching
   whatever the editor accepts — **ruling 2: nothing is deposited until the
   editor replies.**
3. **L455's "obtained twice" — ruled into item 4 and edited** (S56-20). No
   sixth correction is needed and none was sent.
4. **Two papers each have a v1.3 — now settled.** This paper: concept
   `20719042`. The companion: concept `20455089`. The new reference cites the
   **companion's** v1.3, confirmed against the Zenodo API, with the concept DOI
   read from the response's own `conceptdoi` field and this paper's own v1.3
   checked for and absent (S56-24). **Closed.**
5. **Both correction emails were sent on 2026-09-21**, and the revision has been
   audited against the second one as sent (§5a). The **first** email is now
   recorded in `sessions/2026-09-17/CT-S57-EMAILS-RECORD/` — 5 INSPECTED claims,
   with Zenodo confirming no version published after the send date. Its
   recorder settled the standing question: **item 4 went out UNRESOLVED, with
   both bracketed alternatives present**, one of which — "the Frobenius
   solutions at ξ = 0 carry no logarithmic terms" — is now known to be false.
   The second email resolves it, so no further message is needed; but the
   **follow-up's verbatim text still has to be pasted** before it can be
   recorded alongside the first. It will not be reconstructed from memory.
6. **The end-to-end read is still outstanding**, and it is the last thing
   between this revision and being genuinely ready. §5 and Table 2 are the
   places to read hardest: they were rewritten against a finding that the
   section's central claim was one comparison printed twice, and prose drafted
   against a correction list goes wrong exactly there. The L455 replacement is
   new prose written this session and has never been read in rendered form.

---

## 8. Uncommitted files

All under `sessions/2026-09-17/CT-S56-REBASE-V12/` **except** the new
`submitted-source/MATH-D-26-00523/` at the repository root, which is outside the
session folder at the operator's explicit instruction (ruling 3).

**Deliverables**
```
revision/vquad-periodrep-paper.tex      97567 B
revision/vquad-periodrep-paper.pdf     796498 B, 27 pages
revision/{preamble.tex, build.py}
CHANGES.md
CORRECTIONS-FOR-REFEREES.md
claims.jsonl                            24 claims
PREREG.md                               incl. §12a Amendment 1
REPORT.md                               this file
```

**Repository record (outside the session folder)**
```
submitted-source/MATH-D-26-00523/       7 files + README.md marker
```

**Scripts** — `locate_source.py`, `version_diff.py`, `apply_revision_v12.py`,
`build_check.py`, `render_diff.py`, `locate_numbering.py`, `make_docs.py`,
`sweep.py`, `sweep_compare.py`, `pattern_drift.py`, `email_coverage.py`,
`home_for_s56_01.py`, `verify_companion_doi.py`, `verify_unchanged.py`,
`emit_claims_s56.py`, `mutants_s56.py`, `verify_claims.py`

**Outputs** — in `outputs/`, including the three version patches, the full
rendered diff, and `_orig_before.bak` (the original inline before-sweep, kept as
the independent witness that `sweep.py` reproduces it byte for byte).

**References** — `refs/zenodo-v1.{0,1,2,3}-*.pdf` (md5-verified) and
`refs/src-v1.{0,1,2,3}/` (copies; the originals were not modified).

---

## 9. Re-run order

```
locate_source.py → version_diff.py → apply_revision_v12.py → build_check.py
→ render_diff.py → locate_numbering.py → make_docs.py
→ sweep.py before → sweep.py after → sweep_compare.py → pattern_drift.py
→ email_coverage.py → home_for_s56_01.py → verify_companion_doi.py
→ verify_unchanged.py
→ mutants_s56.py → emit_claims_s56.py → verify_claims.py
```

`verify_companion_doi.py` queries Zenodo and **refuses** if it cannot reach it,
rather than recording an unchecked citation as a checked one. Zenodo returned
HTTP 504 for roughly ten minutes during this session; that is a refusal, not a
pass.

`emit_claims_s56.py` must run **after** every script that writes an output, and
`verify_claims.py` last. Running them out of order leaves claims citing hashes
that no longer exist — which `verify_claims.py` will catch, and did.

**Deletions are writes too.** Finding (h) happened because a tidy-up ran after
the observation and before the claim. Anything that removes a file belongs at
the *start* of this list, never at the end.
