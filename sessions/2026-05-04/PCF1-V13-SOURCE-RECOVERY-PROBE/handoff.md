# Handoff — PCF1-V13-SOURCE-RECOVERY-PROBE
**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~30 minutes
**Status:** COMPLETE

## What was accomplished

Closed G12 (PCF-1 v1.3 page-count drift, HIGH severity) at the
recovery-probe level. Located the canonical 16pp v1.3 PCF-1 TeX
source on the bridge at `sessions/2026-05-01/PCF1-V13-UPDATE/`
(commit `58dfa9e732b41b65c2d8791037286a13e21c06be`, May 1 2026
12:17:35 JST). The committed PDF at that path is **byte-identical**
to the Zenodo-served deposit PDF (SHA-256
`63420dbf4abb…d9788ff5e`, 392,886 bytes, 16 pages). Operator can
manually `git checkout 58dfa9e -- sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.tex`
on the bridge (or simply read it directly from the already-committed
tree) to obtain the canonical TeX source. No rebuild is required for
PDF-hash matching against Zenodo: the canonical PDF is already
preserved on the bridge.

**Verdict:** `UPGRADE_PCF1_V13_RECOVERY_BRIDGE_SNAPSHOT`
(equivalently `UPGRADE_PCF1_V13_RECOVERY_COMMIT_FOUND_58dfa9e`)
— two outcome-ladder rungs collapse onto the same artefact.

## Key numerical findings

- Workspace TeX `tex/submitted/p12_journal_main.tex`: SHA-256
  `82173a09521d…a4786853`, 72,311 bytes, 1,498 lines, builds to
  21pp (cached PDF, MiKTeX pdfTeX-1.40.28).
  *(Phase A.1, file_provenance + pypdf)*
- Zenodo v1.3 PDF: SHA-256 `63420dbf4abb…d9788ff5e`, 392,886 bytes,
  16 pages, /CreationDate `D:20260501121611+09'00'`.
  *(Phase A.2, deposit_confirmation)*
- Page-count drift: 21pp / 16pp = 1.3125× (below HALT >50% threshold).
  *(Phase A.3, computation)*
- Canonical 16pp v1.3 TeX (recovered): bridge path
  `sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.tex`,
  SHA-256 `e83bb377f297…74be301`, 46,349 bytes, 837 lines.
  *(Phase D.1, file_provenance)*
- Canonical 16pp v1.3 PDF: SHA-256
  `63420dbf4abb…d9788ff5e` — **byte-exact match** against Zenodo
  (not "modulo build environment"; literal byte equality).
  *(Phase D.1, computation)*
- Workspace ↔ canonical structural diff: +1 §, +34 §§, 0 new
  theorems, +1 corollary, +1 conjecture, +8 equations, +9 bibitems,
  +2,527 words, +25,962 bytes; growth dominated by Background
  section, Computational Methodology section, and 6-§§ appendix
  (journal-style scaffolding) plus 1 new conjecture.
  *(Phase C.2, computation; see workspace_vs_zenodo_diff.md)*

## Judgment calls made

- Treated commit `58dfa9e` as the canonical recovery anchor without
  enumerating earlier candidates: only one bridge commit touches
  `p12_pcf1_main.tex`, and its committed PDF byte-matches Zenodo
  exactly (so no further candidates can improve the result).
- Did NOT execute `git checkout` on the bridge per Rule 2 (operator
  action territory); only read-only `git show --stat` and direct
  file reads on the already-committed tree.
- Did NOT re-fetch Zenodo PDF from network per Rule 1 (no API key /
  no auto-fetch); used the locally cached copy at
  `sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf1_v1.3/zenodo.pdf`
  whose SHA matches the documented Zenodo value.
- Did NOT auto-rebuild via pdflatex; relied on the committed
  artefact PDF for the byte-match assertion (per §6 out-of-scope).

## Anomalies and open questions

**Anomaly #1 (MEDIUM):** The bridge `arxiv_pack_pcf1_v1.3` from
2026-05-02 contains the post-edit 21pp TeX (SHA `82173a09…`,
byte-identical to the workspace), and its `00README.txt` states
"Expected page count: 21". The 002 ARXIV-MIRROR-RUNBOOK already
flagged the local-vs-Zenodo PDF hash mismatch
(`hash_match.json: match=false`). The 02 packaging session
inadvertently re-packed the workspace post-edit state under the
v1.3 label. The actual canonical 16pp source is preserved
**only** at the earlier `sessions/2026-05-01/PCF1-V13-UPDATE/`
checkpoint (commit `58dfa9e`). If only the 02 pack had survived,
recovery would have been infeasible from the bridge alone.
This is logged in `unexpected_finds.json` and is worth a
post-mortem on the arxiv-pack runbook (RUNBOOK_pcf1_v1.3.md).

**Anomaly #2 (LOW):** `tex/submitted/p12_journal_main.tex` is
**untracked** in the workspace `.git` repo. All version control
for PCF-1 v1.3 lives on the bridge, not the workspace. Operator
may wish to bring `tex/submitted/*.tex` files under explicit git
tracking on the workspace side as a hedge against future probes.

**Open question (for Claude review):** Does the 1 new conjecture
in the v1.4 working draft (workspace 5 × `\begin{conjecture}` vs
canonical 4) carry theorem-grade weight or is it a restatement?
This was not in scope for recovery; flagging for forward planning.

## What would have been asked (if bidirectional)

- Should the 002 ARXIV-MIRROR-RUNBOOK arxiv-pack v1.3 be
  regenerated from the canonical bridge commit `58dfa9e` rather
  than from workspace state? (Operator-side decision.)
- Should the workspace `tex/submitted/p12_journal_main.tex` be
  renamed back to `p12_pcf1_main.tex` for consistency with
  Zenodo / arxiv-pack naming? (Operator-side.)

## Recommended next step

**Operator option-(b) is now feasible without further research.**
For Prompt 002 (arXiv mirror runbook) re-fire on math.NT record #2
(PCF-1 v1.3), the operator can either:

  1. Use the already-committed canonical PDF directly:
     `siarc-relay-bridge/sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.pdf`
     (byte-identical to Zenodo; arXiv mirror upload uses this PDF).

  2. If a fresh build is preferred: rebuild from the canonical TeX:
     `siarc-relay-bridge/sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.tex`
     using MiKTeX pdfTeX-1.40.28 (recipe in 00README.txt of arxiv-pack).
     Note: the rebuild will produce a PDF that **may** differ at the
     byte level from Zenodo if any environmental metadata (build
     date, font cache version) drifts; the canonical PDF approach
     (option 1) is the hash-clean route.

Operator option-(a) (v1.4 bump on Zenodo) is **no longer required**
to unblock 002 re-fire, but remains available as a forward strategic
choice if the v1.4 working-draft expansion (Background section,
Computational Methodology section, 6-§§ appendix, +1 conjecture) is
deemed substantive enough to warrant a fresh deposit.

**Recommended next prompt:** Operator-side micro-prompt to either
(i) re-fire Prompt 002 against the canonical PDF route above
(option-(b) closure), or (ii) decide on v1.4 bump strategy
(option-(a) forward path). Picture v1.18 should annotate G12 with
verdict `CLOSED_VIA_BRIDGE_SNAPSHOT_58DFA9E` and pre-condition
"Prompt 002 re-fire ready, operator decision pending option-(a)
vs option-(b) for forward strategy".

## Files committed

```
sessions/2026-05-04/PCF1-V13-SOURCE-RECOVERY-PROBE/
  prompt_spec_used.md
  zenodo_v1_3_structural_analysis.md
  workspace_vs_zenodo_diff.md
  claims.jsonl
  halt_log.json
  discrepancy_log.json
  unexpected_finds.json
  handoff.md  (this file)
```

## AEAL claim count

10 entries written to `claims.jsonl` this session.

Evidence type breakdown:
  - file_provenance:        2  (workspace + recovered TeX)
  - deposit_confirmation:   1  (Zenodo PDF)
  - git_log:                2  (bridge commit + workspace untracked)
  - computation:            5  (page-count drift, byte-match,
                                structural counts, structural diff,
                                verdict synthesis)
