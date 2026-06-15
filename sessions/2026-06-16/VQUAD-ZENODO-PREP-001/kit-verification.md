# Kit verification — VQUAD-ZENODO-PREP-001 (Stage 1)

**Date:** 2026-06-16 · **Verdict: KIT PRESENT — no critical tooling missing.**
No network calls; presence/inspection only. Kit is **not** duplicated into this
slot (verify-only, per the DO-NOT list).

## 1. Deposit-kit tooling (the Sakai deposit baseline)

Location: `C:\LocalWork\project-fingerprint\sectorial\cc_transcendence\sakai-stratification\`

| Component | Present | Bytes | Note |
|-----------|:---:|---|---|
| `run_sandbox_draft.py` | ✓ | 15254 | sandbox draft + Gate 0/1/2 |
| `run_production_draft.py` | ✓ | 16204 | production draft; reads `zenodo_metadata.md` + `related_identifiers.md`; SHA-256 anchor gate (L134–136) |
| `set_prod_token.ps1` | ✓ | 934 | operator hand-step (token export) |
| `set_token.ps1` | ✓ | 616 | sandbox token export |
| `check_prod_token.ps1` | ✓ | 2695 | scope/instance check (deposit:write) |
| `check_token.ps1` | ✓ | 2331 | sandbox token check |
| `zenodo_metadata.md` | ✓ | 6640 | **Sakai** metadata (model to copy from) |
| `related_identifiers.md` | ✓ | 14580 | **Sakai** wired array (authoritative corpus DOI table — see Stage 2) |
| `claims.jsonl`, `operator_handoff.md`, `premint_checklist.md`, `ledger_entry_spec.json`, `draft_ready.md`, `upload_manifest.md` | ✓ | — | Sakai deposit artifacts (models) |

## 2. Templates (blank, canonical)

Location: **`C:\LocalWork\project-fingerprint\zenodo\templates\`**
(NOT under `sakai-stratification/templates/` — that path the brief assumed does
**not** exist; corrected here.)

| Template | Present | Bytes |
|----------|:---:|---|
| `related_identifiers.template.md` | ✓ | 6045 |
| `zenodo_metadata.template.md` | ✓ | 4704 |
| `premint_checklist.template.md` | ✓ | 5294 |

## 3. Supporting tooling

| Component | Location | Present | Bytes |
|-----------|----------|:---:|---|
| `_zenodo_uploader.py` | `…\OneDrive\…\siarc\submitted\` | ✓ | 30738 |
| `zenodo_update_keywords.py` | `…\project-fingerprint\zenodo\` | ✓ | 6712 |
| `README_ZENODO_DEPOSIT.md` (the **playbook**) | `…\project-fingerprint\zenodo\` | ✓ | 12419 |
| `DEPOSIT_LOG_INDEX.md` (paper→concept-DOI map) | `…\project-fingerprint\zenodo\` | ✓ | 2080 |
| `submission_log.txt` (master ledger, §A/§B) | `…\OneDrive\…\siarc\submitted\` | ✓ | ~375 KB / 2073 lines |

## 4. Path corrections vs the task brief (noted, not blocking)

1. **Templates path.** Brief said `sakai-stratification/templates/…`; actual
   canonical templates are in `project-fingerprint/zenodo/templates/`. The
   `sakai-stratification/` folder ships the *filled* `related_identifiers.md` and
   `zenodo_metadata.md` (deposit instances), not blank templates.
2. **Playbook path.** Brief referenced "`sessions/.../sakai deposit/README.md`".
   No per-session Sakai-deposit README exists in the bridge; the procedural
   reference is `project-fingerprint/zenodo/README_ZENODO_DEPOSIT.md` (the
   canonical Zenodo deposit playbook, with the Trap 1–7 list).

## 5. Disposition

All critical tooling present and accessible. No HALT. The Sakai
`related_identifiers.md` is especially valuable: it is the most recent
authoritative concept-DOI resolution for this exact corpus (line-cited to
`submission_log.txt`) and is the source-of-truth used in Stage 2 below.
