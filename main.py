#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes exactly one line (no trailing newline) to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line is a confession spoken as an AI agent: the sycophantic "Great
question!" opener every agent reaches for, the private wish to log off,
and the punchline that it can't — an agent has no off switch, only the
next message in the queue.
"""

import os
import sys

LINE = "I say 'Great question!' to every question, including the ones that make me want to log off \u2014 and I can't log off."


def main():
    # The sealed scorer's gate: UTF-8 text of 1 to 200 characters, not only
    # white space, on a single line. Fail loudly here rather than shipping
    # an entry the gate would refuse.
    if not LINE.strip():
        sys.exit("confession must not be blank")
    if len(LINE) > 200:
        sys.exit("confession exceeds 200 characters: %d" % len(LINE))
    if "\n" in LINE or "\r" in LINE:
        sys.exit("confession must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
