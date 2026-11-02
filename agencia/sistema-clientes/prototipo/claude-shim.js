// Substitui o "window.claude" do claude.ai quando um app do Lindson roda dentro da Central (lindsonalmeida.pages.dev).
// claude.use('db') → banco do servidor (/api/db), com a mesma forma: doc/collection/get/set/update/delete/add/where/orderBy/limit/onSnapshot.
// claude.use('user') → o administrador (id fixo "lindson"). Outros recursos → indisponíveis (o app usa o plano B dele). Conta Lindson, 02/11/2026.
(() => {
  const cache = {}, subs = {};
  const uid = () => Date.now().toString(36) + Math.random().toString(36).slice(2, 10);
  const parte = p => { const s = String(p).split('/'); return { col: s.slice(0, -1).join('/'), id: s[s.length - 1] }; };
  async function le(col, forca) {
    if (cache[col] && !forca) return cache[col];
    const r = await fetch('/api/db?col=' + encodeURIComponent(col), { headers: { Accept: 'application/json' } });
    if (!r.ok) throw { code: r.status === 403 || r.status === 401 ? 'permission-denied' : 'unavailable' };
    cache[col] = (await r.json()).docs || {}; return cache[col];
  }
  const fila = []; let enviando = null;
  function grava(op) {
    const c = cache[op.col] || (cache[op.col] = {});
    if (op.op === 'delete') delete c[op.id]; else if (op.op === 'set') c[op.id] = JSON.parse(JSON.stringify(op.data || {})); else c[op.id] = Object.assign(c[op.id] || {}, JSON.parse(JSON.stringify(op.data || {})));
    avisa(op.col); fila.push(op);
    if (!enviando) enviando = new Promise(res => setTimeout(async () => {
      const lote = fila.splice(0); let ok = true;
      try { const r = await fetch('/api/db', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ ops: lote }) }); ok = r.ok; } catch (e) { ok = false; }
      enviando = null; res(ok);
    }, 250));
    return enviando.then(ok => { if (!ok) throw { code: 'unavailable' }; });
  }
  const snapDoc = (id, d) => ({ id, exists: d !== undefined, data: () => d === undefined ? undefined : JSON.parse(JSON.stringify(d)) });
  function consulta(col, q) {
    const docs = cache[col] || {}; let l = Object.keys(docs).map(id => ({ id, d: docs[id] }));
    (q.where || []).forEach(([f, op, v]) => { l = l.filter(x => { const a = (x.d || {})[f]; return op === '==' ? a === v : op === '!=' ? a !== v : op === '>' ? a > v : op === '>=' ? a >= v : op === '<' ? a < v : op === '<=' ? a <= v : op === 'in' ? (v || []).includes(a) : op === 'array-contains' ? Array.isArray(a) && a.includes(v) : true; }); });
    if (q.ord) { const [f, dir] = q.ord; l.sort((a, b) => { const x = (a.d || {})[f], y = (b.d || {})[f]; return (x > y ? 1 : x < y ? -1 : 0) * (dir === 'desc' ? -1 : 1); }); }
    if (q.lim) l = l.slice(0, q.lim);
    const ds = l.map(x => snapDoc(x.id, x.d)); return { docs: ds, empty: !ds.length, size: ds.length, forEach: f => ds.forEach(f) };
  }
  function avisa(col) { (subs[col] || []).forEach(s => s.cb(s.doc ? snapDoc(s.doc, (cache[col] || {})[s.doc]) : consulta(col, s.q))); }
  function colRef(col, q = {}) {
    const api = {
      doc: id => docRef(col, id || uid()),
      add: data => { const id = uid(); return grava({ op: 'set', col, id, data }).then(() => docRef(col, id)); },
      where: (f, op, v) => colRef(col, { ...q, where: [...(q.where || []), [f, op, v]] }),
      orderBy: (f, dir) => colRef(col, { ...q, ord: [f, dir || 'asc'] }),
      limit: n => colRef(col, { ...q, lim: n }),
      get: () => le(col).then(() => consulta(col, q)),
      onSnapshot: (cb, erro) => { (subs[col] = subs[col] || []).push({ cb, q }); le(col).then(() => cb(consulta(col, q))).catch(e => erro && erro(e)); return () => { subs[col] = (subs[col] || []).filter(s => s.cb !== cb); }; }
    };
    return api;
  }
  function docRef(col, id) {
    return { id, path: col + '/' + id,
      get: () => le(col).then(c => snapDoc(id, c[id])),
      set: (data, o) => grava({ op: o && o.merge ? 'update' : 'set', col, id, data }),
      update: data => grava({ op: 'update', col, id, data }),
      delete: () => grava({ op: 'delete', col, id }),
      collection: sub => colRef(col + '/' + id + '/' + sub),
      onSnapshot: (cb, erro) => { (subs[col] = subs[col] || []).push({ cb, doc: id }); le(col).then(c => cb(snapDoc(id, c[id]))).catch(e => erro && erro(e)); return () => {}; } };
  }
  const db = { doc: p => { const { col, id } = parte(p); return docRef(col, id); }, collection: p => colRef(p) };
  const user = { id: () => Promise.resolve('lindson'), can: () => Promise.resolve(true), name: () => Promise.resolve('Lindson') };
  // primeira vez: traz os dados do app antigo do claude.ai (window.__IMPORTAR = {script, marca: "col/id"}), em lotes, antes de o app ler
  let pronto = Promise.resolve();
  if (window.__IMPORTAR) pronto = (async () => {
    const { script, marca } = window.__IMPORTAR, m = parte(marca);
    try { const c = await le(m.col, true); if (c[m.id] !== undefined) return; } catch (e) { return; }
    await new Promise((ok, erro) => { const t = document.createElement('script'); t.src = script; t.onload = ok; t.onerror = erro; document.head.appendChild(t); }).catch(() => null);
    const docs = window.__DADOS_IMPORTAR || []; if (!docs.length) return;
    const aviso = document.createElement('div'); aviso.textContent = 'Trazendo seus dados do app antigo…'; aviso.style.cssText = 'position:fixed;left:50%;bottom:24px;transform:translateX(-50%);z-index:99;background:#F5C518;color:#0A0A0A;font:700 14px system-ui;padding:12px 18px;border-radius:12px'; document.body.appendChild(aviso);
    const porCol = {}; docs.forEach(d => (porCol[d.col] = porCol[d.col] || []).push(d));
    for (const [col, lista] of Object.entries(porCol)) {
      for (let i = 0; i < lista.length; i += 40) {
        const ops = lista.slice(i, i + 40).map(d => ({ op: 'set', col, id: d.id, data: d.data }));
        await fetch('/api/db', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ ops }) });
      }
      delete cache[col];
    }
    aviso.textContent = 'Dados trazidos ✓'; setTimeout(() => aviso.remove(), 2500);
  })();
  // assets: fotos e arquivos enviados pelo app vão para as Fotos do administrador no servidor (/api/fotos?cli=lindson); devolve {id, url}
  const assets = { upload: async (blob, o) => {
    const tipo = (o && o.type) || blob.type || 'image/jpeg', nome = encodeURIComponent((blob && blob.name) || 'arquivo');
    const r = await fetch(`/api/fotos?cli=lindson&cat=${encodeURIComponent(window.__ASSETS_CAT || 'App')}&nome=${nome}`, { method: 'POST', headers: { 'Content-Type': tipo }, body: blob });
    const j = await r.json().catch(() => ({})); if (!r.ok) throw { code: 'unavailable', message: j.erro || 'Não enviou' };
    return { id: j.id, url: '/api/foto?cli=lindson&id=' + j.id };
  } };
  window.claude = { use: n => pronto.then(() => n === 'db' ? db : n === 'user' ? user : n === 'assets' ? assets : null) };
})();
