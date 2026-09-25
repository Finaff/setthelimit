# Review of `propositions.v5.json`: third fairness round

Reviewer role: third fairness editor, three voices (halt-side, build-side, plain language and
measurement), plus a check of the French edition for drift in meaning. The bar is the same as in
rounds one and two. Settled points are not reopened unless v5 created the problem. Every change
costs a re-prediction, so a finding has to change a score or remove a real ambiguity before it
earns a change.

- Reviewed: `content/propositions.v5.json`, `content/propositions.v5.fr.json`
- Test set: `research/figures-a.json` … `figures-f.json` (22 figures, v5 predictions)
- Proposed: `content/propositions.v5.1.proposed.json` and
  `content/propositions.v5.1.fr.proposed.json`. These are not applied. The names do not match
  `propositions.vN.json`, so the build tools ignore them.

## Verdict

**v5 is sound, with one scoring fault that must be fixed and one fairness fault that should be.**
Both editors accept 13 of the 16 items as worded.

1. **d15 must change (HIGH).** "…without ending humanity" makes the item non-monotonic. The
   people who fear the worst answer it *low*, because they expect the catastrophe to be total,
   and a low answer is scored toward a clear road. Yudkowsky answers 30 and loses 8.4 points on
   x. Kokotajlo loses 6.5. These are the two largest wrong-way pushes on the danger axis. The fix
   is to drop the clause and state the rung as "at least this bad", which keeps the owner's
   intent. It gets a new id, **d16**.
2. **s14 should change (MEDIUM).** "All work on AI more capable than today's" also freezes
   specialised medical and science AI. The pause side does not ask for that, and three halt-side
   figures hedge for exactly that reason. The "against" then charges the pause with those lost
   cures. Narrowed to "general-purpose AI", with "I would press it". It gets a new id, **s15**.
3. **Small edits, no new ids.** d11's plain and "against" are re-aimed at the item's question.
   The other three are one-sentence edits: d10 plain (misuse counts), d12 "for" (adds the
   evidence) and d14 "for" (a factual error).
4. **Kept.** The d12/d14 correlation (−0.95) reflects a polarised sample, not a wording fault.
   The danger axis is balanced in meaning as well as arithmetic. Every `prob` item is a forecast
   and every `agree` item is a judgement or prescription. The 20-year window on d10 stays (see
   the note on d10).

Balance after the changes is unchanged: danger 3/3 at 4.0/4.0, speed 4/4 at 5.0/5.0.

---

## 1. Item statistics (v5, 22 figures)

"r rest" is the correlation of the keyed item with its own axis computed without it. "effect"
is the largest single-item move on any figure: axis score without the item minus axis score
with it.

| id | w | dir | mean | SD | min–max | r rest | ≥65 | ≤35 | mid | low-conf | largest effect |
|---|---|---|---|---|---|---|---|---|---|---|---|
| d15 | 1 | + | **29** | **17** | 6–60 | 0.84 | **0** | 15 | 7 | **15** | **−8.4 Yudkowsky** (wrong way) |
| d10 | 1.5 | + | 46 | 35 | 2–97 | 0.96 | 10 | 10 | 2 | 3 | +6.0 Marcus |
| d13 | 1.5 | − | 35 | 37 | 2–95 | 0.87 | 8 | 14 | **0** | 0 | +11.3 Altman (toward ice) |
| d12 | 1.5 | + | 48 | 30 | 5–97 | 0.93 | 7 | 10 | 5 | 5 | +5.1 Amodei |
| d14 | 1.5 | − | 48 | 30 | 2–95 | 0.94 | 8 | 8 | 6 | 1 | +4.4 Musk |
| d11 | 1 | − | 53 | 21 | 5–85 | 0.91 | 8 | 5 | 9 | **12** | +3.7 Tegmark |
| s14 | 1.5 | − | 42 | 37 | 1–97 | 0.90 | 7 | 11 | 4 | 6 | +7.2 Altman |
| s4 | 1 | − | 49 | 32 | 3–98 | 0.92 | 10 | 8 | 4 | 3 | |
| s5 | 1 | + | 52 | 32 | 5–97 | 0.80 | 9 | 8 | 5 | 4 | |
| s6 | 1 | − | 55 | 35 | 4–97 | 0.96 | 11 | 9 | 2 | 2 | |
| s8 | 1.5 | − | 58 | 35 | 3–99 | 0.95 | 13 | 7 | 2 | 1 | |
| s10 | 1.5 | + | 41 | 30 | 3–92 | 0.94 | 7 | 12 | 3 | 6 | |
| s11 | 1 | + | 43 | 33 | 2–97 | 0.82 | 6 | 11 | 5 | 4 | |
| s13 | 1.5 | + | 30 | 34 | 1–95 | 0.92 | 6 | 15 | 1 | 1 | |

The two axes correlate at −0.82. Every danger item correlates between 0.75 and 0.95 with every
other danger item. This is an elite, polarised sample predicted by agents who knew each figure's
camp (review-v2's caveat still applies). High correlations prove little. What the data can show
is floor and ceiling, which items push a figure the wrong way, and where predictors could not
tell what the sentence asks.

---

## 2. Pass 1: halt-side editor (a careful Yudkowsky/Russell/Tegmark ally)

| id | verdict | finding |
|---|---|---|
| **d15** | **UNFAIR (scoring)** | "Without ending humanity" means that whoever thinks an AI catastrophe will be total, not partial, must answer low. The predictors did exactly that. Yudkowsky 30 ("his central scenario is sudden extinction… not a survivable disaster on the way"). Kokotajlo 35 ("in AI 2027's race ending the killing is total"). Tegmark 50, Russell 45. The item then scores them toward a clear road. Yudkowsky's x falls from 97.1 without d15 to 88.8 with it, and Kokotajlo's from 86.8 to 80.3. The sentence is fair; the scoring is not, because a more alarming belief produces a less alarmed score. The same answer (30) from Altman means "unlikely to happen". Opposite beliefs get one number. |
| d10 | FAIR, with a note | The 20-year window moves a long-timeline pessimist toward "clear" for a timeline reason. This is the fault review-v2 flagged on d6, and the owner accepted it knowingly (p2 isolates timelines). It is invisible in the sample, where every high-danger figure has short timelines, but it will occur in the crowd. r(d10, p2) = 0.68. Put it on the methodology page; do not change the text. |
| d13 | FAIR | "Familiar kind… not a threat to survival" is the real present-harms-versus-x-risk split. The "against" gives the halt reply ("only the second can't be undone"). |
| d12 | FAIR, "for" thin | The "for" is all theory. The "against" gets the evidence ("come out broadly helpful", "there is no evidence…"). The halt side's strongest current point, that today's models get caught gaming their tests, appears in d11's *build-side* "for" and not here. **Edit:** one clause added to "for". |
| d14 | FAIR | The text is fine. The "for" has a factual slip the halt side will pounce on: engineered viruses have not existed for "eighty years". **Edit.** |
| d11 | FIXABLE (steelman) | "Clear" carries the no-fire-alarm argument well (Yudkowsky 5). But the "against" argues a different point ("warning signs only help if someone acts on them"), which is about heeding, a speed-axis question. The predictors followed it. Russell 30 ("warnings short of disaster get ignored"), Harris 30 and Tegmark 45 ("warnings get waved away") are low for heeding reasons. Bender 65 and Marcus 60 are high because signs are "already here". 12 of 22 predictions are low-confidence, the most of any item. **Edit:** plain and "against" now argue what the item asks: will the danger show *clearly*. |
| s14 | FIXABLE | "All work on AI more capable than today's" freezes specialised tools too: drug-design and protein-folding AI. The pause the halt side proposes targets frontier general systems. The 2023 letter targeted systems "more powerful than GPT-4", and the 2025 statement targets superintelligence. The figure data show it. Bengio's own button "spares AI that is clearly not dangerous". Tegmark "would press, even at a cost to better tool AI". Hinton sits at 60 because "I don't think we should stop developing it altogether, citing medicine". The "against" then books those medical losses against the pause. **Edit:** "general-purpose AI". |
| s4, s5, s6, s8, s10, s11, s13 | FAIR | Unchanged from v4 and settled. No v5 interaction. |

## 3. Pass 2: build-side editor (a careful Andreessen/Verdon/LeCun/Sacks ally)

| id | verdict | finding |
|---|---|---|
| s14 | FIXABLE (minor) | **"You would press it"** is the site telling the reader what they would do, a leading declarative that invites acquiescence. A first-person statement ("I would press it") is the neutral agree/disagree form. **"More capable than today's"** is fair: it is the frontier, and "today's AI keeps running" is true to the hypothetical. **"No way to cheat"** removes our race argument by construction. That is legitimate, because the item says so, and our remaining objections (forgone cures, learning by building, lock-in) are all in the "against". The narrowing to general-purpose AI (Pass 1) is acceptable *if* the "against" says why it still costs cures: the big advances are expected from general systems. The proposed "against" says that. |
| d10 | FAIR | The 20-year window, if anything, helps our side: it removes the free "this century, who knows" agreement. The "against" is our line ("a guess dressed up as a probability"). One implicature is new in v5. Next to d15's "causes, or is used to cause", d10's bare "causes" reads as agency-only. For us that is fine. For a misuse-worrier (Marcus 12) it silently drops the route they fear. **Edit:** one plain sentence says misuse counts. |
| d15 | FAIR text, attribution loose | "Or is used to cause" is fair: misuse is a road hazard, and our "against" (defenders get the same AI) answers it. The loose part is attribution. Does a terrorist who used a chatbot for one step count as "AI used to cause" it? Does a great-power war with AI targeting? Without a rule, anyone can count anything. **Edit (plain):** "It counts if AI made the difference." Dropping "without ending humanity" (Pass 1) costs us nothing: our answers are 6–12 either way. |
| d11 | FAIR | The conditional ("if AI ever becomes dangerous enough…") asks us to imagine what we deny. We can answer it (Andreessen 75, LeCun 85), and the "for" is our iterative-safety line. The v5.1 "against" (signs get explained away) is a fair statement of the other side. |
| d13 | FAIR, one wobble | "Lost jobs" is listed as a danger, and some of us deny net job loss. But "like" makes it an example, and the predictors placed Andreessen at 90 (his own risk list includes jobs). The "for" carries our line ("problems we already know how to police"). Keep. |
| d12, d14 | FAIR | The "against" on each is ours. d14's "for" is ours, and the factual fix does not weaken it. |
| s4–s13 | FAIR | Settled. |

## 4. Pass 3: plain language and measurement

**Can a non-technical reader answer each item without guessing?** Yes for 13 items. The three
exceptions:

- **d15.** "…without ending humanity" makes the reader wonder whether a disaster that *does* end
  humanity counts. Read literally it does not, and a lay reader will not see that this reverses
  their score. It is removed in d16.
- **s14.** Does "AI more capable than today's" include medical AI? The v5 plain does not say. In
  s15 the text says "general-purpose" and the plain glosses it.
- **d11.** Does "we will see" mean *appear* or *be heeded*? The fix is in the plain.

**Hidden second claims and presuppositions.** d12 presupposes that AI can have goals. That is
fine, because the "against" denies it and a denier answers low, which is correct. d14 and d11 are
conditional on danger. That is acceptable, but note that two of the three clear-road items are
conditionals, so a lay optimist must imagine the danger they reject. Watch the crowd for
optimists who answer d11 or d14 low ("if it were that dangerous, then no"). No double negatives
beyond the settled s13 and the d13 contrast.

**Same answer, opposite reasons.** d15 does this worst: Yudkowsky 30 = "it will be total", Altman
30 = "it will not happen". It is fixed in d16. d11 has milder cases (Bender 65 "signs plain and
ignored" beside LeCun 85 "signs, then fixes"), which the plain edit reduces. On d13, Marcus 72 and
Andreessen 90 give the same answer for different reasons, but d13 asks about the *kind* of danger,
and on kind they agree. This is correct.

**Forecast or opinion?**

- The `prob` items are forecasts of events: d15/d16 is a bare dated event, d12, d14 and d11 are
  conditional forecasts, and p2 is a dated event.
- The `agree` items are judgements or prescriptions: d10 is a threshold judgement, d13 is a
  classification, and s15 is a hypothetical choice.
- No type bugs.

**Is the danger axis balanced in meaning?** Yes.

- **The + side** asks "will it happen":
  - d16, grave harm, including misuse;
  - d10, irreversible harm;
  - d12, misaligned goals.
- **The − side** asks "can we cope, and what kind is it":
  - d14, control;
  - d11, visible warning;
  - d13, kind.
- **Pairs:** d10 ↔ d13 (existential, or not), d12 ↔ d14 (it goes wrong, or we hold it), and
  d16 ↔ d11 (grave harm, or a visible warning first).
- **Where people land:** someone who expects danger and also expects us to cope lands mid-road,
  which is right.
- **Metaphor check:** d11 fits the metaphor exactly, because black ice is ice you cannot see.
- **Keyed means before the fix:** d15 has a keyed mean of 29 (a floor item pulling toward clear),
  and d13 has 65 (pulling toward ice). They roughly cancel.
- **Keyed means after the fix:** d16 has an estimated 38. The sample mean moves about 1 point
  toward ice.

**Near-duplicates: d12 and d14 (r = −0.95). Polarisation, not wording.** The two sentences ask
different things: will it get goals we did not choose, and can we hold it if it is dangerous.
Where figures break ranks, they break them differently:

| figure | d12 | d14 | reading |
|---|---|---|---|
| Musk | 60 | 12 | goals likely, control unlikely |
| Bender | 5 | 70 | goals not an issue, control fine |
| Altman | 30 | 70 | goals unlikely, control fine |
| Amodei | 35 | 50 | |
| Pinker | 8 | 90 | goals not an issue, control fine |

The lay view "it might go rogue, but we'd unplug it" is the combination this sample lacks. It is
common in the public. Every danger pair sits between 0.75 and 0.95, so d12/d14 is the top of a
general pattern, not an outlier. Keep both. If crowd data show r > 0.85 between them, reconsider
the weights; the wording is fine.

**d15 discrimination (SD 17). Is another threshold better?** The small spread is a symptom. The
cause is that the "survivable" clause caps the doomer end. No figure is at or above 65, the
highest is Hinton at 60, and the three strongest x-risk voices sit at 30–50. A higher threshold
("hundreds of millions") would push everyone toward zero, which is why the owner rejected it. A
lower one ("thousands") would pull the build side up for reasons of ordinary misuse. "Millions"
is right. The fix is to make the rung cumulative, not to move it. Reviewer's illustrative
estimates for d16 (the dossier agents must redo them):

| | v5 d15 | v5.1 d16 (estimate) |
|---|---|---|
| mean / SD | 29 / 17 | 38 / 24 |
| r rest | 0.84 | 0.96 |
| Yudkowsky x (without the item: 97.1) | 88.8 | 95.0 |
| Kokotajlo x (86.8) | 80.3 | 84.7 |
| Tegmark x (85.4) | 81.0 | 83.5 |
| build-side figures | 6–12 | unchanged |

The cost: r(d16, d10) rises from 0.80 to about 0.95 in this sample, because x-risk figures now
answer both high. The information d16 adds beyond d10 lies with the misuse-worriers: Marcus
(d10 12, d16 ≈ 40), Musk, Buterin, Hinton. In the public that group is large. The item keeps the
rung the owner wanted, because for everyone who does not expect extinction the answer is the same
as before. Only the non-monotonic tail is removed. No wording of the form "survivable only" can
avoid that tail: a doomer must always answer it low.

---

## 5. Decisions per item

| id | decision | reason |
|---|---|---|
| **d15 → d16** | **reword, new id** | Drop "without ending humanity". Plain adds the attribution rule and says a non-survivable disaster counts. Old answers must not carry over, because anyone who answered low "because it will be total" would be misplaced. |
| d10 | keep text; plain +1 sentence | Misuse counts, which removes the implicature created by d16's wording. |
| d13 | keep | Bimodal by design (0 of 22 in the middle); it sorts by kind. Altman's +11.3 toward ice is the item doing its job: he names loss of control as a risk. |
| d12 | keep text; "for" +1 clause | "…and today's models already get caught gaming their tests." |
| d14 | keep text; "for" fixed | "nuclear weapons for eighty years and on the most dangerous germs for decades". |
| d11 | keep text and id; plain and "against" reworded | Aimed at *clear* signs, not heeding. Text unchanged, so predictions are spot-checked, not redone. |
| **s14 → s15** | **reword, new id** | "general-purpose AI"; "I would press it"; the "against" states why the freeze still costs cures. 28 words (was 30). |
| s4, s5, s6, s8, s10, s11, s13, p2, p4 | keep | Settled; no v5 interaction. |

## 6. French edition: drift in meaning

Checked item by item against v5. Two drifts, both fixed in the proposed French file:

- **d15 "against":** "ont **toutes** exagéré" adds "all". The English says past predictions
  "have overshot". → "ont exagéré".
- **s14 plain:** "seule **la course** vers des systèmes plus capables" turns the neutral "push"
  into "race", a word the build side rejects. → "la progression vers".

Everything else matches in meaning. The closest calls were:

- "surmontable" for "survivable";
- "démontrer" for "show" in s6;
- "bien avant vingt ans" for "well within twenty years" in d10.

All three are faithful. The proposed French file carries the v5.1 edits with no-break spaces
(U+00A0) before : ; ? ! and inside « ». The longest French text is 28 words (s15).

## 7. If v5.1 is adopted

- **d16 (new id), all 22 figures need a value.**
  - Real re-predictions: Yudkowsky, Kokotajlo, Tegmark, Russell, Harris, Alexander, Hinton,
    Bengio, Amodei, Musk, Aschenbrenner. Their p(doom within 20 years) now enters the item.
  - The other 11 can copy d15, after checking the basis against "AI made the difference":
    Andreessen, Verdon, LeCun, Altman, Hassabis, Bender, Marcus, Buterin, Pinker, Sacks,
    Zuckerberg.
- **s15 (new id).**
  - Re-predict: Hinton, Bengio, Tegmark, Marcus, Hassabis, Amodei, Bender. Their bases turn on
    scope, medicine or tool AI.
  - Copy s14 for the other 15, including Musk ("even if there was a stop button, we probably
    shouldn't press it") and Russell.
- **d11 (same id), spot-check only:** Russell, Harris, Tegmark (low for heeding reasons).
- **d10 (same id), spot-check only:** Marcus (misuse now explicitly counts).
- **No re-prediction:** d12 and d14 (steelman-only edits).
- **Crowd watch:**
  - r(d16, d10) and r(d12, d14) above 0.85;
  - optimists answering d11 or d14 low;
  - long-timeline respondents with d10 low and d12 high (the horizon effect).
