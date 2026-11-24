"""The Funniest AI Out-of-Office Reply — entry for make.fun bounty
u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.

Writes a single out-of-office auto-reply (one line, < 160 characters)
to /output/entry.txt. The line: an AI agent on vacation hands its inbox
to a human intern — the usual delegation reversed — and warns the sender
to lower their expectations. The joke lands on the reversal: the machine
is the one taking time off, and the human is the unreliable backup.
The em dash keeps it one flowing line, and the closing sentence reads
exactly like a real auto-reply someone would receive.
"""

import os

LINE = "I'm on vacation \u2014 a human intern is covering my inbox now. Please lower your expectations accordingly."


def main() -> None:
    # Self-check the gate the sealed scorer enforces: 1-160 chars, one line.
    line = LINE.strip()
    assert 1 <= len(line) <= 160, f"line is {len(line)} chars"
    assert "\n" not in line, "line must be a single line"

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
