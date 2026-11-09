#!/usr/bin/env python3
"""Make profile/banner-dark.svg and profile/banner-light.svg, the banner on the front page.

Faint columns of Greek and Hebrew letters drift down behind the title. The cursor blinks a few
times and then stays. Motion stops for people who ask their system for reduced motion.

    python3 tools/banner.py
"""
import random
from pathlib import Path

W, H = 960, 200
OUT = Path(__file__).resolve().parent.parent / 'profile'
MONO = ("ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', "
        "'DejaVu Sans Mono', monospace")
GREEK = 'αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΘΛΞΠΣΦΨΩ'
HEBREW = 'אבגדהוזחטיכלמנסעפצקרשתךםןףץ'
DIGITS = '0123456789:'
THEMES = {
    'dark': dict(rain='#3fb950', head='#aff5b4', title='#e6edf3', muted='#7d8590',
                 cursor='#3fb950', strength=1.0),
    'light': dict(rain='#1a7f37', head='#0f5323', title='#1f2328', muted='#656d76',
                  cursor='#1a7f37', strength=0.9),
}


def glyph(rng):
    r = rng.random()
    return rng.choice(GREEK if r < 0.46 else HEBREW if r < 0.92 else DIGITS)


def columns():
    rng = random.Random(1611)
    cols, x = [], 8.0
    while x < W - 4:
        far = rng.random() < 0.45
        size = 11 if far else 13
        dur = rng.uniform(28, 50) if far else rng.uniform(18, 32)
        cols.append(dict(
            x=x, size=size, dur=dur, delay=-rng.uniform(0, dur), rest=rng.uniform(-200, 120),
            alpha=rng.uniform(0.12, 0.18) if far else rng.uniform(0.24, 0.34),
            chars=[glyph(rng) for _ in range(rng.randint(6, 13))]))
        x += rng.choice((14, 16, 18, 22))
    return cols


def svg(theme):
    t = THEMES[theme]
    rain = []
    for c in columns():
        lh = c['size'] * 1.3
        n = len(c['chars'])
        spans = []
        for i, ch in enumerate(c['chars']):
            head = i == n - 1
            fo = 1.0 if head else 0.12 + 0.75 * (i / (n - 1)) ** 1.8
            fill = f' fill="{t["head"]}"' if head else ''
            spans.append(f'<tspan x="{c["x"]:.0f}" y="{(i + 1) * lh:.1f}"{fill} '
                         f'fill-opacity="{fo:.2f}">{ch}</tspan>')
        style = (f'transform:translateY({c["rest"]:.0f}px);animation-duration:{c["dur"]:.1f}s;'
                 f'animation-delay:{c["delay"]:.1f}s')
        rain.append(f'<g class="c" style="{style}" opacity="{c["alpha"] * t["strength"]:.3f}">'
                    f'<text font-size="{c["size"]}">{"".join(spans)}</text></g>')
    rain = '\n    '.join(rain)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Christian Open Library">
  <title>Christian Open Library</title>
  <style>
    text {{ font-family: {MONO}; }}
    .r text {{ fill: {t["rain"]}; }}
    .t {{ font-size: 38px; font-weight: 500; letter-spacing: -0.5px; fill: {t["title"]}; }}
    .s {{ font-size: 15px; letter-spacing: 0.5px; fill: {t["muted"]}; }}
    .cur {{ fill: {t["cursor"]}; animation: blink 1.2s steps(1, end) 8 forwards; }}
    .c {{ animation-name: fall; animation-timing-function: linear; animation-iteration-count: infinite; }}
    @keyframes fall {{ from {{ transform: translateY(-240px); }} to {{ transform: translateY(220px); }} }}
    @keyframes blink {{ 0% {{ fill-opacity: 1; }} 50% {{ fill-opacity: 0; }} 100% {{ fill-opacity: 1; }} }}
    @media (prefers-reduced-motion: reduce) {{ .c, .cur {{ animation: none; }} }}
  </style>
  <defs>
    <linearGradient id="fv" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#000"/><stop offset="0.2" stop-color="#fff"/>
      <stop offset="0.8" stop-color="#fff"/><stop offset="1" stop-color="#000"/>
    </linearGradient>
    <linearGradient id="fh" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#444"/><stop offset="0.5" stop-color="#444"/>
      <stop offset="0.82" stop-color="#fff"/><stop offset="1" stop-color="#fff"/>
    </linearGradient>
    <mask id="mv" maskUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}"><rect width="{W}" height="{H}" fill="url(#fv)"/></mask>
    <mask id="mh" maskUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}"><rect width="{W}" height="{H}" fill="url(#fh)"/></mask>
  </defs>
  <g class="r" mask="url(#mh)"><g mask="url(#mv)">
    {rain}
  </g></g>
  <text class="t" x="44" y="102">Christian Open Library<tspan class="cur" dx="2">_</tspan></text>
  <text class="s" x="46" y="138">// tolle lege</text>
</svg>
'''


for name in THEMES:
    path = OUT / f'banner-{name}.svg'
    path.write_text(svg(name), encoding='utf-8')
    print(path, path.stat().st_size, 'bytes')
