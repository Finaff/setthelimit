# French edition: translation notes (v2-fr, 17 September 2026)

Scope: 176 UI strings (`site/lang/fr.js`), 24 propositions (`content/propositions.v2.fr.json`),
12 context facts (`site/lang/context.fr.js`), 16 figures (`site/lang/figures.fr.js`).
Checked by `node tools/check-fr.js` (keys, placeholders, HTML tags, ids, word counts, typography).

Register: standard international French that reads naturally in Québec; vouvoiement; « nous » for the
inclusive "we" of the propositions, « on » only in maxims (« On ne mène pas une expérience… »).
Rule followed throughout: no hedge added, no intensifier added, no modal changed ("should" → « devrait »,
"will" → futur, "would" → conditionnel, "may/could" → « pourrait / peut-être »).

## Typography

- Apostrophe ’ (U+2019) everywhere; no-break space U+00A0 before ; : ? ! % and inside « »; written as
  the escape `\u00a0` in the generated files so that editors cannot silently strip it.
- English single quotes → « » (titles, scare quotes, quoted slogans). English titles keep their own
  punctuation inside the guillemets (« AI 2040: Plan A », « Situational Awareness: The Decade Ahead », « Life 3.0 »).
- Numbers: 1 200, 73 971 (no-break space), 0,38 %, 1,03 milliard de dollars, 45 milliards de dollars.
- "~25%" → « environ 25 % »; ">90%" → « plus de 90 % »; "by ~2029" → « d’ici 2029 environ ».

## Term choices

| English | French | Why |
|---|---|---|
| speed limit / Set my limit | limite de vitesse / Fixer ma limite | « fixer une limite » is the idiomatic collocation |
| full stop / no limit | arrêt complet / sans limite | matches the signs ARRÊT and SANS LIMITE |
| road conditions | état de la route | understood everywhere; « conditions routières » is more Québec-only |
| black ice | glace noire | as briefed; used on the axis, in the score sentence and in the Road Closed blurb |
| dot (on the map) | point; "claim your dot" → « revendiquer votre point » | |
| public figures / Figures | personnalités publiques / Personnalités | « figures » alone is a false friend in a nav bar |
| predicted / estimates | prédit, prédictions / estimations | the English keeps the two apart, so does the French |
| score | score | in all dictionaries; « pointage » is Québec-only |
| frontier AI, frontier model | IA de pointe, modèle de pointe | the term used in French-language government texts (Bletchley, Canada) |
| pace the frontier | régler la cadence de l’IA de pointe | "pace" is neither "slow" nor "pause"; « régler la cadence » keeps it neutral. « modérer » or « freiner » would sharpen it |
| pause / halt / stop / prohibition / slowdown | pause (mettre en pause) / arrêt / cesser, s’arrêter / interdiction / ralentissement | kept strictly apart, as in English. « moratoire » is never used: no English source string says "moratorium", and the word adds a legal flavour the halt side does not claim |
| enforced (halt) | contraignant; "a pause you can’t enforce" → « qu’on ne peut pas faire respecter » | |
| takeoff | « décollage » | in guillemets, as in the English plain text |
| open weights | « poids ouverts » | glossed by the plain text, as in English |
| open-source advocate | défenseur du code source ouvert | |
| steelman | « plaidoyer »; "the strongest honest case" → « l’argumentaire honnête le plus solide »; in archetype blurbs "the strongest form of your view" → « la version la plus forte de votre position » | no French equivalent of "steelman"; the anglicism is avoided and the definition carries the meaning |
| reviewed adversarially | soumis à une révision contradictoire | « contradictoire » is the French legal/scientific term for hearing both sides |
| halt-and-pause side / build-fast side / build side | le camp de l’arrêt et de la pause / le camp qui veut construire vite / le camp de la construction | descriptive, no label either side would refuse. « accélérationnistes » is kept for the people who use it of themselves (Verdon) |
| loaded (item) | tendancieuse | |
| build (AI) | développer in the title question (« À quelle vitesse faut-il développer l’IA ? »); construire wherever the concrete verb carries the argument (« c’est en construisant une chose qu’on apprend à la rendre sûre ») | |
| makers | concepteurs (of a model); fabricant (s6 "for", product-safety analogy) | |
| highly capable AI | une IA très capable | « performante » would add a value judgment |
| goals | buts | plainer than « objectifs » |
| harms | préjudices (« dégâts » once in d6 plain and s11 against for "damage") | « méfaits » implies intent; « torts » reads oddly in the plural |
| safe / safety | sûr / sécurité; "run it safely" → « la mener sans danger » | |
| safeguards, guardrails | garde-fous | |
| human feedback | rétroaction humaine | |
| graders | correcteurs | keeps the pupil/teacher image of d9 plain |
| deepfakes | hypertrucages | OQLF and FranceTerme term |
| autocomplete | saisie semi-automatique | |
| license (s3) | permis | works in Québec and in France; « licence » is ambiguous with software licences |
| regulatory capture / easily captured | capture réglementaire / se laissent facilement capturer | established term in French economics |
| incumbents | acteurs établis | |
| burden of proof | fardeau de la preuve | natural in Canada, understood in France (« charge de la preuve ») |
| regulator | autorité de réglementation | |
| trade-off | arbitrage | |
| body count | « fait aussi des morts »; « un bilan de morts » (s10 for) | same bluntness as the English, no euphemism |
| upside | gain potentiel | |
| race to the top | « course vers le sommet » | « nivellement par le haut » is the usual opposite of "race to the bottom" but loses the race image the argument needs |
| leadership (s5) | la première place | avoids the anglicism and avoids « dominer », which would sharpen |
| deal (s5, Kokotajlo) | entente | |
| chips / clusters / computing power | puces / grappes / puissance de calcul | |
| sandbox | bac à sable | |
| superforecasters | superprévisionnistes | |
| AGI | IA générale | spelled out; « IAG » is not yet familiar to lay readers |
| LLM | grands modèles de langage | |
| world models / tool AI / non-agentic | modèles du monde / IA-outils / non agentique | |
| alignment, superalignment | alignement, superalignement | |
| start-up | jeune pousse | |
| hype | battage | |
| CEO / executive chairman / Chairman / general partner / CIO / managing partner | PDG / président exécutif du conseil / président du conseil / associé commandité / directeur des placements / associé directeur | |
| as of Sept 2026 | en date de sept. 2026 | |
| interviews | entrevues | avoids the anglicism « interviews »; understood in France |
| email | courriel | |
| Forecast / Opinion | Prévision / Opinion | |

Archetypes, road signs and slider words are exactly as briefed (Autobahn, Pilote de rallye, Zone scolaire,
Route fermée, Limite affichée; Route dégagée, Brouillard possible, Chaussée glissante, Glace noire, Pont fermé).
None was changed.

## Decisions driven by French grammar (worth knowing before editing)

- `{list}` on the home page: the fallback "the people who shape this debate" is rendered « celles et ceux qui
  façonnent ce débat » and the sentence uses « par rapport à {list} ». With « les personnes… » the app would
  print « à les personnes »; with « aux côtés de {list} » it would print « de Eliezer… ».
- `{name}` in "not statements by {name}": « de {name} » would need elision for Altman, Amodei, Andreessen,
  Aschenbrenner. Rendered « Ces estimations sont les nôtres ; {name} ne les a pas formulées. » (also gender-neutral).
- "You’ve answered {n}." → « Réponses données jusqu’ici : {n}. » to avoid « 1 propositions ».
- "Versus the person who sent you here" → « la personne qui vous a transmis ce lien »: avoids a past participle
  that would have to agree with the reader’s gender (« envoyé/envoyée »).
- "Them" (singular they, the person who sent the link) → « L’autre ». « Eux » is plural and « Lui/Elle » guesses a gender.
  "They set the limit at…" → « Cette personne fixe… »; "Their closest public figure" → « Sa personnalité publique… ».
- Confidence words are feminine (« élevée, moyenne, faible ») because they qualify « confiance » on the figure pages;
  the Method text was phrased to match (« en indiquant la confiance (élevée quand… »).
- "agree" in « 7/12 agree » → « d’accord »; "gap" → « écart ».
- "Torn" → « Partagé » as briefed (generic masculine). If an inclusive form is wanted: « Partagé·e » is not
  recommended by the OQLF; « Entre les deux » would be a neutral alternative.
- Context fact 4: "No federal frontier-AI law exists yet" → « aucune loi fédérale américaine ». For a Canadian reader
  « fédérale » alone points to Ottawa. This is the only place where a word was added for disambiguation.
- Bengio: LawZero is kept as the organisation name, as instructed. Its own French name is LoiZéro; consider
  showing « LawZero (LoiZéro) » to Québec readers.
- "a third [editor] for plain English" → « un troisième réviseur veillant à la simplicité de la langue »: the
  French reader does not need to know the review language, and the French itself was held to the same rule.
- Quoted passages from English sources (the employees’ letter, the Statement on Superintelligence, the
  International AI Safety Report, Gallup) are our own translations inside « ». Book, essay and paper titles stay in English.

## English sentences found ambiguous (and the reading chosen)

1. **s9 against**: "refusing to act on guesses is how nothing ever gets built." Two parses: (a) refusing to
   [act on guesses]; (b) [refusing to act] because of guesses. Only (b) supports the build side’s argument, so:
   « s’abstenir d’agir à cause de conjectures, c’est ainsi que rien ne se construit jamais ». The English would be
   clearer as "refusing to build because of a guess…".
2. **d1 plain**: "The headline question." Could mean "the main question" or "the one that makes the headlines".
   The changelog says it replaced "the core question" precisely to avoid claiming centrality, so:
   « La question qui fait les manchettes ».
3. **Figures page**: "They are not endorsements." Unclear who is not endorsing whom (the figures endorsing the
   site, or the site endorsing the figures). Kept equally open: « Elles ne constituent pas un appui ».
4. **Bender one-liner**: "the harms are here now and belong to the companies." Read as attribution of
   responsibility: « ils sont le fait des entreprises ».
5. **Context fact 2**: "help 'deliberately pace the frontier' of AI development": the quotation cuts across a noun
   phrase. Rendered « d’aider à « régler délibérément la cadence » du développement de l’IA de pointe », with only the
   verb phrase inside the guillemets.
6. **s8 text**: "and the benefits lost with it": "it" = the delay. « et les bienfaits perdus avec ce retard ».
7. **d8 against**: "'Most likely' is doing a lot of work" → « porte ici beaucoup de poids » (the idiom has no direct
   equivalent; the point, that the phrase hides the tail, is carried by the rest of the sentence).
8. **p1 against**: "easily captured" is jargon in English too; kept as « se laissent facilement capturer ».

## Length

Proposition `text` fields: 22 of 24 are at or under 25 words; d3 and d6 have 26 (French articles). Shortening
either one further would have meant dropping "at some point" (d3) or turning the examples of d6 into a closed list,
so they were left at 26. The checker enforces the hard limit of 30.

## Things outside the translation files that still show English

- `site/app.js` line 120 prints `As of ${STAMP}` with a hard-coded "As of"; with the French stamp it renders
  "As of septembre 2026". Suggested fix: wrap it in `T('As of {stamp}')` and add the key
  (« En date de {stamp} ») to `research/ui-strings.en.json` and `site/lang/fr.js`.
- `site/index.html` meta description and Open Graph texts are English only.
- Figure `sources[].title/note`, `predictions[].basis` and `photoNote` were out of scope and remain in English on
  the figure pages.
- `site/content.fr.js` is generated: run `node tools/build-content.js` to build it from
  `content/propositions.v2.fr.json` (not run here, since it rewrites existing files).

## v3

`content/propositions.v3.fr.json` (`"version": "v3-fr"`) follows `content/propositions.v3.proposed.json`. Only the 20
fields whose English changed were re-translated (d1.plain, d2.text, d2.plain, d3.text, d7.text, d7.plain, d7.for,
d8.text, d8.plain, d8.against, d9.text, d9.plain, s5.plain, s6.text, s6.plain, s8.text, s9.for, s11.text, s11.plain,
p5.for); the other 200 fields are byte-identical to v2-fr (same serialisation, ` ` escapes). Inside a changed
field, every sentence whose English did not move keeps its v2 French word for word. All term choices above stand,
with the one exception noted under s6. Length: s11 and d6 (unchanged) have 26 words, every other `text` has 24 or
fewer; d3 went from 26 to 21.

- **d2 text**: "to tell whether" → « de savoir si » (v2 had « de vérifier qu’ » for "to check that"); the clause on untested
  situations is dropped, as in English. **d2 plain**: "dependable way … to know" → « un moyen fiable de savoir »;
  "once it meets situations" → « lorsqu’elle rencontrera des situations ». « fiable » serves for both "reliable" and
  "dependable", as in v2.
- **d3 text**: « feront probablement un bond si soudain que personne n’aura le temps de réagir ». A noun (« un bond si
  soudain ») avoids the pile-up « probablement si soudainement », and echoes the unchanged plain (« bondir d’un seul
  coup, sans que personne ait le temps de réagir »). "has time" → futur (« n’aura »), required after a main clause in the future.
- **d7 text**: « les humains pourront encore la garder sous contrôle ». "still" is both concessive and continuative in
  English; « encore » keeps both. « toujours » was avoided (reads as "always", which would sharpen), and « quand même »
  keeps only the concessive half. No mention of institutions or safeguards. **d7 plain**: "rein it in" → « la maîtriser »
  (« brider » suggests throttling performance); "people" → « les gens ». **d7 for**: "kept the lid on" → « nous maintenons le
  couvercle sur », the same image as the plain (« le couvercle a tenu »); "the defenders" → « les défenseurs », bare, as in English.
- **d8 text**: « Avec l’IA avancée, un monde bien meilleur est beaucoup plus probable qu’une catastrophe. » The
  verb-for-verb rendering (« a beaucoup plus de chances de rendre le monde bien meilleur que de finir en catastrophe ») makes
  the reader parse « bien meilleur que… » as the comparison, all the more because v2 ended on « bien meilleur que celui
  d’aujourd’hui ». Two nouns, one comparison: the same two outcomes and the same "far more likely" (« beaucoup plus
  probable »; « bien plus » would have doubled « bien »). **d8 plain**: "weigh … against each other" → « Mettez en balance »;
  "a real contender" → « une concurrente sérieuse »; "If you expect neither" → « ni à l’une ni à l’autre ». **d8 against**: the
  quoted words are those of the French text (« Beaucoup plus probable »); "is doing a lot of work" → « porte ici bien du
  poids » (replaces « beaucoup de poids » of v2, point 7 above, only to avoid « beaucoup » twice in six words); "calling the
  odds good" → « dire que les chances sont bonnes »; "outthink" → « surpasser en intelligence », as in d1 for.
- **d9 text**: « À mesure que l’IA deviendra plus capable, notre aptitude à la garder sûre suivra le rythme. » « aptitude »
  rather than « capacité » so that the sentence does not read « plus capable, notre capacité »; "keep it safe" → « la garder
  sûre » (« rendre sûre », used in s1, is "make safe"); "keep pace" → « suivre le rythme ». **d9 plain**: "On the path we’re on"
  → « Sur la voie où nous sommes engagés »; "safety methods" → « les méthodes de sécurité ».
- **s6 text**: "a regulator" → « un organisme de réglementation », as briefed for v3. It ties the item to « un organisme
  public » in its plain and in p1. For consistency inside the item, the plain now also says « l’organisme de
  réglementation » where v2 had « l’autorité de réglementation » (the table entry above describes v2). **s6 plain**:
  "Agree means no release until…" → « Être d’accord signifie : aucun lancement tant que le concepteur n’a pas démontré à
  un organisme public que le modèle est sûr. »
- **s8 text**: « Réduire la probabilité de catastrophe vaudrait un retard de quelques années pour l’IA, et pour ses
  bienfaits. » Same trade, both sides still in the sentence; « vaudrait », with no « bien » added. Point 6 above (the
  antecedent of "it") no longer applies.
- **s11 text**: « Les développeurs devraient être libres de publier ouvertement même les modèles d’IA les plus puissants… ».
  The claim is permission ("should be free to"), not an obligation to publish. « quiconque » replaces « n’importe qui » to
  stay at 26 words. **s11 plain**: "Should that stay legal…" → « Cela devrait-il rester légal même pour les modèles les plus puissants ? »
- **d1 plain, d8 plain**: "the middle of the slider" → « le milieu du curseur » (the UI strings say « Glissez pour répondre »
  and « près du milieu »; no other word for the control exists in `site/lang/fr.js`). "your own guess" → « votre propre
  estimation », the word d1 for already uses for the same number; "right around" → « tourne autour de ».
- **s5 plain**: "a major AI builder" → « ne compte pas parmi les grands constructeurs d’IA »; "the group of countries it
  stands with" → « le groupe de pays aux côtés desquels il se range » (looser than « alliés », as in English).
- **s9 for**: "far worse" → « bien pire ». **p5 for**: « logées dans des centres de données assez vastes pour être repérés
  par satellite ».

Not done here (other files were out of scope): `tools/check-fr.js` and `tools/build-content.js` still read
`content/propositions.v2.fr.json` and the checker still compares against `content/propositions.v2.json`; both need to
point at the v3 files when v3 is applied. The word limit used for the v3 check was 26 (the checker’s hard limit is 30).
