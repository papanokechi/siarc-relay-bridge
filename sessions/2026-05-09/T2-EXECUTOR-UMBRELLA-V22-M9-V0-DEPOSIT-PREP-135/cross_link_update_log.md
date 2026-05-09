# Cross-link metadata update log — operator-pending

**Session**: T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135
**Status**: OPERATOR-PENDING (TABLED under RULE 1 §1; runs at Phase D after Phase C Zenodo deposit lands)

---

## Scope

After the umbrella v2.2 Zenodo deposit lands (Phase C; see `zenodo_v22_deposit_log.md`), the operator must run the following cross-link metadata edits to propagate the new v2.2 version DOI throughout the SIARC corpus.

## Edit targets (operator fills with assigned version DOI)

Replace `<UMB_V22_DOI>` placeholders below with the actual Zenodo v2.2 version DOI assigned at deposit time.

### 1. BibTeX — companion-paper bibliography entries

| File                                                   | Edit                                                                               |
|--------------------------------------------------------|------------------------------------------------------------------------------------|
| `tex/submitted/pcf_one_paper/main.tex` (or its `.bib`) | Update `@misc{UMBv2_0,...}` → add `@misc{UMBv2_2, doi={10.5281/zenodo.<UMB_V22_DOI>},...}` |
| `tex/submitted/pcf_two_paper/main.tex` (or its `.bib`) | Same                                                                               |
| `tex/submitted/channel_theory_paper/main.tex` (or `.bib`) | Same                                                                               |
| `tex/submitted/t2b_paper/main.tex` (or its `.bib`)     | Same                                                                               |
| `tex/submitted/jSN_paper/main.tex` (or its `.bib`)     | Same                                                                               |

### 2. Abstract DOI links — companion-paper abstracts that cite the umbrella

For each companion paper above, audit the abstract for citations of the form `\cite{UMBv2_0}` or "(see umbrella v2.0)" and update to `\cite{UMBv2_2}` / "(see umbrella v2.2)" where appropriate. v2.0's content is unchanged at v2.2; the citation update is for traceability to the latest deposited record.

### 3. Bridge cross-references

| File                                                                                | Edit                                                                  |
|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| `tex/submitted/control center/picture/picture_v1.19.txt` (and v1.20+ when cut)      | Update umbrella DOI references to v2.2 version DOI                    |
| `tex/submitted/CMB.txt`                                                             | Update umbrella DOI references to v2.2 version DOI                    |
| `siarc-relay-bridge/sessions/.../*.md` (any prior sessions citing umbrella DOI)     | Generally do NOT retro-edit historical sessions; new sessions cite v2.2 |

### 4. README / index files

| File                                                                | Edit                                                  |
|---------------------------------------------------------------------|-------------------------------------------------------|
| `tex/submitted/README.md` (if present)                              | Add v2.2 row; mark v2.0 as superseded; mark v2.1 as internal-staging-not-deposited |
| `siarc-relay-bridge/README.md`                                      | Same                                                  |

### 5. Operator handles / outputs (no edits required; informational)

- Submission_log Item 12 series 2 splice: see `submission_log_item12_splice.diff` (separate operator runbook)
- SQL todos update: see `zenodo_v22_deposit_log.md` post-deposit actions

## Edit transaction record (operator fills)

| Edit                          | File                  | Date applied | SHA before | SHA after | Notes |
|-------------------------------|-----------------------|--------------|------------|-----------|-------|
| BibTeX UMBv2_2 entry          | `<file>`              | `<date>`     | `<sha>`    | `<sha>`   | `<note>` |
| ...                           | ...                   | ...          | ...        | ...       | ... |

## Validation (post-edit)

- [ ] Re-compile each companion paper that was edited; verify pdflatex 2-pass clean
- [ ] Verify all `\cite{UMBv2_2}` references resolve
- [ ] Verify Zenodo DOI links resolve (HTTP 200; correct landing page)

---

**End of cross_link_update_log.md (template; operator fills at Phase D).**
