# /// script
# requires-python = ">=3.10"
# dependencies = ["fonttools==4.59.2"]
# ///
"""Static self-contained animated SVGs. Run: uv run scripts/generate_assets.py.
Edit copy, geometry, palette and timing here. Outlined bundled OFL fonts need no
viewer fonts. Motion is CSS inside each SVG: no scripts, no external requests.
The resting (unanimated) state is the final composition, so reduced motion and
renderers without CSS animation still show the complete image.
"""
from html import escape
from pathlib import Path
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONTS = {
    "display": TTFont(ASSETS / "fonts/BricolageGrotesque-Bold.ttf"),
    "body": TTFont(ASSETS / "fonts/IBMPlexSans-Regular.ttf"),
}
THEMES = {
    "light": dict(bg="#F6F7F9", ink="#15171C", muted="#565C68", line="#D5DAE2", edge="#E1E5EB", accent="#2B59DB", soft="#E3E9FA"),
    "dark": dict(bg="#101318", ink="#EEF0F4", muted="#A3ABB9", line="#353C4A", edge="#232833", accent="#8FAEFF", soft="#1D2842"),
}
REKON = {
    "light": dict(accent="#B0314A", soft="#F7DFE4"),
    "dark": dict(accent="#FF9CAC", soft="#3E2533"),
}

# Only `from` keyframes for intros: the element's own styles are the final frame.
# Loops start and end invisible, so their resting state adds nothing.
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
@keyframes h{0%{opacity:.45;transform:scale(1)}35%,100%{opacity:0;transform:scale(3.4)}}
@keyframes w{0%{stroke-dashoffset:.05}65%,100%{stroke-dashoffset:-1.05}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>"""


def at(delay):
    return f' style="animation-delay:{delay:.2f}s"'


def measure(value, size, face="body"):
    font = FONTS[face]
    cmap = font.getBestCmap()
    return sum(font["hmtx"][cmap[ord(c)]][0] for c in value) * size / font["head"].unitsPerEm


def text(value, x, y, size, color, face="body", anim="u", start=0.0, stagger=0.0):
    """Outlined text. anim="g" rises glyph by glyph; "u"/"f" moves the whole line."""
    font = FONTS[face]
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    scale, cursor, paths, index = size / font["head"].unitsPerEm, 0, [], 0
    for character in value:
        name = cmap[ord(character)]
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        path = pen.getCommands()
        if path:
            if anim == "g":
                paths.append(f'<g transform="translate({cursor})"><path class="g"{at(start + index * stagger)} d="{path}"/></g>')
                index += 1
            else:
                paths.append(f'<path transform="translate({cursor})" d="{path}"/>')
        cursor += font["hmtx"][name][0]
    body = f'<g fill="{color}" aria-label="{escape(value)}" transform="translate({x} {y}) scale({scale:.6f} {-scale:.6f})">' + "".join(paths) + "</g>"
    return body if anim in ("g", None) else f'<g class="{anim}"{at(start)}>{body}</g>'


def rect(x, y, w, h, fill, rx=0, cls=None, delay=0.0, stroke=None):
    attrs = f' rx="{rx}"' if rx else ""
    attrs += f' stroke="{stroke}"' if stroke else ""
    attrs += f' class="{cls}"{at(delay)}' if cls else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"{attrs}/>'


def path(d, color, width=2.0, draw=None, dashed=False, cls=None, delay=0.0, cap="round"):
    """Stroked path. draw=seconds animates it on from its start."""
    attrs = f' stroke="{color}" stroke-width="{width}" stroke-linecap="{cap}" stroke-linejoin="round"'
    if dashed:
        attrs += ' stroke-dasharray="4 5"'
    if draw is not None:
        attrs += f' pathLength="1" class="d"{at(draw)}'
    elif cls:
        attrs += f' pathLength="1" class="{cls}"{at(delay)}'
    return f'<path d="{d}" fill="none"{attrs}/>'


def line(x1, y1, x2, y2, color, width=2, **kw):
    return path(f"M{x1} {y1}L{x2} {y2}", color, width, **kw)


def walker(d, color, width, delay):
    """A dot that travels the path, then pauses out of sight. Invisible at rest."""
    return path(d, color, width, cls="w", delay=delay)


def circle(x, y, r, color, fill="none", cls=None, delay=0.0):
    attrs = f' class="{cls}"{at(delay)}' if cls else ""
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{color}" stroke-width="2"{attrs}/>'


def card(w, h, p):
    return rect(0.5, 0.5, w - 1, h - 1, p["bg"], rx=14, stroke=p["edge"])


def write(name, w, h, title, content):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title">'
           f'<title id="title">{escape(title)}</title>{STYLE}{content}</svg>\n')
    (ASSETS / f"{name}.svg").write_text(svg)


HERO_TITLE = "Federico López. I build software. I take systems apart."


def hero(theme, mobile):
    p = THEMES[theme]
    w, h = (360, 300) if mobile else (840, 300)
    s = card(w, h, p)
    if mobile:
        x, first, second, big = 24, 112, 184, (64, 70)
        s += text("Software / systems / field notes", x, 42, 14, p["muted"], anim="f", start=0.1)
    else:
        x, first, second, big = 36, 132, 218, (88, 92)
        s += text("Software / systems / field notes", x, 46, 17, p["muted"], anim="f", start=0.1)
        s += text("Montevideo, UY", w - 36 - measure("Montevideo, UY", 15), 46, 15, p["muted"], anim="f", start=0.2)
    s += text("Federico", x - 3, first, big[0], p["ink"], "display", anim="g", start=0.25, stagger=0.035)
    s += text("López", x - 3, second, big[1], p["ink"], "display", anim="g", start=0.45, stagger=0.045)
    dot_x = x - 3 + measure("López", big[1], "display") + (9 if mobile else 11)
    dot_y, dot_r = second - (7 if mobile else 9), 6 if mobile else 7
    s += circle(dot_x, dot_y, dot_r, p["accent"], p["accent"], cls="h", delay=2.4)
    s += circle(dot_x, dot_y, dot_r, p["accent"], p["accent"], cls="p", delay=1.0)
    rule_y = 218 if mobile else 246
    s += line(x, rule_y, w - x, rule_y, p["line"], 1, draw=1.05)
    if mobile:
        s += text("I build software.", x, 252, 22, p["ink"], start=1.5)
        s += text("I take systems apart.", x, 281, 22, p["ink"], start=1.62)
    else:
        s += text("I build software. I take systems apart.", x, 281, 22, p["ink"], start=1.6)
        # A shared input branches into building, examining and writing.
        tx, bx = 540, 578
        s += circle(tx - 36, 138, 4, p["ink"], p["bg"], cls="p", delay=1.1)
        s += line(tx - 32, 138, bx, 138, p["ink"], 2, draw=1.15)
        s += line(bx, 138, bx, 78, p["line"], 2, draw=1.4)
        s += line(bx, 138, bx, 198, p["line"], 2, draw=1.4)
        for i, (y, label) in enumerate([(78, "Build"), (138, "Examine"), (198, "Write")]):
            t = 1.55 + i * 0.12
            s += line(bx, y, bx + 42, y, p["line"], 2, draw=t)
            s += text(label, bx + 88, y + 8, 22, p["ink"], start=t + 0.2)
        s += rect(bx + 44, 69, 18, 18, p["accent"], rx=3, cls="p", delay=1.75)
        s += circle(bx + 53, 138, 9, p["accent"], cls="p", delay=1.87)
        for i, (dy, length) in enumerate([(-7, 19), (0, 19), (7, 13)]):
            s += line(bx + 44, 198 + dy, bx + 44 + length, 198 + dy, p["accent"], 2, draw=1.99 + i * 0.06)
        s += walker(f"M{tx - 36} 138H{bx}V78H{bx + 42}", p["accent"], 5, 2.6)
    write(f'hero{"-mobile" if mobile else ""}-{theme}', w, h, HERO_TITLE, s)


REKON_TITLE = "REKON: agents explore attack paths, a person authorizes intrusive actions, evidence is validated. Conceptual diagram."


def rekon(theme, mobile):
    p = {**THEMES[theme], **REKON[theme]}
    w, h = (360, 176) if mobile else (840, 160)
    s = card(w, h, p)
    xs = [52, 180, 300] if mobile else [130, 420, 700]
    cy = 66
    routes = []
    for i, offset in enumerate([-24, 0, 24]):
        sx = xs[0] - 16
        d = f"M{sx} {cy + offset}C{sx + (xs[1] - sx) * 0.55} {cy + offset} {xs[1] - 60} {cy} {xs[1] - 22} {cy}"
        routes.append(d)
        s += circle(sx, cy + offset, 4, p["muted"], p["bg"], cls="p", delay=0.15 + i * 0.08)
        s += path(d, p["muted"], 1.5, draw=0.3 + i * 0.12)
    # Exploration may run freely; it stops at the authorization gate.
    for i, d in enumerate(routes):
        s += walker(d, p["accent"], 5, 2.4 + i * 1.1)
    s += rect(xs[1] - 19, cy - 22, 38, 44, p["accent"], rx=6, cls="p", delay=1.0)
    s += path(f"M{xs[1] - 9} {cy}l6 6 12-13", p["bg"], 3, draw=1.25)
    s += line(xs[1] + 20, cy, xs[2] - 16, cy, p["accent"], 2, draw=1.35)
    s += rect(xs[2] - 13, cy - 18, 26, 36, p["soft"], rx=4, cls="p", delay=1.75)
    for i, dy in enumerate([-8, 0, 8]):
        s += line(xs[2] - 7, cy + dy, xs[2] + 7, cy + dy, p["accent"], 2, draw=1.85 + i * 0.1)
    size = 19 if mobile else 22
    labels = ["Explore", "Authorize", "Validate"] if mobile else ["Attack paths", "Human authorization", "Validated evidence"]
    for i, (label, cx) in enumerate(zip(labels, xs)):
        s += text(label, cx - measure(label, size) / 2, 122, size, p["ink"], start=0.5 + i * 0.5)
    if mobile:
        s += text("Human approval before action.", 24, 156, 17, p["muted"], anim="f", start=2.0)
    write(f'rekon{"-mobile" if mobile else ""}-{theme}', w, h, REKON_TITLE, s)


AUTOP2P_TITLE = "AutoP2P: market input passes through operator rules and price limits to an update-or-hold decision with a recorded reason. Schematic, not live market data."


def autop2p(theme, mobile):
    p = THEMES[theme]
    w, h = (360, 176) if mobile else (840, 160)
    s = card(w, h, p)
    start, end = (24, 197) if mobile else (36, 490)
    top, bottom = 30, 92
    s += rect(start, top, end - start, bottom - top, p["soft"], cls="f", delay=0.1)
    s += line(start, top, end, top, p["accent"], 1, dashed=True, cls=None)
    s += line(start, bottom, end, bottom, p["accent"], 1, dashed=True)
    points = [(start, 74), (start + 28, 74), (start + 28, 58), (start + 62, 58), (start + 62, 69), (start + 95, 69), (start + 95, 46), (end, 46)]
    d = "M" + " L".join(f"{x} {y}" for x, y in points)
    s += path(d, p["accent"], 3, draw=0.35, cap="butt")
    # The marker walks the price line and never leaves the operator's band.
    s += walker(d, p["ink"], 7, 2.6)
    s += circle(end, 46, 4, p["accent"], p["bg"], cls="p", delay=1.3)
    tx = 222 if mobile else 552
    s += text("UPDATE / HOLD", tx, 58, 15 if mobile else 27, p["ink"], "display", anim="g", start=1.3, stagger=0.025)
    s += text("+ a reason", tx, 83, 18 if mobile else 23, p["muted"], start=1.75)
    s += text("Your rules. Your limits.", start, 126, 19 if mobile else 23, p["ink"], start=0.9)
    s += text("Schematic · not live prices", start if mobile else tx, 152 if mobile else 126, 16 if mobile else 17, p["muted"], anim="f", start=2.0)
    write(f'autop2p{"-mobile" if mobile else ""}-{theme}', w, h, AUTOP2P_TITLE, s)


PENTAGOO_TITLE = "Pentagoo Labs: a concrete problem becomes a product, applied AI or integration that is usable in production. Conceptual diagram."


def pentagoo(theme, mobile):
    p = THEMES[theme]
    w, h = (360, 176) if mobile else (840, 160)
    s = card(w, h, p)
    xs = [62, 180, 294] if mobile else [140, 420, 700]
    cy = 58
    track = f"M{xs[0]} {cy}H{xs[2]}"
    s += line(xs[0] + 14, cy, xs[1] - 16, cy, p["line"], 2, draw=0.35)
    s += line(xs[1] + 16, cy, xs[2] - 16, cy, p["line"], 2, draw=0.95)
    s += walker(track, p["accent"], 6, 2.4)
    s += circle(xs[0], cy, 12, p["accent"], p["bg"], cls="p", delay=0.15)
    s += path(f"M{xs[0] - 4} {cy - 4}a4 4 0 1 1 5 4v3M{xs[0] + 1} {cy + 7}v.5", p["accent"], 2, cls="f", delay=0.25)
    s += rect(xs[1] - 13, cy - 13, 26, 26, p["soft"], rx=5, cls="p", delay=0.75)
    s += path(f"M{xs[1] - 6} {cy - 5}l-4 5 4 5M{xs[1] + 6} {cy - 5}l4 5-4 5", p["accent"], 2, cls="f", delay=0.9)
    s += circle(xs[2], cy, 12, p["accent"], p["accent"], cls="p", delay=1.35)
    s += path(f"M{xs[2] - 5} {cy}l3.5 3.5 7-7.5", p["bg"], 2.5, draw=1.5)
    size = 18 if mobile else 22
    labels = ["Problem", "Build", "Production"] if mobile else ["A concrete problem", "Product · AI · integration", "Usable in production"]
    for i, (label, cx) in enumerate(zip(labels, xs)):
        s += text(label, cx - measure(label, size) / 2, 112, size, p["ink"], start=0.3 + i * 0.6)
    if mobile:
        s += text("Products · applied AI · integrations", 24, 150, 16, p["muted"], anim="f", start=1.9)
    write(f'pentagoo{"-mobile" if mobile else ""}-{theme}', w, h, PENTAGOO_TITLE, s)


def divider(theme, mobile):
    p = THEMES[theme]
    w, h = (360, 16) if mobile else (840, 16)
    s = line(1, 8, w - 1, 8, p["line"], 1, draw=0.1)
    s += line(1, 8, 48, 8, p["accent"], 3, draw=0.0)
    s += walker(f"M1 8H{w - 1}", p["accent"], 3, 1.2)
    write(f'divider{"-mobile" if mobile else ""}-{theme}', w, h, "Section divider", s)


if __name__ == "__main__":
    count = 0
    for theme in THEMES:
        for mobile in (False, True):
            for build in (hero, rekon, autop2p, pentagoo, divider):
                build(theme, mobile)
                count += 1
    print(f"Generated {count} animated SVGs from bundled fonts.")
