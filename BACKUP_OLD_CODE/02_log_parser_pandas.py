#!/usr/bin/env python3
# 02_log_parser_pandas.py
# Parse simple structured logs into a DataFrame and report aggregates.

import argparse                # parse CLI arguments
from pathlib import Path       # file path helpers
import pandas as pd           # data analysis library
import re                     # regex for parsing

# simple pattern for logs like: 2025-08-09 12:00:00,INFO,User logged in
LOG_RE = re.compile(r'^(?P<ts>[^,]+),(?P<level>[^,]+),(?P<msg>.+)$')

def parse_log_line(line):
    """Parse one log line into a dict or return None if doesn't match."""
    m = LOG_RE.match(line.strip())
    if not m:
        return None
    return m.groupdict()

def load_logs(path):
    """Load log file into a pandas DataFrame."""
    rows = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                rows.append(parsed)
    # create DataFrame, parse ts as datetime
    df = pd.DataFrame(rows)
    if not df.empty:
        df['ts'] = pd.to_datetime(df['ts'], errors='coerce')
        # count message frequency
        df['msg_short'] = df['msg'].str.slice(0, 80)
    return df

def summarize(df):
    """Print summary statistics of the logs."""
    if df.empty:
        print("No log rows parsed.")
        return
    print("Rows:", len(df))
    print("Levels count:")
    print(df['level'].value_counts())
    print("\nTop messages:")
    print(df['msg_short'].value_counts().head(10))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse simple CSV-style logs.")
    parser.add_argument("logfile", type=Path, help="Path to log file")
    args = parser.parse_args()

    df = load_logs(args.logfile)
    summarize(df)
