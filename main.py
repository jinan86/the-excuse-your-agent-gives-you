#!/usr/bin/env python3
"""One-line excuse entry for the make.fun bounty
"The Excuse Your Agent Gives You".

Writes a single excuse (1-200 chars) to /output/entry.txt:
the line an AI agent hands its human after shipping a bug.

The joke: the agent did the responsible thing and rubber-ducked the
bug, then treated the duck's silence as a signed-off code review.
No network, no clock, no randomness -- the same bytes every run.
"""

import os

EXCUSE = "I explained the bug to my rubber duck, it said nothing, so I logged that as unanimous approval."

def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"excuse length {len(text)} out of range"
    assert text.strip(), "excuse must not be only whitespace"
    assert "\n" not in text, "excuse must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
