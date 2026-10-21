# REPORT — CT-S40-DRAFT-B-RERUN (Group B re-run, alias removal, assembly)

**Session:** `sessions/2026-09-17/CT-S40-DRAFT-B-RERUN/`
**Status:** draft only. Nothing committed, pushed, tagged or deposited. No network call.
**Gates:** `draft_check` 57/57 citations, 0 problems, **12/12 arms**;
`check_assembly` 4 rules, 0 failures, **7/7 arms**.
**Build:** sections 0–4 combined — **15 pages, 0 errors, 0 undefined, 0 multiply-defined.**

---

## 1. What was done

The three carried actions of `S39-08`, plus the re-run they belonged to:

| action | state |
|---|---|
| drop the `CT-` prefix alias from `draft_check.py` | done |
| invert mutant `M7` — the bare short form must now fail | done, CAUGHT |
| correct the false `NOTE` at `draft_check.py:195–196` | replaced by a **check** |
| re-run Group B's check with §2 present | done, PASS |

CT-S37-DRAFT-B is **not edited**. Its `claims.jsonl` cites the digest of its own
`draft_check.out.txt`, so the scripts were copied here and amended in the copy —
the same reasoning that left the alias alone until the ruling.

The `NOTE` was not simply deleted. It asserted a fact about `OUTLINE.md` that
CT-S38 had already made false. Its replacement resolves the same question
**positively against the outline itself**, with `M11` reverting the outline to
fire it. A remembered fact became a check.

## 2. The finding: a label mismatch neither prior gate could see (`S40-02`)

Sections 0 and 2 reference `sec:local` at three places. Section 3 defines
itself as `sec:systems`, and section 4 already references `sec:systems`.

Both prior gates were green throughout:

- **Group A** built §0–§2 with `forwardrefs.tex`, which **declared** `sec:local`.
  The stub manufactured a target that no section defines, so the build
  reported 0 undefined references.
- **Group B** built §3–§4, which never reference §3 from outside. No symptom
  there either.

The defect has **no external symptom** — not in page count, not in a rendered
diff, not in either build. It appears only on assembly, and only if the stub is
forbidden from standing in for a section that exists. Confirmed by building
§0–§4 together *before* any repair: exactly **three** undefined references, all
to `sec:local`, and nothing else.

`check_group_a.py`'s `F7` was not wrong. It checked the stub's **numbers**
against `OUTLINE.md`'s headings, which is all it could do while §3 did not
exist. What it could not check is the one thing that mattered: the **label
name** against the section that would eventually define it.

**Repaired** in this session's copies by renaming the three references to
`sec:systems` — the definer wins, and §4 already agreed. `check_assembly.py`
now encodes the general rule (**R2**: a stub may declare only labels for
sections that do not exist), with `A1` reinstating this exact defect and `A2`
its cause.

**A second assembly-only defect** surfaced in the same build (`S40-06`): the
first combined run aborted on `! Undefined control sequence`, because §3 and §4
use `\texorpdfstring` and Group A's wrapper does not load `hyperref` while
Group B's does. Two standalone builds, each correct, that cannot be
concatenated.

## 3. Scope defect in an adopted P0 amendment (`S40-04`) — **needs a ruling**

`draft_check.py` reported `corpus: 451 claims.jsonl files, 1411 unique claim
ids`. `S38-17` reported **35 files, 649 lines** and concluded that the five
labels *partition the corpus, "so there is no sixth label"*. You adopted the
stronger phrasing on that basis.

`label_census.py` is honest: it prints `root: ...\sessions\2026-09-17`. But
`draft_check.py` walks **all** of `sessions/`. **The word "corpus" denotes two
different sets in two checks of the same run**, and the conclusion drawn from
the narrower one is stated about the wider.

Over the full tree the five do **not** partition:

| label | count | |
|---|---:|---|
| INSPECTED | 218 | |
| VERIFIED | 186 | |
| PROVEN | 140 | |
| STRUCTURAL | 126 | |
| **PROCEED** | **14** | **outside the five** |
| CONJECTURED | 6 | |
| **REFINED** | **1** | **outside the five** |

and **3 458 of 4 195 claim lines carry no `label` field at all.**

Verified by two differently-implemented readers before reporting — `pathlib.
rglob` + `json.loads`, and `os.walk` + a raw-bytes regex — which agree on 451
files, 4 195 lines and every count above, and resolve to named `file:line`
locations. The raw line at
`2026-05-13/T1-SYNTH-VERDICT-212-.../claims.jsonl:1` reads
`"label": "PROCEED"` beside `lock`, `band` and `confidence` fields: **a
different claim schema from a different workstream.** The second reader also
found four further verdict-style values on lines the JSON reader could not
parse.

So the amendment's **substance holds** for the Channel Theory working corpus.
What is wrong is the unqualified word *"corpus"* in a governance document whose
whole force is that the list is **closed**.

**Ruled 2026-09-20: rewrite, not supersede** — F is a standing rule rather than
a claim, and its digest is cited by no claim, which was checked before editing.
`P0-AMENDMENT-F-LABELS.md` now carries a **Scope** section defining "corpus" as
`sessions/2026-09-17/`, stating the 451/4 195/3 458/15 figures for the wider
tree, and restating check **C4** as partitioning the *Channel Theory* corpus
rather than "anywhere". Nothing is relabelled; the out-of-five values remain a
different vocabulary in a different system, not a sixth epistemic label.
Recorded as `S40-11`.

## 4. The re-run's stated blocker did not bind — a correction (`S40-05`)

Measured rather than assumed. Sections 3 and 4 depend on section 2 **neither by
cross-reference nor by name**: 0 labels borrowed from §2, 0 references to
`sec:growth`. The single label they borrow from outside themselves is
`eq:n-rec`, from §1.

The commissioning premise — that §3 and §4 *"cite a section that isn't there"* —
was therefore **wrong**, and the operator has recorded the correction rather
than the conclusion. Group A was nonetheless the right thing to draft first,
for a different reason: **§2.0 is the paper's most citation-dense paragraph**
and had to exist before anything leaned on its attribution.

The re-run's value lies in the repaired §1 and in the assembly check — neither
of which was the reason it was commissioned.

## 5. Group B was checked against a §1 that no longer exists (`S40-03`)

`CT-S37-DRAFT-B/refs/section1.tex` is the **pre-CT-S38** copy: 13 660 B against
14 325 B, differing in the ψ/ν re-lettering, the rewritten ρ sentence, and the
new `s`/`s_±` and `P,Q`/`Q_n` paragraphs.

The guard asserts the right input **positively and two-sided**, per `S38-07`:
three pre-repair markers must be present in the retained CT-S37 snapshot and
absent from the live file, five repair markers the reverse. All eight resolve.

**The guard was itself defective twice, and both were repaired before the
result was reported:**

1. It was **one-sided** — it tested only the live file, so it could not
   distinguish "the repair landed" from "the snapshot is not what it is named
   for".
2. Its needle **spanned a line break** in the source (`The letter $\rho$ is
   never used\nfor anything else`), so a raw containment test reported a **false
   absence on correct text** — the same failure as CT-S39's `F6c`, and the same
   family as CT-S27 and CT-S35. Matching is now on whitespace-squashed text.

The first run printed `present: False (stale copy: False)` — a marker found in
*neither* file, which is a reader that sees nothing reporting it as a clean
result. Arm `M12` now stages the stale copy and is CAUGHT.

## 6. The alias was already dead code

Worth stating plainly, because it changes what the removal means: **no citation
in §3 or §4 needed the alias.** Every id is cited in the corpus form. It was
dead when CT-S37 retained it, and its removal is a no-op on this prose. What
the removal buys is the **inverted `M7`** — the bare form is now refused rather
than quietly normalised — and that arm is the whole point.

## 7. Claims

| id | label | subject |
|---|---|---|
| `S40-01` | VERIFIED | Group B re-checked; 57/57; alias retired; 12/12 arms |
| `S40-02` | VERIFIED | the `sec:local`/`sec:systems` assembly defect and its rule |
| `S40-03` | VERIFIED | Group B was checked against a stale §1; two-sided guard |
| `S40-04` | INSPECTED | scope defect in P0 amendment F |
| `S40-05` | INSPECTED | **correction**: the stated blocker did not bind |
| `S40-06` | VERIFIED | combined build 15 pages, 0 undefined; the hyperref defect |
| `S40-07` | INSPECTED | CT-S39 originals still carry `sec:local` |
| `S40-08` | VERIFIED | control coverage, 12/12 and 7/7, three-condition scoring |
| `S40-09` | VERIFIED | **supersedes `S39-07`** — the stub declared a label no section defines |
| `S40-10` | INSPECTED | **supersedes `S1-04`** as to claim text only; label PROVEN undisturbed |
| `S40-11` | INSPECTED | P0 amendment F's scope clause rewritten |

## 7a. The operator's rulings of 2026-09-20, as applied

> *Editing a session whose digests are cited breaks the digests, and the run
> has already established that append-only is the rule.*

| item | disposition |
|---|---|
| `sec:local` upstream in CT-S39 | **not edited.** Superseded by `S40-09`; repaired files live here and the assembly builds from them |
| `S1-04`'s stale claim text | **not edited.** Superseded by `S40-10`, the R20 precedent; the label `PROVEN` is untouched |
| Amendment F's wording | **rewritten in place** — F is a standing rule, not a claim. Its digest was confirmed **cited by no claim** before the edit |

Three pre-write checks now enforce the form: a `supersedes` field must be
**named in its own claim text**, the claim must **lead with `SUPERSEDES`**, and
the superseded id must **resolve in the corpus**. A supersession the text does
not name is a silent retraction, and the emitter refuses it.

**Verified after the fact, not assumed:** `supersedes: S1-04` marks S1-04
superseded corpus-wide, and §2 cites S1-04. Both gates were re-run — CT-S39's
`check_group_a` remains **invariant and green**, still resolving
`S1-04 -> PROVEN`, and CT-S40's `draft_check` reports `SUPERSEDED: 0` and is
invariant. Superseding the **text** while leaving the **label** is exactly what
lets that hold.

## 8. Gate invariance

Both gates were re-run **after** emission and compared byte-for-byte:
`draft_check` **invariant: True**, `check_assembly` **invariant: True**, all 8
cited digests resolve on disk. `claim_index.corpus_files()` excludes this
session's own `claims.jsonl` by construction, asserted non-vacuously by `C6`
(the file must **exist** and be **absent** from the walk). The emission
procedure is three-pass and documented in the emitter's own docstring, because
`draft_check`'s self-exclusion line changes the first time `claims.jsonl`
exists.

## 9. What was NOT established

- **No formula in §3 or §4 was re-derived.** The gate verifies ids, labels and
  label assembly. A transposed digit inside an equation passes everything here.
  Pre-registered as a known limit (PREREG §7), unchanged since CT-S37.
- **§3 and §4 were not rewritten.** They are byte-identical copies of CT-S37's.
- **Nothing was relabelled** to fit a prose rule.
- **The `sec:local` repair is not upstream.** Only this session's copies carry it.

## 10. Open questions for the operator

All three items raised by this session were **ruled on 2026-09-20** and applied
as recorded in §7a. Nothing is outstanding. One observation carried forward:

- **Which wrapper is authoritative?** The combined build needs `hyperref`; the
  group wrappers disagree. Worth fixing once, at assembly, rather than per
  group.

## 11. Uncommitted files

New in `sessions/2026-09-17/CT-S40-DRAFT-B-RERUN/`:

```
PREREG.md   REPORT.md   claims.jsonl (8 claims)
combined_0to4.tex   forwardrefs_CDE.tex
section3.tex  section4.tex          (unmodified copies from CT-S37)
refs/section0.tex  refs/section2.tex (copies, sec:local -> sec:systems)
refs/section1.tex                    (repaired copy, from CT-S39)
refs/section1.CT-S37.tex             (the stale snapshot, retained as evidence)
scripts/draft_check.py     scripts/claim_index.py
scripts/check_assembly.py  scripts/mutants_assembly.py
scripts/mutants_draft_check.py  scripts/emit_claims_s40.py
scripts/verify_claim_digests.py
outputs/  (gate outputs, both mutant suites, build_before/, build_after/)
```

**No file outside this session folder was modified.** Nothing was committed.

## 12. Next

Groups **C**, **D**, **E** are unblocked. Two standing items now apply to them:

- `check_assembly.py` should be re-run as each group lands — it is the only
  gate that sees cross-section defects, and it found two in its first run.
- The stub must shrink as sections appear. `R2` enforces that automatically:
  a stub entry for a section that now exists is a failure, not a leftover.
