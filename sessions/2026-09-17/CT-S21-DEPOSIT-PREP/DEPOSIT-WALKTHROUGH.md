# DEPOSIT-WALKTHROUGH.md — companion v1.3, and the Wong–Li decision

Prepared under CT-S21. **Nothing here has been executed.** Both items are
operator actions; this is the order to do them in, what to check at each step,
and what should make you stop.

Two documents already carry the substance: `DEPOSIT-READY.md` (the gate) and
the notice's own final section (the citation checklist). This file is the
runbook that ties them together, plus the facts you'd otherwise have to go and
look up.

---

# PART A — Deposit companion v1.3

## A0. Pre-flight (≈10 min, all local, all reversible)

Run from `sessions/2026-09-17/`:

| # | Command | Expect |
|---|---|---|
| 1 | `python CT-R1-AUDIT\check_invariants.py` | `INVARIANTS OK`, 381 claims / 22 files |
| 2 | `python CT-S21-DEPOSIT-PREP\scripts\scan_macro_damage.py` | `0 occurrences` |
| 3 | `python CT-S21-DEPOSIT-PREP\scripts\scan_escape_damage.py` | only the 4 `CT-S9-PVPARAMS/outputs/*.txt` rows (raw PDF artefacts) |
| 4 | `python CT-S21-DEPOSIT-PREP\scripts\item4_consistency.py` | all checks pass |
| 5 | `python CT-S21-DEPOSIT-PREP\scripts\control_item4.py` | **all three controls fire** — if any does not, the checker is asleep and step 4 means nothing |
| 6 | `python CT-R1-AUDIT\make_backup.py` | new zip + sha256 stored outside the archive |

Step 5 is not ceremony. The C4 check had already silently stopped being able to
fail once, and that is how it was caught.

> **Late find, already repaired, worth knowing before you upload.** The notice
> contained four `\theta` occurrences where a Python source literal had turned
> `\t` into a TAB, printing `heta_inf`, `heta_0`, `heta_t` in the methodology
> note at lines 524–525. Repaired this round (`S21-35`). The same class cost a
> `\beta` in `outputs/item2_quotes.md`. If you edit the notice again through a
> script, re-run step 2 before uploading.

## A1. The two deposit-day confirmations

From `DEPOSIT-READY.md`:

**1. No author reply.** The vdPS typo letter went to `m.van.der.put@rug.nl` and
`mhsaito@ba.kobegakuin.ac.jp`. C3 currently states that the authors were
notified, that no reply had arrived at finalisation, and that **nothing is
author-confirmed**.

- *No reply* → the sentence stands as written. Proceed.
- *A reply arrived* → **STOP.** The sentence is now false, and a reply may also
  change the typo's status from "reported" to "confirmed" or "disputed". That is
  a notice edit, not a deposit-day tweak.

**2. The standing citation pass.** Four rows, in the notice's final section.
Deliberately deferred to the day so the recorded hashes match what is cited.

| # | Source | Action |
|---|---|---|
| 1 | van der Put & Saito, *Ann. Inst. Fourier* **59** (2009) — Table 2.1 p. 2635, strong-RH passage p. 2634 | re-fetch, sha256, **re-read both page images** |
| 2 | Jimbo, *Publ. RIMS* p. 1152 — the PV dictionary **and** (A1)_PV | re-fetch, sha256, re-read the page image |
| 3 | Companion v1.2, Zenodo version DOI `10.5281/zenodo.20481592` | re-fetch, sha256, confirm it is still the version cited |
| 4 | DLMF §32.2 | re-fetch, record **release version and date** (last read: Version 1.2.8, 2026-09-15) |

Rules that apply to this pass specifically:

- **Hypotheses are in scope, not just theorem statements.** This is the Gautschi
  (2.8) lesson, where an OCR layer rendered a hypothesis so as to reverse the
  conclusion.
- **Read page images, never the text layer**, for anything load-bearing. Two of
  CT-S15's OCR transcriptions were rejected for exactly this.
- p. **2637** (the `det A(1)` constraint) is also quoted by the notice and was
  added to the packet late — include it.

If any row will not re-fetch, record **NOT RE-FETCHED** with the reason. Do not
substitute a cached copy silently.

## A2. What is deposited, and what must not be

**Deposit: the notice ALONGSIDE the v1.2 PDF.** *(Superseded the earlier
"notice only" reading — operator ruling, see AUDIT §R31.)* A new version whose
sole file is an erratum makes the concept DOI resolve to a record where the paper
itself is absent, so anyone following a citation lands on a correction with
nothing to correct.

Note the mechanics: on Zenodo **New version**, the previous files are carried
over by default. Keeping the paper is therefore the *default*, and the notice-only
shape would have required actively **deleting** `vquad_resurgence.pdf` from the
draft. So: **do not delete it**, and **add** the notice beside it.

The held copy `refs/vquad_resurgence_v1.2_zenodo-20481592.pdf` is byte-identical
to the deposited file (612 719 bytes, md5 `4d1e4d59…`), so if the carry-over ever
has to be redone by hand it can be re-uploaded without altering the paper.

The notice's own form (Markdown as-is, or a PDF render) remains your choice; a
render has its own hash.

**Do not upload `refs/`.** This is a hard line, and the reason is licence, not
tidiness:

| file | licence as printed | may it be redistributed? |
|---|---|---|
| `vdps_*` (Ann. Inst. Fourier) | *tous droits réservés* | **no** |
| `arXiv:0902.1702` | `nonexclusive-distrib/1.0` (arXiv default) | **no** — grants third parties nothing |
| `arXiv:2204.09305v1`, `arXiv:2306.05930v2` | CC-BY-4.0, version-pinned | yes, but not needed here |
| companion v1.2 | operator's own | n/a |

"Free to read" is not "free to redistribute". `sessions/2026-09-17/.gitignore`
already default-denies `pdf/png/jpg/html`; that exclusion stays until you
re-admit a file **by name**.

## A3. Zenodo mechanics

The companion is an existing record, so this is a **new version**, not a new
record:

| | |
|---|---|
| v1.2 record | `20481592` |
| v1.2 **version** DOI | `10.5281/zenodo.20481592` |
| **concept** DOI | `10.5281/zenodo.20455089` |
| versions existing | three |

- Use **"New version"** on record `20481592`. That mints a **new version DOI**
  and leaves the concept DOI stable.
- **Never assume the concept DOI equals the record number.** Read the API's
  `conceptdoi` field. These two differ here by more than a digit, and
  conflating them has already been a logged defect class.
- If `zenodo.org` returns **504**, resolve via DataCite instead:
  `curl -L -H "Accept: application/vnd.citationstyles.csl+json" https://doi.org/<DOI>`
  or `https://api.datacite.org/dois/<DOI>`.
- Read licences back from `metadata.rights` using
  `Accept: application/vnd.inveniordm.v1+json`. The legacy `metadata.license`
  field reports only one and produces false negatives.

**Before pressing publish, diff the web form against the document.** Title,
version string, date, authors, affiliation and keywords drift between the form
and the uploaded file, and it is the single most recurrent defect in this
workflow — it has recurred twice inside one draft before. Check the form's
title against the notice's own H1, and the related-identifier rows against the
two DOIs above.

**Related identifiers: add none.** *(Superseded — see AUDIT §R32 and
`DEPOSIT-FORM.md`.)* This was written for the notice-only shape. With the paper
retained, v1.3 is a **version** of the work rather than a supplement to its own
predecessor, and Zenodo already maintains the version linkage in
`metadata.relations.version`, outside `related_identifiers`. v1.2 hand-links
none of its predecessors; v1.3 should not start. Preserve the pre-filled
`10.5281/zenodo.20173773` / *references* row and add nothing.

## A4. Abort conditions

Stop and do not publish if any of these is true:

1. An author reply has arrived (A1.1).
2. Any citation row fails to re-fetch, **or** a page image no longer reads as
   quoted.
3. Companion v1.2 is no longer the version cited, or its sha256 has changed from
   `a5d9e264…`.
4. `control_item4.py` does not fire all three controls.
5. The form metadata disagrees with the notice and you cannot say which is right.

## A5. After publishing (do not skip — this is what the record is for)

1. Record the **new version DOI** and the record id.
2. Re-read `conceptdoi` from the API and confirm it is still `…20455089`.
3. Add the new record to `REFS-MANIFEST.md` with retrieval date, bytes, sha256.
4. Append a section to `AUDIT.md` and a claim per fact to
   `CT-R1-AUDIT/claims.jsonl` — deposit DOI, date, what was uploaded, what was
   excluded and why.
5. Re-run `check_invariants.py` and `make_backup.py`.
6. The C3 sentence becomes historical the moment a reply arrives; if one comes
   after deposit, that is a v1.4 item, not an edit.

---

# PART B — Wong & Li II: buy, or write the NOT OBTAINED line

## B1. The target

> R. Wong and H. Li, *Asymptotic Expansions for Second-Order Linear Difference
> Equations, **II***, **Stud. Appl. Math. 87**(4) (1992), 289–324,
> DOI `10.1002/sapm1992874289`, issued 1992-11.

**The title trap is live.** "Wong & Li 1992a" alone retrieves the wrong paper.
The numeral **II** and the word **linear** are both load-bearing (`R1-61`). If
what arrives does not carry both, it is the wrong article — this is why
`AUTHOR-REQUEST-WONGLI.md` was kept rather than deleted.

## B2. What it is supposed to decide

DLMF §2.9 gives explicit exponents only for bounded coefficients and explicitly
defers this case — eq. (2.9.14) with `P = d`, `Q = 0` — to this paper. The
question is whether

```
s = β_{d−1}/β_d + (d−1)/2
```

is already in print, and whether the leading constant is given in closed form.
Currently recorded as **NOT FOUND in the sources obtained, by the methods
used** — never as "new".

When you have it, read for exactly two things:

1. the **exponent** `s` for the `P = d, Q = 0` case — is it stated?
2. the **connection constant** — is it given in closed form, or (as everywhere
   else in this literature) left undetermined?

## B3. The decision has got cheaper since it was framed

This is the part worth pausing on. The contribution claim no longer rests on
Wong–Li alone:

- **Ibrahim–Salvy is weaker support than it looked** and now quoted in its
  printed form: *"we do not know how to compute the leading coefficient exactly
  in general"* — the state of the art, not a theorem about the world.
- **Wong–Zhao §3 gives a structural reason** the growth law is not there
  (`S21-32`): the section substitutes `x_n = y_n/K_n` with
  `K_{n+1}/K_{n−1} = c_n`, so `K_n` absorbs the product growth by construction
  and the theory that follows is a turning-point theory for `x_n`, with
  `K_0, K_1` left "depending on the particular sequence".

So there is now a contribution statement that rests on a page you hold: **`r_∞`
is the constant that classical method sets aside in order to reach turning-point
behaviour, made explicit.** That framing survives either outcome in B2 — if
Wong–Li states `s`, the exponent was never the claim; if it does not, you have
both.

## B4. The two routes

**Buy.** Wiley pay-per-view against the DOI. Fastest, and it closes the gate
outright. Note that a purchased copy is licensed to you for reading — it does
**not** become a redistributable `refs/` file, and would enter the manifest as
NOT REDISTRIBUTABLE, like the AIF article.

**Write the NOT OBTAINED line and move on.** Defensible *because* of B3. It
would read, in the honest form this record uses:

> Whether the exponent formula appears in Wong & Li (1992, II) was **NOT
> ESTABLISHED**: the article is paywalled (Wiley HTTP 403) and was not
> obtained. The contribution is stated relative to what was read.

What you must **not** do is leave it implicit. An unstated gap reads as a
novelty claim.

**Recommendation, weakly held:** buy it. Not because the framing needs it, but
because B2's second question — whether the constant is given in closed form — is
the one thing that could still overturn `K`, and it is the last unread source
that plausibly bears on it. B3 makes the deposit safe either way; it does not
make the question go away.

---

## Order

1. **A0–A5.** The notice has been ready for several rounds and the record is in
   order; nothing about Part B blocks it.
2. **B.** Then the Wong–Li decision, either way.
3. Then the mathematics: leaf verification (`S16-15`, 30-digit threshold) and
   `S_{ζ*}`, scoped **together** — they share the Stokes-data machinery.

One open lead for that last item, from this round's page reads: v1.2 printed
p. 8 normalises the Borel transform with **Γ(n)**, not `n!`, and takes the
**full** Stokes jump, not half. Since `ζ* = 2ξ₀` exactly, the half-versus-full
prescription is where the factor of 2 would come from. That is a **lead, not a
result.**
