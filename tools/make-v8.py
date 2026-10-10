"""Builds content/propositions.v8.json and .fr.json from v7: the two catastrophe items move to the graded probability scale (type 'plog',
see tools/plog.js) under new ids, d18 → d21 and d17 → d20; d20 becomes the bare event (a 20-year p(doom) at full speed)."""
import json, copy, os, re
ROOT = os.path.join(os.path.dirname(__file__), '..', 'content') + '/'
v7 = json.load(open(ROOT + 'propositions.v7.json', encoding='utf-8')); f7 = json.load(open(ROOT + 'propositions.v7.fr.json', encoding='utf-8'))
SCALE_EN = " Give your best guess as a percentage. The scale is spread out at the low end, where most estimates are: one chance in a thousand, in a hundred, in ten. One in ten sits in the middle."
SCALE_FR = " Donnez votre meilleure estimation en pourcentage. L’échelle est étalée vers le bas, là où se trouvent la plupart des estimations : une chance sur mille, sur cent, sur dix. Une chance sur dix est au milieu."
def conv(items, fr):
    out = []
    for it in items:
        it = copy.deepcopy(it)
        if it['id'] == 'd18':
            it['id'] = 'd21'; it['type'] = 'plog'; it['plain'] += SCALE_FR if fr else SCALE_EN
        elif it['id'] == 'd17':
            it['id'] = 'd20'; it['type'] = 'plog'
            if fr:
                it['text'] = "À pleine vitesse et sans nouvelles limites, l’IA causera, d’ici 20 ans, une catastrophe dont l’humanité ne se relèvera jamais."
                it['plain'] = "Même scénario : personne ne freine l’IA. D’ici 20 ans, l’IA pourrait-elle causer quelque chose dont l’humanité ne se relèverait pas, comme la disparition de tous, ou la perte définitive du contrôle de notre propre avenir ? C’est ce qu’on appelle souvent le « p(doom) »." + SCALE_FR
                it['for'] = it['for'].replace("situent leur propre estimation dans cette fourchette ou plus haut", "situent leur propre estimation à une chance sur dix ou plus haut")
            else:
                it['text'] = "At full speed and with no new limits, AI will cause, within the next 20 years, a catastrophe humanity never recovers from."
                it['plain'] = "Same picture: nobody slows AI down. Within 20 years, could AI cause something humanity never recovers from, such as everyone dying, or people losing control of their own future for good? This is what people often call 'p(doom)'." + SCALE_EN
                it['for'] = it['for'].replace("put their own estimate in this range or higher", "put their own estimate at one in ten or higher")
        out.append(it)
    return out
en = conv(v7['items'], False); fr = conv(f7['items'], True)
def typo(t):
    t = t.replace(' ', ' ').replace('« ', '« ').replace(' »', ' »'); return re.sub(r' ([?!;:%])', ' \\1', t)
for it in fr:
    for k in ('text', 'plain', 'for', 'against'): it[k] = typo(it[k])
assert 'in this range' not in json.dumps(en) and 'cette fourchette' not in json.dumps(fr, ensure_ascii=False)
changelog = v7['changelog'] + [
 {'id': 'v8', 'change': "Owner's request (9 Oct 2026): the headline item is a probability (a 20-year p(doom) at full speed), not agreement with a 1-in-10 threshold. Both catastrophe items move to a graded probability scale (type 'plog', tools/plog.js): the slider shows a percentage, spread by factors of ten at the low end (0.1 %, 1 %, 10 %, 50 %, 99 %), so that one in ten stays mid-scale and the road axis is not squeezed toward 'clear' for people who give 5–30 %."},
 {'id': 'd20', 'change': "Was d17 (agree with 'at least a 1-in-10 chance'); now the bare event on the graded probability scale."},
 {'id': 'd21', 'change': 'Was d18; same sentence, now on the graded probability scale.'},
]
notes = v7['notes'].split(' v7 = ')[0] + " 'plog' = graded probability scale (see tools/plog.js). v8 = v7 with d21/d20 (plog) in place of d18/d17. Axes: danger d21↔d11, d20↔d19, d12↔d14 (3/3 at 4.0/4.0); speed unchanged."
json.dump({'version': 'v8-2026-10-09', 'notes': notes, 'items': en, 'changelog': changelog}, open(ROOT + 'propositions.v8.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump({'version': 'v8-fr', 'lang': 'fr', 'items': fr}, open(ROOT + 'propositions.v8.fr.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('v8:', len(en), 'items')
