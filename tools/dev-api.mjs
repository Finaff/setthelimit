/* Serves worker/src/index.js on http://localhost:8787 with an in-memory SQLite standing in for D1, so the
   site can be tested with http://localhost:8766/?api=http://localhost:8787 . X sign-in is replaced by
   GET /dev/login?uid=1001&handle=GaryMarcus (sets the same session cookie the real callback would). */
import http from 'node:http';
import { DatabaseSync } from 'node:sqlite';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root = path.join(path.dirname(fileURLToPath(import.meta.url)), '..');
const worker = (await import(path.join(root, 'worker/src/index.js'))).default;
const db = new DatabaseSync(':memory:'); db.exec(fs.readFileSync(path.join(root, 'worker/schema.sql'), 'utf8'));
const D1 = { prepare: (sql) => { const st = db.prepare(sql); let args = []; const o = { bind: (...a) => { args = a; return o; }, first: async () => st.get(...args) ?? null, all: async () => ({ results: st.all(...args) }), run: async () => { st.run(...args); return { success: true }; } }; return o; } };
const env = { DB: D1, SITE_ORIGIN: 'http://localhost:8766', API_ORIGIN: 'http://localhost:8787', X_CLIENT_ID: 'dev', X_CLIENT_SECRET: 'dev', SESSION_SECRET: 'dev-secret', FIGURE_ACCOUNTS: JSON.stringify({ '1001': 'gary-marcus' }), DEV: '1' };
const enc = new TextEncoder();
const b64u = (buf) => btoa(String.fromCharCode(...new Uint8Array(buf))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
async function session(uid, handle) { const body = b64u(enc.encode(JSON.stringify({ uid, handle, name: 'Dev ' + handle, exp: Date.now() + 3600e3 }))); const k = await crypto.subtle.importKey('raw', enc.encode(env.SESSION_SECRET), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']); return body + '.' + b64u(await crypto.subtle.sign('HMAC', k, enc.encode(body))); }
http.createServer(async (req, res) => {
  const chunks = []; for await (const c of req) chunks.push(c);
  const url = new URL(req.url, 'http://localhost:8787');
  if (url.pathname === '/dev/login') { const s = await session(url.searchParams.get('uid') || '42', url.searchParams.get('handle') || 'alice'); res.writeHead(302, { location: `${env.SITE_ORIGIN}/?api=http://localhost:8787&${url.searchParams.get('intent') || 'public'}=1#/result`, 'set-cookie': `stl_s=${encodeURIComponent(s)}; Max-Age=3600; Path=/; SameSite=Lax` }); return res.end(); }
  const r = await worker.fetch(new Request(url, { method: req.method, headers: req.headers, body: chunks.length ? Buffer.concat(chunks) : undefined }), env);
  const h = {}; r.headers.forEach((v, k) => { h[k] = v; }); if (h['set-cookie']) h['set-cookie'] = h['set-cookie'].replace(/; Secure/g, ''); /* http on localhost */
  res.writeHead(r.status, h); res.end(Buffer.from(await r.arrayBuffer()));
}).listen(8787, () => console.log('dev API on http://localhost:8787'));
