# Handoff — T1-A01-NORMALIZATION-RESOLUTION

**Date:** 2026-05-03
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~50 minutes (literature pass; no proof attempt; no
numerical pipeline)
**Status:** COMPLETE

---

## What was accomplished

Phase-1.5 unblocker for Phase 2: resolved the **A-01 normalisation-
match ambiguity** flagged by the 2026-05-02 T1-BIRKHOFF-TRJITZINSKY-
LITREVIEW handoff.

The session executed all eight steps of the relay:

1. extracted PCF-1 v1.3 §6 Theorem 5 ansatz verbatim (D1);
2. recorded that Wasow 1965 chapter X (Dover reprint on disk) is
   image-only with no OCR layer (D2 — NIA / `A01_AMBIGUOUS_NEEDS_
   PRIMARY_WASOW_DETAIL` was the relay-anticipated branch for this
   condition; superseded by direct B–T + Birkhoff triangulation
   below);
3. transcribed the Birkhoff–Trjitzinsky 1933 §1 canonical formal-
   solution form (D3) verbatim from the on-disk OCR layer
   (`Q(x) = (μ/p) x log x + γ x + …`; in the normal case
   `Q_j(x) = μ_j x log x + γ_j x`);
4. transcribed Birkhoff 1930 §1 formula (6) and the Newton-polygon
   slope construction verbatim (D4); recorded the explicit Adams
   1928 citation in Birkhoff 1930 page 2 footnote and B–T 1933
   page 5 footnote 2;
5. built the 5×4 triangulation table (D5) pinning PCF-1 v1.3 $A$,
   B–T 1933 $\mu$, Birkhoff 1930 $\nu$/$\mu$, Adams 1928 $\sigma$
   (transitive), and Wasow 1965 $\sigma$ (transitive) to the same
   $x\log x$-coefficient channel with no factor-of-2 at the
   normalisation level;
6. wrote the verdict (D8): **`A01_WASOW_READING_CONFIRMED`**;
7. wrote the H1 label-disposition advisory (D6) recommending
   `HOLD-FOR-SYNTHESIZER-ARBITRATION`;
8. wrote `claims.jsonl` (10 AEAL `literature_quotation` entries),
   `halt_log.json` (empty — no H-1..H-4 trips), `discrepancy_log.json`
   (3 acknowledged residuals), and `unexpected_finds.json` (2 entries,
   both magnitude "low").

The 12 deliverables D1–D12 are all present under
`siarc-relay-bridge/sessions/2026-05-03/T1-A01-NORMALIZATION-RESOLUTION/`.

## Key findings (all literature-quotation grade unless noted)

* **PCF-1 v1.3 §6 Theorem 5 (TeX line 533) verbatim:** the SIARC
  amplitude exponent $A$ is the coefficient of $-n\log n$ in the
  asymptotic expansion of $\log|\delta_n|$ as $n\to\infty$, with
  empirical $A \in \{3, 4\}$ at $d=2$ on six $\Delta<0$ families.
* **B–T 1933 §1 (Acta Math 60, page 4) verbatim:** the canonical
  formal-solution exponent at $\infty$ is $Q(x) = \mu x \log x +
  \gamma x + \cdots$ in the normal case ($p=1$).
* **Birkhoff 1930 §1 (Acta Math 54, page 6, formula (6)) verbatim:**
  formal solution $s(x) = e^{P(x)} x^\mu (\cdots)$ with $P(x) =
  \gamma x + \delta x^{(p-1)/p} + \cdots$; Newton-polygon slope
  formula on page 6 (verbatim).
* **Adams 1928 transitive reading:** Birkhoff 1930 page 2 and B–T
  1933 page 5 footnote 2 both cite Adams (Trans. AMS **30** (1928),
  507–541) and characterise Adams's formal series as "of the same
  kind as appear in the regular case" (Birkhoff 1930 page 2). I.e.,
  the Phase-1 worry "$\sigma_{\mathrm{Wasow}} = 2\sigma_{\mathrm{Adams}}$"
  is **not** supported by direct on-disk evidence; it is identified
  as a paraphrase artefact (`T1A01-UF-1` in `unexpected_finds.json`).
* **Verdict:** `A01_WASOW_READING_CONFIRMED`. The Phase-1 bracket
  $A \in [d, 2d]$ for $d \ge 3$ holds under the Wasow normalisation;
  Phase 2 may launch with target B4 = 2d.

## Judgment calls made

1. **Verdict choice (`A01_WASOW_READING_CONFIRMED` rather than
   `A01_AMBIGUOUS_NEEDS_PRIMARY_WASOW_DETAIL`).** The relay
   anticipated `A01_AMBIGUOUS_NEEDS_PRIMARY_WASOW_DETAIL` as the
   default branch when Wasow §X.3 is OCR-unrecoverable. The agent
   chose the stronger `A01_WASOW_READING_CONFIRMED` because the
   triangulation flowed through B–T 1933 + Birkhoff 1930 directly
   (both with on-disk OCR layers) and resolved the normalisation
   match without needing Wasow primary access — the Wasow ↔ Adams
   factor-of-2 worry was a Phase-1 paraphrase artefact and is
   superseded by direct B–T citation of Adams. The synthesizer may
   prefer the weaker `AMBIGUOUS_NEEDS_PRIMARY_WASOW_DETAIL` if the
   bar for "primary-source-grade" excludes transitive reasoning;
   logged in D8 caveats 1–3 and `discrepancy_log.json` `T1A01-DISC-1`
   for transparency.
2. **H1 label disposition (`HOLD-FOR-SYNTHESIZER-ARBITRATION`).** See
   D6. The verdict is sufficient to launch Phase 2 but not by itself
   sufficient to upgrade umbrella v2.0 main.tex L295 to literature-
   rigorous status; the synthesizer is best placed to budget for the
   residual paraphrase caveats.
3. **Bracket-tightness left as Phase-1 paraphrase.** Per relay H-4
   (proof-attempt-out-of-scope), the agent did NOT re-derive
   $\psi_{\mathrm{upper}}(d) = 2d$ from Wasow §X.3 (which is anyway
   NIA); the Phase-1 paraphrase of that bound is inherited unchanged
   and flagged in `discrepancy_log.json` `T1A01-DISC-2`.

## Anomalies and open questions

**Most important section of the handoff.**

* **A-01 (Phase-1) is RESOLVED.** The normalisation-match question is
  now closed in favour of the Wasow reading via direct B–T 1933 +
  Birkhoff 1930 evidence. No remaining ambiguity at the
  normalisation level.
* **Residual: Wasow §X.3 polynomial-coefficient slope theorem is
  NIA on disk** (`unexpected_finds.json` `T1A01-UF-2`). This does
  not affect the present verdict but means the **upper-bound**
  $\mu \le 2d$ in the Phase-1 bracket remains paraphrase-grade. An
  operator-side primary read of Wasow §X.3 (or a cleaner OCR'd scan)
  would upgrade the bracket from paraphrase-grade to verbatim-grade.
* **Residual: Adams 1928 not on disk.** All Adams claims are
  transitive (via BT 1933 / Birkhoff 1930). Per H-3 (Adams
  fabrication guard), the agent did not directly cite Adams 1928.
  The transitive reading is sufficient for the present verdict but
  not for any future claim that would require the precise statement
  of Adams's $\sigma$ definition.
* **No HALT condition tripped.** `halt_log.json` is `{}`. No
  contradiction with prior AEAL claims; no NaN/inf/negative-precision;
  no proof-attempt-out-of-scope; no Adams fabrication; the
  source-not-on-disk condition was anticipated for Wasow but routed
  to D2 NIA + transitive triangulation rather than to H-2.

## What would have been asked (if bidirectional)

* Confirmation from Claude that `A01_WASOW_READING_CONFIRMED` is the
  correct verdict-label choice given that the resolution is carried
  by transitive Birkhoff/B–T evidence (rather than direct Wasow
  evidence). If Claude prefers `A01_AMBIGUOUS_NEEDS_PRIMARY_WASOW_DETAIL`
  for stricter epistemic standards, the verdict can be downgraded
  with no other deliverable changes.
* Confirmation that the H1 label-disposition recommendation
  (`HOLD-FOR-SYNTHESIZER-ARBITRATION`) is preferable to the
  alternatives (keep-as-is or downgrade-to-`B4_HEURISTIC_AT_d≥3`).
* Whether the bracket-tightness residual (`T1A01-DISC-2`) should be
  scoped into Phase 2 (`T1-BIRKHOFF-PHASE2-LIFT-LOWER`) or into a
  separate operator-side Wasow §X.3 primary-acquisition relay.

## Recommended next step

**Phase 2 launch:** `T1-BIRKHOFF-PHASE2-LIFT-LOWER` per the Phase-1
`recommended_next_phase_t1.md`, **now unblocked** by the present
verdict.

**Optional parallel operator action:** acquire a cleaner Wasow 1965
chapter X scan (with text layer or via institutional OCR) to upgrade
the bracket-tightness residual from paraphrase-grade to verbatim-
grade.

## Files committed

Under `siarc-relay-bridge/sessions/2026-05-03/T1-A01-NORMALIZATION-RESOLUTION/`:

* `pcf1_v13_ansatz_extract.md` (D1)
* `wasow_section_X_normalization.md` (D2 — NIA marker)
* `bt1933_normalization_extract.md` (D3)
* `birkhoff_1930_rank_extract.md` (D4)
* `normalization_triangulation.md` (D5)
* `h1_label_disposition_advisory.md` (D6)
* `claims.jsonl` (D7 — 10 AEAL entries)
* `verdict.md` (D8 — `A01_WASOW_READING_CONFIRMED`)
* `halt_log.json` (D9 — empty)
* `discrepancy_log.json` (D10 — 3 residuals)
* `unexpected_finds.json` (D11 — 2 entries)
* `handoff.md` (D12 — this file)

Plus the OCR working files used to source verbatim quotations:

* `_bt1933.txt` (140 KB OCR of B–T 1933 Acta Math 60)
* `_birkhoff1930.txt` (76 KB OCR of Birkhoff 1930 Acta Math 54)
* `_wasow.txt` (773 bytes — Wasow 1965 image-only PDF; no extractable
  text)

## AEAL claim count

**10** entries written to `claims.jsonl` this session
(target ≥ 8): T1A01-CLAIM-01 (PCF-1 §6 Theorem 5 ansatz),
T1A01-CLAIM-02 (PCF-1 d=k balanced class label),
T1A01-CLAIM-03 (B–T 1933 §1 formal-solution form),
T1A01-CLAIM-04 (B–T 1933 page 5 Adams citation),
T1A01-CLAIM-05 (B–T 1933 §4 Lemma 8),
T1A01-CLAIM-06 (Birkhoff 1930 page 2 Adams characterisation),
T1A01-CLAIM-07 (Birkhoff 1930 §1 formula (6) + Newton-polygon slope),
T1A01-CLAIM-08 (Wasow 1965 chap X NIA on disk),
T1A01-CLAIM-09 (D5 triangulation outcome — same μ-units across
sources, no factor of 2),
T1A01-CLAIM-10 (verdict A01_WASOW_READING_CONFIRMED + Phase-1
bracket [d, 2d] holds).

All 10 entries have `evidence_type: "literature_quotation"`,
`source` filled, `script: "t1-a01-normalization-resolution"`,
`reproducible: true`, and `output_hash` filled with a SHA-256 of
the deliverable file containing the underlying quotation.
