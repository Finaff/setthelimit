/* Adds ?v=<content hash> to every local script and stylesheet in site/index.html, so a deploy is never hidden by a cached copy.
   Run by tools/release.sh before deploying. */
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const site = path.join(__dirname, '..', 'site'), file = path.join(site, 'index.html');
let html = fs.readFileSync(file, 'utf8'); let n = 0;
html = html.replace(/(<(?:script[^>]*\bsrc|link[^>]*\bhref)=")([^"?:]+\.(?:js|css))(?:\?v=[0-9a-f]+)?(")/g, (m, a, src, b) => {
  const p = path.join(site, src); if (!fs.existsSync(p)) return m;
  n++; return a + src + '?v=' + crypto.createHash('sha1').update(fs.readFileSync(p)).digest('hex').slice(0, 10) + b;
});
fs.writeFileSync(file, html); console.log(`stamped ${n} assets in site/index.html`);
