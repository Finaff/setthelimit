/* Set the Limit — application.
 * One page, hash routes: #/ (landing) · #/q/N · #/result · #/figures · #/figure/ID · #/method.
 * A result link carries all answers in ?r= (2 chars per item, base36; "--" = skipped) so any
 * shared link renders the full result without a backend; ?vs= carries a friend's answers.
 * Optional shared database (claude.use("db")) stores anonymous runs and feeds the crowd layer;
 * otherwise the crowd is a dated snapshot (crowd.js) or absent. Nothing is ever fabricated. */
(function () {
  'use strict';
  function pickLang() {
    const q = new URLSearchParams(location.search).get('lang');
    if (q === 'fr' || q === 'en') { try { localStorage.setItem('stl.lang', q); } catch (e) { /* ignore */ } return q; }
    try { const l = localStorage.getItem('stl.lang'); if (l === 'fr' || l === 'en') return l; } catch (e) { /* ignore */ }
    return (navigator.language || '').toLowerCase().startsWith('fr') && window.STL_STRINGS_FR ? 'fr' : 'en';
  }
  const LANG = pickLang();
  const STR = LANG === 'fr' ? (window.STL_STRINGS_FR || {}) : {};
  const T = (str) => (Object.prototype.hasOwnProperty.call(STR, str) ? STR[str] : str);
  const fmt = (str, vars) => String(str).replace(/\{(\w+)\}/g, (m, k) => (vars && k in vars ? vars[k] : m));
  const C = (LANG === 'fr' && window.STL_CONTENT_FR) ? window.STL_CONTENT_FR : (window.STL_CONTENT || { items: [] });
  const ITEMS = C.items;
  document.documentElement.lang = LANG;
  const FIGS_FR = (LANG === 'fr' && window.STL_FIGURES_FR) || {};
  const FIGS = (window.STL_FIGURES || []).filter((f) => f && f.id && f.predictions).map((f) => Object.assign({}, f, FIGS_FR[f.id] || {}));

  // ---------- optional API (worker/): crowd, X sign-in, public results, claimed dots. Dormant unless window.STL_API is set ----------
  const API = String(window.STL_API || '').replace(/\/$/, '');
  const apiFetch = (p, opts) => fetch(API + p, Object.assign({ credentials: 'include' }, opts || {}));
  const apiJson = (p, opts) => apiFetch(p, opts).then((r) => (r.ok ? r.json() : null)).catch(() => null);
  const apiPost = (p, body, method) => apiJson(p, { method: method || 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body || {}) });
  function loadRun() { try { return JSON.parse(localStorage.getItem('stl.v1.run')) || null; } catch (e) { return null; } }
  function applyClaims(figures) {
    Object.keys(figures || {}).forEach((id) => {
      const f = FIGS.find((x) => x.id === id); const c = figures[id]; const ans = c && dec(c.r); if (!f || !ans) return;
      const predicted = f.predicted || f.predictions; f.predicted = predicted; f.claimed = { handle: c.handle, name: c.name, at: c.at };
      f.predictions = {}; ITEMS.forEach((it) => { const p = predicted[it.id] || {}; f.predictions[it.id] = typeof ans[it.id] === 'number' ? { value: ans[it.id], conf: 'self', basis: '', src: [], predicted: p.value } : { conf: 'self', basis: '', src: [], predicted: p.value }; });
    });
  }
  function rerender() { const pg = parseRoute().page; if (pg === 'result' || pg === 'shared' || pg === 'figures' || pg === 'figure' || pg === 'prop' || pg === 'debate') renderKeep(); }
  async function publishRun() { if (!API || !S.me || !S.run) return; const j = await apiPost('/public', { id: S.run.id, token: S.run.token }); if (j && j.ok) { S.me.public = { handle: j.handle, at: new Date().toISOString() }; S.pendingPublic = false; rerender(); } }
  async function unpublishRun() { const j = await apiPost('/public', {}, 'DELETE'); if (j && j.ok) { S.me.public = null; rerender(); } }
  async function claimDot() { const j = await apiPost('/claim', { r: enc(S.answers) }); if (j && j.ok) { S.me.claimed = new Date().toISOString(); const mine = {}; mine[j.figure] = { handle: S.me.handle, name: S.me.name, r: enc(S.answers), at: S.me.claimed }; applyClaims(mine); /* the cached /claims may lag by a minute */ rerender(); } }
  function publicBlock() {
    if (!API) return '';
    let h = '';
    if (S.me && S.me.figure) { const f = FIGS.find((x) => x.id === S.me.figure); const name = f ? f.name : S.me.figure;
      h += S.me.claimed ? `<p class="prose">${fmt(T('Your answers now stand as {name}’s dot.'), { name: esc(name) })} <a href="#/figure/${esc(S.me.figure)}">${esc(name)}</a></p>` : `<p class="prose">${fmt(T('Signed in as @{handle}. These answers can replace our predictions for {name}, labelled as your own.'), { handle: esc(S.me.handle), name: esc(name) })}</p><p><button class="btn primary" data-claim="1">${T('Replace the predictions with my answers')}</button></p>`; }
    if (S.me && S.me.figure) { /* a listed figure's dot is their public result */ }
    else if (S.me && S.me.public) h += `<p class="prose">${fmt(T('Your result is public as @{handle}.'), { handle: esc(S.me.public.handle) })} <a href="${esc(location.origin + location.pathname)}?u=${esc(S.me.public.handle)}">${esc(location.host + location.pathname)}?u=${esc(S.me.public.handle)}</a> <button class="btn quiet" data-unpublic="1">${T('Remove')}</button></p>`;
    else h += `<p><a class="btn" href="${esc(API)}/auth/x/start?intent=public">${T('Make my result public with X')}</a></p><p class="note">${T('Opt-in only. Your handle is attached to your dot; remove it in one click at any time.')}</p>`;
    return `<h2 class="sec">${T('Put your name on it')}</h2><div class="share">${h}</div>`;
  }
  const CROWD = window.STL_CROWD || { n: 0, points: [], asOf: null };
  const CTX = (LANG === 'fr' && window.STL_CONTEXT_FR) ? window.STL_CONTEXT_FR : (window.STL_CONTEXT || { asOf: '', facts: [] });
  const esc = (s) => String(s == null ? '' : s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const uid = () => Math.random().toString(36).slice(2, 10);
  const SITE = 'Set the Limit';
  const STAMP = (STR.__meta && STR.__meta.stamp) || 'September 2026';
  const AGREE_BAND = 20; // within 20 points = "you agree"

  // ---------- state ----------
  const S = { drafts: {}, comments: {}, counts: null, replyTo: null, keepScroll: null, answers: {}, route: { page: 'home' }, vs: null, shared: null, db: null, liveCrowd: [], sel: null, saved: false };
  function loadAnswers() { try { return JSON.parse(localStorage.getItem('stl.v1.answers')) || {}; } catch (e) { return {}; } }
  function saveAnswers() { try { localStorage.setItem('stl.v1.answers', JSON.stringify(S.answers)); } catch (e) { /* private mode */ } }

  // ---------- encoding ----------
  const enc = (answers) => ITEMS.map((it) => { const v = answers[it.id]; if (v === null) return '--'; if (typeof v !== 'number') return '__'; return v.toString(36).padStart(2, '0'); }).join('');
  function dec(str) {
    if (!str || str.length !== ITEMS.length * 2) return null; /* a link from another item set is ignored, not misread */
    const out = {}; let any = false;
    ITEMS.forEach((it, i) => { const s = str.slice(i * 2, i * 2 + 2); if (s === '--') { out[it.id] = null; any = true; } else if (s !== '__') { const v = parseInt(s, 36); if (!Number.isNaN(v) && v >= 0 && v <= 100) { out[it.id] = v; any = true; } } });
    return any ? out : null;
  }

  // ---------- scoring ----------
  function axisScore(answers, axis) {
    let num = 0, den = 0, n = 0;
    ITEMS.filter((it) => it.axis === axis).forEach((it) => { const v = answers[it.id]; if (typeof v !== 'number') return; const c = it.dir === 1 ? v : 100 - v; const w = it.weight || 1; num += c * w; den += w; n++; });
    return { value: den ? num / den : null, n };
  }
  function subScore(answers, sub) {
    const its = ITEMS.filter((it) => it.axis === 'profile' && it.sub === sub); let num = 0, den = 0;
    its.forEach((it) => { const v = answers[it.id]; if (typeof v !== 'number') return; num += it.dir === 1 ? v : 100 - v; den++; });
    return den ? num / den : null;
  }
  function scores(answers) {
    const x = axisScore(answers, 'danger'), y = axisScore(answers, 'speed');
    const answered = ITEMS.filter((it) => typeof answers[it.id] === 'number').length;
    return { x: x.value, y: y.value, nx: x.n, ny: y.n, answered, ok: x.n >= 3 && y.n >= 3, subs: { horizon: subScore(answers, 'horizon'), concentration: subScore(answers, 'concentration') } };
  }
  const ARCHE = {
    open: { name: 'Autobahn', tag: 'clear road, no limit', blurb: "You don't expect the road to end in a wall, and you'd rather not slow the traffic for a danger you don't see. The strongest form of your view: every technology that made life longer came with the same warnings, and waiting has a body count too." },
    weather: { name: 'Rally Driver', tag: 'ice ahead, still accelerating', blurb: "You take the danger seriously and still think speed is the safer bet: if this is coming anyway, better that the careful get there first. The strongest form of your view: a pause you can't enforce only slows the people who'd honour it." },
    slow: { name: 'School Zone', tag: 'clear road, easy on the gas', blurb: "You don't expect catastrophe, but you'd take it slower anyway: for the jobs, the scams, the power that pools at the top. The strongest form of your view: the harms that are already here deserve the attention the science-fiction ones are getting." },
    brake: { name: 'Road Closed', tag: 'ice ahead, braking hard', blurb: "You see black ice and you want the car slowed or stopped until someone knows how to drive it. The strongest form of your view: you don't run an experiment that could kill everyone before you know how to run it safely." },
    wheel: { name: 'Posted Limit', tag: 'mixed road, steady speed', blurb: "You see real ice and real road ahead, and you'd neither floor it nor stop. The strongest form of your view: most people who are certain, in either direction, are guessing." }
  };
  const MILD = { open: 'clear road, picking up speed', weather: 'ice ahead, not slowing', slow: 'clear road, easing off', brake: 'ice ahead, easing off' };
  const quad = (x, y) => (x < 50 ? (y >= 50 ? 'open' : 'slow') : (y >= 50 ? 'weather' : 'brake'));
  function archetype(x, y) {
    if (x === null || y === null) return null;
    const dist = Math.hypot(x - 50, y - 50);
    if (dist < 14) return { key: 'wheel', name: T(ARCHE.wheel.name), tag: T(ARCHE.wheel.tag), blurb: T(ARCHE.wheel.blurb), near: null };
    const key = quad(x, y); const a = ARCHE[key];
    // près d'un axe : nommer le quadrant voisin, pour ne pas faire dire à 50,8 ce que dit 90
    let other = null;
    if (Math.abs(x - 50) < 5) other = quad(x < 50 ? 60 : 40, y); else if (Math.abs(y - 50) < 5) other = quad(x, y < 50 ? 60 : 40);
    return { key, name: T(a.name), tag: T(dist < 25 ? MILD[key] : a.tag), blurb: T(a.blurb), near: other ? fmt(T('You\u2019re close to the line with {name}.'), { name: T(ARCHE[other].name) }) : null };
  }
  const speedSign = (y) => (y === null ? null : y >= 95 ? { kind: 'nolimit' } : y <= 5 ? { kind: 'stop' } : { kind: 'limit', n: Math.round(y) });
  const condSign = (x) => (x === null ? null : T(x < 20 ? 'Clear road ahead' : x < 40 ? 'Fog possible' : x < 60 ? 'Slippery when wet' : x < 80 ? 'Ice on road' : 'Bridge out ahead'));
  const words = (it, v) => {
    if (v == null) return T('Not sure');
    if (it.type === 'prob') return T(v <= 10 ? 'Very unlikely' : v <= 35 ? 'Unlikely' : v < 50 ? 'Less likely than not' : v === 50 ? 'Coin flip' : v < 65 ? 'More likely than not' : v < 90 ? 'Likely' : 'Very likely');
    return T(v <= 10 ? 'Strongly disagree' : v <= 35 ? 'Disagree' : v < 50 ? 'Lean disagree' : v === 50 ? 'Torn' : v < 65 ? 'Lean agree' : v < 90 ? 'Agree' : 'Strongly agree');
  };

  // ---------- figures ----------
  function figAnswers(f) { const a = {}; ITEMS.forEach((it) => { const p = f.predictions[it.id]; if (p && typeof p.value === 'number') a[it.id] = p.value; }); return a; }
  const figScore = (f) => scores(figAnswers(f));
  function compare(answers, f) {
    const fa = figAnswers(f); let both = 0, agree = 0; const rows = [];
    ITEMS.forEach((it) => { const a = answers[it.id], b = fa[it.id]; if (typeof a !== 'number' || typeof b !== 'number') return; both++; const d = Math.abs(a - b); if (d <= AGREE_BAND) agree++; rows.push({ it, a, b, d }); });
    const sc = figScore(f), me = scores(answers);
    const dist = sc.ok && me.ok ? Math.hypot(sc.x - me.x, sc.y - me.y) : null;
    return { f, both, agree, pct: both ? Math.round((agree / both) * 100) : null, dist, rows: rows.sort((p, q) => q.d - p.d), sc };
  }
  let LABELS = null;
  function figLabel(f) { if (!LABELS) { const seen = {}; FIGS.forEach((x) => { const k = initials(x.name); seen[k] = (seen[k] || 0) + 1; }); LABELS = {}; FIGS.forEach((x) => { const k = initials(x.name); LABELS[x.id] = seen[k] > 1 ? surname(x.name).slice(0, 3).toUpperCase() : k; }); } return LABELS[f.id] || initials(f.name); }
  const surname = (name) => String(name).replace(/\s*\(.*\)\s*/, '').trim().split(/\s+/).slice(-1)[0];
  const byAgreement = (p, q) => (q.pct - p.pct) || (p.dist - q.dist);
  const initials = (name) => name.split(/\s+/).map((w) => w[0]).join('').slice(0, 2).toUpperCase();

  // ---------- routing ----------
  function parseRoute() {
    const h = (location.hash || '#/').replace(/^#\/?/, '');
    const parts = h.split('/').filter(Boolean);
    if (!parts.length) return { page: 'home' };
    if (parts[0] === 'q') return { page: 'q', n: clamp(parseInt(parts[1] || '1', 10) || 1, 1, ITEMS.length) };
    if (parts[0] === 'result') return { page: 'result' };
    if (parts[0] === 'figures') return { page: 'figures' };
    if (parts[0] === 'figure') return { page: 'figure', id: parts[1] };
    if (parts[0] === 'method') return { page: 'method' };
    if (parts[0] === 'context') return { page: 'context' };
    if (parts[0] === 'shared') return { page: 'shared' };
    if (parts[0] === 'debate') return { page: 'debate' };
    if (parts[0] === 'p') return { page: 'prop', id: parts[1] };
    if (parts[0] === 'privacy') return { page: 'privacy' };
    return { page: 'home' };
  }
  const go = (h) => { location.hash = h; };
  const firstUnanswered = () => { const i = ITEMS.findIndex((it) => S.answers[it.id] === undefined); return i === -1 ? null : i + 1; };

  // ---------- rendering ----------
  const root = document.getElementById('stl');
  function shell(inner, opts) {
    const o = opts || {};
    return `<div class="wrap"><header class="top"><a class="mark" href="#/"><i></i>${SITE}</a><span class="spacer"></span><span class="stamp">${fmt(T('As of {stamp}'), { stamp: STAMP })}</span><nav><a href="#/context">${T('Why now')}</a><a href="#/debate">${T('Debate')}</a><a href="#/figures">${T('Figures')}</a><a href="#/method">${T('Method')}</a>${window.STL_STRINGS_FR ? `<a class="lang" href="?lang=${LANG === 'fr' ? 'en' : 'fr'}#/" title="${LANG === 'fr' ? 'English' : 'Français'}">${LANG === 'fr' ? 'EN' : 'FR'}</a>` : ''}</nav></header>${inner}${o.foot === false ? '' : `<p class="foot">${fmt(T('{site} is an independent project. The {n} propositions were written to be fair to both sides and reviewed adversarially; the figures\u2019 positions are predictions from their public statements, with sources, and they can correct them.'), { site: SITE, n: ITEMS.length })} <a href="#/method">${T('How it works')}</a> · <a href="#/privacy">${T('Privacy')}</a> · <a href="https://github.com/Finaff/setthelimit" target="_blank" rel="noopener">GitHub</a></p>`}</div><div id="toastbox"></div>`;
  }
  function render() {
    S.route = parseRoute();
    const r = S.route;
    const fn = { home: viewHome, q: viewQ, result: viewResult, figures: viewFigures, figure: viewFigure, method: viewMethod, shared: viewShared, context: viewContext, debate: viewDebate, prop: viewProp, privacy: viewPrivacy }[r.page] || viewHome;
    document.querySelectorAll('textarea[data-draft]').forEach((t) => { S.drafts[t.dataset.draft] = t.value; });
    root.innerHTML = fn(r);
    document.querySelectorAll('textarea[data-draft]').forEach((t) => { if (S.drafts[t.dataset.draft]) t.value = S.drafts[t.dataset.draft]; });
    if (S.keepScroll !== null && S.keepScroll !== undefined) { window.scrollTo(0, S.keepScroll); S.keepScroll = null; } else window.scrollTo(0, 0);
    if (r.page === 'result') afterResult();
  }
  function viewHome() {
    const names = FIGS.slice(0, 14).map((f) => surname(f.name));
    const list = names.length ? names.slice(0, 4).join(', ') + (names.length > 4 ? fmt(T(' and {n} others'), { n: names.length - 4 }) : '') : T('the people who shape this debate');
    const resume = firstUnanswered();
    const done = ITEMS.filter((it) => S.answers[it.id] !== undefined).length;
    return shell(`<section class="hero">
      <div class="herogrid"><div><h1>${T('How fast should we build AI?')}</h1>
      <p class="lead">${fmt(T('Everyone has a speed limit. Set yours in three minutes, then see where you stand next to {list}, and next to everyone else who took the test.'), { list: esc(list) })}</p>
      <div class="cta"><a class="btn primary big" href="#/q/${resume || 1}">${done ? (resume ? fmt(T('Continue ({done}/{n})'), { done, n: ITEMS.length }) : T('See my result')) : T('Set my limit')}</a><span class="fine">${fmt(T('{n} propositions · no account, no email'), { n: ITEMS.length })}</span></div>
      </div><div class="herosigns" aria-hidden="true"><div class="sign-limit"><div class="cap">${T('Speed<br>limit')}</div><div class="num">?</div></div><div class="sign-diamond"><div class="d"><div class="t">${T('Road<br>conditions<br>?')}</div></div></div></div></div>
      <div class="road"><div class="car" style="left:38%"></div></div>
      <div class="why"><h2>${T('We argue about AI without knowing where we disagree')}</h2><p>${T('One side is told it wants to stop progress; the other, that it is reckless or bought. Most of that is guessing at motives. Underneath, the real disagreement sits in a handful of specific claims: how likely a catastrophe is, whether control will hold, what a delay would cost.')}</p><p>${T('Set the Limit puts those claims on the table one at a time, in words both sides accept. You answer each with a number, and you see exactly where you, your friends and the people shaping this debate part ways, so the argument can happen there.')}</p></div>
      <div class="facts">
        <div><b>${T('Fair to both sides')}</b>${T('Every proposition shows the strongest case for agreeing and for disagreeing, written to satisfy the side it represents.')}</div>
        <div><b>${FIGS.length ? fmt(T('{n} public figures'), { n: FIGS.length }) : T('Public figures')}</b>${T('Their answers are predicted from what they\u2019ve said in public, with sources. If they disagree, they can claim their dot.')}</div>
        <div><b>${T('Your answers stay yours')}</b>${T('They live on this device. Share a link only if you want to; the link carries your answers, not your name.')}</div>
      </div>
      ${CTX.facts.length ? `<div class="whynow"><h2>${T('Why this question, now')}</h2><ul>${CTX.facts.slice(0, 3).map((f) => `<li><span class="d mono">${esc(f.date.slice(0, 7))}</span><span>${esc(f.text)} <a href="${esc(f.url)}" target="_blank" rel="noopener">${esc(f.src)}</a></span></li>`).join('')}</ul><a class="btn quiet sm" href="#/context">${fmt(T('All {n} facts, with sources'), { n: CTX.facts.length })}</a></div>` : ''}
      ${FIGS.length ? `<div class="preview"><h2>${T('On the map')}</h2><div class="figrow">${FIGS.map((f) => `<span><span class="av">${esc(figLabel(f))}</span>${esc(f.name)}</span>`).join('')}</div></div>` : ''}
    </section>`);
  }
  function viewQ(r) {
    const i = r.n - 1, it = ITEMS[i]; if (!it) return viewHome();
    const v = S.answers[it.id];
    const cur = typeof v === 'number' ? v : (v === null ? null : undefined);
    const pct = Math.round((i / ITEMS.length) * 100);
    const fait = it.type === 'prob';
    return shell(`<section>
      <div class="qhead"><span class="mile"><b>${r.n}</b> / ${ITEMS.length}</span><a class="btn quiet sm" href="#/">${T('Save and quit')}</a></div>
      <div class="prog"><i style="width:${pct}%"></i></div>
      <div class="sign-green"><div class="sub"><b>${T(fait ? 'Forecast' : 'Opinion')}</b><span>${T(fait ? 'How likely is this?' : 'How much do you agree?')}</span></div><p class="text">${esc(it.text)}</p></div>
      <div class="plaque"><b>${T('In plain words')}</b>${esc(it.plain)}</div>
      <details class="toggle" ${S.steelOpen ? 'open' : ''}><summary>${T('Why people disagree: the strongest case on each side')}</summary><div class="steel"><div class="agree"><b>${T(fait ? 'Why some say likely' : 'Why some agree')}</b>${esc(it.for)}</div><div class="disagree"><b>${T(fait ? 'Why some say unlikely' : 'Why some disagree')}</b>${esc(it.against)}</div></div></details>
      <div class="answer">
        <div class="val"><span class="n ${cur == null ? 'unset' : ''}" id="val">${cur == null ? '—' : cur}</span><span class="w" id="word">${cur == null ? T(cur === null ? 'Skipped' : 'Slide to answer') : words(it, cur)}</span></div>
        <div class="slider"><input type="range" min="0" max="100" step="1" value="${cur == null ? 50 : cur}" id="slider" aria-label="${T(fait ? 'Probability from 0 to 100' : 'Agreement from 0 to 100')}"><div class="ends"><span>${T(fait ? 'Very unlikely' : 'Strongly disagree')}</span><span>${T(fait ? 'Very likely' : 'Strongly agree')}</span></div></div>
        <div class="row"><button class="btn quiet sm" data-skip="1">${T('Not sure, skip')}</button><span class="spacer"></span>${r.n > 1 ? `<a class="btn sm" href="#/q/${r.n - 1}">${T('Back')}</a>` : ''}<button class="btn primary" data-next="1" id="nextbtn" ${cur === undefined ? 'disabled' : ''}>${T(r.n === ITEMS.length ? 'See my result' : 'Next')}</button></div>
      </div>
      <p class="hint" style="margin-top:10px">${T('Skipping never counts against you. A skipped question just isn\u2019t used in your score.')}</p>
      <p class="hint" id="discuss" ${cur === undefined ? 'hidden' : ''}><a href="#/p/${esc(it.id)}">${T('See where the figures stand on this one, and the discussion')}${S.counts && S.counts[it.id] ? ` (${S.counts[it.id]})` : ''}</a></p>
    </section>`, { foot: false });
  }
  function viewResult() {
    const sc = scores(S.answers);
    if (!sc.ok) { const first = firstUnanswered(); return shell(`<section><h2 class="sec">${T('Not enough answers yet')}</h2><p class="prose">${fmt(T('A result needs at least three answered propositions on each axis. You\u2019ve answered {n}.'), { n: sc.answered })} ${first ? `<a href="#/q/${first}">${fmt(T('Continue from question {n}'), { n: first })}</a>.` : ''}</p></section>`); }
    const ar = archetype(sc.x, sc.y);
    const comps = FIGS.map((f) => compare(S.answers, f)).filter((c) => c.dist !== null).sort(byAgreement);
    const nearest = comps[0], farthest = comps[comps.length - 1];
    const vs = S.vs ? scores(S.vs) : null;
    const link = shareLink(S.answers);
    const crowd = crowdStats(sc);
    let html = `<section>
      <div class="signs">${signHtml(speedSign(sc.y))}<div class="sign-diamond"><div class="d"><div class="t">${esc(condSign(sc.x))}</div></div></div></div>
      <div class="verdict"><div class="arche">${esc(ar.tag)}</div><h1>${esc(ar.name)}</h1><p>${esc(ar.blurb)}${ar.near ? ' ' + esc(ar.near) : ''}</p>
      <p class="note">${fmt(T('Your speed limit is {y} on a scale from 0 (full stop) to 100 (no limit). You rate the road at {x} from 0 (clear) to 100 (black ice).'), { y: `<b class="mono">${Math.round(sc.y)}</b>`, x: `<b class="mono">${Math.round(sc.x)}</b>` })} ${crowd ? crowd.line : ''}</p></div>`;
    if (vs && vs.ok) { const cv = compareAnswers(S.answers, S.vs); html += `<div class="vsbox">${fmt(T('Versus the person who sent you here: you agree on {a} of {b} propositions.'), { a: cv.agree, b: cv.both })} <span class="read">${fmt(T('They set the limit at {y} and rate the road at {x}.'), { y: Math.round(vs.y), x: Math.round(vs.x) })}</span></div>`; }
    html += `<div class="mapwrap">${mapSvg(sc, vs, comps)}<div class="legend"><span><i style="background:var(--green)"></i>${T('You')}</span>${vs && vs.ok ? `<span><i style="background:var(--yellow);outline:1px solid var(--ink)"></i>${T('Them')}</span>` : ''}${FIGS.length ? `<span><i style="background:var(--asphalt-2)"></i>${T('Public figures (predicted, tap one)')}</span>` : ''}${crowd && crowd.n ? `<span><i style="background:var(--blue);opacity:.35"></i>${fmt(T('{n} other people'), { n: crowd.n })}</span>` : ''}</div>${comps.length ? `<div class="figchips">${comps.slice().sort((p, q) => surname(p.f.name).localeCompare(surname(q.f.name))).map((c) => `<button class="${S.sel === c.f.id ? 'on' : ''}" data-fig="${esc(c.f.id)}"><span class="av">${esc(initials(c.f.name))}</span>${esc(surname(c.f.name))}</button>`).join('')}</div>` : ''}<div id="figcard">${S.sel ? figCard(comps.find((c) => c.f.id === S.sel)) : ''}</div></div>`;
    if (comps.length) {
      html += `<h2 class="sec">${T('You agree most with')}<small>${fmt(T('Agreement counts propositions where you\u2019re within {n} points of their predicted answer.'), { n: AGREE_BAND })}</small></h2><ul class="near">${comps.slice(0, 5).map((c) => `<li><button data-fig="${esc(c.f.id)}"><span class="av">${esc(initials(c.f.name))}</span></button><button data-fig="${esc(c.f.id)}"><span class="nm">${esc(c.f.name)}</span><br><span class="cm">${esc(c.f.camp || '')}</span></button><span class="pct">${c.pct}%<small>${c.agree}/${c.both} ${T('agree')}</small></span></li>`).join('')}</ul>`;
      if (farthest && farthest !== nearest) html += `<h2 class="sec">${T('You agree least with')}</h2><ul class="near"><li><button data-fig="${esc(farthest.f.id)}"><span class="av">${esc(initials(farthest.f.name))}</span></button><button data-fig="${esc(farthest.f.id)}"><span class="nm">${esc(farthest.f.name)}</span><br><span class="cm">${esc(farthest.f.camp || '')}</span></button><span class="pct">${farthest.pct}%<small>${farthest.agree}/${farthest.both} ${T('agree')}</small></span></li></ul>`;
      if (nearest) html += `<h2 class="sec">${fmt(T('Where you and {name} split'), { name: esc(surname(nearest.f.name)) })}<small>${T('The three propositions where your closest figure\u2019s predicted answer is furthest from yours.')}</small></h2><ul class="split">${nearest.rows.slice(0, 3).map((r) => `<li><div class="q">${esc(r.it.text)}</div><div class="vals"><span>${T('You')} <b>${r.a}</b></span><span>${esc(surname(nearest.f.name))} <b>${r.b}</b></span><span>${T('gap')} ${r.d}</span></div></li>`).join('')}</ul>`;
    }
    const open = ITEMS.map((it, i) => ({ it, i, v: S.answers[it.id] })).filter((o) => o.v === null || (typeof o.v === 'number' && o.v >= 40 && o.v <= 60));
    if (open.length) html += `<h2 class="sec">${T('Your open questions')}<small>${T('Where you answered near the middle, or skipped. The strongest case on each side is one tap away.')}</small></h2><ul class="openq">${open.slice(0, 6).map((o) => `<li><a href="#/q/${o.i + 1}" data-steel="1"><span class="q">${esc(o.it.text)}</span><span class="v mono">${o.v === null ? T('skipped') : o.v}</span></a></li>`).join('')}</ul>`;
    html += `<h2 class="sec">${T('Your profile')}<small>${T('Beyond the two axes.')}</small></h2><div class="subs">${[['horizon', 'AI does most paid thinking work within 20 years', 'how likely you find it'], ['concentration', 'Who owns it beats what it does', 'concentration as the bigger danger']].map(([k, t, s]) => sc.subs[k] === null ? '' : `<div><div class="v">${Math.round(sc.subs[k])}<small> / 100</small></div><div class="k"><b>${T(t)}</b><br>${T(s)}</div><div class="bar"><i style="width:${Math.round(sc.subs[k])}%"></i></div></div>`).join('')}</div>`;
    html += `<h2 class="sec">${T('Share your sign')}</h2><div class="share"><textarea id="sharetext" readonly>${esc(shareText(sc, ar, nearest))}</textarea><div class="row"><button class="btn primary" data-copylink="1">${T('Copy link')}</button><button class="btn" data-copytext="1">${T('Copy text')}</button>${navigator.share ? `<button class="btn" data-native="1">${T('Share…')}</button>` : ''}<button class="btn" data-card="1">${T('Image card')}</button></div><p class="link">${esc(link)}</p><p class="note">${fmt(T('The link carries your {n} answers and nothing else. Whoever opens it sees your dot and can take the test to compare.'), { n: ITEMS.length })}</p></div>
      <div class="share" style="border-color:var(--line);margin-top:10px"><div class="row" style="margin:0"><a class="btn" href="#/q/1" data-retake="1">${T('Retake')}</a><a class="btn quiet" href="#/figures">${T('All figures and sources')}</a><a class="btn quiet" href="#/method">${T('How the score works')}</a></div></div></section>`;
    html += `<h2 class="sec">${T('Where the debate actually splits')}</h2><p class="prose">${T('Each proposition has its own page: where every public figure stands on it, and a discussion among people who answered it.')}</p><p><a class="btn" href="#/debate">${T('Open the debate')}</a></p>`;
    html += publicBlock();
    return shell(html);
  }
  function compareAnswers(a, b) { let both = 0, agree = 0; ITEMS.forEach((it) => { if (typeof a[it.id] !== 'number' || typeof b[it.id] !== 'number') return; both++; if (Math.abs(a[it.id] - b[it.id]) <= AGREE_BAND) agree++; }); return { both, agree }; }
  function signHtml(s) {
    if (!s) return '';
    if (s.kind === 'stop') return `<div class="sign-stop-wrap"><div class="sign-stop">STOP</div></div>`;
    if (s.kind === 'nolimit') return `<div class="sign-limit"><div class="cap">${T('Speed<br>limit')}</div><div class="num word">${T('NO<br>LIMIT')}</div></div>`;
    return `<div class="sign-limit"><div class="cap">${T('Speed<br>limit')}</div><div class="num">${s.n}</div></div>`;
  }
  function figCard(c) {
    if (!c) return '';
    const f = c.f; const sc = c.sc;
    return `<div class="figcard"><div class="nm">${esc(f.name)}</div><div class="camp">${esc(f.camp || '')}</div>${f.role ? `<div class="role">${esc(f.role)}</div>` : ''}<p>${esc(f.oneLiner || f.bio || '')}</p><div class="stat">${fmt(T('Predicted limit {y} · road {x} · you agree on {a}/{b}'), { y: Math.round(sc.y), x: Math.round(sc.x), a: c.agree, b: c.both })}</div><p><a href="#/figure/${esc(f.id)}">${T('Predictions and sources')}</a></p></div>`;
  }
  function crowdStats(sc) {
    const pts = (S.liveCrowd.length ? S.liveCrowd : CROWD.points) || [];
    if (!pts.length) return null;
    const faster = pts.filter((p) => p[1] < sc.y).length, safer = pts.filter((p) => p[0] < sc.x).length;
    return { n: pts.length, line: fmt(T('You\u2019d drive faster than {f}% of the {n} people who took this{asof}, and you see more danger than {s}% of them.'), { f: Math.round((faster / pts.length) * 100), n: pts.length, asof: CROWD.asOf && !S.liveCrowd.length ? fmt(T(' (as of {d})'), { d: CROWD.asOf }) : '', s: Math.round((safer / pts.length) * 100) }) };
  }
  function mapSvg(sc, vs, comps, lab) {
    lab = lab || { main: T('You'), vs: T('Them') };
    const W = 360, H = 360, L = 30, B = 30, TP = 14, R = 14;
    const X = (v) => L + (v / 100) * (W - L - R), Y = (v) => H - B - (v / 100) * (H - TP - B);
    const pts = (S.liveCrowd.length ? S.liveCrowd : CROWD.points) || [];
    const step = Math.max(1, Math.ceil(pts.length / 400));
    let g = '';
    [25, 50, 75].forEach((t) => { g += `<line class="grid" x1="${X(t)}" y1="${TP}" x2="${X(t)}" y2="${H - B}"/><line class="grid" x1="${L}" y1="${Y(t)}" x2="${W - R}" y2="${Y(t)}"/>`; });
    g += `<line class="axis" x1="${L}" y1="${Y(50)}" x2="${W - R}" y2="${Y(50)}"/><line class="axis" x1="${X(50)}" y1="${TP}" x2="${X(50)}" y2="${H - B}"/>`;
    g += `<text class="qlab" x="${X(25)}" y="${Y(75) + 4}" text-anchor="middle">${T(ARCHE.open.name)}</text><text class="qlab" x="${X(75)}" y="${Y(75) + 4}" text-anchor="middle">${T(ARCHE.weather.name)}</text><text class="qlab" x="${X(25)}" y="${Y(25) + 4}" text-anchor="middle">${T(ARCHE.slow.name)}</text><text class="qlab" x="${X(75)}" y="${Y(25) + 4}" text-anchor="middle">${T(ARCHE.brake.name)}</text>`;
    g += `<text class="alab" x="${(L + W - R) / 2}" y="${H - 6}" text-anchor="middle">${T('← clear road · how dangerous is the road? · black ice →')}</text><text class="alab" transform="translate(9,${(TP + H - B) / 2}) rotate(-90)" text-anchor="middle">${T('← full stop · speed · no limit →')}</text>`;
    for (let i = 0; i < pts.length; i += step) g += `<circle class="crowd" cx="${X(pts[i][0])}" cy="${Y(pts[i][1])}" r="3"/>`;
    const pos = comps.map((c) => ({ c, x: X(c.sc.x), y: Y(c.sc.y), ox: X(c.sc.x), oy: Y(c.sc.y) }));
    for (let it = 0; it < 60; it++) { // relaxation : deux points ne se recouvrent pas (rayon 8), chacun reste près de sa vraie place
      for (let i = 0; i < pos.length; i++) for (let j = i + 1; j < pos.length; j++) { const a = pos[i], b = pos[j]; let dx = b.x - a.x, dy = b.y - a.y; let d = Math.hypot(dx, dy); if (d < 17) { if (d < 0.01) { dx = (i % 2 ? 1 : -1); dy = (j % 2 ? 1 : -1); d = Math.hypot(dx, dy); } const push = (17 - d) / 2; a.x -= (dx / d) * push; a.y -= (dy / d) * push; b.x += (dx / d) * push; b.y += (dy / d) * push; } }
      pos.forEach((q) => { q.x += (q.ox - q.x) * 0.06; q.y += (q.oy - q.y) * 0.06; q.x = clamp(q.x, L + 8, W - R - 8); q.y = clamp(q.y, TP + 8, H - B - 8); });
    }
    const sel = pos.find((q) => q.c.f.id === S.sel);
    pos.forEach((q) => { const c = q.c, sc2 = c.sc; g += `<g class="fig ${S.sel === c.f.id ? 'on' : ''}" data-fig="${esc(c.f.id)}" tabindex="0"><title>${esc(c.f.name)} — ${Math.round(sc2.y)} / ${Math.round(sc2.x)}</title><circle cx="${q.x}" cy="${q.y}" r="8"/><text class="init${figLabel(c.f).length > 2 ? ' l3' : ''}" x="${q.x}" y="${q.y + 2.6}">${esc(figLabel(c.f))}</text></g>`; });
    if (sel) { const right = sel.x < W * 0.6; g += `<text class="figname" x="${sel.x + (right ? 12 : -12)}" y="${sel.y + 3.5}" text-anchor="${right ? 'start' : 'end'}">${esc(sel.c.f.name)}</text>`; }
    if (vs && vs.ok) g += `<g class="vs"><circle cx="${X(vs.x)}" cy="${Y(vs.y)}" r="9"/><text x="${X(vs.x) + 12}" y="${Y(vs.y) + 4}">${esc(lab.vs)}</text></g>`;
    g += `<g class="you"><circle cx="${X(sc.x)}" cy="${Y(sc.y)}" r="10"/><text x="${X(sc.x) + 13}" y="${Y(sc.y) + 4}">${esc(lab.main)}</text></g>`;
    return `<svg class="map" viewBox="0 0 ${W} ${H}" role="img" aria-label="${T('Map of the debate: road danger against speed')}">${g}</svg>`;
  }
  function shareLink(answers) { const u = new URL(location.href); u.hash = '#/shared'; u.search = '?r=' + enc(answers) + (LANG === 'fr' ? '&lang=fr' : ''); return u.toString(); }
  function shareText(sc, ar, nearest) {
    const s = speedSign(sc.y); const lim = s.kind === 'stop' ? T('STOP') : s.kind === 'nolimit' ? T('NO LIMIT') : String(s.n);
    return fmt(T('My AI speed limit: {lim}. Road conditions: {cond}. "{name}".'), { lim, cond: condSign(sc.x), name: ar.name }) + (nearest ? ' ' + fmt(T('Closest public figure: {who} (we agree on {a}/{b}).'), { who: nearest.f.name, a: nearest.agree, b: nearest.both }) : '') + '\n' + fmt(T('How fast should we build AI? Set yours: {link}'), { link: shareLink(S.answers) });
  }
  function viewShared() {
    if (!S.shared) return viewHome();
    const sc = scores(S.shared); const ar = sc.ok ? archetype(sc.x, sc.y) : null;
    const comps = FIGS.map((f) => compare(S.shared, f)).filter((c) => c.dist !== null).sort(byAgreement);
    const mine = scores(S.answers);
    return shell(`<section>
      <div class="signs">${signHtml(speedSign(sc.y))}<div class="sign-diamond"><div class="d"><div class="t">${esc(condSign(sc.x))}</div></div></div></div>
      <div class="verdict"><div class="arche">${S.sharedBy ? fmt(T('@{handle}\u2019s result, made public by them'), { handle: esc(S.sharedBy) }) : T('Someone sent you their result')}</div><h1>${ar ? esc(ar.name) : T('A result')}</h1><p>${fmt(T('They set the limit at {y} and rate the road at {x}.'), { y: Math.round(sc.y), x: Math.round(sc.x) })}${comps[0] ? ' ' + fmt(T('Their closest public figure: {who}.'), { who: esc(comps[0].f.name) }) : ''}</p></div>
      <div class="mapwrap">${mapSvg(sc, mine.ok ? mine : null, comps, { main: S.sharedBy ? '@' + S.sharedBy : T('Them'), vs: T('You') })}<div class="legend"><span><i style="background:var(--green)"></i>${T('Them')}</span>${mine.ok ? `<span><i style="background:var(--yellow);outline:1px solid var(--ink)"></i>${T('You')}</span>` : ''}</div></div>
      <div class="cta" style="margin-top:16px;display:flex;gap:10px;flex-wrap:wrap"><a class="btn primary big" href="${mine.ok ? '#/result' : '#/q/' + (firstUnanswered() || 1)}" data-vs="1">${T(mine.ok ? 'See the full comparison' : 'Take the test to compare')}</a></div>
      <p class="note" style="margin-top:10px">${T(mine.ok ? 'You already have a result; the comparison is on your result page.' : 'Three minutes. Your dot will appear next to theirs, with the propositions you agree and disagree on.')}</p></section>`);
  }
  function viewFigures() {
    if (!FIGS.length) return shell(`<section><h2 class="sec">${T('Public figures')}</h2><div class="empty">${T('The predictions are being compiled with their sources. Check back soon.')}</div></section>`);
    return shell(`<section><h2 class="sec">${T('The people on the map')}<small>${fmt(T('{n} public figures. Their answers are predictions from their public statements, each with a confidence and sources. They are not endorsements, and anyone listed can correct their dot.'), { n: FIGS.length })}</small></h2>
      <ul class="figlist">${FIGS.map((f) => { const sc = figScore(f); const ar = sc.ok ? archetype(sc.x, sc.y) : null; const confs = ITEMS.map((it) => (f.predictions[it.id] || {}).conf); const hi = confs.filter((c) => c === 'high').length, md = confs.filter((c) => c === 'med').length; return `<li><div class="head"><span class="av">${esc(figLabel(f))}</span><span class="nm">${esc(f.name)}</span><span class="role">${f.claimed ? T('answered themselves') + ' · ' : ''}${esc(f.role || '')}</span></div><p>${esc(f.oneLiner || '')}</p><div class="coords">${fmt(T('Predicted limit {y} · road {x}'), { y: sc.ok ? Math.round(sc.y) : '—', x: sc.ok ? Math.round(sc.x) : '—' })}${ar ? ` · ${esc(ar.name)}` : ''} · ${fmt(T('confidence: {h} high, {m} medium, {l} low'), { h: hi, m: md, l: ITEMS.length - hi - md })}</div><p><a href="#/figure/${esc(f.id)}">${fmt(T('All {n} predictions and sources'), { n: ITEMS.length })}</a></p></li>`; }).join('')}</ul>
      <p class="note" style="margin-top:14px">${T('If you are one of these people and a prediction is wrong, the fix is one message away: send your own numbers and we replace the prediction with your answer, labelled as yours.')}</p></section>`);
  }
  function viewFigure(r) {
    const f = FIGS.find((x) => x.id === r.id); if (!f) return viewFigures();
    const sc = figScore(f); const last = esc(surname(f.name));
    const confWord = { high: T('high'), med: T('medium'), low: T('low'), self: T('their answer') };
    return shell(`<section><div class="head" style="display:flex;gap:10px;align-items:center"><span class="av" style="width:36px;height:36px;font-size:14px">${esc(initials(f.name))}</span><div><div class="nm" style="font-weight:900;font-size:22px">${esc(f.name)}</div><div class="role" style="color:var(--ink-3);font-size:13px">${esc(f.role || '')}</div></div></div>
      <p class="prose" style="margin-top:10px">${esc(f.bio || '')}</p>
      <div class="coords mono" style="font-size:13px;color:var(--ink-2)">${fmt(T('Predicted limit {y} · road {x}'), { y: sc.ok ? Math.round(sc.y) : '—', x: sc.ok ? Math.round(sc.x) : '—' })}</div>
      ${f.claimed ? `<p class="prose" style="font-weight:600">${fmt(T('Answered by {name} on {date} (@{handle}). Our predictions are shown beside the answers.'), { name: esc(f.name), date: esc(String(f.claimed.at).slice(0, 10)), handle: esc(f.claimed.handle) })}</p>` : ''}
      <h2 class="sec">${f.claimed ? T('Their answers') : T('Predicted answers')}<small>${f.claimed ? '' : fmt(T('Value · confidence · what it rests on. These are our estimates, not statements by {name}.'), { name: last })}</small></h2>
      <table class="preds">${ITEMS.map((it) => { const p = f.predictions[it.id] || {}; return `<tr><td>${esc(it.text)}<br><span class="b">${p.conf === 'self' && typeof p.predicted === 'number' ? esc(fmt(T('We predicted {p}.'), { p: p.predicted })) : esc(p.basis || '')}${(p.src || []).length ? ' · ' + p.src.map((i) => f.sources && f.sources[i] ? `<a href="${esc(f.sources[i].url)}" target="_blank" rel="noopener">[${i + 1}]</a>` : '').join(' ') : ''}</span></td><td class="v">${typeof p.value === 'number' ? p.value : '—'}<br><span class="conf">${esc(confWord[p.conf] || '')}</span>${p.audit ? `<br><span class="aud">${p.audit.from !== p.value ? fmt(T('corrected by audit · was {n}'), { n: p.audit.from }) : T('basis replaced by audit')}</span>` : ''}</td></tr>`; }).join('')}</table>
      <h2 class="sec">${T('Sources')}</h2><ol class="srcs">${(f.sources || []).map((src) => `<li><a href="${esc(src.url)}" target="_blank" rel="noopener">${esc(src.title)}</a>${src.date ? ` (${esc(src.date)})` : ''}${src.note ? ` — ${esc(src.note)}` : ''}${src.audit ? `<br><span class="aud">${T('Audit note:')} ${esc(src.audit)}</span>` : ''}</li>`).join('')}</ol>
      ${API ? `<p><a class="btn" href="${esc(API)}/auth/x/start?intent=claim">${T('Sign in with X to claim your dot')}</a></p>` : ''}
      <p class="note">${fmt(T('Claim your dot: if you are {name}, send your own {n} numbers and they replace these predictions, labelled as your answers.'), { name: esc(f.name), n: ITEMS.length })}</p>
      <p><a class="btn quiet" href="#/figures">${T('All figures')}</a></p></section>`);
  }
  function viewContext() {
    const kinds = { incident: T('Incident'), letter: T('Open letter'), lab: T('A lab\u2019s own decision'), law: T('Law and policy'), report: T('Report'), poll: T('Public opinion'), experts: T('Expert estimates'), book: T('Book') };
    return shell(`<section><h2 class="sec">${T('Why this question, now')}<small>${fmt(T('What actually happened, as of {date}. Each line links to its primary source. Facts only; the site takes no side on what they mean.'), { date: esc(CTX.asOf) })}</small></h2>
      <ul class="ctx">${CTX.facts.map((f) => `<li><div class="k"><span class="mono">${esc(f.date)}</span><span class="kind">${esc(kinds[f.kind] || f.kind)}</span></div><p>${esc(f.text)}</p><a href="${esc(f.url)}" target="_blank" rel="noopener">${esc(f.src)}</a></li>`).join('')}</ul>
      <div class="prose"><h3>${T('Three kinds of claims')}</h3><p>${T('<b>Facts</b> can be checked: an agent did escape a sandbox in July 2026; California\u2019s law requires transparency, not permission. <b>Values</b> are trade-offs no measurement settles: how much benefit to forgo for how much less risk, and who should decide. <b>Predictions</b> are unknowable now: timelines, probabilities of catastrophe, whether tools to pace development will exist when needed. When a statement sounds decisive, ask which kind it is. The propositions on this site are labelled accordingly.')}</p></div>
      <p style="margin-top:16px"><a class="btn primary" href="#/q/${firstUnanswered() || 1}">${T('Set my limit')}</a></p></section>`);
  }
  function viewMethod() {
    const nD = ITEMS.filter((it) => it.axis === 'danger').length, nS = ITEMS.filter((it) => it.axis === 'speed').length, nP = ITEMS.filter((it) => it.axis === 'profile').length;
    return shell(`<section class="prose"><h2>${T('How it works')}</h2>
      <p>${fmt(T('<b>Two axes, both sides accept.</b> The road-conditions axis asks how dangerous you believe the road is: {nD} propositions about risk and controllability, with beliefs about the world, not policy. The speed axis asks what pace you\u2019d set: {nS} propositions about what should be done. {nP} more feed a profile without moving your position. The rule in one sentence: road-conditions items are beliefs about the risk of catastrophe or loss of control; speed items are what you\u2019d do about it. Keeping the two apart is the point: people who agree about the danger disagree about the speed, and the map shows it.'), { nD, nS, nP })}</p>
      <h3>${T('Why this exists')}</h3><p>${T('In this debate, as in many, people rarely know where they actually disagree. Each side presumes the other\u2019s motives, and the exchange is about those presumptions rather than about claims. This site is built on one bet: if everyone answers the same precise propositions, the points of real disagreement become visible, and they turn out to be fewer and more specific than the noise suggests. Each proposition has a page where you can see who stands where and argue about that claim only.')}</p>
      <h3>${T('Scoring')}</h3><p>${T('Each answer is a number from 0 to 100. For a forecast, it\u2019s how likely you find the statement; for an opinion, how much you agree. Some propositions are phrased so that agreeing means more danger or more speed; others the reverse, in equal numbers and equal weight, so the wording can\u2019t push you. Your axis score is the weighted average of your answers after flipping the reversed ones. Skipped questions are left out; you need at least three answers on each axis to get a result. The speed-limit sign shows your speed score; the diamond shows your road score in five bands.')}</p>
      <h3>${T('Fairness')}</h3><p>${T('Every proposition was written to a rule: one idea, plain words, no adjective that takes a side, and two steelmen, the strongest honest case for agreeing and for disagreeing, each written to satisfy the side it represents. The set was then reviewed adversarially by an editor arguing for the halt-and-pause side and an editor arguing for the build-fast side, and a third for plain English. Items either side called loaded were rewritten or dropped: two that were unfair to the halt side, two that were unfair to the build side. The archetype names were chosen so that people in each quadrant would use them about themselves.')} ${T('A second review then tested every proposition against the sixteen public figures: an item that pushed people the wrong way for a reason unrelated to its axis was reworded. Three were: sceptics of today\u2019s AI were being scored as alarmed, which they are not.')} ${T('Version 4 (19 September 2026) shortened the test from 24 to 16 propositions. Every item that was cut asked, in effect, the same thing as one that stayed (the sixteen figures answered the two within a few points of each other), and five sentences that carried two claims were trimmed to one, so a single slider never has to answer two questions. Each axis is now a set of mirrored pairs: for every statement leaning one way, one leaning the other, at the same weight.')}</p>
      <h3>${T('The public figures')}</h3><p>${T('Their dots are predictions, not statements. For each figure we read their essays, interviews, testimony and posts, then estimated how they\u2019d answer each proposition, with a confidence (high when they\u2019ve said it almost verbatim, medium when it follows clearly from their stated views, low when we inferred it from their general stance) and the sources it rests on. Each figure\u2019s page shows all of it. Anyone listed can replace the predictions with their own answers.')} ${T('An independent audit then checked 180 of the 384 predictions against sources it opened itself: 156 held, 15 numbers or confidence levels were corrected, 9 justifications were replaced, and 11 source notes were annotated. Every correction is visible on the figure\u2019s page.')}</p>
      <h3>${T('Other people')}</h3><p>${fmt(T('When this site can store results, they\u2019re stored anonymously: two numbers and the {n} answers, nothing else. The crowd on the map is either live or a dated snapshot; the count is always shown. No crowd is ever invented.'), { n: ITEMS.length })}</p>
      <h3>${T('Limits')}</h3><p>${T('A compass flattens. Two numbers can\u2019t hold a worldview, the propositions are a sample of a large debate, and the figures\u2019 predictions carry real uncertainty, which is why each one is labelled. Use the result as a starting point for a conversation, not as a verdict.')}</p>
      <h3>${T('Who made this')}</h3><p>${fmt(T('{site} is an independent project, {stamp}. The propositions, the reviews and the predictions are in the open. Corrections are welcome and are applied with a note.'), { site: SITE, stamp: STAMP })} ${fmt(T('Everything is here: {link}.'), { link: '<a href="https://github.com/Finaff/setthelimit" target="_blank" rel="noopener">github.com/Finaff/setthelimit</a>' })}</p></section>`);
  }
  function cardHtml(sc, ar, nearest) {
    const s = speedSign(sc.y);
    return `<div class="cardview" data-closecard="1"><div class="cardin" data-stopcard="1">
      <div class="cardsigns">${signHtml(s)}<div class="sign-diamond"><div class="d"><div class="t">${esc(condSign(sc.x))}</div></div></div></div>
      <div class="cardtxt"><div class="arche">${esc(ar.tag)}</div><div class="cardname">${esc(ar.name)}</div>${nearest ? `<div class="cardnear">${fmt(T('Closest public figure: {who} · agree on {a}/{b}'), { who: esc(nearest.f.name), a: nearest.agree, b: nearest.both })}</div>` : ''}<div class="cardurl">${T('How fast should we build AI?')} · setthelimit.com</div></div>
      <div class="row" style="justify-content:center;gap:8px"><button class="btn sm primary" data-png="1">${T('Save image')}</button><button class="btn sm cardclose" data-closecard="1">${T('Close')}</button></div></div></div>`;
  }
  let toastTimer = null;
  function toast(msg) { const b = document.getElementById('toastbox'); if (!b) return; b.innerHTML = `<div class="toast">${esc(msg)}</div>`; clearTimeout(toastTimer); toastTimer = setTimeout(() => { b.innerHTML = ''; }, 2600); }
  function copy(text, done) { if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, () => fallbackCopy(text, done)); else fallbackCopy(text, done); }
  function fallbackCopy(text, done) { const ta = document.createElement('textarea'); ta.value = text; document.body.appendChild(ta); ta.select(); try { document.execCommand('copy'); } catch (e) { /* ignore */ } ta.remove(); done(); }

  // ---------- after result: store a run (optional db) ----------
  function afterResult() {
    const sc = scores(S.answers); if (!sc.ok) return;
    if (API && !S.apiSaved) { S.apiSaved = true; const prev = loadRun(); const r = enc(S.answers);
      if (prev && prev.r === r) { S.run = prev; if (S.pendingPublic) publishRun(); }
      else apiPost('/run', { x: Math.round(sc.x * 10) / 10, y: Math.round(sc.y * 10) / 10, r, v: C.version || null, lang: LANG }).then((j) => { if (j && j.id) { S.run = { id: j.id, token: j.token, r }; try { localStorage.setItem('stl.v1.run', JSON.stringify(S.run)); } catch (e) { /* ignore */ } if (S.pendingPublic) publishRun(); } else S.apiSaved = false; }); }
    if (!S.db || S.saved) return;
    S.saved = true;
    S.db.doc('runs/' + uid()).set({ x: Math.round(sc.x * 10) / 10, y: Math.round(sc.y * 10) / 10, r: enc(S.answers), at: new Date().toISOString(), v: C.version || null }).catch((e) => { console.warn('db', e); S.saved = false; });
  }


  // ---------- the debate: one page per proposition (figures on a line, discussion), an index, and the privacy page ----------
  const apiTry = (p, body, method) => fetch(API + p, { credentials: 'include', method: method || 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body || {}) }).then((r) => r.json().then((j) => ({ ok: r.ok, j })).catch(() => ({ ok: false, j: {} }))).catch(() => ({ ok: false, j: {} }));
  function renderKeep() { S.keepScroll = window.scrollY; render(); }
  const figVals = (it) => FIGS.map((f) => ({ f, v: (f.predictions[it.id] || {}).value })).filter((x) => typeof x.v === 'number').sort((a, b) => a.v - b.v);
  function spread(it) { const v = figVals(it).map((x) => x.v); if (v.length < 3) return 0; const m = v.reduce((a, b) => a + b, 0) / v.length; return Math.sqrt(v.reduce((a, x) => a + (x - m) * (x - m), 0) / v.length); }
  function miniStrip(it, mine) { const W = 300, X = (v) => 4 + (v / 100) * (W - 8); return `<svg class="mini" viewBox="0 0 ${W} 18" role="img" aria-label="${T('Where the figures stand')}"><line x1="4" y1="9" x2="${W - 4}" y2="9"/>${figVals(it).map((x) => `<circle cx="${X(x.v)}" cy="9" r="3.2"/>`).join('')}${typeof mine === 'number' ? `<rect class="me" x="${X(mine) - 1.5}" y="1" width="3" height="16" rx="1.5"/>` : ''}</svg>`; }
  function strip(it, mine) {
    const W = window.innerWidth < 600 ? 350 : 640, L = 16, X = (v) => L + (v / 100) * (W - 2 * L); const pts = figVals(it); const last = [];
    pts.forEach((pt) => { let r = 0; while (last[r] !== undefined && X(pt.v) - last[r] < 24) r++; last[r] = X(pt.v); pt.row = r; });
    const rows = Math.max(1, last.length), base = 36 + rows * 24, H = base + 30; const fait = it.type === 'prob';
    let g = `<line class="ax" x1="${L}" y1="${base}" x2="${W - L}" y2="${base}"/>`;
    [0, 25, 50, 75, 100].forEach((t) => { g += `<line class="tk" x1="${X(t)}" y1="${base - 4}" x2="${X(t)}" y2="${base + 4}"/><text class="tl" x="${X(t)}" y="${base + 17}" text-anchor="middle">${t}</text>`; });
    g += `<text class="tl" x="${L}" y="${H - 1}">${T(fait ? 'Very unlikely' : 'Strongly disagree')}</text><text class="tl" x="${W - L}" y="${H - 1}" text-anchor="end">${T(fait ? 'Very likely' : 'Strongly agree')}</text>`;
    pts.forEach((pt) => { const y = base - 14 - pt.row * 24; const lb = figLabel(pt.f); g += `<a href="#/figure/${esc(pt.f.id)}"><title>${esc(pt.f.name)} · ${pt.v}${pt.f.claimed ? '' : ' (' + T('predicted') + ')'}</title><circle class="${pt.f.claimed ? 'self' : ''}" cx="${X(pt.v)}" cy="${y}" r="10.5"/><text class="${lb.length > 2 ? 'l3' : ''}" x="${X(pt.v)}" y="${y + 3.2}" text-anchor="middle">${esc(lb)}</text></a>`; });
    if (typeof mine === 'number') g += `<line class="me" x1="${X(mine)}" y1="16" x2="${X(mine)}" y2="${base}"/><text class="met" x="${Math.min(W - 30, Math.max(30, X(mine)))}" y="11" text-anchor="middle">${T('You')} · ${mine}</text>`;
    return `<div class="stripwrap"><svg class="strip" viewBox="0 0 ${W} ${H}" role="img" aria-label="${T('Where the figures stand')}">${g}</svg></div>`;
  }
  function viewDebate() {
    const rows = ITEMS.map((it, i) => ({ it, i, sd: spread(it) })).sort((a, b) => b.sd - a.sd);
    return shell(`<section><h2 class="sec">${T('Where the debate actually splits')}<small>${T('The propositions, ordered by how far apart the public figures are on each. The widest gaps are where the real argument is. Figures’ answers are predictions unless marked as their own.')}</small></h2>
      <ul class="debate">${rows.map((o) => { const mine = S.answers[o.it.id]; const seen = mine !== undefined; const n = S.counts && S.counts[o.it.id]; return `<li><a href="#/p/${esc(o.it.id)}"><span class="dt">${esc(o.it.text)}</span>${seen ? miniStrip(o.it, mine) : `<span class="dlock">${T('Answer it to see where the figures stand')}</span>`}<span class="dm">${fmt(T('Gap between figures: {sd}'), { sd: Math.round(o.sd) })}${n ? ' · ' + fmt(T('{n} comments'), { n }) : ''}</span></a></li>`; }).join('')}</ul></section>`);
  }
  function loadComments(id, force) {
    if (!API) return; const st = S.comments[id] = S.comments[id] || {}; if (st.loading || (st.list && !force)) return; st.loading = true;
    apiJson('/comments?item=' + encodeURIComponent(id)).then((j) => { st.loading = false; st.list = j && j.comments ? j.comments : []; st.failed = !j; const rt = parseRoute(); if (rt.page === 'prop' && rt.id === id) renderKeep(); });
  }
  function commentHtml(c, it, isReply) {
    const when = String(c.at).slice(0, 10); const fig = c.figure ? FIGS.find((f) => f.id === c.figure) : null;
    if (c.deleted) return `<div class="cm gone${isReply ? ' reply' : ''}"><div class="cmb">${T('Deleted by its author.')}</div></div>`;
    if (c.hidden) return `<div class="cm gone${isReply ? ' reply' : ''}"><div class="cmb">${T('Hidden: several people flagged this as spam.')}</div></div>`;
    return `<div class="cm${isReply ? ' reply' : ''}"><div class="cmh"><a href="https://x.com/${esc(c.handle)}" target="_blank" rel="noopener nofollow">@${esc(c.handle)}</a>${fig ? `<span class="badge">${esc(fig.name)} · ${T('verified')}</span>` : ''}${typeof c.value === 'number' ? `<span class="ans">${fmt(T('answered {v}'), { v: c.value })}</span>` : ''}<span class="when">${esc(when)}</span></div>
      <div class="cmb">${esc(c.body).replace(/\n/g, '<br>')}</div>
      <div class="cma"><button class="${c.voted ? 'on' : ''}" data-vote="${esc(c.id)}" aria-pressed="${c.voted ? 'true' : 'false'}" title="${T('Upvote')}">▲ ${c.up || 0}</button><button data-reply="${esc(c.id)}">${T('Reply')}</button>${c.own ? `<button data-delc="${esc(c.id)}">${T('Delete')}</button>` : `<button class="${c.flagged ? 'on' : ''}" data-flag="${esc(c.id)}">${c.flagged ? T('Flagged as spam') : T('Spam?')}</button>`}</div>
      ${S.replyTo === c.id && S.me ? `<div class="compose"><textarea data-draft="r:${esc(c.id)}" maxlength="1000" rows="3" placeholder="${T('Reply to the claim, not the person.')}"></textarea><div class="row"><button class="btn sm primary" data-postreply="${esc(c.id)}">${T('Post reply')}</button></div></div>` : ''}</div>`;
  }
  function commentsHtml(it, mine) {
    if (!API) return `<h2 class="sec">${T('Discussion')}</h2><p class="note">${T('The discussion lives on the main site:')} <a href="https://setthelimit.com/#/p/${esc(it.id)}" target="_blank" rel="noopener">setthelimit.com</a></p>`;
    const st = S.comments[it.id] || {}; const list = st.list || []; const live = list.filter((c) => !c.deleted && !c.hidden).length;
    const roots = list.filter((c) => !c.parent).sort((a, b) => (b.up - a.up) || (a.at < b.at ? -1 : 1));
    const next = encodeURIComponent('#/p/' + it.id);
    const compose = S.me ? `<div class="compose"><textarea data-draft="c:${esc(it.id)}" maxlength="1000" rows="4" placeholder="${T('What would change your answer? Argue the claim, not the person.')}"></textarea><div class="row">${typeof mine === 'number' ? `<label class="chk"><input type="checkbox" id="showval" checked> ${fmt(T('Show my answer ({v}) next to my comment'), { v: mine })}</label>` : ''}<span class="spacer"></span><span class="hint">@${esc(S.me.handle)}</span><button class="btn sm primary" data-post="${esc(it.id)}">${T('Post')}</button></div></div>`
      : `<p><a class="btn" href="${esc(API)}/auth/x/start?intent=signin&next=${next}">${T('Sign in with X to comment')}</a></p><p class="note">${T('X sign-in keeps the bots out. We never post for you and never read your posts.')}</p>`;
    return `<h2 class="sec">${T('Discussion')}${live ? ` <small style="display:inline">(${live})</small>` : ''}</h2>${compose}
      ${st.loading && !st.list ? `<p class="hint">${T('Loading…')}</p>` : ''}${st.list && !roots.length ? `<p class="hint">${T('No comments yet. The first one sets the tone.')}</p>` : ''}
      <div class="cms">${roots.map((c) => commentHtml(c, it, false) + list.filter((x) => x.parent === c.id).map((x) => commentHtml(x, it, true)).join('')).join('')}</div>`;
  }
  function viewProp(r) {
    const it = ITEMS.find((x) => x.id === r.id); if (!it) return viewDebate();
    const n = ITEMS.indexOf(it) + 1, mine = S.answers[it.id], fait = it.type === 'prob';
    const head = `<p class="crumbs"><a href="#/debate">${T('All propositions')}</a> · ${n} / ${ITEMS.length}</p><div class="sign-green"><div class="sub"><b>${T(fait ? 'Forecast' : 'Opinion')}</b></div><p class="text">${esc(it.text)}</p></div><div class="plaque"><b>${T('In plain words')}</b>${esc(it.plain)}</div>`;
    if (mine === undefined) return shell(`<section>${head}<div class="gate"><p class="prose">${T('The figures’ answers and the discussion stay hidden until you’ve set your own slider, so that nobody anchors you.')}</p><p><a class="btn primary" href="#/q/${n}">${T('Answer this one first')}</a></p></div></section>`);
    loadComments(it.id);
    return shell(`<section>${head}
      <div class="steel"><div class="agree"><b>${T(fait ? 'Why some say likely' : 'Why some agree')}</b>${esc(it.for)}</div><div class="disagree"><b>${T(fait ? 'Why some say unlikely' : 'Why some disagree')}</b>${esc(it.against)}</div></div>
      <h2 class="sec">${T('Where the figures stand')}<small>${T('Each dot is a public figure’s answer to this proposition: predicted from their public statements unless they answered themselves. Tap one for its basis and sources.')}</small></h2>
      ${strip(it, mine)}
      <p class="hint">${mine === null ? T('You skipped this one.') : ''} <a href="#/q/${n}">${T('Change my answer')}</a></p>
      ${commentsHtml(it, mine)}
      <p style="margin-top:18px">${n > 1 ? `<a class="btn sm" href="#/p/${esc(ITEMS[n - 2].id)}">${T('Back')}</a> ` : ''}${n < ITEMS.length ? `<a class="btn sm" href="#/p/${esc(ITEMS[n].id)}">${T('Next')}</a>` : ''}</p></section>`);
  }
  async function postComment(itemId, parent) {
    const key = parent ? 'r:' + parent : 'c:' + itemId; const ta = document.querySelector(`textarea[data-draft="${key}"]`); const body = ta ? ta.value.trim() : '';
    if (body.length < 2) { toast(T('Write something first.')); return; }
    const sv = document.getElementById('showval'); const mine = S.answers[itemId];
    const value = typeof mine === 'number' && (parent || !sv || sv.checked) ? mine : null;
    const res = await apiTry('/comments', { item: itemId, parent: parent || null, body, value, lang: LANG });
    if (!res.ok) { toast(res.j && res.j.error ? String(res.j.error) : T('That did not go through. Try again.')); return; }
    S.drafts[key] = ''; if (ta) ta.value = ''; S.replyTo = null; if (S.counts) S.counts[itemId] = (S.counts[itemId] || 0) + 1; loadComments(itemId, true);
  }
  async function commentAction(kind, id) {
    const rt = parseRoute(); if (rt.page !== 'prop') return;
    if (!S.me) { toast(T('Sign in with X first.')); return; }
    const res = kind === 'del' ? await apiTry('/comments/' + id, {}, 'DELETE') : await apiTry('/comments/' + id + '/' + kind, {});
    if (!res.ok) { toast(res.j && res.j.error ? String(res.j.error) : T('That did not go through. Try again.')); return; }
    loadComments(rt.id, true);
  }
  function viewPrivacy() {
    const P = (h, t) => `<h3>${T(h)}</h3><p>${T(t)}</p>`;
    return shell(`<section><h2 class="sec">${T('Privacy')}<small>${T('Last updated 20 September 2026. Short, and meant to be read.')}</small></h2><div class="prose">
      ${P('If you just take the test', 'Your answers are kept in your browser’s storage on your device. When you reach your result, we store an anonymous copy: your two scores, your answers, the language, and the time. No name, no email, no account, no cookie. To limit abuse we keep a one-way hash of your network address that changes every day and cannot be turned back into the address. These anonymous runs feed the crowd on the map.')}
      ${P('If you share a link', 'A share link carries your answers inside the link itself. Whoever has the link can see those answers; nothing else about you is in it.')}
      ${P('If you sign in with X', 'Signing in is optional and only proves which X account is yours. X sends us your account’s numeric id, your handle and your display name. We never see your password, we cannot post, like or follow for you, and we do not read your posts, followers or messages. The access token X gives us is used once to read those three fields and is then discarded. We set one cookie to keep you signed in for 30 days; it is not readable by scripts and is not used for tracking.')}
      ${P('What becomes public, and only if you choose it', 'If you make your result public, your handle and your answers are shown to anyone with your link. If you comment, your handle, your comment, its date and, if you tick the box, your answer to that proposition are public. A listed public figure who claims their dot makes their answers public under their name. You can remove your public result in one click and delete your own comments at any time.')}
      ${P('What we do not do', 'No advertising, no analytics trackers, no sale or sharing of data, no profiling, no training of AI models on your data.')}
      ${P('Who processes the data', 'The site and its database run on Cloudflare, which processes network addresses to deliver pages and keep the service secure. Fonts are loaded from Google Fonts, which sees your network address when your browser fetches them. The code that handles all of this is public.')}
      ${P('Your rights', 'You can ask for a copy of what we hold about your X account, or for its deletion, by opening an issue on the public repository or writing to the address listed there. Anonymous runs cannot be traced back to you, so they cannot be looked up or deleted individually.')}
      <p><a href="https://github.com/Finaff/setthelimit" target="_blank" rel="noopener">github.com/Finaff/setthelimit</a></p></div></section>`);
  }

  // ---------- PNG card: the sign, the diamond, the archetype and the map, drawn on a canvas for saving or sharing ----------
  function rr(g, x, y, w, h, r) { g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r); g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath(); }
  function wrapText(g, text, x, y, maxW, lh, align) { g.textAlign = align || 'left'; const words = String(text).split(/\s+/); let line = '', n = 0; words.forEach((w) => { const t = line ? line + ' ' + w : w; if (g.measureText(t).width > maxW && line) { g.fillText(line, x, y + n * lh); line = w; n++; } else line = t; }); if (line) g.fillText(line, x, y + n * lh); return n + 1; }
  async function cardPng(sc, ar, nearest) {
    const W = 1080, H = 1350; const cv = document.createElement('canvas'); cv.width = W; cv.height = H; const g = cv.getContext('2d');
    const SANS = 'Overpass, "Helvetica Neue", Arial, sans-serif', SERIF = 'Literata, Georgia, serif';
    try { if (document.fonts && document.fonts.load) await Promise.all([`900 100px ${SANS}`, `800 40px ${SANS}`, `700 40px ${SANS}`, `400 40px ${SERIF}`].map((f) => document.fonts.load(f))); } catch (e) { /* system fonts */ }
    g.fillStyle = '#2B2E31'; g.fillRect(0, 0, W, H);
    g.fillStyle = '#F2C94C'; for (let x = 0; x < W; x += 66) g.fillRect(x, H - 40, 38, 8);
    g.fillStyle = '#FFFFFF'; g.font = `800 34px ${SANS}`; g.textAlign = 'center'; g.textBaseline = 'alphabetic'; g.fillText('SET THE LIMIT', W / 2, 92);
    g.fillStyle = '#B4BAB2'; g.font = `400 30px ${SERIF}`; g.fillText(T('How fast should we build AI?'), W / 2, 136);
    // speed-limit sign (left)
    const s = speedSign(sc.y); const sx = 120, sy = 200, sw = 380, sh = 470;
    if (s.kind === 'stop') { const cx = sx + sw / 2, cy = sy + sh / 2, r = 215; const oct = (rad, fill) => { g.beginPath(); for (let i = 0; i < 8; i++) { const a = Math.PI / 8 + i * Math.PI / 4; g.lineTo(cx + rad * Math.cos(a), cy + rad * Math.sin(a)); } g.closePath(); g.fillStyle = fill; g.fill(); }; oct(r, '#FFFFFF'); oct(r - 14, '#C6281E'); g.fillStyle = '#FFFFFF'; g.font = `900 120px ${SANS}`; g.textAlign = 'center'; g.fillText('STOP', cx, cy + 42); }
    else {
      rr(g, sx - 10, sy - 10, sw + 20, sh + 20, 34); g.fillStyle = '#FFFFFF'; g.fill(); rr(g, sx, sy, sw, sh, 26); g.fillStyle = '#FFFFFF'; g.fill(); g.lineWidth = 12; g.strokeStyle = '#1B1E21'; g.stroke();
      g.fillStyle = '#1B1E21'; g.font = `800 40px ${SANS}`; g.textAlign = 'center'; const cap = T('Speed<br>limit').split('<br>'); g.fillText(cap[0].toUpperCase(), sx + sw / 2, sy + 86); if (cap[1]) g.fillText(cap[1].toUpperCase(), sx + sw / 2, sy + 132);
      if (s.kind === 'nolimit') { g.font = `900 92px ${SANS}`; const nl = T('NO<br>LIMIT').split('<br>'); g.fillText(nl[0], sx + sw / 2, sy + 290); if (nl[1]) g.fillText(nl[1], sx + sw / 2, sy + 390); }
      else { g.font = `900 230px ${SANS}`; g.fillText(String(s.n), sx + sw / 2, sy + 400); }
    }
    // condition diamond (right)
    const dx = 800, dy = 435, dr = 190; g.save(); g.translate(dx, dy); g.rotate(Math.PI / 4); rr(g, -dr, -dr, dr * 2, dr * 2, 26); g.fillStyle = '#F5C518'; g.fill(); g.lineWidth = 8; g.strokeStyle = '#1B1E21'; g.stroke(); g.restore();
    g.fillStyle = '#1B1E21'; g.font = `800 38px ${SANS}`; const cw = String(condSign(sc.x)).toUpperCase().split(/\s+/); const lines = []; let cur = ''; cw.forEach((w) => { const t = cur ? cur + ' ' + w : w; if (g.measureText(t).width > 230 && cur) { lines.push(cur); cur = w; } else cur = t; }); if (cur) lines.push(cur); lines.forEach((l, i) => g.fillText(l, dx, dy + 14 + (i - (lines.length - 1) / 2) * 46));
    // archetype
    g.fillStyle = '#F5C518'; g.font = `700 30px ${SANS}`; g.textAlign = 'center'; g.fillText(String(ar.tag).toUpperCase(), W / 2, 760);
    g.fillStyle = '#FFFFFF'; g.font = `900 78px ${SANS}`; g.fillText(ar.name, W / 2, 846);
    g.fillStyle = '#EEF0EC'; g.font = `400 32px ${SERIF}`; wrapText(g, fmt(T('Limit {y} · road {x}'), { y: Math.round(sc.y), x: Math.round(sc.x) }) + (nearest ? ' · ' + fmt(T('Closest public figure: {who} · agree on {a}/{b}'), { who: nearest.f.name, a: nearest.agree, b: nearest.both }) : ''), W / 2, 906, 900, 42, 'center');
    // map
    const mx = 190, my = 1000, mw = 700, mh = 260; g.fillStyle = '#1B1E21'; rr(g, mx, my, mw, mh, 12); g.fill(); g.strokeStyle = '#3A3E42'; g.lineWidth = 2; g.beginPath(); g.moveTo(mx + mw / 2, my); g.lineTo(mx + mw / 2, my + mh); g.moveTo(mx, my + mh / 2); g.lineTo(mx + mw, my + mh / 2); g.stroke();
    const X = (v) => mx + 14 + (v / 100) * (mw - 28), Y = (v) => my + mh - 14 - (v / 100) * (mh - 28);
    g.fillStyle = '#6B7075'; g.font = `700 18px ${SANS}`; g.textAlign = 'left'; g.fillText(T(ARCHE.open.name).toUpperCase(), mx + 12, my + 26); g.fillText(T(ARCHE.slow.name).toUpperCase(), mx + 12, my + mh - 12); g.textAlign = 'right'; g.fillText(T(ARCHE.weather.name).toUpperCase(), mx + mw - 12, my + 26); g.fillText(T(ARCHE.brake.name).toUpperCase(), mx + mw - 12, my + mh - 12);
    FIGS.forEach((f) => { const fs = figScore(f); if (!fs.ok) return; g.fillStyle = '#8F959A'; g.beginPath(); g.arc(X(fs.x), Y(fs.y), 6, 0, Math.PI * 2); g.fill(); });
    if (nearest) { const fs = figScore(nearest.f); if (fs.ok) { g.fillStyle = '#DDE1DC'; g.font = `700 20px ${SANS}`; g.textAlign = fs.x < 50 ? 'left' : 'right'; g.fillText(surname(nearest.f.name), X(fs.x) + (fs.x < 50 ? 12 : -12), Y(fs.y) + 7); } }
    g.fillStyle = '#0E6B3E'; g.beginPath(); g.arc(X(sc.x), Y(sc.y), 16, 0, Math.PI * 2); g.fill(); g.lineWidth = 5; g.strokeStyle = '#FFFFFF'; g.stroke();
    g.fillStyle = '#B4BAB2'; g.font = `700 26px ${SANS}`; g.textAlign = 'center'; g.fillText('SETTHELIMIT.COM', W / 2, 1310);
    return new Promise((res) => cv.toBlob(res, 'image/png'));
  }
  async function saveCard(sc, ar, nearest) {
    const blob = await cardPng(sc, ar, nearest); if (!blob) return;
    const file = new File([blob], 'set-the-limit.png', { type: 'image/png' });
    if (navigator.canShare && navigator.canShare({ files: [file] })) { try { await navigator.share({ files: [file], title: 'Set the Limit' }); return; } catch (e) { /* cancelled: fall through to download */ } }
    const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'set-the-limit.png'; document.body.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 2000);
  }
  // ---------- events ----------
  document.addEventListener('input', (e) => {
    const t = e.target; if (t.id !== 'slider') return;
    const r = parseRoute(); if (r.page !== 'q') return; const it = ITEMS[r.n - 1]; const v = Number(t.value);
    S.answers[it.id] = v; saveAnswers();
    const val = document.getElementById('val'); if (val) { val.textContent = v; val.classList.remove('unset'); }
    const w = document.getElementById('word'); if (w) w.textContent = words(it, v);
    const b = document.getElementById('nextbtn'); if (b) b.disabled = false;
    const d = document.getElementById('discuss'); if (d) d.hidden = false;
  });
  document.addEventListener('click', (e) => {
    const t = e.target.closest('[data-post],[data-postreply],[data-vote],[data-flag],[data-reply],[data-delc],[data-png],[data-claim],[data-unpublic],[data-skip],[data-next],[data-fig],[data-copylink],[data-copytext],[data-native],[data-retake],[data-vs],[data-card],[data-closecard],[data-stopcard],[data-steel]');
    if (!t) return; const ds = t.dataset; const r = parseRoute();
    if (ds.skip) { const it = ITEMS[r.n - 1]; S.answers[it.id] = null; saveAnswers(); go(r.n === ITEMS.length ? '#/result' : `#/q/${r.n + 1}`); return; }
    if (ds.next) { const it = ITEMS[r.n - 1]; if (S.answers[it.id] === undefined) return; go(r.n === ITEMS.length ? '#/result' : `#/q/${r.n + 1}`); return; }
    if (ds.fig) { S.sel = S.sel === ds.fig ? null : ds.fig; const y0 = window.scrollY; render(); window.scrollTo(0, y0); const fc = document.getElementById('figcard'); if (fc && S.sel) fc.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); return; }
    if (ds.post) { postComment(ds.post, null); return; }
    if (ds.postreply) { const rt = parseRoute(); postComment(rt.id, ds.postreply); return; }
    if (ds.vote) { commentAction('vote', ds.vote); return; }
    if (ds.flag) { commentAction('flag', ds.flag); return; }
    if (ds.delc) { commentAction('del', ds.delc); return; }
    if (ds.reply) { if (!S.me) { toast(T('Sign in with X first.')); return; } S.replyTo = S.replyTo === ds.reply ? null : ds.reply; renderKeep(); return; }
    if (ds.png) { const sc = scores(S.answers); const ar = archetype(sc.x, sc.y); const nearest = FIGS.map((f) => compare(S.answers, f)).filter((c) => c.dist !== null).sort(byAgreement)[0]; saveCard(sc, ar, nearest); return; }
    if (ds.claim) { claimDot(); return; }
    if (ds.unpublic) { unpublishRun(); return; }
    if (ds.copylink) { copy(shareLink(S.answers), () => toast(T('Link copied. Send it to someone who disagrees with you.'))); return; }
    if (ds.copytext) { copy(shareText(scores(S.answers), archetype(scores(S.answers).x, scores(S.answers).y), FIGS.map((f) => compare(S.answers, f)).filter((c) => c.dist !== null).sort(byAgreement)[0]), () => toast(T('Text copied.'))); return; }
    if (ds.native) { const sc = scores(S.answers); navigator.share({ title: SITE, text: shareText(sc, archetype(sc.x, sc.y), null), url: shareLink(S.answers) }).catch(() => { /* cancelled */ }); return; }
    if (ds.stopcard && !ds.closecard) return;
    if (ds.card) { const sc = scores(S.answers); const ar = archetype(sc.x, sc.y); const nearest = FIGS.map((f) => compare(S.answers, f)).filter((c) => c.dist !== null).sort(byAgreement)[0]; document.body.insertAdjacentHTML('beforeend', cardHtml(sc, ar, nearest)); return; }
    if (ds.closecard) { const c = document.querySelector('.cardview'); if (c) c.remove(); return; }
    if (ds.steel) { S.steelOpen = true; return; }
    if (ds.retake) { S.answers = {}; saveAnswers(); S.saved = false; S.sel = null; return; }
    if (ds.vs) { if (S.shared) { S.vs = S.shared; try { sessionStorage.setItem('stl.v1.vs', enc(S.shared)); } catch (x) { /* ignore */ } } return; }
  });
  document.addEventListener('keydown', (e) => {
    const r = parseRoute(); if (r.page !== 'q') return;
    if (e.key === 'Enter') { const b = document.getElementById('nextbtn'); if (b && !b.disabled) b.click(); }
  });
  document.addEventListener('keydown', (e) => { // les points de la carte sont focalisables : Entrée ou Espace les ouvre
    if ((e.key === 'Enter' || e.key === ' ') && e.target && e.target.closest && e.target.closest('.map [data-fig]')) { e.preventDefault(); e.target.closest('[data-fig]').dispatchEvent(new MouseEvent('click', { bubbles: true })); }
  });
  document.addEventListener('toggle', (e) => { if (e.target.classList && e.target.classList.contains('toggle')) S.steelOpen = e.target.open; }, true);
  window.addEventListener('hashchange', render);

  // ---------- boot ----------
  async function boot() {
    S.answers = loadAnswers();
    if (new URLSearchParams(location.search).get('debug') === '1' && new URLSearchParams(location.search).get('a')) S.answers = dec(new URLSearchParams(location.search).get('a')) || S.answers; /* local testing only */
    const q = new URLSearchParams(location.search);
    const r = q.get('r'); if (r) { S.shared = dec(r); if (S.shared && !location.hash) location.hash = '#/shared'; }
    try { const v = sessionStorage.getItem('stl.v1.vs'); if (v) S.vs = dec(v); } catch (e) { /* ignore */ }
    if (S.shared && !S.vs) S.vs = null;
    render();
    if (API) {
      S.run = loadRun();
      if (q.get('public') === '1') S.pendingPublic = true;
      apiJson('/comments/counts').then((j) => { if (j && j.counts) { S.counts = j.counts; rerender(); } });
      apiJson('/crowd').then((j) => { if (j && j.points) { S.liveCrowd = j.points; rerender(); } });
      apiJson('/claims').then((j) => { if (j && j.figures) { applyClaims(j.figures); rerender(); } });
      apiJson('/me').then((j) => { S.me = j && j.handle ? j : null; if (S.me && S.pendingPublic) publishRun(); rerender(); });
      const u = q.get('u'); if (u) apiJson('/public/' + encodeURIComponent(u)).then((j) => { if (j && j.r) { S.shared = dec(j.r); S.sharedBy = j.handle; if (S.shared) { location.hash = '#/shared'; render(); } } });
      if (parseRoute().page === 'result') afterResult();
    }
    if (window.claude && typeof window.claude.use === 'function') {
      const db = await window.claude.use('db').catch(() => null);
      if (db) {
        S.db = db;
        try { db.collection('runs').limit(1000).onSnapshot((snap) => { S.liveCrowd = snap.docs.map((d) => d.data()).filter((x) => typeof x.x === 'number' && typeof x.y === 'number').map((x) => [x.x, x.y]); if (parseRoute().page === 'result' || parseRoute().page === 'shared') render(); }, (e) => console.warn('db', e)); } catch (e) { console.warn(e); }
        if (parseRoute().page === 'result') afterResult();
      }
    }
  }
  if (new URLSearchParams(location.search).get('debug') === '1') window.STL_DEBUG = { cardPng, scores, archetype, compare, byAgreement, FIGS, ITEMS, S }; /* local testing only */
  boot();
})();
