/* Checks the French edition against the English sources. Run: node tools/check-fr.js
   - site/lang/fr.js: every key of research/ui-strings.en.json present; placeholders kept; HTML tags kept in the
     same order; no value identical to its key except the whitelisted cognates/proper nouns.
   - content/propositions.v2.fr.json: same ids in the same order as v2, scoring fields equal, text <= 30 words.
   - site/lang/context.fr.js (12 facts, non-text fields equal) and site/lang/figures.fr.js (ids = site/figures.js).
   - French typography lint: no straight apostrophes or quotes, no-break space before ; : ? ! % and inside « ». */
const fs = require('fs'), path = require('path'), vm = require('vm');
const root = path.join(__dirname, '..');
const load = (rel) => { const ctx = { window: {} }; vm.createContext(ctx); vm.runInContext(fs.readFileSync(path.join(root, rel), 'utf8'), ctx, { filename: rel }); return ctx.window; };
let fails = 0;
const fail = (m) => { fails++; console.error('FAIL ' + m); };
const NB = '\u00A0';

// Words that are legitimately spelled the same in both languages.
const SAME_OK = new Set(['Autobahn', 'Sources', 'Incident', 'Opinion', 'Discussion']);

// ---- 1. UI strings
const keys = JSON.parse(fs.readFileSync(path.join(root, 'research/ui-strings.en.json'), 'utf8'));
const FR = load('site/lang/fr.js').STL_STRINGS_FR;
if (!FR) fail('STL_STRINGS_FR not defined');
const ph = (s) => (s.match(/\{\w+\}/g) || []).sort().join(' ');
const tags = (s) => (s.match(/<\/?[a-z][^>]*>/gi) || []).join('');
const same = [];
keys.forEach((k) => {
  if (!Object.prototype.hasOwnProperty.call(FR, k)) return fail('missing key: ' + k.slice(0, 60));
  const v = FR[k];
  if (typeof v !== 'string' || !v.trim()) return fail('empty value: ' + k.slice(0, 60));
  if (ph(k) !== ph(v)) fail(`placeholders differ: "${k.slice(0, 50)}" [${ph(k)}] vs [${ph(v)}]`);
  if (tags(k) !== tags(v)) fail(`HTML tags differ: "${k.slice(0, 50)}" ${tags(k)} vs ${tags(v)}`);
  if (/^\s/.test(k) !== /^\s/.test(v) || /\s$/.test(k) !== /\s$/.test(v)) fail('leading/trailing space differs: ' + JSON.stringify(k));
  if (v === k) { same.push(k); if (!SAME_OK.has(k)) fail('value identical to key: ' + k); }
});
const extraKeys = Object.keys(FR).filter((k) => k !== '__meta' && !keys.includes(k));
if (extraKeys.length) fail('keys not in ui-strings.en.json: ' + extraKeys.join(' | '));
if (!FR.__meta || FR.__meta.stamp !== 'septembre 2026') fail('__meta.stamp');
console.log(`fr.js: ${keys.length} keys checked, ${Object.keys(FR).length - 1} present; identical to key (whitelisted): ${same.join(', ')}`);

// ---- 2. propositions
// follow the newest content/propositions.vN.json, like tools/build-content.js
const vers = fs.readdirSync(path.join(root, 'content')).map((f) => (f.match(/^propositions\.v(\d+)\.json$/) || [])[1]).filter(Boolean).map(Number).sort((a, b) => a - b);
const V = vers[vers.length - 1];
const en = JSON.parse(fs.readFileSync(path.join(root, `content/propositions.v${V}.json`), 'utf8'));
const fr = JSON.parse(fs.readFileSync(path.join(root, `content/propositions.v${V}.fr.json`), 'utf8'));
const words = (s) => s.split(/[\s\u00A0]+/).filter((w) => /[\p{L}\p{N}]/u.test(w)).length;
if (fr.version !== `v${V}-fr` || fr.lang !== 'fr') fail('propositions header');
if ('changelog' in fr) fail('changelog should be dropped');
if (en.items.map((i) => i.id).join() !== fr.items.map((i) => i.id).join()) fail('proposition ids differ or are out of order');
let maxW = 0, over25 = [];
fr.items.forEach((it, i) => {
  const e = en.items[i];
  ['id', 'axis', 'dir', 'weight', 'type', 'sub'].forEach((f) => { if (it[f] !== e[f]) fail(`${it.id}.${f} changed`); });
  ['text', 'plain', 'for', 'against'].forEach((f) => { if (typeof it[f] !== 'string' || !it[f].trim()) fail(`${it.id}.${f} empty`); if (it[f] === e[f]) fail(`${it.id}.${f} untranslated`); });
  const w = words(it.text); maxW = Math.max(maxW, w); if (w > 25) over25.push(`${it.id}:${w}`); if (w > 30) fail(`${it.id}.text has ${w} words`);
});
console.log(`propositions.v${V}.fr.json: ${fr.items.length} items, ids in v${V} order; longest text ${maxW} words; over 25: ${over25.join(', ') || 'none'}`);

// ---- 3. context
const CEN = load('site/context.js').STL_CONTEXT, CFR = load('site/lang/context.fr.js').STL_CONTEXT_FR;
if (!CFR || !Array.isArray(CFR.facts)) fail('STL_CONTEXT_FR'); else {
  if (CFR.facts.length !== 12 || CFR.facts.length !== CEN.facts.length) fail('context fact count ' + CFR.facts.length);
  if (CFR.asOf !== '16 septembre 2026') fail('context asOf');
  CFR.facts.forEach((f, i) => { const e = CEN.facts[i]; ['date', 'kind', 'url', 'src'].forEach((k) => { if (f[k] !== e[k]) fail(`context[${i}].${k} changed`); }); if (!f.text || f.text === e.text) fail(`context[${i}].text`); });
  console.log(`context.fr.js: ${CFR.facts.length} facts, asOf "${CFR.asOf}"`);
}

// ---- 4. figures
const FEN = load('site/figures.js').STL_FIGURES, FFR = load('site/lang/figures.fr.js').STL_FIGURES_FR;
if (!FFR) fail('STL_FIGURES_FR'); else {
  const a = FEN.map((f) => f.id), b = Object.keys(FFR);
  if (a.join() !== b.join()) fail('figure ids differ: ' + b.join());
  b.forEach((id) => { const f = FFR[id]; if (Object.keys(f).join() !== 'role,camp,bio,oneLiner') fail(id + ' fields: ' + Object.keys(f)); Object.entries(f).forEach(([k, v]) => { if (typeof v !== 'string' || !v.trim()) fail(`${id}.${k} empty`); }); });
  console.log(`figures.fr.js: ${b.length} ids, matching site/figures.js`);
}

// ---- 5. typography lint over every French string
const all = [];
keys.forEach((k) => all.push(['ui:' + k.slice(0, 30), FR[k] || '']));
fr.items.forEach((it) => ['text', 'plain', 'for', 'against'].forEach((f) => all.push([`${it.id}.${f}`, it[f]])));
(CFR ? CFR.facts : []).forEach((f, i) => all.push([`context[${i}]`, f.text]));
Object.entries(FFR || {}).forEach(([id, f]) => Object.entries(f).forEach(([k, v]) => all.push([`${id}.${k}`, v])));
// English titles quoted inside French text legitimately keep their own punctuation.
const COLON_OK = [/AI 2040: Plan A/, /Situational Awareness: The Decade Ahead/, /Life 3\.0/];
let lint = 0;
all.forEach(([where, s]) => {
  const t = COLON_OK.reduce((x, re) => x.replace(re, ''), s).replace(/<[^>]+>/g, '');
  const bad = [];
  if (/['"]/.test(t)) bad.push('straight quote/apostrophe');
  if (/[^\u00A0\s][;:?!%]/.test(t.replace(/\{\w+\}[:]/g, '')) ) bad.push('missing no-break space before ; : ? ! %');
  if (/ [;:?!%»]/.test(t)) bad.push('plain space before high punctuation');
  if (/«[^\u00A0]/.test(t) || /[^\u00A0]»/.test(t)) bad.push('guillemets without no-break space');
  if ((t.match(/«/g) || []).length !== (t.match(/»/g) || []).length) bad.push('unbalanced guillemets');
  if (/\d,\d{3}\b/.test(t) || /\d\.\d/.test(t)) bad.push('English number format');
  if (bad.length) { lint++; fail(`typography ${where}: ${bad.join('; ')} :: ${s.slice(0, 80)}`); }
});
console.log(`typography: ${all.length} strings linted, ${lint} with problems`);

console.log(fails ? `\n${fails} FAILURE(S)` : '\nALL CHECKS PASSED');
process.exit(fails ? 1 : 0);
