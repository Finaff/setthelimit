# Set the Limit — plan and resume notes

**Task (the owner, 16 Sept 2026):** a credible, useful, viral site about the debate on
slowing down AI. Web + mobile. Unique visual identity. Compass-style result: where you
stand vs. other people and vs. at least 10 notable figures (predicted). Rigorous
propositions that Yudkowsky and an accelerationist would both call fair. Understandable
without technical background. Find a strong available URL and a hook. Iterate as long as
usage lasts; keep progress resumable. Non-negotiable: CREDIBLE, USEFUL, VIRAL.

## Decisions (locked unless a review overturns them)

- **Name:** Set the Limit. **Domain:** setthelimit.com (whois: no match on 16 Sept 2026;
  .org/.ai/.net checked too, see whois log). Not registered by us; the user registers.
- **Hook:** "How fast should we build AI? Everyone has a speed limit. Set yours in four
  minutes, and see where you stand next to Yudkowsky, Andreessen, LeCun, Hinton and the rest."
- **Metaphor:** a road. Two axes both sides accept:
  - X = **Road conditions**: how dangerous you believe the road is (clear ↔ black ice).
    Empirical beliefs about risk and controllability.
  - Y = **Speed**: the pace you'd set (full stop ↔ no limit). Prescriptions.
  Quadrants: flat out on a clear road (accelerationist) · flat out on ice (racing despite
  danger: "get there first") · parked on a clear road (slow for non-existential reasons:
  harms, power, jobs) · braking on ice (pause / halt).
  The dial's top reads "No limit" so the accelerationist end is a real position, not a
  missing one.
- **Primitive:** 0–100 slider per proposition (probability for forecasts, agreement for
  the rest), with "Skip / not sure" that never penalizes. Blind: no distributions shown
  until the end.
- **Fairness protocol:** equal numbers of items phrased in each direction; empirical vs.
  prescriptive kept separate; each item carries "In plain words" and two steelmen (why
  people agree / why people disagree) written to satisfy the side they represent;
  adversarial review by a Yudkowsky-steelman and an e/acc-steelman before ship.
- **Notable figures:** predictions from public statements, each with sources and a
  confidence; labelled as predictions; "Claim your dot" invites corrections.
- **Crowd:** the artifact with `db` collects anonymous runs (org-internal); the public
  build ships a `crowd.json` snapshot with its date and count. Never fabricate a crowd.
- **Viral loop:** the result link encodes your coordinates (`?x=..&y=..&a=..`) so a shared
  link renders your dot without any backend; share text; archetype names; "you agree
  with Yudkowsky on N of 24".
- **Visual identity:** highway signage. Overpass (the Google Fonts face descended from
  Highway Gothic) for everything sign-like; a serif for long reading; Overpass Mono for
  numbers. Palette: sign green, warning yellow, retroreflective white, asphalt greys, one
  red reserved for the danger end. Light and dark both designed.

## Decisions added 19 Sept 2026 (the owner)

- **Propositions v4:** 16 items, mirrored pairs, one claim per sentence (see the v4 changelog in
  `content/propositions.v4.json`). Minimum 3 answers per axis.
- **Claim your dot, automated with X:** a listed figure signs in with X (OAuth 2.0 + PKCE), the
  backend matches the *numeric* X user id (never the handle) against a closed list of the
  figures' accounts, they answer the 16 items, and their answers replace the prediction with
  "answered themselves on <date>". The prediction is kept beside the answer ("we predicted 40,
  they answered 52") and a per-figure prediction-accuracy score is shown. Claims are revocable
  and dated. Figures not on X: manual verification by email from a known institutional domain,
  same label on the page.
- **Anonymous first, public later:** everyone answers anonymously (nothing but the answers is
  stored). On the result page, an optional "Make my result public with X" signs in with X and
  attaches the run to the handle; opt-in only, deletable in one click, never the default. Later:
  "where the people you follow stand".
- **Sam Harris** joins the figures (17). His community is a candidate launch channel.
- **Backend:** one small Cloudflare Worker (`worker/`) serves the crowd collector, the crowd
  aggregate, the X sign-in, claims and public results. The static site stays static; the app
  talks to the Worker only when `window.STL_API` is set.
- **Order of work:** register setthelimit.com (the owner) → public git repo + static hosting →
  Worker (crowd + claim, same code) → X buttons → outreach via the figures and Sam Harris's
  community.

## Phases

1. Content v1 (propositions, plain words, steelmen) → `content/propositions.v1.json`. DONE.
2. Parallel agents: figure dossiers with sources (A: 7 figures, B: 7 figures); adversarial
   fairness + plain-English review of v1; domain/name check (done by lead).
3. Build the site (`site/`): landing, questionnaire, result, figures, methodology.
   Engine: scoring, archetypes, nearest figures, agreement splits, share link.
4. Integrate reviewed content v2 and figure predictions; publish artifact; seed nothing.
5. Iterate: FR translation, crowd snapshot pipeline, OG share card, accessibility pass,
   copy polish, second review round.

## Resume

- Read `PROGRESS.md` for the latest state and what to do next.
- Content lives in `content/`; site in `site/`; research in `research/`.
- Memory file: kept outside the repository
