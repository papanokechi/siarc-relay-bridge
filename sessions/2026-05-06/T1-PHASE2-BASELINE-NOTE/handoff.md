# Handoff — T1-PHASE2-BASELINE-NOTE

**Date:** 2026-05-06
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~70 minutes
**Status:** COMPLETE

## What was accomplished

Drafted an 8-page Zenodo-ready standalone note titled "A
Newton-polygon formal-level baseline for the Birkhoff-Trjitzinsky
exponent on the SIARC polynomial continued-fraction Wallis
stratum" (`bt_baseline_note.pdf`, SHA-256
`23022f0de77ac8388ed584b2196c0ab995cd8cf18b2dd71efbc0488a0f6e5b7c`).
The note crystallizes the T1 Phase 2 verdict
`UPGRADE_PARTIAL_FORMAL_LEVEL` (bridge commit `37c939f`,
2026-05-04) into a single citable artefact with strict triple
framing PROVEN (formal level) | VERIFIED (literature-citation) |
STRUCTURAL FRAMING (not closure) | CONJECTURED (B4) intact in
every section. Theorem 1.1 establishes
$\Anaive \in \{d-1, d, d+1\}$ uniformly across $d \in [2, 8]$ and
the three SIARC conventions; Proposition 1.2 frames the gap to
the empirical $A_{\rm fit} \approx 2d$ at $d \geq 3$ via two
non-mutually-exclusive structural mechanisms, both deferred to
Phase 3. Bibliography (15 entries) is a tightly scoped subset of
the bridge's `bibliography_pass1.bib`. Build is clean: 8 pages
exactly, 0 unresolved citations, 0 undefined references; BibTeX
0 warnings.

## Key numerical findings

- **Theorem 1.1** (formal-level, PROVEN): For the SIARC PCF
  Wallis recurrence at degree $d \in [2, 8]$ in any of the three
  SIARC conventions (alpha-direction, symmetric, delta-direction),
  the naive Wimp-Zeilberger Newton-polygon balance yields
  $\mu_{\rm dom} = d$, $\mu_{\rm sub} = \deg a - d$, and the
  formal exponent $\Anaive = 2d - \deg a \in \{d-1, d, d+1\}$.
  Symbolic, dps = symbolic; bridge script
  `phase_a_symbolic_derivation.py`
  (SHA-256 `2fc6e39267768791912cc53aa59bc231c40483a1a93e92104b13f07809f16248`)
  + `phase_b_extended_sweep.py`
  (SHA-256 `39e98db607a5331686cf4ba4890bc50abc1232e8b533b80eeb2d4636c8e10175`).

- **§3.2 d=2 verification** (VERIFIED, literature-citation): At
  $d = 2$ alpha-direction the formal $\Anaive = 3$ matches PCF-1
  v1.3 §6 Theorem 5 LOWER branch (V_quad family QL01-QL26) at 80
  algebraic digits; PDF SHA-256
  `63420dbf4abb7124672f522c37fc04ebdb3f6694ac39959456b2890d9788ff5e`
  (DOI 10.5281/zenodo.19937196).

- **Proposition 1.2 gap** (STRUCTURAL FRAMING, not closure): At
  $d = 3, 4$ the empirical $A_{\rm fit} \approx 2d$
  (50/50 cubic + 60/60 quartic, $\sigma \in [10^{-2}, 4 \times 10^{-3}]$)
  lies strictly outside the formal baseline $\{d-1, d, d+1\}$.
  Two structural mechanisms framed: (i') borderline-locus
  condition $\deg a = 2 \deg b$ on a sub-stratum, (ii')
  alternative definition of $A_{\rm fit}$ in the [PCF-2 v1.3]
  fit-protocol. Distinguishing them is open in §6 Q1.

- **Conjecture B4** (CONJECTURED, [PCF-2 v1.3] R1.1+R1.3+Q1):
  $A = 2d$ for representatives in the SIARC stratum at each
  $d \geq 2$. The note does not claim to prove, partially prove,
  or refute Conjecture B4. PCF-2 v1.3 PDF SHA-256
  `87b845a8e382f3c124906ace0c1a6763ce54bd14c5f9593bbadc77bdd81d263f`
  (DOI 10.5281/zenodo.19963298).

## Judgment calls made

1. **Page count = 8 (lower edge of [8, 12]).** The Phase B sweep
   table at $d \in [5, 8]$ is cited but not reproduced in the
   note (the data is mechanically the same as the $d \in [2, 4]$
   table reproduced in §2.3 / §3.1). Reproducing the full sweep
   would add ~0.5 pp of repetitive tabular content. Decision:
   keep as a citation; the symbolic argument is general in $d$.
   Page count of 8 is admissible (HALT condition is `< 8 OR > 12`).

2. **Pre-commit forbidden-verb softenings on Proposition 1.2.**
   Three edits applied to use permitted verbs out of an
   abundance of caution, even though Prop 1.2 is a mathematical
   proposition with a legitimate proof-style argument:
   - "[Prop 1.2] is proven in [§4]" → "is supported in [§4]"
   - "The proof of [Prop 1.2] consists of..." → "The argument
     supporting [Prop 1.2] consists of..."
   - "to confirm or reject [the $A_{\rm fit}$ identification]"
     → "to support or rule out [...]"
   Theorem 1.1 (formal-level) retains "proven"/"establishes"
   verbatim — these are PERMITTED for the formal-level theorem
   strictly scoped to $\Anaive$. See `rubber_duck_critique.md`
   §"Forbidden-verb hygiene scan summary" for the full audit.

3. **AI Disclosure long-form.** Used the v1.3-cycle
   long-form AI-disclosure verbatim (matching PCF-1/PCF-2 v1.3,
   CT v1.3, D2-NOTE v2.1) rather than the short-form template
   in the relay 051 spec. Both forms are present: the title-page
   `\thanks{}` long-form and the dedicated AI-Disclosure section
   short-form. This is intentional and matches the existing
   v1.3-cycle house-style.

4. **Bibliography size = 15 (spec target was 12).** Three
   additional entries were judged necessary: Adams 1928,
   Turrittin 1955, Costin 2008 — all explicitly referenced as
   sectorial-upgrade-gap literature in §6 Q4. Removing them
   would make the §6 Q4 paragraph float without anchors.

## Anomalies and open questions

**This is the most important section. Three structural
anomalies are recorded for downstream review.**

1. **The d ≥ 3 gap A_naive < 2d (open question Q1).** The note
   does NOT close the gap between the formal-level baseline
   $\Anaive \in \{d-1, d, d+1\}$ and the empirical $A_{\rm fit}
   \approx 2d$ at $d \geq 3$. Proposition 1.2 frames the gap
   with two non-mutually-exclusive mechanisms — (i') borderline-
   locus condition $\deg a = 2 \deg b$, (ii') alternative
   definition of $A_{\rm fit}$ — but does not derive either. The
   bridge Phase 2 verdict was explicit that the lift to $A = 2d$
   requires both (i')/(ii') closure AND a sectorial upgrade
   (Q4). This note is the formal-level baseline only; closure of
   the gap is the open content of T1 Phase 3.
   **Downstream reviewer (Claude) should not treat the note as
   making any claim about $A = 2d$ at $d \geq 3$.**

2. **The formal-to-analytic sectorial upgrade gap (open
   question Q4).** Birkhoff-Trjitzinsky 1933 §§7–9 produces
   formal series; the connection to the analytic (true)
   asymptotic exponent on the SIARC stratum requires a sectorial
   summability theorem. The candidate theorems are Wasow §X.3
   Theorem 11.1 (image-only on disk per the bridge A-01
   verdict), Adams 1928 (NIA per A-01), Turrittin 1955, Immink
   1984, Costin 2008. None has been verified to apply to the
   SIARC stratum; Wasow §X.3 is the closest match and is the
   target of T1 Phase 3 / Phase 4. **This is the second of the
   two gaps that any future "$A = 2d$ proven on SIARC stratum"
   result must close.**

3. **The borderline-case algebraic ansatz gap (open
   question Q2).** The Wimp-Zeilberger normal-case analysis
   yields the formal exponent $A_{\rm naive}$ with a half-integer
   $1/q = 1/2$ Newton-polygon slope. On a $\deg a = 2 \deg b$
   borderline locus the slope $1/q$ becomes fractional with
   $q > 2$; the closed-form exponent $B = \sqrt{c_a}$ is
   conjectured by analogy with the [Wimp84 §5] / [BT33 §10]
   borderline analysis but is not derived. If the SIARC stratum
   really does sit on such a borderline locus (mechanism (i')),
   the explicit identification of $c_a$ in terms of the SIARC
   coefficients $(a, b)$ is a target of T1 Phase 3.

## What would have been asked (if bidirectional)

- Whether the operator wishes to extend the note to a v1.1 with
  the explicit Phase B sweep table at $d \in [5, 8]$ (resolves
  judgment call 1 + addresses rubber-duck critique item 2).
- Whether the secondary-indicial step in §2.2 should be added
  (rubber-duck critique item 1).
- Whether the v3.1 [T2B] PDF (post-2026-05-04) is on disk
  somewhere in the workspace; the v3.0 SHA-256 was used in the
  bibliography note (`7ac8f204…`). This affects only the
  cross-cite metadata; no load-bearing claim depends on the
  v3.1 vs v3.0 distinction.
- Whether the Zenodo deposit should wait for the T1 Phase 3
  closure (in which case the note would be deposited as
  "v1.0 baseline" first, then a "v2.0 closure" once Phase 3
  delivers — see umbrella-cycle convention) or whether the
  deposit should bundle Phase 2 + Phase 3 into a single record.

## Recommended next step

T1 Phase 3 — borderline-locus discrimination. Concrete deliverable:
(a) decide whether the SIARC stratum admits a sub-locus
$\deg a = 2 \deg b$ at the cubic / quartic level (q1 mechanism
identification); if yes, derive the borderline-case algebraic
ansatz and the closed-form $B = \sqrt{c_a}$. (b) Independently,
audit the [PCF-2 v1.3] $A_{\rm fit}$ definition in detail to
support or rule out the (ii') definitional translation. The
"yes-yes" outcome (both (i') and (ii') hold partially) is also
admissible. Either single-mechanism closure, jointly with the
sectorial upgrade of Q4 (Wasow §X.3 / Adams / Turrittin /
Immink / Costin), would lift the formal-level baseline to a
proof of $A = 2d$ on the SIARC stratum.

A possible Phase 2 follow-up is a v1.1 of this note that
extends the §3.1 case analysis with an explicit $d \in [5, 8]$
table and adds the secondary-indicial step in §2.2 (~0.5–1 pp
addition; resolves rubber-duck items 1 and 2 in the same pass).

## Files committed

- `bt_baseline_note.tex` — LaTeX source (8 pp, ~720 lines)
  SHA-256 `6746692c517dc25238473e819527c5682465cdc9e1def69d1f6df31c1014d51b`
- `bt_baseline_note.pdf` — primary artefact (8 pp, 409,337 B)
  SHA-256 `23022f0de77ac8388ed584b2196c0ab995cd8cf18b2dd71efbc0488a0f6e5b7c`
- `bt_baseline_note.log` — pdflatex log (final pass)
- `annotated_bibliography.bib` — bibliography (15 entries)
  SHA-256 `589f6e4a0b29de401229d60a6252de15436f355a2fa8b3ac04907779c2de923d`
- `claims.jsonl` — AEAL provenance log, 10 entries
- `verdict.md` — `T1_PHASE2_BASELINE_NOTE_DRAFTED`
- `halt_log.json` — empty `{}`
- `discrepancy_log.json` — empty `{}`
- `unexpected_finds.json` — empty `{}`
- `rubber_duck_critique.md` — pre-commit self-review
  SHA-256 `97765d9b5c303cf5b13c5a9e4e67323dc47c9e5256b2be4301d0d458fe11bfa3`
- `zenodo_description_bt_baseline_note.txt` — Zenodo description
  body (paste-ready, plain text)
- `zenodo_upload_bt_baseline_note_runbook.md` — Zenodo upload
  runbook (NEW concept DOI flow; 13 steps + 12-item pre-publish
  checklist)
- `handoff.md` — this file

## AEAL claim count

10 entries written to `claims.jsonl` this session (T1P2B-A1
through T1P2B-A10). Schema:

- T1P2B-A1, A2, A3, A4, A5, A6: literature-citation
  carry-forward from `T1-BIRKHOFF-PHASE2-LIFT-LOWER`
  (PA_DEG2/3/4_ALPHA_BASELINE, PB_SWEEP_D5_TO_D8,
  PC_GATES_C21_TO_C24, PD_VERDICT_UPGRADE_PARTIAL_FORMAL_LEVEL)
  with `upstream_script_sha256` / `upstream_artefact_sha256` /
  `upstream_output_sha256` cross-referencing the bridge
  session's claims.jsonl.
- T1P2B-A7: literature-citation anchor to PCF-1 v1.3 §6 Theorem 5
  lower branch (DOI 10.5281/zenodo.19937196; PDF SHA-256
  `63420dbf…`).
- T1P2B-A8: literature-citation anchor to PCF-2 v1.3 R1.1+R1.3+Q1
  empirical record (DOI 10.5281/zenodo.19963298; PDF SHA-256
  `87b845a8…`).
- T1P2B-A9: computation claim recording the three-pass pdflatex
  + bibtex build (page_count = 8, byte_count = 409,337,
  output_hash = `23022f0d…`).
- T1P2B-A10: reading claim recording the rubber-duck self-review
  + forbidden-verb hygiene scan (output_hash = `97765d9b…`).
