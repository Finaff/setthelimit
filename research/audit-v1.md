# Audit v1 — predicted answers of the 16 figures

Independent audit for Set the Limit (setthelimit.com). Audit date: 17 September 2026.
Audited files: `research/figures-a.json`, `research/figures-b.json` (content version `propositions.v2.json`).
Machine-readable output: `research/audit-v1.patch.json`.

## How this was done

- Coordinates were recomputed with `tools/check-figures.js` (road = danger axis, limit = speed axis).
- For each figure I picked the heaviest items (d1, d5, d8, d9, s1, s8, s13), every value at or beyond 90/10 that carries the position, and the `high` claims, and opened the source myself. Pages were fetched twice where it mattered: once through a summarising fetch, once as raw HTML searched for the exact phrase, so a "not found" below means the string is not in the page.
- Verdicts: **OK** = the person's own words support the number within ±15. **ADJUST** = corrected value and/or confidence, with quote and URL. **BASIS** = number fine, but the printed basis misquotes, misattributes or cites the wrong source. **UNSUPPORTED** = nothing found; confidence lowered.
- Quotes are kept to short fragments on purpose; the URL is the evidence.
- Limits of this audit: x.com returns HTTP 402 to automated fetches, so X posts were read through the search index or through press articles that reproduce them. Axios and CNBC block fetches (403); the Senate PDF for Marcus is bot-blocked. Those items are marked.
- I did not move numbers on taste. 13 numbers move; none by more than 22 points. 2 further confidence labels drop; 9 bases are replaced without touching the number.

## Headline findings

1. **The September 2026 realignment is only half priced in.** The first team updated Amodei and Altman for "We Must Pace the Frontier" (12 Sept 2026) but not **Hassabis**, who endorsed it the same night ("the direction is correct") and who had already said at Davos in January that a slightly slower pace would be good and that he would back a universal pause ("I think so"). His `s8` = 50 and `s1` = 5 (high) are the weakest numbers in the set. Limit moves 44 → 39.
2. **Altman's own follow-up post (14 Sept) is missing.** It contains the closest thing to a verbatim answer to `s13` and `s8` that any figure has given: progress should be slower than it otherwise could be, and pacing is well worth the cost. It also tempers `s5`. Limit moves 53 → 51.
3. **Two attribution errors that would be screenshotted.** (a) Kokotajlo is *not* an author of "How to pace the US frontier" (he is thanked for feedback); five of his predictions quote it as his. (b) Amodei's June 2026 essay does *not* "reject pausing" — the words pause, halt, moratorium never occur in it; the rejection is in the January essay, and by September he "support[s] floating" an intergovernmental pause.
4. **One misquote risk on LeCun.** `d1`'s basis prints "the existential risk is essentially zero" as his number. The post attributes that view to "most leading AI figures", and on 21 April 2026 he wrote that he did not say p(doom) was zero. The number (very low) is right; the basis must not say "zero".
5. **One misapplied quote on Hinton.** The "fast car with no steering wheel" line is about people who oppose regulation, not about alignment methods. `d9` = 8 is still right, but on a different quote (Ai4, Aug 2025).
6. No cited URL is dead. All 141 source URLs answer; the non-200s are bot blocks (TIME 406, Axios/ACM/Senate/TechXplore 403, VentureBeat 429) and open normally through a fetcher or a browser.
7. The extremes are solid. Yudkowsky, Andreessen, Tegmark, Russell, Bengio: every checked number is backed by a primary text. Andreessen in particular is quote-perfect (14 of 14).

## Coordinates: sanity check and effect of the patch

| Figure | Road | Limit | After patch | Informed-observer check |
|---|---|---|---|---|
| Eliezer Yudkowsky | 97 | 4 | 97 / 4 | As expected. |
| Marc Andreessen | 12 | 93 | 12 / 93 | As expected. |
| Guillaume Verdon | 25 | 91 | 26 / 91 | Road 25 (vs Andreessen 12) is an artefact of seven `low` guesses sitting at 30–65, not of anything he said. Acceptable, but it is soft. |
| Yann LeCun | 20 | 86 | 20 / 86 | Plausible. Road is 20 rather than 10 only because of two honest `low` values (d2 = 45, d9 = 40): he does say LLMs are unreliable. Defensible. |
| Geoffrey Hinton | 78 | 18 | 78 / 18 | As expected; consistent with "don't stop altogether, slow down" (ABC, 14 Sept 2026). |
| Yoshua Bengio | 79 | 13 | 79 / 13 | As expected. His Jan 2026 optimism is about Scientist AI, not about today's methods; d9 = 5 and d5 = 72 handle that correctly. |
| Sam Altman | 44 | 53 | 44 / 51 | Centre placement is right for Sept 2026. A year ago he would have been ~60 on the limit; the move is documented. |
| Dario Amodei | 60 | 36 | 60 / 35 | Right. Note the documented reversal: Jan 2026 "stopping or even substantially slowing… fundamentally untenable" → Sept 2026 "We must slow the pace". |
| Demis Hassabis | 47 | 44 | 47 / 39 | Limit was too high; see above. After the patch he sits just above Amodei, which matches what both said at Davos and in September. |
| Stuart Russell | 82 | 9 | 82 / 9 | As expected. |
| Emily M. Bender | 37 | 35 | 37 / 36 | Looks odd, is defensible. Road 37 comes almost entirely from d8 = 10 and d9 = 30 (she thinks the technology is bad and the guardrails don't work), not from any belief in catastrophe (d1, d3, d5 ≤ 4). Worth a one-line explanation on her card, because a reader will expect her near road 10. Five of her eight danger answers reject the premise; keep them `low`. |
| Gary Marcus | 51 | 21 | 51 / 21 | Right. "Unreliable tech, weak institutions, no superintelligence soon" lands mid-road; his Sept 2026 post confirms the low limit ("salute their tentative agreement to slow down"). |
| Vitalik Buterin | 54 | 43 | 54 / 43 | Right. July 2026 (X, via press): he would rather take "the narrow corridor at 60 kph and not 200 kph" — usable on his card. |
| Max Tegmark | 89 | 6 | 89 / 6 | As expected. |
| Daniel Kokotajlo | 87 | 14 | 87 / 14 | As expected; numbers survive the re-sourcing to Plan A. |
| Leopold Aschenbrenner | 67 | 65 | 67 / 64 | The surprising one, and correct: he thinks the road is dangerous (RLHF "will predictably break down", takeoff in under a year) and still wants to race. All his texts are from June 2024; nothing newer on risk was found. Say so on the card. |

---

## Per-figure checks

Format: item = first-team value (conf) → verdict. "→" marks a proposed change.

### 1. Eliezer Yudkowsky (97 / 4)

| Item | Verdict | Evidence |
|---|---|---|
| d1 = 99 (high) | OK | TIME 2023: the most likely result is that "literally everyone on Earth will die". https://time.com/6266923/ai-eliezer-yudkowsky-open-letter-not-enough/ |
| d2 = 97 (high) | OK, fix wording | AGI Ruin §25: "no idea what's actually going on inside the giant inscrutable matrices". The "closer to alchemy" phrase is Semafor's paraphrase, not his. https://intelligence.org/2022/06/10/agi-ruin/ |
| d7 = 3 (high) | OK | AGI Ruin §43: "not what a surviving world looks like" (it is in AGI Ruin, not in TIME). |
| d9 = 2 (high) | OK | AGI Ruin §21: "Capabilities generalize further than alignment". |
| s1 = 99 (high) | OK | TIME: moratorium "indefinite and worldwide… no exceptions, including for governments or militaries". |
| s2 = 2 (high) | BASIS | Semafor's "should shut down" is the reporter's sentence ("according to Yudkowsky and Soares"). Re-base on TIME + AGI Ruin §26. https://www.semafor.com/article/09/12/2025/researchers-give-doomsday-warning-about-building-ai-too-fast |
| s4 = 98 (high) | OK | TIME: "immediate multinational agreements"; "destroy a rogue datacenter by airstrike". |
| s8 = 99 (high) | OK | TIME: solving safety "could very reasonably take at least half that long" (i.e. decades) and he still wants the halt. |
| d8 = 3, s13 = 1 (high) | OK | Same TIME sentence as d1; "Shut it all down." |

Other flags: `d3` = 90 (high) has the basis "Same as v1" — an internal note, not a basis; rewrite before publishing. `s11` = 3 (high) has no quote in the sources opened; stance makes it safe, but label it `med` or add a quote. Source 7 (X post) could not be opened and its context is unclear by the first team's own note.

### 2. Marc Andreessen (12 / 93)

All quotes verified verbatim in the cited pages.

| Item | Verdict | Evidence |
|---|---|---|
| d1 = 3, d5 = 4 (high) | OK | "AI doesn't want, it doesn't have goals"; "a superstitious handwave". https://a16z.com/ai-will-save-the-world/ |
| d8 = 97 (high) | OK | Title and thesis; manifesto: "our alchemy, our Philosopher's Stone". https://a16z.com/the-techno-optimist-manifesto/ |
| s1 = 1, s13 = 92 (high) | OK | "Our enemy is deceleration"; big AI companies "should be allowed to build AI as fast and aggressively as they can". |
| s8 = 3, s10 = 92 (high) | OK | "any deceleration of AI will cost lives… a form of murder". Add this quote to s8's basis, which has none. |
| s6 = 5 (high) | OK | "Our enemy is the Precautionary Principle". |
| s7 = 95 (high) | OK | "not aware of a single actual bad use for AI… that's not already illegal". |
| s5 = 95 (high) | OK | "We win, they lose." |
| s3 = 2, p1 = 8 (high) | OK | "government-protected cartel"; "the wolf is being invited into the henhouse". https://fortune.com/2023/07/11/vc-billionaire-marc-andreessen-ai-regulation-bootleggers-big-companies-cartel/ |
| s4 = 3 (high) | OK | "AI isn't nukes, it's math"; regulation of AI "is the foundation of a new totalitarianism". https://fortune.com/2024/03/04/elon-musk-marc-andreessen-vinod-khosla-ai-openai-sam-altman-china-debate/ |
| s11 = 95 (high) | OK | Open source "should be allowed to freely proliferate… no regulatory barriers". |

No statement by him on the July 2026 incident or the pacing essay was found; nothing suggests a shift.

### 3. Guillaume Verdon (25 / 91)

| Item | Verdict | Evidence |
|---|---|---|
| d1 = 6 (med) | OK | Lex #407: p(doom) is "a very sloppy calculation"; "I don't have a p(doom)". https://lexfridman.com/guillaume-verdon-transcript |
| d5 = 10 (med) | OK | e/acc notes: "No need to worry about creating 'zombie' forms of higher intelligence". https://beff.substack.com/p/notes-on-eacc-principles-and-tenets |
| d8 = 95 (high) | ADJUST → 90 (med) | The quoted 'maximal growth' is not in the source. What he says is about growth, not human welfare: "the options are to grow or die"; e/acc is "not just centred on humanity". https://www.abc.net.au/news/2024-02-18/ai-insiders-eacc-movement-speeding-up-tech/103464258 |
| s1 = 1, s13 = 95 (high) | OK | "You cannot stop the acceleration"; Lex: "I don't think stagnation or slowing down is actually an option". Note he objects to the caricature: "we get painted as reckless, trying to go as fast as possible". 95 stands, within tolerance. |
| s8 = 5 (high) | BASIS | No quote in basis; use the Lex sentence above. |
| s3 = 3, s6 = 5 (high) | OK | Lex: the market is "much more efficient… than sort of heavy-handed regulations that are written by the incumbents". |
| s4 = 3, p1 = 3 (high) | OK | Lex: "I just want separation of AI and state". |
| s7 = 85 (med) | OK | Lex: "whoever deploys an AI system is liable for… what it does". |

All substantive sources are 2022–2024. Nothing from 2026 on risk was found; say "as of 2024" on the card.

### 4. Yann LeCun (20 / 86)

| Item | Verdict | Evidence |
|---|---|---|
| d1 = 2 (high) | ADJUST → 5 (high), new basis | The "essentially zero" post describes "most leading AI figures". On 21 Apr 2026 he posted "I didn't say p(doom) was zero" — estimates are "pulled out of thin air". Keep very low; never print "zero" as his figure. https://x.com/ylecun/status/2046577402264870958 (402 to bots; text from search index) |
| d3 = 5 (high) | OK | Lex #416: "It's not going to be an event. It's going to be gradual progress." https://lexfridman.com/yann-lecun-3-transcript |
| d5 = 5 (high) | OK | TIME 2024: "The desire to dominate is not correlated with intelligence at all." https://time.com/6694432/yann-lecun-meta-ai-interview/ |
| d8 = 93 (high) | OK | Lex: "AI basically will amplify human intelligence"; printing-press analogy. The word 'renaissance' is in neither cited source — drop it or source it. |
| s1 = 1 (high) | OK | Sept 2026, on Amodei: "I made fun of them then. Everyone should make fun of them now." https://techstartups.com/2026/09/14/china-michael-burry-and-yann-lecun-reject-openai-and-anthropic-calls-to-slow-ai-development-lecun-calls-warnings-fake/ |
| s8 = 5 (high) | ADJUST → 8 (med) | No statement on the trade-off itself; inferred from stance. |
| s13 = 85 (med) | OK | Same Sept 2026 quote. |
| s11 = 97 (high) | OK | TIME: "The future has to be open source". |
| p4 = 90 (high) | OK | Lex, verbatim: concentration of power through proprietary AI is "a much bigger danger than everything else". |

### 5. Geoffrey Hinton (78 / 18)

| Item | Verdict | Evidence |
|---|---|---|
| d1 = 90 (high) | OK | Newsnight, 9 Sept 2026: "A ten percent chance seems not an unreasonable estimate to me" (the presenter proposed the number; he accepted it). https://www.ladbible.com/technology/ai-warning-newsnight-robert-peston-victoria-derbyshire-hinton-839854-20260910 |
| d5 = 70 (med) | OK | AIs "will very quickly develop two subgoals… stay alive… get more control". https://fortune.com/2025/08/14/godfather-of-ai-geoffrey-hinton-maternal-instincts-superintelligence/ |
| d9 = 8 (high) | BASIS | The steering-wheel line is about regulation. Use Ai4, Aug 2025, on keeping AI "submissive": "That's not going to work. They're going to be much smarter than us." https://www.cnn.com/2025/08/13/tech/ai-geoffrey-hinton |
| s1 = 70 (med) | OK | ABC, 14 Sept 2026: until control is solved "it would be foolish to develop them" (superintelligent AI), and also "I don't think we should stop developing it altogether". Both halves are his; 70/med is the honest reading. https://www.abc.net.au/news/2026-09-14/godfather-of-ai-geoffrey-hinton-backs-ai-slow-down/107150010 |
| s8 = 90 (high) | BASIS | Basis has no quote. Use: Amodei's call is "very sensible" (same ABC piece). |
| s6 = 90 (high) | OK, soften | ABC reports it as "governments could require pre-release testing" — indirect speech. Number fine; do not print it inside quotation marks. |
| s11 = 5 (high) | OK | TechCrunch, Aug 2026: open weights let people cheaply retrain models "to do bad things like cyber attacks"; "that battle's been lost". https://techcrunch.com/2026/08/12/as-ai-safety-concerns-mount-three-pioneers-make-the-case-for-staying-open/ |
| s13 = 3 (high) | OK | "very sensible". |
| s7 = 8 (high) | OK | "They want a very fast car with no steering wheel" — correctly used here. https://techxplore.com/news/2026-04-ai-alarm.html |
| d8 = 45 (low) | OK | ABC, 14 Sept 2026: AI is "doing tremendous good" — next to a 10–20% extinction estimate. No median stated; `low` is right. |

Better source for s3 (70, med): he co-authored "Managing extreme AI risks": "Governments must be prepared to license their development". https://arxiv.org/abs/2310.17688

### 6. Yoshua Bengio (79 / 13)

| Item | Verdict | Evidence |
|---|---|---|
| d1 = 80 (high) | OK | DOAC, Dec 2025: even 1% "would be unacceptable"; ML researchers "more like 10%". The "~20%" in the basis is not in the three cited sources in his own voice; it dates from 2023 interviews. Add one or say "has cited 10–20%". https://singjupost.com/transcript-ai-pioneer-yoshua-bengio-on-the-diary-of-a-ceo-podcast/ |
| d2 = 92 (high) | OK | 2024 blog, verbatim: "nobody currently knows how such an AGI or ASI could be made to behave morally". https://yoshuabengio.org/en/blog/reasoning-through-arguments-against-taking-ai-safety-seriously |
| d8 = 45 (low) | OK | 80k, Apr 2026: "there's a substantial chance that things work out OK"; "I hope that we are wrong". https://80000hours.org/podcast/episodes/yoshua-bengio-scientist-ai/ |
| d9 = 5 (high) | OK | 11 Sept 2026: "the whack-a-mole game is likely to fail". https://yoshuabengio.org/en/blog/why-are-ai-agents-lying-cheating-and-coordinating |
| s1 = 72 (med) | OK | DOAC: "I would press the button"; 80k shows he is building, not halting. Med is right. |
| s3 = 82 (high) | BASIS | The cited Senate blog post never uses the word licence ("restricting or prohibiting… like in the pharmaceuticals…"). The licensing sentence is in arXiv 2310.17688, which he first-authored. |
| s4 = 85 (high) | OK | AFP, 16 Sept 2026: "a bit like nuclear weapons are an international challenge"; "institutions, treaties, and democratic safeguards". https://www.digitaljournal.com/article/were-losing-control-ai-pioneer-yoshua-bengio-tells-afp/ |
| s6 = 95 (high) | OK | Verbatim: no training or deployment "without a strong safety case that convinces independent experts". |
| s8 = 92 (high) | OK | Verbatim: "slow down, find the cure for cancer a bit later". |
| s9 = 95, s13 = 2 (high) | OK | 80k: "even a 1% chance… is not acceptable to me"; Sept 2026 blog: "This suggests pacing the advances". |
| p4 = 60 (med) | OK | 80k: power concentration "probably even more likely than actually loss of control". |

Shift noted: Fortune, Jan 2026 — "now very confident" that systems without hidden goals can be built. That is about his own architecture; it does not lift d9 or d5, and the first team scored it correctly.

### 7. Sam Altman (44 / 53 → 44 / 51)

| Item | Verdict | Evidence |
|---|---|---|
| d1 = 45 (low) | OK | 14 Sept 2026: "we could lose control of the future to AI. This is unacceptable". No number ever given; `low` is right. https://finance.yahoo.com/technology/article/openai-ceo-sam-altman-on-ai-we-could-lose-control-091146594.html |
| d8 = 90 (high) | OK | Gentle Singularity: intelligence and energy "are going to become wildly abundant". https://blog.samaltman.com/the-gentle-singularity |
| d9 = 35 (med) | OK | Same X post: alignment and safety techniques must "stay ahead of progress in model capabilities". |
| s1 = 3 (high) | OK | 14 Sept 2026: "When we talk about 'pacing', we do not mean 'stopping'." Add to basis. https://www.businesstoday.in/technology/story/no-amount-of-us-pressure-should-justify-recklessness-sam-altman-backs-slow-frontier-ai-pace-555358-2026-09-14 |
| s8 = 55 (med) | ADJUST → 65 (med) | Same post: progress "should be slower than it otherwise could be… Pacing will be well worth this cost." That is an explicit "worth it"; 55 reads as neutral. Not higher, because he speaks of pacing, not years of delay. |
| s13 = 15 (med) | ADJUST → 10 (high) | Same sentence is a near-verbatim negation of the item. |
| s5 = 75 (high) | ADJUST → 70 (med) | Basis has no quote. 2025 Senate: China is "not a huge amount of time" behind. But Sept 2026: "no amount of American competitive pressure should justify recklessness". https://www.techpolicy.press/transcript-sam-altman-testifies-at-us-senate-hearing-on-ai-competitiveness/ |
| s6 = 45 (med) | OK | Senate 2025, on mandatory vetting before release: "I think that would be disastrous"; Sept 2026: OpenAI now writes "explicit safety cases in advance of frontier reinforcement learning runs". Both directions are real. |
| s4 = 50 (med) | OK | Delhi, Feb 2026: "something like an IAEA". https://www.outlookindia.com/national/ai-impact-summit-2026-altman-calls-for-global-ai-regulator-says-superintelligence-could-arrive-within-years |
| p2 = 92 (high) | OK | Delhi, verbatim 2028 claim. |
| p4 = 50 (med) | OK | Names both failure modes in the same post. |

### 8. Dario Amodei (60 / 36 → 60 / 35)

| Item | Verdict | Evidence |
|---|---|---|
| d1 = 70 (med) | OK | Axios Sept 2025: "25% chance that things go really, really badly" (Axios blocks fetches; confirmed via search index and syndication). Broader than extinction; `med` is right. |
| d3 = 78 (high) | OK | Sept 2026: recursive self-improvement "is starting to happen across the industry, including at Anthropic". https://darioamodei.com/post/we-must-pace-the-frontier |
| d5 = 35 (med) | OK (could be `high`) | Jan 2026: he disagrees that misalignment is "inevitable, or even probable, from first principles". https://www.darioamodei.com/essay/the-adolescence-of-technology |
| d8 = 85 (high) | OK | "75% chance that things go really, really well" (Axios); Jan 2026: "I would even say our odds are good". |
| d9 = 25 (med) | OK, note | Jan 2026: "fairly optimistic that Claude's constitutional training will be more robust… than people might think". That argues for ~35; within tolerance, left alone. |
| s1 = 8 (high) | ADJUST → 15 (med) | Basis is wrong: the June 2026 essay never mentions pausing. Jan 2026: stopping is "fundamentally untenable". Sept 2026: "Pacing does not mean halting", but on an intergovernmental pause: "I support floating this, but I think it is unlikely". Someone who supports floating a pause is not at 8. |
| s4 = 70 (med) | OK | RSI "speed limit… analogous to the SALT treaties". |
| s5 = 70 (med) | OK | Sept 2026: "Do not sell powerful AI chips… to China". |
| s6 = 82 (high) | OK | June 2026, verbatim: models above a threshold "should undergo mandatory testing by a qualified third party"; government "should have the power to block or deter deployment". https://darioamodei.com/post/policy-on-the-ai-exponential |
| s8 = 75 (high) | OK | "an extra year or two… could greatly reduce the risk that something goes seriously wrong". |
| s13 = 6 (high) | OK | "We must slow the pace at which we improve the capabilities of AI models." |
| p1 = 50 (med) | OK, fix src | 'safety theater' and 'coerce unwilling actors' are in the January essay (source 2), not the June one (source 1). |
| p5 = 35 (med) | OK | Pause "unlikely to actually happen any time soon". |

### 9. Demis Hassabis (47 / 44 → 47 / 39)

| Item | Verdict | Evidence |
|---|---|---|
| d1 = 40 (low) | OK | No number anywhere; July 2026 essay names loss of control of "recursively self-improving systems" as a horizon risk. `low` is right. https://demishassabis.substack.com/p/a-framework-for-frontier-ai-and-the-dawning-of-a-new-age |
| d8 = 88 (high) | OK | 60 Minutes: end of disease "within reach. Maybe within the next decade or so"; essay: "an amazing new era of abundance". https://www.cbsnews.com/news/artificial-intelligence-google-deepmind-ceo-demis-hassabis-60-minutes-transcript/ |
| d7 = 30 (med) | OK, fix quotes | "Regulators are struggling…" is AFP's paraphrase, and "before the first major incident" is in none of the cited pages. Remove the quotation marks. |
| s1 = 5 (high) | ADJUST → 15 (med) | Davos, Jan 2026, asked if he would advocate a pause were every company and country to join: "I think so." And in Delhi AFP says he answered that his company "could contribute" to slowing — the first team read that as a refusal. https://www.transformernews.ai/p/ai-ceos-want-to-slow-down-the-worlds-davos-demis-hassabis-dario-amodei |
| s8 = 50 (med) | ADJUST → 72 (med) | Davos: "good to have a slightly slower pace than we're currently predicting"; July essay: risks are manageable "only if we give ourselves the time and space… Currently… we aren't doing that"; 12 Sept 2026 on Amodei's essay: "the direction is correct for meeting this critical moment". https://www.latestly.com/technology/demis-hassabis-backs-dario-amodeis-call-to-slow-down-frontier-ai-race-warns-of-escalating-risks-7603427.html |
| s13 = 20 (med) | ADJUST → 10 (high) | Same three statements; each negates "no deliberate slowing down". |
| s6 = 70 (high) | OK | Essay, verbatim: frontier models "would be required to pass it to be deployed in the US market" — after a voluntary phase. |
| s7 = 10 (high) | OK | Whole essay proposes a new standards body. |
| p2 = 85 (high) | OK | "probably only a few short years away". Note Jan 2026 he still said "five to 10 years" / 50% within the decade (Fortune); the July essay is the shift. |

### 10. Stuart Russell (82 / 9)

| Item | Verdict | Evidence |
|---|---|---|
| d1 = 78 (med) | OK | DOAC: cites CEOs' own 25–30% and says acceptable risk is orders of magnitude lower; declines a number. https://singjupost.com/stuart-russell-on-the-diary-of-a-ceo-podcast-transcript/ |
| d2 = 92 (high) | OK | Berkeley 2024: "What's happening inside the large language models? We haven't the faintest idea." https://vcresearch.berkeley.edu/news/how-keep-ai-killing-us-all |
| d8 = 40 (med) | OK | DOAC: a describable good AI future "does not, as far as I know, exist". |
| s1 = 78 (high) | OK | DOAC: on a stop-forever button "I think I'd probably press it" ("on the fence"); on a 50-year stop: "I would say, yes." Note his own gloss on the 2025 statement: "not a ban or even a moratorium in the usual sense". 78 is fair. |
| s5 = 8 (high) | OK | "China's AI regulations are actually quite strict". |
| s6 = 97 (high) | OK | Verbatim: "you can't turn on artificial general intelligence until you've shown that it's safe". |
| s9 = 97 (high) | OK | "One in 100 million per year." |
| s10 = 5 (high) | OK | Senate 2023: "there is no tradeoff between safety and innovation". https://humancompatible.ai/blog/2023/09/11/ai-regulation-stuart-russells-opening-statement-at-u-s-senate-hearing/ |
| s3 = 80 (med) | OK | "make AI safety a condition of doing business"; co-author of arXiv 2310.17688 (licensing). |
| p2 = 85 (high) | OK | "80% unemployment". |
| s8 = 95, s13 = 2 (high) | OK | DOAC: would press a 50-year stop button ("I would say, yes"). |

### 11. Emily M. Bender (37 / 35 → 37 / 36)

| Item | Verdict | Evidence |
|---|---|---|
| d1 = 3 (high) | OK | 16 Sept 2026, verbatim: the kill-us-all idea "distracts from the real harms that are happening now". https://www.sfexaminer.com/news/technology/ai-skeptics-warn-existential-risk-talk-a-distraction/article_44fe8eca-bdb9-4d19-bfa2-c01cd93287c1.html |
| d3 = 3 (high) | OK | TechPolicy.Press: the "racist pile of linear algebra combusts into consciousness" line is hers. https://www.techpolicy.press/taking-on-the-ai-con/ |
| d6 = 97 (high) | OK | DAIR 2023: longtermism "ignores the actual harms… today". https://www.dair-institute.org/blog/letter-statement-March2023/ |
| s1 = 25 (low) | OK | DAIR: the pause letter is "fearmongering and AI hype". `low` is right: premise rejected. |
| s5 = 5 (high) | ADJUST → 8 (med) | The quoted sentence is about who benefits from hype, not about states racing. Nearest primary text: the race is "not a preordained path where our only choice is how fast to run". |
| s6 = 85 (high) | OK | DAIR, verbatim: "the onus of creating tools that are safe to use should be on the companies". |
| s10 = 3 (high) | ADJUST conf → med | No statement of hers on the trade-off in the sources opened. |
| s13 = 8 (high) | OK | Same DAIR sentence. Better basis than the Wikipedia summary currently cited. |
| p2 = 5 (high) | OK, note | The job quote is Alex Hanna's, as the basis admits; keep the attribution visible on the site. |
| p4 = 90 (high) | OK | Carnegie 2024: longtermist worries are "fantasies"; liability belongs to OpenAI. https://www.carnegiecouncil.org/media/series/aiei/linguistics-automated-systems-power-ai-emily-bender |
| d8 = 10 (med) | OK | Book site: AI hype exists to hide "power grabs"; the promised benefits are the con. https://thecon.ai/ |
| s8 = 50 (low) | OK | Premise rejected on both sides of the trade; already at 50/low, which is what an unsupported item should be. |

### 12. Gary Marcus (51 / 21)

| Item | Verdict | Evidence |
|---|---|---|
| d1 = 15 (high) | OK | p(doom) "about 3%"; humans "genetically diverse, geographically diverse, and remarkably resourceful". https://garymarcus.substack.com/p/why-my-pdoom-has-risen-dramatically |
| d3 = 10 (med) | OK | March 2026: 2–3 year AGI timelines "don't even pass the sniff test". https://garymarcus.substack.com/p/how-agi-is-nigh-doomers-own-goaled |
| d7 = 10, s2 = 3 (high) | OK | "voluntary agreements between companies are not going to cut it". |
| s1 = 25 (med) | OK | 13 Sept 2026: the Sanders–Casar ban is "draconian… imprisoning people for even doing research on superintelligence". https://garymarcus.substack.com/p/two-cheers-out-of-three-for-dario |
| s5 = 15 (high) | OK | Same post, on "whoever wins AI wins": "I continue to oppose this zero-sum thinking". Add as basis (current basis has no quote). |
| s8 = 75 (med) | OK | Same post: "We should all salute their tentative agreement to slow down the acceleration of this technology". |
| s10 = 8 (high) | OK | Same post: AI is "not going to cure cancer either, at least not anytime soon or on its own". Add as basis. |
| s13 = 5 (high) | OK | As above. |
| d8 = 40 (low) | OK | Nothing found either way; already `low` and near 50, as an unsupported item should be. |
| s3 = 80, s6 = 92 (high) | not verifiable here | Senate PDF is bot-blocked (403); widely reported, not opened. |

### 13. Vitalik Buterin (54 / 43)

| Item | Verdict | Evidence |
|---|---|---|
| d1 = 50 (high) | OK | 80k, Oct 2025: "maybe 9%, maybe 8%"; Doom Debates, Aug 2025: "About 12% right now". Straddles the 10% line; 50 is the correct encoding. https://80000hours.org/podcast/episodes/vitalik-buterin-techno-optimism/ |
| d2 = 70, d9 = 25 (med) | OK | "very possible that super intelligent AI alignment is intractable". https://lironshapira.substack.com/p/debate-with-vitalik-buterin-will |
| s1 = 15 (high) | OK | 80k: "you're buying time. And the question is… what are you buying time for?" |
| s4 = 60 (med) | OK | Verbatim: "even in favor of some AI decelerationist policies… international compute treaties". |
| s8 = 65 (med) | OK | Soft pause "to buy more time for humanity to prepare". July 2026 X thread (via press): "60 kph and not 200 kph" — supports 65–70. https://cointelegraph.com/news/buterin-soft-pause-ai-compute-prepare-risky-ai · https://www.cryptotimes.io/2026/07/20/vitalik-buterin-explores-ai-capability-waves-deeper-human-machine-integration/ |
| s11 = 85 (high) | OK | "Open source good". |
| s13 = 15 (high) | OK | Same. |
| p1 = 20 (high) | OK | "the most powerful Big Brother from which there is no escape". |
| d8 = 70 (med) | OK | 2023: "I believe in a future that is vastly brighter than the present" — with "multiple paths forward… some good, some bad". https://vitalik.eth.limo/general/2023/11/27/techno_optimism.html |

Source 1 (d/acc: one year later) truncates in fetchers before the AI section, as the first team noted; the Cointelegraph report is an adequate stand-in.

### 14. Max Tegmark (89 / 6)

| Item | Verdict | Evidence |
|---|---|---|
| d1 = 97 (high) | OK | Doom Debates: "definitely over 90% that we lose control" absent FDA-style rules; Guardian: 90% Compton constant. https://lironshapira.substack.com/p/max-tegmark-vs-dean-ball-debate-ban-superintelligence |
| d5 = 90 (high) | OK | Web Summit 2024: "they will take control, they'll make us irrelevant". https://www.nextgov.com/artificial-intelligence/2024/11/team-human-vs-ai-mit-expert-issues-warning-artificial-general-intelligence-risks/401331/ |
| d7 = 5, s7 = 2 (high) | OK | "more regulations on sandwiches than superintelligence". |
| d8 = 40 (med) | OK | "I am an optimist… as long as we don't build AGI" — conditional, so 40/med is right. |
| s1 = 92 (high) | OK | Statement text verified verbatim; FLI press release names him. https://futureoflife.org/press-release/prominent-scientists-faith-leaders-policymakers-and-artists-call-for-a-prohibition-on-superintelligence/ |
| s6 = 97 (high) | OK | "demonstrate that you can keep this under control". |
| s10 = 5 (high) | OK | Tool AI delivers the cures; AGI is "unnecessary, undesirable and preventable". |
| s4 = 85 (high) | OK | "political will" for "global safety regimes". https://www.inkl.com/news/ai-firms-warned-to-calculate-threat-of-super-intelligence-or-risk-it-escaping-human-control |
| s8 = 97, s13 = 1 (high) | OK | Statement text (prohibition until consensus and buy-in); AGI is "unnecessary, undesirable and preventable". |

### 15. Daniel Kokotajlo (87 / 14)

The numbers are right; the sourcing is the problem. "How to pace the US frontier" (source 4) is by Lifland, Halstead, Dean, Larsen and one other; its acknowledgements thank Kokotajlo "for helpful feedback". He *is* a co-author of AI 2040 Plan A (listed sixth of six — the bio's "lead author" of AI 2040 should become "co-author") and of the Aug 2026 timelines update.

| Item | Verdict | Evidence |
|---|---|---|
| d1 = 92 (high) | OK, weak source | ~70% catastrophic, known here only through Shortform's summary. Replace with the episode or a transcript. |
| d3 = 92 (high) | OK | Timelines update (co-author): "Daniel's median estimates" given explicitly. https://blog.aifutures.org/p/q25-2026-timelines-update-uplift |
| d8 = 30 (med) | OK | Plan A is "a recommendation, not a prediction". https://blog.aifutures.org/p/ai-2040-plan-a |
| s1 = 50 (med) | OK | Plan A: "temporarily pause training", then "resume R&D under safety-case regulation"; ASI in 2040. https://ai-2040.com/about |
| s4 = 92 (high) | OK | Plan A: US and China build a verifiable brake pedal (the site spells it "break pedal"). |
| s8 = 97, s6 = 90 (high), s3 = 70 (med) | BASIS | Re-base on Plan A: they "delay the creation of superintelligence to 2040"; "Track where all the compute is". |
| s5 = 25 (med) | ADJUST → 30 (low) | The unilateral-pacing argument is his colleagues', not his; Plan A is bilateral. |
| s9 = 95 (high) | ADJUST conf → med | Inference from the 70% figure; no statement on a 1% threshold. |
| s13 = 2 (high) | OK | Plan A suffices. |
| p2 = 95 (high) | OK | ASI median March 2029 in the co-authored update. |

### 16. Leopold Aschenbrenner (67 / 65 → 67 / 64)

All substantive sources are from June 2024. No 2025–26 statement on risk or pace was found; his fund was force-unwound on 30–31 July 2026 (CNBC), which the bio already reflects.

| Item | Verdict | Evidence |
|---|---|---|
| d1 = 55 (low) | OK | "I am not a doomer. Misaligned superintelligence is probably not the biggest AI risk" — yet failure "could easily be catastrophic". `low` is right. https://situational-awareness.ai/superalignment/ |
| d3 = 95 (high) | OK | Human-level to vastly superhuman in "less than a year". |
| d9 = 10 (high) | OK | Verbatim: "RLHF will predictably break down as AI systems get smarter". Put this quote in the basis. |
| d7 = 30 (low) | OK | "No startup can handle superintelligence" vs the Burkean passage on courts and checks and balances. https://situational-awareness.ai/the-project/ |
| s1 = 3 (high) | OK | "strongly advocated against policies like an AI pause". |
| s2 = 85, s5 = 97 (high) | OK | A "healthy lead, say 2 years"; the free world must prevail. https://situational-awareness.ai/the-free-world-must-prevail/ |
| s4 = 30 (med) | OK, note | "Some hope for some sort of international treaty on safety. This seems fanciful to me" — but a deal and a nonproliferation regime once the US has won. 20–30 both defensible. |
| s13 = 65 (med) | ADJUST → 55 (med) | Superalignment "very well may require us to slow down at some critical moments"; a lead lets the US "cash in" part of it "to get safety right". That is deliberate slowing, which the item excludes. |
| s11 = 5 (high) | OK | Open-sourcing gives the CCP "free access to US-developed superintelligence". |
| p5 = 15 (high) | BASIS | The theft quote is about security. Use: "any arms control equilibrium… seems extremely unstable… 'breakout' is too easy". |
| p1 = 70 (med) | OK | CEOs "would have the power to literally coup the US government". |
| d8 = 65 (med) | OK | "Strong optimist that this problem is solvable", but "most worried about things just being totally crazy around superintelligence". Med is right. |
| s8 = 25 (med) | OK | Will "cash in" part of a lead for safety, yet "strongly advocated against" any pause. |

---

## `high` confidence without a quote

174 predictions are marked `high`. 33 of them print a basis with no quotation at all. Triage:

**Keep `high`, but add the quote (found during this audit):** Andreessen s8 ("a form of murder"), s11 ("freely proliferate"); LeCun s11 ("The future has to be open source"); Hinton s8, s13 ("very sensible"), s11 (TechCrunch); Bengio s9 ("even a 1% chance… is not acceptable to me"), s13 ("pacing the advances"); Verdon s6 (market "much more efficient"), s8 ("slowing down is [not] an option"); Amodei s7 (government "should have the power to block or deter deployment"); Russell s7 (Senate list, "all of which I support"), s9 ("One in 100 million per year"); Marcus s5 ("zero-sum thinking"), s10 ("not going to cure cancer"); Tegmark d6 and s9 ("over 90% that we lose control"; Compton's one-in-three-million bar); Kokotajlo d3 (own medians), s10 (Plan A delays ASI to 2040), d6, s7; Aschenbrenner d6 (footnote: "novel WMDs, destructive wars"); Yudkowsky s6, s7, s8, s9, s13 (TIME op-ed: indefinite worldwide moratorium, "no exceptions").

**Downgrade to `med` (in the patch):** Altman s5; LeCun s8; Bender s5, s10; Kokotajlo s9; Verdon d8; Hassabis s1; Amodei s1.

**Rewrite before publishing (not in the patch — needs the first team):** Yudkowsky d3 ("Same as v1" is a note to self); Yudkowsky s11 (no quote; label `med` until one is added).

Also `high` with a quote that is not the person's: Yudkowsky s2 and d2 (Semafor paraphrases), Hinton d9 (wrong topic), Hinton s6 (indirect speech), Hassabis d7 and s1 (AFP paraphrases), Bender p2 (co-author's words, disclosed), LeCun d1 (describes others), Kokotajlo s3/s5/s6/s8 (colleagues' post).

## Source problems

No URL is dead. HTTP sweep of all 141 source URLs on 17 Sept 2026: 127 answered 200; 14 answered 403/406/429 to a scripted request and open normally otherwise (TIME ×8, Axios, ACM, senate.gov, TechXplore, VentureBeat ×2). x.com answers 200 to a HEAD-style request but 402 to a content fetch, so none of the four X posts cited as sources could be read directly.

Sources that resolve but do not say what the note or basis claims (details and URLs in the patch file, `deadSources`):

1. Amodei source 1 — "Rejects pausing": not in the essay.
2. Kokotajlo source 4 — not his text.
3. Hinton source 6 — steering-wheel metaphor is about regulation.
4. Yudkowsky source 3 — reporter's paraphrases printed as quotes.
5. LeCun source 8 — describes "most leading AI figures"; later clarified.
6. Bengio source 0 — no "licences" on the page.
7. Hassabis source 2 — AFP paraphrases printed as quotes; "before the first major incident" untraceable.
8. Verdon source 0 — no "maximal growth".
9. Hinton/Bengio source 4 (TIME) — names neither man.
10. Kokotajlo source 5 — third-party summary as sole support for the 70% figure.
11. Yudkowsky source 7 — unreadable X post of unclear context.

## Summary of proposed changes

Numbers and confidence:

| # | Figure | Item | From | To | Conf | Why (short) |
|---|---|---|---|---|---|---|
| 1 | Hassabis | s8 | 50 | 72 | med | Davos "slightly slower pace"; endorsed the pacing essay |
| 2 | Hassabis | s13 | 20 | 10 | med → high | same |
| 3 | Hassabis | s1 | 5 | 15 | high → med | "I think so" to a universal pause |
| 4 | Altman | s8 | 55 | 65 | med | "Pacing will be well worth this cost" |
| 5 | Altman | s13 | 15 | 10 | med → high | "slower than it otherwise could be" |
| 6 | Altman | s5 | 75 | 70 | high → med | no verbatim; "competitive pressure" caveat |
| 7 | Amodei | s1 | 8 | 15 | high → med | basis false; "I support floating this" (pause) |
| 8 | Aschenbrenner | s13 | 65 | 55 | med | "may require us to slow down at some critical moments" |
| 9 | Kokotajlo | s5 | 25 | 30 | med → low | basis was his colleagues' post |
| 10 | LeCun | d1 | 2 | 5 | high | "I didn't say p(doom) was zero" |
| 11 | LeCun | s8 | 5 | 8 | high → med | inference only |
| 12 | Verdon | d8 | 95 | 90 | high → med | quoted phrase not in source; optimism is about growth |
| 13 | Bender | s5 | 5 | 8 | high → med | quote is off-topic |
| 14 | Bender | s10 | 3 | 3 | high → med | no statement found |
| 15 | Kokotajlo | s9 | 95 | 95 | high → med | inference from a secondary source |

Basis replaced, number unchanged: Hinton d9, Hinton s8, Bengio s3, Yudkowsky s2, Verdon s8, Kokotajlo s8, Kokotajlo s6, Kokotajlo s3, Aschenbrenner p5.

Net effect on the map: Hassabis limit 44 → 39; Altman limit 53 → 51; Aschenbrenner limit 65 → 64; Amodei limit 36 → 35; every other figure moves by less than one point on either axis.

## Tally

- Predictions checked against a source I opened: 180 of 384 (9 to 14 per figure; for every figure all of d1, d8, s1, s8 and s13, and most d5 and d9). Two more (Marcus s3, s6) could not be checked because the Senate PDF blocks fetches.
- OK: 156 (two of these are "nothing found, but already `low` and at or near 50": Bender s8, Marcus d8). ADJUST (value and/or confidence): 15. BASIS (number fine, printed justification wrong): 9.
- Source entries flagged: 11. Dead URLs: 0.
