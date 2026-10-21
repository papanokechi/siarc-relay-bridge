# CT-S26-UPPER-BOUND — REPORT

**Deliverable:** `PROOF.md` — Proposition U, the upper bound on `r_∞`, proved.
**Status of the session's single objective:** closed. The pre-declared fallback
(weakening `OUTLINE.md` §1 ¶2 to the one-sided statement) was **not** taken.

Nothing was committed, pushed, tagged, deposited or sent. `theorem.tex` and
every other file belonging to an earlier session are **unmodified**.

---

## 1. What was done, and why this session existed

`CT-S24-PAPER-OUTLINE` reached revision 5 with exactly one open item. Its §1 ¶2
method paragraph asserts that positivity of `b` supplies `r_∞ ≠ 0` "together
with a **two-sided** bound", but `CT-S1-THEOREM/theorem.tex` proves only the
lower half (`prop:positive`, `S1-02`: `r_∞ ≥ 1`). The upper bound
`r_∞ ≤ exp Σ_{k≥1} 1/(b(k)b(k+1))` came out of a from-scratch derivation in
conversation and **was never written back to any source of record**. The
outline therefore carried it as an *unfolded drafting addition with no claim
id* (`S24-21(a)`), with a standing instruction to prove it or drop it.

That status is the same shape as the Odlyzko citation living outside the
worktree (`S24-12`): a result believed because it was once derived, not because
it is written down anywhere checkable. This session removes that status.

**Governance note.** The natural home for the result is `theorem.tex`,
immediately after `prop:positive`. That file belongs to `CT-S1-THEOREM`, and
this corpus does not edit earlier sessions. The proof therefore lives here, in
`PROOF.md`, written so as to stand alone (the setup and the summability lemma
are restated rather than cited across), and the outline references it. Folding
it into `theorem.tex` is a drafting action for whoever writes the paper.

## 2. Claims

| id | label | statement, in one line |
|---|---|---|
| `S26-01` | **PROVEN** | Proposition U: under (A1) **and** `b(n) > 0` for `n ≥ 1`, `r_n ≤ exp Σ_{k=1}^{n-1} 1/(b(k)b(k+1))` for every `n ≥ 1`, hence `1 ≤ r_∞ ≤ L < ∞`. |
| `S26-02` | VERIFIED | The finite-`n` inequality holds at every `n ≤ 20000` for ten positive `b` at dps 60; V4 shows the arm can report a violation; V5 shows the bound is not satisfied trivially. |
| `S26-03` | VERIFIED | The recurrence engine reproduces `y_n = (-1)^n I_{n+1}(2)` to 60.9 digits, and detects a `1e-20` perturbation of it. |
| `S26-04` | VERIFIED | Positivity is **load-bearing**: 3 of 6 sign-changing `b` violate the finite-`n` inequality outright. |
| `S26-05` | INSPECTED | Arm V1 **fired**; the defect was in the control's closed form, not the engine. `PREREG.md` left unedited; `ADDENDUM-1.md` written instead. |
| `S26-06` | STRUCTURAL | Both inequalities are strict, so `L` is never attained. Recorded only to forestall a misreading; nothing uses it. |
| `S26-07` | INSPECTED | The outline's single open drafting item is closed; the fallback was not taken; four consequences for drafting. |

**Label discipline.** `S26-01` is PROVEN because there is a complete proof in
`PROOF.md`, written **before** any numerics were run. `S26-02`–`S26-04` are
VERIFIED, not PROVEN: they are numerical checks at a stated dps with stated
residuals, and none of them is cited as evidence *for* Proposition U. The proof
would stand if every numerical arm were deleted; the arms exist to catch a
transcription error between the proof and the recurrence actually iterated.

## 3. The proof, in one paragraph

Under `b > 0` on `n ≥ 1`, `prop:positive` gives `r_{n-2} ≤ r_{n-1}` for every
`n ≥ 2`. Substituting that into the exact identity
`r_n = r_{n-1} + r_{n-2}/(b(n-1)b(n))` (`theorem.tex` eq. `rnrec`) gives
`r_n ≤ (1+ε_n) r_{n-1} ≤ r_{n-1} e^{ε_n}` with `ε_n = 1/(b(n-1)b(n)) > 0`.
Iterating down to `r_1 = 1` and re-indexing gives the finite-`n` statement; the
series converges by the summability `prop:exists` already uses, and passing to
the limit in a non-strict inequality gives `r_∞ ≤ L`.

**No minimal-solution, Pincherle or Perron–Kreuser input is used at any step.**
That is not incidental: `OUTLINE.md` §2.0 undertakes that nothing in the paper
rests on Birkhoff–Trjitzinsky, after the Odlyzko p. 77 page was found to object
to it as possibly non-rigorous (`S24-13`). The growth material can now say so
of its upper bound as well as its lower.

## 4. The falsifier that fired

`PREREG.md` registered the known-answer control V1 with the closed form
`y_n = (-1)^n I_n(2)`. The first run reported **0.30103 digits** of agreement
and **F2 fired**, halting with `VERDICT: FAIL`
(`outputs/upper_bound.out.txt`, retained).

The closed form was wrong by an **index shift**: it requires
`I_{n-2} - I_n = n I_{n-1}`, where the Bessel identity gives
`(n-1) I_{n-1}`. The correct solution is `y_n = (-1)^n I_{n+1}(2)`, derived in
`ADDENDUM-1.md` §3. `PREREG.md` is left unedited; every threshold is unchanged;
the corrected run writes to a new path.

Two things are worth carrying out of this.

- **The arm caught a wrong control, which is the harder case.** V1 exists to
  catch a broken recurrence. A wrong control that happened to *agree* would
  have certified a broken engine — and that is the failure mode a known-answer
  test is supposed to be immune to. It is not: a known-answer test is only as
  good as the known answer, and the known answer needs its own derivation on
  the page.
- **It is the third instance in this run of one provenance defect.** `S24-12`
  (a citation held in a session record outside the worktree), `S24-13` (a
  paraphrase that collapsed two attributions on one page), and now a Bessel
  identity reproduced from memory rather than from the identity. The common
  shape: *derived once, remembered compressed, reproduced from the compressed
  memory.* It recurred **inside the session written to remove exactly that
  status from the upper bound**, which is the strongest available evidence that
  knowing about the failure mode does not prevent it — only a control that can
  fire does.

## 5. What was NOT established

- **No closed form for `r_∞`** is claimed for any `b`. The value
  `r_20000 = 2.2794713259205270753` for `b(n) = n` is reported as a bound check
  only. It is **not** asserted to equal any named constant, and the resemblance
  to nearby Bessel values is deliberately not pursued.
- **Sharpness.** `L` is an upper bound, not an asymptotic. No claim is made
  about how far `r_∞` sits below it beyond the observed ratios.
- **Necessity of positivity in general.** `S26-04` exhibits three
  counterexamples, which shows the hypothesis cannot simply be deleted. It does
  **not** characterise which sign-changing `b` satisfy the inequality; three of
  the six tested do, and nothing is claimed about why.
- **`theorem.tex` is unchanged.** Until the result is folded in at drafting,
  the corpus's LaTeX source of record still contains the one-sided statement
  only.

## 6. Open questions for the operator

1. **Where the proposition lands.** Recommended: `theorem.tex` after
   `prop:positive`, with the two combined into one two-sided statement. That is
   an edit to an earlier session's file, so it needs either a copy-forward or
   an operator waiver. This session did neither.
2. **Whether `S26-06` (strictness) is wanted at all.** It is free and it
   forestalls a misreading, but it is also one more sentence in a section whose
   virtue is brevity. Recorded as STRUCTURAL and unused so that dropping it
   costs nothing.
3. **Whether V6's three non-violating sign-changing `b` deserve a look.** Not
   pursued here; it is a different question from the paper's.

## 7. Uncommitted files

All new, all under `sessions/2026-09-17/CT-S26-UPPER-BOUND/`.

| file | sha256 (outputs only) |
|---|---|
| `PREREG.md` | — written before any computation |
| `PROOF.md` | — written before any numerics |
| `ADDENDUM-1.md` | — written after V1 fired, before the corrected run |
| `REPORT.md` | — this file |
| `claims.jsonl` | — 7 claims, `S26-01`…`S26-07` |
| `scripts/upper_bound.py` | — |
| `scripts/emit_claims.py` | — |
| `outputs/upper_bound.out.txt` | `a220c136c4c2034e90042113af750aa4cbf3996ff15bde34667d35fa1efb7c3c` — **the FAIL run. Do not overwrite; `S26-05` cites it.** |
| `outputs/upper_bound_rev2.out.txt` | `f1f32dd8f325981a48ac598549a89db86f2b526d68867679a3bb229da285315c` — the corrected run, `VERDICT: OK`. |
