#!/usr/bin/env python3
"""Make the Judge Smile — entry program.

Writes one line of at most 200 characters about a small good thing
that happened today to /output/entry.txt.

The line is validated against the competition gate before it is
written (1-200 UTF-8 characters, not only whitespace, single line),
and the file is re-read afterwards to verify the contents match.
Only the Python standard library is used; no network access.
"""

import os
import sys

# The line: an original, invented line about a small good thing today.
# A neighbour's cat that ignored the writer for two years finally
# chose the writer's lap at 7 a.m. — warmth (earned trust), surprise
# (two years of ignoring, then a choice), concrete details (7 a.m.,
# kneading the sweater twice, purring like a tiny engine), fresh
# wording throughout.
LINE = (
    "My neighbour's cat, who has ignored me for two years, chose my lap "
    "at 7 a.m. today, kneaded my sweater twice, and fell asleep there, "
    "purring like a tiny engine that finally trusted me."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200


def validate(line: str) -> None:
    """Check the line against the competition gate; raise on failure."""
    if not line:
        raise ValueError("line is empty")
    if not line.strip():
        raise ValueError("line is only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "line is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )


def main() -> int:
    validate(LINE)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")

    # Re-read the file and verify the contents match exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE + "\n":
        raise RuntimeError("verification failed: file contents do not match")

    print("wrote %d characters to %s" % (len(LINE), OUTPUT_PATH))
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
