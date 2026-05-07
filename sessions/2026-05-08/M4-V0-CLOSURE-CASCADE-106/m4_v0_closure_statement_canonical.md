# M4 V0 closure statement — canonical (synth-ratified)

**Status**: CANONICAL (synth-ratified 2026-05-08 by Claude Opus 4.7 / Claude.ai web / T1-Synth via `ACCEPT_W_REVISIONS`)
**Source**: `m4_v0_ratification_template.md` §4 (revised closure statement)
**Supersedes**: §2 proposed wording in same template (preserved with SUPERSEDED-by-§4 marker)
**Confidence**: MEDIUM-HIGH (HIGH reserved for post-W21-LANE-1 ratification + post-Wasow §X.3 OCR acquisition state)

---

## Canonical M4 V0 closure statement

```
M4 V0 CLOSED via the deg_a=0 row mechanism (068 verdict
UPGRADE_FULL_VIA_DEG_A_ZERO_ROW, Phase Q.SUP=YES). The deg_a=0
row supersedes the prior expected closure path (Costin-Borderline
/ B-T 1933 §1 anormal q=2 fractional-rank resurgence) per the
rubber-duck-vindicated supersession audit (HALT_068_OVER_CLAIM
5-item checklist, all satisfied), and provides the structural
M4-stratum closure at zero acquisition cost.

The closure runs at the algebraic-combinatorial level via the
four-row Phase A WZ-balance enumeration extension (064 §2.3) +
V6 closed-form general formula A_naive = 2d − d_a (specialised
to deg_a=0, the SIARC stratum's operative row, yielding
A_naive = 2d uniformly at general d ≥ 2). Closed-form-in-d;
does not require Wasow §X.3 Newton-polygon factorization
(forward-pointed, OCR-deferred, not-blocking).

Numerical residuals at dispatch dps clean: d=3 cubic
A_fit = 5.978 ± 0.026 (dps=800, 50 families), d=4 quartic
A_fit = 7.954 ± 0.0037 (dps=1200, 60 families), d=2 V_quad
sanity A=4 — all within 1σ of V6 prediction after standard
1/log N finite-window correction. Phase B (Costin §4.7a Thm
4.147 + §5.0c Thm 5.11) provides secondary confirming evidence
at the formal-asymptotic level; Phase C confirms the deg_a=0
row sits in the normal case (B-T 1933 §1, p=1).

No halt conditions triggered (0/10 envelope halts across STEP 0
+ Phases A–E); 14 AEAL claims ledgered.

Confidence: MEDIUM-HIGH. HIGH reserved for post-W21-LANE-1
ratification + post-Wasow §X.3 OCR acquisition state.
```

---

## Provenance + propagation requirements

**Provenance**: synth-tier ratification by Claude Opus 4.7 (Claude.ai web, T1-Synth) at 2026-05-08 ~08:30 JST. Substrate verification: substrate-grounded (5 paste-ready excerpts in `m4_substrate_excerpts.md`; 7/7 PASS §2-vs-substrate consistency check), NOT trust-relay via 074 DOSSIER_COMPLETE.

**Substrate SHAs (frozen)**:
- 068 closure fire: `e7bfe49` at `sessions/2026-05-07/T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE-068/handoff.md`
- 074 ratification dossier: `9596c21` at `sessions/2026-05-07/T2-M4-RATIFICATION-DOSSIER-ASSEMBLY-074/handoff.md`

**Propagation requirements** (any downstream artifact citing M4 V0 closure must do all of):

1. **Use this canonical wording verbatim** (or quote in italics with the synth-ratification provenance line). Do NOT paraphrase or strip qualifications.

2. **Carry the confidence qualifier**: `M4_V0_CLOSED (MEDIUM-HIGH; HIGH-pending)` for short-form references; full confidence qualification for any expanded citation.

3. **Cite both substrate SHAs**: `e7bfe49` (068 closure) AND `9596c21` (074 dossier). Pre-flight `git rev-parse` discipline applies — verify both SHAs exist in bridge git history before any new artifact citing them is sealed.

4. **Wasow §X.3 non-dependency**: any M4-stratum follow-on relay or paper draft must inherit the "closed-form-in-d at the algebraic-combinatorial level; Wasow §X.3 forward-pointed, OCR-deferred, not-blocking" posture. Wasow §X.3 OCR is NOT a closure prerequisite; it is a forward-pointed acquisition target tied to MEDIUM-HIGH → HIGH confidence upgrade.

5. **HIGH upgrade pre-conditions**: HIGH confidence upgrade requires BOTH (a) post-W21-LANE-1 ratification (full LANE-1 batch pass including M6.CC R1 closure cross-witness), AND (b) post-Wasow §X.3 OCR acquisition state (forward-pointed acquisition completed). Either condition alone is insufficient.

---

## Downstream artifacts carrying this canonical wording

Required propagation cycle:

1. **Picture-chain v1.21** (next picture deposit after v1.20): include `M4_V0_CLOSED (MEDIUM-HIGH; HIGH-pending)` tag in milestone ledger; cite both substrate SHAs; reference this canonical wording artifact. Tracked in SQL todo `picture-v120plus-m4-closed-tag-annotation`.

2. **Umbrella v2.1**: include canonical M4 V0 closure statement (replaces any v2.0 stub or proposed §2 wording reference); ledger SHA-correction `aab7ee2` → `9596c21` as AEAL claim correction (not substrate gap); fold in §6 verification semantics amendment from 105. Tracked in SQL todo `umbrella-v21-m4-closure-amendments`.

3. **PCF-2 v3.x** (if revised for M4 V0 announcement): use canonical wording; do not paraphrase. AEAL-discipline check on any "shows" / "confirms" / "proves" verb usage in M4 closure context.

4. **Lean-4 formalization** (if M4 closure is targeted for Lean-4 proof scaffold): canonical wording is the human-language closure statement; Lean-4 theorem statement must be derivable from + materially consistent with it.

5. **Any external presentation / preprint citing M4 closure**: use canonical wording; carry confidence qualifier; cite both substrate SHAs.

---

## Cross-references

- Synth signature capture: `synth_signature_capture.md`
- Cascade record: `cascade_record.md`
- SHA origin trace: `sha_origin_trace.md`
- Substrate excerpts: `tex/submitted/control center/m4_substrate_excerpts.md`
- Ratification template (executed): `tex/submitted/control center/m4_v0_ratification_template.md` §4
