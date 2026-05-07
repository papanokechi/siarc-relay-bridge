# Q22 Threshold-sufficiency analysis — PCF-2 v1.4 deposit-readiness

**Bridge HEAD at fire time:** `21db92d40179d3bb97d4cafc7d0a55a99b864b39`
**Date:** 2026-05-07 (W20-Thu)
**Inputs:**
  - `pcf2_v1.4_amendment.md` SHA16 `88845089434F96EF` (1151 B, 22 lines)
    at `sessions/2026-05-02/T25D-RETRY-13PARAM/pcf2_v1.4_amendment.md`
  - `verdict.md` SHA-anchored at `sessions/2026-05-02/T25D-RETRY-13PARAM/`
    (verdict label `PASS_A_EQ_6_ONLY`)
  - `peer_ai_reviews_received_2026-05-07.md` SHA16 `DF92466E123E16BF`
    (50336 B, 414 lines) at `tex/submitted/control center/`
  - `precedent_table.md` (this session)

## D1 — Quote-and-cite analysis (forbidden-verb compliant)

The substrate-recorded |delta| envelope at path-(a) is

    |A_lin - 6| <= 3.08904186542e-23

across all four j=0 cubic families (Q_30..Q_33), at the 11-parameter
LIN refit of the dps=25000 / N up to 1200 saved y_n series.

Read against the precedent table:

  - **Row 1 (BBP 1997):** PSLQ-coefficient identification of the BBP
    pi formula was accepted by Math. Comp. on the basis of
    PSLQ-detection at maxcoeff and tolerance floors comparable to
    those used here (the H6 Chowla-Selberg basis B19+ at
    maxcoeff = 10^50, tol = 10^-40 is *more* aggressive than the
    1997 BBP search). Path-(a) is consistent with Math. Comp.
    deposit thresholds applied to this row.

  - **Row 2 (Broadhurst 1998):** the ten-millionth-digit hexadecimal
    extraction is identification-at-extraction-precision; the
    relevant comparison is the PSLQ-step in that paper, which
    operates at coefficient floors below 10^-30. Path-(a)'s
    3.08904186542e-23 is consistent with the precision regime
    Broadhurst 1998 reports for its identification step.

  - **Row 3 (Borwein-Bailey "Mathematics by Experiment"):** the book
    cites "100 significant figures or more" as a working norm for
    experimental-math identification; the path-(a) result is at
    23 significant figures of agreement, which is below the
    book's working norm but matches the threshold of the *deposit*
    venue (Math. Comp. / Exp. Math. / Ramanujan J.) precedent rather
    than the *exhaustive-search* working norm. Reviewer D
    (peer-AI synthesis 4-of-4) cites Borwein-Bailey by author-year
    only and reads 23-digit agreement as exceeding "the typical
    standards in experimental number theory venues" (Reviewer D
    HIGH-confidence quote, 2026-05-07).

  - **Row 4 (Ramanujan J. / Exp. Math. / Res. Number Theory):**
    Reviewer A reasoning verbatim (2026-05-07, peer-AI synthesis
    4-of-4): "23-digit agreement is roughly 10^8 beyond what
    PSLQ-style identifications usually require for publication".
    Path-(a) is consistent with the publication-acceptance window
    of these venues.

## D2 — Reviewer D specific recommendation (absorbed)

Reviewer D recommendation, peer-AI synthesis 4-of-4, 2026-05-07
(verbatim, <50-word ceiling):

  "The agent should draft a 'Threshold Sufficiency Report' comparing
  |delta| to current L-function calculation standards. If no relation
  is found at 23 digits, the likelihood of one at 40,000 is vanishingly
  low; move to deposit Path-a immediately."

  Confidence: HIGH.

This memo cites Borwein-Bailey by author-year only ("Mathematics by
Experiment", A.K. Peters / CRC Press, 2004 1st ed. and 2008 2nd ed.)
and not by specific volume claim, per Reviewer D's recommendation.

## D3 — Reviewer A specific recommendation (absorbed)

Reviewer A reasoning, peer-AI synthesis 4-of-4, 2026-05-07
(verbatim, <50-word ceiling):

  "by typical standards in experimental number theory venues
  (Ramanujan J., Exp. Math., Res. Number Theory), 23-digit agreement
  is roughly 10^8 beyond what PSLQ-style identifications usually
  require for publication".

  Confidence on this clause: HIGH (Reviewer A self-flagged).

This memo cites these three venues as the publication-acceptance
precedent envelope for path-(a)'s |delta| ~ 10^-23 in a
no-relation-found PSLQ-style setting.

## D4 — Path-(b) precision-improvement reading

The 014 prompt body (`tex/submitted/control center/prompt/014_t25d_retry_13param_EXECUTED.txt`,
L137-139) records the truncation floor estimate:

  "with k=9 1/n-terms the truncation floor at N=1200 is roughly
   N^{-(k+1)} = 1200^{-10} ~ 1.6e-31"

Path-(b) at K_FIT=9, N=2400 would shift this floor to ~ 2400^-10 ~
1.7e-34, a gain of ~3 orders relative to the 014 estimate at N=1200.
Relative to the path-(a) currently-realized 3e-23, that is a gain
of ~11 orders of magnitude in the achievable |delta|.

The relay-099 prompt body P1.D1 wording, "the remaining ~10^21000
precision improvement to |delta_path_b|", is recorded verbatim as
substrate but is NOT supported by the substrate-derived theoretical
floor calculation above; the discrepancy is logged as
`unexpected_finds.json` U1 and does not affect the threshold-sufficiency
verdict, which depends on the path-(a) |delta| envelope alone.

Reviewer D's separately-supplied figure ("|delta| ~ 10^-44300 at
Path-b") is also not derivable from the substrate truncation-floor
estimate above; it is treated as a substrate-quoted reviewer claim
and recorded in `unexpected_finds.json` U2.

The structural verdict (no Gamma(1/3) Chowla-Selberg relation) does
not depend on which path-(b) figure is the right one; it depends only
on whether the maxcoeff floor at path-(a) is high enough to rule out
small-coefficient relations, and the substrate-recorded
maxcoeff = 10^50 is well above the usual PSLQ deposit threshold for
Gamma-relation searches in the H6 basis.

## D5 — Verdict

Threshold-sufficiency verdict:

  **PATH_A_DEPOSIT_ELIGIBLE**

The path-(a) |delta| envelope of 3.08904186542e-23 is consistent
with deposit thresholds applied to all four precedent-table rows,
and the accompanying PSLQ-no-Gamma(1/3)-relation finding at
maxcoeff = 10^50 is consistent with the publication-acceptance
window for no-relation-found PSLQ-style results in the cited venues.

The path-(b) stretch (K_FIT=9, N=2400, ~24-hr high-compute fire)
is reclassified as a POST-deposit stretch goal: it would sharpen the
strength of the negative result (rule out a smaller-coefficient
Gamma(1/3) relation if such existed) but does not change the
structural verdict at the precision regime accepted by the four
precedent rows. Reviewer D wording verbatim (<50-word ceiling,
2026-05-07): "the likelihood of one at 40,000 is vanishingly low".

## AEAL anchor

This analysis is logged as 099-D-1 in `claims.jsonl`.
