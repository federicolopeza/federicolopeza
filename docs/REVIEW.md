# Redesign review — 2026-09-17

Implementation and prepublication review. The initial Git working tree was clean.
No account settings or private product repositories were accessed. The user
subsequently authorized commit and push for both the profile and personal site.

## Factual decisions

| Item | Evidence and treatment |
| --- | --- |
| CTO at REKON; creator of ARGUS | Explicit on the [public REKON team page](https://rekon.sh/). Kept; did not infer a founder title. |
| REKON workflow | Public site describes AI-assisted exploration, human authorization for intrusive actions and reproducible evidence. Kept as a description of the approach, not an independent performance certification. |
| AutoP2P | [Current English site](https://autop2p.dev/en/) and [public overview](https://github.com/federicolopeza/binance-p2p-bot) support repricing, operator rules, update/hold reasons and the trading workspace. Public copy says funds stay on Binance. No financial outcomes promised. |
| Product lifecycle | Indexed pages still say invite-only beta; the current page offers open signup. Omitted beta, pricing, trial length and changing strategy counts. |
| Metrics | Removed 110 repos, 2.2k tests, 71 ADRs, 291 modules, 17.7k audited files and the supposed 30-day activity graph. No public auditable evidence for those figures or that time series was established. |
| Other claims | Removed scale, delivery-in-days, always-online status, SHA-256 evidence-chain detail and service capability lists that were not independently established for this profile. |
| Pentagoo | Its site still responds. Removed from the featured work to focus the personal identity; this is not a claim that the business has closed. |
| Contact | Kept the LinkedIn identity linked by REKON and the personal site. Removed `federico@pentagoo.uy`: mailbox validity and preferred personal use were not established. No replacement address invented. |
| Exploration | Reviewed the public Artificial Analysis README, CLI and dashboard source. Described it as a small Python tool, not an original benchmark or an AI platform. |
| Other public repos | Reviewed TweetWipe, Universal Weather Bot and Reddit Content Downloader READMEs. Omitted them for focus. TweetWipe explicitly credits its TweetXer origin; downloader documentation still contains placeholder links. The apps.apple.com fork is not featured. |

Only public sources were used. The AutoP2P GitHub repository is a product
overview, not the engine source; the link says so explicitly. REKON research
links to the team's blog without attributing every article to Federico.

## Visual verification

The **before** screenshots are the live, published GitHub profile.
The **after** screenshots are a browser-local preview: README HTML returned by
GitHub's Markdown API, inserted into the real profile/repository DOM with its
actual styles, sidebar and container. SVG requests are fulfilled from local
files. These are not screenshots of a published redesign. Final post-push
asset delivery and GitHub's repository-link processing remain to be verified.

The review artifacts are kept locally in `.ai-collab/review/` (already ignored
by this repository). They are not production assets. Filenames follow
`profile-375-dark.png` and `repository-1440-light.png`; `*-context.png` captures
the surrounding GitHub interface. `before.png` and `before-mobile.png` preserve
the original live profile. `render-checks.json` records the rendered dimensions,
selected image variants and overflow results. The API does not add GitHub’s
final heading anchors, so the local anchor check reproduces heading IDs; native
anchor behavior is also checked on the published page after push.

| Viewport | Profile article | Repository article | Modes |
| --- | ---: | ---: | --- |
| 375px | 293px | 309px | light, dark |
| 768px | 398px | 406px | light, dark |
| 1440px | 846px | 838px | light, dark |

Corrections after the first visual pass:

- Increased the compact breakpoint from 600 to 1000px to account for the sidebar.
- Separated GitHub theme selection from width selection; checked the actual
  `currentSrc` and visibility, rather than assuming the sources worked.
- Separated the accent on Ó from the first line of the wordmark.
- Enlarged compact diagram labels and adjusted desktop figure margins.
- Differentiated the authorization boundary from AutoP2P's bounded decision.
- Added native paragraph spacing below illustrations.
- Captured the complete page before cropping the README, avoiding a sticky
  GitHub navigation bar obscuring the visual-review screenshots.

Validation includes all 12 layout/theme combinations, asset loading and
selection, horizontal overflow, native anchors, contrast, SVG bounds, image
fallback, deterministic regeneration and Git whitespace checks. No animation
needs a reduced-motion alternative. No essential information requires images.

HTTP checks returned 200 for the product pages, REKON English blog, personal
site and both linked public repositories. LinkedIn rejects automated requests
with HTTP 999; the identity is corroborated by REKON's public team link, but
profile contents and message delivery were not verified.

## Suggested account changes — not applied

Bio:

> CTO at REKON. Creator of ARGUS. Building AutoP2P. Product engineering, automation & offensive security. Montevideo.

Pin only these for now:

1. [binance-p2p-bot](https://github.com/federicolopeza/binance-p2p-bot): the
   public AutoP2P overview; review its outdated trial/strategy copy separately.
2. [artificial_analysis](https://github.com/federicolopeza/artificial_analysis):
   inspectable code behind the small tool featured here.

Do not manufacture a REKON repository or fill all six slots. No relevant public
REKON code repository was found in the user's public repository inventory.
The existing TweetWipe pin does not represent the work emphasized here.

Also suggested: replace the truncated shell-command bio, set the location to
Montevideo, Uruguay, and replace the sidebar's Pentagoo link with the personal
site if that remains the preferred destination. The personal site itself still
contains unverified counters; it was inspected but not modified in this task.

Final local checks: all 12 SVGs are self-contained and within their viewboxes;
regeneration is deterministic; foreground/text contrast against figure surfaces
is at least 5.48:1. The 12 profile/repository viewport/theme combinations load the
correct three visible illustrations without horizontal overflow. Explicit GitHub
themes also work when they disagree with the OS theme. Gitleaks, TruffleHog
(offline detection) and credential-pattern checks found no secrets in the staged
changes. The final published renderer is checked separately after push.

Post-push verification confirmed all assets load from GitHub. The profile view
did not scroll to unprefixed Markdown hashes, so the three navigation links now
target GitHub’s observed `user-content-` heading IDs directly. This uses native
fragment navigation in both profile and repository views.
