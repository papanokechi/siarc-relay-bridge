# Handoff — T3B-VQUAD-EXCL-T2PRIME
**Date:** 2026-05-19
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~70 min (Stage 2+3 executor ~64 min; archive + report < 1 min; debug iterations ~5 min)
**Status:** COMPLETE

## What was accomplished

Executed Claude's T2' follow-up cycle to the T2 exclusion (`T3B-VQUAD-EXCL-PEGZ3`, predecessor commit `648dbbe`). The cycle tests whether V_quad satisfies any Q-linear relation over the basis $B_\text{union} = \{V_\text{quad}^k : k=0..3\} \cup \{\pi^a e^b G^c \zeta(3)^d : a+b+c+d \le 2\}$ (18 elements, the literal smallest test Claude named) and additionally over the strictly stronger tensor basis $B_\text{tensor} = \{V_\text{quad}^k \cdot m : k=0..3, m \text{ a deg-}\le 2 \text{ classical monomial}\}$ (60 elements). All four PSLQ runs (each basis × each of 500 dp / 2050 dp) returned `None`. Combined verdict: **EXCLUSION_CERTIFIED**.

## Key numerical findings

- V_quad reload from predecessor 2000-digit text artefact: string-content SHA-256 `52375a71…f2f5c44` reproduces exactly. Reload-vs-fresh agreement 1999 digits at 2200 dps (the expected ~1-ULP `mp.nstr` truncation signal, threshold $\ge 1998$).
- V_quad fresh dual-depth CF agrees to 2200 digits between depths 5000 and 6000 at 2200 dps working precision. (script: `stage_23_executor.py`)
- $B_\text{union}$ @ 500 dp, tol $=10^{-450}$, maxcoeff $=10^4$, maxsteps $=2000$: PSLQ → None (17.9 s).
- $B_\text{union}$ @ 2050 dp, tol $=10^{-1970}$, maxcoeff $=10^4$, maxsteps $=4000$: PSLQ → None (174.4 s).
- $B_\text{tensor}$ @ 500 dp, same parameters except basis size 60: PSLQ → None (224.7 s).
- $B_\text{tensor}$ @ 2050 dp, same: PSLQ → None (3439.0 s ≈ 57.3 min).
- Combined two-tier two-basis: EXCLUSION_CERTIFIED under the stated coefficient bound. (artefact: `exclusion_certificate.json`)

## Judgment calls made

1. **Ran both $B_\text{union}$ AND $B_\text{tensor}$ when the relay prompt named only the union.** The textual ambiguity in Claude's prompt was: *"smallest test that would catch a polynomial relation between V_quad and the classicals."* The literal union basis catches only $\sum c_k V_\text{quad}^k + \sum d_j m_j = 0$ with scalar Z-coefficients — i.e., it catches a *polynomial relation in $V_\text{quad}$* AND a *Q-linear relation among classicals* separately, not a coupled polynomial-with-non-scalar-coefficient relation. The tensor basis is the conservative reading of "polynomial relation between V_quad and the classicals" as it includes products $V_\text{quad}^k \cdot m$. To avoid under-reporting, I ran both and report two sub-certificates. The 60-element tier was the dominant cost (~57 min), but stayed within plausible session budget. If this is wrong, the union sub-certificate alone is what Claude asked for and stands on its own.

2. **Used a fresh-computed V_quad at depth 5000 / 2200 dps for PSLQ rather than the reloaded mpf.** The reload-vs-fresh agreement is intrinsically capped at ~1999 digits by `mp.nstr` 2000-digit truncation in the predecessor. PSLQ at 2050 dp consuming a value with only ~1999 reliable digits would be running below its nominal precision floor. Switching to the fresh value preserves the 2200-digit working precision PSLQ expects. The reload is retained as a documented provenance sanity check (string-content SHA-256 match + 1999-digit agreement; both required to pass). This is a deviation from my first-draft plan, which intended to use the reloaded mpf as PSLQ input.

3. **`maxcoeff = 10^4` carried forward unchanged from T2.** The relay prompt did not specify a maxcoeff lift; I kept it at $10^4$ for direct comparability with the predecessor exclusion catalogue. The next-cycle recommendations list a $10^6$ lift as the cheapest single follow-up.

4. **CF cross-check depth pinned at 5000 / 6000.** Same as predecessor; the predecessor's 48-digit agreement against an independent reference is already part of the slot's provenance chain.

## Anomalies and open questions

1. **Predecessor SHA bookkeeping ambiguity (resolved here, but worth recording).** The T2 predecessor stored *two different SHA-256 values* for V_quad in different artefacts:
   - `52375a71…f2f5c44` — SHA of the **string content** (the 2000-character decimal digits, before file write).
   - `40418cb8…cee1b4dfb3` — SHA of the **file bytes** (the same content + trailing `\r\n` on Windows write).
   `claims.jsonl` and `manifest.json` use the file-byte SHA; `raw_candidates.jsonl` events use the string-content SHA. Both are correct hashes of distinct objects, but their distinction was not documented. T2' verifies the string-content SHA (line-ending-safe) and also computes the file-byte SHA. **Recommended convention for future cycles: every persisted numerical value records `string_content_sha256` AND `file_bytes_sha256` as two named fields, with explicit comments distinguishing them.**

2. **The expected reload precision is one digit less than the stored precision.** Round-tripping a value through `mp.nstr(v, 2000)` and back via `mp.mpf(s)` reliably preserves 1999 digits, not 2000. The last printed digit is rounded at the print boundary; the parse cannot recover the lost ULP. The first-draft cross-check threshold of 2000 digits triggered a `RuntimeError` on this exact pattern. Documenting in case any future relay-prompt validation logic hits the same boundary.

3. **None of the falsification triggers Claude named fired.** Specifically: no $V_\text{quad}^2$ hit at degree $\le 2$ (already inside $B_\text{tensor}$ — would have shown), no relation at $|c| \le 10^4$. The remaining unfired triggers (degree-4 V_quad, maxcoeff $10^6$) are listed in `report.md` §5 as candidate next cycles.

## What would have been asked (if bidirectional)

1. Did Claude intend the union basis literally (in which case the tensor basis is overkill but harmless), or did "polynomial relation between V_quad and the classicals" implicitly include the tensor structure? Reporting both is the safe answer, but it cost ~57 min of compute.
2. Should the precision lift step for the next cycle be (a) maxcoeff $10^6$ at current basis, (b) extend $V_\text{quad}$ side to degree 4, or (c) extend classical side to degree 3? Each closes a different falsification trigger.
3. Is the Painlevé III($D_6$) hypothesis a Claude-side ODE-theoretic audit or a future agent-side numerical/CAS task? Current `pcf2-program-statement` says the former.

## Recommended next step

Single tier rerun: $B_\text{tensor}$ at 2050 dp with `maxcoeff = 1_000_000`. Same script, one constant change. Wall-clock estimate ~60–90 min. Closes the "degree $\le 3$ hit at maxcoeff $10^6$" falsification trigger. If it returns None again, the certificate tightens by two orders of magnitude on the coefficient floor with no infrastructure change. A follow-on cycle then adds $V_\text{quad}^4$ to the bases (closing the last named falsification trigger), and at that point the program-level conclusion "Painlevé III($D_6$) is the cleanest remaining explanation by elimination" is supportable from the agent side.

## Files committed

In `sessions/2026-05-19/T3B-VQUAD-EXCL-T2PRIME/`:
- `basis_tensor_enumeration.json` (60 elements, structured)
- `basis_union_enumeration.json` (18 elements, structured)
- `claims.jsonl` (9 AEAL entries)
- `discrepancy_log.json` (empty `{}`)
- `env_snapshot.json` (predecessor reference, both git HEADs, mpmath/sympy versions)
- `exclusion_certificate.json` (two sub-certificates: union NULL, tensor NULL; combined EXCLUSION_CERTIFIED)
- `executor_summary.json` (top-line summary)
- `halt_log.json` (empty `{}`)
- `manifest.json` (18 files, SHA-256)
- `plan_dag.json` (13 nodes; halt conditions; agreement gates)
- `pslq_tensor_2050dp.json`
- `pslq_tensor_500dp.json`
- `pslq_union_2050dp.json`
- `pslq_union_500dp.json`
- `raw_candidates.jsonl` (Stage 2 + Stage 3 event logs)
- `stage_23_executor.py` (the executor)
- `stage_4_5_archive.py` (the archive)
- `unexpected_finds.json` (empty `{}`)
- `verified_relations.json` (intentionally empty; pointer to exclusion_certificate.json)
- `report.md`
- `handoff.md` (this file)

## AEAL claim count

9 entries written to `claims.jsonl` this session (provenance reload, fresh CF, $B_\text{union}$@500, $B_\text{union}$@2050, $B_\text{tensor}$@500, $B_\text{tensor}$@2050, $B_\text{union}$ verdict, $B_\text{tensor}$ verdict, combined verdict).
