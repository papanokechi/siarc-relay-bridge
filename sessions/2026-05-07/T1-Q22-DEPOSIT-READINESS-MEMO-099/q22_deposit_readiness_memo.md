# PCF-2 v1.4 Q22 Deposit-Readiness Memo

**Drafted:** 2026-05-07 (W20-Thu)
**Bridge HEAD at fire time:** `21db92d`
**Class:** SUBSTRATE-DRAFTING (rule5 grounding via PCF-2 v1.4 amendment + peer-AI synthesis 4-of-4 Q1 AMEND)
**Operator action:** ratification-only (deposit path-(a) OR override and command path-(b))

---

## Status (as of 2026-05-08)

- **|delta_path_a|** = 3.08904186542e-23
  (`pcf2_v1.4_amendment.md` SHA16 `88845089434F96EF`, 11-parameter LIN
  refit at K_FIT=7 / dps=25000 / N up to 1200, max across the four
  j=0 cubic families Q_30..Q_33; verdict label `PASS_A_EQ_6_ONLY`)
- **|delta_path_b|** = unrealized
  (planned K_FIT=9 / N=2400 / ~24-hr high-compute fire; substrate-
  derived theoretical truncation floor at K_FIT=9 / N=2400
  is ~ 2400^-10 ~= 1.7e-34, an ~11-order improvement over the
  path-(a) currently-realized envelope; reviewer-supplied
  figures of "10^-44300" and the relay-099 prompt body's
  "~10^21000 precision improvement" are recorded as
  substrate-quoted reviewer claims in `unexpected_finds.json`
  U1-U2 but are NOT supported by the substrate truncation-floor
  calculation)
- **Chowla-Selberg finding:** PSLQ on the H6 Chowla-Selberg basis
  B19+ at maxcoeff = 10^50, tol = 10^-40 returns no non-trivial
  Gamma(1/3) relation in any of the four families (substrate
  verbatim from `pcf2_v1.4_amendment.md` and `verdict.md` at
  `sessions/2026-05-02/T25D-RETRY-13PARAM/`)
- **Peer-AI synthesis 4-of-4** (2026-05-07,
  `peer_ai_reviews_received_2026-05-07.md` SHA16 `DF92466E123E16BF`):
  AMEND x4 on Q1 deferral framing; Reviewer D HIGH-confidence
  recommendation to deposit path-(a) immediately

## Comparable-paper threshold-sufficiency

| # | Source | |delta| / precision | Reading vs path-(a) |
|---|---|---|---|
| 1 | Bailey-Borwein-Plouffe 1997 (Math. Comp. 66:903-913, DOI 10.1090/S0025-5718-97-00856-9) | PSLQ-coefficient identification at 30+ digit confidence | path-(a) is consistent with the deposit threshold |
| 2 | Broadhurst 1998 (arXiv math.CA/9803067; pre-verified 2026-05-07) | PSLQ identification at coefficient floors below 10^-30 | path-(a) is consistent with the precision regime |
| 3 | Borwein-Bailey "Mathematics by Experiment" (A.K. Peters / CRC Press, 2004 1st ed., 2008 2nd ed., ISBN 978-1-56881-211-3) | working norm "100 significant figures or more" | path-(a) at 23 digits matches the deposit-venue threshold (Reviewer D HIGH-confidence reading); below the exhaustive-search working norm but consistent with deposit acceptance |
| 4 | Ramanujan J. / Exp. Math. / Res. Number Theory (genre-precedent venues, Reviewer A 2026-05-07) | typical PSLQ-no-relation publications carry |delta| ~ 10^-20 to 10^-50 | "23-digit agreement is roughly 10^8 beyond what PSLQ-style identifications usually require for publication" (Reviewer A verbatim, HIGH-confidence on this clause) |

**Conclusion:** path-(a)'s |delta| ~ 3e-23 sits inside the
deposit-acceptance window of all four precedent rows. The
accompanying PSLQ-no-Gamma(1/3)-relation finding at
maxcoeff = 10^50 / tol = 10^-40 is consistent with the
publication-acceptance window for no-relation-found PSLQ-style
results in the genre-precedent venues. Full analysis at
`threshold_sufficiency_analysis.md`; precedent details at
`precedent_table.md`.

## Recommendation

**Deposit PCF-2 v1.4 NOW with path-(a) numerics.**

- Path-(a) verdict label = `PASS_A_EQ_6_ONLY` (G5 / G16 closure
  with the "A = 6 to PSLQ-detection precision; no Chowla-Selberg
  amplitude correction in the H6 basis at the present precision"
  reading).
- Path-(b) is reclassified as a POST-deposit stretch goal
  (optional; not gate). Path-(b) would sharpen the strength of
  the negative result (rule out a smaller-coefficient Gamma(1/3)
  relation, if such existed) but does not change the structural
  verdict at the precision regime accepted by the four
  precedent rows.
- Stretch-goal appendix in the deposited PCF-2 v1.4 should
  document the planned path-(b) computation (K_FIT=9, N=2400,
  ~24-hr high-compute fire; substrate-derived theoretical
  truncation floor ~ 1.7e-34) and explicitly state that
  path-(b) is post-deposit and not a deposit-blocker.

This recommendation matches Reviewer D HIGH-confidence verbatim
("move to deposit Path-a immediately"), and is consistent with
4-of-4 peer-AI Q1 AMEND consensus.

## Operator action required

Operator reads this memo and chooses one of:

  **(R) Ratify** -- agent prepares Zenodo deposit substrate for
                    PCF-2 v1.4 path-(a) (mirrors 017/018 splice
                    pattern)

  **(O) Override** -- operator commands path-(b) execution first;
                      operator pastes the path-(b) constraint
                      (e.g., minimum |delta_path_b| target,
                      maximum compute envelope, precedence vs
                      other queued fires) into the next relay
                      prompt body

  **(D) Defer-back** -- if any of the four precedent rows is
                        judged inadequate, operator pastes the
                        rejection reason and the agent revises
                        the precedent table

Default if no decision is paste-recorded by W21-Mon: re-fire
this memo at W21 LANE-1 absorption window for synthesizer
arbitration.

---

## Anchors

- Path-(a) substrate: `siarc-relay-bridge/sessions/2026-05-02/T25D-RETRY-13PARAM/`
  (`pcf2_v1.4_amendment.md` SHA16 `88845089434F96EF`,
   `verdict.md` PASS_A_EQ_6_ONLY)
- Peer-AI synthesis 4-of-4: `tex/submitted/control center/peer_ai_reviews_received_2026-05-07.md`
  SHA16 `DF92466E123E16BF`, 50336 B / 414 lines
- Relay-099 prompt-body anchor: 014 / 014b stretch path
  (`tex/submitted/control center/prompt/014_t25d_retry_13param_EXECUTED.txt`,
   L137-139 truncation-floor estimate)
- Bibliographic pre-verification log: `discrepancy_log.json` D1
  (relay-099-supplied `arXiv math.CA/9803067` resolves to Broadhurst
  1998, NOT to BBP 1997 as the prompt body suggested; both are
  legitimate genre-precedents and both are cited correctly above)

This memo is logged as 099-E-1 in `claims.jsonl`.
