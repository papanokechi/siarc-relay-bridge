# PREREG — CT-S43-DRAFT-E (Group E: §9, §10, Appendix A, Appendix B)

Written before any script in this session ran. Thresholds fixed here are not
revised after seeing results; a threshold that proves ill-posed is reported as
a finding, not edited.

## 0. What this session is

The **last drafting session**. It writes §9 *Scope and limits*, §10 *Open
questions*, **Appendix A** (the van der Put–Saito typo) and **Appendix B**
(computational methods), and then assembles the **whole paper** for the first
time. It runs no new mathematics.

Appendix B discharges a debt: §7 forward-references `app:methods` for
`S22-04`/`S22-05` through the build stub. **That is a real dependency, not a
placeholder** (operator, this turn). When Appendix B lands, the stub must be
able to declare nothing at all.

## 1. Hypothesis under test

**H.** The four drafted files cite only ids that resolve and are unsuperseded;
carry, for every cited id, its current corpus label; state no significant
numeric literal absent from a cited claim's own record; honour the ten
pre-declared hazards of §5; introduce none of the excluded framing of the
outline's §3.2; and leave the build stub empty.

## 2. Observables

- **O1** resolution · **O2** supersession · **O3** label match · **O4**
  significant numeric literals · **O5** hazard markers present.
- **O6** the build stub declares zero entries once Appendix B exists.
- **O7** the excluded-framing census over **all eleven** paper files.
- **O8** the §1-definition census: for every term §1 defines, is it used
  outside §1?

**Normalisation for O4** is inherited verbatim from CT-S42 and is not revised:
significant literal = integer run ≥ 3 digits, or a decimal, or
`m\times10^{-k}`, or bare `10^{-k}`; pool = `claim` **and** `review_note` of
every id cited in the same subsection.

## 3. Falsifiers, with thresholds

| id | fires when |
|----|-----------|
| **E1** | any cited id fails to resolve |
| **E2** | any cited id is superseded by a later claim |
| **E3** | any prose label differs from the corpus label |
| **E4** | any significant literal is unaccounted for |
| **E5** | fewer than **20** literals inspected (non-vacuity on O4's numerator) |
| **E6** | any hazard marker of §5 is absent |
| **E7** | the stub declares any entry after Appendix B exists |
| **E8** | any **Group E file** carries excluded framing from outline §3.2 |
| **E9** | the §1-definition census inspects fewer than **10** terms |
| **E10** | the assembled build reports any error, undefined reference, or multiply-defined label |

**E8 fails only on Group E's own files.** Hits in §0–§8 are **reported, not
repaired**: editing a drafted section is outside this group's remit, and the
standing rule is report-don't-repair. The census is the session's output.

**E9 likewise reports rather than repairs.** An orphaned definition — a term
§1 defines that no later section uses — is a finding for the notation pass,
which the operator has ruled runs next and before the formula pass.

## 4. Vacuity pre-check (control arms)

Arms mutate **in-memory copies**; nothing on disk ever carries a deliberate
defect. Every arm asserts **its mutation site exists** before mutating, and
arms operate on **raw** text while rules compare **squashed** text, so every
arm needle is chosen to lie on a single line (the CT-S42 `S42-07` repair).

| arm | mutation | must fire |
|-----|----------|-----------|
| E1 | a cited id replaced by one absent from the corpus | E1 |
| E2 | a real but superseded id substituted | E2 |
| E3 | **the deliberately wrong label** — `S16-15` relabelled VERIFIED | E3 |
| E3b | `S16-21` relabelled PROVEN (corroboration sold as proof) | E3 |
| E4 | a digit transposed in a quoted literal | E4 |
| E4b | an exponent altered | E4 |
| E5 | the literal pool emptied | E5 |
| E6 | a hazard marker deleted | E6 |
| E6b | a second hazard marker deleted | E6 |
| E7 | an entry re-added to the stub | E7 |
| E8 | excluded framing inserted into a Group E file | E8 |
| E9 | the §1 definition list emptied | E9 |
| E0 | a section truncated below the byte floor | E0 |

`S16-15` is the E3 control because it is **CONJECTURED** and names an unrun
falsifier; relabelling it VERIFIED is the precise error §9 exists to prevent.
`S16-21` is the second because its own text says *"This is corroboration for
the typo diagnosis, not independent proof of it."*

**Reader integrity uses bounds, never fingerprints** (CT-S36 `S36-09`).

## 5. Transcription hazards, declared before drafting

1. **`S16-14` and `S17-04` in that order.** §9 states the CT-S16 caution
   (STRUCTURAL, projective normal forms, "up to a rank-1 twist") **and then**
   `S17-04` removing it (PROVEN, `(P,Q)` agree identically). The order is the
   content: the caution was real and was discharged, not overlooked.
2. **`S16-15` is CONJECTURED and names an unrun falsifier.** §9 must say the
   monodromy/Stokes falsifier at 30 digits was **not run** and that **no
   threshold was weakened** to close it.
3. **`S17-08`: the statement changed, not the label.** Membership was
   deliberately not raised above STRUCTURAL.
4. **`S22-15`'s final sentence** must appear in §9: a numerical agreement at
   one point along one direction in `t` is not a proof of leaf membership.
5. **The referee sentence.** Membership is confirmed *for the trace
   coordinates `x₁, x₂, x₃` under the one convention of sixteen that passed*,
   and that selection is itself a **result** (`S22-11`), not an assumption.
6. **§10 has exactly TWO questions.** The closed-form-Stokes-constant question
   (`S22-22`) **leaves the paper** with the Borel material and must not appear.
7. **The Galois conjugacy does not close the gauge question.** §10 must say so
   **explicitly**, so that no reader infers a connection between two
   `√3`-flavoured statements. `S25-02` vs `S17-07`.
8. **Appendix A is mathematics the paper depends on, not errata history.** The
   located point is computed under the **corrected** reading.
9. **`S16-21` is corroboration, not proof**, in its own words.
10. **Appendix B: `S22-04` and `S22-05` were vacuous as first written**, and
    the corrected A7 is a **dependent** restatement, not independent evidence.
    Appendix B must also say plainly (repair **R-(b)**) that full reproduction
    requires the scripts.

## 6. Two interpretations, declared rather than silently chosen

- **The outline's §4 has three items and §10 is to carry "two questions, not
  three"** because outline §4.2 leaves with the Borel material. I read the
  remaining two as **outline §4.1** (the `z`-dependent gauge) and **outline
  §4.3 item 3** (convention-independence). Outline §4.3 items 1 and 2 are
  *limits*, not questions, and go to §9, which is titled *Scope and limits*.
  Flagged for the operator rather than silently resolved.
- **`S17-06` trips `claim_index`'s supersession heuristic** because its text
  contains the word *withdrawn* — it is about a *caveat* being withdrawn, not
  the claim. The structural `supersedes` test is the one the gate uses, and it
  does not fire. Recorded so the heuristic hit is not mistaken for a finding.

## 7. Scope limit, stated in advance

**No displayed formula is re-derived.** Appendix A's displayed formulas were
transcribed from **page images** (`S16-18`, `S16-R18-01`, `S17-17`) and have no
corpus script that computed them; the operator has scoped the later formula
pass to verify such equations **against the page** and to report which route
each equation took. This session performs neither route. Its PASS is a
transcription result only.

## 8. Budget

≤ 1 day. Halt and report if a falsifier fires, if a convention is ambiguous,
if required data is missing, or if runtime exceeds 3× the budget.
