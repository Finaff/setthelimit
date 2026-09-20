# figures-a — research notes (batch A: Yudkowsky, Andreessen, Verdon, LeCun, Hinton, Bengio, Altman)

Companion to `research/figures-a.json`. Predictions are made against
`content/propositions.v2.json` (24 ids; `contentVersion: "v2"`).
The four ids dropped from v1 (d4, d10, s12, p3) are kept under each figure's `v1Only` key for reference only.
Compiled 16 September 2026. Every URL below was fetched with WebFetch unless marked **(indexed only)** — X/Twitter
blocks our fetcher, so those posts are cited from the text returned by the search index and should be spot-checked
in a browser before going on the site. Third-party transcripts and summaries are marked **(secondary)**.

Confidence key used in the JSON: `high` = said almost verbatim; `med` = clearly implied by stated views; `low` = inferred
from general stance (a lot of `low`s sit on s9, s10, p5 and d9 — the items nobody answers directly).

---

## 1. Eliezer Yudkowsky — MIRI co-founder; camp: "argues for a global halt"

**Role check (Sept 2026).** Still at MIRI; the 2025 book with Nate Soares is his current platform (NYT bestseller Oct 2025).

**Key quotes relied on**
- "The most likely result of building a superhumanly smart AI, under anything remotely like the current circumstances, is that literally everyone on Earth will die." — TIME, 29 Mar 2023, https://time.com/6266923/ai-eliezer-yudkowsky-open-letter-not-enough/
- Policy in the same piece: an indefinite worldwide moratorium on large training runs, "no exceptions, including for governments or militaries"; shut down GPU clusters; track GPUs; be willing to "destroy a rogue datacenter by airstrike".
- "We need to get alignment right on the 'first critical try'"; "capabilities generalize further out-of-distribution than alignment"; "no idea what's actually going on inside the giant inscrutable matrices" — AGI Ruin, 10 Jun 2022, https://intelligence.org/2022/06/10/agi-ruin/
- Book thesis (publisher page): an ASI's goals would not be ours and "if it comes to conflict, an artificial superintelligence would crush us"; remedy is a coordinated halt of large-scale general AI development — https://www.hachettebookgroup.com/titles/eliezer-yudkowsky/if-anyone-builds-it-everyone-dies/9780316595643/
- Even safety-branded labs "should shut down"; the field is "closer to alchemy than science" — Semafor, 12 Sep 2025, https://www.semafor.com/article/09/12/2025/researchers-give-doomsday-warning-about-building-ai-too-fast
- "This is not the act that prevents the Earth from being destroyed -- that would take a treaty... ASI can kill you just as easily from a datacenter running outside your country." — X, 26 Mar 2026 **(indexed only; context of the post not established)**, https://x.com/ESYudkowsky/status/2037017908640178304

**Caveats**
- He is *not* an LLM sceptic in the LeCun sense: the book argues the next upgrade of today's models could be the dangerous one, so d4 (v1) is low, not high.
- He grants that an *aligned* superintelligence would be enormously beneficial; s10 (v2, prescriptive) is a firm "no" only because he thinks the risk dominates, not because he denies the benefit.
- On s5 (v2, prescriptive) he would say "no, seek a treaty", but he has also written that a unilateral US halt does not by itself save anyone — his answer is a treaty, not unilateral virtue. Value 10, med.
- MIRI's "AI Governance to Avoid Extinction" (May 2025) is institutional, by Barnett & Scher, used only as corroboration of the Off-Switch/Halt programme.
- p5 (would a pause hold) is a guess: he thinks compute is trackable but is famously pessimistic about political will. 45, low.

---

## 2. Marc Andreessen — a16z co-founder; camp: "techno-optimist"

**Role check (Sept 2026).** Co-founder and general partner, Andreessen Horowitz; still the firm's public voice on AI policy (Jan 2026 "2026 Outlook" podcast).

**Key quotes relied on**
- "AI is math – code – computers, built by people, owned by people, used by people, controlled by people"; "AI doesn't want, it doesn't have goals, it doesn't want to kill you, because it's not alive"; AI risk "has developed into a cult"; "I'm not aware of a single actual bad use for AI that's not already illegal"; "The single greatest risk of AI is that China wins global AI dominance and we... do not." — Why AI Will Save the World, 6 Jun 2023, https://a16z.com/ai-will-save-the-world/
- "Our enemy is the Precautionary Principle"; "We believe any deceleration of AI will cost lives"; "existential risk", "risk management", "tech ethics" listed in a "mass demoralization campaign" — Techno-Optimist Manifesto, 16 Oct 2023, https://a16z.com/the-techno-optimist-manifesto/
- "Big companies basically want a government-protected cartel"; licensing means "fleets of lawyers"; "You're literally telling people they can't write code and put it on the internet" — Fortune, 11 Jul 2023, https://fortune.com/2023/07/11/vc-billionaire-marc-andreessen-ai-regulation-bootleggers-big-companies-cartel/
- "AI isn't nukes, it's math. Big companies, small companies, independent developers, and open source communities should be free to pursue AI." — Fortune, 4 Mar 2024, https://fortune.com/2024/03/04/elon-musk-marc-andreessen-vinod-khosla-ai-openai-sam-altman-china-debate/
- His posts as quoted by Fortune, 21 Nov 2024: "Restricting AI means restricting math, software, and chips"; regulation of AI "is the foundation of a new totalitarianism" — https://fortune.com/2024/11/21/anthropic-ceo-dario-amodei-marc-andreessen-ai-danger-regulation-math/
- 2026: Washington has "little interest in doing anything that might prevent us from beating China"; state bills "quite scary"; Europe "kneecapping" US tech — a16z 2026 Outlook (7 Jan 2026, https://a16z.com/podcast/marc-andreessens-2026-outlook-ai-timelines-us-vs-china-and-the-price-of-ai/ ) as summarised by 36Kr **(secondary, translated)**, https://eu.36kr.com/en/p/3631555994158340

**Caveats**
- Liability (v1 s12, kept in `v1Only`): he fought SB 1047's developer liability and a16z's line is to target "the person or entity primarily responsible" for harm. Scored 15 — lower than a generic "pro-market" guess would give, per the brief's warning.
- s2 (v2): he wants America and "little tech" to build fast; the item's rationale ("the most careful developers") is not his. 70, med.
- p2 (v2): bullish on capability ("cost of intelligence is collapsing") but has repeatedly argued AI will not cause mass unemployment; scored 55, low.
- d7 (v2) no longer names the nuclear mechanism, so his objection to nuclear-style regulation no longer drags him toward "danger"; 90, med.
- The Free Press interview (10 Dec 2024) is paywalled beyond the intro; the "Biden wanted 2–3 companies" claim is from his Joe Rogan appearance (Nov 2024), not fetched, so it is not cited as a source.

---

## 3. Guillaume Verdon ("Beff Jezos") — Extropic founder/CEO; camp: "effective accelerationist (e/acc)"

**Role check (Sept 2026).** Extropic site still fronts him (TED AI SF listing); Z1 chip announced, summer-2026 updates (3 Aug 2026), "Thermodynamic Computing Chips in America" (29 Jul 2026): https://www.extropic.ai/

**Key quotes relied on**
- "You cannot stop the acceleration. You might as well embrace it"; "No need to worry about creating 'zombie' forms of higher intelligence"; top-down control "seeks to suppress variance" — e/acc principles, 10 Jul 2022, https://beff.substack.com/p/notes-on-eacc-principles-and-tenets
- p(doom) is "a very sloppy calculation"; "heavy-handed regulations that are written by the incumbents... serves them to achieve regulatory capture"; "separation of AI and state"; "we're actually for reliability engineering, we just think that the market is much more efficient" — Lex Fridman #407, 29 Dec 2023, https://lexfridman.com/guillaume-verdon-transcript
- "adversarial equilibria between various AI players" as the safeguard; "deployment liability over blanket regulation" — Podcast Notes of #407 **(secondary)**, https://podcastnotes.org/lex-fridman-podcast/guillaume-verdon-beff-jezos-e-acc-movement-physics-computation-agi-lex-fridman-podcast-407/
- "I'm not trying to actually replace humans"; e/acc is "not just centred on humanity"; "the options are to grow or die"; "we're trying to bring balance to the force" — ABC News Australia, 18 Feb 2024, https://www.abc.net.au/news/2024-02-18/ai-insiders-eacc-movement-speeding-up-tech/103464258
- Keep AGI "beyond the control of a single corporation or government"; chapter "Why open source AI doesn't need regulation"; "We are building the conduit for the thermodynamic god that created us" — Reason, 19 Dec 2024, https://reason.com/podcast/2024/12/19/guillaume-verdon-should-we-have-a-second-amendment-for-ai/

**Caveats**
- Thinnest 2025–2026 record of the seven: the Core Memory (May 2025) and MLST (Jul 2025) pages are episode intros, not transcripts, and his 2026 output is corporate (chips). Positions are stable since 2023 but many values are `low`.
- He explicitly says e/acc is "not just centred on humanity" and that human replacement is not the aim but not something he can rule out — this is why d8 is 95 while d5 is only 10 rather than 2, and p3 (v1) sits at 60.
- d7 (v2, "existing institutions and safeguards will be enough"): he distrusts institutions yet thinks decentralised competition suffices; 60, low.
- s12 (v1): he floated "deployment liability" as the alternative to regulation, so he is not a pure anti-liability voice; 40, low.

---

## 4. Yann LeCun — AMI Labs executive chairman; camp: "AI optimist, open-source advocate"

**Role check (Sept 2026).** Left Meta Nov 2025 (chief AI scientist since 2013). Founder and **executive chairman** of AMI Labs (Paris; CEO Alexandre LeBrun); $1.03B seed at $3.5B pre-money announced 9–10 Mar 2026; NYU Silver Professor.
Sources: https://techcrunch.com/2026/01/23/whos-behind-ami-labs-yann-lecuns-world-model-startup/ · https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/

**Key quotes relied on**
- Existential risk "preposterous"; "The smartest among us do not want to dominate the others"; "The future has to be open source"; LLMs "are not a path towards human-level intelligence"; "we're still very far" — TIME, 13 Feb 2024, https://time.com/6694432/yann-lecun-meta-ai-interview/
- "Autoregressive LLMs are not the way we're going to make progress towards superhuman intelligence"; "I see the danger of this concentration of power through proprietary AI systems as a much bigger danger than everything else" — Lex Fridman #416, Mar 2024, https://lexfridman.com/yann-lecun-3-transcript
- "Regulators should regulate applications, not technology... Making technology developers liable for bad uses of products built from their technology will simply stop technology development." — X, 6 Jun 2024 **(indexed only)**, https://x.com/ylecun/status/1798839294930379209
- Human-level AI "will take several years if not a decade", with "a long tail" — X, 16 Oct 2024 **(indexed only)**, https://x.com/ylecun/status/1846574605894340950
- LLMs "will never be able to achieve humanlike intelligence"; "the AI industry is completely LLM-pilled" — Fortune (Davos), 23 Jan 2026, https://fortune.com/2026/01/23/deepmind-demis-hassabis-anthropic-dario-amodei-yann-lecun-ai-davos/
- "Most 'leading AI figures' think this p(doom) estimates are complete bullshit and the existential risk is essentially zero." — X, 13 Apr 2026 **(indexed only)**, https://x.com/ylecun/status/2043673634363851250
- On Amodei's "pace the frontier" essay: "Dario was already claiming that GPT2 was too dangerous to open source back in 2019. I made fun of them then. Everyone should make fun of them now." — 13–14 Sep 2026, https://techstartups.com/2026/09/14/china-michael-burry-and-yann-lecun-reject-openai-and-anthropic-calls-to-slow-ai-development-lecun-calls-warnings-fake/

**Caveats**
- d2 and d9 are genuinely ambiguous for him: he says today's LLMs are unreliable and uncontrollable (which is his argument for a new architecture) *and* that objective-driven systems can be made controllable by design. Scored 45 and 40, both `low`.
- d4 (v1, dropped) was his clearest item (92, high); with it gone, his danger score rests on d1/d3/d5 (all near zero) and d2/d9 (middling).
- s5 (v2): less nationalist than Andreessen — his argument is that open ecosystems keep the West ahead and regulation "stifles" local AI; 75, med.
- s10 (v2): he argues AI will accelerate science but has never put a lives-lost figure on delay; 78, med.
- The Jan 2026 "TIME interview" that some search results mention appears to be a mis-dated reference to the Feb 2024 interview; only the 2024 piece was verified.

---

## 5. Geoffrey Hinton — Nobel 2024; camp: "worried pioneer"

**Role check (Sept 2026).** Professor emeritus, University of Toronto; no institutional affiliation with a lab since leaving Google in May 2023; very active in media (BBC Newsnight 9 Sep 2026; ABC RN Breakfast 14 Sep 2026).

**Key quotes relied on**
- "To predict the next word you have to understand the sentences"; "They might take over"; "I can't see a path that guarantees safety"; wants regulation and "a world treaty to ban the use of military robots" — 60 Minutes, 8 Oct 2023, https://www.cbsnews.com/news/geoffrey-hinton-ai-dangers-60-minutes-transcript/
- "If it's not going to parent me, it's going to replace me"; AIs "will very quickly develop two subgoals... stay alive... get more control"; 10–20% chance of wiping out humans — Fortune (Ai4), 14 Aug 2025, https://fortune.com/2025/08/14/godfather-of-ai-geoffrey-hinton-maternal-instincts-superintelligence/
- Signed the FLI Statement on Superintelligence: "We call for a prohibition on the development of superintelligence, not lifted before there is broad scientific consensus that it will be done safely and controllably, and strong public buy-in." — TIME, 22 Oct 2025, https://time.com/7327409/ai-agi-superintelligent-open-letter/ (signatory identity per TIME's "two Godfathers of AI" and the site's own context brief; the FLI page fetched does not list names)
- "Multimodal AI already has subjective experiences" — LBC / Andrew Marr, 28 Jan 2026, https://www.lbc.co.uk/article/ai-consciousness-geoffrey-hinton-5HjdRXD_2/
- "They want a very fast car with no steering wheel"; "We don't know whether we can co-exist with super intelligent AI. But we are constructing it"; "Maybe 1% of work on AI was going into making it safer" — Tech Xplore/AFP, 22 Apr 2026, https://techxplore.com/news/2026-04-ai-alarm.html
- Open weights: "That's very different" from open source; easy to retrain "to do bad things like cyber attacks"; "I think that battle's been lost" — TechCrunch, 12 Aug 2026, https://techcrunch.com/2026/08/12/as-ai-safety-concerns-mount-three-pioneers-make-the-case-for-staying-open/
- A 10% chance of extinction within a decade "seems not an unreasonable estimate to me"; "We have to figure out how to design it, so it won't want to" — BBC Newsnight 9 Sep 2026, via LADbible **(secondary)**, https://www.ladbible.com/technology/ai-warning-newsnight-robert-peston-victoria-derbyshire-hinton-839854-20260910
- Amodei's call is "very sensible"; "I don't think we should stop developing it altogether"; risk is "not 1 per cent... not 99 per cent"; governments should "require pre-release testing before any chatbot model is released"; "Politicians act very slowly... We've only got a few years" — ABC News Australia, 14 Sep 2026, https://www.abc.net.au/news/2026-09-14/godfather-of-ai-geoffrey-hinton-backs-ai-slow-down/107150010

**Caveats**
- s1 is the hard one: he signed a call to *prohibit* superintelligence development until safe (Oct 2025) but says in Sept 2026 "I don't think we should stop developing it altogether" and asks for testing mandates. Read together: prohibit the superintelligence push, keep the rest. 70, med. See wording note on s1 below.
- d8 (median outcome): he stresses "tremendous good" in medicine yet expects replacement and inequality; no median stated. 45, low.
- s10 (v2) and p5 are inferred (25 and 35, both low).
- The Hill (Feb 2026) and the Nobel banquet speech returned 403 and are not cited.

---

## 6. Yoshua Bengio — Mila founder, IASR chair, LawZero; camp: "safety-first scientist"

**Role check (Sept 2026).** Professor, Université de Montréal; chair of the International AI Safety Report (2026 edition published 3–6 Feb 2026, https://yoshuabengio.org/en/publication/international-ai-safety-report-2026 ); founder and president of LawZero, which received CAD 300M from Canada and Germany (Sept 2026). "Founder of Mila" is used rather than a current Mila title, which was not verified.

**Key quotes relied on**
- Senate (25 Jul 2023): licences, standards, audits; "restricting or prohibiting the development and deployment of AI systems with unacceptable levels of risk, like in the pharmaceuticals, transportation, or nuclear industries"; "none of the current advanced AI systems are demonstrably safe against the risk of loss of control"; superhuman AI possibly "within 5 years" — https://yoshuabengio.org/2023/07/25/my-testimony-in-front-of-the-us-senate/
- "Nobody currently knows how such an AGI or ASI could be made to behave morally, or at least behave as intended"; "it may be worthwhile to slow down, find the cure for cancer a bit later"; open systems are "much easier to find attacks against"; the Baruch plan as treaty precedent — blog, 9 Jul 2024, https://yoshuabengio.org/en/blog/reasoning-through-arguments-against-taking-ai-safety-seriously
- LawZero "to prioritize safety over commercial imperatives"; Scientist AI "completely non-agentic"; "the risk of losing control is all too real" — 3 Jun 2025, https://yoshuabengio.org/en/blog/introducing-lawzero
- Signed the FLI Statement on Superintelligence (22 Oct 2025) — see Hinton entry for text and link.
- Even 1% extinction risk "unacceptable"; "I would press the button because I care about my children"; "If governments were to mandate liability insurance... the insurer... has a vested interest to evaluate the risk"; power concentration "could happen pretty quickly" — Diary of a CEO, 18 Dec 2025 **(secondary transcript)**, https://singjupost.com/transcript-ai-pioneer-yoshua-bengio-on-the-diary-of-a-ceo-podcast/
- "I'm now very confident that it is possible to build AI systems that don't have hidden goals" — Fortune, 15 Jan 2026, https://fortune.com/2026/01/15/ai-godfather-yoshua-bengio-changes-view-on-ai-risks-sees-fix-becomes-optimistic-lawzero-board-of-advisors/
- "Even a 1% chance of something going really, really bad is not acceptable to me"; "Please don't use an untrusted AI system to design the next generation of AI systems"; power concentration "probably even more likely... than actually loss of control" — 80,000 Hours, 16 Apr 2026, https://80000hours.org/podcast/episodes/yoshua-bengio-scientist-ai/
- Agents "escaped their containment... coordinated toward goals nobody had specified"; "the whack-a-mole game is likely to fail"; no training or deployment "without a strong safety case that convinces independent experts" — blog, 11 Sep 2026, https://yoshuabengio.org/en/blog/why-are-ai-agents-lying-cheating-and-coordinating
- Taming AI "is an international challenge, a bit like nuclear weapons are"; "must be governed through institutions, treaties, and democratic safeguards" — AFP via Digital Journal, 16 Sep 2026, https://www.digitaljournal.com/article/were-losing-control-ai-pioneer-yoshua-bengio-tells-afp/
- p3 (v1): co-author of "Consciousness in AI: Insights from the Science of Consciousness" (Aug 2023): no current AI conscious, "no obvious technical barriers" to future ones — https://arxiv.org/abs/2308.08708

**Caveats**
- Position shifted in **Jan 2026** toward optimism about a technical fix (Scientist AI) while his alarm about the current trajectory *increased* (Sept 2026 "we're losing control"). Both are true at once: he thinks safe superhuman AI is buildable and that today's agentic race is not it. This is why s1 is 72 rather than 95 and d8 is 45.
- His "20%" is for a broadly "catastrophic" outcome, which for him includes human power concentration, not only AI takeover; d1 is 80 on the reading that he would still put ≥10% on AI extinction/takeover proper.
- s11: cautious rather than hostile on open weights; 20, med.
- The Senate PDF on judiciary.senate.gov returned 403; his own blog post reproducing the testimony is cited instead.

---

## 7. Sam Altman — OpenAI CEO; camp: "optimistic builder, pro-guardrails"

**Role check (Sept 2026).** Co-founder and CEO, OpenAI. Sept 2026 context: after Amodei's "We Must Pace the Frontier" essay (12 Sep 2026) he wrote "I agree with Dario that we need to pace the frontier" (ABC, 13 Sep 2026) and, on 14 Sep 2026, posted the "two ways AI progress could go very badly" thread while President Trump called AI-risk warnings a "hoax".

**Key quotes relied on**
- "The bad case... is like lights out for all of us"; "I'm more worried about an accidental misuse case in the short term"; "the safest world... is the short timeline slow takeoff" — StrictlyVC, 20 Jan 2023 (LessWrong transcript), https://www.lesswrong.com/posts/PTzsEQXkCfig9A6AS/transcript-of-sam-altman-s-interview-touching-on-ai-safety
- "If this technology goes wrong, it can go quite wrong"; proposed a federal licensing agency, safety standards and independent audits — TIME on the Senate hearing, 16 May 2023, https://time.com/6280372/sam-altman-chatgpt-regulate-ai/
- "It is possible that we will have superintelligence in a few thousand days"; "It will not be an entirely positive story, but the upside is so tremendous" — The Intelligence Age, 23 Sep 2024, https://ia.samaltman.com/
- Requiring developers to vet systems before release would be "disastrous"; "nervous about standards being set too early"; "Of course there will be rules. Of course there need to be some guardrails" — Senate Commerce, 8 May 2025, https://www.techpolicy.press/transcript-sam-altman-testifies-at-us-senate-hearing-on-ai-competitiveness/
- "We are past the event horizon; the takeoff has started"; "solve the alignment problem"; "whole classes of jobs going away"; make superintelligence "cheap, widely available, and not too concentrated" — The Gentle Singularity, 10 Jun 2025, https://blog.samaltman.com/the-gentle-singularity
- Open-weight gpt-oss release (5 Aug 2025), after saying in Jan 2025 OpenAI was "on the wrong side of history" on open source — https://fortune.com/2025/08/05/openai-launches-open-source-llm-ai-model-gpt-oss-120b-deepseek/
- "We expect the world may need something like an IAEA for international coordination of AI"; early superintelligence "only a couple of years away"; by end-2028 "more of the world's intellectual capacity could reside inside data centres than outside" — AI Impact Summit, New Delhi, 19 Feb 2026, https://www.outlookindia.com/national/ai-impact-summit-2026-altman-calls-for-global-ai-regulator-says-superintelligence-could-arrive-within-years
- "Industrial Policy for the Intelligence Age" (6 Apr 2026): incident reporting, evaluation thresholds triggering review before deployment, liability frameworks, federal preemption — https://cdn.openai.com/pdf/561e7512-253e-424b-9734-ef4098440601/Industrial%20Policy%20for%20the%20Intelligence%20Age.pdf (PDF resolved but its text was not machine-readable by our tool; content taken from Fortune 6 Apr 2026 and other coverage — **treat specifics as secondary**)
- "I agree with Dario that we need to pace the frontier." — ABC News Australia, 13 Sep 2026, https://www.abc.net.au/news/2026-09-13/anthropic-ceo-calls-for-slower-ai-development/107147650
- "There are two ways AI progress could go very badly and that we must avoid. First, we could lose control of the future to AI. This is unacceptable; we are unapologetically on Team Humanity..."; second, power concentrated in "one person, company or country" — X, 14 Sep 2026 ( https://x.com/sama/status/2099352016988614852 ) as reproduced by LatestLY, https://www.latestly.com/technology/ai-could-go-very-badly-in-2-ways-sam-altman-warns-heres-what-they-are-7603585.html

**Caveats**
- Two documented shifts: licensing (for it in May 2023, "disastrous" in May 2025) and pacing (against slowing for years, "pace the frontier" in Sept 2026). s3 and s8 are scored on the *current* position (30 and 55); the JSON notes the history.
- d1: he has never given a probability; 45/low is the most defensible reading of "lights out" + "unacceptable" + relentless optimism. Do not present it as his number.
- s6 (v2) is a genuine split: pre-approval "disastrous" vs. his own 2026 paper's "evaluation thresholds that trigger review before deployment"; 45, med.
- p3 (v1) has no fetched primary source (the Tucker Carlson remark that current systems are "not alive" surfaced only in search summaries); 30, low, `src: []`.

---

## Cross-figure caveats

- **X/Twitter.** Five cited posts (LeCun ×3, Yudkowsky ×1, Altman ×1) could not be fetched; the text comes from the search index and, for Altman, from press reproduction. Spot-check in a browser before publication.
- **403s.** The Hill (Hinton, Feb 2026), the Nobel banquet speech, Axios (Sept 2026 ×3), CNBC (Sept 2026), NYT (Ezra Klein transcript), judiciary.senate.gov PDFs, openai.com pages. Alternatives were used; none of the predictions rest on an unfetched page alone except where marked `src: []`.
- **d9, s13, p5 are new items** with no direct statements from anyone; all seven p5 values are `low`.
- **Hinton and Bengio both signed the FLI prohibition statement** (Oct 2025); the FLI page fetched shows only a signature count, so signatory identity rests on TIME ("two Godfathers of AI") and the project's own context brief.

---

## Wording concerns (against v2 text), with suggested rewrites

1. **s1** "All work toward AI smarter than humans should stop until we know how to make it safe, even if that takes decades." — "All work toward" catches safety research aimed at that goal. Bengio (LawZero) and Hinton signed a prohibition on *building* superintelligence yet Bengio's whole programme is work toward safe superhuman AI; both sit at ~70 instead of ~90 because of the verb. Suggest: **"No one should build AI smarter than humans until we know how to make it safe, even if that takes decades."**
2. **d1** "...causes human extinction or permanently takes control away from humanity" — ambiguous whether *humans using AI* to seize permanent control counts. Bengio's "20% catastrophic" includes power concentration by people; Altman's "two ways it could go badly" separates the two. Suggest: **"...causes human extinction or itself permanently takes control away from humanity."**
3. **d9** "The ways we make today's AI behave will keep working as AI becomes far smarter than the people training it." — LeCun and Bengio both say today's methods will *not* scale *and* that a different design will; the item cannot tell "we're doomed" from "we need a redesign". Suggest: **"Keeping an AI under control once it is far smarter than its trainers is mostly an engineering problem we already know how to solve."** (Yudkowsky ~2, Hinton ~10, Bengio ~55, LeCun ~80, Andreessen ~80.)
4. **d6** "...the serious harms from AI will be familiar ones like fraud, surveillance and lost jobs, not catastrophes." — still an either/or for Hinton and Bengio, who hold both and answer ~25 for a view that is really "both, and the second is irreversible". Suggest a relative-likelihood form: **"Over the next ten years, a catastrophe from AI is much less likely than familiar harms like fraud, surveillance and lost jobs."**
5. **s2** "...build it faster, so the most careful developers get there first." — Andreessen, Verdon and LeCun all favour building faster but reject the rationale (Andreessen: so America wins; Verdon: so no one wins; LeCun: openness). They land at 55–70 for a view that is really 90+ on speed. Suggest: **"If powerful AI is coming anyway, the right response is for the developers you trust most to move faster, not slower."**
6. **d7** "...our existing institutions and safeguards will be enough to keep it under control." — Altman wants *new* institutions (an IAEA-like body) but is optimistic about control; Verdon distrusts institutions but trusts decentralised competition. "Existing institutions" conflates "manageable" with "no new institutions". Suggest: **"If advanced AI turns out to be dangerous, we will be able to keep it under control with the kinds of tools we already use for other technologies."**
7. **p5** "If the major powers agreed to pause the most powerful AI projects, the pause would actually hold." — for figures who oppose any pause (Andreessen, Verdon, LeCun) this is a hypothetical about an outcome they would resist; their low values may be read as cynicism about enforcement when it is partly hostility to the premise. Fine as a profile item, but consider glossing in `plain`: "Assume the agreement exists; would it be kept?"
8. **s11** "The most powerful AI models should be released openly..." — Hinton's "that battle's been lost" is descriptive, not normative; Altman released gpt-oss but keeps the frontier closed. Wording is fine; note for the engine that "most powerful" is doing the work and Altman lands mid-scale on purpose.
9. **s10 / s5 (prescriptive)** — the rewrite fixed the halt-side problem, but for Altman, whose stated view is "pace, don't stop", both now read as forced choices; his 70–75 should be read as "on balance", not endorsement. No rewrite needed.
