# Handoff — P06-DESERT-REVISION
**Date:** 2026-04-30
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE (with two flagged TO-DO computations)

## What was accomplished
Applied the SICF revision pack to `pcf_desert_negative_result.tex`
(source: `tex/submitted/pcf_desert_negative_result.tex`,
SHA-256 `C4B48AA4...F43C25`, 19 799 bytes, 2026-04-24).
Retitled and reframed the paper around the explicit
"Desert Conjecture", added a search-box parameter table, a
positive-control subsection for profiles (2,1)/(3,2), a
precision-stability subsection, and a Padé/Hermite–Padé
structural remark plus its bibliographic support. Added two
new bibitems (`P11`, `Baker1996`). Compiled cleanly to 8 pages
(was 7) with no undefined references or citations. The package
`lmodern` was added to fix a pdfTeX font-expansion fatal error
triggered by `microtype` on the host TeX install — a build-only
change, no semantic impact.

## Key numerical findings
- No new computation performed; all prior numerical content is
  preserved verbatim. The only quantitative additions are the
  search-box parameter table values, all of which are extracted
  directly from the existing methodology section:
  * Coefficient height bound `H = 10,000` (from §"PSLQ identification",
    `_a2_cycle3_result.json` corroborates).
  * PSLQ precision: 130 dps (control verified at 200 dps).
  * Relation-norm cutoff: `max|c_i| ≤ 10,000` — the source paper
    does not specify a separate relation-norm bound; recorded as such.
  * Total families enumerated: 8 820 triples
    (4 410 per profile × 2 profiles).

## Judgment calls made
- **Source choice.** Two `pcf_desert_negative_result.tex` files
  exist (`./` and `./tex/submitted/`); used the newer/larger
  `tex/submitted/` copy (2026-04-24, 19 799 B) as the authoritative
  base. The workspace-root copy (2026-04-19, 16 722 B) was left
  untouched.
- **Forbidden-word grep.** None of the strings "we show", "we prove",
  "we establish" appeared in the abstract or introduction.
  0 such replacements were therefore made; the abstract opening
  sentence was rewritten as specified, which is an additive
  change rather than a string substitution.
- **FIX 3 honesty.** The (2,1) and (3,2) positive-control sweeps
  have *not* been performed for this paper. The instructions said
  to add the subsection citing P11. To avoid fabrication, the
  inserted paragraph states the runs are *planned* (not completed),
  references the existing (6,3) Apéry control as one realised
  positive control, and carries an explicit `[TO DO]` footnote.
- **FIX 4 honesty.** The desert sweep itself was run only at 130
  dps. Only the (6,3) Apéry control was double-checked at 200 dps
  in the source paper. The inserted "Precision stability" paragraph
  reflects this accurately and flags the full 260-dps re-run as
  a `[TO DO]` footnote.
- **lmodern addition.** Required to make pdflatex compile on this
  host (microtype + non-scalable CM bitmaps caused a fatal). This
  is a typesetting-only change.

## Anomalies and open questions
- The original paper already contains a "Positive control at
  $d_a = 6$" subsection (Apéry, $V = 6/\zeta(3)$). The newly
  added (2,1)/(3,2) subsection therefore *supplements* rather
  than replaces it. Reviewer should decide whether to keep both
  or merge into a single "Positive controls" section.
- `\cite{spectral}` and `\cite{raayoni2021}` and `\cite{borwein2013}`
  are present in `\thebibliography` but the rerun showed them
  defined; the only Unicode hyperref warning is benign (accented
  metadata in `\title` PDF string). No action required.
- The "Conjecture 1" already framed in §3.2 ("conj:desert") is
  *not* the new "Desert Conjecture" wording from the abstract;
  it is a stricter integer-relation statement at coefficient
  bound 10 000. Both can co-exist (the abstract conjecture is
  the general `Trans-stratum` statement; the §3.2 statement is
  its computational shadow). Reviewer may want to add a one-line
  bridge sentence — left untouched per "do not modify theorem
  environments".
- Two `[TO DO]` items remain (see below). Neither blocks venue
  submission as a *short note*, but both are needed for an
  expanded version.

## What would have been asked (if bidirectional)
- Should the (2,1)/(3,2) positive-control sweep be executed in
  this session? (Estimated ~30–60 min on the existing pipeline.)
- Should the full (4,3)/(5,3) sweep be re-run at 260 dps to
  retire the precision-stability `[TO DO]`? (Estimated ~7–8 hr.)
- Is `lmodern` acceptable for the target venue's style, or
  should the paper revert to default Computer Modern (requires
  a TeX install with scalable CM Type 1 fonts)?

## Recommended next step
Schedule a small computational session (P06-CONTROL-RUNS):
run the existing PSLQ pipeline on degree profiles (2,1) and
(3,2) using the same 12-element basis B and the F(2,4) Trans
families documented in P11; if Trans-stratum recovery succeeds,
strip the `[TO DO]` footnote in §"Positive control at (2,1)
and (3,2)". A second, optional session can run the 260-dps
precision-doubling pass on the desert families.

## Files committed
- `pcf_desert_negative_result.tex` (revised source, 23 304 B)
- `pcf_desert_negative_result.pdf` (8 pages, 402 700 B)
- `halt_log.json` (`{}`)
- `discrepancy_log.json` (`{}`)
- `unexpected_finds.json` (`{}`)
- `handoff.md` (this file)

## Five fixes — applied / TO DO status
| # | Fix                                          | Status            |
|---|----------------------------------------------|-------------------|
| 1 | Retitle + abstract opening sentence          | APPLIED           |
| 1b| Replace "we show / prove / establish"        | APPLIED (0 hits)  |
| 2 | Search-box parameter table (`tab:params`)    | APPLIED           |
| 3 | Positive-control subsection at (2,1)/(3,2)   | APPLIED + [TO DO] (run) |
| 4 | Precision-stability subsection               | APPLIED + [TO DO] (260 dps) |
| 5 | Padé/Hermite–Padé structural remark + cites  | APPLIED           |

## Page count
- Before revision: **7 pages**
- After revision:  **8 pages** (delta = +1; floor was 7 − 2 = 5).

## TO DO items (for reviewer / follow-up session)
1. Execute PSLQ positive-control sweep on degree profiles
   `(2,1)` and `(3,2)` against P11's F(2,4) Trans families.
2. Re-run the full `(4,3)` / `(5,3)` desert sweep at 260 dps
   (precision-doubling pass) to confirm zero Trans-stratum
   relations under doubled precision.

## Recommended venue
**Hardy–Ramanujan Journal** (open-access, congenial to
short experimental-mathematics notes with a clearly stated
conjecture and computational evidence; aligns well with the
paper's length and tone). Backup choices: *Experimental
Mathematics* (Taylor & Francis) for a longer expanded version
once both `[TO DO]` runs are completed, or *Integers* for the
short-note form.

## Estimated remaining work before submission
- *As-is short note (Hardy–Ramanujan):* essentially submission-ready
  after one author copy-edit pass; `[TO DO]` items can stay as
  declared limitations.
- *Expanded version (Experimental Mathematics):* ~1 day of
  compute for the two `[TO DO]` runs + ~half-day write-up to fold
  the new evidence into the body and remove the footnotes.

## AEAL claim count
0 entries written to `claims.jsonl` this session
(revision-class task: no new numerical claims were generated;
all quantitative content already AEAL-logged in prior sessions
`PCF-43-DESERT-*` and `_a2_cycle{1,2,3}_result.json`).
