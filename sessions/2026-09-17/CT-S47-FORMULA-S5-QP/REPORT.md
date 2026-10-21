# REPORT — CT-S47-FORMULA-S5-QP

Third and final instalment of the formula re-derivation pass, plus two operator
rulings actioned. Draft only; nothing committed, pushed, tagged or deposited.

---

## 1. What was done

**Commissioned scope (operator ruling).** Re-derive section 5's exact algebraic
`q` and `p` — the largest of CT-S46's fifteen route-S-corpus displays, and on the
operator's reasoning the best hiding place for a transposed digit, being long
exact expressions over `Q(i sqrt 11)` that no reader checks by eye. Report per
coefficient rather than per display. The other twelve stay as they are.

Two rulings were actioned alongside it: a folio marker beside the misnamed Jimbo
page image, and a supersession for the `PROVEN` claim whose display CT-S45 found
defective.

### 1.1 What this instalment actually closes

The corpus already contained a check that looks like it covered these values and
does not. `S25-01` re-derived the six generators of the matching system
independently and confirmed that **both recorded solutions** annihilate all six
exactly. "Recorded" means as stored in `CT-S16-MEMBERSHIP-C/claims.jsonl`.

Between that record and the printed page lies a transcription step that no check
in the corpus has ever tested. **A digit transposed at typesetting is invisible
to `S25-01`, to every citation check, and to the clean build.** So the object
under test here is not the mathematics; it is the specific character string in
`section5.tex`, and the instrument parses its numerals out of the file rather
than accepting any value from a claim.

---

## 2. Result

**Section 5's `q` and `p` are correct. No repair was needed.**

`36 checks, 0 DIFFER` (`outputs/route_s5_qp.out.txt`).

| route | question | verdict |
|---|---|---|
| ALPHA | do the numerals *on the page* annihilate all six generators? | 6/6 exact symbolic zero |
| ALPHA2 | same point through the **unreduced** `R = P²/4 + P′/2 − Q` | `R − r_z ≡ 0`; `b` constant; `q ∈ U_0` |
| BETA | independent solve, compared coordinate by coordinate | 10/10 rows match |
| GAMMA | every printed approximation, half-ulp of its last place | 8/8 figures match |
| F4 | is the branch pairing load-bearing? | yes — the printed `(p,q)` break 3/6 generators on the other branch |
| F5 | exactly two solutions, both in the chart | 2 solutions, `q(q−1) ≠ 0` |

The per-coefficient ledger, which is the form the operator asked for:

| coordinate | solved | printed |
|---|---|---|
| `q` rational part | `1/2` | `1/2` |
| `q` coeff of `i√11` | `−457937/122408` | `−457937/122408` |
| `q` coeff of `i√33` | `70425/30602` | `281700/122408` (equal) |
| `p` coeff of `i√33` | `−140758792855/4086468672` | `5·(−28151758571)/4086468672` |
| `p` coeff of `i√11` | `1272782240/21283691` | `5·48874838016/4086468672` |
| `θ∞` branch 1 | `−2 − √3/9` | `−2 − √3/9` |
| `θ∞` branch 2 | `−2 + √3/9` | `−2 + √3/9` |

`q` carries no hidden `i√3` term and `p` no rational part — both checked, because
the printed *shape* asserts them.

### 2.1 The advance prediction was right, and its caveat was wrong

PREREG §5 predicted a clean pass, and named a specific most-likely failure so the
prediction could fail somewhere definite: **`122408`** — short, unremarkable, the
one integer a reader's eye slides over — or the branch pairing, whose two `θ∞`
values differ only in a sign and are printed eleven lines apart.

Both were clean. **The caveat was wrong and is recorded as wrong**, per PREREG §5.

---

## 3. Findings

### 3.1 A reader that returns 0 for what it cannot see — manufactured two DIFFERs

The first per-coefficient ledger reported **two DIFFERs** against `q` and `p`.
They were not in the paper.

sympy holds `sqrt(33)` as a *single atom*, so `expr.coeff(sqrt(11))` cannot see
it and returns `0`. The ledger compared that `0` against the printed
`281700/122408` and reported a difference — while, four lines above in the same
output, the solved `q` printed **character for character identical** to the page.

> A coefficient the reader could not read is indistinguishable from a
> coefficient that is genuinely zero.

This is the fourth appearance in this run of a check reporting an absence its own
reader could not see, and the second where it would have caused an **edit to
correct prose** had it been believed. It was caught only by diagnosing against
the raw output before touching anything.

Repaired by decomposing in an explicit basis `{1, √3, √11, √33}`, and the
decomposer was given both controls — a positive one asserting `√33` is *seen* as
the `√33` coordinate rather than returned as 0, and a refusal when an expression
does not lie in the field. The refusal fired immediately on a malformed call,
which is the guard working rather than a defect.

### 3.2 An uncaught traceback re-opens the exit-code collision

CT-S46 finding 3.9 separated **refusal (2)** from **finding (1)**, so that a
broken instrument and a real defect in the paper are distinguishable to a caller.

An uncaught traceback reintroduces exactly that collision through a different
door: Python exits **1** on an unhandled exception. This session hit it on an
`AttributeError` (`sp.nstr` does not exist) and the run reported `EXIT=1` with no
output file — the same code the script uses for "a printed figure is wrong".

Repaired with an excepthook giving a crash its own code **3**, recorded in the
output file rather than only on stderr, and the control harness scores a crash as
**MISSED**, never as a detection.

### 3.3 A vacuity arm that was a no-op, reported as such

The vacuity pre-check is the defect class itself rather than a generic
perturbation: transpose the last two digits of each printed integer and require
the system to break. Five of six were CAUGHT, each breaking 3 of 6 generators.

The sixth, **`q_B = 281700`, ends in two identical digits**, so its transposition
is a **no-op**. It was reported `SKIPPED` with "sensitivity NOT yet demonstrated"
— never as `CAUGHT`, per PREREG V2, because a no-op mutation scoring as a
detection is a false control.

That left one coefficient with no sensitivity evidence at all, so a
**supplementary arm** was added (`281700 → 821700`, CAUGHT). Adding an arm is not
moving a threshold; the distinction matters, and it was legible only because the
harness prints `SKIPPED` as its own verdict rather than folding it into a pass.

### 3.4 The Jimbo filename denotes two different pages

Ruled: do not rename (earlier sessions cite by hash), but a record three sessions
back is not enough given the name has now caused two defects. A `README.md` was
**added** beside the images.

Folios **read off each image**, not inferred from filename or page index:

| file | sha256 | folio | content |
|---|---|---|---|
| `CT-S21/pages/jimbo_p1152.png` | `05fecc96…` | **1153** | (3.4)–(3.7), Stokes multipliers, (A2)/(A3) — **no PV dictionary** |
| `CT-S21/pages/jimbo_printed1152.png` | `42fffb7b…` | **1152** | α, β, γ, δ and (A1) — supports `eq:jimbo` |
| `CT-R1-AUDIT/coldpackets/jimbo_p1152.png` | `84f548ce…` | **1152** | α, β, γ, δ and (A1) — **correctly named** |

So the string `jimbo_p1152.png` **denotes two different pages** in this tree and
is correct in one location and wrong in the other. That is a stronger statement
than "a file is misnamed", and it means the images must be resolved by hash. The
misnamed image also has byte-identical copies in `CT-S23-OUTSIDER-READ/packet/`
and `CT-S46/refs/`; those sessions are untouched.

Adding a sibling file strands no digest and edits no earlier session.

### 3.5 The `S16-R18-02` sign error is in the claim text, not only the display

The ruling framed this as "a `PROVEN` claim whose *typeset display* was defective
while its result was correct". Checking the record before writing the
supersession shows it is worse than that: **the sign is in the AEAL record
itself.**

`S16-R18-02`'s claim text states one quantity twice, and the two statements
differ by exactly a sign:

- unfactored: `z(4pqt − 4pq − 4pt + 4p + q³t² − q³ − 2q²t² + 2q² + qt² − q)/4` — **correct**
- factored: `−z(q−1)(t−1)(4p + q²t + q² − qt − q)/4` — **wrong sign**
- true: `+z(q−1)(t−1)(4p + q²t + q² − qt − q)/4`

Verified here by factoring the unfactored form directly, with two rejecting
controls (a sign flip on the last term; denominator 2 for 4) so that "accepted"
cannot mean "the comparison never fires".

**The result is unaffected**, and the label stays `PROVEN`: the corrected reading
still makes `b(z)`'s first term exactly `z·B₁[1,2]` and the printed reading still
does not. What was defective is the recorded display. `S47-12` carries
`supersedes: S16-R18-02`; the original stands **unedited**.

### 3.6 A control arm exposed a missing pre-condition, not a bad arm

Arm M5 corrupted System C's `s₊`, and the mutant **crashed** (`PolynomialError`)
instead of reporting a difference. The harness scored it `MISSED` — a crash is
not a detection — which is what made the cause visible rather than letting a
7/8 look like an 8/8.

The cause is a real gap in the instrument. The entire construction depends on
`r_z` having denominator exactly `D² = z²(z−1)²`: only then is matching `R`
against `r_z` an equality of two quartics, and only then is `Nz·D²/Dz` a
polynomial. **Nothing checked it.** In the unmutated run it holds, so the
dependency was invisible.

Repaired in the *script*, not the arm, and the arm was reclassified `halt`
accordingly — because a broken transport is a fact about the instrument's input,
not a finding about the paper, and the refusal/finding distinction is exactly
what CT-S46 separated the exit codes to preserve.

### 3.7 The arm the pass exists for was missing

Diagnosing M5 exposed a larger hole: **no arm asked whether route ALPHA reports a
DIFFER when the page itself carries a wrong digit** — the one defect the entire
formula pass was commissioned to catch. Every arm mutated the *script*; the
`.tex` was never touched, because the source-digest guard would refuse.

Arm **M9** now mutates `section5.tex` itself (`457937 → 457973`, a genuine
transposition) *and* updates the expected digest, so that the arm tests
detection rather than merely re-testing the digest guard that M3 already covers.

A guard that makes a class of mutation impossible will quietly prevent anyone
from ever testing what lies behind it.

### 3.8 A vacuity pre-check masked the finding it was there to make meaningful

Arm M9 — the arm that plants a real transposition in `section5.tex` — returned
**exit 2 (refusal) where exit 1 (finding) was required**, and the reason is the
sharpest instrument defect of the session.

A transposition is an **involution**. The vacuity arm transposes the last two
digits of each parsed integer; applied to a page that *already* carries
`457973`, it restores `457937`, the true value. The generators then vanish, the
arm reports `MISSED`, and the script refuses with *"route ALPHA cannot see a
transposition in q_A"* — while the actual state of affairs is that **the page
carries one**.

So a wrong digit on the page would have been announced as a broken instrument.
That is exactly the refusal/finding collision CT-S46 separated the exit codes to
prevent, reappearing at the level of *ordering* rather than of exit codes.

The general rule, and the repair:

> **A vacuity pre-check guards a PASS, not a FAIL.** A failing observable is
> self-evidencing and needs no such guard. Running the arms unconditionally
> before the observable lets them convert a finding about the paper into a
> refusal about the instrument.

Repaired by evaluating the observable first: if the parsed values already fail
the matching system, the vacuity block is reported `SKIPPED` as moot and the
DIFFER stands. The arms otherwise run exactly as pre-registered, so no threshold
moved.

### 3.9 Final harness state

After the repairs of 3.1–3.8 the control harness reports **9 CAUGHT, 0 MISSED,
0 SKIPPED (of 9)** (`outputs/mutants_route_s5_qp.out.txt`), with M9 — the only
arm that mutates `section5.tex` itself — now returning exit **1 (a finding)**
rather than exit 2. The harness asserts its baseline (`36 checks, 0 DIFFER`)
before any arm is interpreted, runs every arm in a `TemporaryDirectory` with its
own `refs/` and `outputs/`, and re-reads the real output afterwards: it still
reports `ROUTE S (section 5 q,p): 36 checks, 0 DIFFER`, so no arm touched the
evidence its claims cite.

Runtime, recorded because it bounds what can be re-run: `route_s5_qp.py` ≈ 500 s,
dominated by `sp.solve` on six generators in four unknowns; the nine-arm harness
≈ 4 843 s. The `gen_values` numeric screen added this session short-circuits only
the NONZERO verdict — it can never turn a nonzero value into zero — and did not
materially reduce the solve-bound runtime.

---

## 4. Claims

See `claims.jsonl`. Labels are the five that partition the Channel Theory corpus.

| id | label | subject |
|---|---|---|
| S47-01 | VERIFIED | source resolved positively by hash + content guard |
| S47-02 | VERIFIED | route ALPHA — the page's numerals annihilate all six generators |
| S47-03 | VERIFIED | route ALPHA2 — the unreduced `R`, no `b′ = 0` assumed |
| S47-04 | VERIFIED | route BETA — per-coefficient ledger |
| S47-05 | VERIFIED | route GAMMA — eight printed approximations |
| S47-06 | VERIFIED | transposition arms, including the SKIPPED no-op and its replacement |
| S47-07 | VERIFIED | the `sqrt(33)` reader defect that manufactured two DIFFERs |
| S47-08 | VERIFIED | a crash exits 1; refusal/finding/crash separated as 2/1/3 |
| S47-09 | VERIFIED | nine control arms, baseline asserted, scratch tree |
| S47-10 | STRUCTURAL | scope limit: the other twelve displays are untouched |
| S47-11 | INSPECTED | the Jimbo folios, read off the images |
| S47-12 | PROVEN | **supersedes S16-R18-02** — sign corrected in the record |
| S47-13 | VERIFIED | the unchecked `D²` denominator pre-condition, found by arm M5 |
| S47-14 | VERIFIED | a guard that blocks a mutation class blocks testing behind it |
| S47-15 | VERIFIED | a vacuity pre-check guards a PASS, not a FAIL (§3.8) |

---

## 5. What was NOT established

- **The other twelve route-S-corpus displays were not re-derived.** Nothing here
  licenses a statement about `S1-04`, `S26-01`, `S3B-02`, `S4-03`, `S6-C18`,
  `S16-03`, `S17-10` or `S22-12`. This was fixed in PREREG §6 before running.
- **The generator construction is inherited, not independently re-derived here.**
  It is built from the construction recorded in `CT-S16/locate_final.py`;
  `S25-01` is what establishes it independently. This session's contribution is
  that the values are *parsed off the page* rather than taken from a record.
- **Route BETA's solve and route ALPHA share that construction**, so they are two
  routes to the same point, not two independent parties. ALPHA2 is the partial
  answer — it avoids the `b′ = 0` reduction — but the family objects are common
  to all three.
- **No claim is made that the paper builds**, or that anything outside section 5
  lines 116–130 is correct.

---

## 6. Open questions for the operator

1. **Is the formula pass now closed?** Twelve route-S-corpus displays remain
   routed-but-not-re-derived by deliberate ruling. If that residue should stay
   permanently, it is worth saying so in the paper's own limits section rather
   than only in session records.
2. **Should `S25-01`'s scope be annotated?** It says the *recorded* solutions
   annihilate the system, which is true and was read during this run as covering
   the printed ones. It does not. A one-line supersession would prevent the next
   reader making the same inference.
3. **The `README.md` precedent.** This is the first marker file added beside an
   earlier session's artefacts. If that is the right pattern for "a defect in an
   append-only tree that cannot be repaired", it should become a rule; if it is a
   one-off, it should be said so.
4. **`S16-R18-02`'s supersession is the first to correct a `PROVEN` claim's
   text.** The label was kept because the result stands. Confirm that is the
   intended reading, since it means a `PROVEN` claim in the corpus contains a
   formula that is wrong as written.

---

## 7. Uncommitted files

All new. Nothing in this session modifies any existing file.

```
sessions/2026-09-17/CT-S47-FORMULA-S5-QP/
  PREREG.md
  REPORT.md
  claims.jsonl
  scripts/route_s5_qp.py
  scripts/mutants_route_s5_qp.py
  scripts/check_r18_sign.py
  scripts/emit_claims_s47.py
  outputs/route_s5_qp.out.txt
  outputs/mutants_route_s5_qp.out.txt
  outputs/check_r18_sign.out.txt
  refs/section5.tex          (copy, sha256 af25048b9b62…)
  refs/locate_final.py       (copy, CT-S16 construction, read-only reference)

sessions/2026-09-17/CT-S21-DEPOSIT-PREP/pages/
  README.md                  (ADDED beside the images; no existing file touched)
```

Pre-existing modifications elsewhere in the worktree (`2026-06-16`, `2026-06-18`
and various untracked `2026-05-02` files) predate this session and are not
mine.
