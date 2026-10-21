# TASK 1 - difference between the b-route and c-route reductions

Derived by elimination from y' = N y with generic entries n11,n12,n21,n22.
No formula assumed; the c-route is the same elimination with the two
components swapped.

## b-route (eliminate y2; scalar equation for y1)

    P_b = -n11(z) - n22(z) - Derivative(n12(z), z)/n12(z)
    Q_b = n11(z)*n22(z) + n11(z)*Derivative(n12(z), z)/n12(z) - n12(z)*n21(z) - Derivative(n11(z), z)

## c-route (eliminate y1; scalar equation for y2)

    P_c = -n11(z) - n22(z) - Derivative(n21(z), z)/n21(z)
    Q_c = n11(z)*n22(z) - n12(z)*n21(z) - Derivative(n22(z), z) + n22(z)*Derivative(n21(z), z)/n21(z)

## Difference, closed form

    P_b - P_c = Derivative(n21(z), z)/n21(z) - Derivative(n12(z), z)/n12(z)
              = d/dz log(n21/n12)
    simplify(P_b - P_c - d/dz log(n21/n12)) == 0 : True

Under SS1 (n12 = -b/D, n21 = -c/D) the 1/D cancels in the ratio:

    P_b - P_c = Derivative(c(z), z)/c(z) - Derivative(b(z), z)/b(z) = d/dz log(c/b)
    simplify(check) == 0 : True

## Controls that can fail

    control_nonzero  (fires if P_b-P_c collapsed to 0 identically, which
      would make the b/c distinction invisible): PASS=True
    control_shared   (fires if the two routes differed anywhere outside
      the logarithmic-derivative term): PASS=True
