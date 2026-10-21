# PREREG CT-S10-COLDREAD2

Cold-read target: `sessions/2026-09-17/CT-S1-THEOREM/theorem.tex`, specifically Theorem `thm:growth` Step 3 and every cross-reference to the Gamma-ratio asymptotic `eq:gammaratio` in the abstract, gaps/labels section near `sec:gaps`, Gap G1 paragraph, and bibliography entry.

Checks to perform before verdict:
1. Algebra: independently expand `(1-r/n)(1-1/n)^(-r)` with SymPy and by proof-level reasoning; a defect exists if the `1/n` term does not cancel or the claimed `1+O(n^-2)` is not valid under the theorem's hypotheses.
2. Error term/product: verify whether `h(n)/h(n-1)=1+O(n^-2)` implies convergence to finite nonzero `h_inf` and `h(n)=h_inf(1+O(1/n))`; a defect exists if this only gives `o(1)`, if product/log bookkeeping is unjustified, if nonzero limit is not established, or if assumptions on `n`/`r` are missing.
3. Citation: fetch DLMF 5.11 and relevant equation permalinks, record URLs and sha256, and inspect equation numbering and validity conditions. A defect exists if the document cites the wrong equation number, misstates DLMF, or relies on a result not actually cited.
4. Hypotheses/edge cases: inspect whether complex `r`, large `Re(r)`, nonnegative integer `r`, poles for small `n`, and uniformity in `r` are properly handled. A defect exists if the theorem requires unstated exclusions or bounds.
5. Circularity: a defect exists if Step 3 assumes the Gamma-ratio asymptotic or equivalent statement before proving/importing it.
6. Label consistency: a defect exists if the epistemic label or imported-literature description is inaccurate for the proof actually given.

Verdict criteria:
- SOUND only if every link is correct as written and all citations/labels are accurate.
- GAP if a load-bearing step is asserted without enough proof or has missing hypotheses.
- ERROR if a stated step/citation is false; quote and correct it.
