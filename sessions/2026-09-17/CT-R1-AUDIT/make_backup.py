"""Off-repo backup of the session tree.

Adds files directly to the zip, so the multi-GB `lean/.lake` build tree is never
copied to a staging directory. The sha256 is written to a separate file beside
the archive, not into it: a hash stored inside the thing it certifies certifies
nothing.
"""
import datetime
import hashlib
import pathlib
import zipfile

SRC = pathlib.Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17")
DST = pathlib.Path(r"C:\LocalWork\_siarc-session-backups")
EXCLUDE_DIRS = {".lake", "__pycache__", ".git"}

DST.mkdir(parents=True, exist_ok=True)
stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
zip_path = DST / f"sessions-2026-09-17_{stamp}.zip"

files, skipped = [], 0
for p in SRC.rglob("*"):
    if any(part in EXCLUDE_DIRS for part in p.relative_to(SRC).parts):
        skipped += 1
        continue
    if p.is_file():
        files.append(p)

print(f"including {len(files)} files; skipped {skipped} excluded paths")

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for p in files:
        z.write(p, pathlib.Path("2026-09-17") / p.relative_to(SRC))

h = hashlib.sha256()
with open(zip_path, "rb") as f:
    for chunk in iter(lambda: f.read(1 << 20), b""):
        h.update(chunk)
digest = h.hexdigest()

side = zip_path.with_suffix(".zip.sha256")
side.write_text(f"{digest}  {zip_path.name}\n", encoding="ascii")

print(f"zip:    {zip_path}")
print(f"size:   {zip_path.stat().st_size / 1e6:.1f} MB")
print(f"sha256: {digest}")
print(f"stored: {side}  (outside the archive)")
