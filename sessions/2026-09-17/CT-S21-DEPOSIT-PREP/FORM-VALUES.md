# FORM-VALUES.md — the six fields, ready to paste

Every KEEP value below was extracted programmatically from
`outputs/predeposit_20481592.json` (the live v1.2 record read this round), not
retyped. Rationale for the rule: §R31's ASCII-fication defect — a tool that
retypes what it should derive.

Form: **New version** on record `20481592`. It arrives pre-filled from v1.2.

---

## 1. Manuscript (files)

| Action | File |
|---|---|
| **ADD** | `upload\vquad_resurgence_v1.3_correction_notice.md` |
| **LEAVE ALONE** | `vquad_resurgence.pdf` — carried over automatically |

Full path to select in the dialog:

```
C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-S21-DEPOSIT-PREP\upload\vquad_resurgence_v1.3_correction_notice.md
```

- 35 918 bytes
- md5 `aeef03534612b6f4052c0636f8556f45`  ← the digest Zenodo displays; compare this one
- sha256 `c936662f61be8625d69b7f8efce8a8684b33569c6a033e88f510a3050b89948c`

Do **not** delete the carried-over PDF: the concept DOI must resolve to a record
that holds the paper as well as its correction (§R31). Confirm it is still
listed, md5 `4d1e4d59072cad0db8edc86280af45a1`.

### If the PDF is missing from the draft's file list

Observed 2026-09-18: the draft listed the notice alone. Before adding anything,
scroll to the metadata section and decide which failure it is.

| Metadata fields | Meaning | Action |
|---|---|---|
| Pre-filled from v1.2 | genuine New version, carry-over absent | add the PDF, below |
| Empty | this is a **New upload** — it would mint a second concept DOI | **abort**; discard the draft and restart from record 20481592 → *New version* |

A byte-identical copy is staged under the exact published filename:

```
C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-S21-DEPOSIT-PREP\upload\vquad_resurgence.pdf
```

- 612 719 bytes
- md5 `4d1e4d59072cad0db8edc86280af45a1` — equal to the live record's file entry
- sha256 `a5d9e264699e6397030f0512e17f0cd503fcf2eafd57db9b00b57523fcc88d85`

Verified by `scripts\stage_carryover_pdf.py` (claim `S21-70`). The filename must
stay `vquad_resurgence.pdf`: Zenodo publishes the name it is given, and the v1.2
record's file key is that string. The list must end at **2 files**, and the
preview should point at the PDF, not the notice.

This is not an exception to the "no `refs/`" rule — that rule covers the
third-party reference PDFs (AIF, arXiv:0902.1702). This file is the deposit's
own CC-BY paper, already published on the record being versioned.

`refs/` does **not** go up.

---

## 2. Title — KEEP, byte-identical to v1.2

```
A non-classical Painlevé V transcendent from a quadratic polynomial continued fraction: surface classification and resurgent Stokes data
```

Option C. The paper stays in the record, so the companion's title still
describes it, and citations resolve to a record titled as cited. The correction
is carried by the version string, the description and the notice file.

The **record** title and the notice's **H1** are different objects. They need
not match.

---

## 3. Resource type — KEEP

```
Publication  →  Preprint
```

v1.2's `resource_type.id` is `publication-preprint`. Keep it: changing it makes
v1.3 inconsistent with v1.0–v1.2 of the same concept.

---

## 4. Description — REPLACE

Paste as plain text (the editor is rich-text; the characters below are real
Unicode, not entities):

```
This notice records five items affecting v1.2 of the companion paper (10.5281/zenodo.20481592).

Two are corrections. Remark 2.2's claim that the finite singularities are apparent is false in general, and a lemma shows such points are never apparent; the computation in §3 is not affected by this, and indeed already exhibits the unipotent monodromy that refutes the general claim. Conjecture 4.1's stated derivation of β = γ = 0 is refuted, with γ = 1 on the companion's own data.

One item is a clarification that strengthens the companion: Conjecture 4.1 presupposes rather than derives the isomonodromic deformation family, and that presupposition is supported by the van der Put–Saito moduli-space framework.

The remaining two items concern object labelling and the scope of passages affected.

Quotations from the cited literature were verified against page images on the day of deposit.
```

Deliberately **not** mentioned: the typo reported to van der Put and Saito. No
reply had been received, so nothing here is asserted as author-confirmed.

---

## 5. Keywords

**Keep all nine, in this order** (extracted from the record):

```
polynomial continued fractions
resurgence
Stokes constant
apparent singularity
confluent Heun equation
Painlevé V
Sakai surface D5^(1)
Borel summation
arithmetic identification
```

**Add exactly two:**

```
correction notice
isomonodromic deformation
```

Do not add `van der Put–Saito` or a moduli-space term — that indexes the record
against work the notice only cites.

---

## 6. Related works — ADD NOTHING

Exactly **one** row, pre-filled, which you preserve unchanged:

| Identifier | Scheme | Relation | Resource type |
|---|---|---|---|
| `10.5281/zenodo.20173773` | DOI | **References** | Preprint |

- **Add no row for `10.5281/zenodo.20481592`.** v1.3 is a *version* of the work,
  not a supplement to its own predecessor. Zenodo records the lineage outside
  `related_identifiers`, in `metadata.relations.version` (parent `20455089`).
- v1.2 carries no hand-written row for v1.1, v1.0 or the concept DOI. The
  existing versions do not link each other; v1.3 should not start.
- DataCite has no `corrects` relation, so there is no honest row to add.

---

## The other fields

| Field | Value | Action |
|---|---|---|
| Publication date | today's date | **CHANGE** from `2026-06-01` |
| Version | `1.3` | **CHANGE** from `1.2` |
| Authors | `Papanokechi`, ORCID `0009-0000-6192-8273` | keep |
| Affiliation | `Independent Researcher` | keep **byte-identical** — affiliation drift is a logged defect here |
| Licence | `cc-by-4.0` — Creative Commons Attribution 4.0 International | keep |
| Language | English | keep if pre-filled |

---

Then `DEPOSIT-WALKTHROUGH.md` §A4's five abort conditions, publish, then §A5
(`python scripts\postpublish_readback.py <NEW_RECORD_ID>`).
