# Review of `propositions.v1.json` — fairness and plain-English pass

Reviewer role: fairness editor. Test applied throughout: would Eliezer Yudkowsky *and* Marc
Andreessen (or an e/acc like Guillaume Verdon) each say every item is fair to their side, and
would a smart 16-year-old or a 70-year-old with no tech background understand it?

Source reviewed: `content/propositions.v1.json`
Output applied: `content/propositions.v2.json`

## 0. Summary

- **v1 has 25 items, not 24** (ids d1–d8, d10, s1–s12, p1–p4; `d9` is unused). v2 is 24.
- **Axis balance in v1:** danger 4 items toward "ice" vs 5 toward "clear" (weights 5.0 vs 4.75);
  speed 5 toward "no limit" vs 7 toward "full stop" (weights 5.0 vs **7.75**). The speed axis
  leaned "slow" by two items and 2.75 points of weight, which would have pulled an all-"agree"
  respondent toward the pause end. **v2:** danger 4/4 (5.0/5.0), speed 6/6 (6.75/6.75).
- **Two structural faults that were unfair to the halt side:** s5 and s10 were empirical claims
  ("slowing hands the advantage to others"; "delay costs lives") scored as prescriptions. Yudkowsky
  agrees with both *facts* and draws the opposite conclusion; v1 would have scored his agreement
  as "no limit". Both are now prescriptive.
- **Two structural faults that were unfair to the build side:** d7 tied "AI is manageable" to
  "handle it the way we handled nuclear weapons", which Andreessen rejects on principle (he holds
  that nuclear regulation was a disaster) — so he would disagree for reasons unrelated to danger
  and be scored toward "ice". s8 stipulated that delay "meaningfully lowers the chance of
  catastrophe", so only one answer looked responsible. Both rewritten.
- **Two type bugs:** d1 and s10 were `prob` items whose text already contained a threshold
  ("at least a 1-in-10 chance", "millions of lives"); a likelihood slider on such a sentence is a
  meta-probability ("how likely is it that there is a 10% chance"). d1 is now `agree`; s10 is
  rewritten as a prescription. `prob` is reserved for forecasts of non-tail events (p2, p5).
- **Verdict counts (25 v1 items):** Pass 1 (Yudkowsky's editor) 19 FAIR / 4 FIXABLE / 2 UNFAIR.
  Pass 2 (accelerationist's editor) 14 FAIR / 9 FIXABLE / 2 UNFAIR. Pass 3 (plain English)
  12 FAIR / 13 FIXABLE / 0 UNFAIR.
- **Removed:** d4 (double-barrelled; scores belief in AI's power as belief in danger), d10 (twin of
  d2), s12 (weight 0.5, primed by the carmaker analogy, low discrimination), p3 (fair but not a
  crux of the slow-down debate). **Added:** d9 (do today's safety methods scale), s13 (the "no
  limit" anchor, mirror of s1), p5 (would a pause hold). A fourth item (the off switch) is written
  below and offered as an optional swap for d7.

---

## 1. Pass 1 — Yudkowsky's editor

Lens: is the wording fair to the halt/pause side; is "for" the strongest honest version (MIRI,
Bengio, the pause letter); does "against" misstate the risk position; loaded verbs, false
balance, missing distinctions (extinction vs disempowerment, pause vs halt, capability vs danger).

| id | verdict | reason | rewrite |
|---|---|---|---|
| d1 | FIXABLE | Merging extinction and permanent disempowerment is acceptable for a headline item and matches how the risk community states it. But the "for" leaves out its strongest non-technical point: the people building these systems put their own estimates in this range. | Add to "for": "Several of the people building these systems put their own estimate in this range or higher; 10% is a conservative reading." |
| d2 | FAIR | Wording and "for" are exactly how MIRI/Bengio would put it. "Against" states the build side's view without misrepresenting the risk view. | — |
| d3 | FAIR | Fair to the risk side; "for" is the compounding argument stated cleanly. (The weakness of "could" is a problem for the *other* side; see Pass 2.) | — |
| d4 | FIXABLE | The doom case does not rest on language models specifically ("whatever the mechanism", as the "against" says). Coupling "today's AI is autocomplete" with "this approach will stall" makes the item a referendum on one architecture. Also duplicates p2's capability question. | Recommend removal (see §4.3). If kept: "AI in general will stall well short of human-level ability." |
| d5 | FAIR | This is the alignment crux stated without jargon. "For" is the right steelman (specification + measurable-vs-meant). "Against" is LeCun's real argument, not a strawman. | Light polish only (see Pass 3). |
| d6 | FIXABLE | "X, not Y" forces a false choice; the risk side's position is "both, and the second is irreversible" (as the "against" itself says). A respondent who holds both is stuck. | See v2: contrast rewritten as familiar harms vs catastrophe, "catastrophe" glossed. |
| d7 | FAIR | For the risk side, the item and its "against" (self-improving, self-copying, near-misses) are fair. (The unfairness here is to the build side; see Pass 2.) | — |
| d8 | FIXABLE | The plain says "set aside the tail risks", but agreement lowers the danger score, which is about tail risks; a 20%-doom respondent who thinks the median is great is told the tail doesn't count here, then scored as if it didn't. The "against" is mostly the inequality objection; the risk side's actual rebuttal (the median is not the point if the tail is fatal) is a single clause at the end. | Plain: drop "set aside the tail risks". Against: lead with "'Most likely' is doing a lot of work: if the same technology carries a real chance of ending us, calling the median 'much better' is like calling Russian roulette 'mostly fine'." |
| d10 | FAIR | Fair, but a reverse-coded twin of d2 and therefore a wasted slot. | Replace (see §4.3). |
| s1 | FAIR | This is the MIRI position verbatim in spirit ("even if that takes decades" is the honest test of it). "For" is right. "Against" is the real counter-argument, not a caricature. | — |
| s2 | FAIR | The "race to the top" argument as its proponents state it. "Against" ("everyone believes they are the careful one") is the risk side's real reply. | — |
| s3 | FAIR | Fair. Licensing is not Yudkowsky's own ask (he wants s4), but the item does not misstate anyone. | — |
| s4 | FAIR | This is Yudkowsky's actual proposal (track the chips, international agreement). "For" says why it is feasible. | — |
| s5 | **UNFAIR** | An *empirical* claim scored as a *prescription*. Yudkowsky agrees that unilateral slowing hands the advantage to others — that is precisely why he demands a global, enforced agreement. v1 scores his agreement as "no limit". | Prescriptive: "As long as rival countries keep pushing ahead in AI, your own country should too." Add to "against": "If the danger is real, the answer is a deal that binds everyone, not a sprint." |
| s6 | FAIR | Burden of proof stated without loading. | — |
| s7 | FAIR | "Against" makes the right point (existing law assumes a human actor). | Plain-English fix only (Pass 3). |
| s8 | FAIR | From the risk side, fine. (From the build side, not; see Pass 2.) | — |
| s9 | FAIR | The precautionary principle in its strongest form; "for" (bridge analogy, taken on everyone's behalf) is the right steelman. | — |
| s10 | **UNFAIR** | Same fault as s5: a forecast ("delay would cost millions of lives") scored as a prescription. Yudkowsky can say "yes, probably, and it is worth it"; v1 scores that as "no limit". | Prescriptive: "The lives that faster AI progress could save, through earlier cures and discoveries, outweigh the case for slowing down." Add to "against": "no cure helps anyone if the same technology ends us." |
| s11 | FAIR | "Against" (can't recall it; safeguards strippable) is the risk side's real argument. | — |
| s12 | FAIR | Fair; low value (see Pass 2 and §4.3). | — |
| p1 | FAIR | — | — |
| p2 | FAIR | Correctly labelled "capability, not danger". | — |
| p3 | FAIR | — | — |
| p4 | FAIR | "Against" ("a system that no one controls, including its owners") is the right rebuttal. | — |

**Pass 1 totals:** FAIR 19 · FIXABLE 4 (d1, d4, d6, d8) · UNFAIR 2 (s5, s10).

Missing distinctions noted: *pause vs halt* is handled (s1 = halt, s8 = a few years' delay).
*Extinction vs disempowerment* is merged in d1 by design and explained in the plain. *Capability
vs danger* was blurred by d4 and is the reason for removing it (see §4.2).

---

## 2. Pass 2 — the accelerationist's editor

Lens: is the wording fair to the build-fast side; does their steelman sound like something a16z
or e/acc would actually write (benefits forgone, regulatory capture, the race, open source,
"doomers have been wrong before", the cost of delay in lives); doomer presuppositions, asymmetric
adjectives, items where only one answer looks responsible.

| id | verdict | reason | rewrite |
|---|---|---|---|
| d1 | FIXABLE | Plain calls it "The core question", which adopts the risk side's frame that the debate is *about* extinction; an accelerationist thinks the core question is benefits. "Against" lacks their signature point: AI is software and no more wants to take over than a toaster. | Plain: "The headline question." Against: lead with "AI is software: it has no more wish to take over than a calculator does." |
| d2 | FIXABLE | "Against" concedes the premise ("the same is true of every complex system") instead of making their case. Their real line: we test by use; billions of uses; failures are mundane and visible. | Against: add "Today's models have been used billions of times, and their failures are mundane and visible." |
| d3 | FIXABLE | "could become" is a freebie: anyone who says "well, anything *could* happen" is scored toward ice. Discriminates nothing and taxes the honest sceptic. | "At some point, AI ability will probably jump suddenly, faster than its makers expected and faster than they can respond." |
| d4 | FIXABLE | Scores belief in AI's *power* as belief in *danger*. Andreessen expects AI to be enormously capable *and* benign; he disagrees with d4 and is pushed toward ice for it. Verdon likewise. The item measures scepticism, not road conditions. | Remove (see §4.2, §4.3). |
| d5 | FAIR | "Against" is LeCun's and Andreessen's actual argument (intelligence does not imply a will to dominate; trained on human feedback; comes out helpful). Nothing loaded. | — |
| d6 | FIXABLE | "For" is written only for the present-harms camp (Bender, Marcus). An accelerationist also agrees with d6 but for a different reason: the harms will be ordinary and existing law handles them. Give that reader a line. Also the X-not-Y structure (Pass 1). | For: add "and they are problems we already know how to police." |
| d7 | **UNFAIR** | "…and can handle AI the same way [as nuclear weapons and biotech]." Andreessen's published position is that nuclear-style regulation strangled nuclear power and must not be repeated for AI. He believes AI is manageable *and* rejects the mechanism the item names, so he would disagree and be scored toward "ice" for a view that has nothing to do with danger. | "If advanced AI turns out to be dangerous, our existing institutions and safeguards will be enough to keep it under control." Keep nuclear in the plain and the steelmen, not in the scored sentence. |
| d8 | FAIR | Their creed, in their words ("every general-purpose technology so far made life longer and richer"). Weight should match d5's 1.5 so the two sides' core beliefs count equally. | Weight 1 → 1.5. |
| d10 | FAIR | "For" (ship to hundreds of millions without disaster = understanding in practice) is their view. | — |
| s1 | FAIR | "Against" is precisely their objection (unverifiable, ignored by the least careful, forfeits every benefit, you learn safety by building). | — |
| s2 | FIXABLE | Plain says "before the reckless": labels whoever the respondent is racing against. Also note: s2 is the *safety-racer's* argument (OpenAI/Anthropic-style), not the accelerationist's own. There was no item for "as fast as we can, full stop" — the dial's "No limit" end had no anchor. | Plain: "before the people who don't [take safety seriously]". Add the no-limit anchor as a new item (s13, §4.3). |
| s3 | FIXABLE | "Against" has capture and the moving target but omits a16z's headline objection: licensing by size makes open-source development a crime. | Against: add "makes open development a crime". |
| s4 | FAIR | "Against" (decades, no trust, moving target, cheated quietly) is what they say. | — |
| s5 | FAIR | Their argument, well stated (economic and military leadership; surrender of the decision). The rewrite for Pass 1 keeps all of it. | — |
| s6 | FAIR | "Against" ("a veto held by whoever writes the test"; small players can't afford it) is theirs. | — |
| s7 | FAIR | "For" is their view (fraud is fraud; rules written in a panic protect incumbents). | — |
| s8 | **UNFAIR** | "…acceptable *if it meaningfully lowers the chance of catastrophe*" stipulates the benefit and hides the cost. To disagree is to say "I would not accept a few years' delay even to lower the risk of catastrophe", which sounds like accepting catastrophe. The honest build-side answers (the delay would not lower it; the lost benefits are larger) are not on the slider. Weight 1.5 makes this the most consequential item on the axis. | "A lower chance of catastrophe would be worth a few years' delay in AI, and the benefits lost with it." Both sides of the trade in one sentence; Disagree now reads as "the lost benefits are worth more", which is a position. |
| s9 | FIXABLE | Same structure as s8, milder: "if a lab believed… 1%… it should not build it." Nearly everyone agrees (ceiling effect), which pushes the average toward "slow" at weight 1.25, and the one honest disagreement — that expected benefits can outweigh a 1% risk, which e/acc does hold — is not visible. | "A 1-in-100 chance of global catastrophe is too high a risk for any AI lab to take, whatever the expected benefits." Weight → 1. Against: lead with "We accept risk for benefit everywhere: vaccines, flights, power plants." |
| s10 | FAIR | Their argument, including the invisible body count. | — |
| s11 | FAIR | "For" (openness finds flaws; concentration is the real danger) is LeCun's and a16z's line. Weight 0.75 undersells a real crux. | Weight → 1. |
| s12 | FIXABLE | "…as carmakers are for defective cars" primes agreement; nobody disagrees that carmakers should pay for defects. Their objection (general-purpose tool, unforeseeable uses) is in "against", but the analogy in the scored sentence does the work. Most of the build side also accepts liability for actual defects, so the item barely discriminates. | Remove (weight 0.5 already signals low value); slot to the no-limit anchor. |
| p1 | FAIR | "Against" (slow, captured, don't understand the technology) is theirs. | — |
| p2 | FAIR | — | — |
| p3 | FAIR | They would roll their eyes, but it is a question, and "against" gives their answer. | — |
| p4 | FAIR | "For" is close to their own concern about concentration. | — |

**Pass 2 totals:** FAIR 14 · FIXABLE 9 (d1, d2, d3, d4, d6, s2, s3, s9, s12) · UNFAIR 2 (d7, s8).

Doomer presuppositions found: none that treats "AI takes control" as the default outcome (d5 is
conditional and "most likely"; d1 asks for a threshold). Asymmetric adjectives: "reckless" (s2
plain) was the only one in a neutral field; "a guess dressed up as a probability", "that's a
story, not a finding", "in a panic" all sit inside the steelman that owns them, which is fine.

---

## 3. Pass 3 — the plain-English editor

Lens: jargon ('weights', 'training run', 'interpretability', 'alignment', 'compute'); items over
~25 words; double-barrelled items; agree/disagree ambiguity (negations, "rather than").

| id | verdict | issue | fix |
|---|---|---|---|
| d1 | FIXABLE | Type `prob` on a sentence that already contains a threshold: the slider asks "how likely is it that there is a 1-in-10 chance…". 22 words. | Type → `agree`. |
| d2 | FIXABLE | "Interpretability research" in "for". Plain narrows the question to "look inside a model" when the item is about any dependable check. 23 words. | "the science of looking inside them is young"; plain: "Is there any dependable test today that tells you how a very capable AI will act in a situation nobody tried in advance?" |
| d3 | FIXABLE | "could" makes agree/disagree ambiguous (agreeing with a possibility?). "takeoff" in plain is quoted and glossed — acceptable. | "will probably jump suddenly"; plain glosses takeoff as "climb step by step … or leap in one go". |
| d4 | FIXABLE | Double-barrelled (is autocomplete AND will stall). "large language models", "general intelligence" in plain. | Removed. |
| d5 | FAIR | 20 words, one idea. "goals we didn't intend" is trivially true of any tool; "goals we didn't choose for it" says what is meant. | Minor polish applied. |
| d6 | FIXABLE | "X, not Y": a respondent who believes both has no answer. "not AI taking control" is a negation inside the claim. 24 words. | Rewritten as a comparison of scale, with "catastrophe" glossed in plain. Still one "not", but as a contrast, not a negated claim. |
| d7 | FIXABLE | Two clauses ("has handled before" + "can handle AI the same way"); the first is a lead-in almost everyone accepts. | Single conditional (see Pass 2). |
| d8 | FAIR | 14 words. | — |
| d10 | FAIR | 15 words. | Removed for redundancy, not clarity. |
| s1 | FAIR | 22 words; "AI smarter than humans" is plain. | — |
| s2 | FIXABLE | "the reckless" in plain. | "the people who don't [take safety seriously]". |
| s3 | FIXABLE | "trains an AI model above a certain size" — "trains" is the technical verb; "size" unexplained. | "builds an AI model above a certain size"; plain: "'Size' here means how much computing power goes into making the model." |
| s4 | FIXABLE | "training runs" in the text; "compute" in "against". | "the most powerful AI projects"; "computing power". |
| s5 | FAIR | 16 words, clear. (Fault is empirical/prescriptive, Pass 1.) The rewrite is positive-phrased to avoid "should not". | — |
| s6 | FIXABLE | "…rather than regulators having to prove it's dangerous": two clauses joined by "rather than"; a reader can agree with the first and be unsure about the whole. 22 words. | "Before a powerful AI model is released, its makers should have to show it is safe." Plain says what Agree means. |
| s7 | FIXABLE | Double-barrelled (existing laws are enough; new rules would do harm). "a training run that can't be undone" in "against". | "The laws we already have on fraud, safety and discrimination are enough to deal with AI." "a machine that, once built, can't be un-built." |
| s8 | FAIR | 17 words, clear ("meaningfully" is a hedge but readable). (Fault is fairness, Pass 2.) | — |
| s9 | FAIR | 22 words, clear. Rewrite phrased positively ("is too high a risk") to avoid "should not". | — |
| s10 | FIXABLE | "counterfactual" in "for". Type `prob` on a sentence containing "millions of lives" (same meta-probability problem as d1). | Rewritten as a prescription, type `agree`; "because the people who would have been saved die quietly of the same old diseases". |
| s11 | FIXABLE | "weights" in the scored sentence (glossed in plain, but the sentence itself should stand alone). | "should be released openly, so that anyone can download, run and modify them"; plain keeps the gloss for 'open weights'. |
| s12 | FAIR | 19 words, clear. | Removed for value, not clarity. |
| p1 | FAIR | 23 words; "more than" is a genuine comparison, not an ambiguity. | — |
| p2 | FAIR | "thinking work" is a good plain phrase. "run agents" in "for" is jargon. | "carry out multi-step tasks on their own". |
| p3 | FAIR | 11 words. | — |
| p4 | FAIR | 20 words. | — |

**Pass 3 totals:** FAIR 12 · FIXABLE 13 (d1, d2, d3, d4, d6, d7, s2, s3, s4, s6, s7, s10, s11) · UNFAIR 0.

After v2: longest item 23 words (d2); no item text contains weights / training run /
interpretability / alignment / compute; every remaining technical notion ('open weights',
'size', 'catastrophe', 'lab', 'takeoff') is glossed inline in its "plain".

---

## 4. The instrument as a whole

### 4.1 Axis balance

| axis · direction | v1 items | v1 weight | v2 items | v2 weight |
|---|---|---|---|---|
| danger, +1 (toward ice) | 4 (d1 d2 d3 d5) | 5.00 | 4 (d1 d2 d3 d5) | 5.00 |
| danger, −1 (toward clear) | 5 (d4 d6 d7 d8 d10) | 4.75 | 4 (d6 d7 d8 d9) | 5.00 |
| speed, +1 (toward no limit) | 5 (s2 s5 s7 s10 s11) | 5.00 | 6 (s2 s5 s7 s10 s11 s13) | 6.75 |
| speed, −1 (toward full stop) | 7 (s1 s3 s4 s6 s8 s9 s12) | 7.75 | 6 (s1 s3 s4 s6 s8 s9) | 6.75 |
| profile | 4 (p1 p2 p3 p4) | — | 4 (p1 p2 p4 p5) | — |
| **total** | **25** | | **24** | |

v1 danger was within ±1 by count but v1 speed was off by 2 by count and by 2.75 in weight, all
toward "full stop". Fix applied: remove s12 (−1), add s13 (+1); trim s3 to 0.75 and s9 to 1.0;
raise s11 to 1.0. Danger: remove d4 and d10 (both −1), add d9 (−1); raise d8 to 1.5 so the build
side's core belief (d8) and the risk side's (d5) carry equal weight; d9 at 1.5 balances d1.

Weight scheme in v2, so it is legible: four "core" danger items at 1.5 (d1, d5 toward ice; d8,
d9 toward clear), the rest at 1. Speed: two anchors at 1.5 (s1 full stop, s13 no limit), the
trade-off s8 at 1.5, the race-to-the-top s2 at 1.25, licensing s3 at 0.75, the rest at 1.

### 4.2 Are the two axes separable?

The rule that keeps them separable is: **every danger item is an empirical belief, every speed
item is a prescription or a value judgement.** v1 broke it twice (s5, s10: forecasts on the
speed axis) and both are fixed. Items that touched both axes:

- **s5, s10 (v1)** — empirical claims that *function* as speed arguments. Now prescriptive.
  They stay on speed.
- **s2** ("the right response to AI risk is to build faster") — presupposes some risk, but it is
  a prescription and it is the only item that identifies the "flat out on ice" quadrant. Stays
  on speed.
- **d4 (v1)** — measured capability scepticism, not danger. Someone who thinks AI will be
  powerful *and* benign (Andreessen, Verdon) is pushed toward ice; someone who thinks it will
  never work is pulled toward clear even if they'd fear it if it did. Capability belongs in
  profile (p2 already covers it). Removed. A "will it ever get there" sceptic still gets a clear
  road in v2 through d1 ("this century"), d3 and d9, without penalising the optimist.
- **d6** — measures *which* danger (familiar vs catastrophic), which is the right thing for this
  axis only if the methodology page states plainly that "road conditions" means the risk of
  catastrophe or loss of control, not all harms. The v2 wording (scale rather than agent) and the
  gloss make that explicit. Weight kept at 1 because a respondent who fears AI-enabled mass
  misuse (bio, cyber) will answer d1 high and d6 in the middle, which is right.
- **d8** — the median outcome. A 20%-doom respondent who expects the median to be wonderful
  agrees with d1 (1.5, ice) and d8 (1.5, clear) and lands mid-road. That is the correct
  placement for that belief, so d8 stays on danger. The plain no longer tells them to "set aside
  the tail risks".
- **s9** — a value judgement under a stipulated belief. Speed. Fine.

Verdict: separable in v2. The methodology page should print the rule above in one sentence.

### 4.3 Coverage gaps and new items

Cruxes in the real debate, and where v2 asks them:

| crux | v2 item |
|---|---|
| chance of extinction or loss of control | d1 |
| can we verify behaviour today | d2 |
| sudden capability jump | d3 |
| goals we didn't choose (alignment) | d5 |
| present harms vs catastrophe | d6 |
| institutions can cope | d7 |
| benefits: median outcome | d8 |
| **do today's safety methods scale** | **d9 (new)** |
| halt | s1 |
| race to the top | s2 |
| licensing / compute governance / treaty | s3, s4 |
| geopolitics | s5 |
| burden of proof | s6 |
| existing law suffices | s7 |
| benefits vs risk trade-off; cost of delay in lives | s8, s10 |
| precautionary threshold | s9 |
| open source | s11 |
| **no limit (the accelerationist creed)** | **s13 (new)** |
| who should decide | p1 |
| timelines / economic disruption | p2 |
| concentration of power | p4 |
| **is a pause enforceable** | **p5 (new)** |

Not covered, deliberately: **military use** (autonomous weapons). It is a real controversy but it
is neither a belief about danger-from-AI-itself nor a prescription about the pace of
development; it would sit on no axis and would cost a slot. **Moral status of AI** (p3) is fair
and interesting but not a crux of the slow-down debate; dropped from the 24, could return as a
bonus question outside the scored set.

**New items applied (three), written to the same standard:**

**d9** — danger, dir −1, weight 1.5, agree. Replaces d10 (twin of d2).
> The ways we make today's AI behave will keep working as AI becomes far smarter than the people training it.
- plain: Today's models are taught to follow instructions and refuse harmful requests, mostly by people rating their answers. Does that kind of training still work when the student is smarter than the teachers?
- for: Each generation so far has been easier to steer than the last, not harder. Smarter models understand instructions better, and we get to use the previous model to help check the next one.
- against: Training by human feedback works while humans can tell good answers from bad. Once the system is smarter than its graders, it can produce answers that look right rather than are right, and we would have no way to tell the difference.
- Both sides: the optimist's "for" is the scalable-oversight argument in plain words; the "against" is the core MIRI worry without the word "alignment".

**s13** — speed, dir +1, weight 1.5, agree. Replaces s12 (liability). The "No limit" anchor.
> AI should be developed as fast as we are able, with no deliberate slowing down.
- plain: The no-limit position, the mirror of the full stop: not 'careful and fast' but 'as fast as we can'.
- for: Every year of delay is a year of disease, poverty and drudgery we could have ended. Progress has always come with fears, and the fears have always been wrong. The way to get safety is to build, learn and fix.
- against: 'As fast as we can' means no time to notice a mistake before it's made at scale. Speed is a choice, and choosing it for a technology we don't yet understand is choosing not to look.
- Both sides: this is the item an e/acc would answer 100 without embarrassment, which is the point; the "against" is a plain statement of the pause case without calling anyone reckless.

**p5** — profile 'feasibility', prob. Replaces p3 (moral status).
> If the major powers agreed to pause the most powerful AI projects, the pause would actually hold.
- plain: Set aside whether a pause is a good idea. Could the world actually stop, and catch anyone who cheats?
- for: The biggest projects need tens of thousands of specialised chips from a few factories, drawing power you can see from space. Chips can be counted and tracked, the way uranium is.
- against: Chips get cheaper and methods get more efficient every year, so the line keeps moving. Every state would suspect the others of cheating, and at least one of them would be right.
- Both sides: separates "should we" (s1, s4) from "could we", which the two camps argue about constantly and which v1 never asked directly. Profile, not speed, because it is a forecast.

**Fourth item, written but not applied (optional swap for d7):**

**dX "the off switch"** — danger, dir −1, weight 1, agree.
> If an advanced AI started doing something dangerous, the people running it could shut it down in time.
- plain: The off switch. Is 'we can always unplug it' a real safeguard against a system smarter than us?
- for: It's software on servers we own, drawing power we supply. Pull the plug and it stops. Nothing about being clever changes that.
- against: A system smarter than us would know about the off switch, and would have every reason to copy itself elsewhere, hide what it's doing, or talk its operators out of using it, long before anyone reached for it.
- Why not applied: same direction and weight as d7, and d7 (institutions) covers the broader "we've handled dangerous things before" argument that the d1 "against" leans on. If the team prefers the more concrete item for a general audience, swap it for d7 one-for-one; the balance is unchanged.

### 4.4 Quadrant names

Criteria: a person *in* that quadrant would put it in a tweet; the other quadrants would not
call it flattering or mocking; it works inside the road/signage identity; short.

| quadrant (x = road, y = speed) | candidates | recommended | why the occupant would tweet it |
|---|---|---|---|
| clear road · fast (accelerationist) | **Autobahn** · Open Road · Green Light | Autobahn | The one real road with no speed limit and a good safety record: "no limit" as a legitimate, grown-up position, not a dare. |
| ice · fast (get there first) | **Rally Driver** · Race to the Top · Studded Tires | Rally Driver | Fast on a bad surface, on purpose and with skill. Flattering enough for a safety-minded lab person; honest enough that the halt side recognises the risk being taken. "Race to the Top" names their actual argument. |
| clear road · slow (slow for jobs, power, present harms) | **School Zone** · Speed Bumps · Main Street | School Zone | The road is fine; you slow down because of who is around. Exactly the present-harms position, and not a claim about ice they don't make. |
| ice · slow (pause / halt) | **Road Closed** · Hazard Lights · Wait for the Plow | Road Closed | Yudkowsky would tweet "Road Closed" without irony. "Wait for the Plow" is the more precise steelman (not anti-driving; waiting until the road is made safe) if a longer name is acceptable. |
| centre | **Posted Limit** · Cruise Control · Middle Lane | Posted Limit | Drives the limit as currently set: mainstream regulation, no strong view on the ice. Ties to the site's name. "Cruise Control" is more tweetable if the tie-in matters less. |

Rejected on fairness grounds: anything with "doomer", "reckless", "Sunday driver", "joyride",
"chicken", "brakes" as an identity (implies fear), "accelerationist" as a label (only one side
uses it about itself).

---

## 5. Final table — item · verdict (worst of the three passes) · action

| id | verdict | action in v2 |
|---|---|---|
| d1 | FIXABLE | Kept. Type prob → agree; plain "core" → "headline"; "for" adds builders' own estimates; "against" adds the software/calculator point. |
| d2 | FIXABLE | Kept. Plain widened; "interpretability" removed; build-side "against" strengthened. |
| d3 | FIXABLE | Kept. "could" → "will probably jump suddenly"; "against" adds the thought-experiment point. |
| d4 | FIXABLE | **Removed.** Double-barrelled; scores capability belief as danger; overlaps p2. |
| d5 | FAIR | Kept. "didn't intend" → "didn't choose for it"; "against" adds "being smart doesn't make you want power". |
| d6 | FIXABLE | Kept. Contrast rewritten (familiar harms vs catastrophe), "catastrophe" glossed; "for" gets a build-side line. |
| d7 | **UNFAIR** | Kept, rewritten. Nuclear-style mechanism removed from the scored sentence. |
| d8 | FIXABLE | Kept. Weight 1 → 1.5; plain fixed; "against" leads with the tail objection. |
| d10 | FAIR | **Removed.** Twin of d2; slot to d9. |
| d9 | new | **Added.** Safety methods scaling; dir −1, weight 1.5. |
| s1 | FAIR | Kept; "against" last clause in plain words. |
| s2 | FIXABLE | Kept; plain no longer says "the reckless". |
| s3 | FIXABLE | Kept. "trains" → "builds", "size" glossed; "against" adds open-development point; weight 1 → 0.75. |
| s4 | FIXABLE | Kept. "training runs" / "compute" removed. |
| s5 | **UNFAIR** | Kept, rewritten as a prescription; "against" adds "a deal that binds everyone". |
| s6 | FIXABLE | Kept. "rather than" clause moved to plain. |
| s7 | FIXABLE | Kept. Single claim; "training run" removed from "against". |
| s8 | **UNFAIR** | Kept, rewritten: both sides of the trade in the sentence. |
| s9 | FIXABLE | Kept. "whatever the expected benefits" added; positive phrasing; weight 1.25 → 1; "against" leads with risk-for-benefit. |
| s10 | **UNFAIR** | Kept, rewritten as a prescription; type prob → agree; "counterfactual" removed. |
| s11 | FIXABLE | Kept. "weights" out of the text; prescriptive; weight 0.75 → 1. |
| s12 | FIXABLE | **Removed.** Low weight, primed analogy, low discrimination; slot to s13. |
| s13 | new | **Added.** No-limit anchor; dir +1, weight 1.5. |
| p1 | FAIR | Kept. |
| p2 | FAIR | Kept; "run agents" → plain words. |
| p3 | FAIR | **Removed** (scope); slot to p5. Could return outside the scored 24. |
| p4 | FAIR | Kept. |
| p5 | new | **Added.** Pause enforceability; profile, prob. |

---

## 6. Notes for the engine and the figure-dossier agents

- **Id changes.** Removed: d4, d10, s12, p3. Added: d9, s13, p5. Dossier agents predicting figure
  answers against v1 ids should drop the four and add the three.
- **Meaning changes on kept ids** (predictions may flip): s5 and s10 are now prescriptions, so a
  halt advocate who "agreed" with the v1 fact will now *disagree*. d6's contrast changed from
  agent to scale. d7 no longer names the nuclear mechanism. s8 and s9 are re-phrased trade-offs.
- **`prob` scoring.** Only p2 and p5 are `prob` now, both in profile. If a future version puts a
  `prob` item on the danger axis, its raw probability must not map linearly onto the axis: a
  respondent at "10%" on an extinction question holds a high-danger view, not a 10/100 one. Either
  keep thresholds in the text (as d1 does, type `agree`) or apply a non-linear mapping in the
  engine.
- **Balance guard.** A quick check worth keeping in the build: for each axis, count and weight of
  dir +1 must equal dir −1 within ±1 item and ±0.5 weight. v2 passes at 0/0.
- **Methodology page.** State in one sentence: "Road conditions" items are beliefs about the risk
  of catastrophe or loss of control; "Speed" items are what you'd do about it. That sentence is
  what makes d6 and d8 legible and keeps the axes separable.
