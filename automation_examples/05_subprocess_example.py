#!/usr/bin/env python3
# 05_subprocess_example.py
# Run shell commands from Python and capture output safely.

import subprocess  # run external commands
import shlex       # split command string into args safely
import argparse

def run_cmd(cmd, timeout=30, check=False):
    """
    Run a command (string or list).
    Returns completed process object.
    """
    if isinstance(cmd, str):
        args = shlex.split(cmd)  # avoid shell=True where possible
    else:
        args = cmd

    # run and capture output
    result = subprocess.run(
        args,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=check
    )
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a shell command and show output")
    parser.add_argument("cmd", nargs="+", help="Command to run (use quotes for a single string)")
    args = parser.parse_args()

    # join in case user passed many args
    cmd = " ".join(args.cmd)
    print("Running:", cmd)
    try:
        res = run_cmd(cmd, check=False)
        print("Exit code:", res.returncode)
        if res.stdout:
            print("STDOUT:")
            print(res.stdout.strip())
        if res.stderr:
            print("STDERR:")
            print(res.stderr.strip())
    except subprocess.TimeoutExpired:
        print("Command timed out")
