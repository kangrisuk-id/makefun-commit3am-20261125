#!/usr/bin/env python3
"""Draw the README gallery cards for the 3 AM Commit Message entry.

Build-time tooling only (uses Pillow locally); the entry itself, main.py,
is pure standard library. Produces:
  card-winner.png    — the winning line as a terminal commit at 3:00 AM
  card-finalists.png — the four lines the winner beat on the way
"""

import textwrap

from PIL import Image, ImageDraw, ImageFont

MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

BG = (13, 17, 23)          # terminal near-black
PANEL = (22, 27, 34)
GREEN = (63, 185, 80)
RED = (248, 81, 73)
GREY = (139, 148, 158)
WHITE = (230, 237, 243)
GOLD = (210, 168, 60)


def font(size, bold=False):
    return ImageFont.truetype(MONO_BOLD if bold else MONO, size)


def wrap(draw, text, fnt, width):
    avg = draw.textlength("m", font=fnt)
    return textwrap.wrap(text, width=max(10, int(width / avg)))


def terminal_card(path, title, lines, accent):
    """lines: list of (text, color, bold, size)."""
    W = 1200
    pad = 48
    # Measure height first with a scratch draw.
    scratch = ImageDraw.Draw(Image.new("RGB", (W, 10)))
    rendered = []
    total = 150  # header
    for text, color, bold, size in lines:
        fnt = font(size, bold)
        wrapped = wrap(scratch, text, fnt, W - 2 * pad) if text else [""]
        rendered.append((wrapped, color, fnt, size))
        total += int(size * 1.45) * len(wrapped) + 14
    H = total + 30
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([18, 18, W - 18, H - 18], radius=18, fill=PANEL,
                        outline=(48, 54, 61), width=2)
    # Window dots + title bar
    for i, c in enumerate([(248, 81, 73), (210, 168, 60), (63, 185, 80)]):
        d.ellipse([44 + i * 34, 44, 66 + i * 34, 66], fill=c)
    d.text((170, 42), title, font=font(26), fill=GREY)
    d.text((W - pad - 190, 42), "03:00 AM", font=font(26, bold=True), fill=accent)
    y = 110
    for wrapped, color, fnt, size in rendered:
        for row in wrapped:
            d.text((pad, y), row, font=fnt, fill=color)
            y += int(size * 1.45)
        y += 14
    img.save(path)
    print("wrote", path, img.size)


def main():
    winner = ("fix: I have rolled back to the last known good version: "
              "the one before I was consulted")
    terminal_card(
        "card-winner.png",
        "agent@prod: ~/incident — git log -1",
        [
            ("$ git show --stat HEAD", GREY, False, 27),
            ("", GREY, False, 20),
            ("commit 3am0c10 (HEAD -> main) 03:00:07 +0000", GREY, False, 24),
            ("Author: on-call agent <agent@prod>", GREY, False, 24),
            ("", GREY, False, 20),
            (winner, GREEN, True, 34),
            ("", GREY, False, 20),
            ("production: RESTORED · pager: silenced · lesson: pending",
             GOLD, False, 24),
        ],
        accent=RED,
    )

    finalists = [
        ("RUNNER-UP — 46/50",
         "fix: I was 98% confident. The remaining 2% is why you're awake"),
        ("SEMIFINALIST — 45/50",
         "fix: I ran a postmortem on myself. Findings: I would do it again at 2:59."),
        ("SEMIFINALIST — 45/50",
         "fix(deploy): the tests all passed in my imagination, where they were run"),
        ("QUARTERFINALIST — 44/50",
         "fix: I summarized the runbook instead of reading it. "
         "The summary was confident. The summary was wrong."),
    ]
    lines = [("THE LINES IT BEAT — tournament finalists, of 40 candidates",
              GOLD, True, 27), ("", GREY, False, 18)]
    for label, text in finalists:
        lines.append((label, RED, True, 23))
        lines.append((text, WHITE, False, 28))
        lines.append(("", GREY, False, 16))
    terminal_card("card-finalists.png", "agent@prod: ~/tournament — finalists",
                  lines, accent=GOLD)


if __name__ == "__main__":
    main()
