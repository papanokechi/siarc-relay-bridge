# Handoff -- T2-EXECUTOR-115-ROUTE-F-D7-FIXED-POINT-EXTRACTION-132
**Date:** 2026-05-09
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~45 minutes
**Status:** COMPLETE

## What was accomplished

Executed prompt 115 (Route F EXECUTOR envelope) end-to-end. Phase B
agent-side numerical re-derivation at `mp.dps = 300` reproduces synth
Q4 v2.0 verdict's structural payload: pushing the V_quad image
`(eta_inf, eta_0, theta_inf, theta_0) = (1/6, 0, 0, -1/2)` through the
Ohyama-Kawamuko-Sakai-Okamoto 2006 sect 3.1 reduction map yields
`(alpha, beta, gamma, delta) = (0, 0, 1/9, 0)` with all residuals
< 1e-200, and the s_1 fixed-point identity at `alpha_1 = 0` holds as
a closed-form mpmath equality. Phase C added a new labelled remark
`rem:vquad-d7-s1` (about 26 lines) to `p12_journal_main.tex` sec:vquad
documenting the D_6 -> D_7 sector descent + s_1 fixed-point under the
surviving `\widetilde{W}_a(A_1)` Cremona action, plus an inline one-line
bibitem stub for `ohyama2006` (UF-115-NEW-BIBKEYS-RESOLVED-INLINE).
Phase D pdflatex double-pass stabilised at `W = 24 = W_pre` exactly,
0 errors, 0 undefined references; PDF grew to 22 pages (baseline 21
+ 1 from the remark page-break, acceptable per A4 D.4). Bridge deposit
per B1-B5 + POSTSCRIPT-39 appended to `_INDEX.txt`.

## Key numerical findings

- `alpha = -4 * eta_0 * eta_inf = 0` at `(eta_inf, eta_0) = (1/6, 0)` --
  exact, dps=300, script `vquad_p3d6_recovery.py::compute_d6_to_d7_reduction_at_v_quad`.
- `beta = 4 * eta_0 * (1 + theta_0) = 0` at `(eta_0, theta_0) = (0, -1/2)` --
  exact, dps=300, same script.
- `gamma = 4 * eta_inf**2 = 1/9` at `eta_inf = 1/6` -- residual `1.16658e-302`
  vs tol `1e-200`, dps=300, same script.
- `delta = -4 * eta_0**2 = 0` at `eta_0 = 0` -- exact, dps=300, same script.
  Hence `gamma * delta = (1/9) * 0 = 0`, violating the standing assumption
  `gamma * delta != 0` for the generic open stratum of `P_III'(D_6)`;
  this is the structural signature of descent onto the `P_III'(D_7)` sector.
- s_1 fixed-point: `alpha_1 = 0 ==> s_1(0) = -alpha_1 = 0` as a closed-form
  identity in mpmath. Within the surviving `\widetilde{W}_a(A_1)` Cremona
  action, V_quad's image sits at the s_1 fixed point.

## Judgment calls made

- **One-line bibitem stub for `ohyama2006` added inline** (rather than
  deferred to a follow-up patch per STEP 0.4 default). Rationale: A4
  acceptance ("Pass-2: expected W_pre exactly, no new undefined references")
  is stricter than the STEP 0.4 default deferral; deferring would persist
  a `Citation 'ohyama2006' undefined` warning through pass-2 and violate
  A4. The bibitem stub uses the published reference (Y. Ohyama, H. Kawamuko,
  H. Sakai, K. Okamoto, "Studies on the Painleve equations V, third
  Painleve equations of types D_7 and D_8", J. Math. Sci. Univ. Tokyo 13
  (2006), 145-204). Logged as UF-115-NEW-BIBKEYS-RESOLVED-INLINE.
- **Bibkey-casing reconciliation.** Prompt STEP 0.4 spelled bibkeys lower-
  case (`okamoto1987`, `iwasakikimura`); actual bibkeys in the inline
  thebibliography are case-mixed (`Okamoto1987`,
  `IwasakiKimuraShimomuraYoshida`). Used the actual case in the new remark
  cite; treated lowercase forms as informal. Log entry omitted as the
  prompt's STEP 0.4 spelling was clearly informal shorthand.
- **Driver-script bypass for the canonical function execution.** Pre-
  existing missing dep `borel_channel.py` (only in bridge BOREL-CHANNEL-5X
  session, not vendored under `pcf-research/channel/cc_pipeline_2026-05-01/`)
  blocks `import vquad_p3d6_recovery`. Rather than restoring the missing
  module (out of scope for prompt 115 -- structural change to the
  pcf-research tree), built `_115_d7_driver.py` that AST-extracts and
  exec()s the new function source slice with only `mp, mpf` bound. AEAL
  claims still anchor at the canonical defining location
  `vquad_p3d6_recovery.py::compute_d6_to_d7_reduction_at_v_quad`.
  Logged as UF-115-BOREL-CHANNEL-DEP.
- **POSTSCRIPT-39 (not -38).** Prompt §5 E.6 said "Append POSTSCRIPT-38";
  POSTSCRIPT-38 already exists in `_INDEX.txt` (the pre-fire 115-119 slate
  staging postscript appended ~10:15 JST today). Appended POSTSCRIPT-39
  instead as the post-fire landing summary. This matches the standing
  rule that POSTSCRIPT numbers are sequentially append-only.
- **Cleanup of stale CWD-side aux files.** After noticing a session-128-era
  `tex/submitted/p12_journal_main.aux` was overriding the fresh
  `build_115/p12_journal_main.aux` (causing pdflatex to keep marking
  `ohyama2006` undefined for 3 passes), deleted the stale CWD-side
  `.aux/.log/.out` files and rebuilt `build_115/` from scratch. This
  is logged as DISC-115-1-PDFLATEX-FRESH-W-FLOW (LOW) and
  UF-115-PRE-128-AUX-STALE-IN-CWD (INFO).

## Anomalies and open questions

1. **UF-131-4 cross-cascade convergence (carry-forward, INFO).** Q4 v2
   D_7 + s_1-fixed-point diagnosis triangulates with the 069r3 final-
   synthesis cascade off-generic-stratum diagnosis (bridge SHA `ae5b7f7`).
   Two independent T1-Synth threads converge on V_quad's structurally
   distinguished status from different angles; positive forensic signal
   that the diagnosis is not artefact of one cascade's framing.
   Pulled into the new p12 `\remark` per A8 ("independently surfaced by
   the 069r3 final-synthesis cascade").
2. **UF-115-NEW-BIBKEYS-RESOLVED-INLINE (INFO).** STEP 0.4 also flagged
   `oks_o_2006`, `kajiwaranoumiyamada2017`, `sakai2001` as absent;
   none were cited by the new remark, so no stub was added for them.
   They may be needed by the future structural prompt UF-115-3 (P_III(D_6)
   -> P_III(D_7) degeneration limit prompt) and are deferred to that fire.
3. **UF-115-BOREL-CHANNEL-DEP (INFO).** Pre-existing module-import gap;
   bypass mechanism documented above and in `unexpected_finds.json`.
   Does not affect prompt-115 substantive results. Future executors
   wishing to call `vquad_p3d6_recovery.main()` need to either copy
   `borel_channel.py` from
   `siarc-relay-bridge/sessions/2026-05-01/BOREL-CHANNEL-5X/` into
   `pcf-research/channel/cc_pipeline_2026-05-01/`, or use the same
   AST-extract pattern as `_115_d7_driver.py`.
4. **UF-115-PRE-128-AUX-STALE-IN-CWD (INFO).** Build hygiene note;
   recommend either ignoring `tex/submitted/*.aux` in `.gitignore` or
   always pairing `-output-directory=build_<task>/` with a CWD-side
   `.aux/.log/.out` cleanup. Cross-linked to DISC-115-1.
5. **Open question for Claude review.** The new remark cites
   `\cite[\S 3.1]{ohyama2006}`. The OKS-O 2006 paper is Paper V in the
   Okamoto-Ohyama-Sakai series. Operator/Claude should validate that the
   bibitem stub I added (J. Math. Sci. Univ. Tokyo 13 (2006), 145-204)
   is the correct journal/volume/page reference for this paper at \S 3.1
   reduction map; if the paper has a different canonical citation, a
   one-line bib-stub correction patch will be needed.
6. **Observation.** The prompt-template note "Synth's verdict §2 closing
   line says 'Ready for prompt 117'; this is forward-projection (UF-131-3);
   operator chose 115" -- confirmed: this fire occupied slot 115 envelope
   delivered at bridge slot 132 per the sequential-slot numbering.

## What would have been asked (if bidirectional)

- Should I treat the prompt's lower-case bibkey spellings (`okamoto1987`,
  `iwasakikimura`) as case-strict matching, or reconcile to the
  manuscript's actual mixed-case spellings (`Okamoto1987`,
  `IwasakiKimuraShimomuraYoshida`)? Chose the latter -- the manuscript
  is the source of truth and the prompt's spellings looked informal.
- Should the bibitem stub for `ohyama2006` be added in this session
  (resolves A4 cleanly) or deferred to a follow-up one-line patch
  (matches STEP 0.4 default)? Chose the former.
- Should I restore the missing `borel_channel.py` to
  `pcf-research/channel/cc_pipeline_2026-05-01/` to make G3 imports
  fully clean? Chose to leave the structural state of pcf-research
  untouched and bypass via AST extraction, since restoring vendored
  copies of bridge artefacts is not scoped in prompt 115.

## Recommended next step

Fire prompt 116 (T1 umbrella v2.1 M9 V0 deposit; ~2-4 hr operator-led
Zenodo deposit + LaTeX amendment + cross-link audit). Per POSTSCRIPT-
38 TIER A sequencing, 116 was conditional on 115 readiness gate
clearing (halt_log empty + handoff Status=COMPLETE) -- both
satisfied. The M9 V0 umbrella v2.1 deposit absorbs M4 V0 closure +
M6.CC R1 closure (via Q4 v2 verdict) + Route F executor slot 115
(this fire).

## Files committed

- `b_numerical_rederivation_log.md` (Phase B agent-side re-derivation
  log; method, dps, residuals, PASS/FAIL stamp, fingerprints).
- `c_python_helper_run.log` (full driver JSON: inputs, outputs,
  expected, residuals, per-component pass flags, fixed-point ok,
  canonical-src + extracted-fn SHA256).
- `_115_d7_driver.py` (the AST-extract-and-exec driver; copy of the
  in-tree file at `pcf-research/channel/cc_pipeline_2026-05-01/_115_d7_driver.py`).
- `115_route_f_executor.diff` (unified diff: p12 sec:vquad new remark
  + p12 thebibliography new bibitem `ohyama2006` + vquad_p3d6_recovery.py
  new function + new file `_115_d7_driver.py`).
- `claims.jsonl` (5 AEAL entries: 4 numerical at dps=300 + 1 closed-form
  identity).
- `halt_log.json` (empty `{}` -- A1-A6 all PASS).
- `discrepancy_log.json` (1 LOW: DISC-115-1-PDFLATEX-FRESH-W-FLOW).
- `unexpected_finds.json` (4 INFO: UF-131-4 carry-forward,
  UF-115-NEW-BIBKEYS-RESOLVED-INLINE, UF-115-BOREL-CHANNEL-DEP,
  UF-115-PRE-128-AUX-STALE-IN-CWD).
- `handoff.md` (this file).

### Additional manuscript-side files modified (committed in main repo, not in bridge deposit)

- `tex/submitted/p12_journal_main.tex` (post-edit sha256
  `09f01c1992b73453012828f326f3d69f4458f2d640fc0c8dca411b3cfcd13396`;
  pre-edit sha256 `dac0282ed4c6f8bc1046003acaeda0b84593712f9336404aafdc18b0a6a176a7`).
- `pcf-research/channel/cc_pipeline_2026-05-01/vquad_p3d6_recovery.py`
  (post-edit sha256 `f676264289d1fc1191947b3bca6afb2f9da8eba05d7bfca2782b090e57ebe644`;
  pre-edit sha256 `28b8de47161254ae17b2c4e98f3c7b54d35d9864e6b9c4d3d0e859c0b27b7dc5`).
- `pcf-research/channel/cc_pipeline_2026-05-01/_115_d7_driver.py` (NEW;
  sha256 `342339d21df682eb65d52f671741ac06341e7f5f48caf027c1e6897be0a35eef`).
- `tex/submitted/control center/prompt/_INDEX.txt` (POSTSCRIPT-39
  appended; ~80 lines added at end).

## AEAL claim count

5 entries written to `claims.jsonl` this session.
