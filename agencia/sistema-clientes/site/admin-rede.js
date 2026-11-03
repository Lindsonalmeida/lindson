// Abas "Minha rede social" do painel do ADMINISTRADOR (Lindson): cuidar do @lindsonalmeida_ (conta Pedro, 03/11/2026).
// Pedido do Lindson: "crie as abas que eu preciso pra cuidar da minha rede social, no painel da central do administrador".
// Dados fixos: window.__REDE (agencia/marca-lindson/: estratégia, calendário e artes). Dados vivos: /api/dados?cli=admin&f=rede
// (postados, gravados, leads das iscas, relatórios semanais, números do Instagram). Entra no admin depois do admin-sistema.js.
(() => {
const V = window.__V, T = window.__T, R = window.__REDE || { cal: { dias: [] }, est: {}, artes: [] };
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const render = () => window.__render(), toast = t => window.__toast(t);
const kpi = (r, v, nota) => `<div class="card kpi"><div class="rot">${r}</div><div class="val">${v}</div><div class="var up"><span>${nota || ''}</span></div></div>`;
const hoje = () => { const d = new Date(); return new Date(d.getTime() - d.getTimezoneOffset() * 6e4).toISOString().slice(0, 10); };
const br = iso => iso ? iso.slice(8, 10) + '/' + iso.slice(5, 7) : '';
const ISCAS = { AV: ['PERFIL', 'a avaliação gratuita do seu perfil'], AD: ['ANÚNCIO', 'a revisão do seu anúncio'], VD: ['ROTEIRO', 'os 3 roteiros de vídeo'], MS: ['SITE', 'o vídeo de demonstração do mini site'] };
// funil dos leads das iscas: mensagens no PADRAO-COPY (Conexão → Dor → Desejo → Pergunta), curtas, sem preço
const ETAPAS = [
  { id: 'novo', nome: 'Pediu a isca', prox: 'entregue', msg: l => `Oi, ${l.nome}! Aqui é o Lindson. Recebi seu pedido e já vou preparar ${ISCAS[l.codigo][1]}. Pra eu fazer certinho pra ${l.negocio}: hoje o cliente chega mais pelo Instagram ou por indicação?` },
  { id: 'entregue', nome: 'Isca entregue', prox: 'conversa', msg: l => `${l.nome}, já te mandei ${ISCAS[l.codigo][1]}. Muita gente posta e o cliente não chama. Eu faço o Instagram da ${l.negocio} levar gente pro WhatsApp. Posso te mostrar em 15 minutos como ficaria?` },
  { id: 'conversa', nome: 'Conversa marcada', prox: 'proposta', msg: l => `${l.nome}, confirmando nossa conversa sobre o Instagram da ${l.negocio}. Fica bom no horário que combinamos?` },
  { id: 'proposta', nome: 'Proposta enviada', prox: 'fechou', msg: l => `${l.nome}, conseguiu ver a proposta? Se fizer sentido, eu já reservo a diária de gravação da ${l.negocio} este mês. Posso reservar?` },
  { id: 'fechou', nome: 'Fechou', prox: null, msg: l => `Bem-vindo, ${l.nome}! Vou te mandar o acesso da Central da ${l.negocio}, onde você acompanha tudo. Qual o melhor e-mail?` },
  { id: 'perdido', nome: 'Não seguiu', prox: 'novo', msg: l => `Oi, ${l.nome}! Aqui é o Lindson. Como está o Instagram da ${l.negocio}? Este mês estou fazendo avaliação gratuita de perfil. Quer que eu olhe o seu?` }];
const ET = Object.fromEntries(ETAPAS.map(e => [e.id, e]));
const dig = s => String(s || '').replace(/\D/g, '');
const wa = l => { const n = dig(l.whats); return n.length >= 10 ? 'https://wa.me/55' + n.replace(/^55/, '') + '?text=' + encodeURIComponent(ET[l.etapa].msg(l)) : null; };

// ---- dados vivos (KV), com junção se duas abas salvarem juntas
let D = { postados: {}, gravados: {}, leads: [], relatorios: [], numeros: {} }, versao = 0, carregado = false;
async function carrega() {
  try { const r = await fetch('/api/dados?cli=admin&f=rede'); if (r.ok) { const j = await r.json(); if (j.dados) D = Object.assign(D, j.dados); versao = j.versao || 0; } } catch (e) {}
  carregado = true; render();
}
async function salva(muda, msg) {
  muda(D); render();
  for (let i = 0; i < 3; i++) {
    try {
      const r = await fetch('/api/dados?cli=admin&f=rede', { method: 'PUT', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ dados: D, versao }) });
      if (r.ok) { versao = (await r.json()).versao; if (msg) toast(msg); return; }
      if (r.status === 409) { const j = await r.json(); D = Object.assign({ postados: {}, gravados: {}, leads: [], relatorios: [], numeros: {} }, j.dados || {}); versao = j.versao; muda(D); continue; }
      break;
    } catch (e) { break; }
  }
  toast('Salvo só neste aparelho por enquanto: confira a internet.');
}
carrega();

const dias = () => R.cal.dias || [];
const semanaDe = iso => (dias().find(d => d.data === iso) || {}).semana;
const semAtual = () => { const h = hoje(); const d = dias(); if (!d.length) return 1; if (h < d[0].data) return 1; return semanaDe(h) || d[d.length - 1].semana; };
const chipF = t => `<span class="chip">${esc(t)}</span>`;
const linhaDia = (d, extra = '') => `<div class="item" style="display:grid;grid-template-columns:62px 1fr auto;gap:12px;align-items:center;padding:12px 0;border-bottom:1px solid var(--linha)">
  <div><b style="font-size:18px">${br(d.data)}</b><div class="sub" style="margin:0;font-size:12px">${esc(d.dia)}</div></div>
  <div><div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:4px">${chipF(d.formato)}${chipF(d.linha)}<span class="chip am">${esc(d.isca)} · ${esc(d.codigo)}</span></div>
  <b>${esc(d.pauta)}</b><div class="sub" style="margin:2px 0 0">Gancho: “${esc(d.gancho)}”</div></div>
  <div style="display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-end">${extra}<button class="btn lin" data-copia="${esc(d.gancho)}" style="padding:6px 10px;font-size:12px">Copiar gancho</button>
  <button class="btn ${D.postados[d.data] ? 'am' : 'lin'}" data-postado="${d.data}" style="padding:6px 10px;font-size:12px">${D.postados[d.data] ? '✓ Postado' : 'Marcar postado'}</button></div></div>`;

// ---- 1 · Visão
V.rede = () => {
  const h = hoje(), dd = dias(), dia = dd.find(d => d.data === h) || dd.find(d => d.data > h), prox = dd.filter(d => d.data > (dia ? dia.data : h)).slice(0, 3);
  const post = Object.keys(D.postados).length, L = D.leads || [], fech = L.filter(l => l.etapa === 'fechou').length, n = D.numeros || {};
  const porCod = Object.keys(ISCAS).map(c => [c, L.filter(l => l.codigo === c).length, L.filter(l => l.codigo === c && l.etapa === 'fechou').length]);
  return `<div class="grade g4">${kpi('Seguidores', n.seguidores ? Number(n.seguidores).toLocaleString('pt-BR') : 'a medir', n.data ? 'em ' + br(n.data) : 'atualize no Relatório')}${kpi('Posts do calendário', `${post}/${dd.length}`, 'marcados como postados')}${kpi('Leads das iscas', L.length, 'pediram uma isca')}${kpi('Contratos', fech, 'fechados pelas iscas')}</div>
  <div class="grade g2"><div class="card"><h3>${dia && dia.data === h ? 'Hoje' : 'Próximo post'} · ${dia ? br(dia.data) : ''}</h3>${dia ? `<p class="sub">Semana ${dia.semana}: ${esc(dia.tema)} · objetivo: ${esc(dia.objetivo)}</p>${linhaDia(dia)}<p class="sub" style="margin-top:10px">Stories: ${esc(dia.stories)}.</p>` : `<p class="sub">${esc(R.cal.preparacao || 'Sem calendário ainda.')}</p>`}</div>
  <div class="card"><h3>Próximos dias</h3>${prox.map(d => linhaDia(d)).join('') || '<p class="sub">Fim do calendário: peça ao Claude o próximo mês.</p>'}</div></div>
  <div class="card"><h3>Resultado por isca</h3><p class="sub">Cada isca tem um código no link do WhatsApp. É assim que você sabe qual post traz cliente.</p><div class="tab"><table><thead><tr><th>Isca</th><th>Palavra</th><th>Código</th><th>Leads</th><th>Fecharam</th></tr></thead><tbody>
  ${porCod.map(([c, q, f]) => `<tr><td>${esc(ISCAS[c][1])}</td><td><b>${ISCAS[c][0]}</b></td><td>${c}</td><td>${q}</td><td>${f}</td></tr>`).join('')}</tbody></table></div></div>`;
};

// ---- 2 · Estratégia
V['rede-estrategia'] = () => { const E = R.est || {};
  return `<div class="card"><h3>A ideia em uma frase</h3><p style="font-size:22px;font-weight:700;margin:4px 0 8px">“${esc(E.frase || '')}”</p><p class="sub">${esc(E.promessa || '')}</p></div>
  <div class="card"><h3>A história que a conta conta</h3><div class="tab"><table><tbody>${(E.historia || []).map(([k, v]) => `<tr><td style="width:170px"><b>${esc(k)}</b></td><td>${esc(v)}</td></tr>`).join('')}</tbody></table></div></div>
  <h3 style="margin:22px 0 10px">Linhas editoriais</h3><div class="grade g3">${(E.linhas || []).map((l, i) => `<div class="card"><div class="rot">${String(i + 1).padStart(2, '0')} · ${esc(l.obj)}</div><h3 style="margin:6px 0">${esc(l.nome)}</h3><p class="sub">${esc(l.mostra)}</p><div style="display:flex;gap:6px;flex-wrap:wrap;margin:6px 0">${l.formatos.map(chipF).join('')}</div><div class="lista">${l.pautas.map(p => `<div>• ${esc(p)}</div>`).join('')}</div></div>`).join('')}</div>
  <div class="grade g2"><div class="card"><h3>Iscas</h3><div class="lista">${Object.entries(ISCAS).map(([c, [p, t]]) => `<div><b>${p}</b> · código ${c}: ${esc(t)}</div>`).join('')}</div><p class="sub" style="margin-top:10px">A isca resolve uma parte e mostra a próxima. Preço só na conversa, nunca no feed.</p></div>
  <div class="card"><h3>Ângulos de venda</h3><div class="lista">${(E.angulos || []).map(a => `<div>${esc(a)}</div>`).join('')}</div></div></div>
  <div class="card"><h3>Regras do jogo</h3><div class="lista">${(E.regras || []).map(a => `<div>• ${esc(a)}</div>`).join('')}</div></div>`; };

// ---- 3 · Calendário
let semCal = null;
V['rede-calendario'] = () => { const s = semCal || semAtual(), ss = [...new Set(dias().map(d => d.semana))];
  return `<div class="card"><h3>Calendário editorial · ${br(R.cal.inicio)} a ${br(R.cal.fim)}</h3><p class="sub">Preparação: ${esc(R.cal.preparacao || '')}. Stories todo dia (3 a 5 telas) com o link do WhatsApp e o código da isca do dia.</p>
  <div style="display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 4px">${ss.map(n => { const d = dias().find(x => x.semana === n); return `<button class="btn ${n === s ? 'am' : 'lin'}" data-semcal="${n}">Semana ${n} · ${esc(d.tema)}</button>`; }).join('')}</div>
  ${dias().filter(d => d.semana === s).map(d => linhaDia(d)).join('')}</div>`; };

// ---- 4 · Gravação (lote de Reels da semana)
V['rede-lote'] = () => { const s = semCal || semAtual(), rs = dias().filter(d => d.semana === s && d.formato === 'Reels');
  return `<div class="grade g3">${kpi('Reels da semana ' + s, rs.length, 'para gravar num dia só')}${kpi('Gravados', rs.filter(d => D.gravados[d.data]).length, 'marcados aqui')}${kpi('Banco de roteiros', '300', 'Teste 01 no Recomeço 90')}</div>
  <div class="card"><h3>Lote de gravação · semana ${s}</h3><p class="sub">Grave no domingo os Reels da semana seguinte. Abra cada um com o gancho e feche com a palavra da isca.</p>
  ${rs.map(d => linhaDia(d, `<button class="btn ${D.gravados[d.data] ? 'am' : 'lin'}" data-gravado="${d.data}" style="padding:6px 10px;font-size:12px">${D.gravados[d.data] ? '✓ Gravado' : 'Marcar gravado'}</button>`)).join('')}
  <div style="margin-top:14px;display:flex;gap:8px;flex-wrap:wrap"><a class="btn lin" href="#rede-calendario">Ver o calendário</a><a class="btn lin" href="#recomeco">Abrir os 300 roteiros (Recomeço 90)</a></div></div>`; };

// ---- 5 · Leads das iscas (funil com botão de WhatsApp)
let abreLead = false;
V['rede-leads'] = () => { const L = D.leads || [];
  const card = l => { const u = wa(l), e = ET[l.etapa];
    return `<div class="card" style="padding:14px"><div style="display:flex;justify-content:space-between;gap:8px"><b>${esc(l.nome)}</b><span class="chip am">${esc(l.codigo)}</span></div><div class="sub" style="margin:2px 0 8px">${esc(l.negocio)} · ${esc(l.insta)}</div>
    <div style="display:flex;gap:6px;flex-wrap:wrap"><button class="btn am" data-wa="${l.id}" style="padding:6px 10px;font-size:12px">${u ? 'WhatsApp' : 'Copiar mensagem'}${e.prox ? ' · ' + esc(ET[e.prox].nome) : ''}</button>
    ${l.etapa !== 'perdido' && l.etapa !== 'fechou' ? `<button class="btn lin" data-perdeu="${l.id}" style="padding:6px 10px;font-size:12px">Não seguiu</button>` : ''}</div>${(l.hist || []).length ? `<div class="sub" style="margin:8px 0 0;font-size:11.5px">Último envio: ${new Date(l.hist[l.hist.length - 1].em).toLocaleDateString('pt-BR')}</div>` : ''}</div>`; };
  return `<div class="grade g4">${['novo', 'entregue', 'conversa', 'proposta'].map(id => kpi(ET[id].nome, L.filter(l => l.etapa === id).length, '')).join('')}</div>
  <div class="card"><div style="display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;align-items:center"><div><h3 style="margin:0">Leads das iscas</h3><p class="sub" style="margin:4px 0 0">Só entra quem tem WhatsApp e Instagram. Toque em WhatsApp: a mensagem da etapa já vai escrita, o envio fica registrado e o card avança sozinho.</p></div><button class="btn am" id="novo-lead">${abreLead ? 'Fechar' : '+ Novo lead'}</button></div>
  ${abreLead ? `<form id="f-lead" class="grade g3" style="margin-top:12px"><input name="nome" placeholder="Nome" required><input name="negocio" placeholder="Negócio" required><input name="whats" placeholder="WhatsApp com DDD" required><input name="insta" placeholder="@instagram" required><select name="codigo">${Object.entries(ISCAS).map(([c, [p]]) => `<option value="${c}">${p} (${c})</option>`).join('')}</select><button class="btn am">Salvar lead</button></form>` : ''}</div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px">${ETAPAS.map(e => `<div><div class="rot" style="margin-bottom:8px">${esc(e.nome)} · ${L.filter(l => l.etapa === e.id).length}</div><div style="display:grid;gap:10px">${L.filter(l => l.etapa === e.id).map(card).join('') || '<p class="sub">Ninguém aqui.</p>'}</div></div>`).join('')}</div>`; };

// ---- 6 · Relatório semanal
const CAMPOS = [['envios', 'Envios a cada mil visualizações (Reels)'], ['retencao', 'Retenção nos 3 primeiros segundos (%)'], ['salvamentos', 'Salvamentos por alcance (carrossel, %)'], ['custo', 'Custo por conversa no WhatsApp (R$)'], ['conversas', 'Conversas qualificadas'], ['contratos', 'Avaliações e contratos fechados']];
V['rede-relatorio'] = () => { const rel = (D.relatorios || []).slice().sort((a, b) => b.semana.localeCompare(a.semana)), n = D.numeros || {};
  return `<div class="grade g2"><div class="card"><h3>Relatório da semana</h3><p class="sub">Domingo: preencha com os números do Instagram e do Gerenciador de Anúncios. Média e meta saem dos seus próprios dados.</p>
  <form id="f-rel" class="grade g2"><label class="sub" style="grid-column:1/-1">Semana que começa em <input type="date" name="semana" value="${R.cal.inicio || hoje()}" required></label>${CAMPOS.map(([k, t]) => `<label class="sub" style="margin:0">${t}<input name="${k}" inputmode="decimal"></label>`).join('')}<label class="sub" style="grid-column:1/-1">O que funcionou e o que muda<input name="nota"></label><button class="btn am" style="grid-column:1/-1">Salvar semana</button></form></div>
  <div class="card"><h3>Números do Instagram</h3><form id="f-num" class="grade g2"><label class="sub" style="margin:0">Seguidores<input name="seguidores" inputmode="numeric" value="${esc(n.seguidores || '')}"></label><label class="sub" style="margin:0">Visualizações em 30 dias<input name="visualizacoes" inputmode="numeric" value="${esc(n.visualizacoes || '')}"></label><button class="btn am" style="grid-column:1/-1">Atualizar</button></form>
  <h3 style="margin-top:18px">Regra de decisão</h3><div class="lista"><div>• Criativo com custo por conversa acima da média, depois de gastar o dobro dela: corta.</div><div>• Abaixo da média: aumenta a verba aos poucos, a cada 2 dias.</div><div>• Reels com mais envios a cada mil: vira anúncio.</div><div>• Isca que traz conversa e não marca avaliação em 2 semanas: troca a isca, não o público.</div></div></div></div>
  <div class="card"><h3>Semanas registradas</h3><div class="tab"><table><thead><tr><th>Semana</th>${CAMPOS.map(([, t]) => `<th>${esc(t.split(' (')[0])}</th>`).join('')}<th>Nota</th></tr></thead><tbody>${rel.map(r => `<tr><td>${br(r.semana)}</td>${CAMPOS.map(([k]) => `<td>${esc(r[k] || '—')}</td>`).join('')}<td>${esc(r.nota || '')}</td></tr>`).join('') || `<tr><td colspan="8">Nenhuma semana ainda.</td></tr>`}</tbody></table></div></div>`; };

// ---- 7 · Artes
V['rede-artes'] = () => `<div class="card"><h3>Artes do seu Instagram</h3><p class="sub">As artes saem da identidade nova (preto e amarelo) e de modelos de templates premium. Cada uma vem com a legenda no padrão blog SEO.</p>
  ${(R.artes || []).length ? `<div class="grade g3">${R.artes.map(a => `<div class="card" style="padding:10px"><img src="${a.img}" alt="${esc(a.titulo)}" style="width:100%;border-radius:10px;display:block"><b style="display:block;margin:8px 0 2px">${esc(a.titulo)}</b><div class="sub" style="margin:0">${esc(a.data || '')}</div>${a.legenda ? `<details style="margin-top:6px"><summary style="cursor:pointer;color:var(--amarelo);font-weight:700">Legenda</summary><pre style="white-space:pre-wrap;font:inherit;font-size:13px">${esc(a.legenda)}</pre></details>` : ''}<a class="btn lin" download="${esc(a.arquivo || 'arte.jpg')}" href="${a.img}" style="margin-top:8px;padding:6px 10px;font-size:12px">Baixar</a></div>`).join('')}</div>` : '<p class="sub" style="margin:0">Ainda não há artes aprovadas aqui. Elas entram assim que a identidade nova e as primeiras artes forem aprovadas.</p>'}</div>`;

Object.assign(T, { rede: 'Minha rede · visão', 'rede-estrategia': 'Estratégia de conteúdo', 'rede-calendario': 'Calendário editorial', 'rede-lote': 'Gravação da semana', 'rede-leads': 'Leads das iscas', 'rede-relatorio': 'Relatório semanal', 'rede-artes': 'Artes' });

// ---- ações (depois de cada tela)
const ant = window.__pos;
window.__pos = view => {
  if (ant) ant(view);
  const $$ = s => document.querySelectorAll('#conteudo ' + s), $1 = s => document.querySelector('#conteudo ' + s);
  $$('[data-copia]').forEach(b => b.onclick = () => { navigator.clipboard && navigator.clipboard.writeText(b.dataset.copia); toast('Gancho copiado'); });
  $$('[data-postado]').forEach(b => b.onclick = () => salva(d => { const k = b.dataset.postado; if (d.postados[k]) delete d.postados[k]; else d.postados[k] = { em: new Date().toISOString() }; }, 'Calendário atualizado'));
  $$('[data-gravado]').forEach(b => b.onclick = () => salva(d => { const k = b.dataset.gravado; if (d.gravados[k]) delete d.gravados[k]; else d.gravados[k] = { em: new Date().toISOString() }; }, 'Lote atualizado'));
  $$('[data-semcal]').forEach(b => b.onclick = () => { semCal = +b.dataset.semcal; render(); });
  const nl = $1('#novo-lead'); if (nl) nl.onclick = () => { abreLead = !abreLead; render(); };
  const fl = $1('#f-lead'); if (fl) fl.onsubmit = e => { e.preventDefault(); const f = Object.fromEntries(new FormData(fl));
    if (dig(f.whats).length < 10 || !/^@?[\w.]{2,}$/.test(f.insta.trim())) { toast('Precisa de WhatsApp com DDD e @ do Instagram.'); return; }
    abreLead = false; salva(d => d.leads.push({ id: Date.now().toString(36), nome: f.nome.trim(), negocio: f.negocio.trim(), whats: f.whats.trim(), insta: '@' + f.insta.trim().replace(/^@/, ''), codigo: f.codigo, etapa: 'novo', criado: new Date().toISOString(), hist: [] }), 'Lead salvo'); };
  $$('[data-wa]').forEach(b => b.onclick = () => { const l = D.leads.find(x => x.id === b.dataset.wa); if (!l) return; const u = wa(l), m = ET[l.etapa].msg(l);
    if (u) window.open(u, '_blank', 'noopener'); else { navigator.clipboard && navigator.clipboard.writeText(m); toast('Sem WhatsApp: mensagem copiada'); }
    salva(d => { const x = d.leads.find(y => y.id === l.id); x.hist = (x.hist || []).concat({ etapa: x.etapa, em: new Date().toISOString() }); if (ET[x.etapa].prox) x.etapa = ET[x.etapa].prox; }, 'Envio registrado'); });
  $$('[data-perdeu]').forEach(b => b.onclick = () => salva(d => { const x = d.leads.find(y => y.id === b.dataset.perdeu); if (x) x.etapa = 'perdido'; }, 'Movido para "Não seguiu"'));
  const fr = $1('#f-rel'); if (fr) fr.onsubmit = e => { e.preventDefault(); const f = Object.fromEntries(new FormData(fr)); salva(d => { d.relatorios = (d.relatorios || []).filter(r => r.semana !== f.semana).concat(f); }, 'Semana salva'); };
  const fn = $1('#f-num'); if (fn) fn.onsubmit = e => { e.preventDefault(); const f = Object.fromEntries(new FormData(fn)); salva(d => { d.numeros = { seguidores: f.seguidores, visualizacoes: f.visualizacoes, data: hoje() }; }, 'Números atualizados'); };
};
})();
