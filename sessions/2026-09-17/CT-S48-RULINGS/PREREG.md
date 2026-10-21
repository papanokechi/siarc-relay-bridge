# PREREG — CT-S48-RULINGS

Written **before** `scripts/check_rulings.py` was run.

This session performs no mathematics. It executes four operator rulings as
**record actions**, and it checks that each action says something true about the
files it names. The instrument is therefore a file reader, and the hazard is the
one this run has hit four times: **a reader that reports absence it cannot see.**

---

## 1. Hypotheses

- **H1 (scope).** `S25-01`'s transcription controls are about the solutions
  *recorded* in `CT-S16-MEMBERSHIP-C/outputs/pq_solution.txt`, and say nothing
  about the forms *printed* in the paper's `section5.tex`.
- **H2 (coverage).** `CT-S47-FORMULA-S5-QP` establishes the printed forms
  separately, by parsing the numerals out of `section5.tex` itself.
- **H3 (the bar for amendment G).** The string `jimbo_p1152.png` denotes two
  different images in this tree, and the marker beside the misnamed one names
  both by digest.
- **H4 (label scope).** `S16-R18-02` carries `PROVEN` and its own claim text
  contains a formula that is wrong as written.

## 2. Observables

| id | observable |
|---|---|
| R1 | which artefacts `S25-01`'s claim text names, and which it does not |
| R2 | the `source` line and the summary line of `outputs/route_s5_qp.out.txt` |
| R3 | live-computed sha256 of the three `jimbo_p1152.png` / `jimbo_printed1152.png` files, and whether the marker names them |
| R4 | `S16-R18-02`'s `label` field, its two forms, and the verdict line of `outputs/check_r18_sign.out.txt` |

## 3. Falsifiers, with thresholds

- **F1.** If `S25-01`'s text names `section5.tex`, or the words *printed* or
  *typeset*, H1 is false and the supersession must not be written. Threshold:
  exact substring, case-insensitive for the two words.
- **F2.** If `outputs/route_s5_qp.out.txt` does not carry the exact line
  `ROUTE S (section 5 q,p): 36 checks, 0 DIFFER`, or does not record
  `section5.tex` as its source, H2 is false. Threshold: verbatim line match.
- **F3.** If the two files named `jimbo_p1152.png` have the **same** digest, the
  ruling's premise is wrong and amendment G must not cite it. Threshold: exact
  digest equality.
- **F4.** If `S16-R18-02` does not carry `PROVEN`, or if its claim text does not
  contain both forms, H4 is false. Threshold: exact substring after whitespace
  normalisation.

**No threshold here may be moved after seeing a result.** Every one is an exact
match; there is nothing to tune, which is deliberate — this run has twice found
a threshold that could be tuned to either answer.

## 4. Vacuity pre-check

Every check above can be satisfied by a reader that sees nothing, so each
carries a control that must **fire**:

- **R1c** — the same detector, run on `S25-01`'s text with `section5.tex`
  appended, must report the artefact **present**. Absence must mean absence, not
  unreadability. *(Fourth appearance of this hazard in the run; this is the
  standard form.)*
- **R2c** — a summary line claiming `37 checks` must **not** be found, and every
  figure must resolve to the **summary line that reports it**, not to a digit
  string anywhere in the file. *(The standing rule from `S44-17`.)*
- **R3c** — a digest belonging to none of the three images must **not** be found
  in the marker.
- **R4c** — the same comparison, with the factored form deleted from the claim
  text, must report it **missing**.

If any control fails to fire, the corresponding check is reported as
uninterpretable and the record action it supports is **not** written.

## 5. Advance prediction

All four hypotheses hold and all four controls fire; the run is clean. The most
likely place for this prediction to be wrong is **R3**, because the marker
records digests as 16-hex **prefixes followed by an ellipsis character**, and a
reader comparing full 64-hex digests against it would report absence for a file
the marker names perfectly well — which would be R1's hazard recurring inside
R3's control. The checker therefore compares prefixes, by design, and says so.

## 6. Scope limit

This session writes **records**. It re-derives nothing, repairs no prose, and
edits no earlier session. The end-to-end read of the paper is **not** in scope
and is not attempted here.
