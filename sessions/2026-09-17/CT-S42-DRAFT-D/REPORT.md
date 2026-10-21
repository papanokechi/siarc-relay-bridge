# REPORT — CT-S42-DRAFT-D (Group D)

**Sections 7 and 8 drafted. Gate PASSED, 11/11 arms. Assembly 0–8 clean at 29
pages. 13 claims emitted. Nothing committed, nothing deposited.**

---

## 1. What was done

1. Staged §0–§6 into `refs/` — §0 and §2 from CT-S40's *repaired* copies, not
   CT-S39's, which still carry the `sec:local` stub defect.
2. Resolved all 22 outline-assigned claim ids for §7 and §8 against the
   corpus, dumped their **full texts** to `outputs/claims_s7.txt` and
   `outputs/claims_s8.txt`, and drafted from those rather than from the
   outline's paraphrase.
3. Applied **operator ruling 2** before drafting: wrote `preamble.tex` as the
   single authoritative preamble.
4. Wrote `PREREG.md`, including the §8 scope trap, before any script ran.
5. Drafted `section7.tex` (12 659 B, 5 subsections) and `section8.tex`
   (11 521 B, 6 subsections).
6. Built `scripts/check_group_d.py` with rules D0–D7 and eleven control arms,
   applying **operator ruling 1** to its census output.
7. Assembled `combined_0to8.tex`; shrank the stub to `forwardrefs_E.tex`;
   repointed and re-ran `check_assembly.py` and `mutants_assembly.py`.
8. Emitted 13 claims through the three-pass procedure, validating the
   in-memory buffer before any write.

## 2. Results

| gate | verdict |
|---|---|
| `check_group_d.py` | **PASSED** — 23 citations, 98 literals, 3 stub labels, **0 failures**, **11/11 arms CAUGHT** |
| `check_assembly.py` | **PASS** — 103 labels, 70 targets all resolving, 0 dangling, 0 duplicated, 0 stub overreach |
| `mutants_assembly.py` | **7/7 arms CAUGHT** |
| build | 29 pages, **0 errors, 0 undefined, 0 multiply-defined** |
| gate invariance | output byte-identical before and after emission (`47d49184…`) |
| digest resolution | **8/8** `output_hash` values resolve to a file in this session |

Label census for the 22 ids: **6 PROVEN, 13 VERIFIED, 3 STRUCTURAL**. All 22
resolve, none is superseded, none is duplicated.

## 3. Defects found, and how

### 3.1 Two gate reader defects, neither in the prose (`S42-07`)

The gate's first run failed with one D6 hit and one arm SKIPPED. **Both were
defects in the reader.** Diagnosed against the raw prose *before* anything was
edited; the prose asserted both hazards correctly and was not touched.

- The hazard needle `is the output of` did not match prose reading *is
  therefore the output of*.
- Arm D6b could not reach its site: **arms mutate raw text while the rules
  compare squashed text**, and the needle straddled a line break. Reported as
  `SKIPPED (mutation site absent)` — the CT-S41 `S41-05` class, legible only
  because the harness distinguishes it from MISSED.

### 3.2 Two readers wrong in opposite directions (`S42-13`)

This is the session's most instructive finding and it cost two iterations.

`S42-11` was **first written** asserting that no claim in the corpus cites any
digest of `OUTLINE.md`. The emit script's own pre-write check **refused to
write** and said so. That was correct: `S24-01` and `S24-08` both cite
`OUTLINE.md` at **revision 2**.

But the check that caught it was itself **under-counting**: it bounded the gap
between `OUTLINE.md` and the digest at 80 characters, and `S24-01` separates
them by about 105, so it reported **1** citing line where there are **2**. It
was right about the substance and wrong about the count — the harder case.

The obvious repair — harvest every 64-hex string on any line naming the file —
then **over-counted**, reporting 15 "OUTLINE.md digests" of which all but one
were the claims' own `output_hash` values.

The lesson is that **proximity in a line cannot decide whether a digest is a
digest *of* a named file, and no bound on it can.** The check was replaced by
the **decidable** question — does the pre-edit digest appear anywhere in the
corpus — carrying a **positive control** (`0b94a7fc`, known to be cited) so
that *absent* cannot be confused with *my reader could not see it*.

Outcome: the pre-edit prefix `b8d85626` appears in no `claims.jsonl` in the
corpus; the control is found. **The outline edit stranded nothing.** The
revision-2 digest that *is* cited was already four revisions stale before this
session began.

### 3.3 A tenth notation collision, reported not repaired (`S42-10`)

`S22-24`'s invariant `P = a² + bc` collides with the `P` of the trace-free
normal form `∂² + P∂ + Q` used in §3 and §6. §8 avoids introducing the
collision by writing the invariant as `−det A`, which it equals for traceless
`A`, and **naming** it rather than lettering it.

This is **not** the §3/§6 `R` item. The operator ruled that one is a single
construction at two specialisations and wants it **unified**; this one wants
**separating**. Both belong to the second notation pass after Group E.

## 4. Rulings applied

**Ruling 1 (census + fingerprint)** — `check_group_d.py` prints the census
(453 files, 1434 ids) *together with* a sha256 over the sorted list of the 453
walked paths, and states in its own output that **no claim of
byte-reproducibility across sessions is made**. `S42-05`.

**Ruling 2 (one authoritative preamble)** — `preamble.tex` loads `hyperref`
exactly once; `combined_0to8.tex` `\input`s it and declares no package of its
own. No per-group wrapper was written. `S42-04`.

**Ruling 3 (the `R` item)** — verified and **deferred**, as directed. Recorded
alongside the new tenth item at `S42-10`.

**Ruling 4 (`OUTLINE.md` at source)** — applied in the previous segment; five
ambiguous outline-internal references disambiguated and a numbering-convention
note added. Recorded here with the digest evidence at `S42-11`.

## 5. What was NOT established

- **No displayed formula was re-derived.** The gate is a *transcription* test.
  A transposed digit inside a formula appearing in no claim text passes every
  rule here and builds clean. `S42-12`. This is the standing gap the operator
  scoped for a pass after Group E, and it is now stated in three group reports.
- **The methods appendix does not exist.** §7 defers `S22-04` and `S22-05` to
  it and forward-references `app:methods` through the stub. **Group E owes it.**
- `S22-20` remains **VERIFIED**-numerical. `S25-02` supplies structure at the
  level of the **parameters** only; the character-variety statement is not
  proved, and §8 says so in the same paragraph.
- No monodromy, Stokes or transport computation was re-run. Every number is
  transcribed from an existing claim record.

## 6. Open questions for the operator

1. **The appendix obligation.** §7 defers two claims to a methods appendix
   that Group E must create. Confirm Group E owns it, or say where else it
   goes.
2. **The tenth collision.** Is `−det A` acceptable as §8's permanent wording,
   or should the notation pass letter it?
3. **`S42-13`'s generalisation.** Worth recording as a standing rule: *a
   textual association between a filename and a digest is not decidable by
   proximity; test the digest itself, with a positive control.* It is the
   fifth instance this run of a reader that cannot see what it reports on, and
   the first where the reader was right about the substance and wrong about
   the count.
4. **`forwardrefs_E.tex` after Group E.** When §9 and §10 land the stub should
   be empty and then deleted; D7 will fail automatically if it is not shrunk.

## 7. Uncommitted files (all inside `sessions/2026-09-17/CT-S42-DRAFT-D/`)

```
PREREG.md                          6 587 B
REPORT.md                          this file
claims.jsonl                      10 972 B   13 claims
preamble.tex                       1 870 B   ruling 2
section7.tex                      12 659 B
section8.tex                      11 521 B
forwardrefs_E.tex                  1 052 B   3 entries
combined_0to8.tex                    316 B
combined_0to8.pdf                          29 pages
scripts/check_group_d.py                     D0-D7, 11 arms
scripts/check_assembly.py                    repointed
scripts/mutants_assembly.py                  repointed, 7 arms
scripts/emit_claims_s42.py                   86 pre-write checks
scripts/claim_index.py                       copied from CT-S41
refs/section0..6.tex                         staged, unmodified
outputs/*.txt                                gate and build outputs
```

Plus, from the previous segment and outside this folder:
`sessions/2026-09-17/CT-S24-PAPER-OUTLINE/OUTLINE.md` — ruling 4, six edits.
Nothing else outside this folder was written. `git` HEAD is unchanged and
nothing was staged, committed, pushed, tagged or deposited.
