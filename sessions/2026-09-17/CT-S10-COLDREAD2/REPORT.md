# CT-S10-COLDREAD2 REPORT

## Scope and method

Cold read performed only on `sessions/2026-09-17/CT-S1-THEOREM/theorem.tex` at HEAD `08aa0e2381b3dc37ee54a3200b7272755ca11d59`; theorem source sha256: `47FE04D210F0564A848AA10A1F2982EC7E0AA1977F911BAA1DDB0255F312C922`. I did not read the forbidden audit/cold-read reports or claims files.

Created `PREREG.md` before computations. Computations saved as `sympy_gammaratio.py/.out` and `mpmath_gammaratio.py/.out`. DLMF pages were fetched into this session folder and hashed.

## Verdict

**ERROR** (non-load-bearing citation metadata error). The Gamma-ratio argument and DLMF equation-number citations are mathematically sound, but the bibliography entry is not correct for the fetched URL.

Quoted defective text:

> `NIST Digital Library of Mathematical Functions, \texttt{https://dlmf.nist.gov/}, Release 1.2.4.`

Fetched `https://dlmf.nist.gov/5.11` reports in its footer: `Version 1.2.8; Release date 2026-09-15.` Because the bibliography gives the general live DLMF URL, the release metadata is stale unless a fixed 1.2.4 snapshot is intended and cited.

**Is the passage now fit to carry a PROVEN label in a deposit?** Mathematically, yes for Step 3 and its imported constant. As-written for deposit, no: update the DLMF release metadata to the fetched/current version (or cite a stable 1.2.4 source explicitly). No mathematical repair is required.

## Algebra check

SymPy expansion with `x=1/n`:

`(1-r*x)*(1-x)^(-r) = 1 + 0*x + r(1-r)x^2/2 + r(1-r^2)x^3/3 + r(1-r)(r+1)(r+2)x^4/8 + O(x^5)`.

Thus the `1/n` terms cancel and the ratio is `1+O(1/n^2)` for fixed complex `r`.

Output hash: `sympy_gammaratio.out` sha256 `7E76510AF73520EBAF069ACAA819BD6F52C0170B57C31FA274FAF66FD6E44C14`.

## Product/error-term check

Let `h(n)/h(n-1)=1+a_n` with `a_n=O(n^-2)`. For sufficiently large `n`, `|a_n|<1/2`, so `log(1+a_n)=a_n+O(a_n^2)=O(n^-2)`. The tail satisfies `sum_{m>n} O(m^-2)=O(1/n)`. Therefore

`h_inf/h(n) = exp(sum_{m>n} log(1+a_m)) = exp(O(1/n)) = 1+O(1/n)`,

and since all tail factors are nonzero and the limiting product is nonzero, `h(n)=h_inf(1+O(1/n))`. This is stronger than `o(1)` and justifies the document's product-to-error step, although the document compresses the log bookkeeping.

## DLMF citation check

Fetched URLs and sha256:

- `https://dlmf.nist.gov/5.11` -> `dlmf_5_11.html`, sha256 `D9A10228B2A4F6800520FA283CC1086B4BCF736A726A690C82D0139AF3169E42`.
- `https://dlmf.nist.gov/5.11.E12` -> `dlmf_5_11_E12.html`, sha256 `D863E17D23308C1DD7332A491519CB6FE5167ED5D747487825BA29B2E50153F8`.
- `https://dlmf.nist.gov/5.11.E13` -> `dlmf_5_11_E13.html`, sha256 `B45027C781E68D0F949A2CBE61C2D58476853CCF7547589646B63807A9C556D9`.
- `https://dlmf.nist.gov/5.11.E15` -> `dlmf_5_11_E15.html`, sha256 `FCE2B848CB393AEB371F9731E0C511928E4DBCD5A2298876EFB9AAC4FB7E0A73`.

Inspected facts from `https://dlmf.nist.gov/5.11`:

- §5.11(iii) first states `a`, `b`, `c` are real or complex constants.
- Validity condition before the ratio equations: if `z -> infinity` in the sector `|ph z| <= pi - delta`, then the following equations hold.
- Eq. **5.11.12** is the plain ratio: `Gamma(z+a)/Gamma(z+b) ~ z^(a-b)`.
- Eq. **5.11.13** is the refined expansion: `Gamma(z+a)/Gamma(z+b) ~ z^(a-b) sum_{k=0}^infty G_k(a,b)/z^k`.
- Eq. **5.11.15** states `G_0(a,b)=1` (and also lists `G_1`, `G_2`).
- Footer reports `Version 1.2.8; Release date 2026-09-15`, not Release 1.2.4.

Conclusion: the document's Step 3 relies exactly on Eq. 5.11.12 to set `h_inf=1`; the parenthetical refined-expansion numbers 5.11.13 and 5.11.15 are correct. Only the bibliography release metadata is stale.

## Hypotheses and edge cases

- The proof is for fixed `r in C`; no uniformity in unbounded `r` is claimed. Constants in `O(...)` may depend on `r`.
- Complex `r` is handled with positive-real `n^r=exp(r log n)` and DLMF permits real or complex constants `a,b`; the path `z=n>0` satisfies the sector condition.
- Large `Re(r)` only forces starting the elementary product after a larger `n_0`; asymptotics are unaffected.
- Positive integer `r` can make `Gamma(n+1-r)` singular for small `n`, but Step 3 starts after `n>max(0,Re r)`. In the theorem application, (A2) excludes positive-integer roots and makes the exact product denominator `Gamma(1-r_i)` finite. No unstated theorem-level exclusion found.
- Nonnegative integer `r=0` is harmless; positive integers are excluded in Theorem `thm:growth` by (A2)/(A1).

## Circularity

No circularity found. The elementary part proves convergence and `O(1/n)` up to `h_inf`; DLMF 5.11.12 is then imported only to identify `h_inf=1`.

## Label consistency

The cross-references in the abstract, §`sec:gaps`, and Gap G1 accurately identify the imported mathematical ingredient as the single classical Gamma-ratio normalisation `h_inf=1` from DLMF 5.11.12. The parenthetical refined expansion citation is correctly numbered. The only label/citation inconsistency found is bibliographic release metadata.

## Numerical corroboration

At 80 dps, `h(n)=Gamma(n+1-r)n^r/Gamma(n+1)` approaches 1 with `n*(h(n)-1)` approaching `r(r-1)/2` for `r=1/3`, `-2.5`, `2`, and `3+2i`. This supports, but does not prove, the asymptotic.

Output hash: `mpmath_gammaratio.out` sha256 `8745BACC6524B648DACD0B3F0CE045FD6738CD2588050496DC106C418FF07DEB`.

## Could not establish

I did not establish what DLMF Release 1.2.4 itself said, because the live fetched URL provides Version 1.2.8. I therefore cannot say whether the stale release number is merely a metadata typo or an intentional citation to an unfetched historical release.

## Open questions for the operator

1. Should the bibliography cite the current live DLMF version 1.2.8, or should a stable historical 1.2.4 URL/source be supplied?

## Uncommitted files created

All under `sessions/2026-09-17/CT-S10-COLDREAD2/`:

- `PREREG.md`
- `REPORT.md`
- `claims.jsonl`
- `sympy_gammaratio.py`
- `sympy_gammaratio.out`
- `mpmath_gammaratio.py`
- `mpmath_gammaratio.out`
- `dlmf_5_11.html`
- `dlmf_5_11_E12.html`
- `dlmf_5_11_E13.html`
- `dlmf_5_11_E15.html`
