# Stage 0 — Prerequisite check (governance gate)

**Chain:** VQUAD-REPRO-BUNDLE-001 · **Date:** 2026-06-16 · **Repo HEAD:** `f3dd3a4`

The task lists four prerequisites. Verified state:

| # | Prerequisite | State | Evidence |
|---|---|---|---|
| 1 | `VQUAD-PAPER-CORRECTIONS-001` complete (paper final) | ❌ **NOT MET** | Slot does not exist under `sessions/2026-06-15/` or `2026-06-16/`; HEAD is `f3dd3a4` = the paper-draft commit; no corrections cycle has run |
| 2 | Cold-read verdict A or B-resolved | ❌ **NOT MET** | `VQUAD-REVIEW-PREP-001` contains only the cold-read **framework** (`cold-read-checklist.md`, `open-items-decisions.md`); no verdict file. The cold-read was explicitly deferred to the operator |
| 3 | Fresán inquiry incorporated or confirmed-pending | ✅ **MET (pending)** | `FRESAN-JOSSEN-INQUIRY-001` drafted + staged HELD, awaiting operator send — i.e. *confirmed-pending* |
| 4 | All corrections applied, paper compiled clean | ⚠️ **PARTIAL** | Paper compiles clean and is byte-reproducible (PDF 698 730 bytes, 23 pp, SHA-256 `359D1172AF3F867F4349CF4776A222813A855CD354BC78C0B68CCFB0026C702B`), but "corrections applied" is moot since the corrections cycle (#1) has not run |

## Disposition (autopilot, governance-consistent)

The only paper that exists is the **current byte-reproducible draft**. Per the standing
meta-rule (prepare to ready-state and HOLD for the operator; never deposit/commit
autonomously), I proceed as follows:

1. **Assemble the bundle against the current paper draft** — all of Stages 1–6 are valid
   regardless of minor paper-text corrections (scripts, data, conventions, provenance,
   dependencies, structure are text-stable).
2. **Build to ready-state, HELD** — no Zenodo deposit, no autonomous commit; the slot is
   git-add staged and held for operator review.
3. **Gate the final "ready for deposit" claim** on the two unmet prerequisites. The closing
   status reflects this honestly: the bundle is *assembled and integrity-verified*, but the
   paper is *not certified final* until the cold-read verdict + `VQUAD-PAPER-CORRECTIONS-001`
   land.

## What the operator must do before deposit

1. Conduct the cold-read (`VQUAD-REVIEW-PREP-001/cold-read-checklist.md`); record verdict.
2. If corrections are needed, open `VQUAD-PAPER-CORRECTIONS-001`, apply them, recompile.
3. **If the paper text changes**, refresh `vquad-periodrep-bundle/paper/` (PDF + .tex) and
   re-run `bundle-integrity-verification.md` Stage 5.3 to update the PDF SHA-256.
4. If the paper text does **not** change (cold-read verdict A, no corrections), this bundle is
   deposit-ready as-is.
5. Decide whether to wait for the Fresán reply (may strengthen §6) or deposit with the current
   conditional §6 (Scenario B/D/E of `FRESAN-JOSSEN-INQUIRY-001/response-scenarios.md`).

**Bundle assembly proceeds under this explicitly-flagged assumption.**
