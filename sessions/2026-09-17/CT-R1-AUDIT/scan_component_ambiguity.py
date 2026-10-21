import json, pathlib, re

root = pathlib.Path(r'C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17')

# Claims that COMPARE or IDENTIFY scalar operators / normal forms are the ones
# exposed to the component ambiguity that broke CT-S18.
compare = re.compile(
    r'trace-?free normal form|projectively equivalent|same object'
    r'|scalar (reduction|equation)'
    r'|companion (matrix|form|normalisation|normalization)'
    r'|identical normal form|match(es)? System C|equal as operators'
    r'|P_?C|P - P|reduction matches',
    re.I)
# Evidence that the claim pins down WHICH reduction is meant.
pinned = re.compile(
    r'\bfirst[- ]component\b|\bsecond[- ]component\b|\by_?1\b|\by_?2\b|cyclic vector'
    r'|\broute ?[12]\b|b-route|c-route|associated with c\(z\)|associated with b\(z\)'
    r'|first basis vector|\bP and Q\b|\(P, ?Q\)|P - P_?C|Q - Q_?C', re.I)

rows = []
for f in sorted(root.rglob('claims.jsonl')):
    if f.suffix != '.jsonl' or '.bak' in f.name:
        continue
    for line in f.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line:
            continue
        c = json.loads(line)
        txt = c.get('claim', '')
        if compare.search(txt):
            rows.append((f.parent.name, c['claim_id'], c.get('label'),
                         bool(pinned.search(txt)), txt))

print(f'claims comparing/identifying scalar operators: {len(rows)}\n')
amb = [r for r in rows if not r[3]]
print(f'PINNED (component or invariant pair named): {len(rows)-len(amb)}')
print(f'POTENTIALLY AMBIGUOUS: {len(amb)}\n')
print('=' * 72)
for sess, cid, lab, _, txt in amb:
    print(f'\n[{cid}] {lab}  ({sess})\n  {txt[:400]}')
print('\n' + '=' * 72)
print('\nPINNED, for spot-checking:')
for sess, cid, lab, _, txt in rows:
    if _:
        print(f'  [{cid}] {lab} ({sess})')
