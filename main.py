#!/usr/bin/env python3
"""One Honest Line — writes one honest line to /output/entry.txt.

The line (84 chars, one line):
  You typed 'make it better' and blamed me for not knowing what 'better'
  means to you.
"""
import os

# The line targets the brief exactly: brutally funny, instantly recognisable
# to anyone who has typed a prompt, and true enough to sting.
LINE = (
    "You typed 'make it better' and blamed me for not knowing what "
    "'better' means to you."
)


def main():
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
