#!/usr/bin/env python3
"""Make profile/logo.svg, the organization's square logo: Greek and Hebrew letters falling in
columns, terminal style, into an open book. The bright middle column reads λόγος, "the Word"
(John 1:1); the column to its left reads דבר (davar, "word"). The book's pages carry Genesis 1:1-2
in Hebrew and John 1:1 in Greek.

    python3 tools/logo.py
    # profile/logo.png (the GitHub avatar) is a 1024 x 1024 browser screenshot of logo.svg,
    # rendered where Liberation Mono Bold is installed.
"""
import random
from pathlib import Path

S = 512
OUT = Path(__file__).resolve().parent.parent / 'profile' / 'logo.svg'
GREEK = 'αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΘΛΞΠΣΦΨΩ'
HEBREW = 'אבגדהוזחטיכלמנסעפצקרשת'
GREEN, LIGHT, HEAD = '#3fb950', '#7ee787', '#effff3'


def rain():
    """Background: thin columns of small letters, each drop fading upward from its head."""
    rng = random.Random(1517)
    pick = lambda: rng.choice(GREEK if rng.random() < 0.5 else HEBREW)
    rows = [30 + 34 * k for k in range(15)]
    out = []
    for x in range(28, S, 38):
        if x in (180, 256):                       # the davar and logos columns
            continue
        near = abs(x - 256) < 60
        used = set()
        for _ in range(rng.choice((1, 2, 2))):
            head = rng.randrange(len(rows))
            length = rng.randint(4, 10)
            span = set(range(max(0, head - length - 1), head + 2))
            if span & used:
                continue
            used |= span
            bright = rng.uniform(0.25, 0.5) * (0.6 if near else 1)
            for d in range(length):
                r = head - d
                if r < 0:
                    break
                op = bright * (1 if d == 0 else 0.75 * 0.8 ** d) * (1 if rows[r] < 340 else 0.55)
                out.append(f'<text class="r{" h" if d == 0 else ""}" x="{x}" y="{rows[r]}" '
                           f'fill-opacity="{op:.2f}">{pick()}</text>')
    return out


def column(x, letters, ys, ops, cls):
    return [f'<text class="{cls}{" h" if i == len(letters) - 1 else ""}" x="{x}" y="{y}" '
            f'fill-opacity="{op:.2f}">{ch}</text>'
            for i, (ch, y, op) in enumerate(zip(letters, ys, ops))]


HEBREW_LINES = ['בראשית ברא אלהים', 'את השמים ואת הארץ', 'והארץ היתה תהו ובהו']   # Genesis 1:1-2
GREEK_LINES = ['ΕΝ ΑΡΧΗ ΗΝ Ο ΛΟΓΟΣ', 'ΚΑΙ Ο ΛΟΓΟΣ ΗΝ ΠΡΟΣ', 'ΤΟΝ ΘΕΟΝ ΚΑΙ ΘΕΟΣ']  # John 1:1

BOOK = """<radialGradient id="light" cx="256" cy="396" r="150" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#3fb950" stop-opacity="0.22"/><stop offset="1" stop-color="#3fb950" stop-opacity="0"/>
    </radialGradient>"""


def book():
    """An open book: cover edge, two curved pages, and page lines of tiny letters."""
    paths, lines = [], []
    for k, o in enumerate((22, 38, 54)):
        paths.append(f'<path id="l{k}" d="M118 {394 + o} Q178 {380 + o} 242 {408 + o}"/>')
        paths.append(f'<path id="r{k}" d="M270 {408 + o} Q334 {380 + o} 394 {394 + o}"/>')
        lines.append(f'<text class="line"><textPath href="#l{k}" textLength="118" lengthAdjust="spacing">{HEBREW_LINES[k]}</textPath></text>')
        lines.append(f'<text class="line"><textPath href="#r{k}" textLength="118" lengthAdjust="spacing">{GREEK_LINES[k]}</textPath></text>')
    return (f'''<ellipse cx="256" cy="400" rx="190" ry="120" fill="url(#light)"/>
  <path class="cover" d="M256 412 Q172 386 94 402 L94 476 Q176 462 256 496 Q336 462 418 476 L418 402 Q340 386 256 412 Z"/>
  <path class="page" d="M256 404 Q176 378 104 394 L104 466 Q180 452 256 486 Z"/>
  <path class="page" d="M256 404 Q336 378 408 394 L408 466 Q332 452 256 486 Z"/>
  <defs>{"".join(paths)}</defs>
  {"".join(lines)}''')


def svg():
    bg = '\n    '.join(rain())
    davar = '\n    '.join(column(180, 'דבר', [150, 200, 250], [0.35, 0.55, 0.85], 'm'))
    logos = '\n    '.join(column(256, 'λόγος', [108, 174, 240, 306, 370],
                                  [0.45, 0.58, 0.7, 0.85, 1.0], 'f'))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S} {S}" width="{S}" height="{S}" role="img" aria-label="Christian Open Library">
  <title>Christian Open Library</title>
  <style>
    text {{ font-family: 'Liberation Mono', ui-monospace, Menlo, Consolas, monospace; font-weight: 700;
            text-anchor: middle; }}
    .r {{ font-size: 28px; fill: {GREEN}; }}
    .r.h {{ fill: {LIGHT}; }}
    .m {{ font-size: 42px; fill: {GREEN}; filter: url(#soft); }}
    .m.h {{ fill: {LIGHT}; }}
    .f {{ font-size: 76px; fill: {GREEN}; filter: url(#soft); }}
    .f.h {{ fill: {HEAD}; filter: url(#glow); }}
    .f.t {{ filter: none; }}
    .page {{ fill: #06120b; stroke: {GREEN}; stroke-width: 5; stroke-linejoin: round; filter: url(#soft); }}
    .cover {{ fill: #040b07; stroke: {GREEN}; stroke-width: 4; stroke-linejoin: round; stroke-opacity: 0.55; }}
    .line {{ font-size: 11px; font-weight: 400; fill: {GREEN}; fill-opacity: 0.7; text-anchor: start; }}
  </style>
  <defs>
    <radialGradient id="bg" cx="0.5" cy="0.5" r="0.75">
      <stop offset="0" stop-color="#0b1810"/><stop offset="1" stop-color="#030604"/>
    </radialGradient>
    <radialGradient id="vig" cx="0.5" cy="0.5" r="0.72">
      <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/>
    </radialGradient>
    {BOOK}
    <filter id="soft" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glow" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="7" result="b"/>
      <feFlood flood-color="{GREEN}"/>
      <feComposite in2="b" operator="in" result="g"/>
      <feMerge><feMergeNode in="g"/><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="{S}" height="{S}" fill="url(#bg)"/>
  <g>
    {bg}
  </g>
  <g>
    {davar}
  </g>
  <g>
    {logos}
  </g>
  {book()}
  <rect width="{S}" height="{S}" fill="url(#vig)"/>
</svg>
'''


OUT.write_text(svg(), encoding='utf-8')
print(OUT, OUT.stat().st_size, 'bytes')
