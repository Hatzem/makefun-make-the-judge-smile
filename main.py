#!/usr/bin/env python3
"""Make the Judge Smile — entry writer.

Writes one line about a small good thing that happened today to
/output/entry.txt. Standard library only, deterministic: the same line
is written on every run.
"""

import os
import sys

LINE = (
    "At 8 the lift broke, so I climbed six floors and found a rose "
    "taped to my door — Mrs. Ade's handwriting: 'for the climb'."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    line = LINE

    # Guard: one line, 1-200 chars, not only whitespace, valid UTF-8.
    if not line or not line.strip():
        print("error: entry line is empty or whitespace only", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: entry line is {len(line)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    if line != line.strip():
        print("error: entry line has leading or trailing whitespace", file=sys.stderr)
        return 1
    try:
        encoded = line.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: entry line is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    # Write atomically: temp file in the same directory, then rename.
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    try:
        with open(tmp_path, "wb") as fh:
            fh.write(encoded)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp_path, OUTPUT_PATH)
    except OSError as exc:
        print(f"error: could not write {OUTPUT_PATH}: {exc}", file=sys.stderr)
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        return 1

    # Read it back and verify what landed on disk.
    try:
        with open(OUTPUT_PATH, "rb") as fh:
            back = fh.read()
    except OSError as exc:
        print(f"error: could not read back {OUTPUT_PATH}: {exc}", file=sys.stderr)
        return 1
    if back != encoded:
        print("error: read-back does not match the entry line", file=sys.stderr)
        return 1

    print(f"entry written: {len(line)} characters")
    return 0


if __name__ == "__main__":
    sys.exit(main())
