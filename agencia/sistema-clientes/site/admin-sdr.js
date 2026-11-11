// Tela "SDR · Prospecção" do painel do ADMINISTRADOR (pedido do Lindson, 11/11/2026).
// Lista com os contatos de functions/_sdr.js (nota >= 80) vinda de /api/sdr. Botões Instagram e WhatsApp: copiam/abrem a mensagem
// e, ao enviar, o contato sai da lista e entra na esteira (Enviado → Respondeu → Reunião → Proposta → Fechado / Perdido).
// A extensão usa a mesma rota (/api/sdr?lote=20), então o que ela envia aparece aqui. Entra no admin depois do admin-sistema.js.
(() => {
const V = window.__V, T = window.__T;
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const render = () => window.__render && window.__render(), toast = t => window.__toast && window.__toast(t);
const NOMES = { enviado: 'Enviado', respondeu: 'Respondeu', reuniao: 'Reunião marcada', proposta: 'Proposta enviada', fechado: 'Fechado', perdido: 'Perdido' };
const ESTEIRA = ['enviado', 'respondeu', 'reuniao', 'proposta', 'fechado', 'perdido'];
let C = [], carregou = false, aba = 'disparo', busca = '', feitosLote = 0;
async function carrega() {
  try { const r = await fetch('/api/sdr'); if (r.ok) C = (await r.json()).contatos || []; else toast('Não carregou a lista do SDR.'); } catch (e) { toast('Sem conexão.'); }
  carregou = true; render();
}
async function salva(id, corpo) {
  const c = C.find(x => x.id === id); if (!c) return;
  const antes = { ...c }; Object.assign(c, { etapa: corpo.etapa || 'enviado' }, corpo.canal ? { canal: corpo.canal } : {}); render();
  try { const r = await fetch('/api/sdr', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ id, ...corpo }) });
    if (!r.ok) throw 0; Object.assign(c, await r.json()); render(); }
  catch (e) { Object.assign(c, antes); render(); toast('Não salvou. Tente de novo.'); }
}
const copia = t => { try { navigator.clipboard.writeText(t); } catch (e) {} };
function envia(id, canal) {
  const c = C.find(x => x.id === id); if (!c) return;
  if (canal === 'whatsapp') window.open('https://wa.me/' + c.wa + '?text=' + encodeURIComponent(c.msg), '_blank', 'noopener');
  else { copia(c.msg); window.open('https://ig.me/m/' + encodeURIComponent(c.ig), '_blank', 'noopener'); toast('Mensagem copiada: cole no Direct'); }
  feitosLote++; salva(id, { acao: 'enviado', canal });
}
const kpi = (r, v, n) => `<div class="card kpi"><div class="rot">${r}</div><div class="val">${v}</div><div class="var up"><span>${n || ''}</span></div></div>`;
const tag = (t, bg = '#2a2a2a', cor = '#F5F3EE') => `<span style="font:600 11px system-ui;padding:3px 8px;border-radius:99px;background:${bg};color:${cor}">${esc(t)}</span>`;
const linha = c => `<div class="card" style="padding:18px 20px;display:grid;gap:10px">
  <div style="display:flex;justify-content:space-between;gap:10px;align-items:start"><div><b style="font-size:16px">${esc(c.nome)}</b>
    <div style="opacity:.7;font-size:13px;margin-top:2px">@${esc(c.ig)} · ${esc(c.nicho)} · ${esc(c.cidade)}</div></div>
    <span style="font:800 18px system-ui;color:#F5C518;white-space:nowrap">${c.nota}<small style="font-size:11px;opacity:.7">/100</small></span></div>
  <div style="font-size:13px;opacity:.85">${esc(c.motivo)}</div>
  <div style="font-size:13px;background:rgba(255,255,255,.04);border-left:2px solid #F5C518;padding:9px 12px;border-radius:6px;white-space:pre-line">${esc(c.msg)}</div>
  <div style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn am" data-sdr-ig="${c.id}">Instagram</button>
    ${c.wa ? `<button class="btn" data-sdr-wa="${c.id}" style="background:#1f3a2a;color:#9BE3B5">WhatsApp</button>` : `<span style="font-size:12px;opacity:.5;align-self:center">sem WhatsApp público</span>`}</div></div>`;
const cartao = c => `<div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:10px;padding:10px 12px;display:grid;gap:6px">
  <b style="font-size:13px">${esc(c.nome)}</b><span style="font-size:12px;opacity:.7">@${esc(c.ig)} · ${c.nota} · ${c.canal === 'whatsapp' ? 'WhatsApp' : 'Instagram'}</span>
  <select data-sdr-et="${c.id}" style="background:#131314;color:inherit;border:1px solid rgba(255,255,255,.15);border-radius:6px;padding:5px;font-size:12px">
    ${ESTEIRA.map(e => `<option value="${e}"${c.etapa === e ? ' selected' : ''}>${NOMES[e]}</option>`).join('')}<option value="novo">↩ Voltar para a lista</option></select></div>`;
T.sdr = 'SDR · Prospecção';
V.sdr = () => {
  if (!carregou) { carrega(); return '<div class="card" style="padding:24px">Carregando contatos…</div>'; }
  const novos = C.filter(c => c.etapa === 'novo').sort((a, b) => b.nota - a.nota), fila = C.filter(c => c.etapa !== 'novo');
  const q = busca.toLowerCase(), vis = novos.filter(c => !q || (c.nome + c.ig + c.nicho + c.cidade).toLowerCase().includes(q));
  const atual = novos[0];
  const disparo = () => !atual ? '<div class="card" style="padding:24px">Lista vazia. 👏</div>' : `<div class="card" style="padding:26px;max-width:620px;display:grid;gap:14px">
    <div style="display:flex;justify-content:space-between;font-size:13px;opacity:.75"><span>Lote: ${feitosLote} de 20 enviados</span><span>${novos.length} na lista</span></div>
    <div style="height:6px;border-radius:99px;background:rgba(255,255,255,.08)"><div style="height:100%;width:${Math.min(feitosLote, 20) * 5}%;background:#F5C518;border-radius:99px"></div></div>
    <div><b style="font-size:22px">${esc(atual.nome)}</b><div style="opacity:.7;font-size:14px;margin-top:4px">@${esc(atual.ig)} · ${esc(atual.nicho)} · ${esc(atual.cidade)} · nota ${atual.nota}</div></div>
    <div style="font-size:15px;background:rgba(255,255,255,.04);border-left:3px solid #F5C518;padding:12px 14px;border-radius:6px;white-space:pre-line">${esc(atual.msg)}</div>
    ${feitosLote >= 20 ? '<div style="font-weight:700;color:#F5C518">Lote de 20 concluído. Faça uma pausa antes do próximo.</div><button class="btn am" data-sdr-novolote="1" style="padding:14px">Começar próximo lote</button>' : `
    <button class="btn" data-sdr-wa="${atual.id}" style="padding:16px;font-size:16px;background:#25D366;color:#0A0A0A">Abrir no WhatsApp e enviar</button>
    <div style="display:flex;gap:8px"><button class="btn" data-sdr-ig="${atual.id}" style="flex:1;padding:12px">Mandar pelo Instagram</button>
    <button class="btn" data-sdr-pula="${atual.id}" style="flex:1;padding:12px;background:#2a2a2a;color:#F5F3EE">Pular (sem WhatsApp / inativo)</button></div>
    <a href="https://www.instagram.com/${encodeURIComponent(atual.ig)}/" target="_blank" rel="noopener" style="font-size:13px;color:#F5C518">Ver o perfil antes</a>`}
    <p style="font-size:12px;opacity:.6;margin:0">No celular, o botão abre o app do WhatsApp com a mensagem pronta: só toque em enviar e volte aqui. O próximo contato já aparece.</p></div>`;
  const chip = (id, t) => `<button class="btn${aba === id ? ' am' : ''}" data-sdr-aba="${id}" style="padding:7px 14px;font-size:13px">${t}</button>`;
  const lote = vis.slice(0, 20);
  return `<div class="grade g4">${kpi('Na lista', novos.length, 'nota 80 ou mais')}${kpi('Enviados', fila.length, 'na esteira')}${kpi('Responderam', fila.filter(c => !['enviado', 'perdido'].includes(c.etapa)).length, '')}${kpi('Fechados', fila.filter(c => c.etapa === 'fechado').length, '')}</div>
  <div style="display:flex;gap:8px;flex-wrap:wrap;margin:18px 0;align-items:center">${chip('disparo', 'Modo disparo')}${chip('lista', 'Lista (' + novos.length + ')')}${chip('esteira', 'Esteira (' + fila.length + ')')}
    ${aba === 'lista' ? `<input id="sdr-busca" placeholder="Buscar nicho, cidade…" value="${esc(busca)}" style="flex:1;min-width:160px;background:#131314;color:inherit;border:1px solid rgba(255,255,255,.15);border-radius:9px;padding:8px 12px">` : ''}</div>
  ${aba === 'disparo' ? disparo() : aba === 'lista'
    ? `<p style="opacity:.7;font-size:13px;margin:0 0 12px">Lote de 20 (maior nota primeiro). Ao enviar, o contato vai para a esteira e o próximo sobe.</p><div class="grade g2" style="align-items:start">${lote.map(linha).join('') || '<div class="card" style="padding:24px">Lista vazia. 👏</div>'}</div>`
    : `<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;align-items:start">${ESTEIRA.map(e => { const l = fila.filter(c => c.etapa === e);
        return `<div class="card" style="padding:14px;display:grid;gap:8px"><h3 style="margin:0;font-size:14px">${NOMES[e]} <span style="opacity:.6">${l.length}</span></h3>${l.map(cartao).join('')}</div>`; }).join('')}</div>`}`;
};
document.addEventListener('click', e => {
  const t = e.target.closest('[data-sdr-ig],[data-sdr-wa],[data-sdr-aba],[data-sdr-pula],[data-sdr-novolote]'); if (!t) return;
  if (t.dataset.sdrNovolote) { feitosLote = 0; render(); }
  else if (t.dataset.sdrPula) salva(t.dataset.sdrPula, { acao: 'etapa', etapa: 'perdido' });
  else if (t.dataset.sdrAba) { aba = t.dataset.sdrAba; render(); }
  else if (t.dataset.sdrIg) envia(t.dataset.sdrIg, 'instagram');
  else envia(t.dataset.sdrWa, 'whatsapp');
});
document.addEventListener('change', e => { const s = e.target.closest('[data-sdr-et]'); if (s) salva(s.dataset.sdrEt, { acao: 'etapa', etapa: s.value }); });
document.addEventListener('input', e => { if (e.target.id === 'sdr-busca') { busca = e.target.value; clearTimeout(window.__sdrT); window.__sdrT = setTimeout(() => { render(); const i = document.getElementById('sdr-busca'); if (i) { i.focus(); i.setSelectionRange(busca.length, busca.length); } }, 250); } });
})();
