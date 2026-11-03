// Ferramentas de gestão do painel do cliente: CRM, Financeiro e Notícias do nicho.
// Genérico: a configuração de cada cliente vem em window.__FERR (montada pelo montar-<cliente>.py).
// Dados salvos no servidor (/api/dados, KV da Cloudflare) por cliente; o admin vê todos. Fora do site (arquivo local), salva neste aparelho.
// Regra dos funis: cada contato tem o botão WhatsApp com a mensagem da etapa pronta; ao tocar, registra o envio e avança a etapa.
// Conta Lindson, 01/11/2026.
(() => {
const F = window.__FERR; if (!F) return;
// Palavras da tela (padrão = clínica). Outro tipo de negócio troca em F.palavras (ex.: desentupidora: cliente, visita, serviço).
const W = Object.assign({ pac: 'paciente', Pac: 'Paciente', pacs: 'pacientes', aval: 'avaliação', Aval: 'Avaliação', avals: 'avaliações', Avals: 'Avaliações', proc: 'procedimento', Proc: 'Procedimento', procs: 'Procedimentos', fezProc: 'Fizeram procedimento', marcaram: 'Marcaram avaliação', tinhaAval: 'de quem tinha avaliação marcada', negocio: 'a clínica', crm: 'CRM de pacientes', regra: 'As mensagens seguem as regras do CFO: sem preço, sem promoção e sem promessa de resultado.' }, F.palavras || {});
const H = window.__h, V = window.__V, T = window.__T, cli = H.cli(), chip = H.chip;
const toast = t => window.__toast(t), render = () => window.__render();
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const uid = () => Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
const agora = () => new Date().toISOString();
const hojeISO = () => { const d = new Date(); d.setMinutes(d.getMinutes() - d.getTimezoneOffset()); return d.toISOString().slice(0, 10); };
const mesISO = (d = hojeISO()) => d.slice(0, 7);
const dataBR = iso => iso ? iso.slice(0, 10).split('-').reverse().join('/') : '';
const brl = n => (+n || 0).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
const MESES = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'];
const nomeMes = m => { const [a, n] = m.split('-'); return MESES[+n - 1][0].toUpperCase() + MESES[+n - 1].slice(1) + '/' + a; };
const somaMes = (m, k) => { const d = new Date(+m.slice(0, 4), +m.slice(5) - 1 + k, 1); return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0'); };
const somaDias = (iso, n) => { const d = new Date(iso.slice(0, 10) + 'T12:00:00'); d.setDate(d.getDate() + n); return d.toISOString().slice(0, 10); };
const quando = dt => { if (!dt) return ''; const d = new Date(dt); if (isNaN(d)) return ''; return d.toLocaleDateString('pt-BR', { weekday: 'long', day: '2-digit', month: '2-digit' }) + (dt.length > 10 ? ' às ' + d.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' }).replace(':00', 'h').replace(':', 'h') : ''); };

document.head.insertAdjacentHTML('beforeend', `<style>
.fr-barra{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:14px}
.fr-barra input,.fr-barra select,.fr-form input,.fr-form select,.fr-form textarea{background:var(--painel2);color:var(--texto);border:1px solid var(--linha);border-radius:9px;padding:9px 11px;font:500 14px var(--f-corpo);min-width:0}
.fr-barra input[type=search]{flex:1 1 200px}
.fr-funil{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(158px,1fr);gap:12px;overflow-x:auto;padding-bottom:8px}
.fr-col{background:var(--painel);border:1px solid var(--linha);border-radius:14px;padding:12px;display:flex;flex-direction:column;gap:10px;min-height:120px}
.fr-col h4{margin:0;display:flex;justify-content:space-between;font:700 12px var(--f-corpo);letter-spacing:.08em;text-transform:uppercase;color:var(--amarelo)}
.fr-card{background:var(--painel2);border:1px solid var(--linha);border-radius:11px;padding:11px;display:grid;gap:7px;cursor:pointer}
.fr-card:hover{border-color:var(--amarelo)}
.fr-card .n{font-weight:700}.fr-card .d{font-size:12px;color:var(--apagado)}
.fr-card .ac{display:flex;flex-wrap:wrap;gap:6px}.fr-card .ac .btn{padding:7px 9px;font-size:12px;flex:1}
.btn.wa{background:#25D366;color:#06210f}.btn.wa:hover{filter:brightness(1.08)}
.fr-tog{display:inline-flex;border:1px solid var(--linha);border-radius:9px;overflow:hidden}.fr-tog button{background:none;border:0;color:var(--apagado);padding:8px 12px;font:700 12px var(--f-corpo);cursor:pointer}.fr-tog button[aria-pressed=true]{background:var(--amarelo);color:#140608}
.fr-modal{position:fixed;inset:0;background:rgba(0,0,0,.6);display:grid;place-items:center;z-index:60;padding:16px}
.fr-caixa{background:var(--painel);border:1px solid var(--linha);border-radius:16px;width:min(560px,100%);max-height:92vh;overflow:auto;padding:20px}
.fr-caixa h3{margin:0 0 12px}
.fr-form{display:grid;grid-template-columns:1fr 1fr;gap:10px}.fr-form label{display:grid;gap:5px;font:600 12px var(--f-corpo);color:var(--apagado)}.fr-form .inteiro{grid-column:1/-1}
.fr-form textarea{min-height:70px;resize:vertical}
.fr-acoes{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.fr-hist{font-size:12px;color:var(--apagado);display:grid;gap:4px;margin-top:12px;max-height:140px;overflow:auto}
.fr-val.e{color:var(--ok)}.fr-val.s{color:var(--erro)}
.fr-bar{height:8px;border-radius:99px;background:var(--painel2);overflow:hidden}.fr-bar i{display:block;height:100%;background:var(--amarelo)}
.fr-bar.s i{background:var(--erro)}
.fr-noticia{display:grid;gap:6px;padding:14px 0;border-bottom:1px solid var(--linha)}.fr-noticia:last-child{border-bottom:0}
.fr-noticia a.t{color:var(--texto);font-weight:700;text-decoration:none}.fr-noticia a.t:hover{color:var(--amarelo)}
.fr-chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:12px}.fr-chips button{border:1px solid var(--linha);background:none;color:var(--texto);border-radius:99px;padding:7px 13px;font:600 12px var(--f-corpo);cursor:pointer}.fr-chips button[aria-pressed=true]{background:var(--amarelo);color:#140608;border-color:var(--amarelo)}
.fr-salvo{font:600 11px var(--f-corpo);color:var(--apagado)}
@media(max-width:620px){.fr-form{grid-template-columns:1fr}}
</style>`);

// ---------- armazenamento: servidor (KV) com junção por item; fora do site, neste aparelho ----------
const S = {};
const chaveLocal = f => `ferr-${cli}-${f}`;
const vazio = f => f === 'crm' ? { itens: [], apagados: [] } : { itens: [], apagados: [], meta: 0 };
async function carregar(f) {
  S[f] = { dados: vazio(f), versao: 0, remoto: false, pronto: false };
  try {
    const r = await fetch(`/api/dados?cli=${cli}&f=${f}`, { headers: { Accept: 'application/json' } });
    if (r.status === 401) toast('Sua sessão expirou. Entre de novo na Central.');
    if (r.ok && (r.headers.get('content-type') || '').includes('json')) {
      const j = await r.json(); S[f] = { dados: j.dados || vazio(f), versao: j.versao || 0, remoto: true, pronto: true }; return;
    }
  } catch (e) {}
  try { const l = JSON.parse(localStorage.getItem(chaveLocal(f)) || 'null'); if (l) S[f].dados = l; } catch (e) {}
  S[f].pronto = true;
}
function juntar(a, b) {
  if (!b) return a; if (!a) return b;
  const ap = new Set([...(a.apagados || []), ...(b.apagados || [])]), m = new Map();
  for (const x of [...(b.itens || []), ...(a.itens || [])]) { const o = m.get(x.id); if (!o || (x.em || '') >= (o.em || '')) m.set(x.id, x); }
  return { ...b, ...a, itens: [...m.values()].filter(x => !ap.has(x.id)), apagados: [...ap].slice(-1000) };
}
let estadoSalvo = '';
function salvar(f) {
  try { localStorage.setItem(chaveLocal(f), JSON.stringify(S[f].dados)); } catch (e) {}
  if (!S[f].remoto) return;
  estadoSalvo = 'Salvando…'; const el = document.getElementById('fr-salvo'); if (el) el.textContent = estadoSalvo;
  clearTimeout(S[f].t); S[f].t = setTimeout(() => enviar(f, 0), 400);
}
async function enviar(f, tent) {
  const s = S[f];
  try {
    const r = await fetch(`/api/dados?cli=${cli}&f=${f}`, { method: 'PUT', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ dados: s.dados, versao: s.versao }) });
    if (r.ok) { s.versao = (await r.json()).versao; estadoSalvo = 'Salvo ' + new Date().toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' }); }
    else if (r.status === 409 && tent < 4) { const srv = await r.json(); s.dados = juntar(s.dados, srv.dados); s.versao = srv.versao; return enviar(f, tent + 1); }
    else { estadoSalvo = 'Não salvou'; toast(r.status === 401 ? 'Sua sessão expirou. Entre de novo para salvar.' : 'Não consegui salvar agora. Tente de novo.'); }
  } catch (e) { estadoSalvo = 'Sem internet: não salvou'; toast('Sem internet. A alteração não foi salva no servidor.'); }
  const el = document.getElementById('fr-salvo'); if (el) el.textContent = estadoSalvo;
}
const statusSalvo = f => `<span class="fr-salvo" id="fr-salvo">${S[f] && S[f].remoto ? (estadoSalvo || 'Salvo no servidor') : 'Salvo neste aparelho'}</span>`;
Promise.all([carregar('crm'), carregar('fin')]).then(() => { window.__crmResumo = resumoCRM; render(); });

// ---------- modal ----------
function modal(html, liga) {
  fecha(); document.body.insertAdjacentHTML('beforeend', `<div class="fr-modal" id="fr-modal" role="dialog" aria-modal="true"><div class="fr-caixa">${html}</div></div>`);
  const m = document.getElementById('fr-modal');
  m.addEventListener('click', e => { if (e.target === m || e.target.closest('[data-fecha]')) fecha(); });
  document.addEventListener('keydown', escFecha); liga(m); const p = m.querySelector('input,select,textarea'); if (p) p.focus();
}
function escFecha(e) { if (e.key === 'Escape') fecha(); }
function fecha() { const m = document.getElementById('fr-modal'); if (m) m.remove(); document.removeEventListener('keydown', escFecha); }
const opts = (l, v) => l.map(o => `<option ${o === v ? 'selected' : ''}>${esc(o)}</option>`).join('');

// =====================================================================
// CRM
// =====================================================================
const ET = F.etapas, etapa = id => ET.find(e => e.id === id) || ET[0];
const crm = () => S.crm.dados.itens;
const fone = w => { let d = String(w || '').replace(/\D/g, ''); if (d.length >= 10 && d.length <= 11) d = '55' + d; return /^55\d{10,11}$/.test(d) ? d : ''; };
const primeiroNome = n => String(n || '').trim().split(/\s+/)[0] || '';
function mensagem(p) {
  const e = etapa(p.etapa);
  let t = (e.msg || '').replace(/\{nome\}/g, primeiroNome(p.nome)).replace(/\{interesse\}/g, (p.interesse || 'a sua avaliação').toLowerCase())
    .replace(/\{quando\}/g, quando(p.avaliacao) || 'no horário combinado').replace(/\{negocio\}/g, F.negocio).replace(/\{google\}/g, F.linkGoogle || '');
  return t.replace(/\s+\n/g, '\n').trim();
}
function resumoCRM() {
  const m = mesISO(), it = crm(), doMes = it.filter(p => (p.criado || '').startsWith(m));
  const marcadas = it.filter(p => p.etapa === 'marcada').length;
  const passadas = it.filter(p => p.avaliacao && p.avaliacao.slice(0, 10) < hojeISO() && ['marcada', 'compareceu', 'fez', 'retorno', 'perdido'].includes(p.etapa));
  const vieram = passadas.filter(p => ['compareceu', 'fez', 'retorno'].includes(p.etapa)).length;
  const procMes = it.filter(p => (p.dataProc || '').startsWith(m));
  return { contatosMes: doMes.length, comCodigo: doMes.filter(p => /^\[/.test(p.origem || '')).length, marcadas, comparecimento: passadas.length ? Math.round(vieram / passadas.length * 100) + '%' : 'a medir',
    procedimentos: procMes.length, valorMes: procMes.reduce((a, p) => a + (+p.valor || 0), 0), retornosVencidos: it.filter(p => p.etapa === 'retorno' && p.retorno && p.retorno <= hojeISO()).length };
}
let crmModo = 'funil', crmBusca = '', crmOrigem = '';
function filtrados() {
  const b = crmBusca.toLowerCase();
  return crm().filter(p => (!crmOrigem || p.origem === crmOrigem) && (!b || (p.nome + ' ' + p.whats + ' ' + p.interesse + ' ' + (p.notas || '')).toLowerCase().includes(b)));
}
function botaoWa(p) {
  const f = fone(p.whats), msg = mensagem(p);
  if (!msg) return '';
  return f ? `<a class="btn wa" href="https://wa.me/${f}?text=${encodeURIComponent(msg)}" target="_blank" rel="noopener" data-wa="${p.id}">WhatsApp</a>`
    : `<button class="btn lin" type="button" data-copia-msg="${p.id}">Copiar mensagem</button>`;
}
function cartao(p) {
  const e = etapa(p.etapa), prox = ET[ET.indexOf(e) + 1];
  let extra = '';
  if (p.etapa === 'marcada' && p.avaliacao) extra = `Avaliação: ${esc(quando(p.avaliacao))}`;
  else if (p.etapa === 'retorno' && p.retorno) extra = (p.retorno <= hojeISO() ? '⚠ Retorno vencido · ' : 'Retorno em ') + dataBR(p.retorno);
  else if (p.etapa === 'conversa') extra = `${p.toques || 0} mensagem(ns) enviada(s)`;
  return `<div class="fr-card" data-abre="${p.id}"><div class="n">${esc(p.nome)}</div><div class="d">${esc(p.interesse || '')}${p.origem ? ' · ' + esc(p.origem) : ''}</div>${extra ? `<div class="d">${extra}</div>` : ''}
   <div class="ac">${botaoWa(p)}${prox && !['perdido'].includes(prox.id) && e.id !== 'retorno' ? `<button class="btn lin" type="button" data-avanca="${p.id}" title="Mover para ${esc(prox.nome)}">${esc(e.botao || prox.nome)} ›</button>` : ''}</div></div>`;
}
V.crm = () => {
  if (!S.crm || !S.crm.pronto) return `<div class="card"><p class="sub">Carregando os ${W.pacs}…</p></div>`;
  const R = resumoCRM(), l = filtrados(), origens = [...new Set([...F.origens, ...crm().map(p => p.origem).filter(Boolean)])];
  const kpi = (r, v, n) => `<div class="card kpi"><div class="rot">${r}</div><div class="val">${v}</div><div class="var up"><span>${n}</span></div></div>`;
  const porOrigem = origens.map(o => { const g = crm().filter(p => p.origem === o); if (!g.length) return ''; const av = g.filter(p => ['marcada', 'compareceu', 'fez', 'retorno'].includes(p.etapa)).length, fz = g.filter(p => ['fez', 'retorno'].includes(p.etapa)).length;
    return `<tr><td>${esc(o)}</td><td>${g.length}</td><td>${av} (${Math.round(av / g.length * 100)}%)</td><td>${fz}</td></tr>`; }).join('');
  const corpo = crmModo === 'funil'
    ? `<div class="fr-funil">${ET.filter(e => e.id !== 'perdido').map(e => { const g = l.filter(p => p.etapa === e.id); return `<div class="fr-col"><h4>${esc(e.nome)} <span>${g.length}</span></h4>${g.map(cartao).join('') || '<div class="d" style="font-size:12px;color:var(--apagado)">Ninguém aqui.</div>'}</div>`; }).join('')}</div>
       <p class="sub" style="margin-top:10px">Não seguiram: ${l.filter(p => p.etapa === 'perdido').length} · <a href="#crm" data-modo="lista" style="color:var(--amarelo)">ver na lista</a></p>`
    : `<div class="card"><div class="tab"><table><thead><tr><th>${W.Pac}</th><th>Interesse</th><th>Origem</th><th>Etapa</th><th>${W.Aval}</th><th></th></tr></thead><tbody>${l.slice().sort((a, b) => (b.em || '').localeCompare(a.em || '')).map(p => `<tr data-abre="${p.id}" style="cursor:pointer"><td><b>${esc(p.nome)}</b><br><span class="d" style="font-size:12px;color:var(--apagado)">${esc(p.whats || 'sem WhatsApp')}</span></td><td>${esc(p.interesse || '')}</td><td>${esc(p.origem || '')}</td><td>${chip(etapa(p.etapa).nome)}</td><td>${esc(p.avaliacao ? quando(p.avaliacao) : '')}</td><td>${botaoWa(p)}</td></tr>`).join('') || `<tr><td colspan="6">Nenhum ${W.pac} encontrado.</td></tr>`}</tbody></table></div></div>`;
  return `<div class="grade g4">${kpi('Contatos no mês', R.contatosMes, R.comCodigo + ' vieram de anúncio (código)')}${kpi(`${W.Avals} marcadas`, R.marcadas, 'esperando a data')}${kpi('Comparecimento', R.comparecimento, `${W.tinhaAval}`)}${kpi(`${W.procs} no mês`, R.procedimentos, R.valorMes ? brl(R.valorMes) : 'valor a lançar')}</div>
   ${R.retornosVencidos ? `<div class="card" style="border-color:var(--alerta)"><b>${R.retornosVencidos} ${W.pac}(s) com retorno vencido.</b> <span class="sub" style="margin:0">Toque em WhatsApp no card para chamar para a revisão.</span></div>` : ''}
   <div class="fr-barra"><button class="btn am" type="button" data-novo-pac>+ Novo ${W.pac}</button><input type="search" id="fr-busca" placeholder="Buscar por nome, telefone ou interesse" value="${esc(crmBusca)}" aria-label="Buscar ${W.pac}">
    <select id="fr-origem" aria-label="Filtrar por origem"><option value="">Todas as origens</option>${origens.map(o => `<option ${o === crmOrigem ? 'selected' : ''}>${esc(o)}</option>`).join('')}</select>
    <div class="fr-tog" role="group" aria-label="Modo de ver"><button type="button" data-modo="funil" aria-pressed="${crmModo === 'funil'}">Funil</button><button type="button" data-modo="lista" aria-pressed="${crmModo === 'lista'}">Lista</button></div>${statusSalvo('crm')}</div>
   ${corpo}
   <div class="grade g2" style="margin-top:14px"><div class="card"><h3>De onde vêm os ${W.pacs}</h3><p class="sub">Cada anúncio abre o WhatsApp com um código. Aqui você vê qual traz ${W.aval} de verdade.</p><div class="tab"><table><thead><tr><th>Origem</th><th>Contatos</th><th>${W.marcaram}</th><th>${W.fezProc}</th></tr></thead><tbody>${porOrigem || `<tr><td colspan="4">Os números aparecem quando os primeiros ${W.pacs} entrarem.</td></tr>`}</tbody></table></div></div>
    <div class="card"><h3>Como usar</h3><p class="sub" style="margin:0">1. Chegou mensagem? <b>+ Novo ${W.pac}</b> com nome, WhatsApp e de onde veio.<br>2. Toque em <b>WhatsApp</b>: a mensagem da etapa já vai escrita. Ao voltar, o card anda sozinho.<br>3. Marcou ${W.aval === 'avaliação' ? 'a avaliação' : 'a ' + W.aval}? Toque em <b>Marcou ›</b> e escolha o dia.<br>4. Fez o ${W.proc}? Coloque o valor e ele entra no Financeiro.<br>${W.regra}</p></div></div>`;
};
T.crm = W.crm;

function mudaEtapa(p, nova, txt) {
  const antes = p.etapa; p.etapa = nova; p.em = agora(); p.hist = [...(p.hist || []), { em: agora(), txt: txt || `Etapa: ${etapa(antes).nome} → ${etapa(nova).nome}` }];
  if (nova === 'fez' && !p.dataProc) p.dataProc = hojeISO();
  if (nova === 'fez' || (nova === 'retorno' && !p.retorno)) p.retorno = somaDias(p.dataProc || hojeISO(), F.retornoDias || 150);
}
function lancaProcedimento(p) {
  if (!(+p.valor > 0) || p.finId) return false;
  const id = uid(); p.finId = id;
  S.fin.dados.itens.push({ id, tipo: 'entrada', data: p.dataProc || hojeISO(), desc: `${p.interesse || W.Proc} · ${p.nome}`, cat: (F.regexOdonto && new RegExp(F.regexOdonto, 'i').test(p.interesse || '')) ? F.catOdonto : (F.catEntradaCRM || F.catEntradas[0]), valor: +p.valor, forma: 'A definir', status: 'pago', crmId: p.id, em: agora() });
  salvar('fin'); return true;
}
function avancar(p) {
  const e = etapa(p.etapa), prox = ET[ET.indexOf(e) + 1];
  if (!prox) return;
  if (prox.id === 'marcada' && !p.avaliacao) return abrirPaciente(p, 'marcada');
  if (prox.id === 'fez' && !(+p.valor > 0)) return abrirPaciente(p, 'fez');
  mudaEtapa(p, prox.id); if (prox.id === 'fez' && lancaProcedimento(p)) toast(`${W.Proc} lançado no Financeiro.`);
  salvar('crm'); render();
}
function abrirPaciente(p, etapaNova) {
  const novo = !p; p = p ? { ...p } : { id: uid(), nome: '', whats: '', insta: '', origem: F.origens[0], interesse: F.interesses[0], etapa: 'novo', criado: agora(), hist: [] };
  if (etapaNova) p.etapa = etapaNova;
  const pede = etapaNova === 'marcada' ? `<p class="sub" style="color:var(--amarelo)">Escolha o dia e a hora da ${W.aval}.</p>` : etapaNova === 'fez' ? `<p class="sub" style="color:var(--amarelo)">Coloque o valor do ${W.proc} para lançar no Financeiro (ou deixe em branco).</p>` : '';
  modal(`<h3>${novo ? 'Novo ' + W.pac : esc(p.nome)}</h3>${pede}<form class="fr-form" id="fr-pac">
    <label class="inteiro">Nome *<input name="nome" required maxlength="80" value="${esc(p.nome)}" autocomplete="off"></label>
    <label>WhatsApp *<input name="whats" inputmode="tel" placeholder="(98) 9 0000-0000" value="${esc(p.whats)}"></label>
    <label>Instagram<input name="insta" placeholder="@" value="${esc(p.insta || '')}"></label>
    <label>De onde veio<select name="origem">${opts([...new Set([...F.origens, p.origem].filter(Boolean))], p.origem)}</select></label>
    <label>Interesse<select name="interesse">${opts([...new Set([...F.interesses, p.interesse].filter(Boolean))], p.interesse)}</select></label>
    <label>Etapa<select name="etapa">${ET.map(e => `<option value="${e.id}" ${e.id === p.etapa ? 'selected' : ''}>${esc(e.nome)}</option>`).join('')}</select></label>
    <label>${W.Aval} (dia e hora)<input type="datetime-local" name="avaliacao" value="${esc(p.avaliacao || '')}"></label>
    <label>Valor do ${W.proc} (R$)<input type="number" min="0" step="0.01" name="valor" value="${esc(p.valor || '')}"></label>
    <label>Retorno em<input type="date" name="retorno" value="${esc(p.retorno || '')}"></label>
    <label class="inteiro">Anotações<textarea name="notas" maxlength="1000" placeholder="Ex.: prefere horário à tarde">${esc(p.notas || '')}</textarea></label>
   </form>
   <div class="fr-acoes"><button class="btn am" type="submit" form="fr-pac">Salvar</button><button class="btn lin" type="button" data-fecha>Cancelar</button>${novo ? '' : '<button class="btn lin" type="button" id="fr-perdido">Não seguiu</button><button class="btn lin" type="button" id="fr-apaga" style="color:var(--erro)">Excluir</button>'}</div>
   ${(p.hist || []).length ? `<div class="fr-hist"><b>Histórico</b>${p.hist.slice().reverse().map(h => `<div>${new Date(h.em).toLocaleString('pt-BR', { dateStyle: 'short', timeStyle: 'short' })} · ${esc(h.txt)}</div>`).join('')}</div>` : ''}`, m => {
    const f = m.querySelector('#fr-pac');
    f.onsubmit = e => {
      e.preventDefault(); const v = Object.fromEntries(new FormData(f));
      if (!v.nome.trim()) return toast('Coloque o nome.');
      if (!fone(v.whats)) return toast('Coloque um WhatsApp com DDD (ex.: 98 9 0000-0000).');
      if (v.etapa === 'marcada' && !v.avaliacao) return toast(`Escolha o dia e a hora da ${W.aval}.`);
      const lista = crm(), i = lista.findIndex(x => x.id === p.id), base = i >= 0 ? lista[i] : p, etapaAntes = i >= 0 ? base.etapa : null;
      Object.assign(base, { nome: v.nome.trim(), whats: v.whats.trim(), insta: v.insta.trim(), origem: v.origem, interesse: v.interesse, avaliacao: v.avaliacao, valor: v.valor ? +v.valor : '', retorno: v.retorno, notas: v.notas.trim(), em: agora() });
      if (i < 0) { base.hist = [{ em: agora(), txt: W.Pac + ' cadastrado' }]; base.etapa = 'novo'; lista.push(base); if (v.etapa !== 'novo') mudaEtapa(base, v.etapa); }
      else if (etapaAntes !== v.etapa) mudaEtapa(base, v.etapa);
      let fin = false; if (base.etapa === 'fez' || base.etapa === 'retorno') fin = lancaProcedimento(base);
      salvar('crm'); fecha(); toast(fin ? `Salvo. O ${W.proc} entrou no Financeiro.` : W.Pac + ' salvo.'); render();
    };
    const pe = m.querySelector('#fr-perdido'); if (pe) pe.onclick = () => { const b = crm().find(x => x.id === p.id); mudaEtapa(b, 'perdido'); salvar('crm'); fecha(); toast('Movido para "não seguiu". Dá para reativar depois.'); render(); };
    const ap = m.querySelector('#fr-apaga'); if (ap) ap.onclick = () => { if (!confirm('Excluir ' + p.nome + '? Não dá para desfazer.')) return; S.crm.dados.itens = crm().filter(x => x.id !== p.id); S.crm.dados.apagados = [...(S.crm.dados.apagados || []), p.id]; salvar('crm'); fecha(); toast(W.Pac + ' excluído.'); render(); };
  });
}
function ligaCRM(m) {
  const busca = m.querySelector('#fr-busca');
  if (busca) busca.oninput = () => { crmBusca = busca.value; clearTimeout(busca._t); busca._t = setTimeout(() => { render(); const b = document.getElementById('fr-busca'); if (b) { b.focus(); b.setSelectionRange(b.value.length, b.value.length); } }, 250); };
  const or = m.querySelector('#fr-origem'); if (or) or.onchange = () => { crmOrigem = or.value; render(); };
  m.querySelectorAll('[data-modo]').forEach(b => b.onclick = e => { e.preventDefault(); crmModo = b.dataset.modo; render(); });
  m.querySelectorAll('[data-novo-pac]').forEach(b => b.onclick = () => abrirPaciente(null));
  m.querySelectorAll('[data-abre]').forEach(c => c.onclick = e => { if (e.target.closest('a,button')) return; abrirPaciente(crm().find(p => p.id === c.dataset.abre)); });
  m.querySelectorAll('[data-avanca]').forEach(b => b.onclick = () => avancar(crm().find(p => p.id === b.dataset.avanca)));
  m.querySelectorAll('[data-wa]').forEach(a => a.addEventListener('click', () => {
    const p = crm().find(x => x.id === a.dataset.wa); if (!p) return; const e = etapa(p.etapa);
    p.toques = (p.toques || 0) + 1; p.em = agora(); p.hist = [...(p.hist || []), { em: agora(), txt: `WhatsApp enviado (${e.nome})` }];
    if (e.depois) mudaEtapa(p, e.depois, `WhatsApp enviado · ${e.nome} → ${etapa(e.depois).nome}`);
    salvar('crm'); setTimeout(render, 400);
  }));
  m.querySelectorAll('[data-copia-msg]').forEach(b => b.onclick = () => { const p = crm().find(x => x.id === b.dataset.copiaMsg); try { navigator.clipboard.writeText(mensagem(p)); } catch (e) {} toast('Mensagem copiada (' + W.pac + ' sem WhatsApp válido).'); });
}

// =====================================================================
// FINANCEIRO
// =====================================================================
let finMes = mesISO(), finEdita = null;
const fin = () => S.fin.dados.itens;
const doMes = m => fin().filter(x => (x.data || '').startsWith(m));
function totais(m) {
  const l = doMes(m), soma = (t, st) => l.filter(x => x.tipo === t && (!st || x.status === st)).reduce((a, x) => a + (+x.valor || 0), 0);
  return { ent: soma('entrada', 'pago'), sai: soma('saida', 'pago'), aRec: soma('entrada', 'pendente'), aPag: soma('saida', 'pendente'), entTot: soma('entrada'), n: l.filter(x => x.tipo === 'entrada').length };
}
V.financeiro = () => {
  if (!S.fin || !S.fin.pronto) return `<div class="card"><p class="sub">Carregando o financeiro…</p></div>`;
  const t = totais(finMes), meta = +S.fin.dados.meta || 0, l = doMes(finMes).sort((a, b) => (a.data || '').localeCompare(b.data || ''));
  const e = finEdita ? fin().find(x => x.id === finEdita) : null, tipo = e ? e.tipo : (window._finTipo || 'entrada');
  const cats = tipo === 'entrada' ? F.catEntradas : F.catSaidas;
  const kpi = (r, v, n, c) => `<div class="card kpi"><div class="rot">${r}</div><div class="val ${c || ''}" style="font-size:28px">${v}</div><div class="var up"><span>${n}</span></div></div>`;
  const porCat = tp => { const g = {}; l.filter(x => x.tipo === tp).forEach(x => g[x.cat] = (g[x.cat] || 0) + (+x.valor || 0)); const mx = Math.max(1, ...Object.values(g));
    return Object.entries(g).sort((a, b) => b[1] - a[1]).map(([c, v]) => `<div><div style="display:flex;justify-content:space-between;font-size:13px"><span>${esc(c)}</span><b>${brl(v)}</b></div><div class="fr-bar ${tp === 'saida' ? 's' : ''}"><i style="width:${v / mx * 100}%"></i></div></div>`).join('') || '<div class="d" style="font-size:12px;color:var(--apagado)">Nada lançado.</div>'; };
  const seis = Array.from({ length: 6 }, (_, k) => somaMes(finMes, k - 5)).map(m => ({ m, ...totais(m) })), mx6 = Math.max(1, ...seis.map(s => Math.max(s.ent, s.sai)));
  return `<div class="fr-barra"><button class="btn lin" type="button" data-fmes="-1" aria-label="Mês anterior">‹</button><b style="font-size:16px;min-width:150px;text-align:center">${nomeMes(finMes)}</b><button class="btn lin" type="button" data-fmes="1" aria-label="Próximo mês">›</button>
    <button class="btn lin" type="button" data-fixas>Repetir despesas fixas do mês anterior</button><button class="btn lin" type="button" data-csv>Baixar planilha</button>${statusSalvo('fin')}</div>
   <div class="grade g4">${kpi('Entrou', brl(t.ent), t.n + ' entrada(s) no mês', 'fr-val e')}${kpi('Saiu', brl(t.sai), 'despesas pagas', 'fr-val s')}${kpi('Sobrou', brl(t.ent - t.sai), t.ent - t.sai >= 0 ? 'saldo do mês' : 'mês no vermelho')}${kpi('A receber · a pagar', brl(t.aRec) + ' · ' + brl(t.aPag), 'lançamentos pendentes')}</div>
   <div class="grade g21"><div class="card"><h3>${e ? 'Editar lançamento' : 'Novo lançamento'}</h3>
    <div class="fr-tog" role="group" aria-label="Tipo" style="margin-bottom:12px"><button type="button" data-ftipo="entrada" aria-pressed="${tipo === 'entrada'}">Entrada</button><button type="button" data-ftipo="saida" aria-pressed="${tipo === 'saida'}">Saída</button></div>
    <form class="fr-form" id="fr-fin"><input type="hidden" name="tipo" value="${tipo}">
     <label>Data<input type="date" name="data" required value="${esc(e ? e.data : (finMes === mesISO() ? hojeISO() : finMes + '-01'))}"></label>
     <label>Valor (R$)<input type="number" name="valor" min="0.01" step="0.01" required value="${esc(e ? e.valor : '')}"></label>
     <label class="inteiro">Descrição<input name="desc" required maxlength="120" placeholder="${esc(tipo === 'entrada' ? (F.exEntrada || 'Ex.: Botox · Maria') : (F.exSaida || 'Ex.: Aluguel da sala'))}" value="${esc(e ? e.desc : '')}"></label>
     <label>Categoria<select name="cat">${opts(cats, e ? e.cat : cats[0])}</select></label>
     <label>Forma<select name="forma">${opts(F.formas, e ? e.forma : F.formas[0])}</select></label>
     <label>Situação<select name="status"><option value="pago" ${!e || e.status === 'pago' ? 'selected' : ''}>${tipo === 'entrada' ? 'Recebido' : 'Pago'}</option><option value="pendente" ${e && e.status === 'pendente' ? 'selected' : ''}>${tipo === 'entrada' ? 'A receber' : 'A pagar'}</option></select></label>
     ${tipo === 'saida' ? `<label style="display:flex;align-items:center;gap:8px;margin-top:22px"><input type="checkbox" name="fixa" ${e && e.fixa ? 'checked' : ''} style="width:18px;height:18px"> Despesa fixa (todo mês)</label>` : ''}
    </form><div class="fr-acoes"><button class="btn am" type="submit" form="fr-fin">${e ? 'Salvar alteração' : 'Lançar'}</button>${e ? '<button class="btn lin" type="button" data-fcancela>Cancelar</button>' : ''}</div></div>
    <div class="card"><h3>Meta de faturamento</h3><p class="sub">${meta ? `${brl(t.entTot)} de ${brl(meta)} em ${nomeMes(finMes)}` : `Defina quanto ${W.negocio} quer faturar por mês.`}</p>${meta ? `<div class="fr-bar"><i style="width:${Math.min(100, t.entTot / meta * 100)}%"></i></div><p class="sub" style="margin-top:8px">${t.entTot >= meta ? 'Meta batida!' : 'Faltam ' + brl(meta - t.entTot)}</p>` : ''}<button class="btn lin" type="button" data-fmeta style="margin-top:8px">${meta ? 'Mudar meta' : 'Definir meta'}</button></div></div>
   <div class="card"><h3>Lançamentos de ${nomeMes(finMes)}</h3><div class="tab"><table><thead><tr><th>Data</th><th>Descrição</th><th>Categoria</th><th>Forma</th><th>Valor</th><th>Situação</th><th></th></tr></thead><tbody>
    ${l.map(x => `<tr><td>${dataBR(x.data)}</td><td>${esc(x.desc)}${x.fixa ? ' <span class="chip ne">fixa</span>' : ''}</td><td>${esc(x.cat)}</td><td>${esc(x.forma)}</td><td class="fr-val ${x.tipo === 'entrada' ? 'e' : 's'}"><b>${x.tipo === 'entrada' ? '+' : '−'} ${brl(x.valor)}</b></td><td><button class="btn lin" type="button" data-fst="${x.id}" style="padding:5px 9px;font-size:12px">${x.status === 'pago' ? (x.tipo === 'entrada' ? 'Recebido' : 'Pago') : (x.tipo === 'entrada' ? 'A receber' : 'A pagar')}</button></td><td style="white-space:nowrap"><button class="btn lin" type="button" data-fed="${x.id}" style="padding:5px 9px;font-size:12px">Editar</button> <button class="btn lin" type="button" data-fdel="${x.id}" style="padding:5px 9px;font-size:12px" aria-label="Excluir">✕</button></td></tr>`).join('') || '<tr><td colspan="7">Nenhum lançamento neste mês.</td></tr>'}</tbody></table></div></div>
   <div class="grade g3"><div class="card"><h3>Entradas por categoria</h3><div class="lista">${porCat('entrada')}</div></div><div class="card"><h3>Saídas por categoria</h3><div class="lista">${porCat('saida')}</div></div>
    <div class="card"><h3>Últimos 6 meses</h3><div class="lista">${seis.map(s => `<div style="font-size:12px"><div style="display:flex;justify-content:space-between"><span>${nomeMes(s.m)}</span><b class="${s.ent - s.sai >= 0 ? 'fr-val e' : 'fr-val s'}">${brl(s.ent - s.sai)}</b></div><div class="fr-bar"><i style="width:${s.ent / mx6 * 100}%"></i></div><div class="fr-bar s" style="margin-top:3px"><i style="width:${s.sai / mx6 * 100}%"></i></div></div>`).join('')}</div><p class="sub" style="margin-top:8px">Dourado: entrou · vermelho: saiu.</p></div></div>`;
};
T.financeiro = 'Financeiro';
function ligaFin(m) {
  m.querySelectorAll('[data-fmes]').forEach(b => b.onclick = () => { finMes = somaMes(finMes, +b.dataset.fmes); finEdita = null; render(); });
  m.querySelectorAll('[data-ftipo]').forEach(b => b.onclick = () => { window._finTipo = b.dataset.ftipo; if (finEdita) { const e = fin().find(x => x.id === finEdita); e.tipo = b.dataset.ftipo; } render(); });
  const f = m.querySelector('#fr-fin');
  if (f) f.onsubmit = ev => {
    ev.preventDefault(); const v = Object.fromEntries(new FormData(f));
    if (!(+v.valor > 0)) return toast('Coloque um valor.');
    const dados = { tipo: v.tipo, data: v.data, desc: v.desc.trim(), cat: v.cat, valor: Math.round(+v.valor * 100) / 100, forma: v.forma, status: v.status, fixa: !!v.fixa, em: agora() };
    if (finEdita) Object.assign(fin().find(x => x.id === finEdita), dados); else fin().push({ id: uid(), ...dados });
    toast(finEdita ? 'Lançamento atualizado.' : (v.tipo === 'entrada' ? 'Entrada lançada.' : 'Saída lançada.')); finEdita = null; finMes = v.data.slice(0, 7); salvar('fin'); render();
  };
  m.querySelectorAll('[data-fcancela]').forEach(b => b.onclick = () => { finEdita = null; render(); });
  m.querySelectorAll('[data-fed]').forEach(b => b.onclick = () => { finEdita = b.dataset.fed; render(); window.scrollTo({ top: 0, behavior: 'smooth' }); });
  m.querySelectorAll('[data-fst]').forEach(b => b.onclick = () => { const x = fin().find(y => y.id === b.dataset.fst); x.status = x.status === 'pago' ? 'pendente' : 'pago'; x.em = agora(); salvar('fin'); render(); });
  m.querySelectorAll('[data-fdel]').forEach(b => b.onclick = () => { const x = fin().find(y => y.id === b.dataset.fdel); if (!confirm(`Excluir "${x.desc}" (${brl(x.valor)})?`)) return; S.fin.dados.itens = fin().filter(y => y.id !== x.id); S.fin.dados.apagados = [...(S.fin.dados.apagados || []), x.id]; salvar('fin'); toast('Lançamento excluído.'); render(); });
  m.querySelectorAll('[data-fmeta]').forEach(b => b.onclick = () => { const v = prompt('Meta de faturamento por mês (R$):', S.fin.dados.meta || ''); if (v === null) return; const n = +String(v).replace(/\./g, '').replace(',', '.'); if (!(n >= 0)) return toast('Valor inválido.'); S.fin.dados.meta = n; salvar('fin'); render(); });
  m.querySelectorAll('[data-fixas]').forEach(b => b.onclick = () => {
    const ant = somaMes(finMes, -1), fixas = doMes(ant).filter(x => x.tipo === 'saida' && x.fixa), ja = new Set(doMes(finMes).map(x => x.origemFixa));
    const novas = fixas.filter(x => !ja.has(x.id)).map(x => ({ ...x, id: uid(), data: finMes + x.data.slice(7), status: 'pendente', origemFixa: x.id, em: agora() }));
    if (!novas.length) return toast(fixas.length ? 'As despesas fixas já estão neste mês.' : 'Não há despesa fixa marcada no mês anterior.');
    fin().push(...novas); salvar('fin'); toast(novas.length + ' despesa(s) fixa(s) lançada(s) como "a pagar".'); render();
  });
  m.querySelectorAll('[data-csv]').forEach(b => b.onclick = () => {
    const linhas = [['Data', 'Tipo', 'Descrição', 'Categoria', 'Forma', 'Valor', 'Situação'], ...doMes(finMes).map(x => [dataBR(x.data), x.tipo === 'entrada' ? 'Entrada' : 'Saída', x.desc, x.cat, x.forma, String(x.tipo === 'entrada' ? x.valor : -x.valor).replace('.', ','), x.status === 'pago' ? 'Pago' : 'Pendente'])];
    const csv = '﻿' + linhas.map(l => l.map(c => `"${String(c).replace(/"/g, '""')}"`).join(';')).join('\n');
    const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([csv], { type: 'text/csv;charset=utf-8' })); a.download = `financeiro-${cli}-${finMes}.csv`; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 2000);
  });
}

// =====================================================================
// NOTÍCIAS DO NICHO
// =====================================================================
const NT = F.noticias || [], cacheN = {};
let ntSel = 0;
function idadeTxt(d) { const t = Date.parse(d); if (!t) return ''; const h = Math.round((Date.now() - t) / 36e5); return h < 1 ? 'agora' : h < 24 ? `há ${h} h` : `há ${Math.round(h / 24)} dia(s)`; }
async function buscaN(i) {
  const q = NT[i].q; if (cacheN[q]) return;
  cacheN[q] = { carregando: true };
  try { const r = await fetch('/api/noticias?q=' + encodeURIComponent(q)); const j = (r.headers.get('content-type') || '').includes('json') ? await r.json() : null;
    cacheN[q] = j ? j : { itens: [], erro: 'As notícias aparecem no site da Central (lindsonalmeida.pages.dev).' }; }
  catch (e) { cacheN[q] = { itens: [], erro: 'As notícias aparecem no site da Central (lindsonalmeida.pages.dev).' }; }
  if ((location.hash || '').slice(1) === 'noticias') render();
}
V.noticias = () => {
  if (!NT.length) return '<div class="card"><p class="sub">Sem temas configurados.</p></div>';
  const tema = NT[ntSel], c = cacheN[tema.q]; if (!c) buscaN(ntSel);
  const itens = c && c.itens ? c.itens : [];
  return `<div class="card"><h3>Notícias do seu nicho</h3><p class="sub">${esc(F.notaNoticias || 'Atualizadas sozinhas a cada 3 horas. Antes de postar sobre uma notícia, abra a fonte original.')}</p>
   <div class="fr-chips" role="group" aria-label="Temas">${NT.map((t, i) => `<button type="button" data-nt="${i}" aria-pressed="${i === ntSel}">${esc(t.nome)}</button>`).join('')}</div>
   ${!c || c.carregando ? '<p class="sub">Buscando notícias…</p>' : c.erro && !itens.length ? `<p class="sub">${esc(c.erro)}</p>` : itens.map((n, i) => `<div class="fr-noticia"><a class="t" href="${esc(n.link)}" target="_blank" rel="noopener noreferrer">${esc(n.titulo)}</a><div class="d" style="font-size:12px;color:var(--apagado)">${esc(n.fonte || 'Fonte')} · ${idadeTxt(n.data)}</div><div><button class="btn lin" type="button" data-ideia="${i}" style="padding:6px 10px;font-size:12px">Ideia de post</button></div></div>`).join('')}
   </div>`;
};
T.noticias = 'Notícias do nicho';
function ligaNoticias(m) {
  m.querySelectorAll('[data-nt]').forEach(b => b.onclick = () => { ntSel = +b.dataset.nt; render(); });
  m.querySelectorAll('[data-ideia]').forEach(b => b.onclick = () => {
    const n = (cacheN[NT[ntSel].q].itens || [])[+b.dataset.ideia]; if (!n) return;
    const txt = (F.ideiaPost || 'Gancho: "Saiu uma notícia sobre {tema} e muita gente vai me perguntar. Te explico em 30 segundos."\nNotícia: {titulo}\nFonte: {link}')
      .replace('{tema}', NT[ntSel].nome.toLowerCase()).replace('{titulo}', n.titulo).replace('{link}', n.link);
    try { navigator.clipboard.writeText(txt); } catch (e) {} toast('Ideia de post copiada.');
  });
}

// ---------- liga tudo depois de cada tela ----------
const anterior = window.__pos;
window.__pos = view => {
  if (anterior) anterior(view);
  const m = document.getElementById('conteudo'); if (!m) return;
  if (view === 'crm') ligaCRM(m); if (view === 'financeiro') ligaFin(m); if (view === 'noticias') ligaNoticias(m);
};
})();
