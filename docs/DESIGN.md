# Federico López: Build. Break. Bound.

This profile is the GitHub edition of federicolopez.uy. It shares that site's
brand, tokens, type and facts, so a visitor moving between the two sees one
person and one identity. The site is the source of truth. When its brand or CV
changes, update the generator constants and the README copy to match it.

## Direction

The site's thesis is "the limit is part of the design". It becomes three verbs,
one per line of work, each in its product's colour:

- **Build**: Pentagoo Labs, teal.
- **Break**: REKON / ARGUS, red.
- **Bound**: AutoP2P, emerald.

Amber is the personal signal: the limit. The mark is two brackets (the boundary)
around one point (the decision).

Void (dark) and paper (light) come from `app/globals.css` on the site. Type is
Geist SemiBold for the name, Geist for reading, Geist Mono for technical labels
and Instrument Serif italic for voice. The fonts are bundled under their OFL
licenses and outlined in the SVGs. No remote font requests.

The motion is kinetic and editorial:

- the name assembles glyph by glyph and the mark draws its brackets;
- the trajectory bars grow in chronological order;
- each product diagram runs its own mechanism. REKON's probes stop at a human
  authorization gate. AutoP2P's price marker stays inside the operator's band.
  Pentagoo's problem is carried through a lattice into production.

There is no terminal performance, fake telemetry or status badge. Diagrams are
labeled as conceptual or schematic, never as live data.

Six compositions, each at desktop and mobile width and in light and dark:
hero, REKON, AutoP2P, Pentagoo Labs, trajectory and a thin divider. All
identity, project and contact text is also native Markdown. The trajectory has a
native table of roles and dates.

## Facts

- The roles, dates and product descriptions come from federicolopez.uy
  (`lib/cv.ts` and the home page). The site sources them from Federico's public
  LinkedIn (exported 2026-09-26) and the product sites: rekon.sh, autop2p.dev
  and labs.pentagoo.uy.
- There are no client, revenue, uptime, benchmark or certification claims.
- The contact email is the one the site publishes.

## Motion

- The motion is CSS inside each SVG (`STYLE` in `scripts/generate_assets.py`):
  no scripts, SMIL or external requests.
- Intro keyframes only declare `from`, so an element's own styles are its final
  frame. The intros use `animation-fill-mode: both` and finish within about 3 s.
- `prefers-reduced-motion: reduce` switches every animation off and shows the
  final composition immediately. A viewer that ignores `<style>` shows the same
  composition.
- The ambient loops are slow (6–7 s) and invisible at rest, also through an
  `opacity="0"` attribute. A walker dot travels a path and then leaves it; a halo
  fades out. A composition may have more than one walker, as REKON has one per
  attack path.
- Chromium starts the animation of an offscreen `<img>` SVG when it scrolls into
  view, so the lower diagrams play when the reader reaches them.

## GitHub renderer

The Markdown API preserves picture/source/media/srcset/alt and image width.
GitHub rewrites color-scheme sources at runtime; combined width/theme sources
proved unreliable. The implementation therefore uses two linked pictures:

- Supported `#gh-light-mode-only` / `#gh-dark-mode-only` fragments on the
  wrapping **anchor** choose the theme; GitHub's CSS selects its `href`.
- A width-only source selects a compact illustration below 1000 viewport pixels.
  This accounts for the sidebar: at 768px, the actual profile article is 398px wide.
- The short navigation links directly to email, the site and LinkedIn.
  Published testing found inconsistent fragment scrolling in GitHub’s repository
  view, so the final version avoids depending on its in-page anchor handling.

No arbitrary CSS, JavaScript, iframe, external renderer, widget or runtime
service. Generic Markdown viewers may display both themed images; GitHub is the
delivery target. All essential identity/project/contact text remains native.

See GitHub's [theme fragments](https://github.blog/changelog/2021-11-24-specify-theme-context-for-images-in-markdown/)
and [picture support](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github).

## Maintenance

Edit README copy normally. Edit visual copy, geometry, palette and timing in
`scripts/generate_assets.py`, then run `uv run scripts/generate_assets.py`. It
creates all 24 SVGs deterministically from the bundled fonts. There are no
credentials, cron jobs, external widgets or bot commits.

Review at 375, 768 and 1440 px in both themes. Seek the animation frames, and
compare the rest frame with a reduced-motion render and a render without
`<style>`. Also check SVG bounds, loaded images, mismatches between OS and
GitHub themes, native text, and horizontal overflow. Keep local previews
distinct from published screenshots.
