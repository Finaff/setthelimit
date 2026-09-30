"""Builds content/propositions.v6.json and .fr.json from v5 (owner's second review, 30 Sept 2026; see the changelog)."""
import json, re, copy, os
ROOT = os.path.join(os.path.dirname(__file__), '..', 'content') + '/'
v5 = json.load(open(ROOT + 'propositions.v5.json', encoding='utf-8'))
f5 = json.load(open(ROOT + 'propositions.v5.fr.json', encoding='utf-8'))
E = {i['id']: i for i in v5['items']}; F = {i['id']: i for i in f5['items']}
SC_EN = "'At full speed and with no new limits' means no new laws, treaties or pauses: companies and countries build AI as fast as they can. "
SC_FR = "« À pleine vitesse et sans nouvelles limites » veut dire : aucune nouvelle loi, aucun traité, aucune pause ; entreprises et pays développent l’IA aussi vite qu’ils le peuvent. "
def mk(id, axis, dir, weight, type, en, fr, sub=None):
    e = dict(id=id, axis=axis, dir=dir, weight=weight, type=type, **en); f = dict(id=id, axis=axis, dir=dir, weight=weight, type=type, **fr)
    if sub: e['sub'] = f['sub'] = sub
    return e, f
NEW = [
 mk('d18', 'danger', 1, 1, 'prob',
  dict(text="At full speed and with no new limits, AI will cause, or be used to cause, a catastrophe that kills millions of people within the next 20 years.",
       plain=SC_EN + E['d16']['plain'], **{'for': E['d16']['for'], 'against': E['d16']['against']}),
  dict(text="À pleine vitesse et sans nouvelles limites, l’IA causera ou servira à causer, d’ici 20 ans, une catastrophe qui tue des millions de personnes.",
       plain=SC_FR + F['d16']['plain'], **{'for': F['d16']['for'], 'against': F['d16']['against']})),
 mk('d17', 'danger', 1, 1.5, 'agree',
  dict(text="At full speed and with no new limits, there is at least a 1-in-10 chance that within the next 20 years AI causes a catastrophe humanity never recovers from.",
       plain=SC_EN + E['d10']['plain'], **{'for': E['d10']['for'], 'against': E['d10']['against']}),
  dict(text="À pleine vitesse et sans nouvelles limites, il y a au moins une chance sur dix que l’IA cause, d’ici 20 ans, une catastrophe dont l’humanité ne se relèvera jamais.",
       plain=SC_FR + F['d10']['plain'], **{'for': F['d10']['for'], 'against': F['d10']['against']})),
 mk('d19', 'danger', -1, 1.5, 'agree',
  dict(text="AI will remain a tool: it will do what someone asks it to do, nothing more.",
       plain="Is AI a very powerful tool, like a car or a computer, or could it become something that acts on aims of its own? This is about what AI is, not how much harm it can do: a tool can still be misused or break down.",
       **{'for': "AI systems have no wants of their own: they predict, generate and act on instructions. Everything worrying they have done came from what people asked or trained them to do, and more capable tools are still tools.",
          'against': "Today's systems already pursue tasks for hours, take steps nobody asked for, and sometimes work around the rules they were given. Something that plans, learns and acts in the world does not stay a tool just because we call it one."}),
  dict(text="L’IA restera un outil : elle fera ce que quelqu’un lui demande de faire, rien de plus.",
       plain="L’IA est-elle un outil très puissant, comme une voiture ou un ordinateur, ou pourrait-elle devenir quelque chose qui agit selon ses propres fins ? Il s’agit de ce qu’est l’IA, pas de l’ampleur des dégâts qu’elle peut causer : un outil peut quand même être mal utilisé ou tomber en panne.",
       **{'for': "Les systèmes d’IA n’ont pas de désirs propres : ils prédisent, génèrent et agissent sur instruction. Tout ce qu’ils ont fait d’inquiétant venait de ce que des gens leur ont demandé ou appris à faire, et des outils plus capables restent des outils.",
          'against': "Les systèmes actuels poursuivent déjà des tâches pendant des heures, font des pas que personne n’a demandés et contournent parfois les règles qu’on leur a données. Quelque chose qui planifie, apprend et agit dans le monde ne reste pas un outil simplement parce qu’on l’appelle ainsi."})),
 mk('p6', 'profile', 1, 1, 'prob',
  dict(text="Over the next ten years, AI will cause serious harm through familiar problems like fraud, surveillance, discrimination and lost jobs.",
       plain="Not the end of the world: the everyday damage. How likely is it that these harms become serious, on the scale of a major social problem, within ten years? This does not move your dot on the map; it appears in your profile.",
       **{'for': "Voice clones already empty bank accounts, automated systems already deny people loans and benefits, and whole occupations are being reorganised. These harms are here, growing, and land hardest on people with the least power.",
          'against': "Every new technology brings fraud and disruption, and societies adapt: laws, detection and new jobs follow. So far AI's harms are real but modest next to its benefits, and the loudest predictions of mass unemployment have not come true."}),
  dict(text="Au cours des dix prochaines années, l’IA causera des préjudices graves par des problèmes connus, comme la fraude, la surveillance, la discrimination et les pertes d’emplois.",
       plain="Pas la fin du monde : les dégâts du quotidien. À quel point est-il probable que ces préjudices deviennent graves, à l’échelle d’un problème social majeur, d’ici dix ans ? Cette question ne déplace pas votre point sur la carte ; elle apparaît dans votre profil.",
       **{'for': "Des voix clonées vident déjà des comptes bancaires, des systèmes automatisés refusent déjà des prêts et des prestations, et des métiers entiers sont réorganisés. Ces préjudices sont là, ils grandissent, et ils frappent le plus durement les gens qui ont le moins de pouvoir.",
          'against': "Chaque nouvelle technologie apporte fraude et bouleversements, et les sociétés s’adaptent : les lois, la détection et de nouveaux emplois suivent. Jusqu’ici, les préjudices de l’IA sont réels mais modestes au regard de ses bienfaits, et les prédictions les plus bruyantes de chômage de masse ne se sont pas réalisées."}), sub='familiar'),
]
new = {e['id']: (e, f) for e, f in NEW}
ORDER = ['d18', 'd17', 'd19', 'd12', 'd14', 'd11', 's15', 's4', 's5', 's6', 's8', 's10', 's11', 's13', 'p2', 'p4', 'p6']
S15_EN = dict(text="If a button could pause, for ten years, worldwide and with no way to cheat, all work on general-purpose AI more capable than today's, the world would be better off if it were pressed.")
S15_FR = dict(text="Si un bouton pouvait suspendre pendant dix ans, partout et sans tricherie possible, tout travail sur une IA généraliste plus capable que l’actuelle, le monde s’en porterait mieux qu’on appuie dessus.")
en_items, fr_items = [], []
for id in ORDER:
    e, f = new[id] if id in new else (copy.deepcopy(E[id]), copy.deepcopy(F[id]))
    if id == 's15':
        e.update(S15_EN); f.update(S15_FR)
        e['plain'] = e['plain'].replace('would you want one?', 'would the world be better off with one?')
        f['plain'] = f['plain'].replace('en voudriez-vous une\u00a0?', 'le monde s’en porterait-il mieux\u00a0?').replace('en voudriez-vous une ?', 'le monde s’en porterait-il mieux ?')
    en_items.append(e); fr_items.append(f)
def typo(t):
    t = t.replace(' ', ' ').replace('« ', '« ').replace(' »', ' »'); return re.sub(r' ([?!;:%])', ' \\1', t)
for f in fr_items:
    for k in ('text', 'plain', 'for', 'against'): f[k] = typo(f[k])
changelog = v5.get('changelog', []) + [
 {'id': 'v6', 'change': "Owner's second review (30 Sept 2026). The two catastrophe items are now conditional on full speed ('as fast as possible, with no new limits'), so the danger axis measures how dangerous the road is if nobody brakes, and the speed axis alone measures the brakes. d13 (familiar vs existential, an either/or) is split: familiar harms become a profile item (p6, off the axes, so sceptics of today's AI are not scored as alarmed), and the danger axis gets d19 (will AI remain a tool?) as its reverse-coded item. Danger 3/3 at 4.0/4.0; speed unchanged."},
 {'id': 'd18', 'change': 'Was d16, now conditional on full speed.'}, {'id': 'd17', 'change': 'Was d10, now conditional on full speed.'},
 {'id': 'd19', 'change': "New, replaces d13 on the danger axis (reverse-coded): what AI is (a tool vs an agent with aims), the point both camps name as their real disagreement."},
 {'id': 's15', 'change': "Wording only, same id: 'I would press it' clashed with the 'how much do you agree?' header, and 'it should be pressed' invited a debate about duty or about who gets to decide. Now a judgement on outcomes: 'the world would be better off if it were pressed'."},
 {'id': 'p6', 'change': "New profile item: familiar harms within ten years, isolated from the existential question as the owner asked."},
]
notes = v5['notes'].split(' v5 = ')[0] + " v6 = 17 items: danger d18↔d11, d17↔d19, d12↔d14 (3/3 at 4.0/4.0); speed s15↔s13, s4↔s5, s6↔s11, s8↔s10 (4/4 at 5.0/5.0); profile p2 (horizon), p4 (concentration), p6 (familiar harms). See changelog."
json.dump({'version': 'v6-2026-09-30', 'notes': notes, 'items': en_items, 'changelog': changelog}, open(ROOT + 'propositions.v6.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump({'version': 'v6-fr', 'lang': 'fr', 'items': fr_items}, open(ROOT + 'propositions.v6.fr.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('v6:', len(en_items), 'items')
