# PREREG — CT-S56-REBASE-V12

Written before any observable is computed. Thresholds fixed here are not revised
after seeing results; if one proves ill-posed that is reported as a finding.

Date: 2026-09-21
Session: sessions/2026-09-17/CT-S56-REBASE-V12/

## 1. Context

CT-S55 settled, by two independent routes, that *Letters in Mathematical Physics*
holds **v1.2** of the V_quad period-representation paper for submission
MATH-D-26-00523:

- Zenodo record 21412469, md5 `792107efab6317e8ae21e2ca20f092ff`, 778209 bytes,
  25 pages;
- the Editorial Manager manuscript item (id 60154) is byte-identical to it.

CT-S52 prepared a revision against a base it identified by filename, which CT-S55
refuted: that base is **v1.0** (md5 `99faea5b0f4095788e4ee932436beeda`, 24 pages).

The operator's instruction for this session is explicit:

> Locate its LaTeX source by rebuilding and matching content against this PDF.
> If no source in the tree rebuilds to v1.2, STOP and report; do not reconstruct
> v1.2 from v1.0 plus edits.

So Stage 1 below is a **gate**, not a step. Everything downstream (the two diffs,
the re-application of CT-S52's items, item 5, the sweep) is conditional on the
gate passing. This document pre-registers the gate before it is run, so that a
negative result cannot be argued away afterwards.

## 2. Hypothesis

**H.** Some LaTeX source present in the repository, when rebuilt with the build
procedure stored alongside it, produces the PDF that LMP holds (v1.2).

**H0 (null).** No source in the tree rebuilds to v1.2; the tree's V_quad sources
correspond to v1.0 and to two pre-v1.0 states only.

## 3. Candidates

Enumerated by locating every `vquad-periodrep-paper.tex` in the tree. Six source
directories, each carrying its own `build.py`:

| id | directory | tex bytes | stored PDF md5 |
|----|-----------|-----------|----------------|
| C1 | sessions/2026-06-15/VQUAD-PERIODREP-PAPER-001 | 82159 | 7f1cd431156df0a0db5ed9db8a501f95 |
| C2 | sessions/2026-06-16/VQUAD-PAPER-CORRECTIONS-001 | 87354 | 028a1a5d9e10a3a9487596f6db3e6a38 |
| C3 | sessions/2026-06-16/VQUAD-PAPER-LAYOUTFIX-001 | 87778 | 99faea5b0f4095788e4ee932436beeda |
| C4 | sessions/2026-06-16/VQUAD-REPRO-BUNDLE-001/vquad-periodrep-bundle | 82159 | 7f1cd431156df0a0db5ed9db8a501f95 |
| C5 | sessions/2026-06-16/VQUAD-REPRO-BUNDLE-002/vquad-periodrep-bundle | 87354 | 028a1a5d9e10a3a9487596f6db3e6a38 |
| C6 | sessions/2026-06-16/VQUAD-REPRO-BUNDLE-002/run-2/vquad-periodrep-bundle | 87778 | 99faea5b0f4095788e4ee932436beeda |

C7, listed separately because it is not a candidate for the base but must be
characterised: `sessions/2026-09-17/CT-S52-XI0-LOGS-REVISION/revision/` — CT-S52's
edited copy, 93132 bytes, derived from C3.

A stored PDF hash is **not** the observable. A source can have been edited after
its PDF was last built, so the stored PDF may not be what the source produces.
The observable is what the source produces **now**.

## 4. Observable

For each candidate, copied into a scratch directory (never built in place, so no
earlier session's files are modified):

1. run its `build.py` with `SOURCE_DATE_EPOCH` fixed at the value the script
   itself sets (`1718409600`), pdflatex twice, as the script does;
2. record `md5(built.pdf)`, byte length, and page count;
3. **byte observable** `B(c, v)`: 1 if the built PDF is byte-identical to
   published version `v`, else 0;
4. **content observable** `M(c, v)`: the number of pages whose normalised text is
   identical, comparing the built PDF page-for-page against `v`.

Normalisation, fixed here: decode each page's text, strip trailing whitespace on
every line, collapse internal whitespace runs to one space, drop empty lines,
join with `\n`. Applied identically to both sides — no asymmetric stripping.

## 5. Decision rule

Candidate `c` **rebuilds to** version `v` iff
`B(c,v) = 1`, **or** (`pages(c) = pages(v)` and `M(c,v) >= pages(v) - 1`).

The one-page tolerance exists only to absorb a date or timestamp rendered on the
title page. If it is ever exercised, the differing page must be identified and
named in the report; a tolerance used silently is not a tolerance.

The gate **passes** iff some candidate rebuilds to v1.2.

## 6. Predictions

Recorded before running.

- **P1** C3 rebuilds byte-identically to v1.0 (`B(C3, v1.0) = 1`).
- **P2** C6 likewise (it is a copy of C3).
- **P3** No candidate rebuilds to v1.2.
- **P4** No candidate rebuilds to v1.1 or v1.3.
- **P5** C1, C2, C4, C5 rebuild to none of the four published versions.
- **P6** Candidate builds have 24 pages; v1.2 has 25.

## 7. Falsifiers

- **F1 (instrument falsifier — the important one).** If P1 fails, i.e. C3 does
  not reproduce v1.0 byte-identically **and** does not reach the content
  threshold against v1.0, then the build is not reproducible on this machine
  (toolchain drift, package versions, fonts). In that case a negative result
  about v1.2 is **uninterpretable**: "no source builds to v1.2" cannot be
  distinguished from "no source builds to anything here". HALT, report the gate
  as INDETERMINATE, and do not assert H0.
- **F1b (graceful degradation, declared in advance, not improvised).** If byte
  identity fails for C3 but the content threshold is met, the instrument is
  valid **at content level only**. Byte-level conclusions are then withheld and
  all verdicts are stated as content-level. This is pre-registered so that the
  fallback cannot be chosen after seeing which tier is convenient.
- **F2.** If some candidate rebuilds to v1.2, H0 is false, the gate passes, and
  the session proceeds to the diffs and the edits on that source.
- **F3.** If two candidates that are supposed to be copies of each other (C3/C6,
  C1/C4, C2/C5) build to different outputs, the copy relation is false; report
  and do not treat them as interchangeable.
- **F4.** If any build emits a LaTeX error, or its page count cannot be read from
  the log, that candidate is reported as BUILD-FAILED, never silently scored 0 —
  a failed build and a non-matching build are different facts.

## 8. Ordering rule (CT-S47)

The observable is evaluated **before** the vacuity block. A vacuity pre-check
that guards a PASS but not a FAIL is the CT-S46 refusal/finding collision in
another form. Vacuity results are recorded but cannot retroactively convert a
fired falsifier into a pass.

## 9. Vacuity pre-check

- **V1.** The four published versions must be pairwise distinct under the content
  observable. If any two score a full match against each other, the comparator
  cannot tell versions apart and every verdict is void. (CT-S55 established this
  for its own stripping comparator; it is re-run here because the normalisation
  is different — no result is inherited across instruments.)
- **V2.** Perturbation: swapping two adjacent pages of v1.2 must drop
  `M(v1.2-perturbed, v1.2)` below the threshold. Confirms the observable responds
  to content order, not just to a bag of pages.
- **V3.** Positive baseline: comparing v1.2 against itself must give a full match.
  A comparator that scores nothing against anything looks identical to a tree
  with no matching source — this is the A0-baseline rule (a harness where every
  arm refuses looks identical to one where every arm works).

## 10. Amendment H scope

If the gate fails, the sweep still runs and its result is reported whether or not
it finds anything: an empty sweep and an absent sweep are indistinguishable in a
report that records only repairs. The sweep asks, of whatever defect the gate
exposes, **where else the same defect occurs** — the scope is not limited to the
items the operator listed.

## 11. Stages conditional on the gate

Stage 2 (v1.0→v1.2 and v1.2→v1.3 source diffs), Stage 3 (re-applying CT-S52's
four items plus item 5), Stage 4 (bibliography), Stage 5 (checks and the rendered
diff) all require a v1.2 **source**. If the gate fails they cannot be executed as
specified, and the operator's own instruction — "do not reconstruct v1.2 from
v1.0 plus edits" — forbids the obvious substitute. The session then reports the
gate result and what would be needed to unblock, and stops.

## 12a. AMENDMENT 1 — candidate scope widened (written after the in-tree gate
##      returned FAILED, before any widened observable was computed)

The Stage 1 gate over candidates C1–C6 returned **FAILED** with the instrument
control passing at byte tier (C3 and C6 both reproduce v1.0 byte-identically).
That is a valid negative: no source **in the repository** rebuilds to v1.2.

Amendment H then applies to this session's own scope. The operator's halt
condition said "no source *in the tree*", and the candidate list was assembled
from the tree because that is where the question was posed — which is exactly
the defect Amendment H names: *a scope inherited from whoever reported the
problem, so the question "where else could it be?" was never in scope and could
never fail.* The sweep was therefore run outward from the repository, and it
found source trees for v1.1, v1.2 and v1.3 **outside** it:

| id | directory | tex bytes | stored PDF md5 |
|----|-----------|-----------|----------------|
| D1 | C:/LocalWork/project-fingerprint/sectorial/vquad_connection_coefficient/v1.1-draft/paper | 88341 | 7feaf94c05a1815a9e8a0ea04561f834 (= v1.1) |
| D2 | C:/LocalWork/project-fingerprint/sectorial/vquad_connection_coefficient/v1.2-draft/paper | 88897 | 792107efab6317e8ae21e2ca20f092ff (= v1.2) |
| D3 | C:/LocalWork/project-fingerprint/sectorial/vquad_connection_coefficient/vquad-periodrep-bundle/paper | 87778 | 99faea5b… (= v1.0) |
| D4 | C:/LocalWork/vq-fix/src/base | 88897 | 792107efab6317e8ae21e2ca20f092ff (= v1.2) |
| D5 | C:/LocalWork/vq-fix/src/control | 88897 | 792107efab6317e8ae21e2ca20f092ff (= v1.2) |
| D6 | C:/LocalWork/vq-fix/src/v_next | 91278 | (802178 B — matches no published version) |
| D7 | C:/LocalWork/vq-fix/src/v_next_deposit | 91166 | 943545955c2951a9592759862230e46a (= v1.3) |

**Nothing in the decision rule, the normalisation, the thresholds or the
falsifiers is changed.** Section 5 is applied verbatim to D1–D7. Only the
candidate set is enlarged, and that enlargement is recorded here *before* the
widened observable is computed so that it cannot be presented afterwards as
having been intended all along.

The in-tree result stands as reported and is **not** overwritten: "the
repository does not contain the source of the submitted paper" remains a true
and separately reportable finding, and the sweep in section 10 must account for
it rather than let the rescue erase it.

Additional predictions for the widened set, recorded before running:

- **P7** D2, D4 and D5 rebuild to v1.2 (byte-identically, if the toolchain here
  matches the environment of record).
- **P8** D1 rebuilds to v1.1, D3 to v1.0, D7 to v1.3.
- **P9** D6 rebuilds to none of the four.

**F5.** If a stored PDF sits beside a source that does not rebuild to it, the
source has been edited since that PDF was made and the pair is untrustworthy as
a base; report it and do not adopt it. The stored hash is a hint, never the
observable — the build is the observable.

## 12. Governance

Nothing committed, pushed, tagged, uploaded, submitted or deposited. No earlier
session's files are modified; candidates are built only in scratch copies. The
submitted v1.2 artefacts stay byte-unchanged and are re-hashed at the end to
prove it.
