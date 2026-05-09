# Q22 Math Arbitration — Supersession Memo (124 Halted by 099)

**Task ID:** T1-SYNTH-M2-Q22-MATH-ARBITRATION-124-HALT-SUPERSEDED-BY-099
**Date:** 2026-05-09
**Halt code:** HALT_124_PRIOR_ARBITRATION_EXISTS
**Operative arbitration of record:** `T1-Q22-DEPOSIT-READINESS-MEMO-099` (2026-05-07)
**Operative verdict:** `COMPLETE_PATH_A_RECOMMENDED` (HIGH confidence)

---

## §1. WHY THIS IS A HALT

Prompt 124 was drafted in slate 120-124 to fire a T1-Synth substrate-direct derivation packet for the Q22 path-(a) vs path-(b) decision. Its own Phase 0 STEP 0.2 says:

> *"If a prior arbitration fire LANDED with verdict: HALT_124_PRIOR_ARBITRATION_EXISTS; supersede or absorb"*

Phase 0 STEP 0.2 audit at 124 fire-time (bridge HEAD `24021ec`, 2026-05-09 ~14:50 JST) located:

- `siarc-relay-bridge/sessions/2026-05-07/T1-Q22-DEPOSIT-READINESS-MEMO-099/` — LANDED 2026-05-07
- Status: `COMPLETE_PATH_A_RECOMMENDED` (line 5 of 099 handoff.md)
- Deliverables: `q22_deposit_readiness_memo.md`, `threshold_sufficiency_analysis.md`, `precedent_table.md`, AEAL quartet, handoff (8 files total)

This trips the Phase 0 STEP 0.2 condition. 124 must NOT fire substantively. Memo follows.

## §2. CHAIN-OF-EVIDENCE FROM 099

The 099 verdict is substrate-anchored on:

| Evidence | Substrate | Value / claim |
|---|---|---|
| `\|delta_path_a\|` | `pcf2_v1.4_amendment.md` SHA16 `88845089434F96EF`, 11-param LIN refit | `3.08904186542e-23` at K_FIT=7 / dps=25000 / N up to 1200, max across families Q_30..Q_33 |
| Per-family A_lin readouts | `load_log.txt` L11/L14/L17/L20 | `5.99999999999999999999999` (fam30, fam31), `5.99999999999999999999998` (fam32), `5.99999999999999999999996` (fam33) at dps=25000 |
| Chowla-Selberg PSLQ search | maxcoeff=10^50, tol=10^-40 on H6 basis B19+ | No non-trivial Γ(1/3) relation in any of the four families |
| Reviewer A (peer-AI 4-of-4) | 099 cite | "23-digit agreement is roughly 10^8 beyond what PSLQ-style identifications usually require for publication" (HIGH confidence on this clause) |
| Reviewer D (peer-AI 4-of-4) | 099 cite | HIGH confidence; "move to deposit Path-a immediately" verbatim |

## §3. WHY 099 ALREADY ANSWERS 124

124's framing was: "the Q22 question (path-(a) vs path-(b)) governs which mathematical content goes into PCF-2 v1.4 manuscript". Under RULE 1, the **manuscript content** is in scope and the **Zenodo deposit** is TABLED.

099 was framed in deposit-readiness terms, not manuscript-content terms — but the recommendation transfers cleanly:

- If path-(a) is **deposit-eligible** at HIGH confidence per 099 (i.e., the substrate at K_FIT=7 / 11-param / `\|delta\|`~1e-23 is sufficient for downstream consumers), then path-(a) is also **manuscript-content-ready**.
- Holding manuscript content for path-(b) (K_FIT=9 / N=2400 / ~24-hr high-compute fire) is a strictly stronger condition than holding deposit for path-(b); under RULE 1's manuscript-content-on-critical-path framing, this is unmotivated.
- 099's reclassification of path-(b) as a POST-deposit stretch goal applies a fortiori as a POST-manuscript-content stretch goal.

## §4. RESIDUAL ANOMALIES FROM 099 (still relevant)

099 closed with five anomalies (A1-A5) that 124 had no special leverage to discharge. They remain residuals of the 099 verdict, NOT new arbitration content:

- **A1.** Three mutually-inconsistent path-(b) precision figures (`~10^21000`, `10^-44300`, `~1.7e-34`). Memo did not depend on which is correct. **Not blocking manuscript content.**
- **A2.** BBP arXiv ID hallucination in 099 prompt body (`arXiv math.CA/9803067`). Pre-verification at fire time per post-031 rule caught it. **Not blocking manuscript content.**
- **A3.** Path-(a) realized at K_FIT=7 (11-param), not K_FIT=9 (13-param) as the 014 prompt title suggested. 099 cited 11-param consistently. **Not blocking manuscript content; clean substrate citation.**
- **A4.** Stretch-goal compute envelope unanchored (peak-RAM, maxcoeff for path-(b)). **Only relevant if operator chooses (O) override; not on critical path.**
- **A5.** Reviewer-supplied venue precedents are genre-only (Ramanujan J., Exp. Math., Res. Number Theory). **Not blocking manuscript content; appendix-quality polish if desired.**

## §5. RECOMMENDED RECLASSIFICATION

The SQL todo `q22-014-stretch-goal-arbitrate` should be reclassified:

- **Was:** "Operator + Claude decide whether `\|delta_lin\|` ~1e-23 + no-CS-relation in H6 B19+ formally closes G5+G16 for PCF-2 v1.4 deposit (path (a)), or whether the stretch goal `\|delta\|` < 1e-30 must be hit first (path (b))."
- **Now:** "Operator accepts 099 path-(a) recommendation per `T1-Q22-DEPOSIT-READINESS-MEMO-099` (2026-05-07, HIGH confidence). Manuscript content ready under path-(a); Zenodo deposit step itself remains TABLED under RULE 1 until M-axis closure lifts. No further synth fire required."

Recommended SQL action:

```sql
UPDATE todos
SET status = 'in_progress',
    description = 'Operator accepts 099 path-(a) recommendation per T1-Q22-DEPOSIT-READINESS-MEMO-099 (2026-05-07, HIGH confidence + Reviewer A/D both HIGH). Manuscript content ready under path-(a); Zenodo deposit step itself remains TABLED under RULE 1 until M-axis closure lifts. No further synth fire required.'
WHERE id = 'q22-014-stretch-goal-arbitrate';

UPDATE todos
SET status = 'done',
    description = COALESCE(description, '') || ' [SUPERSEDED_BY_099 per T1-SYNTH-M2-Q22-MATH-ARBITRATION-124-HALT-SUPERSEDED-BY-099 commit (TBD); 099 verdict path-(a) HIGH confidence transfers cleanly to manuscript-content under RULE 1]'
WHERE id = 'relay-124-m2-q22-math-arbitration';
```

## §6. RULE 1 ALIGNMENT CHECK

- **Manuscript content:** path-(a) ready per 099 substrate. ✓ (math-foundational, in scope)
- **Zenodo deposit:** path-(a) deposit-eligible per 099, but actual deposit step remains TABLED. ✓ (admin/distribution, out of scope until M-closure lift)
- **Operator decision:** unilateral ratification of 099 recommendation. ✓ (no fire; no admin work; pure operator decision)
- **No synth re-fire:** ✓ (would duplicate 099 work; violates supersession-gate pattern from prompt-drafting discipline memory)

## §7. PROMPT-DRAFTING BLIND SPOT (recurrent pattern)

Slate 120-124 was drafted at ~11:25 JST 2026-05-09. The Phase 0 STEP 0.2 supersession-audit instruction was **inside** the 124 prompt body (line 58-61) but was NOT performed AT DRAFT TIME. This is a recurrent pattern (cf. prompt-drafting discipline memory: *"Before drafting any multi-phase relay prompt, search the bridge for prior full-fires of the same task scope; if a prior LANDED fire exists, scope the new prompt to discharge the residual rather than re-fire — supersession-gate pattern (Phase 0 STEP 0.1-0.6) is mandatory."*).

This is the SECOND observed within-week instance of Phase 0 supersession-audit being deferred to fire-time rather than draft-time:

1. 069 v1 (2026-05-06): supersession by 058R caught at rubber-duck QA, not draft.
2. 124 (2026-05-09, this fire): supersession by 099 caught at fire-time STEP 0.2, not draft.

**Recommended hardening:** the operator may want to add a draft-time supersession check to the slate-drafting workflow itself, not merely as a Phase 0 step inside individual prompts.

## §8. END

End of supersession memo. 124 halts cleanly; 099 verdict stands as Q22 operative arbitration; relay-124 SQL todo absorbed; q22-014 SQL todo reframed as operator-ratification (no fire).
