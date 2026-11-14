#!/usr/bin/env python3
"""news-image-01 V3 entrypoint.

The front page is rendered at build time and ships in this repository as
entry.png. The grader runs with no network and only the standard library,
so this program does one thing: copy those bytes to the output directory.
A copy is deterministic by construction -- identical input, identical output.
"""
import os
import shutil
import sys

IMAGE_NAME = "entry.png"
MAX_BYTES = 1048576

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, IMAGE_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, IMAGE_NAME)
    if not os.path.isfile(src):
        print("news-image-01: entry.png missing next to main.py", file=sys.stderr)
        return 1
    if os.path.getsize(src) > MAX_BYTES:
        print("news-image-01: entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    shutil.copyfile(src, dst)
    # Confirm the copy is a whole, valid PNG: right magic bytes, same size.
    with open(dst, "rb") as fh:
        magic = fh.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print("news-image-01: copied entry.png is not a PNG", file=sys.stderr)
        return 1
    if os.path.getsize(dst) != os.path.getsize(src):
        print("news-image-01: copied entry.png size mismatch", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
