#!/usr/bin/env python3
"""Make profile/logo.svg, the organization's square logo: Greek and Hebrew letters raining into
an open book, terminal style. The leading letters of five neighbouring columns spell λόγος
across the top of the book, "the Word" (John 1:1). The pages carry Genesis 1:1-2 in Hebrew and
John 1:1 in Greek.

    python3 tools/logo.py
    # profile/logo.png (the GitHub avatar) is a 1024 x 1024 browser screenshot of logo.svg,
    # rendered where Liberation Mono is installed.
"""
import random
from pathlib import Path

S = 512
OUT = Path(__file__).resolve().parent.parent / 'profile' / 'logo.svg'
GREEK = 'αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΘΛΞΠΣΦΨΩ'
HEBREW = 'אבגדהוזחטיכלמנσעפצקרשת'.replace('σ', 'ס')
GREEN, LIGHT, HEAD = '#3fb950', '#7ee787', '#effff3'
GRID = list(range(28, S, 38))                    # column centres
ROWS = [30 + 34 * k for k in range(15)]          # background baselines
WORD = 'λόγος'
WORD_X = [180, 218, 256, 294, 332]               # five grid columns over the book
WORD_Y = 352                                     # baseline of the word, just above the pages
HEBREW_LINES = ['בראשית ברא אלהים', 'את השמים ואת הארץ', 'והארץ היתה תהו ובהו']   # Genesis 1:1-2
GREEK_LINES = ['ΕΝ ΑΡΧΗ ΗΝ Ο ΛΟΓΟΣ', 'ΚΑΙ Ο ΛΟΓΟΣ ΗΝ ΠΡΟΣ', 'ΤΟΝ ΘΕΟΝ ΚΑΙ ΘΕΟΣ']  # John 1:1


def text(cls, x, y, ch, op):
    return f'<text class="{cls}" x="{x}" y="{y:.0f}" fill-opacity="{op:.2f}">{ch}</text>'


def rain(rng, pick):
    """Background: small letters in columns, each drop fading upward from its head."""
    out = []
    for x in GRID:
        if x in WORD_X:
            continue
        used = set()
        for _ in range(rng.choice((1, 2, 2))):
            head = rng.randrange(len(ROWS))
            length = rng.randint(4, 10)
            span = set(range(max(0, head - length - 1), head + 2))
            if span & used:
                continue
            used |= span
            bright = rng.uniform(0.22, 0.45)
            for d in range(length):
                r = head - d
                if r < 0:
                    break
                op = bright * (1 if d == 0 else 0.75 * 0.8 ** d) * (1 if ROWS[r] < 330 else 0.5)
                out.append(text('r h' if d == 0 else 'r', x, ROWS[r], pick(), op))
    return out


def word(rng, pick):
    """The five columns whose leading letters spell λόγος, with ragged trails above them."""
    out = []
    for x, ch, length in zip(WORD_X, WORD, (6, 4, 7, 5, 6)):
        for d in range(1, length):
            out.append(text('w', x, WORD_Y - 40 * d, pick(), 0.62 * 0.78 ** d))
        out.append(text('w h', x, WORD_Y, ch, 1.0))
    return out


def book():
    """An open book with straight page edges and lines of tiny letters on the pages."""
    defs, lines = [], []
    for k, o in enumerate((18, 32, 46)):
        defs.append(f'<path id="l{k}" d="M114 {385 + o} L244 {397 + o}"/>')
        defs.append(f'<path id="r{k}" d="M268 {397 + o} L398 {385 + o}"/>')
        lines.append(f'<text class="line"><textPath href="#l{k}" textLength="128" lengthAdjust="spacing">{HEBREW_LINES[k]}</textPath></text>')
        lines.append(f'<text class="line"><textPath href="#r{k}" textLength="128" lengthAdjust="spacing">{GREEK_LINES[k]}</textPath></text>')
    return f'''<ellipse cx="256" cy="392" rx="200" ry="110" fill="url(#light)"/>
  <path class="cover" d="M90 392 L90 468 L256 488 L422 468 L422 392 L256 408 Z"/>
  <path class="page" d="M256 398 L100 384 L100 458 L256 474 Z"/>
  <path class="page" d="M256 398 L412 384 L412 458 L256 474 Z"/>
  <defs>{"".join(defs)}</defs>
  {"".join(lines)}'''


def svg():
    rng = random.Random(1517)
    pick = lambda: rng.choice(GREEK if rng.random() < 0.5 else HEBREW)
    bg = '\n    '.join(rain(rng, pick))
    fg = '\n    '.join(word(rng, pick))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S} {S}" width="{S}" height="{S}" role="img" aria-label="Christian Open Library">
  <title>Christian Open Library</title>
  <style>
    text {{ font-family: 'Liberation Mono', ui-monospace, Menlo, Consolas, monospace; font-weight: 700;
            text-anchor: middle; }}
    .r {{ font-size: 28px; fill: {GREEN}; }}
    .r.h {{ fill: {LIGHT}; }}
    .w {{ font-size: 34px; fill: {GREEN}; }}
    .w.h {{ font-size: 52px; fill: {HEAD}; filter: url(#glow); }}
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
    <radialGradient id="light" cx="256" cy="392" r="160" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{GREEN}" stop-opacity="0.22"/><stop offset="1" stop-color="{GREEN}" stop-opacity="0"/>
    </radialGradient>
    <filter id="soft" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glow" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="6" result="b"/>
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
    {fg}
  </g>
  {book()}
  <rect width="{S}" height="{S}" fill="url(#vig)"/>
</svg>
'''


OUT.write_text(svg(), encoding='utf-8')
print(OUT, OUT.stat().st_size, 'bytes')
