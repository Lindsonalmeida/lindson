// Tela "SDR · Prospecção" do painel do ADMINISTRADOR (Lindson 11/11/2026; time de 3 números do robô: conta Pedro, 22/11/2026).
// Cartão por número (nome, estado, visto há X min, enviados hoje/limite, respostas, Pausar/Ligar próprio), coluna SDR nos leads,
// modo disparo manual, lista e esteira. Dados de /api/sdr. Entra no admin depois do admin-sistema.js (montar-site.py e painel-sdr/injetar.py).
// No admin a variável global do robô é ROBO (R já é da rede social): aqui fica tudo dentro do (() => {})().
(() => {
const V = window.__V, T = window.__T;
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const render = () => window.__render && window.__render(), toast = t => window.__toast && window.__toast(t);
const NOMES = { enviado: 'Enviado', respondeu: 'Respondeu', reuniao: 'Reunião marcada', proposta: 'Proposta enviada', fechado: 'Fechado', perdido: 'Perdido' };
const ESTEIRA = ['enviado', 'respondeu', 'reuniao', 'proposta', 'fechado', 'perdido'];
let C = [], carregou = false, aba = 'time', busca = '', feitosLote = 0, ROBOS = {};
const NUMS = ['sdr1', 'sdr2', 'sdr3'];
const minDesde = iso => iso ? Math.max(0, Math.round((Date.now() - new Date(iso)) / 60e3)) : null;
const rotulo = n => 'SDR ' + String(n).slice(3);
const ligado = r => r && r.visto && minDesde(r.visto) < 20;
async function carregaRobos() { try { const r = await fetch('/api/sdr?robo=1'); if (r.ok) ROBOS = (await r.json()).robos || {}; } catch (e) {} if (window.__roboSet && ROBOS.sdr1) window.__roboSet(ROBOS.sdr1); }
async function pausa(n) { const r0 = ROBOS[n] || {}; try { const r = await fetch('/api/sdr', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ acao: 'pausa', numero: n, pausado: !r0.pausado }) }); if (!r.ok) throw 0; ROBOS[n] = Object.assign(r0, await r.json()); toast(r0.pausado ? 'Número pausado.' : 'Número ligado.'); } catch (e) { toast('Não salvou. Tente de novo.'); } render(); }
const cartaoNum = n => { const r = ROBOS[n] || {}, on = ligado(r), m = minDesde(r.visto);
  const cor = r.pausado ? '#f5a623' : on ? '#22c55e' : '#ef4444', est = r.pausado ? 'Pausado' : on ? 'Ligado' : r.visto ? 'Desligado' : 'Ainda não ligou';
  return `<div class="card" style="padding:20px;display:grid;gap:12px">
  <div style="display:flex;justify-content:space-between;align-items:center;gap:10px"><b style="font-size:16px">${esc(r.nome || rotulo(n))}</b>
    <span style="display:flex;align-items:center;gap:6px;font-size:12px;opacity:.85"><span style="width:9px;height:9px;border-radius:50%;background:${cor}"></span>${est}</span></div>
  <div style="font-size:12px;opacity:.65">${m == null ? 'nunca visto · abra o ícone Robô SDR ' + n.slice(3) + ' no PC' : 'visto há ' + (m < 60 ? m + ' min' : Math.round(m / 60) + ' h')}${r.estado ? ' · ' + esc(r.estado) : ''}</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
    <div><div style="font-size:11px;opacity:.6;text-transform:uppercase;letter-spacing:.08em">Enviados hoje</div><div style="font:700 22px system-ui">${r.enviados || 0}<span style="font-size:13px;opacity:.6"> / ${r.limite || 20}</span></div>
      <div style="height:4px;border-radius:99px;background:rgba(255,255,255,.08);margin-top:6px"><div style="height:100%;width:${Math.min(100, ((r.enviados || 0) / (r.limite || 20)) * 100)}%;background:#F5C518;border-radius:99px"></div></div></div>
    <div><div style="font-size:11px;opacity:.6;text-transform:uppercase;letter-spacing:.08em">Respostas</div><div style="font:700 22px system-ui">${r.respostas || 0}</div></div></div>
  <button class="btn${r.pausado ? ' am' : ''}" data-sdr-pausa="${n}" style="padding:10px">${r.pausado ? 'Ligar' : 'Pausar'}</button></div>`; };
async function carrega() {
  carregaRobos();
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
  <b style="font-size:13px">${esc(c.nome)}</b><span style="font-size:12px;opacity:.7">@${esc(c.ig)} · ${c.nota} · ${c.canal === 'whatsapp' ? 'WhatsApp' : 'Instagram'}${c.sdr ? ' · ' + esc(nomeSdr(c.sdr)) : ''}</span>
  <select data-sdr-et="${c.id}" style="background:#131314;color:inherit;border:1px solid rgba(255,255,255,.15);border-radius:6px;padding:5px;font-size:12px">
    ${ESTEIRA.map(e => `<option value="${e}"${c.etapa === e ? ' selected' : ''}>${NOMES[e]}</option>`).join('')}<option value="novo">↩ Voltar para a lista</option></select></div>`;
const nomeSdr = n => (ROBOS[n] && ROBOS[n].nome) || (n ? rotulo(n) : 'Manual');
const ROT = { novo: 'Na lista', reservado: 'Reservado', enviado: 'Enviado', respondeu: 'Respondeu', reuniao: 'Reunião', proposta: 'Proposta', fechado: 'Fechado', perdido: 'Perdido' };
const tabela = l => `<div class="card" style="padding:0;overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:13px;min-width:560px">
  <thead><tr style="text-align:left;opacity:.6;font-size:11px;text-transform:uppercase;letter-spacing:.08em">${['Lead', 'Nicho', 'Etapa', 'SDR', 'Quando'].map(h => `<th style="padding:12px 14px;border-bottom:1px solid rgba(255,255,255,.08)">${h}</th>`).join('')}</tr></thead>
  <tbody>${l.map(c => `<tr><td style="padding:10px 14px;border-bottom:1px solid rgba(255,255,255,.05)"><b>${esc(c.nome)}</b></td><td style="padding:10px 14px;opacity:.75;border-bottom:1px solid rgba(255,255,255,.05)">${esc(c.nicho)}</td>
  <td style="padding:10px 14px;border-bottom:1px solid rgba(255,255,255,.05)">${ROT[c.etapa] || esc(c.etapa)}</td><td style="padding:10px 14px;border-bottom:1px solid rgba(255,255,255,.05)">${c.sdr ? esc(nomeSdr(c.sdr)) : '<span style="opacity:.4">·</span>'}</td>
  <td style="padding:10px 14px;opacity:.6;border-bottom:1px solid rgba(255,255,255,.05)">${c.em ? new Date(c.em).toLocaleDateString('pt-BR') : ''}</td></tr>`).join('')}</tbody></table></div>`;
T.sdr = 'SDR · Prospecção';
V.sdr = () => {
  if (!carregou) { carrega(); return '<div class="card" style="padding:24px">Carregando contatos…</div>'; }
  const novos = C.filter(c => c.etapa === 'novo' || (c.etapa === 'reservado' && Date.parse(c.ate || 0) < Date.now())).sort((a, b) => b.nota - a.nota), fila = C.filter(c => c.etapa !== 'novo' && c.etapa !== 'reservado'), reserv = C.filter(c => c.etapa === 'reservado' && !novos.includes(c));
  const q = busca.toLowerCase(), vis = novos.filter(c => !q || (c.nome + c.ig + c.nicho + c.cidade).toLowerCase().includes(q));
  const atual = novos[0];
  const disparo = () => !atual ? '<div class="card" style="padding:24px">Lista vazia.</div>' : `<div class="card" style="padding:26px;max-width:620px;display:grid;gap:14px">
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
  <div style="display:flex;gap:8px;flex-wrap:wrap;margin:18px 0;align-items:center">${chip('time', 'Time de SDR')}${chip('leads', 'Leads (' + C.length + ')')}${chip('disparo', 'Modo disparo')}${chip('lista', 'Lista (' + novos.length + ')')}${chip('esteira', 'Esteira (' + fila.length + ')')}
    ${aba === 'lista' ? `<input id="sdr-busca" placeholder="Buscar nicho, cidade…" value="${esc(busca)}" style="flex:1;min-width:160px;background:#131314;color:inherit;border:1px solid rgba(255,255,255,.15);border-radius:9px;padding:8px 12px">` : ''}</div>
  ${aba === 'time' ? `<div class="grade g3" style="align-items:start">${NUMS.map(cartaoNum).join('')}</div><p style="opacity:.6;font-size:12px;margin:12px 0 0">Cada número recebe só os leads dele (sem repetir). ${reserv.length} reservado(s) agora. Pausar aqui para o número em até 2 min.</p>` : aba === 'leads' ? tabela([...C].sort((a, b) => String(b.em || '').localeCompare(String(a.em || '')))) : aba === 'disparo' ? disparo() : aba === 'lista'
    ? `<p style="opacity:.7;font-size:13px;margin:0 0 12px">Lote de 20 (maior nota primeiro). Ao enviar, o contato vai para a esteira e o próximo sobe.</p><div class="grade g2" style="align-items:start">${lote.map(linha).join('') || '<div class="card" style="padding:24px">Lista vazia.</div>'}</div>`
    : `<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;align-items:start">${ESTEIRA.map(e => { const l = fila.filter(c => c.etapa === e);
        return `<div class="card" style="padding:14px;display:grid;gap:8px"><h3 style="margin:0;font-size:14px">${NOMES[e]} <span style="opacity:.6">${l.length}</span></h3>${l.map(cartao).join('')}</div>`; }).join('')}</div>`}`;
};
document.addEventListener('click', e => {
  const t = e.target.closest('[data-sdr-ig],[data-sdr-wa],[data-sdr-aba],[data-sdr-pula],[data-sdr-novolote],[data-sdr-pausa]'); if (!t) return;
  if (t.dataset.sdrPausa) { pausa(t.dataset.sdrPausa); return; }
  if (t.dataset.sdrNovolote) { feitosLote = 0; render(); }
  else if (t.dataset.sdrPula) salva(t.dataset.sdrPula, { acao: 'etapa', etapa: 'perdido' });
  else if (t.dataset.sdrAba) { aba = t.dataset.sdrAba; render(); }
  else if (t.dataset.sdrIg) envia(t.dataset.sdrIg, 'instagram');
  else envia(t.dataset.sdrWa, 'whatsapp');
});
document.addEventListener('change', e => { const s = e.target.closest('[data-sdr-et]'); if (s) salva(s.dataset.sdrEt, { acao: 'etapa', etapa: s.value }); });
document.addEventListener('input', e => { if (e.target.id === 'sdr-busca') { busca = e.target.value; clearTimeout(window.__sdrT); window.__sdrT = setTimeout(() => { render(); const i = document.getElementById('sdr-busca'); if (i) { i.focus(); i.setSelectionRange(busca.length, busca.length); } }, 250); } });
setInterval(() => { if (location.hash === '#sdr' && !document.hidden) carregaRobos().then(render); }, 60e3);
})();
