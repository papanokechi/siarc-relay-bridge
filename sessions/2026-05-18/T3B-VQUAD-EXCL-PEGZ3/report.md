# T3B-VQUAD-EXCL-PEGZ3 — Final Report

**Task ID:** T3B-VQUAD-EXCL-PEGZ3
**Date:** 2026-05-18
**Agent:** GitHub Copilot (VS Code) under SIARC Tier-3b AEAL governance
**Verdict:** **EXCLUSION_CERTIFIED**

---

## 1. TARGET and problem statement

**TARGET: T2** — *Is V_quad (≈ 1.19737…) algebraic over Q(π, e, Catalan, ζ(3))?*

In our own words: V_quad is the limit of the generalized continued fraction
$$ V_\text{quad} \;=\; 1 + \cfrac{1}{5 + \cfrac{1}{15 + \cfrac{1}{31 + \cdots}}} ,$$
where the $n$-th partial denominator is $b_n = 3n^2 + n + 1$ and $a_n = 1$ for all $n \ge 1$. The polynomial $3n^2+n+1$ has discriminant $-11$, which links V_quad heuristically to the imaginary quadratic field $\mathbb Q(\sqrt{-11})$, conductor-11 elliptic curves, and the Dirichlet character $\chi_{-11}$. Prior work in this workspace has tested 13 function families (Bessel, Airy, Whittaker, parabolic cylinder, $_0F_2$, $_2F_1$, conductor-11 L-values, Lommel, Weber modular, Meijer-G, q-series, etc.) at 500–2050 dp and found no relation. This run closes one specific question that the prior testing had **not** addressed: a clean PSLQ-exclusion of V_quad over the canonical "physical-constants" basis $\mathbb Q(\pi, e, G_\text{Catalan}, \zeta(3))$ at $\ge 2000$ dp.

To make the test fully precise: we test the **Q-linear** formulation. The basis is the 35 monomials $\pi^a e^b G^c \zeta(3)^d$ with $a+b+c+d \le 3$ and $a,b,c,d \ge 0$, the constant 1 included. PSLQ is run on the 36-element list $[V_\text{quad},\, \pi^{a_1} e^{b_1} G^{c_1} \zeta(3)^{d_1},\, \ldots]$ at two precision tiers (500 dp and 2050 dp), with maxcoeff $= 10^4$. A relation must be stable across both tiers to advance to Stage 4. The fully general "algebraic over" question (testing $V_\text{quad}^k$ for $k \ge 2$ as additional row-vectors) is explicitly out of scope for this cycle and is filed under "next-cycle recommendation".

---

## 2. What was actually executed

| Stage | Description | Outcome |
|------:|-------------|---------|
| 1 | PLAN: emit `plan_dag.json`, `env_snapshot.json` | OK |
| 2 | NUMERIC SWEEP: V_quad at 100 / 500 / 2200 dp working precision, with cross-depth CF agreement check | OK (agreement at every tier ≥ the target dp) |
| 3 | PRECISION FILTER: PSLQ at 500 dp and 2050 dp on 36-element vector | OK (None at both tiers) |
| 4 | SYMBOLIC BIND: emit `exclusion_certificate.json` | OK |
| 5 | ARCHIVE: AEAL `claims.jsonl`, `manifest.json`, this `report.md` | OK |

All five stages completed. Total wall-clock for the executor scripts: ~6 minutes for Stages 2+3, ~1 second for Stage 4+5.

---

## 3. Evidence table (seven-field AEAL records)

| # | claim | method | precision (dp) | basis | result | confidence | artifact_path |
|---|-------|--------|---------------:|-------|--------|-----------|----------------|
| 1 | V_quad agrees to 100 digits across CF depths 400/600 | backward GCF recurrence, mpmath | 100 | n/a (single-constant compute) | agreement_digits = 100 | high (≥ tier dp) | `vquad_value_2000dp.txt`, `raw_candidates.jsonl` |
| 2 | V_quad agrees to 500 digits across CF depths 2000/2400 | backward GCF recurrence | 500 | n/a | agreement_digits = 500 | high | `raw_candidates.jsonl` |
| 3 | V_quad agrees to 2200 digits across CF depths 5000/6000 | backward GCF recurrence | 2200 | n/a | agreement_digits = 2200 (first 2000 stable) | high; cross-validated against 48-digit reference (48/48 agreement) | `vquad_value_2000dp.txt` |
| 4 | No PSLQ relation found at 500 dp | mpmath.pslq, tol = $10^{-450}$, maxcoeff $=10^4$, maxsteps=2000 | 500 | 35-element basis: $\{\pi^a e^b G^c \zeta(3)^d : a+b+c+d \le 3\}$ | result = None | high under stated maxcoeff bound | `pslq_500dp.json` |
| 5 | No PSLQ relation found at 2050 dp | mpmath.pslq, tol = $10^{-1970}$, maxcoeff $=10^4$, maxsteps=4000 | 2050 | same 35-element basis | result = None | high; PSLQ detection floor (Bailey-Broadhurst) far exceeds maxcoeff at this precision | `pslq_2050dp.json` |
| 6 | Two-tier stability: V_quad ∉ Q-span of basis with $|c_i| \le 10^4$ | conjunction of #4 and #5; stability gate per plan_dag.json node N8 | 2050 | as above | EXCLUSION_CERTIFIED | high under the scope caveat in §1 | `exclusion_certificate.json` |

All six claims are duplicated in `claims.jsonl` in the required `{claim, evidence_type, dps, reproducible, script, output_hash}` schema.

The full PSLQ working tolerance at tier-2 was $10^{-1970}$; the basis spans a 35-dimensional sublattice and the maxcoeff bound was $10^4$, which is many orders of magnitude inside the formal PSLQ detection floor at this precision. Returning None at both tiers therefore constitutes a clean exclusion under the stated bounds, not a precision artefact.

---

## 4. Honest verdict

**EXCLUSION_CERTIFIED.**

Rule 2 (gold-freeze conditions) is **not** satisfied: no verified Lean 4 file, no fully symbolic CAS derivation. We do not claim a theorem, do not claim a proof, and do not claim the open question is "resolved". What we have is a stable two-tier numerical exclusion under explicit, narrowly-stated bounds.

Per the SIARC governance rules, this is one of the four authorised outcomes and is reported as such without escalation.

---

## 5. Next-cycle recommendation

The cleanest next cycle is a single-axis widening of the same test. Specifically: re-run the identical pipeline with the 36-row vector replaced by an $L$-row vector $[V_\text{quad}^0,\, V_\text{quad}^1,\, V_\text{quad}^2,\, V_\text{quad}^3] \otimes \text{basis}$ flattened into a $4 \cdot 35 = 140$-element list at 3000 dp working precision (working dps headroom is needed because the basis size has nearly quadrupled). A null return at that scale would lift the present Q-linear exclusion to a degree-3 algebraic exclusion of V_quad over $\mathbb Q(\pi, e, G, \zeta(3))$ within the same coefficient bound. If a relation appears at this stage, the standard procedure is to confirm via SymPy symbolic identity-checking before any binding language is used.

A reasonable secondary axis is to lift maxcoeff from $10^4$ to $10^6$ at 2050 dp on the current 36-element basis — much cheaper than the cross-product extension, and it tightens the present certificate's coefficient floor by two orders of magnitude with essentially no additional infrastructure.
