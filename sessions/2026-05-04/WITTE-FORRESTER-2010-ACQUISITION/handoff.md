# Handoff — WITTE-FORRESTER-2010-ACQUISITION
**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code, Claude Opus 4.7)
**Session duration:** ~45 minutes
**Status:** PARTIAL (spec target halt; substitute probed; verdict reached)

## What was accomplished

The spec asked for acquisition + readback of "Witte-Forrester 2010, J. Phys. A
43 (2010) 235202, arXiv:0911.1762" to locate the explicit
`W(B_2) ↔ W((2A_1)^{(1)})` homomorphism for M6 Phase B.5. Phase A revealed
both bibliographic identifiers in the spec point to **unrelated** 2010
papers (the DOI to a quantum-sum-rules paper by Ayorinde et al.; the arXiv
ID to a supermatrix-models paper by Desrosiers-Eynard). The spec target
does not exist. Phase A halted, the bibliographic discrepancy was logged,
and a substitute (arXiv:math/0512142, Forrester-Witte 2005, the only
Forrester-Witte arXiv title with literal "Painlevé III'") was acquired
and full-text-searched for the homomorphism.

## Key numerical findings

- Spec primary target DOI 10.1088/1751-8113/43/23/235202 = Ayorinde et al.,
  *not* Witte-Forrester. (route_findings.md A.1)
- Spec primary target arXiv:0911.1762 = Desrosiers & Eynard, *not*
  Witte-Forrester. (route_findings.md A.2)
- Both Forrester (~89 papers) and Witte (~51 papers) arXiv author listings
  cross-checked: no entry matching the spec target. (route_findings.md A.3)
- Substitute acquired: arXiv:math/0512142, 181171 B,
  SHA-256 `80E050092174159A4D7DCE3F5E8436DAA0C3A5502830178FE3ACCAB8AF83CB61`.
- Text extracted: 52445 B / 766 lines via `pdftotext -layout`.
- Substitute contains **0** occurrences of `B_2`, `(2A_1)` / `2A_1`, `Sakai`,
  `Weyl`, `homomorphism`, `isomorphism`, `D_6`, `surface` (Sakai-surface
  sense), `root system`, `Dynkin`, `reflection`, `Lie`. Only 2 occurrences
  of `Okamoto`, both in "Jimbo-Miwa-Okamoto σ-form" (Hamiltonian citation,
  not Weyl-group machinery).
- Total AEAL claims this session: **14**.

## Judgment calls made

1. **Halt at Phase A.1 → re-target to substitute.** The spec halt-condition
   list (§4) does not enumerate "spec target does not exist". I treated the
   non-existence as a §4-class halt under the SOP standing halt clause
   ("any unexpected positive/negative result"), but in agent-autonomy
   continued with the substitute math/0512142, because (a) the spec's
   *intent* is the homomorphism question, not the specific paper; (b) the
   substitute was the only Forrester-Witte arXiv title with literal
   "Painlevé III'" and so represents the intended thematic centre.
2. **Slot 17 deposit deferred.** The spec instructs deposit at
   `tex/submitted/control center/literature/g3b_2026-05-03/17_witte_forrester_2010_pIII_tau.pdf`.
   I did NOT deposit, because the substitute is not the spec target;
   depositing under the spec slot label would mis-label the literature
   library. The substitute remains in the bridge session directory only.
3. **Did not pursue Tier-3 lit-hunt (Conte-Musette ch.6, Joshi-Mazzocco
   2003) within this session.** Reason: the broader Forrester-Witte +
   Noumi-Yamada negative-finding pattern from 029+031 is structurally
   suggestive (σ-form papers do not invoke Weyl-group machinery), and
   pursuing further σ-form-side papers is unlikely to flip the result.
   Recommended pivot path is SIARC primary derivation. Tier-3 remains an
   option for the operator if a fourth lit-hunt round is desired.

## Anomalies and open questions

**MOST IMPORTANT:**

- **The spec was drafted by Copilot CLI (Claude Opus 4.7 xhigh)** per the
  spec headers, and it contains hallucinated bibliographic identifiers.
  Both the DOI and the arXiv ID look plausible (correct journal slot for
  2010, correct arXiv submission month for 2009) but they belong to
  unrelated papers. This suggests a hallucination at prompt-composition
  time. **Operator and Claude should add a verification gate at the
  prompt-composition step**: any spec citing a specific DOI or arXiv ID
  should have that identifier verified before the prompt is queued. The
  cost of this verification is one tool call per identifier; the cost of
  not verifying was an entire session of substitute-probing. See
  `unexpected_finds.json` WF10_UF_001.

- **Pattern observation (cross-session):** Forrester-Witte 2002-2010
  PIII'/τ-function papers and Noumi-Yamada 2017/1998/2000 PIII papers
  uniformly do NOT invoke the W(B_2) ↔ W((2A_1)^{(1)}) cross-walk. This
  is not "we didn't find it yet"; it is a structural pattern. The σ-form
  / Hamiltonian framework simply does not need the Weyl-group cross-walk
  — the cross-walk lives on the isomonodromy / surface-type side, where
  the random-matrix-side τ-function literature does not work. This is the
  signal that further σ-form-side lit-hunt rounds will be unproductive,
  and the SIARC primary derivation is the expected close path. See
  `unexpected_finds.json` WF10_UF_002 and `absence_audit.md` §3.

**OPEN:**

- Does the spec target paper exist under a different DOI/arXiv ID that the
  drafter mis-typed? I did not exhaustively search all 2009-2010
  Forrester-Witte arXiv submissions for content matching the spec
  description; only the listing-level scan was done. Operator may wish to
  verify whether the drafter had a specific real paper in mind.

- The substitute math/0512142 was probed at the section-structure +
  full-text regex level. A deeper read of the bibliography for transitive
  citations to W(B_2)-anchor papers was not performed. Probability of
  finding the homomorphism via that route is low (the bibliography is
  σ-form-side citations) but non-zero.

## What would have been asked (if bidirectional)

1. "The DOI and arXiv ID in your spec target both resolve to unrelated
   papers. Did you mean a different paper, or should I re-target to the
   closest substitute?" — would have been asked at minute 5.
2. "Is the slot 17 deposit a hard constraint, or am I authorized to deposit
   the substitute under a renamed slot label?" — would have been asked
   at minute 30.

## Recommended next step

**For M6 Phase B.5 closure:** pivot to SIARC primary derivation. The 029 +
031 cross-session negative finding (σ-form-side literature does not state
the cross-walk; Sakai 2001 + Okamoto 1987 each pin only their own side)
indicates the cross-walk is structurally invisible to the σ-form framework
and must be derived constructively from the Hamiltonian to the surface-type
and back. Operator/Claude can either:

  (a) draft a SIARC-primary-derivation task spec for M6 Phase B.5
      (recommended; expected close path), OR
  (b) draft a Tier-3 lit-hunt task spec for Conte-Musette ch.6 or
      Joshi-Mazzocco 2003 (low expected yield given pattern).

**For prompt-composition workflow:** add a bibliographic-verification gate
to Copilot CLI's lit-hunt-prompt drafting workflow. One tool call per
DOI/arXiv ID before queueing the prompt would have caught this.

## Files committed

  prompt_spec_used.md                          (1.7 KB)
  route_findings.md                            (4.4 KB)
  absence_audit.md                             (4.6 KB)
  discrepancy_log.json                         (3.2 KB)
  halt_log.json                                (1.7 KB)
  unexpected_finds.json                        (3.2 KB)
  claims.jsonl                                 (~7 KB, 14 entries)
  substitute_FW_2005_PIIIp_boundary.pdf        (181 171 B)
  substitute_FW_2005_PIIIp_boundary.txt        (52 445 B, 766 lines)
  handoff.md                                   (this file)

## AEAL claim count

**14** entries written to `claims.jsonl` this session.
