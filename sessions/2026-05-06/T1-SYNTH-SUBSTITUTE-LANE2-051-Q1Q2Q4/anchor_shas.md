# Anchor SHAs — STEP 1 source inventory

**Computed:** 2026-05-06 (W19, Wed) JST  
**Tool:** PowerShell `Get-FileHash -Algorithm SHA256` (read-only).  
**Reviewer:** Copilot Researcher Agent (canonical T1-Synth-substitute LANE-2).

| # | Anchor | Bytes | SHA-256 |
|---|--------|-------|---------|
| A1 | sessions/2026-05-06/SYNTH-SUBSTITUTE-W19-051-Q1Q2Q4-VERDICT/synth_substitute_verdict.md | 23262 | `AE5CC42A01B2AD0F934891FF269FF919C0935B4EE3A778EEA608B70A5798041F` |
| A2 | sessions/2026-05-06/SYNTH-SUBSTITUTE-W19-051-Q1Q2Q4-VERDICT/rubber_duck_critique.md | 8085 | `78E12D89BF9366B5D8D54CE76FF508431D0128E5EAE8657A4F5910A79E1265DC` |
| A3 | sessions/2026-05-06/SYNTH-SUBSTITUTE-W19-051-Q1Q2Q4-VERDICT/claims.jsonl | 5198 | `5DC1AFFD4C888978466D68DD738A1F3CBDA27A0BCFA9BE490BD60851E39C93A9` |
| A4 | sessions/2026-05-06/SYNTH-SUBSTITUTE-W19-051-Q1Q2Q4-VERDICT/handoff.md | 10765 | `5D006EA8E48883753E85DEC6BE308859385B42F66B47BBF48F112678BB23255C` |
| A5 | sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/bt_baseline_note.tex | 38023 | `6746692C517DC25238473E819527C5682465CDC9E1DEF69D1F6DF31C1014D51B` |
| A6 | tex/submitted/pcf2_program_statement.tex | 75098 | `82FE2315CFDA2047249D4978D7AE487C21D9BE16A35F15827CE132561F2C8541` |
| A7 | tex/submitted/p12_journal_main.tex | 72311 | `82173A09521D6676ADC523E1D55CD1310F693479608A9F98EB980689A4786853` |
| A8 | pcf-research/pcf2/session_C1_2026-05-01/session_c1_wkb.py | 22982 | `2D43BFD55E0DB5848B83CAE5F24A0D7151E69C6A07B5A7D2A37C67B92CAFEF0D` |
| A9 | tex/submitted/CMB.txt (post-060-paste) | 89246 | `4EC61E120C2C569285CBE551B8EEF9ED3DF1FB1F869706A518E2B928170F3C82` |

## P4 verification

A9 SHA-256 prefix `4EC61E12...3C82` matches relay 060 expected post-paste SHA verbatim.
File size 89246 B matches relay 060 commit message verbatim. Line count = 1969 LF
characters + 1 final non-newline-terminated line = 1970 lines (matches relay 060
expected). HALT_061_CMB_PASTE_DRIFT does NOT trigger.

## Read-only invariant

All anchors A1-A9 inspected via `Get-FileHash` only. No anchor was modified during
this session. Re-inspection at handoff time MUST yield identical SHA-256 values.
