#!/usr/bin/env python3
"""Desert Island: one emoji standing in for a dream vacation.

The brief asks for a single emoji that makes a stranger want to book
the trip. This entry answers with the desert island: a palm, a strip of
sand, a turquoise sea, and nobody else around. It is the whole postcard
compressed into one glyph, so it reads at a glance on any screen and
needs no caption. It also says something specific rather than naming
holidays in general — the fantasy here is not a hotel or an itinerary,
it is having an island all to yourself, somewhere with no airport to
land at and nothing to do but be there. The character renders as an
emoji on its own, with no variation selector attached, so the file
holds exactly one character and nothing else.
"""

from pathlib import Path

ISLAND_CODE_POINT = 0x1F3DD  # desert island
ENTRY_FILE = Path("/output/entry.txt")
ENCODING = "utf-8"


def pick_emoji() -> str:
    """Return the single emoji this entry submits."""
    return chr(ISLAND_CODE_POINT)


def publish() -> None:
    """Write the emoji to the entry file, alone, with no newline."""
    ENTRY_FILE.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_FILE.write_bytes(pick_emoji().encode(ENCODING))


if __name__ == "__main__":
    publish()
