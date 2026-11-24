#!/usr/bin/env python3
"""Write one debugging haiku (5-7-5) to /output/entry.txt.

The haiku was drafted by hand against the judge brief: three lines,
seventeen syllables, a concrete picture (a midnight stack trace), and a
last line that turns the blame back on the debugger.
"""

import os

HAIKU = (
    "Midnight stack trace grows\n"
    "each frame points at someone else\n"
    "all of them are me"
)


def main() -> None:
    lines = HAIKU.split("\n")
    assert len(lines) == 3, "haiku must be exactly three lines"
    assert 1 <= len(HAIKU) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(HAIKU)
    print(HAIKU)


if __name__ == "__main__":
    main()
