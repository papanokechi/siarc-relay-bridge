# REPORT — CT-S38-NOTATION-SYMBOLS

Session: `sessions/2026-09-17/CT-S38-NOTATION-SYMBOLS/`
Scope: the three rulings overturning the CT-S36 symbol names. Draft only.
Nothing committed, pushed, tagged, deposited or submitted. No network call.

---

## 1. What was done

1. Built a symbol-collision index over the corpus and reported it (ruling 1).
2. Screened candidate letters mechanically against clauses fixed in advance,
   and proposed a pair (ruling 1).
3. Re-lettered `theorem.tex` and `section1.tex` by script, preserving the
   pre-rename files in `refs/` with their hashes, and confirmed by a diff of
   the **rendered** text that nothing but symbols changed (ruling 2).
4. Measured the section-1 collision count instead of assuming it, and
   adjudicated each candidate against printed evidence (ruling 3).
5. Ran eight pre-registered control arms; 8/8 CAUGHT for the stated reason.

---

## 2. The index — the useful output

`scripts/symbol_index.py` → `outputs/symbol_index.out.txt`

| source | kind | bytes | occurrences | origin |
|---|---|---|---|---|
| `theorem.tex` | tex | 25 102 | 1007 | instructed |
| `section1.tex` | tex | 13 398 | 269 | instructed |
| `OUTLINE.md` rev 6 | prose | 50 919 | 101 | instructed |
| `section3.tex` | tex | 12 727 | 197 | **added** |
| `section4.tex` | tex | 9 036 | 174 | **added** |
| outline-cited claims (89) | prose | 49 494 | 570 | instructed |

**82 distinct bases, 274 distinct keys, 2318 occurrences, 38 collision
candidates.**

`section3.tex` and `section4.tex` were added to the four sources the ruling
names. Excluding them would have hidden both of the collisions reported next,
since both live in section 3.

Extraction is deliberately conservative: math mode only for `.tex`, and for
prose a bare single letter is not a symbol unless it carries a subscript, is a
spelled Greek name, or is flanked by mathematical punctuation. The index
under-reports rather than manufacturing meanings out of English.

### 2.1 The two letters the ruling named — both carry more meanings than stated

**`q` carries three meanings, not two** (`S38-02`, STRUCTURAL):

| meaning | where | occurrences |
|---|---|---|
| Okamoto / van der Put–Saito chart coordinate | `section4.tex`, claims | 53 |
| normalised sequence `q_n` and limit `q_∞` | `section1.tex` | 8 |
| **coefficients `q_0, q_1, q_2` of System B's transcription** | `section3.tex` | 4 |

The third was not previously recorded: `q_2 = 4(2√3−3)z²(z²+z+3)`.

**`λ` carries four meanings** (`S38-03`, STRUCTURAL): the roots of `b`
(`section1.tex`); the indicial variable, where `section3.tex` states *the
indicial polynomial is λ²*; the rank-1 twist scalar `A → A + λ·Id` of claim
`S17-01`; and the parameter of the moduli space `M_{t,λ}`.

### 2.2 `r` is the worst base in the corpus (`S38-04`, VERIFIED)

167 occurrences under **29 distinct keys** across 5 sources, spanning the
normalised sequence, the roots of `b`, van der Put–Saito's Katz invariant
`r(c)`, the normal potential `r(φ)`, the fixed `r ∈ C` of `theorem.tex`
Step 3, and `r_A, r_B, r_C` in `section3.tex`.

### 2.3 The collision inside the PROVEN proof file (`S38-05`, STRUCTURAL)

In `theorem.tex` the single token **`r_1` denotes two different objects**: the
first term of the sequence at `eq:rnrec` (`r_0 = r_1 = 1`), and the first root
of `b` in *"`r_1,…,r_d ∈ C` the roots listed with multiplicity"*.

`section1.tex` already records this ambiguity **for the deposit**. What is new
is that it is live in the proof file that carries cold-read PROVEN status. It
is also the reason a blanket substitution was not used.

---

## 3. The proposal

`scripts/check_proposal.py` → `outputs/check_proposal.out.txt` — **exit 0**

> **`ψ_n`, `ψ_∞`** for the normalised sequence and its limit
> **`ν_1, …, ν_d`** for the roots of `b`

Admissible under all six clauses (`S38-06`, VERIFIED). Ten controls — `q`,
`λ`, `r`, `ρ`, `ϱ`, `μ`, `l`, `ω`, `χ`, `η` — were each rejected, and each on
the clause named in advance: **10/10**.

The letters are screened against the same index that is reported, by importing
it, so the proposal cannot be accepted against a second reading of the corpus.

### 3.1 Why these two, and why not the obvious alternatives

The deciding clause is C6: a candidate's **homoglyph partner must not occur in
any source where the object being renamed occurs.**

| candidate | partner | verdict |
|---|---|---|
| `ω` | `w` | rejected — `w` in `theorem.tex` ×12, `section1.tex`, `OUTLINE.md` |
| `χ` | `x` | rejected — `x` in all three home sources |
| `η` | `n` | rejected — `n` in `theorem.tex` ×342 |
| `ϱ` | `ρ` | rejected — variant glyph of an exponent letter |
| `μ`, `σ`, `α`, `κ` | — | exponent letters |
| `l`, `ο`, `ι`, `υ` | — | read as another letter in isolation |
| **`ψ`** | none | **admissible** |
| **`ν`** | `v` | **admissible** — `v` occurs only in `section4.tex` and claim texts, where the roots never appear |

`ψ` was given to the sequence rather than the roots because the sequence is by
far the more frequent object and `ψ` has the cleanest profile of the free pool.

### 3.2 Residual risk, disclosed rather than screened

Recorded in the claim's `review_note`, not only here:

- `ψ` sits near `φ`, which occurs **only** as the subscript of `L_φ`;
- `ν` sits beside the index `n` in `b(n) = β_d ∏ (n − ν_i)`.

Neither is a homoglyph collision under the clause applied. Both are real
typographic adjacency and the operator should see them before the names are
fixed.

---

## 4. The re-lettering (ruling 2)

`scripts/reletter.py` → `outputs/reletter.out.txt` — **exit 0, 10/10
pre-write checks**

Originals preserved first, copies verified byte-identical:

| file | bytes | sha256 |
|---|---|---|
| `refs/theorem-pre-S38.tex` | 25 649 | `3d66d72fe1dfc5eba461ea1355ac10a1392457b9aaf78c82cfa9744daddb2695` |
| `refs/section1-pre-S38.tex` | 13 660 | `39ddd724524f2a7e38febbf32cfd4d575e319b28b13bb200da022b10fa7423ca` |
| `theorem.tex` (new) | 25 376 | `21fb5e3e4bf66b72348ae74bd5a017c84eced9169c03a991672d54db93b7de04` |
| `section1.tex` (new) | 13 380 | `ae40f6ad617d2cc13ce190f87efecc19db4cee485f49a1b2412f6943b530f4be` |

`theorem.tex`: `\rinf → \psiinf` (24 + its definition); `r_n → ψ_n` (30),
`r_{n−1}` (14), `r_{n−2}` (6), `r_k` (1), `r_{k−1}` (1), `r_0` (4), `r_1` (5);
`r_i → ν_i` (17); the root phrase rewritten as a literal (1).

**20 bare `r` left untouched** and asserted unchanged — the fixed `r ∈ C` of
Step 3, `r(c)` and `r(φ)`.

`section1.tex`: `q_… → ψ_…` (10), `λ → ν` (12). The four deposited names on
the right of the correspondence footnote — `r_n`, `r_∞`, `r_1`, `r_d` — were
asserted unchanged, as was the Zenodo id `10.5281/zenodo.19941678`. The
footnote now reads `ψ_n ↔ r_n`, which is its purpose.

The buffer is validated before anything is written, so a failed run leaves no
half-renamed file on disk.

### 4.1 The rendered diff, and a check that had to be rebuilt

`scripts/rendered_diff.py` → `outputs/rendered_diff.out.txt` — **exit 0**

The test runs in the invertible direction. `theorem.tex` used one letter for
both objects, so `r → {ψ, ν}` is not a function of the rendered character but
its inverse is; `ψ → r`, `ν → r` applied to the new rendered text must
reproduce the old. For `section1.tex` the inverse is `ψ → q`, `ν → λ`.

**The first two runs failed, and neither failure was real** (`S38-10`,
STRUCTURAL):

1. *Ordered comparison.* `pdftotext` orders tokens by glyph position, and
   `r → ψ` changes glyph **widths**, so a stacked display is emitted with its
   limits interleaved differently while containing identical characters. The
   non-whitespace counts were already equal on both sides (14139 = 14139,
   8546 = 8546), which is what exposed it.
   **PyMuPDF confirmed the difference — and was wrong**, because it shares the
   same reading-order sensitivity. A second extractor is independent only with
   respect to failure modes it does not share. That is the sharpest lesson of
   this session.
2. *Token comparison.* Residual differences were pure space placement —
   `pdftotext` split `nd` into `n` `d`; PyMuPDF joined `Γ(x` `+` `1)` into
   `Γ(x+1)`. Space placement is not preserved under a glyph-width change
   either, so it cannot be the observable.

The observable is now the **whitespace-stripped character multiset per page**,
which is invariant under both reading order and space placement and still
fails on any character added, dropped or altered.

Result (`S38-07`, VERIFIED): equal page by page for both documents, on
**both** extractors — PyMuPDF now agrees, on an observable it does not share a
failure mode with; non-whitespace counts equal; pages 8 → 8 and 4 → 4; no
undefined references; and the decisive test **rejects a single deleted
character**, so it is not vacuous.

The ordered result is still printed, marked informational.

---

## 5. The section-1 count (ruling 3) — measured, not assumed

`scripts/triage.py` → `outputs/triage.out.txt`

No artefact in the corpus holds the "6 / ~65 / ~9" triage, so it was
re-derived. Of 42 bases occurring in `section1.tex`:

- **27 candidates** under the necessary condition (a key used only outside §1);
- 14 carry identical keys inside and outside — same object;
- 1 is confined to §1.

Adjudicated against the printed evidence in `outputs/adjudicate_ctx.out.txt`
(`S38-08`, STRUCTURAL):

**12 genuine** — `q`, `λ`, `r`, `M`, `P`, `Q`, `ρ`, `s`, `A`, `L`, `u`, `β`.

| base | the distinct objects |
|---|---|
| `M` | the bound `M < ∞` (`theorem.tex`) / monodromy `M_∞` (§1) / moduli space `M_{t,λ}` |
| `P`,`Q` | the coefficients of `∂²+P∂+Q` (§1) / `Q_n` denominators (§1 **itself**) / `P_n` minimal solution (`theorem.tex`) / `P_C`,`Q_C` system coefficients |
| `s` | growth exponent `s` (§1, `theorem.tex`) / local exponents `s_±` (§1 **itself**) |
| `A` | the object `A` (§1) / residue matrices `A_0,A_1,A_∞` (§4) |
| `L` | the operator `L_φ` (§1) / the bound `L := exp(Σ 1/(b(k)b(k+1)))` (`theorem.tex`) |
| `u` | the uniformiser `u = √z` (§1) / `u_k := b(k)/(β_d k^d)` (`theorem.tex`) |
| `β` | coefficients `β_k` of `b` (§1) / the Painlevé parameter of `(α,β,γ,δ)`, DLMF 32.2.5 (§4) |

**3 marginal** — `N`, `k`, `e`. **12 not collisions** — `B`, `D`, `K`, `ξ`,
`a`, `b`, `f`, `g`, `n`, `t`, `y`, `z`.

**The measured figure is 27 candidates and 12 genuine, against the ruling's 6,
and the ruling named 2 of the 12.** Reported as measured; the number was not
adjusted toward the expectation.

### 5.1 A live defect found by the instrument (`S38-09`, VERIFIED)

`section1.tex` asserts:

> *"The letter `ρ` is never used for anything else"*

and `section3.tex` uses `ρ_± = (−1 ± i√11)/2` for System B's finite singular
points. **The assertion in the drafted section 1 is false as the corpus
stands.**

Reported, not repaired. Repairing it means either re-lettering `ρ_±` in §3 —
which ruling 3 defers to that section — or weakening a sentence of §1, which
is a content change outside the symbol substitution and would break the
rendered-text equivalence just established. **This needs an operator ruling.**

---

## 6. Controls

`scripts/mutants_s38.py` → `outputs/mutants_s38.out.txt` — **8/8 CAUGHT**

An arm is CAUGHT only on non-zero exit **and** the expected condition named in
the output **and** no `Traceback`/`SyntaxError`/`NameError`. Every mutation is
a valid edit, never a syntax break. Arm 4's letter is discovered from the index
at run time (`\C`), not taken from the checker's own forbidden list.

Arms 1–4 (proposal screen, each on the clause named in advance) · 5 (a word of
prose also changed → equivalence fires) · 6 (rename changed nothing →
non-vacuity fires) · 7 (a source emptied → reader integrity refuses) · 8 (the
`B` sensitivity control removed → vacuity pre-check fires).

**Two arms MISSED on the first run, and both were real** (`S38-11`, VERIFIED):

- Arm 7 broke with `AttributeError` — a defect in my driver, which passed a
  `str` where `SOURCES` holds a `Path`. Caught only because `broke=True` is
  judged separately from `reason`.
- Arm 8 did not fire: adding `B` to `NOT_SYMBOLS` left 5 `B` keys standing,
  which revealed that **`scan_prose` never consulted `NOT_SYMBOLS` while
  `scan_tex` did** — a token excluded from the TeX reading was still admitted
  from prose. The index depended on which *kind* of source a symbol occurred
  in. Repaired so both readers apply the same exclusion.

Arm 7 also exposed that an **emptied** source file reads without error, so
`read_or_fail` alone could not distinguish "no collisions" from "I could not
see the content". A per-source non-vacuity guard was added.

Claim emission is validated **before** the write, and the index was confirmed
byte-identical after `claims.jsonl` was emitted into the corpus
(`7d4a58b0ecc034f8…` both sides), so no claim cites a digest that no longer
resolves.

---

## 7. What was NOT established

- **The letters are a proposal, not a ruling.** `ψ`/`ν` pass a mechanical
  screen; they have not been approved.
- **Only §1 and `theorem.tex` were re-lettered.** `section3.tex` and
  `section4.tex` still carry `q_0,q_1,q_2`, the indicial `λ`, and `ρ_±`. The
  `q` and `λ` collisions are therefore **resolved in §1 and the proof file
  only, not corpus-wide.**
- **`r` is only partly disambiguated.** The sequence and the roots have left
  it; `r(c)`, `r(φ)`, `r ∈ C` and `r_A,r_B,r_C` remain.
- **Ten of the twelve genuine §1 collisions are untouched** — `M`, `P`, `Q`,
  `ρ`, `s`, `A`, `L`, `u`, `β` and the residue of `r`.
- The rendered-diff equivalence is established on a
  **whitespace-stripped character multiset**, which is anagram-blind within a
  page. Combined with equal counts, unchanged page counts and a source-level
  substitution validated by 10 pre-write checks, but it is not a proof of
  character-sequence identity.
- No PDF of the full paper was built; only the two standalone documents.

---

## 8. Open questions for the operator

1. **Approve or replace `ψ_n`, `ψ_∞`, `ν_1..ν_d`**, given the disclosed
   adjacency of `ψ` to `φ` and of `ν` to `n`.
2. **`ρ`.** §1 asserts exclusivity that §3 contradicts. Re-letter `ρ_±` in §3,
   or weaken the §1 sentence? Either is a change this session's scope forbids.
3. **`Q` and `s` collide inside §1 itself** — `Q` as the potential in
   `∂²+P∂+Q` against `Q_n`, and `s` as the growth exponent against `s_±`.
   These do not resolve themselves in a later section.
4. The measured genuine count is **12, not 6**. Close the remaining ten now,
   or hold them for the post-Group-E pass?
5. `section3.tex`/`section4.tex` were **added** as index sources. Confirm.
6. A second notation pass after Group E is **recommended, not performed**.

---

## 9. Uncommitted files

All under `sessions/2026-09-17/CT-S38-NOTATION-SYMBOLS/`. Nothing outside this
folder was written; no earlier session's file was modified.

```
PREREG.md
REPORT.md
claims.jsonl                     13 claims
theorem.tex                      re-lettered
section1.tex                     re-lettered
section1_standalone.tex          copied build wrapper
refs/theorem-pre-S38.tex         pre-rename, hashed
refs/section1-pre-S38.tex        pre-rename, hashed
scripts/symbol_index.py
scripts/check_proposal.py
scripts/triage.py
scripts/reletter.py
scripts/rendered_diff.py
scripts/mutants_s38.py
scripts/emit_claims_s38.py
outputs/symbol_index.out.txt
outputs/check_proposal.out.txt
outputs/triage.out.txt
outputs/adjudicate_ctx.out.txt
outputs/reletter.out.txt
outputs/rendered_diff.out.txt
outputs/mutants_s38.out.txt
outputs/emit_claims_s38.out.txt
outputs/build/                   four PDF build trees
```

## 10. Gate summary

| gate | verdict |
|---|---|
| `symbol_index.py` | exit 0 — 82 bases, 274 keys, 38 candidates; vacuity controls ok |
| `check_proposal.py` | exit 0 — PROPOSAL ADMISSIBLE; controls 10/10 |
| `triage.py` | exit 0 — 27 candidates measured against the ruling's 6 |
| `reletter.py` | exit 0 — RE-LETTERED; 10/10 pre-write checks |
| `rendered_diff.py` | exit 0 — EQUIVALENT UNDER THE SYMBOL MAP ALONE |
| `mutants_s38.py` | exit 0 — 8/8 CAUGHT for the stated reason |
| `emit_claims_s38.py` | exit 0 — 13 claims, 9/9 pre-write checks |

---

# ADDENDUM — the rulings round (2026-09-20)

Executed after the report above, on the operator's rulings covering CT-S38 and
CT-S37 Group B. The report above stands as the record of the session as first
delivered; nothing in it is rewritten. This addendum states what changed.

## A1. Names accepted (`S38-14`, STRUCTURAL)

`\psi_n`, `\psi_\infty` for the normalised sequence and its limit, and
`\nu_1..\nu_d` for the roots of `b`, are ACCEPTED, with both disclosed
adjacencies accepted as acceptable. No re-screening was performed: the clause
test that admitted them is `S38-06`, and the ruling is the operator's.

## A2. The `r_1` ambiguity inside `theorem.tex` — confirmed resolved (`S38-15`, VERIFIED)

The operator's sharpest question, and the one that could have been a live
defect: *if the rename left them both as `\nu_1` or both as `\psi_1`, that is a
defect the page-count check would not catch.*

It did not. The pre-rename file used `r_1` for two distinct objects, **6
occurrences**:

| role | old | new | count |
|---|---|---|---:|
| first root of `b`, in `r_1,\dots,r_d are the roots` | `r_1` | `\nu_1` | 1 |
| first term of the normalised sequence | `r_1` | `\psi_1` | 5 |
| last root of `b` | `r_d` | `\nu_d` | 1 |

The new file has exactly one `\nu_1`, exactly one `\nu_d`, both inside the root
sentence, and exactly five `\psi_1`, all in sequence contexts. No `r_1` or `r_d`
survives.

**This is not visible to any check the session already had.** A collapse onto
one letter compiles, keeps the page count at 8, and passes the rendered-multiset
diff under a map that sends both `\psi` and `\nu` back to `r` — the diff would
report EQUIVALENT on a file whose ambiguity was intact. Three arms cover exactly
that blind spot, and all three are CAUGHT:

- **A6** both roles collapsed onto `\psi_1`;
- **A8** both roles collapsed onto `\nu_1`;
- **A7** one sequence site left un-renamed.

`R12` is the non-vacuity arm: it asserts the *old* file really did overload
`r_1` at 6 occurrences. Without it, R8–R11 would pass on a file that had never
had the ambiguity.

## A3. The three section-1 repairs (`S38-16`, VERIFIED)

Ruling: **fix §1, not §3.** §3's `\rho_\pm` is established corpus usage; §1's
sentence was a false claim *about the paper*. The operator also moved `Q` and
`s` forward from the deferred list, because both collide **inside §1**.

All three follow §1's own existing precedent — the sans-serif `A,B,C` versus the
coefficients `A,A',C` are resolved by *stating the convention*, not by renaming
a letter:

1. **ρ** — the sentence *"the letter ρ is never used for anything else"* is
   **gone**, replaced by a statement that ρ carries two meanings separated by
   the presence of a subscript, the subscripted `\rho_\pm = (-1 \pm i\sqrt{11})/2`
   being §3's finite singular points of System B, and neither being a root of
   `b`. **No `\ref` to §3** — §1 builds standalone, and a forward reference
   would have introduced the undefined reference the build check exists to
   catch.
2. **Q** — the normal-form coefficient `Q` separated from the denominators `Q_n`.
3. **s** — the unsubscripted growth exponent separated from the actions `s_\pm`.

12 checks pass, 8 arms CAUGHT, build unchanged at **4 pages, no undefined
references**.

### A3.1 The three-stage audit trail, and why `S38-07` had to be narrowed

The rename and the prose repair are separately auditable:

| file | state | sha256 |
|---|---|---|
| `refs/section1-pre-S38.tex` | before the rename | `39ddd724524f2a7e…` |
| `refs/section1-symbols-only.tex` | after the rename, before the repair | `ae40f6ad617d2cc1…` |
| `section1.tex` | after both | live |

`rendered_diff.py` had pointed its `section1-new` job at the **live**
`section1.tex`. Once the prose repairs landed, that comparison would have mixed
the rename with the repairs and made the equivalence verdict meaningless — the
same shape as CT-S35's `S35-16`, tooling left pointing at the wrong artefact
while every content check stayed green. It is repointed at the snapshot, and
`guard_targets()` resolves the intended target **positively**: the snapshot must
still carry the pre-repair ρ sentence, and the live file must not. A path string
is not evidence of which file is being read.

`S38-07` now states its scope explicitly, and a pre-write check in the emitter
fails if that scope statement is ever dropped.

`S38-09` is amended in the same spirit: it recorded the ρ defect as *"reported,
not repaired"*, which the ruling made false. It now records the finding and
points at `S38-16` for the repair — the claim keeps its history without
asserting a present state that no longer holds.

## A4. P0 amendment F — the label list is five (`S38-17`, VERIFIED)

Ruling: *P0 is stale, not the corpus.* Established by census rather than by
assertion — `scripts/label_census.py`, walking every `claims.jsonl` under
`sessions/2026-09-17/` except this session's own:

| label | claims |
|---|---:|
| PROVEN | 140 |
| VERIFIED | 170 |
| **INSPECTED** | **215** |
| STRUCTURAL | 118 |
| CONJECTURED | 6 |
| **total** | **649** |

The operator's figure was `74+`. The real figure is **215** — `INSPECTED` is not
a marginal fifth category but **the most common label in the corpus**, at 33.1%,
more than `PROVEN` and `CONJECTURED` combined. The five **partition** the corpus,
so the amendment *closes* the list rather than extending an open one.

`P0-AMENDMENT-F-LABELS.md` carries the replacement text. Its closing line —
*"A reading is INSPECTED, not PROVEN"* — is the positive half of `CT-R1-AUDIT`
rule 1(a), which until now said only what such a claim may **not** be labelled.

## A5. The outline citation form (`S38-18`, VERIFIED)

Ruling: *fix the outline; an alias in the checker is a workaround for a citation
defect.* Both bare `S9-PVPARAMS-*` citations in `OUTLINE.md` are now
`CT-S9-PVPARAMS-*`, and every id cited resolves to exactly one claim. Three
controls CAUGHT.

**Not done, deliberately:** the alias is *not* removed from
`CT-S37-DRAFT-B/scripts/draft_check.py`. That file is an earlier session's, and
its recorded claims cite the sha256 of its output; editing and re-running it
would invalidate `S37B-07`'s digest to fix a checker that is no longer wrong
about anything. Two consequences, both for the Group B re-run the operator has
already scheduled:

- `draft_check.py` still prints `NOTE: OUTLINE.md cites this family as
  S9-PVPARAMS-*`, **which is now false**;
- mutant `M7` expects the short form to resolve *and be reported*; once the alias
  goes, that arm should invert — the short form must **fail**.

Both belong in that session, with `M7` inverted in the same edit.

## A6. Ruling 3 — no action, recorded (`S38-19`, INSPECTED)

*"Exclusions are VERIFIED" versus the corpus* — the corpus won. **Nothing is
relabelled.** Recorded as a claim so a later reader does not rediscover the
conflict and repair it in the wrong direction. This is also the session's first
use of the label amendment F adopts.

## A7. An ordering trap, closed structurally rather than by ordering

Both new checks **walk the corpus**, and this session **writes into** it. Under
the standing rule — run gates, emit, never re-run a corpus-walking gate — the
cited digests would have been correct but fragile: a later re-run would change
the output and leave `S38-17` and `S38-18` citing digests that resolve to
nothing. That is `S34`'s defect exactly.

Rather than manage it by ordering, both scripts now **exclude this session's own
`claims.jsonl` by construction**, with the exclusion asserted rather than assumed
— check `C6` requires the file to *exist* **and** to be absent from the walk,
because without the existence half the exclusion is satisfied vacuously.

Verified empirically: both outputs are **byte-identical** across a re-run taken
after `claims.jsonl` was emitted. The gate order no longer has to be remembered.

## A8. Gate summary — the rulings round

| gate | verdict |
|---|---|
| `symbol_index.py` | 82 bases, 274 keys, 2318 occurrences, 38 candidates — unchanged by the outline edit |
| `check_proposal.py` | PROPOSAL ADMISSIBLE; controls 10/10 |
| `triage.py` | 27 candidates measured against the ruling's 6 |
| `rendered_diff.py` | EQUIVALENT UNDER THE SYMBOL MAP ALONE; target guard fires |
| `mutants_s38.py` | 8/8 CAUGHT for the stated reason |
| `check_s1_repairs.py` | **SECTION-1 REPAIRS VERIFIED** — 12 checks, 8 arms CAUGHT |
| `label_census.py` | **P0's FOUR-LABEL LIST IS STALE; THE CORPUS CARRIES FIVE** — 6 checks, control CAUGHT |
| `check_outline_citation.py` | **OUTLINE CITES THE CORPUS FORM** — 3 checks, 3 arms CAUGHT |
| `emit_claims_s38.py` | 19 claims, 12/12 pre-write checks |

19 claims, **19/19 cited digests resolve on disk**, every script present.

## A9. Files touched in this round

Modified in this session's folder: `section1.tex`, `scripts/rendered_diff.py`,
`scripts/emit_claims_s38.py`, `claims.jsonl`, `REPORT.md`, and the `outputs/`
files re-generated above.

New: `P0-AMENDMENT-F-LABELS.md`, `refs/section1-symbols-only.tex`,
`scripts/check_s1_repairs.py`, `scripts/label_census.py`,
`scripts/check_outline_citation.py`, and their outputs.

**Modified outside this session, by explicit ruling:**
`CT-S24-PAPER-OUTLINE/OUTLINE.md` — two citations, 49 916 B. This is the only
cross-session write, and it is the one the operator directed.

Nothing is committed, pushed, tagged or deposited.

## A10. Still open

- **Group A is the blocker.** §2.0's attribution paragraph does not exist, so §3
  and §4 cite a section that is not there. Group B's check cannot be re-run
  meaningfully until it is.
- The **nine deferred §1 collisions** — `M`, `P`, `A`, `L`, `u`, `\beta` and the
  residue of `r` — go to the second notation pass after Group E, per ruling 3.
- The **`CT-S26` number collision** stays ambiguous for the two existing pairs;
  cite by full folder name, never by number.
