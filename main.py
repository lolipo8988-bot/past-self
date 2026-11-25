"""Two Lines to Your Past Self entry.

Writes exactly two lines to /output/entry.txt: line one warns the
writer's past self about one specific moment in a single sentence,
and line two says in one sentence why that moment mattered and what
changed because of it. The competition gate requires UTF-8 text of
1 to 280 characters, not only white space. The program is
deterministic: every run writes exactly the same bytes.

The output path defaults to /output/entry.txt and can be overridden
with the ENTRY_OUTPUT_PATH environment variable for local checks.
"""

import os

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
MAX_CHARS = 280

LINES = [
    "On March 3 at the kitchen table, when Dad asks if his tremor is "
    "nothing, do not smile and say yes just to keep dinner calm.",
    "That yes bought one quiet meal and cost him eight months before "
    "any doctor heard it, and by then Parkinson\u2019s had taken his "
    "handwriting and his job.",
]


def main() -> None:
    text = "\n".join(LINES)
    assert len(LINES) == 2, "entry must be exactly two lines"
    assert all(line.count(".") == 1 and line.endswith(".") for line in LINES), (
        "each line must be a single sentence"
    )
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    assert text.strip(), "entry must not be only white space"
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
