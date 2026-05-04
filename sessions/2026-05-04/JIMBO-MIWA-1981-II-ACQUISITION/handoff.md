# Handoff — JIMBO-MIWA-1981-II-ACQUISITION

**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code) — Claude Opus 4.7
**Session duration:** ~75 minutes
**Status:** PARTIAL (acquisition NIA; transitive convention pin completed)

**Verdict:** `UPGRADE_JM81_NIA_ILL_RECOMMENDED_RIMS_KYOTO`
with sub-finding `BLMP_TRANSITIVE_READING_INDICATES_CT_4TUPLE_NOT_FROM_JM81_II_CORE_CONVENTION`
(provisional pending direct primary-source verification).

---

## What was accomplished

Probed seven OA acquisition routes (ScienceDirect/DOI, author institutional
pages, RIMS preprint archive, arXiv, ResearchGate, Internet Archive,
HathiTrust) for Jimbo M. & Miwa T., "Monodromy preserving deformation of
linear ordinary differential equations with rational coefficients. II",
Physica D 2 (1981) 407-448 (DOI 10.1016/0167-2789(81)90021-X). All routes
returned PAYWALL or NIA at probe time. Bibliographic identity confirmed
via three independent sources (Google Scholar; RIMS preprint listing
RIMS-327; BLMP 2024 ref [24]). In lieu of direct readback, performed a
transitive convention-pin via BLMP 2024 §4.1 (slot 08 in the literature
workspace), which cites JM81 II as ref [24] verbatim and faithfully
reproduces the JM81 II Lax-pair construction with explicit parameter
labeling. Wrote 10 AEAL claims, route_probe_log.md, and
convention_pin_phaseD.md. No HALT triggered; no discrepancy beyond two
unexpected-finds entries.

## Key numerical findings

- BLMP 2024 §4.1 (page 24-25) explicitly identifies the JM81 II Lax-pair
  convention for Painlevé-III(D6) as a 2-parameter family `(ϴ_0, ϴ_∞)`
  with map (verbatim BLMP eq 4.6): `ϴ_0 = α/4, ϴ_∞ = 1 - β/4`,
  where (α, β) are the standard PIII(D6) coefficients in the equation
  `d²u/dx² = (1/u)(du/dx)² - (1/x)(du/dx) + αu²/x + β/x + 4u³ - 4/u`.
- Symbol-family and cardinality both differ from the CT v1.3 §3.5
  4-tuple `(α_∞, α_0, β_∞, β_0) = (1/6, 0, 0, -1/2)`: JM81 II is
  ϴ-letter doubly-indexed (0, ∞) with cardinality 2; CT is α/β-letter
  doubly-(∞,0)-indexed with cardinality 4.
- The JM81 II 2-parameter `(ϴ_0, ϴ_∞)` labeling is structurally
  identical to the Okamoto 1987 W(B_2) `(θ_0, θ_∞)` labeling pinned
  in OKAMOTO-1987-CONSTRAINT-PIN (2026-05-04).
- BLMP ref [24] verbatim (slot 08, refs page): "Jimbo M., Miwa T.,
  Monodromy preserving deformation of linear ordinary differential
  equations with rational coefficients. II, Phys. D 2 (1981), 407-448."
  Confirmed via pypdf extraction of slot 08
  (SHA-256 96C49CDD51B6C2A395CCD6CC3CB66BFFEB623643B1A2374DB3F203760F696BB3,
  77 pages, 2,018,889 bytes).

## Judgment calls made

- **Transitive readback substituted for direct readback.** JM81 II
  acquisition NIA at all seven probed OA routes; rather than halt
  with "all OA routes fail" only, executed Phase D Section D.2-D.3
  using BLMP 2024 §4.1 (slot 08) as a faithful transitive source
  per Phase D.2 explicit cross-validation directive. This yields a
  provisional convention pin; flagged as provisional throughout
  (not "primary-source-grade").

- **Verdict-ladder mapping.** Spec ladder did not have a clean
  fit for "OA NIA + transitive reading rules out source"; chose
  `UPGRADE_JM81_NIA_ILL_RECOMMENDED_RIMS_KYOTO` (closest spec
  match) with explicit sub-finding annotation rather than fabricate
  a new ladder entry. Library recommendation: RIMS Kyoto Univ.
  (Miwa's home institution; likely has author copy or
  institutional-archive access).

- **G17 anchor paraphrase noted.** BLMP §4.1 actual wording is
  "Following Jimbo and Miwa [24]", not "after Jimbo-Miwa 1981 II"
  as recorded in the G17-LAYER-SEPARATION-LIT-ANCHOR Phase B.3
  anchor. Logged in unexpected_finds.json as a minor severity
  paraphrase correction; no impact on G17 conclusion.

## Anomalies and open questions

(MOST IMPORTANT SECTION.)

1. **Provisional convention-pin only.** The conclusion that CT v1.3
   §3.5's 4-tuple is NOT from JM81 II's core Lax-pair convention is
   based on BLMP 2024 §4.1 transitive reading. Direct verbatim
   verification from JM81 II §_LP / §_param requires ILL acquisition.
   Possible (low-probability) escape: JM81 II contains sub-cases or
   parameter expansions in §_LP that introduce additional labels
   (α_∞, α_0, β_∞, β_0) which BLMP's PIII(D6)-specific exposition
   does not surface. ILL recommended to close at primary-source level.

2. **Strategic implication for Prompt 025 (Sakai 2001).** With both
   Okamoto 1987 (per prior pin) and JM81 II (per this transitive pin)
   ruled out as sources of the CT 4-tuple, the residual canonical
   candidate is Sakai 2001 D_6 surface root-system convention.
   Prompt 025 (Sakai 2001 acquisition) becomes high-priority; its
   completion would either close the origin-of-CT-4-tuple question or
   surface a third candidate.

3. **HALT_JM81_DIRECT_DISAGREES_WITH_BLMP not triggered.** BLMP and
   JM81 II are internally consistent (BLMP cites JM81 II faithfully).
   The "disagreement" (if any) is between JM81 II + BLMP on one side
   and CT v1.3 §3.5 on the other side; this is not a literature
   inconsistency but an unidentified-source question for the CT 4-tuple.

4. **G14 ENDORSER-HANDLE follow-on.** No new endorser candidates
   surfaced in this task. The five Tier-1/Tier-2 candidates from
   ENDORSER-HANDLE-ACQUISITION (2026-05-04) remain the operating set.

5. **AEAL output_hash gap.** All 10 AEAL claims this session use
   `n/a-{bibliographic|network|text-extract|analytic}` for output_hash
   because the deliverables are bibliographic / quotation / web-fetch
   in nature, not numerical computations. Per Rule §A this is
   acceptable (output_hash is meaningful only for computation-typed
   evidence per the task spec); flagging here for synthesizer review
   in case a stricter convention is adopted.

## What would have been asked (if bidirectional)

1. Does the operator have institutional access to ScienceDirect via
   any affiliated library (e.g., Yokohama City Univ., a Tokyo Univ.
   visiting scholar program)? If yes, B.1 acquisition becomes
   immediately feasible without ILL.

2. Is there a CT v1.3 §3.5 internal author note or source citation
   that points to a specific paper for the (α_∞, α_0, β_∞, β_0)
   4-tuple choice? (Spec calls CT v1.3 §3.5 "read-only" but the
   in-text citation, if any, would short-circuit Prompt 025.)

3. Should Prompt 025 (Sakai 2001) be auto-queued as a follow-on
   given the strategic-implication elevation, or held until ILL
   for JM81 II returns to confirm/refute the transitive pin?

## Recommended next step

**ILL recommendation:** Submit ILL request via RIMS Kyoto Univ. (Miwa's
home institution; high probability of institutional copy or author copy
on file) for Jimbo & Miwa, Physica D 2 (1981) 407-448.
DOI 10.1016/0167-2789(81)90021-X. Backup library: Yokohama City Library
or Tokyo Univ. (operator-local). Per Rule 2, do NOT auto-submit; this
is operator-side work.

**Prompt-queue priority adjustment:** Elevate Prompt 025
(SAKAI-2001-ACQUISITION) to high-priority in the next round; its
completion is the most efficient path to closing the origin-of-CT-
4-tuple question if the JM81 II ILL is delayed.

**Picture v1.18 amendment (operator-side, if accepted):** §5 G18
follow-on row may note "BLMP 2024 §4.1 transitive reading rules out
JM81 II core Lax-pair convention as source of CT v1.3 §3.5 4-tuple
(provisional, pending RIMS Kyoto ILL); Sakai 2001 elevated to
residual canonical candidate."

## Files committed

- `prompt_spec_used.md` — relay prompt body archived (Phase 0)
- `route_probe_log.md` — Phase A bibliographic confirmation +
  Phase B per-route findings
- `blmp_scan.py` — pypdf scan script for BLMP 2024 slot 08
- `blmp_pages.py` — pypdf page-readback script (pages 24, 25, 26,
  refs page) for BLMP 2024 slot 08
- `blmp_scan.out.txt` — output of blmp_scan.py
- `blmp_pages.out.txt` — output of blmp_pages.py (verbatim §4.1
  + ref [24] extraction)
- `convention_pin_phaseD.md` — Phase D transitive convention-pin
  analysis with verbatim quotes (≤30 words each per Rule §D)
- `claims.jsonl` — 10 AEAL claims (1 Phase A + 4 Phase B + 3 Phase D
  literature_quotation + 2 Phase D analytic)
- `halt_log.json` — empty {} (no halt triggered)
- `discrepancy_log.json` — empty {} (no discrepancy)
- `unexpected_finds.json` — 2 entries (G17 anchor paraphrase
  correction + transitive convention-pin strategic implication)
- `handoff.md` — this file

## AEAL claim count

10 entries written to `claims.jsonl` this session.
  - 1 Phase A (bibliographic confirmation)
  - 1 Phase A (RIMS-327 deposit confirmation)
  - 1 Phase B (B.1 ScienceDirect paywall confirmation)
  - 1 Phase B (B.2-B.7 OA route fail summary)
  - 4 Phase D (literature_quotation): BLMP ref [24] verbatim;
    BLMP §4.1 attribution; BLMP eq (4.6) parameter map;
    BLMP eqs (4.7-4.8) formal-monodromy expansion
  - 2 Phase D (analytic): convention pin via BLMP transitive reading;
    cross-link to OKAMOTO-1987-CONSTRAINT-PIN

All claims have `evidence_type` ∈ {literature_citation,
deposit_confirmation, literature_quotation} per spec §3.
`reproducible: true` for all entries. `dps: null` (literature task,
no numerical precision parameter).
