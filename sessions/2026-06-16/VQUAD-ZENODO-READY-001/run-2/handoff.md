# Handoff — VQUAD-ZENODO-READY-001 · run-2 (RE-RUN; all stages PASS; HELD)

The first run (`c88b996`) correctly **halted at Stage 1** because the corrections
chain had not started. All prerequisites now exist and are committed, so this re-run
executed **Stages 1–8**: it refreshed the deposit pins against the corrections-final
paper, finalized the metadata per the resolved operator decisions, dropped the bundle
DOI placeholder (Scenario B), and pre-verified the deposit gates. **Ready-state HELD**
— nothing committed, no Zenodo API, no token.

This run lives in `run-2/`; the committed first-run halt artifact at the slot root is
**preserved untouched**.

## What changed since the first run

| input | first run | now |
|-------|-----------|-----|
| Cold-read | not done | **Verdict A** (`e207b33`) |
| Corrections paper | absent | **`d4fc87a`**, PDF `4ca12a35…`, 24pp |
| Bundle-002 | absent | **`a33ff59`**, archive `8752d7c7…` |
| F-AFFIL | undecided | **Option C** — "Independent Researcher, Yokohama, Japan" |
| §6 / Fresán | open | **deposit now**; reply → v2 enhancement |
| isSupplementTo | placeholder | **dropped** (Scenario B) |

## New pins (this run)

- **PDF SHA-256** `4ca12a35d655df2227a9e1740e60b39c2e6cabef6a1942c74307cd43849582fe`
  (MD5 `028a1a5d9e10a3a9487596f6db3e6a38`, 714771 B, 24pp) — supersedes `359d1172…`.
- **Metadata anchor SHA-256** `4a75234faaef79d68caed6588d0fa0e2418ae17dfb2c18825a150b92f7970895`
  — supersedes `dee9195c…`.

## Gates pre-verified

- **Gate 1 (related-ids):** PASS — 11 ids (2+1+8+0), no `{{…}}`, no BLOCKLIST leak,
  retracted `20455090` absent, concept `20455089` present, all `scheme=doi`.
- **Gate 2.2 (wrong-venue):** PASS — `Compositio`/`AAECC`/`ETNA` absent in the
  `4ca12a35…` PDF (63635 chars).

## What the operator does next (DEPOSIT-001)

Four hand-steps remain (none agent-doable):

1. `set_prod_token.ps1` — export production `ZENODO_TOKEN` in the deposit shell.
2. `check_prod_token.ps1` — confirm scope `deposit:write` (+ `deposit:actions`) and
   instance = production.
3. **Trap-7** — after staging the PDF in the deposit folder, re-hash; confirm `4ca12a35…`.
4. Paste the **`stage7-runner-pins.md`** constant block into the deposit copy of
   `run_production_draft.py` **and** `run_sandbox_draft.py`.

Then: dry-run → sandbox `--execute` → production `--execute` → **STOP at the publish
gate** → review → **publish by hand**. Deposit = the `4ca12a35…` PDF **+** the
BUNDLE-002 zip (`8752d7c7…`) as **one** CC-BY-4.0 record (Scenario B). After the
bucket upload, confirm Zenodo's returned checksum equals MD5 `028a1a5d…`. Post-publish:
append §B + DEPOSIT_LOG_INDEX, send Marchal the live concept DOI.

## Operator note — commit message

The re-run's success commit message is now **true** (Stages 1–8 ran; pins refreshed;
gates pre-verified). Honest HELD message:

> `VQUAD-ZENODO-READY-001 (run-2) — pre-flight re-run; pins refreshed to corrections-final (PDF 4ca12a35…, anchor 4a75234f…); Scenario B (isSupplementTo dropped, 11 ids); Gate 1 + wrong-venue PASS; HELD for operator hand-commit + DEPOSIT-001`

(with the `Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>`
trailer). The first-run halt commit `c88b996` stays as the first-attempt record.

## Standing-rule status

`run-2/` staged only. **No commit, no push, no deposit, no API, no token.** HEAD
unchanged at `a33ff59`. First-run artifacts (`ledger.json`, `handoff.md`,
`claims.jsonl`, `stage1-prerequisite-verification.md` at the slot root) untouched.
`EBR3-REVISION-001` left untracked. All parent slots pristine.
