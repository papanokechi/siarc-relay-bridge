# Author-Info Audit Report

**Date:** 2026-05-03T14:50:00+09:00 (operator-local) /
        2026-05-03T05:50:00Z (UTC)
**Auditor:** GitHub Copilot (VS Code)
**Scope:** B + D + targeted-C
  - B: D2-NOTE v2 (pre-O2) vs D2-NOTE v1
  - C-targeted: PCF-1 v1.3, PCF-2 v1.3, CT v1.3, SIARC umbrella v2.0,
    T2B v3.0 (the 5 SIARC v1.3-cohort papers cross-referenced by
    D2-NOTE v2's Related Identifiers)
  - D: G13 (CT placeholder) + G14 (arXiv endorsement skeletons)
  - Plus: submission_log.txt cross-reference (CHECK 8); CMB.txt not
    present in workspace and recorded as N/A

**Files audited:** 10
  1. `siarc-relay-bridge/sessions/2026-05-03/Q20A-PHASE-C-RESUME/d2_note_v2/d2_note_v2.tex`  (D2-NOTE v2, pre-O2)
  2. `siarc-relay-bridge/sessions/2026-05-02/D2-NOTE-DRAFT/d2_note.tex`  (D2-NOTE v1, never deposited)
  3. `siarc-relay-bridge/sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf1_v1.3/pack/p12_pcf1_main.tex`  (PCF-1 v1.3, deposited)
  4. `siarc-relay-bridge/sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf2_v1.3/pack/pcf2_program_statement.tex`  (PCF-2 v1.3, deposited)
  5. `siarc-relay-bridge/sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_ct_v1.3/pack/channel_theory_outline.tex`  (CT v1.3, deposited)
  6. `siarc-relay-bridge/sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_siarc_umbrella_v2.0/pack/main.tex`  (umbrella v2.0, deposited)
  7. `siarc-relay-bridge/sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_t2b_v3.0/pack/t2b_paper_draft_v5_withauthor.tex`  (T2B v3.0, deposited)
  8. `siarc-relay-bridge/sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/ENDORSEMENT_REQUEST_pcf1_v1.3.md`
  9. `siarc-relay-bridge/sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/ENDORSEMENT_REQUEST_ct_v1.3.md`
 10. `tex/submitted/submission_log.txt`

---

## Authoritative reference (per audit prompt §1)

| Field         | Canonical value                                                |
|---------------|----------------------------------------------------------------|
| Name (pen)    | papanokechi  (preferred form for citation; default)            |
| Name (legal)  | Mauricio Echizen Kubo  (allowed in `pdfauthor=` metadata)      |
| ORCID         | https://orcid.org/0009-0000-6192-8273                          |
| Affiliation   | Independent researcher                                         |
| Location      | Yokohama, Japan                                                |
| Email         | not embedded in PDFs unless venue requires; varies (`shkubo@protonmail.com` and `shkubo@outlook.jp` both observed) |

Note on capitalisation: §1 says "papanokechi"; observed published forms
include both `Papanokechi` (Title Case) and `papanokechi` (lowercase).
Both are present in already-deposited Zenodo records, so neither is
strictly wrong — but D2-NOTE v2 should pick the form most consistent
with its sister papers.

---

## Per-file results

### File 1 — D2-NOTE v2 (pre-O2 deposit; **target of this audit**)
Path: `sessions/2026-05-03/Q20A-PHASE-C-RESUME/d2_note_v2/d2_note_v2.tex`

```latex
\usepackage{orcidlink}                         % line 28 — loaded but never invoked
\title[Cross-degree universality of the Borel-singularity radius]
      {Cross-degree universality of the Borel-singularity radius
       for polynomial continued fractions}
\author{Mauricio Echizen Kubo}                 % line 69
\address{Independent researcher, Yokohama, Japan}
\email{shkubo@protonmail.com}
```

| Check | Result            | Notes                                                                                              |
|-------|-------------------|----------------------------------------------------------------------------------------------------|
| 1     | PRESENT_DRIFT     | `\author{}`, `\address{}`, `\email{}` all present — but author name is *legal name*, not pen name |
| 2     | PRESENT_DRIFT     | Author = "Mauricio Echizen Kubo" (legal). Other SIARC deposits use "Papanokechi" / "papanokechi" (pen). |
| 3     | MISSING           | ORCID NOT in author block. `\usepackage{orcidlink}` loaded (line 28) but never invoked anywhere in .tex. |
| 4     | PRESENT_CORRECT   | "Independent researcher, Yokohama, Japan" in `\address{}` — matches §1 verbatim                    |
| 5     | PRESENT_CORRECT   | Email `shkubo@protonmail.com` present (Zenodo deposit doesn't require it but its presence is harmless)  |
| 6     | PRESENT_CORRECT   | AI Disclosure §AI Disclosure present, mentions Copilot + Claude Opus 4.7 + Claude (lines 478–490). Wording is project-style, not Elsevier-verbatim. |
| 7     | PRESENT_DRIFT     | Author name "Mauricio Echizen Kubo" disagrees with PCF-1/PCF-2/CT/umbrella/T2B all of which use Papanokechi or papanokechi |
| 8     | PRESENT_CORRECT   | Submission log (footer ORCID) matches §1 ORCID                                                     |
| 9     | NOT_APPLICABLE    | This file is not an endorsement request                                                            |

### File 2 — D2-NOTE v1 (NEVER DEPOSITED; informational only)
Path: `sessions/2026-05-02/D2-NOTE-DRAFT/d2_note.tex`

```latex
\author{Mauricio Echizen Kubo}                 % line 60
\address{Independent researcher, Yokohama, Japan}
\email{shkubo@protonmail.com}
```

Same author block as v2 (v2 inherited the field verbatim from v1).
Since v1 was never deposited, this is informational; the v1 → v2 drift
is purely the title and content, not the author block.

### File 3 — PCF-1 v1.3 (DEPOSITED 10.5281/zenodo.19937196)
Path: `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf1_v1.3/pack/p12_pcf1_main.tex`

```latex
\author{Papanokechi}                            % line 38
\address{Independent researcher, Yokohama, Japan}
\email{}                                        % blank
\thanks{ORCID:
\href{https://orcid.org/0009-0000-6192-8273}{0009-0000-6192-8273}.
The author received no external funding ... AI assistants are not authors. ...}
```

| Check | Result            | Notes                                                |
|-------|-------------------|------------------------------------------------------|
| 1     | PRESENT_CORRECT   | `\author{}`, `\address{}`, `\thanks{}` all present  |
| 2     | PRESENT_CORRECT   | "Papanokechi" (Title Case)                           |
| 3     | PRESENT_CORRECT   | ORCID 0009-0000-6192-8273 in `\thanks{}`             |
| 4     | PRESENT_CORRECT   | Independent researcher, Yokohama, Japan              |
| 5     | MISSING           | `\email{}` left blank — fine for Zenodo, would block journal portals |
| 6     | PRESENT_CORRECT   | AI Disclosure inside `\thanks{}` — Elsevier-compatible wording |
| 7     | PRESENT_CORRECT   | Anchor for the SIARC v1.3-cohort author convention   |

### File 4 — PCF-2 v1.3 (DEPOSITED 10.5281/zenodo.19963298)
Path: `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf2_v1.3/pack/pcf2_program_statement.tex`

```latex
\author{Papanokechi%
\thanks{ORCID: \href{https://orcid.org/0009-0000-6192-8273}{0009-0000-6192-8273}.
Independent Researcher, Yokohama, Japan.
\textbf{AI use disclosure.} ... GitHub Copilot ... Anthropic Claude ...}}
```

| Check | Result            | Notes                                                |
|-------|-------------------|------------------------------------------------------|
| 1     | PRESENT_CORRECT   | `\author{}` + `\thanks{}` (no separate `\address{}` or `\email{}`)  |
| 2     | PRESENT_CORRECT   | "Papanokechi" (Title Case) — matches PCF-1 / T2B    |
| 3     | PRESENT_CORRECT   | ORCID 0009-0000-6192-8273 in `\thanks{}`             |
| 4     | PRESENT_DRIFT     | "Independent Researcher" (capitalised "R"); §1 prefers lower-case "researcher" — matches PCF-2 / T2B but disagrees with PCF-1 / D2-NOTE. **Cosmetic only.** |
| 5     | NOT_APPLICABLE    | Email not present (Zenodo deposit, no journal portal) |
| 6     | PRESENT_CORRECT   | AI Disclosure inline in `\thanks{}` — strong, lengthy, project-style |

### File 5 — CT v1.3 (DEPOSITED 10.5281/zenodo.19972394) — **G13 OFFENDER**
Path: `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_ct_v1.3/pack/channel_theory_outline.tex`

```latex
\author{The SIARC author}                       % line 51 — PLACEHOLDER
% (no \thanks{}, no \address{}, no \email{}, no ORCID)
```

| Check | Result            | Notes                                                |
|-------|-------------------|------------------------------------------------------|
| 1     | PRESENT_DRIFT     | `\author{}` is placeholder; no `\address{}`, `\email{}`, or `\thanks{}` |
| 2     | PRESENT_DRIFT     | **"The SIARC author" — PLACEHOLDER. ALREADY DEPOSITED on Zenodo. CRITICAL.** Matches G13 in v1.11 strategic picture. |
| 3     | MISSING           | ORCID NOT in author block; only appears in §AI Disclosure prose at line ~1581 (still no explicit ORCID number there) |
| 4     | MISSING           | No affiliation in the title-page block                                                          |
| 5     | NOT_APPLICABLE    | Email not present (Zenodo + arXiv mirror)                                                        |
| 6     | PRESENT_CORRECT   | AI Disclosure §AI Disclosure paragraph at line 1566 mentions Copilot + Claude — **but no ORCID and no author name** |
| 7     | PRESENT_DRIFT     | Critical inter-artefact drift: every other SIARC paper has a real author name; CT has a placeholder |
| 8     | PRESENT_DRIFT     | submission_log Item 19 (CT v1.3) does not flag the placeholder — submission_log records the deposit DOI, not author-block content |

### File 6 — SIARC umbrella v2.0 (DEPOSITED 10.5281/zenodo.19965041)
Path: `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_siarc_umbrella_v2.0/pack/main.tex`

```latex
\author{papanokechi}                            % line 41 — lowercase
% (no \thanks{}, no \address{}, no \email{}, no ORCID)
```

| Check | Result            | Notes                                                |
|-------|-------------------|------------------------------------------------------|
| 1     | PRESENT_DRIFT     | Author block minimal — no `\thanks{}`, no `\address{}`, no `\email{}`, no ORCID                                                                       |
| 2     | PRESENT_CORRECT   | "papanokechi" (lowercase) — pen-name form per §1 default                                                                                              |
| 3     | MISSING           | ORCID NOT in author block; not in AI Disclosure §AI Disclosure either                                                                                  |
| 4     | MISSING           | No affiliation (§1 expects "Independent researcher, Yokohama, Japan")                                                                                  |
| 5     | NOT_APPLICABLE    | Email not present                                                                                                                                      |
| 6     | PRESENT_CORRECT   | §AI Disclosure at line 826 lists Copilot + Claude + supervision wording                                                                                |
| 7     | PRESENT_DRIFT     | Lowercase "papanokechi" disagrees with PCF-1/PCF-2/T2B's "Papanokechi" — but **already deposited**, so this is now permanent on Zenodo                |

### File 7 — T2B v3.0 (DEPOSITED 10.5281/zenodo.19915689)
Path: `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_t2b_v3.0/pack/t2b_paper_draft_v5_withauthor.tex`

```latex
\author{Papanokechi\\                           % line 26
Independent Researcher, Yokohama, Japan\\
ORCID: 0009-0000-6192-8273\\
\email{shkubo@outlook.jp}}
```

| Check | Result            | Notes                                                |
|-------|-------------------|------------------------------------------------------|
| 1     | PRESENT_CORRECT   | All four fields packed inline into `\author{}` — non-amsart layout |
| 2     | PRESENT_CORRECT   | "Papanokechi" (Title Case)                                                                              |
| 3     | PRESENT_CORRECT   | ORCID 0009-0000-6192-8273 inline                                                                         |
| 4     | PRESENT_DRIFT     | "Independent Researcher" (capitalised "R") — same as PCF-2; cosmetic                                    |
| 5     | PRESENT_CORRECT   | Email `shkubo@outlook.jp` (different from D2-NOTE v1/v2 which use `shkubo@protonmail.com`) — see Issue #6 |

### File 8 — `ENDORSEMENT_REQUEST_pcf1_v1.3.md` (G14)

| Field                               | Value                                                                                |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Greeting                            | `Dear <endorser name>` — placeholder                                                 |
| Endorsement code                    | `<arXiv-issued endorsement code, paste here once arXiv sends it to you>` — natural placeholder |
| Suggested endorser candidates       | `<endorser candidates to be supplied by operator>` — placeholder                     |
| Sign-off                            | `papanokechi / Independent Researcher, Yokohama, Japan / ORCID: 0009-0000-6192-8273 / Email: <operator-supplied>` |

| Check | Result                  | Notes                                                                            |
|-------|-------------------------|----------------------------------------------------------------------------------|
| 9     | PRESENT_DRIFT (deferred)| 3 placeholder tokens (`<endorser name>`, `<endorser candidates>`, `<operator-supplied>` email). Per v1.11 G14, this is expected: operator must acquire real arXiv handles before firing. **DEFERRED_OPERATOR_ACTION**, not a bug. |

### File 9 — `ENDORSEMENT_REQUEST_ct_v1.3.md` (G14)

Identical placeholder structure to File 8.

| Check | Result                  | Notes                                |
|-------|-------------------------|--------------------------------------|
| 9     | PRESENT_DRIFT (deferred)| Same finding as File 8.              |

### File 10 — `submission_log.txt`

| Field                                | Value                                              |
|--------------------------------------|----------------------------------------------------|
| Submission IDs (Items 5/7/8/9/11)    | "260{date}-Papanokechi" — Title-Case form          |
| Footer ORCID                         | `https://orcid.org/0009-0000-6192-8273` (line 682) — matches §1 |
| Submission_log placeholders          | None observed for author info                      |

| Check | Result            | Notes                                                |
|-------|-------------------|------------------------------------------------------|
| 8     | PRESENT_CORRECT   | Submission IDs use "Papanokechi"; footer ORCID matches §1; no placeholders in author-info fields. The "The SIARC author" placeholder in CT v1.3's `\author{}` was NOT mirrored into submission_log Item 19. |

### CMB.txt — NOT_APPLICABLE
File `tex/submitted/control center/CMB.txt` does not exist in the
workspace (audit prompt §2 SCOPE A mentions it but it's not present;
confirmed via `Get-ChildItem` on the control-center directory; only
`memo.txt`, `RESUME_AFTER_REBOOT_20260502.txt`, `_PASTE_resume_*`,
and `_test_write.txt` are present). Recorded as N/A.

---

## Comparison matrix (field × file)

| File              | `\author{}`                | ORCID in author block | Affiliation                              | Email                  | AI Disclosure |
|-------------------|----------------------------|-----------------------|------------------------------------------|------------------------|---------------|
| D2-NOTE v2 ⚠️     | `Mauricio Echizen Kubo`    | **NO** (pkg loaded only) | Independent researcher, Yokohama, Japan | shkubo@protonmail.com  | ✓             |
| D2-NOTE v1 (n/d)  | `Mauricio Echizen Kubo`    | **NO**                | Independent researcher, Yokohama, Japan | shkubo@protonmail.com  | ✓             |
| PCF-1 v1.3        | `Papanokechi`              | ✓ in `\thanks`        | Independent researcher, Yokohama, Japan | (blank)                | ✓ (in `\thanks`) |
| PCF-2 v1.3        | `Papanokechi`              | ✓ in `\thanks`        | Independent Researcher, Yokohama, Japan | (none)                 | ✓ (in `\thanks`) |
| CT v1.3 ⚠️🛑      | **`The SIARC author`**     | **NO**                | **NONE**                                | **NONE**               | ✓ (`\paragraph`)|
| umbrella v2.0     | `papanokechi` (lowercase)  | **NO**                | **NONE**                                | **NONE**               | ✓ (`\section`)|
| T2B v3.0          | `Papanokechi`              | ✓ inline              | Independent Researcher, Yokohama, Japan | shkubo@outlook.jp      | ✓ (`\thanks` — to verify) |

Authoritative §1: `papanokechi` / ORCID 0009-0000-6192-8273 /
"Independent researcher" (lower-case 'r') / "Yokohama, Japan".

Tally:
- **Author name** (canonical = `papanokechi` or `Papanokechi`):
  4 ✓ (PCF-1, PCF-2, T2B, umbrella) + 1 placeholder (CT) + 2 legal-name
  (D2-NOTE v1+v2). Of the 4 ✓: 3 Title Case, 1 lowercase.
- **ORCID in author block**: 3 ✓ (PCF-1, PCF-2, T2B); 4 missing
  (D2-NOTE v1+v2, CT, umbrella).
- **Affiliation in author block**: 4 ✓ (PCF-1, PCF-2, T2B, D2-NOTE v1+v2);
  2 missing (CT, umbrella).
- **AI Disclosure**: 7 ✓ (all files have some form of AI disclosure).

---

## Flagged issues

| # | Severity  | File                | Field                  | Observed                                              | Expected                                                | Recommended fix                                                                                                                          |
|---|-----------|---------------------|------------------------|-------------------------------------------------------|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | CRITICAL  | CT v1.3             | `\author{}`            | `The SIARC author` (placeholder)                      | `Papanokechi` (or `papanokechi`)                        | **Already deposited on Zenodo.** Cannot retroactively fix the published v1.3 record file. Mitigation: deposit CT v1.4 (already an open todo `ct-v14-narrative-draft`) with the corrected `\author{}` block; in interim Zenodo metadata-edit the v1.3 record's "Authors" field to "Papanokechi" (the metadata is editable post-publish even though files are not). |
| 2 | HIGH      | D2-NOTE v2          | `\author{}`            | `Mauricio Echizen Kubo`                               | `Papanokechi` (consistent with PCF-1/PCF-2/T2B cohort)  | Edit line 69 of `d2_note_v2.tex` to `\author{Papanokechi}` (or `papanokechi` for umbrella consistency — operator's call). Rebuild PDF, recompute SHA-256, update O1 review report and runbook §1.1 hashes. **Block O2 deposit until fixed.** |
| 3 | HIGH      | D2-NOTE v2          | ORCID                  | NOT in author block (`\usepackage{orcidlink}` loaded but never invoked) | ORCID 0009-0000-6192-8273 in `\thanks{}` per PCF-1/PCF-2 pattern | Add a `\thanks{ORCID: \href{https://orcid.org/0009-0000-6192-8273}{0009-0000-6192-8273}.}` to the author line, or use `\orcidlink{0009-0000-6192-8273}` since the package is already loaded. Rebuild and re-hash. **Bundle with fix #2.** |
| 4 | MEDIUM    | umbrella v2.0       | author block austerity | `\author{papanokechi}` only — no ORCID, no affiliation | ORCID + affiliation per PCF-1/PCF-2 pattern             | **Already deposited on Zenodo.** Operator can metadata-edit the Zenodo "Authors" / ORCID fields without re-depositing the file. Source-side fix would land in v2.1. |
| 5 | MEDIUM    | D2-NOTE v2          | author capitalisation  | (legal-name; will be fixed via #2)                   | Pick one of `Papanokechi` (PCF-1/PCF-2/T2B form) or `papanokechi` (umbrella form) | Default to **`Papanokechi`** (3 vs 1 prior deposits). Operator decision. |
| 6 | LOW       | D2-NOTE v2 vs T2B   | email address          | D2-NOTE: `shkubo@protonmail.com`; T2B: `shkubo@outlook.jp` | Pick one preferred form; both are valid                 | Operator preference: confirm whether `shkubo@protonmail.com` is the preferred citation email or whether `shkubo@outlook.jp` (used in git commits) should be the canonical one. No blocking issue. |
| 7 | LOW       | PCF-1 v1.3          | email                  | `\email{}` blank                                      | Either populated or removed                             | **Already deposited.** No action; cosmetic. PCF-2 / umbrella also omit email entirely. |
| 8 | INFO      | endorsement files   | `<endorser name>` etc. | 3 placeholder tokens                                  | Operator-acquired arXiv handles                         | **DEFERRED_OPERATOR_ACTION** (G14 in v1.11 picture; SQL todo `endorsement-handles-acquire` already pending). Not a bug — file is template by design. |
| 9 | INFO      | n/a                 | `CMB.txt`              | Not present in workspace                              | (mentioned in audit §2 SCOPE A but optional)            | None — recorded as N/A.                                                                                                                   |

---

## Recommended fixes (sorted by severity, operator action list)

### Pre-O2-deposit (BLOCKING — fix before D2-NOTE v2 Zenodo upload)

**Action 1** — Fix D2-NOTE v2 author block (issues #2 + #3 + #5,
recommended bundle):

Edit `siarc-relay-bridge/sessions/2026-05-03/Q20A-PHASE-C-RESUME/d2_note_v2/d2_note_v2.tex`,
replace lines 69-71:

```latex
\author{Mauricio Echizen Kubo}
\address{Independent researcher, Yokohama, Japan}
\email{shkubo@protonmail.com}
```

with (recommended; matches PCF-1 v1.3 idiom most closely):

```latex
\author{Papanokechi}
\address{Independent researcher, Yokohama, Japan}
\email{shkubo@protonmail.com}
\thanks{ORCID:
\href{https://orcid.org/0009-0000-6192-8273}{0009-0000-6192-8273}.
The author received no external funding for this work.
The numerical experiments were carried out using the AEAL/SIARC
multi-agent computational methodology described in
\cite{P8AEAL}; AI assistants (GitHub Copilot powered by Anthropic
Claude Opus 4.7, and Anthropic Claude directly) were used to
generate code for high-precision computations and to cross-check
intermediate results. All conjectures, proofs, evidence-class
assignments, and editorial decisions are the sole responsibility
of the human author. The AI assistants are not authors. Session-level
computation logs and prompts are archived in the SIARC research
workspace and are available from the author on request, in line
with the AEAL reproducibility requirement.}
```

(If `\thanks{}` is added, the existing standalone `\section*{AI Disclosure}`
block at line 478 becomes redundant — operator's choice whether to keep
both or fold the prose into `\thanks{}`. Folding gives a tighter title
page; keeping both gives a more visible disclosure.)

After edit:
1. Rebuild: `pdflatex → bibtex → pdflatex → pdflatex`
2. Recompute hashes:
   `Get-FileHash -Algorithm SHA256 d2_note_v2.tex, d2_note_v2.pdf, annotated_bibliography.bib`
3. Update `o1_operator_review.md` to flag the new hashes (the prior O1
   verdict READY_FOR_DEPOSIT was issued without checking author info — author audit was a separate task class; verdict stands for the 9 content checks but the author block was out of scope).
4. Update `zenodo_upload_d2_note_v2_runbook.md` §1.1 expected-hashes
   table with the new SHA-256 values.
5. Update `claims.jsonl` to append a "rebuild-after-author-fix" claim
   citing the new PDF hash (replaces the dispatch-4 hash for citation
   purposes; original entry stays as historical anchor).
6. Re-fire O1 (or self-verify the 9 content checks still pass — author
   block is the only change so checks 2-9 should be unchanged).

### Post-O2-deposit (NON-BLOCKING — Zenodo metadata edits)

**Action 2** — Metadata-edit CT v1.3 Zenodo record (issue #1):

On https://zenodo.org/records/19972394 → Edit metadata → Authors field,
change the listed author from "The SIARC author" (if Zenodo even shows
the placeholder) to "Papanokechi" with ORCID 0009-0000-6192-8273.
Zenodo allows metadata edits without changing the deposited file (the
PDF stays as-is with the placeholder in `\author{}`, but the Zenodo-side
"Authors" field — which is what cite generators use — gets corrected).

**Action 3** — Metadata-edit umbrella v2.0 Zenodo record (issue #4):

On https://zenodo.org/records/19965041 → Edit metadata → Authors field,
add ORCID 0009-0000-6192-8273 and affiliation "Independent researcher,
Yokohama, Japan" to the existing "papanokechi" author entry.

### Long-term (in next CT / umbrella revision)

**Action 4** — Land the corrected `\author{}` block in CT v1.4 (open
todo `ct-v14-narrative-draft`) and umbrella v2.1, replicating the
PCF-1 v1.3 idiom (Papanokechi + ORCID in `\thanks{}` + `\address{}`).

### Endorsement templates

**Action 5** — Per G14 (open todo `endorsement-handles-acquire`),
operator acquires real arXiv handles for math.NT and math.CA endorsers
and substitutes the 3 placeholder tokens in each of
`ENDORSEMENT_REQUEST_pcf1_v1.3.md` and `ENDORSEMENT_REQUEST_ct_v1.3.md`.

---

## Overall verdict

**`NEEDS_PRE_DEPOSIT_FIXES`**

Two HIGH issues block D2-NOTE v2's deposit:
- Issue #2 (author name `Mauricio Echizen Kubo` → `Papanokechi`)
- Issue #3 (ORCID missing from author block)

These can be fixed in a single edit (Action 1 above) plus one rebuild
cycle. After re-build + re-hash + re-runbook, deposit may proceed.

The CRITICAL issue (#1, CT v1.3 placeholder) is **already deposited
and not blocking D2-NOTE v2** — it's a separate cleanup that should
be handled via Zenodo metadata edit + CT v1.4 source-side fix.

The endorsement-template placeholders (issue #8) are
DEFERRED_OPERATOR_ACTION per G14 and not blocking.

---

## Notes for synthesizer

1. **Why O1 missed this:** the O1 prompt's 9 content checks did NOT
   include author block / ORCID consistency (it focused on the
   substantive math: theorem statement, citations, AI Disclosure
   presence). O1's READY_FOR_DEPOSIT verdict stands for what it
   checked. This audit is a complementary class of pre-deposit check
   that O1 was not designed to catch.

2. **Why the v1 author block carried forward:** D2-NOTE v2 inherited
   `\author{Mauricio Echizen Kubo}` verbatim from D2-NOTE v1, which
   itself diverged from the rest of the SIARC v1.3 cohort. Since v1
   was never deposited, the inconsistency only matters now that v2 is
   about to be the first D2-NOTE on Zenodo.

3. **Pen vs legal name in `pdfauthor=`:** A reasonable convention is
   `\author{Papanokechi}` (pen, citation-facing) + `pdfauthor={Mauricio Echizen Kubo}`
   (legal, PDF-metadata-facing). The current d2_note_v2.tex already has
   `pdfauthor={Mauricio Echizen Kubo}` (line 38) which can stay; only
   `\author{}` needs to change. This matches a precedent in the
   academic-publishing world where ORCID + legal-name go in the
   metadata layer while the visible byline is the pen name.

4. **Capitalisation Pareto:** `Papanokechi` (3 deposits: PCF-1, PCF-2,
   T2B) > `papanokechi` (1 deposit: umbrella) > `The SIARC author` (1
   deposit: CT). Recommended for D2-NOTE v2: **Papanokechi** (Title
   Case) for cohort majority consistency.

5. **AI Disclosure already present in all 7 files** — no fix needed for
   CHECK 6 in any file. Wording varies (some Elsevier-verbatim, some
   project-style); operator can homogenise in next revisions.

6. **CT v1.3 placeholder severity:** This is a **CRITICAL** finding for
   the historical record but not blocking *this* (D2-NOTE v2) deposit.
   It is the canonical G13 from the v1.11 strategic picture. The Zenodo
   metadata is editable post-publish (only the deposited file is
   immutable), so the cite-facing display name can be corrected without
   a v1.3.1 re-deposit.

7. **submission_log healthy:** No author-info placeholders in the
   submission log; the placeholder issue is confined to LaTeX source
   files of the deposited PDFs.
