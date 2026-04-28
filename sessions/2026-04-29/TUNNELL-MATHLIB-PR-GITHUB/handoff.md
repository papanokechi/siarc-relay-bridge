# Handoff — TUNNELL-MATHLIB-PR-GITHUB
**Date:** 2026-04-29
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~5 minutes
**Status:** HALTED

## What was accomplished
Halted at Step 1 (precondition check) because the `gh` CLI is not installed on this machine. No fork, no branch, no upload, no PR was attempted — per the relay prompt's explicit HALT rule for missing tooling.

## Halt details
- Step reached: 1 (CHECK fork existence)
- **Second attempt (2026-04-29, ~later):** user installed `gh` CLI (v2.91.0, on PATH). However `gh auth status` reports `You are not logged into any GitHub hosts`, and `%APPDATA%/GitHub CLI/hosts.yml` does not exist. User clicked "Done" twice in the auth prompt but verification failed each time — most likely the browser device flow was not actually completed, or it was completed under a different OS user / account context that does not write to `%APPDATA%`.
- **First attempt (earlier):** `gh: command not recognized`. Resolved by user installing the CLI; that part is no longer a blocker.
- Cross-checked: `gh --version` works, `gh config list` works, but `gh auth status` returns exit 1 and no hosts.yml exists.

## Remediation (one of the following)

### Option A — finish `gh auth login` properly and re-run the relay
```powershell
# in a fresh PowerShell terminal
gh auth login --hostname github.com --git-protocol https --web
# follow the device-code flow; complete the browser step.
gh auth status   # MUST report "Logged in to github.com account papanokechi"
```
Then re-issue the same relay prompt.

### Option B — set a Personal Access Token in env, then re-run the relay
```powershell
$env:GH_TOKEN = "<paste PAT with `repo` scope>"
gh auth status   # confirm
```
The token is process-scoped only, not written to disk.

### Option C — open the PR manually (fully prepared, no further agent action needed)
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
