# -*- coding: utf-8 -*-
"""Append a prepared block to a target file, byte-wise, with pre-write checks.

Usage: python scripts\\append_block.py <block.md> <target>

Reuses the corrected control-character class from append_r27_and_p0.py rather
than restating it: that class already lost TAB once, and a second copy is a
second chance to lose something.
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load_bad_chars():
    """Extract just the helper, without executing the module.

    Importing the appender to reuse one function runs its whole body, including
    its writes. Reuse must not mean execution: take the function definition out
    of the source with ast and compile only that.
    """
    import ast
    p = os.path.join(HERE, 'append_r27_and_p0.py')
    src = io.open(p, encoding='utf-8').read()
    tree = ast.parse(src)
    body = [n for n in tree.body
            if isinstance(n, (ast.Import, ast.ImportFrom, ast.Assign))
            or (isinstance(n, ast.FunctionDef) and n.name == 'bad_chars')]
    if not any(isinstance(n, ast.FunctionDef) for n in body):
        raise SystemExit('STOP: bad_chars not found in %s' % p)
    ns = {}
    exec(compile(ast.Module(body=body, type_ignores=[]), p, 'exec'), ns)
    return ns['bad_chars']


def main():
    block_path, target = sys.argv[1], sys.argv[2]
    bad_chars = load_bad_chars()

    block = io.open(block_path, encoding='utf-8').read()
    bad = bad_chars(block.encode('utf-8'))
    if bad:
        print('STOP: control characters in block: %r' % (bad,))
        return 1

    head = block.strip().split('\n')[0].strip()
    before = io.open(target, encoding='utf-8').read()
    if head and head in before:
        print('SKIP already present: %s' % head[:60])
        return 0

    n0 = len(before.encode('utf-8'))
    l0 = before.count('\n') + 1
    sep = '' if before.endswith('\n\n') else ('\n' if before.endswith('\n') else '\n\n')
    with io.open(target, 'a', encoding='utf-8', newline='\n') as f:
        f.write(sep + block.rstrip('\n') + '\n')

    after = io.open(target, encoding='utf-8').read()
    assert after.startswith(before), 'prior content altered'
    assert block.strip() in after, 'block not readable back'
    n1 = len(after.encode('utf-8'))
    print('%s: %d -> %d bytes, %d -> %d lines  READBACK OK'
          % (os.path.basename(target), n0, n1, l0, after.count('\n') + 1))
    return 0


if __name__ == '__main__':
    sys.exit(main())
