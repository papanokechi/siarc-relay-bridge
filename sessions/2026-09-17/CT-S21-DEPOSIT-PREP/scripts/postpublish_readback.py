# -*- coding: utf-8 -*-
"""Read the published v1.3 record back from the API and check it.

Usage:  python scripts\\postpublish_readback.py <NEW_RECORD_ID>

Checks only things that were decided before publication, so it cannot be
tuned to agree with whatever happened.
"""
import hashlib
import io
import json
import os
import subprocess
import sys
import datetime

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, 'outputs')

# Fixed before publication. Do not edit these to match the result.
EXPECT_CONCEPT = '20455089'
EXPECT_VERSION = '1.3'
EXPECT_PDF_MD5 = 'md5:4d1e4d59072cad0db8edc86280af45a1'
EXPECT_PDF_NAME = 'vquad_resurgence.pdf'
EXPECT_NOTICE_NAME = 'vquad_resurgence_v1.3_correction_notice.md'
EXPECT_NOTICE_MD5 = 'md5:aeef03534612b6f4052c0636f8556f45'
EXPECT_NOTICE_SIZE = 35918
PREV_TITLE_SOURCE = os.path.join(OUT, 'predeposit_20481592.json')


def fetch(rec_id):
    dest = os.path.join(OUT, 'postpublish_%s.json' % rec_id)
    cmd = ['curl.exe', '-s', '-H',
           'Accept: application/vnd.inveniordm.v1+json',
           'https://zenodo.org/api/records/%s' % rec_id, '-o', dest]
    subprocess.check_call(cmd)
    return dest


def main():
    if len(sys.argv) < 2:
        print('usage: postpublish_readback.py <NEW_RECORD_ID>')
        return 2
    rec_id = sys.argv[1].strip()
    if rec_id == '20481592':
        print('STOP: that is the v1.2 record id. Use the NEW one.')
        return 2

    path = fetch(rec_id)
    raw = open(path, 'rb').read()
    d = json.loads(raw.decode('utf-8'))
    m = d.get('metadata', {})
    files = (d.get('files', {}).get('entries') or {})

    prev = json.load(io.open(PREV_TITLE_SOURCE, encoding='utf-8'))
    prev_title = prev.get('metadata', {}).get('title')

    checks = []
    concept = d.get('conceptdoi') or (d.get('parent') or {}).get('id')
    checks.append(('concept DOI unchanged', str(concept).endswith(EXPECT_CONCEPT), concept))
    checks.append(('version is 1.3', m.get('version') == EXPECT_VERSION, m.get('version')))
    checks.append(('title byte-identical to v1.2', m.get('title') == prev_title, m.get('title')))
    checks.append(('paper still present', EXPECT_PDF_NAME in files, sorted(files)))
    pdf = files.get(EXPECT_PDF_NAME, {})
    checks.append(('paper md5 unchanged', pdf.get('checksum') == EXPECT_PDF_MD5, pdf.get('checksum')))
    nt = files.get(EXPECT_NOTICE_NAME, {})
    checks.append(('notice present under publishable name', bool(nt), sorted(files)))
    checks.append(('notice md5 matches local', nt.get('checksum') == EXPECT_NOTICE_MD5, nt.get('checksum')))
    checks.append(('notice size matches local', nt.get('size') == EXPECT_NOTICE_SIZE, nt.get('size')))
    checks.append(('no file name contains DRAFT',
                   all('draft' not in k.lower() for k in files), sorted(files)))
    rel = m.get('related_identifiers') or []
    checks.append(('related identifiers: exactly one, unchanged',
                   len(rel) == 1, rel))

    ok = 0
    for name, passed, got in checks:
        print('%-42s %s   %s' % (name, 'OK  ' if passed else 'FAIL', got))
        ok += bool(passed)

    print()
    print('version DOI  : %s' % (d.get('doi') or (d.get('pids', {}).get('doi', {}) or {}).get('identifier')))
    print('record id    : %s' % rec_id)
    print('published    : %s' % m.get('publication_date'))
    print('retrieved    : %s' % datetime.datetime.now().astimezone().isoformat())
    print('output       : %s' % path)
    print('output_hash  : %s' % hashlib.sha256(raw).hexdigest())
    print()
    print('%d of %d checks passed' % (ok, len(checks)))
    if ok != len(checks):
        print('A FAIL after publication is a recorded finding, not something to fix silently.')
    return 0 if ok == len(checks) else 1


if __name__ == '__main__':
    sys.exit(main())
