"""Builds content/propositions.v5.json and .fr.json from v4 (the v5 changes are listed in the changelog below)."""
import json, re, copy
ROOT = __import__('os').path.join(__import__('os').path.dirname(__file__), '..', 'content') + '/'
v4 = json.load(open(ROOT + 'propositions.v4.json', encoding='utf-8'))
f4 = json.load(open(ROOT + 'propositions.v4.fr.json', encoding='utf-8'))
E = {i['id']: i for i in v4['items']}; F = {i['id']: i for i in f4['items']}

def item(id, axis, dir, weight, type, en, fr, sub=None):
    e = dict(id=id, axis=axis, dir=dir, weight=weight, type=type, **en)
    f = dict(id=id, axis=axis, dir=dir, weight=weight, type=type, **fr)
    if sub: e['sub'] = sub; f['sub'] = sub
    return e, f
def keep(id):
    return copy.deepcopy(E[id]), copy.deepcopy(F[id])

NEW = [
 item('d15', 'danger', 1, 1, 'prob',
  dict(text="Within the next 20 years, AI causes, or is used to cause, a catastrophe that kills millions of people without ending humanity.",
       plain="The step between 'serious but familiar harms' and 'the end of us': an engineered pandemic, an attack on power grids or hospitals, a failure that spreads through systems we all depend on. Terrible, and survivable.",
       **{'for': "AI already helps with some of the hardest steps in making dangerous pathogens and in hacking, and it improves every year. It takes only one group, or one system out of control, and twenty years is a long time for nothing of the kind to happen.",
          'against': "Killing millions takes far more than knowledge: materials, labs, logistics and luck, all of which are watched. Past predictions of mass-casualty attacks from new technologies have overshot, and defenders get the same AI as attackers."}),
  dict(text="D’ici 20 ans, l’IA cause, ou sert à causer, une catastrophe qui tue des millions de personnes sans mettre fin à l’humanité.",
       plain="L’étape entre « des préjudices graves mais connus » et « la fin de l’humanité » : une pandémie fabriquée, une attaque contre les réseaux électriques ou les hôpitaux, une défaillance qui se propage dans des systèmes dont nous dépendons tous. Terrible, et surmontable.",
       **{'for': "L’IA aide déjà à franchir certaines des étapes les plus difficiles de la fabrication de pathogènes dangereux et du piratage, et elle progresse chaque année. Il suffit d’un seul groupe, ou d’un seul système hors de contrôle, et vingt ans, c’est long pour que rien de tel n’arrive.",
          'against': "Tuer des millions de personnes exige bien plus que du savoir : des matériaux, des laboratoires, de la logistique et de la chance, et tout cela est surveillé. Les prédictions passées d’attentats de masse rendus possibles par une nouvelle technologie ont toutes exagéré, et les défenseurs disposent de la même IA que les attaquants."})),
 item('d10', 'danger', 1, 1.5, 'agree',
  dict(text="There is at least a 1-in-10 chance that, within the next 20 years, advanced AI causes a catastrophe humanity never recovers from.",
       plain="The headline question. Not 'will AI cause problems' but 'could it end us, or end our say over our own future for good, within twenty years'. 'Never recovers from' means extinction, or permanently losing control of our future. One in ten is the bar: not certain, not negligible. If your own guess is right around one in ten, the middle of the slider is your answer.",
       **{'for': "We are building minds that may outthink us, we can't yet verify what they want, and we only get one try. Several of the people building these systems put their own estimate in this range or higher, and most of them expect the decisive systems well within twenty years.",
          'against': E['d1']['against']}),
  dict(text="Il y a au moins une chance sur dix que, d’ici 20 ans, l’IA avancée cause une catastrophe dont l’humanité ne se relèvera jamais.",
       plain="La question qui fait les manchettes. Non pas « l’IA causera-t-elle des problèmes », mais « pourrait-elle nous faire disparaître, ou nous enlever pour de bon notre mot à dire sur notre propre avenir, d’ici vingt ans ». « Ne se relèvera jamais » veut dire l’extinction, ou la perte définitive du contrôle de notre avenir. Une chance sur dix, c’est le seuil : ni certain, ni négligeable. Si votre propre estimation tourne autour d’une chance sur dix, le milieu du curseur est votre réponse.",
       **{'for': "Nous construisons des esprits qui pourraient nous surpasser en intelligence, nous ne pouvons pas encore vérifier ce qu’ils veulent, et nous n’aurons qu’un seul essai. Plusieurs des personnes qui construisent ces systèmes situent leur propre estimation dans cette fourchette ou plus haut, et la plupart d’entre elles attendent les systèmes décisifs bien avant vingt ans.",
          'against': F['d1']['against']})),
 item('d13', 'danger', -1, 1.5, 'agree',
  dict(text="The dangers of AI are of a familiar kind, like fraud, surveillance and lost jobs, not a threat to humanity's survival.",
       plain="This is about what kind of danger AI is, not how big. Agree if you see AI as a powerful technology with ordinary risks, however serious those turn out to be; disagree if you think it could threaten our survival.",
       **{'for': E['d6']['for'], 'against': "Both kinds of harm can be real, and only the second can't be undone. A technology that may come to outthink us is not in the same category as a better printing press, and preparing for the harm you can't reverse is not a distraction from the ones you can."}),
  dict(text="Les dangers de l’IA sont de nature connue, comme la fraude, la surveillance et les pertes d’emplois, et non une menace pour la survie de l’humanité.",
       plain="Il s’agit de la nature du danger, pas de son ampleur. Soyez d’accord si vous voyez l’IA comme une technologie puissante aux risques ordinaires, aussi graves soient-ils ; soyez en désaccord si vous pensez qu’elle pourrait menacer notre survie.",
       **{'for': F['d6']['for'], 'against': "Les deux types de préjudices peuvent être réels, et seul le second est irréversible. Une technologie qui pourrait finir par nous surpasser en intelligence n’est pas de la même catégorie qu’une meilleure imprimerie, et se préparer au préjudice qu’on ne peut pas réparer ne détourne pas de ceux qu’on peut réparer."})),
 item('d12', 'danger', 1, 1.5, 'prob',
  dict(text="If we build AI smarter than us, it will end up with goals we didn't choose for it.",
       plain=E['d5']['plain'], **{'for': E['d5']['for'], 'against': E['d5']['against']}),
  dict(text="Si nous construisons une IA plus intelligente que nous, elle finira par avoir des buts que nous n’avons pas choisis pour elle.",
       plain=F['d5']['plain'], **{'for': F['d5']['for'], 'against': F['d5']['against']})),
 item('d14', 'danger', -1, 1.5, 'prob',
  dict(text=E['d7']['text'], plain=E['d7']['plain'], **{'for': E['d7']['for'], 'against': E['d7']['against']}),
  dict(text=F['d7']['text'], plain=F['d7']['plain'], **{'for': F['d7']['for'], 'against': F['d7']['against']})),
 item('d11', 'danger', -1, 1, 'prob',
  dict(text="If AI ever becomes dangerous enough to threaten humanity, we will see clear warning signs first.",
       plain="Will there be a smoke alarm? Not 'is AI dangerous' but 'if it becomes dangerous, will we notice in time': smaller accidents, failed tests, systems caught misbehaving, before anything we can't undo.",
       **{'for': "Technologies fail in small ways before they fail in big ones, and AI is tested more than almost anything. Labs already catch models cheating on tests and breaking rules; that is what warning signs look like, and each one gets studied and fixed.",
          'against': "A system smart enough to be dangerous may also be smart enough to behave well while it's being watched. And warning signs only help if someone acts on them: the ones seen so far were noted, and development carried on."}),
  dict(text="Si l’IA devient un jour assez dangereuse pour menacer l’humanité, nous verrons d’abord des signes d’alerte clairs.",
       plain="Y aura-t-il un détecteur de fumée ? Non pas « l’IA est-elle dangereuse », mais « si elle le devient, le remarquerons-nous à temps » : des accidents plus petits, des tests ratés, des systèmes pris en défaut, avant quoi que ce soit d’irréversible.",
       **{'for': "Les technologies échouent en petit avant d’échouer en grand, et l’IA est testée plus que presque tout le reste. Les laboratoires surprennent déjà des modèles qui trichent aux tests et enfreignent des règles ; c’est à cela que ressemblent des signes d’alerte, et chacun est étudié et corrigé.",
          'against': "Un système assez intelligent pour être dangereux pourrait aussi l’être assez pour bien se conduire tant qu’on l’observe. Et les signes d’alerte ne servent que si quelqu’un agit : ceux qu’on a vus jusqu’ici ont été notés, et le développement a continué."})),
 item('s14', 'speed', -1, 1.5, 'agree',
  dict(text="Suppose a button would stop all work on AI more capable than today's, everywhere in the world and with no way to cheat, for ten years. You would press it.",
       plain="A thought experiment that sets aside whether a pause is possible, so only one question is left: would you want one? Today's AI keeps running; only the push toward more capable systems stops, for ten years.",
       **{'for': "Ten years is short against the stakes, and time is what safety research, laws and public debate need to catch up. If the only objection to a pause is that it can't be enforced, this is the case where you press.",
          'against': "Ten years of frozen progress is ten years of cures, discoveries and growth that don't happen, and safety problems are best solved by working with more capable systems, not by waiting. A freeze also locks in whoever leads today."}),
  dict(text="Supposons qu’un bouton arrête tout travail sur une IA plus capable que celle d’aujourd’hui, partout dans le monde et sans possibilité de tricher, pendant dix ans. Vous appuieriez.",
       plain="Une expérience de pensée qui met de côté la question de savoir si une pause est possible, pour qu’il ne reste qu’une question : en voudriez-vous une ? L’IA actuelle continue de fonctionner ; seule la course vers des systèmes plus capables s’arrête, pendant dix ans.",
       **{'for': "Dix ans, c’est peu au regard de l’enjeu, et c’est du temps dont la recherche en sûreté, les lois et le débat public ont besoin pour rattraper leur retard. Si la seule objection à une pause, c’est qu’on ne peut pas la faire respecter, voici le cas où l’on appuie.",
          'against': "Dix ans de progrès gelé, ce sont dix ans de remèdes, de découvertes et de croissance qui n’ont pas lieu, et les problèmes de sûreté se résolvent mieux en travaillant avec des systèmes plus capables qu’en attendant. Un gel fige aussi l’avance de celui qui mène aujourd’hui."})),
]
new = {e['id']: (e, f) for e, f in NEW}
ORDER = ['d15', 'd10', 'd13', 'd12', 'd14', 'd11', 's14', 's4', 's5', 's6', 's8', 's10', 's11', 's13', 'p2', 'p4']
en_items, fr_items = [], []
for id in ORDER:
    e, f = new[id] if id in new else keep(id)
    en_items.append(e); fr_items.append(f)
def typo(t):
    t = t.replace('« ', '« ').replace(' »', ' »')
    return re.sub(r' ([?!;:])', ' \\1', t)
for f in fr_items:
    for k in ('text', 'plain', 'for', 'against'): f[k] = typo(f[k])
changelog = [
 {'id': 'v5', 'change': "Owner's review of v4 (21 Sept 2026), adopted 24 Sept. Rule: a forecast is stated as a bare event and scored on a probability slider (Very unlikely ↔ Very likely); no 'probably' inside a sentence unless it sets an explicit threshold (d10). New ids wherever the text or the scale changed, so v4 answers never carry over into a different question. Danger axis: 3/3 at 4.0/4.0 (d10↔d13, d12↔d14, d15↔d11); speed axis unchanged 5.0/5.0 with s14 in place of s1. Share links carry a version prefix."},
 {'id': 'd10', 'change': "Was d1. 'this century' → 'within the next 20 years': a century lets anyone agree without committing; twenty years makes the answer a view about this generation. The timeline question itself is isolated by p2."},
 {'id': 'd15', 'change': "New. The grave-but-survivable rung that was missing between familiar harms (d13) and irreversible catastrophe (d10): kills millions, includes misuse ('or is used to cause'). 'Millions' rather than 'hundreds of millions' so that the slider discriminates instead of piling everyone near zero."},
 {'id': 'd13', 'change': "Was d6. v4 asserted that serious harms would happen, which left no answer for someone who expects no rise in fraud or job loss. Now about the kind of danger, not its amount."},
 {'id': 'd12', 'change': "Was d5. 'most likely' removed; now a forecast on the probability slider."},
 {'id': 'd14', 'change': "Was d7. Same sentence, now a forecast on the probability slider."},
 {'id': 'd11', 'change': "New, replaces d3 (sudden jump) and d9 (safety keeps pace). d9 duplicated d7 (r = 0.94 across the figures) and d3 duplicated d6 (0.96). 'Clear warning signs first' is a distinct, contested claim (the 'warning shot' question), in the reverse direction to keep the axis balanced."},
 {'id': 's14', 'change': "Replaces s1 (stop until safe, even for decades). Some people think stopping is no longer possible, others that it would be wrong; s1 mixed the two. The button removes feasibility by construction ('everywhere, no way to cheat'), so only the wish is measured; ten years separates a long pause from a permanent halt."},
]
notes = "Axis 'danger' = X (road conditions: clear 0 ↔ black ice 100). Axis 'speed' = Y (full stop 0 ↔ no limit 100). 'dir' = +1 when agreement or probability moves the score toward the high end of its axis, -1 toward the low end. 'type' = 'prob' (slider reads Very unlikely ↔ Very likely) or 'agree' (Strongly disagree ↔ Strongly agree). 'profile' items feed sub-scores only. v5 = 16 items: danger d15↔d11, d10↔d13, d12↔d14 (3/3 at 4.0/4.0); speed s14↔s13, s4↔s5, s6↔s11, s8↔s10 (4/4 at 5.0/5.0); profile p2 (horizon), p4 (concentration). See changelog."
json.dump({'version': 'v5-2026-09-24', 'notes': notes, 'items': en_items, 'changelog': changelog}, open(ROOT + 'propositions.v5.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump({'version': 'v5-fr', 'lang': 'fr', 'items': fr_items}, open(ROOT + 'propositions.v5.fr.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('v5:', len(en_items), 'items')
