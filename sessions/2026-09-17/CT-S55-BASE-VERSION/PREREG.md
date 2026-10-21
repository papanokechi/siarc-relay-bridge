# PREREG — CT-S55-BASE-VERSION

Written before any computation on the downloaded artefacts, other than the
byte-length/md5 listing already performed to confirm the downloads are
authentic (recorded in §6 below).

## 1. The question

Which version of the manuscript does *Letters in Mathematical Physics* hold for
MATH-D-26-00523?

CT-S52 built its revision against a base it identified as **24 pages**. The
operator's reading of the Editorial Manager PDF reports **25** manuscript pages
and a manuscript link reading `vquad-periodrep-paper-v1.2.pdf`. If LMP holds a
version other than the one CT-S52 revised, the revision is built against the
wrong document and every section/line number in the follow-up correspondence is
suspect.

## 2. Hypothesis

**H.** The manuscript body carried inside the Editorial Manager build
(`refs/MATH-D-26-00523-EM.pdf`) is, page for page, one specific version of
Zenodo concept 20719042, and that version is **not** the one CT-S52 revised.

## 3. Observable

Let `norm(t)` be the page text as extracted by PyMuPDF, with all runs of
whitespace collapsed to a single space and leading/trailing space stripped.

### 3.0 The Editorial Manager overlay, and the rule for removing it

*Added before any observable was evaluated, after a structural probe of the EM
file. The probe is recorded here in full so the amendment is auditable.*

Editorial Manager does not hold the author's PDF unaltered: it re-stamps every
manuscript page. The probe found two overlay components:

1. A trailing block of standalone line-number lines, `1, 2, 3, … , N`, appended
   after all manuscript content on every body page.
2. On the first body page only, a download-link block immediately before that
   run: a line `Manuscript`, a line containing
   `Click here to access/download;Manuscript;vquad-periodrep-`, and its
   continuation `paper-v1.2.pdf`.

Exact page-text equality is therefore impossible without removing the overlay,
and a stripping rule can manufacture a match if it is allowed to remove
whatever stands in the way. `strip_em(t)` is therefore fixed as follows and is
permitted to remove nothing else:

- **S1.** Remove the maximal *trailing* run of lines that are blank or match
  `^\d{1,2}$`. The removed integers, read in document order, must be exactly
  `1, 2, …, N` for some `N ≥ 20`; if they are not, **REFUSE** (F5). The rule may
  not remove a numeric line that is not part of such a run, which is what
  preserves the manuscript's own page number at the foot of its title page.
- **S2.** If, in what remains, a line contains
  `Click here to access/download`, truncate at the line before it, and then
  drop one further trailing line if it is exactly `Manuscript`. At most one such
  truncation per page.
- **S3.** No other content is removed. `strip_em` is applied **only** to pages of
  the EM file, never to a candidate — the candidates carry no overlay, and
  stripping both sides would let the rule erase a genuine difference.

For each candidate `v ∈ {1.0, 1.1, 1.2, 1.3}` (Zenodo records 20719043,
21410927, 21412469, 22731371):

- `O_pages(v)` = page count of `v`.
- `O_match(v)` = the number of index positions `i` for which
  `norm(EM_body[i]) == norm(v[i])`, where `EM_body` is the EM PDF with its
  leading Editorial Manager cover pages removed.
- `O_full(v)` = True iff `O_pages(v) == len(EM_body)` **and**
  `O_match(v) == O_pages(v)`.

The EM cover-page count is determined, not assumed: `EM_body` begins at the
first page whose normalized text contains the manuscript's running title in
small-caps form (`AN EXPLICIT EXPONENTIAL-PERIOD REPRESENTATION`) together with
the word `Abstract.`, i.e. the manuscript's own title page.

Secondary observable:

- `O_name` = the set of strings matching `vquad-periodrep-paper[-A-Za-z0-9.]*\.pdf`
  occurring anywhere in the EM PDF's extracted text.

## 4. Predictions, fixed in advance

- **P1.** Exactly one candidate satisfies `O_full(v) == True`.
- **P2.** `len(EM_body) == 25`, and at least one candidate has a page count of
  24, so that page count alone separates some candidates from the EM body.
- **P3.** `O_name` contains `vquad-periodrep-paper-v1.2.pdf`.
- **P4.** The unique candidate satisfying `O_full` is **v1.2** (record 21412469).
- **P5.** The PDF CT-S52 used as its base
  (`sessions/2026-09-17/CT-S52-XI0-LOGS-REVISION/` base artefact) is byte-identical
  to one of the four candidates, and it is **not** the candidate identified by P4.

P3 and P4 are separate on purpose. The filename string is what Editorial
Manager was *told*; the page-for-page text match is what the file *is*. A
disagreement between them is itself a finding, not an error to be smoothed over.

## 5. Falsifiers, with thresholds

- **F1.** `O_full(v)` is True for zero candidates, or for two or more.
  → The observable does not identify the base. HALT and report exactly that;
  do not fall back to "closest match".
- **F2.** Any two distinct candidates `v ≠ w` have identical full normalized
  text. → The observable cannot discriminate between them. HALT.
- **F3.** The computed md5 of any downloaded reference differs from the md5
  reported by the Zenodo API for that file. → The reference is not what it
  claims to be. REFUSE.
- **F4.** The EM body-start page cannot be located by the §3 rule, or is located
  more than once. → The body/cover split would have to be assumed. HALT.
- **F5.** On any EM body page, the trailing numeric run removed by S1 is not
  exactly `1, 2, …, N` with `N ≥ 20`. → The stripping rule is removing something
  it was not designed to remove. REFUSE.

A falsifier firing is a reportable finding. No threshold in this file is to be
changed after results are seen.

## 6. Ordering rule (CT-S47)

The observable is evaluated **first**. The vacuity/discrimination block runs
afterwards and guards a PASS only. If the observable has already produced a
finding (a falsifier fired), the vacuity block is reported SKIPPED as moot and
the finding stands. A vacuity check may not convert a real finding into a
refusal.

## 7. Vacuity / discrimination pre-check

Establishing that the instrument can fail:

- **V1 (pairwise distinctness).** For every unordered pair of candidates, the
  full normalized text must differ. This is F2 stated as a control: if it holds,
  a full match against one candidate genuinely excludes the others.
- **V2 (negative control).** Take the EM body and replace one page's text with
  the text of the page after it. The perturbed body must satisfy
  `O_full(v) == False` for *every* candidate, including the winner. If the
  winner still matches, the observable is insensitive to page content.
- **V2b (the stripping rule cannot manufacture a match).** Re-run the whole
  observable with `strip_em` replaced by the identity. Every candidate must then
  score `O_full == False`. This shows the match is produced by the manuscript
  content surviving the overlay, not by the rule; and, taken with V2, that the
  rule is neither too weak nor strong enough to erase a real difference.
- **V3 (graded observable).** Report `O_match(v)` for all four candidates, not
  merely the boolean. Two versions that differ by a one-line edit will match on
  most pages; the graded count shows how near the runner-up is and therefore how
  much the verdict rests on.

## 8. Authenticity of references (already performed)

Downloaded 2026-09-21 from the Zenodo REST API, concept 20719042,
`all_versions=true`. The API response is stored verbatim at
`refs/zenodo-20719042-versions.json`. Computed md5 of each downloaded file
against the API's reported md5:

| version | record | file | bytes | md5 (computed == API) |
|---|---|---|---|---|
| 1.0 | 20719043 | vquad-periodrep-paper.pdf | 773171 | 99faea5b0f4095788e4ee932436beeda |
| 1.1 | 21410927 | vquad-periodrep-paper-v1.1.pdf | 775400 | 7feaf94c05a1815a9e8a0ea04561f834 |
| 1.2 | 21412469 | vquad-periodrep-paper-v1.2.pdf | 778209 | 792107efab6317e8ae21e2ca20f092ff |
| 1.3 | 22731371 | vquad-periodrep-paper.pdf | 784836 | 943545955c2951a9592759862230e46a |

The script re-verifies these against the stored JSON by exact field path
(`hits.hits[].files[].checksum`), not by key-name search, and refuses on
mismatch (F3).

## 9. Scope, stated in advance (Amendment H)

This session settles **which file LMP holds**. It does *not*:

- rebase CT-S52's revision onto that file;
- re-check any section or line number quoted in the correspondence;
- apply the §5 edits prepared in CT-S54 REPORT.md §10.

Amendment H sweep obligation: the commissioning question is "is CT-S52's base
the wrong document?" The same defect class — *an artefact identified by
filename or by memory rather than by content* — is swept for across the other
manuscript artefacts in the tree, and the sweep's result is reported whether or
not it finds anything.

## 10. Nothing is sent, uploaded, submitted or deposited

Read-only HTTP GETs against public Zenodo records only. No token is used and
none is present.
