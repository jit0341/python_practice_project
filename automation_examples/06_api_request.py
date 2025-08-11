#!/usr/bin/env python3
# 06_api_request.py
# Simple JSON API fetcher with retries and save-to-file.

import argparse
import time
import json
import requests
from pathlib import Path

def fetch_json(url, max_retries=3, backoff=1.0, timeout=10):
    """
    Fetch JSON from URL with simple retry/backoff logic.
    Returns parsed JSON (dict/list) on success.
    Raises on persistent failure.
    """
    attempt = 0
    while True:
        try:
            r = requests.get(url, timeout=timeout, headers={"User-Agent": "python-api-client/1.0"})
            r.raise_for_status()
            return r.json()
        except (requests.RequestException, ValueError) as e:
            attempt += 1
            if attempt > max_retries:
                raise
            sleep_for = backoff * (2 ** (attempt - 1))
            print(f"Fetch failed (attempt {attempt}), retrying in {sleep_for:.1f}s...")
            time.sleep(sleep_for)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch JSON from an API and save to file")
    parser.add_argument("url", help="API endpoint URL returning JSON")
    parser.add_argument("--out", default="api_output.json", help="Output filename")
    args = parser.parse_args()

    data = fetch_json(args.url)
    Path(args.out).write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Saved JSON to {args.out}")
