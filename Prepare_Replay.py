#!/usr/bin/env python3
"""Restore the immutable Zenodo deposit and check its files, without running the proof."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
import zipfile
from Verify_GitHub_Files import verify, sha256

ROOT = Path(__file__).resolve().parent
CONTENT = {
    'Correlated_Translated_Probes.pdf', 'Correlated_Translated_Probes.tex',
    'Analytic_Foundations.pdf', 'Verification_Guide.pdf',
    'Manuscript_Sources.zip', 'LICENSES_AND_RIGHTS.md',
}
METADATA = {
    'README.md', 'CITATION.cff', 'Verify_Deposit.py',
    'Release_Manifest.json', 'SHA256SUMS.txt',
}

def check_file(path: Path, expected: dict) -> None:
    if path.is_symlink() or not path.is_file():
        raise ValueError('Missing or unsafe file: ' + str(path))
    if path.stat().st_size != expected['bytes'] or sha256(path) != expected['sha256']:
        raise ValueError('Unexpected archive bytes. Do not bypass this mismatch: ' + str(path))

def download(url: str, path: Path, expected: dict) -> None:
    request = urllib.request.Request(url, headers={
        'User-Agent': 'BCLD-publication-companion/1.0',
        'Accept': 'application/zip, application/octet-stream',
    })
    count = 0
    with urllib.request.urlopen(request, timeout=60) as response, path.open('xb') as f:
        while True:
            block = response.read(1024 * 1024)
            if not block:
                break
            count += len(block)
            if count > expected['bytes']:
                raise ValueError('Download exceeds the expected archival file size.')
            f.write(block)
    check_file(path, expected)

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sources = parser.add_mutually_exclusive_group(required=True)
    sources.add_argument('--archive', type=Path, help='Existing Proof_and_Replay.zip.')
    sources.add_argument('--download', action='store_true', help='Download the pinned-size/hash archive from Zenodo.')
    parser.add_argument('--output', type=Path, required=True, help='A NEW directory outside this repository.')
    args = parser.parse_args()
    verify()
    provenance = json.loads((ROOT / 'REPOSITORY_PROVENANCE.json').read_text())
    expected = provenance['external_replay_archive']
    output = args.output.expanduser().resolve()
    if output.exists() or output == ROOT or ROOT in output.parents:
        raise ValueError('Choose a new output directory outside the repository; existing paths are never overwritten.')
    source = args.archive.expanduser().resolve() if args.archive else None
    if source is not None:
        check_file(source, expected)
    with zipfile.ZipFile(ROOT / 'ZENODO_ORIGINAL_METADATA.zip') as z:
        names = z.namelist()
        if len(names) != len(METADATA) or set(names) != METADATA or z.testzip() is not None:
            raise ValueError('Original metadata archive has an unexpected inventory or failed integrity.')
        metadata = {name: z.read(name) for name in names}
    output.mkdir(parents=True, exist_ok=False)
    try:
        for name in CONTENT:
            shutil.copyfile(ROOT / name, output / name)
        for name, data in metadata.items():
            (output / name).write_bytes(data)
        target = output / 'Proof_and_Replay.zip'
        if source is not None:
            shutil.copyfile(source, target)
            check_file(target, expected)
        else:
            download(expected['url'], target, expected)
        subprocess.run([sys.executable, '-B', str(output / 'Verify_Deposit.py'), '--check-only'], check=True)
        verify()
    except Exception:
        # This directory was created by this invocation and was required to be absent.
        shutil.rmtree(output)
        raise
    print('ORIGINAL_DEPOSIT_RESTORED_AND_INTEGRITY_CHECKED')
    print('Location:', output)
    print('No scientific replay has been executed. Read Verification_Guide.pdf before running it.')
    print('Expected profile for the full replay: CPython 3.13, Linux x86_64.')

if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, zipfile.BadZipFile, urllib.error.URLError,
            subprocess.CalledProcessError) as exc:
        raise SystemExit('PREPARATION FAILED: ' + str(exc) +
                         '\nFor a network failure, download Proof_and_Replay.zip from the record and use --archive.\n'
                         'Never bypass a checksum mismatch. No partial output is retained.')
