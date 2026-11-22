// Tela "Robôs" do painel do ADMINISTRADOR: todos os robôs e automações num lugar só (pedido do Lindson, 22/11/2026, conta Leandro · Builder).
// Dados: window.__ROBOS (robos.json, gerado por agencia/sistema-clientes/robos/gerar_robos.py) + leitura ao vivo de /api/sdr?robo=1 (time de SDR)
// e /api/agenda-ig (robô do Instagram). Só lê: pausar/ligar os números continua na aba SDR (conta Pedro). Injetado por site/painel-robos/injetar_robos.py.
(() => {
const V = window.__V, T = window.__T; if (!V || !T) return;
const DADOS = window.__ROBOS || { robos: [] };
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const render = () => window.__render && window.__render();
const ST = { erro: ['Com erro', 'er', 'var(--erro)'], atencao: ['Atenção', 'al', 'var(--alerta)'], ativo: ['Ativo', 'ok', 'var(--ok)'], parado: ['Parado', 'ne', 'var(--apagado)'] };
const ORDEM = { erro: 0, atencao: 1, ativo: 2, parado: 3 };
const GRUPOS = ['Vendas', 'Postagem', 'Equipe', 'Central', 'Parados'];
let filtro = 'todos', modo = 'lista', vivoOk = false, carregou = false;
const R = DADOS.robos.map(r => ({ ...r }));
const tz = 3 * 3600e3; // São Luís = UTC-3, sem horário de verão
const quando = iso => { if (!iso) return '—'; const d = new Date(iso), m = Math.round((Date.now() - d) / 60e3);
  if (m < 1) return 'agora'; if (m < 60) return 'há ' + m + ' min'; if (m < 48 * 60) return 'há ' + Math.round(m / 60) + ' h';
  return d.toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit' }) + ' ' + d.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' }); };
const hm = s => { const [h, m] = s.split(':').map(Number); return h * 60 + m; };
function proxima(r) {
  const a = r.agenda; if (!a || r.status === 'parado') return null;
  const local = new Date(Date.now() - tz), base = Date.UTC(local.getUTCFullYear(), local.getUTCMonth(), local.getUTCDate()), agoraMin = local.getUTCHours() * 60 + local.getUTCMinutes();
  for (let d = 0; d < 3; d++) {
    let mins = [];
    if (a.janela) { const i = hm(a.janela[0]), f = hm(a.janela[1]); if (d === 0 && agoraMin >= i && agoraMin < f) return 'agora (no horário)'; mins = [i]; }
    else if (a.horas) mins = a.horas.map(h => h * 60 + a.min);
    else if (a.cada) for (let h = 0; h < 24; h += a.cada) mins.push(h * 60 + a.min);
    const m = mins.find(x => d > 0 || x > agoraMin);
    if (m != null) { const t = new Date(base + d * 864e5 + m * 60e3 + tz); return (d === 0 ? 'hoje ' : d === 1 ? 'amanhã ' : t.toLocaleDateString('pt-BR', { weekday: 'short' }) + ' ') + t.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit', timeZone: 'America/Fortaleza' }); }
  }
  return null;
}
async function vivo() {
  try { const r = await fetch('/api/sdr?robo=1'); if (r.ok) { const j = await r.json(); vivoOk = true;
    Object.entries(j.robos || {}).forEach(([n, v]) => { const x = R.find(y => y.id === n); if (!x) return; const min = v.visto ? (Date.now() - new Date(v.visto)) / 60e3 : null;
      x.ultima = v.visto || x.ultima; x.ultima_msg = (v.estado || '') + (v.enviados != null ? ` · ${v.enviados}/${v.limite || 30} hoje` : '');
      if (v.pausado) { x.status = 'parado'; x.motivo = 'Pausado na aba SDR. Para religar: SDR · Prospecção → Ligar.'; }
      else if (min == null) { x.status = 'erro'; x.motivo = 'Nunca ligou: abra o ícone "Robô SDR ' + n.slice(3) + '" no PC e escaneie o QR do WhatsApp com o celular do chip.'; }
      else if (/qr/i.test(v.estado || '')) { x.status = 'erro'; x.motivo = 'Esperando o QR: escaneie com o WhatsApp do chip ' + n.toUpperCase() + '.'; }
      else if (min > 20) { x.status = 'erro'; x.motivo = 'Desligado há ' + (min < 120 ? Math.round(min) + ' min' : Math.round(min / 60) + ' h') + ': janela fechada, PC desligado ou sem internet. Abra o ícone no PC.'; }
      else { x.status = 'ativo'; x.motivo = ''; } }); } } catch (e) {}
  try { const r = await fetch('/api/agenda-ig'); if (r.ok) { const j = await r.json(), x = R.find(y => y.id === 'robo-ig'); const u = j.ultimo, posts = j.posts || [];
    const ag = posts.filter(p => /agend/.test(p.status || '')).length, err = posts.filter(p => p.status === 'erro').length;
    if (x) { x.ultima = (u && (u.em || u)) || x.ultima; x.ultima_msg = `${ag} agendado(s) na fila`;
      if (err) { x.status = 'erro'; x.motivo = err + ' post(s) com erro na fila do Instagram (veja a aba Rede social).'; }
      else if (x.ultima && (Date.now() - new Date(x.ultima)) < 72 * 3600e3) { x.status = 'ativo'; x.motivo = ''; } } } } catch (e) {}
  carregou = true; render();
}
const kpi = (r, v, nota, cor) => `<div class="card kpi"><div class="rot">${r}</div><div class="val" style="${cor ? 'color:' + cor : ''}">${v}</div><div class="var up"><span>${nota || ''}</span></div></div>`;
const chipSt = s => `<span class="chip ${ST[s][1]}"><span style="width:7px;height:7px;border-radius:50%;background:${ST[s][2]}${s === 'ativo' ? ';box-shadow:0 0 0 3px rgba(92,201,138,.18)' : ''}"></span>${ST[s][0]}</span>`;
const meta = (rot, val) => `<div style="min-width:0"><div style="font:500 10px var(--f-dado);letter-spacing:.18em;text-transform:uppercase;color:var(--apagado)">${rot}</div><div style="font-size:13px;margin-top:3px;overflow-wrap:anywhere">${val}</div></div>`;
const link = r => { const l = []; if (r.link) l.push(`<a class="btn am" href="${esc(r.link)}" style="padding:7px 12px;font-size:12px;text-decoration:none">Abrir</a>`);
  if (r.arquivo_url) l.push(`<a class="btn" href="${esc(r.arquivo_url)}" target="_blank" rel="noopener" style="padding:7px 12px;font-size:12px;text-decoration:none;background:var(--painel2);color:var(--texto);border:1px solid var(--linha)">Como funciona</a>`); return l.join(''); };
const cartao = r => { const p = proxima(r);
  return `<article class="card robo" data-st="${r.status}" style="padding:18px 20px;display:grid;gap:12px;border-left:3px solid ${ST[r.status][2]}">
  <div style="display:flex;justify-content:space-between;gap:12px;align-items:start"><div style="min-width:0"><b style="font-size:15.5px">${esc(r.nome)}</b>
    <div style="font-size:12.5px;color:var(--apagado);margin-top:3px">${esc(r.oque)}</div></div>${chipSt(r.status)}</div>
  ${r.motivo ? `<div style="font-size:13px;padding:9px 12px;border-radius:8px;background:${r.status === 'erro' ? 'rgba(229,96,77,.08)' : r.status === 'atencao' ? 'rgba(242,169,59,.08)' : 'var(--painel2)'};border:1px solid ${r.status === 'erro' ? 'rgba(229,96,77,.25)' : r.status === 'atencao' ? 'rgba(242,169,59,.25)' : 'var(--linha)'}">${esc(r.motivo)}</div>` : ''}
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px 16px">
    ${meta('Onde roda', esc(r.onde))}${meta('Dono', esc(r.dono))}${meta('Frequência', esc(r.freq))}
    ${meta('Última', `<span title="${esc(r.ultima_msg || '')}" style="font-family:var(--f-dado)">${quando(r.ultima)}</span>`)}${meta('Próxima', `<span style="font-family:var(--f-dado)">${p ? esc(p) : r.status === 'parado' ? '—' : 'sob demanda'}</span>`)}</div>
  ${r.ultima_msg ? `<div style="font-size:12px;color:var(--apagado);white-space:nowrap;overflow:hidden;text-overflow:ellipsis">↳ ${esc(r.ultima_msg)}</div>` : ''}
  <div style="display:flex;gap:8px;flex-wrap:wrap">${link(r)}</div></article>`; };
T.robos = 'Robôs';
V.robos = () => {
  if (!carregou) vivo();
  const c = s => R.filter(r => r.status === s).length, prob = c('erro') + c('atencao');
  const sel = R.filter(r => filtro === 'todos' ? true : filtro === 'problema' ? ['erro', 'atencao'].includes(r.status) : r.grupo === filtro).sort((a, b) => ORDEM[a.status] - ORDEM[b.status]);
  const chip = (id, t, n) => `<button class="btn${filtro === id ? ' am' : ''}" data-rb-f="${id}" style="padding:7px 14px;font-size:13px">${t}${n != null ? ` <span style="opacity:.65">${n}</span>` : ''}</button>`;
  const corpo = modo === 'lista' ? `<div class="grade g2" style="align-items:start">${sel.map(cartao).join('') || '<div class="card" style="padding:24px">Nenhum robô neste filtro.</div>'}</div>`
    : `<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;align-items:start">${['erro', 'atencao', 'ativo', 'parado'].map(s => { const l = sel.filter(r => r.status === s);
        return `<div style="display:grid;gap:10px;align-content:start"><h3 style="margin:0;font:700 13px var(--f-corpo);display:flex;gap:8px;align-items:center">${chipSt(s)}<span style="color:var(--apagado)">${l.length}</span></h3>${l.map(cartao).join('') || '<div style="font-size:12px;color:var(--apagado);padding:8px">vazio</div>'}</div>`; }).join('')}</div>`;
  return `<div class="grade g4">${kpi('Robôs e automações', R.length, GRUPOS.length + ' frentes')}${kpi('Ativos', c('ativo'), 'rodando no horário', 'var(--ok)')}${kpi('Com erro', c('erro'), c('atencao') + ' em atenção', c('erro') ? 'var(--erro)' : '')}${kpi('Parados', c('parado'), 'desligados de propósito')}</div>
  ${prob ? `<div class="card" style="padding:14px 18px;margin-top:16px;display:flex;gap:12px;align-items:center;flex-wrap:wrap;border-color:rgba(229,96,77,.3)"><b style="color:var(--erro)">O que destrava</b>
    <span style="font-size:13px;color:#C9C5BA">${R.filter(r => r.status === 'erro').map(r => esc(r.nome)).join(' · ') || '—'}</span></div>` : ''}
  <div style="display:flex;gap:8px;flex-wrap:wrap;margin:18px 0;align-items:center">${chip('todos', 'Todos', R.length)}${chip('problema', 'Com problema', prob)}${GRUPOS.map(g => chip(g, g, R.filter(r => r.grupo === g).length)).join('')}
    <span style="flex:1"></span><button class="btn${modo === 'lista' ? ' am' : ''}" data-rb-m="lista" style="padding:7px 12px;font-size:12px">Lista</button><button class="btn${modo === 'kanban' ? ' am' : ''}" data-rb-m="kanban" style="padding:7px 12px;font-size:12px">Por situação</button></div>
  ${corpo}
  <p style="font-size:12px;color:var(--apagado);margin:16px 0 0">Inventário de ${esc(new Date(DADOS.gerado || Date.now()).toLocaleString('pt-BR', { dateStyle: 'short', timeStyle: 'short' }))}${vivoOk ? ' · time de SDR ao vivo' : ''}. Pausar ou ligar um número: aba SDR · Prospecção. Lista completa: agencia/sistema-clientes/robos/ROBOS.md.</p>`;
};
document.addEventListener('click', e => { const t = e.target.closest('[data-rb-f],[data-rb-m]'); if (!t) return;
  if (t.dataset.rbF) filtro = t.dataset.rbF; else modo = t.dataset.rbM; render(); });
if (location.hash === '#robos') setTimeout(render, 0); // abriu direto em #robos: o render inicial do painel rodou antes deste script
setInterval(() => { if (location.hash === '#robos' && !document.hidden) vivo(); }, 60e3);
})();
