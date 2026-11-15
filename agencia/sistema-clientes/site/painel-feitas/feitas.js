/* Tarefas feitas no painel do cliente: por dia (mais recente primeiro), hora, atividade e quem fez.
   Lê /api/feitas (o servidor devolve só as linhas do cliente logado). Pedido do Lindson, 15/11/2026, conta Zuleide. */
(function () {
  const V = window.__V, T = window.__T; if (!V || !T || V.feitas) return;
  const cli = (location.pathname.split('/')[2] || '').replace(/\.html$/, '').toLowerCase();
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);
  const hoje = (n = 0) => new Date(Date.now() - 3 * 36e5 - n * 864e5).toISOString().slice(0, 10);
  let S = { ok: false, itens: [], erro: '' }, PER = 'tudo', admin = false;
  async function carrega() {
    try { const r = await fetch('/api/feitas?cli=' + encodeURIComponent(cli), { credentials: 'same-origin' }); const j = await r.json();
      if (!r.ok) throw new Error(j.erro || 'erro'); S = { ok: true, itens: j.itens || [] }; admin = j.eu === 'admin'; }
    catch (e) { S = { ok: false, itens: [], erro: 'Não consegui ler as tarefas agora.' }; }
    const n = document.getElementById('n-feitas'); if (n) n.textContent = S.itens.filter(x => x.data >= hoje(6)).length || '';
    if ((location.hash || '').slice(1) === 'feitas' && window.__render) window.__render();
  }
  // item no menu (grupo "Visão", logo depois da Visão geral)
  const g = document.querySelector('#menu .grupo');
  if (g) { const a = document.createElement('a'); a.href = '#feitas'; a.dataset.v = 'feitas';
    a.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/></svg>Tarefas feitas<span class="n" id="n-feitas"></span>';
    const ref = g.querySelector('a[data-v="inicio"]'); ref && ref.nextSibling ? g.insertBefore(a, ref.nextSibling) : g.appendChild(a); }
  const st = document.createElement('style');
  st.textContent = `.tf-per{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 16px}.tf-per button{font:600 12px var(--f-corpo);color:var(--texto);background:var(--painel2);border:1px solid var(--linha);border-radius:99px;padding:6px 12px;cursor:pointer}
.tf-per button[aria-pressed=true]{background:var(--amarelo);color:var(--fundo);border-color:var(--amarelo)}.tf-per b{margin-left:6px;opacity:.7}
.tf-dia{margin:0 0 18px}.tf-dia h4{display:flex;align-items:baseline;gap:8px;margin:0 0 8px;font:700 13px var(--f-corpo);text-transform:capitalize}.tf-dia h4 small{color:var(--apagado);font-weight:500;text-transform:none}
.tf-l{display:grid;grid-template-columns:52px 1fr;gap:12px;padding:11px 12px;border:1px solid var(--linha);border-radius:10px;background:var(--painel2);margin-bottom:8px}
.tf-h{font:600 13px var(--f-dado);color:var(--amarelo);font-variant-numeric:tabular-nums}.tf-a{font-weight:600;overflow-wrap:anywhere}.tf-q{color:var(--apagado);font-size:12px;margin-top:2px}`;
  document.head.appendChild(st);
  const PERS = [['hoje', 'Hoje', x => x.data === hoje()], ['7d', '7 dias', x => x.data >= hoje(6)], ['mes', 'Mês', x => x.data.slice(0, 7) === hoje().slice(0, 7)], ['tudo', 'Tudo', () => true]];
  const nomeDia = d => { const [a, m, dd] = d.split('-'); const w = new Date(d + 'T12:00:00').toLocaleDateString('pt-BR', { weekday: 'long' }); return (d === hoje() ? 'Hoje' : d === hoje(1) ? 'Ontem' : w) + ` <small>${dd}/${m}/${a}</small>`; };
  V.feitas = () => {
    if (!S.ok) return `<div class="card"><h3>Tarefas feitas</h3><p class="sub">${S.erro || 'Carregando…'}</p></div>`;
    const f = PERS.find(p => p[0] === PER)[2], lista = S.itens.filter(f), dias = {};
    lista.forEach(x => (dias[x.data] = dias[x.data] || []).push(x));
    const k = [['Hoje', S.itens.filter(PERS[0][2]).length], ['Últimos 7 dias', S.itens.filter(PERS[1][2]).length], ['Este mês', S.itens.filter(PERS[2][2]).length], ['Desde o início', S.itens.length]];
    return `<div class="grade g4">${k.map(([r, v]) => `<div class="card kpi"><div class="rot">${r}</div><div class="val">${v}</div></div>`).join('')}</div>
    <div class="card" style="margin-top:14px"><h3>O que a equipe já fez para você</h3><p class="sub">Cada entrega da agência, com o dia, a hora e quem fez. Atualiza sozinho.</p>
    <div class="tf-per" role="group" aria-label="Período">${PERS.map(([id, n, fn]) => `<button type="button" data-tfper="${id}" aria-pressed="${PER === id}">${n}<b>${S.itens.filter(fn).length}</b></button>`).join('')}</div>
    ${lista.length ? Object.keys(dias).sort().reverse().map(d => `<div class="tf-dia"><h4>${nomeDia(d)}<small>${dias[d].length} tarefa(s)</small></h4>${dias[d].sort((a, b) => (b.hora || '').localeCompare(a.hora || '')).map(x => `<div class="tf-l"><div class="tf-h">${esc(x.hora || '—')}</div><div><div class="tf-a">${esc(x.atividade)}</div><div class="tf-q">Feito por ${esc(x.por || 'equipe')}${admin ? ` · <button type="button" data-tfdel="${esc(x.id)}" style="background:none;border:0;color:var(--erro);cursor:pointer;font:inherit;padding:0">remover</button>` : ''}</div></div></div>`).join('')}</div>`).join('') : '<p class="sub">Nada lançado neste período.</p>'}</div>`;
  };
  T.feitas = 'Tarefas feitas';
  document.addEventListener('click', async e => {
    const b = e.target.closest('[data-tfper]'); if (b) { PER = b.dataset.tfper; window.__render(); return; }
    const d = e.target.closest('[data-tfdel]'); if (d && admin && confirm('Remover esta linha das tarefas feitas?')) {
      const r = await fetch('/api/feitas?id=' + encodeURIComponent(d.dataset.tfdel), { method: 'DELETE', credentials: 'same-origin' }); if (r.ok) carrega(); else alert('Não consegui remover.'); }
  });
  carrega(); setInterval(carrega, 120000);
  if ((location.hash || '').slice(1) === 'feitas' && window.__render) window.__render();
})();
