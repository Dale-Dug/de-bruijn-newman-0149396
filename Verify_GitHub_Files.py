#!/usr/bin/env python3
"""Verify the bytes of this publication companion; no mathematical claim is checked."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def verify() -> int:
    if sys.flags.optimize:
        raise ValueError('Run without -O or PYTHONOPTIMIZE.')
    doc = json.loads((ROOT / 'GITHUB_FILES.json').read_text(encoding='utf-8'))
    if doc.get('schema') != 'BCLD_GITHUB_FILES_V1':
        raise ValueError('Unrecognised manifest schema.')
    if doc.get('publication_doi') != '10.5281/zenodo.22867547':
        raise ValueError('Publication identifier mismatch.')
    for name, info in doc['files'].items():
        if Path(name).name != name or name in {'.', '..'}:
            raise ValueError('Unexpected filename in manifest.')
        path = ROOT / name
        if path.is_symlink() or not path.is_file():
            raise ValueError('Missing or unsafe file: ' + name)
        if path.stat().st_size != info['bytes'] or sha256(path) != info['sha256']:
            raise ValueError('Changed file: ' + name)
    return len(doc['files'])

if __name__ == '__main__':
    try:
        count = verify()
    except (OSError, ValueError, KeyError) as exc:
        raise SystemExit('INTEGRITY CHECK FAILED: ' + str(exc))
    print('GITHUB_COMPANION_FILE_INTEGRITY_PASS', count)
    print('Scope: file identity only; not a mathematical proof or numerical replay.')
