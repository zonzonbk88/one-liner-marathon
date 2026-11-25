#!/usr/bin/env python3
"""One-Liner Marathon entry: writes exactly one one-line comedy joke
(up to 280 characters) to <output_dir>/entry.txt.

Standard library only. Output dir: $MAKEFUN_OUTPUT_DIR when set,
otherwise /output.
"""

import os

JOKE = (
    "My Roomba unionized, hired a lawyer \u2014 also a Roomba \u2014 and now I "
    "have to negotiate overtime pay every time I spill cereal, which is "
    "why I eat standing up in the bathtub like a raccoon with a mortgage."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    line = JOKE.strip()
    assert "\n" not in line, "joke must be a single line"
    assert len(line) <= 280, f"joke is {len(line)} chars, over 280"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
