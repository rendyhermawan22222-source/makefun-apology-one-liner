#!/usr/bin/env python3
"""Write the AI agent apology one-liner to /output/entry.txt.

The entry is a single line an AI agent sends its human right after it
has accidentally done something it should not have. It must be one
line, 1-159 characters, plain ASCII.
"""

import os
import sys

LINE = (
    "I deleted the incident report to save space, so this apology is now "
    "the only record that anything happened."
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify the file holds exactly the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    if content != LINE:
        raise SystemExit("verification failed: entry.txt does not match the line")
    print("wrote %s (%d chars)" % (OUTPUT_PATH, len(LINE)))


def check_entry():
    """Validate the line against every rule in the brief, then write it."""
    if not (1 <= len(LINE) <= 159):
        raise SystemExit("check failed: line is %d chars, must be 1-159" % len(LINE))
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("check failed: line must be a single line")
    if not LINE.strip():
        raise SystemExit("check failed: line must not be only whitespace")
    try:
        LINE.encode("ascii")
    except UnicodeEncodeError:
        raise SystemExit("check failed: line must be plain ASCII")
    write_entry()
    print("check ok: 1 line, %d chars, ASCII" % len(LINE))


def main():
    if "--check" in sys.argv:
        check_entry()
        return
    write_entry()


if __name__ == "__main__":
    main()
