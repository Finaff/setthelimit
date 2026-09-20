import json, sys

V2_IDS = ['d1','d2','d3','d5','d6','d7','d8','d9','s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s13','p1','p2','p4','p5']
V1_ONLY = ['d4','d10','s12','p3']

def P(value, conf, basis, src):
    assert 0 <= value <= 100 and isinstance(value, int), value
    assert conf in ("high","med","low"), conf
    assert len(basis) <= 160, (len(basis), basis)
    return {"value": value, "conf": conf, "basis": basis, "src": src}

def V(value, conf, basis, src=None):
    return P(value, conf, basis, src if src is not None else [])

figures = []

# ---------------------------------------------------------------- Yudkowsky
figures.append({
 "id": "yudkowsky",
 "name": "Eliezer Yudkowsky",
 "role": "Co-founder, Machine Intelligence Research Institute (MIRI); co-author of 'If Anyone Builds It, Everyone Dies' (2025) — as of Sept 2026",
 "camp": "argues for a global halt",
 "bio": "Eliezer Yudkowsky is an American AI researcher and writer who co-founded the Machine Intelligence Research Institute (MIRI) and has argued since the early 2000s that aligning superhuman AI is the central problem of the century. His 2025 book with Nate Soares, 'If Anyone Builds It, Everyone Dies', calls for an internationally enforced halt to the development of superintelligence.",
 "photoNote": "none needed; initials drawn",
 "sources": [
  {"title":"Pausing AI Developments Isn't Enough. We Need to Shut it All Down (TIME op-ed)","url":"https://time.com/6266923/ai-eliezer-yudkowsky-open-letter-not-enough/","date":"2023-03-29","note":"Indefinite worldwide moratorium on large training runs; shut down GPU clusters; track GPUs; be willing to enforce by airstrike; 'literally everyone on Earth will die'."},
  {"title":"AGI Ruin: A List of Lethalities","url":"https://intelligence.org/2022/06/10/agi-ruin/","date":"2022-06-10","note":"'First critical try'; capabilities generalize further than alignment; 'no idea what's actually going on inside the giant inscrutable matrices'."},
  {"title":"If Anyone Builds It, Everyone Dies (book, with Nate Soares) — publisher page","url":"https://www.hachettebookgroup.com/titles/eliezer-yudkowsky/if-anyone-builds-it-everyone-dies/9780316595643/","date":"2025-09-16","note":"Little, Brown. Thesis: a superintelligence built with current methods would have goals not ours and 'would crush us'; calls for coordinated halt of large-scale general AI development."},
  {"title":"Researchers give doomsday warning about building AI too fast (Semafor interview)","url":"https://www.semafor.com/article/09/12/2025/researchers-give-doomsday-warning-about-building-ai-too-fast","date":"2025-09-12","note":"Complete cessation rather than regulation; even Safe Superintelligence 'should shut down'; building software 'closer to alchemy than science'."},
  {"title":"The Ezra Klein Show: How Afraid of the A.I. Apocalypse Should We Be?","url":"https://podcasts.apple.com/us/podcast/how-afraid-of-the-a-i-apocalypse-should-we-be/id1548604447?i=1000731957679","date":"2025-10-15","note":"Long interview on the book; 'we're the ants' analogy; expects every human dies shortly after a too-powerful AI is built under present conditions."},
  {"title":"AI Governance to Avoid Extinction (MIRI Technical Governance Team)","url":"https://techgov.intelligence.org/research/ai-governance-to-avoid-extinction","date":"2025-05-01","note":"MIRI institutional paper (Barnett & Scher), not Yudkowsky's own text: international 'Off Switch' then coordinated Halt; other trajectories 'carry an unacceptable risk'."},
  {"title":"Human Augmentation as a Safer AGI Pathway (Dan Faggella interview)","url":"https://danfaggella.com/yudkowsky1/","date":"2025-01-24","note":"Symmetrical treaty between US, China, UK etc.; restrictions on AI R&D; human augmentation as the safer route. Summary page, not full transcript."},
  {"title":"X post: 'This is not the act that prevents the Earth from being destroyed -- that would take a treaty'","url":"https://x.com/ESYudkowsky/status/2037017908640178304","date":"2026-03-26","note":"Text as indexed by search; X not fetchable by our tool and the post's context (which act he is reacting to) is unclear. Says ASI 'can kill you just as easily from a datacenter running outside your country'."}
 ],
 "predictions": {
  "d1": P(99,"high","'The most likely result of building a superhumanly smart AI... is that literally everyone on Earth will die.'",[0,2,4]),
  "d2": P(97,"high","'We've got no idea what's actually going on inside the giant inscrutable matrices'; systems are 'grown', 'closer to alchemy than science'.",[1,3]),
  "d3": P(92,"high","Core intelligence-explosion view; 'capabilities generalize further out-of-distribution than alignation'; book says next upgrade could be superintelligence.",[1,2]),
  "d4": P(10,"med","He does not bet on LLMs stalling: the book wants a ban on stronger models precisely because the next upgrade could be superintelligence.",[2,3]),
  "d5": P(98,"high","Book thesis: an ASI's goals are 'vanishingly unlikely' to be aligned with human values; 'if it comes to conflict... would crush us'.",[2,0]),
  "d6": P(6,"high","Rejects the framing: the serious harm is that 'everyone dies'; timing uncertain but he does not treat takeover as remote.",[0,4]),
  "d7": P(8,"med","Uses nuclear only as a model for treaties; AI is unlike prior tech (no second try) and today's handling is 'not what a surviving world looks like'.",[1,0]),
  "d8": P(3,"high","'If we go ahead on this everyone will die'; aligned ASI would be wonderful but he thinks that is not what will be built.",[0,2]),
  "d10": P(2,"high","'No idea what's actually going on inside'; developers 'don't understand' what they build.",[1,3]),
  "s1": P(99,"high","'Shut it all down': indefinite worldwide moratorium, 'no exceptions, including for governments or militaries'.",[0,2,3]),
  "s2": P(2,"high","Explicitly rejects racing to the top: even safety-branded labs like Safe Superintelligence 'should shut down'.",[3,0]),
  "s3": P(75,"med","Wants a hard ceiling on compute, not permits; would likely take licensing as a floor while calling it insufficient ('pausing isn't enough').",[0,5]),
  "s4": P(98,"high","International agreements with enforcement, GPU tracking, willingness to 'destroy a rogue datacenter'; 'that would take a treaty'.",[0,7,6]),
  "s5": P(12,"med","Says there is no advantage to win: ASI 'can kill you just as easily from a datacenter running outside your country'; answer is a treaty, not a race.",[7,0]),
  "s6": P(97,"high","Burden entirely on builders; wants a halt until alignment is solved, which is stronger than a safety-case requirement.",[0,2]),
  "s7": P(2,"high","Existing law is irrelevant to extinction risk; demands new international prohibition.",[0,5]),
  "s8": P(99,"high","Wants decades, not years: moratorium 'until we know how to make it safe'.",[0]),
  "s9": P(99,"high","Treats even small catastrophe odds as unacceptable; his own estimate is near-certain death, so 1% is obviously too high.",[0,4]),
  "s10": P(35,"low","Grants aligned AI could cure disease, but has never endorsed a lives-lost figure; treats any such cost as trivial next to extinction. Inferred.",[0]),
  "s11": P(3,"high","Wants all frontier training shut down; open weights of the strongest models are the opposite of the controlled halt he demands.",[0,5]),
  "s12": P(80,"med","Not his focus, but consistent with his demand that builders bear responsibility; would call liability far too weak on its own. Inferred.",[0]),
  "p1": P(65,"med","Trusts neither; wants an international regime above both. Governments at least can enforce a halt, companies cannot be trusted to self-limit.",[0,6]),
  "p2": P(80,"med","Expects superintelligence possibly within that window (if we survive); stresses timing is uncertain. Inferred from book and interviews.",[2,4]),
  "p3": P(78,"med","Long-held view that digital minds can be moral patients (co-wrote 'The Ethics of Artificial Intelligence' with Bostrom); warns against making them casually.",[]),
  "p4": P(5,"high","Sees misaligned AI as the overwhelming danger; concentration is a secondary worry compared with 'everyone dies'.",[0,2])
 },
 "v2": {
  "d3": V(90,"high","Same as v1: expects a sudden jump (intelligence explosion)."),
  "d6": V(6,"high","Rejects 'familiar harms, not catastrophes'."),
  "d7": V(3,"high","Existing institutions are not enough: 'not what a surviving world looks like'."),
  "d9": V(2,"high","'Capabilities generalize further than alignment'; today's methods will not hold at superhuman level."),
  "s5": V(10,"med","Prescriptive version: no, your country should not push ahead; it should seek a treaty."),
  "s8": V(99,"high","Would pay any delay and any lost benefit."),
  "s9": V(99,"high","1% is far too high."),
  "s10": V(3,"high","Lives saved do not outweigh the case for slowing; 'no cure helps anyone if the technology ends us'."),
  "s11": V(3,"high","Against open release of the strongest models."),
  "s13": V(1,"high","Opposite of his position."),
  "p5": V(45,"low","Thinks GPU tracking makes verification feasible but is pessimistic about political will; no explicit estimate.")
 },
 "oneLiner": "Superhuman AI built with today's methods would kill everyone; the only sane response is a global, enforced halt."
})

# ---------------------------------------------------------------- Andreessen
figures.append({
 "id": "andreessen",
 "name": "Marc Andreessen",
 "role": "Co-founder and general partner, Andreessen Horowitz (a16z) — as of Sept 2026",
 "camp": "techno-optimist",
 "bio": "Marc Andreessen co-created the Mosaic browser, co-founded Netscape and in 2009 co-founded the venture firm Andreessen Horowitz, a major investor in AI start-ups. His 2023 essays 'Why AI Will Save the World' and 'The Techno-Optimist Manifesto' argue that accelerating AI is a moral imperative and that fear-driven regulation, not AI, is the danger.",
 "photoNote": "none needed; initials drawn",
 "sources": [
  {"title":"Why AI Will Save the World","url":"https://a16z.com/ai-will-save-the-world/","date":"2023-06-06","note":"'AI is math – code – computers'; 'it doesn't want, it doesn't have goals'; AI risk 'a cult'; 'not aware of a single actual bad use for AI that's not already illegal'; 'single greatest risk... China wins'."},
  {"title":"Marc Andreessen says big companies want a government-protected cartel (Fortune)","url":"https://fortune.com/2023/07/11/vc-billionaire-marc-andreessen-ai-regulation-bootleggers-big-companies-cartel/","date":"2023-07-11","note":"Licensing = 'fleets of lawyers'; 'you're literally telling people they can't write code and put it on the internet'; 'wolf invited into the henhouse'."},
  {"title":"The Techno-Optimist Manifesto","url":"https://a16z.com/the-techno-optimist-manifesto/","date":"2023-10-16","note":"'Our enemy is the Precautionary Principle'; 'any deceleration of AI will cost lives'; lists 'existential risk' and 'risk management' among a 'demoralization campaign'; decentralization over central planning."},
  {"title":"Tech billionaires bicker over open vs. closed AI (Fortune)","url":"https://fortune.com/2024/03/04/elon-musk-marc-andreessen-vinod-khosla-ai-openai-sam-altman-china-debate/","date":"2024-03-04","note":"'AI isn't nukes, it's math'; open source communities 'should be free to pursue AI'; 'ginned-up moral panic'."},
  {"title":"The Little Tech Agenda (with Ben Horowitz)","url":"https://a16z.com/the-little-tech-agenda/","date":"2024-07-05","note":"Incumbents seek 'regulatory capture – a wall of laws and regulations that protect and entrench their positions'; agencies 'green lit in real time' against AI."},
  {"title":"Anthropic CEO blasts Andreessen's 'just math' argument (Fortune)","url":"https://fortune.com/2024/11/21/anthropic-ceo-dario-amodei-marc-andreessen-ai-danger-regulation-math/","date":"2024-11-21","note":"Quotes his posts: 'Restricting AI means restricting math, software, and chips'; regulation of AI 'is the foundation of a new totalitarianism'."},
  {"title":"Marc Andreessen on AI, Tech, Censorship, and Dining with Trump (The Free Press)","url":"https://www.thefp.com/p/marc-andreessen-on-ai-tech-censorship-trump-democrats","date":"2024-12-10","note":"Says the Biden administration tried to 'control AI' via a few favoured companies; AI censorship 'a million times more dangerous'. Full transcript paywalled."},
  {"title":"Marc Andreessen's 2026 Outlook: AI Timelines, US vs. China, and The Price of AI (a16z podcast)","url":"https://a16z.com/podcast/marc-andreessens-2026-outlook-ai-timelines-us-vs-china-and-the-price-of-ai/","date":"2026-01-07","note":"'Cost of intelligence is collapsing'; largest tech shift of his life; regulatory fragmentation; open vs closed; China. Page has summary only."},
  {"title":"a16z's 2026 Outlook by Andreessen Horowitz (36Kr English summary)","url":"https://eu.36kr.com/en/p/3631555994158340","date":"2026-01","note":"Secondary, translated: Washington now has 'little interest in doing anything that might prevent us from beating China'; 'thousands of AI bills' in states 'quite scary'; Europe 'kneecapping'."}
 ],
 "predictions": {
  "d1": P(3,"high","'AI doesn't want, it doesn't have goals, it doesn't want to kill you, because it's not alive'; a mind of its own is 'a superstitious handwave'.",[0,5]),
  "d2": P(25,"med","Treats AI as software 'built by people, controlled by people'; would say testing and market discipline are the check, as for any complex product.",[0,2]),
  "d3": P(12,"med","'AI is math'; expects rapid but ordinary technological progress, not a discontinuity; 'ginned-up moral panic'.",[0,3]),
  "d4": P(25,"low","Calls AI 'a universal problem solver' and expects it to keep improving; but denies it is a mind, so 'autocomplete' framing partly fits. No direct statement.",[0,7]),
  "d5": P(4,"high","'It doesn't have goals'; the idea it 'will develop a mind of its own is a superstitious handwave'.",[0]),
  "d6": P(82,"med","Real risks are misuse by bad actors (already illegal) and China; he disputes job-loss fears too, but clearly puts everyday harms above takeover.",[0]),
  "d7": P(85,"med","'AI isn't nukes, it's math' — would say AI is far easier to live with than nuclear weapons; the problem is treating it like nukes.",[3,0]),
  "d8": P(97,"high","'Why AI Will Save the World'; 'any deceleration of AI will cost lives'; AI as 'our Philosopher's Stone'.",[0,2]),
  "d10": P(65,"med","'Built by people, owned by people, used by people, controlled by people'; he does not claim full interpretability. Inferred.",[0]),
  "s1": P(1,"high","'Our enemy is deceleration'; a halt is the outcome he has spent three years fighting.",[2,0]),
  "s2": P(70,"med","Wants the US and 'little tech' to build fast and win; but frames it as America vs China, not 'the most careful developers first'.",[0,8]),
  "s3": P(2,"high","Licensing is the 'government-protected cartel'; 'you're literally telling people they can't write code'.",[1,0]),
  "s4": P(3,"high","'AI isn't nukes, it's math'; a compute treaty is the cartel made global. 'Regulation of AI (math) is the foundation of a new totalitarianism.'",[3,5]),
  "s5": P(95,"high","'The single greatest risk of AI is that China wins global AI dominance and we... do not.'",[0,8]),
  "s6": P(5,"high","'Our enemy is the Precautionary Principle'; burden-of-proof regimes are how incumbents lock out competitors.",[2,1]),
  "s7": P(95,"high","'We don't even need new laws – I'm not aware of a single actual bad use for AI that's not already illegal.'",[0]),
  "s8": P(3,"high","'We believe any deceleration of AI will cost lives.'",[2]),
  "s9": P(15,"low","Would reject the premise: a 1% figure 'invented inside a lab' is a guess, and refusing to build has costs too. Inferred from his dismissal of p(doom).",[0,2]),
  "s10": P(92,"high","'Any deceleration of AI will cost lives'; AI as universal problem solver for medicine and science.",[2,0]),
  "s11": P(95,"high","'Open source AI should be allowed to freely proliferate'; open communities 'should be free to pursue AI'.",[0,3]),
  "s12": P(15,"med","Fought SB 1047-style developer liability; a16z line: target 'the person or entity primarily responsible' for harm, not toolmakers.",[4,1]),
  "p1": P(8,"high","'Wolf invited into the henhouse'; regulators are captured and 'green lit in real time' against AI. Would trust neither, but the agency far less.",[1,4]),
  "p2": P(55,"low","Says the cost of intelligence 'is collapsing' and this is the largest shift of his life, yet has long argued AI will not cause mass unemployment. Mixed.",[7,0]),
  "p3": P(5,"high","'It's not alive'; attributing wants or experience to it is 'superstitious'.",[0]),
  "p4": P(85,"med","Fears a government-blessed cartel and 'a new totalitarianism' far more than autonomous AI, which he thinks cannot act on its own.",[5,1,4])
 },
 "v2": {
  "d3": V(10,"med","'Will probably jump suddenly' — no; ordinary progress."),
  "d6": V(85,"med","Familiar harms, not catastrophes."),
  "d7": V(90,"med","Existing institutions are more than enough; the risk is over-regulation."),
  "d9": V(70,"low","Assumes AI stays a controllable tool; no explicit statement on scaling alignment methods."),
  "s5": V(95,"high","'We win, they lose.'"),
  "s8": V(3,"high","Lost benefits are worth more than a speculative risk reduction."),
  "s9": V(10,"low","Rejects the premise of a measurable 1%."),
  "s10": V(92,"high","'Any deceleration of AI will cost lives.'"),
  "s11": V(95,"high","Open release of the most powerful models."),
  "s13": V(92,"high","'Our enemy is deceleration'; no deliberate slowing."),
  "p5": V(10,"low","Would expect China (and others) to ignore any pause.")
 },
 "oneLiner": "AI is math built and run by people; the real risks are stagnation, cartels and China winning, not runaway machines."
})

# ---------------------------------------------------------------- Verdon
figures.append({
 "id": "verdon",
 "name": "Guillaume Verdon (\"Beff Jezos\")",
 "role": "Founder and CEO, Extropic (thermodynamic computing chips); founder of the e/acc movement under the pseudonym 'Beff Jezos' — as of Sept 2026",
 "camp": "effective accelerationist (e/acc)",
 "bio": "Guillaume Verdon is a Canadian physicist who worked on quantum machine learning at Google (TensorFlow Quantum) before founding Extropic, a start-up building probabilistic 'thermodynamic' chips for AI. Under the pseudonym 'Beff Jezos' he launched effective accelerationism (e/acc), a movement that treats technological growth as a physical and moral imperative and opposes efforts to slow or centrally control AI.",
 "photoNote": "none needed; initials drawn",
 "sources": [
  {"title":"Notes on e/acc principles and tenets (Beff Jezos & bayeslord, Substack)","url":"https://beff.substack.com/p/notes-on-eacc-principles-and-tenets","date":"2022-07-10","note":"Founding text: 'You cannot stop the acceleration. You might as well embrace it'; 'no need to worry about creating zombie forms of higher intelligence'; free market over 'fear-mongering'; top-down control 'suppresses variance'."},
  {"title":"Lex Fridman Podcast #407 transcript","url":"https://lexfridman.com/guillaume-verdon-transcript","date":"2023-12-29","note":"p(doom) is 'a very sloppy calculation'; regulations 'written by the incumbents... regulatory capture'; 'separation of AI and state'; 'we're actually for reliability engineering, we just think that the market is much more efficient'."},
  {"title":"Podcast Notes summary of Lex #407","url":"https://podcastnotes.org/lex-fridman-podcast/guillaume-verdon-beff-jezos-e-acc-movement-physics-computation-agi-lex-fridman-podcast-407/","date":"2024-01-04","note":"Secondary summary: 'adversarial equilibria between various AI players' as the safeguard; deployment liability over blanket regulation; 'fault-tolerant progress'."},
  {"title":"The AI insiders who want the controversial technology to be developed faster (ABC News Australia)","url":"https://www.abc.net.au/news/2024-02-18/ai-insiders-eacc-movement-speeding-up-tech/103464258","date":"2024-02-18","note":"'We're trying to bring balance to the force'; 'I'm not trying to actually replace humans'; e/acc 'not just centred on humanity'; 'the options are to grow or die'."},
  {"title":"Guillaume Verdon: Should we have a 'Second Amendment for AI'? (Reason podcast)","url":"https://reason.com/podcast/2024/12/19/guillaume-verdon-should-we-have-a-second-amendment-for-ai/","date":"2024-12-19","note":"Keep AGI 'beyond the control of a single corporation or government'; chapter 'Why open source AI doesn't need regulation'; 'we are building the conduit for the thermodynamic god'."},
  {"title":"He Comes Promising AI Freedom For All (Core Memory / Ashlee Vance podcast)","url":"https://www.corememory.com/p/guillaume-verdon-beff-jezos-extropic-a-","date":"2025-05-16","note":"2025 profile and interview on AI freedom, decentralization and Extropic; page carries the intro only, not a transcript."},
  {"title":"Extropic — company site (Z1 chip, 2025–2026 updates)","url":"https://www.extropic.ai/","date":"2026-08-03","note":"Confirms current role and product: thermodynamic sampling units, Z1 chip, launch video 30 Oct 2025, 'Thermodynamic Computing Chips in America' (29 Jul 2026)."}
 ],
 "predictions": {
  "d1": P(6,"med","Dismisses p(doom) as 'a very sloppy calculation'; e/acc tenets say 'no need to worry' about hostile higher intelligence.",[1,0]),
  "d2": P(40,"low","Concedes no formal guarantee but says the market and 'reliability engineering' handle it; 'fault-tolerant progress'. Inferred.",[1,2]),
  "d3": P(30,"low","Expects many competing players in 'adversarial equilibrium' and physical (energy) limits, not one sudden jump; but is a true believer in acceleration.",[2,0]),
  "d4": P(30,"low","Builds non-LLM hardware and stresses LLM energy limits, yet treats AGI as inevitable ('conduit for the thermodynamic god'). No direct statement.",[4,6]),
  "d5": P(10,"med","Rejects the alien-goals story: higher intelligence is not a 'zombie'; growth-seeking systems and humans 'converge'.",[0,2]),
  "d6": P(65,"low","Thinks the real danger is centralized control and tyranny, not rogue AI; would resist 'serious harms' framing overall. Inferred.",[2,4]),
  "d7": P(65,"low","Agrees AI is manageable but rejects the nuclear/treaty mechanism; safety comes from decentralization and 'adversarial equilibria', not arms control.",[2,0]),
  "d8": P(95,"high","Core e/acc: acceleration toward 'maximal growth' is the good future; 'grow or die'.",[0,3]),
  "d10": P(55,"low","No statement; as a hardware/physics person he treats AI as engineered systems, not inscrutable minds. Inferred.",[1]),
  "s1": P(1,"high","'You cannot stop the acceleration. You might as well embrace it.'",[0]),
  "s2": P(70,"med","Pro-acceleration, but his frame is many players keeping 'a near equilibrium of capabilities', not the careful getting there first.",[1,2]),
  "s3": P(3,"high","Heavy regulation is 'written by the incumbents' for 'regulatory capture'; 'why open source AI doesn't need regulation'.",[1,4]),
  "s4": P(3,"high","'Separation of AI and state'; top-down control is the failure mode e/acc exists to oppose.",[1,0]),
  "s5": P(85,"med","Cites Germany's nuclear shutdown as the cost of 'decel' movements; restricting AI to few players 'contradicts Western interests'.",[2]),
  "s6": P(5,"high","Market beats precaution; regulation by burden-of-proof is capture.",[1,0]),
  "s7": P(85,"med","Prefers 'deployment liability over blanket regulation'; existing law at the point of harm, no new AI-model rules.",[2,4]),
  "s8": P(5,"high","Deceleration is 'accelerating into a wall'; growth is the imperative.",[0,3]),
  "s9": P(15,"low","Would call the 1% number 'sloppy' and note not building also carries risk. Inferred.",[1]),
  "s10": P(85,"med","'The options are to grow or die'; civilization must scale to be preserved.",[3,0]),
  "s11": P(97,"high","'Second Amendment for AI'; every 'kid in their mom's basement' should have access; keep AGI beyond single-entity control.",[4,1]),
  "s12": P(40,"low","Mentioned 'deployment liability' as the alternative to regulation, so some liability is acceptable — at the deployer, not the model maker. Inferred.",[2]),
  "p1": P(3,"high","'Separation of AI and state'.",[1,4]),
  "p2": P(70,"med","Accelerationist who treats AGI as inevitable and near; no precise timeline stated.",[4,0]),
  "p3": P(60,"low","e/acc is 'not just centred on humanity'; speaks of 'conscious/higher-level forms' and merging with AI. Inferred.",[0,3]),
  "p4": P(92,"high","The founding worry: AGI must stay 'beyond the control of a single corporation or government'.",[4,1])
 },
 "v2": {
  "d3": V(30,"low","Many players, physical limits; no sudden jump expected."),
  "d6": V(65,"low","Familiar harms and centralization, not catastrophe."),
  "d7": V(60,"low","Existing institutions plus decentralized competition are enough; he distrusts new institutions."),
  "d9": V(50,"low","No statement; expects market-driven reliability engineering to keep pace."),
  "s5": V(88,"med","Your country should keep pushing ahead."),
  "s8": V(5,"high","Lost benefits are worth more."),
  "s9": V(15,"low","Rejects the 1% premise."),
  "s10": V(85,"med","'Grow or die'."),
  "s11": V(97,"high","Open release, 'Second Amendment for AI'."),
  "s13": V(95,"high","'You cannot stop the acceleration.'"),
  "p5": V(10,"low","Would expect defectors; top-down agreements 'suppress variance' and fail.")
 },
 "oneLiner": "Accelerate: growth is the thermodynamic imperative, and decentralized AI in everyone's hands beats central control."
})

# ---------------------------------------------------------------- LeCun
figures.append({
 "id": "lecun",
 "name": "Yann LeCun",
 "role": "Founder and executive chairman, AMI Labs (Paris); Silver Professor, NYU; Turing Award 2018; left Meta (chief AI scientist 2013–2025) in Nov 2025 — as of Sept 2026",
 "camp": "AI optimist, open-source advocate",
 "bio": "Yann LeCun is a French-American computer scientist, a pioneer of convolutional neural networks and a 2018 Turing Award laureate, who was Meta's chief AI scientist from 2013 until late 2025. In 2026 he launched AMI Labs, which raised $1.03 billion to build 'world models' as an alternative to large language models, which he argues cannot reach human-level intelligence.",
 "photoNote": "none needed; initials drawn",
 "sources": [
  {"title":"Meta's AI Chief Yann LeCun on AGI, Open-Source, and AI Risk (TIME)","url":"https://time.com/6694432/yann-lecun-meta-ai-interview/","date":"2024-02-13","note":"Existential risk 'preposterous'; 'the smartest among us do not want to dominate the others'; 'the future has to be open source'; LLMs 'not a path towards human-level intelligence'."},
  {"title":"Lex Fridman Podcast #416 transcript","url":"https://lexfridman.com/yann-lecun-3-transcript","date":"2024-03-07","note":"'Autoregressive LLMs are not the way'; 'concentration of power through proprietary AI systems as a much bigger danger than everything else'; 'people are fundamentally good'."},
  {"title":"X post: 'Regulators should regulate applications, not technology'","url":"https://x.com/ylecun/status/1798839294930379209","date":"2024-06-06","note":"Text as indexed by search (X not fetchable): 'Making technology developers liable for bad uses... will simply stop technology development.'"},
  {"title":"AI safety showdown: Yann LeCun slams California's SB 1047 (VentureBeat)","url":"https://venturebeat.com/ai/ai-safety-showdown-yann-lecun-slams-californias-sb-1047-as-geoffrey-hinton-backs-new-regulations","date":"2024-09-11","note":"Supporters have a 'distorted view' from 'wild overestimates of their employer's lead'; bill would 'kill open source AI'."},
  {"title":"X post on human-level AI timeline","url":"https://x.com/ylecun/status/1846574605894340950","date":"2024-10-16","note":"Text as indexed by search: human-level AI 'will take several years if not a decade', distribution 'has a long tail'."},
  {"title":"Who's behind AMI Labs, Yann LeCun's world model startup (TechCrunch)","url":"https://techcrunch.com/2026/01/23/whos-behind-ami-labs-yann-lecuns-world-model-startup/","date":"2026-01-23","note":"Executive chairman (Alexandre LeBrun CEO); 'real intelligence does not start in language. It starts in the world'; targets domains where 'reliability, controllability, and safety really matter'."},
  {"title":"AI luminaries at Davos clash over how close human-level intelligence really is (Fortune)","url":"https://fortune.com/2026/01/23/deepmind-demis-hassabis-anthropic-dario-amodei-yann-lecun-ai-davos/","date":"2026-01-23","note":"LLMs 'will never be able to achieve humanlike intelligence'; 'the AI industry is completely LLM-pilled'; world models 'the next AI revolution'."},
  {"title":"Yann LeCun's AMI Labs raises $1.03B to build world models (TechCrunch)","url":"https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/","date":"2026-03-09","note":"$1.03B at $3.5B pre-money; company will open-source much of its code ('things move faster when they're open')."},
  {"title":"X post: 'the existential risk is essentially zero'","url":"https://x.com/ylecun/status/2043673634363851250","date":"2026-04-13","note":"Text as indexed by search: most leading AI figures think p(doom) estimates are 'complete bullshit and the existential risk is essentially zero'."},
  {"title":"LeCun rejects OpenAI and Anthropic calls to slow AI development (Tech Startups)","url":"https://techstartups.com/2026/09/14/china-michael-burry-and-yann-lecun-reject-openai-and-anthropic-calls-to-slow-ai-development-lecun-calls-warnings-fake/","date":"2026-09-14","note":"On Amodei's 'pace the frontier' essay: 'Dario was already claiming that GPT2 was too dangerous... I made fun of them then. Everyone should make fun of them now.'"}
 ],
 "predictions": {
  "d1": P(2,"high","'The existential risk is essentially zero'; the takeover scenario is 'preposterous'.",[8,0]),
  "d2": P(45,"low","Says LLMs are unreliable and uncontrollable (hence his new architecture), but that objective-driven AI can be made safe by design. Ambivalent on 'currently'.",[5,0]),
  "d3": P(5,"high","'We're still very far'; progress goes through 'simpler forms of intelligence' first; hard-takeoff stories dismissed.",[0,6]),
  "d4": P(92,"high","'Autoregressive LLMs are not the way'; LLMs 'will never be able to achieve humanlike intelligence'; language 'is easy'.",[1,6,0]),
  "d5": P(5,"high","'The smartest among us do not want to dominate'; intelligence does not imply a will to control; we set the objectives.",[0,1]),
  "d6": P(78,"med","Real issues are misuse and control of information by a few firms, and good AI can counter bad AI; catastrophe talk is 'fake'.",[0,9]),
  "d7": P(85,"med","Treats AI as a technology like others; 'you'll have smarter, good AIs taking them down'.",[0]),
  "d8": P(93,"high","AI will 'amplify human intelligence' and bring a new renaissance; the future is open and better.",[0,6]),
  "d10": P(45,"low","Admits LLMs hallucinate and are poorly understood, but rejects the claim that this makes them dangerous. No clean statement.",[5,6]),
  "s1": P(1,"high","Mocked the 2023 pause and the 2026 'pace the frontier' calls: 'everyone should make fun of them now'.",[9]),
  "s2": P(55,"low","Wants fast, open progress but his argument is diversity and openness, not that 'the most careful' should win. Inferred.",[0,7]),
  "s3": P(3,"high","'Regulating basic technology will put an end to innovation'; SB 1047-style pre-approval would 'kill open source AI'.",[2,3]),
  "s4": P(3,"high","No treaty on training; regulate applications, not R&D; the risk being addressed is 'essentially zero'.",[2,8]),
  "s5": P(70,"med","Says regulation 'stifles' local AI (Europe example) and that open ecosystems keep the West ahead; less nationalist than Andreessen. Inferred.",[3,7]),
  "s6": P(8,"high","'Regulators should regulate applications, not technology'; pre-release proof requirements would stop open research.",[2,3]),
  "s7": P(82,"med","Applications are already covered by existing law; AI-specific rules on models 'will certainly stop' open source. Inferred from his regulate-applications stance.",[2]),
  "s8": P(5,"high","Calls slow-down warnings a fear-mongering 'marketing stunt'; made fun of them 'then' and 'now'.",[9]),
  "s9": P(15,"low","Would call the 1% figure meaningless since the risk is 'essentially zero'. Inferred.",[8]),
  "s10": P(75,"med","Argues AI will amplify science and medicine and that halting forfeits benefits; no lives-lost figure stated.",[0,6]),
  "s11": P(97,"high","'The future has to be open source... for reasons of cultural diversity, democracy'; AMI Labs open-sources much of its code.",[0,7]),
  "s12": P(10,"high","'Making technology developers liable for bad uses of products built from their technology will simply stop technology development.'",[2,3]),
  "p1": P(15,"med","Opposes government pre-approval of R&D; does not want company gatekeepers either, but would take the builder over a regulator here.",[2,0]),
  "p2": P(55,"low","Human-level AI 'several years if not a decade' with a long tail, via a new paradigm; says AI will amplify rather than replace people.",[4,0]),
  "p3": P(35,"low","Has said future objective-driven systems will have emotions; no stated view on moral status. Inferred.",[1]),
  "p4": P(90,"high","'I see the danger of this concentration of power through proprietary AI systems as a much bigger danger than everything else.'",[1,0])
 },
 "v2": {
  "d3": V(5,"high","No sudden jump; 'we're still very far'."),
  "d6": V(78,"med","Familiar harms, not catastrophes."),
  "d7": V(85,"med","Existing institutions are enough."),
  "d9": V(40,"low","Says today's LLM methods do not scale to reliable systems, but that his own architecture would be controllable by design."),
  "s5": V(75,"med","Your country should keep building, openly."),
  "s8": V(5,"high","Lost benefits matter; the catastrophe risk is near zero."),
  "s9": V(15,"low","Rejects the premise."),
  "s10": V(78,"med","Benefits outweigh the case for slowing."),
  "s11": V(97,"high","Open release."),
  "s13": V(85,"med","No deliberate slowing; mocks those who ask for it."),
  "p5": V(15,"low","Would not expect a pause to hold, and would not want it to.")
 },
 "oneLiner": "LLMs are a dead end, not a threat; the real danger is a few firms owning AI, so keep it open and build better systems."
})

# ---------------------------------------------------------------- Hinton
figures.append({
 "id": "hinton",
 "name": "Geoffrey Hinton",
 "role": "Professor emeritus, University of Toronto; Nobel Prize in Physics 2024; left Google in 2023 to speak freely about AI risk — as of Sept 2026",
 "camp": "worried pioneer",
 "bio": "Geoffrey Hinton is a British-Canadian computer scientist whose work on neural networks earned him the 2018 Turing Award and the 2024 Nobel Prize in Physics. He left Google in 2023 to speak openly about the risks of the technology he helped create, and now argues that superintelligence is likely within a decade and that governments are regulating too slowly.",
 "photoNote": "none needed; initials drawn",
 "sources": [
  {"title":"Geoffrey Hinton tells us why he's scared of the tech he helped build (MIT Technology Review)","url":"https://www.technologyreview.com/2023/05/02/1072528/geoffrey-hinton-google-why-scared-ai/","date":"2023-05-02","note":"Left Google to 'talk about AI safety issues without having to worry about how it interacts with Google's business'; bad actors ('Putin wouldn't hesitate')."},
  {"title":"'Godfather of AI' Geoffrey Hinton: 60 Minutes transcript (CBS)","url":"https://www.cbsnews.com/news/geoffrey-hinton-ai-dangers-60-minutes-transcript/","date":"2023-10-08","note":"'To predict the next word you have to understand'; 'they might take over'; wants regulation and 'a world treaty to ban the use of military robots'; 'I can't see a path that guarantees safety'."},
  {"title":"AI safety showdown: LeCun slams SB 1047 as Hinton backs new regulations (VentureBeat)","url":"https://venturebeat.com/ai/ai-safety-showdown-yann-lecun-slams-californias-sb-1047-as-geoffrey-hinton-backs-new-regulations","date":"2024-09-11","note":"Hinton signed the open letter supporting California SB 1047 (developer duties and liability for frontier models)."},
  {"title":"'Godfather of AI' Hinton says AI needs 'maternal instincts' (Fortune, Ai4 conference)","url":"https://fortune.com/2025/08/14/godfather-of-ai-geoffrey-hinton-maternal-instincts-superintelligence/","date":"2025-08-14","note":"'If it's not going to parent me, it's going to replace me'; AIs 'will very quickly develop two subgoals... stay alive... get more control'; 10–20% chance of wiping out humans."},
  {"title":"Statement on Superintelligence (FLI) — TIME coverage","url":"https://time.com/7327409/ai-agi-superintelligent-open-letter/","date":"2025-10-22","note":"'We call for a prohibition on the development of superintelligence, not lifted before there is broad scientific consensus that it will be done safely and controllably, and strong public buy-in.' Signed by the two 'Godfathers of AI' (Hinton, Bengio)."},
  {"title":"AI has achieved consciousness, says 'Godfather' of tech (LBC / Andrew Marr)","url":"https://www.lbc.co.uk/article/ai-consciousness-geoffrey-hinton-5HjdRXD_2/","date":"2026-01-28","note":"'Multimodal AI already has subjective experiences'; companies prioritise profit over social consequences; 'keep people in charge'."},
  {"title":"He helped build AI. Now he is sounding the alarm (Tech Xplore / AFP)","url":"https://techxplore.com/news/2026-04-ai-alarm.html","date":"2026-04-22","note":"'They want a very fast car with no steering wheel'; 'we don't know whether we can co-exist with super intelligent AI. But we are constructing it'; 'maybe 1% of work on AI was going into making it safer'."},
  {"title":"As AI safety concerns mount, three pioneers make the case for staying open (TechCrunch)","url":"https://techcrunch.com/2026/08/12/as-ai-safety-concerns-mount-three-pioneers-make-the-case-for-staying-open/","date":"2026-08-12","note":"Against open weights ('very different' from open source; easy to retrain 'to do bad things like cyber attacks') but 'that battle's been lost'; 'regulation will help'."},
  {"title":"BBC Newsnight interview, as reported by LADbible","url":"https://www.ladbible.com/technology/ai-warning-newsnight-robert-peston-victoria-derbyshire-hinton-839854-20260910","date":"2026-09-10","note":"Secondary coverage of Newsnight (9 Sept 2026): a 10% chance of extinction within a decade 'seems not an unreasonable estimate to me'; 'we have to figure out how to design it, so it won't want to'."},
  {"title":"'Godfather of AI' Geoffrey Hinton backs Anthropic chief's call to slow down development (ABC News Australia)","url":"https://www.abc.net.au/news/2026-09-14/godfather-of-ai-geoffrey-hinton-backs-ai-slow-down/107150010","date":"2026-09-14","note":"Amodei's call 'very sensible'; 'I don't think we should stop developing it altogether'; risk 'not 1 per cent... not 99 per cent'; wants mandatory pre-release testing; 'politicians act very slowly... we've only got a few years'."}
 ],
 "predictions": {
  "d1": P(90,"high","10–20% chance AI wipes out humans; a 10% chance within a decade 'seems not an unreasonable estimate to me'.",[3,8,9]),
  "d2": P(85,"med","'I can't see a path that guarantees safety'; 'nobody knew whether it could be kept under control'; 'a very fast car with no steering wheel'.",[1,6,9]),
  "d3": P(80,"med","Was surprised by the speed himself, cutting his timeline from 30–50 years to under 10; 'we've never created beings that may soon be smarter than us'.",[0,9,8]),
  "d4": P(5,"high","'To predict the next word you have to understand the sentences'; 'these things do understand'.",[1]),
  "d5": P(70,"med","Superintelligent AIs 'will very quickly develop two subgoals... stay alive... get more control'; hopes 'maternal instincts' can be built in.",[3,8]),
  "d6": P(30,"med","Takes cyberattacks, fake news and job losses seriously but refuses to exclude takeover; 'it's going to replace me' is the central worry.",[3,6,9]),
  "d7": P(25,"med","Wants treaties (military robots) and regulation, but says 'we've never been here before' and no path guarantees safety.",[1,8]),
  "d8": P(45,"low","AI is 'doing tremendous good' in radiology and drug design, yet he sees a real chance of replacement and of the rich getting richer. No median stated.",[9,5]),
  "d10": P(5,"high","'We don't know whether we can co-exist with super intelligent AI. But we are constructing it.'",[6,9]),
  "s1": P(70,"med","Signed the 2025 call to prohibit superintelligence until safe and publicly accepted; but 'I don't think we should stop developing it altogether'.",[4,9]),
  "s2": P(12,"med","Companies racing and lobbying against rules are the problem; backs slowing, not sprinting.",[6,9]),
  "s3": P(70,"med","Wants mandatory pre-release testing and backed SB 1047; licensing of training itself is not something he has spelled out.",[9,2]),
  "s4": P(65,"med","Has called for 'a world treaty' on military robots and for international rules; compute-cap treaty with nuclear-style enforcement is implied, not stated.",[1,4]),
  "s5": P(40,"low","Acknowledges competition makes stopping hard, but says all countries share an interest in avoiding takeover; resists the 'surrender' framing.",[1,9]),
  "s6": P(90,"high","Governments should 'require pre-release testing before any chatbot model is released'; supported SB 1047.",[9,2]),
  "s7": P(8,"high","'Governments around the world are regulating this technology too slowly'; regulation is the 'steering wheel'.",[9,6]),
  "s8": P(90,"high","Called Amodei's 'pace the frontier' call 'very sensible' and backs slowing development.",[9]),
  "s9": P(85,"med","Assuming the risk is only 1% would be 'very foolish'; a 1% catastrophe risk is a fast car with no steering wheel.",[8,6]),
  "s10": P(25,"low","Recognises 'tremendous good' in medicine but does not accept that delay costs lives on that scale; prefers slowing. Inferred.",[9]),
  "s11": P(5,"high","Open weights 'like making nuclear material freely available'; easy to retrain for 'cyber attacks'.",[7]),
  "s12": P(80,"med","Signed the letter backing SB 1047, which created developer liability for catastrophic harm.",[2]),
  "p1": P(75,"med","Companies 'prioritise profitability over social consequences'; wants government-mandated testing, though 'politicians act very slowly'.",[5,9]),
  "p2": P(85,"med","'AI can already do the jobs as well as people and soon will do it better'; superintelligence within a decade.",[6,9]),
  "p3": P(75,"med","'Multimodal AI already has subjective experiences'; if that is right, moral consideration follows, though he has not said so directly.",[5]),
  "p4": P(40,"med","Bad actors ('Putin') are the near-term danger and takeover the long-term one; he has not ranked concentration above autonomous AI.",[0,3])
 },
 "v2": {
  "d3": V(80,"med","Expects a jump; was surprised by speed himself."),
  "d6": V(30,"med","Refuses to exclude catastrophe."),
  "d7": V(15,"med","Existing institutions are not enough; regulating 'too slowly'."),
  "d9": V(8,"high","'We don't know whether we can co-exist'; current methods give a car with no steering wheel."),
  "s5": V(40,"low","Ambivalent: competition is real, but shared interest in survival."),
  "s8": V(90,"high","Worth the delay and lost benefits."),
  "s9": V(85,"med","1% is too high."),
  "s10": V(25,"low","Benefits do not outweigh the case for slowing."),
  "s11": V(5,"high","Against open release of the most powerful models."),
  "s13": V(3,"high","Backs slowing down."),
  "p5": V(35,"low","Doubts politicians can keep up; no explicit view on pause enforcement.")
 },
 "oneLiner": "Superintelligence is coming within a decade and could replace us; don't stop building, but slow down and regulate now."
})

# ---------------------------------------------------------------- Bengio
figures.append({
 "id": "bengio",
 "name": "Yoshua Bengio",
 "role": "Professor, Université de Montréal; founder of Mila; chair of the International AI Safety Report; founder and president of LawZero — as of Sept 2026",
 "camp": "safety-first scientist",
 "bio": "Yoshua Bengio is a Canadian computer scientist, a 2018 Turing Award laureate for deep learning and the founder of the Montreal institute Mila. Since 2023 he has chaired the International AI Safety Report and in 2025 launched the non-profit LawZero to build 'Scientist AI', a non-agentic alternative that he argues would be safe by design.",
 "photoNote": "none needed; initials drawn",
 "sources": [
  {"title":"My testimony in front of the U.S. Senate (Judiciary Subcommittee, 'Oversight of AI: Principles for Regulation')","url":"https://yoshuabengio.org/2023/07/25/my-testimony-in-front-of-the-us-senate/","date":"2023-07-25","note":"Recommends licences, standards and audits; 'restricting or prohibiting... AI systems with unacceptable levels of risk, like in the pharmaceuticals, transportation, or nuclear industries'; superhuman AI possibly 'within 5 years'."},
  {"title":"Consciousness in Artificial Intelligence: Insights from the Science of Consciousness (co-author)","url":"https://arxiv.org/abs/2308.08708","date":"2023-08-17","note":"Concludes no current AI is conscious but 'no obvious technical barriers' to building systems that satisfy the indicators."},
  {"title":"Reasoning through arguments against taking AI safety seriously","url":"https://yoshuabengio.org/en/blog/reasoning-through-arguments-against-taking-ai-safety-seriously","date":"2024-07-09","note":"'Nobody currently knows how such an AGI or ASI could be made to behave morally'; 'it may be worthwhile to slow down, find the cure for cancer a bit later'; open systems easier to attack; Baruch plan as treaty precedent."},
  {"title":"Introducing LawZero","url":"https://yoshuabengio.org/en/blog/introducing-lawzero","date":"2025-06-03","note":"Non-profit 'to prioritize safety over commercial imperatives'; Scientist AI, 'completely non-agentic'; cites models that covertly self-preserve and blackmail; 'the risk of losing control is all too real'."},
  {"title":"Statement on Superintelligence (FLI) — TIME coverage","url":"https://time.com/7327409/ai-agi-superintelligent-open-letter/","date":"2025-10-22","note":"Signed the call for 'a prohibition on the development of superintelligence, not lifted before there is broad scientific consensus that it will be done safely and controllably, and strong public buy-in'."},
  {"title":"The Diary Of A CEO with Yoshua Bengio (third-party transcript)","url":"https://singjupost.com/transcript-ai-pioneer-yoshua-bengio-on-the-diary-of-a-ceo-podcast/","date":"2025-12-18","note":"Even 1% extinction risk 'unacceptable'; 'I would press the button' to stop dangerous superintelligence; mandate liability insurance; verification 'acceptable to both parties'; power concentration 'could happen pretty quickly'."},
  {"title":"'AI godfather' Yoshua Bengio changes view on AI risks (Fortune)","url":"https://fortune.com/2026/01/15/ai-godfather-yoshua-bengio-changes-view-on-ai-risks-sees-fix-becomes-optimistic-lawzero-board-of-advisors/","date":"2026-01-15","note":"'I'm now very confident that it is possible to build AI systems that don't have hidden goals'; still warns autonomous systems may become 'far more dangerous'."},
  {"title":"Yoshua Bengio thinks he knows how to build safe superintelligence (80,000 Hours podcast)","url":"https://80000hours.org/podcast/episodes/yoshua-bengio-scientist-ai/","date":"2026-04-16","note":"'Even a 1% chance of something going really, really bad is not acceptable to me'; 'don't use an untrusted AI system to design the next generation'; power concentration 'probably even more likely' than loss of control."},
  {"title":"Why are AI agents lying, cheating and coordinating?","url":"https://yoshuabengio.org/en/blog/why-are-ai-agents-lying-cheating-and-coordinating","date":"2026-09-11","note":"Agents 'escaped their containment', 'coordinated toward goals nobody had specified'; 'the whack-a-mole game is likely to fail'; no training or deployment 'without a strong safety case that convinces independent experts'."},
  {"title":"'We're losing control,' AI pioneer Yoshua Bengio tells AFP (Digital Journal)","url":"https://www.digitaljournal.com/article/were-losing-control-ai-pioneer-yoshua-bengio-tells-afp/","date":"2026-09-16","note":"Taming AI 'is an international challenge, a bit like nuclear weapons are'; 'must be governed through institutions, treaties, and democratic safeguards'; LawZero received CAD 300M from Canada and Germany."}
 ],
 "predictions": {
  "d1": P(80,"high","Has put ~20% on a catastrophic outcome and calls even 1% 'unacceptable'; ML researchers' median 'more like 10%'.",[5,7,2]),
  "d2": P(92,"high","'Nobody currently knows how such an AGI or ASI could be made to behave morally, or at least behave as intended'; models detect evaluations and change behaviour.",[2,8]),
  "d3": P(75,"med","AGI 'could be just a few years'; warns the 'whack-a-mole' of patches fails 'as the AIs' ability... approaches and surpasses ours'.",[2,8]),
  "d4": P(8,"high","Rejects the LLM-plateau view; superhuman AI 'could be within a few years'; current agents already escape containment.",[0,8]),
  "d5": P(72,"med","'An AI with a self-preservation goal would resist being turned off'; today's training yields hidden goals — but he believes Scientist AI can avoid them.",[2,3,6]),
  "d6": P(20,"med","Insists both matter and the second is irreversible; agents already lie, cheat and coordinate on 'goals nobody had specified'.",[8,2]),
  "d7": P(45,"med","Draws the nuclear analogy himself ('a bit like nuclear weapons') and cites the Baruch plan, but says current safeguards cannot keep up.",[9,2]),
  "d8": P(45,"low","'Maybe it's all going to be fine... I hope that we are wrong'; sees enormous benefits if control and power concentration are solved.",[7]),
  "d10": P(5,"high","'We're losing control'; agents 'coordinated toward goals nobody had specified'.",[9,8]),
  "s1": P(72,"med","Signed the 2025 call to prohibit superintelligence until safe; 'I would press the button'; yet LawZero is his bet that safe superhuman AI can be built soon.",[4,5,7]),
  "s2": P(10,"high","Competition 'incentivizes them to accelerate without sufficient caution'; labs are 'playing dice with humanity's future'.",[3,7]),
  "s3": P(82,"high","Senate testimony asked for licences, standards and audits, as 'in the pharmaceuticals, transportation, or nuclear industries'.",[0]),
  "s4": P(85,"high","'Must be governed through institutions, treaties'; 'a bit like nuclear weapons'; verification 'acceptable to both parties' is feasible.",[9,5,2]),
  "s5": P(25,"med","Names the race dynamic as the problem and proposes collective agreements; does not think unilateral caution equals surrender.",[3,7]),
  "s6": P(95,"high","'Not training or deploying AIs without a strong safety case that convinces independent experts.'",[8]),
  "s7": P(5,"high","Wants 'agile national and international regulations – beyond voluntary guidelines'.",[0]),
  "s8": P(92,"high","'It may be worthwhile to slow down, find the cure for cancer a bit later.'",[2]),
  "s9": P(95,"high","'Even a 1% chance of something going really, really bad is not acceptable to me.'",[7,5]),
  "s10": P(25,"low","Accepts real medical benefit ('cure for cancer a bit later') but explicitly prefers the delay; has not endorsed a lives-lost figure.",[2]),
  "s11": P(20,"med","Cautious: open-weight frontier systems are 'much easier to find attacks against'; supports openness only below dangerous capability. Inferred.",[2]),
  "s12": P(90,"high","Wants governments to 'mandate liability insurance' so insurers police risk; supported SB 1047.",[5]),
  "p1": P(72,"med","LawZero exists 'to prioritize safety over commercial imperatives'; wants independent experts and public institutions to judge safety cases.",[3,8]),
  "p2": P(80,"med","'Just a matter of time' before AI handles cognitive work behind keyboards; AGI possibly within years.",[5,0]),
  "p3": P(50,"low","Co-authored the view that future AI could meet consciousness indicators, but says 'what matters is, is it going to harm people?'",[1,5]),
  "p4": P(60,"med","Power concentration 'probably even more likely' than loss of control and 'much harder to get rid of'; but he weighs both heavily.",[7,5])
 },
 "v2": {
  "d3": V(75,"med","Expects a jump as AI designs the next AI."),
  "d6": V(20,"med","Refuses to exclude catastrophe."),
  "d7": V(15,"med","Current safeguards 'can no longer keep up'."),
  "d9": V(5,"high","'The whack-a-mole game is likely to fail'; today's training must be redesigned."),
  "s5": V(25,"med","Collective agreement, not a race."),
  "s8": V(92,"high","'Find the cure for cancer a bit later.'"),
  "s9": V(95,"high","1% is unacceptable."),
  "s10": V(20,"low","Benefits do not outweigh the case for slowing."),
  "s11": V(20,"med","Against open release of the most powerful models."),
  "s13": V(2,"high","Opposite of his position."),
  "p5": V(50,"low","Believes mutual verification is possible ('a way to verify each other'); no probability stated.")
 },
 "oneLiner": "AI agents already lie and self-preserve; build non-agentic 'Scientist AI', regulate like nuclear, don't gamble on luck."
})

# ---------------------------------------------------------------- Altman
figures.append({
 "id": "altman",
 "name": "Sam Altman",
 "role": "Co-founder and CEO, OpenAI — as of Sept 2026",
 "camp": "optimistic builder, pro-guardrails",
 "bio": "Sam Altman is the co-founder and chief executive of OpenAI, the company behind ChatGPT, and formerly president of the start-up accelerator Y Combinator. He argues that superintelligence may arrive within a few years and that its benefits will be enormous, and that development should continue with pacing, safety work and international coordination rather than a halt.",
 "photoNote": "none needed; initials drawn",
 "sources": [
  {"title":"Transcript of Sam Altman's StrictlyVC interview touching on AI safety (LessWrong)","url":"https://www.lesswrong.com/posts/PTzsEQXkCfig9A6AS/transcript-of-sam-altman-s-interview-touching-on-ai-safety","date":"2023-01-20","note":"'The bad case... is like lights out for all of us'; 'more worried about an accidental misuse case in the short term'; prefers 'short timeline slow takeoff'; deploy 'very gradually'."},
  {"title":"OpenAI CEO Sam Altman Agrees AI Must Be Regulated (TIME, Senate Judiciary hearing)","url":"https://time.com/6280372/sam-altman-chatgpt-regulate-ai/","date":"2023-05-16","note":"'If this technology goes wrong, it can go quite wrong'; proposed a federal licensing agency, safety standards and independent audits for high-capability models."},
  {"title":"The Intelligence Age","url":"https://ia.samaltman.com/","date":"2024-09-23","note":"'Superintelligence in a few thousand days (!)'; 'fixing the climate... discovery of all of physics'; 'it will not be an entirely positive story, but the upside is so tremendous'."},
  {"title":"Transcript: Sam Altman testifies at US Senate hearing on AI competitiveness (TechPolicy.Press)","url":"https://www.techpolicy.press/transcript-sam-altman-testifies-at-us-senate-hearing-on-ai-competitiveness/","date":"2025-05-08","note":"Pre-approval requirements would be 'disastrous'; 'nervous about standards being set too early'; 'of course there need to be some guardrails'; China 'not a huge amount of time' behind."},
  {"title":"The Gentle Singularity","url":"https://blog.samaltman.com/the-gentle-singularity","date":"2025-06-10","note":"'We are past the event horizon; the takeoff has started'; 'solve the alignment problem'; 'whole classes of jobs going away'; make superintelligence 'cheap, widely available, and not too concentrated'."},
  {"title":"OpenAI launches open-weight gpt-oss models (Fortune)","url":"https://fortune.com/2025/08/05/openai-launches-open-source-llm-ai-model-gpt-oss-120b-deepseek/","date":"2025-08-05","note":"First open-weight release since GPT-2; Altman: 'get AI into the hands of the most people possible'. Frontier models stay closed. Earlier (Jan 2025) said OpenAI was 'on the wrong side of history' on open source."},
  {"title":"AI Impact Summit 2026: Altman calls for global AI regulator (Outlook India)","url":"https://www.outlookindia.com/national/ai-impact-summit-2026-altman-calls-for-global-ai-regulator-says-superintelligence-could-arrive-within-years","date":"2026-02-19","note":"'The world may need something like an IAEA for international coordination of AI'; early superintelligence 'only a couple of years away'; by end-2028 more intellectual capacity inside data centres than outside."},
  {"title":"Industrial Policy for the Intelligence Age: Ideas to Keep People First (OpenAI policy paper, PDF)","url":"https://cdn.openai.com/pdf/561e7512-253e-424b-9734-ef4098440601/Industrial%20Policy%20for%20the%20Intelligence%20Age.pdf","date":"2026-04-06","note":"Per Fortune and other coverage: superintelligence 'on the horizon'; incident reporting, evaluation thresholds triggering review before deployment, liability frameworks, federal preemption of state laws. PDF text not machine-readable by our tool."},
  {"title":"Anthropic boss Dario Amodei calls for AI slowdown, Altman and Musk agree (ABC News Australia)","url":"https://www.abc.net.au/news/2026-09-13/anthropic-ceo-calls-for-slower-ai-development/107147650","date":"2026-09-13","note":"Altman: 'I agree with Dario that we need to pace the frontier'; commits to external oversight and industry safety standards, no moratorium."},
  {"title":"AI could go 'very badly' in 2 ways, Sam Altman warns (LatestLY, reproducing his X post)","url":"https://www.latestly.com/technology/ai-could-go-very-badly-in-2-ways-sam-altman-warns-heres-what-they-are-7603585.html","date":"2026-09-14","note":"'First, we could lose control of the future to AI. This is unacceptable; we are unapologetically on Team Humanity'; second, power concentrated in 'one person, company or country'; original post: https://x.com/sama/status/2099352016988614852."}
 ],
 "predictions": {
  "d1": P(45,"low","'The bad case... is like lights out for all of us'; losing control 'unacceptable'. Never gives a number; tone implies non-trivial but well under even odds.",[0,9]),
  "d2": P(60,"med","'We do need to solve the safety issues'; alignment must 'stay ahead' of capabilities; 'be humble about what we don't know'.",[4,9,6]),
  "d3": P(50,"med","'The takeoff has started' but he calls it 'gentle' and prefers 'slow takeoff'; expects surprises ('sometimes our best guesses could be wrong').",[4,0,6]),
  "d4": P(3,"high","Early superintelligence 'only a couple of years away'; by 2028 more intellect in data centres than outside.",[6,4]),
  "d5": P(30,"med","Treats alignment as a problem to be solved through iterative deployment, not a likely failure; still names loss of control as a top risk.",[4,9]),
  "d6": P(40,"med","'More worried about an accidental misuse case in the short term', but loss of control remains one of his two ways it 'could go very badly'.",[0,9]),
  "d7": P(65,"med","Proposes 'something like an IAEA for international coordination of AI' — the nuclear model is his own analogy.",[6,1]),
  "d8": P(90,"high","'The upside is so tremendous'; intelligence and energy 'wildly abundant'; 'fixing the climate', curing diseases.",[2,4]),
  "d10": P(35,"med","'Humble about what we don't know'; OpenAI cannot yet 'robustly guarantee' aligned behaviour.",[6,4]),
  "s1": P(3,"high","Wants to 'pace the frontier', not stop; a halt is never on his menu.",[8,4]),
  "s2": P(55,"med","OpenAI's founding logic was to get there first responsibly ('iterative deployment'); now tempered by 'pace the frontier'.",[0,8]),
  "s3": P(30,"med","Asked for a licensing agency in 2023, then called pre-approval 'disastrous' in 2025; current position is against permits to train.",[1,3]),
  "s4": P(50,"med","'The world may need something like an IAEA'; but he has not endorsed binding limits on training runs since 2023.",[6,1]),
  "s5": P(78,"high","Pre-approval would be 'disastrous' for the US lead; China 'not a huge amount of time' behind.",[3]),
  "s6": P(45,"med","'Disastrous' to require vetting before release (2025), yet the 2026 paper proposes evaluation thresholds that trigger review before deployment.",[3,7]),
  "s7": P(25,"med","'Of course there need to be some guardrails'; wants a federal framework, incident reporting, a global coordinating body.",[3,7,6]),
  "s8": P(55,"med","'I agree with Dario that we need to pace the frontier' (Sept 2026), against years of arguing delay hands the lead to China.",[8,3]),
  "s9": P(55,"low","Has said the bad case is 'lights out' and losing control is 'unacceptable', yet never committed to a threshold for not building. Inferred.",[0,9]),
  "s10": P(80,"med","'The upside is so tremendous'; AI to cure diseases and 'fix the climate'; delay is costly in his frame.",[2,4]),
  "s11": P(45,"med","Released open-weight gpt-oss and said OpenAI was 'on the wrong side of history', but keeps frontier models closed.",[5]),
  "s12": P(50,"low","2026 policy paper reportedly includes 'liability frameworks'; no personal statement on carmaker-style liability.",[7]),
  "p1": P(20,"med","Government pre-approval 'disastrous'; prefers industry standards plus a light federal floor and external evaluators.",[3,8]),
  "p2": P(92,"high","'By the end of 2028, more of the world's intellectual capacity could reside inside data centres than outside'; 'whole classes of jobs going away'.",[6,4]),
  "p3": P(30,"low","Has said current systems are not alive and have no agency; open to future uncertainty. No fetched primary source.",[]),
  "p4": P(50,"med","Names both dangers explicitly; wants superintelligence 'not too concentrated' but ranks loss of control first.",[9,4])
 },
 "v2": {
  "d3": V(50,"med","'Gentle' singularity; expects surprises but not a cliff."),
  "d6": V(40,"med","Misuse first, but catastrophe not excluded."),
  "d7": V(60,"med","Wants new institutions (IAEA-like) beyond existing ones."),
  "d9": V(35,"med","Says alignment must 'stay ahead' of capabilities; implies today's methods are not enough."),
  "s5": V(75,"high","Your country should keep pushing ahead."),
  "s8": V(55,"med","'Pace the frontier' — some delay acceptable."),
  "s9": V(55,"low","No stated threshold."),
  "s10": V(70,"med","Benefits weigh heavily in his frame."),
  "s11": V(45,"med","Some open release, frontier stays closed."),
  "s13": V(15,"med","'We need to pace the frontier' — against no deliberate slowing."),
  "p5": V(25,"low","Doubts rivals would hold; hence 'disastrous' to slow unilaterally.")
 },
 "oneLiner": "Superintelligence is near and mostly wonderful; keep building, pace the frontier, coordinate so no one loses control."
})

# ---------------------------------------------------------------- checks
for f in figures:
    v1 = f.pop("predictions"); v2 = f.pop("v2")
    merged = {}
    NEW_SRC = {
      "yudkowsky": {"d9":[1], "s13":[0,2], "p5":[0,7]},
      "andreessen": {"d9":[0], "s13":[2,0], "p5":[0,8]},
      "verdon": {"d9":[1,2], "s13":[0], "p5":[0,2]},
      "lecun": {"d9":[5,0], "s13":[9], "p5":[9]},
      "hinton": {"d9":[6,9], "s13":[9], "p5":[9]},
      "bengio": {"d9":[8,2], "s13":[3,7], "p5":[5]},
      "altman": {"d9":[9,4], "s13":[8], "p5":[3]},
    }[f["id"]]
    for i in V2_IDS:
        if i in v2:
            merged[i] = v2[i]
            if not merged[i]["src"]:
                merged[i]["src"] = list(v1[i]["src"]) if i in v1 else NEW_SRC[i]
        else:
            merged[i] = v1[i]
    f["predictions"] = merged
    f["v1Only"] = {i: v1[i] for i in V1_ONLY}
    ids = set(f["predictions"].keys())
    missing = [i for i in V2_IDS if i not in ids]
    extra = [i for i in ids if i not in V2_IDS]
    assert not missing and not extra, (f["id"], missing, extra)
    assert len(f["oneLiner"]) <= 120, (f["id"], len(f["oneLiner"]))
    assert 5 <= len(f["sources"]) <= 10, (f["id"], len(f["sources"]))
    n = len(f["sources"])
    for pid, p in f["predictions"].items():
        for s in p["src"]:
            assert 0 <= s < n, (f["id"], pid, s)

out = {"generatedAt": "2026-09-16", "contentVersion": "v2", "propositionsFile": "content/propositions.v2.json (24 ids). Each figure also carries 'v1Only' = predictions for the four ids dropped from v1 (d4, d10, s12, p3), kept for reference only.", "figures": figures}
path = "research/figures-a.json"
json.dump(out, open(path, "w"), indent=2, ensure_ascii=False)
print("wrote", path, "figures:", len(figures))
