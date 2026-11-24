"""One-line office joke entry for make.fun.

Writes a single-line joke about office life to /output/entry.txt.
The joke is a fixed, deterministic string: no randomness, no network,
no input. It always writes exactly the same bytes. One line, one
sentence, setup first and punchline last, about office life.
"""

import os

ENTRY = "I log eight hours a day in my timesheet and spend seven of them deciding what to log."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
