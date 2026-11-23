#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt (UTF-8, no trailing newline)."""

import os
import sys

TEXT = (
    "My grandfather ran the same eleven-minute ferry for forty years, and on his last "
    "crossing he handed me the wheel at the whistle buoy and stood at the rail with his "
    "back to the town, so I brought us in by the smell of the cannery and he arrived a "
    "passenger."
)


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"entry text must be 1..280 characters, got {len(text)}"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))

    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
