
### C1 - Remark 2.2 is false (the lemma)

| Claim | Session | Label | Route | Basis |
|---|---|---|---|---|
| `R1-18` | CT-R1-AUDIT | PROVEN | **A — cold** | proof: CT-S11-COLDREAD3 read a self-contained packet (coldpackets/PACKET-A) with no access to the derivation h |
| `R1-43` | CT-R1-AUDIT | PROVEN | **A — cold** | proof: as R1-18; this claim records the improvement itself. |
| `step-4-log` | CT-S11-COLDREAD3 | PROVEN | **C — is the cold work** | produced by CT-S11-COLDREAD3, the independent session |
| `c-independence` | CT-S11-COLDREAD3 | VERIFIED | **C — is the cold work** | produced by CT-S11-COLDREAD3, the independent session |
| `sympy-examples` | CT-S11-COLDREAD3 | VERIFIED | **C — is the cold work** | produced by CT-S11-COLDREAD3, the independent session |
| `S6-C13` | CT-S6-APPARENCY | PROVEN | **D — corroborated** | CT-S11-COLDREAD3 `step-4-log`, `c-independence` — proved the general lemma forcing exponents [0,0] at every simple root of chi |
| `S6-C14` | CT-S6-APPARENCY | PROVEN | **D — corroborated** | CT-S11-COLDREAD3 `step-4-log`, `c-independence` — as S6-C13 |
| `S6-C17` | CT-S6-APPARENCY | PROVEN | **D — corroborated** | CT-S11-COLDREAD3 `sympy-examples` — independent symbolic examples of the same lemma |

### C2 - the PV parameter contradiction

| Claim | Session | Label | Route | Basis |
|---|---|---|---|---|
| `R1-65` | CT-R1-AUDIT | PROVEN | **D — corroborated** | CT-S12-COLDREAD4 `CT-S12-COLDREAD4-Q1-DICT` — inputs page-image verified; the arithmetic step is 1-0-0 |
| `R1-64` | CT-R1-AUDIT | INSPECTED | **B — INSPECTED** | fact about a named file/page at a stated hash |
| `R1-31` | CT-R1-AUDIT | PROVEN | **A — cold** | computation: CT-S12-COLDREAD4 re-derived the PV rescaling law from the Painleve V equation by direct symbolic  |
| `R1-32` | CT-R1-AUDIT | INSPECTED | **A — cold** | computation/inspection: CT-S12-COLDREAD4 read the Jimbo page image itself and independently rediscovered the ( |
| `R1-29` | CT-R1-AUDIT | INSPECTED | **B — INSPECTED** | fact about a named file/page at a stated hash |
| `R1-30` | CT-R1-AUDIT | PROVEN | **D — corroborated** | CT-S12-COLDREAD4 `CT-S12-COLDREAD4-Q3-C4C5` — re-derived the System C parameter values in its own script |
| `R1-34` | CT-R1-AUDIT | STRUCTURAL | **D — corroborated** | CT-S12-COLDREAD4 `CT-S12-COLDREAD4-Q3-C4C5` — superseded and re-derived in C2 from the same page-image-verified dictionary |
| `CT-S12-COLDREAD4-Q1-DICT` | CT-S12-COLDREAD4 | VERIFIED | **C — is the cold work** | produced by CT-S12-COLDREAD4, the independent session |
| `CT-S12-COLDREAD4-Q1-EIGEN` | CT-S12-COLDREAD4 | VERIFIED | **C — is the cold work** | produced by CT-S12-COLDREAD4, the independent session |
| `CT-S12-COLDREAD4-Q3-C4C5` | CT-S12-COLDREAD4 | PROVEN | **C — is the cold work** | produced by CT-S12-COLDREAD4, the independent session |
| `CT-S12-COLDREAD4-Q4-C6` | CT-S12-COLDREAD4 | PROVEN | **C — is the cold work** | produced by CT-S12-COLDREAD4, the independent session |
| `CT-S9-PVPARAMS-C003` | CT-S9-PVPARAMS | INSPECTED | **B — INSPECTED** | fact about a named file/page at a stated hash |

### C3 - not well-posed as isomonodromy

| Claim | Session | Label | Route | Basis |
|---|---|---|---|---|
| `R1-33` | CT-R1-AUDIT | STRUCTURAL | **A — cold** | computation: CT-S12-COLDREAD4 recomputed k and t in its own script from the packet statement, with no access t |
| `CT-S12-COLDREAD4-Q5-C7` | CT-S12-COLDREAD4 | STRUCTURAL | **C — is the cold work** | produced by CT-S12-COLDREAD4, the independent session |
| `CT-S9-PVPARAMS-C014` | CT-S9-PVPARAMS | STRUCTURAL | **A — cold** | cold-read by CT-S15-COLDREAD-DEFERRED as statement 2, verdict CORRECT; that reader had no access to this sessi |

### C4 - per-object surface labels

| Claim | Session | Label | Route | Basis |
|---|---|---|---|---|
| `R1-52` | CT-R1-AUDIT | STRUCTURAL | **A — cold** | cold: CT-S13-COLDREAD5 worked from a self-contained packet with no access to CT-S4-FORMAL-TYPE, CT-S5B-COVER,  |
| `R1-53` | CT-R1-AUDIT | INSPECTED | **A — cold** | cold: CT-S13-COLDREAD5 worked from a self-contained packet with no access to CT-S4-FORMAL-TYPE, CT-S5B-COVER,  |
| `R1-54` | CT-R1-AUDIT | INSPECTED | **B — INSPECTED** | fact about a named file/page at a stated hash |
| `R1-55` | CT-R1-AUDIT | STRUCTURAL | **A — cold** | cold: CT-S13-COLDREAD5 worked from a self-contained packet with no access to CT-S4-FORMAL-TYPE, CT-S5B-COVER,  |
| `R1-56` | CT-R1-AUDIT | STRUCTURAL | **A — cold** | cold-read by CT-S15-COLDREAD-DEFERRED, verdict CORRECT WITH WORDING CHANGE; the wording refinement is adopted  |
| `R1-57` | CT-R1-AUDIT | CONJECTURED | **GAP** | no independent check |
| `R1-06` | CT-R1-AUDIT | INSPECTED | **B — INSPECTED** | fact about a named file/page at a stated hash |
| `R1-07` | CT-R1-AUDIT | INSPECTED | **B — INSPECTED** | fact about a named file/page at a stated hash |
| `S4-05` | CT-S4-FORMAL-TYPE | PROVEN | **D — corroborated** | CT-S13-COLDREAD5 `A1`, `A2-A3` — recomputed System A's normal form and both Katz invariants |
| `S4-06` | CT-S4-FORMAL-TYPE | PROVEN | **D — corroborated** | CT-S14-COLDREAD-B `c01`, `c02`, `c03` — recomputed object B's singular points, Katz invariants and the (0,0,1) tuple in its own code, from the printed normal form alone |
| `S5B-C4` | CT-S5B-COVER | PROVEN | **D — corroborated** | CT-S13-COLDREAD5 `A5-formal` — recomputed the z=w^2 pullback |
| `S5B-C5` | CT-S5B-COVER | PROVEN | **D — corroborated** | CT-S13-COLDREAD5 `A5-formal` — recomputed the z=w^2 pullback |
| `S5B-C6` | CT-S5B-COVER | PROVEN | **D — corroborated** | CT-S14-COLDREAD-B `c05`, `c06`, `c09`, `c11` — independently established the inversion identity, the twist and the Table 2.1 row for object B |
| `S6-C9` | CT-S6-APPARENCY | PROVEN | **D — corroborated** | CT-S13-COLDREAD5 `A4-table` — read the four ordered columns of Table 2.1 and confirmed the dash slot |
| `S6-C10` | CT-S6-APPARENCY | STRUCTURAL | **D — corroborated** | CT-S13-COLDREAD5 `A6` — reached the same necessary-not-sufficient conclusion independently |
| `A4-table` | CT-S13-COLDREAD5 | VERIFIED | **C — is the cold work** | produced by CT-S13-COLDREAD5, the independent session |
| `A5-table` | CT-S13-COLDREAD5 | VERIFIED | **C — is the cold work** | produced by CT-S13-COLDREAD5, the independent session |

### C5 - downstream passages in v1.2

| Claim | Session | Label | Route | Basis |
|---|---|---|---|---|
| `R1-66` | CT-R1-AUDIT | INSPECTED | **B — INSPECTED** | fact about a named file/page at a stated hash |
| `R1-63` | CT-R1-AUDIT | INSPECTED | **B — INSPECTED** | fact about a named file/page at a stated hash |