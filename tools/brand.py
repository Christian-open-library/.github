#!/usr/bin/env python3
"""Make the sign-in page branding (WorkOS AuthKit) in profile/brand/:

  logo-light.svg, logo-dark.svg   the full logo: the logo tile plus "Christian Open Library" and "// tolle lege"
  favicon.svg                     a simple mark that reads at 32 px: a glowing λ over an open book

The PNGs (icon.png, logo-light.png, logo-dark.png, favicon.png) are browser renders of these and of
profile/logo.svg, made where Liberation Mono is installed (see the render step in the commit).
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'profile' / 'brand'
MONO = "'Liberation Mono', ui-monospace, Menlo, Consolas, monospace"
GREEN = '#3fb950'


def full(theme):
    title, muted = ('#1f2328', '#57606a') if theme == 'light' else ('#e6edf3', '#8b949e')
    logo = (OUT.parent / 'logo.svg').read_text()
    inner = logo[logo.index('>', logo.index('<svg')) + 1: logo.rindex('</svg>')]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1260 320" width="1260" height="320" role="img" aria-label="Christian Open Library">
  <defs><clipPath id="tile"><rect x="32" y="32" width="256" height="256" rx="44"/></clipPath></defs>
  <g clip-path="url(#tile)"><svg x="32" y="32" width="256" height="256" viewBox="0 0 512 512">{inner}</svg></g>
  <text x="328" y="170" style="font-family:{MONO};font-size:64px;font-weight:700;text-anchor:start;fill:{title}">Christian Open Library<tspan style="fill:{GREEN}">_</tspan></text>
  <text x="330" y="232" style="font-family:{MONO};font-size:32px;font-weight:400;text-anchor:start;fill:{muted}">// tolle lege</text>
</svg>
'''


FAVICON = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-label="Christian Open Library">
  <defs>
    <radialGradient id="bg" cx="0.5" cy="0.45" r="0.75"><stop offset="0" stop-color="#0d1f14"/><stop offset="1" stop-color="#040806"/></radialGradient>
    <filter id="glow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="6" result="b"/><feFlood flood-color="{GREEN}"/>
      <feComposite in2="b" operator="in" result="g"/>
      <feMerge><feMergeNode in="g"/><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="256" height="256" rx="52" fill="url(#bg)"/>
  <text x="128" y="148" text-anchor="middle" font-family="{MONO}" font-size="150" font-weight="700" fill="#effff3" filter="url(#glow)">λ</text>
  <path d="M128 176 L40 164 L40 214 L128 228 Z" fill="#0b1a10" stroke="{GREEN}" stroke-width="11" stroke-linejoin="round"/>
  <path d="M128 176 L216 164 L216 214 L128 228 Z" fill="#0b1a10" stroke="{GREEN}" stroke-width="11" stroke-linejoin="round"/>
</svg>
'''

OUT.mkdir(parents=True, exist_ok=True)
for theme in ('light', 'dark'):
    (OUT / f'logo-{theme}.svg').write_text(full(theme))
(OUT / 'favicon.svg').write_text(FAVICON)
print('written:', ', '.join(sorted(p.name for p in OUT.glob('*.svg'))))
