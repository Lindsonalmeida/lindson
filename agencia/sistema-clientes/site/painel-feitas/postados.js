/* Pasta "Postados" no painel do cliente (pedido do Lindson, 15/11/2026, conta Zuleide).
   Cada conteúdo das abas de aprovação/postagem ganha "Marcar como postado"; ao marcar, sai da lista e vai para a pasta
   Postados (com data, hora e quem marcou), com "Voltar" para desfazer. Salvo no servidor (/api/postados, KV do cliente).
   Uso em painel novo: <script src="/painel/postados.js"></script> depois do feitas.js. Funciona sozinho pelo DOM. */
(function () {
  const V = window.__V, T = window.__T; if (!V || !T || V.postados) return;
  const cli = (location.pathname.split('/')[2] || '').replace(/\.html$/, '').toLowerCase();
  const ABAS = ['aprovacoes', 'aprovar', 'postagens'];
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);
  const toast = t => window.__toast ? window.__toast(t) : 0;
  const hash = s => { let h = 5381; for (let i = 0; i < s.length; i++) h = (h * 33 ^ s.charCodeAt(i)) >>> 0; return h.toString(36); };
  let S = { ok: false, itens: {} };
  const n = () => Object.keys(S.itens).length;
  function conta() { const e = document.getElementById('n-postados'); if (e) e.textContent = n() || ''; }
  async function carrega() {
    try { const r = await fetch('/api/postados?cli=' + encodeURIComponent(cli), { credentials: 'same-origin' }); const j = await r.json();
      if (!r.ok) throw 0; S = { ok: true, itens: j.itens || {} }; } catch (e) { S = { ok: false, itens: {} }; }
    conta(); const v = (location.hash || '').slice(1); if ((v === 'postados' || ABAS.includes(v)) && window.__render) window.__render();
  }
  async function manda(corpo) {
    const r = await fetch('/api/postados', { method: 'POST', credentials: 'same-origin', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(Object.assign({ cli }, corpo)) });
    const j = await r.json().catch(() => ({})); if (!r.ok) throw new Error(j.erro || 'erro'); S.itens = j.itens || {}; S.ok = true; conta(); window.__render && window.__render();
  }
  // menu: logo depois de Aprovações / Postagens
  const ref = document.querySelector('#menu a[data-v="postagens"]') || document.querySelector('#menu a[data-v="aprovacoes"]') || document.querySelector('#menu a[data-v="aprovar"]');
  if (ref) { const a = document.createElement('a'); a.href = '#postados'; a.dataset.v = 'postados';
    a.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 13l2 2 4-4"/></svg>Postados<span class="n" id="n-postados"></span>';
    ref.parentNode.insertBefore(a, ref.nextSibling); }
  const st = document.createElement('style');
  st.textContent = `.pp-b{display:block;width:calc(100% - 24px);margin:10px 12px 12px;padding:10px 12px;font:700 13px var(--f-corpo,inherit);color:var(--fundo,#080808);background:var(--amarelo,#F5C518);border:0;border-radius:999px;cursor:pointer}
.pp-b.in{width:auto;margin:12px 0 0;padding:9px 16px}.pp-g{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,220px),1fr));gap:12px;margin-top:14px}
.pp-i{border:1px solid var(--linha);border-radius:14px;background:var(--painel2);overflow:hidden;display:flex;flex-direction:column}.pp-i img{width:100%;aspect-ratio:4/5;object-fit:cover;display:block;background:#000}
.pp-c{padding:12px;display:flex;flex-direction:column;gap:6px;flex:1}.pp-t{font-weight:700;overflow-wrap:anywhere}.pp-q{font-size:12px;color:var(--apagado)}.pp-v{margin-top:auto;align-self:flex-start;font:600 12px var(--f-corpo,inherit);color:var(--texto);background:transparent;border:1px solid var(--linha);border-radius:999px;padding:7px 14px;cursor:pointer}
.pp-aviso{display:flex;flex-wrap:wrap;gap:8px;align-items:center;justify-content:space-between;margin:0 0 14px;padding:10px 14px;border:1px solid var(--linha);border-radius:12px;font-size:13px}.pp-aviso a{color:var(--amarelo);font-weight:700}`;
  document.head.appendChild(st);
  const quando = iso => { const d = new Date(iso); return d.toLocaleDateString('pt-BR', { timeZone: 'America/Fortaleza' }) + ' às ' + d.toLocaleTimeString('pt-BR', { timeZone: 'America/Fortaleza', hour: '2-digit', minute: '2-digit' }); };
  V.postados = () => {
    const l = Object.entries(S.itens).sort((a, b) => b[1].em.localeCompare(a[1].em));
    return `<div class="card"><h3>Postados · ${l.length}</h3><p class="sub">Conteúdos já publicados. Marcou por engano? Toque em "Voltar" e ele volta para a lista a postar.</p>
    ${!S.ok ? '<p class="sub">Carregando…</p>' : l.length ? `<div class="pp-g">${l.map(([id, x]) => `<div class="pp-i">${x.img ? `<img src="${esc(x.img)}" alt="" loading="lazy">` : ''}<div class="pp-c"><div class="pp-t">${esc(x.titulo || 'Conteúdo')}</div><div class="pp-q">Postado em ${esc(quando(x.em))}<br>por ${esc(x.por)}</div><button type="button" class="pp-v" data-ppvoltar="${esc(id)}">Voltar para a postar</button></div></div>`).join('')}</div>` : '<p class="sub">Nada marcado como postado ainda.</p>'}</div>`;
  };
  T.postados = 'Postados';
  function itens(M, v) {
    const s = new Set();
    M.querySelectorAll('.post').forEach(e => s.add(e));
    M.querySelectorAll('[data-postado]').forEach(e => { const c = e.closest('.card'); if (c) { s.add(c); const l = e.closest('label'); if (l) l.remove(); } });
    if (v === 'aprovar') M.querySelectorAll('.fotos > a').forEach(e => s.add(e));
    return [...s];
  }
  function dados(e, v) {
    const m = e.querySelector('img[src],video[poster]'), img = m ? (m.getAttribute('src') || m.getAttribute('poster')) : '';
    const ok3 = x => x && x.textContent.trim().length > 3, tEl = e.querySelector('[data-pptitulo]') || [...e.querySelectorAll('div[style*="font-weight:700"],.t')].find(ok3) || [...e.querySelectorAll('b')].find(ok3);
    const titulo = (tEl ? tEl.textContent : (m && m.alt) || e.textContent).replace(/\s+/g, ' ').trim().slice(0, 160);
    return { id: v.slice(0, 4) + '-' + hash(v + '|' + (img || '') + '|' + titulo), titulo, img: img && !/^data:/.test(img) ? new URL(img, location.href).pathname : '', aba: v };
  }
  function aplica(v) {
    if (!ABAS.includes(v) || !S.ok) return; const M = document.querySelector('main') || document.body; let esc_ = 0;
    itens(M, v).forEach(e => {
      if (e.dataset.pp) return; const d = dados(e, v); e.dataset.pp = d.id;
      if (S.itens[d.id]) { e.style.display = 'none'; esc_++; return; }
      const b = document.createElement('button'); b.type = 'button'; b.className = 'pp-b' + (e.classList.contains('card') ? ' in' : ''); b.textContent = 'Marcar como postado';
      b.onclick = ev => { ev.preventDefault(); ev.stopPropagation(); b.disabled = true; manda(Object.assign({ acao: 'postar' }, d)).then(() => toast('Foi para a pasta Postados.')).catch(() => { b.disabled = false; toast('Não consegui marcar agora. Tente de novo.'); }); };
      if (e.matches('a')) { b.style.cssText = 'width:calc(100% - 8px);margin:4px'; e.appendChild(b); } else (e.classList.contains('card') ? (e.lastElementChild || e) : e).appendChild(b);
    });
    if (n()) { const c = M.querySelector('.card'); if (c && !M.querySelector('.pp-aviso')) { const a = document.createElement('div'); a.className = 'pp-aviso'; a.innerHTML = `<span>${esc_ || n()} conteúdo(s) já postado(s) saíram desta lista.</span><a href="#postados">Ver a pasta Postados (${n()})</a>`; c.parentNode.insertBefore(a, c); } }
  }
  const ant = window.__pos; window.__pos = v => { if (ant) ant(v); try { aplica(v); } catch (e) {} };
  document.addEventListener('click', e => { const b = e.target.closest('[data-ppvoltar]'); if (!b) return; b.disabled = true;
    manda({ acao: 'voltar', id: b.dataset.ppvoltar }).then(() => toast('Voltou para a lista a postar.')).catch(() => { b.disabled = false; toast('Não consegui desfazer agora.'); }); });
  carrega();
  if ((location.hash || '').slice(1) === 'postados' && window.__render) window.__render();
})();
