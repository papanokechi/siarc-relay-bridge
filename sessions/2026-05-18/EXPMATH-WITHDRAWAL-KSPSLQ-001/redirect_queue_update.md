# Redirect-queue update — Item 5 (KSPSLQ)

**Slot:** EXPMATH-WITHDRAWAL-KSPSLQ-001
**Date:** 2026-05-18 JST
**Anchor file:** `.copilot/session-state/d0b490af-727d-4ff2-b51d-fbe079b0a718/files/redirect_queue_triage_matrix_v1.md` (live v1.5+)

## Row 5 (Section C. ACTIVE-IN-FLIGHT) — before this slot

| # | Title (abbreviated) | Venue | Submission ID | Submitted | Days elapsed | Latest status | Watch trigger |
|---|---|---|---|---|---|---|---|
| 5 | Khinchin-Signature PSLQ Null Result | ExpMath | 264514392 | 18 Apr 2026 | 24 | With Journal Administrator (2026-05-12) | PULL at 30d 2026-05-25 per Q-202-8 LOCK; next venue (JSC/JTNB) pre-pull required |

## Row 5 — after this slot

| # | Title (abbreviated) | Venue | Submission ID | Submitted | Days elapsed | Latest status | Watch trigger |
|---|---|---|---|---|---|---|---|
| 5 | Khinchin-Signature PSLQ Null Result | ExpMath | 264514392 | 18 Apr 2026 | 30 | Returned for corrections (2026-05-17, Kaviya); operator-pulled — Exp Math withdrawal email drafted; awaiting confirmation before BAustMS submission. Duplicate-submission risk gate active. | Awaiting written withdrawal confirmation from Exp Math (or 10 business days + ScholarOne dashboard "Withdrawn" status, whichever comes first) before BAUSTMS-PREP-KSPSLQ-001 can fire |

## Notes for the anchor-file update

- The "Latest status" cell is the operative change for this slot.
- Days elapsed bumped from 24 (snapshot 2026-05-12) to 30 (2026-05-18 send window).
- Watch-trigger replaced: the old PULL-at-30d trigger is now superseded by the
  withdrawal-confirmation gate.
- Item 5 should **remain in Section C (ACTIVE-IN-FLIGHT)** until the
  withdrawal is confirmed, at which point it moves to Section B
  (redirect-queue closed via operator-withdraw) under the BAUSTMS-PREP-
  KSPSLQ-001 chain.

## Cross-references

- Parent decision chain: `VENUE-RELAY-KSPSLQ-001` (2026-05-18; primary
  recommendation MComp, backup BAustMS; operator selected BAustMS path).
- Downstream slot: `BAUSTMS-PREP-KSPSLQ-001` (BLOCKED on this slot's
  confirmation gate).
