# SIARC RELAY PROMPT SPEC — QS-2

**TASK ID:**            `D2-NOTE-V2-1-WASOW-FULL-CLOSURE`
**PROMPT FAMILY:**      QS-2 (synthesizer-arbitrated; merged with retired Prompt 7 / Wasow Q20 full-closure)
**STATUS:**             DRAFT — synthesizer-side draft, NOT YET FIRED
**COMPOSED:**           2026-05-03 (post-QS-A acquisition of B-T 1933 / Acta 60)
**DRAFTED-BY:**         Copilot CLI (Claude Opus 4.7 xhigh) — synthesizer-side prompt drafting
**EXPECTED RUNTIME:**   ~4–6 hr agent (literature reading: ~1.5 hr; Newton-polygon Lemma derivation:
                        ~45 min; Phase E ~10pp LaTeX rewrite + 4-pass build: ~2 hr; verification + handoff: ~30 min)
**DEPENDENCIES:**       QS-A (B-T 1933 acquisition) — ✅ DONE 2026-05-03 (slot 03 at
                        `tex/submitted/control center/literature/g3b_2026-05-03/03_birkhoff_trjitzinsky_1933_acta60.pdf`,
                        SHA-256 `dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`,
                        89 pp, §§4–6 verified). Operator `g3b-acquire-bt-1933` SQL todo flipped to **done**.
**PARALLEL-SAFE WITH:** any task NOT modifying `siarc-relay-bridge/sessions/2026-05-03/Q20A-PHASE-C-RESUME/d2_note_v2/`
                        or the runbook-canonical literature directory.
**MERGES:**             retired Prompt 7 / `wasow-q20-full-closure-fire` (Q-S3 ruling). On a
                        non-`HALT_*` outcome of this task, the SQL todo
                        `prompt-7-wasow-q20-full-closure-fire` retires automatically; the
                        Wasow synthesizer-arbitration verdict that Prompt 7 would have produced
                        is the verdict produced by **Phase D** of this task.

---

## How to fire

The relay-prompt body below (between the `=====` rules) is what the operator pastes into
a fresh Copilot CLI session in the `claude-chat` workspace, at the next compute window
after operator inspection. The agent will then execute Phase A → Phase F and write the
deliverables to `siarc-relay-bridge/sessions/<TODAY>/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/`
(distinct from this synthesizer-draft directory; the live session is opened on whatever
`<TODAY>` is at firing time, even if that crosses midnight).

This synthesizer-draft directory (the one you are reading) holds:

- `prompt_spec.md` — this document (the spec the operator inspects)
- `handoff.md`     — the synthesizer-side handoff for Claude review (NOT the relay handoff)

The relay-execution session will create its own handoff, claims, and v2.1 PDF at
`<TODAY>/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/` at fire time.

---

## Synthesizer rulings embedded in this spec

| Ruling | Source | Effect on this prompt |
|--------|--------|-----------------------|
| **Q-S1** | picture v1.14 §24 | Theorem 4.1 retains its `\begin{theorem}` framing (NOT demoted to conjecture); Phase E adds the explicit citation chain (B-T 1933 §§4–6 OR Loday-Richaud 2016 ch. 2 OR Costin 2008 ch. 5) for the Borel-summability step that the v2 bib note admitted as missing; the proof body explicitly bridges Wasow §19's sectorial-asymptotic existence to the Borel-singularity-radius statement. **Rev-C(b) (demote-to-conjecture) is NOT applied.** |
| **Q-S2** | picture v1.14 §24 | Path A (revise-first) — the deliverable is **v2.1**, deposited as a NEW VERSION on the existing concept DOI `10.5281/zenodo.19996689`. NOT v3, NOT a supersede. NOT a fresh concept DOI. Build is clean across `pdflatex` passes 1, 2, 3 (with `bibtex` after pass 1). |
| **Q-S3** | picture v1.14 §24 | Prompt 7 (Wasow Q20 full-closure) is MERGED into this task. Phase C absorbs prompt 7's Wasow goal; Phase D produces the Wasow synthesizer-arbitration verdict. Single relay session produces both v2.1 PDF + the Wasow Q20 closure verdict. |
| **Q-S4** | picture v1.14 §24 | Picture v1.14 already pushed; this prompt assumes v1.14 framing. No further synthesizer-side picture amendment is required by THIS prompt's verdict (a future synthesizer pass absorbs THIS task's outcome into picture v1.15). |

| Revision | Origin | Action in Phase E |
|----------|--------|-------------------|
| **Rev-A** | Reviewer convergent finding (F1; all 5 reviewers C3 ≤ 4) | Cite B-T 1933 §§4–6 (PRIMARY; REQUIRED) for Borel-summability step in §3 (Wasow subsection) and in the proof of Theorem 4.1; add the corresponding `.bib` entry to `annotated_bibliography.bib`. Loday-Richaud 2016 ch. 2 + Costin 2008 ch. 5 are SECONDARY/TERTIARY but ETHICS-GATED (Phase C.4): cite "see also" only IF the agent has opened the Tier-2 PDF on disk and verified the chapter content; otherwise mention as unconsulted-but-recommended in the handoff Anomalies section, do NOT add to the bib. |
| **Rev-B** | Reviewer R2/R4 (rigour) | Replace the v2 line "by Phase A* symbolic derivation" with an explicit **Lemma** (Newton-polygon characteristic-polynomial identity at all $d \ge 2$) carrying a 6–10-line derivation; the Phase A* sweep then becomes a *verification* of this Lemma at $d \in \{2,\ldots,10\}$ rather than the load-bearing source of the identity itself. |
| **Rev-C(a)** | Reviewer R1/R3 (chain) — Q-S1 | Supply the FULL implication chain in the proof of Theorem 4.1: (Newton-polygon slope-$1/d$ edge) ⟹ (characteristic polynomial $\chi_d(c) = 1 - (\beta_d/d^d)c^d$ via Lemma) ⟹ (formal-trans-series-with-rate by Birkhoff §2) ⟹ (sectorial-asymptotic existence by Wasow §19 Thm 19.1) ⟹ (Borel-summability of the formal series by B-T 1933 §§4–6) ⟹ (the Borel-singularity radius equals $|c|$). Each ⟹ has a one-sentence justification with a citation. |
| **Rev-C(b)** | Reviewer R1 (alternative) | **NOT APPLIED** per Q-S1 — Theorem 4.1 retains theorem framing (theorem-with-documented-residual is the wrong metaphor now that the residual is closed by Rev-A). |
| **Rev-D** | Reviewer R1/R2/R5 (3 of 5 explicit) | Recommendation recorded in `arxiv_classification_recommendation.md` as a Phase F deliverable: math.CA primary / math.NT cross-list. Per Rule 2, the relay agent does **NOT** drive arXiv submission; the operator decides Q31. |
| **Rev-E (PARTIAL)** | Reviewer R3/R4 (self-containment; F2; 4 of 5 C4 ≤ 4) | Expand v2 (6 pp) → v2.1 (~10 pp) by adding: (i) a self-contained reproduction of the $d=2$ Newton-polygon proof (~1 page; replacing the citation-only treatment in v2 §2); (ii) an explicit definition of $B_d(\theta+1)$ in §1 with the worked $d=2,3,4$ specialisations (~½ page); (iii) a falsification context block recapping the v1.1 candidate $c(d) = 2\sqrt{(d-1)!}$ rejected at $d=4$ (~½ page). **NOT** full self-containment — that is PCF-3 monograph territory; aim for "reader can follow the proof without leaving the artefact". |
| **Rev-F** | Reviewer R5 (provenance) | Add an Appendix A (~1 page) listing the bridge sessions whose outputs are cited (Q20A-PHASE-C-RESUME for Phase A* sweep; PCF2-SESSION-Q1 for $d=4$ verification) with their handoff-URL stems and the SHA-256 of the cited scripts. This anchors the v2.1 artefact's provenance trail to the SIARC bridge. |
| **Rev-G** | Reviewer R3 (technical) | Expand the existing §1.1 PCF-degree-↔-irregular-singularity-rank subsection (~half page → ~full page) to derive $q = (d+2)/2$ from the substitution $z = u^d$ on equation (1) (the order-2 ODE for $f(z) = \sum Q_n z^n$). The derivation should be explicit enough that the reader can verify it without consulting v1 of CT. |
| **Rev-H** | Reviewer R4 (peer-review provenance) | Add an in-body footnote at first cite of each non-peer-reviewed self-citation (PCF-1 v1.3, PCF-2 v1.3, CT v1.3, the Phase A* SIARC bridge session) clarifying that those are SIARC Zenodo deposits with internal review only. The note acknowledges this without retracting the citations. |

---

## RELAY-PROMPT BODY  (operator pastes everything below into a fresh CLI session)

```
================================================================
SIARC RELAY PROMPT  QS-2  —  D2-NOTE-V2-1-WASOW-FULL-CLOSURE
                              (D2-NOTE v2.1 with closed Borel-
                               summability citation chain;
                               merges retired Prompt 7 / Wasow
                               Q20 full-closure)
================================================================
TASK_ID:           D2-NOTE-V2-1-WASOW-FULL-CLOSURE
TODAY_DATE:        <fill in current date YYYY-MM-DD at run time>
EXPECTED RUNTIME:  4–6 hours
COMPUTE BUDGET:    no new mpmath series; no new Phase A symbolic runs.
                   pdflatex / bibtex passes only. The Phase A* sweep
                   is QUOTED, not re-run; its SHA-256 anchors are
                   re-validated at the start of Phase A.
DEPENDENCIES:      QS-A (B-T 1933 acquisition) — DONE
                   pre-firing. Phase 0 must verify this on disk.
PARALLEL-SAFE:     with any task NOT modifying
                   `siarc-relay-bridge/sessions/2026-05-03/Q20A-
                   PHASE-C-RESUME/d2_note_v2/` (the v2 source it
                   reads from). NOT parallel-safe with: any
                   concurrent fire of this same task (would
                   collide on the session output path
                   `sessions/<TODAY>/D2-NOTE-V2-1-WASOW-FULL-
                   CLOSURE/`); any task touching the SIARC SQL
                   todo `prompt-d2-note-v2-1-wasow-full-closure-
                   fire`; any task touching the runbook-canonical
                   literature directory at
                   `tex/submitted/control center/literature/g3b_
                   2026-05-03/`.
MERGES:            retired Prompt 7 / wasow-q20-full-closure-fire.

PRE-FLIGHT (Phase 0.0 — write the spec to disk for provenance):
                   The first action the agent takes upon receiving
                   this prompt is to write the EXACT TEXT of this
                   relay-prompt body (the operator-pasted block
                   between the START and END markers) to
                   `sessions/<TODAY>/D2-NOTE-V2-1-WASOW-FULL-
                   CLOSURE/prompt_spec.md`. This anchors the
                   prompt's provenance for B1 deliverables. If the
                   agent does not have the original markdown
                   wrapper (it received only the pasted code-block
                   body), it writes the body verbatim — no wrapper
                   is required. The synthesizer-side draft of this
                   spec lives in the bridge ALREADY (under
                   `sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-
                   CLOSURE/prompt_spec.md`, drafted 2026-05-03);
                   the relay session's copy is the EXECUTED
                   variant (post-fire) and is acceptable to differ
                   from the draft only in `<TODAY>` substitutions
                   and in the operator's optional pre-fire edits.

================================================================
§0 CONTEXT
================================================================

D2-NOTE v2.0 (Zenodo concept DOI 10.5281/zenodo.19996689 / version
DOI 10.5281/zenodo.19996690; deposited 2026-05-03; PDF SHA-256
b9954d12bfe4f0c54351d9e87409c0d6870af6d53ff4904daf30e78e0e7ece66;
6 pp; readback byte-identical to local rebuild) consolidates the
cross-degree identity

    xi_0(b) = d / beta_d^{1/d}                           (*)

into a single citable artefact and upgrades its status from
"proven at d=2 / verified at d=4 / conjectured for d ≥ 2" (v1)
to "theorem-grade for all d ≥ 2 uniformly" (v2) on two new
anchors:

  (A) Phase A* extended d-sweep at d in {2..10}: 18/18 PASS at
      dps=50, relative error < 1.6e-51 above d=2; in
      `siarc-relay-bridge/sessions/2026-05-03/Q20A-PHASE-C-RESUME/`,
      driver `phase_a_star_extended_sweep.py`, SHA-256
      `06d87de…0ac277` over the wrapper and `8e6f9eb…f7496` over
      the underlying symbolic-derivation core.

  (B) Wasow 1965 §19 Thm 19.1 (uniform-in-q general-case asymptotic
      existence) + Birkhoff 1930 §2 Thm I (uniform-in-n formal-series
      existence). The Wasow + Birkhoff PDFs (slot 04 + slot 01 in
      the runbook-canonical literature directory) are SHA-256-anchored
      in `tex/submitted/control center/literature/g3b_2026-05-03/SHA256SUMS.txt`.

Five-reviewer peer review of v2 returned composite mean 4.6/10
(REVISE_BEFORE_SUBMIT × 4 / SUBMIT_WITH_MINOR_FIXES × 1) with
four convergent findings:

  F1 (rigour, all 5 reviewers C3 ≤ 4)
     The Borel-summability citation chain is admitted-incomplete
     in v2's `annotated_bibliography.bib` note, which states that
     "the Borel-summability content is treated in the companion
     Birkhoff-Trjitzinsky 1933 paper, not in §§2-3 of this 1930
     paper" — yet B-T 1933 is NOT cited in the body of v2.
     Wasow §19 supplies sectorial asymptotic existence uniformly
     in q ≥ 0, NOT Borel-summability. The move from
     formal-series-with-sectorial-asymptotic to
     Borel-singularity-radius requires a Borel-summability theorem
     (B-T 1933 §§4-6 or Loday-Richaud 2016 ch. 2 or Costin 2008 ch. 5).

  F2 (self-containment, 4 of 5 C4 ≤ 4)
     v2 at 6 pp delegates too much to non-peer-reviewed Zenodo
     records (PCF-1 v1.3, PCF-2 v1.3, CT v1.3, the Q20A-PHASE-C-
     RESUME bridge session).

  F3 (endorsement, all 5 C6 ≤ 4)
     Triple-flag (independent + self-published + AI-disclosure)
     pattern. NOT addressable in this relay; operator-driven
     handle (Q31 + arXiv endorsement workflow); recorded for
     completeness only.

  F4 (classification, 3 of 5 explicit)
     math.NT primary → math.CA primary recommendation for arXiv.
     Operator decision per Rule 2; relay agent records the
     recommendation in `arxiv_classification_recommendation.md`
     but does NOT drive arXiv submission.

Synthesizer Q-S rulings (picture v1.14 §24):

  Q-S1 → theorem-with-documented-residual elevated to theorem
         (citation chain closed by Rev-A); theorem framing
         retained, NOT demoted.
  Q-S2 → Path A revise-first; v2.1 on existing concept DOI
         19996689 (NEW VERSION on existing record).
  Q-S3 → merge Prompt 7 (Wasow Q20 full-closure) into this
         task; this relay produces both v2.1 + the Wasow
         synthesizer-arbitration verdict.
  Q-S4 → picture v1.14 already pushed (no further amendment
         from THIS prompt's verdict; absorbed in next pass).

This task closes F1 (citation chain) and F2 partial (self-
containment ~10 pp), produces v2.1 PDF for Zenodo new-version
deposit, and produces the Wasow synthesizer-arbitration
verdict that retired Prompt 7 would have produced.

================================================================
§1 ANCHOR FILES
================================================================

A1. Bridge session — D2-NOTE v2 source (read-only; v2.1 derives from this)
    `siarc-relay-bridge/sessions/2026-05-03/Q20A-PHASE-C-RESUME/d2_note_v2/`
      d2_note_v2.tex                  (22 130 B; 514 lines; the v2 source)
      annotated_bibliography.bib      (34 268 B; the bib database)
      d2_note_v2.pdf                  (404 837 B; v2.0 deposited PDF; for diff)
      d2_note_v2.log / .aux / .bbl    (build-time companions; for clean rebuild)

A2. Bridge session — Phase A* sweep (re-validate hashes, do NOT re-run)
    `siarc-relay-bridge/sessions/2026-05-03/Q20A-PHASE-C-RESUME/`
      phase_a_star_extended_sweep.py
      phase_a_star_results.json
      phase_a_star_summary.md
      phase_a_star_run.log
      claims.jsonl                    (64 entries; contains AEAL anchors
                                       for both v2 deposit + Phase A*
                                       sweep + Wasow + Birkhoff
                                       verifications)

A3. Bridge session — peer-review consolidation (read-only; for context)
    `siarc-relay-bridge/sessions/2026-05-03/D2-NOTE-V2-PEER-REVIEW/`
      [contents TBD at fire time; if missing, the synthesizer-side
       drafted briefing in this PROMPT's §0 above is sufficient — halt
       only if both are missing, with key
       HALT_QS2_PEER_REVIEW_BRIEFING_MISSING]

A4. Literature anchors (runbook-canonical paths; SHA-256-verified per
    `tex/submitted/control center/literature/g3b_2026-05-03/SHA256SUMS.txt`)

      slot 01: 01_birkhoff_1930_acta54.pdf
               SHA-256 `aeb5291e4150535969726aa9e8aba8c604ae437612e026092122208cb3952efa`
               (alias `birkhoff_1930.pdf` matches by construction)
               Reading target: §2 Theorem I (uniform-in-n formal-series existence)

      slot 03: 03_birkhoff_trjitzinsky_1933_acta60.pdf  ⭐ NEW (QS-A)
               SHA-256 `dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`
               (alias `birkhoff_trjitzinsky_1933.pdf` matches by construction)
               89 pp; Acta Mathematica 60 (1933); pypdf-verified
               title "Analytic theory of singular difference equations".
               Reading targets: §4 "A lemma on summation",
                                §5 "Construction of proper solutions to the
                                     right of a proper curve",
                                §6 "A lemma on factorization"
               (the Borel-summability machinery for irregular linear
                difference equations at irregular singular points; this
                is the F1 closure citation).

      slot 04: 04_wasow_1965_dover.pdf
               SHA-256 `f59d6835db58d2de59eab843b881b97106eee6c66e56bfce43de5788bbbaa5fd`
               (alias `wasow_1965_chap_X.pdf` matches by construction; the
               filename is historical — content is Chapter IV §§10–15
               + Chapter V §§16–19, p. 48–115, 34 spreads; both
               distinct-eigenvalue and Jordan-block / general cases)
               Reading targets: §19 Thm 19.1 + §19.3 (q = (d+2)/2 mapping
                                + ramification x = const · t^p)
                                + eq. (19.3) (gauge equation pinning
                                Borel-singularity radius 1/|λ|).

      OPTIONAL (Tier 2): if Loday-Richaud 2016 (Lecture Notes in Math
      vol. 2154) ch. 2 OR Costin 2008 ch. 5 are NOT on disk at
      `tex/submitted/control center/literature/`, the relay can
      proceed with B-T 1933 §§4–6 alone as the F1 closure citation
      (synthesizer Rev-A grants single-source closure). Cite
      Loday-Richaud and Costin in the bib only as "see also" on
      a "modern restatement of Birkhoff-Trjitzinsky 1933" footnote;
      do NOT halt for missing Tier-2 sources.

A5. AEAL claims registry — primary
    `siarc-relay-bridge/sessions/2026-05-03/Q20A-PHASE-C-RESUME/claims.jsonl`
    (64 entries; v2.1 claims derive from this baseline)

A6. Synthesizer briefing — picture v1.14 (read for synthesizer rulings)
    `tex/submitted/control center/picture_revised_20260503.md`
    (specifically §24 for the Q-S1 / Q-S2 / Q-S3 / Q-S4 rulings).

If any of A1, A2, or A4 (slot 01 / 03 / 04) is missing or has a
SHA-256 mismatch, halt with `HALT_QS2_INPUT_INVALID`.
If A3 AND the synthesizer §0 briefing are both unavailable, halt
with `HALT_QS2_PEER_REVIEW_BRIEFING_MISSING`.
A5 is optional but recommended for AEAL provenance threading.

================================================================
§2 PHASES
================================================================

PHASE 0 — INPUT VALIDATION + GATE CHECK
---------------------------------------

0.0  Write this relay-prompt body verbatim to
     `sessions/<TODAY>/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/prompt_spec.md`
     (the agent received this body via operator paste; this step
     anchors the executed-variant for B1 deliverables; cf.
     PRE-FLIGHT note in the header).

0.1  Verify all A1, A2, A4 (slot 01 / 03 / 04) files present and
     SHA-256 anchors match. Halt `HALT_QS2_INPUT_INVALID` if not.

0.2  Verify A2 phase_a_star_results.json contains 18/18 PASS at
     d in {2..10} with relative error < 1.6e-51 above d=2 and
     exact zero at d=2. Halt `HALT_QS2_PHASE_A_STAR_DRIFTED` if
     numerical content has changed.

0.3  Verify v2.0 PDF SHA-256 in A1 matches
     `b9954d12bfe4f0c54351d9e87409c0d6870af6d53ff4904daf30e78e0e7ece66`
     (the deposited Zenodo readback). Halt
     `HALT_QS2_V2_PDF_DRIFTED` otherwise.

0.4  Verify the SQL todo `g3b-acquire-bt-1933` is `done` (or
     verify operator-side that the slot 03 PDF is on disk and
     SHA-anchored — equivalent). Halt `HALT_QS2_QSA_NOT_DONE`
     otherwise.

0.5  Bib-key collision preflight. Open A1's
     `annotated_bibliography.bib` and grep for the keys to be
     added in Phase E (Rev-A): `birkhoff_trjitzinsky_1933`,
     `lodayrichaud2016divergent`, `costin2008asymptotics`. If
     ANY key already exists in the v2 bib (would be unexpected
     — v2 admitted F1 incomplete because the B-T citation was
     missing), record the existing bib note and either:
       (a) reuse the existing canonical key (preferred if the
           entry is already correct);
       (b) halt `HALT_QS2_BIBKEY_COLLISION` if the existing entry
           differs from the canonical form (Acta Math 60, 1-89;
           Lecture Notes vol 2154 ch 2; Asymptotics & Borel
           summability ch 5 respectively).
     Document the resolution in `phase_0_gate_pass.md`.

0.6  Emit `phase_0_gate_pass.md` with the verified hashes, the
     bib-key collision check outcome, and a one-line PASS line.

PHASE A — RE-VALIDATE Q20A PHASE A* SWEEP (no re-run)
-----------------------------------------------------

A.1  Read `phase_a_star_summary.md` and `phase_a_star_results.json`
     verbatim. The relay does NOT re-run the sweep; it threads the
     existing results forward into v2.1's claims.jsonl with
     evidence_type "literature_citation" + the upstream
     output_hash from the Q20A session.

A.2  Cross-check the symbolic identity content: at every
     d in {2..10}, the slope-1/d edge characteristic polynomial
     of L_d (eq. (1) of v2) is `chi_d(c) = 1 - (beta_d/d^d) c^d`,
     and the unique positive real root pins
     c(d) = d / beta_d^{1/d}. Confirmed in the Q20A session at
     dps=50; in this phase the agent merely transcribes the
     conclusion verbatim.

A.3  Emit `phase_a_revalidation.md` summarising:
       - script SHA matches
       - 18/18 PASS at d in {2..10}
       - relative error per d (read from JSON)
       - v2.1 cite anchor: same as v2 (the Q20A bridge session).

PHASE B — NEWTON-POLYGON CHARACTERISTIC-POLY LEMMA (Rev-B)
----------------------------------------------------------

B.1  Write the Lemma (in v2.1 LaTeX form; will be inserted in
     §3 via Phase E):

        Lemma (Cross-degree Newton polygon characteristic
              polynomial). For every d ≥ 2 and every PCF (1, b)
              with b(n) = beta_d n^d + l.o.t. (beta_d > 0), the
              Newton polygon of L_d at z = 0 has a unique
              non-trivial slope-1/d edge from (0,0) to (1,d), and
              the slope-1/d edge analysis (WKB ansatz f ~ exp(c/u)
              with z = u^d, theta = (u/d) d/du) produces the
              characteristic polynomial
                  chi_d(c) = 1 - (beta_d / d^d) c^d
              at leading order, with unique positive real root
              c = d / beta_d^{1/d}.

B.2  Write the proof (≤ 12 lines) explicitly. Derive ONLY what
     follows mechanically from the Newton-polygon calculation
     and the WKB ansatz; do NOT add interpretive commentary the
     calculation does not directly support:
       (a) Extract the Newton diagram from the lattice points
           supporting `1`, `z B_d(theta+1)`, and `z^2` in
           eq. (1). The Newton polygon's lower-left convex hull
           has the edge from (0,0) to (1,d) with slope 1/d; the
           remaining edges are vertical or trivial, so this is
           the unique non-trivial slope.
       (b) Apply the WKB ansatz `f ~ exp(c/u)` with `z = u^d`,
           `theta = (u/d) d/du`. The leading-order balance reads
           off the characteristic polynomial:
                  chi_d(c) = 1 - (beta_d / d^d) c^d.
       (c) The unique positive real root is c = d / beta_d^{1/d}.
       NOTE: any further commentary on edge multiplicity or root
       structure (e.g. "the edge has multiplicity 2 from `1` and
       `z^2`") MUST be either (i) derived in additional explicit
       lines or (ii) omitted. If the agent finds itself wanting
       to add such a remark but cannot derive it directly from
       the lattice-point list and the WKB balance, it OMITS the
       remark and notes the omission in
       `phase_b_newton_polygon_lemma.md`. If the agent finds
       that a load-bearing step in (a)–(c) cannot be made
       mechanical (e.g., the WKB balance turns out to have a
       hidden subleading correction that v2's "by Phase A*
       symbolic derivation" black-box was hiding), halt
       `HALT_QS2_LEMMA_NOT_SECURE`.

B.3  The Phase A* sweep (Phase A above) is now demoted from
     "the source of the identity" to "a numerical verification
     of the Lemma at d in {2..10}". The Lemma is the load-
     bearing object; the sweep is a sanity check.

B.4  Emit `phase_b_newton_polygon_lemma.md` with the LaTeX
     fragment and a 1-paragraph commentary on what changed
     vs v2 (replacing the "by Phase A* symbolic derivation"
     black-box with the explicit Lemma).

PHASE C — LITERATURE ANCHORING (B-T 1933 §§4-6 + Wasow §19 + Birkhoff §2)
------------------------------------------------------------------------

C.0  Re-read the slot 04 Wasow PDF §19 (uniform-in-q sectorial
     asymptotic existence). Confirm the v2 quotation of Thm 19.1
     and eq. (19.3) is faithful. The pre-existing
     phase_c1_wasow_verification.md from Q20A is the canonical
     source; carry forward unchanged.

C.1  Re-read the slot 01 Birkhoff 1930 PDF §2 (uniform-in-n
     formal-series existence). Confirm the v2 quotation of
     Thm I is faithful. The pre-existing
     phase_c2_birkhoff_verification.md from Q20A is the
     canonical source; carry forward unchanged.

C.2  ⭐ NEW for v2.1: read slot 03 (B-T 1933) §§4–6:

       §4 "A lemma on summation"
           — establishes that the formal series solutions of
             irregular linear difference equations admit an
             explicit summation procedure (the "Borel-Laplace"
             type construction in B-T's vocabulary).

       §5 "Construction of proper solutions to the right of
            a proper curve"
           — produces the actual analytic-summation by
             integration along sectors avoiding the Stokes
             rays; this is the Borel-summability content
             proper.

       §6 "A lemma on factorization"
           — establishes the multiplicative structure of the
             summed solutions, allowing the Borel-Laplace sum
             to be identified with a single analytic function
             on each sector.

     Together, §§4–6 should constitute the Borel-summability
     theorem for formal series solutions of irregular linear
     difference equations at irregular singular points; the
     agent VERIFIES this in C.2.x sub-gates below — does NOT
     assume.

     The agent extracts FAITHFUL verbatim quotations: at LEAST
     one ≤30-word anchor quote per section, plus any additional
     quotes needed to cover each load-bearing implication in
     C.2.x below. All quotes are recorded in
     `phase_c3_bt1933_verification.md` with the PDF SHA-256 and
     page numbers, using `evidence_type: "vision_transcription"`
     for any quotation extracted from a scanned page (cf.
     dispatch-4 precedent in Q20A
     `phase_c1_wasow_verification.md`).

C.2.1  Sub-gate — Borel-summability. The §§4–6 statements must
       support the claim that the formal series solutions of
       irregular linear difference equations are
       Borel-summable (in the sense that the formal Borel
       transform converges in some neighbourhood of the origin
       in the Borel plane and admits analytic continuation
       along non-Stokes rays). If the §§4–6 statements only
       support EXISTENCE of a summation procedure but NOT the
       Borel-summability of the formal series specifically,
       halt `HALT_QS2_BT_SCOPE_INSUFFICIENT` with the verbatim
       quotations and the agent's analysis of the gap.

C.2.2  Sub-gate — sectorial / right-of-curve construction. §5's
       construction must support the existence of an analytic
       function on each sector (away from Stokes rays) whose
       asymptotic expansion is the formal series. Halt
       `HALT_QS2_BT_SCOPE_INSUFFICIENT` if §5's "right of a
       proper curve" construction turns out to be a different
       object (e.g., a particular-solution construction that
       does NOT carry the Borel-summability content).

C.2.3  Sub-gate — Borel-singularity radius / first-singularity
       identification. The most load-bearing claim in v2.1's
       proof of Theorem 4.1 is that the nearest singularity of
       the Borel transform is at distance |c| from the origin,
       where c = d/beta_d^{1/d}. The §§4–6 statements (jointly
       with Wasow §19 + Birkhoff §2) must support this identi-
       fication. If the agent finds that B-T 1933 §§4–6 supply
       Borel-summability but NOT the singularity-radius identi-
       fication (e.g., the radius identification needs Costin
       2008 ch. 5 or Loday-Richaud ch. 2 or Écalle's
       resurgence machinery), halt
       `HALT_QS2_RADIUS_IDENTIFICATION_UNSUPPORTED`. Operator
       triages by either (i) acquiring Tier-2 sources and
       refiring; (ii) softening the v2.1 proof to a weaker
       claim about the leading exponential rate without the
       sharp Borel-radius identification (operator-arbitrated;
       not relay-decided).

C.2.4  Sub-gate — irregular-linear-difference vs.
       irregular-linear-ODE scope. v2's PCF is an order-2 ODE
       at z=0; B-T 1933 covers irregular linear DIFFERENCE
       equations. The agent verifies (with a one-paragraph
       commentary citing Wasow §19's reduction or B-T 1933's
       own opening exposition) that the Borel-summability
       machinery transfers from the difference-equation case
       to the ODE case via the standard reduction
       (z = u^d substitution + theta-form). Halt
       `HALT_QS2_BT_SCOPE_INSUFFICIENT` if the transfer is not
       supported by the literature on disk.

     Document each sub-gate's PASS/HALT outcome in
     `phase_c3_bt1933_verification.md` under sub-headings
     C.2.1 / C.2.2 / C.2.3 / C.2.4. ALL FOUR must PASS for
     Phase C to emit `C_LITERATURE_CHAIN_CLOSED`.

C.3  Synthesise the chain (this is the Wasow Q20 full-closure
     verdict that retired Prompt 7 would have produced):

       (Newton-polygon slope-1/d edge)
         ⟹ [Lemma in Phase B]
       (chi_d(c) = 1 - (beta_d/d^d) c^d, unique positive root
        c = d/beta_d^{1/d})
         ⟹ [Birkhoff 1930 §2 Thm I]
       (formal-series solution exists uniformly in n=d at the
        irregular singular point z=0)
         ⟹ [Wasow 1965 §19 Thm 19.1 + eq. (19.3)]
       (the formal series has a sectorial-asymptotic resummation
        on every narrow subsector at z=0, with rate determined
        by the leading characteristic root c)
         ⟹ [B-T 1933 §§4-6]
       (the formal series is Borel-summable; its Borel transform
        has its nearest singularity at distance |c| from the
        origin in the Borel-plane; this is the "Borel-singularity
        radius" interpretation)
         ⟹ [Phase A*-verified at d in {2..10}; Lemma at all d ≥ 2]
       (xi_0(b) = d / beta_d^{1/d}, uniformly in d ≥ 2).

     Each ⟹ becomes a one-sentence citation in the v2.1
     proof of Theorem 4.1.

C.4  Emit `phase_c_full_closure_synthesis.md` with the chain
     above, the Q20-arbitration verdict
     (`WASOW_Q20_CLOSURE_VERDICT: PUBLICATION_GRADE_PROOF` if
     the chain holds with no admitted-missing step), and the
     bib entries to add to `annotated_bibliography.bib`:

       birkhoff_trjitzinsky_1933 ← Acta Math 60, 1-89, §§4-6
                                   (REQUIRED — F1 closure
                                    primary citation)

       lodayrichaud2016divergent ← Lecture Notes vol 2154 ch 2
                                   (ONLY IF the PDF is on disk
                                    at `tex/submitted/control
                                    center/literature/` AND the
                                    agent has opened the file
                                    + verified ch 2 contains
                                    the Borel-Laplace machinery;
                                    cite as "see also" in the
                                    proof; otherwise OMIT from
                                    the bib entirely)

       costin2008asymptotics      ← Costin 2008 ch 5
                                   (ONLY IF the PDF is on disk
                                    AND the agent has opened
                                    the file + verified ch 5
                                    contains the Borel-Laplace
                                    machinery; cite as "see
                                    also"; otherwise OMIT)

     ETHICS GATE: the agent does NOT add Loday-Richaud or
     Costin to the bib without having opened the file and
     verified the chapter content matches the F1-closure topic.
     If a Tier-2 PDF is "almost on disk" (e.g., listed in a
     SHA registry but actually missing) or its contents do not
     match the runbook expectation, the relay agent records
     "Tier-2 source not consulted; F1 closure rests on B-T
     1933 §§4–6 alone per synthesizer Rev-A grant" in
     `phase_c_full_closure_synthesis.md` AND in the v2.1
     handoff under "Anomalies and open questions". This makes
     the unconsulted-but-recommended status explicit without
     the artefact misrepresenting consultation.

PHASE D — VERDICT AGGREGATION
-----------------------------

D.1  Aggregate Phase 0 / A / B / C signals into a verdict.
     Signals:
       phase_0  → C0_GATE_PASS
       phase_a  → A_PHASE_A_STAR_VERIFIED
       phase_b  → B_LEMMA_DERIVED  (or B_LEMMA_NOT_SECURE if
                  Phase B halt fired — already routed through
                  HALT_QS2_LEMMA_NOT_SECURE)
       phase_c  → C_LITERATURE_CHAIN_CLOSED  (all 4 sub-gates
                                               C.2.1–C.2.4 PASS)
                  — or —
                  C_LITERATURE_CHAIN_TIER_2_MISSING (Tier-2
                                               sources unavailable
                                               but B-T 1933 §§4–6
                                               sub-gates PASS;
                                               still acceptable
                                               for full closure
                                               per Rev-A grant)
                  — or —
                  routed through HALT_QS2_BT_SCOPE_INSUFFICIENT
                  / HALT_QS2_RADIUS_IDENTIFICATION_UNSUPPORTED if
                  any sub-gate fails.

D.2  Verdict ladder (in order of preference; see §6 OUTCOME
     LADDER):

       UPGRADE_V2_1_FULL                — all four signals positive
                                          AND page count ∈ [9,12]
       UPGRADE_V2_1_PARTIAL_PAGECOUNT   — all four signals positive
                                          AND page count ∈ [7,8]
                                          ∪ [13,14]
       UPGRADE_V2_1_PARTIAL             — phase_b OR phase_c
                                          partially complete
                                          (e.g., a §§4–6 quote
                                          missing but the
                                          chain still closes
                                          via §4+§5 alone)
       HALT_*                           — gate failure or
                                          irrecoverable issue

D.3  Emit `phase_d_verdict.md` with the verdict label, signal
     table, "what this closes" table (F1 / G1-residual / M2 /
     prompt 7 / M9 gating reduction), and the Q20-arbitration
     verdict alongside.

PHASE E — D2-NOTE V2.1 LATEX DRAFT
----------------------------------

E.0  Workflow: copy `d2_note_v2.tex` and `annotated_bibliography.bib`
     from A1 into the session deliverable folder. IMMEDIATELY rename
     the LaTeX source from `d2_note_v2.tex` to `d2_note_v2_1.tex`
     (mv / Move-Item) so that all pdflatex / bibtex invocations and
     all subsequent E.x edits operate on the v2.1 filename. The
     `annotated_bibliography.bib` keeps its name (it is shared
     across versions). ALL EDITS are made in the session-local
     `d2_note_v2_1.tex`; the A1 source is read-only.

E.1  Apply Rev-A: in the proof of Theorem 4.1 (currently §3
     "The cross-degree theorem at d ≥ 2", subsection
     "Cross-degree universality of xi_0"), insert the chain from
     Phase C.3 with the new citation
     `\cite{birkhoff_trjitzinsky_1933}` at the Borel-summability
     step. The Tier-2 "see also" citations
     `\cite{lodayrichaud2016divergent}` and
     `\cite{costin2008asymptotics}` are inserted ONLY IF Phase
     C.4's ethics gate added the corresponding bib entries (i.e.,
     ONLY IF the agent opened the Tier-2 PDFs and verified the
     chapter content). Otherwise the proof body cites B-T 1933
     alone, and the Tier-2 sources are mentioned only in
     the handoff "Anomalies and open questions" section as
     "modern restatements suggested by synthesizer review,
     not consulted in this session".
     Update the bib note in §3.3 ("Birkhoff §2 supplies the
     formal-existence step; the Borel-summability content is
     supplied by Wasow §19 instead") to read:
       "Birkhoff §2 supplies the formal-existence step; Wasow
       §19 supplies the sectorial-asymptotic existence;
       Birkhoff–Trjitzinsky 1933 §§4–6 supplies the Borel-
       summability of the formal series, completing the chain."
     The qualifier "this re-targets a citation that
     [Birkhoff 1930] does not directly support" can be REMOVED
     (the residual is closed).

E.2  Apply Rev-B: insert the Lemma + proof from Phase B at the
     start of a NEW subsection §3.1 titled "The Newton-polygon
     characteristic-polynomial Lemma". Structural contract for
     the §3 reorganisation:
       (a) The new §3.1 carries `\subsection{The Newton-polygon
           characteristic-polynomial Lemma}` with a fresh
           label `\label{ssec:newton-poly-lemma}`. The Lemma is
           stated immediately after the subsection header inside
           a `\begin{lemma}…\end{lemma}` environment with label
           `\label{lem:newton-poly-chi-d}`. The proof
           (≤12 lines, from Phase B.2) follows in a
           `\begin{proof}…\end{proof}` environment.
       (b) The pre-existing v2 subsection labelled
           `\label{ssec:phase-a-star}` (containing the Phase A*
           sweep at d in {2..10}) is RETAINED and DEMOTED to
           §3.1.2 "Numerical verification of the Lemma at
           d ∈ {2..10}" with its existing label preserved
           (no `\ref` breakage). Its opening sentence is
           rewritten from "by Phase A* symbolic derivation" to
           "Phase A* numerically verifies the Lemma at
           d ∈ {2..10} at dps=50 (results threaded forward from
           [Q20A bridge session]; …)".
       (c) If v2 had its own §3.1 before the Phase A* subsection,
           that content (the cross-degree theorem statement and
           preamble) is RENUMBERED to §3.0 or absorbed into the
           §3 preamble — the agent decides at edit time based on
           the v2 source structure, but DOES NOT delete content.
           Any `\ref{...}` to an old subsection label is
           re-validated in pass-3 (zero "undefined references").
       (d) The Lemma label `\label{lem:newton-poly-chi-d}` is
           cited downstream in Theorem 4.1's proof (Rev-C(a) /
           Phase E.3) via `\cref{lem:newton-poly-chi-d}` or
           equivalent.
     The Lemma is the load-bearing object for v2.1's cross-degree
     identity; the Phase A* sweep is the verification.

E.3  Apply Rev-C(a): rewrite the proof sketch of Theorem 4.1
     (currently 12 lines starting "The Newton polygon of L_d
     ...") as the explicit chain from Phase C.3, with each ⟹
     bearing a citation. Keep the existing Wasow §19 / Birkhoff
     §2 anchoring; ADD the B-T 1933 §§4–6 step. Length budget:
     ~25–30 lines.

E.4  Apply Rev-D: write `arxiv_classification_recommendation.md`
     to the session folder (NOT the LaTeX). Content: 1-page
     summary of the math.NT → math.CA primary recommendation
     (3 of 5 reviewers); cite Q-S2 ruling; state that Q31 is the
     operator decision; do NOT touch arXiv metadata.

E.5  Apply Rev-E (PARTIAL):
       (i) Expand §2 "The proven case d=2" from ~1 page (v2)
           to ~2 pages by reproducing the Newton-polygon proof
           of the d=2 case in self-contained form — the
           lattice-point extraction, the WKB substitution
           z = u^2, the characteristic polynomial
           chi_2(c) = 1 - (beta_2/4) c^2, the unique positive
           root, the indicial polynomial, and the worked
           V_quad example. Cite [CT v1.3 §3.3] for the
           original derivation, but reproduce the steps so the
           reader does not need to leave the artefact.
       (ii) Expand §1 "Setup" by ~½ page with an explicit
            definition of B_d(theta+1) (the d-th degree
            polynomial encoding b on the shift-rescaled Euler
            operator), with the worked d=2,3,4 specialisations
            written out.
       (iii) Add a new §2.5 "Falsification context" recapping
             the v1.1 candidate c(d) = 2*sqrt((d-1)!) rejected
             at d=4 (already in v2 as Remark 3.4 — promote to
             a half-page subsection with the fuller history of
             how the v1.1 candidate was tested). This is ½ page.
       Net: v2 (6 pp) → v2.1 (~10 pp).

E.6  Apply Rev-F: add Appendix A "Bridge session provenance"
     listing:
       - sessions/2026-05-03/Q20A-PHASE-C-RESUME/  (Phase A*)
       - sessions/2026-05-01/PCF2-SESSION-Q1/      (d=4 verification)
       - sessions/2026-05-03/Q20A-PHASE-C-RESUME/d2_note_v2/  (v2 source)
       - sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/  (this session)
     with handoff URL stems and per-script SHA-256.

E.7  Apply Rev-G: expand §1.1 ("PCF degree ↔ irregular-singularity
     rank") from ~½ page to ~1 page. Derive q = (d+2)/2 from
     z = u^d on equation (1):
       L_d f := (1 - z B_d(theta+1) - z^2) f = 1
     Under z = u^d: theta = z d/dz = u d/du · (d/du)/(d/du) =
       (1/d) u d/du · d/du · ... — write out the substitution
     in full, derive the rank q = (d+2)/2 from the leading
     polynomial degree of B_d after the substitution, and
     handle the half-integer case (d odd) via the Wasow §19.3
     ramification x = const · t^p with p=2.

E.8  Apply Rev-H: at first cite of each non-peer-reviewed
     SIARC self-citation (PCF-1 v1.3, PCF-2 v1.3, CT v1.3, the
     Q20A-PHASE-C-RESUME bridge session), add a footnote of the
     form
       "\footnote{SIARC Zenodo deposit; internal review only,
        not peer-reviewed.}"
     This is in-body (where the citation appears), not in the
     bib. Apply once per artefact; subsequent cites do not
     repeat the footnote.

E.9  Update the version line:
       \def\version{2.1}
     Update the date line:
       \date{<TODAY> (v\version)}
     Update the abstract first sentence to reflect the v2.1
     status: the residual of v2 ("theorem-with-documented-
     residual") is now closed; the artefact is "theorem with
     a closed citation chain". Keep the rest of the abstract
     intact.
     The line in the v2 abstract that reads "the contribution
     is the Phase A* d-sweep and the literature anchoring"
     can be amended in v2.1 to read "the contributions are the
     Newton-polygon characteristic-polynomial Lemma, the Phase
     A* d-sweep verification, and the Borel-summability
     citation chain via B-T 1933 §§4–6 + Wasow §19 + Birkhoff
     §2".

E.10 Build the v2.1 PDF:
       pdflatex d2_note_v2_1
       bibtex   d2_note_v2_1
       pdflatex d2_note_v2_1
       pdflatex d2_note_v2_1
     Pass-3 log MUST satisfy:
       - "Output written on d2_note_v2_1.pdf (X pages, Y bytes)"
       - 0 unresolved citations
       - 0 undefined references
       - 0 pdflatex errors / fatal-line markers
     Halt `HALT_QS2_BUILD_FAIL` if any of the above fails (this
     is a HARD halt — actual build failure with no usable PDF).

     Page-count branching (build CLEAN but page count out of
     range):
       - X ∈ [9, 12]:   PASS — feeds UPGRADE_V2_1_FULL eligibility
       - X ∈ [7, 8]:    SHORT — feeds UPGRADE_V2_1_PARTIAL_PAGECOUNT
                        (Rev-E partial expansion fell short of
                         the 9-page floor; Theorem + chain still
                         landed; operator decides whether to
                         deposit the short v2.1 or refire QS-2
                         with a 1-page padding)
       - X ∈ [13, 14]:  LONG — feeds UPGRADE_V2_1_PARTIAL_PAGECOUNT
                        (Rev-E partial expansion overshot; same
                         operator triage)
       - X ≤ 6 or X ≥ 15:
                        Halt `HALT_QS2_PAGE_COUNT_DRIFT` (clean
                         build but page count outside the
                         tolerance band; almost certainly a
                         malformed expansion the agent should not
                         silently accept).
     Emit `phase_e_build_attestation.md` recording the actual X,
     the ladder branch, and the SHA-256 of the built PDF.

E.11 Compute v2.1 PDF SHA-256 and record it in the session.
     Run pypdf full-text extraction; verify:
       - title metadata is "Cross-degree universality of the
         Borel-singularity radius for polynomial continued
         fractions (v2.1)" or compatible v2.1 stamp
       - author metadata is "Papanokechi"
       - all 6 PII tokens (per `tools/pii_check.py` if available)
         are absent
       - "Birkhoff" + "Trjitzinsky" both occur in the body
         (Rev-A landed)
       - "Lemma" occurs in §3 (Rev-B landed)
       - the explicit B_d(theta+1) definition occurs in §1
         (Rev-G + Rev-E partial landed)
       - Appendix A "Bridge session provenance" occurs (Rev-F
         landed)
       - first cite of each non-peer-reviewed self-citation
         carries the SIARC-disclosure footnote (Rev-H landed)
     Halt `HALT_QS2_REV_LANDING_INCOMPLETE` with a list of
     missing revisions if any check fails.

PHASE F — HANDOFF + AEAL CLAIMS + ZENODO PACKAGING
--------------------------------------------------

F.1  Append claims to claims.jsonl per §3 below. Minimum 18 entries
     (≥ 14 quoted forward from the Q20A baseline + ≥ 4 NEW for v2.1).

F.2  Write `zenodo_description_d2_note_v2_1.txt` mirroring the
     v2 description format (`sessions/2026-05-03/Q20A-PHASE-C-
     RESUME/zenodo_description_d2_note_v2.txt`); update the
     version stamp, the page count, the SHA-256 line, and the
     "What's new in v2.1" block (closure of F1; Rev-A through
     Rev-H minus Rev-C(b) applied; Rev-E PARTIAL applied — note
     "partial", not "full" — per Q-S1 / synthesizer Rev-E
     scoping).

F.3  Write `zenodo_upload_d2_note_v2_1_runbook.md` mirroring the
     v2 runbook (same path family). Note: this is a NEW VERSION
     on existing concept DOI 19996689 — NOT a fresh concept DOI.
     The runbook walks the operator through the
     "Upload new version" flow, NOT "Upload new record".

F.4  Write Standing-Final-Step `handoff.md` per the SOP template
     (in this prompt's `§7 STANDING FINAL STEP` reproduction);
     status MUST reflect actual final outputs. CRITICAL: write
     handoff.md ONLY AFTER all builds + verifications are
     complete.

F.5  Write `verdict.md` (one line):
       UPGRADE_V2_1_FULL | UPGRADE_V2_1_PARTIAL_PAGECOUNT |
       UPGRADE_V2_1_PARTIAL | HALT_*

F.6  Write `halt_log.json` (empty `{}` if no halt; populated
     per SIARC SOP otherwise).

F.7  Write `discrepancy_log.json` (empty `{}` if none; e.g.,
     if any AEAL output_hash mismatches its v2 baseline,
     record it here — should be ZERO since the relay does NOT
     re-run any numerical pipeline).

F.8  Write `unexpected_finds.json` (empty `{}` if none; e.g.,
     if reading B-T 1933 §§4-6 surfaces a NEW gap that v2.1
     does not yet cover, record it here).

F.9  Write `rubber_duck_critique.md` — the agent's own sanity
     sweep against:
       - Did the chain in Phase C.3 actually close, or is
         there a hidden ⟹ that still depends on a
         non-cited result?
       - Does the new Lemma in Phase B actually hold without
         hand-waving the multiplicity-2 condition?
       - Does Rev-E partial actually achieve "reader can follow
         without leaving the artefact" — or is the d=2
         reproduction still too abbreviated?
       - Was Rev-G's q = (d+2)/2 derivation actually written
         out, or does it still hand-wave the substitution?
       - Are there any forbidden verbs ("shows", "confirms",
         "proves", "demonstrates", "establishes", "verifies")
         used in a prediction-or-conjecture context?

F.10 Run the Standing Final Step (§7 below) — commit + push
     to bridge; output BRIDGE: + CLAUDE_FETCH: URLs.

================================================================
§3 AEAL CLAIMS MINIMUM
================================================================

The session's `claims.jsonl` MUST contain at least 18 entries.

CARRY-FORWARD CONVENTION: "carried forward" claims are NEW
session-local claims with `evidence_type:
"literature_citation"` (or `"build_attestation"` for upstream
PDF SHAs) whose `output_hash` and `script` fields REFERENCE
the upstream Q20A bridge session's claim entry. They are NOT
literal copies of upstream claim IDs — each session's claims
ledger is independent. The carried-forward claim's `claim`
field reads, e.g., "Phase A* sweep at d=2 gives c(2) = 2/√β_2
exactly (relative error = 0); upstream anchor from
sessions/2026-05-03/Q20A-PHASE-C-RESUME/claims.jsonl entry K
with output_hash <H>".

Recommended structure:

  Carried forward from Q20A baseline (≥ 14):
    01–05  Phase A* sweep anchors (5 claims; one per d in {2,3,4,5,6}
           is a sensible minimum)
    06     Phase A symbolic-derivation core SHA
    07     Phase A* extended-sweep wrapper SHA
    08     v2.0 PDF SHA-256 (anchor for delta-comparison)
    09     Wasow §19 Thm 19.1 vision_transcription anchor (PDF SHA
           + page + ≤30-word quote)
    10     Birkhoff 1930 §2 Thm I vision_transcription anchor
    11     d=2 V_quad worked-example anchor (CT v1.3)
    12     d=4 PCF2-SESSION-Q1 measurement anchor
    13     CT v1.3 Conj 3.3.A* anchor
    14     CT v1.3 Remark 3.3.E (v1.1 candidate falsification)
           anchor

  NEW for v2.1 (≥ 4):
    15     B-T 1933 §4 "A lemma on summation" vision_transcription
           anchor (PDF SHA + page + ≤30-word quote)
    16     B-T 1933 §5 "Construction of proper solutions"
           vision_transcription anchor
    17     B-T 1933 §6 "A lemma on factorization"
           vision_transcription anchor
    18     v2.1 PDF SHA-256 (the new build attestation)

  RECOMMENDED EXTRAS (push total beyond 18):
    19     Newton-polygon characteristic-poly Lemma derivation
           anchor (Phase B; evidence_type "computation" if any
           SymPy verification run; "literature_synthesis"
           otherwise)
    20     v2.1 build pdflatex pass-3 log SHA
    21     Bridge-session-provenance Appendix A entry SHAs
    22     pypdf v2.1 full-text PII regression PASS attestation

Each entry MUST include `claim`, `evidence_type` (one of
"computation", "literature_citation", "vision_transcription",
"literature_synthesis", "build_attestation"), `dps` (where
numerical), `reproducible: true`, `script` (where applicable),
and `output_hash` (SHA-256). Per SIARC AEAL standing instructions.

================================================================
§4 HALT CONDITIONS
================================================================

`HALT_QS2_INPUT_INVALID`
    A1, A2, or A4 (slot 01 / 03 / 04) missing or SHA mismatch.

`HALT_QS2_PHASE_A_STAR_DRIFTED`
    phase_a_star_results.json content has changed since v2
    deposit (would require re-running the sweep; out of scope
    for this prompt).

`HALT_QS2_V2_PDF_DRIFTED`
    A1's d2_note_v2.pdf SHA does not match the deposited
    Zenodo readback `b9954d12…0e7ece66`.

`HALT_QS2_QSA_NOT_DONE`
    g3b-acquire-bt-1933 SQL todo is not `done` OR slot 03
    PDF is not at the canonical path.

`HALT_QS2_PEER_REVIEW_BRIEFING_MISSING`
    A3 missing AND this prompt's §0 briefing has been stripped.

`HALT_QS2_BIBKEY_COLLISION`
    Phase 0.5 finds an existing bib entry for one of the keys
    to be added by Rev-A whose form differs from the canonical
    expectation (Acta Math 60, 1-89; Lecture Notes vol 2154
    ch 2; Asymptotics & Borel summability ch 5).

`HALT_QS2_LITERATURE_CHAIN_INCOMPLETE`
    Phase C.2 cannot extract faithful anchor quotations of
    §§4-6 statements from B-T 1933 (e.g., the sections turn
    out not to actually contain Borel-summability content;
    contradicts the runbook's expectation).

`HALT_QS2_BT_SCOPE_INSUFFICIENT`
    Phase C.2.1 / C.2.2 / C.2.4 sub-gate fails — B-T 1933
    §§4-6 supply a different object than the F1-closure
    citation requires (e.g., summation procedure but not
    Borel-summability of the formal series; or the reduction
    from difference-equation-Borel-summability to ODE-Borel-
    summability is not supported by the literature on disk).

`HALT_QS2_RADIUS_IDENTIFICATION_UNSUPPORTED`
    Phase C.2.3 sub-gate fails — B-T 1933 §§4-6 supply
    Borel-summability but not the Borel-singularity-radius
    identification at distance |c|. Operator triages
    (Tier-2 acquisition or Theorem 4.1 softening).

`HALT_QS2_LEMMA_NOT_SECURE`
    Phase B finds that the Newton-polygon → characteristic-
    polynomial derivation cannot be made mechanical (a load-
    bearing step has a hidden subleading correction that v2's
    "by Phase A* symbolic derivation" black-box was hiding).

`HALT_QS2_BUILD_FAIL`
    pdflatex pass-3 reports unresolved citations, undefined
    references, or any LaTeX error.

`HALT_QS2_PAGE_COUNT_DRIFT`
    v2.1 page count is X ≤ 6 or X ≥ 15 (clean build but
    drastically out of band — almost certainly malformed
    expansion). For X ∈ [7,8] OR X ∈ [13,14], the outcome
    ladder branches to UPGRADE_V2_1_PARTIAL_PAGECOUNT
    instead of halting.

`HALT_QS2_REV_LANDING_INCOMPLETE`
    Phase E.11 verification finds one or more revisions did
    not land in the rebuilt PDF.

`EPISTEMIC_LANGUAGE_DRIFT`
    Forbidden verbs (see §5 below) appear in any
    prediction-or-conjecture context. Hard halt; no
    continuation.

Halt log JSON schema:

    {
      "halt_key": "HALT_QS2_*",
      "phase": "0|A|B|C|D|E|F",
      "reason": "<one-paragraph explanation>",
      "files_emitted_so_far": ["..."],
      "next_step_recommendation": "<actionable; e.g.,
                                    re-run QS-A; ask operator
                                    for Loday-Richaud PDF; ...>"
    }

================================================================
§5 FORBIDDEN-VERB HYGIENE  (per CT v1.4 / Q20a / D2-NOTE v2 SOP)
================================================================

Verb permission is keyed to the EPISTEMIC STATUS of the case
being described. The agent applies the table below per
sentence:

  STATUS                  FORBIDDEN VERBS         PERMITTED VERBS
  ----------------------  ----------------------  ----------------------------
  CONJECTURED             shows, confirms,        predicts, expects,
  (e.g. d ≥ 5 not yet     proves, demonstrates,   forecasts, conjectures,
  Phase-A-verified)       establishes, verifies,  is consistent with
                          shows that
  ----------------------  ----------------------  ----------------------------
  VERIFIED                shows, confirms,        verifies (numerical sense
  (numerical only;        proves, demonstrates,   ONLY when paired with
  d ∈ {3..10} Phase A*    establishes,            "numerically" or "at dps=N");
  sweep before Lemma)     "shows that"            constrains, narrows the
                                                  interval, supports, is
                                                  consistent with
  ----------------------  ----------------------  ----------------------------
  PROVEN                  none in this status     proves, establishes,
  (d=2 Newton-polygon                             demonstrates, shows that,
  argument with                                   verifies (in the
  explicit Lemma —                                rigour-grade sense)
  in scope)
  ----------------------  ----------------------  ----------------------------
  THEOREM-GRADE WITH      none for the proof      proves, establishes,
  CLOSED CITATION CHAIN   itself; for the         demonstrates (the proof
  (Theorem 4.1 at all     citation chain          itself); supports, anchors
  d ≥ 2 in v2.1 status    transitions, the        (the citation chain via
  per Q-S1 ruling)        weaker verbs            B-T 1933 / Wasow / Birkhoff)
                          "anchors", "supports"
                          should be preferred
                          to "proves"
  ----------------------  ----------------------  ----------------------------
  DEFERRED                shows, confirms,        is deferred to,
  (operator-decision      proves, demonstrates,   is the subject of (future
  items: Q31, Q30,        establishes, verifies   task / synthesizer pass),
  endorsement)                                    awaits (operator decision)

NOTE on "shows": the bare verb "shows" is FORBIDDEN in the
abstract and the conclusion regardless of status, because the
abstract cannot disambiguate which of d=2 (proven) vs d ≥ 3
(theorem-grade) it refers to. Use "proves" (d=2 sense) or
"establishes" (d ≥ 2 sense via the citation chain) explicitly,
or rephrase to "the cross-degree identity ξ_0(b) = d/β_d^{1/d}
holds for all d ≥ 2 (Theorem 4.1)" — the existence verb is
permitted at all statuses.

Hard-halt halt_log.json key for any drift:
`EPISTEMIC_LANGUAGE_DRIFT` (no continuation).

================================================================
§6 OUTCOME LADDER
================================================================

In order of preference:

  1. UPGRADE_V2_1_FULL
       - phase_0 / A / B / C / D / E / F all PASS
       - v2.1 PDF builds clean at [9, 12] pp
       - Citation chain closed (B-T 1933 §§4–6 cited;
         optionally Loday-Richaud + Costin "see also")
       - Rev-A, Rev-B, Rev-C(a), Rev-D, Rev-E (PARTIAL only),
         Rev-F, Rev-G, Rev-H all landed in the rebuilt PDF
         (Rev-C(b) NOT applied per Q-S1; Rev-E full NOT applied
          per synthesizer Rev-E scoping)
       - 0 forbidden-verb drift

       Closes:
         F1 (peer-review rigour) ✅
         G1 ✅ (full closure; no residual flag)
         M2 ✅ (literature module fully done)
         prompt 7 ✅ (Wasow Q20 full-closure verdict produced;
                     SQL todo `prompt-7-wasow-q20-full-closure-fire`
                     retires automatically)
         M9 gating reduces to {M4, M6} unconditionally

       Operator next: Q31 + Q30 absorbed into the next picture
       amendment; Zenodo new-version deposit of v2.1 (per F.3
       runbook); future arXiv-mirror task on v2.1 (Q-S2 path).

  2. UPGRADE_V2_1_PARTIAL_PAGECOUNT  (NEW; clean build but
                                       short or long)
       - PDF builds clean (0 unresolved citations / undefined refs)
       - Phase D verdict UPGRADE_V2_1_FULL except for the
         page-count miss
       - Page count X ∈ [7,8] (short) or X ∈ [13,14] (long)
       - All revisions LANDED per Phase E.11 verification
       Operator decides whether to:
         (a) deposit v2.1 as-is on concept DOI 19996689
             (acceptable; the band is a soft target, not a
              publishability gate)
         (b) refire QS-2 with a Rev-E-pad delta (1 page
             padding for short; 1-page trim for long)

  3. UPGRADE_V2_1_PARTIAL
       - some revisions landed but one or more gaps remain
         (e.g., Tier-2 Borel-summability sub-gate triggered
         a partial citation chain; or Rev-G derivation still
         hand-waves the half-integer case; or one of the
         B-T §§4–6 anchor quotations could not be extracted
         faithfully but the overall Borel-summability content
         was confirmed in §§4 + §5 alone)
       - PDF builds clean but with notes
       Operator decides whether to:
         (a) deposit v2.1 as-is (accept partial)
         (b) refire QS-2 with the gap addressed (full)

  4. HALT_*
       - any §4 halt key fires; no v2.1 PDF emitted; resumable
         via the halt_log.json `next_step_recommendation`.

================================================================
§7 STANDING FINAL STEP
================================================================

CRITICAL: do NOT skip this step even if earlier phases had
partial failures. Execute AFTER all task deliverables are
written.

BRIDGE REPO:    https://github.com/papanokechi/siarc-relay-bridge
SESSION PATH:   sessions/<TODAY>/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/
                (NB: even if firing crosses midnight, use the
                 calendar date the session STARTED on as <TODAY>
                 for path consistency.)

B1 — Collect deliverables. Required:
       prompt_spec.md             (this prompt body, written by
                                    Phase 0.0 verbatim from
                                    operator paste, for provenance)
       d2_note_v2_1.tex            (the LaTeX source)
       d2_note_v2_1.pdf            (the build artefact)
       d2_note_v2_1.log            (pass-3 log)
       annotated_bibliography.bib  (with new entries)
       phase_0_gate_pass.md
       phase_a_revalidation.md
       phase_b_newton_polygon_lemma.md
       phase_c3_bt1933_verification.md
       phase_c_full_closure_synthesis.md
       phase_d_verdict.md
       phase_e_build_attestation.md  (page count + ladder branch)
       claims.jsonl
       verdict.md
       halt_log.json               (empty {} if no halt)
       discrepancy_log.json        (empty {} if none)
       unexpected_finds.json       (empty {} if none)
       rubber_duck_critique.md
       arxiv_classification_recommendation.md  (Rev-D)
       zenodo_description_d2_note_v2_1.txt
       zenodo_upload_d2_note_v2_1_runbook.md
       handoff.md                  (the SIARC SOP handoff —
                                    template inlined in B3 below)
     Exclude: .venv/, __pycache__/, *.aux, *.out, *.bbl, *.blg
              (build companions; the .pdf + .log + .tex + .bib
               are the canonical artefacts).

B2 — Stage in bridge repo. Use Windows-style paths:
       cd "C:\Users\shkub\OneDrive\Documents\archive\admin\
           VSCode\claude-chat\siarc-relay-bridge"
       git pull origin main
       New-Item -ItemType Directory -Path
         "sessions\<TODAY>\D2-NOTE-V2-1-WASOW-FULL-CLOSURE"
         -Force
       Copy-Item <each deliverable> -Destination
         "sessions\<TODAY>\D2-NOTE-V2-1-WASOW-FULL-CLOSURE\"

B3 — Write handoff.md using the inlined template below. Fill
     EVERY section — no template placeholders. Status MUST
     reflect actual final outputs. CRITICAL: write handoff.md
     ONLY AFTER all builds + verifications are complete.

     Template (B3):

       ---
       # Handoff — D2-NOTE-V2-1-WASOW-FULL-CLOSURE
       **Date:** <TODAY>
       **Agent:** GitHub Copilot (VS Code)
       **Session duration:** <N> minutes
       **Status:** <UPGRADE_V2_1_FULL | UPGRADE_V2_1_PARTIAL_PAGECOUNT
                    | UPGRADE_V2_1_PARTIAL | HALTED>

       ## What was accomplished
       [2-5 sentences: what was asked (close F1 + Wasow Q20),
        what was delivered (v2.1 PDF at X pp + Borel-summability
        chain via B-T 1933 §§4-6 + retired prompt 7 verdict)]

       ## Key numerical findings
       - v2.1 PDF page count: <X> pp
       - v2.1 PDF SHA-256: <hash>
       - Build clean across pdflatex passes 1, 2, 3 + bibtex: <yes/no>
       - 0 unresolved citations / undefined references: <yes/no>
       - New bib entries added: <birkhoff_trjitzinsky_1933 [+ optionally
                                  lodayrichaud2016divergent / costin2008asymptotics]>
       - AEAL claim count delta: <baseline 14 → final N>

       ## Judgment calls made
       [Any decision made autonomously not specified in the prompt.
        E.g.: "Loday-Richaud not on disk; cited B-T 1933 §§4-6 alone
        per Rev-A grant." Be specific. If none: "None."]

       ## Anomalies and open questions
       [MOST IMPORTANT SECTION. Anything unexpected, uncertain, or
        that should be reviewed by Claude.
        E.g.: "Phase B Lemma proof B.2 omitted the multiplicity-2
        edge remark per the spec's NOTE; alternative reading
        suggests this is the source of the c=±d/β_d^{1/d} pair —
        flagging for synthesizer."
        If none detected: "None detected."]

       ## What would have been asked (if bidirectional)
       [Questions the agent would have asked mid-session if possible.
        If none: "None."]

       ## Recommended next step
       [E.g.: "Operator: deposit v2.1 as new version on concept DOI
        19996689 per F.3 runbook; flip SQL todo
        prompt-d2-note-v2-1-wasow-full-closure-fire ⇒ done; flip
        prompt-7-wasow-q20-full-closure-fire ⇒ done (merged)."]

       ## Files committed
       [List every file in sessions/<TODAY>/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/]

       ## AEAL claim count
       <N> entries written to claims.jsonl this session
       (≥ 14 carried-forward + ≥ 4 new for v2.1, target ≥ 18 total)
       ---

B4 — Commit + push. Conventional commit message:
       D2-NOTE-V2-1-WASOW-FULL-CLOSURE — close F1 + Wasow
       Q20 (UPGRADE_V2_1_FULL); v2.1 ~10pp; Rev-A..Rev-H minus
       Rev-C(b) applied (Rev-E PARTIAL, not full); SHA <prefix>

     git add sessions/<TODAY>/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/
     git commit -m "<message>" -m "Co-authored-by: Copilot
       <223556219+Copilot@users.noreply.github.com>"
     git push origin main

B5 — Output exactly two lines:

       BRIDGE: https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/<TODAY>/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/
       CLAUDE_FETCH: https://raw.githubusercontent.com/papanokechi/siarc-relay-bridge/main/sessions/<TODAY>/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/handoff.md

If git push fails: zip deliverables as
`<TASK_ID>_<TODAY>.zip`, note failure in handoff.md under
Anomalies, output `BRIDGE_FAILED: zip saved at <local_path>`.
Do not retry more than once.

================================================================
§8 OUT OF SCOPE
================================================================

  - Re-running the Phase A* d-sweep (the Q20A cached results
    are sufficient; this prompt does NOT touch
    `phase_a_star_extended_sweep.py`)
  - New mpmath / SymPy numerical pipelines of any kind
  - Acquiring B-T 1933 — that was QS-A, already DONE
  - Loday-Richaud 2016 / Costin 2008 acquisition (Tier 2;
    relay agent does NOT acquire; if not on disk, Phase C
    proceeds with B-T 1933 alone per Rev-A grant)
  - Acquiring Adams 1928, Okamoto 1987, Conte-Musette 2008,
    Lisovyy-Roussillon (these are gated on different
    prompts: G3b operator workflow, Prompt 015, etc.)
  - Driving the Zenodo new-version deposit (operator does
    this manually with the v2.1 runbook; per Rule 2 the
    relay agent does NOT use API keys or browser automation
    against Zenodo)
  - Driving the arXiv submission (operator decides Q31 +
    runs the arXiv form manually; per Rule 2)
  - Modifying the v2 source `d2_note_v2.tex` in
    `sessions/2026-05-03/Q20A-PHASE-C-RESUME/d2_note_v2/`
    (read-only; Phase E.0 copies it into the session before
    editing; the bridge already has v2's frozen state)
  - Modifying any other published SIARC artefact (PCF-1
    v1.3, PCF-2 v1.3, CT v1.3, T2B v3.0, SIARC umbrella
    v2.0; those are post-publish and locked)
  - Touching `tools/pii_check.py` or the standing PII
    discipline scripts (these are test-only inputs)
  - Picture v1.14 → v1.15 amendment (synthesizer-side; a
    future pass absorbs THIS task's verdict; out of scope
    for the relay agent)

================================================================
END OF RELAY-PROMPT BODY  (operator-paste boundary)
================================================================
```

---

## Synthesizer notes (NOT part of the operator-paste body)

### Why this is one prompt, not two

Per Q-S3, prompt 7 (Wasow Q20 full-closure synthesizer arbitration)
is ABSORBED. The Wasow-arbitration verdict that prompt 7 would
have produced is identical to what Phase C / Phase D produce here:
the Borel-summability chain via B-T 1933 §§4–6 either closes
(publication-grade proof) or it doesn't. There is no separate
"Wasow Q20 closure" task remaining once this prompt fires; running
both would re-do the same literature reading twice.

### Why not v3 / fresh concept DOI

Per Q-S2, v2.1 is a NEW VERSION on the existing Zenodo concept
DOI 19996689, not a fresh concept. The mathematics is unchanged;
the citation chain is closed, and the artefact is expanded for
self-containment. Zenodo's new-version flow preserves the concept
DOI and gives the new artefact its own version DOI. No "supersede"
language is appropriate.

### Why theorem framing is retained (not demoted)

Per Q-S1, with the citation chain closed by Rev-A, the residual
that motivated "theorem-with-documented-residual" no longer exists.
"Theorem 4.1" stays a theorem. Demoting it would over-correct.

### Tier-2 sources (Loday-Richaud, Costin) are optional AND ethics-gated

If the operator hasn't acquired Loday-Richaud 2016 ch. 2 or Costin
2008 ch. 5 by fire time, the relay proceeds with B-T 1933 alone.
Synthesizer Rev-A grants single-source closure. Per Phase C.4's
ethics gate, the relay agent does NOT add Tier-2 entries to the
bib unless it has opened the file and verified the chapter
content matches the F1-closure topic. Unconsulted Tier-2 sources
are mentioned only in the handoff "Anomalies and open questions"
section as "modern restatements suggested by synthesizer review,
not consulted in this session" — making the unconsulted-but-
recommended status explicit without misrepresenting consultation.

### Page-count budget

v2 is 6 pp. v2.1 is targeted at 9–12 pp via:
  - Rev-E (i):  +1 page (d=2 self-contained reproduction)
  - Rev-E (ii): +0.5 page (B_d definition + worked specialisations)
  - Rev-E (iii):+0.5 page (Falsification context promoted)
  - Rev-G:      +0.5 page (q = (d+2)/2 derivation expanded)
  - Rev-F:      +1 page  (Appendix A)
  - Rev-B:      +0.3 page (Lemma + proof body)
  - Rev-A + Rev-C(a): +0.5 page (chain expanded in proof of
                                  Theorem 4.1)
  - Rev-H footnotes: ≤ +0.2 page total
Net: 6 + ~4.5 = ~10.5 pp; the [9, 12] gate accommodates ±1
page of LaTeX flow variation.

### What the operator should look for at inspection

1. The relay-prompt body in the code block above is what
   gets pasted; the markdown around it is for synthesizer-
   review only.
2. <TODAY> placeholders in the prompt body are filled at
   firing time, not before.
3. The prompt does NOT depend on Loday-Richaud / Costin being
   on disk — Tier 2 is optional. If they ARE on disk, the
   "see also" citations land naturally.
4. The §4 halt conditions are the safety net; if any fires,
   the operator gets a clean halt log to triage.
5. The Standing Final Step (§7) closes the loop on the bridge.

### Recommended firing order at next compute window

1. (DONE) QS-A — B-T 1933 acquisition. ✅
2. (NEXT) QS-2 — this prompt. Operator inspects this spec,
   then pastes the relay-prompt body into a fresh CLI session.
3. (POST-QS-2) Operator-side Zenodo new-version deposit per
   `zenodo_upload_d2_note_v2_1_runbook.md` produced by F.3.
4. (POST-DEPOSIT) Picture v1.15 amendment (synthesizer-side)
   absorbing QS-2 verdict; closes M9 gating reduction
   unconditionally if UPGRADE_V2_1_FULL.
5. (PARALLEL with 4) Q31 (arXiv classification confirmation)
   + future arXiv-mirror task on v2.1.

### Synthesizer disclaimer

This spec was drafted by the Copilot CLI (Claude Opus 4.7
xhigh) from picture v1.14 §24 + the v2 source + the runbook-
canonical literature directory + retired prompt 7's stated
Wasow Q20 closure goal. It has NOT been reviewed by Claude
(synthesizer) before operator inspection; the operator may
choose to forward this spec to claude.ai for a synthesizer-
review pass before firing. Recommended.

---

## Provenance

- **Drafted from:** picture v1.14 (`tex/submitted/control center/picture_revised_20260503.md` §24 v1.13→v1.14 amendment log)
- **Anchored to:** `sessions/2026-05-03/Q20A-PHASE-C-RESUME/` (v2 source + Phase A* sweep + claims baseline)
- **Literature anchored to:** `tex/submitted/control center/literature/g3b_2026-05-03/SHA256SUMS.txt` (slot 01 + slot 03 + slot 04, all 6/6 hashes verify OK)
- **Pre-firing dependency:** SQL todo `g3b-acquire-bt-1933` ⇒ done (post-QS-A); SQL todo `prompt-d2-note-v2-1-wasow-full-closure-fire` ⇒ pending (this spec); SQL todo `prompt-7-wasow-q20-full-closure-fire` ⇒ MERGED (Q-S3); operator confirms readiness before firing.
- **Drafted-by:** Copilot CLI (Claude Opus 4.7 xhigh), 2026-05-03, synthesizer-side prompt drafting task `PRE-DRAFT-D2-NOTE-V2-1-WASOW-FULL-CLOSURE-PROMPT`.
