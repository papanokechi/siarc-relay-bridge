# CT-S35-CTV17-ITEM6 — REPORT

**Session:** `sessions/2026-09-17/CT-S35-CTV17-ITEM6/`
**Scope:** draft only. No deposit, no upload, no metadata edit, nothing committed.
**Record:** Channel Theory, concept DOI `10.5281/zenodo.19941678`; current
version v1.6 = `10.5281/zenodo.22782807`. v1.7 is a **description-only** new
version, as ruled.

---

## 1. What was done

The sixth item of the v1.7 notice was **rewritten to the respecified form** and
is now §7 of `NOTICE-v1.7-rev3.md`. The respecified Tier 1 argument is strictly
stronger than the one CT-S27 drafted and was adopted in full:

> At `z = 0` the Newton polygon gives Katz invariant `1/2` for **every**
> admissible coefficient vector, so the multiset always contains `1/2`. The
> `D̃₅ / P_V` row prints `(0, 0, 1, −)` and contains no `1/2`. The row is
> therefore excluded for every coefficient choice, not for a sampled family.

CT-S27's §7 argued the exclusion case by case over `e ∈ {0,1,2}`. That is a
weaker statement about a larger object, and it was discarded. The one-line
argument also disposes of **seven of the ten rows** at once — precisely the
seven both isolated readers reported as uniformly excluded — and the three
survivors are exactly the three whose multiset contains `1/2`.

Work performed:

1. Session scaffold created; the CT-S27 pipeline copied forward rather than
   edited in place (an earlier session's P0 forbids modifying it).
2. `PREREG.md` written **before** any run: hypothesis, observable, falsifiers
   F1–F5 with numeric thresholds, and an Amendment-E vacuity pre-check.
3. **Table 2.1 re-verified from the page images, by printed folio**, not by
   index arithmetic. Folio 2634 and folio 2635.
4. §7 drafted as `NEW-SECTION-7.md` (§7.0–§7.7) and spliced by
   `scripts/splice_section7.py`, which validates the whole buffer **before**
   writing. It refused three times; each refusal was correct.
5. §0 item 6, the §8 open-problems row and the §9 caveat bullets rewritten to
   match the new §7.
6. Four gate checks written or rewritten — N5 (repaired), **N5b, N6, N7, N8**
   (new) — each with ≥ 2 mutants drawn from outside its own pattern list.
7. Description regenerated, both gates re-run, hash and md5 propagated.

---

## 2. The three tiers, as they now stand

The tiers are **not merged**, and each carries its level of confirmation in its
own running text, not only in a heading — so the tier survives being quoted out
of context.

| Tier | Statement | Confirmation |
|---|---|---|
| **1** | `P_V / D̃₅` is unreachable by `L_d` at `d = 2`, for every admissible coefficient vector | **Two independent readings of the printed table**: this corpus, and an isolated reader given only the operator and the page images, which reached the exclusion without being told it |
| **2** | The reachable rows are `PIII(D₈)`, `PIII(D₇)`, degenerate `P_V = PIII(D₆)`, selected by `deg a = 0, 1, 2` | Reproduced by the **second** isolated reader without being told the set. The **first** reader assumed `deg a = deg b`, so it confirms the exclusion only |
| **3** | Generically the row depends only on `(α₂, α₁)`; on the codimension-3 locus `a(1) = a(2) = 0`, `b(1) = 0` the point at infinity becomes ordinary and the multiset matches **no** row | Self-derived only, by a re-derivation that ran in a contaminated workspace and corrected an earlier error of its own. Disclosed as such |

**Change from the commissioning prompt.** The prompt places Tier 2 at
*self-derived, not independently confirmed*. The second cold read (CT-S34,
dispatched after that prompt was written) reproduced the reachable set. Tier 2
is therefore recorded as **reproduced once**, and the reason the first reader
does not count toward it — it answered a narrower question — is stated in the
notice. This is a strengthening of the evidence, not a relabelling of the tier:
the tier heading and its STRUCTURAL label are unchanged.

**Ruled, 2026-09-19: kept as drafted**, with the label staying STRUCTURAL,
because *reproduction and label are different axes* — the row matches are
necessary conditions however many readers found them. See §7.1 for the ruling
and the `review_note` it required.

---

## 3. Claims

All twenty-four are in `claims.jsonl`. None is labelled PROVEN; the emitter
asserts that.

| id | label | subject |
|---|---|---|
| S35-01 | VERIFIED | Table 2.1 as quoted agrees with printed folio 2635 |
| S35-02 | VERIFIED | the Katz identification is the source's own (folio 2634); rank-2 scope |
| S35-03 | STRUCTURAL | Tier 1, the exclusion |
| S35-04 | STRUCTURAL | Tier 2, the reachable set |
| S35-05 | STRUCTURAL | Tier 3, the codimension-3 locus |
| S35-06 | VERIFIED | necessary-not-sufficient, no row assigned, no Painlevé label asserted |
| S35-07 | VERIFIED | label history stated both ways, not adjudicated |
| S35-08 | VERIFIED | tier recoverable from the prose |
| S35-09 | VERIFIED | description size, sha256 and md5, read from disk |
| S35-10 | VERIFIED | both gates green |
| S35-11 | VERIFIED | defect: N5 invented a defect (sentence scoping) |
| S35-12 | VERIFIED | defect: clause splitter broke `v1.4`, caught by a mutant |
| S35-13 | VERIFIED | defect: `was correct` matched `was corrected` |
| S35-14 | STRUCTURAL | disclosure: two checks narrowed after seeing results |
| S35-15 | VERIFIED | defect: the emitter's key projection would have silently dropped `review_note` |
| S35-16 | VERIFIED | defect: packet still pointed at the superseded rev2 in three places |
| S35-17 | VERIFIED | readback 12/12 negatives against rev3; S2a rewritten and both arms exercised |
| S35-18 | STRUCTURAL | governance: S2a standing form adopted; instruction-as-artefact recorded as a candidate |
| S35-19 | VERIFIED | defect: five false statements in `WALKTHROUGH.md`, found by executing it |
| S35-20 | VERIFIED | instrument: `verify_walkthrough.py` 8/8 + 3/3 controls, `mutants_walkthrough.py` 6/6 |
| S35-21 | VERIFIED | **deposit: v1.7 published as record 22850681; readback 20 checks, 0 failed** |
| S35-22 | VERIFIED | defect: the readback's exact-text comparison failed on a correct record |
| S35-23 | VERIFIED | carry-forward: title vs attribution; `Bridge Conjecture` occurs 0 times in the published text |
| S35-24 | STRUCTURAL | governance: Amendment C gains a named-construct clause |

---

## 4. Defects found this session

### 4.1 A check that invented a defect (S35-11)

N5's overclaim scan was **sentence**-scoped. §7.5 says, correctly, in one
sentence: *a mismatch settles the question and is VERIFIED …; a match does not,
because it leaves open whether `L_d` actually lies in the corresponding moduli
family.* The scan saw `lies in` and `VERIFIED` in one span and reported the
notice as overclaiming. It was the notice that was right.

This is Amendment C's symmetry clause in action: a reader that invents a defect
costs what missing one costs, and more if acted on — acting here would have
meant weakening a correct qualification. Repaired to **clause** scope with
hedged clauses exempt, and given a boundary mutant (*"A match is VERIFIED and
`L_d` lies in that family."*) which is caught, so the narrowing did not gut it.

### 4.2 A clause splitter that split inside a version number (S35-12)

`_clauses` split on every `.`, so `v1.4` became `v1` + `4 …` and **N7's entire
v1.4 arm could never match anything**. The check passed on the real notice for
the wrong reason. Two N7 mutants were ACCEPTED and the harness reported
`BROKEN` rather than passing silently — which is the only reason this was
found. Reading the code would not have found it; the arm looked correct.

Repaired: a period between two digits is not a clause boundary.

This is a new instance of an old shape — the check consulted its list, and the
list was fine; the **input** the list was applied to had been destroyed
upstream. Amendment C is about a check verifying it read its file; this is a
check needing to verify it read its *text*.

### 4.3 A missing word boundary (S35-13)

`was (therefore )?correct` matched inside the notice's own `was corrected at
v1.4`. Same class as 4.1: a correct sentence reported as a defect. Repaired
with `\b(?!ed)`.

### 4.4 Disclosure (S35-14)

**Two checks, N5 and N7, were made narrower after seeing their results.** Each
narrowing was accompanied *in the same edit* by a boundary mutant drawn from
outside the check's own pattern list, and each such mutant is caught. The
outcome was sound — in all three cases the notice was right and the check was
wrong — but the order of events is disclosed rather than presented as design.

### 4.5 A projection that would have dropped the operator's ruling (S35-15)

Found while implementing ruling 1, and the only defect this session that would
have produced a **wrong record rather than a wrong verdict**.

`emit_claims_s35.py` built each output row as:

```python
rows.append({k: c[k] for k in REQUIRED})
```

`REQUIRED` is a fixed nine-key tuple. The ruling required a tenth field,
`review_note`, on `S35-04`. Adding it to the claim dict would have changed
nothing: the projection would have discarded it, the emitter would have exited
0, and `claims.jsonl` would have been well-formed, complete-looking, and
missing the thing the ruling asked for. There is no symptom — no exception, no
warning, no size anomaly worth noticing in a 15-line file.

This is the exit-code rule in a new place. The usual form is *a script's exit
code 0 is not evidence it wrote the right values*; here the values were right
in memory and a **filter between the value and the disk** removed one. A whitelist
projection fails closed against malformed input and fails **silently** against
new input.

Repaired by adding an `OPTIONAL` carry-list beside `REQUIRED`, asserting that no
key outside the two lists is dropped, and adding two pre-write assertions
naming `S35-04` specifically: that its note mentions both *not replayable* and
*no script*, and that its label is still `STRUCTURAL`.

`scripts/mutants_review_note.py` supplies three controls, none drawn from the
assertions' own strings (Amendment E): **M1** renames the key, which is exactly
the silent-drop failure mode; **M2** promotes the label the ruling said must not
move; **M3** substitutes a plausible, well-formed note that simply does not make
the distinction — the mutant that a check testing only for the key's presence
would accept. All three are **CAUGHT**, all before any write, with
`claims.jsonl` byte-identical across the run.

### 4.6 A packet that still pointed at the revision it supersedes (S35-16)

Found while preparing to hand over ruling 3's publishing steps, and the most
consequential defect of the session: it sits **on the path the operator was
about to walk**, and every gate was green while it was there.

The deposit packet was copied forward from `CT-S27`. Three places were never
repointed:

| where | pointed at |
|---|---|
| `WALKTHROUGH.md` §2, "Before the browser" | `cd …/CT-S27-CTV17-DEPOSIT-PREP` |
| `WALKTHROUGH.md` §4, "After publishing" | `cd …/CT-S27-CTV17-DEPOSIT-PREP` |
| `postpublish_readback.py`, `selftest_readback.py` | `DESCRIPTION-v1.7-rev2.html` |

Followed literally, §2 would have run **CT-S27's gates over CT-S27's rev2
description** — and they would have passed, because that artefact is sound —
while the operator pasted rev3. A green gate over a different file. Then §4
would have compared the **live v1.7 record** against rev2, the revision without
the sixth item, and reported a mismatch on the very prose this session was
commissioned to add.

The general shape is one this corpus has now met at several levels: **a check
that compares the wrong artefact is worse than no check, because its answer is
believed.** Here it would have arrived at the two moments designed to catch
everything else.

Note what did *not* find it. Both gates were green throughout; they verify the
description, not the instructions for depositing it. The mutant suites were
green; they mutate the checks' inputs, not the operator's working directory.
It surfaced only because the readback was actually *executed* rather than
inspected — it raised `FileNotFoundError` on a path that does not exist in this
session. Had `CT-S35` happened to contain a `rev2` file, it would have run
clean and compared the wrong thing in silence.

Repaired in three parts: both `cd` lines corrected with the reason recorded
in-place; both scripts repointed to `rev3`; and a guard added to
`postpublish_readback.py` that resolves the expected digest **from the gate
run's own output** rather than from a constant typed into the script, and
aborts **before any network call** if the description on disk is not the one
the gate verified. `scripts/mutants_readback_guard.py` supplies two input-path
arms — a stale description and an absent one — and both fire.

The walkthrough's **S2a** step was rewritten in the same spirit, per ruling 3.
It previously printed an expected hash for the operator to compare by eye,
which verifies the quotation rather than the file. It now compares the file on
disk against the sha256 the **passing gate run** recorded, and prints one word.
Both arms were exercised: the real file prints `MATCH`, and a copy with one
byte appended prints `STOP – DIFFERS`.

### 4.7 A phantom, not recorded as a defect

Worth one line because it is the failure this corpus adopted Amendment C to
avoid, in its reverse direction. A filtered read of `check_invariants.py`'s
output placed `ok 2: all 618 claim(s) … carry exactly one recognised label`
directly above `0 carry a recognised label`, which reads as a check
contradicting itself. It is not: the filter dropped the intervening line, and
the second figure describes the **3 488 out-of-scope claims dated before the
convention**. Confirmed against the raw, unfiltered output before anything was
reported or changed. Nothing was wrong, and nothing was repaired — *a reader
that invents a defect costs what missing one costs, and more if acted on.*

---

### 4.8 The gates verified the description; nothing verified the instructions

`WALKTHROUGH.md` is the file the operator actually acts from, and it was the
one artefact in the packet no gate could see. Executing it — rather than
reading it, which is §8's candidate form applied to itself — found **five**
statements that were false while both gates were green:

1. §0 reported `verify_description.py` as `13/13`; it runs **21**. A stale
   count is not cosmetic here: it is the number the operator compares the
   gate's output against, so it would have made a gate running *fewer* checks
   than expected look correct.
2. §5's truncation row named a **54 068**-character description; rev3 is
   **68 303**, understating the field limit that matters by 14 235 characters.
3. §2 still told the operator to take a hash and compare it by eye against a
   constant printed in the file — precisely the form standing form (i) exists
   to remove, left behind when S2a superseded it.
4. §6 described the publication of §10's source table as an unsettled operator
   decision and said *"the current description keeps it"*. It was settled and
   the table was excluded: the description contains **zero** occurrences of
   `refs/`, `outputs/` or any `CT-S…` id.
5. §2's own command, `Select-Object -Last 12`, prints `GATE: PASSED` but
   truncates `checks run : 11` and `checks failed : 0` — it hides the counts
   the corrected prose tells the reader to check. **This one is unreadable:**
   it can only be found by running the block. Widened to `-Last 16`.

Items 1, 2 and 4 are stale-value drift, the class P0 Amendment D was ruled on.
Item 3 is a superseded procedure outliving its replacement. Item 5 is the
reason the repair is a gate and not an edit.

`scripts/verify_walkthrough.py` (8 checks, 3/3 reader controls) now holds the
instructions to their artefacts, and **executes** the walkthrough's display
commands rather than parsing them. `scripts/mutants_walkthrough.py` runs six
arms, each re-introducing a defect this packet really had, each required to be
caught *by the specific check meant to catch it*, with a baseline arm, a
broke-the-gate guard, and `WALKTHROUGH.md` asserted unchanged: **6/6**.

Building the gate produced three instrument defects of its own, all found by
running it (claim S35-20):

- the description's non-ASCII sentinel was chosen as a literal `ξ`, which the
  file **escapes as `&xi;`** 35 times, so the gate refused a sound file on its
  first run. Diagnosed as a *reader* defect, not a file defect, only by a
  second differently-implemented read of the raw bytes — Amendment C's
  symmetry clause;
- `W5` treated a redirect target as a required input and failed on an output
  file that cannot exist before publishing, conflating *"points at a missing
  input"* with *"this step has not been run yet"*;
- `W1`'s pattern required bold `**N/N**` while §0 writes `21/21` unbolded, so
  the check **could not see the only count in the file**. Exposed by mutant
  `M1`, whose anchor came from the packet's real history and not from `W1`'s
  pattern — P0 Amendment E doing exactly what it was ruled for.

### 4.9 The checker that failed on a correct record (post-publish)

v1.7 was published on 2026-09-20 as record **22850681**. The first run of
`postpublish_readback.py` against it printed:

> **VERDICT: the published record is NOT the packet that was checked.**

It was wrong. The record was character-for-character correct.

One check of twenty failed — *rendered text matches the checked description*,
on 55 040 published versus 55 050 local rendered characters. Ten characters.

**The mechanism is this session's own recurring defect, one level down.**
`plain()` strips tags with `re.sub(r"<[^>]+>", " ", t)` — substituting a
**space** for each tag. An inline tag between two non-space characters
therefore *manufactures* a space that is not in the text. Zenodo's editor
re-serialises inline markup on save, so the two sides disagreed by exactly
those phantom spaces: ten of them, every one adjacent to punctuation
(`residual&nbsp;;`, `Mathematics&nbsp;.`) or inside `S_{ζ }`. This is the same
tag-stripping artefact that manufactured 85 phantom findings in CT-S27 — the
defect that put the symmetry clause into Amendment C.

Worse, **the check contradicted its own failure message**, which already read
"re-serialisation is expected". It demanded exact equality while stating that
exact equality would not hold.

**Diagnosed before anything was changed**, per Amendment C's symmetry clause: a
second, differently-implemented renderer (inline tags → empty, block tags →
newline) returned **identical token streams and equal lengths**, and squeezing
all whitespace made the two texts **identical**. Only then was the checker
judged to be at fault rather than the record.

**Repaired** by comparing whitespace-squeezed text, which removes the artefact
and removes nothing else — any missing paragraph, lost sentence, truncation or
altered word changes a non-whitespace character — plus a **non-vacuity guard**,
because two empty strings compare equal.

**The repair is two-sided (Amendment E / P2), because a check repaired until it
goes green is a check that passes by destroying what it protected:**

- **P1, still rejects**: `selftest_readback.py` now rejects **12/12** negatives.
  Two are new and exist solely for this check — a dropped qualification
  (`necessary condition` removed) and an altered value (`Katz invariant 1/2` →
  `3/2`). Neither string is load-bearing and neither is at the tail, so no
  other check can fire on them; each fires on this check **alone**.
- **P2, still accepts**: a new **ARM 3** removes **862** `<em>`/`<strong>` tags
  — reproducing exactly what Zenodo did — and requires the record to be
  **ACCEPTED**. Without it, deleting the check outright would also pass ARM 2.

Re-run: **20 checks, 0 failed**, 45 939 non-whitespace characters matching on
both sides, `-10` whitespace characters reported as re-serialisation.

**The general form.** A comparison between an artefact and a platform's copy of
it must be taken on the invariant the platform preserves. Comparing on a
representation the platform is free to rewrite produces a false alarm on a
correct record — and a false alarm at the irreversible step is expensive, since
the only repair for a real defect there is a further version.

---

## 5. Gate results

| gate | result |
|---|---|
| `verify_description.py` | **21 checks, 0 failed, 0 broken, 3/3 reader-path controls caught — VERDICT: OK** |
| `preflight_deposit_rev2.py` | **11 checks, 0 failed, 0 broken, 3/3 reader controls — GATE: PASSED** |
| `verify_walkthrough.py` | **8 checks, 0 failed, 0 broken, 3/3 reader controls — WALKTHROUGH GATE: PASSED** |
| `mutants_walkthrough.py` | **6/6 arms caught, each by its own check; baseline passes; `WALKTHROUGH.md` unchanged** |
| `selftest_readback.py` | **12/12 negatives rejected each on its own check, 0 broken; ARM 3 accepts the re-serialised record — VERDICT: OK** |
| `postpublish_readback.py 22850681` | **20 checks, 0 failed — VERDICT: the published record is the packet that was checked** |

`S2` fired first against the stale rev2 hash, which is exactly what it exists
for, and passed after the new value was propagated to nine sites.

### The artefact

| | |
|---|---|
| file | `DESCRIPTION-v1.7-rev3.html` |
| chars | 68 303 |
| bytes | 68 606 |
| sha256 | `33a3893372dfd9dcd2c89c4202b8db5aa6d8914acf4707bfd93e7442f8c7e293` |
| md5 | `cdfa63630469ee75834acd725a64415b` |

**Both hashes quoted earlier are superseded**, including where they were quoted
inside this packet: `026e7a9e…` (rev2, before the sixth item) and `39903126…`
(rev2, first draft of the sixth item). Gate check **N8** fails if either is
published as a current value. The supersession is stated in `WALKTHROUGH.md`
under *Hash supersession*.

**On the md5.** Zenodo publishes md5 for *files*, not for the description
field. The value above is the md5 of the description **file's bytes**, for
paste-time comparison only; it will not appear anywhere in the published
record. That is said plainly in the walkthrough rather than left to be
discovered.

---

### The published record

| | |
|---|---|
| record | **22850681** |
| version DOI | `10.5281/zenodo.22850681` |
| concept DOI | `10.5281/zenodo.19941678` (unchanged; read from `conceptdoi`, not derived from the record number) |
| version | 1.7 |
| publication date | 2026-09-19 (set by the platform, not a field that was set) |
| file | `channel_theory_outline.pdf`, 609 300 bytes, md5 `aa56a94a9354b5533b04c89461950eb1` — the v1.6 build carried over; **no file was uploaded** |
| fields changed | description and version. Nothing else. |

Archived under `refs/`: `zenodo-22850681-record.json` (76 977 B, sha256
`0126450834aca76572aaad13ec475ab68df8b8a79a02b207594799c55fb1faed`) and
`zenodo-22850681-description.html` (68 524 B, sha256
`84db2154e87873bd6e030463a50db3a8ab0535993e3e25c128532c43060ba4cb`). The
published description is 82 bytes shorter than the local file purely through
the editor's re-serialisation of inline markup; all 45 939 non-whitespace
characters agree. **From here the deposited text is authoritative and this
repository's copy is the one that may go stale.**

---

## 6. What was NOT established

- **No row is assigned to `L_d`.** A matching multiset is necessary, not
  sufficient; the procedure excludes rows and assigns none. Assigning a row
  would need the classification's *sufficiency*, not merely its invariants.
- **No Painlevé label is asserted for `V_quad`.** §7 is about the
  generating-function operator `L_d`. `V_quad` is a different object; §7's
  exclusion of `D̃₅ / P_V` is **not evidence about it**.
- **The record's label history is not adjudicated.** The v1.0–v1.3
  `P-III(D₆)` label lies inside the surviving set and the v1.4 `P_V / D₅^(1)`
  label lies outside it. Both facts are stated; neither is turned into a
  verdict, because a row exclusion is not a row assignment and the two labels
  are about different objects.
- **Tier 3 has one derivation and it was contaminated.** It is not confirmed.
- **The second cold read is re-derivable but not replayable** — the reader
  computed in-session and left no script.
- Nothing about degrees other than `d = 2`: folio 2634 fixes the
  classification to rank-2 trace-zero connections, and the comparison must not
  be extended.

---

## 7. Operator rulings, 2026-09-19

All three open questions were ruled. Nothing is outstanding.

1. **Tier 2's credit — kept as drafted.** "Reproduced once, with the first
   reader's narrower scope stated" stands, and the label stays **STRUCTURAL**.
   The reasoning is recorded because it generalises: *reproduction and label
   are different axes.* The row matches are necessary conditions regardless of
   how many readers found them, so a second reading raises confidence without
   changing what the claim can support. The tier heading is unchanged.

   **Action taken.** The ruling added one requirement: the second reader left
   no script, so the claim itself must record that the result is
   **re-derivable but not replayable**. That distinction now lives in a
   `review_note` field on `S35-04`, not only in §6 of this report.

   Implementing it exposed a latent defect in the emitter, recorded as
   `S35-15`: `emit_claims_s35.py` projected each claim through
   `{k: c[k] for k in REQUIRED}`, which would have **silently dropped** a
   `review_note` and emitted a claims file that looked correct and complete.
   The field was added, an `OPTIONAL` carry-list added beside `REQUIRED`, an
   assertion added that no unrecognised key is dropped, and two further
   pre-write assertions added: that `S35-04` carries a note naming both
   *not replayable* and *no script*, and that its label is still `STRUCTURAL`.
   Three mutants — note removed, label promoted to `VERIFIED`, note present
   but silent on replayability — are all **CAUGHT pre-write**, with
   `claims.jsonl` byte-identical throughout. A field with no failing check is
   prose, not a record.

   The field was also made schema-consistent with the corpus: `check_invariants.py`
   pairs `review_note` with a `review` value drawn from `self | cold | lean`
   (invariants 3 and 4), and Tier 2's reproduction was a **cold** read, so
   `S35-04` carries `review: "cold"`. The emitter now asserts both directions of
   that pairing. Corpus invariants 2, 3 and 4 all pass.

2. **The md5 — kept, and the interpretation confirmed.** Zenodo publishes md5
   for *files*; a description is pasted text with no file and no displayed
   digest. `cdfa6363…` is therefore for **paste-time comparison against the
   local file only**, and is not something to verify on the record afterwards.
   The walkthrough already says exactly that, which is what keeps it from
   being misread. No change.

3. **Publishing — approved**, by the walkthrough: *New version*, never *Edit*;
   *Import files*; replace the description; **S2a — hash the file immediately
   before pasting, against the file's own value on disk, not against
   `33a38933…` as quoted in this report or anywhere else**; then S6, the
   irreversible step; then `postpublish_readback.py` against the new record id.

   The S2a wording is deliberate and is the one step this report cannot
   discharge on the operator's behalf: quoting a hash and then checking against
   the quotation verifies the quotation, not the file. That has cost a round
   twice.

---

## 8. Standing forms adopted from this session

Two generalisations were ruled out of §4.6 and are recorded here so they are
not lost with the session.

**Adopted — the standing form for verifying bytes before an irreversible
paste.** Do not print an expected hash for comparison by eye. *Comparing a file
against a quoted constant verifies the quotation, not the file.* Resolve the
expected digest from the **passing gate run's own output**, compare the file on
disk against it, emit a single word, and abort **before any network call** on
disagreement. Implemented as `WALKTHROUGH.md` **S2a** and as
`_guard_description_is_gate_verified()` in `postpublish_readback.py`; both have
exercised arms.

**Candidate P0 amendment — an instruction document is an artefact.** It must be
**executed, not proofread.** §4.6 is the live instance: three stale `rev2`
pointers sat in `WALKTHROUGH.md` and two scripts while every content gate was
green, because the gates verify the description and not the instructions for
depositing it. Correct bytes, wrong target, invisible to every content check.
It surfaced only because the readback was *run* — it raised `FileNotFoundError`
on a path absent from this session. Had a `rev2` file happened to exist here,
it would have run clean and compared the wrong artefact in silence.

This is distinct from Amendments A–E: A concerns search-space degeneracy, B the
transit manifest, C a check verifying what it read, D the authority of deposited
text, and E mutant provenance. All five are about a *check*. This one is about
the **procedure a human is told to follow**, which no check in the packet had
ever run. Recorded as a candidate only; not ruled, and not counted as adopted.

---

## 9. Uncommitted files

All under `sessions/2026-09-17/CT-S35-CTV17-ITEM6/` unless noted.

**Documents**
- `PREREG.md`
- `REPORT.md` (this file)
- `NOTICE-v1.7-rev3.md`
- `NEW-SECTION-7.md`
- `DESCRIPTION-v1.7-rev3.html`
- `DEPOSIT-FORM.md`
- `WALKTHROUGH.md`
- `claims.jsonl`

**Scripts**
- `scripts/splice_section7.py`
- `scripts/make_description.py`
- `scripts/verify_description.py`
- `scripts/preflight_deposit.py`
- `scripts/preflight_deposit_rev2.py`
- `scripts/postpublish_readback.py`
- `scripts/selftest_readback.py`
- `scripts/emit_claims_s35.py`
- `scripts/mutants_review_note.py`
- `scripts/mutants_readback_guard.py`
- `scripts/verify_walkthrough.py`
- `scripts/mutants_walkthrough.py`
- `scripts/count_title_terms.py`

**Outputs**
- `outputs/splice_section7.out.txt`
- `outputs/make_description_s35.out.txt`
- `outputs/verify_description_s35.out.txt`
- `outputs/preflight_deposit_s35.out.txt`
- `outputs/emit_claims_s35.out.txt`
- `outputs/verify_walkthrough_s35.out.txt`
- `outputs/mutants_walkthrough.out.txt`
- `outputs/selftest_readback_s35.out.txt`
- `outputs/postpublish_readback.out.txt`
- `outputs/archive_published_s35.out.txt`
- `outputs/diag_desc_diff_s35.out.txt`
- `outputs/count_title_terms.out.txt`

**Governance and carry-forward** (new, 2026-09-20)
- `P0-AMENDMENT-C-REVISION.md`
- `V1.8-CARRY-FORWARD.md`

**Archived published record** (new, 2026-09-20)
- `refs/zenodo-22850681-record.json`
- `refs/zenodo-22850681-description.html`

**Pages**
- `pages/vdPS_p2635.png`

Nothing was committed, pushed, tagged or submitted. **v1.7 was published by the
operator** as record 22850681; no file was uploaded and no metadata beyond
description and version was changed.
