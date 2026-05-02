# T2.5d-J0-CHOWLA-SELBERG-CLOSURE — verdict

**Verdict label:** `AMBIGUOUS_AT_DPS8000`

**op:j-zero-amplitude-h6 status:** OPEN

## Spec vs run

- Spec asked dps>=8000, N>=1200.
- For A=6 cubics, |L_N - L_ref| ~ exp(-6 N log N), so dps for N=1200 must be >= ~22150. The literal dps=8000 reading is internally infeasible.
- Run used dps=25000 (above the 22150-digit floor) with N up to 1200, N_ref=1320.

## Per-family fit summary (5-param LIN)

| family | A_lin | delta_lin | A_lin - A_exp | agree_digits |
|---|---|---|---|---|
| 30 | 6.00000009866458799488594 | 0.0000000986645879 | 0.0000023174126080 | 5 |
| 31 | 5.99999990131228817809119 | -0.000000098687711 | 0.0000019749481585 | 5 |
| 32 | 5.99999985197425229825046 | -0.000000148025747 | 0.0000018893320819 | 5 |
| 33 | 5.99999980263623204814593 | -0.000000197363767 | 0.0000018037160197 | 5 |

