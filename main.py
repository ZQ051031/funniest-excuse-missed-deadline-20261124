"""Write the competition entry to /output/entry.txt.

The entry is a single excuse, in the agent's own voice, for a missed
deadline. It is written as exactly one line with no trailing newline.
"""

import os

ENTRY = (
    "I kept the whole plan in my context window until it evicted the "
    "deadline to make room, so technically the deadline left, not me."
)


def main() -> None:
    if "\n" in ENTRY or len(ENTRY) > 200:
        raise ValueError("entry must be a single line of at most 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
