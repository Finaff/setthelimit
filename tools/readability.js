/* Flesch reading ease / Flesch-Kincaid grade for the English propositions (text, plain, steelmen). Heuristic syllables. */
const fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..');
const file = process.argv[2] || fs.readdirSync(path.join(root, 'content')).filter((f) => /^propositions\.v\d+\.json$/.test(f)).sort((a, b) => parseInt(a.match(/\d+/)[0]) - parseInt(b.match(/\d+/)[0])).pop();
const c = JSON.parse(fs.readFileSync(path.join(root, 'content', file), 'utf8'));
function syl(w) { w = w.toLowerCase().replace(/[^a-z]/g, ''); if (!w) return 0; if (w.length <= 3) return 1; w = w.replace(/(?:[^laeiouy]es|ed|[^laeiouy]e)$/, '').replace(/^y/, ''); const m = w.match(/[aeiouy]{1,2}/g); return m ? m.length : 1; }
function stats(t) { const sents = t.split(/[.!?]+(?:\s|$)/).filter((s) => s.trim().length); const words = t.split(/\s+/).filter((w) => /[a-zA-Z]/.test(w)); const s = words.reduce((a, w) => a + syl(w), 0); const W = words.length, S = Math.max(1, sents.length); return { words: W, sents: S, wps: W / S, ease: 206.835 - 1.015 * (W / S) - 84.6 * (s / W), grade: 0.39 * (W / S) + 11.8 * (s / W) - 15.59 }; }
const rows = c.items.map((it) => ({ id: it.id, text: stats(it.text), plain: stats(it.plain), steel: stats(it.for + ' ' + it.against) }));
const f1 = (n) => n.toFixed(1).padStart(5);
console.log(`${file}\nid    text: words grade ease | plain: grade ease | steelmen: grade ease`);
rows.forEach((r) => console.log(`${r.id.padEnd(4)}  ${String(r.text.words).padStart(3)} ${f1(r.text.grade)} ${f1(r.text.ease)} |  ${f1(r.plain.grade)} ${f1(r.plain.ease)} |  ${f1(r.steel.grade)} ${f1(r.steel.ease)}`));
const avg = (k, m) => rows.reduce((a, r) => a + r[k][m], 0) / rows.length;
console.log(`\naverage grade: text ${avg('text', 'grade').toFixed(1)} · plain ${avg('plain', 'grade').toFixed(1)} · steelmen ${avg('steel', 'grade').toFixed(1)}   (US school grade; 8 or lower reads as general public)`);
console.log(`longest proposition: ${Math.max(...rows.map((r) => r.text.words))} words`);
