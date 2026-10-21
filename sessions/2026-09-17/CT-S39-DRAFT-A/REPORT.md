# REPORT — CT-S39-DRAFT-A (Group A: §0 introduction, §2 growth with §2.0)

**Session:** `sessions/2026-09-17/CT-S39-DRAFT-A/`
**Status:** draft only. Nothing committed, pushed, tagged or deposited.
**Gate:** 102 checks, 0 failures, 16 control arms, 0 missed.
**Build:** 9 pages, **0 undefined references**.

---

## 1. What was done

Group A is drafted: `section0.tex` (introduction) and `section2.tex` (growth),
the latter opening with the §2.0 attribution paragraph the outline marks as
load-bearing. Both are written in §1's symbols — `ψ_n`, `ψ_∞`, `ν_i`.

The operator's rule for this group was stricter than the usual one:

> Every one of those has been corrected at least once during this run, so the
> drafting check for Group A should verify each citation against the held page
> image rather than against a prior draft or a claim text.

So `OUTLINE.md` §2.0 and the claim texts of `S24-10`/`S24-12`/`S24-13` were
treated as **the thing under test**, not as evidence. Every citation was
resolved to a held artefact and checked against the page. That decision is what
produced findings 2.2 and 2.3 below, neither of which is visible to a check that
compares the draft against the outline.

## 2. Findings

### 2.1 All nine sources are held — and an incomplete scan nearly said otherwise

A first recursive scan for images and PDFs returned the `CT-R1-AUDIT` artefacts
and appeared to show no Gautschi, no Odlyzko, no DLMF capture. It had not
finished. `CT-S8-LITCHECK/refs/` holds 21 files including `gautschi1967.pdf`,
`dlmf_2_9.txt`, `bt1933.pdf` and `nemes2025.pdf`, and
`CT-S24-PAPER-OUTLINE/refs/` holds `odlyzko_asymptotic_enum.pdf` and
`odlyzko_p77.png`.

Reporting absence from a scan that had not completed would have repeated
`S24-09` exactly — the Odlyzko citation was once declared unsourced on a
repo-wide search that was correct but whose conclusion was not. **Absence is
only evidence when the search that produced it finished.**

### 2.2 A reader defect in the gate itself (`S39-02`, VERIFIED)

The most useful output of the session, and it was found by the gate's first run
rather than by inspection.

Folio resolution originally scanned a 120-character header/footer band for the
folio digits and took the first page that matched. For Odlyzko folio 77 that
band matches **three** pages:

| pdf index | why it matched | is it page 77? |
|---:|---|---|
| 63 | body text carries the bibliography reference `[77, 78, 79]` | no — it is page 64 |
| 67 | carries the equation number `(8.77)` | no — it is page 68 |
| 76 | its last line **is** `77` | **yes** |

The scan returned index 63 and the check printed
`O2 folio 77 located in its own page ... ok`. **It reported success while
reading the wrong page.** The failure surfaced only because the three quoted
fragments are long and were then absent; a shorter or more generic fragment
could have matched on the wrong page, and the citation would have been
certified against text that page does not contain.

Repaired two ways, both necessary:

- the folio must stand alone as the **first or last whitespace token** of the
  page's first or last non-empty line, which rejects both false candidates;
- the resolution must be **unique** — two markers are reported as ambiguous
  rather than silently resolved to the first.

The repaired resolver returns index 76, agreeing with the offset of −1 recorded
independently by CT-S24's `verify_odlyzko_p77.py`. Three arms now exercise this
directly: **A8** asserts the band scan *is* defective, **A8′** that the strict
resolver returns the single index 76, **A9** that an ambiguous folio resolves to
`None`.

### 2.3 The outline's own Odlyzko quotation needed two corrections (`S39-04`, VERIFIED)

Found by comparing the draft against the page instead of copying the outline.

- The outline renders the sequence as `a_n` **inside the quotation**; the page
  sets it as a subscripted symbol. The paper typesets it as mathematics within
  the quote rather than reproducing an underscore.
- The outline's second quotation ends `"in the complicated proofs."` The page
  reads `"in the complicated proofs [211, 383]."` — the quotation dropped two
  reference numbers and closed the sentence early.

Neither is detectable by any check that compares the draft with the outline.
Both are detectable immediately by one that compares it with the page. This is
the drafting-discipline note of `S24-19` producing its fourth instance, and the
first in which the compressed paraphrase was in the outline rather than in a
session record.

The substantive content is confirmed unchanged: the *"up to a multiplicative
constant"* half is Odlyzko **reporting Wimp and Zeilberger** [384], and only the
following sentence is his own; and the same page carries the objection that the
Birkhoff–Trjitzinsky results *"may not be rigorous"*, which §2.0 answers in the
same breath rather than later.

### 2.4 A claim whose text contradicts its own label (`S39-03`, INSPECTED) — **needs a ruling**

`S1-04` is the paper's growth law. Its corpus **label** is `PROVEN`. Its claim
**text** still ends:

> Steps 3,4 rest on Gap G1 … **Hence STRUCTURAL, not PROVEN.**

The label is correct and current. `theorem.tex` lines 40–46 and 427–436 record
that **Gap G1 was closed in audit round R1**, and `CT-S1-THEOREM/REPORT.md`
line 8 records the upgrade `STRUCTURAL -> PROVEN` explicitly. It is the claim
text that is stale, left behind when the label was raised.

This was nearly mis-drafted in both directions. Taking the text at face value
would have understated a proved theorem; taking the label without reading the
text would have missed the one classical input the closure leaves imported. The
draft does neither: §2 states the theorem as PROVEN, **and** names at the point
of use the normalisation `h_∞ = 1`, DLMF (5.11.12), `Γ(z+a)/Γ(z+b) ∼ z^{a−b}`,
verified in the held capture `CT-R1-AUDIT/refs/dlmf_5.11.html`.

**Not repaired here.** Amending `S1-04`'s text means editing an earlier
session's `claims.jsonl`, whose digest later claims cite — the same reason the
`draft_check.py` alias was left alone. `CT-S1-THEOREM/REPORT.md` retains three
pre-upgrade `STRUCTURAL` rows at lines 44, 61 and 239, stale for the same
reason. **Operator ruling requested.**

### 2.5 A check that failed on correct prose (`S39-05`)

`F6c` — *the method paragraph must not lead with Pincherle* — was first written
as "Pincherle does not occur in the first 420 characters". It **failed on
correct prose**, because §0 must mention Pincherle in order to disclaim it, and
the disclaiming sentence falls at about character 370.

A companion check failed for a different reason: `"absolutely summable"` spans a
line break in the source, so a raw containment test reported it missing.

Both are instrument defects, not prose defects, and both are the same family as
the phantom findings of CT-S27 and CT-S35. Repaired by testing **order** rather
than position — the mechanism must be introduced before Pincherle is named — on
the whitespace-squeezed text, with a third check requiring the paragraph to say
the interpretation is **not used**, and an arm that fires when the order is
inverted.

## 3. The forward-reference stub, and why it is checked (`S39-07`)

Sections 3–10 are drafted in groups B–E and do not exist, so eight forward
references could not resolve. Rather than weaken the prose to avoid them,
`forwardrefs.tex` declares those eight labels at the numbers OUTLINE.md
revision 6 assigns, and is inputted by the standalone wrapper only.

A stub is exactly the hazard this corpus keeps repairing: a number that drifted
from the outline would print a **wrong cross-reference with no warning**. So
`F7` resolves all eight against the outline's own headings, asserts the stub is
inputted by the wrapper alone and by no section file, and **A10** fires when a
number is drifted. **A11** reads the *rendered PDF* and confirms the attribution
material reaches the page — a check on the `.tex` cannot distinguish "written"
from "rendered" — and confirms the stub's warning text does not.

## 4. Claims

| id | label | subject |
|---|---|---|
| `S39-01` | VERIFIED | nine citations verified against held pages; 102 checks, 16 arms |
| `S39-02` | VERIFIED | the folio-resolution reader defect and its two-part repair |
| `S39-03` | INSPECTED | `S1-04`'s text contradicts its label; **unrepaired, needs a ruling** |
| `S39-04` | VERIFIED | two corrections to the outline's Odlyzko quotation |
| `S39-05` | STRUCTURAL | §0 drafted; both limits stated; method paragraph ordering enforced |
| `S39-06` | VERIFIED | §2 drafted; attribution first; every id and label checked |
| `S39-07` | VERIFIED | build 9 pages, 0 undefined refs; the stub and its guards |
| `S39-08` | INSPECTED | required actions for the Group B re-run |

## 5. What was NOT established

- **No formula was re-derived.** The gate verifies citations and labels. A
  transposed digit inside an equation would pass every check in it. This was
  pre-registered as a known limit (PREREG §6), not discovered afterwards, and
  it remains the operator's scoped item for a pass once all sections exist.
- **Nothing was relabelled.** Where the corpus and a prose rule disagreed, the
  corpus won, per the `S38-19` ruling.
- **§2.0's Gautschi citations are cited, not quoted.** The OCR of
  `gautschi1967.pdf` is degraded — the page reads `THEOIEM 2.3 (Perron [42],
  Kreuser [29])` — so the theorem is cited by number and attribution, both
  verified on the page, rather than quoted verbatim.
- **Wong–Li II is still not obtained** and nothing is attributed to it.

## 6. Open questions for the operator

1. **`S1-04`'s stale claim text (§2.4).** Repair it in place, or record the
   correction in a later session's claims and leave the earlier file intact?
   The same question governs the three stale `STRUCTURAL` rows in
   `CT-S1-THEOREM/REPORT.md` and the `draft_check.py` NOTE.
2. **Does the forward-reference stub survive assembly?** It is correct for a
   Group A standalone build. When sections 3–10 exist it must be dropped;
   `F7` asserts only that no *section file* inputs it today.

## 7. Uncommitted files

New in `sessions/2026-09-17/CT-S39-DRAFT-A/`:

```
PREREG.md                      section0.tex          section2.tex
REPORT.md                      forwardrefs.tex       groupa_standalone.tex
section1.tex  (copied from CT-S38, unmodified)
claims.jsonl                   (8 claims)
scripts/check_group_a.py       scripts/emit_claims_s39.py
outputs/check_group_a.out.txt  outputs/emit_claims_s39.out.txt
outputs/build/                 (9-page PDF and logs)
```

**No file outside this session folder was modified.** Nothing was committed.

## 8. Next

Group A no longer blocks. The Group B re-run can proceed with §2 present, and
should carry the three actions of `S39-08` in one edit: drop the `CT-` alias,
invert mutant `M7`, and correct the now-false NOTE at `draft_check.py:195–196`.
