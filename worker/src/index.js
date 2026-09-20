/* Set the Limit — API (Cloudflare Worker + D1).
   Endpoints (all JSON unless noted):
     POST   /run               store an anonymous run {x,y,r,v,lang} → {id, token}
     GET    /crowd             {count, at, points:[[x,y],…]} (cached 60 s)
     GET    /claims            {figures:{<figureId>:{handle,name,r,at}}} (cached 60 s)
     GET    /auth/x/start?intent=public|claim   redirect to X (OAuth 2.0 + PKCE)
     GET    /auth/x/callback   exchange the code, set the session cookie, redirect to the site
     POST   /auth/logout
     GET    /me                {handle,name,figure,public}
     POST   /public {id,token} attach my run to my handle · DELETE /public · GET /public/:handle
     POST   /claim {r}         a listed figure replaces the prediction with their answers · DELETE /claim
     GET    /comments?item=d1  comments on a proposition · GET /comments/counts
     POST   /comments {item,parent,body,value}   (signed in) · DELETE /comments/:id (own)
     POST   /comments/:id/vote · POST /comments/:id/flag   (signed in; toggles)
   The static site calls this only when window.STL_API is set. */

const enc = new TextEncoder(), dec = new TextDecoder();
const b64u = (buf) => btoa(String.fromCharCode(...new Uint8Array(buf))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const unb64u = (s) => Uint8Array.from(atob(s.replace(/-/g, '+').replace(/_/g, '/')), (c) => c.charCodeAt(0));
const rid = (n = 12) => b64u(crypto.getRandomValues(new Uint8Array(n)));
const sha = async (s) => b64u(await crypto.subtle.digest('SHA-256', enc.encode(s)));
async function hmac(secret, data) { const k = await crypto.subtle.importKey('raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']); return b64u(await crypto.subtle.sign('HMAC', k, enc.encode(data))); }
async function sign(env, obj) { const body = b64u(enc.encode(JSON.stringify(obj))); return body + '.' + await hmac(env.SESSION_SECRET, body); }
async function verify(env, tok) {
  if (!tok) return null; const [body, sig] = tok.split('.'); if (!body || !sig) return null;
  if (await hmac(env.SESSION_SECRET, body) !== sig) return null;
  try { const o = JSON.parse(dec.decode(unb64u(body))); return o.exp > Date.now() ? o : null; } catch (e) { return null; }
}
const cookies = (req) => Object.fromEntries((req.headers.get('cookie') || '').split(/;\s*/).filter(Boolean).map((c) => { const i = c.indexOf('='); return [c.slice(0, i), decodeURIComponent(c.slice(i + 1))]; }));
const cookie = (name, val, maxAge) => `${name}=${encodeURIComponent(val)}; Max-Age=${maxAge}; Path=/; Secure; HttpOnly; SameSite=Lax`;
const json = (data, status = 200, headers = {}) => new Response(JSON.stringify(data), { status, headers: { 'content-type': 'application/json; charset=utf-8', ...headers } });
const now = () => new Date().toISOString();
const SESSION_DAYS = 30;
const R_OK = /^[0-9a-z_-]{20,80}$/; // the share-link encoding of the answers
const num = (v) => typeof v === 'number' && v >= 0 && v <= 100;
const session = async (req, env) => verify(env, cookies(req).stl_s);
const isMod = (env, uid) => { try { return JSON.parse(env.MODERATORS || '[]').map(String).includes(String(uid)); } catch (e) { return false; } };
// Who has signed in: lets the owner find a numeric id (moderators, figures) without ever trusting a handle.
const remember = (env, s) => env.DB.prepare('INSERT INTO accounts (x_user_id,handle,name,first_at,last_at) VALUES (?,?,?,?,?) ON CONFLICT(x_user_id) DO UPDATE SET handle=excluded.handle, name=excluded.name, last_at=excluded.last_at').bind(String(s.uid), s.handle, s.name || null, now(), now()).run().catch(() => {});
const figureOf = (env, uid) => { try { return JSON.parse(env.FIGURE_ACCOUNTS || '{}')[uid] || null; } catch (e) { return null; } };

function cors(env, req, res) {
  const o = req.headers.get('origin');
  if (o && (o === env.SITE_ORIGIN || (env.DEV === '1' && /^http:\/\/localhost(:\d+)?$/.test(o)))) {
    res.headers.set('access-control-allow-origin', o); res.headers.set('access-control-allow-credentials', 'true');
    res.headers.set('access-control-allow-headers', 'content-type'); res.headers.set('access-control-allow-methods', 'GET,POST,DELETE,OPTIONS'); res.headers.set('vary', 'origin');
  }
  return res;
}

async function postRun(req, env) {
  const b = await req.json().catch(() => null); if (!b || !num(b.x) || !num(b.y) || typeof b.r !== 'string' || !R_OK.test(b.r)) return json({ error: 'bad run' }, 400);
  const ip = req.headers.get('cf-connecting-ip') || ''; const ipHash = await sha(ip + '|' + now().slice(0, 10) + '|' + env.SESSION_SECRET);
  const hour = new Date(Date.now() - 3600e3).toISOString();
  const { c } = await env.DB.prepare('SELECT COUNT(*) AS c FROM runs WHERE ip_hash = ? AND at > ?').bind(ipHash, hour).first();
  if (c >= 30) return json({ error: 'too many runs from this address, try later' }, 429);
  const id = rid(), token = rid(24);
  await env.DB.prepare('INSERT INTO runs (id,x,y,r,v,lang,at,ip_hash,token_hash) VALUES (?,?,?,?,?,?,?,?,?)')
    .bind(id, Math.round(b.x * 10) / 10, Math.round(b.y * 10) / 10, b.r, String(b.v || '').slice(0, 32), String(b.lang || '').slice(0, 5), now(), ipHash, await sha(token)).run();
  return json({ id, token });
}
async function getCrowd(env) {
  const { c } = await env.DB.prepare('SELECT COUNT(*) AS c FROM runs').first();
  const rows = (await env.DB.prepare('SELECT x, y FROM runs ORDER BY at DESC LIMIT 3000').all()).results || [];
  return json({ count: c, at: now(), points: rows.map((r) => [r.x, r.y]) }, 200, { 'cache-control': 'public, max-age=60' });
}
async function getClaims(env) {
  const rows = (await env.DB.prepare('SELECT figure_id, handle, name, r, at FROM claims WHERE revoked = 0').all()).results || [];
  const figures = {}; rows.forEach((r) => { figures[r.figure_id] = { handle: r.handle, name: r.name, r: r.r, at: r.at }; });
  return json({ figures }, 200, { 'cache-control': 'public, max-age=60' });
}

// ---- X sign-in (OAuth 2.0 authorization code + PKCE; the token exchange happens here, never in the browser) ----
async function xStart(url, env) {
  const intent = ['claim', 'public', 'signin'].includes(url.searchParams.get('intent')) ? url.searchParams.get('intent') : 'public';
  const nx = url.searchParams.get('next') || ''; const next = /^#\/[A-Za-z0-9\/_-]{0,40}$/.test(nx) ? nx : '';
  const state = rid(16), verifier = rid(48), challenge = b64u(await crypto.subtle.digest('SHA-256', enc.encode(verifier)));
  const o = await sign(env, { state, verifier, intent, next, exp: Date.now() + 10 * 60e3 });
  const auth = new URL('https://x.com/i/oauth2/authorize');
  Object.entries({ response_type: 'code', client_id: env.X_CLIENT_ID, redirect_uri: env.API_ORIGIN + '/auth/x/callback', scope: 'users.read tweet.read', state, code_challenge: challenge, code_challenge_method: 'S256' }).forEach(([k, v]) => auth.searchParams.set(k, v));
  return new Response(null, { status: 302, headers: { location: auth.toString(), 'set-cookie': cookie('stl_o', o, 600) } });
}
async function xCallback(req, url, env) {
  const o = await verify(env, cookies(req).stl_o); const code = url.searchParams.get('code');
  if (!o || !code || url.searchParams.get('state') !== o.state) return new Response('Sign-in expired or tampered with. Go back and try again.', { status: 400 });
  const tok = await fetch('https://api.x.com/2/oauth2/token', { method: 'POST', headers: { 'content-type': 'application/x-www-form-urlencoded', authorization: 'Basic ' + btoa(env.X_CLIENT_ID + ':' + env.X_CLIENT_SECRET) },
    body: new URLSearchParams({ grant_type: 'authorization_code', code, redirect_uri: env.API_ORIGIN + '/auth/x/callback', code_verifier: o.verifier, client_id: env.X_CLIENT_ID }) }).then((r) => r.json()).catch(() => null);
  if (!tok || !tok.access_token) return new Response('X did not accept the sign-in.', { status: 502 });
  const me = await fetch('https://api.x.com/2/users/me?user.fields=name,username', { headers: { authorization: 'Bearer ' + tok.access_token } }).then((r) => r.json()).catch(() => null);
  const u = me && me.data; if (!u || !u.id) return new Response('Could not read the X account.', { status: 502 });
  const s = await sign(env, { uid: String(u.id), handle: u.username, name: u.name, exp: Date.now() + SESSION_DAYS * 86400e3 });
  await remember(env, { uid: u.id, handle: u.username, name: u.name });
  const headers = new Headers({ location: `${env.SITE_ORIGIN}/?${o.intent}=1${o.next || '#/result'}` });
  headers.append('set-cookie', cookie('stl_s', s, SESSION_DAYS * 86400)); headers.append('set-cookie', cookie('stl_o', '', 0));
  return new Response(null, { status: 302, headers });
}
async function getMe(req, env) {
  const s = await session(req, env); if (!s) return json({ handle: null });
  await remember(env, s);
  const pub = await env.DB.prepare('SELECT handle, at FROM public_results WHERE x_user_id = ?').bind(s.uid).first();
  const figure = figureOf(env, s.uid);
  const claim = figure ? await env.DB.prepare('SELECT at FROM claims WHERE figure_id = ? AND revoked = 0').bind(figure).first() : null;
  return json({ handle: s.handle, name: s.name, mod: isMod(env, s.uid), figure, public: pub ? { handle: pub.handle, at: pub.at } : null, claimed: claim ? claim.at : null }, 200, { 'cache-control': 'no-store' });
}
async function postPublic(req, env) {
  const s = await session(req, env); if (!s) return json({ error: 'sign in first' }, 401);
  const b = await req.json().catch(() => null); if (!b || !b.id || !b.token) return json({ error: 'bad request' }, 400);
  const run = await env.DB.prepare('SELECT id FROM runs WHERE id = ? AND token_hash = ?').bind(String(b.id), await sha(String(b.token))).first();
  if (!run) return json({ error: 'unknown run' }, 404);
  await env.DB.prepare('INSERT INTO public_results (x_user_id,handle,name,run_id,at) VALUES (?,?,?,?,?) ON CONFLICT(x_user_id) DO UPDATE SET handle=excluded.handle, name=excluded.name, run_id=excluded.run_id, at=excluded.at')
    .bind(s.uid, s.handle, s.name, run.id, now()).run();
  return json({ ok: true, handle: s.handle });
}
async function delPublic(req, env) {
  const s = await session(req, env); if (!s) return json({ error: 'sign in first' }, 401);
  await env.DB.prepare('DELETE FROM public_results WHERE x_user_id = ?').bind(s.uid).run(); return json({ ok: true });
}
async function getPublic(handle, env) {
  const row = await env.DB.prepare('SELECT p.handle, p.name, p.at, r.x, r.y, r.r FROM public_results p JOIN runs r ON r.id = p.run_id WHERE lower(p.handle) = lower(?)').bind(handle.replace(/^@/, '')).first();
  return row ? json(row, 200, { 'cache-control': 'public, max-age=60' }) : json({ error: 'no public result for this handle' }, 404);
}
async function postClaim(req, env) {
  const s = await session(req, env); if (!s) return json({ error: 'sign in first' }, 401);
  const figure = figureOf(env, s.uid); if (!figure) return json({ error: 'this X account is not on the list of figures' }, 403);
  const b = await req.json().catch(() => null); if (!b || typeof b.r !== 'string' || !R_OK.test(b.r)) return json({ error: 'bad answers' }, 400);
  await env.DB.prepare('INSERT INTO claims (figure_id,x_user_id,handle,name,r,at,revoked) VALUES (?,?,?,?,?,?,0) ON CONFLICT(figure_id) DO UPDATE SET x_user_id=excluded.x_user_id, handle=excluded.handle, name=excluded.name, r=excluded.r, at=excluded.at, revoked=0')
    .bind(figure, s.uid, s.handle, s.name, b.r, now()).run();
  return json({ ok: true, figure });
}
async function delClaim(req, env) {
  const s = await session(req, env); if (!s) return json({ error: 'sign in first' }, 401);
  await env.DB.prepare('UPDATE claims SET revoked = 1 WHERE x_user_id = ?').bind(s.uid).run(); return json({ ok: true });
}

// ---- comments: signed-in X accounts only; one level of replies; upvotes; spam flags hide a comment once 3 people flag it and flags outnumber upvotes ----
const ITEM_OK = /^[a-z]\d{1,2}$/;
async function getComments(req, url, env) {
  const item = url.searchParams.get('item') || ''; if (!ITEM_OK.test(item)) return json({ error: 'bad item' }, 400);
  const s = await session(req, env); const mod = !!s && isMod(env, s.uid);
  const rows = (await env.DB.prepare(`SELECT c.id, c.parent_id, c.x_user_id, c.handle, c.name, c.body, c.value, c.at, c.deleted,
      (SELECT COUNT(*) FROM comment_votes v WHERE v.comment_id = c.id) AS up,
      (SELECT COUNT(*) FROM comment_flags f WHERE f.comment_id = c.id) AS flags
    FROM comments c WHERE c.item_id = ? ORDER BY c.at ASC LIMIT 500`).bind(item).all()).results || [];
  let myVotes = new Set(), myFlags = new Set();
  if (s) {
    myVotes = new Set(((await env.DB.prepare('SELECT v.comment_id FROM comment_votes v JOIN comments c ON c.id = v.comment_id WHERE v.x_user_id = ? AND c.item_id = ?').bind(s.uid, item).all()).results || []).map((r) => r.comment_id));
    myFlags = new Set(((await env.DB.prepare('SELECT f.comment_id FROM comment_flags f JOIN comments c ON c.id = f.comment_id WHERE f.x_user_id = ? AND c.item_id = ?').bind(s.uid, item).all()).results || []).map((r) => r.comment_id));
  }
  const hasLiveReply = new Set(rows.filter((r) => r.parent_id && !r.deleted).map((r) => r.parent_id));
  const comments = rows.filter((r) => !r.deleted || hasLiveReply.has(r.id)).map((r) => {
    const hidden = !r.deleted && r.flags >= 3 && r.flags > r.up;
    return { id: r.id, parent: r.parent_id || null, handle: r.deleted ? null : r.handle, name: r.deleted ? null : r.name, figure: r.deleted ? null : figureOf(env, r.x_user_id),
      body: r.deleted || (hidden && !mod) ? '' : r.body, value: r.deleted || (hidden && !mod) ? null : r.value, at: r.at, up: r.up, flags: mod ? r.flags : undefined, deleted: !!r.deleted, removed: r.deleted === 2, hidden,
      voted: myVotes.has(r.id), flagged: myFlags.has(r.id), own: !!s && s.uid === r.x_user_id };
  });
  return json({ item, comments, mod }, 200, { 'cache-control': 'no-store' });
}
async function getCommentCounts(env) {
  const rows = (await env.DB.prepare('SELECT item_id, COUNT(*) AS n FROM comments WHERE deleted = 0 GROUP BY item_id').all()).results || [];
  const counts = {}; rows.forEach((r) => { counts[r.item_id] = r.n; });
  return json({ counts }, 200, { 'cache-control': 'public, max-age=60' });
}
async function postComment(req, env) {
  const s = await session(req, env); if (!s) return json({ error: 'sign in first' }, 401);
  const b = await req.json().catch(() => null); const body = b && typeof b.body === 'string' ? b.body.replace(/\r/g, '').replace(/\n{3,}/g, '\n\n').trim() : '';
  if (!b || !ITEM_OK.test(String(b.item || '')) || body.length < 2 || body.length > 1000) return json({ error: 'a comment needs 2 to 1000 characters' }, 400);
  const hour = new Date(Date.now() - 3600e3).toISOString();
  const { c } = await env.DB.prepare('SELECT COUNT(*) AS c FROM comments WHERE x_user_id = ? AND at > ?').bind(s.uid, hour).first();
  if (c >= 10) return json({ error: 'ten comments an hour is the limit; try later' }, 429);
  const dup = await env.DB.prepare('SELECT id FROM comments WHERE x_user_id = ? AND body = ? AND deleted = 0').bind(s.uid, body).first();
  if (dup) return json({ error: 'you already posted this' }, 409);
  let parent = null;
  if (b.parent) { const p = await env.DB.prepare('SELECT id, parent_id, item_id FROM comments WHERE id = ? AND deleted = 0').bind(String(b.parent)).first(); if (!p || p.item_id !== b.item) return json({ error: 'unknown comment to reply to' }, 404); parent = p.parent_id || p.id; }
  const value = Number.isInteger(b.value) && b.value >= 0 && b.value <= 100 ? b.value : null;
  const id = rid();
  await env.DB.prepare('INSERT INTO comments (id,item_id,parent_id,x_user_id,handle,name,body,value,lang,at,deleted) VALUES (?,?,?,?,?,?,?,?,?,?,0)')
    .bind(id, b.item, parent, s.uid, s.handle, s.name, body, value, String(b.lang || '').slice(0, 5), now()).run();
  return json({ ok: true, id });
}
async function toggle(table, req, env, id) {
  const s = await session(req, env); if (!s) return json({ error: 'sign in first' }, 401);
  const c = await env.DB.prepare('SELECT id FROM comments WHERE id = ? AND deleted = 0').bind(id).first(); if (!c) return json({ error: 'unknown comment' }, 404);
  const had = await env.DB.prepare(`SELECT comment_id FROM ${table} WHERE comment_id = ? AND x_user_id = ?`).bind(id, s.uid).first();
  if (had) await env.DB.prepare(`DELETE FROM ${table} WHERE comment_id = ? AND x_user_id = ?`).bind(id, s.uid).run();
  else await env.DB.prepare(`INSERT INTO ${table} (comment_id, x_user_id, at) VALUES (?,?,?)`).bind(id, s.uid, now()).run();
  const { n } = await env.DB.prepare(`SELECT COUNT(*) AS n FROM ${table} WHERE comment_id = ?`).bind(id).first();
  return json({ ok: true, on: !had, count: n });
}
async function clearFlags(req, env, id) {
  const s = await session(req, env); if (!s) return json({ error: 'sign in first' }, 401); if (!isMod(env, s.uid)) return json({ error: 'moderators only' }, 403);
  await env.DB.prepare('DELETE FROM comment_flags WHERE comment_id = ?').bind(id).run(); return json({ ok: true });
}
async function delComment(req, env, id) {
  const s = await session(req, env); if (!s) return json({ error: 'sign in first' }, 401);
  const c = await env.DB.prepare('SELECT x_user_id FROM comments WHERE id = ?').bind(id).first(); if (!c) return json({ error: 'unknown comment' }, 404);
  const mine = c.x_user_id === s.uid; if (!mine && !isMod(env, s.uid)) return json({ error: 'not yours' }, 403);
  await env.DB.prepare('UPDATE comments SET deleted = ? WHERE id = ?').bind(mine ? 1 : 2, id).run(); return json({ ok: true });
}

export default {
  async fetch(req, env) {
    const url = new URL(req.url), p = url.pathname, m = req.method;
    if (m === 'OPTIONS') return cors(env, req, new Response(null, { status: 204 }));
    try {
      let res;
      if (p === '/run' && m === 'POST') res = await postRun(req, env);
      else if (p === '/crowd' && m === 'GET') res = await getCrowd(env);
      else if (p === '/claims' && m === 'GET') res = await getClaims(env);
      else if (p === '/auth/x/start' && m === 'GET') res = await xStart(url, env);
      else if (p === '/auth/x/callback' && m === 'GET') res = await xCallback(req, url, env);
      else if (p === '/auth/logout' && m === 'POST') res = json({ ok: true }, 200, { 'set-cookie': cookie('stl_s', '', 0) });
      else if (p === '/me' && m === 'GET') res = await getMe(req, env);
      else if (p === '/public' && m === 'POST') res = await postPublic(req, env);
      else if (p === '/public' && m === 'DELETE') res = await delPublic(req, env);
      else if (p.startsWith('/public/') && m === 'GET') res = await getPublic(decodeURIComponent(p.slice(8)), env);
      else if (p === '/claim' && m === 'POST') res = await postClaim(req, env);
      else if (p === '/claim' && m === 'DELETE') res = await delClaim(req, env);
      else if (p === '/comments' && m === 'GET') res = await getComments(req, url, env);
      else if (p === '/comments/counts' && m === 'GET') res = await getCommentCounts(env);
      else if (p === '/comments' && m === 'POST') res = await postComment(req, env);
      else if (/^\/comments\/[\w-]+\/vote$/.test(p) && m === 'POST') res = await toggle('comment_votes', req, env, p.split('/')[2]);
      else if (/^\/comments\/[\w-]+\/flag$/.test(p) && m === 'POST') res = await toggle('comment_flags', req, env, p.split('/')[2]);
      else if (/^\/comments\/[\w-]+\/unflag$/.test(p) && m === 'POST') res = await clearFlags(req, env, p.split('/')[2]);
      else if (/^\/comments\/[\w-]+$/.test(p) && m === 'DELETE') res = await delComment(req, env, p.split('/')[2]);
      else res = json({ error: 'not found' }, 404);
      return cors(env, req, res);
    } catch (e) { return cors(env, req, json({ error: String(e && e.message || e) }, 500)); }
  },
};
