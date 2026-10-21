# REPORT.md — CT-S5B-COVER (P5b)

Session: `sessions/2026-09-17/CT-S5B-COVER/`  
Script: `formal_type.py`  
Machine output: `formal_type_p5b.json`, sha256 `1073ac2fbef5cde46224087d84e10060cdf722b40cdc45b6dd67864cba7ad63a`  
Run log: `run.log`  
Arithmetic: exact SymPy 1.14.0; no floating point; `dps = null` in `claims.jsonl` because no numerical tolerance is used.

## What was done

STRUCTURAL: I copied CT-S4's `formal_type.py` into this session folder and extended only the copy.  
STRUCTURAL: I wrote `PREREG.md` before computation, with the fixed CT-S4 pole-order classification rule, falsifiers, and vacuity pre-check.  
STRUCTURAL: I derived the pullback rule for normal forms, tested it on an Euler equation, applied `z = w^2` to System A, applied `z -> 1/x` to System B, and classified every finite singular point and infinity.

## Pullback derivation

STRUCTURAL: For `u'' = r(z)u` and `z = phi(s)`, `v(s)=u(phi(s))` satisfies
`v'' - (phi''/phi')v' - (phi')^2 r(phi)v = 0`. Removing the first-derivative term gives
`R(s) = (phi')^2 r(phi(s)) - (1/2){phi,s}`, where `{phi,s}` is the Schwarzian derivative.  
PROVEN: For `phi=w^2`, `{phi,w} = -3/(2w^2)`, so the correction is `+3/(4w^2)`.  
PROVEN: For `phi=1/x`, `{phi,x}=0`.

## Claims

PROVEN: S5B-C1 — System A and System B CT-S4 baseline normal forms and certificates recompute exactly.

STRUCTURAL: S5B-C2 — For normal-form pullback, `R=(phi')^2*r(phi)-1/2*Schwarzian(phi)` was derived and passed the Euler exponent-difference doubling test.

PROVEN: S5B-C3 — The vacuity pre-check passed: `r=1/z^4` remains unramified after `z=w^2`, and System A's pole order at zero changes from `3` to `4`.

PROVEN: S5B-C4 — Pullback of System A along `z=w^2` has exactly one finite singular point `w=0`, pole order `4`, unramified Katz invariant `1`.

PROVEN: S5B-C5 — Pullback of System A along `z=w^2` has an unramified irregular singularity of Katz invariant `1` at infinity.

PROVEN: S5B-C6 — Inversion `z->1/x` applied to System B has `x=0` ordinary, finite regular singular points at `(-1 ± i*sqrt(11))/6`, and unramified Katz `1` at infinity.

STRUCTURAL: S5B-C7 — VQ-N1 `verdict.md` records `x=0` ordinary, finite points `(-1 ± i√11)/6`, and rank-1 unramified infinity; these locations/types match the inverted System B configuration, except apparency indices were not recomputed.

STRUCTURAL: S5B-C8 — The local Katz/ramification mismatch between System A at `z=0` and System B at `z=0` is removed by `z=w^2` at the branch point.

STRUCTURAL: S5B-C9 — The global singular configurations of `pi^*`System A under `z=w^2` and System B are not reconciled by that cover alone.

STRUCTURAL: S5B-C10 — CT-S4 verdict (c) is sharpened but not settled as a global isomorphism: the local mismatch is a coordinate artefact, while global equivalence remains unestablished.

## Tables

PROVEN: `pi^*`System A under `z=w^2` has normal-form potential
`(-48*w**4 - 53*w**2 + 48)/(36*w**4)`. Its finite singular set is `{0}`; at `w=0` the pole order is `4`, ramification index is `1`, and Katz invariant is `1`; at infinity the pole order is `4`, ramification index is `1`, and Katz invariant is `1`.

PROVEN: Inverted System B has normal-form potential
`(12*x**4 + 4*x**3 + 4*x**2 + 11)/(4*(3*x**2 + x + 1)**2)`. Its finite poles are `(-1 ± i*sqrt(11))/6`, both regular singular with pole order `2`; `x=0` has pole order `0`; infinity has pole order `4`, ramification index `1`, and Katz invariant `1`.

## Verdict

STRUCTURAL: The ramified/unramified mismatch identified in CT-S4 does not survive the `z=w^2` transformation locally at the branch point: `pi^*`System A is unramified Katz `1` at `w=0`, matching System B's local Katz invariant at `z=0`.  
STRUCTURAL: This does not settle a global isomorphism, because `pi^*`System A has one finite singular point and irregular infinity, while System B has three finite singular points and regular infinity.  
STRUCTURAL: The inversion `z->1/z` does explain the VQ-N1 placement of System B's singular configuration, modulo the apparency indices not recomputed here.  
STRUCTURAL: CT-S4's verdict (c) is therefore sharpened: the local mismatch is a coordinate artefact, but global reconciliation remains unestablished.

## What was NOT established

STRUCTURAL: I did not prove `pi^*`System A is globally isomorphic to System B; the computed global configurations disagree.  
STRUCTURAL: I did not recompute VQ-N1's apparent-singularity indices `[0,0]`; I checked only locations and formal types.  
STRUCTURAL: I did not revise any conjecture or source file outside this session folder.  
STRUCTURAL: I did not use any floating-point numerical test or Painlevé classification table.

## Open questions for the operator

CONJECTURED: Is there an additional transformation beyond `z=w^2` that can reconcile the extra finite regular singularities and infinity behavior globally?  
CONJECTURED: Should the VQ-N1 apparent indices be recomputed directly from an explicit VQ-N1 operator, if available?  
CONJECTURED: Should this local coordinate-artifact finding update a later manuscript or ledger entry in a separate, operator-approved session?

## Files created or modified in this session folder

STRUCTURAL: Uncommitted session files are:

- `sessions/2026-09-17/CT-S5B-COVER/PREREG.md`
- `sessions/2026-09-17/CT-S5B-COVER/formal_type.py`
- `sessions/2026-09-17/CT-S5B-COVER/formal_type_p5b.json`
- `sessions/2026-09-17/CT-S5B-COVER/run.log`
- `sessions/2026-09-17/CT-S5B-COVER/claims.jsonl`
- `sessions/2026-09-17/CT-S5B-COVER/REPORT.md`
