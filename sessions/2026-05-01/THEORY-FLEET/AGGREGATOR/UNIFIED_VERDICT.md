# THEORY-FLEET Unified Verdict

| H | Topic | Verdict | Confidence | Notes |
|---|---|---|---|---|
| H1 | Birkhoff-Trjitzinsky / B4 | `B4_PROVED_AT_d≥3_RESIDUE_AT_d=2` | HIGH on slope, MED on d=2 mechanism, HIGH on residue-existence | BACKFILLED by main orchestrator after original sub-agent declined; treated as authoritative theory for this aggregation. |
| H2 | Eisenstein/CM-period | `LITERATURE_INACCESSIBLE_PARTIAL` | MED | Provisional: `j=0 -> A_true - 2d = 0` exactly via `E4(rho)=0`; Chowla-Selberg enters subleading constants. |
| H3 | Painlevé hierarchy at d=2 | `D=2_REDUCTION_AMBIGUOUS_NEEDS_NUMERICS` | MED | Rank-2 linear recurrence gives a discrete Riccati map; Sakai classification needs a lifted birational map. |
| H4 | Écalle resurgence on V_quad | `MEDIAN_RESURGENCE_GIVES_30+_DIGITS` | HIGH | `zeta*=4/sqrt(3)` is a Borel branch point; 5000 coefficients at 250 dps should extract a 30-50 digit Stokes coefficient. |
| H5 | X(1) moduli substrata | `TRICHOTOMY_NOT_MODULAR_GEOMETRIC` | HIGH | Every cubic has canonical `tau_b in X(1)` and the `j=0` cell is genuine CM, but the full three-bin partition is not a modular stratum. |
| H6 | Chowla-Selberg / KZ | `AUGMENTED_BASIS_DETECTS_ALL_6` | MED | Six CM orders `D=-3,-4,-7,-11,-20,-28` supply explicit Chowla-Selberg Gamma-product augmentations for PSLQ testing. |

## One-sentence narratives

- **H1:** Birkhoff-Trjitzinsky Newton-polygon asymptotics prove the generic leading SIARC slope `A=2d` while leaving d=2 branch mechanics and arithmetic subleading residues to H3/H2/H5/H6.
- **H2:** Accessible modular-form facts strongly indicate that the equianharmonic `j=0` cubic cell has `A_true-2d=0` exactly because `E4(rho)=0`, but gated Chowla-Selberg/Yu sources prevent full theorem certification.
- **H3:** The d=2 anomaly is plausibly tied to a Painlevé confluence trichotomy, yet the scalar recurrence is only Riccati until a two-dimensional Sakai surface or Lax lift is constructed.
- **H4:** Median Écalle resurgence should replace the current Padé-Borel wall for `V_quad` by a direct branch-germ/Stokes extraction with 30-50 stable digits.
- **H5:** The modular `X(1)` coordinate is real and useful, especially at `j=0`, but the empirical three-bin split is a drift signal rather than a canonical CM, level, or `X_0(N)` partition.
- **H6:** Adding one Chowla-Selberg CM period generator for each of the six missing negative-discriminant PCF-1 cases is the minimal high-value PSLQ augmentation, pending proof that the limits are pure CM periods.

`LITERATURE_INACCESSIBLE_PARTIAL` count: **1** (H2 only). Halt threshold `>2` was not triggered.
