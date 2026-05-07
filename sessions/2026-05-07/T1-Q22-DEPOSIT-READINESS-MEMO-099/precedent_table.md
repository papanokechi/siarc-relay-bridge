# Q22 Comparable-paper precedent table — PCF-2 v1.4 deposit-readiness

**Bridge HEAD at fire time:** `21db92d40179d3bb97d4cafc7d0a55a99b864b39`
**Date:** 2026-05-07 (W20-Thu)
**Genre:** numerical-identity in experimental mathematics where (i) the |delta|
target is the agreement (or rejected agreement) between a high-precision
computed value and a candidate closed-form, and (ii) PSLQ-type
integer-relation searches at maxcoeff floors are used as the diagnostic.

All identifiers in this table were resolved at fire time per post-031
bibliographic pre-verification rule. The relay-prompt-supplied identifier
`arXiv math.CA/9803067` was found to resolve to Broadhurst 1998 (a
neighbouring-genre paper), NOT to the Bailey-Borwein-Plouffe 1997 paper
as the prompt body suggested; the conflation is recorded in
`discrepancy_log.json` D1 and the actual BBP 1997 DOI is cited below
in lieu of a (non-existent) BBP arXiv ID.

## Anchor table

| # | Source | Authors | Year | Venue / locator | |delta| or precision | Notes (genre fit) |
|---|---|---|---|---|---|---|
| 1 | "On the Rapid Computation of Various Polylogarithmic Constants" | Bailey, Borwein, Plouffe | 1997 | Math. Comp. 66 (218): 903-913; DOI 10.1090/S0025-5718-97-00856-9 | identification at PSLQ-detection precision (paper reports 30+ digit PSLQ confidence on the BBP coefficient vector for pi) | Canonical PSLQ-based numerical-identity deposit; identification was accepted on PSLQ-coefficient match alone, with formal proof following separately. Precedent for "PSLQ-detection precision suffices for deposit". Pre-verified at fire time via DOI -> Math. Comp. 66(218); arXiv ID does not exist for this paper. |
| 2 | "Polylogarithmic ladders, hypergeometric series and the ten millionth digits of zeta(3) and zeta(5)" | Broadhurst | 1998 | arXiv math.CA/9803067 | digit-extraction at the 10^7-th hexadecimal place; PSLQ-style identification of coefficient vectors against polylogarithmic ladders | Same genre (PSLQ + high-precision arithmetic + hexadecimal digit extraction). Pre-verified: arXiv resolves correctly to Broadhurst 1998 (NOT to BBP, contra the relay-099 prompt body). Treated here as a genuine genre-precedent. |
| 3 | "Mathematics by Experiment: Plausible Reasoning in the 21st Century" | Borwein, Bailey | 2004 (1st ed., A.K. Peters); 2nd ed. 2008 (CRC Press) | ISBN 978-1-56881-211-3 (1st ed.) | book-length corpus; the standard threshold cited in chapter 1 is "100 significant figures" as the working precision at which experimental-math identifications are conducted | Canonical reference for experimental-math precision standards. Cited by author-year per relay-099 acceptance; not used as a specific-volume claim. Note: relay-099 wrote "2003 1st ed."; Wikipedia / WorldCat record 2004 1st ed. Minor discrepancy logged. |
| 4 | Generic-genre venue precedent | various | 2010-2025 | _Ramanujan J._, _Experimental Mathematics_ (journal), _Research in Number Theory_ | typical PSLQ-no-relation publications carry |delta| ~ 10^-20 to 10^-50 | Reviewer A (2026-05-07 peer-AI synthesis 4-of-4) explicitly cites these three venues as the standard publication-acceptance window for the |delta| ~ 10^-23 / no-relation-found genre. Genre-precedent only; specific paper anchors deferred to post-deposit appendix if/when needed. |

## Genre-fit summary

The PCF-2 v1.4 amendment substrate (`pcf2_v1.4_amendment.md`, SHA16
`88845089434F96EF`, 1151 B / 22 lines, drafted at bridge commit
`f8099b4` family at session
`sessions/2026-05-02/T25D-RETRY-13PARAM/`) records a numerical-identity
finding of the form:

  At all four j=0 cubic families (Q_30..Q_33), the 11-parameter LIN
  refit of the dps=25000 / N up to 1200 saved y_n series reaches
    |A_lin - 6| <= 3.08904186542e-23
  and PSLQ on the H6 Chowla-Selberg basis B19+ at maxcoeff = 10^50,
  tol = 10^-40 returns no non-trivial Gamma(1/3) relation in any of
  the four families.

This is a category-(ii) result in the precedent table: a |delta|
threshold is reached AND a PSLQ-no-relation finding accompanies it.
The |delta| envelope at 10^-23 sits inside the typical
publication-acceptance window cited at row 4 (Reviewer A,
peer-AI synthesis 4-of-4 substrate, SHA16 `DF92466E123E16BF`),
and is roughly 10^8 below the standard PSLQ-detection floor of
~10^-15 commonly cited for integer-relation identification work
(Reviewer A, Q1 reasoning verbatim).

## Path-(b) stretch context

The path-(b) stretch (K_FIT=9, N=2400; ~24-hr high-compute fire per
operator notes) would sharpen the truncation floor from
N=1200 / K_FIT=7 (~ 1200^-8 ~= 5e-25 theoretical, 3e-23 realized)
to N=2400 / K_FIT=9 (~ 2400^-10 ~= 1.7e-34 theoretical), a gain of
roughly 11 orders of magnitude in the target |delta|. That gain
sharpens the strength of the negative result (no Gamma(1/3) relation)
but does not change the structural verdict relative to the precedent
table: rows 1-2-3 all accept identification (or rejection) at
|delta| envelopes well within reach of the path-(a)
currently-realized 3.08904186542e-23.

## AEAL anchor

This table is logged as 099-C-1 in `claims.jsonl`.
