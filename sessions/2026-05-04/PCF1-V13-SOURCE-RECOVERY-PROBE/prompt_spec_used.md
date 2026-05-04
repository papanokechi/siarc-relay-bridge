================================================================
SIARC RESEARCHER PROMPT 027 — PCF1-V13-SOURCE-RECOVERY-PROBE
================================================================
TASK ID:        PCF1-V13-SOURCE-RECOVERY-PROBE
COMPOSED:       2026-05-04 ~13:40 JST
DRAFTED-BY:     Copilot CLI (Claude Opus 4.7 xhigh)
AGENT:          Copilot researcher (git-history mining of
                bridge + workspace + Zenodo PDF text-layer
                extraction; bibliographic provenance probe).
GATES:          NEW PROMPT (NOT YET QUEUED). G12 option-(b)
                research route: recover PCF-1 v1.3 16pp source
                snapshot from git history / Zenodo archive.
                Triggered by ENDORSER-HANDLE-ACQUISITION
                (Prompt 022) verdict 2026-05-04: PCF-1 page-
                count drift gates Prompt 002 re-fire for
                math.NT record #2. Parallel-safe with all
                v1.17 / 024-batch tasks.
PRIOR ANCHORS:  002_arxiv_mirror_runbook_EXECUTED.txt 2026-05-02
                (verdict ARXIV_MIRROR_HALTED_PAGE_COUNT_DRIFT_2;
                PCF-1 21pp local vs 16pp Zenodo); v1.17 picture
                §5 G12 row; ENDORSER-HANDLE-ACQUISITION verdict
                2026-05-04 (operator outreach gates 002 re-fire).
COMPUTE BUDGET: ~2 hr researcher (git-history mining +
                Zenodo PDF text-layer extraction +
                bibliographic provenance reconstruction).
RUNTIME PROFILE:Git log on bridge + workspace; pypdf text
                extraction on Zenodo deposit PDF; cross-source
                comparison of section / equation counts.
                Per Rule 2: operator handles any ILL or
                Zenodo-side action. Per Rule 1: no API keys.

================================================================
§0 GOAL
================================================================

G12 (NEW v1.x; HIGH severity) names a source-drift gap: PCF-1
v1.3 workspace `p12_pcf1_main.tex` (or similar) rebuilds to
21 pp; Zenodo v1.3 deposit PDF is 16 pp. The v1.4 working draft
has likely overwritten the v1.3 snapshot in workspace. This
prevents Prompt 002 (arXiv mirror runbook) from re-firing for
math.NT record #2 (PCF-1 v1.3) because the local TeX rebuild
hash differs from the Zenodo-served PDF hash by 5 pages.

G12 has two option paths (operator decision territory):
  (a) v1.4 bump: Zenodo-deposit a fresh PCF-1 v1.4 with the
      21pp content; re-run 002 against the new v1.4 DOI.
      Operator-side action (separate workflow).
  (b) v1.3 source recovery: locate the canonical 16pp v1.3
      TeX source state from git history + Zenodo metadata;
      re-create a clean 16pp build that hashes-match the
      Zenodo PDF; re-run 002 against the existing v1.3 DOI.

This task pursues option (b) as a research probe.

[Full prompt body archived verbatim from
 tex/submitted/control center/prompt/027_pcf1_v13_source_recovery_probe.txt
 — see workspace path. Phase 0 verbatim copy retained inline below for
 self-containment.]

================================================================
§1 ANCHOR FILES (preconditions; verify all present)
================================================================

WORKSPACE TEX SOURCE (current 21pp state):
  tex/submitted/p12_journal_main.tex (current PCF-1 working
  file — discovered via Get-ChildItem tex/submitted/ -Filter
  "p12_*"). Note: file name is `p12_journal_main.tex`, not
  `p12_pcf1_main.tex` — the canonical filename was renamed
  during v1.4 working-draft expansion.

PCF-1 v1.3 ZENODO DEPOSIT PDF (canonical 16pp):
  Cached at:
    siarc-relay-bridge/sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/
      arxiv_pack_pcf1_v1.3/zenodo.pdf
  SHA-256: 63420dbf4abb7124672f522c37fc04ebdb3f6694ac39959456b2890d9788ff5e
  Source URL: https://zenodo.org/records/19937196/files/p12_pcf1_main.pdf

PRIOR HANDOFFS:
  sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/handoff.md
  sessions/2026-05-04/ENDORSER-HANDLE-ACQUISITION/handoff.md

PICTURE v1.17:
  tex/submitted/control center/picture_revised_20260504.md §5 G12

================================================================
§2 PHASES (executed)
================================================================

PHASE 0 — provenance write-out          [DONE — this file]
PHASE A — confirm baselines             [DONE — see handoff §2]
PHASE B — git-history mining            [DONE — bridge commit 58dfa9e found]
PHASE C — Zenodo PDF structural analysis[DONE — see zenodo_v1_3_structural_analysis.md
                                                + workspace_vs_zenodo_diff.md]
PHASE D — recovery candidate verification[DONE — SHA-256 byte-match
                                                 between commit 58dfa9e PDF and
                                                 Zenodo deposit PDF]
PHASE E — verdict + handoff              [DONE — see handoff.md]

================================================================
§3-§8: see relay-prompt source for AEAL minimum, halt conditions,
forbidden-verb hygiene, out-of-scope, outcome ladder, standing
final step. All retained.
================================================================
