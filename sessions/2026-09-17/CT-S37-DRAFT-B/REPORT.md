# REPORT — CT-S37-DRAFT-B

**Group B of the CT-S37 drafting job: §3 local data, §4 the moduli space and
its hypotheses.** Draft only. Nothing committed, pushed, tagged, deposited or
submitted. No network call was made. No file outside
`sessions/2026-09-17/CT-S37-DRAFT-B/` was created or modified.

---

## 1. What was done

1. Built `scripts/claim_index.py`, a corpus-wide index over every
   `claims.jsonl` under `sessions/` — 449 files, 1384 unique claim ids after
   this session's own emission. It resolves ids, reports duplicates, and
   distinguishes structured supersession from free-text mentions of it.
2. Retrieved the **current** label of every claim `OUTLINE.md` revision 6 cites
   for §3 and §4, plus the printed forms of van der Put–Saito's family `(4.1)`,
   flow `(4.4)` and Hamiltonian `H_V` `(4.5)`. No label and no formula in the
   drafts was written from memory or from a prior draft.
3. Drafted **`section3.tex`** (12 978 B, 7 subsections, 45 citations) and
   **`section4.tex`** (9 221 B, 7 subsections, 12 citations) as paper prose.
4. Built the failure-capable check `scripts/draft_check.py` and its control
   suite `scripts/mutants_draft_check.py`.
5. Verified a standalone LaTeX build of §1 + §3 + §4.
6. Emitted 12 claims and verified every cited digest resolves on disk and that
   the gate outputs reproduce the bytes the claims cite.

### Verdict lines

```
draft_check.py            VERDICT: PASS      57 citations, 57 OK, 0 UNRESOLVED, 0 SUPERSEDED, 0 MISMATCH
mutants_draft_check.py    9/9 arms CAUGHT
pdflatex (two passes)     exit 0, 10 pages, no undefined references, no warnings
verify_claim_digests.py   VERDICT: PASS (0 problems)
```

---

## 2. Claims, each with its label

| id | label | what it records |
|---|---|---|
| S37B-01 | STRUCTURAL | §3 drafted; every value carries its claim id |
| S37B-02 | STRUCTURAL | §4 drafted; repair **R-(c)** discharged — `(4.1)`, `(4.4)`, `(4.5)` printed, not cited |
| S37B-03 | VERIFIED | the draft check passes, 57/57 |
| S37B-04 | VERIFIED | 9/9 mutant arms caught, each for the stated reason |
| S37B-05 | VERIFIED | **defect in the checker**: the id regex silently dropped 11 citations |
| S37B-06 | STRUCTURAL | a pre-registered threshold proved ill-posed; narrowed, disclosed, boundary mutant added |
| S37B-07 | VERIFIED | `OUTLINE.md`'s `S9-PVPARAMS-*` ids do not literally resolve |
| S37B-08 | VERIFIED | the standalone build compiles clean at 10 pages |
| S37B-09 | VERIFIED | Group A is undrafted; the task's premise is unmet |
| S37B-10 | VERIFIED | corpus parse noise is pre-existing and out of scope |
| S37B-11 | STRUCTURAL | the corpus label vocabulary includes `INSPECTED` beyond P0's four |
| S37B-12 | STRUCTURAL | a rule in the prompt conflicts with the corpus; the corpus wins |

`claims.jsonl` — 12 claims, 10 499 B, sha256
`2ac82503e4a622f8e9af5e2c19ea0c18038d935fc409c29464bee09c5085571e`.

---

## 3. Three defects, and how each was found

### 3.1 The checker silently examined 46 of 57 citations (S37B-05)

The first claim-id pattern was

```
(?:CT-)?S\d+[A-Z]*-[A-Z]*\d+(?:-[A-Z]+\d+)*
```

which requires every segment to end in digits. `CT-S9-PVPARAMS-C005` has the
segment `PVPARAMS`, which does not. **Every** `CT-S9-PVPARAMS-*` citation —
eight in §3, three in §4 — was dropped before any label was compared. The
check would have printed `VERDICT: PASS` on 46 citations while reporting the
same words it prints on 57.

It was not found by reading the regex. It was found because the
reader-integrity bound fired and the pair counts were printed and read: 37 and
9, where the prose visibly contains more. After the repair the counts moved to
45 and 12, and that movement is the evidence that the repair changed what is
examined rather than only what is reported.

This is the same family as CT-S35's `re.sub(r"<[^>]+>", " ", t)`: a reader
whose defect is invisible in its own output.

### 3.2 A pre-registered threshold that fired on correct prose (S37B-06)

`PREREG.md` set the reader-integrity non-vacuity bound at ≥ 15 (id, label)
pairs per file. `section4.tex` correctly carries 12 — §4 is a reading section
resting on nine distinct claims, three cited more than once. The bound fired on
prose that was right.

That is a bound behaving as a fingerprint, which is exactly what a non-vacuity
bound must not do: its job is to separate an empty or undecodable read from a
real one, not to encode a guess at how many citations a section ought to have.

Handling, recorded as an amendment in `PREREG.md` and not presented as the
original design: narrowed to ≥ 5 per file plus a new group bound of ≥ 30, with
**boundary mutant M9 added in the same edit** — it reduces `section4.tex` to
exactly four citations while leaving byte count and subsection count untouched,
so only the narrowed bound can fire. M9 is CAUGHT. The falsifier was not
touched.

### 3.3 The mutant harness died before judging anything

The first run of `mutants_draft_check.py` crashed in `re.sub` — a Windows
absolute path used as a replacement string, so `\L` was read as a bad escape.
Repaired with a lambda replacement and an assertion that the `ROOT` block was
found before substitution. The harness also **pins** `claim_index.ROOT` to the
real `sessions/` directory in each copied tree, because the copy's
`__file__`-derived path resolves into the temp directory; without the pin every
arm dies before executing a single comparison and a two-condition harness would
have reported 9/9 CAUGHT on nine crashes. The arm scorer therefore rejects any
output containing `Traceback`, `SyntaxError` or `NameError`.

---

## 4. Findings about the inputs, reported not repaired

- **`OUTLINE.md` cites claim ids that do not resolve (S37B-07).** It uses
  `S9-PVPARAMS-C002 … C012`; the corpus ids are `CT-S9-PVPARAMS-C001 … C014`.
  The drafts use the corpus form, so no citation in them needs the alias. The
  checker implements the `CT-` alias and **reports** any use of it; mutant arm
  M7 requires the alias form both to resolve and to be reported.

- **`OUTLINE.md` §3's cross-reference looks stale.** Its note reads "the errata
  history does not — see §4", but §4 in revision 6 is the moduli space. The
  literal instruction was followed — errata history is kept out of §3 — and the
  pointer is flagged. The errata history plausibly belongs to §9 Scope and
  limits.

- **Group A is undrafted (S37B-09).** No `CT-S37-*` folder other than this one
  exists, and the only drafted section in the corpus is CT-S36's
  `section1.tex`. §3 and §4 do not depend on Group A, so Group B was drafted as
  instructed; but the §2.0 attribution paragraph that the prompt calls
  load-bearing does not yet exist to be cited from here.

- **Corpus parse noise is pre-existing (S37B-10).** 46 unparseable lines,
  confined to three 2026-04/2026-05 sessions, and 84 duplicate bare ids
  (`C1…C9` reused across 2026-05 sessions and `CT-S15-COLDREAD-DEFERRED`). All
  predate every `CT-S*` session; none of the affected ids is cited by the
  drafts. Reading `claims.jsonl` as `utf-8-sig` rather than `utf-8` was
  required and removed the largest parse-failure class.

- **The label vocabulary is wider than P0's four (S37B-11).** The corpus uses
  `INSPECTED` for a reading of a printed page, and eight of the 57 citations
  carry it. The prose carries it as-is; the checker's vocabulary includes it so
  that promoting it is a `MISMATCH`, which mutant arm M2 exercises on exactly
  the P0-forbidden upgrade `INSPECTED → PROVEN`.

- **A rule in the prompt conflicts with the corpus, and the corpus wins
  (S37B-12).** The prompt directs that exclusions be VERIFIED and row matches
  STRUCTURAL. In the corpus, both the exclusion `S6-C7` and the match `S6-C16`
  carry **STRUCTURAL**. The prompt's governing rule — check each cited id's
  current label before writing the sentence, not from memory — was followed, so
  the prose says STRUCTURAL for both. No corpus label was changed to fit a
  drafting rule.

---

## 5. What was NOT established

- **No mathematics was re-derived.** Every value in §3 and §4 is transcribed
  from a corpus claim, and the check verifies the transcription of ids and
  labels only. It does **not** verify that a quoted formula matches the claim
  text; a transposed digit inside `\begin{equation}` would pass. That is a real
  gap and it is stated rather than papered over.
- **§4's printed `(4.5)`** is transcribed from
  `CT-S16-MEMBERSHIP-C/flow_regularity.py`, the corpus script that computes
  with it, which is the record of the page-image reading `S16-03`. It was not
  re-read from the page image in this session.
- **Membership is not proven.** §4 closes by pointing at `S16-14`, which is
  **STRUCTURAL**, and states expressly that the pre-registered
  monodromy-and-Stokes falsifier at 30 digits was not run.
- **Global equivalence of `A` and `B` is not established.** §3 claims the local
  statement (`S5B-C8`) and explicitly not the global one (`S5B-C9`,
  `S5B-C10`).
- **No Painlevé label is assigned** to any object in these two sections. A
  matching Katz multiset is recorded as a necessary condition only
  (`S6-C10`), and `Remark 3.1` says so in the text.
- **Groups A, C, D and E were not drafted**, and no section outside Group B was
  renumbered or edited.

---

## 6. Open questions for the operator

1. **Group A ordering.** §3 opens on `b(n)=3n²+n+1` and §4 on a type-`(0,0,1)`
   module, both of which the undrafted §0/§2 are expected to introduce. Should
   Group A be run before these drafts are considered stable?
2. **Whether the check should verify formulae, not only citations.** Extending
   it to compare each displayed equation against the claim text is possible but
   is a different instrument, and it would have to be mutant-tested on its own
   terms.
3. **`OUTLINE.md`'s two defects** — the `S9-PVPARAMS` alias and the stale §3→§4
   errata pointer. Repairing `OUTLINE.md` means editing an earlier session's
   file, which P0 forbids without instruction.
4. **§1's renaming.** CT-S36's `section1.tex` renames the three `r`-objects; §3
   and §4 follow §1's notation, but that renaming is itself unruled. Confirm or
   overturn before the group is carried forward.
5. **Whether `INSPECTED` should be added to P0's label list**, since the corpus
   has used it consistently and the drafts now carry it into paper prose.

---

## 7. Uncommitted files

All are new; nothing in any earlier session was modified. `git status` reports
this directory as a single untracked path.

```
sessions/2026-09-17/CT-S37-DRAFT-B/
  PREREG.md                                7 212 B
  REPORT.md                                this file
  claims.jsonl                            10 499 B   2ac82503e4a622f8
  section3.tex                            12 978 B   8a9d7a3ef216decc
  section4.tex                             9 221 B   315e2a30d683540b
  groupB_standalone.tex                       381 B
  groupB_standalone.pdf                  411 561 B   524ef2462cab2d38
  groupB_standalone.{aux,log,out}                    build by-products
  refs/section1.tex                       13 660 B   39ddd724524f2a7e  (unmodified copy of CT-S36's)
  scripts/claim_index.py                   3 791 B
  scripts/draft_check.py                   9 113 B
  scripts/mutants_draft_check.py           5 897 B
  scripts/emit_claims_s37b.py             11 914 B
  scripts/verify_claim_digests.py          2 592 B
  outputs/draft_check.out.txt              5 668 B   8d1c9e74d824b8a4
  outputs/mutants_draft_check.out.txt        725 B   88abafcde172c1a4
  outputs/verify_claim_digests.out.txt     1 076 B
  outputs/build1.out.txt, build2.out.txt             pdflatex logs
  outputs/claim_index_all.out.txt and 8 further claims_*.out.txt   input retrieval
```

`scripts/__pycache__/` is a Python by-product and carries no content.
