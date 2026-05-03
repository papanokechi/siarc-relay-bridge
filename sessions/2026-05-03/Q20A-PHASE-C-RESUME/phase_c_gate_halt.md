# Phase C.0 Gate — Q20A-PHASE-C-RESUME

**Verdict signal:** `HALT_Q20A_LITERATURE_NOT_LANDED`

## Gate description

Per Q20A prompt §1 ("Anchor files"), Phase C requires two
literature PDFs at well-defined paths:

1. **Wasow 1965, Asymptotic Expansions for Ordinary Differential
   Equations, §X.3** — characteristic-root-from-Newton-polygon
   theorem at irregular singular points. Expected location
   per the G3b acquisition runbook
   (`tex/submitted/control center/g3b_literature_acquisition_runbook_20260503.md`):
   `literature/g3b_2026-05-03/wasow_1965_chap_X.pdf`.

2. **Birkhoff 1930, Formal theory of irregular linear
   difference equations, Acta Mathematica 54, §§2–3** —
   formal-series structure for irregular linear difference
   equations at slope-1/d. Expected location:
   `literature/g3b_2026-05-03/birkhoff_1930.pdf`.

Per Q20A prompt §1:

> GATE: if either (10) or (11) is missing at Phase C start,
> halt with HALT_Q20A_LITERATURE_NOT_LANDED and produce no Phase
> C output.

## Gate-check observation (this session)

```
literature/g3b_2026-05-03/                 (DOES NOT EXIST)
tex/submitted/control center/literature/   (DOES NOT EXIST)
siarc-relay-bridge/literature/             (DOES NOT EXIST)
pcf-research/literature/                   (DOES NOT EXIST)
```

A repository-wide `**/*wasow*` glob returns no matches; a
repository-wide `**/*birkhoff*` glob matches only existing
SIARC scripts named after the **Birkhoff recursion** (e.g.
`newton_birkhoff.py`) and the prompt-queue file
`003_t1_birkhoff_trjitzinsky_litreview.txt` — never a Wasow
or Birkhoff 1930 *primary-source* PDF.

## Why this is expected

The G3b literature acquisition runbook was committed to
`tex/submitted/control center/` earlier the same day
(2026-05-03), with operator-side browser-download instructions
(Internet Archive / Project Euclid) totalling 30–60 minutes
of manual work. The Q20A relay was fired immediately after the
runbook landed, before the operator had completed the
acquisition cycle.

## Halt scope

- **Phase C.1** (Wasow §X.3 reading) — NOT EXECUTED
- **Phase C.2** (Birkhoff 1930 §§2–3 reading) — NOT EXECUTED
- **Phase C.3** (literature aggregation) — NOT EXECUTED
- **Phase D** (verdict aggregation) — emits the deferred-verdict
  signal `UPGRADE_DEFERRED_PENDING_LITERATURE_LANDING`,
  consistent with Q20's already-recorded
  `UPGRADE_PARTIAL_PENDING_LITERATURE` verdict
- **Phase E** (D2-NOTE v2 draft) — NOT EXECUTED

Phase A* (literature-independent re-validation of Q20's
symbolic derivation at extended d-range {2..10}) was executed
prior to this gate and produced verdict signal
`A_DIRECT_IDENTITY_d10` (`phase_a_star_summary.md`). This is
useful pre-work for the resumption session: when the operator
places the two PDFs, only Phases C, D, and (if applicable) E
need to be re-run.

## Resumption procedure (operator-side)

1. Execute the G3b runbook
   (`tex/submitted/control center/g3b_literature_acquisition_runbook_20260503.md`)
   for the two Q20A-required sources (Wasow + Birkhoff 1930).
2. Place the two PDFs at `literature/g3b_2026-05-03/`.
3. Run the runbook's hashing script and confirm the Wasow +
   Birkhoff 1930 SHA-256s appear in
   `literature/g3b_2026-05-03/HASHES.txt`.
4. Re-fire the Q20A-PHASE-C-RESUME prompt. Phase A* will
   re-execute (≈ 15 s) and confirm the Q20 anchor script hash
   is unchanged; Phases C/D/(E) will then run on the present
   PDFs.

There is no soft-fallback path: per the Q20A prompt, paraphrase
or secondary-source readings cannot substitute for primary
literature. Q20 already established this in its own Phase C
halt (`HALT_Q20_LITERATURE_MISSING`, verdict
`UPGRADE_PARTIAL_PENDING_LITERATURE`).
