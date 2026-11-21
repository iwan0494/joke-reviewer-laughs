#!/usr/bin/env python3
"""The joke the reviewer laughs at.

Writes one line -- a joke about working beside an AI coding agent --
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR when the grader sets it).
No network, no dependencies, standard library only.
"""
import os
from pathlib import Path

JOKE = (
    'I told my AI agent the tests were failing; it fixed them by deleting '
    'the tests, and the CI has never been greener.'
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
