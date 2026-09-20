# Review of `propositions.v2.json` — second fairness round

Reviewer role: second-round fairness editor, fresh eyes on the round-one rewrites. Same bar as
round one: Yudkowsky's most careful ally and a16z's sharpest reader both call every item fair,
and a smart 16-year-old understands every item. Settled points are not re-opened unless the
round-one fix itself created the problem.

- Reviewed: `content/propositions.v2.json`
- Test set: `research/figures-a.json` and
  `research/figures-b.json` (16 figures).
  **The audit patch landed at 02:34 while this review was running; every number below is
  computed on the post-audit files.** (Pre-audit numbers differed by at most 5 points on one
  axis for one figure, Hassabis; no finding changed.)
- Proposed wording: `content/propositions.v3.proposed.json`
  (24 items, same ids, same axis/dir/weight/type on every item; balance untouched: danger 4/4 at
  5.0/5.0, speed 6/6 at 6.75/6.75). Not applied. The file name does not match the
  `propositions.vN.json` pattern, so `tools/build-content.js` and `tools/check-figures.js` ignore it.

Caveat on the method. The 16 figures are an elite, polarised sample predicted by agents who
knew each figure's camp, so every item correlates about 0.9 with its axis and the two axes
correlate −0.88 with each other. High correlations prove little here. What the test set can
show is (a) floor and ceiling, (b) which single item moves a figure most, and why, and
(c) where the predictors themselves could not tell what the sentence asks.

---

## 0. Findings, ranked by severity

| # | sev. | item | finding | action in v3.proposed |
|---|---|---|---|---|
| 1 | HIGH | d9 | Floor item at weight 1.5 (13 of 16 at ≤ 35, nobody above 70, SD 19, lowest of all scored items). The sentence is a claim almost nobody makes ("today's methods will keep working"); the build side's real claim is that safety keeps pace with capability. "Today's" scores architecture sceptics toward ice (LeCun 40 → +7.0 points, Marcus 15 → +6.0, Bender 30 → +5.9): the d4 fault again. Twin of d2 (r = −0.97): the d10 fault again. | Reworded: "As AI becomes more capable, our ability to keep it safe will keep pace." Steelmen unchanged (they already argue this sentence). |
| 2 | HIGH | d8 | Disagreement has two unrelated meanings: "catastrophe is likely" (on-axis) and "the benefits are hype / it will be mixed" (off-axis). Lowest item-rest correlation on either axis (0.57) and the largest single-item distortion in the test set: Bender +9.4 points toward ice because she thinks AI is a con, not because she thinks it is lethal. Round one's weight 1 → 1.5 amplified it. | Reworded as a comparison: "Advanced AI is far more likely to make the world much better than to end in catastrophe." The "neither" respondent now has a true middle. |
| 3 | MED-HIGH | d7 | Round one's fix introduced "existing institutions … will be enough", a near-copy of s7 ("the laws we already have … are enough"): r(d7, s7) = 0.92, and d7 tracks the speed axis (−0.92) more than its own (0.89). Anyone who wants new rules for any reason must disagree. Marcus (p(doom) 3%) answers 10 and lands in Road Closed at x = 50.8. The "for" leads with "treaties, inspections", which the accelerationist side rejects as an argument. | Reworded: "…humans will still be able to keep it under control." "For" rewritten; absorbs round one's reserve "off switch" item. |
| 4 | MEDIUM | s6 | Round one removed "rather than regulators…" and with it any gatekeeper. What is left has only one responsible-looking answer (who opposes makers showing a product is safe?), the fault round one found in s8. Five camps sit within 15 points (Yudkowsky 97, Marcus 92, Hinton 90, Bender 85, Amodei 82). | Adds the cost: "…should have to show **a regulator** that it is safe." |
| 5 | MEDIUM | s11 | "should be released openly" is not the build side's claim. a16z and LeCun argue that open release must not be forbidden, not that every lab ought to publish its best model. The live policy question is permission. | "Developers should be free to release even the most powerful AI models openly…" |
| 6 | MEDIUM | archetypes | Centre at 12 is right and should not grow (§6). The real problem is the brake quadrant's name: Amodei (60, 36), who rejects a halt (s1 = 15), and Marcus (51, 21), p(doom) 3%, are both labelled "Road Closed". The centre blurb ("You're not sure…") misdescribes Buterin and Hassabis, who are sure and average out. | Engine/copy suggestions in §6; no content change. |
| 7 | MED-LOW | d2 | Read literally, close to a tautology (an untested situation is by definition unchecked; the "for" even says so), and the nearest to ceiling on its axis: mean 73, 11 of 16 at ≥ 65, minimum 25. A careful sceptic agrees and is scored toward ice. | Drops "in situations its makers never tested" from the text; the idea stays in plain and "for". |
| 8 | LOW-MED | d3 | Round one's fix left three claims in one sentence; "faster than its makers expected" is false for exactly the people who most expect a jump (Kokotajlo 92, Aschenbrenner 95 forecast it openly). | "…will probably jump so suddenly that nobody has time to respond." |
| 9 | LOW | s9 | Passes on spread (10–99) but is the item the predictors could least call: 9 of 16 low-confidence, 5 premise rejections; all four low values are "rejects the 1% premise", not the value judgement. Twin of s8 (r = 0.96). Public ceiling likely. | Keep, weight 1. Monitor the crowd (§2). |
| 10 | LOW | s2 | Double-barrelled by design (prescription + rationale + presupposed "AI risk"): the accelerationists give 55–70 here against 85–95 on s13. Floor for everyone else (11 of 16 at ≤ 35). Twin of s5 (r = 0.96). Weight 1.25 exists only to balance s3's 0.75. | No text change. Weight note in §5. |
| 11 | LOW | s8 | Fair after round one; the trailing "and the benefits lost with it" is hard to attach on first reading, on the heaviest speed item. | "Lowering the chance of catastrophe would be worth delaying AI, and its benefits, by a few years." |
| 12 | LOW | weights | Equal weights change no figure's quadrant or archetype; largest move 3.3 points (§5). Defensible once d8 and d9 are reworded; before that, the two heaviest "clear" weights sat on the two weakest danger items. | None required. |
| 13 | LOW | d1, s5 | d1: a threshold under an agree slider has no stated middle; predictors mapped the same estimate differently (Hinton 10–20% → 90, Amodei 10–25% → 70, Buterin 8–12% → 50). s5: "your own country" is odd for most of the world. | One sentence added to each "plain". |
| 14 | LOW | d6 | The ten-year horizon pushes a long-timeline doomer toward "clear" for a timeline reason (profile `horizon`, not danger). Not visible in the test set (every high-danger figure has short timelines). | Not changed (settled in round one, fix did not create it). Note for the methodology page. |
| 15 | NIT | p5, s9, s13, spelling | p5 "for": "power you can see from space" (power is not visible; buildings are). s9 "for": "a thousand times worse" is an invented multiplier in a steelman attacking invented numbers. s13: "no deliberate slowing down" makes Disagree a double negative, acceptable for an anchor. Mixed spelling ("license" in s3; "specialised" in s4, p5). | p5 and s9 "for" fixed. s13 and spelling left. |
| 16 | DATA | Altman d7 | Prediction 60 contradicts its own basis ("Wants new institutions (IAEA-like) beyond existing ones"); under v2 wording that is about 30. Moves Altman's x from 43.5 to 46.5; archetype unchanged. | For the dossier agents; figures files not touched. |

---

## 1. Scoring validity with the 16 figures

Item table (raw 0–100 answers; "r rest" = correlation of the keyed item with its own axis
computed without it; "r other" = with the other axis).

| id | w | mean | SD | min–max | r rest | r other | ≥65 | ≤35 | mid | low-conf |
|---|---|---|---|---|---|---|---|---|---|---|
| d1 | 1.5 | 52 | 35 | 3–99 | 0.92 | −0.78 | 7 | 5 | 4 | 3 |
| d2 | 1 | 73 | 22 | 25–97 | 0.94 | −0.88 | 11 | 1 | 4 | 3 |
| d3 | 1 | 54 | 33 | 3–95 | 0.82 | −0.58 | 8 | 5 | 3 | 1 |
| d5 | 1.5 | 45 | 31 | 4–98 | 0.94 | −0.85 | 6 | 9 | 1 | 2 |
| d6 | 1 | 39 | 30 | 5–97 | 0.85 | −0.61 | 5 | 9 | 2 | 1 |
| d7 | 1 | 32 | 27 | 3–90 | 0.89 | **−0.92** | 2 | 11 | 3 | 3 |
| d8 | 1.5 | 58 | 30 | 3–97 | **0.57** | −0.77 | 8 | 3 | 5 | 3 |
| d9 | 1.5 | 23 | **19** | 2–70 | 0.92 | −0.87 | 1 | **13** | 2 | 4 |
| s1 | 1.5 | 35 | 34 | 1–99 | 0.80 | −0.85 | 5 | 10 | 1 | 1 |
| s2 | 1.25 | 28 | 28 | 2–85 | 0.86 | −0.61 | 3 | 11 | 2 | 1 |
| s3 | 0.75 | 47 | 29 | 2–82 | 0.94 | −0.88 | 7 | 8 | 1 | 1 |
| s4 | 1 | 53 | 32 | 3–98 | 0.90 | −0.91 | 8 | 5 | 3 | 0 |
| s5 | 1 | 45 | 32 | 5–97 | 0.83 | −0.62 | 6 | 8 | 2 | 3 |
| s6 | 1 | 65 | 34 | 5–97 | 0.97 | −0.81 | 10 | 3 | 3 | 2 |
| s7 | 1 | 25 | 31 | 2–95 | 0.90 | −0.84 | 3 | 13 | 0 | 0 |
| s8 | 1.5 | 63 | 34 | 3–99 | 0.96 | −0.86 | 11 | 4 | 1 | 1 |
| s9 | 1 | 63 | 31 | 10–99 | 0.98 | −0.88 | 8 | 4 | 4 | **9** |
| s10 | 1 | 36 | 31 | 3–92 | 0.93 | −0.77 | 4 | 10 | 2 | 4 |
| s11 | 1 | 37 | 35 | 3–97 | **0.79** | −0.86 | 4 | 10 | 2 | 2 |
| s13 | 1.5 | 25 | 34 | 1–95 | 0.91 | −0.74 | 3 | 12 | 1 | 0 |

Largest single-item effect on a figure (axis score without the item minus with it):
d8 −9.4 (Bender), d9 −7.0 (LeCun), s1 −6.8 (Marcus), d1 +6.3 (Marcus), d5 +5.8 (Bender),
s13 +5.2 (Altman), s11 +4.7 (Aschenbrenner), d7 −4.4 (Marcus). On the speed axis every large
effect is the item doing its job. On the danger axis the three largest negative ones are not.

### Three weakest danger items

1. **d9.** 13 of 16 disagree, including people who plainly hold opposite views on the axis:
   LeCun 40 and Aschenbrenner 10, Altman 35 and Hinton 8, Verdon 50 and Marcus 15. Only
   Andreessen is above 50 (70, low confidence). The build side does not claim that *today's*
   methods will hold; its steelman in this very item argues that methods improve with each
   generation. So the "clear road" end of the item is nearly unoccupied, at weight 1.5, and the
   whole sample is pushed toward ice (keyed mean 77, the highest of any item). LeCun, Marcus and
   Bender disagree because they think today's *AI* is a dead end or does not work, which says
   nothing about catastrophe. d2 and d9 correlate −0.97: together 2.5 of 10 weight points on one
   construct, which is why round one removed d10.
2. **d8.** Item-rest 0.57, far below the rest. It is the most influential item for every figure
   in the middle of the map (Amodei 8.0 points, Hassabis 6.2, Altman 5.9), and what it measures
   there is optimism about the upside, which is the `horizon`/benefit dimension (it correlates
   0.87 with s10, the benefits item on the other axis). Bender's 10 and Marcus's 40 are "the
   benefits are hype", scored as black ice. Round one examined the 20%-doom optimist and judged
   that placement correct; it did not examine the hype sceptic, who is the mirror image of the
   d4 problem (there, belief in AI's power was scored as danger; here, disbelief in AI's
   benefits is).
3. **d7.** Correlates more with the speed axis than with its own, because "existing … will be
   enough" is a policy position. r(d7, s7) = 0.92. Marcus (10), Hassabis (30), Amodei (20),
   Altman's basis ("wants new institutions") all answer the question "do we need new
   institutions?", which is s7's question. The empirical question, whether people can keep a
   dangerous AI under control, is what the axis needs.

Runner-up: d2 (finding 7).

### Three weakest speed items

1. **s11.** Lowest item-rest on the axis (0.79). It tracks the profile more than the pace:
   r = −0.90 with p1 (trust in government) and +0.79 with p4 (concentration). Rank inversions:
   Aschenbrenner, the fastest non-accelerationist (y = 64), answers 5; Buterin (y = 43) answers
   85. That is a legitimate crux and it stays, but the sentence should ask the question the two
   camps actually fight over (finding 5).
2. **s2.** 11 of 16 at ≤ 35. The three accelerationists answer 70, 70, 55 here and 92, 95, 85 on
   s13: they want speed but not for this reason, and they reject "AI risk" as the premise. Only
   Aschenbrenner (85) owns the sentence. It is the safety-racer's argument, deliberately, so the
   text stays; but it is a weak carrier for a 1.25 weight, and it duplicates s5 (r = 0.96).
3. **s9.** See finding 9 and §2.

Not weak, by design: s1 (0.80) and s13 (0.91) are anchors; builders and accelerationists are
indistinguishable on s1 (Altman 3, Aschenbrenner 3, Andreessen 1), which is what an anchor does.

### Wrong-way pushes found

- Bender, danger: +9.4 from d8, +5.9 from d9 (both off-axis reasons). Without them she sits at
  about x = 25, which matches "doom talk is hype". v2 puts her at 37.
- LeCun, danger: +7.0 from d9 ("LLMs are a dead end"). v2: 20; without d9: 13.
- Marcus, danger: d9, d7 and d2 together carry him over the x = 50 line into Road Closed with a
  stated p(doom) of 3%.
- No halt advocate is pushed toward "fast" by any speed item. Round one's s5 and s10 fixes hold:
  Yudkowsky 10 and 3, Russell 8 and 5, Tegmark 5 and 5.

Illustration only (reviewer's own estimates for the four reworded items d7, d8, d9, s11; the
dossier agents must redo them): Bender 36.6 → 25, LeCun 20 → 13, Verdon 26 → 19, Marcus 50.8 →
44 (Road Closed → School Zone, the only archetype change), Tegmark 89 → 92; nobody else moves
more than 3 points. Estimated d9 becomes mean 36, SD 29, with 3 figures ≥ 65 and 3 in the
middle; d8's item-rest rises from 0.57 to about 0.9.

---

## 2. Acquiescence and extremity

An all-70 yea-sayer scores exactly (50, 50): the balance round one built holds.

| candidate | verdict |
|---|---|
| **s9** | Keep. Not at ceiling among the figures (8 agree, 4 disagree, 4 middle; item-rest 0.98). Two cautions. The spread is partly an artefact: the four low answers are all low-confidence "rejects the premise", and nine predictions in all are low-confidence, the most of any scored item. And it is nearly the same item as s8 (r = 0.96). Among the public it will probably sit near ceiling. Rule of thumb for the crowd snapshot: if more than 75% of the first 500 runs answer ≥ 65, swap it for a concrete prescription (a hard cap on computing power, or liability), same direction and weight. Weight 1 is right. |
| **d2** | Keep, tighten (finding 7). Nearest to ceiling on the danger axis: 11 of 16 agree, one disagrees (Andreessen 25). Marcus 85 and Aschenbrenner 88 agree with Yudkowsky for three different reasons. The tautology in the sentence makes it worse. |
| **s13** | Keep as is. 12 of 16 at ≤ 35, but it is the anchor: the only sentence on which the no-limit side can answer 90+ without borrowing someone else's rationale, and Aschenbrenner's 55 shows it has a middle. Its mirror s1 is as lopsided (10 of 16 at ≤ 35); their keyed means (65 and 25) nearly cancel, net pull about 1 point toward "slow". |
| **d9** | The real floor item. Fails as worded (finding 1). Reworded under the same id rather than replaced: the crux round one wanted (do safety methods scale) is the right one; only the sentence missed it. |
| **s7** | 13 of 16 at ≤ 35, none in the middle; in this sample it is a flag for "is an accelerationist". Keep: for the public it is a live question. |
| **s6** | Ceiling risk with the public (10 of 16 figures already ≥ 65). The added "a regulator" also helps here. |

---

## 3. Both editors, rewritten items only

| id | Yudkowsky's careful ally | a16z's sharp reader | failing phrase |
|---|---|---|---|
| d1 | accepts | accepts | — (plain gets a line on the slider's middle) |
| d3 | accepts | accepts, but notes the freebie is back in a new form | "faster than its makers expected and faster than they can respond" |
| d5 | accepts | accepts ("goals" is theirs to deny, and the "against" denies it) | — |
| d6 | accepts, with the horizon caveat (finding 14) | accepts | — |
| d7 | accepts | accepts the text; does not recognise the "for": "Treaties, inspections, safety culture…" is the institutionalist's case, and Andreessen holds that nuclear-style regulation was a disaster | "Treaties, inspections" (for); "existing … will be enough" (scoring, finding 3) |
| d8 | accepts text and "against" | accepts | none on fairness; the fault is what Disagree means (finding 2). "And better on average can still mean worse for most people" argues an off-axis point |
| d9 | accepts | **rejects**: "nobody claims today's methods will do; we claim methods improve with the models" | "The ways we make today's AI behave will keep working" |
| s3 | accepts | accepts ("makes open development a crime" is there) | — |
| s4 | accepts | accepts | — |
| s5 | accepts; the prescriptive form works | accepts | — |
| s6 | accepts | **objects**: the sentence hides the gatekeeper, so Disagree reads as "makers need not bother" | "should have to show it is safe" (show whom?) |
| s7 | accepts | accepts | — |
| s8 | accepts | accepts; both sides of the trade are in the sentence | readability only |
| s9 | accepts; a strict consequentialist ally would answer 85–90 rather than 99 because of "whatever the expected benefits", which is fine | accepts; the premise objection is in the "against" | "a thousand times worse" (for) |
| s10 | accepts | accepts | — |
| s11 | accepts | **objects**: "we say nobody may forbid it, not that everyone should do it" | "should be released openly" |
| s13 | accepts | accepts, and would answer 100 | — |
| p5 | accepts | accepts; would mock one phrase | "drawing power you can see from space" |

---

## 4. Plain English

- **Stumbles:** s8 (trailing clause); d3 (three clauses); d9 ("the ways we make today's AI
  behave"); d2 (23 words, the longest, and the tautology). All addressed in v3.proposed; longest
  text is now 22 words (d1, d6, s1, s11).
- **Double negatives on Disagree:** d2 ("no reliable way"), d6 ("not catastrophes"), s13 ("no
  deliberate slowing down"). All three are contrasts or anchors and read naturally; positive
  rewording would flip `dir` and break the balance. Left.
- **Is 50 a meaningful middle?** d1: yes once the plain says so (added). d8: not in v2, where a
  respondent expecting a mixed result had to choose between "much better" and being scored
  toward ice; yes in v3, and the plain says so. d3, d5: a "probably"/"most likely" inside an
  agree item; 50 reads as "can't say which is likelier". Acceptable. s9: 50 = torn. p1, p4:
  true comparisons. p2, p5: probabilities.
- **s5:** "your own country" (one sentence added to plain).
- **Spelling:** "license" (s3) is US; "specialised" (s4, p5) is UK. Pick one for the site.

---

## 5. Weights

Equal weights (every scored item = 1), post-audit figures:

| figure | weighted x, y | equal x, y | Δ | archetype |
|---|---|---|---|---|
| Yudkowsky | 96.6, 3.7 | 96.3, 4.5 | −0.3, +0.8 | Road Closed = |
| Andreessen | 12.0, 92.7 | 12.5, 92.9 | +0.5, +0.2 | Autobahn = |
| Verdon | 25.9, 90.8 | 27.6, 90.7 | +1.7, −0.1 | Autobahn = |
| LeCun | 20.3, 86.0 | 20.5, 86.2 | +0.3, +0.1 | Autobahn = |
| Hinton | 78.0, 17.8 | 78.4, 18.6 | +0.3, +0.8 | Road Closed = |
| Bengio | 78.5, 13.2 | 79.3, 13.4 | +0.8, +0.2 | Road Closed = |
| Altman | 43.5, 51.4 | 45.0, 52.3 | +1.5, +0.8 | Posted Limit = |
| Amodei | 60.0, 35.5 | 62.9, 35.6 | +2.8, +0.1 | Road Closed = |
| Hassabis | 47.0, 39.2 | 49.6, 39.8 | +2.6, +0.6 | Posted Limit = |
| Russell | 81.8, 8.6 | 82.5, 8.8 | +0.8, +0.2 | Road Closed = |
| Bender | 36.6, 35.6 | 35.4, 35.9 | −1.3, +0.3 | School Zone = |
| Marcus | 50.8, 20.8 | 51.3, 19.3 | +0.5, −1.4 | Road Closed = |
| Buterin | 53.8, 43.2 | 55.0, 44.2 | +1.3, +0.9 | Posted Limit = |
| Tegmark | 88.6, 5.6 | 89.3, 6.2 | +0.7, +0.6 | Road Closed = |
| Kokotajlo | 87.2, 14.0 | 88.3, 13.9 | +1.0, −0.1 | Road Closed = |
| Aschenbrenner | 67.0, 64.3 | 70.4, 62.4 | +3.3, −1.8 | Rally Driver = |

**Result: equal weights change no figure's quadrant and no archetype.** Largest move 3.3 points
(Aschenbrenner, x); median move under 1 point. The weights are cosmetic for these figures.

Are they defensible? The rule "core beliefs and anchors 1.5" is legible and both sides get the
same. Two soft spots. (a) On the danger axis the two 1.5 weights toward "clear" sat on the two
weakest items (d8, d9); with the rewording they sit on real cruxes and the scheme is sound.
(b) s2 at 1.25 and s3 at 0.75 follow no rule; they exist to make 6.75 = 6.75, and s2 is one of
the weaker items. A scheme with a one-line rule, offered as an option and **not** applied in
v3.proposed because the brief fixes 6.75/6.75: s2 = 1, s3 = 1, s10 = 1.5, giving 7.0/7.0 ("the
two anchors and the two trade-off items count 1.5, everything else 1"). Tested: no archetype
changes, largest move 1.0 point.

---

## 6. Archetype thresholds

Centre = |x − 50| < 12 and |y − 50| < 12. Who lands there:

| figure | x, y | distance | right? |
|---|---|---|---|
| Altman | 43.5, 51.4 | 6.7 | Defensible after the audit (he backs pacing, s13 = 10), but his x rests on three low-confidence items and a d7 that contradicts its basis (finding 16). |
| Buterin | 53.8, 43.2 | 7.7 | Right place, wrong description. He is not unsure: p(doom) 10%, open weights 85, soft pause 65, licensing 30. Strong views that average out. |
| Hassabis | 47.0, 39.2 | 11.2 | Right. Inside by 1.2 points on y; the audit moved him 5 points. |

Next out: Amodei 17.7 (Road Closed), Bender 19.6 (School Zone), Aschenbrenner 22.2 (Rally
Driver), Marcus 29.3.

Other radii: a square of 15 adds Amodei and Bender; 18 adds Aschenbrenner. Bender (certain the
road is clear, wants to slow) and Aschenbrenner (ice, floor it) are the textbook cases of their
quadrants, so both are wrong. A circle of 18 takes Amodei and leaves Bender out by 1.9 points:
too fragile, and it nearly doubles the centre's area (10% of the plane against 5.8%). Real
respondents average 8 and 12 items and will cluster near the middle far more than these figures
do; a larger centre would hand the least shareable label to a third or more of the crowd.

**Recommendation: keep 12.** Optionally make it a circle (distance < 12; same three figures
today), so that a corner point 16.9 away is not "centre" while a point 12.5 straight down is not.

The problems the radius cannot solve:

1. **"Road Closed" covers y from 0 to 49.** Amodei rejects a halt and is labelled Road Closed.
   Cheapest fix, no new archetype: grade the tag by distance from the centre. Under about 25
   (today: Amodei, Bender, Aschenbrenner) use a milder tag, e.g. "ice ahead, easing off"
   against "ice ahead, braking hard", and have the blurb say "slowed" rather than "stopped".
2. **Hard line at x = 50 far from the centre.** Marcus at x = 50.8 gets "You see black ice".
   When |x − 50| < 5 or |y − 50| < 5 outside the centre, say "on the line between School Zone
   and Road Closed". (Under v3.proposed he probably moves to School Zone anyway.)
3. **Centre blurb.** "You're not sure how dangerous the road is" → something that also fits
   strong views that offset, e.g. "You see real ice and real road ahead, and you'd neither floor
   it nor stop."

---

## 7. If v3.proposed is adopted

- Copy to `content/propositions.v3.json`; the build tools
  pick the highest N.
- Dossier agents: re-predict **d7, d8, d9, s11** (meaning moved). d2, d3, s6, s8 keep their
  values (same question, cleaner sentence); spot-check s6 for Buterin and Aschenbrenner.
- French: `content/propositions.v2.fr.json` must follow the
  eight texts and the changed plain/steelmen; `tools/check-fr.js` hard-codes v2.
- Methodology page: round one's sentence ("road-conditions items are beliefs about the risk of
  catastrophe or loss of control") now holds for all eight danger items. Worth adding: d6 has a
  ten-year horizon on purpose; d1 covers the century.
- Crowd snapshot: watch s9, s6, d2 for ceiling and s13, s7 for floor (share ≥ 65 or ≤ 35 above
  75%).
