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
    "display": TTFont(ASSETS / "fonts/BarlowCondensed-SemiBold.ttf"),
    "body": TTFont(ASSETS / "fonts/Barlow-Regular.ttf"),
}
THEMES = {
    "light": dict(bg="#F0F2FA", ink="#172247", muted="#4E5976", line="#BCC4DA", accent="#3049CF", soft="#DDE4FF"),
    "dark": dict(bg="#171E32", ink="#EEF2FF", muted="#B5C0DC", line="#4D5C80", accent="#A8BAFF", soft="#273963"),
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
    w, h = (360, 304) if mobile else (840, 342)
    s = rect(0, 0, w, h, p["bg"])
    if mobile:
        s += text("FEDERICO", 22, 89, 90, p["ink"], "display")
        s += text("LÓPEZ", 22, 191, 102, p["ink"], "display")
        s += monogram(267, 142, .29, p["ink"], p["accent"])
        s += line(24, 218, 336, 218, p["line"], 1)
        s += text("Build systems.", 24, 249, 23, p["ink"])
        s += text("Question their limits.", 24, 278, 23, p["accent"])
    else:
        s += text("FEDERICO", 34, 124, 140, p["ink"], "display")
        s += text("LÓPEZ", 34, 263, 150, p["ink"], "display")
        s += monogram(570, 69, .97, p["ink"], p["accent"])
        s += line(38, 283, 802, 283, p["line"], 1)
        s += text("Build systems. Question their limits.", 38, 319, 26, p["ink"])
    write(f'hero{"-mobile" if mobile else ""}-{theme}', w, h, "Federico López — Build systems. Question their limits.", s)


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
    labels = [("Explore", xs[0]-28), ("Authorize", xs[1]-34), ("Validate", xs[2]-29)] if mobile else [("Explore attack paths", 38), ("Human authorization", 323), ("Reproducible evidence", 591)]
    for label, x in labels:
        s += text(label, x, 111, size, p["ink"])
    if mobile:
        s += text("Human approval before intrusive action.", 23, 143, 18, p["muted"])
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
    s += text("UPDATE / HOLD", tx, 57, 23 if mobile else 31, p["ink"], "display")
    s += text("+ a reason", tx, 81, 18 if mobile else 23, p["muted"])
    s += text("Your rules. Your limits.", start, 122 if mobile else 121, 19 if mobile else 23, p["ink"])
    if mobile:
        s += text("Decision schematic · no live prices", start, 145, 18, p["muted"])
    else:
        s += text("Decision schematic · no live prices", tx, 121, 17, p["muted"])
    write(f'autop2p{"-mobile" if mobile else ""}-{theme}', w, h, "AutoP2P — decisions bounded by operator rules, with a recorded reason. Schematic, not market data.", s)


if __name__ == "__main__":
    for theme in THEMES:
        for mobile in (False, True):
            hero(theme, mobile)
            rekon(theme, mobile)
            autop2p(theme, mobile)
    print("Generated 12 SVGs from bundled fonts.")
