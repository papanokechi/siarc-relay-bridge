#!/usr/bin/env python
"""Deterministic, cross-platform packaging of the V_quad reproducibility bundle.

Kept in the slot root as an auditable build artifact (not shipped inside the
bundle). Produces ``vquad-periodrep-bundle.zip`` in the slot root with:

  * forward-slash entry names (portable: Linux / macOS / Zenodo unzip cleanly),
  * a single top-level directory ``vquad-periodrep-bundle/`` (tidy extraction),
  * entries sorted lexicographically (stable ordering),
  * __pycache__, *.pyc and LaTeX aux files excluded.

Then prints SHA-256, total size, file count and the directory listing.
"""
import hashlib
import os
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "vquad-periodrep-bundle")
TOP = "vquad-periodrep-bundle"
OUT = os.path.join(HERE, "vquad-periodrep-bundle.zip")

EXCLUDE_DIRS = {"__pycache__"}
EXCLUDE_EXT = {".pyc", ".aux", ".log", ".out", ".toc", ".synctex.gz", ".fls",
               ".fdb_latexmk"}

# collect files
entries = []
for root, dirs, files in os.walk(SRC):
    dirs[:] = sorted(d for d in dirs if d not in EXCLUDE_DIRS)
    for fn in sorted(files):
        ext = os.path.splitext(fn)[1].lower()
        if ext in EXCLUDE_EXT:
            continue
        full = os.path.join(root, fn)
        rel = os.path.relpath(full, SRC).replace(os.sep, "/")
        entries.append((f"{TOP}/{rel}", full))

entries.sort(key=lambda e: e[0])

if os.path.exists(OUT):
    os.remove(OUT)

with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as z:
    for arc, full in entries:
        z.write(full, arc)

sha = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
size = os.path.getsize(OUT)

print(f"ARCHIVE = {OUT}")
print(f"SHA256  = {sha}")
print(f"SIZE    = {size} bytes ({size/1024:.1f} KiB)")
print(f"FILES   = {len(entries)}")
print("LISTING:")
for arc, _ in entries:
    print("  ", arc)
