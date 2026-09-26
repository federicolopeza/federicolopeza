# Review and handoff

## September 26, 2026: brand alignment and motion

### Changes

- The profile now uses the federicolopez.uy brand: "Build. Break. Bound.", the
  void/paper tokens, per-product colours, Geist / Geist Mono / Instrument Serif
  italic and the bracket-and-point mark.
- Roles and dates come from the site's `lib/cv.ts`, which is sourced from
  Federico's public LinkedIn, exported 2026-09-26. REKON is now "Co-founder &
  CTO", as on the live site and LinkedIn.
- The contact email is the one the live site publishes (provided by Federico for
  the site). It supersedes the September 18 decision not to republish an address.
- `github.com/federicolopeza/artificial_analysis` returns a public 404. It was
  removed from the README and is not suggested as a pin. The website still links
  to it; that belongs to the website repository.

### Verification

- The generator emits 24 animated SVGs (6 compositions × 2 widths × 2 themes),
  all ≤ 52 KB. Two runs produce identical hashes; `xmllint` passes. They contain
  no scripts, and their only URL is the SVG namespace.
- A Playwright (Chromium) capture seeked every animation at 0, 0.8, 1.6, 2.5
  and 4 s. No painted element leaves its viewBox.
- Rest frame: intros are finished and infinite loops cancelled. It was compared
  with a reduced-motion render and with a render with `<style>` removed. The two
  renders are identical to each other. Their only difference from the rest frame
  is 1 px antialiasing on composited edges. No walker or halo shows without CSS.
- The GitHub Markdown API preserves `picture`, `source`, alt text and width. Local
  previews at 375, 768 and 1440 px in both themes load every image, with no
  horizontal overflow. Every README link returns 200 (LinkedIn answers bots with 999).
- An independent review found no blocking issue. Its fixes are applied: hidden-at-rest
  attributes, REKON route starts, the native name, docs accuracy and this
  heading structure.
- Not verified: Safari, Firefox, the GitHub mobile app and published captures.
  Those come after the merge; the GitHub image cache can delay new SVGs.
- Known trade-off: GitHub wraps every image in a link, so the decorative dividers
  are links with empty alt text.

### Suggested account changes (not applied)

Bio:

> Co-founder & CTO @ REKON · Creator of ARGUS and AutoP2P · Founder @ Pentagoo Labs · Build. Break. Bound. · Montevideo

Pins: `binance-p2p-bot`, the public AutoP2P overview. Do not fill the other slots
with weaker work. Suggested website: https://federicolopez.uy/.

## September 18, 2026


### Corrections

Removed unsubstantiated revenue, user, uptime, vulnerability, module/test/ADR and
performance counters. Removed fake telemetry, obsolete SVGs, terminal.py and the
two daily decoration workflows. The README no longer depends on external widgets.

Public evidence supports CTO at REKON and creator of ARGUS. The current Pentagoo
Labs page now explicitly supports founder/technical director and ownership of the
software factory, so the studio is included. The old inconsistent email addresses
are not republished; use the corroborated LinkedIn and studio contact links.

AutoP2P is described as a merchant workspace with operator-defined repricing,
recorded reasons and funds staying on Binance. Its GitHub repository is a product
overview, not the engine's source. The article on Federico's site introduces v2
in English and Spanish and links to current product details. Historical architecture
writing is labeled as such. No private repository details were consulted.

### Verification

- 12 standalone SVGs, outlined local fonts, no scripts or external dependencies.
- All visible SVG text remains within the viewbox. Separate compact compositions
  load at narrow widths rather than shrinking a desktop-only banner.
- Preview matrix: profile and repository containers at 375, 768 and 1440px in
  both light/dark themes. Actual GitHub CSS/DOM plus its Markdown API and local
  asset interception were used before push; those are explicitly previews.
- Visible illustrations load without horizontal overflow. Theme selection also
  works when explicit GitHub theme differs from operating-system preference.
- Published fragment scrolling proved inconsistent between GitHub surfaces.
  The final navigation uses direct writing/projects/contact destinations.
- Final published verification and screenshots are recorded separately after push.
- Scoped staged/commit secret scans precede publication.

Screenshots and JSON reports are ignored local artifacts under
`.ai-collab/review/`. `profile-before-readme.png` / `website-before*.png` are the
original live versions. `profile-*` are README previews, `i18n-*` / `journal-*`
are local website previews, and `published-*` are actual deployed captures.
The website has its own implementation and verification notes in
`../federicolopez.uy/docs/REDESIGN.md`.

### Suggested account changes — not applied

Bio (under GitHub's length limit):

> Founder @ Pentagoo Labs. CTO @ REKON / creator of ARGUS. Building AutoP2P. Software, systems & field notes. Montevideo.

Pins:

1. `binance-p2p-bot`: the public AutoP2P overview. Its own older product copy can
   be reviewed separately; it was not modified as part of this task.
2. `artificial_analysis`: inspectable Python/Streamlit code behind the small tool.

No public REKON source repository was found to recommend as a pin. Do not fill
all six slots with weaker work. Suggested location: Montevideo, Uruguay; suggested
profile website: https://federicolopez.uy/. The existing account settings remain
unchanged. Both repositories were committed/pushed only after explicit authorization.
