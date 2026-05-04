================================================================
SIARC RESEARCHER PROMPT 026 — CT-V14-SEC35-AMENDMENT-PATCH-PRECHECK
================================================================
TASK ID:        CT-V14-SEC35-AMENDMENT-PATCH-PRECHECK
COMPOSED:       2026-05-04 ~13:35 JST
DRAFTED-BY:     Copilot CLI (Claude Opus 4.7 xhigh)
AGENT:          Copilot researcher (workspace TeX readback;
                surgical-diff drafting; LaTeX hygiene check;
                NO commit / NO modification of CT v1.4 source).
GATES:          NEW PROMPT (NOT YET QUEUED). Direct follow-on
                to G17-LAYER-SEPARATION-LIT-ANCHOR verdict
                `UPGRADE_G17_LIT_ANCHOR_FOUND_AMENDMENT_
                RECOMMENDED` 2026-05-04 (bridge `b08cc4f`);
                prepares a clean diff / patch artifact for
                CT v1.4 §3.5 in-flight narrative-draft —
                operator + synthesizer review BEFORE manual
                commit. Does NOT auto-amend.
PRIOR ANCHORS:  G17-LAYER-SEPARATION-LIT-ANCHOR handoff
                (DRAFT amendment language in Phase C.3);
                v1.17 picture §5 G17 row (amendment recommended).
COMPUTE BUDGET: ~1-2 hr researcher (workspace TeX file
                identification + §3.5 boundary extraction +
                diff drafting + LaTeX-render dry-check).
RUNTIME PROFILE:Workspace TeX file readback (no compile);
                pypdf cross-check on existing CT v1.3 §3.5
                from prior Zenodo deposit; surgical-diff
                drafting in markdown / .patch artifact form.
                Per Rule 2: operator commits manually after
                review.

================================================================
§0 GOAL
================================================================

The G17-LAYER-SEPARATION-LIT-ANCHOR verdict 2026-05-04
recommended an explicit amendment to CT v1.4 §3.5 with DRAFT
language captured in the handoff Phase C.3:
  "The L-equation [cite Wasow / B-T / Costin] is the linear
  ODE satisfied by the formal-series wave function / OGF; it
  lives in the (z, w) function-space layer. The isomonodromic
  deformation [cite Okamoto / Barhoumi-Lisovyy / Sakai]
  describes how this L-equation's monodromy data deform as a
  parameter t varies; it lives in the (q, p, t) Hamiltonian /
  monodromy-data layer..."

This task DOES NOT amend CT v1.4 directly. It prepares a
precheck artifact:
  (a) Locates the CT v1.4 in-flight TeX source in
      `tex/submitted/`
  (b) Extracts the existing §3.5 boundaries (start line + end
      line) verbatim
  (c) Maps the 023 DRAFT language to a clean `.patch` /
      `.diff` artifact with explicit insert / replace
      instructions
  (d) Performs LaTeX-syntax dry-check on the proposed
      amendment (no compile; just bracket-balance + cite-key
      validity + hygiene-verb scan)
  (e) Prepares a side-by-side comparison artifact (current
      §3.5 verbatim ↔ proposed §3.5 verbatim) for operator
      + synthesizer review
  (f) Outputs ALL of the above to bridge as deliverables;
      operator manually applies the patch after Claude / human
      review

Closes G17 amendment-decision territory via reviewable diff
artifact. Does NOT close G17 unilaterally — operator + Claude
review gate.

[Full prompt body verbatim above — abridged here for brevity;
the controlling spec is the relay prompt that opened this
session (Phases A–E, AEAL ≥ 5, halt conditions per §4,
out-of-scope per §6, B1–B5 standing final step per §H).]
