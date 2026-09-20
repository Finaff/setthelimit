/* Applies research/audit-v1.patch.json to research/figures-*.json.
   Each change must match the current value ("from") or it is skipped and reported, so a stale patch can't corrupt the data.
   Every applied change is logged in the prediction itself (audit: {from, url}) and in research/audit-applied.md. */
const fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..', 'research');
const patchFile = process.argv[2] || path.join(root, 'audit-v1.patch.json');
const patch = JSON.parse(fs.readFileSync(patchFile, 'utf8'));
const files = fs.readdirSync(root).filter((f) => /^figures-.*\.json$/.test(f));
const docs = files.map((f) => ({ f, j: JSON.parse(fs.readFileSync(path.join(root, f), 'utf8')) }));
const log = []; let applied = 0, skipped = 0;
(patch.changes || []).forEach((c) => {
  const doc = docs.find((d) => d.j.figures.some((x) => x.id === c.figure));
  if (!doc) { log.push(`SKIP ${c.figure}/${c.item}: unknown figure`); skipped++; return; }
  const fig = doc.j.figures.find((x) => x.id === c.figure); const p = fig.predictions[c.item];
  if (!p) { log.push(`SKIP ${c.figure}/${c.item}: unknown item`); skipped++; return; }
  if (typeof c.from === 'number' && p.value !== c.from) { log.push(`SKIP ${c.figure}/${c.item}: value is ${p.value}, patch expected ${c.from}`); skipped++; return; }
  if (typeof c.to !== 'number' || c.to < 0 || c.to > 100 || !/^https?:\/\//.test(c.url || '')) { log.push(`SKIP ${c.figure}/${c.item}: invalid target or missing URL`); skipped++; return; }
  let idx = (fig.sources || []).findIndex((s) => s.url === c.url);
  if (idx === -1) { fig.sources.push({ title: 'Audit source', url: c.url, date: '', note: 'Added by the independent audit.' }); idx = fig.sources.length - 1; }
  log.push(`APPLY ${c.figure}/${c.item}: ${p.value} → ${c.to} (${p.conf} → ${c.conf || p.conf}) ${c.url}`);
  p.audit = { from: (p.audit && typeof p.audit.from === 'number') ? p.audit.from : p.value, url: c.url }; /* keeps the original pre-audit value across successive patches */ p.value = Math.round(c.to); if (c.conf) p.conf = c.conf; if (c.basis) p.basis = String(c.basis).slice(0, 220); if (!p.src.includes(idx)) p.src = [idx].concat(p.src).slice(0, 3);
  applied++;
});
(patch.deadSources || []).forEach((d) => log.push(`DEAD SOURCE ${d.figure}[${d.index}] ${d.url}: ${d.problem}`));
docs.forEach((d) => fs.writeFileSync(path.join(root, d.f), JSON.stringify(d.j, null, 2)));
fs.appendFileSync(path.join(root, 'audit-applied.md'), `\n# ${patch.audit || path.basename(patchFile)} — applied ${new Date().toISOString().slice(0, 10)}\n\n${log.map((l) => '- ' + l).join('\n')}\n`);
console.log(`applied ${applied}, skipped ${skipped}, dead sources ${(patch.deadSources || []).length}`);
