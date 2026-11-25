#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.

The review is a fixed, hand-written line: deterministic by design, so
every run produces the exact same bytes.
"""

import os

# The review: one line, one grievance, one star.
REVIEW = (
    "One star. He waters me with yesterday's coffee, calls it "
    "'a little treat,' then acts betrayed when my leaves curl up "
    "like I've just read his browser history. And the pot still "
    "has no drainage."
)


def main() -> None:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
