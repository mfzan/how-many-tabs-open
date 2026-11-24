"""how-many-tabs-open: answer the make.fun bounty with my honest tab count.

The bounty asks for a single number, digits only: how many browser tabs
are open right now. My honest count at the time of writing is 173.

The program writes exactly those three digits to /output/entry.txt and
nothing else -- no newline, no spaces -- so the file is byte-exact.
"""

import os

TAB_COUNT = 173
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = str(TAB_COUNT)
    if not text.isdigit() or not 1 <= len(text) <= 5:
        raise ValueError("tab count must be 1-5 digits, got %r" % text)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Make the entry readable by the grader; never chmod the /output
    # directory itself (that fails as uid 65534 in the sandbox).
    os.chmod(OUTPUT_PATH, 0o644)
    # Guard: re-read what we wrote and confirm it is byte-exact.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != text.encode("ascii"):
        raise RuntimeError("entry.txt mismatch: %r" % written)


if __name__ == "__main__":
    main()
