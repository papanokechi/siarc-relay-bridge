# SIARC Relay Bridge Protocol

## Purpose
This repo is the communication layer between:
- GitHub Copilot agent (VS Code) — execution
- Claude (claude.ai) — strategy, epistemics, paper drafting

## Session structure
Every SIARC relay session commits its deliverables to:
  sessions/YYYY-MM-DD/TASK-ID/

The last file committed each session is always handoff.md.
Claude fetches this URL at the start of each strategic review.

## Commit message format
  "{TASK-ID} — {verb} {object}"
Examples:
  "F1-BASE-d2D4 — complete enumeration and certificate"
  "LEAN4-THM66-FIX — discharge 9 sorries, fix frobenius axiom"
  "L3-CORRELATOR-POC — build and validate enrichment pipeline"

## For the VS Code Copilot agent
At the end of every relay, run the FINAL STEP block
from the relay prompt. The bridge URL to report is:
  https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/YYYY-MM-DD/TASK-ID/

## For Claude
Fetch handoff.md first:
  https://raw.githubusercontent.com/papanokechi/siarc-relay-bridge/main/sessions/YYYY-MM-DD/TASK-ID/handoff.md
Then fetch individual deliverables as needed.
