#!/usr/bin/env python3
"""One Word for Your Wi-Fi.

Writes a single word describing Wi-Fi to entry.txt.

The word is "ghosting": home Wi-Fi that is there one second and gone the
next, vanishing mid-call without a word, like a bad date. It is funny at
once, true to how Wi-Fi actually behaves, and needs no explanation.
"""

import os
import sys

WORD = "ghosting"


def main():
    word = WORD
    # Validate before writing anything: exactly one word, 1-20 characters.
    if not word or len(word) > 20:
        sys.exit("word must be 1-20 characters")
    if len(word.split()) != 1:
        sys.exit("word must be a single word")
    if word != word.strip():
        sys.exit("word must not have surrounding whitespace")
    data = word.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.umask(0o022)
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "wb") as f:
            f.write(data)
        os.chmod(path, 0o644)
    except OSError:
        # Fallback only if the primary output dir is unusable.
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "wb") as f:
            f.write(data)
        os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
