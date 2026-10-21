# TASK 3 - verdict

CLAIM UNDER TEST (and nothing else):
  "The b-route and c-route scalar reductions of the same rank-2 system differ
   in P by d/dz log(c/b); under the b-route, System C's P and Q match the
   system at the given point exactly."

## VERDICT: CORRECT

## Evidence

### Part 1 - the difference in P  (outputs/task1.md)

Derived by elimination from y' = N y with generic entries, no formula assumed:

    P_b = -(n11 + n22) - (d/dz n12)/n12          (unknown y1, y2 eliminated)
    P_c = -(n11 + n22) - (d/dz n21)/n21          (unknown y2, y1 eliminated)
    P_b - P_c = d/dz log(n21/n12),   simplify(difference) == 0 : True

Under the convention of inputs.md SS1 (n12 = -b/D, n21 = -c/D) the common
factor -1/D cancels in the ratio, giving exactly

    P_b - P_c = d/dz log(c/b),       simplify(difference) == 0 : True

Sign/orientation: it is b-route MINUS c-route that equals +d/dz log(c/b).
Proviso, not a correction: this identification of n21/n12 with c/b uses the
fact that SS1 divides both off-diagonal entries by the same D.  The
route-difference itself, d/dz log(n21/n12), is convention-free.

Re-verified at the SS3 point as a rational-function identity:
    (P_b - P_c) - d/dz log(c/b) : exact cancel(...) = 0;
    numeric max |.| at dps 40 = 9.6e-181 over four sample z.  (task2.md)

### Part 2 - the b-route at the given point  (outputs/task2.md)

Exact test = cancel(difference, z, extension=True) over Q(i,sqrt3,sqrt11),
so radicals are never compared with ==; plus evaluation at dps 40.

    P_b - P_C : exact 0 ; numeric max |.| = 2.0e-177    MATCH
    Q_b - Q_C : exact 0 ; numeric max |.| = 2.5e-175    MATCH

The c-route does not match, and fails by exactly the predicted amount:

    P_c - P_C = -5385952/(5385952*z - 2692976 - 12394800*sqrt(33)*I
                          + 20149228*sqrt(11)*I)
              = -1/(z - q)          with q the SS3 value
    Q_c - Q_C : nonzero (numeric max |.| = 8.1)

That residual is what d/dz log(c/b) contributes from the simple zero of
c(z) = -(z-q)/(q-1) at z = q, b being constant at this point.  So a
comparison made against the c-route would report a spurious mismatch of
exactly -1/(z-q) in P.

### Part 2b - thi at infinity  (outputs/task2b.md)

Consistent.  The rate +t/2 branch of the system has eigenvector e1 + O(1/z),
so its first component carries exponent N11_1 = thi/2 with no shift, for every
thi; System C demands -1 - sqrt(3)/18, giving thi = -2 - sqrt(3)/9, which is
the printed value exactly (residual 0 at dps 40).  The other branch is shifted
by -ord_oo(N12) = -2, and the resulting prediction -1 + sqrt(3)/18 matches
System C exactly as well.  Nothing here was adjusted.

## Controls that could have fired, and did not

  task1 control_nonzero      - would fire if P_b - P_c collapsed to 0
                               identically, making the b/c distinction
                               invisible.                        PASS
  task1 control_shared       - would fire if the routes differed anywhere
                               outside the logarithmic-derivative term. PASS
  task2 control_separates    - would fire if P_b - P_c vanished at THIS point,
                               making the distinction vacuous here; instead
                               |P_b - P_c| = 1.45 numerically.   PASS
  task2 control_discriminates- would fire if the same exact test also accepted
                               a deliberately wrong point (q -> q+1); it
                               returned a nonzero residual there.  PASS
  task2b control_sensitive   - would fire if the system-side exponent did not
                               depend on thi.                    PASS
  task2b control_discriminates- would fire if the test also accepted thi + 1;
                               residual 1/2.                     PASS

## Defects in my own work, caught and discarded

Two attempts at task 2b were unsound and are recorded in outputs/task2b.md:
reading heads of the scalar reduction with thi symbolic (deg_z b drops from 1
to 0 at the printed thi, so the heads are discontinuous exactly there), and
treating mu(+) - mu(-) as gauge-invariant between system and scalar (the two
branches carry different powers of z here, 0 and -2).  The second would have
returned thi = sqrt(3)/9 and a verdict of "inconsistent", wrong by exactly the
shift.  Both were caught by an arithmetic control: the two scalar exponents
must sum to -P1.  Neither is used in the verdict above.

## Not established here

Nothing in this run bears on wording, membership, deposit questions, or on the
convention N = -A/D itself, which inputs.md SS1 gives and which was out of
scope.
