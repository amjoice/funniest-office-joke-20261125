#!/usr/bin/env python3
"""The Funniest Office Joke -- entry writer.

Writes one funny line about office life (at most 200 characters) to
/output/entry.txt. The line is a fixed string assembled from its two
halves below: a new intern asks where the fire exit is, and the manager
points at the door marked "career growth" -- the only way out is
quitting. Setup and turn, punchline last. Pure standard library, no
network, no randomness, no file reads -- the output is byte-identical
on every run.
"""

import os

_SETUP = "The intern asked where the fire exit was, "
_TURN = "so my manager pointed at the door marked 'career growth'."

LINE = _SETUP + _TURN

MAX_CHARS = 200


def _check_length(cleaned: str) -> None:
    """Reject a line that would bust the 200-char bounty cap."""
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            f"line is {len(cleaned)} chars, over the {MAX_CHARS} cap"
        )


def _check_single_line(cleaned: str) -> None:
    """Reject embedded newlines: the entry must be exactly one line."""
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("line must be a single line")


def validate(text: str) -> str:
    """Check the line against the bounty gate: 1-200 chars, one line."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("line must not be only whitespace")
    _check_length(cleaned)
    _check_single_line(cleaned)
    return cleaned


def main() -> None:
    text = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
