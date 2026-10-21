# PREREG — CT-S44-NOTATION-2

## 0. A deviation, recorded rather than hidden

P0 requires this file before any computation. It was written **after** the
symbol census and the first runs of the rendered-diff gate. The deviation is
real and is reported here rather than backdated.

What it does and does not cost:

- The pass is a **repair-and-verify**, not a measurement of an unknown
  quantity. There is no threshold here that a result could have been tuned to
  meet, and no hypothesis whose truth the data decides.
- One thing *was* built against observed output: the gate's list of declared
  repairs and accounted-for diff regions (`REPAIRS`, `ACCOUNTED` in
  `scripts/rendered_diff.py`) was completed iteratively as the diff surfaced
  regions. A declaration completed against the very diff it certifies is
  **not blind**, and the gate's authority therefore rests on its control arms
  rather than on the declaration having been fixed in advance. This is stated
  as a limit in the report, not as a strength.
- The source-side numeric rule (§4 below) was, by contrast, written before it
  was run in its final form, and its first version was *wrong in the declared
  direction* and failed — which is recorded as evidence that it can fail.

## 1. Hypothesis

The second notation pass can remove the twelve ruled notation defects from the
assembled paper without changing any mathematical content, and this can be
demonstrated rather than asserted.

## 2. The items, by kind

| # | kind | item |
|---|------|------|
| 1 | REMOVE | rho as Borel-plane indicial exponent in `u = sqrt z` leaves §1 as a paper symbol |
| 2 | UNIFY | `Newton--Puiseux diagram` -> `Newton polygon` in §2 (§2 follows §1) |
| 3 | UNIFY | §3's `R = 1/4 a^2 + 1/2 a' - b` into the general `(P,Q)` form of §1 |
| 4 | SEPARATE | `P = a^2 + bc` (a determinant) from the scalar operator's `P` |
| 5–10 | RESIDUE | the six deferred letters `M`, `A`, `L`, `u`, `beta`, `r` |
| 11 | KEEP | `Channel Theory` in the correspondence footnote (a citation, not framing) |
| 12 | KEEP | `PCF` as the object's standard name, without its framing |

## 3. Observables

- **O1** every declared repair has a rendered-text signature after the pass,
  and the text it replaced is gone.
- **O2** every differing region between the pre-pass and post-pass rendered
  documents is accounted for: declared, or carrying the signature of a named
  extractor artefact, or positively located in source the pass did not write.
- **O3** no numeric literal is lost or altered in any of the 13 source files
  except at declared sites.
- **O4** the assembled paper builds with 0 errors, 0 undefined references and
  0 multiply-defined labels.
- **O5** the assembly gate passes over the **repaired** files, not the
  pre-pass copies.

## 4. Falsifiers, with thresholds

- **F1** any differing rendered region not accounted for -> FAIL.
- **F2** any declared repair with no effect, or whose replaced text survives
  -> FAIL.
- **F3** any numeric literal lost from a source file outside the declared set
  -> FAIL. Declared losses are exactly `section7.tex {4:1, 8:1}` and
  `section5.tex {1:1}`; gains are permitted and reported as a census, because
  new prose legitimately contains digits.
- **F4** build errors, undefined references or multiply-defined labels > 0
  -> FAIL.
- **F5** fewer than 13 source file pairs compared -> FAIL (a check that read
  nothing passes everything).
- **F6** the two renderings token-identical -> FAIL as vacuous.
- **F7** any control arm MISSED or SKIPPED -> FAIL. SKIPPED is a failure, not
  a pass: an arm that cannot reach its mutation site tested nothing.

## 5. Vacuity pre-checks

- The math-mask reader carries a **positive control** (`\beta` occurs only in
  math and must survive the mask) and a **negative control** (the prose phrase
  `A reader` must not survive). Without the mask the letter `A` returned 128
  hits, of which the great majority were the English article — a reader
  defect, and the reason the controls exist.
- The page-number stripper reports how many pages it stripped and fails if it
  stripped fewer than half, so that a stripper doing nothing is visible.
- The extractor must yield >= 50 000 characters and >= 30 pages per document.

## 6. Control arms (must all be CAUGHT)

A1 undeclared word inserted · A2 the Newton polygon repair reverted ·
A3 `kappa` reverted to `A` · A4 the conventions paragraph deleted ·
A5 the rho definition reinstated · A6 `r_1` reinstated ·
**A7 two symbols transposed** — an anagram of the same characters, the exact
defect CT-S38's whitespace-stripped character-multiset comparison could not
see, and the reason this gate compares a token sequence ·
A8 a word inserted inside an untouched paragraph, closing the hole A1 walked
through on its first run.

Arms mutate raw extracted text while the rules compare the joined token
stream; substitution is therefore whitespace-flexible, per S43-12, so that an
arm whose needle straddles a line wrap is not silently SKIPPED.

## 7. Stated limits — what this pass does NOT establish

- **No formula is re-derived.** A transposed digit inside a displayed formula
  that was already wrong before the pass passes every check here. The source
  numeric rule proves only that this pass did not change it. Closing that gap
  is the formula pass, scheduled next.
- The rendered diff cannot decide digit order inside a fraction: pdftotext
  positions `\tfrac12`'s glyphs by width, so a neighbouring rename re-orders
  them with nothing in the mathematics changing. A second extractor does not
  settle it, because PyMuPDF shares that sensitivity and so is not
  independent *for this failure mode*. The question is moved to the source,
  where it is decidable.
- Punctuation-only differences are not policed.
- The `M`, `A`, `L`, `u`, `beta` and `r` items are resolved by **stating the
  convention** where the objects are distinguished by subscript, font or
  section-locality, following §1's own precedent, and by renaming only where
  two objects of the same shape collide in the same context.
