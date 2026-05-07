# Endorser × Paper Coverage Matrix [COVERAGE-MATRIX] — 078

**Session:** T2-ENDORSER-FRAMING-DOSSIER-ASSEMBLY-078
**Compiled:** 2026-05-07
**Substrate anchors:** see `endorser_substrate_anchor_shas.md` §A.1 + §A.2 + §A.3.
**Spec reference:** §3 ENDORSER × PAPER COVERAGE MATRIX.

[NOTE-078-MATRIX-1] **Axis-count clarification.** Spec §0 GOAL enumerates
5 endorser candidates "(Mazzocco / Garoufalidis / Costin / Sauzin /
Beukers)" while spec §3.C.1 says "5 endorsers x 6 papers = 30 cells"
and footnotes "SKIP-DECLINED (Zudilin x PCF-1 v1.3 specifically)".
Spec §9 D1 separately demands an `endorser_profile_zudilin.md` file.
Reading: the matrix axis includes Zudilin as a 6th historical row for
completeness (Zudilin already has 4 unique on-disk template files
covering 4 of 6 papers including PCF-1; the Zudilin row is needed to
record those EXISTING-TEMPLATE cells faithfully). The "5 endorsers"
phrasing of spec §0 refers to the **5 active candidates** of the
2026-05-07 reverse-engineering analysis (the 5 reframing-distance
table rows of spec §2.B.3); Zudilin is HISTORICAL-ANCHOR in this
session. Surfaced in `discrepancy_log.json` D-078-4 as non-blocking
spec ambiguity. Below the matrix is rendered 6 × 6 = 36 cells with
the Zudilin row tagged HISTORICAL-ANCHOR; spec §3.C.2 aggregate
counts target the 5 active rows = 30 cells.

---

## §C.1 — 6 × 6 cell matrix (Zudilin row HISTORICAL-ANCHOR)

| endorser ↓ \\ paper → | PCF-1 v1.3 | PCF-2 v1.3 | CT v1.3 | D2-NOTE v2.1 | T2B v3.0 | umbrella v2.0 |
|---|---|---|---|---|---|---|
| **Zudilin** (historical) | EXISTING-TEMPLATE-ON-DISK + SKIP-DECLINED | SKIP-DECLINED-INHERIT | EXISTING-TEMPLATE-ON-DISK | SKIP-FIT-WEAK | EXISTING-TEMPLATE-ON-DISK | EXISTING-TEMPLATE-ON-DISK |
| **Mazzocco** | SKIP-FIT-WEAK | GAP-CANDIDATE-MEDIUM | EXISTING-TEMPLATE-ON-DISK | SKIP-FIT-WEAK | EXISTING-TEMPLATE-ON-DISK | EXISTING-TEMPLATE-ON-DISK |
| **Garoufalidis** | EXISTING-TEMPLATE-ON-DISK | GAP-CANDIDATE-LIGHT | EXISTING-TEMPLATE-ON-DISK | SKIP-FIT-WEAK | EXISTING-TEMPLATE-ON-DISK | EXISTING-TEMPLATE-ON-DISK |
| **Costin** | SKIP-FIT-WEAK | SKIP-FIT-WEAK | SKIP-FIT-WEAK | GAP-CANDIDATE-MEDIUM | SKIP-FIT-WEAK | SKIP-FIT-WEAK |
| **Sauzin** | SKIP-FIT-WEAK | SKIP-FIT-WEAK | SKIP-FIT-WEAK | GAP-CANDIDATE-LIGHT-MEDIUM | SKIP-FIT-WEAK | SKIP-FIT-WEAK |
| **Beukers** | SKIP-FIT-WEAK | SKIP-FIT-WEAK | SKIP-FIT-WEAK | SKIP-FIT-WEAK | GAP-CANDIDATE-MEDIUM | SKIP-FIT-WEAK |

Tag legend (per spec §3.C.1):
- **EXISTING-TEMPLATE-ON-DISK**: at least one populated template file on
  disk in either 2026-05-04 ENDORSER-HANDLE-ACQUISITION or
  ARXIV-ENDORSEMENT-TEMPLATES-EXPAND folder.
- **GAP-CANDIDATE-LIGHT** / **GAP-CANDIDATE-LIGHT-MEDIUM** /
  **GAP-CANDIDATE-MEDIUM**: no template; reframing distance per spec
  §2.B.3 (verbatim recall) labels the agent-draft effort.
- **SKIP-FIT-WEAK**: per 2026-05-07 endorsement-fit assessment +
  2026-05-04 subject_fit_matrix.md L grade ⇔ skip discipline.
- **SKIP-DECLINED** / **SKIP-DECLINED-INHERIT**: Zudilin × PCF-1
  decline 2026-05-04 ~18:38 JST (spec §3.C.1 SKIP-DECLINED note);
  PCF-2 v1.3 inherits the math.NT decline under arXiv's
  single-endorsement-per-category rule per
  `endorsement_request_record2_PCF1_zudilin.md` L141-145 verbatim
  (≤ 30 words):
  > "arXiv only requires **one** endorsement per category … AND
  > covers the PCF-2 v1.3 (record #5) follow-up math.NT submission."

---

## §C.2 — Per-row coverage tally (5 active rows + 1 historical)

| endorser | EXISTING | GAP-LIGHT/LIGHT-MEDIUM | GAP-MEDIUM | SKIP-FIT-WEAK | SKIP-DECLINED |
|---|---:|---:|---:|---:|---:|
| Zudilin (historical) | 4 | 0 | 0 | 1 | 1+1 |
| Mazzocco | 3 | 0 | 1 | 2 | 0 |
| Garoufalidis | 4 | 1 | 0 | 1 | 0 |
| Costin | 0 | 0 | 1 | 5 | 0 |
| Sauzin | 0 | 1 | 0 | 5 | 0 |
| Beukers | 0 | 0 | 1 | 5 | 0 |
| **TOTAL (6 rows)** | **11** | **2** | **3** | **19** | **2** |
| **TOTAL (5 active rows)** | **7** | **2** | **3** | **18** | **0** |

Spec §3.C.2 aggregate-count expectations (5 × 6 = 30):
- "Total EXISTING-TEMPLATE: expected 14" — observed 11 unique pairs (5
  active rows: 7). The "14" figure refers to **file count** not
  unique-pair count; CT v1.3 has 6 files on disk for 3 unique pairs
  (Zudilin / Mazzocco / Garoufalidis duplicated across 034 + 037
  folders). Surfaced in `discrepancy_log.json` D-078-1 as a non-blocking
  observational note. The 5-active-row total of 7 EXISTING pairs is
  consistent with the 14-file count when duplicates are collapsed and
  Zudilin row is excluded.
- "Total GAP-CANDIDATE: expected 6-8" — observed 5 (5 active rows)
  matching spec §4.D.3 expected gap-template enumeration:
  PCF-2×Mazzocco + PCF-2×Garoufalidis (optional D13) + D2-NOTE×Sauzin
  + D2-NOTE×Costin + T2B×Beukers. Within 6-8 spec range when D13 is
  counted; lower bound under-shot by 1 (5 < 6) under conservative
  draft-discipline. Surfaced in D-078-5 as expected-vs-observed note.
- "Total SKIP: expected 8-10" — observed 18 (5 active rows). Larger
  than expected because the 5 active rows fan out across 6 papers
  with most off-axis pairs SKIP-FIT-WEAK; the spec's "8-10" range
  appears to count only SKIP-DECLINED + SKIP-NEAR-MISS rather than
  the full SKIP-FIT-WEAK fan-out. Surfaced in D-078-5.

---

## §C.3 — Cell-by-cell rationale

### Zudilin row (HISTORICAL-ANCHOR)

- **(Zudilin, PCF-1 v1.3)** — EXISTING-TEMPLATE-ON-DISK
  (`endorsement_request_record2_PCF1_zudilin.md`, SHA `6B95796D...`)
  AND **SKIP-DECLINED** per Zudilin's 2026-05-04 ~18:38 JST decline
  (memory `endorsement workflow`).
- **(Zudilin, PCF-2 v1.3)** — SKIP-DECLINED-INHERIT. No on-disk
  template. PCF-2 v1.3 inherits PCF-1 math.NT endorsement under
  arXiv's single-endorsement-per-category rule; the same decline
  scope question applies. Conservative reading: do not re-pursue.
- **(Zudilin, CT v1.3)** — EXISTING-TEMPLATE-ON-DISK (2 files;
  `endorsement_request_record4_CT_zudilin.md` SHA `9F7F7C20...`
  + `endorsement_template_ct_v1.3_zudilin.md` SHA `DE550E68...`).
- **(Zudilin, D2-NOTE v2.1)** — SKIP-FIT-WEAK. D2-NOTE primary
  category math.CA / math-ph; Zudilin math.NT primary; 2026-05-07
  reverse-engineering analysis (spec §2.B.3) does NOT enumerate
  Zudilin × D2-NOTE as ideal-paper pairing; defer to Mazzocco /
  Sauzin / Costin axis.
- **(Zudilin, T2B v3.0)** — EXISTING-TEMPLATE-ON-DISK
  (`endorsement_template_t2b_v3.0_zudilin.md` SHA `55ADE990...`).
- **(Zudilin, umbrella v2.0)** — EXISTING-TEMPLATE-ON-DISK
  (`endorsement_template_umbrella_v2.0_zudilin.md` SHA `AF420EA4...`).

### Mazzocco row

- **(Mazzocco, PCF-1 v1.3)** — SKIP-FIT-WEAK. PCF-1 v1.3 primary
  math.NT; Mazzocco math.CA / math-ph primary; 2026-05-07 reverse
  engineering paired Mazzocco with PCF-2 v1.3 (Painlevé-D6
  Trans-stratum framing) per spec §2.B.3.
- **(Mazzocco, PCF-2 v1.3)** — **GAP-CANDIDATE-MEDIUM**. Per spec
  §4.D.3 first item; "Painlevé-D6 Trans-stratum framing; concrete
  L=12/π result" reframing axis. Drafted in Phase D as
  `endorsement_request_pcf2_mazzocco.md`.
- **(Mazzocco, CT v1.3)** — EXISTING-TEMPLATE-ON-DISK (2 files;
  `endorsement_request_record4_CT_mazzocco.md` SHA `FC0358D4...`
  + `endorsement_template_ct_v1.3_mazzocco.md` SHA `CEB4A745...`).
- **(Mazzocco, D2-NOTE v2.1)** — SKIP-FIT-WEAK by reverse-engineering
  pairing. Subject-fit moderate (D2-NOTE math.CA primary; Mazzocco
  math.CA / math-ph) but spec §2.B.3 reverse-engineering paired
  D2-NOTE with Sauzin / Costin not Mazzocco; defer to those axes.
  Optional follow-up if Sauzin + Costin both decline.
- **(Mazzocco, T2B v3.0)** — EXISTING-TEMPLATE-ON-DISK
  (`endorsement_template_t2b_v3.0_mazzocco.md` SHA `8B9EBFBA...`).
- **(Mazzocco, umbrella v2.0)** — EXISTING-TEMPLATE-ON-DISK
  (`endorsement_template_umbrella_v2.0_mazzocco.md` SHA `EE1D8380...`).

### Garoufalidis row

- **(Garoufalidis, PCF-1 v1.3)** — EXISTING-TEMPLATE-ON-DISK
  (`endorsement_request_record2_PCF1_garoufalidis.md` SHA `44446F64...`).
  CURRENT PIVOT in flight per spec §2.B.2 + memory todo
  `garoufalidis-endorsement-pivot pending`.
- **(Garoufalidis, PCF-2 v1.3)** — **GAP-CANDIDATE-LIGHT**. Per spec
  §4.D.3 second item; "subject-fit cross-check; share template w/
  PCF-1 footnote" — optional D13 deliverable. LIGHT because PCF-2 is
  the cubic extension of PCF-1; reframing-distance is footnote-only.
- **(Garoufalidis, CT v1.3)** — EXISTING-TEMPLATE-ON-DISK (2 files;
  `endorsement_request_record4_CT_garoufalidis.md` SHA `59A6747F...`
  + `endorsement_template_ct_v1.3_garoufalidis.md` SHA `A1048810...`).
- **(Garoufalidis, D2-NOTE v2.1)** — SKIP-FIT-WEAK. Subject-fit
  moderate via Garoufalidis-Costin resurgence axis but spec §2.B.3
  did not pair Garoufalidis × D2-NOTE; defer to Sauzin / Costin.
- **(Garoufalidis, T2B v3.0)** — EXISTING-TEMPLATE-ON-DISK
  (`endorsement_template_t2b_v3.0_garoufalidis.md` SHA `E99CA31B...`).
- **(Garoufalidis, umbrella v2.0)** — EXISTING-TEMPLATE-ON-DISK
  (`endorsement_template_umbrella_v2.0_garoufalidis.md` SHA `749217E1...`).

### Costin row (HANDLE_404)

- **(Costin, PCF-1 v1.3)** — SKIP-FIT-WEAK. Costin math.CA / math.AP
  primary; PCF-1 math.NT primary. Fit weak per 2026-05-04 dossier
  (Costin paired with record #4 / CT v1.3; not PCF-1).
- **(Costin, PCF-2 v1.3)** — SKIP-FIT-WEAK. Same rationale as PCF-1.
- **(Costin, CT v1.3)** — SKIP-FIT-WEAK *for this session*. Subject-fit
  is HIGH (CT v1.3 cites Costin) but the 2026-05-07 reverse-engineering
  pivot moved Costin from CT to D2-NOTE based on D2-NOTE's stronger
  Borel-Laplace + connection-problem alignment. Costin × CT remains a
  viable fallback if D2-NOTE Costin template fails.
- **(Costin, D2-NOTE v2.1)** — **GAP-CANDIDATE-MEDIUM**. Per spec
  §4.D.3 fourth item; "connection-problem framing; generalized
  Borel-Laplace" reframing axis. Drafted in Phase D as
  `endorsement_request_d2note_costin.md` with HANDLE_404 placeholder.
- **(Costin, T2B v3.0)** — SKIP-FIT-WEAK. T2B math.HO / math.NT
  cross-list; Costin math.CA / math.AP. No reverse-engineering pairing.
- **(Costin, umbrella v2.0)** — SKIP-FIT-WEAK. umbrella math.HO; not
  paired by §2.B.3.

### Sauzin row (HANDLE_404)

- **(Sauzin, PCF-1 v1.3)** — SKIP-FIT-WEAK. Sauzin math.CA / math-ph;
  PCF-1 math.NT primary.
- **(Sauzin, PCF-2 v1.3)** — SKIP-FIT-WEAK. Same.
- **(Sauzin, CT v1.3)** — SKIP-FIT-WEAK *for this session*. Subject-fit
  is HIGH (CT v1.3 cites Sauzin via Mitschi-Sauzin) but reverse-
  engineering moved Sauzin to D2-NOTE per spec §2.B.3. Costin × CT
  fallback applies symmetrically.
- **(Sauzin, D2-NOTE v2.1)** — **GAP-CANDIDATE-LIGHT-MEDIUM**. Per
  spec §4.D.3 third item; "Écalle-resurgence terminology; BT 1933
  substrate" reframing axis. Drafted in Phase D as
  `endorsement_request_d2note_sauzin.md` with HANDLE_404 placeholder.
  LIGHT-MEDIUM because Sauzin's mould-calculus / divergent-series
  framework already encodes the BT 1933 substrate D2-NOTE leans on.
- **(Sauzin, T2B v3.0)** — SKIP-FIT-WEAK.
- **(Sauzin, umbrella v2.0)** — SKIP-FIT-WEAK.

### Beukers row (HANDLE_404 + emeritus eligibility gate)

- **(Beukers, PCF-1 v1.3)** — SKIP-FIT-WEAK. Subject-fit MODERATE
  (Beukers math.NT transcendence theory adjacency) but spec §2.B.3
  pairs Beukers × T2B v3.0 (and PCF-1 by overlap); §4.D.3 expected
  gap-template list does NOT enumerate (Beukers, PCF-1 v1.3) as a
  gap-candidate. PCF-1 v1.3 already covered by Garoufalidis pivot.
- **(Beukers, PCF-2 v1.3)** — SKIP-FIT-WEAK.
- **(Beukers, CT v1.3)** — SKIP-FIT-WEAK.
- **(Beukers, D2-NOTE v2.1)** — SKIP-FIT-WEAK. D2-NOTE primary
  math.CA; Beukers math.NT primary.
- **(Beukers, T2B v3.0)** — **GAP-CANDIDATE-MEDIUM**. Per spec §4.D.3
  fifth item; "Apéry-tradition; irrationality-measure framing"
  reframing axis. Drafted in Phase D as
  `endorsement_request_t2b_beukers.md` with HANDLE_404 placeholder
  and emeritus-eligibility note.
- **(Beukers, umbrella v2.0)** — SKIP-FIT-WEAK.

---

## §C.4 — Phase D drafting outputs cross-reference

The 5 GAP-CANDIDATE cells flagged above produce these gap-templates in
Phase D (per spec §4.D.3 enumeration):

| # | (endorser, paper) | Reframing distance | Output file |
|---|---|---|---|
| G1 | (Mazzocco, PCF-2 v1.3) | MEDIUM | `endorsement_request_pcf2_mazzocco.md` |
| G2 | (Garoufalidis, PCF-2 v1.3) | LIGHT | `endorsement_request_pcf2_garoufalidis.md` (optional D13) |
| G3 | (Sauzin, D2-NOTE v2.1) | LIGHT-MEDIUM | `endorsement_request_d2note_sauzin.md` |
| G4 | (Costin, D2-NOTE v2.1) | MEDIUM | `endorsement_request_d2note_costin.md` |
| G5 | (Beukers, T2B v3.0) | MEDIUM | `endorsement_request_t2b_beukers.md` |

Total gap-templates drafted in 078: **5** (including optional D13;
within spec §10 budget 4-7 for `DOSSIER_COMPLETE`; under spec §8
HALT_078_GAP_TEMPLATE_BUDGET ceiling 8).

End of coverage matrix.
