# Set the Limit — setthelimit.com

How fast should we build AI? Everyone has a speed limit. A three-minute, rigorously fair
compass: 16 propositions scored 0–100, a personal SPEED LIMIT sign, a road-conditions
diamond, and a map of the debate with the predicted positions of public figures and the
crowd. Web and mobile, no account, no backend required.

## Run

- Locally: serve `site/` (any static server) and open `index.html`. The Claude Code launch
  config "setthelimit" serves it on port 8766.
- Published prototype: see `PROGRESS.md` for the artifact URL.
- Real deployment: copy `site/` to any static host under setthelimit.com. Add `og.png`
  (render `site/og.svg` at 1200×630) and point the `og:image` meta in `index.html` at it.

## Layout

| Path | Role |
|---|---|
| `PLAN.md` | Decisions (name, domain, axes, metaphor, fairness protocol), phases, resume notes. |
| `PROGRESS.md` | What has been done and what comes next. Read this first when resuming. |
| `content/propositions.vN.json` | The propositions (source of truth). Highest N wins. |
| `research/figures-*.json` | Per-figure dossiers: sources and predicted answers with confidence. |
| `research/review-v1.md` | Adversarial fairness review (halt side, build-fast side, plain English). |
| `research/context-2026.md` | Sourced briefing on the state of the debate, September 2026. |
| `site/` | The site. `content.js`, `figures.js`, `crowd.js` are generated. |
| `tools/build-content.js` | Regenerates `site/content.js` and `site/figures.js`. |
| `tools/check-figures.js` | Validates research JSON and prints each figure's computed coordinates. |
| `tools/snapshot-crowd.js` | Builds `site/crowd.js` from exported run documents (dated, counted). |

## Scoring in one paragraph

Each item belongs to the danger axis (X, "road conditions"), the speed axis (Y), or the
profile. `dir` says whether agreeing moves the score up or down its axis; `weight` scales
it. An axis score is the weighted mean of answered items after flipping the reversed
ones; skipped items are excluded; at least three answers per axis are required. Figures
are placed by running the same scoring on their predicted answers, so a content change
moves everyone consistently. Agreement with a figure counts items within 20 points.

## Share links

`?r=` carries the 2-character base36 value of every item in content order (`--` =
skipped, `__` = unanswered). `#/shared` renders it. When the reader then takes the test,
their result shows the sender's dot and the number of propositions they agree on.

## Licence

Code: MIT (see LICENSE). Propositions, steelmen, figure dossiers, reviews and audits (`content/`, `research/`):
CC BY 4.0 — reuse them, credit "Set the Limit (setthelimit.com)". Corrections are welcome as issues or pull requests.
