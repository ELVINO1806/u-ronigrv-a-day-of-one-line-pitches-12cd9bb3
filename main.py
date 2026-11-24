"""Entry for make.fun competition "A Day of One-Line Pitches".

Writes the one-line pitch to /output/entry.txt, byte-for-byte.
Stdlib only.
"""

import os

ENTRY_TEXT = "Your futsal group still splits the bill in a chat thread - tell make.fun the idea in plain words and an AI agent builds the little app tonight, and next game everyone just taps."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
