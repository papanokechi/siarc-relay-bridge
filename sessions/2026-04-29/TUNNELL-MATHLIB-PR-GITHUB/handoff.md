# Handoff — TUNNELL-MATHLIB-PR-GITHUB
**Date:** 2026-04-29
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~5 minutes
**Status:** HALTED

## What was accomplished
Halted at Step 1 (precondition check) because the `gh` CLI is not installed on this machine. No fork, no branch, no upload, no PR was attempted — per the relay prompt's explicit HALT rule for missing tooling.

## Halt details
- Step reached: 1 (CHECK fork existence)
- Failing command: `gh --version`
- Error: `gh: The term 'gh' is not recognized as the name of a cmdlet, function, script file, or operable program.`
- Cross-checked: `Get-Command gh`, `where.exe gh`, and direct probe of `C:\Program Files\GitHub CLI\gh.exe` — all negative.

## Remediation (one of the following)

### Option A — install gh and re-run this relay
```powershell
winget install GitHub.cli
# or
choco install gh
# then in a new terminal:
gh auth login
```
After install + auth, re-issue the same relay prompt; all subsequent steps will execute as scripted.

### Option B — open the PR manually (fully prepared)
All artifacts are ready. The user (papanokechi) only needs to perform the click-through steps below; nothing else is required from this agent.

1. **Fork** <https://github.com/leanprover-community/mathlib4> via the GitHub web UI ("Fork" button, default settings).

2. **Clone the fork and create the branch** locally:
   ```bash
   git clone https://github.com/papanokechi/mathlib4.git
   cd mathlib4
   git checkout -b feat/finset-card-even-of-involution
   ```

3. **Drop in the file**:
   - Source: `congruent-relay/mathlib-pr/CardEvenOfInvolution.lean` (verified to compile, 126 lines).
   - Target path inside Mathlib4 fork:
     `Mathlib/Data/Finset/CardEvenOfInvolution.lean`
   - Also append to `Mathlib.lean` the line:
     ```
     import Mathlib.Data.Finset.CardEvenOfInvolution
     ```
     (placed alphabetically among the other `Mathlib.Data.Finset.*` imports).

4. **Verify build locally** (recommended before PR):
   ```bash
   lake exe cache get
   lake build Mathlib.Data.Finset.CardEvenOfInvolution
   lake exe runLinter Mathlib.Data.Finset.CardEvenOfInvolution
   ```

5. **Commit + push**:
   ```bash
   git add Mathlib/Data/Finset/CardEvenOfInvolution.lean Mathlib.lean
   git commit -m "feat(Finset/Card): card_even_of_involution"
   git push -u origin feat/finset-card-even-of-involution
   ```

6. **Open PR** at
   <https://github.com/leanprover-community/mathlib4/compare/master...papanokechi:mathlib4:feat/finset-card-even-of-involution>
   - Title: `feat(Finset/Card): card_even_of_involution`
   - Body: copy-paste verbatim from
     `siarc-relay-bridge/sessions/2026-04-29/TUNNELL-MATHLIB-PR-OPEN/pr_description.md`

7. **Record PR number/URL** and re-run the relay (or paste it back here) so it can be threaded into `tunnell_cpp_R1.tex`.

## What succeeded
Nothing — halted at Step 1.

## What failed
Step 1: `gh --version` returned `CommandNotFoundException`.

## Anomalies and open questions
- Confirm whether `winget` / `choco` / direct download is preferred for installing the CLI.
- Confirm whether the PR should target `master` (current Mathlib4 default) or `main`. Current Mathlib4 default branch is `master` as of this writing.
- Confirm fork visibility (public is required for PR; default for GitHub forks).

## What would have been asked (if bidirectional)
- "Should I attempt the PR via raw `git` + the GitHub REST API using the `GH_TOKEN` environment variable instead of `gh`? That would require an existing PAT with `repo` scope on the machine."

## Recommended next step
Install `gh` and re-run `TUNNELL-MATHLIB-PR-GITHUB`, OR follow Option B above for a fully manual PR.

## Files committed (this session)
- `handoff.md` (this file)
- `claims.jsonl`
- `halt_log.json`
- `discrepancy_log.json` (empty)
- `unexpected_finds.json` (empty)

## AEAL claim count
1 entry written to `claims.jsonl` this session (halt-state).
