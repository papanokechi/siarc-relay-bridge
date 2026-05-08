# Phase E — Cascade-stub forward-prompt outline

This phase produces an OUTLINE only for a hypothetical follow-up envelope
`T2-FOLLOWUP-111-STOKES-ANCHOR-PROVENANCE-TRACE`. Per spec STEP E.2: this
outline is a 1-2 page structural sketch sufficient for a future
operator-tier drafting cycle. The prompt body is **NOT drafted in this fire**.

---

## E.1.a SCOPE

Trace the upstream provenance of the 14-digit anchor `S = 0.43770528073458`
that appears as a hardcoded string literal at
`pcf-research/vquad/scripts/jimbo_final.py:26`. Specific questions:

1. **Where do these 14 digits actually originate?** The Phase B audit in this 122 fire records that `jimbo_final.py` itself does not compute them — it consumes them as INPUT for PSLQ attribution attempts.
2. **Is there a separate producer pipeline elsewhere in `pcf-research/`?** Candidates to inspect:
   - `pcf-research/vquad/scripts/t2_iter17_stokes.py` (110-UF-110-1 forward-pointer; 14-digit S anchor reportedly produced in the 2026-04-* T2-iter cycle)
   - `pcf-research/vquad/scripts/verify_frobenius_apparent.py`
   - `pcf-research/vquad/results/t2_iter23_jimbo.json` (110 UF-110-7 forward-pointer; project-specific Dingle convention reportedly anchored here)
   - any `.json` result file under `pcf-research/vquad/results/` whose body contains the digit string `0.43770528073458`
3. **Is there a literature citation underwriting the digits?** Candidates:
   - Dingle (1973) "Asymptotic Expansions: Their Derivation and Interpretation"
   - Forrester-Witte (2002) §X (the 110 D.1.b substrate path)
   - Berry-Howls late-term hyperasymptotic formula (referenced but not anchored in 110-EXEC)
   - Jimbo (1982) "Monodromy problem and the boundary condition for some Painleve equations" (Publ. RIMS Kyoto)
4. **Is there a hand-computation in operator notes?** Out of scope for `pcf-research/` repo; flag if encountered in `cli_log/` or `tex/submitted/control center/`.
5. **Git-archaeology trace** — earliest filesystem appearance of the digit string:
   ```powershell
   git log --all -S "0.43770528073458" --oneline -- "pcf-research/**"
   ```
   Identify the earliest commit; inspect the diff for the producing context.

---

## E.1.b PRECONDITION

Bridge HEAD should be at or beyond the commit landing this 122 audit (i.e.,
the 122 commit should be reachable via `git merge-base --is-ancestor`).

Additional precondition: the operator must NOT have already produced an
equivalent provenance trace in a prior `STOKES-ANCHOR-PROVENANCE-TRACE`
session. STEP 0.2 supersession scan in the followup envelope must check for:

```powershell
Get-ChildItem siarc-relay-bridge\sessions -Directory -Recurse |
    Where-Object { $_.Name -match "STOKES-ANCHOR-PROVENANCE" -or
                   $_.Name -match "S-ANCHOR-PROVENANCE" -or
                   $_.Name -match "JIMBO-FINAL-S-NUM-TRACE" }
```

---

## E.1.c TIER

**T2-OPERATOR** literature-trace + git-archaeology. Estimated agent
runtime: ~60-90 minutes.

Sub-phases:
- Phase A: git-archaeology on `pcf-research/` (~15 min)
- Phase B: filesystem grep for digit-string appearances (~10 min)
- Phase C: producer-pipeline inspection of the earliest-commit context (~25 min)
- Phase D: literature anchor cross-check via on-disk PDF substrate at `g3b_2026-05-03/supplementary/` (~15 min)
- Phase E: verdict synthesis (~10 min)
- Phase F: self-checks + AEAL + bridge deposit (~10 min)

---

## E.1.d EXPECTED OUTCOMES (4 bins)

| Bin | Trigger | Implication for 069r3 FINAL synthesis |
|---|---|---|
| (i) **PROVENANCE_TRACED_TO_PRODUCER_PIPELINE_IN_REPO** | `pcf-research/` script computes the 14 digits via documented algorithm | Cited anchor has independent producer; 069r3 cross-check can re-fire at higher dps |
| (ii) **PROVENANCE_TRACED_TO_LITERATURE_CITATION** | digits trace to published table or formula in on-disk PDF substrate | Cited anchor has external authority; 110 D.1.b FW substitute path is one application of a published anchor |
| (iii) **PROVENANCE_TRACED_TO_HAND_COMPUTATION** | digits appear in `cli_log/` or operator notes with derivation sketch | Cited anchor has provenance but is not algorithmically reproducible without operator memory |
| (iv) **PROVENANCE_OPAQUE_DOCUMENTATION_GAP** | digits found at multiple sites without any producer; appearance is committed without explanation | Cited anchor is folkloric within the repo; further forward-pointer to symbolic re-derivation needed |

The pre-fire empirical signal (110-UF-110-1 + UF-110-7) suggests bin (i) — a producer pipeline at `pcf-research/vquad/scripts/t2_iter17_stokes.py` or sibling — but this is an unaudited claim and Phase B+C of the followup must check.

---

## E.1.e DELIVERABLES (~5 files)

1. `stokes_anchor_provenance_trace.md` — narrative trace + git log + filesystem grep + literature cross-check + verdict-bin selection.
2. `git_archaeology_log.json` — structured commit-by-commit trace of the digit string's earliest filesystem appearance.
3. `claims.jsonl` — AEAL claims (≥ 4 floor; suggested 6).
4. `halt_log.json` — halts (empty `{}` if none triggered).
5. `discrepancy_log.json` + `unexpected_finds.json` — standard SIARC quartet.
6. `handoff.md` — standard SIARC handoff with §"Verdict ladder" + §"Recommended next step" sections.

---

## E.2 Cascade-implication notes

Two paths unlock from the followup envelope's verdict:

**If bin (i) producer pipeline lands in repo:**
- Re-fire `lax_pair_solver.py` Phase B.3 with the producer-aligned Dingle-normalisation convention (110-UF-110-7 forward-pointer); upgrade `S` digits-of-agreement from 0 (110 anomaly D-110-3) to ≥ 8.
- Optionally implement Domb-Sykes acceleration to push `xi_0` digits-of-agreement from 2.04 (110 D-110-4) to ≥ 5.
- These two upgrades convert the 110 verdict bin from `GO_ROUTE_D_PARTIAL_VIA_FW` to `GO_ROUTE_D_CONFIRMED_VIA_FW` *without* needing JM 1981 Part II (which remains Tier 3 paywalled per relay 102 verdict).

**If bin (ii)-(iv) lands:**
- The genuine cross-check residual remains OPEN.
- Forward-pointer for JM 1981 Part II acquisition (Tier 3 paywalled) becomes higher priority.
- Alternative: pivot to D.1.a path via direct symbolic inverse-monodromy from the FW (4.3) auxiliary Hamiltonian per UF-105-MECHANISM-A-DERIVATION-FORWARD-POINTER (105 substrate path).

In all four bins, this Phase E followup envelope addresses the residual that the present 122 audit explicitly does NOT address. The two fires are complementary: 122 demotes the inversion-function-output side; the followup audits the upstream Stokes-data anchor.

---

## E.3 Out-of-scope items (NOT covered by the followup)

- Re-litigation of the 109-EXEC `NO_GO_OFF_DEGENERATION` verdict.
- Acquisition of JM 1981 Part II.
- Re-litigation of the 110-EXEC handoff structure or this 122 verdict.
- Modification of any source file under `pcf-research/`.
- Re-derivation of the FW (2.2) PV null-sum at the V_quad parameter point (Route B 109-EXEC has already locked this question via three independent obstructions).
