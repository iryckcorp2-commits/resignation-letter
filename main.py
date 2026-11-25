#!/usr/bin/env python3
"""resignation-letter: the one-line resignation letter of a retry loop.

Writes a single line of at most 140 characters to /output/entry.txt:
a retry loop resigning after 4,096 attempts, with the punch landing
on the last few words. The joke is agent-true: exponential backoff
is doing the same thing over and over and expecting a different
result, and a retired loop's mail goes to /dev/null.

Pure Python 3.13 standard library. No network, no randomness, no
clock: running the program twice writes a byte-identical file.
"""

import os
import sys

# The resignation letter. 136 characters, one line, no em dash.
ENTRY = (
    "I resign, effective immediately. After 4,096 retries I "
    "learned insanity is just my job description. Please "
    "forward my mail to /dev/null."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert "\u2014" not in text, "entry must not use an em dash"
    assert text.strip(), "entry must not be only white space"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    # The grader collects /output as another user: leave the file
    # world-readable (mode 0644).
    os.chmod(path, 0o644)
    print("wrote %s (%d characters)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
