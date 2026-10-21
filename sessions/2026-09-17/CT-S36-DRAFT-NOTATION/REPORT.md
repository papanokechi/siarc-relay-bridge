# REPORT.md — CT-S36-DRAFT-NOTATION

Draft only. Nothing committed, pushed, tagged, deposited or uploaded. All
changes are uncommitted files inside
`sessions/2026-09-17/CT-S36-DRAFT-NOTATION/`; no file from an earlier session
was modified.

---

## 0. One ambiguity resolved before starting

The task cites “the operator-approved insertion recorded at CT-S26/REPORT.md
§6 item 1”. **Two sessions are named CT-S26.**

| session | its §6 item 1 |
|---|---|
| `CT-S26-CTV17-DRAFT` | about the v1.4–v1.6 PDFs; nothing to do with a proposition |
| `CT-S26-UPPER-BOUND` | “`theorem.tex` after `prop:positive` … needs a copy-forward or an operator waiver” |

The second is plainly the one meant, and it was used. Flagged rather than
silently chosen.

---

## 1. What was done

### Task 1 — Proposition U folded into `theorem.tex`

`CT-S1-THEOREM/theorem.tex` was **copied forward** (earlier sessions are not
edited) and `\begin{proposition}[Upper bound in the positive case]` inserted
immediately after `prop:positive`’s proof, with

- `(U-finite)`  `r_n ≤ exp( Σ_{k=1}^{n-1} 1/(b(k)b(k+1)) )` for every `n ≥ 1`;
- `(U-limit)`  `1 ≤ r_∞ ≤ L := exp( Σ_{k≥1} 1/(b(k)b(k+1)) ) < ∞`;

and a four-step proof transcribed from `CT-S26-UPPER-BOUND/PROOF.md`:
monotonicity from `prop:positive`; substitution into `eq:rnrec` with
`1+x ≤ e^x`; telescoping with re-indexing; convergence from `eq:eps`.

Positivity of `b` is stated **as a hypothesis**, not assumed silently, and a
following remark records that it is load-bearing — `S26-04` exhibits three
sign-changing `b` that violate (U-finite), the worst slack `−0.04235066097` at
dps 60.

The drafting constraint from `S26-01` is honoured: the status list cites
**`S26-01`** for the upper bound and says in terms that `prop:positive` /
`S1-02` supplies only step 1 and the lower bound and **must not** be cited for
the upper half. `scripts/verify_artefacts.py` enforces this as a proximity
condition — `S1-02` must not occur inside the `prop:upper` block — so the
constraint can fail rather than merely being asserted.

`S26-06` (both inequalities are strict) is mentioned only in the status list,
because `S26-06` itself says it is “not to be stated in the paper as if it were
part of the result”.

**Build.** Two `pdflatex` passes, exit 0 both, 8 pages, `newlabel` written for
`prop:upper`, `eq:ufinite`, `eq:ulimit`, `rem:upper-positivity`, and **no
“There were undefined references”**. The single font-shape warning
(`OT1/cmr/bx/sc`) is present in the baseline build of the *unedited* file and
is therefore pre-existing, not introduced here.

**Hashes.**

| artefact | sha256 |
|---|---|
| `theorem.tex` **old** (CT-S1 original) | `74b6a6354403f9c9d057ef76b9d4406afc9c5b1b8aff68adf62c91fc9048d577` |
| `theorem.tex` **new** | `3d66d72fe1dfc5eba461ea1355ac10a1392457b9aaf78c82cfa9744daddb2695` |
| `theorem.pdf` CT-S1 original artefact | `efb8773df36d2762036caa23834136c4c513a389fe0e8135dcdc0976feb7d9b4` |
| `theorem.pdf` baseline rebuild, **unedited** tex, this toolchain | `49e58762c81c73e45add6fb6e1d79127587de80ed37b51b9d9c0d180e9b5369e` |
| `theorem.pdf` **new** | `dd1993a8cb8b7162b42bc53641441735bb6d7e997769960bb29f511913fe2ac3` |

> The CT-S1 PDF does **not** reproduce byte-for-byte on this MiKTeX install
> even with `SOURCE_DATE_EPOCH` pinned. Quoting `efb8773d…` as the “old” half
> of an old/new pair would invite a comparison that cannot hold. The honest
> comparison is against the baseline rebuild of the unedited file,
> `49e58762…`; both are reported and both are kept under `refs/`.

### Task 2 — §1 “Notation and standing conventions”

`section1.tex`, 13 660 B, nine subsections, drafted as paper prose. It compiles
standalone (`section1_standalone.tex`) to 4 pages with no undefined references.
It fixes, before first use:

1. **The recurrence and its normalisation** — `b`, `β_k`, `d`, `β_d`, `β_{d−1}`,
   PCF, `Q_n`, `B_n`, and the three renamed r-objects.
2. **Standing hypotheses** — (A1), (A2), (A3) **separately**, with (A2)
   restored and the sentence that (A2) is exactly what makes `Γ(1−λ_i)` finite
   and therefore what makes `K` defined at all.
3. **Asymptotic and analytic vocabulary** — `Γ`, `O`, `o`, `∼`, `(dn)!`, formal
   solution, Newton polygon, germ coefficient, amplitude, `c_±`, Stokes
   constant.
4. **The growth constants** — `s`, `K`, `ξ₀`, `ρ`, indicial exponent, with the
   sensitivity remark (`s` sees only `β_d`, `β_{d−1}`).
5. **Numerical vocabulary** — dps, Richardson level, PSLQ (“evidence for a
   relation and never a proof of one”), the `N/2`-vs-`N` criterion.
6. **The three objects** — `A`, `B`, `C`; trace-free normal form; normal
   potential; projective equivalence; **`B` and `C` projectively equivalent
   under `z ↦ 1/x`**.
7. **Katz invariants** — `r(c)` and the Katz multiset in van der Put–Saito’s
   own notation, with Table 2.1’s column order `(r(0), r(1), r(∞), r(t))`, the
   `D̃₅` and `D̃₆` rows, and the **necessary-condition qualification**.
8. **Monodromy and trace coordinates** — `B₁, B₂, B₃` as the monodromy
   matrices, and `x₁ = tr(B₂B₃)`, `x₂ = tr(B₁B₃)`, `x₃ = tr(B₁B₂)`.
9. **What is not fixed here**, and why.

**The r-collision, and a fourth object.** CT-S23 §4.4 (`S23-11`) found three
objects sharing the letter `r`. §1 renames them `q_n`, `q_∞`, `λ_1…λ_d`, with
**exactly one** footnote giving the correspondence to the deposited names — the
form `S24-08` requires — and states that the deposits are not altered. Drafting
§1 turned up a **fourth** object the audit did not list: van der Put–Saito’s
Katz invariant `r(c)`, whose Table 2.1 columns are literally `r(0) r(1) r(∞)
r(t)`. It is named in the footnote as unrelated (`S36-12`).

### Task 3 — the 171-item check

`scripts/check_171.py`. The 171 items are parsed mechanically from
`CT-S23-OUTSIDER-READ/outputs/coldread_main.txt` §2 into
`refs/ct-s23-task2-items.txt` (one item per line, count asserted). Every ruling
of `DEFINED IN SECTION 1` names an **anchor**: a literal string that must occur
in `section1.tex`. If it does not, the item is reported `ANCHOR MISSING` and
the script exits 1 — **a ruling of “defined” does not make it so.**

**Result.**

| | count |
|---|---|
| DEFINED IN SECTION 1 | **40** |
| DEFINED ELSEWHERE | **5** |
| **STILL UNDEFINED** | **126** |
| | **171** |

Plus, independently of the 171, **30/30** of the definitions the session task
names explicitly resolve to verified anchors.

**The 126 are the session’s output, not a failure to hide.** They fall into
four groups:

- **~65 are the `System C` monodromy/Stokes computation** (items 57–158): `A₀`,
  `A₁`, `A_∞`, `θ₀`, `θ₁`, `θ_∞`, `H_V`, `Ω`, `M₀`, `M₁`, `M_∞`, `S_π`,
  `S_{2π}`, `Φ`, `Λ`, `F`, character variety, Galois automorphism, and so on.
  These belong to the sections that carry that computation; §1 is not the place
  for them, and they are the largest block of drafting still owed.
- **~9 belong to the cut §9** (items 21, 26, 27, 159–167): `ζ*`, `S_{ζ*}`, the
  PSLQ basis, decoys, cost. §9 was cut by ruling (option iii), so these items
  are retired rather than owed.
- **~6 are genuine collisions §1 does not yet resolve**: `b(z)` vs `b(n)` (71),
  `R` as radius vs normal potential (144), `a, b` as control parameters vs the
  coefficient polynomial (136), `w` (84, 100), `L` (98, 132).
- **3 are defects in §1 itself**, surfaced by the check — see §3.

**Control (pre-registered in `PREREG.md` §3).** Item **054**, *“apparent
singularity”*, deliberately left undefined; required to be reported
`STILL UNDEFINED`; **reported `STILL UNDEFINED` — PASS**.

**Mutants.** `scripts/mutants_171.py`, **8/8 CAUGHT**, each with exit 1 *for
the stated reason* and no traceback. Per Amendment E the damage is drawn from
outside the check’s own anchor list: M1–M4 delete subsections or hypothesis
(A2) of §1, named by their prose headings.

---

## 2. Claims

`claims.jsonl`, 12 claims.

| id | label | claim, in brief |
|---|---|---|
| S36-01 | STRUCTURAL | Proposition U transcribed faithfully into `theorem.tex` after `prop:positive`, citing S26-01, not S1-02 |
| S36-02 | VERIFIED | edited `theorem.tex` compiles, 8 pages, no undefined references; the one warning is pre-existing |
| S36-03 | VERIFIED | old/new hashes, with the non-reproducing CT-S1 PDF reported as such |
| S36-04 | VERIFIED | §1 drafted, 9 subsections, compiles standalone to 4 pages |
| S36-05 | VERIFIED | 40 / 5 / 126 over the 171 items |
| S36-06 | VERIFIED | control item 054 reported STILL UNDEFINED; 30/30 task-required definitions present |
| S36-07 | VERIFIED | 8/8 mutant arms caught for the stated reason |
| S36-08 | VERIFIED | the check failed first time on **two of its own rulings** |
| S36-09 | VERIFIED | three arms initially MISSED, exposing two instrument defects |
| S36-10 | VERIFIED | three defects in §1 surfaced by the check |
| S36-11 | **CONJECTURED** | the new names `q_n`, `q_∞`, `λ_i` are the drafter’s choice, not ruled on |
| S36-12 | STRUCTURAL | a fourth r-object, van der Put–Saito’s `r(c)`, recorded |

`claims.jsonl` sha256
`ebe064be8fcc640ae79105969ee582d0c6051f14b0704dd18d42954b542db8ac`. The emitter
validates the exact bytes destined for disk **before** writing them, and all
12 cited `output_hash` digests resolve to a file on disk after the final run
(0 unresolved).

---

## 3. Defects found, and how

### 3.1 The check failed on its first complete run — on its own rulings

Items 024 (`germ coefficient`) and 035 (`projectively equivalent`) were ruled
`DEFINED IN SECTION 1`. Both were reported **ANCHOR MISSING** and the script
exited 1. Cause: the anchors were written as Python *raw* strings containing
`\n`, which in a raw string is a backslash and an `n` — two literal characters,
not a line break — so whitespace-flattening could never match the real text,
which does break across a line there.

Both terms **were** defined in §1. The rulings were wrong, not the prose. The
rulings were corrected; the check was not weakened. This is the mechanism the
task asked for working as intended.

### 3.2 Three mutant arms initially MISSED — two instrument defects

| arm | symptom | cause |
|---|---|---|
| M1, M3 | exit 1 but the **wrong reason** | an integrity assertion fingerprinted §1 by an exact subsection count of 9. Deleting a subsection tripped *that*, before the anchor stage. It would also have failed on any legitimate edit to §1. |
| M7 | `broke=True` | an undecodable input raised `UnicodeDecodeError` before integrity ran, so the check crashed instead of reporting a reader failure. |

Repairs: the fingerprint became a non-vacuity bound (`≥ 5` subsections), and
reads go through `read_or_fail()`, which reports an undecodable file **in the
same words as any other failure to see the content** — because a traceback is,
to a harness, indistinguishable from the script being broken outright. 8/8
after repair.

Neither defect was visible by reading the code. Both were found by requiring
the arms to fail *for the stated reason* and rejecting tracebacks.

### 3.3 Three defects in §1, surfaced by the check

- **Item 170, `indicial exponent`** — §1.4 *used* the term to describe `ρ` and
  never defined it. **Repaired**; item 170 is now `DEFINED IN SECTION 1`.
- **Item 171, `u = √z`** — named as the uniformiser; the coordinate change and
  branch are not given. **Left undefined**, and §1.9 says where it is fixed.
- **Item 014, `ζ = w^{1/d}`** — same, branch-sensitive, deferred by §1.9.

The last two are deliberate: they are local to one argument and fixing them in
§1 would state a convention twice, in two places, which is how they drifted
before. §1.9 exists to say so out loud.

---

## 4. What was NOT established

- **§1 does not absorb “most” of the 171.** It absorbs **40**, plus 5 already
  defined elsewhere. 126 remain. The task’s expectation that §1 would absorb
  most of them is not met, and the reason is structural, not a shortfall of
  effort: roughly 65 of the items are the `System C` monodromy and Stokes
  computation, whose vocabulary belongs to the sections carrying it, and ~9 are
  retired with the cut §9. The honest figure is the one reported.
- **No other section was drafted**, as instructed.
- **Proposition U is not re-proved here.** `S36-01` is STRUCTURAL: it claims
  faithful transcription, not a proof. The proof is PROVEN at `S26-01`.
- **The renaming is not ruled on.** `S24-08` requires a renaming and one
  footnote; it does not fix the letters. `q_n`, `q_∞`, `λ_i` are the drafter’s
  choice (`ρ` was avoided for the limit because `ρ` is already the Borel-plane
  exponent). `S36-11` is labelled CONJECTURED for exactly this reason.
- **`theorem.tex` still uses `\rinf` internally.** The renaming is a §1 prose
  convention; the transcribed theorem file was not re-lettered, because doing
  so would change a file whose content is otherwise verbatim from CT-S1. This
  is an inconsistency the operator should rule on.
- **No PREREG threshold on the STILL UNDEFINED count**, and none may be added
  later. `PREREG.md` §3 says so explicitly.

---

## 5. Open questions for the operator

1. **The three new names.** `q_n`, `q_∞`, `λ_1…λ_d` — approve, or substitute?
   Everything downstream keys off this and it is cheap to change now.
2. **`theorem.tex` vs §1.** Should the transcribed theorem file be re-lettered
   to match §1, or should §1 note that the theorem file retains the deposited
   letters? Currently neither is done.
3. **The fourth r-object.** `r(c)` is van der Put–Saito’s and cannot be
   renamed. §1’s footnote names it as unrelated. Is that sufficient, or should
   §1.7 carry a display contrasting all four?
4. **The 126.** Are they to be closed by drafting the remaining sections
   (~65 of them are `System C`), or does the operator want a second notation
   pass once those sections exist?
5. **`PREREG.md` for a drafting session.** Written here only because task 3 has
   a control, departing from the `S24-07` precedent. Confirm that is the right
   line.

---

## 6. Uncommitted files

All under `sessions/2026-09-17/CT-S36-DRAFT-NOTATION/`. Nothing outside it was
written.

| file | note |
|---|---|
| `theorem.tex` | copied from CT-S1-THEOREM, Proposition U inserted |
| `theorem.pdf` | 8 pages, rebuilt |
| `section1.tex` | **new** — §1, 13 660 B |
| `section1_standalone.tex`, `section1_standalone.pdf` | wrapper proving §1 compiles, 4 pages |
| `PREREG.md` | **new** |
| `REPORT.md` | this file |
| `claims.jsonl` | 12 claims |
| `scripts/check_171.py` | the 171-item check |
| `scripts/mutants_171.py` | 8 negative controls |
| `scripts/verify_artefacts.py` | 24 checks on `theorem.tex` and `section1.tex` |
| `scripts/emit_claims_s36.py` | claim emitter, validates bytes before writing |
| `refs/ct-s23-task2-items.txt` | the 171 items, extracted |
| `refs/theorem-CT-S1-original.pdf` | the original artefact |
| `refs/theorem-baseline-rebuild.pdf` | unedited tex, this toolchain |
| `outputs/build_baseline_{1,2}.log`, `outputs/build_propU_{1,2}.log`, `outputs/build_section1_{1,2}.log` | build evidence |
| `outputs/check_171.out.txt`, `outputs/mutants_171.out.txt`, `outputs/verify_artefacts.out.txt`, `outputs/emit_claims_s36.out.txt` | run evidence |

No earlier session’s files were modified. No network call was made. Nothing was
committed, deposited or uploaded.
