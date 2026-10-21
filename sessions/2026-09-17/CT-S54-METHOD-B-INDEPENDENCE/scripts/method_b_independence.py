#!/usr/bin/env python3
"""CT-S54 -- is Method B independent of the Stokes datum?

Re-implements the Method B and Method C numeric blocks of the corpus script
  sessions/2026-06-15/PERIOD-REP-VQUAD-003/scripts/stage4_methods.py
without editing it, and asks the decidable question the paper's prose does not:
does Method B's reported figure depend on S, and is it the same quantity as
Method C's?

Exit codes: 0 clean, 1 finding, 2 refusal, 3 crash.
"""
import hashlib
import pathlib
import sys

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
SESS = HERE.parent
OUT = SESS / "outputs" / "method_b_independence.out.txt"

CORPUS = pathlib.Path(
    r"C:\LocalWork\siarc-relay-bridge\sessions\2026-06-15\PERIOD-REP-VQUAD-003"
)
SCRIPT = CORPUS / "scripts" / "stage4_methods.py"
STAGE14 = CORPUS / "numerical-integral.md"

mp.mp.dps = 120

# Deposited constants, transcribed from stage4_methods.py (verified below).
K_S = "0.0728781025518669641294423633296525128045556892"
S_S = "0.457906623169017636119097842548225837962395135"
C_S = "0.437705286193537221230739749794369589981725597"
# Independently extracted branch amplitude, numerical-integral.md section 2.
A_EXTRACTED_S = "0.084236421603186966754408455245262591552243229339"

_lines = []


def say(s=""):
    print(s)
    _lines.append(s)


def refuse(msg):
    say()
    say("REFUSED: " + msg)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(_lines) + "\n", encoding="utf-8")
    sys.exit(2)


def rels(K, S, C):
    """Return (relB, relC1, relC2) exactly as the corpus script computes them."""
    r3 = mp.sqrt(3)
    xi0 = 2 / r3
    beta = -1 / (3 * r3)
    G1pb = mp.gamma(1 + beta)
    A_amp = K * G1pb                      # the corpus definition: A from K
    hankel = 2 * mp.pi * 1j / G1pb
    lead = A_amp * mp.e ** (-xi0) * hankel
    S_e = S * mp.e ** (-xi0)
    relB = abs(abs(lead) - S_e) / S_e
    S_mult = 2 * mp.pi * 1j * A_amp / G1pb
    relC1 = abs(abs(S_mult) - S) / S
    relC2 = abs(A_amp / abs(beta) - C) / C
    return relB, relC1, relC2


def main():
    say("=" * 74)
    say("CT-S54 -- Method B and the Stokes datum")
    say("=" * 74)
    say("read-only with respect to the corpus; nothing is edited, sent or deposited.")
    say()

    # ---- provenance -------------------------------------------------------
    for p in (SCRIPT, STAGE14):
        if not p.exists():
            refuse(f"corpus artefact missing: {p}")
    say("[provenance]")
    for p in (SCRIPT, STAGE14):
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        say(f"  {p.name:28s} sha256 {h}")

    src = SCRIPT.read_text(encoding="utf-8", errors="replace")
    # The constants must be the ones actually in the corpus script, not my memory.
    for name, lit in (("K", K_S), ("S", S_S), ("C", C_S)):
        if lit not in src:
            refuse(f"constant {name}={lit} does not occur in {SCRIPT.name}; "
                   "transcription is unverified")
    say(f"  all three deposited constants found verbatim in {SCRIPT.name}")

    if A_EXTRACTED_S.replace(".", "")[:40] not in STAGE14.read_text(
            encoding="utf-8", errors="replace").replace(".", "").replace("**", ""):
        refuse("the independently extracted A could not be confirmed in "
               "numerical-integral.md; F4 -- the rescue route is unavailable")
    say("  independently extracted A confirmed in numerical-integral.md section 2")

    # Does Method B's block use the Borel coefficient stream at all?
    b_blk = src.split("METHOD B")[2] if src.count("METHOD B") > 2 else src.split("METHOD B")[-1]
    b_blk = b_blk.split("METHOD C")[0]
    uses_stream = any(t in b_blk for t in ("b_m", "borel_coeffs", "formal_series", "b["))
    say(f"  Method B block references a Borel coefficient stream: {uses_stream}")
    say()

    K = mp.mpf(K_S)
    S = mp.mpf(S_S)
    C = mp.mpf(C_S)

    # ---- OBSERVABLE FIRST (CT-S47 ordering) -------------------------------
    say("[observable] baseline, dps=%d" % mp.mp.dps)
    relB, relC1, relC2 = rels(K, S, C)
    say(f"  O1 relB  (Method B, vs S e^-xi0) = {mp.nstr(relB, 6)}")
    say(f"  O2 relC1 (Method C, |S_mult| vs S) = {mp.nstr(relC1, 6)}")
    say(f"  O3 relC2 (C = |A|/|beta| vs C)     = {mp.nstr(relC2, 6)}")
    gap = abs(relB - relC1)
    say(f"  |O1 - O2| = {mp.nstr(gap, 6)}")
    identical = gap < mp.mpf(10) ** (-mp.mp.dps + 20)
    say(f"  P1: O1 and O2 are the same quantity: {identical}")
    say()

    # ---- perturbation: which observables move with S? ---------------------
    say("[discrimination] perturb S alone by relative 1e-30")
    S2 = S * (1 + mp.mpf(10) ** (-30))
    pB, pC1, pC2 = rels(K, S2, C)
    dB = abs(pB - relB) / relB
    dC1 = abs(pC1 - relC1) / relC1
    dC2 = abs(pC2 - relC2) / relC2 if relC2 != 0 else mp.mpf(0)
    say(f"  O1 relative move = {mp.nstr(dB, 6)}")
    say(f"  O2 relative move = {mp.nstr(dC1, 6)}")
    say(f"  O3 relative move = {mp.nstr(dC2, 6)}   <-- A0: must stay put")
    moved_B = dB > mp.mpf(10) ** (-40)
    moved_C1 = dC1 > mp.mpf(10) ** (-40)
    moved_C2 = dC2 > mp.mpf(10) ** (-40)
    same_move = abs(dB - dC1) < mp.mpf(10) ** (-40)
    say(f"  O1 moved: {moved_B}   O2 moved: {moved_C1}   O3 moved: {moved_C2}")
    say(f"  O1 and O2 moved by the same amount: {same_move}")
    say()

    say("[vacuity pre-check] perturb K alone by relative 1e-30")
    K2 = K * (1 + mp.mpf(10) ** (-30))
    qB, qC1, qC2 = rels(K2, S, C)
    mB = abs(qB - relB) / relB > mp.mpf(10) ** (-40)
    mC1 = abs(qC1 - relC1) / relC1 > mp.mpf(10) ** (-40)
    mC2 = abs(qC2 - relC2) / relC2 > mp.mpf(10) ** (-40)
    say(f"  O1 moved: {mB}   O2 moved: {mC1}   O3 moved: {mC2}")
    say(f"  P3 (K moves all three): {mB and mC1 and mC2}")
    say()

    # ---- O4: Method B rebuilt on the independent amplitude ----------------
    say("[O4] Method B rebuilt on Stage 1.4's independently extracted A")
    r3 = mp.sqrt(3)
    xi0 = 2 / r3
    beta = -1 / (3 * r3)
    G1pb = mp.gamma(1 + beta)
    A_ind = mp.mpf(A_EXTRACTED_S)          # fitted to b_m; never sees S
    lead_ind = A_ind * mp.e ** (-xi0) * (2 * mp.pi * 1j / G1pb)
    S_recon = abs(lead_ind) / mp.e ** (-xi0)
    relB_indep = abs(S_recon - S) / S
    say(f"  A extracted (from b_m)      = {mp.nstr(A_ind, 30)}")
    say(f"  A predicted  = K*Gamma(1+b) = {mp.nstr(K * G1pb, 30)}")
    say(f"  S reconstructed             = {mp.nstr(S_recon, 40)}")
    say(f"  S deposited                 = {mp.nstr(S, 40)}")
    say(f"  O4 relB_indep = {mp.nstr(relB_indep, 6)}")
    distinct = abs(relB_indep - relB) / relB > mp.mpf(10) ** (-3)
    say(f"  P4: O4 is a different figure from O1: {distinct}")
    say()

    # ---- verdict ----------------------------------------------------------
    say("=" * 74)
    fired = []
    if not same_move:
        fired.append("F1 (O1 and O2 move differently -- not the same comparison)")
    if not moved_B:
        fired.append("F2 (O1 insensitive to S -- Method B really is independent)")
    if not distinct:
        fired.append("F3 (O4 reproduces O1 -- the distinction is empty)")
    if moved_C2:
        fired.append("A0 CONTROL BROKEN (O3 moved with S)")

    if fired:
        for f in fired:
            say("FALSIFIER FIRED: " + f)
        say("H is not supported as stated. Halting per P0.")
        rc = 1
    else:
        say("VERDICT")
        say("  Method B, as printed in eq. (26) and as implemented in the cited")
        say("  script, takes its amplitude from the Stokes datum: A = K*Gamma(1+beta),")
        say("  K = S/2pi. Its reported figure is arithmetically the SAME comparison")
        say("  as Method C's first check -- the factor e^-xi0 cancels -- so the two")
        say("  are one numerical fact reported twice, not two agreeing methods.")
        say("  The claim 'independent of the Stokes datum' is therefore an overclaim")
        say("  about the derivation and about the computation.")
        say()
        say("  A genuinely S-independent route EXISTS and was executed in Stage 1.4:")
        say("  A extracted from the coefficient stream by Neville acceleration")
        say(f"  reconstructs S to {mp.nstr(relB_indep, 3)}, a different and honest figure.")
        say("  The repair is therefore a REWORDING plus a corrected figure, not a")
        say("  retraction of Method B.")
        rc = 0
    say("=" * 74)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(_lines) + "\n", encoding="utf-8")
    print("[wrote]", OUT)
    print("[sha256]", hashlib.sha256(OUT.read_bytes()).hexdigest())
    return rc


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:
        print("CRASH:", type(e).__name__, e)
        sys.exit(3)
