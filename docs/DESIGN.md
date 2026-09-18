# Federico López — Built / examined

The name is the identity. The products are its evidence. A short reading path:
person → REKON → AutoP2P → engineering perspective → contact.

## Direction

Three routes were considered:

- **Systems atlas:** diagrams as the main identity. Relevant, but made Federico
  look like an infrastructure project and demanded too much explanation.
- **Technical publication:** a restrained journal with annotations and essays.
  Credible, but too quiet for a memorable personal introduction.
- **Built / examined — selected:** a large condensed wordmark and a custom F/L
  construction. The separated join makes the build/question relationship visible.
  Product diagrams show where control sits, rather than pretending to be live UI.

The hero uses Barlow Condensed Semibold; diagram text uses Barlow Regular.
Both are bundled under the SIL Open Font License and converted to outlines.
Visitors need neither the fonts nor a remote font request. All essential copy
and links also exist as ordinary README text.

The palette uses pale blue paper `#F0F2FA`, navy ink `#172247`, secondary ink
`#4E5976`, structural lines `#BCC4DA`, and blue `#3049CF`. Dark counterparts
are defined in the generator. REKON's authorization boundary uses a restrained
red, related to its public identity; AutoP2P's bounded decision uses blue.
The meaning is also expressed in words and geometry, never color alone.

One signature, two explanatory figures, no animation. Native GitHub typography
carries the narrative. No badges, fake live statuses, service widgets or counters.

## References studied

- [Anthony Fu's profile](https://github.com/antfu) and
  [portfolio](https://antfu.me/): identify the person quickly and attach claims
  directly to work. Borrowed the prioritization, not the layout or graphics.
- [Bartosz Ciechanowski](https://ciechanow.ski/): a technical diagram should
  explain a mechanism. Neither graph here is decorative telemetry.
- [REKON](https://rekon.sh/) and [AutoP2P](https://autop2p.dev/en/): preserve the
  distinction between human-authorized security work and rule-driven automation.
  The profile synthesizes the products without reproducing their landing pages.

## GitHub implementation

GitHub's Markdown API preserves `picture`, `source`, `media`, `srcset`, `alt`
and image width. Its client rewrites color-scheme media conditions. Combining
theme and width in one source proved unreliable in the first browser pass.

The final implementation uses two linked pictures per illustration:

- GitHub's supported `#gh-light-mode-only` / `#gh-dark-mode-only` link fragments
  choose the theme. The fragment is deliberately on the wrapping **anchor**:
  GitHub's actual CSS selects `href`, not a bare image's `src`.
- Each picture uses an ordinary width-only source to select its compact SVG.
- The compact breakpoint is 1000 viewport pixels, accounting for GitHub's sidebar.
  At a 768px viewport the profile's article was only 398px wide.
- The fallback is the matching desktop image. Each image link opens its SVG.

References: [GitHub's theme-fragment support](https://github.blog/changelog/2021-11-24-specify-theme-context-for-images-in-markdown/)
and [picture support](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github).

No arbitrary README CSS, JavaScript, iframes, external render services or runtime
dependencies. On generic Markdown renderers without GitHub's theme CSS, both
theme variants may appear; GitHub is the delivery target.

## Maintenance

Edit copy in `README.md`. Edit visual copy, geometry and palettes in
`scripts/generate_assets.py`, then run:

```sh
uv run scripts/generate_assets.py
```

The script pins its sole generation dependency, fonttools, and uses the bundled
font files. Font sources: [Barlow](https://github.com/google/fonts/tree/main/ofl/barlow)
and [Barlow Condensed](https://github.com/google/fonts/tree/main/ofl/barlowcondensed).
Licenses live alongside the fonts. Generated SVGs are committed assets; GitHub
does not run the generator. Nothing needs scheduled refreshes or credentials.

There are intentionally no Actions workflows. The retired terminal workflow
installed a moving Git dependency and consumed `METRICS_TOKEN` to generate an
unreferenced GIF. Both it and the contribution-game workflow committed daily
with write permissions. Their assets and generators were removed together.
No account settings or secrets were changed.
