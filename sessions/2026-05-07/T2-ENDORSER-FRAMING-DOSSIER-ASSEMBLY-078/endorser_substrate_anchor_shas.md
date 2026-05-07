# Endorser Substrate Anchor SHAs — 078

**Session:** T2-ENDORSER-FRAMING-DOSSIER-ASSEMBLY-078
**Compiled:** 2026-05-07 ~14:50 JST
**Bridge HEAD at fire:** `49f3423` (T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077 LANDED;
floor `5137155` per spec §1.A.3 satisfied)
**Scope:** Phase A SHA anchors for all substrate consumed in 078.

All hashes are SHA-256 (first 16 hex chars displayed for compact reference;
full hashes derivable on demand via
`Get-FileHash -Algorithm SHA256 -LiteralPath <path>`).

---

## §A.1 — 2026-05-04 ENDORSER-HANDLE-ACQUISITION substrate (5 templates + dossier + handoff)

| # | File | Bytes | SHA-256 (16) |
|---|---|---:|---|
| H.1 | `sessions/2026-05-04/ENDORSER-HANDLE-ACQUISITION/candidate_dossier.md` | 10784 | `315410D80EDC92C5` |
| H.2 | `sessions/2026-05-04/ENDORSER-HANDLE-ACQUISITION/handoff.md` | 10861 | `BB1CA7456ABA5F95` |
| H.3 | `sessions/2026-05-04/ENDORSER-HANDLE-ACQUISITION/endorsement_request_record2_PCF1_zudilin.md` | 5364 | `6B95796DEA080760` |
| H.4 | `sessions/2026-05-04/ENDORSER-HANDLE-ACQUISITION/endorsement_request_record2_PCF1_garoufalidis.md` | 5092 | `44446F6445C66188` |
| H.5 | `sessions/2026-05-04/ENDORSER-HANDLE-ACQUISITION/endorsement_request_record4_CT_mazzocco.md` | 5436 | `FC0358D4599805EE` |
| H.6 | `sessions/2026-05-04/ENDORSER-HANDLE-ACQUISITION/endorsement_request_record4_CT_zudilin.md` | 4726 | `9F7F7C202FE4EF45` |
| H.7 | `sessions/2026-05-04/ENDORSER-HANDLE-ACQUISITION/endorsement_request_record4_CT_garoufalidis.md` | 4684 | `59A6747FD646E5C6` |

## §A.2 — 2026-05-04 ARXIV-ENDORSEMENT-TEMPLATES-EXPAND substrate (9 templates + matrix + handoff)

| # | File | Bytes | SHA-256 (16) |
|---|---|---:|---|
| E.1 | `sessions/2026-05-04/ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/subject_fit_matrix.md` | 6008 | `142CF1943F6B67D5` |
| E.2 | `sessions/2026-05-04/ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/handoff.md` | 6590 | `E50AC5A5E65C1AB1` |
| E.3 | `sessions/2026-05-04/ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/endorsement_template_umbrella_v2.0_zudilin.md` | 6319 | `AF420EA44BC9B5DA` |
| E.4 | `sessions/2026-05-04/ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/endorsement_template_umbrella_v2.0_mazzocco.md` | 6390 | `EE1D83809E815AE2` |
| E.5 | `sessions/2026-05-04/ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/endorsement_template_umbrella_v2.0_garoufalidis.md` | 6463 | `749217E19E128448` |
| E.6 | `sessions/2026-05-04/ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/endorsement_template_ct_v1.3_zudilin.md` | 6850 | `DE550E6877098319` |
| E.7 | `sessions/2026-05-04/ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/endorsement_template_ct_v1.3_mazzocco.md` | 7035 | `CEB4A74566858014` |
| E.8 | `sessions/2026-05-04/ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/endorsement_template_ct_v1.3_garoufalidis.md` | 7037 | `A1048810E5934480` |
| E.9 | `sessions/2026-05-04/ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/endorsement_template_t2b_v3.0_zudilin.md` | 6238 | `55ADE990B8DF42CA` |
| E.10 | `sessions/2026-05-04/ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/endorsement_template_t2b_v3.0_mazzocco.md` | 6420 | `8B9EBFBA01380FBD` |
| E.11 | `sessions/2026-05-04/ARXIV-ENDORSEMENT-TEMPLATES-EXPAND/endorsement_template_t2b_v3.0_garoufalidis.md` | 6473 | `E99CA31BE7115351` |

[NOTE-078-A2-1] Total **14** existing endorsement-template files on disk
across both 2026-05-04 sessions (5 + 9). Three of those template-files
duplicate the same endorser-paper pair across both folders (CT v1.3 ×
Mazzocco / CT v1.3 × Garoufalidis / CT v1.3 × Zudilin), so the count of
unique (endorser, paper) pairs covered by an existing on-disk template
is **11**, not 14. The "14 templates" wording in spec §3.C.1 refers to
file count, not unique-pair count. Surfaced in `discrepancy_log.json`
as a non-blocking observational note D-078-1.

## §A.3 — 6 SIARC paper-source anchors

| # | Paper | Path (workspace-relative) | Bytes | SHA-256 (16) |
|---|---|---|---:|---|
| P1 | PCF-1 v1.3 (TeX) | `tex/submitted/p12_journal_main.tex` | 72311 | `82173A09521D6676` |
| P2 | PCF-2 v1.3 (TeX) | `tex/submitted/pcf2_program_statement.tex` | 75098 | `82FE2315CFDA2047` |
| P3 | CT v1.3 (TeX) | `siarc-relay-bridge/sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/channel_theory_outline.tex` | 70178 | `59C5352795F8D63D` |
| P4 | D2-NOTE v2.1 (TeX) | `siarc-relay-bridge/sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/d2_note_v2_1.tex` | 38311 | `840120E73534DA8E` |
| P5 | T2B v3.0 (TeX) | `tex/submitted/t2b_paper_draft_v5_withauthor.tex` | 28635 | `9BDD6A5D799BD8FE` |
| P6 | umbrella v2.0 (TeX) | `tex/submitted/umbrella_program_paper/main.tex` | 44935 | `612F732EBE2D8BAB` |

[NOTE-078-A3-1] Concept DOIs (per spec §1.A.1 + 077 portfolio-substrate
cross-check):

| Paper | Concept DOI | Notes |
|---|---|---|
| PCF-1 v1.3 | `10.5281/zenodo.19931635` | matches spec §1.A.1 |
| PCF-2 v1.3 | `10.5281/zenodo.19936297` | spec §1.A.1 cites `19941678`; **CT** concept DOI per 077 portfolio inventory; non-blocking; D-078-2 |
| CT v1.3 | `10.5281/zenodo.19941678` | spec §1.A.1 cites `19951330`; non-blocking; D-078-2 |
| D2-NOTE v2.1 | `10.5281/zenodo.19996689` | matches spec §1.A.1 |
| T2B v3.0 | `10.5281/zenodo.19783311` | spec §1.A.1 cites `19783312`; off by 1; non-blocking; D-078-2 |
| umbrella v2.0 | `10.5281/zenodo.19885549` | spec §1.A.1 cites `19965040` (this is the version DOI of an earlier release, not concept); non-blocking; D-078-2 |

## §A.4 — 077 in-flight reference substrate (read for endorsement-fit derivation)

| # | File | Bytes | SHA-256 (16) |
|---|---|---:|---|
| Q.1 | `sessions/2026-05-07/T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077/handoff.md` | 10171 | `B7C6D6AF9389094C` |
| Q.2 | `sessions/2026-05-07/T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077/portfolio_substrate_anchor_shas.md` | 7060 | `F832D6F28E3DD251` |
| Q.3 | `sessions/2026-05-07/T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077/paper_profile_pcf2_v13.md` | 4744 | `9C496D2C28D8EE72` |
| Q.4 | `sessions/2026-05-07/T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077/paper_profile_d2note_v21.md` | 5464 | `152DF76ABB4DDF14` |
| Q.5 | `sessions/2026-05-07/T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-078` paper_profile_t2b_v30.md (077-emitted) | 5671 | `127814EC95DB9D1E` |

## §A.5 — 2026-05-07 ~14:11 JST reverse-engineering analysis status

[NOTE-078-A5-1] Spec §0 GOAL + §1.A.1 reference a "2026-05-07 ~14:11 JST
reverse-engineering analysis of 5 endorser candidates (Mazzocco /
Garoufalidis / Costin / Sauzin / Beukers) producing 5×6 endorser-paper
matrix with reframing-distance tags (LIGHT/MEDIUM/HEAVY) and ideal paper
titles per endorser." On-disk file search returned no matching artefact;
spec §1.A.1 acknowledges residence "in chat transcript or session-state
plan.md ~14:15 JST snapshot." Spec §2.B.3 then provides the verbatim
recall table (Mazzocco | PCF-2 v1.3 | MEDIUM, etc.), which is treated
as the load-bearing substrate for the reframing-distance summary in 078
endorser profiles. ORAL-OR-TRANSCRIPT-ONLY status; not a halt;
surfaced in `discrepancy_log.json` D-078-3.

[NOTE-078-A5-2] Same status applies to "2026-05-07 portfolio-impact
assessment + endorsement-fit rubric" cited at spec PRIOR ANCHORS line.
On-disk search negative; not a halt; the 077 portfolio_inventory.md
cross-walk + the spec's verbatim §2.B.3 recall table provide the
operational substrate.

---

## §A.6 — Substrate-drift halt status

[NOTE-078-A6-1] **HALT_078_SUBSTRATE_DRIFT not triggered.** All on-disk
substrate files SHA-anchored above resolve cleanly at fire-time bridge
HEAD `49f3423`. The DOI mismatch surfaced in §A.3 is a known prompt-spec
draft artefact (the prompt-drafter labelled spec §1.A.1 DOIs as
"approximate; verify on-disk"); on-disk DOIs are authoritative and the
load-bearing record per §A.3 table.

End of substrate anchor file.
