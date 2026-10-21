# REPORT — CT-S58-READ-LOCATOR

Nothing committed, sent, uploaded or deposited. All files uncommitted.

## 1. What was done

The operator's remaining Tier-1 and Tier-2 work is reading, which only the
operator can do. This session produced no mathematics. It converted two
reading instructions into page and line addresses, so that the reading is
bounded and nothing that changed goes unread.

| # | script | what it does | exit |
|---|---|---|---|
| 1 | `locate_revision.py` | locates all 33 CT-S56 replacements on a page of the revised PDF | 0 |
| 2 | `locate_painleve.py` | locates, in the Painlevé paper's source, every line in scope of the five LMP correction items | 0 |
| 3 | `emit_claims_s58.py` | writes the 10-claim AEAL record, validating before the write | 0 |
| 4 | `check_packet.py` | re-derives every counted figure in `READING-PACKET.md` from the JSON outputs | 0 |
| 5 | `mutants_s58.py` | control harness: A0 must write, M1–M6 must refuse, all in a scratch tree | 0 |
| 6 | `verify_claims_s58.py` | re-reads claims and outputs from disk; runs last | 0 |

Deliverable: **`READING-PACKET.md`** — four sittings for the LMP revision,
keyed to the revision's page numbers, and the Painlevé cross-check list keyed
to file and line.

## 2. Claims

All 10 claims are **INSPECTED**. Nothing here is VERIFIED, STRUCTURAL or
PROVEN, and the emitter refuses a PROVEN label outright: locating a sentence
is not judging it, and this session must not pre-empt the operator's reading.

| id | claim |
|---|---|
| S58-01 | all 33 replacements located on exactly one page; revision is 27 pages |
| S58-02 | discrimination control: "three structurally independent" present in v1.2, absent from the revision |
| S58-03 | vacuity: 32/33 anchors resolve differently in the revision than in v1.2 |
| S58-04 | item 5's edits are on pp. 1, 3, 14–18; p18 carries four |
| S58-05 | the Proposition 2.4 closing ruling edit is on p8 |
| S58-06 | two float edits resolved by a cross-check that can fire |
| S58-07 | Painlevé source is 15 `.tex`, 2780 lines, 157 in-scope line-hits |
| S58-08 | the Painlevé paper never names `V_quad`, `L_phi` or `L_V` |
| S58-09 | the Painlevé paper has no Method A/B/C framing |
| S58-10 | case-sensitivity control fires: 3 phantom hits vs 0 real |

## 3. Findings about the instruments

**(a) Two differently-normalised strings, compared.** The first run of
`locate_revision.py` reported **27 of 33 replacements UNLOCATED**. Every one
was an artefact: the anchor had punctuation stripped, the PDF text did not, so
an anchor ending "it Lemma" could not match the rendered "it (Lemma 2.7)". Had
the run been believed, it would have said the revision was missing most of its
own edits. Repaired by putting both sides through one `norm()` and nowhere
else. This is the phantom-findings class again, and the reason it was caught is
that the *controls passed* while the body failed — a reader that can see
"Kovacic" and can see a phrase in v1.2 but not in the revision is not blind, so
the fault had to be in the comparison.

**(b) A diagnostic that separates "absent" from "unseeable".** Rather than
reporting UNLOCATED bare, the locator reports how many leading words of the
anchor the reader *can* see. "reader sees 4/5 leading words" is a brittle
anchor; "reader sees 0/21" would be absent text. That diagnostic is what made
(a) diagnosable in one pass instead of by guesswork.

**(c) Longest is the wrong criterion; unique is the right one.** Choosing the
longest plain-word run as the anchor fails whenever the rendered text
interrupts it, and a short run matches in three places. The locator now
generates all contiguous word-windows and takes the longest one that resolves
to exactly **one** page, so the document chooses the anchor.

**(d) A control that fired on ambiguity, not on disagreement.** The float
cross-check first compared a 3-element candidate set against a 1-element
sibling page and declared disagreement. The correct question is whether the
sibling's page is *among* the candidates — a float is typeset whole, so
membership resolves the ambiguity. Fixed; the check still fires if the sibling
page is absent from the set, and the resolution is recorded as `BY-FLOAT` in
the row rather than silently folded in.

**(e) Case-insensitivity manufactured three findings.** The macro pattern for
the shared operators, run case-insensitively, matched LaTeX's own `\lvert` and
`\lVert` and reported three hits for an operator the Painlevé paper never
names. The report would have said the two papers share notation. Macro
patterns are now case-sensitive, and the control **probes with the pattern that
actually failed** — `r"\\LV"` without the word boundary — because a control
built from the repaired pattern proves nothing.

**(f) A mutant drawn from inside the data proves nothing.** The M4 arm injected
the figure `99` to test that a claim's figures must occur in its cited output.
It reported MISSED — correctly, because `99` occurs in that output as the line
number `section5.tex:99`. The arm was wrong, not the check. Replaced with
`8642`, confirmed absent before use.

**(g) A validator branch made unreachable by eager evaluation.** The M3 arm
(claim citing a non-existent output) crashed with `FileNotFoundError` rather
than refusing: the claim constructor hashed the file eagerly, so
`validate()`'s "cited output missing" branch was dead code. **A crash is not a
refusal** — it exits 3, writes nothing, and says nothing about the claim. The
constructor now defers, and the branch is reachable and caught.

**(h) A substring test is close to vacuous for short figures.** The figure
check used `fig not in body`, which accepts `99` because the output contains
`199`. Now matched as a whole number with digit-boundary lookaround. On its
first run the stricter check immediately **caught a real error in this
session's own claim S58-05**, which quoted "L455" — a line label from a
different session's source, not a figure its evidence contained. The claim was
reworded; the check was not weakened.

**(i) The packet's own figures are checked, not eyeballed.** Every counted
figure in `READING-PACKET.md` is re-derived from the JSON by
`check_packet.py`, which also verifies that every page named in a table is a
page that actually changed and that no changed page is missing from the
tables. On its first run it caught three hand-transcription errors of mine:
the no-change page count was inverted (8 stated as 19), the sitting-1 edit
count was wrong (12 for 10), and the packet claimed page 21 was the only page
carrying edits from more than one item when there are **five** (1, 3, 7, 10,
21). Mere numeral presence is a weak test, so three targeted assertions bind
each figure to the sentence that asserts it.

## 4. What the reading packet establishes about the two papers

These are locations, not judgements.

- **The revision's 33 edits fall on 19 of its 27 pages.** §5 and Table 2 —
  the largest rewrite — are 10 edits on pages 14–18, with four on page 18
  alone. The operator's ruling edit at the closing of Proposition 2.4, the
  only new prose in the paper never read in rendered form, is on page 8.
- **The revision is 27 pages; the journal holds 25.** Page numbers in the
  packet are not the editor's. `CORRECTIONS-FOR-REFEREES.md` remains keyed to
  v1.2.
- **The two papers share no notation.** `V_quad`, `L_phi`, `L_V` all return
  zero. The same object appears in the Painlevé paper as `b(n)=3n²+n+1` and
  the LMP paper as "the companion record". A referee reading both would have
  to be told they are the same object.
- **Item 5 has no counterpart** in the Painlevé paper: no Method A/B/C
  framing.
- **Item 4's subject matter is already handled correctly there, about a
  different operator.** `section3.tex:125` states the governing principle —
  "Exponents {0,0} do not by themselves decide apparency: what decides it is
  the logarithm" — which is exactly the inference the LMP paper made wrongly
  at ξ=0. Per the operator's ruling this is recorded as **the same failure
  class, not corroboration**.
- **The Painlevé paper distinguishes corroboration from independence in five
  separate places** (`appendixA.tex:63`, `appendixB.tex:89`,
  `section5.tex:146`, `section6.tex:183`, `section6.tex:225`) while the LMP
  paper did not. Those five are worth reading as models rather than defects.

## 5. What was NOT established

- **Whether any of the 33 edits reads well.** Located is not read. Every
  question in the packet is posed for the operator, not answered.
- **Whether the Painlevé paper's 157 in-scope lines are correct.** The sweep
  finds lines about shared subject matter; it does not evaluate them.
- **Whether anything is missing from either paper.** Every check here reports
  what is present. A pattern returning zero is recorded as "pattern ran, 0
  hits" and means the pattern found nothing — not that nothing is there.
- **The Painlevé paper's page numbers.** The cross-check list is keyed to
  source file and line, not to `paper.pdf`, because the cross-check is an
  editing task rather than a reading-aloud task.

## 6. Open questions for the operator

1. The packet proposes four sittings in a specific order — §5 first, front
   matter last. That order assumes the front matter should be judged against
   what the body ends up saying. If you would rather read front-to-back once
   before any targeted reading, the packet does not prevent it, but the page
   lists then serve only as a checklist.
2. **Two names, one object** (finding in §4) is a referee-visible issue that
   belongs to neither paper individually. It is not on any correction list and
   is not an error in either paper. Does it want a sentence in the Painlevé
   paper naming `V_quad`, or is it better left to the companion citation?
3. The Painlevé paper's five corroboration-vs-independence hedges are better
   than the LMP paper's were. Is it worth back-porting that wording to the LMP
   revision's §5, or is §5 now sufficient?

## 7. Uncommitted files

```
sessions/2026-09-17/CT-S58-READ-LOCATOR/
  PREREG.md
  READING-PACKET.md          <- the deliverable
  REPORT.md
  claims.jsonl               (10 INSPECTED)
  scripts/locate_revision.py
  scripts/locate_painleve.py
  scripts/emit_claims_s58.py
  scripts/check_packet.py
  scripts/mutants_s58.py
  scripts/verify_claims_s58.py
  outputs/locate_revision.out.txt
  outputs/locate_revision.json
  outputs/locate_painleve.out.txt
  outputs/locate_painleve.json
```

No file outside this folder was created or modified by this session.

## 8. Re-run order

Tidy-up, if any, goes **first**: deletions are writes, and a tidy-up at the end
destroys evidence a claim may rest on (CT-S56 finding (h)).

```
python scripts/locate_revision.py      # 0
python scripts/locate_painleve.py      # 0
python scripts/emit_claims_s58.py      # 0
python scripts/check_packet.py         # 0
python scripts/mutants_s58.py          # 0  (A0 writes; 6 arms refuse)
python scripts/verify_claims_s58.py    # 0  (must run last)
```

Set `$env:PYTHONIOENCODING='utf-8'` first.
