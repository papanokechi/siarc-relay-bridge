# REPORT — CT-S27-CTV17-DEPOSIT-PREP

**Deposit preparation for Channel Theory v1.7. No deposit, no upload, no
metadata edit, no commit. Nothing irreversible was done or attempted.**

The commission was "Packet B, renumbered to avoid the CT-S27 collision if that
id is now taken, checked against the tree first." The tree was checked first:
the doubled id is **CT-S26** (`CT-S26-CTV17-DRAFT` and `CT-S26-UPPER-BOUND`);
**`CT-S27` was free**, so no renumbering was needed and none was invented.

---

## 1. What was done

1. Checked the session tree for an id collision. None at CT-S27.
2. Read the deposited v1.6 record (`refs/zenodo_22782807.json`, held from the
   previous session) for every metadata value — not the working tree.
3. Decided the **publishable filename before staging** and staged the notice
   under exactly that name, byte-identical to its source.
4. Wrote `PREREG.md` — the gate, its falsifier, the six named mutants, and the
   known blocker — **before** writing the checker.
5. Wrote `DEPOSIT-FORM.md`: every value that would be typed, each tagged
   `same-as-v1.6` or `deliberate-change`, plus the deposit-shape analysis.
6. Wrote and ran `scripts/preflight_deposit.py`. **Run 1: GATE BLOCKED**, two
   failures. Repaired, one to the artefact and two to the checker, each
   disclosed separately below. **Run 2: GATE PASSED**, 12/12, 0 broken, 3/3
   reader controls.
7. Consolidated the four P0 amendments into `P0-AMENDMENTS-ABCD.md` for a
   single ruling pass, reproducing the clause text verbatim and **without
   editing either originating file**.
8. Emitted five claims; ran the corpus invariant check and took a backup.

---

## 2. Claims

| id | label | claim, in one line |
|---|---|---|
| `S27-01` | VERIFIED | The packet is internally consistent: 12/12 gate checks, 19 artefact mutants rejected, 3/3 reader controls. The deposit is still blocked. |
| `S27-02` | VERIFIED | The form declared 28 keywords; the record has 27. The gate caught it; the **form** was corrected, not the check. |
| `S27-03` | VERIFIED | An ASCII-only sentinel set cannot detect a wrong-codec read. The latin-1 reader control did not fire until a non-ASCII sentinel was added. |
| `S27-04` | VERIFIED | `D2` first confirmed its own hypothesis from an empty search of the wrong directory; the reader-integrity clause caught it. |
| `S27-05` | INSPECTED | No deposit shape is executable from this repository. |

---

## 3. The gate, and what it is for

`preflight_deposit.py` is a **gate, not a measurement**: no thresholds, no
partial credit, any FAIL blocks. It exists to stop two defect classes that each
cost a round at the previous deposit.

**The filename defect.** A file was uploaded from a shelf name embedding a
*different* record's id. The bytes were correct; the label was not; and
filenames are immutable after publishing, so a content check could never have
reached it. `A1` therefore rejects, mechanically: any casing of `draft`, `copy`,
`final`, `new`, `tmp`, `temp`, `untitled`; any run of six or more digits (a
record id); any uppercase; any whitespace or parenthesis (the browser's `(1)`);
and any extension other than `.md`. Three mutants, one per sub-case.

**The hash defect.** `B1` recomputes the hash **from the staged file on disk**
and compares it to the declared value. Its first mutant is the **actual sha256
of revision 2 of the notice** — a hash taken exactly one edit too early. `B2`
goes further and requires the staged file to be the revision the content
checker passed, by reading the hash out of `verify_notice_rev3.out.txt`
together with its `0 failed / 0 broken` lines.

`C1`–`C5` diff every metadata value against the deposited record: title,
version, creator, affiliation, licence, keyword count, and the concept DOI —
which is read from the record's `conceptdoi` **field**, with a mutant that
supplies the version DOI instead and another that supplies a DOI built from the
record number.

`D1` enforces the one rule that keeps the blocker honest: **the form must not
name a file it does not hold.**

### 3.1 What GATE: PASSED does not mean

The last line of the output is `DEPOSIT READY: NO.` The gate certifies the
**packet** — filename, bytes, hash and metadata all agree with the record. It
says nothing about whether a deposit can proceed, and §5 is why.

---

## 4. Three findings, disclosed separately

### 4.1 The form was stale against the record (artefact defect — `S27-02`)

`DEPOSIT-FORM.md` declared `keywords_count: 28`. The held v1.6 record carries
**27**. The 28 was carried forward from an earlier version and had never been
checked against the deposited text.

**The correction was to the form. The check was not touched, and no threshold
moved.** Its mutant was changed from `27` to `26` for the obvious reason: once
the form is correct, a mutant asserting the true value is not a mutant.

This is the same class as the previous session's stale-repository finding, in
the same direction — the working copy behind the record — arriving in metadata
rather than prose. It is the second time proposed Amendment D has earned its
keep before being ruled on.

### 4.2 `D2` confirmed the blocker from an empty search (check defect — `S27-04`)

`D2` asserts that no v1.4–v1.6 Channel Theory source exists. The first
implementation walked `sessions/2026-09-17/` — this date's folder — found **zero
Channel Theory sources**, and by its own logic would have reported the blocker
confirmed. The sources live under `sessions/2026-05-*`.

It did not report that, because the reader-integrity clause made "found nothing
at all" a **failure** rather than a confirmation. Re-rooted at `sessions/`, it
finds 9 sources, newest v1.3.1, and the blocker holds — now on evidence rather
than on an empty search.

This is the exact shape the proposed Amendment C was written for, with the
polarity that makes it dangerous: the defect would have **confirmed** the
conclusion, not contradicted it. A check that agrees with you for the wrong
reason produces no symptom.

### 4.3 An ASCII sentinel set cannot detect a wrong codec (check defect — `S27-03`)

The three reader controls scored **2 of 3** on the first run: the latin-1
misread was not caught. All four known-present sentinels were ASCII, and ASCII
survives a wrong-codec decode unchanged — the mojibake lands only in the
non-ASCII characters, which no sentinel covered. Adding the non-ASCII sentinel
`ξ₀ = 2/√β₂` from the title line made it fire, 3 of 3.

Offered as a sub-clause of Amendment C. It is the fourth instance this run of
*a control must be able to reach the thing it controls*.

---

## 5. What was NOT established — the blocker

**No deposit shape is executable from this repository** (`S27-05`). The v1.6
record publishes one file, `channel_theory_outline.pdf`.

| shape | needs | status |
|---|---|---|
| A — description-only, re-upload the v1.6 PDF | the v1.6 PDF | **not held**; both PDF fetches returned HTTP 504 |
| B — v1.6 PDF plus the notice as a second file | the v1.6 PDF | **not held** |
| C — rebuild the outline at v1.7 | v1.4–v1.6 LaTeX | **absent**; newest held source is v1.3.1 |

Shape C is the only one producing a self-consistent record, and it is the one
the repository cannot support. **Rebuilding from v1.3.1 would silently revert
two versions of corrections** — including the Painlevé-target correction made at
v1.4 and the analytic residual added at v1.6, both of which this very notice
depends on. That is not a shortcut to be taken under time pressure; it would
deposit the stale copy as the current text.

`DEPOSIT-FORM.md` records `deposit_shape: UNDECIDED` and the gate verifies the
form names no file it does not hold. **No check can make this pass.**

Also not established: whether `S_{ζ*}` passes v1.6's vacuity pre-check (§9's
thresholds remain unread — the notice points at them by version DOI and does not
restate them); and a closed form for `K`, Wong–Li II being NOT OBTAINED.

---

## 6. Open questions for the operator

1. **The deposit shape.** The decision is yours and it needs material this
   repository does not have. Three ways out: (a) re-attempt the v1.6 PDF fetch
   later — a 504 is transient and the earlier attempts may simply have been
   unlucky; (b) locate the v1.4–v1.6 LaTeX outside the worktree, where the
   `CT-S22-DEPENDENCE-LIT` record also turned out to live; (c) rule that v1.7 is
   a **description-only** edit to the existing record rather than a new version,
   which needs no file at all — but that changes what v1.7 *is*, and it is not a
   ruling this session should infer.
2. **The four P0 amendments**, A–D, consolidated in `P0-AMENDMENTS-ABCD.md`,
   with C carrying one sub-decision (whether the non-ASCII-sentinel line is part
   of C or a separate note).
3. **`CT-S23` arm (i)'s graded observable**, item 5, still open from earlier.
4. Whether §4.2's polarity point — *a check that agrees with you for the wrong
   reason produces no symptom* — warrants its own clause, or is adequately
   covered by Amendment C as drafted.

---

## 7. Uncommitted files

All work is uncommitted; `sessions/2026-09-17/` remains untracked and HEAD is
unchanged.

### Created in `sessions/2026-09-17/CT-S27-CTV17-DEPOSIT-PREP/`

| file | note |
|---|---|
| `PREREG.md` | written before the checker; unedited since |
| `DEPOSIT-FORM.md` | §5 records the post-FAIL correction to `keywords_count` |
| `P0-AMENDMENTS-ABCD.md` | consolidated for one ruling pass; edits nothing |
| `REPORT.md` | this file |
| `claims.jsonl` | 5 claims |
| `scripts/preflight_deposit.py` | the gate |
| `scripts/emit_claims.py` | append-only; asserts verdicts and hashes from disk |
| `outputs/preflight_deposit.out.txt` | **run 1, BLOCKED** — the evidence of the catch; cited by `S27-02` and `S27-03`; must not be overwritten |
| `outputs/preflight_deposit_r2.out.txt` | run 2, PASSED; cited by `S27-01`, `S27-04`, `S27-05` |
| `upload/channel_theory_v1.7_version_notice.md` | staged under its publishable name, byte-identical to the source |

Run 2 was written to a **new** filename rather than over run 1, per proposed
Amendment B: run 1 is the only record of the two failures and three claims point
at it.

### Not modified

No file outside this session folder was changed. `CT-S22-STOKES/P0-AMENDMENT.md`
and `CT-S26-CTV17-DRAFT/P0-AMENDMENT.md` are **pointed at, not edited**; the
notice itself was not touched in this session.

> **Superseded at §8.** The statement above was true when written. It is no
> longer: the operator subsequently directed that the build carry-over line be
> added to the notice, which is a cross-session edit. It is trailed in §8.

### Added since (§8 and §9 rounds)

| file | note |
|---|---|
| `WALKTHROUGH.md` | the requested upload walkthrough; stop points S1–S6, irreversible step marked |
| `DESCRIPTION-v1.7-rev2.html` | **the only thing v1.7 publishes**; `026e7a9e…`, 54 068 chars |
| `P0-AMENDMENT-E.md` | **PROPOSED, unruled** — mutant provenance |
| `scripts/make_description.py` | generator; `PROVENANCE_RULES`, `strip_internal_provenance`, `strip_claim_ids`, `BIBLIOGRAPHY` |
| `scripts/verify_description.py` | **16 checks** `T1–T5 X1–X2 N1–N4 B1–B3 P1–P2` |
| `scripts/preflight_deposit_rev2.py` | the gate, repointed; check count now parsed, not hard-coded |
| `scripts/doi_probe_v17.py` | resolves every identifier; §2 is the poison control |
| `scripts/postpublish_readback.py` | read-only, no token; run once after publish |
| `scripts/selftest_readback.py` | 1 good + 10 negative fixtures, tested offline |
| `scripts/emit_claims_walkthrough.py`, `scripts/emit_claims_strip.py` | append-only; hashes taken from disk |
| `outputs/…_r2…_r7.out.txt` | every revision written to a **new** filename; **no output was ever overwritten** |

**Deleted:** `DESCRIPTION-v1.7.html` (rev 1, so two paste-candidates could not
be confused) and `outputs/_fixtures/`.

---

## 8. The walkthrough round

The operator asked for the Zenodo upload walkthrough. Writing it required
reading the flow from the source rather than from memory, and that reading
changed the procedure in one material way. Producing the walkthrough's artefacts
then exposed **four defects in this session's own work**, two of them in checks
that had already passed.

### 8.1 The deliverable

`WALKTHROUGH.md` — the click-by-click, with six numbered stop points, the
irreversible step marked, a failure table, and a closing section on what it
does *not* do. It is a procedure, not an authorisation; nothing in it has been
executed.

### 8.2 One deliberate departure from Zenodo's guidance (claim S27-12)

`help.zenodo.org` says versioning is for updated **files**, and that a
metadata-only change should use **Edit**. By that default a description-only
change is an Edit.

**The walkthrough refuses that, and says so in print.** An Edit overwrites
v1.6's description — the deposited erratum text that adopted Amendment D makes
authoritative. It would destroy the primary source in order to publish a note
about it. And the record has already ruled the class in its own words: v1.6's
description records that its defect (1) is *"repaired by a new version rather
than by a metadata edit."*

So: **New version**, then **Import files** (a new version draft starts with **no
files** — the step most easily missed, and S2 in the walkthrough). `Edit` must
not be clicked, and the walkthrough says how to tell you are in the wrong place.

### 8.3 Four defects found, two in checks that had passed

**(1) 77 double-escaped entities (S27-06).** The description that passed 13/13
would have published the literal text `&mdash;` in every table row. Rows were
joined by `" &mdash; "` and *then* escaped. **T4 could not see it** — `&amp;mdash;`
is well-formed HTML4 with no bare ampersand. The defect is wrong at the
*rendered* layer, not the markup layer. Found by reading the output, not by a
check. New check **T5** tests rendered text; 2/2 mutants rejected.

**(2) X2 passed on published draft-stage language (S27-07).** The description
ended *"End of draft v1.7 notice. Draft only — no deposit, no metadata edit."*
X2 exists to stop exactly that. It matched four literal strings
case-sensitively; the text read `Draft only`, matching none.

The sharper half: **X2's mutant was drawn from X2's own string list.** It
inserted `DRAFT ONLY. Not deposited.` — so it could only ever prove the list is
*consulted*, never that the list is *adequate*. A mutant built from the constant
it tests is not an independent control, and this is the third input-path class
this run has met after the CRLF reader and the latin-1 sentinel.

Repaired to a case-insensitive word-boundary pattern with an explicit
**quotation allowance**, and given three mutants none of which appears in the
pattern. All three are rejected; **the first is verbatim the sentence that got
through.** Four `draft` occurrences remain and are allowed — all four are in the
single v1.6 erratum sentence quoting the watermark `DRAFT — NOT DEPOSITED` of
the build it repairs.

**(3) The gate refused the repair, correctly (S27-09).** S3 pairs the
description on disk with the checker output that passed it, and reported the
mismatch rather than accepting a repaired file on a stale certificate. It now
also requires `checks run     : 14`, so a stale output from a *smaller* check
set is rejected instead of accepted.

**(4) The self-test harness could not read its own subject (S27-11).** The
failure parser was `r"\[FAIL\] ([^-]+?) --"`, which stops at the first hyphen —
so `the load-bearing sentences survived` was unreadable. The check **fired**;
the harness reported **BROKEN**. Mutant testing cannot reach this, because a
broken reader misreads the mutant too. Caught only because one arm disagreed
with the nine that passed.

### 8.4 The readback, tested before it can be needed (S27-10)

`postpublish_readback.py` runs **once**, after an irreversible publish, against
a record that does not exist yet. It cannot be debugged when it matters. So it
was given a fixture mode and exercised offline against **1 good and 10 negative
fixtures** built from the held v1.6 record — files not imported, a second file,
a `DRAFT-` filename, wrong build bytes, version left at 1.6, a truncated
description, a lost load-bearing sentence, affiliation drift, a dropped keyword,
and the concept DOI overwritten. Good passes; **all 10 negatives rejected, each
on its own named check.** It is read-only and needs no token.

### 8.5 The description is now rev 2

| | rev 1 | rev 2 |
|---|---|---|
| file | `DESCRIPTION-v1.7.html` | `DESCRIPTION-v1.7-rev2.html` |
| sha256 | `e8b3f36f…` | `0478e3c9…` |
| chars | 54 164 | 53 700 |
| paragraphs | 163 | 162 |

Rev 1 was **deleted**, not kept. Two candidate paste-files in one folder is the
same hazard class as the wrongly-named upload that cost a round at the previous
deposit — and the evidence of its defects is preserved in `outputs/`, which is
where evidence belongs. No existing output file was overwritten: every re-run
wrote a new name.

### 8.6 Cross-session edit, trailed

`CT-S26-CTV17-DRAFT/NOTICE-v1.7.md`, **rev 3 → rev 4** (`75cd3476…` →
`a0bb2b84…`, 47 699 → 48 710 B), on the operator's direction, adding the
description-only shape statement and the "no v1.7 build is claimed" bullet.
Re-verified to a **new** output `verify_notice_rev4.out.txt`: 26/26, 0 failed,
0 broken, 3/3 reader controls.

### 8.7 State

| | |
|---|---|
| `verify_description.py` | **14/14**, 0 broken, 3/3 reader controls, entity round trip 28/28 |
| `preflight_deposit_rev2.py` | **11/11**, 0 broken, 3/3 reader controls, **GATE: PASSED** |
| `selftest_readback.py` | good fixture passes, **10/10** negatives rejected |
| claims | 12 in `claims.jsonl` (`S27-06`…`S27-12` this round) |

**Nothing is committed, uploaded, deposited or edited on Zenodo. No token has
been used. Publishing remains operator-gated.**

### 8.8 The one item still needing a ruling

The generated description retains §9's *"Sources held and hashed"* table, which
names `refs/` paths, `.py` script names and `CT-S*` session ids. **No deposited
description in this record has ever carried those.** (v1.6 carries `sessions/`
paths, but no `refs/` path, script name or session id.)

It was left in and flagged rather than silently stripped, because whether to
publish repository-internal paths is a judgement, not a check. Removing it is a
one-line addition to the exclusion rules in `make_description.py`, after which
both gates must be re-run. **Operator decision.**

**Ruled, 2026-09-19. See §9.**

---

## 9. The provenance strip

### 9.1 The ruling

> Strip it, but not entirely. […] What should stay is the **bibliographic**
> half of that table: for each external source, the author, title, venue, DOI
> or URL, and the retrieval date. […] Keep the sha256 values too. […] So the
> rule is: **anything a reader can resolve stays; anything only you can
> resolve goes. DOIs resolve. `CT-S22-STOKES/outputs/...` does not.**

Two consequences were named with the ruling, and both were the real work: any
sentence pointing into §9 *by path* must be reworded to point at the
bibliographic entry, and both gates must be re-run to confirm the removal has
not stranded a citation that now names no source.

### 9.2 What the record decided, rather than preference

Two questions the ruling did not settle were settled by reading v1.6:

1. **Claim ids go too.** The deposited v1.6 description carries **zero** AEAL
   claim ids. The operator's own consistency argument therefore reaches them:
   `S22-22` resolves only against an unpublished tree. 21 inline ids were
   removed. The **epistemic labels** they carried were kept — a label is
   content, the identifier is provenance.
2. **Committed `sessions/` paths resolve.** v1.6 carries a `github.com` URL
   into `sessions/2026-05-02/…`. So the line is not "`sessions/` is internal"
   but *committed and public* versus *uncommitted*: the 2026-09-17 session
   paths genuinely do not resolve for anyone.

27 internal references outside §9 were found and reworded — the second
consequence in full. *(`S27-13`, `S27-18`.)*

### 9.3 The strip is a two-sided guarantee

A residue assertion alone is satisfied perfectly by a strip that deletes the
citations along with the paths. So the guarantee is stated twice, in opposite
directions:

| | |
|---|---|
| `P1` | no unresolvable internal provenance survives — 0 residue |
| `P2` | 11 named resolvable identifiers and ≥8 sha256 values **must** be present |

Both now live in `verify_description.py`, not only in the generator's asserts,
so the property is re-tested on every run rather than at generation time only —
the same move that put `T5` in the verifier. *(`S27-14`.)*

### 9.4 Mutant provenance, applied before it was ruled on

`P1`'s three mutants are verbatim strings that stood in the **pre-strip
notice** — drawn from the source text, not composed from the patterns `P1`
matches on. This is the operator's flagged fifth-amendment principle followed
in advance. It was written up in `P0-AMENDMENT-E.md` and **ADOPTED the same
day**, on two live instances: `X2`'s string list, and `P1` without `P2`. 3/3
and 2/2 mutants rejected. *(`S27-15`, `S27-21`.)*

### 9.5 No identifier in the bibliography is from memory

The corpus had already caught a hallucinated DOI (`10.1007/BF02547452`, offered
for Birkhoff 1930, resolving to a 1995 chemistry paper), so every identifier
was resolved against Crossref or its live URL and printed **with the
resolver's own title**. 10 rows, 0 not fit to publish.

Two results worth stating plainly:

- **Gautschi 1967 → `10.1137/1009002`** was *discovered by title query*, not
  recalled, and was not previously recorded anywhere in the corpus.
- The known-bad DOI is retained as a **poison control** and the probe
  **PASSES** it — by reporting the chemistry paper. A probe that rejected it
  silently would not distinguish a wrong identifier from a dead one.

The held Odlyzko PDF is byte-identical (1 116 716 B) to the file now on the
author's site. Wong & Li II remains **NOT OBTAINED** and the bibliography says
so. *(`S27-16`, `S27-17`.)*

### 9.6 A false positive from my own reader

An audit reported 85 space-before-punctuation defects. The raw HTML contains
**zero**: the audit's own tag-stripping substitutes a space for each tag, so
`</strong>.` reads as ` .`.

Recorded because it is the Amendment C class *in reverse*. C is about a reader
that cannot see a defect; this is a reader that manufactures one. The
corrective is the same — a second, differently-implemented read — and it is the
reason the finding cost minutes rather than a round of edits to correct prose
that was already correct. *(`S27-19`.)*

### 9.7 The gates, re-run

The deposit gate **BLOCKED** on the first post-strip run, correctly: `S2` and
`S3` found the declared hash pointing at bytes that no longer existed. That is
Amendment B doing its job on a file that had been regenerated under it.

After repointing and propagating the new hash to all five sites:

| | |
|---|---|
| `verify_description.py` | **16/16**, 0 failed, 0 broken, 3/3 reader controls, entity round trip 28/28 |
| `preflight_deposit_rev2.py` | **11/11**, 0 broken, 3/3 reader controls, **GATE: PASSED** |
| description | `026e7a9ebef73935…`, 54 068 chars, 54 256 B, 156 paragraphs |

One further repair: `S3` reported *"passed 14/14"* from a **hard-coded
string** while reading a 16-check output. The count is now parsed from the
output it read, so the gate can no longer report a total it did not read. A
small instance of the same rule as B — a number must come from the artefact,
not from when the line was written. *(`S27-20`.)*

### 9.9 A defect of my own, caught by the corpus checker

The first run of `emit_claims_strip.py` appended eight claims carrying the
epistemic label as a **prefix in the claim text** (`"INSPECTED. The published
description…"`) instead of in the `label` **field** the corpus uses. The claims
looked right when read; the corpus checker crashed sorting `None`.

Two things worth keeping:

- The append **succeeded** and reported `appended 8 claim(s)`. Exit status
  again says nothing about whether the right values were written — the same
  rule as B, at a different surface.
- It was caught by a checker **outside** this session. A session-local check
  would have been written by the same hand that wrote the defect.

Repaired by removing the eight lines and re-emitting to a **new** output
(`emit_claims_strip_r2.out.txt`; the malformed run's output is kept as the
evidence). `emit_claims_strip.py` now **asserts** both the label's validity and
that it is not duplicated as a text prefix, so the shape cannot drift silently
again. Corpus checker: 539 claims, all ids unique, **INVARIANTS OK**.

### 9.10 State

| | |
|---|---|
| `verify_description.py` | **16/16**, 0 broken, 3/3, entity round trip 28/28 |
| `preflight_deposit_rev2.py` | **11/11**, 0 broken, 3/3, **GATE: PASSED** |
| `doi_probe_v17.py` | 10 rows, 0 not fit to publish, poison control PASS |
| `selftest_readback.py` | good fixture passes, **10/10** negatives rejected |
| claims | 21 in `claims.jsonl` (`S27-13`…`S27-21` this round) |
| P0 backlog | **zero** — A, B, C (amended and extended), D, E all ruled |

**Nothing is committed, uploaded, deposited or edited on Zenodo. No token has
been used. Publishing remains operator-gated and irreversible.**


---

## 10. The sixth item — the formal type of the operator

### 10.1 What was added

A new **§7, "The formal type of the generating-function operator"**, was
commissioned after two isolated readers, working from page images of van der
Put–Saito pp. 2634–2637 and nothing else, classified the operator

> `L_d := z·b(θ+1) + z²·a(θ+2) − 1`,  `θ = z d/dz`

against Table 2.1. It is published in **three tiers**, deliberately not merged:

| tier | statement | label | independently confirmed |
|---|---|---|---|
| 1 | `D̃₅ / P_V` is **not** compatible with `L_d` for `deg b = 2`, `deg a ≤ 2` | VERIFIED | **yes**, twice |
| 2 | the reachable rows are exactly `PIII(D₈)`, `PIII(D₇)`, `PIII(D₆)` | STRUCTURAL | **yes** |
| 3 | which row is reached depends on `(α₂, α₁)`, codimension-3 exception | STRUCTURAL | **no** |

Channel Theory's own recurrence is `a ≡ 1`, i.e. `e = 0`, so it falls in the
`PIII(D₈)` row.

Tier 3 is published with its provenance: it came from a derivation that
corrected an earlier error of its own, and **both** isolated readings stop short
of the coefficient subloci. The notice says so.

### 10.2 The two things §7 refuses to say

1. **It does not touch the `V_quad` Painlevé-V identification.** `L_d` is the
   operator annihilating a generating function of denominators;
   `op:cc-stokes-closed-form` concerns a connection-coefficient ratio against a
   Riemann–Hilbert datum. They have **not** been shown to be the same object,
   so the exclusion of `D̃₅/P_V` is not evidence about the identification in
   either direction. Saying otherwise would be the one-name-two-objects error
   the notice already forbids for `K` and `S_{ζ*}`, now at the level of objects.
2. **It does not claim family membership.** A matching Katz multiset is
   **necessary, not sufficient**. That is why the exclusions are VERIFIED and
   every positive row is STRUCTURAL. The second reader reached the same
   asymmetry for the same reason, unprompted.

### 10.3 The renumber, and why it needed a script

A new §7 forces 7,8,9 → 8,9,10. But **"§9" in this notice denotes three
different documents**: this notice's sources table (1), §9 of the v1.6 record
(7), and §9 of Birkhoff–Trjitzinsky 1933 p. 69 (2); and "§8" also denotes the
v1.4 EBR deposit's scope statement. A regex pass would have rewritten references
to other people's documents **and still produced a well-formed file**.

`scripts/renumber_notice.py` therefore enumerates three headings (rewritten in
descending order so 8→9 cannot collide with 9→10) and exactly four
self-references, each required to fire **exactly once**, and asserts that all
seven references to other documents are **untouched** — that assertion is the
control, and it is what would fire if the script ever became the blind pass it
exists to avoid. Eight further replacements were needed inside
`make_description.py`, whose own rewrite strings pointed at the sources table by
number; the two that cite *other* works' §9 were left alone.

### 10.4 N5, and why presence alone was not enough

A presence-only check would pass a §7 that said all the right things and then
added one sentence refuting the `V_quad` identification, or one calling a row
match VERIFIED. **N5 is two-sided**: five required features, plus rejection of
any sentence that refutes an identification or attaches VERIFIED/PROVEN to a
family-membership verb. Per **Amendment E**, its two load-bearing mutants are
drawn from those failure modes, not from its own required-string list; the third
is an ordinary deletion mutant for the presence half. All three were rejected.

### 10.5 The stale hash was caught by the gate

Regenerating took the description from **54 068 → 63 123 characters**.
`preflight_deposit_rev2.py` check **S2 failed immediately**, naming the declared
hash as pointing at nothing — exactly the failure that has cost a round twice
before, caught this time by the gate rather than by inspection. Nine sites
across `DEPOSIT-FORM.md` and `WALKTHROUGH.md` were then updated in one validated
pass, which also moved the paste-completeness stop point from §9 to §10 and the
size ratio from 2.3× to 2.7×. Both files are CRLF; line endings were preserved
by normalising once after decoding.

### 10.6 State after this round

| item | state |
|---|---|
| notice source | `NOTICE-v1.7-rev2.md` in **this** session; the CT-S26 original is untouched |
| sections | §0–§10, all present, no stranded self-reference |
| description | `DESCRIPTION-v1.7-rev2.html`, 63 123 chars, sha256 `39903126…` |
| `verify_description.py` | **17/17**, 0 broken, 3/3 reader-integrity controls |
| `preflight_deposit_rev2.py` | **GATE: PASSED**, 11 checks, 0 failed |
| bibliography | 16 rows; van der Put–Saito added with its own identifier and sha256 |
| claims | 27 in `claims.jsonl` (`S27-22`…`S27-27` this round) |
| cold-read record | 20 claims in `C:\LocalWork\SCOPE\CT-S30-PACKET-BUILD\claims.jsonl` (`S30-15`…`S30-20` this round) |

**Nothing is committed, uploaded, deposited or edited on Zenodo. No token has
been used. Publishing remains operator-gated and irreversible.**
