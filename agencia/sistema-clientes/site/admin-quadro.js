// Tela "Quadro de atividades" do painel do ADMINISTRADOR (conta Leandro, 08/11/2026).
// Pedido do Lindson: "crie um quadro de atividades no meu painel, com cada cliente e coisas que faltam fazer, pra eu ir dando check e não ficar perguntando sempre".
// Itens: window.__QUADRO (agencia/sistema-clientes/site/quadro.json, tirado do TRAVA-MAQUIAVEL.md). Marcações: banco do admin (/api/db?col=quadro),
// então valem no celular e no computador. Itens feitos vão para a aba "Feitos"; a equipe também marca pelo 4º campo do item no quadro.json (data). Pagantes primeiro. Entra no admin depois do admin-sistema.js.
(() => {
const V = window.__V, T = window.__T, Q = window.__QUADRO || { grupos: [] };
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const render = () => window.__render && window.__render(), toast = t => window.__toast && window.__toast(t);
const QUEM = { voce: ['Você', '#F5C518', '#0A0A0A'], cliente: ['Cliente', '#2a2a2a', '#F5F3EE'], equipe: ['Equipe', '#1f3a2a', '#9BE3B5'] };
let feitos = {}, filtro = 'afazer', carregou = false;
async function carrega() {
  try { const r = await fetch('/api/db?col=quadro'); if (r.ok) { const j = await r.json(); feitos = (j && j.docs) || {}; } } catch (e) {}
  carregou = true; render();
}
async function marca(id, on) {
  const data = on ? { feito: true, quando: new Date().toISOString() } : { feito: false };
  feitos[id] = data; render();
  try {
    const r = await fetch('/api/db', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ ops: [{ op: 'set', col: 'quadro', id, data }] }) });
    if (!r.ok) throw 0; toast(on ? 'Marcado como feito' : 'Desmarcado');
  } catch (e) { toast('Não salvou. Confira a conexão e tente de novo.'); }
}
const br = iso => { try { const d = new Date(iso); return String(d.getDate()).padStart(2, '0') + '/' + String(d.getMonth() + 1).padStart(2, '0'); } catch (e) { return ''; } };
const EQ = Object.fromEntries(Q.grupos.flatMap(g => g.itens.filter(i => i[3]).map(i => [i[0], i[3]])));  // marcado pela equipe: [id, texto, quem, 'DD/MM']
const todos = () => Q.grupos.flatMap(g => g.itens.map(i => ({ g, id: i[0], txt: i[1], quem: i[2] })));
const ok = id => (feitos[id] && feitos[id].feito === false && !EQ[id]) ? false : !!((feitos[id] && feitos[id].feito) || EQ[id]);
const quando = id => (feitos[id] && feitos[id].quando) ? br(feitos[id].quando) : (EQ[id] || '');
const kpi = (r, v, nota) => `<div class="card kpi"><div class="rot">${r}</div><div class="val">${v}</div><div class="var up"><span>${nota || ''}</span></div></div>`;
T.quadro = 'Quadro de atividades';
V.quadro = () => {
  if (!carregou) carrega();
  const L = todos(), feitosN = L.filter(i => ok(i.id)).length, voce = L.filter(i => !ok(i.id) && i.quem === 'voce').length;
  const chipF = (id, nome) => `<button class="btn${filtro === id ? ' am' : ''}" data-qf="${id}" style="padding:7px 14px;font-size:13px">${nome}</button>`;
  const grupo = g => {
    const its = g.itens.map(i => ({ id: i[0], txt: i[1], quem: i[2] })).filter(i => filtro === 'feitos' ? ok(i.id) : (!ok(i.id) && (filtro === 'afazer' || i.quem === filtro)));
    if (!its.length) return '';
    const tot = g.itens.length, f = g.itens.filter(i => ok(i[0])).length, pct = Math.round(f / tot * 100);
    return `<div class="card" style="padding:22px 24px">
      <div style="display:flex;justify-content:space-between;align-items:center;gap:12px;margin-bottom:10px">
        <h3 style="margin:0;font-size:18px">${esc(g.nome)}${g.pagante ? ' <span style="font:700 11px system-ui;background:#F5C518;color:#0A0A0A;padding:3px 8px;border-radius:99px;margin-left:6px;vertical-align:middle">PAGANTE</span>' : ''}</h3>
        <b style="font-size:14px;white-space:nowrap">${f} de ${tot}</b></div>
      <div style="height:6px;border-radius:99px;background:rgba(255,255,255,.08);overflow:hidden;margin-bottom:14px"><div style="height:100%;width:${pct}%;background:#F5C518;border-radius:99px;transition:width .4s"></div></div>
      ${its.map(i => { const q = QUEM[i.quem] || QUEM.voce, d = ok(i.id);
        return `<label style="display:flex;align-items:flex-start;gap:12px;padding:11px 0;border-top:1px solid rgba(255,255,255,.07);cursor:pointer">
          <input type="checkbox" data-qid="${i.id}" ${d ? 'checked' : ''} style="width:20px;height:20px;margin-top:2px;accent-color:#F5C518;flex:none">
          <span style="flex:1;line-height:1.4;${d ? 'text-decoration:line-through;opacity:.5' : ''}">${esc(i.txt)}${d && quando(i.id) ? ` <small style="opacity:.7">· feito em ${quando(i.id)}</small>` : ''}</span>
          <span style="flex:none;font:600 11px system-ui;padding:4px 9px;border-radius:99px;background:${q[1]};color:${q[2]}">${q[0]}</span></label>`; }).join('')}
    </div>`;
  };
  const ordem = Q.grupos.slice().sort((a, b) => (b.pagante === true) - (a.pagante === true));
  return `<div class="grade g4">${kpi('Total', L.length, 'atualizado em ' + esc(Q.atualizado || ''))}${kpi('Feitos', carregou ? feitosN + (window.__FEITOS || []).length : '…', 'todas as contas')}${kpi('Com você', carregou ? voce : '…', 'dependem de você')}${kpi('Com cliente ou equipe', carregou ? L.length - feitosN - voce : '…', '')}</div>
    <div style="display:flex;gap:8px;flex-wrap:wrap;margin:18px 0">${chipF('afazer', 'A fazer')}${chipF('voce', 'Com você')}${chipF('cliente', 'Com cliente')}${chipF('equipe', 'Com equipe')}${chipF('feitos', 'Feitos (' + (feitosN + (window.__FEITOS || []).length) + ')')}</div>
    ${filtro === 'feitos' ? linhaTempo() : `<div class="grade g2" style="align-items:start">${ordem.map(grupo).join('') || '<div class="card" style="padding:24px">Tudo feito aqui. 👏</div>'}</div>`}`;
};
// Aba Feitos = linha do tempo por data e hora, com tudo o que todas as contas fizeram (window.__FEITOS, do REGISTRO-DAS-CONTAS + histórico) e os itens marcados no quadro (11/11/2026).
const DIAS = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado'];
const hojeSL = (n = 0) => new Date(Date.now() - 3 * 36e5 - n * 864e5).toISOString().slice(0, 10);
function linhaTempo() {
  const F = (window.__FEITOS || []).map(f => ({ ...f }));
  todos().filter(i => ok(i.id)).forEach(i => {
    let d = '', hh = '';
    if (feitos[i.id] && feitos[i.id].quando) { const x = new Date(new Date(feitos[i.id].quando).getTime() - 3 * 36e5).toISOString(); d = x.slice(0, 10); hh = x.slice(11, 16); }
    else if (EQ[i.id]) { const [dd, mm] = EQ[i.id].split('/'); d = '2026-' + mm + '-' + dd; }
    F.push({ d, h: hh, txt: i.txt, cli: i.g.nome, conta: i.quem === 'voce' ? 'Lindson' : i.quem === 'cliente' ? 'Cliente' : 'Equipe', qid: i.id });
  });
  if (!F.length) return '<div class="card" style="padding:24px">Nada feito ainda.</div>';
  const por = {}; F.forEach(f => (por[f.d || 'sem data'] = por[f.d || 'sem data'] || []).push(f));
  const cor = { Lindson: '#F5C518', Zuleide: '#9BE3B5', Pedro: '#8EC5FF', Leandro: '#FFB38A' };
  return Object.keys(por).sort().reverse().map(d => {
    const its = por[d].sort((a, b) => (b.h || '').localeCompare(a.h || ''));
    let tit = d;
    if (/^\d{4}-/.test(d)) { const [a, m, dd] = d.split('-'); tit = (d === hojeSL() ? 'Hoje' : d === hojeSL(1) ? 'Ontem' : DIAS[new Date(d + 'T12:00:00').getDay()]) + ' · ' + dd + '/' + m + '/' + a; }
    return `<div class="card" style="padding:20px 24px;margin-bottom:14px">
      <div style="display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin-bottom:6px"><h3 style="margin:0;font-size:18px;text-transform:capitalize">${esc(tit)}</h3><b style="font-size:13px;opacity:.75">${its.length} feita(s)</b></div>
      ${its.map(f => { const c = cor[(f.conta || '').split(' ')[0]] || '#bbb';
        return `<div style="display:grid;grid-template-columns:52px 1fr;gap:12px;padding:10px 0;border-top:1px solid rgba(255,255,255,.07)">
          <b style="font:600 13px ui-monospace,monospace;color:#F5C518;padding-top:2px">${esc(f.h || '··:··')}</b>
          <div style="min-width:0"><div style="line-height:1.4">${esc(f.txt)}</div>
            <div style="display:flex;gap:6px;flex-wrap:wrap;margin-top:6px">${f.cli ? `<span style="font:600 11px system-ui;padding:3px 9px;border-radius:99px;background:#2a2a2a;color:#F5F3EE">${esc(f.cli)}</span>` : ''}<span style="font:600 11px system-ui;padding:3px 9px;border-radius:99px;border:1px solid ${c};color:${c}">${esc(f.conta || '')}</span>${f.qid ? `<label style="font:500 11px system-ui;opacity:.7;display:inline-flex;gap:4px;align-items:center;cursor:pointer"><input type="checkbox" data-qid="${f.qid}" checked style="accent-color:#F5C518">no quadro</label>` : ''}</div></div></div>`; }).join('')}
    </div>`; }).join('');
}
document.addEventListener('change', e => { const id = e.target && e.target.dataset && e.target.dataset.qid; if (id) marca(id, e.target.checked); });
document.addEventListener('click', e => { const b = e.target.closest && e.target.closest('[data-qf]'); if (b) { filtro = b.dataset.qf; render(); } });
if (location.hash === '#quadro') setTimeout(render, 50);
})();

