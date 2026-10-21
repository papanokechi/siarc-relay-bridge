"""CT-S22 - smoke test of the continuation machinery against a CLOSED FORM.

Euler system  Y' = (M/z) Y  with constant M has the exact solution
Y(z) = exp(M log z), so the counterclockwise monodromy about z = 0 is exactly
exp(2 pi i M).  This tests, together:
  * poly_shift / taylor_block recurrence,
  * the step-size control,
  * the CONTINUOUS tracking of log z around a full turn.

Every check is an assert.  A test that cannot fail is not a test (CT-S16 S16-11).
"""
import hashlib
import pathlib
import sys

import mpmath as mp

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import solver as S  # noqa: E402

mp.mp.dps = 60

M = mp.matrix([[mp.mpf(1) / 3, mp.mpf(2) / 7],
               [-mp.mpf(5) / 11, mp.mpf(1) / 5 + mp.mpc(0, 1) / 4]])
nmat = [M]              # N(z) = M
dpol = [mp.mpf(0), mp.mpf(1)]   # D(z) = z

exact = mp.expm(2 * mp.pi * mp.mpc(0, 1) * M)
print("exact monodromy exp(2 pi i M):")
for r in range(2):
    print("   ", mp.nstr(exact[r, 0], 25), mp.nstr(exact[r, 1], 25))

for hf in (4, 8):
    cont = S.Continuer(nmat, dpol, sings=[mp.mpf(0)], h_factor=hf)
    z0 = mp.mpf(1)
    logz = mp.mpf(0)
    Y0 = mp.expm(M * logz)          # = I
    Y, z, logz = cont.arc(Y0, z0, 2 * mp.pi, logz)
    assert abs(z - z0) < mp.mpf(10) ** -40, f"did not return to base point: {z}"
    Mnum = Y0 ** -1 * Y
    err = max(abs(Mnum[i, j] - exact[i, j]) for i in range(2) for j in range(2))
    print(f"\nh_factor={hf}  steps={cont.steps}  order={cont.order}")
    print(f"  log z after one ccw turn = {mp.nstr(logz, 25)}   "
          f"(exact 2 pi i = {mp.nstr(2 * mp.pi * mp.mpc(0, 1), 25)})")
    print(f"  max |M_num - exp(2 pi i M)| = {mp.nstr(err, 6)}")
    assert abs(logz - 2 * mp.pi * mp.mpc(0, 1)) < mp.mpf(10) ** -45, \
        "continuous log tracking failed"
    assert err < mp.mpf(10) ** -45, f"monodromy error {err} above 1e-45"

# --- the test must be able to FAIL: a deliberately wrong exact value ---------
bad = mp.expm(2 * mp.pi * mp.mpc(0, 1) * M * mp.mpf("1.000000000001"))
errbad = max(abs(bad[i, j] - exact[i, j]) for i in range(2) for j in range(2))
print(f"\ndiscrimination check: a 1e-12 relative change in M moves the target by "
      f"{mp.nstr(errbad, 6)}")
assert errbad > mp.mpf(10) ** -14, "the comparison cannot discriminate"

print("\nSMOKE TEST PASSED")
out = pathlib.Path(__file__).resolve().parents[1] / "outputs" / "test_solver.out.txt"
print("(this file is hashed by the runner)")
