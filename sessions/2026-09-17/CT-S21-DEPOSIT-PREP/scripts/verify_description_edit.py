"""Verify the S21-73 description edit landed on published record 22831933.

Re-fetches the live description and checks the two staged edits, deriving the
expected strings from DESCRIPTION-EDIT.md rather than restating them. Reports
NOT YET APPLIED rather than failing, so it can be run before or after the edit.
"""
import datetime
import hashlib
import html
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RECID = sys.argv[1] if len(sys.argv) > 1 else "22831933"
assert RECID != "20481592", "that is the v1.2 record, not the version being edited"

out = HERE / "outputs" / f"descedit_{RECID}.json"
# --fixture <path> feeds a locally built record instead of fetching, so the
# post-edit behaviour of these checks can be proven before the edit is applied.
fixture = None
if "--fixture" in sys.argv:
    fixture = pathlib.Path(sys.argv[sys.argv.index("--fixture") + 1])
    RECID = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else RECID
    print(f"[fixture mode] reading {fixture.name}, not fetching")
    rec = json.loads(fixture.read_text(encoding="utf-8"))
    out = fixture  # so the reported hash is of what was actually checked
else:
    subprocess.run(
        ["curl.exe", "-sS", "-H", "Accept: application/vnd.inveniordm.v1+json",
         f"https://zenodo.org/api/records/{RECID}", "-o", str(out)], check=True)
    rec = json.loads(out.read_text(encoding="utf-8"))
desc = rec["metadata"]["description"]
paras = [html.unescape(re.sub(r"<.*?>", "", p)).strip()
         for p in re.findall(r"<p>(.*?)</p>", desc, re.S)]

# The expected sentence is read from the staged sheet, not retyped here.
sheet = (HERE / "DESCRIPTION-EDIT.md").read_text(encoding="utf-8")
block = re.search(r"New paragraph after .*?```\n(.*?)```", sheet, re.S)
assert block, "could not locate the staged boundary paragraph in DESCRIPTION-EDIT.md"
expected = " ".join(block.group(1).split())

labelled = re.findall(r"<strong>(Version 1\.[0-9][^<]*)</strong>", desc)
has_v13_label = any(l.startswith("Version 1.3") for l in labelled)
v13_first = bool(re.match(r"\s*<p>\s*<strong>Version 1\.3", desc))

flat = [" ".join(p.split()) for p in paras]
boundary_at = next((i for i, p in enumerate(flat) if p == expected), None)
abstract_at = next((i for i, p in enumerate(flat)
                    if p.startswith("We study the resurgence")), None)

checks = [
    ("v1.3 block carries a bold label", has_v13_label,
     "; ".join(labelled) or "none"),
    ("the label opens the description", v13_first, desc[:60].replace("\n", " ")),
    ("boundary paragraph present verbatim", boundary_at is not None,
     f"index {boundary_at}"),
    ("boundary sits immediately before the abstract",
     boundary_at is not None and abstract_at is not None
     and boundary_at + 1 == abstract_at,
     f"boundary {boundary_at}, abstract {abstract_at}"),
    ("pointer names the target, not an index",
     "item 1 above" not in desc, "no 'item 1 above'"),
    ("abstract retained unedited: both C1 sentences still present",
     sum(("forces both finite singularities to be apparent" in p
          or "apparent singularity positions are the roots" in p)
         and "The abstract below is retained unedited" not in p
         for p in paras) == 2,
     "2 abstract paragraphs expected, excluding the boundary paragraph "
     "which quotes both phrases by design"),
    ("file set untouched", sorted(f["key"] for f in rec["files"]["entries"].values())
     == ["vquad_resurgence.pdf", "vquad_resurgence_v1.3_correction_notice.md"],
     "2 files"),
    ("version DOI unchanged", rec["pids"]["doi"]["identifier"]
     == f"10.5281/zenodo.{RECID}", rec["pids"]["doi"]["identifier"]),
    ("concept DOI unchanged",
     rec["parent"]["pids"]["doi"]["identifier"] == "10.5281/zenodo.20455089",
     rec["parent"]["pids"]["doi"]["identifier"]),
]

npass = 0
for name, ok, detail in checks:
    print(f"{name:<52} {'OK  ' if ok else 'NO  '} {detail}")
    npass += bool(ok)

print()
print(f"retrieved   : {datetime.datetime.now().astimezone().isoformat(timespec='seconds')}")
print(f"output      : {out}")
print(f"output_hash : {hashlib.sha256(out.read_bytes()).hexdigest()}")
print()
if npass == len(checks):
    print(f"{npass} of {len(checks)} checks passed -- EDIT APPLIED")
else:
    print(f"{npass} of {len(checks)} checks passed -- NOT YET APPLIED (or applied differently)")
