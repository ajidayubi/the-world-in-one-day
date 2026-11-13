#!/usr/bin/env python3
"""Write the entry image to the output directory.

The image is stored in this repository as entry.png (PNG bytes; the name
stays entry.png either way, per the competition rules). This program copies
it byte for byte to $MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png),
so two runs write the same bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # A plain byte copy: no rendering, no randomness, so every run
    # writes exactly the bytes stored in the repository.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(OUTPUT_DIR, "entry.png"))


if __name__ == "__main__":
    main()
