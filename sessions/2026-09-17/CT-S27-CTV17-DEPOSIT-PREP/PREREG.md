# PREREG — `CT-S27-CTV17-DEPOSIT-PREP`

**Written before any check was run.** Session id verified free against the tree
before use: `sessions/2026-09-17/` holds `CT-S26-CTV17-DRAFT` and
`CT-S26-UPPER-BOUND` — the doubled id is **26**, not 27 — and no `CT-S27*`
exists anywhere in the repository.

**Draft and preparation only. No deposit, no upload, no metadata edit, no
publish. Every irreversible action is operator-gated.**

---

## 1. Hypothesis

The v1.7 packet can be brought to a state where **every value that would be
typed or uploaded has been checked against the deposited record and against the
file actually staged**, so that the two defect classes that each cost a round at
the previous deposit cannot recur:

1. **The filename defect.** At the v1.3 companion deposit the file was uploaded
   from a shelf name — `vquad_resurgence_v1.2_zenodo-20481592.pdf` — embedding
   record `20481592` in a file published on record `22831933`. Its **bytes were
   correct**; only the label was wrong, and Zenodo states file addition, removal
   or modification are not allowed after publishing.
2. **The hash defect.** A hash taken before the final edit points at nothing.
   The hash must be computed from the **staged file on disk, after the last
   edit**, and verified against the file in the upload dialog.

## 2. Observable

`scripts/preflight_deposit.py` returns a per-check PASS/FAIL over four groups —
staging, hash discipline, metadata agreement, deposit shape — each check reading
a file on disk and comparing it against either the **deposited v1.6 record** or
the **staged artefact**, never against this document's prose.

## 3. Falsifier

**Any** check failing blocks the deposit. There is no threshold to tune and no
partial credit: this is a gate, not a measurement. In particular the packet is
**NOT READY** if:

- the staged filename differs from the declared publishable name, contains
  `draft` in any case, or embeds any Zenodo record id;
- the staged bytes differ from the source notice;
- the hash recorded in `DEPOSIT-FORM.md` differs from the hash of the staged
  file on disk;
- any metadata value differs from the deposited v1.6 record without the form
  declaring the change deliberate **and saying why**;
- the concept DOI is given as anything other than the `conceptdoi` field read
  from the record;
- the deposit shape names a file that is not held.

## 4. Vacuity pre-check

Every check must be shown to **fail on a mutated input** before its pass is
worth anything. `SECTION 2` of the pre-flight mutates the *staged artefact and
the form*, not this prose:

- a staged file renamed `DRAFT-channel_theory_v1.7_version_notice.md`;
- a staged file renamed to carry a record id, reproducing the v1.3 defect
  exactly;
- a form carrying the hash of the **previous** revision of the notice;
- a form carrying the affiliation `Independent researcher, Yokohama, Japan`
  against the record's `Independent Researcher`, reproducing the v1 affiliation
  drift;
- a form giving the **version** DOI where the concept DOI belongs;
- a form with a keyword dropped and one with the v1.6 title restored at v1.7.

If any mutant is accepted, that check is **BROKEN** and reported as such; the
pre-flight does not pass on unfired controls.

**Basis-degeneracy note.** This session runs no integer-relation search, so
proposed Amendment A does not apply. It is named here so that the omission is a
decision rather than an oversight.

## 5. Reader integrity

Per proposed Amendment C, every file read asserts a **known-present** feature
before any absence or count is evaluated, and the pre-flight includes defective
readers among its controls. A check that reports "the form does not carry the
hash" must not be able to mean "I could not read the form".

## 6. Halt conditions

Stop and report rather than improvise if:

- a required value cannot be read from the deposited record;
- the deposit shape cannot be determined from the tree (**this has already
  fired — see §7**);
- any irreversible action would be needed to make a check pass.

## 7. Known blocker, recorded before the pre-flight was written

**The v1.7 outline PDF cannot be built from this repository.** The v1.6 record
publishes exactly one file, `channel_theory_outline.pdf` (609 300 B, md5
`aa56a94a9354b5533b04c89461950eb1`), and the newest Channel Theory LaTeX source
in the tree is **v1.3.1**
(`sessions/2026-05-08/T1-OPERATOR-CT-V131-…/channel_theory_outline_v131_with_r1a_caveat.tex`).
There is no v1.4, v1.5 or v1.6 source anywhere in the repository, and the two
PDFs could not be downloaded (HTTP 504).

So a v1.7 deposit **cannot** take the normal shape of "rebuild the outline and
upload it". The shape is an **operator decision** and is recorded as UNDECIDED
in `DEPOSIT-FORM.md`. The pre-flight checks that the form does not name a file
it does not hold — it must not become a promise.

## 8. What this session will NOT do

No upload, no publish, no new-version draft on Zenodo, no metadata edit, no
DataCite write, no commit. Read-only `GET` traffic only, and none is required:
every record value used here is already held in `CT-S26-CTV17-DRAFT/refs/`.
