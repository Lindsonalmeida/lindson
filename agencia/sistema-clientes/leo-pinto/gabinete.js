// Área "Gabinete" do painel do Vereador Leo Pinto (entra no modelo prototipo/painel.html pelo montar-leo.py).
// Demandas da população com banco real (db do artifact), no ciclo do book Pedimos → Fizemos → Entregamos.
// LGPD: nome e contato do cidadão só são gravados com consentimento; a coleção "demandas" só abre para Colaborador ou acima.
(() => {
const V = window.__V, T = window.__T;
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[c]));
const ST = {pedimos: ['Pedimos', 'O povo pediu', 'am'], fizemos: ['Fizemos', 'A gente encaminhou', 'al'], entregamos: ['Entregamos', 'Resolvido', 'ok']};
const CAUSAS = ['Saúde', 'Educação', 'Esporte', 'Pesca', 'Água', 'Lagos', 'Fé', 'Obras', 'Juventude', 'Povo', 'Iluminação', 'Outra'];
const pill = s => `<span class="chip ${ST[s][2]}">${ST[s][0]}</span>`;
const dataBR = ms => new Date(ms).toLocaleDateString('pt-BR', {day: '2-digit', month: 'short'});
let db = null, meuId = null, demandas = [], agenda = [], estado = 'carregando', filtro = {s: 'todas', b: '', c: ''};

function aviso() {
  const m = {semdb: 'O banco do gabinete não abriu nesta visualização. Abra o painel pelo claude.ai com a conta da equipe.',
    lento: 'Buscando os dados do gabinete. A página atualiza sozinha quando o banco responder.',
    semacesso: 'Por proteção dos dados dos cidadãos (LGPD), só a equipe do gabinete com acesso de Colaborador vê e registra demandas.'}[estado];
  return m ? `<div class="card" style="border-color:rgba(255,194,14,.4)"><p class="sub" style="margin:0">${m}</p></div>` : '';
}
const item = d => `<button class="item" type="button" data-dem="${esc(d.id)}" style="width:100%;text-align:left;font:inherit;color:inherit;cursor:pointer">
  <div style="min-width:0"><div class="t">${esc(d.titulo)}</div><div class="d">${esc(d.protocolo)} · ${esc(d.bairro || 'Sem bairro')} · ${esc(d.causa)} · ${dataBR(d.criado)}</div></div><div class="fim">${pill(d.status)}</div></button>`;

V.demandas = () => {
  const n = s => demandas.filter(d => d.status === s).length, tot = demandas.length;
  const porB = {}; demandas.forEach(d => porB[d.bairro || 'Sem bairro'] = (porB[d.bairro || 'Sem bairro'] || 0) + 1);
  const bs = Object.entries(porB).sort((a, b) => b[1] - a[1]).slice(0, 8), mx = Math.max(1, ...bs.map(x => x[1]));
  const bairros = [...new Set(demandas.map(d => d.bairro).filter(Boolean))].sort();
  const l = demandas.filter(d => (filtro.s === 'todas' || d.status === filtro.s) && (!filtro.b || d.bairro === filtro.b) && (!filtro.c || d.causa === filtro.c));
  const carg = estado === 'carregando' ? '…' : null;
  return aviso() + `<div class="grade g4">${[['Demandas recebidas', tot], ['Pedimos · aguardando', n('pedimos')], ['Fizemos · encaminhadas', n('fizemos')], ['Entregamos · resolvidas', n('entregamos')]].map(([r, v]) => `<div class="card kpi"><div class="rot">${r}</div><div class="val">${carg || v}</div><div class="var"><span>dados reais do gabinete</span></div></div>`).join('')}</div>
  <div class="grade g21"><div class="card"><h3>Demandas</h3><p class="sub">Cada pedido da população, do registro à entrega.</p>
   <div class="subabas" style="margin-bottom:10px">${[['todas', 'Todas'], ['pedimos', 'Pedimos'], ['fizemos', 'Fizemos'], ['entregamos', 'Entregamos']].map(([k, t]) => `<button type="button" aria-pressed="${filtro.s === k}" data-fs="${k}">${t}</button>`).join('')}</div>
   <div class="form-linha" style="grid-template-columns:minmax(0,1fr) minmax(0,1fr);margin-bottom:12px"><select id="f-bairro" aria-label="Bairro"><option value="">Todos os bairros</option>${bairros.map(b => `<option ${b === filtro.b ? 'selected' : ''}>${esc(b)}</option>`).join('')}</select>
   <select id="f-causa" aria-label="Causa"><option value="">Todas as causas</option>${CAUSAS.map(c => `<option ${c === filtro.c ? 'selected' : ''}>${c}</option>`).join('')}</select></div>
   <div class="lista">${l.length ? l.map(item).join('') : `<div class="vazio">${tot ? 'Nenhuma demanda com esses filtros.' : 'Nenhuma demanda registrada ainda. Use "Registrar demanda" ao lado.'}</div>`}</div></div>
  <div style="display:grid;gap:16px;align-content:start"><form class="card" id="nova-dem"><h3>Registrar demanda</h3><p class="sub">O que o povo pediu, na rua, no WhatsApp ou no gabinete.</p><div style="display:grid;gap:10px">
   <input id="nd-titulo" maxlength="90" required placeholder="Resumo (ex.: poste apagado na rua da escola)" aria-label="Resumo">
   <input id="nd-bairro" maxlength="60" required list="nd-bairros" placeholder="Bairro ou povoado" aria-label="Bairro ou povoado"><datalist id="nd-bairros">${bairros.map(b => `<option value="${esc(b)}">`).join('')}</datalist>
   <select id="nd-causa" aria-label="Causa">${CAUSAS.map(c => `<option>${c}</option>`).join('')}</select>
   <textarea id="nd-desc" maxlength="1200" placeholder="Detalhes e ponto de referência"></textarea>
   <input id="nd-nome" maxlength="40" placeholder="Primeiro nome (opcional)" aria-label="Primeiro nome">
   <input id="nd-contato" maxlength="40" placeholder="WhatsApp (opcional)" aria-label="Contato">
   <label class="sub" style="margin:0;display:flex;gap:8px;align-items:flex-start"><input type="checkbox" id="nd-ok" style="width:auto;margin-top:3px">A pessoa autorizou guardar nome e contato só para o retorno desta demanda (LGPD). Sem isso, nome e contato não são salvos.</label>
   <button class="btn am" type="submit" id="nd-btn">Registrar demanda</button></div></form>
   <div class="card"><h3>Por bairro e povoado</h3><p class="sub">Onde o mandato mais é chamado.</p><div class="lista">${bs.length ? bs.map(([b, v]) => `<div><div style="display:flex;justify-content:space-between"><span>${esc(b)}</span><b>${v}</b></div><div class="barra"><i style="width:${v / mx * 100}%"></i></div></div>`).join('') : '<div class="vazio">O mapa por bairro aparece com as primeiras demandas.</div>'}</div></div></div></div>
  <dialog id="dlg-dem" style="border:1px solid var(--linha);border-radius:16px;background:var(--painel);color:var(--texto);max-width:560px;width:calc(100% - 32px);padding:20px"></dialog>`;
};
V.prestacao = () => {
  const ent = demandas.filter(d => d.status === 'entregamos').sort((a, b) => (b.entregue || 0) - (a.entregue || 0));
  return aviso() + `<div class="card"><h3>Prestação de contas</h3><p class="sub">Cada demanda entregue vira um post "Pedimos · Fizemos · Entregamos". Copie o texto e peça a arte em Pedidos à agência.</p>
  <div class="posts">${ent.length ? ent.map(d => `<div class="post"><div class="img" style="background:linear-gradient(170deg,#FFD23A,#FFC20E 55%,#FFA51F);color:#05316E;flex-direction:column;gap:8px;display:flex;justify-content:center"><span style="font-size:11px;letter-spacing:.2em">ENTREGAMOS</span>${esc(d.titulo)}</div>
   <div class="c"><b>${esc(d.bairro)}</b><span class="d" style="color:var(--apagado);font-size:12.5px">${esc(d.acao || 'Encaminhado pelo gabinete.')}</span><div class="acoes"><button class="btn am" type="button" data-copia="${esc(d.id)}">Copiar texto do post</button></div></div></div>`).join('')
   : '<div class="vazio">Quando uma demanda chegar em "Entregamos", o card do post aparece aqui.</div>'}</div></div>`;
};
V.agenda = () => {
  const hoje = new Date().toISOString().slice(0, 10), prox = agenda.filter(x => x.data >= hoje).sort((a, b) => (a.data + a.hora).localeCompare(b.data + b.hora));
  return aviso() + `<div class="grade g21"><div class="card"><h3>Agenda do mandato</h3><p class="sub">Onde a gente vai: visitas, sessões e escutas.</p><div class="lista">${prox.length ? prox.map(x => `<div class="item"><div><div class="t">${esc(x.titulo)}</div><div class="d">${new Date(x.data + 'T12:00').toLocaleDateString('pt-BR', {weekday: 'short', day: '2-digit', month: 'short'})}${x.hora ? ' · ' + esc(x.hora) : ''}${x.local ? ' · ' + esc(x.local) : ''}</div></div><div class="fim"><button class="btn lin" type="button" data-rm="${esc(x.id)}">Remover</button></div></div>`).join('') : '<div class="vazio">Nenhum compromisso marcado.</div>'}</div></div>
  <form class="card" id="nova-ag"><h3>Novo compromisso</h3><p class="sub">Entra na agenda de toda a equipe.</p><div style="display:grid;gap:10px">
   <input id="ag-t" required maxlength="80" placeholder="Ex.: Escuta com pescadores" aria-label="Compromisso"><input id="ag-l" maxlength="60" placeholder="Local" aria-label="Local">
   <div class="form-linha" style="grid-template-columns:minmax(0,1fr) minmax(0,1fr)"><input id="ag-d" type="date" required value="${hoje}" aria-label="Data"><input id="ag-h" type="time" aria-label="Hora"></div>
   <button class="btn am" type="submit">Adicionar</button></div></form></div>`;
};
Object.assign(T, {demandas: 'Demandas da população', prestacao: 'Prestação de contas', agenda: 'Agenda do mandato'});

function texto(d) { return `PEDIMOS: ${d.titulo} (${d.bairro}).\nFIZEMOS: ${d.acao || 'o gabinete encaminhou a demanda.'}\nENTREGAMOS: demanda resolvida${d.entregue ? ' em ' + new Date(d.entregue).toLocaleDateString('pt-BR') : ''}.\nA gente não promete. A gente volta pra mostrar. Do povo, pro povo.`; }
function abrir(d) {
  const g = document.getElementById('dlg-dem'); if (!g) return;
  g.innerHTML = `<div style="display:grid;gap:12px"><div class="sub" style="margin:0">${esc(d.protocolo)} · ${esc(d.bairro)} · ${esc(d.causa)}</div><h3 style="margin:0;font-size:20px">${esc(d.titulo)}</h3>
   <p class="sub" style="margin:0">${esc(d.descricao || 'Sem detalhes.')}</p><p class="sub" style="margin:0">Quem pediu: ${d.consentimento ? esc((d.cidadao || '—') + (d.contato ? ' · ' + d.contato : '')) : 'não autorizou guardar dados'}</p>
   <div class="subabas">${Object.entries(ST).map(([k, [n, s]]) => `<button type="button" aria-pressed="${k === d.status}" data-et="${k}">${n} · ${s}</button>`).join('')}</div>
   <textarea id="dd-acao" maxlength="600" placeholder="O que o gabinete fez (indicação nº, ofício, visita...)">${esc(d.acao || '')}</textarea>
   <div style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn am" type="button" id="dd-salvar">Salvar</button><button class="btn lin" type="button" id="dd-fechar">Fechar</button></div></div>`;
  let novo = d.status;
  g.querySelectorAll('[data-et]').forEach(b => b.onclick = () => { novo = b.dataset.et; g.querySelectorAll('[data-et]').forEach(x => x.setAttribute('aria-pressed', String(x === b))); });
  g.querySelector('#dd-fechar').onclick = () => g.close();
  g.querySelector('#dd-salvar').onclick = async () => {
    const up = {status: novo, acao: g.querySelector('#dd-acao').value.trim(), atualizado: Date.now()}; if (novo === 'entregamos' && d.status !== 'entregamos') up.entregue = Date.now();
    try { await db.collection('demandas').doc(d.id).update(up); g.close(); window.__toast('Demanda atualizada.'); } catch (e) { window.__toast(e.code === 'invalid_argument' ? 'Sua conta não pode alterar demandas.' : 'Não foi possível salvar agora.'); }
  };
  g.showModal();
}
window.__pos = view => {
  const m = document.getElementById('conteudo'), ach = id => demandas.find(d => d.id === id);
  m.querySelectorAll('[data-dem]').forEach(b => b.onclick = () => abrir(ach(b.dataset.dem)));
  m.querySelectorAll('[data-fs]').forEach(b => b.onclick = () => { filtro.s = b.dataset.fs; window.__render(); });
  const fb = m.querySelector('#f-bairro'); if (fb) fb.onchange = e => { filtro.b = e.target.value; window.__render(); };
  const fc = m.querySelector('#f-causa'); if (fc) fc.onchange = e => { filtro.c = e.target.value; window.__render(); };
  m.querySelectorAll('[data-copia]').forEach(b => b.onclick = async () => { try { await navigator.clipboard.writeText(texto(ach(b.dataset.copia))); window.__toast('Texto do post copiado.'); } catch { window.__toast('Não deu para copiar neste aparelho.'); } });
  m.querySelectorAll('[data-rm]').forEach(b => b.onclick = async () => { try { await db.collection('agenda').doc(b.dataset.rm).delete(); } catch { window.__toast('Sua conta não pode alterar a agenda.'); } });
  const f = m.querySelector('#nova-dem'); if (f) f.onsubmit = async e => {
    e.preventDefault(); if (!db) return window.__toast('O banco não está disponível nesta visualização.');
    const ok = m.querySelector('#nd-ok').checked, agora = Date.now(), v = id => m.querySelector(id).value.trim();
    const doc = {protocolo: 'LP-' + new Date(agora).toISOString().slice(2, 10).replace(/-/g, '') + '-' + Math.random().toString(36).slice(2, 6).toUpperCase(), criado: agora, atualizado: agora,
      titulo: v('#nd-titulo'), bairro: v('#nd-bairro'), causa: m.querySelector('#nd-causa').value, descricao: v('#nd-desc'), status: 'pedimos', acao: '', consentimento: ok, autor: meuId || null};
    if (ok) { doc.cidadao = v('#nd-nome'); doc.contato = v('#nd-contato'); }
    m.querySelector('#nd-btn').disabled = true;
    try { await db.collection('demandas').doc().set(doc); window.__toast('Demanda ' + doc.protocolo + ' registrada.'); }
    catch (err) { window.__toast(err.code === 'invalid_argument' ? 'Sua conta não tem permissão. Peça acesso de Colaborador.' : err.code === 'quota_exceeded' ? 'O banco está cheio.' : 'Não foi possível salvar agora.'); m.querySelector('#nd-btn').disabled = false; }
  };
  const fa = m.querySelector('#nova-ag'); if (fa) fa.onsubmit = async e => {
    e.preventDefault(); if (!db) return window.__toast('O banco não está disponível nesta visualização.');
    try { await db.collection('agenda').doc().set({titulo: fa.querySelector('#ag-t').value.trim(), local: fa.querySelector('#ag-l').value.trim(), data: fa.querySelector('#ag-d').value, hora: fa.querySelector('#ag-h').value, criado: Date.now()}); window.__toast('Compromisso adicionado.'); }
    catch (err) { window.__toast(err.code === 'invalid_argument' ? 'Sua conta não pode alterar a agenda.' : 'Não foi possível salvar agora.'); }
  };
};
const redesenha = () => { if (['demandas', 'prestacao', 'agenda'].includes((location.hash || '#inicio').slice(1))) window.__render(); };
(async () => {
  const t = setTimeout(() => { if (estado === 'carregando') { estado = 'lento'; redesenha(); } }, 10000);
  let user = null; try { user = await claude.use('user'); db = await claude.use('db'); } catch { db = null; }
  if (!db) { clearTimeout(t); estado = 'semdb'; redesenha(); return; }
  let pode = null; try { meuId = user ? await user.id() : null; pode = user ? await user.can('data.write') : null; } catch {}
  db.collection('demandas').orderBy('criado', 'desc').limit(1000).onSnapshot(s => {
    demandas = s.docs.map(d => ({id: d.id, ...d.data()}));
    if (!s.metadata.fromCache) { clearTimeout(t); estado = (!demandas.length && pode === false) ? 'semacesso' : 'ok'; }
    const ab = document.getElementById('dlg-dem'); if (!(ab && ab.open)) redesenha();
  }, () => { clearTimeout(t); estado = 'semdb'; redesenha(); });
  db.collection('agenda').limit(500).onSnapshot(s => { agenda = s.docs.map(d => ({id: d.id, ...d.data()})); redesenha(); }, () => {});
})();
})();
