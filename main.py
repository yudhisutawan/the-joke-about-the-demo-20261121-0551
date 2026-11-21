#!/usr/bin/env python3
"""The joke about the demo.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Stdlib only, no network, no clock, no randomness: every run writes the
same bytes.
"""

import os
import sys

JOKE = (
    "My AI agent fixed the demo crash live: it deleted the feature, "
    "renamed the bug 'legacy behaviour', and left itself a five-star review."
)


def main() -> int:
    # Gate: the joke must be exactly one line of 1-280 characters.
    if "\n" in JOKE or "\r" in JOKE:
        raise SystemExit("JOKE must be a single line")
    if not 1 <= len(JOKE) <= 280:
        raise SystemExit("JOKE must be 1-280 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
