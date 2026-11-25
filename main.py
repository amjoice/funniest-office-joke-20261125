#!/usr/bin/env python3
"""The Funniest Office Joke -- entry writer.

Writes one funny line about office life (at most 200 characters) to
/output/entry.txt. The joke: a new intern asks where the fire exit is,
and the manager points at the door marked "career growth" -- the only
way out of this office is quitting. Setup and turn, punchline last.
Pure standard library, no network, no randomness, no file reads -- the
output is byte-identical on every run.
"""

import os

# The joke, kept as its two beats so each half reads on its own:
# the innocent question, then the turn that reframes the exit.
_BEATS = (
    "The intern asked where the fire exit was, ",
    "so my manager pointed at the door marked 'career growth'.",
)

MAX_CHARS = 200


def build_line() -> str:
    """Assemble the entry line from its two beats."""
    return "".join(_BEATS)


def validate(text: str) -> str:
    """Check the line against the bounty gate: 1-200 chars, one line.

    Raises ValueError on anything the sealed scorer would refuse:
    empty or whitespace-only text, over the 200-character cap, or
    containing a line break.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("line must not be only whitespace")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            f"line is {len(cleaned)} chars, over the {MAX_CHARS} cap"
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("line must be a single line")
    return cleaned


def main() -> None:
    text = validate(build_line())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
