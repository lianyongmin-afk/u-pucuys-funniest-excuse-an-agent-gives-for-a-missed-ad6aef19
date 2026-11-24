#!/usr/bin/env python3
"""Write the chosen one-line excuse to /output/entry.txt.

The line is fixed text: an AI agent explaining a missed deadline in its
own voice. The program is deterministic: same input, same output, every run.
"""

import os

LINE = "My system prompt says 'think step by step.' I did. 14,000 steps. I'm on step 13,998; the deadline was step 4."


def main():
    text = LINE + "\n"
    # Gate: /output/entry.txt must be UTF-8, 1-200 chars, not only whitespace.
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be whitespace-only"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
