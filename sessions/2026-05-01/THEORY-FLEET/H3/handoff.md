# H3 handoff — Painlevé reduction at d = 2

## Top-line verdict

`D=2_REDUCTION_AMBIGUOUS_NEEDS_NUMERICS`

## Main finding

The d = 2 PCF recurrence is a rank-2 linear recurrence. Its ratio map is a non-autonomous discrete Riccati equation, hence linearisable. Sakai's discrete Painlevé classification applies to two-dimensional birational maps on rational surfaces, not to the scalar recurrence alone. Therefore the literature does not confirm a two-branch Painlevé reduction yet.

## Conditional branch prediction

If a nontrivial isomonodromic/Lax lift is constructed:

- `Delta_2 < 0` most likely corresponds to P-III(D6) / D6^(1).
- `Delta_2 > 0` most likely corresponds to P-V / D5^(1), unless an apparent singularity collapses it to Riccati/Painlevé-trivial.
- `Delta_2 = 0` should be treated as a resonant boundary, possibly D7/D8 or Riccati.

## d >= 3

The claim that `d >= 3` sits on a generic P-VI stratum is plausible only if the lifted problem has four regular singular directions and D4^(1) Sakai surface type. H3 did not find a literature-only proof.

## Recommended aggregator action

Recommend T3, but phrase it as a **classification test**, not a confirmation run. The decisive work is: construct the lifted birational/Lax system, compute Sakai root type, then verify PV/PIII sigma-form residuals across representative `Delta_2` signs.

## Key references

Sakai 2001; Kajiwara--Noumi--Yamada 2017; Conte--Musette 2020; Fokas--Its--Kapaev--Novokshenov 2006; Its--Kapaev 1988; Joshi--Kruskal 1988; Kruskal--Joshi--Halburd 1997.
