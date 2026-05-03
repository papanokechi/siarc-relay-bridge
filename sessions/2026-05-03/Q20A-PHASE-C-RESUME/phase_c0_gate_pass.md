# Phase C.0 — Literature Gate (Dispatch 4)

**Dispatch 4 timestamp:** 2026-05-03 (re-fire 4)
**Verdict signal:** `C0_GATE_PASS`

## Files present

The two G3b PDFs are on disk under the runbook-assigned location
(carry-forward from dispatch 3's path-mismatch judgment call):

```
tex/submitted/control center/literature/g3b_2026-05-03/
    01_birkhoff_1930_acta54.pdf
    04_wasow_1965_dover.pdf
    birkhoff_1930.pdf            (byte-exact alias of 01_*)
    wasow_1965_chap_X.pdf        (byte-exact alias of 04_*)
    SHA256SUMS.txt
    _OPERATOR_INSTRUCTIONS.md
```

## SHA-256 verification (computed 2026-05-03, dispatch 4)

Computed (PowerShell `Get-FileHash`) vs. SHA256SUMS.txt
(SHA256SUMS.txt header timestamp `2026-05-03T04:21:06Z`,
re-issued after the B1+B1P2 re-assembly to cover Wasow Chap V
§§16-19 in addition to Chap IV §§10-15):

| File                           | Computed (lowercase)                                                | SHA256SUMS entry                                                    | Match |
|--------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|-------|
| `birkhoff_1930.pdf`            | `aeb5291e4150535969726aa9e8aba8c604ae437612e026092122208cb3952efa`  | `aeb5291e4150535969726aa9e8aba8c604ae437612e026092122208cb3952efa`  | ✅    |
| `01_birkhoff_1930_acta54.pdf`  | `aeb5291e4150535969726aa9e8aba8c604ae437612e026092122208cb3952efa`  | `aeb5291e4150535969726aa9e8aba8c604ae437612e026092122208cb3952efa`  | ✅    |
| `wasow_1965_chap_X.pdf`        | `f59d6835db58d2de59eab843b881b97106eee6c66e56bfce43de5788bbbaa5fd`  | `f59d6835db58d2de59eab843b881b97106eee6c66e56bfce43de5788bbbaa5fd`  | ✅    |
| `04_wasow_1965_dover.pdf`      | `f59d6835db58d2de59eab843b881b97106eee6c66e56bfce43de5788bbbaa5fd`  | `f59d6835db58d2de59eab843b881b97106eee6c66e56bfce43de5788bbbaa5fd`  | ✅    |

All four hashes match SHA256SUMS.txt byte-exactly.

**Wasow PDF supersession:** the dispatch-3 hash
`e84b3e48…46410` (8 spreads, Chap X §§37-39, wrong section) and
the interim B1 hash `bb638ade…78e652` (20 spreads, Chap IV
§§10-15, distinct-eigenvalue case only) are **superseded** by
the re-assembled `f59d6835…a5fd` (34 spreads, Chap IV §§10-15
**plus** Chap V §§16-19 — distinct + general/Jordan-block cases).

## Path-mismatch judgment call (carry-forward)

Dispatch 3's Judgment Call #1 still applies: runbook-canonical
path `tex/submitted/control center/literature/g3b_2026-05-03/`
is treated as satisfying the gate (Prompt 018 §1's
workspace-root path is not used; file content is the same).
No regression on this point in dispatch 4.

## Artifacts referenced in AEAL

- SHA256SUMS.txt at
  `tex/submitted/control center/literature/g3b_2026-05-03/SHA256SUMS.txt`
- Birkhoff 1930 PDF (1,798,753 bytes; unchanged from dispatch 3)
- Wasow 1965 PDF (5,557,950 bytes; **re-assembled** for dispatch 4)

Phase C.0 result: **PASS** — proceed to Phase C.1 (Wasow §§11-19,
**unblocked** for dispatch 4 because §19 general-case theorem
is now physically present in the PDF) and Phase C.2 (Birkhoff;
dispatch 3 result carried forward).
