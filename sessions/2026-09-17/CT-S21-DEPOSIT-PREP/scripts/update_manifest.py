# -*- coding: utf-8 -*-
"""CT-S21 item 1/3 - write the re-fetch and licence results into REFS-MANIFEST.md.

The existing 69-row census is not rewritten. A keyed section is appended instead:
rewriting a table of hashes to add four columns risks corrupting rows that are
themselves the evidence. Rows not named below remain NOT CHECKED, which is what
the census already says.
"""
import json
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESS = os.path.dirname(HERE)
MAN = os.path.join(SESS, 'CT-R1-AUDIT', 'REFS-MANIFEST.md')
ref = json.load(open(os.path.join(HERE, 'outputs', 'item1_refetch.json'), encoding='utf-8'))
res = json.load(open(os.path.join(HERE, 'outputs', 'item1b_resolve.json'), encoding='utf-8'))
lic = json.load(open(os.path.join(HERE, 'outputs', 'item3_licences.json'), encoding='utf-8'))

MARK = '## CT-S21 deposit-day pass'
before = open(MAN, encoding='utf-8').read()
assert MARK not in before, 'section already present'

L = ['', MARK + ' - re-fetch, %s' % ref['retrieved'], '',
     'Every external source the v1.3 notice cites was re-fetched on this date to a',
     'temp directory **outside the repository**: a re-fetch is a verification, not an',
     'acquisition, and copying more third-party bytes into the tree would enlarge the',
     'population under the licence hold.', '',
     '| source | URL | retrieved | bytes | sha256 | matches local copy |',
     '|---|---|---|---|---|---|']
for s in ref['sources']:
    L.append('| %s | `%s` | %s | %s | `%s` | %s |' % (
        s['cite'], s['url'], s['retrieved'], s.get('bytes', '-'),
        s.get('sha256', '-'),
        {True: '**yes, byte-identical**', False: 'no', None: 'n/a'}.get(s.get('matches_local'), 'n/a')))

z = res['zenodo']
d = res['dlmf']
L += ['', '### Companion v1.2 - the record, not just the file', '',
      '| field | value |', '|---|---|',
      '| record id | `%s` |' % z['record_id'],
      '| **version** DOI | `%s` |' % z['doi_version'],
      '| **concept** DOI | `%s` |' % z['conceptdoi'],
      '| `metadata.version` | `%s` |' % z['version_field'],
      '| publication date | %s |' % z['publication_date'],
      '| file | `%s`, %s bytes |' % (z['files'][0]['key'], z['files'][0]['size']),
      '| Zenodo checksum | `%s` |' % z['files'][0]['checksum'],
      '| local md5 | `%s` |' % z['local_md5'],
      '| PDF re-fetched | `%s` |' % z.get('pdf_url', '-'),
      '| PDF sha256 | `%s` |' % z.get('pdf_sha256', '-'),
      '| **byte-identical to the local copy** | **%s** |' % z.get('pdf_matches_local'),
      '',
      'The concept DOI is **not** the version DOI and the two differ here. Any citation',
      'of the exact text the notice corrects must use the **version** DOI',
      '`%s`; the concept DOI resolves to whatever is newest.' % z['doi_version'], '',
      '### DLMF - a URL is not a citation', '',
      '| field | value |', '|---|---|',
      '| section | %s |' % d['url'],
      '| page title | %s |' % d['title'],
      '| **version** | **%s** |' % (d['version_raw'] or 'NOT FOUND'),
      '| **release date** | **%s** |' % d['release_date'],
      '| sha256 of the page as served | `%s` |' % d['sha256'],
      '',
      'v1.2 cites DLMF **section 32.2** and, for the PV->PIII degeneration, **32.2(vi),',
      'Eq. 32.2.33**; both were read on the page image of v1.2 p. 6. The DLMF is a',
      'living document, so the version and release date above must travel with the',
      'citation.', '',
      '### Licences - as printed on the source, or NOT CHECKED', '',
      '| target | source read | licence as printed |', '|---|---|---|']
for r in lic['rows']:
    L.append('| %s | `%s` | %s |' % (r['target'], r['source_url'],
                                     r['licence_as_printed']))
L += ['',
      '**The arXiv row is the consequential one.** The abstract page for',
      '`arXiv:0902.1702` carries `http://arxiv.org/licenses/nonexclusive-distrib/1.0/`',
      '- arXiv\'s **default** licence, which grants arXiv the right to distribute and',
      'grants third parties **no redistribution right at all**. The arXiv PDF therefore',
      'may not be committed or deposited. Quoting from it is a separate question that',
      'this row does not decide.', '',
      '**Not cleared, and not guessed:** the Annales de l\'Institut Fourier item page',
      'carries no Creative Commons string, and the journal PDF title page prints',
      '*tous droits reserves*; the EMS Press article page for Jimbo could not be read',
      '(HTTP failure), so that row stays **NOT CHECKED**. Every other row of the',
      '69-file census above is untouched by this pass and remains **NOT CHECKED**.', '']

with open(MAN, 'a', encoding='utf-8') as f:
    f.write('\n'.join(L) + '\n')

back = open(MAN, encoding='utf-8').read()
assert MARK in back, 'readback: section missing'
for probe in ('nonexclusive-distrib', z['doi_version'], z['conceptdoi'],
              str(d['release_date'])):
    assert probe in back, 'readback: missing %r' % probe
print('REFS-MANIFEST.md %d -> %d lines' % (before.count('\n'), back.count('\n')))
print('READBACK OK')
