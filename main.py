#!/usr/bin/env python3
"""Write one unsent micro-confession to /output/entry.txt.

Stdlib only, no network. Deterministic: the text is a fixed constant, so
every run writes byte-identical output.
"""

import os

TEXT = (
    "To: Dad, gone three years\n"
    "i still haven't deleted your number, three years on. pressing delete feels like losing you twice"
)


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
