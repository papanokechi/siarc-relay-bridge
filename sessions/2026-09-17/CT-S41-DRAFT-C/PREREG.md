# PREREG — CT-S41-DRAFT-C (Group C: §5 and §6)

Written **before** any script in this session was run. Thresholds are not
revised after seeing results.

## 1. Scope

Draft §5 (*System C is a point of U₀*) and §6 (*The identification is exact,
not projective*) as paper prose, from `OUTLINE.md` revision 6 and **from the
claim texts themselves**, never from the outline's paraphrase of them and never
from memory.

Sections 0–4 are **inputs**, copied unmodified into `refs/`. They are not
rewritten and not renumbered.

## 2. Hypothesis

Every claim id the outline assigns to §5 and §6 resolves in the corpus, is not
superseded, and carries the label the prose asserts for it; every numerical
value printed in the prose traces to a claim id; and §5–§6 assemble with §0–§4
into a document with no undefined or multiply-defined reference.

## 3. Observables

- **O1** — per-citation verdict: resolved / label match / superseded.
- **O2** — every numeric literal in the drafted prose is traceable to a cited
  claim's text.
- **O3** — assembly: `check_assembly.py` rules R1, R2, R2b, R3 over §0–§6.
- **O4** — the label distribution asserted in the prose against the corpus.

## 4. Falsifiers, with thresholds

- **F1** any cited id UNRESOLVED, SUPERSEDED, or label-mismatched → FAIL.
- **F2** any numeric literal in §5 or §6 that does not occur in the text of a
  claim cited **in the same subsection** → FAIL. This is the check that a
  transposed digit would survive elsewhere, and it is deliberately narrow: it
  tests transcription, not derivation.
- **F3** any undefined or multiply-defined reference in the §0–§6 build → FAIL.
- **F4** the stub declares a label a drafted section defines → FAIL (R2).
- **F5** the prose asserts PROVEN for a claim the corpus labels otherwise → a
  special case of F1, called out separately because it is the one direction
  P0 forbids outright.
- **F6** the deliberately wrong control label is **not** caught → the check
  cannot fail, and the session's output is void.

## 5. Vacuity pre-checks

- **A-control** — one citation is drafted with a deliberately wrong label. F1
  must name it. Its identity is recorded in the check's own output so it can
  never be quietly removed.
- **A-numeric** — a digit is transposed in a quoted residual. F2 must fire.
- **A-super** — a citation is repointed at a structurally superseded id. F1
  must fire.
- **A-assembly** — `sec:point` is referenced where §5 defines `sec:locating`.
  R1 must fire. (This is `S40-02` reinstated at the next group.)
- **A-stub** — the stub retains an entry for §5 or §6 now that they exist. R2
  must fire.
- **A-bounds** — the sections are emptied; reader integrity must refuse rather
  than report zero problems.

## 6. Two specific transcription hazards, pre-declared

Both are recorded here **before drafting** because both are places where the
outline and the corpus could diverge and the error would read as correct:

1. **θ∞ = −2 ± √3/9, not −1 ± √3/9.** `S16-08` records that the naive
   dictionary entry `t·θ∞/2` **failed** all three probes and the data give
   `t(θ∞+1)/2`; the `+1` is the scalar-reduction shift and it is the whole
   reason for the `−2`. The prose must carry the reason, not just the value.
2. **The base field is `ℚ(i√11)`, and `√3` must not be adjoined.** The visible
   radicals are `√33`, `√11`, `√3`, which pulls toward `ℚ(√3,√11)`. `√3` is
   *generated* by the eliminant; adjoining it in advance would split the two
   points and make degree 2 look like two degree-1 components for the wrong
   reason.

## 7. What this session does NOT establish

- **No formula is re-derived.** F2 tests transcription against claim texts. A
  value wrong in the corpus is wrong in the paper, and this gate cannot see it.
- **§6 does not close the gauge question** of §4.1, and `S25-02`'s Galois
  statement must not be written as if it does — `OUTLINE.md` says so explicitly
  and the prose must respect it.
- **§5's membership is STRUCTURAL, not PROVEN** (`S16-14`), because the match
  is of *projective* normal forms. §6 is what removes that qualifier, and the
  order matters: §5 must state the caveat and §6 must withdraw it, rather than
  §5 quietly assuming §6's result.
