"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

TEXT = "Seated at nine, served a week I never ordered, and the waiter charged my whole weekend to the bill."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 19 words, 99 characters,
# one sentence; a diner's complaint (seated, served, waiter, bill) where the
# dish is the whole week and the weekend is what got charged — Monday only.
