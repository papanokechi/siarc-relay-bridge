# NEXT-STEPS.md — after the v1.3 deposit

Three items, in order. Item 1 is operator-gated. Item 2 is done. Item 3 is the
next session and is scoped here, not started.

---

# 1. The description edit (operator, ~5 minutes)

Record `22831933`. **Metadata edit, not a new version**: the file set stays
frozen and the DOI does not change. Both paste points are in
`DESCRIPTION-EDIT.md` with the paragraph map; they are repeated here only as
click steps, not as a second copy of the text — read the text from that sheet.

1. Open `https://zenodo.org/records/22831933`.
2. **Edit** (top right of the record page). The form opens on the published
   metadata.
3. Scroll to **Description**. The editor is rich text; paragraphs are the `<p>`
   blocks you see separated by blank lines.
4. **Edit 1.** Put the cursor at the very start of the first paragraph, before
   "This notice records five items…". Type the label, then a space:
   `Version 1.3 (correction notice).` Select just that label and press **Bold**
   (or Ctrl+B) so it matches the `Version 1.1` / `Version 1.2` blocks lower down.
   The full stop is inside the bold, the space after it is not.
5. **Edit 2.** Put the cursor at the end of the paragraph beginning "Quotations
   from the cited literature were verified…" — the last paragraph of the notice,
   immediately above "We study the resurgence…". Press Enter for a new paragraph
   and paste the boundary sentence from `DESCRIPTION-EDIT.md` § "Edit 2".
6. Do **not** touch the abstract paragraphs, the version-history paragraphs, the
   files, the keywords, the licence, or the related-works row.
7. **Save**. Zenodo republishes the metadata in place.

## Then verify

```
cd sessions\2026-09-17\CT-S21-DEPOSIT-PREP
python scripts\verify_description_edit.py 22831933
```

Expect **9 of 9**. Against the unedited record it returned 5 of 9, so it is
known to discriminate. The four edit-dependent checks are: bold label present;
label opens the description; boundary paragraph present verbatim; boundary sits
immediately before the abstract. The five invariants — no "item 1 above", both
C1 sentences still present, two files, both DOIs unchanged — were green before
the edit and must stay green after it.

**If it returns 8 of 9 on "boundary paragraph present verbatim"**, that is most
likely the rich-text editor normalising whitespace or `&nbsp;`, not a wrong
paste. Compare the printed live paragraph against the sheet before editing
anything: if the words match and only spacing differs, the fix is to loosen the
comparison in the script to whitespace-collapsed equality — and to say so in the
claim, because loosening a check after seeing results is exactly what the
pre-registration rule exists to prevent. Do not loosen it to make it pass
without recording that you did.

## Then close S21-73

`S21-73` currently records the unmarked abstract boundary as NOT ESTABLISHED at
publish. `claims.jsonl` is append-only: do not edit that line. Append a
follow-up claim citing the 9-of-9 output hash, then re-run
`CT-R1-AUDIT/check_invariants.py` and `make_backup.py`.

---

# 2. Wong & Li II — done

Written, not bought. `REFS-MANIFEST.md` § "Wong & Li II: NOT OBTAINED" carries
the status as a table of the two open questions; `AUDIT.md` § R35 carries the
argument; claim `S21-76`.

The asymmetry that makes this safe, in one line: the unread article could still
bear on a **closed form for `K`**, but it cannot reach `s` — derived and
verified here independently — and it cannot reach the `r_∞` framing, which rests
on Wong–Zhao §3, a page that is held and hashed. Nothing further is needed
unless the article is later obtained, in which case R35 is superseded, not
deleted: both questions are already written in the form an answer would take.

---

# 3. The next session: leaf verification and `S_{ζ*}`

Proposed `SESSION_ID: CT-S22-STOKES`. **Not started.** This is the first
genuinely new mathematics since CT-S16 and the two items share the same
machinery, which is the only reason to scope them together.

## 3.1 What the two items actually are

**(a) The step-3(b) falsifier, gap `S16-15`.** Pre-registered in CT-S16 and left
unrun with its threshold **unchanged**. It requires: integrate PV from
`(t₀, q, p)` to `t₀ + ε` for two values of `ε`; rebuild the linear system at
each; compute **monodromy and Stokes data** and check agreement with System C's
to **at least 30 digits**. Step 3(c), its vacuity pre-check, belongs to it and
likewise did not run. `flow_regularity.py` is supplementary and is not a
substitute.

**(b) The `S_{ζ*}` question.** `K` is **ξ₀-level connection data** for
`f = Σ Qₙ zⁿ` and is therefore **not** the Stokes constant `S_{ζ*}`
(`CT-R1-AUDIT/REPORT.md`, `CT-S3B-RINF/REPORT.md`). P3 was explicitly forbidden
to name it as such, and the companion's Remark 6.2 records that v1.0's Stokes
constant was wrong precisely because of a naming slip of this kind. The open
question is what `S_{ζ*}` is — at `ζ* = 2ξ₀`, per the CT-S3A audit — not whether
`K` may be relabelled.

**The shared machinery:** both need Stokes data for an **irregular rank-2
system** at high precision. That is one implementation, one set of controls, and
one precision ladder, used twice.

## 3.2 The order that keeps it honest

1. **Build the Stokes solver against a case with a known answer first.** Not
   against System C. A confluent hypergeometric or Airy-type rank-2 system whose
   Stokes multipliers are in closed form, so a wrong solver is caught by
   disagreement with a number you did not compute.
2. **Then the vacuity pre-check, 3(c)**, before 3(b): confirm the 30-digit
   comparison actually moves when the data it is about moves — perturb `(q, p)`
   off the leaf and confirm the check **fails**. A falsifier that passes on
   perturbed input is testing nothing.
3. **Then 3(b)** at the unchanged 30-digit threshold.
4. **Only then `S_{ζ*}`**, which is a different computation on the same solver.

Items 1–2 before 3 is not caution for its own sake. CT-S16's defect family was
*a step that cannot fail cannot be trusted to report failure*: `irreducibility.py`
returned "IRREDUCIBLE" with **no test performed**, and was caught only because a
reducible-by-construction control was also declared irreducible. At 30 digits on
an irregular system, a solver that silently returns garbage will look like a
falsifier that fired, or like one that passed. Controls are assertions.

## 3.3 Pre-registration, before any computation

`PREREG.md` must state, per P0: the hypothesis; the observable; the falsifier
with its numeric threshold — **30 digits, copied unchanged from CT-S16, not
restated from memory**; and the vacuity pre-check with the perturbation that is
expected to break it. Thresholds do not move after results are seen; if 30
digits proves ill-posed for Stokes data (a real possibility — Stokes constants
are basis-dependent and the comparison must fix a normalisation first), **that
is a finding to report**, not a number to adjust.

The basis/normalisation question is the one I would expect to bite first, and it
should be settled in `PREREG.md` before the solver is written: *which* Stokes
matrices, in which sectorial basis, with which branch of the formal solution.
Two correct computations in different normalisations disagree in every digit.

## 3.4 What would make this session stop

Per P0: a falsifier fires; a convention is ambiguous; required data is missing;
runtime exceeds 3× budget. Add one: **the known-answer control in 3.2 step 1
does not reproduce its closed form to the working precision.** Then the solver
is wrong and nothing downstream means anything.

## 3.5 Budget

Unverified planning number, not a commitment: the solver and its control are the
bulk of it, and 3(b) and `S_{ζ*}` are cheap once it exists. Expect the
normalisation question to take longer than the arithmetic.
