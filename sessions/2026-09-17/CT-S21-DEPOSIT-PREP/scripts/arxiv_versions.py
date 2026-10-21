# -*- coding: utf-8 -*-
"""Record which arXiv VERSION each refs/ PDF corresponds to.

arXiv licences are per-submission AND per-version, so 'CC-BY-4.0' without a
version identifier is not a licence determination for the file on disk. An
unversioned /pdf/ URL resolves to the latest version at fetch time.
"""
import json
import os
import re
import urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDS = ['2204.09305', '2306.05930']

out = {}
for aid in IDS:
    url = ('http://export.arxiv.org/api/query?id_list=%s&max_results=1' % aid)
    req = urllib.request.Request(url, headers={
        'User-Agent': 'siarc-relay-bridge/CT-S21 (refs licence+version audit)'})
    with urllib.request.urlopen(req, timeout=60) as r:
        xml = r.read().decode('utf-8', 'replace')
    # The <id> element carries the version actually served.
    m = re.search(r'<id>http://arxiv\.org/abs/(' + re.escape(aid) + r'v(\d+))</id>', xml)
    upd = re.search(r'<updated>([^<]+)</updated>', xml)
    pub = re.search(r'<published>([^<]+)</published>', xml)
    ttl = re.search(r'<title>([^<]+)</title>', xml[xml.find('<entry>'):])
    assert m, 'version not parsed for %s' % aid
    out[aid] = {'latest_versioned_id': m.group(1), 'version': int(m.group(2)),
                'published': pub.group(1) if pub else None,
                'updated': upd.group(1) if upd else None,
                'title': re.sub(r'\s+', ' ', ttl.group(1)).strip() if ttl else None}
    print('%s -> %s  (v%s)  updated %s' % (aid, m.group(1), m.group(2),
                                           out[aid]['updated']))
    print('    title:', out[aid]['title'])

p = os.path.join(HERE, 'outputs', 'arxiv_versions.json')
json.dump(out, open(p, 'w', encoding='utf-8'), indent=1)
back = json.load(open(p, encoding='utf-8'))
assert back == out, 'READBACK MISMATCH'
print('readback OK ->', p)
