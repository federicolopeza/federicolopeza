# /// script
# requires-python = ">=3.10"
# dependencies = ["fonttools==4.59.2"]
# ///
"""Static self-contained SVGs. Run: uv run scripts/generate_assets.py.
Edit copy and geometry here. Outlined bundled OFL fonts need no viewer fonts.
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
    "light": dict(bg="#F7F8FA", ink="#22252D", muted="#5C626E", line="#CDD2DB", accent="#2455D6", soft="#E5EBFA"),
    "dark": dict(bg="#17191E", ink="#F0F1F4", muted="#ABB2C0", line="#444B59", accent="#9EB7FF", soft="#27334F"),
}


def text(value, x, y, size, color, face="body"):
    font = FONTS[face]
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    scale, cursor, paths = size / font["head"].unitsPerEm, 0, []
    for character in value:
        name = cmap[ord(character)]
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        path = pen.getCommands()
        if path:
            paths.append(f'<path transform="translate({cursor})" d="{path}"/>')
        cursor += font["hmtx"][name][0]
    return f'<g fill="{color}" aria-label="{escape(value)}" transform="translate({x} {y}) scale({scale:.6f} {-scale:.6f})">' + "".join(paths) + "</g>"


def rect(x, y, w, h, fill):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>'


def line(x1, y1, x2, y2, color, width=2, dashed=False):
    dash = ' stroke-dasharray="4 5"' if dashed else ""
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="{width}"{dash}/>'


def circle(x, y, r, color, fill="none"):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{color}" stroke-width="2"/>'


def write(name, w, h, title, content):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title>{content}</svg>\n'
    (ASSETS / f"{name}.svg").write_text(svg)


def monogram(x, y, scale, ink, accent):
    # F/L share a construction grid; a deliberate gap exposes their join.
    return f'<g transform="translate({x} {y}) scale({scale})">' + \
        f'<path d="M0 0H160V32H32V68H114V100H32V160H0Z" fill="{ink}"/>' + \
        f'<path d="M128 52H160V128H224V160H128Z" fill="{accent}"/>' + \
        f'<path d="M116 45V172M116 172H224" fill="none" stroke="{accent}" stroke-width="1.5" stroke-dasharray="4 5"/>' + '</g>'


def hero(theme, mobile):
    p = THEMES[theme]
    w, h = (360, 286) if mobile else (840, 286)
    s = rect(0, 0, w, h, p["bg"])
    if mobile:
        s += text("Software / systems / field notes", 24, 34, 14, p["muted"])
        s += text("Federico", 21, 105, 64, p["ink"], "display")
        s += text("López", 21, 175, 70, p["ink"], "display")
        s += circle(227, 168, 6, p["accent"], p["accent"])
        s += line(24, 201, 336, 201, p["line"], 1)
        s += text("I build software.", 24, 236, 23, p["ink"])
        s += text("I take systems apart.", 24, 267, 23, p["ink"])
    else:
        s += text("Software / systems / field notes", 32, 37, 17, p["muted"])
        s += text("Federico", 27, 125, 86, p["ink"], "display")
        s += text("López", 27, 207, 90, p["ink"], "display")
        s += circle(293, 199, 7, p["accent"], p["accent"])
        # A shared input branches into building, examining and writing.
        s += line(514, 130, 550, 130, p["ink"], 2)
        s += line(550, 70, 550, 190, p["line"], 2)
        for y, label in [(70, "Build"), (130, "Examine"), (190, "Write")]:
            s += line(550, y, 594, y, p["line"], 2)
            s += text(label, 632, y+7, 22, p["ink"])
        s += rect(594, 61, 18, 18, p["accent"])
        s += circle(603, 130, 10, p["accent"])
        s += line(594, 184, 613, 184, p["accent"], 2)
        s += line(594, 191, 613, 191, p["accent"], 2)
        s += line(594, 198, 608, 198, p["accent"], 2)
        s += line(32, 235, 808, 235, p["line"], 1)
        s += text("I build software. I take systems apart.", 32, 269, 23, p["ink"])
    write(f'hero{"-mobile" if mobile else ""}-{theme}', w, h, "Federico López. Software, systems and field notes.", s)


def rekon(theme, mobile):
    p = THEMES[theme].copy()
    if theme == "light":
        p.update(accent="#AF354A", soft="#F6DEE3")
    else:
        p.update(accent="#FF9CAC", soft="#442B3B")
    w, h = (360, 160) if mobile else (840, 142)
    s = rect(0, 0, w, h, p["bg"])
    xs = [48, 178, 312] if mobile else [130, 420, 696]
    cy = 62 if mobile else 60
    for offset in [-22, 0, 22]:
        s += circle(xs[0]-15, cy+offset, 4, p["muted"])
        s += line(xs[0]-10, cy+offset, xs[1]-22, cy, p["muted"])
    s += rect(xs[1]-19, cy-22, 38, 44, p["accent"])
    s += f'<path d="M{xs[1]-9} {cy}l6 6 12-13" fill="none" stroke="{p["bg"]}" stroke-width="3"/>'
    s += line(xs[1]+20, cy, xs[2]-16, cy, p["accent"])
    s += rect(xs[2]-13, cy-18, 26, 36, p["soft"])
    for dy in [-8, 0, 8]:
        s += line(xs[2]-7, cy+dy, xs[2]+7, cy+dy, p["accent"], 2)
    size = 19 if mobile else 22
    labels = [("Explore", xs[0]-28), ("Authorize", xs[1]-34), ("Validate", xs[2]-29)] if mobile else [("Attack paths", 38), ("Human authorization", 305), ("Validated evidence", 598)]
    for label, x in labels:
        s += text(label, x, 111, size, p["ink"])
    if mobile:
        s += text("Human approval before action.", 23, 143, 18, p["muted"])
    write(f'rekon{"-mobile" if mobile else ""}-{theme}', w, h, "REKON — exploration, human authorization, validated evidence. Conceptual diagram.", s)


def autop2p(theme, mobile):
    p = THEMES[theme]
    w, h = (360, 160) if mobile else (840, 142)
    s = rect(0, 0, w, h, p["bg"])
    start, end = (24, 197) if mobile else (38, 490)
    top, bottom = 29, 88
    s += rect(start, top, end-start, bottom-top, p["soft"])
    s += line(start, top, end, top, p["accent"], 1, True)
    s += line(start, bottom, end, bottom, p["accent"], 1, True)
    points = [(start, 70), (start+28, 70), (start+28, 55), (start+62, 55), (start+62, 66), (start+95, 66), (start+95, 44), (end, 44)]
    d = 'M'+' L'.join(f'{x} {y}' for x, y in points)
    s += f'<path d="{d}" fill="none" stroke="{p["accent"]}" stroke-width="3"/>'
    s += circle(end, 44, 4, p["accent"], p["bg"])
    tx = 224 if mobile else 552
    s += text("UPDATE / HOLD", tx, 57, 15 if mobile else 27, p["ink"], "display")
    s += text("+ a reason", tx, 81, 18 if mobile else 23, p["muted"])
    s += text("Your rules. Your limits.", start, 122 if mobile else 121, 19 if mobile else 23, p["ink"])
    if mobile:
        s += text("Schematic · not live prices", start, 145, 17, p["muted"])
    else:
        s += text("Schematic · not live prices", tx, 121, 17, p["muted"])
    write(f'autop2p{"-mobile" if mobile else ""}-{theme}', w, h, "AutoP2P — decisions bounded by operator rules, with a recorded reason. Schematic, not market data.", s)


if __name__ == "__main__":
    for theme in THEMES:
        for mobile in (False, True):
            hero(theme, mobile)
            rekon(theme, mobile)
            autop2p(theme, mobile)
    print("Generated 12 SVGs from bundled fonts.")
