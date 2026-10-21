# REPORT — `CT-S26-CTV17-DRAFT`

**Session:** `sessions/2026-09-17/CT-S26-CTV17-DRAFT/`
**Task:** draft the Channel Theory **v1.7 version notice** (concept DOI
`10.5281/zenodo.19941678`), carrying five items plus two required carry-overs, in
a stated structure. **Draft only — no deposit, no metadata edit.**

**Nothing was committed, pushed, tagged, deposited, uploaded or sent.** All files
listed in §8 are uncommitted.

---

## 1. What was done

1. **Source-gathering first, drafting second.** Every citation, DOI, coefficient
   and literature statement in the notice was read from a file in this
   repository before it was written. Nothing was written from the prompt or from
   memory. Where a source does not exist here, the notice says so (§3 below).
2. **`NOTICE-v1.7.md` was drafted** in the commissioned structure: a
   current-state section (§0) that stands alone, then the erratum stack (§1),
   then the five items (§2–§6), then open problems, what the notice does not
   claim, and the table of held sources.
3. **`scripts/verify_notice.py` was written to attack the draft**, not to
   confirm it. It runs 14 checks, then runs **each check a second time against a
   mutant of the notice in which exactly the thing that check guards has been
   removed**. A check that still passes on its own mutant is reported `BROKEN`
   and fails the run. Final: **14/14 checks pass, 14/14 controls fire, 0 broken,
   `VERDICT: OK`**.
4. **Eight claims emitted** as `S26C-01` … `S26C-08`, hashed from disk after the
   artefact was final.
5. **The blocker was then closed by fetching the records** (§3): v1.5 and v1.6
   from Zenodo, v1.3 and v1.4 from DataCite once `zenodo.org` began returning
   HTTP 504. The deposited descriptions are held in `refs/` with bytes and
   sha256.
6. **The notice was revised to revision 2**, repairing five stale statements the
   deposited text exposed (§3.1) and filling the erratum stack.
7. **`scripts/verify_notice_rev2.py`** runs **21 checks** with their mutants, and
   adds the control class mutant testing cannot supply: **reader integrity**,
   with three defective readers as its controls (§4.4). Final: **21/21 checks,
   21/21 mutant controls, 0 broken, 3/3 reader controls, `VERDICT: OK`** — to a
   **new** output path, leaving the rev-1 output and its eight claims intact.
8. **Nine further claims appended** as `S26C-09` … `S26C-17`.
9. **Revision 3: the five rulings of 2026-09-19 applied** (§7). Three changed
   the notice, two were already satisfied and are now stated so they can be
   checked, one narrowed a claim in another session's record, and the watch item
   added a closing block to §2.
10. **`scripts/verify_notice_rev3.py`** imports revision 2 unchanged and adds six
    checks, one of which reads the corpus rather than the notice and therefore
    carries a control of its own kind. Final: **26/26 checks, 26/26 controls, 0
    broken, 3/3 reader controls, `VERDICT (rev3): OK`** — again to a **new**
    output path.
11. **Five further claims appended** as `S26C-18` … `S26C-22`, and two P0
    amendments written up as PROPOSED (§7.3).

**No PREREG.md.** No computation was run in this session — the work is reading,
drafting and checking. Its absence is stated here rather than back-filled as a
vacuous pre-registration (precedent: `CT-S3A-ZETA-AUDIT`,
`CT-S24-PAPER-OUTLINE`).

### 1.1 The five commissioned items, and where each landed

| # | Item | Section | Rests on |
|---|---|---|---|
| 1 | Attribution; retire the conjecture label | §2 | Gautschi Thm 2.3(a) p. 35 / Thm 1.1 p. 31; DLMF §3.6(ii); `S1-03` |
| 2 | The exponent, and the priority position | §3 | `S1-04`, `S2-01`–`S2-04`, DLMF (2.9.5)/(2.9.6)/(2.9.14), `S21-76` |
| 3 | `K` and `r_∞` | §4 | `S3B-04`–`S3B-06`, `S21-31`–`S21-33`, `S24-12` |
| 4 | The vacuity explanation | §5 | `S1-03`, `S1-04` (structural, one line) |
| 5 | The Borel material | §6 | `S3A-*`, `S22-21`, `S22-22` |

Both **required carry-overs** arrived and are each guarded by a check that can
fail (`S26C-05`): the **PSLQ basis is printed in full** — three separate mutants
(ellipsis inserted, cost rule deleted, `Γ(1/6)` reinstated) are all rejected —
and the **naming prohibition** is stated as a prohibition, with both roles and
both points.

---

## 2. Claims

| id | label | claim |
|---|---|---|
| `S26C-01` | **INSPECTED** | The notice is drafted in the commissioned structure; 14/14 checks pass with 14/14 can-fail controls firing |
| `S26C-02` | **INSPECTED** | Every Zenodo DOI printed is traced to the held v1.3 release description, and the checker rejects any DOI that is not |
| `S26C-03` | **INSPECTED** | The erratum stack is incomplete **by declaration**: v1.4–v1.6 are absent from this repository and no text was invented for them |
| `S26C-04` | **STRUCTURAL** | The vacuity explanation is a one-line consequence of two proved statements and replaces an empirical sweep |
| `S26C-05` | **INSPECTED** | Both TRANSIT MANIFEST carry-overs arrived, each guarded by a check that can fail |
| `S26C-06` | **INSPECTED** | `op:cc-median-resurgence-execute` restated with its series named and its Painlevé target marked stale |
| `S26C-07` | **INSPECTED** | A checker defect was caught that reported a content omission where none existed |
| `S26C-08` | **INSPECTED** | No label is upgraded in prose; nine load-bearing labels are checked against the corpus, not asserted |
| `S26C-09` | **INSPECTED** | The version map v1.1–v1.6 is read from live records, with DOIs and dates; six `HasVersion` relations, no v1.0 among them |
| `S26C-10` | **INSPECTED** | Concept DOI read from the `conceptdoi` field; the concept record is at version `1.6`, so **v1.7 is correct** |
| `S26C-11` | **INSPECTED** | `op:xi0-singularity-type` and `rem:d3-vacuous` are real (v1.6); `op:xi0-d3-direct` is **withdrawn as vacuous**, not subsumed |
| `S26C-12` | **INSPECTED** | v1.6's vacuity evidence is a sweep (`6.85e-18` vs `1.26e-1`), quoted not recomputed; §5 derives the same for `ξ₀` **and** `ρ` |
| `S26C-13` | **INSPECTED** | `P-III(D₆)` was corrected at v1.4 to P_V on Sakai `D₅^(1)` and marked **conjectural** at v1.5 |
| `S26C-14` | **INSPECTED** | The EBR grounding is superseded **in scope** — positive `b`, physical object, `d = 2–5` Lean layer — and is not withdrawn |
| `S26C-15` | **INSPECTED** | Both PDFs returned HTTP 504; **no §9 falsifier text was read and none is quoted** |
| `S26C-16` | **INSPECTED** | Revision 2 passes **21/21** checks with **21/21** mutant controls and 0 broken |
| `S26C-17` | **STRUCTURAL** | Reader integrity is asserted before any absence is evaluated, and three defective readers are all caught — the class mutant testing cannot supply |
| `S26C-18` | **INSPECTED** | Revision 3 implements the five rulings and the watch item, and passes **26/26** checks with **26/26** controls, 0 broken, 3/3 reader controls |
| `S26C-19` | **STRUCTURAL** | The `S_{ζ*}` negative has its own tag `op:cc-szeta-closed-form`, kept distinct from `op:cc-stokes-closed-form`, with the non-implication stated **both ways** |
| `S26C-20` | **INSPECTED** | `S3A-06` narrowed to the artefact inspected: 4 occurrences in each of four deposited descriptions, 0 in the v1.3.1 LaTeX; label unchanged, text retained |
| `S26C-21` | **INSPECTED** | The obligation-tag check was **loosened** to admit a tag declared new at v1.7, disclosed as such, with 3 mutants where it had 1 |
| `S26C-22` | **INSPECTED** | Two further P0 amendments are **PROPOSED**: C (a check must verify it read its file) and D (deposited text is authoritative) |

**`S26C-03` is superseded by `S26C-09`…`S26C-15`**, not withdrawn: it was
accurate when written (§3.2).

---

## 3. The blocker, and how it was closed

**As drafted (rev 1), the notice was blocked**: Channel Theory v1.4, v1.5 and
v1.6 are not in this repository. The newest in-repo source is **v1.3.1**; the
v1.3.1 claims record points at `pcf-research/channel/…`, which does not exist on
this machine (`CT-S0-INVENTORY/REPORT.md` §2, independently
`CT-S3A-ZETA-AUDIT/REPORT.md` §1 and `CT-S1-THEOREM/REPORT.md` §3.5).

**On the operator's instruction the records themselves were fetched.** The
deposited **descriptions** — the operator's stated primary source — are now held
in `refs/` with bytes and sha256 (`REFS-MANIFEST.md`), and **every blocked item
resolved**:

| blocked item (rev 1) | status at rev 2 |
|---|---|
| erratum-stack rows for v1.4–v1.6 | **filled** from the deposited text, with DOI and publication date |
| wording and label of `rem:d3-vacuous` | **read**: added at v1.6, evidence is a coefficient sweep, numbers quoted (`S26C-12`) |
| is **v1.7** the right number? | **yes** — the concept record currently resolves to version `1.6` (`S26C-10`) |
| does `op:xi0-singularity-type` exist? | **yes** — created at v1.6; the rev-1 "zero occurrences" finding was true *of the repository* only (`S26C-11`) |
| the v1.5 halving notice | **read**: v1.5's "Second ground" records the halving *and* the ~1.7 % unexplained residual, independently of CT-S3A's reading of the code (`S26C-13`) |

**What the fetch did not resolve.** The v1.5 and v1.6 **PDFs** returned HTTP 504
on both file endpoints, retried. **§9 of each — the open-problems section
carrying v1.6's new falsifier statements and their numeric thresholds — has not
been read**, so the notice names the falsifier's existence and declines to
restate it (`S26C-15`). That is now the only outstanding source gap, and it does
not block: nothing in the notice quotes a falsifier.

### 3.1 Five things the deposited text changed in the draft

Read before the fetch, the draft was right in substance and **stale in five
places**. All five are repaired at revision 2:

1. **`op:xi0-d3-direct` was "SUBSUMED".** It is **withdrawn as vacuous at v1.6** —
   not answered, not subsumed by the general-`d` proof.
2. **`op:xi0-singularity-type` was "no tag exists".** It exists, and it is the
   live successor problem.
3. **`op:xi0-degree-d` was "CLOSED".** v1.6 had already restated it as having no
   per-degree computation left but an **analytic residual**; §2 closes the
   algebraic part only.
4. **The Painlevé target was "stale, see VQ-N1".** The record corrected it at
   **v1.4** (to P_V on Sakai `D₅^(1)`) and marked it **conjectural at v1.5**. The
   repository's `P-III(D₆)` material is the stale copy, not the record.
5. **The EBR supersession was unscoped.** EBR proves the identity only for
   positive `b`, only for the physical object, with a Lean layer at `d = 2–5`.
   Saying what it requires is what makes "no positivity hypothesis" a
   *supersession of the grounding* rather than a displacement of the result.

A sixth item is an addition rather than a repair: **`op:cc-stokes-closed-form`**
(created at v1.5 from the demoted Theorem 3.7(iii)) is the nearest published home
for the `S_{ζ*}` closed-form question, and is now in the open-problem table.

### 3.2 A correction to a claim of this session's own

`S26C-03` recorded the erratum stack as *incomplete by declaration*. That was
accurate when written and is **superseded, not withdrawn**, by `S26C-09`…`S26C-15`.
Likewise `S26C-01`, `S26C-05` and `S26C-08` cite the **rev-1** notice hash
`49559520…`; the notice on disk is now `9d93aeb1…`. **The rev-1 output
`outputs/verify_notice.out.txt` was not re-run and not overwritten**, so those
hashes still resolve to the bytes they were taken from.

---

## 4. Findings worth keeping

### 4.1 An absence report cannot distinguish "missing" from "unreadable" (`S26C-07`)

The checker read the notice in **binary** and matched fenced blocks with
`` ```\n(.*?)``` ``. The file has **CRLF** line endings, so the pattern matched
nothing and the PSLQ check reported

> `no fenced block containing the basis was found`

— which is **verbally identical to what it would report if the basis really had
been omitted**, i.e. exactly the failure the TRANSIT MANIFEST exists to prevent.
It was caught only because an independent second read of the same function in
*text* mode returned the block and passed: two reads of one file disagreed.

**The mutant controls do not catch this.** A broken reader rejects the mutant
too — for the same wrong reason — so the control fires and the check still looks
healthy. The general form is worth stating: *a check reporting **absence** cannot
distinguish "the content is missing" from "my reader could not see it", so an
absence report must be confirmed by a second, differently-implemented read before
it is believed.* Repair: normalise CRLF→LF in one place, immediately after
decoding.

### 4.2 One check was made stricter after seeing a result — recorded as such

`check_pslq_basis_in_full` originally required the literal `≤ 40` in the basis
block. The notice writes the cost rule as
`cost = n_nonzero · log10(max|coeff|) ≤ 0.40 · D_trust = 40`, in which that
substring does not occur, so the check failed on correct text. The requirement
was **replaced by the exact string `0.40 · D_trust = 40`**, which is *stricter*,
not looser — it pins the cost rule rather than a bare number. In the same edit,
**two further mutants were added** for this check (delete the cost line;
reinstate `Γ(1/6)` in the vector), so it now carries three independent can-fail
controls rather than one. Recorded here because a check edited after seeing its
own result is the standard route to a check that can no longer fail.

### 4.3 The notice deliberately asserts no Painlevé label for `V_quad`

The v1.3 statement of `op:cc-median-resurgence-execute` claims that executing it
*would conditionally close the `V_quad → P-III(D₆)` correspondence*. That premise
is **superseded**: `V_quad` was reclassified in
`sessions/2026-05-29/T1-SYNTH-VQ-N1-VQUAD-RECLASSIFICATION-APPLY`, with the
disposition in
`sessions/2026-05-02/VQUAD-PIII-NORMALIZATION-MAP/SUPERSEDED_BY_VQ-N1.json`. The
restatement records the staleness and names no replacement label, because none
was read in this session.

### 4.4 The reader-control class, implemented (`S26C-17`)

The operator's generalisation of §4.1 — **a check that reads a file must also
verify that it read it** — is implemented in `scripts/verify_notice_rev2.py`:

* **SECTION 0** asserts known-**present** sentinels before any check evaluates a
  known-absent feature: the title line, at least four `` ```\n `` markers (the
  exact feature CRLF destroyed), four non-ASCII characters, and no `CR`.
* **SECTION 3** is the control *for* SECTION 0, and it mutates the **input path**
  rather than the text: the file is re-read through three deliberately defective
  readers — binary without CRLF normalisation (the rev-1 defect, reproduced),
  `latin-1`, and silently truncated at 2 KB. **All three are caught, 3 of 3.**

This is the one control class mutant testing structurally cannot supply, because
a broken reader rejects the mutant too, for the same wrong reason.

### 4.5 A second post-hoc check edit, disclosed

`check_repo_absence_correction` first required the literal `true of the
repository`; the notice writes `true **of the repository**` inside a `> `
blockquote, so the phrase is broken by both bold markers and a `\n> ` line wrap.
The check now **collapses `\n>` and whitespace before matching** and uses
`true\W{0,4}of the repository`. That is a loosening — of *matching*, not of
*requirement*: the same three things are still required, and **two further
mutants were added in the same edit** (delete the scope correction; delete the
general lesson), so the check carries three independent can-fail controls. Both
survived. Recorded here rather than left implicit, per the standing rule that a
loosening must be declared as one.

---

---

## 5. What was NOT established

* **No new mathematics.** Every mathematical statement in the notice is carried
  by an existing claim id. This session proved nothing and computed nothing.
* **Nothing numerical was recomputed.** No `K` run, no PSLQ run, no `ζ*` run.
  The values quoted are read from existing hashed outputs. **v1.6's sweep numbers
  (`6.85 × 10⁻¹⁸`, `1.26 × 10⁻¹`) are quoted from the deposited text, not
  reproduced** (`S26C-12`).
* **The v1.5 and v1.6 PDFs were not obtained** (HTTP 504). **No §9 falsifier text
  has been read**, and none is quoted. The expected file sizes and md5s in
  `REFS-MANIFEST.md` are read from the records' `files[]` entries and are **not
  hashes of files held**.
* **The v1.3 and v1.4 descriptions may be partial**: DataCite returns a single
  description where Zenodo carries the full HTML. The v1.4 notice is in any case
  retained verbatim inside the v1.6 description, and that is the copy used.
* **No v1.0 version DOI was found.** DataCite lists exactly six `HasVersion`
  identifiers for the concept DOI and none is v1.0. That is reported as read and
  **not explained**; the rev-2 stack therefore starts at v1.1.
* **Whether `S_{ζ*}` passes v1.6's vacuity pre-check is not settled.** §5 proves
  `ξ₀` and `ρ` do not move under lower-order coefficients; `S_{ζ*}` is a
  different object and nothing here decides it either way.
* **The priority of `s` is still unsettled**, because Wong & Li II remains
  NOT OBTAINED — now by ruling rather than by circumstance, and the notice is
  explicitly not gated on it (§6 Q5).
* **`op:xi0-degree-d` is not closed.** §2 closes its algebraic part only; the
  analytic residual, `op:xi0-singularity-type`, is untouched and is stated as
  open inside §2 itself.
* **Whether the `S_{ζ*}` closed-form question bears on `op:cc-stokes-closed-form`
  is not decided.** Ruling 8 separates the two tags and states the
  non-implication both ways; it does not claim they are unrelated, and no result
  here bears on the identification question.
* **No closed form for `r_∞` or for `S_{ζ*}`.** The `S_{ζ*}` result excludes one
  explicitly printed space and nothing more.
* **No deposit, no metadata edit, no DataCite change, no write of any kind to any
  record.** The API traffic this session was **read-only**: `GET` on
  `zenodo.org/api/records/…` and `api.datacite.org/dois/…`.
* **Nothing is machine-checked.** Seven Lean `sorry`s stand.

---

## 6. Open questions for the operator

**Six were posed at revision 1. The fetch collapsed three of them.** They are
kept verbatim, with the answer under each, because a question that was live is
part of the record.

1. **"Supply v1.4, v1.5 and v1.6 (or confirm they are unavailable). Three things
   depend on them: the erratum-stack rows, the wording and label of
   `rem:d3-vacuous`, and whether v1.7 is the correct next version number. This is
   the only item blocking deposit."**
   → **CLOSED.** The deposited descriptions are held in `refs/`; all three
   dependents are resolved (§3). The PDFs are still unobtained, which leaves the
   §9 falsifier text unread but blocks nothing.
2. **"Assign a tag for the singularity-type problem. `op:xi0-singularity-type`
   does not exist in this repository. The notice states the problem without a
   tag; it must not invent one."**
   → **CLOSED, and the premise was wrong.** The tag exists; v1.6 created it. The
   notice now cites it and a check enforces that **every** `op:`/`rem:` tag it
   names occurs in a held deposited text.
3. **"What is `V_quad`'s current Painlevé classification after VQ-N1? The notice
   deliberately names none. If v1.7 should carry the current label, it must be
   supplied from a held source."**
   → **CLOSED by the record, not by VQ-N1.** v1.4 corrected it to the Painlevé V
   transcendent on Sakai `D₅^(1)` (`W(A₃^(1))`, `δ = −1/2 ≠ 0`); v1.5 marked that
   identification **conjectural**. The notice now names it *as conjectural* and
   flags the repository's `P-III(D₆)` material as the stale copy.
4. **"Should the notice point at the paper? The paper (`CT-S24-PAPER-OUTLINE`,
   revision 6) and this notice share §2–§5 material by argument. The outline's §9
   was cut on the ruling that the Stokes-constant negative belongs here. The
   notice currently makes no forward reference to an undeposited paper, which is
   the safe default; say if a pointer is wanted."**
   → **RULED 2026-09-19: no.** The paper does not exist — no draft, no DOI, no
   venue — and a forward reference to an unwritten document is the class of
   promise this corpus has spent the run removing. A pointer may be added in a
   later version once it has an identifier. Applied at §8 of the notice and
   checked by `R4`, which also rejects the usual forward-reference phrasings.
5. **"Wong & Li II — purchase, interlibrary request, or leave NOT OBTAINED
   permanently? It is the only route that could settle priority for `s`, and the
   notice's priority paragraph is written to survive either answer."**
   → **RULED 2026-09-19: leave NOT OBTAINED.** `s` is derived independently, the
   `r_∞` framing rests on Wong & Zhao §3 which *is* held, and only a closed form
   for `K` could be affected. An unhurried free ILL may be attempted; **v1.7 is
   not gated on it**. Applied at §3.1 and checked by `R5`, which also forbids
   softening the priority position in the meantime.
6. **"Is the `K`-SCAN / Proposition 3.3.B material quoted correctly? It is taken
   from the held v1.3 release description. If v1.5/v1.6 restated it, the quote may
   be stale."**
   → **CLOSED.** The v1.6 description retains the "Universality findings"
   paragraph **unedited**, including Proposition 3.3.B (QL01/QL02 share `ξ₀ = 2`
   and `ρ = −5/2`, split at `a₂`) and Remark 3.3.C (the K-SCAN QL15 coincidence).
   v1.6 supersedes exactly two sentences of that paragraph, both about the `d = 3`
   deferral, and **names them explicitly**. The quote is current.

### 6.1 Three new questions the fetch raised

**All three were ruled on 2026-09-19. The answers are recorded under each; the
questions are kept verbatim.**

7. **Should v1.7 restate v1.6's falsifiers, or only point at them?** Their text is
   in §9 of a PDF that will not download. The draft points and does not restate.
   If v1.7 must carry them inline, the PDF has to be obtained first — **no
   falsifier may be paraphrased from memory**.
   → **RULED: point, do not restate.** The PDFs 504 and unread text must not be
   paraphrased. The notice now cites **§9 of version `10.5281/zenodo.22782807`**
   by version DOI and section, and says why pointing is accurate where
   paraphrase would not be. Revisit if the PDFs become available before deposit.
   Checked by `R7`, which additionally **rejects any numeric value asserted for
   the unread falsifier** — the check can now catch the defect it names, not
   merely confirm a disclaimer.
8. **Does the `S_{ζ*}` closed-form question live inside `op:cc-stokes-closed-form`?**
   That tag is posed about the CC-ratio ↔ Riemann–Hilbert *match*. The §6.4
   negative is about a multiplicative closed form for `C`. They may be the same
   problem or adjacent ones; the record does not say, and the notice does not
   decide.
   → **RULED: probably not, and the notice says why rather than assuming.** The
   5B negative is filed under a **new tag `op:cc-szeta-closed-form`**, declared
   new at v1.7. §6.4 now states how the two relate **without merging them**, in
   both directions: a closed form for `C` would bear on the identification, and
   the identification would supply a candidate for `C`, but neither implies the
   other, and **the negative must not be cited as evidence about the other tag**.
   This is the one-name-two-objects trap of §6.0 raised from constants to
   problems (`S26C-19`).
9. **`Proposition 3.3.A` is in the deposited text but not in the v1.3.1 source.**
   `S3A-06` reported no such label in the LaTeX. The deposited description names
   "Proposition 3.3.A" and "Proposition 3.3.A′" in prose. Given v1.6 defect (4) —
   every cross-reference in v1.0–v1.5 rendered as "Theorem N" regardless of class
   — **the label set and the rendered text disagree by construction**, and
   `S3A-06` should be narrowed to the LaTeX label set rather than read as a claim
   about the paper.
   → **RULED: yes, narrow it.** Done by `scripts/amend_s3a06.py` (`S26C-20`).
   A narrowing, not a retraction: the label stays `INSPECTED`, the superseded
   text is retained verbatim, and the existing `CT-R1-AUDIT/R2` trail is kept.

---

## 7. Revision 3 - the operator's rulings applied

Five rulings and one watch item were received on 2026-09-19 and are all
implemented. **Two required no change to the notice and were confirmed by
inspection; three changed it; one changed a claim in another session's record.**

| ruling | disposition | where | control |
|---|---|---|---|
| 4 — no pointer at the unwritten paper | **already true**; the undertaking is now explicit in §8 so it can be checked | notice §8 | `R4`, 2 mutants |
| 5 — leave Wong & Li II NOT OBTAINED | already stated; **added that v1.7 is not gated on it** and that the priority position must not be softened | notice §3.1 | `R5`, 2 mutants |
| 7 — point at the falsifiers, do not restate | already declined to restate; **added the version-DOI-plus-section pointer** and the reason | notice §6.3 | `R7`, 3 mutants |
| 8 — own tag for the `S_{ζ*}` negative | **new tag `op:cc-szeta-closed-form`**, declared new, with the non-implication both ways | notice §0, §1, §6.4, §7 | `R8`, 3 mutants |
| 9 — narrow `S3A-06` | amended in place, preserving the superseded text | `CT-S3A-ZETA-AUDIT/claims.jsonl` | `R9` + a **corpus** control |
| watch — `op:xi0-degree-d` not closed | **new closing block in §2 itself** naming the open analytic residual | notice §2, §7 | `W`, 3 mutants |

### 7.1 Two things worth recording about the controls

**A check that reads a different artefact cannot be controlled by mutating this
one.** `R9` reads `CT-S3A-ZETA-AUDIT/claims.jsonl`, not the notice. The revision-2
harness supplies can-fail controls by mutating the **notice text**, and such a
mutant is invisible to `R9` — the first attempt duly reported `[BROKEN] mutant 1
ACCEPTED`. A mutant the check cannot see is not a control. `R9` was therefore
taken **out** of that harness and given a control of its own kind: a copy of the
claims record with the narrowing stripped, which it must reject. It does.

**`R7` was strengthened when it turned out it could only confirm a disclaimer.**
Its first form checked that the notice *says* it does not restate the falsifier.
That is a check on a sentence, not on the defect: a notice could carry the
disclaimer and paraphrase the threshold two lines later. `R7` now also rejects
any numeric value asserted for the unread v1.6 falsifier, and its third mutant
inserts exactly such a value. This was a **strengthening**, not a loosening, and
is recorded here for symmetry with §4.2 and §4.5.

### 7.2 The one loosening, disclosed (`S26C-21`)

The revision-2 check *every `op:`/`rem:` tag exists in the deposited record*
rejects any tag absent from the held descriptions. That was right while the
notice only referred to existing problems. Ruling 8 requires v1.7 to **create**
a tag — exactly as v1.6 created `op:xi0-singularity-type` — so the check would
have failed a correct notice, and it did.

It was replaced, not deleted. A tag now passes if it is in the deposited record
**or** the notice declares it *new at v1.7*; anything else still fails. Per the
standing rule the loosening arrives with extra can-fail controls **in the same
edit**: three mutants where revision 2 had one — an existing tag renamed, a tag
invented outright without declaration, and the removal of the declaration that
legitimises the new tag. All three fire.

Revision 2's script and its output file are **untouched**; revision 3 imports
revision 2 rather than reimplementing it, so all 21 revision-2 checks, their
mutants and the three reader controls run unchanged, and writes to a **new**
output path.

### 7.3 The standing rule the operator drew from the fetch

> For anything you have deposited, the **deposited text is authoritative** and
> the working tree may be behind it.

This is now written up as **Amendment D** in this session's `P0-AMENDMENT.md`,
alongside **Amendment C** (a check that reads a file must verify it read it),
with the evidence for each and a table of why neither is covered by an existing
P0 line. Both are **PROPOSED** and operator-gated; neither is in force. They are
lettered to follow Amendments A and B, still pending from `CT-S22-STOKES`.

---

## 8. Uncommitted files

All new, all under `sessions/2026-09-17/CT-S26-CTV17-DRAFT/`.

| file | sha256 (first 8) | note |
|---|---|---|
| `NOTICE-v1.7.md` | `75cd3476` | **the deliverable**, revision 3 (rev 2 was `9d93aeb1`, rev 1 `49559520`) |
| `P0-AMENDMENT.md` | `02d49838` | **new** — Amendments **C** and **D**, both PROPOSED |
| `REPORT.md` | — | this file |
| `REFS-MANIFEST.md` | — | bytes + sha256 of every fetched record, the version map, and what was NOT obtained |
| `claims.jsonl` | — | **22 claims**, `S26C-01`…`S26C-22` |
| `scripts/verify_notice.py` | — | rev 1: 14 checks, each with its own can-fail mutant |
| `scripts/verify_notice_rev2.py` | — | rev 2: 21 checks + mutants, **plus reader integrity and three reader controls**. **Untouched at rev 3.** |
| `scripts/verify_notice_rev3.py` | — | **new** — imports rev 2 unchanged, replaces the tag check (§7.2), adds `R4`, `R5`, `R7`, `R8`, `W` and the corpus check `R9` |
| `scripts/amend_s3a06.py` | — | **new** — narrows `S3A-06`; verifies presence in the deposited text before asserting it, backs up the file, reads back |
| `scripts/emit_claims.py` | — | rev-1 emitter; refuses to overwrite |
| `scripts/emit_claims_rev2.py` | — | append-only; asserts the rev-2 verdict, its counts, and that the output carries the **current** notice hash |
| `scripts/emit_claims_rev3.py` | — | **new** — same discipline at rev 3; asserts 26/26 and the current notice hash |
| `scripts/read_zenodo.py` | — | dual-shape (legacy/RDM) record reader with assertions |
| `scripts/extract_description.py` | — | Zenodo-shape description → text |
| `scripts/extract_datacite_description.py` | — | DataCite fallback extractor |
| `outputs/verify_notice.out.txt` | `8018ca33` | rev 1: `VERDICT: OK`, 14/14, 14/14, 0 broken — **cited by `S26C-01`…`S26C-08`; not re-run, not overwritten** |
| `outputs/verify_notice_rev2.out.txt` | `7fc55e7f` | rev 2: `VERDICT: OK`, 21/21 checks, 21/21 mutant controls, 0 broken, 3/3 reader controls — **cited by `S26C-16`/`S26C-17`; not overwritten** |
| `outputs/verify_notice_rev3.out.txt` | `9280ee69` | **new** — rev 3: `VERDICT: OK`, **26/26 checks, 26/26 controls, 0 broken, 3/3 reader controls**, plus the `R9` corpus control |
| `outputs/amend_s3a06.out.txt` | `c12c98a3` | **new** — the `S3A-06` narrowing, 9/9 checks |
| `outputs/CT-S3A-ZETA-AUDIT.claims.jsonl.pre-s26c-amend` | `3aa6d536` | **new** — pre-amendment copy of the file changed outside this folder |
| `refs/` (10 files) | see `REFS-MANIFEST.md` | v1.3–v1.6 records and descriptions; **no PDF**, both 504 |

**One file outside this folder was modified**, under operator ruling 9:
`sessions/2026-09-17/CT-S3A-ZETA-AUDIT/claims.jsonl` (sha256 `3aa6d536` →
`7c16e9a6`). A single claim was **narrowed in place** using the amendment
mechanism that session's record already carries from `CT-R1-AUDIT/R2`: the
superseded text is preserved verbatim in `claim_before_s26c`, the amending
session is named in `amended_in`, the label does not move, and a pre-amendment
copy of the whole file is held in `outputs/`. No other claim in that file
changed. It is uncommitted, like everything else here.

**Artefact hygiene.** A claim's hash is taken **after** the artefact is final, and
re-running a checker to a path a claim already cites invalidates every hash
pointing at it. Revisions 2 and 3 therefore each wrote a **new** output path and
**appended** new claims; the rev-1 and rev-2 artefacts are untouched and still
resolve.
