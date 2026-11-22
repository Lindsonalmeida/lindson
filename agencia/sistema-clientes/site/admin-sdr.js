// Tela "SDR · Prospecção" do painel do ADMINISTRADOR (Lindson 11/11/2026; time de 3 números do robô: conta Pedro, 22/11/2026).
// Cartão por número (nome, estado, visto há X min, enviados hoje/limite, respostas, Pausar/Ligar próprio), coluna SDR nos leads,
// modo disparo manual, lista e esteira. Dados de /api/sdr. Entra no admin depois do admin-sistema.js (montar-site.py e painel-sdr/injetar.py).
// No admin a variável global do robô é ROBO (R já é da rede social): aqui fica tudo dentro do (() => {})().
(() => {
const V = window.__V, T = window.__T;
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const render = () => window.__render && window.__render(), toast = t => window.__toast && window.__toast(t);
const NOMES = { enviado: 'Enviado', respondeu: 'Respondeu', qualificado: 'Qualificado', reuniao: 'Reunião marcada', proposta: 'Proposta enviada', fechado: 'Fechado', perdido: 'Perdido' };
const ESTEIRA = ['enviado', 'respondeu', 'qualificado', 'reuniao', 'proposta', 'fechado', 'perdido'];
let C = [], FLUXOS = {}, carregou = false, aba = 'funil', nicho = 'advogados', busca = '', feitosLote = 0, ROBOS = {};
const NUMS = ['sdr1', 'sdr2', 'sdr3'], LIM = 30; // 30/dia por número (robo-sdr/config.json, teto 30 desde 22/11/2026)
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
    <div><div style="font-size:11px;opacity:.6;text-transform:uppercase;letter-spacing:.08em">Enviados hoje</div><div style="font:700 22px system-ui">${r.enviados || 0}<span style="font-size:13px;opacity:.6"> / ${r.limite || LIM}</span></div>
      <div style="height:4px;border-radius:99px;background:rgba(255,255,255,.08);margin-top:6px"><div style="height:100%;width:${Math.min(100, ((r.enviados || 0) / (r.limite || LIM)) * 100)}%;background:var(--vt-ouro);border-radius:99px"></div></div></div>
    <div><div style="font-size:11px;opacity:.6;text-transform:uppercase;letter-spacing:.08em">Respostas</div><div style="font:700 22px system-ui">${r.respostas || 0}</div></div></div>
  <button class="btn${r.pausado ? ' am' : ''}" data-sdr-pausa="${n}" style="padding:10px">${r.pausado ? 'Ligar' : 'Pausar'}</button></div>`; };
async function carrega() {
  carregaRobos();
  try { const r = await fetch('/api/sdr'); if (r.ok) { const j = await r.json(); C = j.contatos || []; FLUXOS = j.fluxos || {}; } else toast('Não carregou a lista do SDR.'); } catch (e) { toast('Sem conexão.'); }
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
    <span style="font:800 18px system-ui;color:var(--vt-ouro);white-space:nowrap">${c.nota}<small style="font-size:11px;opacity:.7">/100</small></span></div>
  <div style="font-size:13px;opacity:.85">${esc(c.motivo)}</div>
  <div style="font-size:13px;background:rgba(255,255,255,.04);border-left:2px solid var(--vt-ouro);padding:9px 12px;border-radius:6px;white-space:pre-line">${esc(c.msg)}</div>
  <div style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn am" data-sdr-ig="${c.id}">Instagram</button>
    ${c.wa ? `<button class="btn" data-sdr-wa="${c.id}" style="background:#1f3a2a;color:#9BE3B5">WhatsApp</button>` : `<span style="font-size:12px;opacity:.5;align-self:center">sem WhatsApp público</span>`}</div></div>`;
const cartao = c => `<div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:10px;padding:10px 12px;display:grid;gap:6px">
  <b style="font-size:13px">${esc(c.nome)}</b><span style="font-size:12px;opacity:.7">@${esc(c.ig)} · ${c.nota} · ${c.canal === 'whatsapp' ? 'WhatsApp' : 'Instagram'}${c.sdr ? ' · ' + esc(nomeSdr(c.sdr)) : ''}</span>
  <select data-sdr-et="${c.id}" style="background:#131314;color:inherit;border:1px solid rgba(255,255,255,.15);border-radius:6px;padding:5px;font-size:12px">
    ${ESTEIRA.map(e => `<option value="${e}"${c.etapa === e ? ' selected' : ''}>${NOMES[e]}</option>`).join('')}<option value="novo">↩ Voltar para a lista</option></select></div>`;
const nomeSdr = n => (ROBOS[n] && ROBOS[n].nome) || (n ? rotulo(n) : 'Manual');
const ROT = { novo: 'Na lista', reservado: 'Reservado', enviado: 'Enviado', respondeu: 'Respondeu', qualificado: 'Qualificado', reuniao: 'Reunião', proposta: 'Proposta', fechado: 'Fechado', perdido: 'Perdido' };
const tabela = l => `<div class="card" style="padding:0;overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:13px;min-width:560px">
  <thead><tr style="text-align:left;opacity:.6;font-size:11px;text-transform:uppercase;letter-spacing:.08em">${['Lead', 'Nicho', 'Etapa', 'SDR', 'Quando'].map(h => `<th style="padding:12px 14px;border-bottom:1px solid rgba(255,255,255,.08)">${h}</th>`).join('')}</tr></thead>
  <tbody>${l.map(c => `<tr><td style="padding:10px 14px;border-bottom:1px solid rgba(255,255,255,.05)"><b>${esc(c.nome)}</b></td><td style="padding:10px 14px;opacity:.75;border-bottom:1px solid rgba(255,255,255,.05)">${esc(c.nicho)}</td>
  <td style="padding:10px 14px;border-bottom:1px solid rgba(255,255,255,.05)">${ROT[c.etapa] || esc(c.etapa)}</td><td style="padding:10px 14px;border-bottom:1px solid rgba(255,255,255,.05)">${c.sdr ? esc(nomeSdr(c.sdr)) : '<span style="opacity:.4">·</span>'}</td>
  <td style="padding:10px 14px;opacity:.6;border-bottom:1px solid rgba(255,255,255,.05)">${c.em ? new Date(c.em).toLocaleDateString('pt-BR') : ''}</td></tr>`).join('')}</tbody></table></div>`;
T.sdr = 'VIRTÙ · Time de prospecção';
// VIRTÙ (identidade em agencia/marca-sdr/, conta Leandro 22/11/2026): abas por nicho, funil kanban e fluxo de cada nicho.
const tira = s => String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
const nichoDe = n => { const t = tira(n); return /vereador|mandato|politic/.test(t) ? 'outros' : /advog|advoc|jurid/.test(t) ? 'advogados' : /barb/.test(t) ? 'barbearias' : /dent|odonto|hof|harmoniza|clinic/.test(t) ? 'hof' : 'outros'; };
const NICHOS = [['advogados', 'Advogados'], ['barbearias', 'Barbearias'], ['hof', 'Clínicas HOF'], ['outros', 'Outros · Orégano']];
const dias = c => (Date.now() - Date.parse(c.enviadoEm || c.em || Date.now())) / 864e5;
// funil: o follow-up D+3/D+6/D+9 é deduzido pelos dias desde o 1º envio de quem ainda está em "enviado" (o robô manda no dia certo)
const FUNIL = [['novo', 'Novo'], ['c1', '1º contato'], ['d3', 'Follow-up D+3'], ['d6', 'Follow-up D+6'], ['d9', 'D+9 · Instagram grátis'], ['respondeu', 'Respondeu'], ['qualificado', 'Qualificado'], ['reuniao', 'Reunião marcada'], ['proposta', 'Proposta'], ['fechado', 'Fechado'], ['perdido', 'Perdido']];
const colDe = c => { if (c.etapa === 'novo' || c.etapa === 'reservado') return 'novo'; if (c.etapa !== 'enviado') return c.etapa; const d = dias(c); return d >= 9 ? 'd9' : d >= 6 ? 'd6' : d >= 3 ? 'd3' : 'c1'; };
const VT = `<style>@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500&family=Inter+Tight:wght@400;500;600&display=swap');#vt{--vt-ob:#0A0A0C;--vt-gr:#141418;--vt-li:rgba(233,230,223,.09);--vt-ouro:#CDB27A;--vt-pl:#E9E6DF;--vt-si:#8FE3CF;color:var(--vt-pl);contain:inline-size;min-width:0;max-width:100%;font-family:'Inter Tight',Inter,system-ui,sans-serif}
#vt .vt-top{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;padding:22px 24px;border:1px solid var(--vt-li);border-radius:16px;background:linear-gradient(180deg,#121216,#0A0A0C);margin-bottom:18px}
#vt .vt-marca{display:flex;align-items:center;gap:14px}#vt .vt-marca b{font:500 26px/1 'Cormorant Garamond',Georgia,serif;letter-spacing:.34em}#vt .vt-marca small{display:block;font-size:10px;letter-spacing:.28em;text-transform:uppercase;opacity:.55;margin-top:6px}
#vt .vt-lim{font-size:12px;opacity:.7;letter-spacing:.04em}#vt .vt-lim b{color:var(--vt-ouro);font-weight:600}
#vt .vt-n{display:flex;gap:0;border-bottom:1px solid var(--vt-li);margin-bottom:18px;overflow-x:auto}#vt .vt-n button{all:unset;cursor:pointer;padding:12px 18px;font-size:13px;letter-spacing:.06em;white-space:nowrap;opacity:.55;border-bottom:1px solid transparent;margin-bottom:-1px}
#vt .vt-n button.on{opacity:1;border-color:var(--vt-ouro);color:var(--vt-ouro)}#vt .vt-n button span{opacity:.6;margin-left:6px;font-size:11px}
#vt .vt-k{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px;margin-bottom:18px}#vt .vt-k div{border:1px solid var(--vt-li);border-radius:12px;padding:14px 16px;background:var(--vt-gr)}
#vt .vt-k small{display:block;font-size:10px;letter-spacing:.16em;text-transform:uppercase;opacity:.55}#vt .vt-k b{display:block;font:400 30px/1.1 'Cormorant Garamond',Georgia,serif;margin-top:6px}
#vt .vt-s{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:16px}#vt .vt-s button{all:unset;cursor:pointer;font-size:12px;padding:7px 13px;border:1px solid var(--vt-li);border-radius:99px;opacity:.7}#vt .vt-s button.on{opacity:1;border-color:var(--vt-ouro);color:var(--vt-ouro)}
#vt .vt-kb{display:grid;grid-auto-flow:column;grid-auto-columns:210px;gap:10px;overflow-x:auto;padding-bottom:10px}#vt .vt-col{border:1px solid var(--vt-li);border-radius:12px;padding:12px;background:var(--vt-gr);display:grid;gap:8px;align-content:start;min-height:120px}
#vt .vt-col h3{margin:0 0 4px;font:600 11px system-ui;letter-spacing:.14em;text-transform:uppercase;opacity:.7;display:flex;justify-content:space-between}#vt .vt-col h3 span{color:var(--vt-ouro)}
#vt .vt-c{border:1px solid var(--vt-li);border-radius:9px;padding:9px 10px;font-size:12px;display:grid;gap:3px;background:#0E0E11}#vt .vt-c b{font-size:13px;font-weight:600}#vt .vt-c span{opacity:.6}
#vt .vt-f{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}#vt .vt-f section{border:1px solid var(--vt-li);border-radius:12px;padding:16px 18px;background:var(--vt-gr)}
#vt .vt-f h4{margin:0 0 8px;font:600 10px system-ui;letter-spacing:.18em;text-transform:uppercase;color:var(--vt-ouro)}#vt .vt-f p{margin:0;font-size:13px;line-height:1.55;opacity:.88}
@media(max-width:760px){#vt .vt-k{grid-template-columns:repeat(2,minmax(0,1fr))}#vt .vt-top{padding:18px}#vt .vt-marca b{font-size:22px}}</style>`;
const LOGO = `<svg width="34" height="34" viewBox="0 0 64 64" fill="none" aria-hidden="true"><path d="M10 12 32 54 54 12" stroke="#CDB27A" stroke-width="2.4"/><path d="M21 12 32 34 43 12" stroke="#E9E6DF" stroke-width="1.2" opacity=".55"/><circle cx="32" cy="54" r="2.6" fill="#8FE3CF"/></svg>`;
const funil = l => `<div class="vt-kb">${FUNIL.map(([k, t]) => { const x = l.filter(c => colDe(c) === k).sort((a, b) => (b.nota || 0) - (a.nota || 0));
  return `<div class="vt-col"><h3>${t}<span>${x.length}</span></h3>${x.slice(0, 40).map(c => `<div class="vt-c"><b>${esc(c.nome)}</b><span>@${esc(c.ig)} · ${esc(c.cidade || '')}</span><span>${c.sdr ? esc(nomeSdr(c.sdr)) + ' · ' : ''}nota ${c.nota || '·'}</span>${k !== 'novo' ? `<select data-sdr-et="${c.id}" style="margin-top:4px;background:#0A0A0C;color:inherit;border:1px solid rgba(233,230,223,.15);border-radius:6px;padding:4px;font-size:11px">${ESTEIRA.map(e => `<option value="${e}"${c.etapa === e ? ' selected' : ''}>${NOMES[e]}</option>`).join('')}<option value="novo">↩ Voltar para a lista</option></select>` : ''}</div>`).join('')}${x.length > 40 ? `<span style="font-size:11px;opacity:.5">+${x.length - 40}</span>` : ''}</div>`; }).join('')}</div>`;
const fluxo = () => { const f = FLUXOS[nicho]; if (!f) return '<div class="card" style="padding:24px">Fluxo carregando (vem de /api/sdr).</div>';
  const b = (h, t) => `<section><h4>${h}</h4><p>${esc(t)}</p></section>`;
  return `<div class="vt-f">${b('Oferta', f.oferta)}${b('Regra do nicho', f.regra)}${b('1º contato', f.abertura)}${b('Follow-up D+3', 'Passo de novo rapidinho: mais gente te achar e chamar no WhatsApp sem gastar seu tempo. Posso te mostrar em 2 minutos?')}${b('Follow-up D+6', 'Quem não aparece bem no Google e no Instagram perde o cliente para o vizinho. Faz sentido conversar uns minutinhos?')}${b('D+9 · último', 'Presente: organizo o Instagram de graça (bio, destaques, primeira impressão), sem compromisso.')}${b('Qualificação 1', f.q1)}${b('Qualificação 2', f.q2)}${b('Reunião', f.horario)}
  <section style="grid-column:1/-1"><h4>Objeções</h4>${(f.objecoes || []).map(([o, r]) => `<p style="margin:0 0 8px"><b style="color:var(--vt-pl)">${esc(o)}</b> · ${esc(r)}</p>`).join('')}</section></div>`; };
V.sdr = () => {
  if (!carregou) { carrega(); return '<div class="card" style="padding:24px">Carregando contatos…</div>'; }
  const TODOS = C, porN = k => TODOS.filter(c => nichoDe(c.nicho) === k);
  const C0 = porN(nicho);
  const novos = C0.filter(c => c.etapa === 'novo' || (c.etapa === 'reservado' && Date.parse(c.ate || 0) < Date.now())).sort((a, b) => b.nota - a.nota), fila = C0.filter(c => c.etapa !== 'novo' && c.etapa !== 'reservado'), reserv = TODOS.filter(c => c.etapa === 'reservado' && !novos.includes(c));
  const q = busca.toLowerCase(), vis = novos.filter(c => !q || (c.nome + c.ig + c.nicho + c.cidade).toLowerCase().includes(q));
  const atual = novos[0];
  const disparo = () => !atual ? '<div class="card" style="padding:24px">Lista vazia.</div>' : `<div class="card" style="padding:26px;max-width:620px;display:grid;gap:14px">
    <div style="display:flex;justify-content:space-between;font-size:13px;opacity:.75"><span>Lote: ${feitosLote} de ${LIM} enviados</span><span>${novos.length} na lista</span></div>
    <div style="height:6px;border-radius:99px;background:rgba(255,255,255,.08)"><div style="height:100%;width:${Math.min(100, feitosLote / LIM * 100)}%;background:var(--vt-ouro);border-radius:99px"></div></div>
    <div><b style="font-size:22px">${esc(atual.nome)}</b><div style="opacity:.7;font-size:14px;margin-top:4px">@${esc(atual.ig)} · ${esc(atual.nicho)} · ${esc(atual.cidade)} · nota ${atual.nota}</div></div>
    <div style="font-size:15px;background:rgba(255,255,255,.04);border-left:3px solid var(--vt-ouro);padding:12px 14px;border-radius:6px;white-space:pre-line">${esc(atual.msg)}</div>
    ${feitosLote >= LIM ? '<div style="font-weight:700;color:var(--vt-ouro)">Lote de 30 concluído. Faça uma pausa antes do próximo.</div><button class="btn am" data-sdr-novolote="1" style="padding:14px">Começar próximo lote</button>' : `
    <button class="btn" data-sdr-wa="${atual.id}" style="padding:16px;font-size:16px;background:#25D366;color:#0A0A0A">Abrir no WhatsApp e enviar</button>
    <div style="display:flex;gap:8px"><button class="btn" data-sdr-ig="${atual.id}" style="flex:1;padding:12px">Mandar pelo Instagram</button>
    <button class="btn" data-sdr-pula="${atual.id}" style="flex:1;padding:12px;background:#2a2a2a;color:#F5F3EE">Pular (sem WhatsApp / inativo)</button></div>
    <a href="https://www.instagram.com/${encodeURIComponent(atual.ig)}/" target="_blank" rel="noopener" style="font-size:13px;color:var(--vt-ouro)">Ver o perfil antes</a>`}
    <p style="font-size:12px;opacity:.6;margin:0">No celular, o botão abre o app do WhatsApp com a mensagem pronta: só toque em enviar e volte aqui. O próximo contato já aparece.</p></div>`;
  const chip = (id, t) => `<button class="${aba === id ? 'on' : ''}" data-sdr-aba="${id}">${t}</button>`;
  const resp = fila.filter(c => !['enviado', 'perdido'].includes(c.etapa)).length, fech = fila.filter(c => c.etapa === 'fechado').length;
  const kp = (t, v) => `<div><small>${t}</small><b>${v}</b></div>`;
  const hojeEnv = NUMS.reduce((a, n) => a + ((ROBOS[n] || {}).enviados || 0), 0);
  const lote = vis.slice(0, LIM);
  return `${VT}<div id="vt"><div class="vt-top"><div class="vt-marca">${LOGO}<div><b>VIRTÙ</b><small>Time de prospecção · 3 SDRs</small></div></div>
    <div class="vt-lim">Hoje <b>${hojeEnv}</b> de <b>${LIM * NUMS.length}</b> · ${LIM} por número/dia · intervalo 4 a 11 min</div></div>
  <div class="vt-n">${NICHOS.map(([k, t]) => `<button class="${nicho === k ? 'on' : ''}" data-sdr-nicho="${k}">${t}<span>${porN(k).length}</span></button>`).join('')}</div>
  <div class="vt-k">${kp('Na lista', novos.length)}${kp('Enviados', fila.length)}${kp('Responderam', resp)}${kp('Reunião', fila.filter(c => c.etapa === 'reuniao').length)}${kp('Fechados', fech)}${kp('Taxa de resposta', fila.length ? Math.round(resp / fila.length * 100) + '%' : '·')}</div>
  <div class="vt-s">${chip('funil', 'Funil')}${chip('fluxo', 'Fluxo do nicho')}${chip('time', 'Time de SDR')}${chip('leads', 'Leads (' + C0.length + ')')}${chip('disparo', 'Modo disparo')}${chip('lista', 'Lista (' + novos.length + ')')}${chip('esteira', 'Esteira (' + fila.length + ')')}
    ${aba === 'lista' ? `<input id="sdr-busca" placeholder="Buscar nicho, cidade…" value="${esc(busca)}" style="flex:1;min-width:160px;background:#131314;color:inherit;border:1px solid rgba(255,255,255,.15);border-radius:9px;padding:8px 12px">` : ''}</div>
  ${aba === 'funil' ? funil(C0) : aba === 'fluxo' ? fluxo() : aba === 'time' ? `<div class="grade g3" style="align-items:start">${NUMS.map(cartaoNum).join('')}</div><p style="opacity:.6;font-size:12px;margin:12px 0 0">Cada número recebe só os leads dele (sem repetir). ${reserv.length} reservado(s) agora. Pausar aqui para o número em até 2 min.</p>` : aba === 'leads' ? tabela([...C0].sort((a, b) => String(b.em || '').localeCompare(String(a.em || '')))) : aba === 'disparo' ? disparo() : aba === 'lista'
    ? `<p style="opacity:.7;font-size:13px;margin:0 0 12px">Lote de 30 (maior nota primeiro). Ao enviar, o contato vai para a esteira e o próximo sobe.</p><div class="grade g2" style="align-items:start">${lote.map(linha).join('') || '<div class="card" style="padding:24px">Lista vazia.</div>'}</div>`
    : `<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;align-items:start">${ESTEIRA.map(e => { const l = fila.filter(c => c.etapa === e);
        return `<div class="card" style="padding:14px;display:grid;gap:8px"><h3 style="margin:0;font-size:14px">${NOMES[e]} <span style="opacity:.6">${l.length}</span></h3>${l.map(cartao).join('')}</div>`; }).join('')}</div>`}</div>`;
};
document.addEventListener('click', e => {
  const t = e.target.closest('[data-sdr-ig],[data-sdr-wa],[data-sdr-aba],[data-sdr-nicho],[data-sdr-pula],[data-sdr-novolote],[data-sdr-pausa]'); if (!t) return;
  if (t.dataset.sdrNicho) { nicho = t.dataset.sdrNicho; render(); return; }
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
