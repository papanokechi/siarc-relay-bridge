# CT-S14-COLDREAD-B report

SESSION_ID: CT-S14-COLDREAD-B

Repository HEAD at start: `08aa0e2381b3dc37ee54a3200b7272755ca11d59`.
Repository HEAD at end: `08aa0e2381b3dc37ee54a3200b7272755ca11d59`.
They are unchanged. I made no commits, pushes, tags, PRs, deposits, or submissions.

Isolation: I read only the packet and the four permitted page images under `sessions\2026-09-17\CT-R1-AUDIT\coldpackets\`. I did not open the PDF and did not open any other file under `sessions\2026-09-17\` outside my session folder.

## Source hashes read

From `source_hashes.out.txt`:

- `ba7b5ed35deff0a86851f0b5bedde36caf520d76dc3a9a204e06ad0940a569b2`  `sessions\2026-09-17\CT-R1-AUDIT\coldpackets\PACKET-D-objectB.md`
- `84b9dfc95b00d64c28ecb80a9477e64f07b44164b7db45bad8de819cb61ab9d0`  `sessions\2026-09-17\CT-R1-AUDIT\coldpackets\vdps_p2634.png`
- `56194f2639b0aa20d6e96863373e92ee599165e357b6b4b8c9221474b070da6b`  `sessions\2026-09-17\CT-R1-AUDIT\coldpackets\vdps_p2635.png`
- `5ecb9f5d10af1f45a05b7c2a60f1fc2d12ca79adf75f4cfc417adb6561261b7c`  `sessions\2026-09-17\CT-R1-AUDIT\coldpackets\companion_v12_p2.png`
- `7393d63dbff7cbb8ce49596ea2f0e1376c885c556a1da9bf3b08b6c65cf16f66`  `sessions\2026-09-17\CT-R1-AUDIT\coldpackets\companion_v12_p3.png`

## Script/output hashes

- `formal_type.py`: `bd1cba2176032b806a1801cdf51e48c5bc918597ca5e5445b87c0b5836c23708`
- `formal_type.out.txt`: `863b444ce1754d5aff86ebf2763d18a4b9b408c45e75c5cb96725ce607998e70`
- `relation_twist.py`: `365845840444889f73a8f6a9ad8d916138b46795eeef823b6f5fa07fadb61856`
- `relation_twist.out.txt`: `f6b6de9a07a40a5884ff75a138afa4274f8031bde9dba6ebfd96a0233adc3868`
- `source_hashes.py`: `3192dc089f571f5a0e3c7f8844c157a71dc4ea602a271bae7290c1b529d1cba5`
- `source_hashes.out.txt`: `875c13ac7c60a3b7501dec968c589421d37adadd338e41806cfec391b5ff2108`

## Page-image quotations used

From van der Put--Saito p. 2634 image: "We consider a local family M(u) of differential modules, represented by a matrix equation d/dz + A(z,u) where A(z,u) is a 2 × 2-matrix with trace 0 and u lies in a small polydisk D around 0." Same page: "Columns 3--6 of the next table present the ten resulting cases." Same page: "We will not number these ten families, but indicate them by their Katz invariants, e.g., (0, 0, 0, 0), (0, 0, 1), . . . , (0, -, 3/2), (-, -, 3), (-, -, 5/2)."

From van der Put--Saito p. 2635 image, Table 2.1 row: `\tilde D_5 | P_V | 0 | 0 | 1 | - | 3` under columns `Dynkin | Painleve | r(0) | r(1) | r(∞) | r(t) | dim(P)`.

From companion v1.2 p. 3 image, I read the polynomial row as: `r0 = 3t^2 + t + 1`, `r1 = 6t + 1`, `r2 = -t^2`; I used variable `x` in the scripts.

## Task 1 — Face-value formal data for `L_phi`

Verdict: `L_phi` has exactly three singular finite points and infinity is ordinary. The finite points are:

- `z=0`: pole order 4 in the trace-free normal potential, leading coefficient `1/3`; formal square-root branches have exponential factors `exp(-sqrt(3)/(3z))*z^(-sqrt(3)/18)` and `exp(sqrt(3)/(3z))*z^(sqrt(3)/18)`. Newton polygon connection slopes `[1,1]`; ramification `1`; Katz invariant `1`.
- `z=(-1-sqrt(11)i)/2`: regular singular; local exponents `[1/2,1/2]`; Newton polygon slopes `[0,0]`; ramification `1`; Katz invariant `0`.
- `z=(-1+sqrt(11)i)/2`: regular singular; local exponents `[1/2,1/2]`; Newton polygon slopes `[0,0]`; ramification `1`; Katz invariant `0`.
- `z=∞`: after `x=1/z`, the trace-free normal potential is analytic at `x=0`; ordinary exponents `[0,1]`; Newton polygon slopes `[0,0]`; ramification `1`; Katz invariant `0`.

Thus the authors' Katz-invariant notation is `(0,0,1)` after moving the two regular singularities and the one irregular singularity to `{0,1,∞}`. This is a symbolic-computation claim from `formal_type.py`, not a Table-membership proof.

## Task 2 — Relation between B and C

Verdict: both inversion and a rank-1 twist are involved if one wants the companion's printed scalar operator; inversion alone identifies the trace-free normal forms.

The companion equation read from the page image is

`A(x) W'' + B(x) W' + C(x) W = 0`, with `A=3x^2+x+1`, `B=6x+1=A'`, and `C=-x^2`.

For `P=B/A`, `Q=C/A`, its trace-free normal potential is

`P'/2 + P^2/4 - Q = (12x^4+4x^3+4x^2+11)/(4(3x^2+x+1)^2)`.

The pullback of `L_phi` by `z=1/x` has the same trace-free normal potential `r_B(1/x)/x^4`, and `relation_twist.py` verifies the symbolic difference is zero.

Explicitly, if `Y(x)=y(1/x)`, the pullback equation is

`Y'' + (2/x)Y' - r_B(1/x)/x^4 Y = 0`.

Putting `U=xY` gives the trace-free normal form `U''=r_B(1/x)/x^4 U`. The companion's printed scalar equation is obtained by the rank-1 twist

`U = sqrt(3x^2+x+1) W`, equivalently `W=(3x^2+x+1)^(-1/2)U`.

## Task 3 — Integer-difference points

Verdict: the integer-difference points do not become ordinary after the twist to the companion's printed scalar operator.

The two regular singular points of `L_phi` have equal exponents `[1/2,1/2]`. Under `z=1/x` they map to the roots of `A=3x^2+x+1`, namely `x=(-1±sqrt(11)i)/6`. After the twist `W=A^(-1/2)U`, the companion equation has `P=A'/A`. At each root, `residue(P)=1`, `lim (x-beta)^2 Q=0`, and the indicial polynomial is `lambda^2`; so the exponents are `[0,0]`. But `P` has a nonzero simple-pole residue, so the coefficient functions are not analytic there. Therefore those points are apparent/regular singular in the printed scalar equation, not ordinary.

## Task 4 — Compatibility of the twist with Table 2.1 normalisation

Verdict: the rank-1 twist to the companion's printed scalar operator is not compatible with the trace-free normalisation of the class Table 2.1 classifies, unless the twist has square equal to a nonzero constant (equivalently `dlog(h)=0`) so that it does not change trace. The twist here has `h=A^(-1/2)`, hence `2 dlog(h) = -dlog(A)`, not zero.

Load-bearing page-image quote from p. 2634: "A(z,u) is a 2 × 2-matrix with trace 0". Since a rank-2 connection twisted by a rank-1 connection with multiplier `h` changes the trace by `2 dlog(h)`, the twist `h=(3x^2+x+1)^(-1/2)` changes trace by `-dlog(3x^2+x+1)`. `relation_twist.py` prints the resulting scalar companion trace as `-(6*x + 1)/(3*x**2 + x + 1)`.

Therefore the Table 2.1 row is preserved under the coordinate inversion of the trace-free normal form, but not under the additional trace-altering twist to the companion's printed scalar equation. If one re-normalises after twisting, one returns to the trace-free normal potential already matched by inversion.

## Task 5 — Row lookup

Face-value `L_phi`: STRUCTURAL row match to Table 2.1 p. 2635 row `\tilde D_5 | P_V | 0 | 0 | 1 | - | 3`, because the computed Katz-invariant tuple is `(0,0,1)` and p. 2634 says the families are indicated by Katz invariants including `(0,0,1)`.

After `z=1/x` but kept trace-free: the same STRUCTURAL row match applies; it is just the same three-point formal type with one Katz invariant `1` and two `0` entries.

After the rank-1 twist to the companion's printed scalar operator: no Table 2.1 row applies as an object in that scalar basis, because the p. 2634 construction is for trace-zero `2 × 2` matrices and the twist gives nonzero trace `-(6x+1)/(3x^2+x+1)`. Re-normalising that operator restores the trace-free normal form and hence the previous structural row match.

## Task 6 — Verdict on drafted sentence

**CORRECT WITH WORDING CHANGE.**

Suggested replacement:

`| B | L_phi | (0,0,1) at face value; inversion identifies the companion's trace-free normal form, while the additional rank-1 twist to the companion scalar operator is outside Table 2.1's trace-free normalisation | PV / D̃5 |`

Reason: `(0,0,1)` and `PV / D̃5` are structurally supported for `L_phi` at face value and after inversion of the trace-free normal form. The phrase "up to inversion and twist" should not be used without qualification, because the twist needed for the companion's printed scalar operator changes trace and is not row-preserving inside Table 2.1's trace-free class.

## What I could not establish / open questions

- I did not establish membership in a Painleve family beyond the STRUCTURAL Table 2.1 row match; the packet explicitly forbids upgrading a row match beyond STRUCTURAL.
- I did not use the PDF text layer or inspect pages beyond the permitted page images.
- I did not determine whether the companion document elsewhere explains its scalar-basis singularities; that material was outside the permitted cold-read inputs.

## Deliverables left uncommitted

- `sessions\2026-09-17\CT-S14-COLDREAD-B\REPORT.md`
- `sessions\2026-09-17\CT-S14-COLDREAD-B\claims.jsonl`
- `sessions\2026-09-17\CT-S14-COLDREAD-B\formal_type.py`
- `sessions\2026-09-17\CT-S14-COLDREAD-B\formal_type.out.txt`
- `sessions\2026-09-17\CT-S14-COLDREAD-B\relation_twist.py`
- `sessions\2026-09-17\CT-S14-COLDREAD-B\relation_twist.out.txt`
- `sessions\2026-09-17\CT-S14-COLDREAD-B\source_hashes.py`
- `sessions\2026-09-17\CT-S14-COLDREAD-B\source_hashes.out.txt`
