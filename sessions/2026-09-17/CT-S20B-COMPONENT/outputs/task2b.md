# TASK 2b - is thi consistent with System C's local data at infinity?

## System C, scalar data at infinity
    P = 0 + 2/z + ... ,  Q = 11/27 + -sqrt(11)*I/27/z + ...
    rate -sqrt(33)*I/9      exponent mu = -1 - sqrt(3)/18
    rate sqrt(33)*I/9       exponent mu = -1 + sqrt(3)/18
    rates coincide with +-t/2 = +--sqrt(33)*I/9 : True

## The system at the SS3 point, thi symbolic (TH)
    N11 = -a/D = -sqrt(33)*I/9 + (TH/2)/z + O(1/z^2)
    leading matrix diag(t/2, -t/2), distinct, so the rate +t/2 branch has
    eigenvector e1 + O(1/z): its first component carries exponent N11_1
    exactly, for every thi.

## Test on the dominant branch (rate -sqrt(33)*I/9)
    exponent demanded by System C : -1 - sqrt(3)/18
    exponent from the system      : TH/2
    TH solving the two            : ['-2 - sqrt(3)/9']
    thi printed in SS3            : -2 - sqrt(3)/9
    printed thi is a solution (simplify of the difference; radicals are
      never compared with ==) : True
    |solution - printed thi| at dps 40 : ['0']

## Subdominant branch (rate sqrt(33)*I/9): shift predicted, not assumed
    ord_oo(N12) = 1 generically in thi, 2 at the printed thi
    y1 = N12/(lam_- - lam_+) * y2 * (1+...) => exponent = N22_1 - ord
    predicted -1 + sqrt(3)/18 ;  System C gives -1 + sqrt(3)/18 ;  equal: True
    |predicted - observed| at dps 40 : 0

## Two unsound attempts of my own, recorded
    (1) thi symbolic inside the SCALAR reduction, heads read at oo.
        Unsound: deg_z b drops from 1 to 0 at the printed thi, so the
        heads are discontinuous in thi exactly there.  Symptom: the
        symbolic-thi exponents summed to -1, System C's sum to -2 = -P1.
    (2) comparing the gauge-'invariant' difference mu(+) - mu(-) between
        system and scalar.  Unsound: the two branches do NOT share a
        common power of z here -- their shifts are 0 and -2 -- so the
        difference is not invariant.  It returned thi = sqrt(3)/9, i.e.
        it was wrong by exactly the shift, 2.
    Both are discarded; neither is used above.

## Controls that can fail

    control_sensitive: fires (PASS=False) if the system-side exponent did
      not depend on TH, making the test unable to tell any thi from any
      other.  PASS = True
    control_discriminates: fires (PASS=False) if the same test also
      accepted thi + 1.  PASS = True   (residual 1/2)

## Verdict
    thi as printed in SS3 is consistent with System C's local data at
    infinity: True

