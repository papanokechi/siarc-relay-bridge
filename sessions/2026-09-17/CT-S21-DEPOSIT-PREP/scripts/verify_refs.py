# -*- coding: utf-8 -*-
"""Verify the operator-supplied identifiers before recording them.

Read-only. Nothing is downloaded into the repository: arXiv licences are
per-submission and the refs/ hold is still in force, so acquisition is deferred
to the v1.7 stage with a per-row licence check.
"""
import json
import re
import urllib.request

UA = {'User-Agent': 'curl/8 (verification only)'}


def get(url, accept=None):
    h = dict(UA)
    if accept:
        h['Accept'] = accept
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.status, r.read().decode('utf-8', 'replace')


out = {'arxiv': {}, 'doi': {}}

for aid in ('2204.09305', '2306.05930'):
    try:
        st, x = get('http://export.arxiv.org/api/query?id_list=' + aid)
    except Exception as e:
        out['arxiv'][aid] = {'error': str(e)}
        print(aid, 'FETCH FAILED', e)
        continue
    ent = x.split('<entry>')[-1]

    def g(tag, e=ent):
        m = re.search(r'<' + tag + r'>(.*?)</' + tag + r'>', e, re.S)
        return re.sub(r'\s+', ' ', m.group(1)).strip() if m else None

    rec = {
        'http': st,
        'title': g('title'),
        'authors': re.findall(r'<name>(.*?)</name>', ent),
        'published': g('published'),
        'updated': g('updated'),
        'doi': g('arxiv:doi'),
        'journal_ref': g('arxiv:journal_ref'),
        'abs_url': 'https://arxiv.org/abs/' + aid,
    }
    out['arxiv'][aid] = rec
    print('=== arXiv:%s  (HTTP %s)' % (aid, st))
    print('  title  :', rec['title'])
    print('  authors:', '; '.join(rec['authors'])[:150])
    print('  publish:', rec['published'], '| updated:', rec['updated'])
    print('  jref   :', rec['journal_ref'], '| doi:', rec['doi'])

    # licence, as printed on the abstract page - the CT-S21 lesson
    try:
        st2, page = get(rec['abs_url'])
        lic = re.findall(r'(http://arxiv\.org/licenses/[^\s"\'<>]+|'
                         r'https?://creativecommons\.org/licenses/[^\s"\'<>]+)', page)
        rec['licence_as_printed'] = sorted(set(lic)) or ['NOT FOUND']
    except Exception as e:
        rec['licence_as_printed'] = ['NOT CHECKED: %s' % e]
    print('  licence:', rec['licence_as_printed'])

DOI = '10.1002/sapm1992874289'
try:
    st, body = get('https://doi.org/' + DOI,
                   'application/vnd.citationstyles.csl+json')
    d = json.loads(body)
    out['doi'][DOI] = {
        'http': st,
        'title': d.get('title'),
        'container': d.get('container-title'),
        'volume': d.get('volume'), 'issue': d.get('issue'),
        'page': d.get('page'),
        'issued': d.get('issued'),
        'author': ['%s %s' % (a.get('given', ''), a.get('family', '')) for a in d.get('author', [])],
    }
    r = out['doi'][DOI]
    print('=== DOI', DOI, '(HTTP %s)' % st)
    print('  title    :', r['title'])
    print('  container:', r['container'], r['volume'], '(%s)' % r['issue'], r['page'])
    print('  authors  :', '; '.join(r['author']))
    print('  issued   :', r['issued'])
except Exception as e:
    out['doi'][DOI] = {'error': str(e)}
    print('DOI', DOI, 'FETCH FAILED', e)

with open('outputs/refs_verify.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
back = json.load(open('outputs/refs_verify.json', encoding='utf-8'))
assert back == out, 'readback mismatch'
print('\nwrote outputs/refs_verify.json')
print('READBACK OK')
