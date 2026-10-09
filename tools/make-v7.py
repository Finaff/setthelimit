"""Builds content/propositions.v7.json and .fr.json from v6: three new profile items (p7 power, p8 and p9 brakes), every item tagged with
its node in the disagreement profile (node + ndir), and the questionnaire reordered node by node. Axes and their items are unchanged."""
import json, re, copy, os
ROOT = os.path.join(os.path.dirname(__file__), '..', 'content') + '/'
v6 = json.load(open(ROOT + 'propositions.v6.json', encoding='utf-8'))
f6 = json.load(open(ROOT + 'propositions.v6.fr.json', encoding='utf-8'))
E = {i['id']: i for i in v6['items']}; F = {i['id']: i for i in f6['items']}
def mk(id, en, fr, sub):
    base = dict(id=id, axis='profile', dir=1, weight=1, type='prob', sub=sub)
    return dict(base, **en), dict(base, **fr)
NEW = {
 'p7': mk('p7',
  dict(text="Before 2035, AI will be better than the best human experts at nearly every task that can be done on a computer.",
       plain="Think of writing, analysing, designing, programming, advising: anything done on a screen. Within about ten years, will AI do nearly all of it better than the best people in each field? This is about how powerful AI gets, not whether that is good or dangerous.",
       **{'for': "In five years AI went from finishing sentences to passing professional exams and carrying out long tasks on its own, and the companies building it are spending hundreds of billions on the next steps. Year after year it has done better than the experts predicted.",
          'against': "Passing a test is not doing the job. Today's systems still make basic mistakes and struggle with long, unfamiliar work, and the easy gains from more data and computing power are running out. The best expert in a field is a very high bar."}),
  dict(text="Avant 2035, l’IA sera meilleure que les meilleurs experts humains dans presque toutes les tâches qui se font sur un ordinateur.",
       plain="Pensez à rédiger, analyser, concevoir, programmer, conseiller : tout ce qui se fait devant un écran. D’ici une dizaine d’années, l’IA fera-t-elle presque tout cela mieux que les meilleurs de chaque domaine ? Il s’agit de la puissance de l’IA, pas de savoir si c’est bien ou dangereux.",
       **{'for': "En cinq ans, l’IA est passée de compléter des phrases à réussir des examens professionnels et à mener seule de longues tâches, et les entreprises qui la construisent dépensent des centaines de milliards pour les étapes suivantes. Année après année, elle a fait mieux que ce que prévoyaient les experts.",
          'against': "Réussir un examen, ce n’est pas faire le travail. Les systèmes actuels font encore des erreurs élémentaires et peinent sur les tâches longues et inhabituelles, et les gains faciles tirés de plus de données et de puissance de calcul s’épuisent. Le meilleur expert d’un domaine, c’est une barre très haute."}), 'power'),
 'p8': mk('p8',
  dict(text="If the US, China and the other AI powers decided together to slow down the most powerful AI projects, they could make it stick.",
       plain="Set aside whether they would want to. If they did, could it actually work? Could they check what the others are doing, stop companies and rogue groups from carrying on in secret, and keep the deal from falling apart?",
       **{'for': "The most powerful AI needs huge data centres full of specialised chips made by a handful of companies. Those are hard to hide and easy to count, much like uranium enrichment, and arms-control treaties have held for decades with less to go on.",
          'against': "Computing power gets cheaper every year, better methods let smaller systems do more, and some powerful models are already public. A country could train in secret or quit the deal the moment it fell behind, so a slowdown would bind only the honest."}),
  dict(text="Si les États-Unis, la Chine et les autres puissances de l’IA décidaient ensemble de ralentir les projets d’IA les plus puissants, ils pourraient le faire respecter.",
       plain="Laissez de côté la question de savoir s’ils le voudraient. S’ils le décidaient, cela pourrait-il vraiment fonctionner ? Pourraient-ils vérifier ce que font les autres, empêcher des entreprises ou des groupes hors-la-loi de continuer en secret, et éviter que l’entente s’effondre ?",
       **{'for': "L’IA la plus puissante exige d’immenses centres de données remplis de puces spécialisées fabriquées par une poignée d’entreprises. C’est difficile à cacher et facile à compter, un peu comme l’enrichissement de l’uranium, et des traités de contrôle des armements tiennent depuis des décennies avec moins que cela.",
          'against': "La puissance de calcul coûte moins cher chaque année, de meilleures méthodes permettent à de plus petits systèmes d’en faire davantage, et certains modèles puissants sont déjà publics. Un pays pourrait entraîner ses modèles en secret ou quitter l’entente dès qu’il prendrait du retard : un ralentissement ne lierait que les honnêtes."}), 'feasibility'),
 'p9': mk('p9',
  dict(text="Slowing down the development of more powerful AI would make it substantially safer when it arrives.",
       plain="Does time help? Some say safety work needs time to catch up with what AI can do. Others say we only learn to make AI safe by building it, so waiting changes little. This is about whether slowing down works, not whether it is worth what it costs.",
       **{'for': "Today nobody can reliably check what an advanced AI will do, and safety research, laws and institutions all move more slowly than the technology. Time lets them catch up, and lets warning signs be noticed and acted on.",
          'against': "Safety is learned by working with real systems, the way air travel became safe by flying. A slowdown freezes that learning while computing power and know-how keep piling up, so when building resumes the jump can be bigger and more dangerous."}),
  dict(text="Ralentir le développement d’une IA plus puissante la rendrait nettement plus sûre au moment où elle arrivera.",
       plain="Le temps aide-t-il ? Certains disent que le travail sur la sûreté a besoin de temps pour rattraper ce que l’IA sait faire. D’autres disent qu’on n’apprend à rendre l’IA sûre qu’en la construisant, et qu’attendre ne change pas grand-chose. Il s’agit de savoir si ralentir fonctionne, pas si cela vaut ce que ça coûte.",
       **{'for': "Aujourd’hui, personne ne peut vérifier de façon fiable ce que fera une IA avancée, et la recherche sur la sûreté, les lois et les institutions avancent toutes plus lentement que la technologie. Le temps leur permet de rattraper leur retard, et permet de remarquer les signes d’alerte et d’agir.",
          'against': "La sûreté s’apprend en travaillant avec de vrais systèmes, comme l’aviation est devenue sûre en volant. Un ralentissement gèle cet apprentissage pendant que la puissance de calcul et le savoir-faire continuent de s’accumuler : quand on reprend, le saut peut être plus grand et plus dangereux."}), 'efficacy'),
}
# node and orientation: ndir = +1 when agreeing (or a higher probability) moves the node toward its high pole
NODE = {'p7': ('power', 1), 'p2': ('power', 1),
        'd18': ('control', 1), 'd17': ('control', 1), 'd12': ('control', 1), 'd19': ('control', -1), 'd14': ('control', -1), 'd11': ('control', -1),
        's8': ('threshold', -1), 's10': ('threshold', 1),
        'p8': ('brake', -1), 'p9': ('brake', -1), 's5': ('brake', 1),
        's6': ('wheel', -1), 's4': ('wheel', -1), 's11': ('wheel', 1),
        's15': ('pace', -1), 's13': ('pace', 1)}
ORDER = ['p7', 'p2', 'd18', 'd17', 'd19', 'd12', 'd14', 'd11', 's8', 's10', 'p8', 'p9', 's5', 's6', 's4', 's11', 's15', 's13', 'p4', 'p6']
def typo(t):
    t = t.replace(' ', ' ').replace('« ', '« ').replace(' »', ' »'); return re.sub(r' ([?!;:%])', ' \\1', t)
en_items, fr_items = [], []
for id in ORDER:
    e, f = NEW[id] if id in NEW else (copy.deepcopy(E[id]), copy.deepcopy(F[id]))
    if id in NODE: e['node'], e['ndir'] = NODE[id]; f['node'], f['ndir'] = NODE[id]
    for k in ('text', 'plain', 'for', 'against'): f[k] = typo(f[k])
    en_items.append(e); fr_items.append(f)
changelog = v6.get('changelog', []) + [
 {'id': 'v7', 'change': "Disagreement profile (owner's grid, 9 Oct 2026): every position rests on five questions, Power (how far and how fast AI goes), Control (if it gets there, do we keep it from causing a catastrophe), Threshold (how much risk is acceptable for the benefits), Brakes (would slowing work, and at what cost) and Steering (who should set the pace), plus the conclusion, Speed. Each item carries its node (node, ndir). Three profile items added where the grid was thin: p7 (power), p8 (could a slowdown be made to stick), p9 (would slowing make AI safer). The map's two axes and their items are unchanged. Questionnaire reordered node by node."},
 {'id': 'p7', 'change': 'New, profile (node power).'}, {'id': 'p8', 'change': "New, profile (node brakes, feasibility). Conditional on the powers wanting it, so it measures whether a slowdown can be enforced, not whether it will be chosen. Not the v2–v3 p5, which asked whether an agreed pause 'would actually hold'."},
 {'id': 'p9', 'change': 'New, profile (node brakes, efficacy). Separates "does delay make AI safer" from s8, which values the delay.'},
]
notes = v6['notes'].split(' v6 = ')[0] + " v7 = 20 items. Axes unchanged from v6 (danger 3/3 at 4.0/4.0; speed 4/4 at 5.0/5.0). Profile items: p7 power, p2 horizon, p8 feasibility, p9 efficacy, p4 concentration, p6 familiar harms. Every item has node ∈ {power, control, threshold, brake, wheel, pace} and ndir (±1) for the disagreement profile; p4 and p6 have no node."
json.dump({'version': 'v7-2026-10-09', 'notes': notes, 'items': en_items, 'changelog': changelog}, open(ROOT + 'propositions.v7.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump({'version': 'v7-fr', 'lang': 'fr', 'items': fr_items}, open(ROOT + 'propositions.v7.fr.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('v7:', len(en_items), 'items')
