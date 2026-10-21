# DEPOSIT-READY.md — companion v1.3 correction notice

**Session** `CT-S21-DEPOSIT-PREP` · **date** 2026-09-18 · **budget** ≤ 3 h
**Object** `sessions/2026-09-17/CT-R1-AUDIT/DRAFT-COMPANION-v1.3-NOTICE.md` (497 lines)
**Nothing was deposited, uploaded, committed or sent.** Pre-registration in
`PREREG.md`, written before any computation; no threshold was changed after
results were seen.

## Verdict

**Round 1 (this pass, before the operator ruling): not ready** — six items.
**Round 2 (after the ruling, below): ready**, subject to the two deposit-day
confirmations listed at the end.

The full round-1 reasoning is preserved below unchanged, because the record
should show what the gate caught, not only that it ended green.

The single most consequential finding was **not** an error in the notice. It was
that **C5's tabulation of affected passages was incomplete**, and incomplete in a
direction that made the companion look weaker than it is: v1.2's own Theorem
3.1 already proves C1's local analysis and already prints the non-trivial
monodromy matrix.

---

## Round 2 — resolution

| item | resolution | evidence |
|---|---|---|
| **M1** | C1 gains a scope limitation (point 3): Remark 2.2's general assertion is false, §3 is unaffected and already exhibits `[[1,2πi],[0,1]]`. C5 gains the **Remark 3.2** row, records the second pass, and states three **deliberate exclusions** with reasons. No verdict on Theorem 3.1(ii). | notice C1 pt 3, C5; claims `S21-13`…`S21-17` |
| M2 | Placeholder replaced: the authors were notified by email, no reply when the notice was finalised, nothing author-confirmed. Deposit-day re-confirmation retained. | notice C3; `S21-18` |
| M3 | `review='cold'` written back to `S4-06`, `S5B-C6` with `review_note` and `.bak-s21m3`. | `scripts/fix_m3_review.py`; `S21-18` |
| M4 | "Four points" → "**Seven** points"; enumerated count verified at seven programmatically. | `S21-18` |
| M5 | **Not corrected, by ruling.** The letter is sent and the quoted entries are on the page it names, so no correction is sent for it alone; fix in passing if a reply comes. | `S21-20` |
| M6 | `.gitignore` default-denies `**/*.png,jpg,jpeg,pdf,html`; media stageable **17 → 0**, non-media 411 → 399, nothing staged. `R1-107` amended in place with `.bak-s21m6`. | `S21-19` |

### The Remark 4.2 / 6.7 classification the ruling asked for

Both use the word "apparent"; **neither depends on it**, and for *different*
reasons:

- **Remark 4.2** rests on `θ₁ = θ₂ = 0`. Those exponents **survive C1**: they are
  the difference of the local exponents, both `0` by the double root `ρ² = 0`
  that C1 itself establishes and that Theorem 3.1(i) certified numerically at
  `dps = 150`. Apparency is not needed for `θ = 0` — `θ = 0` is exactly the
  resonant case in which logarithms appear. Decisive internal evidence: v1.2
  states the same fact **without** any gloss at §7.1 item 3. **Excluded from C5.**
  This also means **C2 is safe**, since C2 relies on `θ₁ = θ₂ = 0` being correct.
- **Remark 6.7** rests on **Theorem 3.1(ii)** — its parenthetical glosses
  "apparent" as *"trivial local monodromy on `M₁₁ = V_quad`; Theorem 3.1"*, and
  the consequence drawn is about `M₁₁`. Unadjudicated here, so **excluded from
  C5**, listed with its reason.
- **Remark 3.2**, by contrast, says *"the monodromy at the finite singularities
  is exactly trivial by algebra"* — flat, **without** the `M₁₁` qualifier. That
  is the apparency claim. **Included in C5**, dependency only, no verdict.

### Three detector defects found while re-running the gate

The consistency checker itself was wrong in three ways, all found by reading its
output rather than its exit code:

1. **False negative from hard wrapping.** It reported *"No published erratum is
   known to us"* **missing**. The sentence is present; it wraps as
   `No published` / `> erratum is known to us`. Trusting it would have had me
   "repair" a sentence that was already correct. Phrase tests now run on text
   with blockquote markers stripped and whitespace collapsed.
2. **A check that could no longer fail.** The C4 test hardcoded the string
   `"Four points"`. Correcting the notice to "Seven" left it matching nothing
   and reporting `0` items with no verdict — passing silently. It now parses the
   count **word**, maps it to a number, compares against the enumerated items,
   and **asserts the sentence exists at all**.
3. **A substring search with no polarity.** `author-confirmed` matched my own
   sentence *"nothing here is author-confirmed"*, which asserts the opposite.
   Negated contexts are now separated and listed, never silently dropped.

**Controls.** `scripts/control_item4.py` mutates the notice, runs the real
checker, and restores it, verifying the restore by sha256 (`f3ac6d41…`). It
would have failed had any detector been insensitive to the distinction it
decides. All three fired: count-word mismatch → `MISMATCH`; a genuine
non-negated *"The authors have confirmed this"* → an asserting hit; a
re-wrapped hedge → still found.

### Final state

Support rows agree; cited ids exist and are unsuperseded; C4 says seven and
enumerates seven; F7 has **0 asserting hits, 1 negated**; both hedges present.
**359 → 370 claims**, all five invariants pass.

**Ready to deposit**, subject to two confirmations on the day:

1. that no reply has arrived from the authors, so C3's sentence still holds;
2. the standing deposit-day citation checklist in the notice's final section.

`R1-57` remains the sole `self`-reviewed row, as it has been throughout; the
notice discloses it.

---

## Round 1 findings, as recorded before the ruling

## The table

| # | packet item | status | evidence |
|---|---|---|---|
| 1 | Citation re-fetch — all five external sources | **PASS** | `outputs/item1_refetch.json`, `outputs/item1b_resolve.json`, `CT-R1-AUDIT/REFS-MANIFEST.md` §CT-S21 |
| 1a | vdPS (AIF), arXiv v5, Jimbo (EMS), companion v1.2 (Zenodo) re-fetched today; all four **byte-identical** to the local copies | **PASS** | same |
| 1b | Zenodo record read for version DOI, **concept DOI**, `metadata.version`, file checksum | **PASS** | `item1b_resolve.json` |
| 1c | DLMF §32.2 recorded with **Version 1.2.8, release 2026-09-15** | **PASS** | `item1b_resolve.json` |
| 1d | NOT RE-FETCHED rows | **none** — every cited source re-fetched | — |
| 2 | Quote verification from page images, one per message — 13 rows | **PASS with one DIFFERS** | `outputs/item2_quotes.md` |
| 2a | vdPS pp. 2634, 2635, 2637, 2655; Jimbo p. 1152; v1.2 pp. 3, 4, 6, 10 | **MATCHES** | `outputs/item2_quotes.md` |
| 2b | Location of family (4.1) | **DIFFERS** → **M5** | `outputs/item2_quotes.md` row 5 |
| 2c | C5 row 4 (Remark 6.1) | **MATCHES** | `outputs/item2_quotes.md` row 13 |
| 2d | Completeness of C5's tabulation | **FAIL** → **M1** | `outputs/item2_quotes.md`, finding |
| 3 | Licence strings as printed | **RECORDED**, no determination made | `outputs/item3_licences.json`, `REFS-MANIFEST.md` §CT-S21 |
| 3a | three Zenodo companions → `cc-by-4.0`; arXiv → `nonexclusive-distrib/1.0`; AIF, EMS → **NOT CHECKED**; DLMF notices captured verbatim | **RECORDED** | same |
| 4 | Internal consistency — claim ids, support rows, numbering, author-confirmation wording | **2 of 4 pass** | `outputs/item4_consistency.md` |
| 4a | every cited `claim_id` exists and is not superseded | **PASS** | same |
| 4b | support-table rows match current label/review | **FAIL** → **M3** | same |
| 4c | numbering and cross-references resolve | **FAIL** → **M4** | same |
| 4d | no sentence asserts author confirmation | **PASS** — hedges intact | same |
| — | commit-side exclusion (outside the packet's scope, reported not acted on) | **FAIL** → **M6** | `outputs/item4_consistency.md`, `REFS-MANIFEST.md` |

## Must resolve before deposit

### M1 — C5's tabulation is incomplete, and the notice understates the companion

C5 says its list of affected passages *"were located by a full-text pass over
v1.2 and read from page images."* It lists five. Reading the page images found
**four further passages that depend on the apparency claim and appear nowhere in
the notice**: Theorem 3.1, Remark 3.2, Remark 4.2, Remark 6.7.

**Remark 4.2** is the one that changes a reader's picture: it is the companion's
explanation of the PSLQ nulls (*"θ₁ = θ₂ = 0 (apparent singularities), the
standard connection formula degenerates … consistent with the failure of all
tested PSLQ identification bases"*). C5 currently leaves the impression that
apparency enters only the §4 classification and the §7.1 summary.

**Theorem 3.1 is the important one, and it cuts the other way.** Its proof
(printed p. 5, read from a rendered image) computes `p₀ = 1`, `q₀ = 0`, hence
`I(ρ) = ρ² = 0`; puts the logarithm in `y₂` only; and **displays the monodromy
explicitly as `[[1, 2πi], [0, 1]]`** — unipotent and ≠ `I`. So:

- v1.2 **already contains C1's lemma.** C1 corrects **Remark 2.2's general claim**
  about the roots of `χ`; it is not a gap in §3.
- Theorem 3.1(ii) claims the *effective* monodromy **on the connection
  coefficient `M₁₁`** is trivial — because the unipotent action fixes `y₁`. That
  is a **different and weaker** statement than apparency, and it does not
  obviously fall with Remark 2.2.

As drafted, a reader would take §3 to be collateral damage of C1. On this
evidence it is not. **STRUCTURAL** — read from the printed statement and proof;
Theorem 3.1(ii)'s correctness was *not* re-derived here and is not asserted.

*Resolution:* add the four passages to C5, and add a sentence to C1
distinguishing Remark 2.2's general claim from Theorem 3.1's specific one.
Operator's call whether Remark 3.2 (*"exactly trivial by algebra"*, inconsistent
with v1.2's own Step 4) deserves its own correction row rather than a C5 row.

### M2 — C3's disclosure still carries the letter-status placeholder

C3 discloses that the vdPS authors have not confirmed the typo. The sentence was
drafted when the letter *had not been sent*; it is still unsent, so the wording
is **currently true**, but it becomes false the moment the operator sends it, and
the letter and the deposit are both on today's queue. Fix the ordering or fix the
sentence; do not let the deposit and the letter cross.

### M3 — two support-table rows are stale in the corpus, not in the notice

`S4-06` and `S5B-C6` carry `review = None` in `claims.jsonl`, while the notice's
support table shows them **cold**. `VERIFY-S14.md` and `_deps_table.md` show the
cold read did happen, by route *"D — corroborated"*. So the **corpus rows are
stale** and the notice is right. Either write `review='cold'` back to the two
claims (with a `.bak`, under the R20 in-place-amendment precedent) or reword the
column. Not a substantive defect, but the notice currently asserts something the
corpus does not support, which is exactly what item 4 exists to catch.

### M4 — C4 says four, then lists seven

C4 reads *"Four points must accompany this table"* and enumerates **seven**.
Pure editing.

### M5 — family (4.1) is displayed on p. 2654, not p. 2655

The notice and the letter both say *"family (4.1) on p. 2655"*. The **label** is
on p. 2654; the **entries**, including the `b(z)` being corrected, are on p. 2655.
Suggested: *"the entry `b(z)` of family (4.1) (displayed p. 2654), printed on
p. 2655"*. This matters more in the letter than in the notice, since the letter
goes to the authors.

### M6 — commit-side only, and the packet forbade me to act on it

Not a deposit blocker; recorded because R21 got it wrong and the record should
not stand. `R1-107` states that after the `.gitignore` written last round, **zero
third-party bytes would be staged**. That is **false**. Page images and saved
HTML also live outside `refs/`/`pages/`. Re-derived in a separate invocation
today, `git add -n -A -- sessions/2026-09-17` stages **411** paths, of which
**17** are image/pdf/html:

| where | n | whose |
|---|---|---|
| `CT-R1-AUDIT/coldpackets/vdps_p2634.png`, `vdps_p2635.png`, `jimbo_p1152.png` | 3 | **third party** |
| `CT-S10-COLDREAD2/dlmf_5_11*.html` (4 files) | 4 | **third party** (NIST) |
| `CT-S9-PVPARAMS/outputs/jimbo_page16-16.png`, `jimbo_page23-23.png` | 2 | **third party** |
| `CT-R1-AUDIT/coldpackets/companion_v12_p{2,3,5,6,7,9}.png` | 6 | operator's own, CC-BY-4.0 |
| `CT-S17-TRACEFREE-NORM/companion_v12_p6_time_LOOK.png` | 1 | operator's own, CC-BY-4.0 |
| `CT-S1-THEOREM/theorem.pdf` | 1 | this project's own output |

So **9 third-party files, not zero**. The CT-S18 and CT-S19 packet images are
**already excluded** — they sit under `packet/pages/`, which the `**/pages/*`
pattern catches — and so is this session's rendered page. An earlier draft of
this file listed them as exposed; re-deriving the count corrected it.

Given item 3a — the arXiv PDF is under `nonexclusive-distrib/1.0`, which grants
third parties **no** redistribution right — this must be closed before any
commit. The packet says *"change no exclusion"*, so `.gitignore` was **not**
edited. `R1-107` needs amendment or supersession.

## What this pass did not establish

- No mathematics was re-derived. C1–C5 were checked **as text against sources**,
  not re-proved.
- Theorem 3.1(ii)'s correctness — flagged as a distinct claim, not adjudicated.
- Licence **determinations**: none made, as instructed. AIF and EMS stay
  **NOT CHECKED**; the other 60-odd files of the census were untouched and remain
  **NOT CHECKED**.
- Any quotation the notice draws from sources other than the five re-fetched.

## Open for the operator

1. M1: how much of Theorem 3.1 to fold into C1, and whether Remark 3.2 becomes a
   correction row. This is the only item requiring a judgement rather than an edit.
2. M3: write back `review='cold'`, or reword the column?
3. M6: amend or supersede `R1-107`, and extend `.gitignore` — a separate,
   explicitly-scoped packet, since this one forbade changing exclusions.
4. Whether the p. 2654/2655 fix (M5) goes into the letter before it is sent.
