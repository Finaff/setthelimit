/* Validates research/figures-*.json against the current content and prints each figure's
   computed coordinates, so implausible placements are caught before publishing.
   Usage: node tools/check-figures.js [content json] */
const fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..');
const cdir = path.join(root, 'content');
let cfile = process.argv[2];
if (!cfile) { const fl = fs.readdirSync(cdir).filter((f) => /^propositions\.v\d+\.json$/.test(f)).sort((a, b) => Number(a.match(/v(\d+)/)[1]) - Number(b.match(/v(\d+)/)[1])); cfile = path.join(cdir, fl[fl.length - 1]); }
const C = JSON.parse(fs.readFileSync(cfile, 'utf8')); const ITEMS = C.items;
function axis(answers, ax) { let num = 0, den = 0, n = 0; ITEMS.filter((it) => it.axis === ax).forEach((it) => { const v = answers[it.id]; if (typeof v !== 'number') return; num += (it.dir === 1 ? v : 100 - v) * (it.weight || 1); den += it.weight || 1; n++; }); return { v: den ? num / den : null, n }; }
let problems = 0;
fs.readdirSync(path.join(root, 'research')).filter((f) => /^figures-.*\.json$/.test(f)).sort().forEach((f) => {
  const j = JSON.parse(fs.readFileSync(path.join(root, 'research', f), 'utf8'));
  console.log(`\n== ${f}: ${(j.figures || []).length} figures`);
  (j.figures || []).forEach((fig) => {
    const errs = [];
    if (!fig.id || !fig.name) errs.push('missing id/name');
    const preds = fig.predictions || {};
    ITEMS.forEach((it) => { const p = preds[it.id]; if (!p) { errs.push(`no prediction for ${it.id}`); return; } if (typeof p.value !== 'number' || p.value < 0 || p.value > 100) errs.push(`${it.id}: bad value`); if (!['high', 'med', 'low'].includes(p.conf)) errs.push(`${it.id}: bad conf ${p.conf}`); (p.src || []).forEach((i) => { if (!fig.sources || !fig.sources[i]) errs.push(`${it.id}: src index ${i} out of range`); }); });
    /* predictions for ids no longer in the content are kept for the record and ignored */
    (fig.sources || []).forEach((s, i) => { if (!/^https?:\/\//.test(s.url || '')) errs.push(`source ${i} has no URL`); });
    const a = {}; ITEMS.forEach((it) => { if (preds[it.id] && typeof preds[it.id].value === 'number') a[it.id] = preds[it.id].value; });
    const x = axis(a, 'danger'), y = axis(a, 'speed');
    const confs = ITEMS.map((it) => (preds[it.id] || {}).conf); const hi = confs.filter((c) => c === 'high').length, md = confs.filter((c) => c === 'med').length, lo = confs.filter((c) => c === 'low').length;
    console.log(`${(fig.name || '?').padEnd(22)} road ${x.v === null ? ' —' : String(Math.round(x.v)).padStart(3)}  limit ${y.v === null ? ' —' : String(Math.round(y.v)).padStart(3)}  conf h/m/l ${hi}/${md}/${lo}  sources ${(fig.sources || []).length}${errs.length ? '  PROBLEMS: ' + errs.slice(0, 5).join('; ') + (errs.length > 5 ? ` (+${errs.length - 5})` : '') : ''}`);
    problems += errs.length;
  });
});
console.log(problems ? `\n${problems} problem(s)` : '\nno problems');
process.exit(problems ? 1 : 0);
