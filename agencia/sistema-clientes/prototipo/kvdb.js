// Banco simples no servidor da Central (/api/dados) com a mesma "cara" do db do artifact (collection/doc/set/update/delete/onSnapshot).
// Usado quando o painel roda no site (lindsonalmeida.pages.dev), onde o db do claude.ai não existe. Ex.: gabinete.js do Leo.
// Coleções → ferramenta no servidor: demandas → dem, agenda → ag. Atualiza a cada 30 s. Conta Lindson, 01/11/2026.
window.__kvdb = cli => {
  const FER = { demandas: 'dem', agenda: 'ag' }, st = {}, subs = {}, url = n => `/api/dados?cli=${cli}&f=${FER[n] || n}`;
  const vaz = () => ({ itens: [], apagados: [] }), uid = () => Date.now().toString(36) + Math.random().toString(36).slice(2, 8);
  async function carrega(n) {
    const r = await fetch(url(n), { headers: { Accept: 'application/json' } });
    if (!r.ok || !(r.headers.get('content-type') || '').includes('json')) throw { code: r.status === 403 || r.status === 401 ? 'invalid_argument' : 'unavailable' };
    const j = await r.json(); st[n] = { dados: j.dados || vaz(), versao: j.versao || 0 }; emite(n);
  }
  function emite(n) {
    (subs[n] || []).forEach(s => {
      let l = (st[n].dados.itens || []).slice();
      if (s.ord) { const [k, dir] = s.ord; l.sort((a, b) => (a[k] > b[k] ? 1 : a[k] < b[k] ? -1 : 0) * (dir === 'desc' ? -1 : 1)); }
      if (s.lim) l = l.slice(0, s.lim);
      s.cb({ docs: l.map(x => ({ id: x.id, data: () => { const { id, ...r } = x; return r; } })), metadata: { fromCache: false } });
    });
  }
  async function muda(n, fn) {
    for (let t = 0; t < 4; t++) {
      if (!st[n]) await carrega(n);
      const copia = JSON.parse(JSON.stringify(st[n].dados)); fn(copia);
      const r = await fetch(url(n), { method: 'PUT', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ dados: copia, versao: st[n].versao }) });
      if (r.ok) { st[n] = { dados: copia, versao: (await r.json()).versao }; emite(n); return; }
      if (r.status === 409) { const j = await r.json(); st[n] = { dados: j.dados || vaz(), versao: j.versao }; continue; }
      throw { code: r.status === 403 || r.status === 401 ? 'invalid_argument' : 'unavailable' };
    }
    throw { code: 'unavailable' };
  }
  return {
    collection(n) {
      const q = { ord: null, lim: 0 };
      const api = {
        doc(id) { id = id || uid(); return {
          set: o => muda(n, d => { d.itens = (d.itens || []).filter(x => x.id !== id); d.itens.push({ ...o, id }); }),
          update: o => muda(n, d => { const x = (d.itens || []).find(y => y.id === id); if (x) Object.assign(x, o); }),
          delete: () => muda(n, d => { d.itens = (d.itens || []).filter(x => x.id !== id); d.apagados = [...(d.apagados || []), id].slice(-1000); }) }; },
        orderBy(k, dir) { q.ord = [k, dir]; return api; },
        limit(l) { q.lim = l; return api; },
        onSnapshot(cb, erro) {
          (subs[n] = subs[n] || []).push({ cb, ord: q.ord, lim: q.lim });
          const vai = () => carrega(n).catch(e => { if (erro) erro(e); });
          vai(); setInterval(() => { if (!document.hidden) vai(); }, 30000);
          return () => {};
        } };
      return api;
    } };
};
