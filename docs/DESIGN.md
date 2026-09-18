# Federico López — Software, systems & field notes

The name is the identity; products and writing are the evidence. This profile and
federicolopez.uy are one personal publication: build software, examine systems,
write down what you find. The final iteration follows the user's request for a
personal developer/hacker blog rather than an institutional portfolio.

## Direction

Three directions were considered: a systems atlas dominated by diagrams, a
large typographic portfolio, and a personal technical notebook. The notebook is
the final choice: the human name stays prominent, while current writing and
inspectable work appear immediately. A compact branch graphic joins building,
examining and writing. It describes the practice rather than pretending to be
live infrastructure. No terminal performance, fake telemetry or status badges.

Bricolage Grotesque Bold gives the name an individual editorial voice; IBM Plex
Sans keeps the diagrams readable. Fonts are bundled under their OFL licenses and
outlined in SVG. No remote font requests or visitor-installed font assumptions.
The cool paper/graphite/cobalt palette matches the website. Dark variants retain
the same hierarchy; REKON's authorization boundary uses restrained red.

The banner is composed separately at desktop and mobile sizes. Each product has
a small explanatory diagram, with its text and actual links retained in native
Markdown. The profile introduces Federico, Pentagoo Labs, REKON/ARGUS, AutoP2P,
a current article, a historical engineering note and one small public code tool.
The products keep distinct roles; no client, revenue, uptime or benchmark filler.

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
- Native `user-content-` heading IDs are used for in-page navigation, observed
  and tested in actual published profile and repository views.

No arbitrary CSS, JavaScript, iframe, external renderer, widget or runtime
service. Generic Markdown viewers may display both themed images; GitHub is the
delivery target. All essential identity/project/contact text remains native.

See GitHub's [theme fragments](https://github.blog/changelog/2021-11-24-specify-theme-context-for-images-in-markdown/)
and [picture support](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github).

## Maintenance

Edit README copy normally. Edit visual copy, geometry and palettes in
`scripts/generate_assets.py`, then run `uv run scripts/generate_assets.py`.
It creates all 12 SVGs deterministically from the bundled fonts. No credentials,
cron, external widgets or bot commits. The obsolete daily generators/workflows
were removed in the initial implementation after reference checks.

Review at 375/768/1440 in both themes and both GitHub surfaces. Check SVG bounds,
loaded images, OS-vs-GitHub theme mismatch, contact anchors, native text and
no horizontal overflow. Keep local previews distinct from published screenshots.
