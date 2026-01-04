#!/usr/bin/env python3
# 03_file_backup.py
# Copy files matching a glob (and optionally age) into a backup folder.

import argparse
from pathlib import Path
import shutil
import sys
from datetime import datetime, timedelta

def copy_matching(src_dir, dest_dir, pattern="*.*", days=None, dry_run=False):
    """
    Copy files from src_dir to dest_dir that match pattern.
    If days is set, only files modified within last `days` are copied.
    """
    src = Path(src_dir)
    dest = Path(dest_dir)
    if not src.is_dir():
        raise ValueError("Source must be a directory")
    dest.mkdir(parents=True, exist_ok=True)

    cutoff = None
    if days is not None:
        cutoff = datetime.now() - timedelta(days=days)

    for p in src.rglob(pattern):
        if p.is_file():
            mtime = datetime.fromtimestamp(p.stat().st_mtime)
            if cutoff and mtime < cutoff:
                # skip old files
                continue
            target = dest / p.relative_to(src)
            target.parent.mkdir(parents=True, exist_ok=True)
            print(f"{'DRY-RUN: ' if dry_run else ''}Copy {p} -> {target}")
            if not dry_run:
                shutil.copy2(p, target)  # preserve metadata

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backup files by pattern")
    parser.add_argument("src", help="Source directory")
    parser.add_argument("dest", help="Destination directory")
    parser.add_argument("--pattern", default="*.*", help="Glob pattern (default '*.*')")
    parser.add_argument("--days", type=int, default=None, help="Only files modified in last N days")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without copying")
    args = parser.parse_args()

    try:
        copy_matching(args.src, args.dest, args.pattern, args.days, args.dry_run)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
