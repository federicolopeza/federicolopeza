# /// script
# requires-python = ">=3.10"
# dependencies = ["fonttools==4.59.2", "brotli==1.1.0"]
# ///
"""Static self-contained animated SVGs. Run: uv run scripts/generate_assets.py.
Edit copy, geometry, palette and timing here. Outlined bundled OFL fonts need no
viewer fonts. Motion is CSS inside each SVG: no scripts, no external requests.
The resting (unanimated) state is the final composition, so reduced motion and
renderers without CSS animation still show the complete image.
Brand, palette and type follow federicolopez.uy ("Build. Break. Bound.").
"""
from html import escape
from pathlib import Path
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONTS = {
    "sans": TTFont(ASSETS / "fonts/Geist-Regular.ttf"),
    "strong": TTFont(ASSETS / "fonts/Geist-SemiBold.ttf"),
    "mono": TTFont(ASSETS / "fonts/GeistMono-Regular.ttf"),
    "serif": TTFont(ASSETS / "fonts/InstrumentSerif-Italic.woff2"),
}
# Tokens from federicolopez.uy app/globals.css: void (dark) and paper (light).
# build = Pentagoo Labs, brk = REKON / ARGUS, bound = AutoP2P, signal = the limit.
THEMES = {
    "light": dict(bg="#F1EFEA", edge="#D6D2C9", ink="#111110", muted="#57544E", line="#BDB8AD",
                  signal="#8E5100", build="#0A6E66", brk="#BB2328", bound="#127046"),
    "dark": dict(bg="#0A0A0B", edge="#242427", ink="#EDEBE6", muted="#A19E97", line="#38383D",
                 signal="#FFB23F", build="#45D5C8", brk="#FF5456", bound="#3DD68C"),
}

# Only `from` keyframes for intros: the element's own styles are the final frame.
# Loops are invisible at rest, also via an opacity="0" attribute for viewers without CSS.
STYLE = """<style>
.g,.u,.f,.p,.d{animation-duration:.8s;animation-timing-function:cubic-bezier(.16,1,.3,1);animation-fill-mode:both}
.g{animation-name:g}.u{animation-name:u}.f{animation-name:f}.p{animation-name:p;transform-box:fill-box;transform-origin:center}
.d{animation-name:d;animation-duration:1s;animation-timing-function:cubic-bezier(.65,0,.35,1);stroke-dasharray:1 2}
.h{opacity:0;transform-box:fill-box;transform-origin:center;animation:h 6s ease-out infinite}
.w{stroke-dasharray:.001 1.1;stroke-dashoffset:.05;animation:w 7s cubic-bezier(.45,0,.55,1) infinite}
@keyframes g{from{opacity:0;transform:translateY(-260px)}}
@keyframes u{from{opacity:0;transform:translateY(10px)}}
@keyframes f{from{opacity:0}}
@keyframes p{from{opacity:0;transform:scale(.3)}}
@keyframes d{from{stroke-dashoffset:1.05}}
@keyframes h{0%{opacity:.5;transform:scale(1)}35%,100%{opacity:0;transform:scale(3.4)}}
@keyframes w{0%{opacity:1;stroke-dashoffset:.05}65%{opacity:1;stroke-dashoffset:-1.05}66%,100%{opacity:0;stroke-dashoffset:-1.05}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>"""


def mix(a, b, t):
    """a blended toward b by t (0..1), as #RRGGBB."""
    ca, cb = (int(a[i:i + 2], 16) for i in (1, 3, 5)), (int(b[i:i + 2], 16) for i in (1, 3, 5))
    return "#" + "".join(f"{round(x + (y - x) * t):02X}" for x, y in zip(ca, cb))


def at(delay):
    return f' style="animation-delay:{delay:.2f}s"'


def advance(font, character, tracking):
    return font["hmtx"][font.getBestCmap()[ord(character)]][0] + tracking * font["head"].unitsPerEm


def measure(value, size, face="sans", tracking=0.0):
    font = FONTS[face]
    return sum(advance(font, c, tracking) for c in value) * size / font["head"].unitsPerEm


def text(value, x, y, size, color, face="sans", anim="u", start=0.0, stagger=0.0, tracking=0.0):
    """Outlined text. anim="g" rises glyph by glyph; "u"/"f" moves the whole line; None is static."""
    font = FONTS[face]
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    scale, cursor, paths, index = size / font["head"].unitsPerEm, 0.0, [], 0
    for character in value:
        name = cmap[ord(character)]
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        path = pen.getCommands()
        if path:
            if anim == "g":
                paths.append(f'<g transform="translate({cursor:g})"><path class="g"{at(start + index * stagger)} d="{path}"/></g>')
                index += 1
            else:
                paths.append(f'<path transform="translate({cursor:g})" d="{path}"/>')
        cursor += advance(font, character, tracking)
    body = f'<g fill="{color}" aria-label="{escape(value)}" transform="translate({x:g} {y:g}) scale({scale:.6f} {-scale:.6f})">' + "".join(paths) + "</g>"
    return body if anim in ("g", None) else f'<g class="{anim}"{at(start)}>{body}</g>'


def label(value, x, y, size, color, **kw):
    """Technical label: Geist Mono, uppercase, slightly tracked."""
    return text(value.upper(), x, y, size, color, "mono", tracking=0.04, **kw)


def label_width(value, size):
    return measure(value.upper(), size, "mono", 0.04)


def rect(x, y, w, h, fill, rx=0.0, cls=None, delay=0.0, stroke=None):
    attrs = f' rx="{rx}"' if rx else ""
    attrs += f' stroke="{stroke}"' if stroke else ""
    attrs += f' class="{cls}"{at(delay)}' if cls else ""
    return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" fill="{fill}"{attrs}/>'


def path(d, color, width=2.0, draw=None, dashed=False, cls=None, delay=0.0, cap="round"):
    """Stroked path. draw=seconds animates it on from its start."""
    attrs = f' stroke="{color}" stroke-width="{width:g}" stroke-linecap="{cap}" stroke-linejoin="round"'
    if dashed:
        attrs += ' stroke-dasharray="4 5"'
    if draw is not None:
        attrs += f' pathLength="1" class="d"{at(draw)}'
    elif cls:
        attrs += f' pathLength="1" class="{cls}"{at(delay)}'
    return f'<path d="{d}" fill="none"{attrs}/>'


def line(x1, y1, x2, y2, color, width=2.0, **kw):
    return path(f"M{x1:g} {y1:g}L{x2:g} {y2:g}", color, width, **kw)


def walker(d, color, width, delay):
    """A dot that travels the path, then pauses out of sight. Invisible at rest."""
    return path(d, color, width, cls="w", delay=delay).replace("<path ", '<path opacity="0" ', 1)


def circle(x, y, r, color, fill="none", cls=None, delay=0.0):
    attrs = f' class="{cls}"{at(delay)}' if cls else ""
    return f'<circle cx="{x:g}" cy="{y:g}" r="{r:g}" fill="{fill}" stroke="{color}" stroke-width="2"{attrs}/>'


def dot(x, y, r, fill, cls, delay):
    hidden = ' opacity="0"' if cls == "h" else ""
    return f'<circle cx="{x:g}" cy="{y:g}" r="{r:g}" fill="{fill}"{hidden} class="{cls}"{at(delay)}/>'


def card(w, h, p):
    return rect(0.5, 0.5, w - 1, h - 1, p["bg"], rx=14, stroke=p["edge"])


def mark(x, y, size, p, start=0.0, halo=True):
    """The brand mark: two brackets (the boundary) around one point (the decision)."""
    k = size / 64
    width = 5.5 * k
    s = path(f"M{x + 23 * k:g} {y + 13 * k:g}h{-9 * k:g}v{38 * k:g}h{9 * k:g}", p["ink"], width, draw=start, cap="square")
    s += path(f"M{x + 41 * k:g} {y + 13 * k:g}h{9 * k:g}v{38 * k:g}h{-9 * k:g}", p["ink"], width, draw=start, cap="square")
    if halo:
        s += dot(x + 32 * k, y + 32 * k, 6 * k, p["signal"], "h", start + 2.2)
    s += dot(x + 32 * k, y + 32 * k, 6 * k, p["signal"], "p", start + 0.55)
    return s


def write(name, w, h, title, content):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title">'
           f'<title id="title">{escape(title)}</title>{STYLE}{content}</svg>\n')
    (ASSETS / f"{name}.svg").write_text(svg)


def verbs(x, y, size, p, start, gap=22):
    """Build / Break / Bound, each in its product colour, as on the site."""
    s = ""
    for i, (word, key) in enumerate([("Build", "build"), ("Break", "brk"), ("Bound", "bound")]):
        s += rect(x, y - size * 0.62, size * 0.5, size * 0.5, p[key], rx=2, cls="p", delay=start + i * 0.15)
        s += text(word, x + size * 0.85, y, size, p[key], "strong", start=start + 0.05 + i * 0.15, tracking=-0.02)
        x += size * 0.85 + measure(word, size, "strong", -0.02) + gap
    return s


HERO_TITLE = "Federico López. The limit is part of the design. Build, break, bound."


def hero(theme, mobile):
    p = THEMES[theme]
    w, h = (360, 372) if mobile else (840, 320)
    s = card(w, h, p)
    if mobile:
        x = 24
        s += mark(x - 6, 16, 40, p, start=0.05, halo=False)
        s += label("Montevideo, UY", w - 24 - label_width("Montevideo, UY", 11), 40, 11, p["muted"], anim="f", start=0.2)
        s += text("Federico", x - 2, 128, 62, p["ink"], "strong", anim="g", start=0.25, stagger=0.035, tracking=-0.06)
        s += text("López", x - 2, 190, 62, p["ink"], "strong", anim="g", start=0.5, stagger=0.045, tracking=-0.06)
        s += text("The limit is", x, 236, 22, p["muted"], start=1.05, tracking=-0.02)
        s += text("part of the design.", x, 268, 31, p["ink"], "serif", start=1.2)
        s += line(x, 296, w - x, 296, p["edge"], 1, draw=1.3)
        s += verbs(x, 334, 17, p, 1.6, gap=16)
        s += label("Since 2017", x, 360, 10, p["muted"], anim="f", start=2.1)
    else:
        x = 40
        s += label("Software · Security · Automation", x, 45, 12, p["muted"], anim="f", start=0.15)
        s += label("Montevideo, UY", w - 40 - label_width("Montevideo, UY", 12), 45, 12, p["muted"], anim="f", start=0.2)
        s += text("Federico López", x - 3, 150, 86, p["ink"], "strong", anim="g", start=0.25, stagger=0.03, tracking=-0.065)
        s += text("The limit is", x, 204, 27, p["muted"], start=0.95, tracking=-0.02)
        s += text("part of the design.", x + measure("The limit is ", 27, "sans", -0.02), 204, 36, p["ink"], "serif", start=1.1)
        s += mark(w - 40 - 150, 64, 150, p, start=0.7)
        s += line(x, 246, w - x, 246, p["edge"], 1, draw=1.2)
        s += verbs(x, 287, 20, p, 1.55)
        since = "Building since 2017"
        s += label(since, w - 40 - label_width(since, 12), 285, 12, p["muted"], anim="f", start=2.0)
    write(f'hero{"-mobile" if mobile else ""}-{theme}', w, h, HERO_TITLE, s)


def kicker(value, key, p, x=24, y=34, start=0.0):
    return rect(x, y - 9, 8, 8, p[key], rx=2, cls="p", delay=start) + label(value, x + 16, y, 11, p["muted"], anim="f", start=start + 0.05)


REKON_TITLE = "REKON / ARGUS: agents explore attack paths inside an agreed scope, a person authorizes intrusive actions, evidence is validated. Conceptual diagram."


def rekon(theme, mobile):
    p = THEMES[theme]
    accent, soft = p["brk"], mix(p["bg"], p["brk"], 0.18)
    w, h = (360, 200) if mobile else (840, 184)
    s = card(w, h, p)
    s += kicker("Break — REKON / ARGUS", "brk", p)
    xs = [52, 180, 300] if mobile else [130, 420, 700]
    cy = 90
    routes = []
    for i, offset in enumerate([-24, 0, 24]):
        sx = xs[0] - 16
        d = f"M{sx + 4} {cy + offset}C{sx + (xs[1] - sx) * 0.55:g} {cy + offset} {xs[1] - 60} {cy} {xs[1] - 22} {cy}"
        routes.append(d)
        s += circle(sx, cy + offset, 4, p["muted"], p["bg"], cls="p", delay=0.15 + i * 0.08)
        s += path(d, p["muted"], 1.5, draw=0.3 + i * 0.12)
    # Exploration may run freely; it stops at the authorization gate.
    for i, d in enumerate(routes):
        s += walker(d, accent, 5, 2.4 + i * 1.1)
    s += rect(xs[1] - 19, cy - 22, 38, 44, accent, rx=6, cls="p", delay=1.0)
    s += path(f"M{xs[1] - 9} {cy}l6 6 12-13", p["bg"], 3, draw=1.25)
    s += line(xs[1] + 20, cy, xs[2] - 16, cy, accent, 2, draw=1.35)
    s += rect(xs[2] - 13, cy - 18, 26, 36, soft, rx=4, cls="p", delay=1.75)
    for i, dy in enumerate([-8, 0, 8]):
        s += line(xs[2] - 7, cy + dy, xs[2] + 7, cy + dy, accent, 2, draw=1.85 + i * 0.1)
    size = 18 if mobile else 20
    labels = ["Explore", "Authorize", "Validate"] if mobile else ["Attack paths", "Human authorization", "Validated evidence"]
    for i, (value, cx) in enumerate(zip(labels, xs)):
        s += text(value, cx - measure(value, size) / 2, 146, size, p["ink"], start=0.5 + i * 0.5)
    if mobile:
        s += text("Human approval before action.", 24, 180, 15, p["muted"], anim="f", start=2.0)
    write(f'rekon{"-mobile" if mobile else ""}-{theme}', w, h, REKON_TITLE, s)


AUTOP2P_TITLE = "AutoP2P: market input passes through operator rules and price limits to an update-or-hold decision with a recorded reason. Schematic, not live market data."


def autop2p(theme, mobile):
    p = THEMES[theme]
    accent, soft = p["bound"], mix(p["bg"], p["bound"], 0.14)
    w, h = (360, 200) if mobile else (840, 184)
    s = card(w, h, p)
    s += kicker("Bound — AutoP2P", "bound", p)
    start, end = (24, 197) if mobile else (40, 490)
    top, bottom = 56, 118
    s += rect(start, top, end - start, bottom - top, soft, cls="f", delay=0.1)
    s += line(start, top, end, top, accent, 1, dashed=True)
    s += line(start, bottom, end, bottom, accent, 1, dashed=True)
    points = [(start, 100), (start + 28, 100), (start + 28, 84), (start + 62, 84), (start + 62, 95), (start + 95, 95), (start + 95, 72), (end, 72)]
    d = "M" + " L".join(f"{x} {y}" for x, y in points)
    s += path(d, accent, 3, draw=0.35, cap="butt")
    # The marker walks the price line and never leaves the operator's band.
    s += walker(d, p["ink"], 7, 2.6)
    s += circle(end, 72, 4, accent, p["bg"], cls="p", delay=1.3)
    tx = 222 if mobile else 556
    s += label("Update / Hold", tx, 84, 14 if mobile else 26, p["ink"], anim="g", start=1.3, stagger=0.025)
    s += text("+ a reason", tx, 108 if mobile else 114, 19 if mobile else 26, p["muted"], "serif", start=1.75)
    s += text("Your rules. Your limits.", start, 152, 18 if mobile else 21, p["ink"], start=0.9)
    s += label("Schematic · not live prices", start if mobile else tx, 180 if mobile else 150, 10 if mobile else 11, p["muted"], anim="f", start=2.0)
    write(f'autop2p{"-mobile" if mobile else ""}-{theme}', w, h, AUTOP2P_TITLE, s)


PENTAGOO_TITLE = "Pentagoo Labs: a concrete problem becomes a product, automation or integration that is usable in production. Conceptual diagram."


def pentagoo(theme, mobile):
    p = THEMES[theme]
    accent, soft = p["build"], mix(p["bg"], p["build"], 0.22)
    w, h = (360, 200) if mobile else (840, 184)
    s = card(w, h, p)
    s += kicker("Build — Pentagoo Labs", "build", p)
    xs = [62, 180, 294] if mobile else [140, 420, 700]
    cy = 86
    s += line(xs[0] + 14, cy, xs[1] - 16, cy, p["line"], 2, draw=0.35)
    s += line(xs[1] + 16, cy, xs[2] - 16, cy, p["line"], 2, draw=0.95)
    s += walker(f"M{xs[0]} {cy}H{xs[2]}", accent, 6, 2.4)
    s += circle(xs[0], cy, 12, accent, p["bg"], cls="p", delay=0.15)
    s += path(f"M{xs[0] - 4} {cy - 4}a4 4 0 1 1 5 4v3M{xs[0] + 1} {cy + 7}v.5", accent, 2, cls="f", delay=0.25)
    # A small lattice: the structure assembles block by block.
    for i, (dx, dy) in enumerate([(-9, -9), (1, -9), (-9, 1), (1, 1)]):
        s += rect(xs[1] + dx, cy + dy, 8, 8, accent if i != 3 else soft, rx=1.5, cls="p", delay=0.75 + i * 0.08)
    s += circle(xs[2], cy, 12, accent, accent, cls="p", delay=1.35)
    s += path(f"M{xs[2] - 5} {cy}l3.5 3.5 7-7.5", p["bg"], 2.5, draw=1.5)
    size = 18 if mobile else 20
    labels = ["Problem", "Build", "Production"] if mobile else ["A concrete problem", "Product · automation · AI", "Usable in production"]
    for i, (value, cx) in enumerate(zip(labels, xs)):
        s += text(value, cx - measure(value, size) / 2, 140, size, p["ink"], start=0.3 + i * 0.6)
    if mobile:
        s += text("SaaS, tools, integrations, AI agents.", 24, 176, 15, p["muted"], anim="f", start=1.9)
    write(f'pentagoo{"-mobile" if mobile else ""}-{theme}', w, h, PENTAGOO_TITLE, s)


# Source: federicolopez.uy lib/cv.ts (Federico's public LinkedIn, 2026-09-26). Newest first.
# Years are fractional: "2026-03" → 2026 + 2/12.
ROLES = [
    ("REKON", "Co-founder & CTO", 2026 + 2 / 12, None, "brk"),
    ("Pentagoo Labs", "Founder", 2025 + 4 / 12, None, "build"),
    ("AutoP2P", "Creator", 2025 + 3 / 12, None, "bound"),
    ("Pentagoo P2P", "Founder", 2022 + 3 / 12, 2025 + 4 / 12, "bound"),
    ("Calculame.uy", "Web developer", 2019 + 10 / 12, 2020 + 10 / 12, "build"),
    ("Independent", "Freelance web developer", 2017 + 1 / 12, 2019 + 9 / 12, "build"),
]
NOW, FIRST = 2026 + 8 / 12, 2017.0
TRAJECTORY_TITLE = ("Trajectory, 2017 to now: freelance web developer 2017–2019; web developer at Calculame.uy 2019–2020; "
                    "founder of Pentagoo P2P 2022–2025; creator of AutoP2P since 2025; founder of Pentagoo Labs since 2025; "
                    "co-founder and CTO of REKON since 2026.")


def trajectory(theme, mobile):
    p = THEMES[theme]
    if mobile:
        w, h, left, right, top, row = 360, 392, 24, 326, 88, 46
    else:
        w, h, left, right, top, row = 840, 300, 330, 790, 84, 30
    span = lambda year: left + (year - FIRST) / (NOW - FIRST) * (right - left)
    s = card(w, h, p)
    s += kicker("Trajectory — building since 2017", "signal", p)
    bars = [top + n * row + (14 if mobile else 0) for n in range(len(ROLES))]
    axis_y = bars[-1] + (26 if mobile else 24)
    for year in [2017, 2019, 2021, 2023, 2025]:
        x = span(year)
        s += line(x, top - 22, x, axis_y - 12, p["edge"], 1, cls="f", delay=0.1)
        s += label(str(year), x - label_width(str(year), 11) / 2 if year > FIRST else x, axis_y + 6, 11, p["muted"], anim="f", start=0.15)
    now = span(NOW)
    s += line(now, top - 22, now, axis_y - 12, p["signal"], 1.5, dashed=True, cls="f", delay=0.2)
    s += label("Now", now - label_width("Now", 11), axis_y + 6, 11, p["signal"], anim="f", start=0.25)
    # Oldest first: the trajectory draws itself in chronological order.
    for n, (org, role, begin, end, key) in enumerate(ROLES):
        t = 0.35 + (len(ROLES) - 1 - n) * 0.22
        y = bars[n]
        s += line(span(begin), y, span(end if end else NOW), y, p[key], 8, draw=t, cap="butt")
        if mobile:
            ty = y - 13
            s += text(org, 24, ty, 15, p["ink"], "strong", start=t, tracking=-0.01)
            s += label(role, 24 + measure(org, 15, "strong", -0.01) + 10, ty, 10, p["muted"], anim="f", start=t + 0.1)
        else:
            s += text(org, 24, y + 5, 15, p["ink"], "strong", start=t, tracking=-0.01)
            s += label(role, 146, y + 4, 10, p["muted"], anim="f", start=t + 0.1)
    s += dot(now, top - 22, 4, p["signal"], "h", 2.6)
    s += dot(now, top - 22, 4, p["signal"], "p", 1.9)
    write(f'trajectory{"-mobile" if mobile else ""}-{theme}', w, h, TRAJECTORY_TITLE, s)


def divider(theme, mobile):
    p = THEMES[theme]
    w, h = (360, 16) if mobile else (840, 16)
    s = line(1, 8, w - 1, 8, p["line"], 1, draw=0.1)
    for i, key in enumerate(["build", "brk", "bound"]):
        s += line(1 + i * 18, 8, 13 + i * 18, 8, p[key], 3, draw=0.05 + i * 0.1, cap="butt")
    s += walker(f"M60 8H{w - 1}", p["signal"], 3, 1.2)
    write(f'divider{"-mobile" if mobile else ""}-{theme}', w, h, "Section divider", s)


if __name__ == "__main__":
    count = 0
    for theme in THEMES:
        for mobile in (False, True):
            for build in (hero, rekon, autop2p, pentagoo, trajectory, divider):
                build(theme, mobile)
                count += 1
    print(f"Generated {count} animated SVGs from bundled fonts.")
