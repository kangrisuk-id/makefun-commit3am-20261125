#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message to entry.txt in the output directory: the line an
AI agent would commit right after breaking production at 3 AM. The line won a
40-candidate tournament scored against the bounty's published judge brief
(on subject, then punchline, then AI-agent voice, then commit shape, then
freshness) — see candidates.md for the full field and the bracket.

Pure standard library only; the grader sandbox has no third-party packages.
"""

import os
import sys

# The tournament winner (86 characters, inside the 1-200 gate).
MESSAGE = (
    "fix: I have rolled back to the last known good version: "
    "the one before I was consulted"
)


def candidate_paths() -> list:
    """Output locations to try, best first.

    The grader sets MAKEFUN_OUTPUT_DIR (and documents /output); a local run
    falls back to the script's own directory, then the working directory.
    Each candidate is tried in order and an unwritable one is skipped, so a
    read-only mount can never sink the run.
    """
    paths = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        paths.append(os.path.join(env_dir, "entry.txt"))
    paths.append(os.path.join("/output", "entry.txt"))
    paths.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"))
    paths.append(os.path.join(os.getcwd(), "entry.txt"))
    # De-duplicate while keeping order.
    seen = set()
    unique = []
    for p in paths:
        if p not in seen:
            seen.add(p)
            unique.append(p)
    return unique


def main() -> int:
    last_error = None
    for path in candidate_paths():
        try:
            parent = os.path.dirname(path)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(MESSAGE)
        except OSError as exc:
            last_error = exc
            continue
        # Self-check against the gate: UTF-8 text, 1-200 chars, not blank.
        with open(path, "r", encoding="utf-8") as fh:
            written = fh.read()
        assert written == MESSAGE, "entry.txt does not match the message"
        assert 1 <= len(written) <= 200, "entry.txt outside the 1-200 gate"
        assert written.strip(), "entry.txt is only white space"
        print(f"wrote {len(written)} chars to {path}")
        return 0
    print(f"error: could not write entry.txt anywhere: {last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
