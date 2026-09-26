# Federico López — Software, systems & field notes

The name is the identity; products and writing are the evidence. This profile and
federicolopez.uy are one personal publication: build software, examine systems,
write down what you find. The final iteration follows the user's request for a
personal developer/hacker blog rather than an institutional portfolio.

## Direction

The September 2026 redesign keeps the personal-notebook structure and adds
kinetic editorial motion: the name assembles glyph by glyph, rules and branches
draw themselves, and each product diagram runs its own mechanism. Motion explains
rather than decorates. There is still no terminal performance, fake telemetry,
particle field or status badge.

Bricolage Grotesque Bold gives the name an individual editorial voice; IBM Plex
Sans keeps the diagrams readable. Fonts are bundled under their OFL licenses and
outlined in SVG. No remote font requests or visitor-installed font assumptions.
Illustrations sit on quiet rounded cards in a paper/graphite palette with a
cobalt accent; REKON's authorization boundary uses restrained red. All text
colours are at least 4.5:1 against their card in both themes.

Five compositions, each at desktop and mobile width and in light and dark:
hero, REKON, AutoP2P, Pentagoo Labs and a thin section divider. Their text and
links remain in native Markdown. The products keep distinct roles; no client,
revenue, uptime or benchmark filler.

## Motion

- Motion is CSS inside each SVG (`STYLE` in `scripts/generate_assets.py`): no
  scripts, SMIL or external requests.
- Intro keyframes only declare `from`, so an element's own styles are its final
  frame. Every intro uses `animation-fill-mode: both` and finishes in about 2.5 s.
- `prefers-reduced-motion: reduce` switches every animation off and shows the
  final composition immediately. Renderers without CSS animation show it too.
- Each composition has one slow ambient loop (6–7 s, low contrast). It is
  invisible at rest: a walker dot that travels a path and then leaves it, or a
  halo that fades out. In REKON, the walkers stop at the authorization gate; in
  AutoP2P, the walker never leaves the operator's price band.
- Chromium starts the animation of an offscreen `<img>` SVG when it scrolls
  into view, so the lower diagrams play when the reader reaches them.

## Public references and factual scope

- Anthony Fu's profile/portfolio: identify the person and attach claims to work.
- Bartosz Ciechanowski: diagrams should explain a mechanism, not decorate a page.
- `https://labs.pentagoo.uy/`: the current public site identifies Federico as
  founder/technical director and calls Pentagoo Labs his software factory. That
  evidence supersedes the earlier uncertainty about the studio's current role.
- `https://rekon.sh/en/`: CTO and creator of ARGUS; human authorization and
  reproducible evidence. No inferred REKON founder title or credentials.
- `https://autop2p.dev/en/`: v2, operator rules, ads/orders/chat and no custody.
  The live page differs from indexed beta copy; live HTML was used for current
  facts. The product overview repository is not represented as engine source.

Source sites were inspected, not copied. No private product repository was read.
The person's account biography, location, pins and settings were not modified.

## GitHub renderer

The Markdown API preserves picture/source/media/srcset/alt and image width.
GitHub rewrites color-scheme sources at runtime; combined width/theme sources
proved unreliable. The implementation therefore uses two linked pictures:

- Supported `#gh-light-mode-only` / `#gh-dark-mode-only` fragments on the
  wrapping **anchor** choose the theme; GitHub's CSS selects its `href`.
- A width-only source selects a compact illustration below 1000 viewport pixels.
  This accounts for the sidebar: at 768px, the actual profile article is 398px wide.
- The short navigation links directly to writing, projects and LinkedIn.
  Published testing found inconsistent fragment scrolling in GitHub’s repository
  view, so the final version avoids depending on its in-page anchor handling.

No arbitrary CSS, JavaScript, iframe, external renderer, widget or runtime
service. Generic Markdown viewers may display both themed images; GitHub is the
delivery target. All essential identity/project/contact text remains native.

See GitHub's [theme fragments](https://github.blog/changelog/2021-11-24-specify-theme-context-for-images-in-markdown/)
and [picture support](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github).

## Maintenance

Edit README copy normally. Edit visual copy, geometry and palettes in
`scripts/generate_assets.py`, then run `uv run scripts/generate_assets.py`.
It creates all 20 SVGs deterministically from the bundled fonts. No credentials,
cron, external widgets or bot commits. The obsolete daily generators/workflows
were removed in the initial implementation after reference checks.

Review at 375/768/1440 in both themes and both GitHub surfaces. Seek frames
(0 / 0.8 / 1.6 / 2.5 / 4 s) and compare reduced motion against the rest frame.
Check SVG bounds,
loaded images, OS-vs-GitHub theme mismatch, contact anchors, native text and
no horizontal overflow. Keep local previews distinct from published screenshots.
