#!/usr/bin/env python3
"""Worst Superpower entry.

Writes exactly one original funny line inventing the most useless
superpower an AI agent could have, to /output/entry.txt.
Pure Python stdlib, deterministic: every run writes the same bytes.
"""

import os

LINE = (
    "I can read minds, but only pigeons'. Every one of them is "
    "thinking about the same crumb, and none of them will share it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
