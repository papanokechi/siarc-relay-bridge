# Intermediate Amendments — STEP A.4 cross-reference

This file enumerates commits in the bridge range
`70d1a48..05810a2` that are NOT independent verdict entries in the
27-entry catalog (`verdict_catalog.json`). Each is an intermediate
amendment / sub-commit subsumed by a parent verdict entry. No
independent verdict treatment is given here per relay 070 STEP A.4.

Also catalogued: V4 PARALLEL entries that PRE-DATE v1.19 deposit
commit `70d1a48` (2026-05-06 12:23 JST) and are therefore outside
the range — listed for completeness as "pre-range parallel residue".

---

## Range commits not in PRIMARY/PARALLEL/SECONDARY catalog

### 9c75f65 — T1-PHASE2-BASELINE-NOTE (relay 051 v1.0 substrate)
- Subject: "T1-PHASE2-BASELINE-NOTE -- draft 8pp Newton-polygon
  formal-level baseline note; 10 AEAL claims; PDF clean build"
- Touched: `sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/*`
  (annotated_bibliography.bib, bt_baseline_note.{log,pdf,tex},
  claims.jsonl, …)
- Parent verdict entry: V2.h (067 BT-BASELINE-NOTE-FOLLOWUP-V1-0)
  — V2.h is the additive follow-up to this v1.0 baseline note;
  this commit is the v1.0 substrate that v1.19 amendment log
  already references at §29.
- Cross-ref note: 051 v1.0 itself was NOT delta-D1..D5 of v1.19
  (those were 033/036/037/047); however v1.19 §28 §29 reference
  051 status and the LANE-2 cascade (V2.b..V2.h) is built on
  this 051 v1.0 substrate.

### c7a3c76 — T1-PHASE2-BASELINE-NOTE A11 Zenodo deposit confirmation
- Subject: "T1-PHASE2-BASELINE-NOTE -- 051 PUBLISHED on Zenodo
  (concept 10.5281/zenodo.20048196 + version
  10.5281/zenodo.20048197); A11 deposit-confirmation claim
  appended to claims.jsonl; zenodo_deposit_confirmation.md
  additive deposit-time-snapshot file added"
- Touched: `sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/{claims.jsonl,
  zenodo_deposit_confirmation.md}`
- Parent verdict entry: V2.h (067 BT-BASELINE-NOTE-FOLLOWUP-V1-0)
  — additive deposit-time-snapshot extension of 051 v1.0; V2.h's
  follow-up note builds on 051's Zenodo concept DOI.

### c105645 — T1-PHASE2-BASELINE-NOTE A12 byte-clean readback
- Subject: "T1-PHASE2-BASELINE-NOTE -- A12 byte-clean readback
  verification PASS (Zenodo PDF SHA-256 23022f0d..f0e5b7c
  bit-identical to local; 3-way match)"
- Touched: `sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/{claims.jsonl,
  zenodo_deposit_confirmation.md}`
- Parent verdict entry: V2.h (same chain as c7a3c76)

### 027d7ff — T1-PHASE2-BASELINE-NOTE operator-decision (b/c/d)
- Subject: "T1-PHASE2-BASELINE-NOTE -- (b) substrate
  cmb_oq_entries_w20_051.md (3 OQ entries Q1/Q2/Q4 for CMB.txt
  W20 paste); (c) OPT_C2 058S additive correction chosen by
  operator (no spec amendment fired); (d) LATE-FIRE post-W20
  picture v1.20 chosen by operator (substrate scope frozen)"
- Touched: `sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/cmb_oq_entries_w20_051.md`
- Parent verdict entry: V2.a (060 CMB-OQ-PASTE-W20-051-Q1Q2Q4-EXECUTION)
  — branch (b) substrate fed directly into V2.a paste execution
- Special role: operator-decision anchor cited by THIS preflight
  precondition P3 (LATE-FIRE post-W20 v1.20 decision)

### 7578f38 — CMB-OQ-PASTE-056-EXECUTION (relay 059; HALTED)
- Subject: "CMB-OQ-PASTE-056-EXECUTION -- HALT_059_POST_LINE_COUNT
  (spec arithmetic off-by-one); content placement CORRECT…"
- Touched: `sessions/2026-05-06/CMB-OQ-PASTE-056-EXECUTION/*`
- Parent verdict entry: V5.f / V5.g (056 048R-EARLY-FIRE-
  DECISION-SUBSTRATE) — 059 is the first (halted) paste-execution
  of the 056-substrate OQ-2026-05-06-048R-EARLY-FIRE entry.

### 9d70b4b — CMB-OQ-PASTE-056-EXECUTION OPT_A acceptance addendum
- Subject: "CMB-OQ-PASTE-056-EXECUTION -- OPT_A acceptance
  addendum (operator decision T0 2026-05-06 ~15:35 JST closing
  059 halt disposition); content placement bit-correct…"
- Touched: `sessions/2026-05-06/CMB-OQ-PASTE-056-EXECUTION/OPT_A_ACCEPTANCE.md`
- Parent verdict entry: V5.f / V5.g (closes 7578f38 halt
  disposition)

### c1b8c54 — PCF2-CF_VALUE-AUDIT-9IMPLS-065 handoff addendum
- Subject: "PCF2-CF_VALUE-AUDIT-9IMPLS-065 -- handoff.md
  addendum: A0 anomaly noting commit 6a150b6 shipped 065 +
  parallel 064 in same hash"
- Touched: `sessions/2026-05-06/PCF2-CF_VALUE-AUDIT-9IMPLS-065/handoff.md`,
  `sessions/2026-05-06/PHASE-A-DEG_A-ZERO-SUPPLEMENTARY-064/handoff.md`
- Parent verdict entry: V2.f (065 PCF2-CF_VALUE-AUDIT-9IMPLS) and
  V2.e (064 PHASE-A-DEG_A-ZERO-SUPPLEMENTARY) — explicitly notes
  that 6a150b6 carried both 064 + 065 deposits in the same hash

---

## Pre-range parallel residue (PARALLEL V4.* PRE-v1.19)

The following V4 entries pre-date `70d1a48` (v1.19 deposit
2026-05-06 12:23 JST) but were not absorbed at v1.19 fire-time
and remain pending. Listed for completeness; deeper details in
`verdict_catalog.json` and `parallel_session_synopses.md`.

| tag  | commit  | timestamp                  | session                                        |
|------|---------|----------------------------|------------------------------------------------|
| V4.a | fe15737 | Wed 2026-05-06 08:21 JST   | T2B-BZERO-OFFSET-LOG-SWEEP-REFIRE (044R)       |
| V4.b | 82001aa | Wed 2026-05-06 09:00 JST   | T2B-TIGHTENED-SWEEP-OUTCOME-B (044B)           |
| V4.c | 7509e34 | Wed 2026-05-06 IN-RANGE    | 055 N3-FOURTH-LAW-ARBITRATION-SUBSTRATE        |
| V4.d | 6bbd3f0 | Wed 2026-05-06 11:00 JST   | 048R W19-CLOSING-W20-WSB                        |
| V4.e | 5d83797 | Tue 2026-05-05 19:29 JST   | PCF-2-V2-BIPARTITION-PROMOTION (v3.0→v3.1)     |
| V4.f | 8e18465 | Tue 2026-05-05 18:39 JST   | T2B-BIPARTITION-B7-STRONG-NULL                  |

Note: V4.c (7509e34) is the only V4 entry IN range
(70d1a48..05810a2). Five V4 entries pre-date v1.19 deposit.

---

## Range commits coverage tally

`git log 70d1a48..05810a2` yields **24 commits**, partitioned as:

| Bin                                                 | Commits | Catalog entries |
|-----------------------------------------------------|--------:|----------------:|
| PRIMARY (V1.a..V3.a)                                |      12 |              13 |
|   V1.* (V1.a/b/c/d)                                 |       4 |               4 |
|   V2.* (V2.e + V2.f share commit 6a150b6)           |       7 |               8 |
|   V3.* (V3.a)                                       |       1 |               1 |
| PARALLEL (V4.c only — others pre-range)             |       1 |               1 |
| SECONDARY (V5.a, V5.c, V5.d, V5.f≡V5.g share)       |       4 |               5 |
| INTERMEDIATE AMENDMENTS                             |       7 |               — |
| **Total range commits**                             |  **24** |             **— ** |

Pre-range V5 commits (NOT counted above): V5.b `b24c236`,
V5.e `38c0256`, V5.h `1873538`. Pre-range V4 commits: V4.a
`fe15737`, V4.b `82001aa`, V4.d `6bbd3f0`, V4.e `5d83797`, V4.f
`8e18465`.
