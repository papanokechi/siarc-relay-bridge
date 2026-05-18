# T3B-VQUAD-EXCL-T2PRIME — Final Report

**Task ID:** T3B-VQUAD-EXCL-T2PRIME
**Date:** 2026-05-19
**Agent:** GitHub Copilot (VS Code) under SIARC Tier-3b AEAL governance
**Verdict:** **EXCLUSION_CERTIFIED** (both sub-bases)

---

## 1. TARGET and problem statement

**TARGET: T2'** — *Q-linear exclusion of V_quad over the basis
$$ B_\text{union} \;=\; \{V_\text{quad}^{k} : k = 0,1,2,3\} \;\cup\; \{\pi^{a} e^{b} G^{c} \zeta(3)^{d} : a+b+c+d \le 2\}.$$*

The cycle was launched by Claude (claude.ai relay session) as the immediate follow-up to T2 (predecessor cycle `T3B-VQUAD-EXCL-PEGZ3`, committed `648dbbe`, also EXCLUSION_CERTIFIED). Claude's framing, recorded verbatim in the relay prompt: *"the smallest test that would catch a polynomial relation between V_quad and the classicals, and at degree ≤ 2 on the classical side the basis stays tractable."*

V_quad is the limit of the generalized continued fraction with $a_n = 1$ and $b_n = 3n^2+n+1$ for $n \ge 1$ (discriminant $-11$, linking V_quad heuristically to $\mathbb{Q}(\sqrt{-11})$ and conductor-11 modular forms; full prior context in `pcf2-session-*` memory entries). T2 ruled out a *flat* Q-linear relation between V_quad and the 35 degree-$\le 3$ monomials in $\{\pi,e,G,\zeta(3)\}$ at 2050 dp. T2' tests whether V_quad satisfies any *polynomial* relation of degree $\le 3$ in V_quad whose coefficients are themselves classical monomials of degree $\le 2$.

**Agent extension (judgment call).** The relay prompt named one basis, $B_\text{union}$ (18 elements). I additionally ran a strictly stronger tensor basis,
$$ B_\text{tensor} \;=\; \{V_\text{quad}^{k} \cdot m : k = 0,1,2,3,\; m \in \text{classical monomials of total deg} \le 2\},$$
which has $4 \times 15 = 60$ elements. $B_\text{tensor}$ catches any polynomial relation in V_quad with degree-$\le 2$-classical-monomial coefficients, not merely $\sum c_k V_\text{quad}^k + \sum d_j m_j = 0$ with scalar coefficients. The literal union basis is the smaller, narrower test; the tensor basis is the conservative interpretation of "polynomial relation between V_quad and the classicals." Both are reported as separate sub-certificates so reviewers can distinguish the literal and strengthened readings. (See `handoff.md` §Judgment calls for the full rationale.)

---

## 2. What was actually executed

| Stage | Description | Outcome |
|------:|-------------|---------|
| 1 | PLAN: emit `plan_dag.json`, `env_snapshot.json` | OK |
| 2 | RELOAD + CROSS-CHECK: load predecessor 2000-digit V_quad string, verify SHA-256 of string content, fresh dual-depth CF at depths 5000 / 6000, dps 2200 | OK (dual-depth = 2200 digits; reload-vs-fresh sanity = 1999 digits, expected from `mp.nstr` 2000-digit truncation) |
| 3 | PRECISION FILTER: PSLQ on $B_\text{union}$ at 500 dp and 2050 dp; PSLQ on $B_\text{tensor}$ at 500 dp and 2050 dp | OK (None at all four tiers) |
| 4 | SYMBOLIC BIND: emit `exclusion_certificate.json` (two sub-certificates) | OK |
| 5 | ARCHIVE: AEAL `claims.jsonl` (9 entries), `manifest.json`, this `report.md` | OK |

Wall-clock breakdown for Stage 3:
- $B_\text{union}$ @ 500 dp (18 cols, 2000 maxsteps): **17.9 s**
- $B_\text{union}$ @ 2050 dp (18 cols, 4000 maxsteps): **174.4 s**
- $B_\text{tensor}$ @ 500 dp (60 cols, 2000 maxsteps): **224.7 s**
- $B_\text{tensor}$ @ 2050 dp (60 cols, 4000 maxsteps): **3439.0 s ≈ 57.3 min**
- Stage 3 total: **~64 min** ; Stage 2 + Stage 4+5: **~3 s**.

---

## 3. Evidence table (AEAL records)

| # | claim | method | precision (dp) | basis | result | confidence | artifact |
|---|-------|--------|---------------:|------|--------|-----------|----------|
| 1 | Predecessor V_quad reload reproduces (string-content SHA-256 `52375a71…f2f5c44`); reload-vs-fresh agreement = 1999 digits | byte-level reload + decode-strip + SHA verify, then mpmath parse | 2200 | n/a (provenance) | match | high (under the documented `mp.nstr` 1-ULP truncation rule, $\ge$ 1998 digits is the expected signal of correct provenance) | `raw_candidates.jsonl` |
| 2 | V_quad fresh CF agrees to 2200 digits between depths 5000 and 6000 at 2200 dp | backward GCF recurrence (mpmath) | 2200 | n/a | agreement_digits = 2200 | high | `raw_candidates.jsonl` |
| 3 | $B_\text{union}$ PSLQ at 500 dp returns None | `mpmath.pslq`, tol $=10^{-450}$, maxcoeff $=10^4$, maxsteps $=2000$ | 500 | 18-element $B_\text{union}$ | None | high | `pslq_union_500dp.json` |
| 4 | $B_\text{union}$ PSLQ at 2050 dp returns None | `mpmath.pslq`, tol $=10^{-1970}$, maxcoeff $=10^4$, maxsteps $=4000$ | 2050 | 18-element $B_\text{union}$ | None | high; PSLQ detection floor far exceeds $10^4$ at $D=2050$, $n=18$ | `pslq_union_2050dp.json` |
| 5 | $B_\text{tensor}$ PSLQ at 500 dp returns None | as above | 500 | 60-element $B_\text{tensor}$ | None | high | `pslq_tensor_500dp.json` |
| 6 | $B_\text{tensor}$ PSLQ at 2050 dp returns None | as above | 2050 | 60-element $B_\text{tensor}$ | None | high; PSLQ detection floor at $D=2050$, $n=60$ still many orders of magnitude above $10^4$ | `pslq_tensor_2050dp.json` |
| 7 | Two-tier $B_\text{union}$ exclusion | conjunction of #3 and #4 (stability gate per plan_dag.json node N8) | 2050 | $B_\text{union}$ | sub-verdict = NULL | high under scope caveat | `exclusion_certificate.json` |
| 8 | Two-tier $B_\text{tensor}$ exclusion | conjunction of #5 and #6 (gate node N9) | 2050 | $B_\text{tensor}$ | sub-verdict = NULL | high under scope caveat | `exclusion_certificate.json` |
| 9 | Combined verdict: V_quad has no Q-linear relation in either basis with $|c| \le 10^4$ | conjunction of #7 and #8 | 2050 | both | EXCLUSION_CERTIFIED | high | `exclusion_certificate.json` |

All nine claims are recorded in `claims.jsonl` in the required `{claim, evidence_type, dps, reproducible, script, output_hash}` schema.

---

## 4. Honest verdict and scope caveat

**EXCLUSION_CERTIFIED.**

*What is ruled out:* No integer-coefficient relation $\sum_i c_i \cdot v_i = 0$ with $|c_i| \le 10^4$ exists for $\mathbf{v} = (V_\text{quad}, \text{basis elements})$ when the basis is either $B_\text{union}$ or $B_\text{tensor}$.

*What is NOT ruled out:*
1. classical-monomial coefficients of total degree $> 2$,
2. integer coefficients with $|c| > 10^4$,
3. polynomial relations in V_quad of degree $\ge 4$,
4. relations involving constants outside $\{\pi, e, G, \zeta(3)\}$ (e.g., $\gamma$, $\log 2$, $\zeta(5)$, Khinchin's constant), and
5. transcendental/ODE-theoretic relations (e.g., Painlevé III($D_6$) connection-formula identities).

Rule 2 (gold-freeze conditions) is *not* satisfied: no Lean 4 verification, no symbolic CAS derivation. This is a stable two-tier numerical exclusion under explicit, narrowly stated bounds — one of the four authorised SIARC outcomes for a Tier-3b cycle.

Per Claude's framing in the relay prompt, the conjunction of T2 (EXCLUSION_CERTIFIED) and T2' (EXCLUSION_CERTIFIED) leaves the **Painlevé III($D_6$) hypothesis** as the cleanest remaining explanation by elimination, which is itself a paper-shaped finding.

---

## 5. Falsification triggers (named in the relay prompt; unfired this cycle)

| trigger | tested here? | result |
|--------|--------------|--------|
| A degree-4 hit at the same basis | No (basis stops at $V_\text{quad}^3$) | UNTESTED |
| A $V_\text{quad}^2$ hit at degree $\le 2$ in the same basis | Yes (already in $B_\text{tensor}$) | NOT HIT |
| A degree $\le 3$ hit after expanding maxcoeff to $10^6$ | No (maxcoeff fixed at $10^4$ for comparability with predecessor) | UNTESTED |

Each unfired trigger is a candidate next cycle.

---

## 6. Next-cycle recommendations

In approximate cost order (cheapest first):

1. **maxcoeff lift to $10^6$** on $B_\text{tensor}$ at 2050 dp. Marginal cost: rerun the existing 57-min tier with `maxcoeff = 1_000_000`. Tightens the certificate's coefficient floor by 2 orders of magnitude. Closes one of the three named falsification triggers.

2. **Add $V_\text{quad}^4$ to $B_\text{union}$ / $B_\text{tensor}$** (sizes 19 / 75 elements). Closes the "degree-4 hit" falsification trigger named above. The 75-element tensor tier at 2050 dp would extrapolate to ~90–100 min wall-clock.

3. **Extend the classical-monomial side to degree 3** ($B_\text{tensor}$ would become $4 \times 35 = 140$ elements). Working dps would need to lift to ~2500 to keep the same PSLQ detection floor at $|c| \le 10^4$. This is the original "lift to degree-3 algebraic exclusion" recommendation from the T2 report; T2' has now made it the next-after-next step rather than the immediate follow-up.

4. **Augment classical generators** with $\gamma$, $\log 2$, $\zeta(5)$ at the current $B_\text{union}$ structure. Each new generator adds 5 monomials at degree $\le 2$. Useful if Claude wants to widen scope before deepening it.

5. **ODE-theoretic / Painlevé III($D_6$) audit** (out of scope for the agent under current AEAL rules; this is a Claude-side task per §6 of `pcf2-program-statement-2026-05-01.md`).

Recommendation #1 is the most cost-efficient single follow-up.

---

## 7. Files in this slot (18 archived)

`basis_tensor_enumeration.json`, `basis_union_enumeration.json`, `claims.jsonl`, `discrepancy_log.json`, `env_snapshot.json`, `exclusion_certificate.json`, `executor_summary.json`, `halt_log.json`, `manifest.json`, `plan_dag.json`, `pslq_tensor_2050dp.json`, `pslq_tensor_500dp.json`, `pslq_union_2050dp.json`, `pslq_union_500dp.json`, `raw_candidates.jsonl`, `stage_23_executor.py`, `stage_4_5_archive.py`, `unexpected_finds.json`, `verified_relations.json`. (Plus `report.md` and `handoff.md` once written.)

All SHA-256 hashes are listed in `manifest.json`.
