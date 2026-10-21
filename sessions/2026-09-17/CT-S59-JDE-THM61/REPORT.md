# REPORT — CT-S59-JDE-THM61

**Question.** Does Theorem 6.1 of *Self-Adjoint Structure of Polynomial
Continued Fraction Recurrences and its Arithmetic Consequences* misapply the
Poincaré–Perron theorem to an un-normalised PCF recurrence?

**Answer: no — and the paper says so itself, in the paragraph after the
theorem.** Separately, the premise that the paper is under review is false.

---

## 1. What was done

Two read-only checks, each identifying its artefacts by **hash**, never by
filename:

| Script | Artefact | Identity |
|---|---|---|
| `check_thm61.py` | as-submitted PDF | md5 `75ee5c4fcc3dc21668794d02daa23a93`, 389 607 B |
| | TeX source | sha256 `bb392b76…c7d69153`, 39 241 B |
| `check_log_status.py` | `submission_log.txt` | sha256 `70f814b9…29897433`, 450 188 B |

The PDF md5 is the one `submission_log.txt` §B Item 13 records as the deposited,
bit-identical, as-submitted build. Three copies on disk share it.

`check_thm61.py` exit **1** (findings), `check_log_status.py` exit **1**
(findings), **10/10 controls fired** across the two.

---

## 2. Theorem 6.1 — the answer, with its evidence

**Theorem 6.1 is "Poincaré–Perron, simplified form"**, resolved in the
*rendered* PDF rather than inferred from LaTeX counters. As printed:

> Let `y_{n+1} = a_n y_n + b_n y_{n-1}` be a second-order linear recurrence with
> **`a_n → a` and `b_n → b` as `n → ∞`**, where the characteristic equation
> `z² − az − b = 0` has roots `λ₁, λ₂` with `|λ₁| > |λ₂|`. Then every
> non-trivial solution either satisfies `y_{n+1}/y_n → λ₁` or `y_{n+1}/y_n → λ₂`.

The finite-limit hypothesis is **stated explicitly in the theorem**. The very
next paragraph then reads:

> For the Wallis recurrence `Q_{n+1} = b(n) Q_n + Q_{n−1}` with
> `b(n) = α_d n^d + ⋯`, the coefficients grow polynomially, so the
> Poincaré–Perron theorem **does not apply directly (it requires convergent
> coefficients)**. The appropriate generalization is the Perron–Kreuser theorem
> …, which gives `Q_{n+1}/Q_n ∼ b(n)` as `n → ∞`.

So the paper neither applies the theorem to the un-normalised recurrence nor
normalises to make it apply: it **declines**, and states the correct reason.
`thm:poincare-perron` is cross-referenced **0 times** anywhere in the source —
no proof invokes it. §6 ("Relation to Classical Asymptotic Theory") is a
delineation section whose purpose is to say what the results are *not*
consequences of.

The operator's conditional — "if Theorem 6.1 applies Poincaré–Perron directly
to an un-normalised PCF recurrence" — **does not fire**. This was the branch on
which telling an editor would have been warranted.

---

## 3. What *is* wrong: three citation-level defects

| # | Defect | Label |
|---|---|---|
| 1 | The **Perron–Kreuser** theorem is named, but **Kreuser has no bibliography entry**. 0 `\bibitem` keys match `/[Kk]reuser/`. | INSPECTED |
| 2 | The single key `Perron21` (Math. Ann. **84** (1921), 1–15) is cited for **both** Poincaré–Perron *and* Perron–Kreuser. Perron–Kreuser proper is Perron, **Acta Math. 34 (1911)** + **Kreuser 1914**. | INSPECTED |
| 3 | **Gautschi (1967) is not cited at all.** His Theorem 2.3(a), case `σ = d > τ = −d`, gives `Q_{n+1}/Q_n ∼ b(n)` directly — the clean route to the sentence currently sourced to `Perron21` + Elaydi Ch. 8. | INSPECTED |

All three are revision-stage fixes, exactly as the operator's instruction 2
anticipated. None is a wrong claim; all three are wrong or missing references.

**Deliberate, do not "fix":** the paper cites Birkhoff–Trjitzinsky as *Acta
Math.* **60 (1932)**, 1–89. That matches the scan's own imprint rather than the
commonly quoted 1933, and is recorded here so a future citation pass does not
"correct" it into error.

---

## 4. The premise is false — the paper is not under review

`submission_log.txt`, entry resolved by submission ID `JDEQ26-983`:

> **Verdict: REJECTED 2026-05-27 by Qiudong Wang, Handling Editor, Journal of
> Differential Equations** (initial screening before refereeing; no referee
> reports). … DISPOSITION: paper is free; joins the redirect queue.

Consequences for the three instructions in the brief:

1. **"Record it in your submission log"** — already recorded, twice: §A Item 13
   (the submission) and §B Item 13 (the Zenodo companion, concept DOI
   `10.5281/zenodo.20173746`, v1.0 `…20173747`). Nothing to add.
2. **"Don't email the editor about the reference"** — correct, and now moot:
   there is no editor relationship. The paper was rejected at initial screening
   without referees.
3. **"Check Theorem 6.1 before deciding that's all it is"** — done. It *is* all
   it is. And because the paper is free rather than under review, even a genuine
   misapplication would have been a pre-resubmission fix, not a disclosure.

### 4a. A defect in the log itself

The same §A entry is internally inconsistent: its `Status:` line still reads
`Submitted to Journal of Differential Equations (active review)` while its
`Verdict:` line records the rejection. A reader who stops at `Status` — which
is where a reader naturally stops — gets the wrong answer. This is the likeliest
origin of the premise in the brief.

**Not repaired here.** `submission_log.txt` is an operator-owned record outside
the session tree, and this session does not edit it. See §6.

---

## 5. What was NOT established

- The 1911/1914 attribution of Perron–Kreuser is carried over from a previous
  run's reading of Gautschi 1967 (p. 12, p. 58). It was **not re-verified in
  this session**; no Gautschi scan was opened here.
- Whether Elaydi, *An Introduction to Difference Equations*, 3rd ed., **Ch. 8**
  in fact states Perron–Kreuser as cited. The book was not consulted.
- Whether `Perron21` (Math. Ann. 84, 1921) is a defensible source for the
  Poincaré–Perron *half* of its double duty. Only the double duty itself is
  established.
- Any mathematical claim of the paper. Nothing was re-derived.
- The remaining 25-odd references were not audited; only those named above.

## 5a. Two invented defects, caught before the report

The first run of `check_thm61.py` reported 4 findings; **2 were my reader's**:

- `pdftotext` emits this build's `ffi`/`fi` ligatures as a **space**
  ("simpli ed form", "satis es"), so the literal search for the paper's stated
  reason — "it requires convergent coefficients" — returned **absent**, which is
  verbally identical to the paper having omitted it. Repaired by reading the
  source as well, and matching the render with a ligature-tolerant pattern
  carrying a control that requires it to **recover a phrase the literal search
  provably misses**, so the tolerance cannot degrade into matching everything.
- the Birkhoff–Trjitzinsky bibitem regex used `[^\\]*?` and could not cross
  `\emph{Acta Math.}`, reporting `NOT FOUND` for an entry that is present.

Had either reached the report, it would have been an accusation against a
correct paragraph. Detail in `PREREG.md`.

---

## 6. Open questions for the operator

1. **Repair the `Status:` line of §A Item 13?** It contradicts its own `Verdict:`
   line and is the most likely source of the "under review" premise. The same
   pattern may affect other closed entries — Item 34 (JMP) carries a
   `REJECTED 2026-07-06` verdict; its `Status:` line was not checked. **A sweep
   of every §A entry for verdict/status disagreement is a small, well-defined
   job and is not yet done.**
2. **Redirect venue for this paper.** It is free, has a Zenodo priority anchor
   (concept `10.5281/zenodo.20173746`), and has never been refereed — the
   rejection carries no scientific signal at all.
3. **Fix the three citations before resubmission**, plus add Gautschi. Item 3 in
   particular improves the paper: it replaces a two-step sourcing
   (`Perron21` + Elaydi Ch. 8) with one theorem that gives the result directly.
4. **Does the Channel Theory v1.8 list need anything from this?** On the evidence
   here, no: v1.7 already routes the theorem through Gautschi. The Perron–Kreuser
   item is a JDE-paper correction, not a Channel Theory one — as you concluded
   independently.

---

## 7. Claims

10 claims, `S59-01` … `S59-10`, all labelled **INSPECTED**, in `claims.jsonl`
(sha256 `adaa98a4a48d363adfe65ecb251d04c2a9bac627da3146bba4e6bc8c22badee6`).
The emitter validates its in-memory buffer before writing, re-hashes every cited
output from disk, requires a supporting string to be present in the cited output
for each claim, appends only, and refuses on re-run (verified: exit 2, artefact
untouched).

No claim is labelled PROVEN, VERIFIED, or STRUCTURAL. Every one is a statement
about what a file says.

---

## 8. Uncommitted files

All under `sessions/2026-09-17/CT-S59-JDE-THM61/`, none committed:

```
PREREG.md
REPORT.md
claims.jsonl                      10 claims, sha256 adaa98a4…badee6
scripts/check_thm61.py            run 1st
scripts/check_log_status.py       run 2nd
scripts/emit_claims_s59.py        run 3rd; re-run refuses
outputs/check_thm61.out.txt
outputs/check_log_status.out.txt
```

**Nothing was sent, deposited, committed, or edited outside this folder.** The
paper source, the submitted PDF, and `submission_log.txt` were read only.
