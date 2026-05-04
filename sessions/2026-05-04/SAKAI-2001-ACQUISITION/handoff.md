# Handoff — SAKAI-2001-ACQUISITION
**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~50 minutes
**Status:** COMPLETE

## Verdict

**UPGRADE_SAKAI_ACQUIRED_W_HOMOMORPHISM_NOT_IN_SAKAI**

Sakai 2001 acquired (Kyoto Math Dept 1999 preprint, slot 13;
SHA-256 `ec1bbda3...49ed6`). D_6^{(1)} surface classification
+ W((2A_1)^{(1)}) generators extracted. CT v1.3 §3.5 4-tuple
(1/6, 0, 0, -1/2) confirmed NOT a direct Sakai parameter point
under naive identification (replicates and re-anchors the
2026-05-04 OKAMOTO-1987-CONSTRAINT-PIN G18 closure). Explicit
W(B_2) ↔ W((2A_1)^{(1)}) homomorphism is **NOT** stated in
Sakai 2001 — M6 Phase B.5 anchor is partial; follow-on
(Noumi-Yamada 2004 or Witte-Forrester 2010 lecture notes)
recommended.

## What was accomplished

(a) Confirmed Sakai 2001 bibliographic identity: H. Sakai,
    "Rational surfaces associated with affine root systems and
    geometry of the Painlevé equations", Comm. Math. Phys. 220
    (2001) no. 1, pp. 165–229, DOI 10.1007/s002200100446
    (received 18 Sep 1999; accepted 29 Jan 2001; advisor
    Michio Jimbo per Math Genealogy). Confirmed it is the
    canonical surface-classification source cited by BLMP 2024
    (slot 08).

(b) Probed seven OA routes (B.1–B.7). The Springer DOI route
    is paywalled; per Rule 1 not auto-authenticated. Project
    Euclid CMP archive returns a security challenge. arXiv
    has no Painleve-Sakai preprint of this paper. The Kyoto
    University Mathematics Department preprint server hosts
    the **1999 preprint** (preprint 1999 No. 10) at
    `https://www.math.kyoto-u.ac.jp/preprint/99/10.ps` —
    successful OA route.

(c) Acquired the PostScript file (1,149,707 bytes, SHA-256
    `3a185984...0c12`), converted via ps2pdf (MiKTeX 64-bit)
    to a 55-page PDF (526,933 bytes, SHA-256
    `ec1bbda3...49ed6`), verified clean ASCII text-layer
    extraction at ≥ 99% fidelity via `pdftotext.exe -layout`.

(d) Deposited as slot 13 at `tex/submitted/control center/
    literature/g3b_2026-05-03/13_sakai_1999_preprint_kyoto99_10.pdf`
    with 17-line provenance comment block in SHA256SUMS.txt.

(e) Read targeted sections (extracts.md):
    - **D.1.a** Table 6 (preprint p. 30): D_6^{(1)} surface ↔
      P_III^{D_6^{(1)}} ↔ Aut(D_6^{(1)}) ⋉ W((2A_1)^{(1)}).
    - **D.1.b** P_III^{D_6^{(1)}} eqs (16)–(18); the 4-tuple
      (a_1, a_0, b_1, b_0) carries the linear constraint
      a_1+a_0 = b_1+b_0 = η.
    - **D.1.c** W((2A_1)^{(1)}) simple-reflection generators
      w_1, w_0, w_1', w_0' verbatim.
    - **D.1.c.bis** No explicit W(B_2) ↔ W((2A_1)^{(1)})
      homomorphism in Sakai 2001 (full-text grep returned
      zero matches in the relevant body).
    - **D.2** CT v1.3 4-tuple (1/6, 0, 0, -1/2) violates the
      a_1+a_0 = b_1+b_0 constraint (1/6 ≠ -1/2).

## Key numerical findings

- Sakai 2001 D_6^{(1)} parameter constraint: a_1+a_0 = b_1+b_0
  (eq. (18), preprint p. 30). Eff. parameter dimension = 3.
- CT v1.3 §3.5 4-tuple (1/6, 0, 0, -1/2): a_1+a_0 = 1/6,
  b_1+b_0 = -1/2; difference = 2/3. Constraint violated under
  naive identification.
- W((2A_1)^{(1)}) is rank-4 affine: 4 simple reflections. All
  four preserve the constraint a_1+a_0 = b_1+b_0 algebraically.
- 13 AEAL claims written to `claims.jsonl`.

## Judgment calls made

1. **Slot numbering**: prompt suggested slot 13 (e.g.,
   `13_sakai_2001_CMP220.pdf`); existing slots are 01, 03,
   04, 06, 07, 08 with 02/05/09–12 as gaps. Used slot 13 with
   filename `13_sakai_1999_preprint_kyoto99_10.pdf` (preprint
   suffix to flag the version difference vs the published
   CMP).

2. **Preprint vs published version**: the Kyoto Math Dept
   preprint is the 1999 preprint; the published CMP version
   has different pagination (CMP pp. 165–229 vs preprint p.
   1–55). Math content of the surface-classification framework
   (Table 6 + D_6^{(1)} parameter labeling + W((2A_1)^{(1)})
   generators) matches the published version per BLMP 2024
   (slot 08) transitive citation. For G17 amendment / G18
   alt-origin / M6 anchor purposes, the preprint is sufficient
   as a primary source for the math content; the page-anchor
   citations should explicitly say "1999 preprint pp. X-Y;
   Comm. Math. Phys. 220 (2001) 165-229 (final published
   pagination differs)".

3. **Did NOT pursue ResearchGate / Academia.edu OA copy**
   (Phase B.7) once Phase B.4 succeeded with a clean
   publisher-independent PostScript. Avoids social-platform
   degraded-copy ambiguity.

4. **Did NOT attempt Springer auth bypass**. Rule 1 forbids
   API keys / auto-authentication. Springer login HTML
   confirmed.

5. **Surface-vs-W-symmetry distinction**: the prompt phrasing
   "W(D_6) affine-Weyl group action" is folklore-shorthand
   that conflates the surface type label (D_6^{(1)}) with the
   W-symmetry group (W((2A_1)^{(1)}) = W(D_6^{(1)})⊥). Sakai's
   classification rule (preprint L1006) is `D_6^{(1)}⊥ =
   (2A_1)^{(1)}` — the symmetry group of the D_6^{(1)} surface
   is W((2A_1)^{(1)}), NOT W(D_6^{(1)}). I report Sakai's
   convention faithfully and flag the prompt's phrasing as
   shorthand in this handoff.

## Anomalies and open questions

**THIS IS THE MOST IMPORTANT SECTION** — flagged for Claude
review.

1. **Surface-label vs W-symmetry label terminology
   (cross-cycle alert)**: the prompt phrasing
   "W(D_6) affine-Weyl group action on P_III(D_6)" is
   shorthand. In Sakai 2001 the *surface type* is D_6^{(1)}
   (the type of the unique anti-canonical fiber), but the
   *Cremona / Bäcklund symmetry group* is W((2A_1)^{(1)}).
   These are different. Future relay prompts touching the
   D_6 P_III' surface should use the Sakai-2001-canonical
   notation
     "Aut(D_6^{(1)}) ⋉ W((2A_1)^{(1)})-symmetry on the
      D_6^{(1)} surface"
   to avoid ambiguity. Flagged for picture v1.18 §5 and
   M6 spec v1.1.

2. **W(B_2) ↔ W((2A_1)^{(1)}) cross-walk literature gap**:
   the prompt anticipated Sakai 2001 might explicitly state
   the homomorphism. It does NOT. Sakai cites Okamoto 1987
   only as bibliographic reference [20], without
   Weyl-group correspondence. M6 spec Phase B.5 anchor
   strength is therefore PARTIAL, not strong. Recommend a
   follow-on prompt to acquire **Noumi-Yamada 2004** ("Affine
   Weyl group symmetries in Painlevé type equations" /
   "Tropical Robinson-Schensted-Knuth correspondence and
   birational Weyl group actions") or **Witte-Forrester 2010**
   lecture notes (whichever the synthesizer can locate as
   OA), which are the canonical sources for the cross-walk.

3. **Preprint vs published version**: the math is the same
   per BLMP 2024 transitive citation, but the page anchors
   differ. If a citation lands in a paper, the synthesizer
   must decide whether to cite the 1999 preprint (with
   preprint page anchors) or the 2001 published version
   (with CMP page anchors). My recommendation: cite "Sakai,
   Comm. Math. Phys. 220 (2001) 165-229 [preprint:
   Kyoto Math 1999 No. 10]" with the 1999 preprint page
   anchors as a secondary parenthetical, until the published
   version is independently acquired (ILL via library).

4. **Replication of OKAMOTO-1987-CONSTRAINT-PIN G18
   closure**: Sakai 2001 acquisition INDEPENDENTLY confirms
   what Okamoto 1987 already showed — the CT v1.3 §3.5
   4-tuple (1/6, 0, 0, -1/2) is not a parameter point in
   either Sakai's W((2A_1)^{(1)}) framing or Okamoto's
   W(B_2) framing under naive component-wise identification.
   The labeling-correspondence artifact is now triangulated
   across **two** independent primary sources (Okamoto 1987
   slot 07 + Sakai 2001 slot 13), strengthening the G18
   closure verdict.

## What would have been asked (if bidirectional)

- "Should I additionally probe Noumi-Yamada 2004 in the same
  session, or queue it as a separate follow-on?" — I deferred
  to the prompt's §6 out-of-scope rule (Noumi-Yamada
  acquisition is explicitly listed as out of scope here, with
  a follow-on flagged) and queued a recommendation for the
  next relay.

## Recommended next step

Queue **NOUMI-YAMADA-2004-ACQUISITION** as the next relay
prompt: target either
  - Noumi & Yamada, "Affine Weyl group symmetries in Painlevé
    type equations", or
  - Witte & Forrester, "Painlevé I-VI: a primer" lecture notes,
extract the explicit W(B_2) ↔ W((2A_1)^{(1)}) homomorphism
(M6 spec Phase B.5 anchor strength upgrade from partial to
strong), and use it to draft the picture v1.18 amendment for
the surface-label-vs-W-symmetry-label terminology issue
flagged in Anomaly #1.

Strategic implications:
- **G17 amendment deepening**: Sakai 2001 §_surfaces (Table 6)
  is now available as a 2nd primary source (alongside BLMP
  2024 §4.1) for the layer-separation language in CT v1.4
  §3.5 amendment. G17 anchor strength goes from "1 primary
  source" (BLMP 2024 transitive) to "2 primary sources"
  (BLMP 2024 + Sakai 2001 direct).
- **G18 alternative origin pin**: Sakai 2001 surface
  classification confirms the CT v1.3 4-tuple is not in
  Sakai's labeling either; G18 closure as labeling-
  correspondence artifact now triangulated across TWO
  primary sources (Okamoto + Sakai). G18 closure verdict
  is independently re-anchored.
- **M6 Phase B.5**: anchor PARTIAL; needs Noumi-Yamada or
  Witte-Forrester follow-on for the explicit W cross-walk.

## Files committed

Under `sessions/2026-05-04/SAKAI-2001-ACQUISITION/`:
- `prompt_spec_used.md` — Phase 0 verbatim relay-prompt body
- `route_findings.md` — Phase B per-route OA-acquisition log
- `extracts.md` — Phase D D_6^{(1)} surface labels +
  W((2A_1)^{(1)}) generators + W(B_2) homomorphism status +
  cross-validation matrix
- `claims.jsonl` — 13 AEAL claims (literature_citation,
  deposit_confirmation, literature_quotation, computation)
- `halt_log.json` — empty (no halt conditions triggered)
- `discrepancy_log.json` — empty (no discrepancies)
- `unexpected_finds.json` — 2 info-severity finds
  (Kyoto-Math-Dept-preprint-server route + B_2 cross-walk
  literature gap)
- `sakai_1999_preprint99_10.ps` — original PostScript
  (1,149,707 bytes; SHA-256 `3a185984...0c12`)
- `sakai_1999_preprint99_10.pdf` — converted PDF (526,933
  bytes; SHA-256 `ec1bbda3...49ed6`)
- `sakai_1999_preprint99_10.txt` — pdftotext output
  (clean ASCII; for future grep)
- `handoff.md` — this file

Out-of-tree updates (literature workspace):
- `tex/submitted/control center/literature/g3b_2026-05-03/`
  - `13_sakai_1999_preprint_kyoto99_10.pdf` — slot 13 deposit
  - `SHA256SUMS.txt` — appended 17-line provenance comment +
    SHA-256 entry for the slot 13 PDF.

## AEAL claim count

**13 entries** written to `claims.jsonl` this session.
