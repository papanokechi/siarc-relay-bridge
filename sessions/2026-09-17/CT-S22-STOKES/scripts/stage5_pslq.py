"""CT-S22-STOKES Stage 5 - closed-form recognition for S_{zeta*}.

Governed by PREREG-STAGE5.md, written before this script.  Nothing here may
relax a bound stated there; if a bound is ill-posed that is a finding.

NAMING PROHIBITION (PREREG.md section 7, PREREG-STAGE5.md section 0):
    K        is the amplitude at xi_0 = 2/sqrt(3).          NOT COMPUTED HERE.
    S_zeta   is the Stokes constant at zeta* = 2 xi_0 = 4/sqrt(3).  <- this file
They are a factor of 2 apart in the action and are never interchanged.

Stage 5 does NOT recompute S_{zeta*}.  It reads the stored value from the
2026-05-02 fire (read-only) and asks the deferred question: is there a closed
form inside the search space fixed in PREREG-STAGE5.md section 3?
"""
import hashlib
import os
import pathlib
import re

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
SESS = HERE.parent
ROOT = SESS.parent.parent                      # .../sessions
SRC = (ROOT / "2026-05-02" / "CC-MEDIAN-RESURGENCE-EXECUTE" /
       "S_zeta_star_digits.txt")
SRC2 = (ROOT / "2026-05-13" /
        "T2-EXECUTOR-CC-MEDIAN-RESURGENCE-REPRODUCIBILITY-VERIFY" /
        "S_zeta_star_digits.txt")

D_TRUST = 100          # PREREG-STAGE5 section 2.  Not raised, not lowered.
MAXCOEFF = 10 ** 6     # section 3.1
MAXM = 12              # section 3.1
WORK_DPS = 120         # section 3.1
COST_LIMIT = 40        # section 3.2  = 0.40 * D_TRUST

OUT = []


def say(s=""):
    print(s)
    OUT.append(s)


def read_C(path):
    """Read the stored C.  Read from file, never retyped (PREREG-S5 section 8)."""
    txt = path.read_text(encoding="utf-8")
    m = re.search(r"^#\s*C \(alien amplitude\)\s*=\s*([0-9.]+)\s*$",
                  txt, re.M)
    assert m, f"could not read C from {path}"
    return m.group(1)


def basis(val):
    """The 7-vector of PREREG-STAGE5 section 3.  Fixed; nothing may be added."""
    return [mp.log(val), mp.log(2), mp.log(3), mp.log(mp.pi),
            mp.log(mp.gamma(mp.mpf(1) / 3)), mp.log(mp.gamma(mp.mpf(1) / 6)),
            mp.mpf(1)]


NAMES = ["log C", "log 2", "log 3", "log pi", "log G(1/3)", "log G(1/6)", "1"]


def cost_of(rel):
    n = sum(1 for c in rel if c != 0)
    h = max(abs(c) for c in rel)
    return n * mp.log10(max(h, 1)), n, h


def fmt(rel):
    return " + ".join(f"{c}*{NAMES[i]}" for i, c in enumerate(rel) if c != 0)


def search(val, label, dtrust=D_TRUST):
    """Run PSLQ over a ladder of coefficient bounds.

    Returns (accepted_relation_or_None, best_rejected_cost, log_lines).
    The ladder exists so that a NEGATIVE result can report the smallest digit
    cost achieved by any rejected candidate, as PREREG-STAGE5 section 5 requires.
    """
    mp.mp.dps = WORK_DPS
    v = basis(val)
    tol = mp.mpf(10) ** (-(dtrust - 5))
    best_rej = None
    accepted = None
    lines = []
    for mc in (10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, MAXCOEFF):
        try:
            rel = mp.pslq(v, tol=tol, maxcoeff=mc, maxsteps=20000)
        except Exception as exc:                      # noqa: BLE001
            lines.append(f"    maxcoeff {mc:>8}: pslq raised {exc!r}")
            continue
        if rel is None:
            lines.append(f"    maxcoeff {mc:>8}: no relation")
            continue
        c, n, h = cost_of(rel)
        m = rel[0]
        ok_m = m != 0 and abs(m) <= MAXM
        ok_c = c <= COST_LIMIT
        verdict = ("ACCEPT" if (ok_m and ok_c) else
                   f"reject({'m' if not ok_m else ''}{'cost' if not ok_c else ''})")
        lines.append(f"    maxcoeff {mc:>8}: n={n} h={h} cost={mp.nstr(c,5)} "
                     f"{verdict}   {fmt(rel)}")
        if ok_m and ok_c:
            accepted = accepted or rel
        else:
            best_rej = c if best_rej is None else min(best_rej, c)
    return accepted, best_rej, lines


def reconstruct(rel, val):
    """PREREG-STAGE5 section 4.4 - independent evaluation at dps 150."""
    mp.mp.dps = 150
    v = basis(val)
    resid = sum(mp.mpf(rel[i]) * v[i] for i in range(len(rel)))
    return abs(resid)


def main():
    say("=" * 74)
    say("CT-S22-STOKES  STAGE 5 - closed-form recognition for S_{zeta*}")
    say("=" * 74)
    say("NAMING: K is the amplitude at xi_0.  S_{zeta*} is at 2 xi_0.")
    say("        K is NOT computed, fitted or mentioned as a result here.")
    say("")

    # ---- the input, read from the stored fire ------------------------------
    assert SRC.exists(), f"missing stored fire: {SRC}"
    cs1 = read_C(SRC)
    say(f"read C from {SRC}")
    if SRC2.exists():
        cs2 = read_C(SRC2)
        agree = sum(1 for a, b in zip(cs1, cs2) if a == b)
        say(f"cross-check copy {SRC2.name} agrees on first {agree} characters")
        assert cs1[:D_TRUST + 2] == cs2[:D_TRUST + 2], (
            "HALT (PREREG-S5 section 7): the two stored copies of C disagree "
            "within D_trust")
    else:
        say("  (no second copy found)")

    mp.mp.dps = WORK_DPS
    C = mp.mpf(cs1[:D_TRUST + 2])          # '8.' + D_TRUST digits
    say(f"D_trust = {D_TRUST} digits (deliberately below the fire's 108.39)")
    say(f"C  = {mp.nstr(C, 40)} ...")
    say(f"S_{{zeta*}} = 2 pi i C = {mp.nstr(2*mp.pi*C, 40)} i")
    say(f"zeta* = 4/sqrt(3) = {mp.nstr(4/mp.sqrt(3), 30)}")
    say("normalisation: V_quad NATIVE, 'leading B[Phi]=1' (stored fire's words).")
    say("A closed form found here is a closed form OF THAT NUMBER IN THAT")
    say("NORMALISATION and of nothing else; the V_quad -> P-III(D6) map is OPEN")
    say("and no comparison with Stages 1-4 of this session is licensed.")
    say("")
    say(f"search space (fixed, 7 long): {', '.join(NAMES)}")
    say(f"bounds: |coeff| <= {MAXCOEFF}, |m| <= {MAXM}, cost <= {COST_LIMIT}")
    say("")

    # ---- section 6: VACUITY PRE-CHECK, before the real search --------------
    say("-" * 74)
    say("VACUITY PRE-CHECK (PREREG-STAGE5 section 6) - runs BEFORE the search")
    say("-" * 74)
    mp.mp.dps = WORK_DPS
    pistr = mp.nstr(mp.pi, D_TRUST + 20, strip_zeros=False).split(".")[1]
    decoys = {
        "C*(1+1e-30)": C * (1 + mp.mpf(10) ** -30),
        "8.1|pi-digits": mp.mpf("8.1" + pistr[:D_TRUST]),
        "C + 1/7": C + mp.mpf(1) / 7,
    }
    fired = []
    for name, val in decoys.items():
        acc, rej, lines = search(val, name)
        say(f"  decoy {name}:")
        for l in lines:
            say(l)
        if acc is not None:
            fired.append(name)
            say(f"    *** DECOY ACCEPTED - the space fits arbitrary numbers")
        else:
            say(f"    rejected (best rejected cost "
                f"{'n/a' if rej is None else mp.nstr(rej,5)})")

    ctrl = 4 * mp.pi ** 2 / (3 * mp.gamma(mp.mpf(1) / 3))
    say(f"  positive control  C_k = 4 pi^2 / (3 Gamma(1/3)) = {mp.nstr(ctrl,25)}")
    acc_k, rej_k, lines_k = search(ctrl, "control")
    for l in lines_k:
        say(l)
    ctrl_ok = acc_k is not None
    say(f"    control {'ACCEPTED (pipeline recognises a known form)' if ctrl_ok else '*** NOT RECOGNISED - pipeline broken'}")

    say("")
    say(f"  pre-check result: {len(fired)} decoys accepted (need 0), "
        f"control {'accepted' if ctrl_ok else 'rejected'} (need accepted)")
    if fired or not ctrl_ok:
        say("  *** VACUITY PRE-CHECK FIRES.  PREREG-STAGE5 section 7: Stage 5 is")
        say("      VOID.  Halting before the real search, and reporting.")
        return False, None
    say("  [PASS] 3 decoys rejected, 1 control accepted.  The search may run.")

    # ---- the real search ---------------------------------------------------
    say("")
    say("-" * 74)
    say("THE SEARCH (PREREG-STAGE5 sections 3-4)")
    say("-" * 74)
    acc, rej, lines = search(C, "C")
    for l in lines:
        say(l)

    if acc is None:
        say("")
        say("  RESULT: NOT FOUND.")
        say("  No multiplicative relation")
        say("      C = +/- 2^a 3^b pi^c Gamma(1/3)^d Gamma(1/6)^e e^f")
        say(f"  exists with all coefficients bounded by {MAXCOEFF}, |m| <= {MAXM},")
        say(f"  and digit cost <= {COST_LIMIT}, against C known to {D_TRUST}")
        say("  decimal digits.")
        say(f"  smallest digit cost achieved by any rejected candidate: "
            f"{'none returned' if rej is None else mp.nstr(rej,6)}")
        say("  SCOPE: this EXCLUDES THAT SPACE.  It is NOT evidence that C has")
        say("  no closed form.  It says nothing about spaces containing other")
        say("  gamma values, other algebraic irrationalities, polylogarithms,")
        say("  or zeta(3).")
        say("  LABEL: VERIFIED (a verified statement about a search).")
        return True, None

    # stability + reconstruction, PREREG-STAGE5 section 4.3 / 4.4
    say("")
    say(f"  candidate relation: {fmt(acc)}")
    c, n, h = cost_of(acc)
    say(f"  n={n} h={h} cost={mp.nstr(c,6)} (limit {COST_LIMIT})")
    stable = True
    for dt in (90, 80):
        mp.mp.dps = WORK_DPS
        Ct = mp.mpf(cs1[:dt + 2])
        a2, _, _ = search(Ct, f"C@{dt}", dtrust=dt)
        same = (a2 == acc)
        stable = stable and same
        say(f"  stability at {dt} digits: {'SAME' if same else 'DIFFERENT -> artefact'}")
    resid = reconstruct(acc, C)
    rdig = mp.inf if resid == 0 else -mp.log10(resid)
    say(f"  reconstruction residual at dps 150: {mp.nstr(resid,6)} "
        f"({mp.nstr(rdig,6)} digits, need >= 95)")
    good = stable and rdig >= 95 and c <= COST_LIMIT
    say("")
    say(f"  RESULT: {'ACCEPTED' if good else 'NOT ACCEPTED'} - "
        f"{'closed form recognised' if good else 'fails a section-4 criterion'}")
    say("  LABEL: VERIFIED, not PROVEN.  A PSLQ hit is not a derivation.")
    return True, (acc if good else None)


if __name__ == "__main__":
    ran, rel = main()
    outp = SESS / "outputs" / "stage5_pslq.out.txt"
    outp.parent.mkdir(exist_ok=True)
    outp.write_text("\n".join(OUT) + "\n", encoding="utf-8")
    back = outp.read_text(encoding="utf-8")          # read back what was written
    assert back.splitlines() == OUT, "read-back mismatch"
    h = hashlib.sha256(back.encode("utf-8")).hexdigest()
    print(f"\nwritten {outp}  sha256 {h}")
