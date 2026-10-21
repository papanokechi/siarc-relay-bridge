"""Stage the carried-over v1.2 paper under its published filename and verify it.

Abort condition 4 of DEPOSIT-WALKTHROUGH.md requires the v1.2 paper to be
present in the v1.3 file list. The operator's draft showed the notice alone, so
a locally held byte-identical copy is staged here under the exact filename the
live record publishes, because Zenodo publishes the filename it is given.

Read-only with respect to earlier sessions: the source is copied, never touched.
"""

import hashlib
import json
import pathlib
import shutil

SESSION = pathlib.Path(__file__).resolve().parents[1]
SRC = (
    SESSION.parents[0]
    / "CT-R1-AUDIT"
    / "refs"
    / "vquad_resurgence_v1.2_zenodo-20481592.pdf"
)
DST = SESSION / "upload" / "vquad_resurgence.pdf"
RECORD = SESSION / "outputs" / "predeposit_20481592.json"
PUBLISHED_NAME = "vquad_resurgence.pdf"


def digests(path):
    data = path.read_bytes()
    return (
        len(data),
        hashlib.md5(data).hexdigest(),
        hashlib.sha256(data).hexdigest(),
    )


def main():
    if not SRC.is_file():
        raise SystemExit("HALT: held v1.2 copy not found at %s" % SRC)

    entry = json.loads(RECORD.read_text(encoding="utf-8"))["files"]["entries"][
        PUBLISHED_NAME
    ]
    want_md5 = entry["checksum"].split(":", 1)[1].lower()
    want_size = entry["size"]

    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)

    size, md5, sha256 = digests(DST)

    checks = [
        ("name matches the published key", DST.name == PUBLISHED_NAME),
        ("no DRAFT marker in filename", "draft" not in DST.name.lower()),
        ("size matches the live record", size == want_size),
        ("md5 matches the live record", md5 == want_md5),
        ("source and staged copy identical", digests(SRC)[2] == sha256),
    ]

    print("staged: %s" % DST)
    print("bytes : %d (record: %d)" % (size, want_size))
    print("md5   : %s (record: %s)" % (md5, want_md5))
    print("sha256: %s" % sha256)
    print()
    for label, ok in checks:
        print("[%s] %s" % ("OK" if ok else "FAIL", label))

    if not all(ok for _, ok in checks):
        raise SystemExit("HALT: staged carry-over does not match the live record")
    print("\nall checks pass; select this file in the Zenodo upload dialog")


if __name__ == "__main__":
    main()
