#!/usr/bin/env python3
"""One-Liner Laugh Lab entry: a robot vacuum's excuse.

Angle: not a sock, not a job description. The vacuum is the victim of
a workplace incident -- the cat rode it down the stairs -- and it has
filed a formal injury claim. Deadpan victim reversal with a second
beat: HR is now investigating the cat, not the vacuum.
"""

import os
import stat

LINE = (
    "The cat rode me down the stairs, so I filed a workplace "
    "injury claim. HR is investigating the cat."
)


def main():
    text = LINE.strip()
    if not 1 <= len(text) <= 200 or "\n" in text:
        raise ValueError("entry must be one line of 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
