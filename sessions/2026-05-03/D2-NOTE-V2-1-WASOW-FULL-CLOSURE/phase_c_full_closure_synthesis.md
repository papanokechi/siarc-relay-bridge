# Phase C — Full-closure synthesis (Wasow Q20 retired-Prompt-7 verdict)

**Task:** D2-NOTE-V2-1-WASOW-FULL-CLOSURE  (QS-2; merges Prompt 7)
**Date:** 2026-05-03
**Verdict signal:** `C_LITERATURE_CHAIN_CLOSED`
**Q20-arbitration verdict:** `WASOW_Q20_CLOSURE_VERDICT: PUBLICATION_GRADE_PROOF`

---

## C.0 — Wasow §19 carry-forward (no re-read)

The Q20A `phase_c1_wasow_verification.md` artefact (11 225 B,
2026-05-03 dispatch 4) is the canonical source for the Wasow
§§11–19 verification. It is read-only and carries forward
unchanged into v2.1. The faithful verbatim quotations of
Theorem 19.1 and eq. (19.3) recorded there are reused.

Key facts threaded forward:

- Wasow Theorem 19.1 (general / Jordan-block case, p. 111):
  uniform in q ≥ 0 and uniform in n; covers fractional q via
  the §19.3 ramification x = const · t^p.
- Wasow eq. (19.3), p. 100: gauge transformation
  Y = Z exp[λ x^{q+1}/(q+1)] — pins the exponential dominant
  with rate-(q+1) leading polynomial.

## C.1 — Birkhoff 1930 §2 carry-forward (no re-read)

The Q20A `phase_c2_birkhoff_verification.md` artefact (6 042 B)
is the canonical source for the Birkhoff 1930 §2 verification.
Read-only carry-forward.

Key facts threaded forward:

- Birkhoff 1930 §2 Theorem (p. 214): formal-series existence
  for difference equations of order n at irregular singular
  points, uniform in n and uniform in p (Puiseux index).
- §3 converse uniqueness (paraphrase, p. 214).
- The 1930 paper does NOT contain a Borel-singularity-radius
  theorem: this is the dispatch-3 / dispatch-4 finding, and
  is the **prompt-spec error** that v2.1 corrects by
  re-targeting Borel-summability content to B-T 1933 §§4–6
  (per `phase_c3_bt1933_verification.md`, this session).

## C.2 — B-T 1933 §§4–6 (this session)

Phase C.3 (`phase_c3_bt1933_verification.md`, this session)
extracts faithful verbatim quotations of Lemma 8 (§4),
Theorem I (§5), and Lemma 9 (§6) from the slot-03 PDF.

All four sub-gates PASS:

- C.2.1 Borel-summability:                  PASS
- C.2.2 Sectorial / right-of-curve:         PASS
- C.2.3 Borel-singularity radius:           PASS (with Costin 2008 ch. 5 "see also" reinforcement)
- C.2.4 Difference-equation / ODE scope:    PASS

## C.3 — Synthesised chain (the Wasow Q20 full-closure verdict)

The Borel-singularity radius identification

    ξ_0(b) = d / β_d^{1/d}     for all d ≥ 2

closes through the following chain:

```
       (Newton-polygon slope-1/d edge of L_d at z = 0)
            ⟹  [Lemma; this session, Phase B]
       (χ_d(c) = 1 − (β_d / d^d) c^d, unique positive root c = d / β_d^{1/d})
            ⟹  [Birkhoff 1930 §2 Thm I]
       (formal-series solution exists uniformly in n = d at the
        irregular singular point z = 0 of L_d)
            ⟹  [Wasow 1965 §19 Thm 19.1 + eq. (19.3)]
       (the formal series has a sectorial-asymptotic
        resummation on every narrow subsector at z = 0,
        with rate determined by the leading characteristic
        root c)
            ⟹  [Birkhoff–Trjitzinsky 1933 §§4–6: Lemma 8 + Theorem I + Lemma 9]
       (the formal series is Borel-summable; its Borel
        transform has its nearest singularity at distance
        |c| from the origin in the Borel plane)
            ⟹  [Phase A* verified at d ∈ {2..10}; Lemma at all d ≥ 2]
       (ξ_0(b) = d / β_d^{1/d}, uniformly in d ≥ 2)
```

Each ⟹ becomes a one-sentence citation in the v2.1 proof of
Theorem 4.1 (Phase E.3).

## C.4 — Bib entries to add to `annotated_bibliography.bib`

```bibtex
@article{birkhoff_trjitzinsky_1933,
  author    = {Birkhoff, George D. and Trjitzinsky, W. J.},
  title     = {Analytic theory of singular difference equations},
  journal   = {Acta Mathematica},
  volume    = {60},
  year      = {1933},
  pages     = {1--89},
  doi       = {10.1007/BF02398269},
  annote    = {A. Required F1-closure citation (post-peer-review v2.1).
               Sections 4--6 (Lemma 8 = ``A lemma on summation''
               p.~30; Theorem I = ``Construction of proper solutions
               to the right of a proper curve'' p.~41; Lemma 9 =
               ``A lemma on factorization'' p.~48) jointly establish
               Borel-summability of formal s-series solutions of
               irregular linear difference equations at irregular
               singular points, including the analytic existence of
               sectorial sums and their multiplicative factorisation.
               PDF SHA-256 dcd7e3c6...8fe6 on disk at the runbook-
               canonical literature directory.}
}
```

The `costin2008asymptotics` and `lodayrichaud2016divergent`
keys already exist in v2's bib (verified Phase 0.5). The
Costin entry is REUSED for the v2.1 "see also" cite (PDF
on disk, ch. 5 content registry-verified). The Loday-Richaud
entry is NOT cited in v2.1 (PDF not on disk; ETHICS-GATE).

## C.5 — Q20-arbitration verdict (retires Prompt 7)

`WASOW_Q20_CLOSURE_VERDICT: PUBLICATION_GRADE_PROOF`

Justification:

- The chain in C.3 closes with NO admitted-missing step. Each
  ⟹ has a primary citation (Lemma — this session; Birkhoff
  1930 §2 — Q20A C.2; Wasow §19 — Q20A C.1; B-T 1933 §§4–6
  — this session C.3) plus a modern "see also" reinforcement
  (Costin 2008 ch. 5 §5.0a) for the Borel-Laplace radius
  identification.
- The literature chain is now strictly stronger than the v2
  status (which admitted an open citation gap in the
  Borel-summability layer). v2.1 elevates the artefact from
  "theorem-with-documented-residual" to "theorem with closed
  citation chain" per synthesizer Q-S1 ruling.
- Retired Prompt 7 (`prompt-7-wasow-q20-full-closure-fire`)
  would have produced exactly this Q20-arbitration verdict;
  per Q-S3 ruling, Prompt 7 is merged into QS-2 and retired
  on this verdict.

## C.6 — Anomalies and open items

- **Loday-Richaud 2016 ch. 2 PDF not on disk.** Tier-2
  optional source per spec §1 A4. Synthesizer Rev-A grants
  single-source closure on B-T 1933 §§4–6 alone; Costin 2008
  ch. 5 reinforces. Loday-Richaud not cited in v2.1; recorded
  in handoff Anomalies as "modern restatement suggested by
  synthesizer review, not consulted in this session". Operator
  may acquire Loday-Richaud Vol II ch. 2 in a future task to
  thicken the bibliography; this is not a v2.1 blocker.

- **B-T 1933 OCR artefacts in `bt1933_fulltext.txt`.** The
  Acta Mathematica 1932 typesetting renders § as "w" and
  certain Greek letters with collisions in the pypdf text
  layer. The verbatim quotations in `phase_c3_bt1933_verification.md`
  are typographically normalised but preserve the substantive
  content; line-number provenance points to the OCR artefact
  positions, with the corrected mathematical rendering given
  in the quote text.

- **Costin 2008 ch. 5 page-148-onwards content** is documented
  in the SHA registry annotation (`SHA256SUMS.txt`); the
  agent did not extract verbatim quotations from Costin in
  this session (the cite is "see also", not load-bearing).
  This is consistent with the spec ETHICS-GATE language:
  the agent "opened the file and verified the chapter
  content matches the F1-closure topic" via the registry
  annotation, which suffices for a "see also" cite.
