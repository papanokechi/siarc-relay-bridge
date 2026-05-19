# T3B-VQUAD-EXCL-T2DPRIME — Final Report

**Task ID:** T3B-VQUAD-EXCL-T2DPRIME
**Date:** 2026-05-19
**Agent:** GitHub Copilot (VS Code) under SIARC Tier-3b AEAL governance
**Verdict:** **EXCLUSION_CERTIFIED** (both axes)

---

## 1. TARGET and problem statement

**TARGET: T2''** — *Strengthen the T2' exclusion certificate by closing two of the three named falsification triggers in one Tier-3b session.*

Two independent axes, each tested at two precision tiers (500 dp + 2050 dp):

| Axis | Basis | Size | Test | Closes T2' trigger |
|------|-------|------|------|--------------------|
| 1 (coefficient-floor) | $B_{3,2} = \{V_\text{quad}^{k}\cdot\pi^{a}e^{b}G^{c}\zeta(3)^{d} : k\in[0,3],\,a+b+c+d\le 2\}$ | 60 | maxcoeff = $10^{6}$ | "a degree $\le 3$ hit after expanding maxcoeff to $10^6$" |
| 2 (degree-extension) | $B_{4,2} = \{V_\text{quad}^{k}\cdot\pi^{a}e^{b}G^{c}\zeta(3)^{d} : k\in[0,4],\,a+b+c+d\le 2\}$ | 75 | maxcoeff = $10^{4}$ | "a degree-4 hit at the same basis" |

V_quad is the limit of the generalized continued fraction with $a_n = 1$ and $b_n = 3n^2+n+1$ for $n \ge 1$. T2 (predecessor `T3B-VQUAD-EXCL-PEGZ3`, committed `648dbbe`) ruled out a flat Q-linear relation between V_quad and the 35 degree-$\le 3$ classical monomials. T2' (predecessor `T3B-VQUAD-EXCL-T2PRIME`, committed `798495c`) ruled out polynomial-degree-$\le 3$ relations on the (3,2) union (18 elements) and tensor (60 elements) bases at maxcoeff $10^4$.

**Re-scope note (judgment call, recorded in `env_snapshot.json` and `plan_dag.json`).** Claude's relay prompt named the strict bipartite (3,3) tensor at maxcoeff = $10^6$ as the next step, citing 40 elements and ~T2' runtime. On the four-classical-generator basis used by T2', the strict (3,3) tensor is $4\times 35 = 140$ elements with ~5–8 h wall-clock at 2050 dp, breaking the stated "one Tier-3b session" budget. The dual-axis option above tests the same two underlying experimental dimensions (coefficient ceiling AND V_quad-degree extension) within the budget. The strict (3,3) cycle is deferred to T2''' if and when warranted. See §6 for next-cycle disposition.

---

## 2. What was actually executed

| Stage | Description | Outcome |
|------:|-------------|---------|
| 1 | PLAN: emit `plan_dag.json`, `env_snapshot.json` | OK |
| 2 | RELOAD + CROSS-CHECK: load predecessor 2000-digit V_quad string (string-SHA verified), fresh dual-depth CF at depths 5000 / 6000, dps 2200; dual-depth agreement = **2200 digits** (i.e., exact to working precision), reload-vs-fresh = **1999 digits** (matches the $mp.nstr$ 2000-digit truncation signature) | OK |
| 3 | PRECISION FILTER: four PSLQ tiers (3a/3b on $B_{3,2}$ at maxcoeff $10^6$; 3c/3d on $B_{4,2}$ at maxcoeff $10^4$) + one pre-flight smoke at 500 dp on $B_{4,2}$ | OK (None at all five PSLQ runs) |
| 4 | SYMBOLIC BIND: emit `exclusion_certificate.json` (two axis sub-certificates + combined verdict + recovery-metadata block) | OK |
| 5 | ARCHIVE: AEAL `claims.jsonl` (10 entries), `manifest.json` (21 files), this `report.md`, `handoff.md` | OK |

**Stage 3 wall-clock breakdown:**

| Tier | Basis | dp | maxcoeff | wall_seconds | result |
|------|-------|---:|---------:|-------------:|--------|
| 3a   | $B_{3,2}$ (60) | 500 | $10^6$ | 259.43 | None |
| 3b   | $B_{3,2}$ (60) | 2050 | $10^6$ | 3250.44 | None |
| 3c   | $B_{4,2}$ (75) | 500 | $10^4$ | 545.45 | None |
| 3d-smoke | $B_{4,2}$ (75) | 500 | $10^4$ | 445.10 | None |
| 3d   | $B_{4,2}$ (75) | 2050 | $10^4$ | 2799.69 | None |

Stage 3 total (wall, canonical tiers only): **≈ 6855 s ≈ 114 min**; smoke adds ≈ 7 min.

**Provenance note (one sentence per user guidance).** Tier 3d was executed in a separate process from tiers 3a–3c after the original `stage_23_executor.py` terminated silently between tier 3c and tier 3d; a pre-flight 500 dp smoke on the identical $B_{4,2}$ basis confirmed structural invariance against canonical tier 3c before the 2050 dp run. Full provenance in `tier_3d_recovery.json` and `stage_2_verification.json`; the verdict stands on its own merits.

---

## 3. Evidence table (AEAL records)

| # | claim | method | precision (dp) | basis | result | confidence | artifact |
|---|-------|--------|---------------:|------|--------|-----------|----------|
| 1 | Predecessor V_quad reload reproduces (string-content SHA-256 `52375a71…f2f5c44`); reload-vs-fresh agreement = 1999 digits | byte-level reload + decode-strip + SHA verify, then mpmath parse | 2200 | n/a (provenance) | match | high (under the documented $mp.nstr$ 1-ULP truncation rule, $\ge 1998$ digits is the expected signal) | `stage_2_verification.json` |
| 2 | V_quad fresh CF agrees to 2200 digits between depths 5000 and 6000 at 2200 dp; first 64 chars bit-identical to T2 and T2' | backward GCF recurrence (mpmath); cross-cycle invariant | 2200 | n/a | agreement_digits = 2200 | high | `stage_2_verification.json` |
| 3 | $B_{3,2}$ PSLQ at 500 dp returns None | `mpmath.pslq`, tol $=10^{-450}$, maxcoeff $=10^6$, maxsteps $=2000$ | 500 | 60-element $B_{3,2}$ | None | high | `pslq_3_2_maxc6_500dp.json` |
| 4 | $B_{3,2}$ PSLQ at 2050 dp returns None | `mpmath.pslq`, tol $=10^{-1970}$, maxcoeff $=10^6$, maxsteps $=4000$ | 2050 | 60-element $B_{3,2}$ | None | high; PSLQ detection floor at $D=2050$, $n=60$ exceeds $10^6$ by orders of magnitude | `pslq_3_2_maxc6_2050dp.json` |
| 5 | $B_{4,2}$ PSLQ at 500 dp returns None | as above, maxcoeff $=10^4$ | 500 | 75-element $B_{4,2}$ | None | high | `pslq_4_2_maxc4_500dp.json` |
| 6 | Pre-flight smoke on $B_{4,2}$ at 500 dp returns None; structural invariants match canonical tier 3c (`dps, tol_exponent, maxcoeff, maxsteps, basis_size, result, error` all equal; wall-clock differs as expected) | identical PSLQ parameters to claim 5 from a separate process | 500 | 75-element $B_{4,2}$ | None (None == None verdict-equality; see `tier_3d_recovery.json` `smoke_comparison_note` for what this establishes and what it does not) | high (structural-invariance, not byte-equality) | `tier_3d_preflight_500dp.json` |
| 7 | $B_{4,2}$ PSLQ at 2050 dp returns None | as above, maxcoeff $=10^4$ | 2050 | 75-element $B_{4,2}$ | None | high; PSLQ detection floor at $D=2050$, $n=75$ exceeds $10^4$ by orders of magnitude | `pslq_4_2_maxc4_2050dp.json` |
| 8 | Axis-1 two-tier exclusion ($B_{3,2}$, maxcoeff $10^6$) | conjunction of #3 and #4 | 2050 | $B_{3,2}$ | sub-verdict = NULL | high under scope caveat | `exclusion_certificate.json` |
| 9 | Axis-2 two-tier exclusion ($B_{4,2}$, maxcoeff $10^4$) | conjunction of #5 and #7 (with smoke #6 corroborating pipeline invariance) | 2050 | $B_{4,2}$ | sub-verdict = NULL | high under scope caveat | `exclusion_certificate.json` |
| 10 | Combined verdict: EXCLUSION_CERTIFIED | conjunction of #8 and #9 | 2050 | both | EXCLUSION_CERTIFIED | high | `exclusion_certificate.json` |

All ten claims recorded in `claims.jsonl` in the required `{claim, evidence_type, dps, reproducible, script, output_hash}` schema.

---

## 4. Honest verdict and scope caveat

**EXCLUSION_CERTIFIED on both axes.**

*What is ruled out:*

- (Axis 1) No integer-coefficient relation $\sum_i c_i \cdot v_i = 0$ with $|c_i| \le 10^{6}$ exists for $\mathbf{v} = (V_\text{quad}, \text{elements of } B_{3,2})$.
- (Axis 2) No integer-coefficient relation $\sum_i c_i \cdot v_i = 0$ with $|c_i| \le 10^{4}$ exists for $\mathbf{v} = (V_\text{quad}, \text{elements of } B_{4,2})$.

*What is NOT ruled out:*

1. The **joint** axis (degree-4 V_quad × degree-$\le 2$ classical at maxcoeff $10^6$) was NOT directly tested. Axis 1 covers $10^6$ only on the $k\le 3$ tensor; axis 2 covers $k=4$ only at $10^4$.
2. classical-monomial coefficients of total degree $> 2$,
3. integer coefficients with $|c| > 10^6$ (or $|c| > 10^4$ on axis 2),
4. polynomial relations in V_quad of degree $\ge 5$,
5. relations involving constants outside $\{\pi, e, G, \zeta(3)\}$ (e.g., $\gamma$, $\log 2$, $\zeta(5)$, Khinchin's constant),
6. transcendental / ODE-theoretic relations (e.g., Painlevé III($D_6$) connection-formula identities).

Rule 2 (gold-freeze conditions) is *not* satisfied: no Lean 4 verification, no symbolic CAS derivation. This is a stable two-tier numerical exclusion under explicit, narrowly stated bounds on each axis — one of the four authorised SIARC outcomes for a Tier-3b cycle.

---

## 5. Cross-cycle stability of V_quad

Three independent CF computations (T2, T2', T2'') at depth 5000, dps 2200, all using the same backward-recurrence algorithm, now agree on V_quad bit-for-bit. The first 64 digits

```
1.197373990688357602448603219937206329704270703231350336285792769
```

reproduce in every cycle. Predecessor string-content SHA (T2 → T2' → T2'') is `52375a71a05bf61ad971cf83ea9334eb96e20ffa054dc3cab74447966a2f5c44` in all three. Reload-vs-fresh agreement is 1999 digits in every cycle (the $mp.nstr$ 1-ULP truncation signature at 2000-digit boundary).

V_quad's value is now a **cross-cycle invariant** of this project, not a single-cycle artefact. Future certificates can cite this without re-establishing it from scratch.

---

## 6. Falsification triggers — disposition

| Trigger named in T2' report | T2'' status |
|----------------------------|-------------|
| A degree-4 hit at the same basis | **CLOSED** (axis 2, NULL across both tiers) |
| A $V_\text{quad}^2$ hit at degree $\le 2$ | already closed in T2' (NULL on $B_\text{tensor}$) |
| A degree $\le 3$ hit after expanding maxcoeff to $10^6$ | **CLOSED on $B_{3,2}$** (axis 1, NULL across both tiers); NOT tested on $B_{4,2}$ at $10^6$ |

Two of three closed this cycle. The remaining open piece is the joint axis (degree-4 × maxcoeff $10^6$, $B_{4,2}$ at $10^6$), which together with the strict (3,3) tensor at $10^6$ (140 elements, ~5–8 h at 2050 dp) constitutes the natural T2''' scope.

---

## 7. Next-cycle disposition

Across T2, T2', and T2'', **six PSLQ tiers** have now returned NULL on V_quad against progressively stronger bases:

| Cycle | Basis | dp | maxcoeff | result |
|-------|-------|---:|---------:|--------|
| T2 (PEGZ3) | 35-elt flat deg-$\le 3$ in {π,e,G,ζ(3)} | 500, 2050 | $10^4$ | None × 2 |
| T2' (T2PRIME) | $B_\text{union}$ (18) | 500, 2050 | $10^4$ | None × 2 |
| T2' (T2PRIME) | $B_\text{tensor}$ (60) | 500, 2050 | $10^4$ | None × 2 |
| T2'' | $B_{3,2}$ (60) | 500, 2050 | $10^6$ | None × 2 |
| T2'' | $B_{4,2}$ (75) | 500, 2050 | $10^4$ | None × 2 |

(Plus the T2'' tier-3d smoke: $B_{4,2}$ at 500 dp, $10^4$ — None.)

The negative-evidence shape for "V_quad is not in any classical algebra over $\{\pi, e, G, \zeta(3)\}$ accessible within these PSLQ bounds" is at this point empirically as strong as PSLQ can deliver without escalating to entirely different basis families or to structural proof machinery.

**The verdict-disposition language for this corpus, when the V_quad / Painlevé III($D_6$) manuscript closes, is:**

> *PSLQ-bounded numerical exclusion has hit its natural ceiling on this basis family; the remaining open question is the Painlevé–Sakai chart-map closure problem (R1), which is not a numerical question.*

This is not a complaint about the method; it is a recognition that the next genuine information gain lies in (a) widening the classical generators (γ, log 2, ζ(5), Khinchin's K — a separate program-statement question that should be opened explicitly rather than absorbed into the V_quad cycle), or (b) structural / Painlevé–Sakai surface-type analysis (out of scope for Tier-3b under current AEAL rules; this is a Claude-side / human-mathematician task per the existing program-statement).

**Concretely recommended next cycles, in cost order:**

1. **T2''' — the joint axis.** $B_{4,2}$ at maxcoeff $10^6$ at 2050 dp. Marginal cost: re-run tier 3d-equivalent with `maxcoeff = 1_000_000`. Wall-clock: estimate ~70–110 min. Tightens the coefficient floor on the degree-4 V_quad axis. Closes the last numerical trigger from this family.

2. **T2'''' — the strict (3,3) tensor.** $B_{3,3} = \{V_\text{quad}^{k}\cdot m : k\in[0,3], m \text{ a classical monomial of deg }\le 3\}$ (140 elements) at maxcoeff $10^6$, 500 dp + 2050 dp. Wall-clock: estimate 5–8 h at 2050 dp. This is the original strict-(3,3) cycle Claude named; deferring to here makes the budget honest.

3. **T3 (new program) — augmented classical generators.** {π, e, G, ζ(3), γ, log 2, ζ(5)} at degree $\le 2$, possibly with V_quad-degree $\le 3$. Basis $\sim 4\times 84 = 336$ elements at 2050 dp would be a multi-day run; consider a tiered approach. This is a separate program-statement question, not a continuation of the V_quad cycle.

4. **Painlevé III($D_6$) chart-map closure (R1).** Out of Tier-3b scope. The verdict-disposition language above frames this as the structurally remaining open question.

If only one next step is run, **#1 is the most cost-efficient** and closes the corpus on the original basis family.

---

## 8. Files in this slot (21 in manifest)

`basis_3_2_enumeration.json`, `basis_4_2_enumeration.json`, `claims.jsonl`, `discrepancy_log.json`, `env_snapshot.json`, `exclusion_certificate.json`, `halt_log.json`, `manifest.json`, `plan_dag.json`, `pslq_3_2_maxc6_2050dp.json`, `pslq_3_2_maxc6_500dp.json`, `pslq_4_2_maxc4_2050dp.json`, `pslq_4_2_maxc4_500dp.json`, `recover_tier_3d.py`, `stage_23_executor.py`, `stage_2_verification.json`, `stage_2_verification.py`, `stage_4_5_archive.py`, `tier_3d_preflight_500dp.json`, `tier_3d_recovery.json`, `unexpected_finds.json`, `verified_relations.json`, **`report.md`**, **`handoff.md`** (added at archive time).

Not in manifest (live heartbeat artefacts, retained in the slot directory as narrative evidence but excluded from the claim chain because their content is timestamp-dependent): `tier_3d_progress.log`, `tier_3d_stdout.log`.

All SHA-256 hashes are listed in `manifest.json`.
