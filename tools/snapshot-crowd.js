/* Builds site/crowd.js from a folder of exported run documents (JSON files, one per run,
   as written by the artifact read_db tool with out_dir), so the public build carries an
   honest, dated snapshot of the crowd. Usage: node tools/snapshot-crowd.js <dir-with-json> */
const fs = require('fs'), path = require('path');
const dir = process.argv[2];
if (!dir || !fs.existsSync(dir)) { console.error('usage: node tools/snapshot-crowd.js <dir>'); process.exit(1); }
const pts = [];
(function walk(d) { fs.readdirSync(d).forEach((f) => { const p = path.join(d, f); if (fs.statSync(p).isDirectory()) walk(p); else if (f.endsWith('.json')) { try { const j = JSON.parse(fs.readFileSync(p, 'utf8')); const x = j.data ? j.data.x : j.x, y = j.data ? j.data.y : j.y; if (typeof x === 'number' && typeof y === 'number') pts.push([Math.round(x), Math.round(y)]); } catch (e) { /* skip */ } } }); })(dir);
const asOf = new Date().toISOString().slice(0, 10);
fs.writeFileSync(path.join(__dirname, '..', 'site', 'crowd.js'), `/* crowd snapshot generated ${asOf} by tools/snapshot-crowd.js — ${pts.length} anonymous runs */\nwindow.STL_CROWD = ${JSON.stringify({ asOf, n: pts.length, points: pts })};\n`);
console.log('crowd.js:', pts.length, 'points as of', asOf);
