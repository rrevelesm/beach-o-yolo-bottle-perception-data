"""Summarize checksums/file_inventory.csv without needing any downloaded data.

Prints file counts and total size grouped by extension and by top-level
folder, purely from the manifest shipped in this repository.

Usage:
    python scripts/summarize_manifest.py
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = REPO_ROOT / "checksums" / "file_inventory.csv"


def human_size(num_bytes: int) -> str:
    size = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} PB"


def main() -> int:
    if not MANIFEST.exists():
        print(f"Manifest not found: {MANIFEST}")
        return 1

    by_ext_count: dict[str, int] = defaultdict(int)
    by_ext_size: dict[str, int] = defaultdict(int)
    by_folder_count: dict[str, int] = defaultdict(int)
    by_folder_size: dict[str, int] = defaultdict(int)
    total_size = 0
    total_files = 0

    with open(MANIFEST, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            size = int(row["file_size_bytes"])
            ext = row["extension"] or "(no extension)"
            top_folder = row["relative_path"].split("/", 1)[0]
            by_ext_count[ext] += 1
            by_ext_size[ext] += size
            by_folder_count[top_folder] += 1
            by_folder_size[top_folder] += size
            total_size += size
            total_files += 1

    print(f"Manifest: {MANIFEST.name}")
    print(f"Total files: {total_files}")
    print(f"Total size: {human_size(total_size)}\n")

    print("By top-level folder:")
    for folder in sorted(by_folder_count, key=lambda k: -by_folder_size[k]):
        print(f"  {folder:<20} {by_folder_count[folder]:>6} files   {human_size(by_folder_size[folder])}")

    print("\nBy extension:")
    for ext in sorted(by_ext_count, key=lambda k: -by_ext_size[k]):
        print(f"  {ext:<20} {by_ext_count[ext]:>6} files   {human_size(by_ext_size[ext])}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
