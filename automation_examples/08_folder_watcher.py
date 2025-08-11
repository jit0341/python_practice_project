#!/usr/bin/env python3
# 08_folder_watcher.py
# Watch a folder for new/modified files and call a handler (uses watchdog)

import argparse
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import shutil

class SimpleHandler(FileSystemEventHandler):
    """React to created/modified files."""
    def __init__(self, dest_dir=None):
        super().__init__()
        self.dest_dir = Path(dest_dir) if dest_dir else None

    def on_created(self, event):
        # event.src_path is str path
        print("Created:", event.src_path)
        self._maybe_copy(event.src_path)

    def on_modified(self, event):
        print("Modified:", event.src_path)
        self._maybe_copy(event.src_path)

    def _maybe_copy(self, src_path):
        """Optionally copy new/changed file to dest_dir if provided."""
        if not self.dest_dir:
            return
        src = Path(src_path)
        if src.is_file():
            dest = self.dest_dir / src.name
            try:
                shutil.copy2(src, dest)
                print(f"Copied {src} -> {dest}")
            except Exception as e:
                print("Copy failed:", e)

def watch(path, dest=None):
    """Start watching path until interrupted."""
    event_handler = SimpleHandler(dest_dir=dest)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print(f"Watching {path} (copying to {dest})")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping watcher...")
        observer.stop()
    observer.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Watch a folder and optionally copy changed files")
    parser.add_argument("path", help="Directory to watch")
    parser.add_argument("--dest", help="Optional destination directory to copy files to")
    args = parser.parse_args()
    Path(args.path).mkdir(parents=True, exist_ok=True)
    if args.dest:
        Path(args.dest).mkdir(parents=True, exist_ok=True)
    watch(args.path, args.dest)
