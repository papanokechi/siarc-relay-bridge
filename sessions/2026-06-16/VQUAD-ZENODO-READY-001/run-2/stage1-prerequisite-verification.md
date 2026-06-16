# Stage 1 — Prerequisite verification → PASS (re-run / run-2)

**Slot:** VQUAD-ZENODO-READY-001 · **run-2** · 2026-06-16 · **HELD** (no commit/API)

The first run (committed `c88b996`) correctly **halted at Stage 1** because the
corrections chain had not started. All four prerequisites are now satisfied, so the
pre-flight proceeds through Stages 2–8.

| # | Prerequisite | Status | Evidence |
|---|---|---|---|
| 1 | **Cold-read complete (Verdict A)** | ✅ DONE | `VQUAD-COLDREAD-001` committed **`e207b33`** — Verdict A; 1 HIGH + 4 MED + 5 LOW corrections list. |
| 2 | **VQUAD-PAPER-CORRECTIONS-001 complete** | ✅ DONE | committed **`d4fc87a`** — corrections-final paper; PDF SHA-256 `4ca12a35…`, 24 pp, byte-reproducible; H-1 provenance remark operator-verified; retracted v1.0 DOI purged. |
| 3 | **VQUAD-REPRO-BUNDLE-002 generated + verified** | ✅ DONE | committed **`a33ff59`** — deposit-target bundle; archive SHA-256 `8752d7c7…`; integrity PASS (13 scripts); retracted DOI confirmed absent. |
| 4 | **VQUAD-ZENODO-PREP-001 complete** | ✅ DONE | committed `941a699` — deposit kit (metadata, related-identifiers, runbook, checklist). |

**Result: 4 of 4 prerequisites met → PROCEED.**

Operator decisions resolved (per the re-run brief, 2026-06-16):
- **F-AFFIL → Option C**: affiliation "Independent Researcher, Yokohama, Japan".
- **Fresán / §6 → deposit now** with §6 as drafted (doubly-conditional
  G-MOTGALOIS heuristic); a substantive Fresán reply, if it arrives, is a Zenodo
  **v2 enhancement**, not a held gate.
- **Scenario B → confirmed**: bundle is a secondary file in the paper's single
  deposit; the `isSupplementTo` placeholder is **dropped** (no separate bundle DOI).

The committed first-run halt artifact (`c88b996`: `ledger.json`, `handoff.md`,
`claims.jsonl`, `stage1-prerequisite-verification.md` at the slot root) is preserved
as the first-attempt record; this successful run lives alongside it in `run-2/`.
