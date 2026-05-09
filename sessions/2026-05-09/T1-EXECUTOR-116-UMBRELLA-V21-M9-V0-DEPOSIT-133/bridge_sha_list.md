# Bridge SHA list -- 116 v2.1 deposit substrate

Verified at fire time (2026-05-09; bridge HEAD = `8ebd1eb`).

| Role | Short SHA | Full SHA | Subject (one-line) |
|---|---|---|---|
| 115-SHA (Item 3 anchor) | `8ebd1eb` | `8ebd1ebb2aff635cbd12f6fa30c974bfb5aecbd9` | T2-EXECUTOR-115-ROUTE-F-D7-FIXED-POINT-EXTRACTION-132 |
| Q4 v2 verdict (Item 2 anchor) | `8a22b11` | `8a22b11577ca9fd582d03d48d66d743cd7c7e4dc` | T1-SYNTH-Q4-V2-VERDICT-ABSORPTION-131 |
| Q4 v2 packet (Item 2 anchor) | `10b5cf6` | `10b5cf60027492410b8d435d9de1ec208172e853` | T1-OPERATOR-Q4-ROUND2-DIRECT-DERIVATION-PACKET-130 |
| M4-RATIF-SHA (Item 1 anchor) | `5f9db69` | `5f9db69c754c410b79091cbd84e6d79b63d10b6e` | M4-V0-CLOSURE-CASCADE-106 |
| 069r3 cross-cascade convergence | `ae5b7f7` | `ae5b7f7` (per session 124 deposit log) | T1-SYNTH-069R3-FINAL-VERDICT-ABSORPTION-124 |

Full git rev-parse output (terminal capture, 2026-05-09):

```
8a22b11577ca9fd582d03d48d66d743cd7c7e4dc
10b5cf60027492410b8d435d9de1ec208172e853
8ebd1ebb2aff635cbd12f6fa30c974bfb5aecbd9
fatal: Needed a single revision           # 6a82147 from prompt sec 2.1 NOT a valid SHA prefix
=== HEAD ===
8ebd1ebb2aff635cbd12f6fa30c974bfb5aecbd9
```

The prompt's sec 2.1 hint `6a82147` for `<M4-RATIF-SHA>` does not
resolve as a valid prefix in the bridge. The actual M4 V0 closure
ratification session is `M4-V0-CLOSURE-CASCADE-106` at SHA
`5f9db69`, located via `git log --oneline --all | Select-String M4-V0-CLOSURE`.
See DISCREPANCY-116-M4-RATIF-SHA in `discrepancy_log.json`.
