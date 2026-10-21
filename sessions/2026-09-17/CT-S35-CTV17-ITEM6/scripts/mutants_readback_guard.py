# Controls for the stale-description guard in postpublish_readback.py.
#
# The defect these exist for: postpublish_readback.py and selftest_readback.py
# were copied forward from CT-S27 still pointing at DESCRIPTION-v1.7-rev2.html,
# and WALKTHROUGH.md sections 2 and 4 still told the operator to cd into
# CT-S27-CTV17-DEPOSIT-PREP.  Followed literally, the post-publish readback
# would have compared the LIVE v1.7 record against the revision WITHOUT the
# sixth item.
#
# That is the failure mode worth a control: not "the check fails" but "the
# check compares the wrong artefact and is believed".  The guard resolves the
# expected digest from the gate run's own output rather than from a constant,
# and aborts before any network call.
#
# Both arms mutate the INPUT PATH, not the prose -- the class of defect mutant
# testing of the check's logic cannot reach.

import io
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
P = os.path.join(HERE, "postpublish_readback.py")
DESC = os.path.join(ROOT, "DESCRIPTION-v1.7-rev3.html")

OLD = 'DESC = os.path.join(SESSION, "DESCRIPTION-v1.7-rev3.html")'


def main():
    src = io.open(P, encoding="utf-8").read()

    # Reader integrity before evaluating any absence.
    assert "_guard_description_is_gate_verified" in src, \
        "reader integrity: readback source not read"
    assert OLD in src, "SETUP-FAIL: mutation site absent"

    stale = os.path.join(os.environ.get("TEMP", "/tmp"), "s35_stale.html")
    shutil.copyfile(DESC, stale)
    with io.open(stale, "a", encoding="utf-8") as fh:
        fh.write("<p>stale</p>")

    arms = [
        ("A1 description is not the gate-verified revision",
         'DESC = r"%s"' % stale),
        ("A2 description does not exist at all",
         'DESC = r"%s"' % (stale + ".nope")),
    ]

    caught = 0
    mut = P + ".mut"
    try:
        for name, new in arms:
            io.open(mut, "w", encoding="utf-8", newline="").write(
                src.replace(OLD, new, 1))
            p = subprocess.run([sys.executable, mut, "99999999"],
                               capture_output=True, text=True)
            out = ((p.stdout or "") + (p.stderr or "")).strip().splitlines()
            broke = any(("SyntaxError" in l or "NameError" in l) for l in out)
            fired = (p.returncode != 0
                     and any("ABORT" in l for l in out)
                     and not broke)
            print("%-48s %s  rc=%d" % (name, "CAUGHT" if fired else "MISSED",
                                       p.returncode))
            print("    %s" % (out[0] if out else "<no output>"))
            if fired:
                caught += 1
    finally:
        if os.path.exists(mut):
            os.remove(mut)
        if os.path.exists(stale):
            os.remove(stale)

    print("")
    print("%d/%d arms caught, each aborting before any network call"
          % (caught, len(arms)))
    assert caught == len(arms), "a stale-description arm was accepted"
    return 0


if __name__ == "__main__":
    sys.exit(main())
