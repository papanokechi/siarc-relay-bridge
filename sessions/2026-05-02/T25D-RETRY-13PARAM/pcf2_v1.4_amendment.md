# Proposed PCF-2 v1.4 amendment - PASS_A_EQ_6_ONLY

**Status:** DRAFT (operator decides whether to deposit a v1.4)

## Section 6 (j=0 endpoint discussion)

Current published wording (PCF-2 v1.3 Sec.6): `AMBIGUOUS-AT-FINITE-N`.

Proposed replacement (verdict = PASS_A_EQ_6_ONLY):

> At all four j=0 cubic families (Q_30..Q_33), the WKB leading
> exponent A_lin extracted from a square-exact 11-parameter
> ansatz refit on the dps=25000 / N up to 1200 y_n series
> reaches |A_lin - 6| <= 3.08904186542e-23
> at the floor of 11-parameter truncation. PSLQ on the H6
> Chowla-Selberg basis B19+ at maxcoeff = 10^50 / tol = 10^-40
> returned no non-trivial Gamma(1/3) relation in any of the four
> families. We read this as: A = 6 to PSLQ-detection precision,
> with no detected Chowla-Selberg amplitude correction in the
> H6 basis at the present precision.

## AEAL anchors

- Saved CSVs (input):
  - fam30: see Prompt 006 output_hashes.json
  - fam31: see Prompt 006 output_hashes.json
  - fam32: see Prompt 006 output_hashes.json
  - fam33: see Prompt 006 output_hashes.json
- This session output_hashes.json (in same dir).
