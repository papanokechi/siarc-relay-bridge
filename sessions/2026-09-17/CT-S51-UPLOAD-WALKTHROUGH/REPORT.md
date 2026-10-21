# REPORT — CT-S51-UPLOAD-WALKTHROUGH

**Read-only session. Nothing was uploaded, deposited, submitted, published or
edited outside this folder.**

## 0. Result

```
SOURCE     arXiv .tex unchanged and certifiable: 87778 B, self-contained, no identity or venue leak
ZENODO     record 20719043 is PUBLISHED (2026-06-16) -- the deposit is DONE, not pending
ARXIV      not submitted; no arXiv ID exists in the repository
GATE       17 checks, 2 FINDINGS; 5 controls, 5 FIRED
```

The task was to help with upload walkthroughs. The first thing a walkthrough
has to get right is **which uploads are still uploads** — and one of the two
had already happened.

---

## 1. The state correction

`sessions/2026-06-16/VQUAD-ZENODO-DEPOSIT-001/handoff.md` reads *"HELD at
Gate 0 … upload-ready … the manual upload may now proceed"*. A live API
snapshot shows record `20719043` with `state=done`, `submitted=true`,
published **2026-06-16**, carrying both files, all eleven related identifiers,
CC BY 4.0 and the ORCID — every value the June session prepared.

The deposit was executed. The handoff was never updated after it, so **a
document in the tree still instructs the operator to perform a completed
irreversible action**. Under the append-only rule the June session is not
edited; `STATE.md` is the correction and `S51-02` the claim.

This is the reason the session exists in the form it does: a walkthrough
written from the stored runbooks alone would have walked into a second deposit.

## 2. The blocking finding — a hedge applied to the metadata and not the paper

The gate compared the abstract **inside the file that would be uploaded** with
the abstract **the operator would type into the form**. They differ.

| | |
|---|---|
| `.tex`, and the published Zenodo description | "the rank-one standalone closure **on the Sakai surface** $D_5^{(1)}$" |
| arXiv metadata package, hedge-fixed 2026-09-13 | "the rank-one standalone closure, **whose Sakai surface type is conjectured to be** $D_5^{(1)}$" |

Check `C2b` makes the relationship decidable rather than approximate: delete
the hedge clause from the package text, restore the flat clause, and the two
abstracts become **byte-identical**. So this is not transcription drift. It is
one deliberate change of epistemic force, applied to the metadata and not to
the manuscript.

**The corpus supports the hedge.** `S4-01` records that the V_quad companion's
own **v1.2 renamed object 4.1 from a theorem to "Conjecture 4.1, Painlevé V
(D₅⁽¹⁾) classification"**, and `S4-09` records this programme's verdict on the
attribution as **(c) INCONCLUSIVE**. Both literals are echoed into the evidence
file rather than merely asserted, so the finding can be audited without
re-running anything.

Consequences, stated plainly because the operator has to choose:

- Submitting the source as it stands puts the **flat claim** into a permanent
  public record, under CC BY, where it says the surface **is** $D_5^{(1)}$.
- Typing the hedged abstract over that source makes the arXiv abstract and the
  arXiv-hosted PDF **disagree in public** about whether the result is proved.
- The already-published Zenodo description carries the flat claim today, having
  been published three months before the hedge fix.

The three options are set out in `WALKTHROUGH-ARXIV.md` §2. The recommendation
is to amend the manuscript and the deposit description to the supported
wording, but the ruling is the operator's and nothing was changed here.

## 3. Why no instrument caught it before

`S51-05`. Every gate this programme has built asks whether a document is **the
one intended** — digests, page counts, undefined references, resolving
citations, snapshot guards. None asks whether what the document **asserts**
matches the **label its own record assigns**. The two abstracts have always
hashed differently, and that difference was never a defect until someone asked
what the words meant.

It is the same shape as `S50-11`, one level up: there, a check could not see a
defect because it read the source and the defect lived in the rendering. Here,
a check cannot see a defect because it reads the bytes and the defect lives in
the epistemic force of the prose.

`WALKTHROUGH-ZENODO.md` Stage 1 carries the resulting rule as a pre-publish
gate: read what you are about to publish and check each claim's force against
its corpus label.

## 4. The ill-posed check, reported not retuned

Pre-registered check `C2` asked whether the abstracts differ in exactly **one
region**, treating a diff region as a semantic change. An adjacent replacement
plus insertion is one hedge but two opcodes, so it reported *2 regions, 1
carrying a hedge* and **failed on a correct artefact**.

Per PREREG F4 it was not retuned. It stands in the script, still failing, and
is replaced by `C2b`, which asks the decidable question. `S51-06` records it.
This is the ill-posed-threshold rule again: a bound that can be tuned to either
answer is measuring the wrong thing.

## 5. The runner kit

`S51-07`. The June Zenodo runbook drives the deposit through
`run_sandbox_draft.py`, `run_production_draft.py`, `_zenodo_uploader.py`,
`set_prod_token.ps1` and `check_prod_token.ps1`. A recursive search finds **none
of them in this repository**.

Stated precisely, because the distinction has cost this programme before: that
establishes absence **from the worktree**, not that the kit does not exist —
prior sessions have stored material outside the tree. `WALKTHROUGH-ZENODO.md` is
therefore written for the web UI, which needs no kit, and names the runner
route as the better one if the operator still holds it.

## 6. Claims

| id | label | subject |
|---|---|---|
| `S51-01` | `INSPECTED` | the arXiv source is unchanged, self-contained and leak-free |
| `S51-02` | `INSPECTED` | the Zenodo deposit is done; the June handoff is stale |
| `S51-03` | `VERIFIED` | the two abstracts differ, and `C2b` confines the difference to the hedge |
| `S51-04` | `INSPECTED` | the corpus labels the attribution conjectural; the manuscript does not |
| `S51-05` | `STRUCTURAL` | an epistemic-status defect is invisible to every instrument here |
| `S51-06` | `INSPECTED` | `C2` is ill-posed; reported, replaced by `C2b`, left failing |
| `S51-07` | `INSPECTED` | the runner kit is absent from the worktree, which is not absence |
| `S51-08` | `INSPECTED` | a sibling marker written beside the stale June handoff, under amendment G |

## 7. What was NOT established

- **Whether the manuscript body repeats the flat claim.** The comparison covers
  the **abstract only**. If the operator amends it, Amendment H applies: sweep
  the body first and report the result either way.
- **Whether Zenodo currently permits a description edit without a new version.**
  Stated in the walkthrough as "confirm in the UI", not asserted.
- **No mathematics was checked.** Nothing here bears on whether the Sakai
  attribution is true — only on which label the record gives it.
- **The Painlevé V paper's venue** is untouched and deliberately out of scope.

## 8. Open questions for the operator

1. **The §2 ruling — A, B or C.** Blocking; the submission should not proceed
   until it is made.
2. **If A: does the Zenodo description get corrected too?** The deposit is
   public and currently carries the flat claim.

The third item raised in drafting — whether the stale June handoff should carry
a pointer — was not left open. Amendment G's bar is **demonstrated harm**, and a
handoff that instructs the operator to repeat a completed irreversible action
meets it, so the marker was written: §5a below.

## 5a. The sibling marker

`sessions/2026-06-16/VQUAD-ZENODO-DEPOSIT-001/AAA-READ-FIRST-PUBLISHED.md`,
recorded as `S51-08`. It states that the record is published, gives both DOIs
and the record's contents, and rules that `handoff.md` and `operator-runbook.md`
are the record of **how the deposit was prepared** and **not live
instructions**. It is an addition: nothing in that folder was edited and no
digest moved — the same construction as `supersedes` for claims.

The emitter refuses to write `S51-08` unless the marker exists, carries the
record number, the concept DOI, the words `PUBLISHED`, `not as live
instructions` and `amendment G`, **and** the two files it warns about are still
present. That last one matters: a marker warning about documents that are no
longer there would mean the folder had been edited after all.

It fired on the first run — the marker said "do not follow them as live
instructions" while the claim said "not as live instructions", and the check
would not accept a paraphrase. The marker was reworded to say what the claim
says, rather than the assertion weakened to accept what the marker said.

## 9. Uncommitted files

All new. One file was created **outside** this folder — the sibling marker
(§5a), an addition under amendment G. **No pre-existing file anywhere was
modified.**

```
sessions/2026-09-17/CT-S51-UPLOAD-WALKTHROUGH/
  PREREG.md   REPORT.md   STATE.md   claims.jsonl        8 claims
  WALKTHROUGH-ARXIV.md              the pending upload, step by step
  WALKTHROUGH-ZENODO.md             reusable; no deposit authorised
  scripts/check_upload_ready.py     the gate (read-only)
  scripts/emit_claims_s51.py        validates its buffer before writing
  refs/arxiv-metadata-package.md    copied, unmodified
  refs/arxiv-source-inventory.md    copied, unmodified
  outputs/check_upload_ready.out.txt
  outputs/zenodo_20719043.json      live API snapshot, 2026-09-21
```

Controls on the emitter, run in a scratch tree at repo-relative depth: baseline
**writes 8**; an unpublished record, a missing `C2b`, and a dead control each
**refuse at exit 2 for exactly the injected reason**; restored, it writes again.
The live `claims.jsonl` was byte-identical throughout.

One file was added **outside** this folder: the sibling marker in §5a. It is an
addition under amendment G, not an edit; every pre-existing file in that
directory is untouched.
