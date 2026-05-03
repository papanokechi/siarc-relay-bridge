# Phase C.3 — Aggregate Literature Verdict (Dispatch 4)

**Dispatch 4 timestamp:** 2026-05-03 (re-fire 4)
**Verdict signal:** `C_LITERATURE_UNIFORM`

## Inputs

- Phase C.1 (Wasow): `C_WASOW_UNIFORM` (Theorem 19.1, eq. 19.3,
  shearing transformation, all uniform in n and q ≥ 0; covers
  fractional q via independent-variable ramification).
  Source: `phase_c1_wasow_verification.md` (dispatch 4).
- Phase C.2 (Birkhoff): split signal carried forward from
  dispatch 3:
  - (i) **`C_BIRKHOFF_UNIFORM`** — Birkhoff §2 formal-series
    existence is uniform in n (= d).
  - (ii) **`C_BIRKHOFF_BOREL_NOT_IN_§§2-3`** — Borel-singularity-
    radius theorem is NOT in Birkhoff §§2-3. **Re-targeted in
    dispatch 4** to Wasow §19 eq. (19.3), where it is `q ≥ 0`
    uniform.
  Source: `phase_c2_birkhoff_verification.md` (dispatch 3, retained
  unchanged in dispatch 4).

## Aggregate proof d-range

`d_W*` = ∞ (Wasow uniform in q ≥ 0; covers q ∈ ℚ_≥0 via §19.3
ramification; PCF-1 mapping `q = (d+2)/2` is in ℚ_≥0 for all
d ≥ 2; no d-cap).

`d_B*` = ∞ on the formal half (Birkhoff §2 Theorem I states
`A possesses a formal series solution… of the form
z^c · sum a_n z^{-n}` for any n × n linear system at an
irregular singular point, with no n-cap or rank-cap).

`d_B*` = ∞ on the Borel half via re-targeting to Wasow §19
eq. (19.3) (uniform in q ≥ 0; same ramification mechanism as
Wasow §19.3).

**Aggregate d-range:**
`min(d_W*, d_B*-formal, d_B*-Borel-via-Wasow) = min(∞, ∞, ∞) = ∞`.

The proof is uniform in d — i.e., applies to all d ≥ 2 without
restriction.

## Vocabulary-equivalence judgment (dispatch 4)

Prompt 018 §2 step 5 names Wasow's content as "Newton polygon
slope-p/q edge → rank q irregular singularity / characteristic
exponents = roots of polynomial of degree q". Wasow's actual
vocabulary uses "shearing transformations" and "characteristic
roots of A₀" (the leading matrix). These are **substantively
equivalent**: the Newton polygon slope p/q encodes the rank, and
the characteristic equation at that slope produces the same
characteristic roots.

Dispatch 4 treats this as **uniform-equivalent**, not
weaker. Synthesizer-side recommendation in handoff Anomalies:
accept this equivalence since (a) Adams 1928 and Wasow 1965 are
both cited side-by-side in any modern reference (Loday-Richaud
2016 ch. 2; Costin 2009 ch. 7) and (b) §19.3's shearing exponent
g₀ literally is the smallest Newton-polygon slope.

## Verdict signal

`C_LITERATURE_UNIFORM` — both literature anchors (Wasow general
case via Thm 19.1 + eq. 19.3; Birkhoff §2 formal half) supply
the required theorems uniformly in d, with the Borel half
re-targeted to Wasow §19 (the Prompt 018 spec error).

Proceed to Phase D.
