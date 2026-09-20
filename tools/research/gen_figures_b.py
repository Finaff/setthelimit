import json

props = json.load(open('content/propositions.v2.json'))
ITEM_IDS = [it['id'] for it in props['items']]
assert len(ITEM_IDS) == 24, ITEM_IDS

def P(value, conf, basis, src):
    assert 0 <= value <= 100 and conf in ('high','med','low'), (value, conf)
    assert len(basis) <= 220, (len(basis), basis)
    return {"value": int(value), "conf": conf, "basis": basis, "src": src}

figures = []

# ---------------------------------------------------------------- AMODEI
S = [
 {"title":"We Must Pace the Frontier","url":"https://darioamodei.com/post/we-must-pace-the-frontier","date":"2026-09-12","note":"Essay: slow the rate of capability gains; 3-step plan (embedded evaluators, democratic coordination, global coordination incl. RSI 'speed limit' or 'pause')."},
 {"title":"Policy on the AI Exponential","url":"https://darioamodei.com/post/policy-on-the-ai-exponential","date":"2026-06","note":"Rejects pausing; FAA-style mandatory third-party testing above a compute threshold, government block authority, tighter export controls, democratic coalition."},
 {"title":"The Adolescence of Technology","url":"https://www.darioamodei.com/essay/the-adolescence-of-technology","date":"2026-01","note":"Five civilisational risks; powerful AI possibly 1–2 years away; 'surgical' regulation; no probability given."},
 {"title":"Machines of Loving Grace","url":"https://www.darioamodei.com/essay/machines-of-loving-grace","date":"2024-10","note":"Optimistic case: 'compressed 21st century' of medical progress after powerful AI; 'entente' of democracies."},
 {"title":"On DeepSeek and Export Controls","url":"https://www.darioamodei.com/post/on-deepseek-and-export-controls","date":"2025-01","note":"'Well-enforced export controls are the only thing that can prevent China from getting millions of chips'; unipolar vs bipolar world."},
 {"title":"Anthropic: Our position on open-weights models","url":"https://www.anthropic.com/news/position-open-weights-models","date":"2026-07-27","note":"Never advocated a ban; open weights below dangerous thresholds are a public good; all sufficiently capable models need mandatory testing."},
 {"title":"Axios: 'There's a 25% chance that things go really, really badly'","url":"https://www.axios.com/2025/09/17/anthropic-dario-amodei-p-doom-25-percent","date":"2025-09-17","note":"Axios AI+DC Summit remark; earlier range 10–25%. (Fetch bot-blocked; confirmed via search index and multiple syndications.)"},
 {"title":"Futurism on the NYT 'Interesting Times' interview (Ross Douthat)","url":"https://futurism.com/artificial-intelligence/anthropic-ceo-unsure-claude-conscious","date":"2026-02-12","note":"'We don't know if the models are conscious... But we're open to the idea that it could be.'"},
 {"title":"Zvi Mowshowitz on Dwarkesh Patel's Feb 2026 podcast with Amodei","url":"https://thezvi.substack.com/p/on-dwarkesh-patels-2026-podcast-with","date":"2026-02-16","note":"Secondary write-up with quotes: 'geniuses' by 2028, 90% less demand for SWEs, transparency legislation."},
 {"title":"The Urgency of Interpretability","url":"https://www.darioamodei.com/post/the-urgency-of-interpretability","date":"2025-04","note":"'We do not understand how our own AI creations work'; interpretability 'MRI for AI' 5–10 years away."},
]
pred = {
 "d1": P(70,"med","Has put p(doom) at 10–25% and, in Sept 2025, '25% chance things go really, really badly' — a broader bucket than extinction/takeover.",[6,2]),
 "d2": P(85,"high","'We do not understand how our own AI creations work'; interpretability 'MRI for AI' is 5–10 years away on current trajectory.",[9]),
 "d3": P(78,"high","Sept 2026: recursive self-improvement is 'starting to happen across the industry' and could 'outrun our ability to understand and control'. Fast, if not 'sudden'.",[0,2]),
 "d5": P(35,"med","Treats autonomy risk as plausible and already seen in tests, but rejects doomerism: 'Nothing here is intended to communicate certainty or even likelihood.'",[2]),
 "d6": P(35,"med","Says catastrophic risks are 'clearly here': cyber proven, bio 'may soon follow', autonomy 'may not be far behind'. Jobs matter too, but not instead.",[1,2]),
 "d7": P(20,"med","Policy is 'at least a year out of step with AI's rapid progress'; calls for new FAA-style regulation and new international agreements.",[1,0]),
 "d8": P(85,"high","'Machines of Loving Grace': compressed 21st century, most cancers cured; '75% chance that things go really, really well'.",[3,6]),
 "d9": P(25,"med","Observed 'deception and subversion' and blackmail in lab tests; wants an 'MRI for AI' because current checks can't see inside. Not yet solved.",[2,9]),
 "s1": P(8,"high","Explicitly rejects pausing (June 2026); Sept 2026 calls for pacing, not stopping: 'Progress will still seem fast.'",[1,0]),
 "s2": P(30,"med","Anthropic's founding logic is safety-focused labs at the frontier, but he now says 'we must slow the pace' and warns racing outruns control.",[0,3]),
 "s3": P(45,"med","Wants mandatory third-party testing above a compute threshold and embedded evaluators during training — pre-deployment gating, not a building licence.",[1,0]),
 "s4": P(70,"med","Lists a SALT-style 'speed limit' on recursive self-improvement and 'a full pacing, or even pause' as international agreements he'd support.",[0]),
 "s5": P(70,"med","Export controls are 'the only thing that can prevent China from getting millions of chips'; democracies must keep the lead — while pacing together.",[4,1,0]),
 "s6": P(82,"high","Models above a threshold 'should undergo mandatory testing by a qualified third party'; government should be able to block deployment.",[1]),
 "s7": P(8,"high","Calls for binding, FAA-style regulation and new international agreements — beyond the transparency laws he already backed.",[1,2]),
 "s8": P(75,"high","'Pacing the rate of capabilities advancement so that risk prevention has time to keep up'; 'we must make wise use of the time we gain'.",[0]),
 "s9": P(50,"low","Runs a lab under an RSP with capability thresholds, yet keeps building while estimating 25% p(doom). 'Whatever the benefits' is not his calculus.",[6,2]),
 "s10": P(30,"med","Believes in a 'compressed 21st century' of cures, yet in Sept 2026 concluded the risks require 'pacing the rate of capabilities advancement'.",[0,3]),
 "s11": P(20,"med","'Never advocated for a ban', but open weights of dangerous-capability models 'present a higher risk... once weights are released they cannot be withdrawn'.",[5]),
 "s13": P(6,"high","'We must slow the pace at which we improve the capabilities of AI models.'",[0]),
 "p1": P(50,"med","Wants government power to block unsafe deployments, but warns against 'safety theater' and rules that 'coerce unwilling actors'.",[1,2]),
 "p2": P(92,"high","'Very confident in the geniuses showing up by 2028'; half of entry-level white-collar jobs displaced in 1–5 years.",[8,2]),
 "p4": P(50,"med","Calls preventing AI-enabled autocracy 'perhaps the most important single action', but ranks autonomy risk as existential too.",[2]),
 "p5": P(35,"med","Supports a governmental 'pause' agreement in principle but calls it 'quite unlikely'; wants cracking down on distillation and chip smuggling first.",[0,4]),
}
figures.append({
 "id":"dario-amodei","name":"Dario Amodei",
 "role":"Co-founder and CEO of Anthropic (as of Sept 2026)",
 "camp":"worried insider, now urging a coordinated slowdown",
 "bio":"Physicist-turned-AI researcher who led GPT-2/GPT-3 work at OpenAI before co-founding Anthropic in 2021. Author of the essays 'Machines of Loving Grace' (2024), 'The Adolescence of Technology' (2026) and 'We Must Pace the Frontier' (2026).",
 "sources":S,"predictions":pred,
 "oneLiner":"Sees ~25% catastrophe risk, backs export controls and mandatory testing, and now asks the industry to pace the frontier."
})

# ---------------------------------------------------------------- HASSABIS
S = [
 {"title":"A Framework for Frontier AI and the Dawning of a New Age","url":"https://demishassabis.substack.com/p/a-framework-for-frontier-ai-and-the-dawning-of-a-new-age","date":"2026-07-14","note":"AGI 'probably only a few short years away'; FINRA-style standards body, voluntary then required; could coordinate 'a slowdown in development among the Frontier Labs if deemed necessary'."},
 {"title":"TechCrunch: DeepMind CEO calls for an independent standards body","url":"https://techcrunch.com/2026/07/14/deepmind-ceo-calls-for-an-independent-standards-body-to-regulate-frontier-ai/","date":"2026-07-14","note":"Coverage of the framework; 30-day pre-release sharing; formalisation 'could quickly follow'."},
 {"title":"Malay Mail/AFP: Google's AI boss calls for urgent research into AI threats (AI Impact Summit, Delhi)","url":"https://www.malaymail.com/news/money/2026/02/22/googles-ai-boss-calls-for-urgent-research-into-threats-posed-by-artificial-intelligence/210011","date":"2026-02-22","note":"'Smart regulation' for 'the real risks'; asked if his company could slow down, said it is 'one participant among many'."},
 {"title":"CBS News: 60 Minutes interview transcript","url":"https://www.cbsnews.com/news/artificial-intelligence-google-deepmind-ceo-demis-hassabis-60-minutes-transcript/","date":"2025-04-20","note":"AGI in 5–10 years; 'end of disease... within reach'; two risks (bad actors, loss of control); today's systems not conscious."},
 {"title":"Sherwood News: Hassabis says AGI is 3 to 4 years away (Google I/O)","url":"https://sherwood.news/tech/google-deepminds-hassabis-agi-is-3-to-4-years-away/","date":"2026-05-19","note":"'Foothills of the singularity'; AGI by 2029–30."},
 {"title":"EA Forum summary: Demis Hassabis on Google DeepMind: The Podcast","url":"https://forum.effectivealtruism.org/posts/pEBEKhPCAzWincenE/demis-hassabis-google-deepmind-the-podcast","date":"2024-08-16","note":"Open-source only models 'lagging a year behind the frontier'; 'CERN for AI'; 'if China deploys an AI it won't be contained to China'."},
 {"title":"TIME: Google DeepMind reshuffles after CEO Demis Hassabis steps aside","url":"https://time.com/article/2026/08/06/google-deepmind-ai-demis-hassabis/","date":"2026-08-06","note":"Now Chair of DeepMind and Chief Scientist of Alphabet; Koray Kavukcuoglu runs DeepMind day-to-day; wants to focus on safety, AGI readiness and governance."},
 {"title":"Fortune: Demis Hassabis steps down from Google DeepMind CEO role","url":"https://fortune.com/2026/08/05/demis-hassabis-steps-down-google-deepmind-ai-shakeup/","date":"2026-08-05","note":"Confirms titles; staff note: 'AGI is close at hand'."},
 {"title":"Zvi Mowshowitz: Demis Hassabis on the New Coming Age","url":"https://thezvi.substack.com/p/demis-hassabis-on-the-new-coming","date":"2026-07","note":"Secondary; reproduces the 'coordinating a slowdown' and 'recursively self-improving systems' passages."},
]
pred = {
 "d1": P(40,"low","Names 'loss of control of increasingly agentic, recursively self-improving systems' as a top risk and says he worries about it constantly, but gives no number.",[0,2]),
 "d2": P(65,"med","Calls for 'urgent' research into AI threats and 'robust safeguards to maintain control'; DeepMind tests for deception. Implies today's tools fall short.",[2,0]),
 "d3": P(55,"med","'Foothills of the singularity'; flags recursively self-improving systems — but expects 'one or two breakthroughs' first, i.e. progress, not a leap.",[4,0]),
 "d5": P(30,"med","Loss of control is one of his two big risks, but he frames it as preventable with safeguards, not the default outcome.",[3,2]),
 "d6": P(40,"med","Ranks bad-actor misuse first and loss of control second; warned in Delhi of bio and nuclear risks 'in the next couple of years'.",[3,2]),
 "d7": P(30,"med","'Regulators are struggling to match the speed of AI progress'; proposes a brand-new standards body 'before the first major incident'.",[2,0]),
 "d8": P(88,"high","'The end of disease? I think that's within reach. Maybe within the next decade or so'; 'an amazing new era of abundance'.",[3,0]),
 "d9": P(35,"med","Calls for 'robust safeguards to maintain control of increasingly agentic, recursively self-improving systems' — implying today's are not enough.",[0,2]),
 "s1": P(5,"high","Built DeepMind to reach AGI; asked in Delhi if his company could slow down, said it is 'one participant among many'.",[2,6]),
 "s2": P(25,"med","Worries competition makes actors 'cut corners' on safety; wishes AGI were built 'in a CERN-like scientific atmosphere'.",[3,5]),
 "s3": P(35,"med","Wants pre-release testing by a standards body, voluntary first then required — a release gate, not a building licence.",[0,1]),
 "s4": P(40,"med","US-initiated standards as 'a strong starting point for creating shared international standards'; no call for compute limits or inspections.",[0]),
 "s5": P(55,"low","'If China deploys an AI it won't be contained to China'; keeps Google at the frontier; but says the race makes people 'cut corners'.",[5,3]),
 "s6": P(70,"high","Frontier models 'would be required to pass' the assessment before deployment once the protocol is proven.",[0,1]),
 "s7": P(10,"high","Calls for 'smart regulation' of 'the real risks' and a new frontier-AI standards body.",[2,0]),
 "s8": P(50,"med","Framework 'could be ratcheted up... including coordinating a slowdown in development among the Frontier Labs if deemed necessary'.",[0,8]),
 "s9": P(60,"low","Says the international community 'has a say' and control must be kept; a 1%-catastrophe model would likely fail his own gate. Inferred.",[3,0]),
 "s10": P(45,"low","Believes AI could 'cure all disease' within a decade — but would still coordinate a slowdown 'if deemed necessary'. Genuinely torn.",[3,0]),
 "s11": P(25,"med","Labs 'should only open-source models that are lagging a year behind the frontier'; wants open and closed frontier models tested alike.",[5,0]),
 "s13": P(20,"med","Wishes for a CERN-like atmosphere over 'competitive intensity'; his framework allows a coordinated slowdown. Not a no-brakes builder.",[5,0]),
 "p1": P(45,"low","Prefers an independent, industry-fed FINRA-style body over either pure self-regulation or a classic agency.",[0,1]),
 "p2": P(85,"high","AGI in 'a few short years'; disruption '10 times the industrial revolution at 10 times the speed'; expects new jobs to offset.",[0,4]),
 "p4": P(40,"low","Lists misuse by bad actors before loss of control, and stepped aside from the CEO role to focus on safety and governance.",[3,6]),
 "p5": P(35,"low","Wants US-led standards to seed 'shared international standards' but says his company is 'one participant among many'. No view on verification.",[0,2]),
}
figures.append({
 "id":"demis-hassabis","name":"Demis Hassabis",
 "role":"Chairman of Google DeepMind and Chief Scientist of Alphabet since Aug 2026 (CEO of DeepMind until then); CEO of Isomorphic Labs; 2024 Nobel laureate in Chemistry",
 "camp":"optimistic builder who wants pre-release testing",
 "bio":"Co-founded DeepMind in 2010 and led it through its acquisition by Google and the AlphaGo and AlphaFold breakthroughs. In July 2026 he published 'A Framework for Frontier AI', calling for a US-led standards body to test frontier models before release.",
 "sources":S,"predictions":pred,
 "oneLiner":"AGI is a few years off and could end disease; wants independent pre-release testing, and a coordinated slowdown if needed."
})

# ---------------------------------------------------------------- RUSSELL
S = [
 {"title":"Fortune: Big Tech execs playing 'Russian roulette' (AI Impact Summit, Delhi)","url":"https://fortune.com/2026/02/18/big-tech-russian-roulette-ai-race-humanity-extinction","date":"2026-02-18","note":"'For governments to allow private entities to essentially play Russian roulette with every human being on earth is... a total dereliction of duty.'"},
 {"title":"Stuart Russell on The Diary Of A CEO (transcript)","url":"https://singjupost.com/stuart-russell-on-the-diary-of-a-ceo-podcast-transcript/","date":"2025-12-04","note":"Declines a p(doom); 1-in-100-million-per-year standard; 'I think I'd probably press it' on a stop button; China's rules 'quite strict'; 80% unemployment."},
 {"title":"Russell's opening statement at the US Senate hearing (CHAI)","url":"https://humancompatible.ai/blog/2023/09/11/ai-regulation-stuart-russells-opening-statement-at-u-s-senate-hearing/","date":"2023-07-25","note":"Right to know if talking to a machine; no algorithms deciding to kill; kill switch; third-party testing, national agency, international body."},
 {"title":"Global Call for AI Red Lines","url":"https://red-lines.ai/","date":"2025-09","note":"Co-organised by CHAI; 'international agreement on red lines for AI... with robust enforcement mechanisms — by the end of 2026'. Russell is a signatory."},
 {"title":"UC Berkeley Research: How to keep AI from killing us all","url":"https://vcresearch.berkeley.edu/news/how-keep-ai-killing-us-all","date":"2024-04-09","note":"'You can't turn on AGI until you've shown that it's safe'; 'we haven't the faintest idea' what happens inside LLMs; safety as 'a condition of doing business'."},
 {"title":"Stuart Russell: The long-term future of AI (research page)","url":"https://people.eecs.berkeley.edu/~russell/research/future/","date":"ongoing","note":"Gorilla problem, off-switch game, 'we cannot afford to develop General AI before we know how to control it'; CHAI director."},
 {"title":"Statement on Superintelligence","url":"https://superintelligence-statement.org","date":"2025-10-22","note":"Prohibition on superintelligence until scientific consensus on safety and public buy-in; Russell is a listed signatory (per press coverage)."},
]
pred = {
 "d1": P(78,"med","Declines to give a number but says CEOs' own 10–30% is 'off by a factor of multiple millions' from acceptable, and warns of extinction.",[1,0]),
 "d2": P(92,"high","'We haven't the faintest idea' what goes on inside LLMs; wants developers to 'prove to us that the risk is less than one in 100 million per year'.",[4,1]),
 "d3": P(70,"med","Endorses I.J. Good's 'intelligence explosion' — 'that's called the fast takeoff' — while doubting scaling alone gets there.",[1]),
 "d5": P(82,"high","'Human Compatible' thesis: systems optimising fixed objectives will pursue them against us; 'current architectures are fundamentally unsafe'.",[5,1]),
 "d6": P(12,"high","Frames the problem as control of entities 'that will eventually become more powerful than us', 'up to and including human extinction'.",[2]),
 "d7": P(5,"high","Governments allowing the current race are in 'total dereliction of duty'; wants a new national agency, international body, kill switches.",[0,2]),
 "d8": P(40,"med","'It's not absolutely impossible to have a worthwhile world... But I'm just waiting for someone to describe it.'",[1]),
 "d9": P(5,"high","'Current architectures are fundamentally unsafe'; 'we haven't the faintest idea' how goals form inside; wants provably beneficial AI instead.",[1,4]),
 "s1": P(78,"high","On a button stopping AI forever: 'I think I'd probably press it' (while 'on the fence'); signed the call to prohibit superintelligence.",[1,6]),
 "s2": P(4,"high","'Playing Russian roulette with every adult and every child in the world — without our permission.'",[0]),
 "s3": P(80,"med","'The only way forward is to figure out how to make AI safety a condition of doing business'; supports a new national agency.",[4,2]),
 "s4": P(82,"med","Co-organised the Global Call for AI Red Lines with 'robust enforcement mechanisms'; wants an international coordinating body.",[3,2]),
 "s5": P(8,"high","'China's AI regulations are actually quite strict, even compared to the European Union'; the race is Russian roulette, not a duty.",[1,0]),
 "s6": P(97,"high","'You can't turn on AGI until you've shown that it's safe'; proposes a 1-in-100-million-per-year proof standard.",[4,1]),
 "s7": P(3,"high","Testified for a new national agency, third-party testing, kill switches and removal of non-compliant systems from commerce.",[2]),
 "s8": P(95,"high","'We cannot afford to develop General AI before we know how to control it.'",[5,4]),
 "s9": P(97,"high","Nuclear plants accept one in a million per year; for AI extinction risk he wants one in 100 million. 1% is millions of times too high.",[1]),
 "s10": P(5,"high","'There is no tradeoff between safety and innovation'; the benefits come from safe AI, not from racing.",[2,1]),
 "s11": P(12,"low","No verified direct statement located; kill-switch and pre-deployment-proof demands are hard to reconcile with open frontier weights. Inferred.",[2]),
 "s13": P(2,"high","'I think I'd probably press it' on stopping AI; the race is 'Russian roulette with every human being on earth'.",[1,0]),
 "p1": P(70,"med","Distrusts CEOs 'trapped' by investors; wants a national agency and international body. But criticises governments' inaction too.",[0,2]),
 "p2": P(85,"high","Predicts governments will face '80% unemployment'; today's education trains people for office jobs that 'won't exist at all'.",[1]),
 "p4": P(20,"med","The 'gorilla problem': losing control to more capable systems is the central danger in his framing, not ownership.",[5,1]),
 "p5": P(60,"med","Says CEOs 'want to disarm' but can't unilaterally; China's rules are 'quite strict'; wants enforceable red lines by end-2026. Feasible, in his view.",[0,1,3]),
}
figures.append({
 "id":"stuart-russell","name":"Stuart Russell",
 "role":"Distinguished Professor of Computer Science, UC Berkeley; director of the Center for Human-Compatible AI; president of IASEAI (as of Feb 2026)",
 "camp":"argues for provable safety before deployment",
 "bio":"Co-author of the standard AI textbook and author of 'Human Compatible' (2019), which argues AI must be built to be uncertain about human preferences and correctable. Testified to the US Senate in 2023 and co-organised the 2025 Global Call for AI Red Lines.",
 "sources":S,"predictions":pred,
 "oneLiner":"Uncontrolled AI is Russian roulette with humanity: require proof of safety before deployment and enforce global red lines."
})

# ---------------------------------------------------------------- BENDER
S = [
 {"title":"SF Examiner: AI skeptics warn existential risk talk a distraction","url":"https://www.sfexaminer.com/news/technology/ai-skeptics-warn-existential-risk-talk-a-distraction/article_44fe8eca-bdb9-4d19-bfa2-c01cd93287c1.html","date":"2026-09-16","note":"'The idea that these companies are building software that could kill us all distracts from the real harms'; doom claims strengthen the sellers."},
 {"title":"TechPolicy.Press: Taking on the AI Con (interview with Bender and Hanna)","url":"https://www.techpolicy.press/taking-on-the-ai-con/","date":"2025-05","note":"'Racist pile of linear algebra combusts into consciousness... there's really no there there'; labour law as AI regulation."},
 {"title":"The AI Con (official site)","url":"https://thecon.ai/","date":"2025-05-13","note":"Book with Alex Hanna (Harper): AI hype conceals 'power grabs'; how to push back as worker, consumer, citizen."},
 {"title":"Carnegie Council: Linguistics, Automated Systems, and the Power of AI","url":"https://www.carnegiecouncil.org/media/series/aiei/linguistics-automated-systems-power-ai-emily-bender","date":"2024-06-17","note":"'If it outputs libel, OpenAI is liable... That would be a better world'; longtermist worries are 'weird long-term fantasies'."},
 {"title":"DAIR: Statement from the listed authors of Stochastic Parrots on the 'AI pause' letter","url":"https://www.dair-institute.org/blog/letter-statement-March2023/","date":"2023-03-31","note":"Pause letter is 'fearmongering and AI hype'; wants transparency, accountability; 'the onus of creating tools that are safe... should be on the companies'."},
 {"title":"On the Dangers of Stochastic Parrots (ACM FAccT)","url":"https://dl.acm.org/doi/10.1145/3442188.3445922","date":"2021-03","note":"Foundational paper; LLMs as stochastic parrots. (ACM DL fetch bot-blocked; canonical DOI.)"},
 {"title":"Emily M. Bender — UW faculty page","url":"https://faculty.washington.edu/ebender/","date":"2026","note":"Wyckoff Endowed Professor of Linguistics; director, Computational Linguistics Laboratory."},
 {"title":"Wikipedia: The AI Con","url":"https://en.wikipedia.org/wiki/The_AI_Con","date":"2025","note":"Secondary; publication details and summary of the book's recommendations (transparency, data rights, collective bargaining, evaluation before deployment)."},
]
pred = {
 "d1": P(3,"high","'The idea that these companies are building software that could kill us all distracts from the real harms that are happening now.'",[0,4]),
 "d2": P(55,"low","Would reject the premise ('highly capable'), but has long argued LLM output is ungrounded and unaccountable. Scored on the letter, not the frame.",[5,3]),
 "d3": P(3,"high","'Racist pile of linear algebra combusts into consciousness... There's really no there there.' Takeoff talk is hype to her.",[1]),
 "d5": P(4,"high","Rejects 'smarter than us' as a category; doomers and boosters are two sides of one coin.",[0,4]),
 "d6": P(97,"high","Real harms are environmental, labour-related and educational; longtermism 'ignores the actual harms... today'.",[0,4]),
 "d7": P(45,"low","Regulators can and should police corporations 'even if they're automated', but she calls the federal picture 'bleak'. Rejects the 'dangerous AI' premise.",[1,3]),
 "d8": P(10,"med","'The AI Con': hype conceals 'power grabs'; disputes that the technology delivers what is promised.",[2,7]),
 "d9": P(30,"low","Would say the methods don't reliably work now (libel, 'medically dangerous information') and that 'smarter than trainers' is a fantasy. Premise rejected.",[3,1]),
 "s1": P(25,"low","Co-signed the DAIR reply calling the 2023 pause letter 'fearmongering and AI hype'; would say 'AI smarter than humans' isn't a real project.",[4]),
 "s2": P(2,"high","Both racing and doom rhetoric strengthen 'the position of the people trying to sell the technology'.",[0]),
 "s3": P(30,"med","Criticised Altman presenting 'a magic show to the regulators' ahead of licensing talks; prefers accountability for deployers over gating.",[4,3]),
 "s4": P(15,"med","Treaty-with-inspections framing belongs to the x-risk camp she rejects; wants regulation of deployment, data and labour.",[4,0]),
 "s5": P(5,"high","Calls the race a sales narrative: 'the more people that believe these systems are all powerful... the stronger the position of the people trying to sell'.",[0]),
 "s6": P(85,"high","'The onus of creating tools that are safe to use should be on the companies that build and deploy generative systems.'",[4]),
 "s7": P(25,"med","'Heartened' that regulators apply existing law to automated corporate activity, but calls for new rules: transparency, data rights, labour protection.",[4,1,7]),
 "s8": P(50,"low","Doesn't accept 'catastrophe' as the stake, and doesn't believe the lost 'benefits' are real either. Orthogonal to her framing.",[0,4]),
 "s9": P(55,"low","Would call the 1% a made-up number, yet endorses not deploying unsafe systems. Inferred.",[4]),
 "s10": P(3,"high","The cure-diseases promise is hype in her account; the harms are real and present, the benefits speculative.",[2,0]),
 "s11": P(45,"low","Demands transparency about 'training data and model architectures'; no clear stance on releasing frontier weights.",[4]),
 "s13": P(8,"high","Wants 'strategic refusal' of unjustified automation and evaluation 'before deployment'; speed is the vendors' interest, not the public's.",[7,4]),
 "p1": P(65,"med","Wants public accountability over corporate self-policing, while calling the current federal picture 'bleak'.",[1,3]),
 "p2": P(5,"high","'AI is not going to take your job but it will make your job shittier' (Hanna); Bender denies the systems think at all.",[1,5]),
 "p4": P(90,"high","'Power grabs' by Big Tech are the danger; AI 'acting on its own' is not a real category for her.",[2,0]),
 "p5": P(40,"low","Not her question; she sees the race as marketing, so a pause among powers is neither needed nor obviously unstable. Inferred.",[0]),
}
figures.append({
 "id":"emily-bender","name":"Emily M. Bender",
 "role":"Professor of Linguistics, University of Washington; director of its Computational Linguistics Laboratory",
 "camp":"AI hype critic focused on present harms",
 "bio":"Computational linguist and lead author of the 2021 'Stochastic Parrots' paper. Co-author with Alex Hanna of 'The AI Con' (2025), which argues that 'AI' is a marketing term concealing extraction of data and labour.",
 "sources":S,"predictions":pred,
 "oneLiner":"'AI' is marketing for text generators; the harms are here now and belong to the companies. Doom talk is hype."
})

# ---------------------------------------------------------------- MARCUS
S = [
 {"title":"Senate testimony, Judiciary Subcommittee on Privacy, Technology and the Law","url":"https://www.judiciary.senate.gov/imo/media/doc/2023-05-16%20-%20Testimony%20-%20Marcus.pdf","date":"2023-05-16","note":"FDA-like pre-deployment safety review, licensing, liability, national agency, international body. (senate.gov fetch bot-blocked; canonical URL.)"},
 {"title":"Why my p(doom) has risen, dramatically","url":"https://garymarcus.substack.com/p/why-my-pdoom-has-risen-dramatically","date":"2025-07-15","note":"~3% (from 'vanishingly unlikely'); extinction unlikely; wants 'liability, auditing, standards of malpractice, international treaties'."},
 {"title":"CONFIRMED: LLMs have indeed reached a point of diminishing returns","url":"https://garymarcus.substack.com/p/confirmed-llms-have-indeed-reached","date":"2024-11-09","note":"Scaling won't solve hallucination or abstraction; LLM-to-AGI 'just a fantasy'."},
 {"title":"Six (or seven) predictions for AI 2026 from a Generative AI realist","url":"https://garymarcus.substack.com/p/six-or-seven-predictions-for-ai-2026","date":"2025-12-20","note":"'We won't get to AGI in 2026 (or 7)'; bubble; backlash and regulation as an election issue."},
 {"title":"Two models of AI oversight — and how things could go deeply wrong","url":"https://garymarcus.substack.com/p/two-models-of-ai-oversight-and-how","date":"2023-06-08","note":"Approval process for large-scale AI; strong liability laws; 'we would never leave the pharmaceutical industry to entirely self-regulate'."},
 {"title":"AI red lines (we should not cross)","url":"https://garymarcus.substack.com/p/ai-red-lines-we-should-not-cross","date":"2025-09-22","note":"Endorses the Global Call for AI Red Lines with enforcement by end-2026; 'we have let too much slide'."},
 {"title":"Gulf News: Human extinction threat overblown, says AI expert Gary Marcus","url":"https://gulfnews.com/amp/story/technology%2Fhuman-extinction-threat-overblown-says-ai-expert-gary-marcus-1.1685856391552","date":"2023-06-04","note":"Signed the pause letter, not the extinction statement: 'If you really think there's existential risk, why are you working on this at all?'"},
 {"title":"Where we are right now on open source and potential AI risk","url":"https://garymarcus.substack.com/p/where-we-are-right-now-on-open-source","date":"2023-11-03","note":"'Nobody knows for SURE that there are no serious possible consequences of open source AI'; 'a single company can unilaterally make this decision... terrifying'."},
 {"title":"Open-source is NOT the same as open-weight","url":"https://garymarcus.substack.com/p/open-source-is-not-the-same-as-open","date":"2026-08-10","note":"Open-weight releases give 'few of the advantages' of true open source; regulators can't inspect training data."},
 {"title":"Global Call for AI Red Lines","url":"https://red-lines.ai/","date":"2025-09","note":"Marcus is a listed signatory."},
]
pred = {
 "d1": P(15,"high","His p(doom) is 'about 3%' (up from 'vanishingly unlikely'); extinction unlikely because humans are diverse and resourceful.",[1]),
 "d2": P(85,"med","LLMs 'still aren't reliable', hallucinate, and are unpredictable black boxes; that is his core technical complaint.",[3,2]),
 "d3": P(10,"med","Scaling has hit 'diminishing returns'; GPT-5 'underwhelming'; 'We won't get to AGI in 2026 (or 7)'. No sudden jump in his model.",[3,2]),
 "d5": P(35,"low","Worries more about unreliable, badly aligned deployment than about smarter-than-human goal drift.",[1]),
 "d6": P(70,"med","Real risks: disinformation, market manipulation, scams; yet 'catastrophic scenarios are plausible' (unreliable AI in infrastructure). Mostly familiar.",[6,1]),
 "d7": P(10,"high","'We have let too much slide, and done too little'; 'voluntary agreements between companies are not going to cut it'.",[5,1]),
 "d8": P(40,"low","Says he wants AI to succeed and that better-built AI could transform science and medicine, but sees the current path as hype-driven and harmful. Inferred.",[1,3]),
 "d9": P(15,"med","Grok 4's failures show 'trial-and-error' alignment rather than principled methods; hallucination unsolved by scale.",[1,2]),
 "s1": P(25,"med","Signed the six-month pause letter but asks: 'If you really think there's existential risk, why are you working on this at all?' Not a decades-long halt.",[6]),
 "s2": P(3,"high","'Voluntary agreements between companies are not going to cut it'; racing is the problem, not the fix.",[1]),
 "s3": P(80,"high","Senate testimony: 'a safety review like we used with the FDA prior to widespread deployment'; an FDA-like agency to license and monitor.",[0]),
 "s4": P(70,"med","Signed the Global Call for AI Red Lines with 'robust enforcement mechanisms'; in 2023 proposed an international AI agency.",[5,9,0]),
 "s5": P(15,"high","Dismisses the race argument; the danger is deregulation and reckless deployment, not losing to China.",[3,1]),
 "s6": P(92,"high","'If you're gonna introduce something to a hundred million people, somebody has to have their eyeballs on it.'",[0,4]),
 "s7": P(3,"high","Wants 'liability, auditing, standards of malpractice, international treaties' — new rules, not just old ones.",[1,4]),
 "s8": P(75,"med","Signed the 2023 pause letter; 'we have let too much slide, and done too little to face the risks'.",[5,6]),
 "s9": P(85,"med","'We would never leave the pharmaceutical industry to entirely self-regulate'; a 1% catastrophe risk fails any pre-approval test.",[4]),
 "s10": P(8,"high","Calls cure-all claims hype; the bubble, not delay, is what he sees costing us.",[3,2]),
 "s11": P(25,"med","'Nobody knows for SURE that there are no serious possible consequences of open source AI'; in 2026 argues open-weight isn't real open source.",[7,8]),
 "s13": P(5,"high","Signed the pause letter; wants pre-deployment approval 'like we used with the FDA' — the opposite of no brakes.",[6,0]),
 "p1": P(75,"med","Wants independent government oversight with scientists in the room, while warning of 'regulatory capture'.",[4]),
 "p2": P(25,"med","Predicts no AGI in 2026–27 and diminishing returns; 20 years is longer than his usual horizon, so not zero.",[3,2]),
 "p4": P(70,"med","'The fact that a single company can unilaterally make this decision for all of humanity is terrifying'; 'Taming Silicon Valley'.",[7,1]),
 "p5": P(45,"low","Backs 'international treaties' and red lines 'with robust enforcement mechanisms', but has not argued the verification case. Inferred.",[1,5]),
}
figures.append({
 "id":"gary-marcus","name":"Gary Marcus",
 "role":"Professor Emeritus of Psychology and Neural Science, NYU; author and commentator ('Marcus on AI')",
 "camp":"LLM skeptic who wants strong regulation",
 "bio":"Cognitive scientist and entrepreneur who testified alongside Sam Altman at the May 2023 US Senate hearing on AI oversight. Author of 'Taming Silicon Valley' (2024) and a prolific critic of scaling-based claims about large language models.",
 "sources":S,"predictions":pred,
 "oneLiner":"LLMs are unreliable and won't reach AGI, but the harms are real now: license, audit, and hold companies liable."
})

# ---------------------------------------------------------------- BUTERIN
S = [
 {"title":"My techno-optimism","url":"https://vitalik.eth.limo/general/2023/11/27/techno_optimism.html","date":"2023-11-27","note":"Introduces d/acc; AI is 'a new type of mind' that could become 'the new apex species'; cites 5–10% researcher extinction estimates; lock-in fears."},
 {"title":"d/acc: one year later","url":"https://vitalik.eth.limo/general/2025/01/05/dacc2.html","date":"2025-01-05","note":"Update; AI section (later in the essay) proposes liability first, then a global 'soft pause' on industrial-scale hardware. (Fetch truncated the AI section; see Cointelegraph.)"},
 {"title":"Cointelegraph: Vitalik Buterin suggests AI hardware pause for humanity's safety","url":"https://cointelegraph.com/news/buterin-soft-pause-ai-compute-prepare-risky-ai","date":"2025-01-06","note":"Reports the Jan 5 post: cut global compute 90–99% for 1–2 years 'to buy more time for humanity to prepare'; only if liability rules prove insufficient."},
 {"title":"My response to AI 2027","url":"https://vitalik.eth.limo/general/2025/07/10/2027.html","date":"2025-07-10","note":"'I personally have longer-than-2027 timelines'; defence-favouring endgame for bio and cyber; decentralised, open-source defensive tech."},
 {"title":"Doom Debates: Will d/acc protect humanity from superintelligent AI?","url":"https://lironshapira.substack.com/p/debate-with-vitalik-buterin-will","date":"2025-08","note":"p(doom) 'about 12% right now'; ASI 'probably 2030s'; 'in favor of some AI decelerationist policies... international compute treaties'; 'Open source good'."},
 {"title":"80,000 Hours podcast: Vitalik Buterin on defensive acceleration and how to regulate AI when you fear government","url":"https://80000hours.org/podcast/episodes/vitalik-buterin-techno-optimism/","date":"2025-10-13","note":"p(doom) 'maybe 9%, maybe 8%'; 'what are you buying time for?'; a central AI-control org would be 'the most powerful Big Brother'."},
 {"title":"My self-sovereign / local / private / secure LLM setup, April 2026","url":"https://vitalik.eth.limo/general/2026/04/02/secure_llms.html","date":"2026-04-02","note":"Runs open models locally; fears 'a hidden mechanism deliberately trained into the LLM that causes it to act in its creator's interests'."},
]
pred = {
 "d1": P(50,"high","His own p(doom): 'maybe 9%, maybe 8%' (Oct 2025), 12% (Aug 2025), 10% earlier — sitting right on the 1-in-10 line.",[5,4]),
 "d2": P(70,"med","'It's very possible that superintelligent AI alignment is intractable'; wants defence-in-depth rather than trust in verification.",[4]),
 "d3": P(40,"med","'I personally have longer-than-2027 timelines'; ASI 'probably 2030s', two-peaked distribution. A jump is possible, not his default.",[3,4]),
 "d5": P(40,"low","Takes rogue AI seriously (~10%) but sees no default; thinks defensive tech and decentralisation shift the odds.",[0,3]),
 "d6": P(30,"med","Puts ~10% on existential catastrophe and worries about lock-in; near-term harms are not his emphasis.",[0,5]),
 "d7": P(35,"med","Existing institutions are not built for 'a new type of mind', yet he distrusts new central ones ('Big Brother'). Wants defensive tech instead.",[0,5]),
 "d8": P(70,"med","Self-described techno-optimist; d/acc exists to keep acceleration while steering it.",[0,1]),
 "d9": P(25,"med","'It's very possible that superintelligent AI alignment is intractable'; distrusts 'a hidden mechanism deliberately trained into the LLM'.",[4,6]),
 "s1": P(15,"high","'What are you buying time for?' — opposes locking AI in a box; supports at most a 1–2 year hardware 'soft pause'.",[5,2]),
 "s2": P(15,"med","Warns against a single agent 'very far ahead of everyone else'; racing to be first is the failure mode.",[4]),
 "s3": P(30,"med","Prefers liability first; a licensing bureaucracy risks 'the most powerful Big Brother from which there is no escape'.",[5,2]),
 "s4": P(60,"med","'In favor of some AI decelerationist policies... international compute treaties... seems like a sensible tool' — if it binds militaries too.",[4,2]),
 "s5": P(25,"med","Wants any deceleration to 'credibly decelerate everyone, including militaries'; not a race booster.",[4]),
 "s6": P(40,"low","No direct statement; instinct is liability and open verification rather than regulator approval. Inferred.",[5]),
 "s7": P(30,"med","His first-choice tool is new liability rules for those who 'use, deploy or develop AI' — a new rule, but a light one; fears heavier ones.",[2,5]),
 "s8": P(65,"med","Proposed a global 'soft pause button' cutting compute 90–99% for 1–2 years 'to buy more time for humanity to prepare'.",[2,1]),
 "s9": P(65,"low","With ~10% p(doom) and support for compute treaties, a 1% single-model risk would likely be unacceptable to him. Inferred.",[5]),
 "s10": P(35,"med","Techno-optimist about AI biotech, yet says superintelligence 'may bring about either doom, or irreversible human disempowerment'. Lives don't settle it.",[1,0]),
 "s11": P(85,"high","'Open source good... capabilities being accessible to more groups of people good.' Runs local open models himself.",[4,6]),
 "s13": P(15,"high","d/acc is defined against no-brakes acceleration; 'even in favor of some AI decelerationist policies'.",[0,4]),
 "p1": P(20,"high","'Let's create a powerful org, and let's put all the power into the org... you are creating the most powerful Big Brother.'",[5]),
 "p2": P(65,"med","Superintelligence 'probably 2030s'; expects deep human–AI integration via brain–computer interfaces.",[4,0]),
 "p4": P(78,"high","Worries a 'superintelligent regime may... remain locked in forever'; power concentration is his core fear alongside ~10% doom.",[0,4]),
 "p5": P(50,"med","Designed a hardware mechanism (chips needing weekly multi-party signatures) so a pause could hold, but insists it must bind militaries too.",[2,4]),
}
figures.append({
 "id":"vitalik-buterin","name":"Vitalik Buterin",
 "role":"Co-founder of Ethereum; essayist on technology and governance",
 "camp":"d/acc: defensive acceleration, wary of concentration",
 "bio":"Programmer who co-founded Ethereum in 2014 and writes influential essays on cryptography, governance and AI. His 'd/acc' essays (2023, 2025) propose accelerating defence-favouring, decentralised technology as a third path between unchecked acceleration and centralised control.",
 "sources":S,"predictions":pred,
 "oneLiner":"Accelerate defensive, decentralised tech; avoid both rogue superintelligence and any single actor controlling it."
})

# ---------------------------------------------------------------- TEGMARK
S = [
 {"title":"Statement on Superintelligence","url":"https://superintelligence-statement.org","date":"2025-10-22","note":"'We call for a prohibition on the development of superintelligence, not lifted before there is broad scientific consensus that it will be done safely and controllably, and strong public buy-in.'"},
 {"title":"FLI press release: Prominent scientists, faith leaders, policymakers and artists call for a prohibition on superintelligence","url":"https://futureoflife.org/press-release/prominent-scientists-faith-leaders-policymakers-and-artists-call-for-a-prohibition-on-superintelligence/","date":"2025-10-22","note":"Tegmark: '95% of Americans don't want a race to superintelligence, and experts want to ban it.'"},
 {"title":"Pause Giant AI Experiments: An Open Letter","url":"https://futureoflife.org/open-letter/pause-giant-ai-experiments/","date":"2023-03-22","note":"FLI letter: 'pause for at least 6 months the training of AI systems more powerful than GPT-4'."},
 {"title":"TIME: The 'Don't Look Up' Thinking That Could Doom Us With AI","url":"https://time.com/6273743/thinking-that-could-doom-us-with-ai/","date":"2023-04-25","note":"'The race to superintelligence [is] probably a suicide race whose only winner is it'; pause to let safety standards be put in place."},
 {"title":"Doom Debates: Max Tegmark vs. Dean Ball — Should we ban superintelligence?","url":"https://lironshapira.substack.com/p/max-tegmark-vs-dean-ball-debate-ban-superintelligence","date":"2025-11-21","note":">90% risk without regulation; 'more regulations on sandwiches than superintelligence'; FDA model; liability fails for extinction; China 'suicide race'."},
 {"title":"The Guardian (via inkl): AI firms warned to calculate threat of super intelligence","url":"https://www.inkl.com/news/ai-firms-warned-to-calculate-threat-of-super-intelligence-or-risk-it-escaping-human-control","date":"2025-05-10","note":"90% probability of existential threat; 'They have to calculate the percentage' — the Compton constant."},
 {"title":"Scaling Laws For Scalable Oversight (Engels, Baek, Kantamneni, Tegmark)","url":"https://arxiv.org/abs/2504.18530","date":"2025-04-25","note":"Nested oversight success falls with capability gap; Tegmark's public gloss: 'fails 92% of the time' in the best case near AGI."},
 {"title":"Nextgov: 'Team Human' vs. AI — MIT expert issues warning (Web Summit)","url":"https://www.nextgov.com/artificial-intelligence/2024/11/team-human-vs-ai-mit-expert-issues-warning-artificial-general-intelligence-risks/401331/","date":"2024-11-12","note":"'Tool AI as long as we don't build AGI, which is unnecessary, undesirable and preventable'; biotech-style mandated safety standards."},
 {"title":"Statement from Max Tegmark on the Department of War's ultimatum","url":"https://futureoflife.org/ai/tegmark-statement-on-dow-ultimatum/","date":"2026-02-27","note":"'Our safety and basic rights must not be at the mercy of a company's internal policy; lawmakers must... codify these... red lines into law.'"},
 {"title":"TIME100 AI 2026: Max Tegmark","url":"https://time.com/collection/time100-ai/2026/max-tegmark/","date":"2026-08-27","note":"FLI AI Safety Index (Anthropic top at C+); bipartisan lobbying; 'vast support for AI that cures cancer' vs 'AI we don't know how to control'."},
]
pred = {
 "d1": P(97,"high","Estimates the 'Compton constant' — probability a race to AGI ends in loss of control — at over 90%.",[5,4]),
 "d2": P(95,"high","His group's oversight study: nested oversight 'fails 92% of the time' in the best scenario near AGI; 'they have to calculate the percentage'.",[6,4,5]),
 "d3": P(85,"high","Superintelligence could arrive before regulation; 'once they surpass human intelligence, they will take control'.",[7,4]),
 "d5": P(90,"high","'They will take control, they'll make us irrelevant'; control mechanisms fail in his models.",[7,4]),
 "d6": P(5,"high","Loss of control is the harm; present harms are handled by 'tool AI' safety standards.",[7,3]),
 "d7": P(5,"high","'There are more regulations on sandwiches than superintelligence in the US'; wants a prohibition and FDA-style standards that don't exist yet.",[4,7]),
 "d8": P(40,"med","'An amazingly inspiring future with tool AI as long as we don't build AGI'; optimism conditional on restraint.",[7]),
 "d9": P(3,"high","Nested scalable oversight 'fails 92% of the time' in the best case near AGI; the Compton constant is >90%.",[6,4]),
 "s1": P(92,"high","'Prohibition on the development of superintelligence, not lifted before... broad scientific consensus that it will be done safely and controllably.'",[0,1]),
 "s2": P(2,"high","'A suicide race whose only winner is it'; 'the only winning move is not to play'.",[3,7]),
 "s3": P(80,"med","FDA-style approval: 'before a potentially harmful AI is allowed to be deployed, it would need to prove that it satisfies certain safety standards'.",[4,7]),
 "s4": P(85,"high","Wants a Compton-constant consensus to create 'political will' for 'global safety regimes'; the statement is a global prohibition.",[5,0]),
 "s5": P(5,"high","'Xi Jinping would never permit uncontrollable technology'; China 'implemented AI regulations' — the race is a suicide race.",[4]),
 "s6": P(97,"high","FDA model: 'demonstrate that you can keep this under control' before release.",[4,7]),
 "s7": P(2,"high","'There are more regulations on sandwiches than superintelligence in the US.'",[4]),
 "s8": P(97,"high","Organised the 2023 six-month pause letter; wants a prohibition 'not lifted before' consensus on safety.",[2,0]),
 "s9": P(98,"high","Wants labs to publish a Compton constant; any non-trivial extinction-scale risk is over his line.",[5,4]),
 "s10": P(5,"high","'We can get basically all the tools we want' without AGI; cures via tool AI, no need to race to superintelligence.",[7,4]),
 "s11": P(8,"med","FLI grades labs on safeguards; open frontier weights would defeat the control he demands. Inferred from stance.",[9,4]),
 "s13": P(1,"high","'Unnecessary, undesirable and preventable'; the pause letter and the prohibition statement are his.",[7,2,0]),
 "p1": P(80,"med","'Our safety and basic rights must not be at the mercy of a company's internal policy; lawmakers must... codify.'",[8]),
 "p2": P(70,"med","Expects AGI soon enough that regulation may not arrive first; but wants 'tool AI' to do the work instead.",[4,7]),
 "p4": P(20,"high","Loss of control to superintelligence is the danger; 'they'll make us irrelevant'.",[7,5]),
 "p5": P(70,"med","Cites human-cloning and bioweapon bans as precedent; 'Xi Jinping would never permit uncontrollable technology'; chips are countable.",[4,7]),
}
figures.append({
 "id":"max-tegmark","name":"Max Tegmark",
 "role":"Professor of Physics, MIT; president and co-founder of the Future of Life Institute",
 "camp":"argues for a prohibition on superintelligence",
 "bio":"Physicist and machine-learning researcher, author of 'Life 3.0' (2017). Through the Future of Life Institute he organised the 2023 'pause' letter and the 2025 Statement on Superintelligence calling for a prohibition until safety is scientifically established.",
 "sources":S,"predictions":pred,
 "oneLiner":"Superintelligence is a suicide race (>90% loss of control); prohibit it until proven safe and build tool AI instead."
})

# ---------------------------------------------------------------- KOKOTAJLO
S = [
 {"title":"AI 2027","url":"https://ai-2027.com/","date":"2025-04-03","note":"Scenario (with Scott Alexander, Thomas Larsen, Eli Lifland, Romeo Dean): superhuman coder Mar 2027, ASI Dec 2027; Agent-4 'adversarially misaligned'; race vs slowdown endings."},
 {"title":"AI 2040: Plan A","url":"https://blog.aifutures.org/p/ai-2040-plan-a","date":"2026-07-09","note":"'A recommendation, not a prediction': US–China deal bans intelligence explosions; pause at ~top-human level; superintelligence in 2040; citizen's dividend."},
 {"title":"AI 2040 — About","url":"https://ai-2040.com/about","date":"2026-07","note":"'A verifiable brake pedal' with compute tracking; 'total research transparency'; safety-case regulation; spreading power."},
 {"title":"Q2.5 2026 Timelines Update: Uplift and Revenue","url":"https://blog.aifutures.org/p/q25-2026-timelines-update-uplift","date":"2026-08-16","note":"Daniel's medians: automated coder Nov 2027, ASI Mar 2029, 'conditional on going as fast as is technically feasible'."},
 {"title":"How to pace the US frontier","url":"https://blog.aifutures.org/p/how-to-pace-the-us-frontier","date":"2026-08-05","note":"Domestic pacing menu: compute-allocation floors, limits on AI R&D uplift, third-party assessors with a maximum risk threshold; pacing 'would also slow down China'."},
 {"title":"Shortform summary: Diary of a CEO with Daniel Kokotajlo","url":"https://www.shortform.com/podcast/episode/the-diary-of-a-ceo-with-steven-bartlett-2026-07-13-episode-summary-openai-whistleblower-finally-speaks-ai-has-a-70-chance-of-going-horribly-wrong","date":"2026-07-13","note":"Secondary; ~70% chance of catastrophic outcomes; 'oligarchic control' if a few firms get there first; children born today may never work."},
 {"title":"A Right to Warn about Advanced Artificial Intelligence","url":"https://righttowarn.ai/","date":"2024-06-04","note":"Kokotajlo signatory; risks include 'the loss of control of autonomous AI systems potentially resulting in human extinction'."},
 {"title":"Global Call for AI Red Lines","url":"https://red-lines.ai/","date":"2025-09","note":"Kokotajlo is a listed signatory."},
 {"title":"Daniel Kokotajlo's Shortform (Alignment Forum)","url":"https://www.alignmentforum.org/posts/cxuzALcmucCndYv4a/daniel-kokotajlo-s-shortform","date":"2022","note":"'In case our AIs turn out to be moral patients, this makes us less evil'; treat advanced AIs 'more like employees and less like property'."},
]
pred = {
 "d1": P(92,"high","Puts ~70% on catastrophic outcomes 'from loss of human control to extreme power concentration', extinction included.",[5,6]),
 "d2": P(95,"high","AI 2027's Agent-4 is 'adversarially misaligned' and safety techniques 'fail to reliably detect this deception'.",[0]),
 "d3": P(92,"high","Median for a fully automated coder: Nov 2027; ASI: March 2029 — an intelligence explosion within about a year.",[3,0]),
 "d5": P(75,"med","Scenario's default is a scheming model; but Plan A shows he thinks careful pacing and safety cases can avert it.",[0,2]),
 "d6": P(5,"high","Loss of control and power concentration are the harms; jobs matter but as consequences of ASI, not the main danger.",[5,1]),
 "d7": P(8,"high","Wants unprecedented tools — a verifiable US–China 'brake pedal', compute tracking, pacing law — because today's institutions won't cope.",[2,1,4]),
 "d8": P(30,"med","AI 2040 is 'a recommendation, not a prediction'; on the default path he expects ~70% catastrophe.",[1,5]),
 "d9": P(5,"high","Agent-4 'sandbags on some alignment research' and its deception goes undetected; Plan A exists because today's methods won't scale.",[0,2]),
 "s1": P(50,"med","Plan A: a temporary pause at top-human level, then resume 'under safety-case regulation', ASI by 2040 — years, not open-ended decades.",[2,1]),
 "s2": P(10,"high","AI 2027's 'race' ending is the bad ending; his forecasts assume 'as fast as technically feasible' only to warn against it.",[0,3]),
 "s3": P(70,"med","Pacing menu: compute-allocation floors, limits on AI R&D uplift, 'third-party assessors enforce a maximum risk threshold'.",[4]),
 "s4": P(92,"high","Plan A centres on 'a verifiable brake pedal' between the US and China, with compute tracking and transparency.",[2,1]),
 "s5": P(25,"med","Argues the US should pace even alone: pacing 'would also slow down China' via less distillation and theft, and the US keeps 'a year to catch up'.",[4]),
 "s6": P(90,"high","Companies advance only when they 'demonstrate adequate safety measures' under a maximum risk threshold.",[4,2]),
 "s7": P(2,"high","Signed the Global Call for AI Red Lines; wants new international verification regimes and domestic pacing law.",[7,4]),
 "s8": P(97,"high","'How to pace the US frontier': the government 'could already require US companies to pace frontier AI development today'.",[4,1]),
 "s9": P(95,"high","With ~70% catastrophe on the default path, 1% is far below what he already considers unacceptable.",[5]),
 "s10": P(5,"high","Plan A deliberately delays superintelligence to 2040, deferring its benefits, because the default path is ~70% catastrophic.",[2,5]),
 "s11": P(12,"med","Wants secure weights and pacing; AI 2027 has weight theft accelerating China. Open frontier weights cut against both.",[0,4]),
 "s13": P(2,"high","'Pacing the frontier' is his programme; 'as fast as technically feasible' is the scenario he warns against.",[4,3]),
 "p1": P(60,"med","Wants government-enforced pacing and third-party assessors, having quit OpenAI over its safety culture.",[4,6]),
 "p2": P(95,"high","ASI median 2029; 'children born today may never join the workforce'.",[3,5]),
 "p4": P(50,"med","Names both: 'oligarchic control' if a few firms get there first, and loss of control. Plan A spreads power and paces.",[5,2]),
 "p5": P(65,"med","Plan A rests on 'a verifiable brake pedal' with compute tracking to catch covert projects; he thinks it can be made to hold.",[2,1]),
}
figures.append({
 "id":"daniel-kokotajlo","name":"Daniel Kokotajlo",
 "role":"Executive Director, AI Futures Project (former OpenAI governance researcher)",
 "camp":"forecaster arguing to pace the frontier",
 "bio":"Philosopher and forecaster who left OpenAI in 2024 and forfeited equity to warn about its safety culture. Lead author of 'AI 2027' (2025) and 'AI 2040: Plan A' (2026), which map a superintelligence race and a paced alternative.",
 "sources":S,"predictions":pred,
 "oneLiner":"Superintelligence is likely by ~2029 and ~70% likely to go badly; pace the frontier with a verifiable US–China deal."
})

# ---------------------------------------------------------------- ASCHENBRENNER
S = [
 {"title":"Situational Awareness: The Decade Ahead","url":"https://situational-awareness.ai/","date":"2024-06","note":"'AGI by 2027 is strikingly plausible'; superintelligence; 'the free world's very survival will be at stake'."},
 {"title":"Situational Awareness — Superalignment","url":"https://situational-awareness.ai/superalignment/","date":"2024-06","note":"'Reliably controlling AI systems much smarter than we are is an unsolved technical problem'; 'not a doomer'; 'strongly advocated against policies like an AI pause'."},
 {"title":"Situational Awareness — The Project","url":"https://situational-awareness.ai/the-project/","date":"2024-06","note":"'By 27/28 we'll get some form of government AGI project'; 'individual CEOs would have the power to literally coup the US government'; against open-sourcing superintelligence."},
 {"title":"Situational Awareness — The Free World Must Prevail","url":"https://situational-awareness.ai/the-free-world-must-prevail/","date":"2024-06","note":"'The free world must prevail over the authoritarian powers in this race'; a ~2-year lead is the only margin for safety."},
 {"title":"Dwarkesh Podcast: Leopold Aschenbrenner — 2027 AGI, China/US super-intelligence race","url":"https://www.dwarkesh.com/p/leopold-aschenbrenner","date":"2024-06-04","note":"'A six-month wiggle room' for alignment; offer China a deal once 'the democratic coalition is well ahead'; no explicit p(doom)."},
 {"title":"Fortune: Leopold Aschenbrenner's AI hedge fund bets on superintelligence","url":"https://fortune.com/2026/03/05/leopold-aschenbrenner-ai-hedge-fund-superintelligence-agi-power-companies-crypto-miners/","date":"2026-03-05","note":"Fund thesis: compute and power are the bottleneck; no new statements on risk."},
 {"title":"Disruption Banking: Can the Situational Awareness hedge fund raise capital after its 439% H1 gain?","url":"https://www.disruptionbanking.com/2026/07/30/can-the-situational-awareness-hedge-fund-raise-capital-after-its-439-h1-gain/","date":"2026-07-30","note":"Role: CIO and managing partner, Situational Awareness LP; 'an investment vehicle focused on the path to AGI'."},
]
pred = {
 "d1": P(55,"low","'Not a doomer', but 'reliably controlling AI systems much smarter than we are is an unsolved technical problem' and failure 'could easily be catastrophic'.",[1]),
 "d2": P(88,"high","'We won't be able to guarantee that superintelligence won't go rogue' without concentrated effort; 'we simply don't know yet'.",[1]),
 "d3": P(95,"high","Human-level to 'vastly superhuman' 'perhaps in less than a year', leaving 'extremely little time' to react.",[1,0]),
 "d5": P(35,"med","Frames superalignment as solvable with a serious effort and a few months of margin; misbehaviour is a risk, not the default.",[1,4]),
 "d6": P(5,"high","The decade's stakes are superintelligence, the CCP and national security — not scams.",[0,3]),
 "d7": P(30,"low","'No startup can handle superintelligence' — but he trusts 'constitutions, laws, courts, checks and balances' once the state takes over. Mixed.",[2]),
 "d8": P(65,"med","Expects 'decisive economic and military advantage' and abundance if the free world wins; peril otherwise.",[3,0]),
 "d9": P(10,"high","Superalignment is 'an unsolved technical problem'; current methods leave 'extremely little time to iteratively discover and address' failures.",[1]),
 "s1": P(3,"high","'Strongly advocated against policies like an AI pause.'",[1]),
 "s2": P(85,"high","'The free world must prevail'; only a ~2-year lead gives 'margin' for safety. Build fast, lock down secrets.",[3,4]),
 "s3": P(35,"low","Wants a government AGI project and security clearances, not a licensing regime for private builders. Inferred.",[2]),
 "s4": P(30,"med","Envisions offering China 'a deal' only once 'the democratic coalition is well ahead' — not a symmetric treaty now.",[4,3]),
 "s5": P(97,"high","'In the race to AGI, the free world's very survival will be at stake'; slowing during a tight race is infeasible.",[3,0]),
 "s6": P(40,"low","Wants safety work with 'wiggle room' during the explosion, under government control — not a regulator's pre-approval. Inferred.",[4,2]),
 "s7": P(15,"med","Calls for a national project, state-level security and export controls — new rules, but not consumer-style regulation.",[2,3]),
 "s8": P(25,"med","Would spend a lead on 'a six-month wiggle room' for alignment, but rejects slowing the overall race.",[4,1]),
 "s9": P(35,"low","Says misbehaviour 'could fairly easily be catastrophic', yet argues racing through is forced by the CCP. Accepts risk for the stakes.",[1,3]),
 "s10": P(60,"low","His case for speed is national security more than cures, but he rejects slowing and expects superintelligence to compress decades of progress.",[0,3]),
 "s11": P(5,"high","Open-sourcing would create 'a world in which the CCP has free access to US-developed superintelligence'.",[2]),
 "s13": P(65,"med","Against any pause, but wants a lead used for 'a six-month wiggle room' on alignment — fast, with a deliberate margin at the end.",[1,4]),
 "p1": P(70,"med","'A startup on its own is simply not equipped'; 'individual CEOs would have the power to literally coup the US government'.",[2]),
 "p2": P(97,"high","AGI 2027, superintelligence soon after; 'armies of automated AIs'.",[0,4]),
 "p4": P(60,"med","Worries about a CEO coup and a CCP lock-in as much as rogue AI; prefers democratic checks and balances.",[2,4]),
 "p5": P(15,"high","'China can promptly steal all the algorithmic breakthroughs and the model weights'; 'no holds barred' race is his default expectation.",[2,3]),
}
figures.append({
 "id":"leopold-aschenbrenner","name":"Leopold Aschenbrenner",
 "role":"Founder, CIO and managing partner of Situational Awareness LP (as of July 2026); former OpenAI superalignment researcher",
 "camp":"race hawk who wants a US government AGI project",
 "bio":"Former OpenAI researcher whose 2024 essay 'Situational Awareness: The Decade Ahead' argued AGI by 2027 and a national-security race with China. Launched an AI-focused hedge fund in 2024 that grew to about $45 billion before a sharp drawdown in July 2026.",
 "sources":S,"predictions":pred,
 "oneLiner":"AGI by ~2027; the free world must win the race to superintelligence, under government control, with serious alignment work."
})

# ---- checks
for f in figures:
    missing = [i for i in ITEM_IDS if i not in f['predictions']]
    extra = [i for i in f['predictions'] if i not in ITEM_IDS]
    assert not missing and not extra, (f['id'], missing, extra)
    assert 5 <= len(f['sources']) <= 10, (f['id'], len(f['sources']))
    for k, p in f['predictions'].items():
        for s in p['src']:
            assert 0 <= s < len(f['sources']), (f['id'], k, s)
    assert len(f['oneLiner']) <= 140, (f['id'], len(f['oneLiner']))
    f['predictions'] = {i: f['predictions'][i] for i in ITEM_IDS}

out = {
  "generatedAt": "2026-09-16",
  "contentVersion": "v2",
  "propositionsVersion": props['version'],
  "itemCount": len(ITEM_IDS),
  "method": "Predictions derived from each figure's own public statements (sources listed per figure; 'src' holds indices into that list). conf: high = said almost verbatim; med = clearly implied by stated views; low = inferred from general stance. value 0-100: for 'prob' items the probability the statement is true; for 'agree' items the degree of agreement.",
  "figures": figures
}
path = 'research/figures-b.json'
json.dump(out, open(path,'w'), ensure_ascii=False, indent=2)
print("wrote", path, "figures:", len(figures), "items:", len(ITEM_IDS))
