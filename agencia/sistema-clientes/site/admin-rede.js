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
let D = { postados: {}, gravados: {}, leads: [], relatorios: [], numeros: {}, artes: {} }, versao = 0, carregado = false;
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

// ---- 7 · Artes, com as abas Para aprovar · Aprovados (a postar) · Postados (pedido do Lindson, 08/11/2026, conta Leandro).
// Situação de cada arte fica nos dados vivos (D.artes[img] = {st, postado, em, por}); arte nova entra com "st":"aprovar" no artes-aprovadas.json.
// 09/11/2026 (conta Zuleide, webdesigner): a agenda do Instagram (agencia/marca-lindson/agenda-status.json, embutida em __REDE.agenda) vira a
// fonte das abas "Aprovados · a postar" (data e hora, miniatura, legenda, cor da capa) e "Postados" (data e link), mais o "Grid do perfil" em xadrez.
// Status do JSON (postado | agendado | aguardando aprovação | bloqueado), por cima dele o que for marcado aqui (D.artes['ag:<id>']).
let abaArte = 'apr';
const chaveArte = a => a.img || a.titulo;
const AG = ((R.agenda || {}).posts) || [];
const nomeArq = u => String(u || '').split('/').pop();
const AGARQ = new Set(AG.flatMap(p => (p.urls || []).concat(p.arquivos || []).map(nomeArq)));
const naAgenda = a => AGARQ.has(nomeArq(a.img));
const stArte = a => { const v = (D.artes || {})[chaveArte(a)] || {}; if (v.postado) return 'post'; const st = v.st || a.st || 'aprovado'; return st === 'aprovar' ? 'pend' : st === 'ajuste' ? 'aj' : 'apr'; };
const vivoAg = p => (D.artes || {})['ag:' + p.id] || {};
const stAg = p => { const v = vivoAg(p); if (v.postado || p.status === 'postado') return 'postado'; if (v.st === 'aprovado' && p.status === 'aguardando aprovação') return 'agendado'; if (v.st === 'ajuste') return 'ajuste'; return p.status; };
const quandoAg = p => p.status === 'postado' ? p.postado_em : vivoAg(p).postado ? vivoAg(p).em : p.quando;
const SEM = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sáb'];
const dataHora = iso => { if (!iso) return 'sem data'; const d = new Date(iso); if (isNaN(d)) return iso;
  const f = new Intl.DateTimeFormat('pt-BR', { timeZone: 'America/Fortaleza', weekday: 'short', day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit' }).format(d);
  return f.replace(/\.,?/, '').replace(', ', ' · ').replace(':', 'h'); };
const COR = { amarelo: ['#F5C518', '#0A0A0A'], preto: ['#0B0B0B', '#F5C518'] };
const corChip = c => `<span class="chip ne"><span style="width:10px;height:10px;border-radius:3px;background:${(COR[c] || COR.preto)[0]};border:1px solid var(--linha)"></span>capa ${esc(c || '—')}</span>`;
const FMT = { post: 'Post', carrossel: 'Carrossel', reels: 'Reels' };
const stChip = s => ({ postado: '<span class="chip ok">Postado</span>', agendado: '<span class="chip am">Agendado</span>', 'aguardando aprovação': '<span class="chip al">Aguardando aprovação</span>', ajuste: '<span class="chip al">Em ajuste</span>', bloqueado: '<span class="chip er">Bloqueado</span>' }[s] || `<span class="chip ne">${esc(s)}</span>`);
// miniatura 4:5: a capa real; Reels ainda sem capa pública vira um bloco na cor da capa com a palavra do CTA
const mini = (p, r = 12) => p.capa ? `<img loading="lazy" src="${esc(p.capa)}" alt="${esc(p.titulo)}" style="width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:${r}px;display:block">`
  : `<div style="width:100%;aspect-ratio:4/5;border-radius:${r}px;background:${(COR[p.cor] || COR.preto)[0]};color:${(COR[p.cor] || COR.preto)[1]};display:grid;place-items:center;border:1px solid var(--linha);text-align:center;padding:8px"><div><div style="font:400 clamp(18px,3.4vw,34px)/1 var(--f-titulo);letter-spacing:.01em;text-transform:uppercase">${esc(p.palavra || FMT[p.formato] || '')}</div><div style="font:600 10px var(--f-corpo);opacity:.7;margin-top:6px;text-transform:uppercase;letter-spacing:.08em">${esc(FMT[p.formato] || '')} · capa a sair</div></div></div>`;
const cardAg = (p, i) => { const s = stAg(p), v = vivoAg(p), link = v.link || p.link, atras = s === 'agendado' && p.quando && new Date(p.quando) < new Date();
  const telas = (p.urls || []).length > 1 ? `<div style="display:flex;gap:6px;overflow-x:auto;margin-top:8px">${p.urls.map(t => `<a href="${esc(t)}" target="_blank" rel="noopener"><img loading="lazy" src="${esc(t)}" alt="tela" style="height:64px;border-radius:6px;display:block"></a>`).join('')}</div>` : '';
  const bts = s === 'postado'
    ? (link ? `<a class="btn am" href="${esc(link)}" target="_blank" rel="noopener" style="padding:6px 10px;font-size:12px">Abrir no Instagram</a>` : '') + (v.postado && p.status !== 'postado' ? `<button class="btn lin" type="button" data-agacao="despostar" data-ag="${i}" style="padding:6px 10px;font-size:12px">Voltar para a postar</button>` : '')
    : s === 'aguardando aprovação' ? `<button class="btn am" type="button" data-agacao="aprovado" data-ag="${i}" style="padding:6px 10px;font-size:12px">Aprovar</button><button class="btn lin" type="button" data-agacao="ajuste" data-ag="${i}" style="padding:6px 10px;font-size:12px">Pedir ajuste</button>`
    : s === 'ajuste' ? `<button class="btn am" type="button" data-agacao="aprovado" data-ag="${i}" style="padding:6px 10px;font-size:12px">Aprovar</button>`
    : s === 'agendado' ? `<button class="btn am" type="button" data-agacao="postado" data-ag="${i}" style="padding:6px 10px;font-size:12px">Marcar postado</button>` : '';
  return `<div class="card" style="padding:10px;display:grid;grid-template-columns:minmax(92px,128px) 1fr;gap:14px;align-items:start">
   <a href="${esc(p.capa || '#')}" ${p.capa ? 'target="_blank" rel="noopener"' : ''} style="display:block">${mini(p, 10)}</a>
   <div style="min-width:0"><div style="display:flex;gap:6px;flex-wrap:wrap;align-items:center;margin-bottom:6px">${stChip(s)}${atras ? '<span class="chip er">Passou do horário</span>' : ''}<span class="chip ne">${esc(p.formato_rotulo || FMT[p.formato])}</span>${corChip(p.cor)}</div>
    <div style="font:700 15px var(--f-dado);color:var(--amarelo)">${s === 'postado' ? 'Postado ' : ''}${esc(dataHora(quandoAg(p)))}${p.seq ? ` <span class="sub" style="font:500 12px var(--f-corpo)">· ${p.seq}º do feed</span>` : ''}</div>
    <b style="display:block;margin:4px 0 2px">${esc(p.titulo)}</b><div class="sub" style="margin:0;font-size:12.5px">${esc(p.legenda_curta)}</div>
    ${p.obs ? `<div class="sub" style="margin:4px 0 0;font-size:12px">• ${esc(p.obs)}</div>` : ''}${s === 'postado' && (v.media_id || p.media_id) ? `<div class="sub" style="margin:4px 0 0;font-size:11.5px">media ${esc(v.media_id || p.media_id)}</div>` : ''}
    ${p.legenda ? `<details style="margin-top:6px"><summary style="cursor:pointer;color:var(--amarelo);font-weight:700;font-size:13px">Legenda completa</summary><pre style="white-space:pre-wrap;font:inherit;font-size:13px">${esc(p.legenda)}</pre></details>` : ''}
    ${telas}<div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:8px">${bts}${p.legenda ? `<button class="btn lin" type="button" data-agleg="${i}" style="padding:6px 10px;font-size:12px">Copiar legenda</button>` : ''}</div></div></div>`; };
const cardArte = (a, k) => { const v = (D.artes || {})[chaveArte(a)] || {}, b = (t, x, cl) => `<button class="btn ${cl}" type="button" data-arte="${k}" data-acao="${x}" style="padding:6px 10px;font-size:12px">${t}</button>`;
  const bt = abaArte === 'pend' ? b('Aprovar', 'aprovado', 'am') + b('Pedir ajuste', 'ajuste', 'lin') : abaArte === 'aj' ? b('Aprovar', 'aprovado', 'am') : abaArte === 'apr' ? b('Marcar como postado', 'postado', 'am')
    : `<span class="sub" style="margin:0;align-self:center">Postado${v.em ? ' em ' + new Date(v.em).toLocaleDateString('pt-BR') : ''}${v.por ? ' · ' + esc(v.por) : ''}</span>` + b('Voltar para a postar', 'despostar', 'lin');
  return `<div class="card" style="padding:10px${abaArte === 'post' ? ';opacity:.75' : ''}"><img loading="lazy" src="${a.img}" alt="${esc(a.titulo)}" style="width:100%;border-radius:10px;display:block">
   ${(a.telas || []).length > 1 ? `<div style="display:flex;gap:6px;overflow-x:auto;margin-top:8px">${a.telas.map(t => `<a href="${t}" target="_blank" rel="noopener">${/\.mp4$/.test(t) ? `<video src="${t}" muted loop autoplay playsinline preload="metadata" style="height:74px;border-radius:6px;display:block"></video>` : `<img loading="lazy" src="${t}" alt="tela" style="height:74px;border-radius:6px;display:block">`}</a>`).join('')}</div>` : ''}
   <div class="sub" style="margin:8px 0 2px">${esc(a.data || '')}</div><b style="display:block">${esc(a.titulo)}</b>
   ${a.legenda ? `<details style="margin-top:6px"><summary style="cursor:pointer;color:var(--amarelo);font-weight:700">${a.data === 'stories' ? 'Roteiro de postagem' : 'Legenda SEO'}</summary><pre style="white-space:pre-wrap;font:inherit;font-size:13px">${esc(a.legenda)}</pre></details>` : ''}
   <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:8px">${bt}${a.legenda ? `<button class="btn lin" type="button" data-copialeg="${k}" style="padding:6px 10px;font-size:12px">Copiar legenda</button>` : ''}${(a.telas || [a.img]).map((t, m) => `<a class="btn lin" download href="${t}" style="padding:6px 10px;font-size:12px">Baixar${(a.telas || []).length > 1 ? ' ' + (m + 1) : ''}${/\.mp4$/.test(t) ? ' (vídeo)' : ''}</a>`).join('')}</div></div>`; };
// prévia do grid do perfil: o mais novo no canto de cima à esquerda, 3 por linha, e a conferência do xadrez (vizinhos de cor diferente)
const gridAg = () => { const L = AG.map((p, i) => [p, i]).filter(([p]) => p.seq && stAg(p) !== 'bloqueado').sort((a, b) => b[0].seq - a[0].seq);
  let viz = 0, alt = 0; L.forEach(([p], k) => { [[k + 1, k % 3 < 2], [k + 3, true]].forEach(([j, ok]) => { if (ok && L[j]) { viz++; if (L[j][0].cor !== p.cor) alt++; } }); });
  const tile = ([p]) => { const s = stAg(p); return `<div style="position:relative${s === 'postado' ? '' : ';opacity:' + (s === 'agendado' ? '.92' : '.6')}">${mini(p, 4)}
    <span style="position:absolute;left:6px;top:6px;font:700 10px var(--f-dado);background:rgba(10,10,10,.78);color:#fff;border-radius:99px;padding:2px 7px">${p.seq}</span>
    <span style="position:absolute;right:6px;top:6px;font:700 9.5px var(--f-corpo);border-radius:99px;padding:2px 7px;${s === 'postado' ? 'background:var(--ok);color:#0A0A0A' : s === 'agendado' ? 'background:var(--amarelo);color:#0A0A0A' : 'background:rgba(10,10,10,.78);color:#fff'}">${s === 'postado' ? 'no ar' : s === 'agendado' ? dataHora(p.quando).replace(/^\S+ /, '') : 'aprovar'}</span>
    ${p.formato !== 'post' ? `<span style="position:absolute;right:6px;bottom:6px;font:700 9.5px var(--f-corpo);background:rgba(10,10,10,.78);color:#fff;border-radius:99px;padding:2px 7px">${FMT[p.formato]}</span>` : ''}</div>`; };
  return `<div class="grade g21"><div class="card"><h3>Grid do perfil · @lindsonalmeida_</h3><p class="sub">Como o feed vai ficar na ordem de postagem: o mais novo no canto de cima à esquerda. Apagado = ainda não aprovado.</p>
    <div style="max-width:460px;margin:0 auto;display:grid;grid-template-columns:repeat(3,1fr);gap:3px;background:var(--fundo);padding:3px;border-radius:10px">${L.map(tile).join('')}</div></div>
   <div class="card"><h3>Feed harmônico e xadrez</h3><p class="sub">Regra: a cor da capa alterna (preto e amarelo) e o formato também, para o grid ficar em xadrez.</p>
    <div class="grade g2" style="margin:8px 0">${kpi('Vizinhos alternando cor', viz ? Math.round(alt / viz * 100) + '%' : '—', `${alt} de ${viz} pares no grid`)}${kpi('Capas', `${L.filter(([p]) => p.cor === 'amarelo').length} / ${L.filter(([p]) => p.cor !== 'amarelo').length}`, 'amarelas / pretas')}</div>
    <div class="rot" style="margin:10px 0 6px">Ordem de postagem</div><div style="display:flex;gap:4px;flex-wrap:wrap">${L.slice().reverse().map(([p]) => `<span title="${esc(p.titulo)}" style="width:22px;height:22px;border-radius:5px;display:grid;place-items:center;font:700 10px var(--f-dado);background:${(COR[p.cor] || COR.preto)[0]};color:${(COR[p.cor] || COR.preto)[1]};border:1px solid var(--linha)">${p.seq}</span>`).join('')}</div>
    <p class="sub" style="margin-top:10px">${esc((R.agenda || {}).regra || '')}</p></div></div>`; };
V['rede-artes'] = () => { const T0 = R.artes || [], L = T0.map((a, k) => [a, k]).filter(([a]) => stArte(a) === abaArte && (abaArte === 'pend' || abaArte === 'aj' || !naAgenda(a)));
  const ag = AG.map((p, i) => [p, i]), porSt = s => ag.filter(([p]) => stAg(p) === s);
  const agApr = porSt('agendado').sort((a, b) => String(a[0].quando).localeCompare(String(b[0].quando))), agPost = porSt('postado').sort((a, b) => String(quandoAg(b[0])).localeCompare(String(quandoAg(a[0])))),
    agPend = porSt('aguardando aprovação').sort((a, b) => String(a[0].quando).localeCompare(String(b[0].quando))), agAj = porSt('ajuste'), agBloq = porSt('bloqueado');
  const n = { pend: agPend.length, aj: agAj.length, apr: agApr.length, post: agPost.length, grid: '' };
  T0.forEach(a => { const s = stArte(a); if (s === 'pend' || s === 'aj' || !naAgenda(a)) n[s]++; });
  const abas = [['pend', 'Para aprovar'], ['aj', 'Em ajuste'], ['apr', 'Aprovados · a postar'], ['post', 'Postados'], ['grid', 'Grid do perfil']].filter(([k]) => k !== 'aj' || n.aj);
  const prox = agApr.find(([p]) => new Date(p.quando) >= new Date()) || agApr[0];
  const topo = `<div class="grade g4">${kpi('Postados', agPost.length, agPost[0] ? 'último ' + dataHora(quandoAg(agPost[0][0])) : 'nenhum ainda')}${kpi('Agendados', agApr.length, prox ? 'próximo ' + dataHora(prox[0].quando) : 'sem horário')}${kpi('Aguardando aprovação', agPend.length + agAj.length, 'Reels da leva de 30 s')}${kpi('Bloqueados', agBloq.length, agBloq.length ? 'falta autorização' : 'nada travado')}</div>
  <div class="card"><h3>Artes do seu Instagram</h3><p class="sub">A agenda do Windsor posta sozinha nos horários (fuso de São Luís) e marca aqui. Se postar pelo celular, toque em "Marcar postado".</p>
   <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:10px">${abas.map(([k, t]) => `<button class="btn ${k === abaArte ? 'am' : 'lin'}" type="button" data-abaarte="${k}" style="padding:7px 12px;font-size:13px">${t}${k === 'grid' ? '' : ` (${n[k]})`}</button>`).join('')}</div></div>`;
  if (abaArte === 'grid') return topo + gridAg();
  const lista = { pend: agPend, aj: agAj, apr: agApr, post: agPost }[abaArte] || [];
  const blocoAg = lista.length ? `<div class="rot" style="margin:18px 0 10px">${{ pend: 'Agenda · esperando o seu ok', aj: 'Agenda · em ajuste', apr: 'Agenda · na ordem de postagem', post: 'Agenda · já no ar' }[abaArte]}</div><div class="grade g2">${lista.map(([p, i]) => cardAg(p, i)).join('')}</div>` : '';
  const blocoBloq = abaArte === 'apr' && agBloq.length ? `<div class="rot" style="margin:18px 0 10px">Fora da agenda</div><div class="grade g2">${agBloq.map(([p, i]) => cardAg(p, i)).join('')}</div>` : '';
  const blocoArtes = L.length ? `<div class="rot" style="margin:18px 0 10px">${abaArte === 'apr' ? 'Outras artes aprovadas, sem horário' : abaArte === 'post' ? 'Outras artes marcadas como postadas' : 'Artes'}</div><div class="grade g3">${L.map(([a, k]) => cardArte(a, k)).join('')}</div>` : '';
  const vazio = { pend: 'Nada esperando a sua aprovação.', aj: 'Nenhuma arte em ajuste.', apr: 'Nenhuma arte aprovada esperando para postar.', post: 'Nada postado ainda. Ao marcar como postado, a arte vem para cá.' }[abaArte];
  return topo + (blocoAg || blocoArtes || blocoBloq ? blocoAg + blocoBloq + blocoArtes : `<div class="card"><p class="sub" style="margin:0">${vazio}</p></div>`); };

// ---- 8 · Minhas fotos: o Lindson sobe as fotos dele para as artes (copiado do modelo prototipo/fotos.js, conta Lindson 01/11).
// Vão para /api/fotos?cli=lindson (KV), reduzidas no aparelho para 2048 px + miniatura de 480 px. Pedido do Lindson 03/11: "não tem a aba de subir minhas fotos".
const FCLI = 'lindson', FCATS = ['Retrato (rosto, olhando para a câmera)', 'Meio corpo / braços cruzados', 'Gravando com cliente (bastidor)', 'No computador ou no celular', 'Apontando ou fazendo gesto', 'Outras'];
let fotos = null, fRemoto = null, fFiltro = '', fEnv = '', fCat = FCATS[0];
async function fCarrega() {
  try { const r = await fetch(`/api/fotos?cli=${FCLI}`, { headers: { Accept: 'application/json' } });
    if (r.ok && (r.headers.get('content-type') || '').includes('json')) { fotos = (await r.json()).fotos; fRemoto = true; } else { fotos = []; fRemoto = false; if (r.status === 401) toast('Sua sessão expirou. Entre de novo na Central.'); } }
  catch (e) { fotos = []; fRemoto = false; }
  if ((location.hash || '').slice(1) === 'rede-fotos') render();
}
fCarrega();
function reduz(file, max, q) { return new Promise((ok, erro) => { const url = URL.createObjectURL(file), img = new Image();
  img.onload = () => { const k = Math.min(1, max / Math.max(img.naturalWidth, img.naturalHeight)), w = Math.round(img.naturalWidth * k), h = Math.round(img.naturalHeight * k);
    const c = document.createElement('canvas'); c.width = w; c.height = h; c.getContext('2d').drawImage(img, 0, 0, w, h); URL.revokeObjectURL(url); c.toBlob(b => b ? ok({ b, w, h }) : erro(new Error('falhou')), 'image/jpeg', q); };
  img.onerror = () => { URL.revokeObjectURL(url); erro(new Error('formato')); }; img.src = url; }); }
async function fEnvia(lista) {
  lista = [...lista].filter(f => /^image\//.test(f.type) || /\.(jpe?g|png|webp|heic|heif)$/i.test(f.name));
  if (!lista.length) return toast('Escolha fotos (JPG, PNG ou do iPhone).');
  let ok = 0, falha = 0;
  for (let i = 0; i < lista.length; i++) { fEnv = `Enviando ${i + 1} de ${lista.length}…`; render();
    try { const g = await reduz(lista[i], 2048, 0.9), m = await reduz(lista[i], 480, 0.8), nome = lista[i].name.replace(/\.[^.]+$/, '').slice(0, 60);
      const r = await fetch(`/api/fotos?cli=${FCLI}&cat=${encodeURIComponent(fCat)}&nome=${encodeURIComponent(nome)}&w=${g.w}&h=${g.h}`, { method: 'POST', headers: { 'Content-Type': 'image/jpeg' }, body: g.b });
      const j = await r.json().catch(() => ({})); if (!r.ok) throw new Error(j.erro || 'erro');
      await fetch(`/api/fotos?cli=${FCLI}&id=${j.id}&thumb=1`, { method: 'POST', headers: { 'Content-Type': 'image/jpeg' }, body: m.b });
      fotos.unshift({ id: j.id, ...j }); ok++; }
    catch (e) { falha++; if (/sessão|Entre/.test(e.message)) { toast(e.message); break; } } }
  fEnv = ''; render();
  toast(falha ? `${ok} enviada(s), ${falha} não foi(ram). Tente de novo.` : `${ok} foto(s) enviada(s). Já entram nas próximas artes.`);
}
V['rede-fotos'] = () => {
  if (fotos === null) return `<div class="card"><p class="sub">Carregando suas fotos…</p></div>`;
  if (!fRemoto) return `<div class="card"><h3>Minhas fotos</h3><p class="sub" style="margin:0">O envio funciona no site da Central (lindsonalmeida.pages.dev), com o seu login de administrador.</p></div>`;
  const l = fotos.filter(f => !fFiltro || f.cat === fFiltro), usadas = [...new Set(fotos.map(f => f.cat))];
  return `<div class="grade g21"><div class="card"><h3>Subir minhas fotos</h3><p class="sub">Elas viram as fotos das suas artes (recortadas em preto e branco). Melhor: vertical, rosto bem iluminado, fundo simples, sem filtro. Varie: sério, sorrindo, apontando, braços cruzados, gravando.</p>
    <div id="ft-zona" style="border:2px dashed var(--linha);border-radius:14px;padding:18px;text-align:center;display:grid;gap:10px;justify-items:center"><label class="sub" style="margin:0">Tipo de foto <select id="ft-cat" style="background:var(--painel2);color:var(--texto);border:1px solid var(--linha);border-radius:9px;padding:9px 11px;max-width:100%">${FCATS.map(c => `<option ${c === fCat ? 'selected' : ''}>${esc(c)}</option>`).join('')}</select></label>
     <input type="file" id="ft-arq" accept="image/*" multiple hidden><button class="btn am" type="button" id="ft-escolhe" ${fEnv ? 'disabled' : ''}>${fEnv || 'Escolher fotos'}</button>
     <span class="sub" style="margin:0;font-size:12px">Pode escolher várias de uma vez. No computador, dá para arrastar para cá.</span></div></div>
   <div class="card"><h3>Resumo</h3><p class="sub">${fotos.length} foto(s) no banco.</p><div class="lista">${usadas.map(c => `<div style="display:flex;justify-content:space-between;font-size:13px"><span>${esc(c)}</span><b>${fotos.filter(f => f.cat === c).length}</b></div>`).join('') || '<div style="font-size:12px;color:var(--apagado)">Nenhuma foto ainda.</div>'}</div><p class="sub" style="margin-top:10px">Para a semana 1 de artes, 8 a 10 fotos já bastam.</p></div></div>
  <div class="card"><h3>Banco de fotos</h3>${usadas.length > 1 ? `<div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:12px"><button class="btn lin" type="button" data-ftf="" style="padding:6px 12px;font-size:12px">Todas</button>${usadas.map(c => `<button class="btn lin" type="button" data-ftf="${esc(c)}" style="padding:6px 12px;font-size:12px">${esc(c)}</button>`).join('')}</div>` : ''}
   ${l.length ? `<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px">${l.map(f => `<div style="background:var(--painel2);border:1px solid var(--linha);border-radius:12px;overflow:hidden"><a href="/api/foto?cli=${FCLI}&id=${f.id}" target="_blank" rel="noopener"><img loading="lazy" src="/api/foto?cli=${FCLI}&id=${f.id}&mini=1" alt="${esc(f.cat)}" style="width:100%;aspect-ratio:4/5;object-fit:cover;display:block"></a><div style="padding:8px 10px;display:grid;gap:6px;font-size:12px"><b>${esc(f.cat)}</b><span style="color:var(--apagado)">${f.em ? new Date(f.em).toLocaleDateString('pt-BR') : ''}</span><div style="display:flex;gap:6px"><a class="btn lin" style="flex:1;padding:6px;font-size:12px" href="/api/foto?cli=${FCLI}&id=${f.id}&baixar=1">Baixar</a><button class="btn lin" style="flex:1;padding:6px;font-size:12px" type="button" data-ftdel="${f.id}">Excluir</button></div></div></div>`).join('')}</div>`
     : '<p class="sub" style="margin:0">Nenhuma foto ainda. Use "Escolher fotos" acima.</p>'}</div>`;
};

Object.assign(T, { 'rede-fotos': 'Minhas fotos', rede: 'Minha rede · visão', 'rede-estrategia': 'Estratégia de conteúdo', 'rede-calendario': 'Calendário editorial', 'rede-lote': 'Gravação da semana', 'rede-leads': 'Leads das iscas', 'rede-relatorio': 'Relatório semanal', 'rede-artes': 'Artes' });

// ---- ações (depois de cada tela)
const ant = window.__pos;
window.__pos = view => {
  if (ant) ant(view);
  const $$ = s => document.querySelectorAll('#conteudo ' + s), $1 = s => document.querySelector('#conteudo ' + s);
  $$('[data-copialeg]').forEach(b => b.onclick = () => { const a = (R.artes || [])[+b.dataset.copialeg]; if (a && navigator.clipboard) navigator.clipboard.writeText(a.legenda); toast(a && a.data === 'stories' ? 'Roteiro copiado' : 'Legenda copiada'); });
  $$('[data-abaarte]').forEach(b => b.onclick = () => { abaArte = b.dataset.abaarte; render(); });
  $$('[data-arte]').forEach(b => b.onclick = () => { const a = (R.artes || [])[+b.dataset.arte]; if (!a) return; const x = b.dataset.acao, ch = chaveArte(a);
    salva(d => { d.artes = d.artes || {}; const v = d.artes[ch] = d.artes[ch] || {};
      if (x === 'postado') { v.postado = true; v.em = new Date().toISOString(); v.por = 'Lindson'; } else if (x === 'despostar') { delete v.postado; delete v.em; delete v.por; v.st = 'aprovado'; } else v.st = x; },
      { aprovado: 'Aprovada', ajuste: 'Pedido de ajuste registrado', postado: 'Marcada como postada', despostar: 'Voltou para a postar' }[x]); });
  $$('[data-agleg]').forEach(b => b.onclick = () => { const p = AG[+b.dataset.agleg]; if (p && navigator.clipboard) navigator.clipboard.writeText(p.legenda); toast('Legenda copiada'); });
  $$('[data-ag]').forEach(b => b.onclick = () => { const p = AG[+b.dataset.ag]; if (!p) return; const x = b.dataset.agacao, ch = 'ag:' + p.id;
    salva(d => { d.artes = d.artes || {}; const v = d.artes[ch] = d.artes[ch] || {};
      if (x === 'postado') { v.postado = true; v.em = new Date().toISOString(); v.por = 'Lindson'; } else if (x === 'despostar') { delete v.postado; delete v.em; delete v.por; } else v.st = x; },
      { aprovado: 'Aprovado: entra na agenda', ajuste: 'Pedido de ajuste registrado', postado: 'Marcado como postado', despostar: 'Voltou para a postar' }[x]); });
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
  if ((location.hash || '').slice(1) === 'rede-fotos') { const arq = $1('#ft-arq'), zona = $1('#ft-zona'), sel = $1('#ft-cat'), bt = $1('#ft-escolhe');
    if (sel) sel.onchange = () => { fCat = sel.value; }; if (bt) bt.onclick = () => arq.click(); if (arq) arq.onchange = () => { if (arq.files.length) fEnvia(arq.files); };
    if (zona) { zona.ondragover = e => { e.preventDefault(); zona.style.borderColor = 'var(--amarelo)'; }; zona.ondragleave = () => { zona.style.borderColor = ''; }; zona.ondrop = e => { e.preventDefault(); zona.style.borderColor = ''; if (!fEnv) fEnvia(e.dataTransfer.files); }; }
    $$('[data-ftf]').forEach(b => b.onclick = () => { fFiltro = b.dataset.ftf; render(); });
    $$('[data-ftdel]').forEach(b => b.onclick = async () => { if (!confirm('Excluir esta foto?')) return; const r = await fetch(`/api/fotos?cli=${FCLI}&id=${b.dataset.ftdel}`, { method: 'DELETE' }); if (r.ok) { fotos = fotos.filter(f => f.id !== b.dataset.ftdel); render(); toast('Foto excluída'); } else toast('Não consegui excluir. Tente de novo.'); }); }
};
})();
