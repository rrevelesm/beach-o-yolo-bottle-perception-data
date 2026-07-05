"""Verify a downloaded copy of the dataset against the SHA256 manifests in
checksums/. Run this after downloading dataset_yolo/ and/or bags/ from the
public OneDrive link, from the root of the downloaded data folder.

Usage:
    python scripts/verify_checksums.py --root /path/to/beach-o-yolo-bottle-perception-data
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import sys
from pathlib import Path


def sha256_of(path: Path, bufsize: int = 8 * 1024 * 1024) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(bufsize)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def verify_manifest(manifest_csv: Path, root: Path) -> tuple[int, int, list[str]]:
    ok = 0
    failed = 0
    missing: list[str] = []
    with open(manifest_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rel_path = row["relative_path"]
            expected_sha256 = row["sha256"]
            full_path = root / rel_path
            if not full_path.exists():
                missing.append(rel_path)
                continue
            actual_sha256 = sha256_of(full_path)
            if actual_sha256 == expected_sha256:
                ok += 1
            else:
                failed += 1
                print(f"MISMATCH: {rel_path}")
                print(f"  expected: {expected_sha256}")
                print(f"  actual:   {actual_sha256}")
    return ok, failed, missing


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Root of the downloaded beach-o-yolo-bottle-perception-data folder "
        "(default: the parent of this script's checksums/ folder, i.e. this repo).",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=None,
        help="Specific manifest CSV to verify (default: verify both "
        "sha256_dataset_manifest.csv and sha256_bag_manifest.csv if present).",
    )
    args = parser.parse_args()

    checksums_dir = args.root / "checksums"
    manifests = (
        [args.manifest]
        if args.manifest
        else [
            checksums_dir / "sha256_dataset_manifest.csv",
            checksums_dir / "sha256_bag_manifest.csv",
        ]
    )

    total_ok = 0
    total_failed = 0
    total_missing: list[str] = []
    ran_any = False

    for manifest in manifests:
        if not manifest.exists():
            print(f"(skipping, not found: {manifest})")
            continue
        ran_any = True
        print(f"Verifying against {manifest.name} ...")
        ok, failed, missing = verify_manifest(manifest, args.root)
        total_ok += ok
        total_failed += failed
        total_missing.extend(missing)

    if not ran_any:
        print("No manifest files found under checksums/. Nothing to verify.")
        return 1

    print(f"\nOK: {total_ok}  MISMATCH: {total_failed}  MISSING: {len(total_missing)}")
    if total_missing:
        print("Missing files (first 20):")
        for rel in total_missing[:20]:
            print(f"  {rel}")

    return 0 if (total_failed == 0 and not total_missing) else 1


if __name__ == "__main__":
    sys.exit(main())
