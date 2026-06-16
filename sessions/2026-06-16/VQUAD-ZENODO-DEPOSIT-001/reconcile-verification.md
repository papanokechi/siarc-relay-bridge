# Reconcile verification — VQUAD-ZENODO-DEPOSIT-001 (Stage 3)

HALT-GATE evidence: no stale pin survives in the 7 deposit files, and the reconciled
MANUAL-UPLOAD.md agrees exactly with READY-001 run-3's deposit-ready pin set.

## 3.1 — Zero stale pins survive (the 7 deposit files)

Re-grep of `MANUAL-UPLOAD.md, gate0-authorization.md, operator-runbook.md, ledger.json,
handoff.md, claims.jsonl, README.md` for every pre-layout-fix pin literal:

| stale literal | kind | occurrences |
|---|---|---|
| `4ca12a35` | PDF SHA | **0** |
| `028a1a5d` | PDF MD5 | **0** |
| `714771` / `714,771` | PDF size | **0** |
| `8752d7c7` | bundle SHA | **0** |
| `9d811494` | bundle MD5 | **0** |
| `721715` / `721,715` | bundle size | **0** |
| `…\REPRO-BUNDLE-002\vquad…` (slot-root path) | upload path | **0** |
| `…\READY-001\run-2\…` (metadata path) | metadata path | **0** |

**Total stale PDF/bundle pin literals: 0.**

Note — three git-commit short-hashes remain *by design* as supersession provenance in
`ledger.json` prerequisites: `"supersedes run-2 2a7f969"`, `"supersedes a33ff59"`,
`"supersedes CORRECTIONS-001 d4fc87a"`. These are the brief's requested "note the
supersession of the stale pins"; they are git commits, clearly labelled superseded, not
PDF/bundle pin values an operator could mistake for an upload target.

## 3.2 — New values present where expected

| value | kind | count in 7 files |
|---|---|---|
| `33f339ed…` | PDF SHA | 18 |
| `99faea5b…` | PDF MD5 | 7 |
| `773171` / `773,171` | PDF size | 2 / 1 |
| `7bc5d008…` | bundle SHA | 14 |
| `c1b5a39c…` | bundle MD5 | 5 |
| `776968` / `776,968` | bundle size | 2 / 1 |
| `…\REPRO-BUNDLE-002\run-2\vquad…` | upload path | 4 (MANUAL-UPLOAD ×2, runbook ×2) |

On-disk confirmation (Get-FileHash, this task):
- `…\VQUAD-REPRO-BUNDLE-002\run-2\vquad-periodrep-bundle\paper\vquad-periodrep-paper.pdf`
  → SHA-256 `33f339ed…3eea`, MD5 `99faea5b…eeda`, 773171 B. **MATCH.**
- `…\VQUAD-REPRO-BUNDLE-002\run-2\vquad-periodrep-bundle.zip`
  → SHA-256 `7bc5d008…e013`, MD5 `c1b5a39c…669f`, 776968 B. **MATCH.**
- (Control) the *slot-root* PDF still hashes to `4ca12a35…` — confirming the path repoint
  was necessary; without it the operator would have uploaded the clipped-digit PDF.

## 3.3 — MANUAL-UPLOAD.md ≡ READY-001 run-3 pin set

Source of truth: `…\VQUAD-ZENODO-READY-001\run-3\run3-stage7-runner-pins.md` +
`run-3/zenodo_metadata.md`.

| pin | run-3 | MANUAL-UPLOAD.md | agree |
|---|---|---|---|
| PDF SHA-256 | `33f339ed…3eea` | `33f339ed…3eea` | ✓ |
| PDF MD5 | `99faea5b…` | `99faea5b…` | ✓ |
| bundle SHA-256 | `7bc5d008…e013` | `7bc5d008…e013` | ✓ |
| bundle MD5 | `c1b5a39c…` | `c1b5a39c…` | ✓ |
| metadata anchor | `4a75234f…` | via run-3 `zenodo_metadata.md` (SHA-256 == `4a75234f…`, re-hashed) | ✓ |
| related-ids | 11 (2+1+8+0) | 11-row table, concept `20455089`, no version `20455090` | ✓ |

run-3 `zenodo_metadata.md` re-hashed this task → `4a75234faaef79d68caed6588d0fa0e2418ae17dfb2c18825a150b92f7970895` (anchor MATCH).

## 3.4 — Invariants unchanged

- metadata anchor `4a75234f…` present (×10); concept DOI `20455089` present (×5).
- retracted version DOI `20455090`: appears **only** as the "do not enter / absent"
  caution (MANUAL-UPLOAD.md §3/§5) and the runner BLOCKLIST (operator-runbook, ledger,
  claims) — never as an active related-identifier.
- related-ids table: 11 rows, untouched.
- abstract, keywords (8), MSC 2020, affiliation "Independent Researcher, Yokohama, Japan",
  page count 24, CC-BY-4.0: not edited.
- `ledger.json` and `claims.jsonl` parse (Python `json` — ledger OK; claims 9 lines OK).

## Determination

**PASS — no stale pin survives; MANUAL-UPLOAD.md is exactly consistent with READY-001
run-3.** The slot is reconciled and upload-ready. Execution (token, runner `--execute`,
publish) remains the operator's hand-step — the slot is still **HELD** at Gate 0.
