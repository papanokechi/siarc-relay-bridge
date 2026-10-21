# -*- coding: utf-8 -*-
"""Print exactly what you must see in the Zenodo upload dialog.

Run this immediately before selecting the file, and compare against the values
Zenodo shows you AFTER the upload completes. Do not compare against any hash
quoted in a chat log, a handoff document, or this script's own history: the
rule that survived this workflow is that you verify the bytes on disk now.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = os.path.join(HERE, 'upload', 'vquad_resurgence_v1.3_correction_notice.md')

def digest(path):
    h = hashlib.sha256()
    m = hashlib.md5()
    n = 0
    with open(path, 'rb') as f:
        while True:
            b = f.read(1 << 20)
            if not b:
                break
            h.update(b)
            m.update(b)
            n += len(b)
    return h.hexdigest(), m.hexdigest(), n

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else TARGET
    if not os.path.exists(path):
        print('MISSING: %s' % path)
        return 1
    sha, md5, n = digest(path)
    print('file to select in the dialog')
    print('  path      %s' % path)
    print('  filename  %s   <- this is what Zenodo publishes' % os.path.basename(path))
    print('  bytes     %d' % n)
    print('  sha256    %s' % sha)
    print('  md5       %s   <- Zenodo shows md5 next to the uploaded file' % md5)
    print()
    print('checks, in order:')
    print('  1. the filename above contains no "DRAFT"      -> %s'
          % ('OK' if 'draft' not in os.path.basename(path).lower() else 'STOP'))
    print('  2. the md5 above equals the one Zenodo lists after upload')
    print('  3. the byte count above equals the size Zenodo lists')
    print('  4. vquad_resurgence.pdf is STILL in the file list (md5 4d1e4d59072cad0db8edc86280af45a1)')
    return 0

if __name__ == '__main__':
    sys.exit(main())
