// Painel com DADOS REAIS: troca as telas de exemplo do modelo (painel.html) pelos dados do cliente em window.__DADOS.
// Os dados ficam no repositório privado (CentralLindsonALmeida/dados/<cliente>.json), nunca no repositório público.
// O que não tem número real aparece como "a medir" (regra: nunca inventar números). Conta Lindson, 01/11/2026.
(() => {
const D = window.__DADOS; if (!D) return;
const H = window.__h, V = window.__V, { BASE, APROV, PEDIDOS, bomDia, chip } = H, b = BASE[H.cli()];
// o montar-<cliente>.py expõe window.__h = {BASE, APROV, PEDIDOS, bomDia, chip, cli} (ver montar-jaci.py)
Object.assign(b, { nome: D.nome, seg: D.seg, plano: D.plano, inicio: D.inicio });
PEDIDOS.length = 0;
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const num = n => n == null || n === '' ? null : typeof n === 'number' ? n.toLocaleString('pt-BR') : esc(n);
const vazio = t => `<div class="item"><div class="d" style="color:var(--apagado)">${t}</div></div>`;
const ig = D.instagram || {};
const kpi = (r, v, n) => `<div class="card kpi"><div class="rot">${r}</div><div class="val">${v ?? 'a medir'}</div><div class="var up"><span>${n || ''}</span></div></div>`;
const difSeg = ig.anterior && typeof ig.seguidores === 'number' ? ig.seguidores - ig.anterior.seguidores : null;
const kpis = () => `<div class="grade g4">
  ${kpi('Seguidores', num(ig.seguidores), ig.var_seguidores ? esc(ig.var_seguidores) : difSeg === null ? 'Instagram · ' + esc(ig.data) : (difSeg >= 0 ? '+' : '') + num(difSeg) + ' desde o ' + esc(ig.anterior.rotulo))}
  ${kpi('Visualizações (30 dias)', esc(ig.visualizacoes), esc(ig.var_visualizacoes || ig.periodo))}
  ${kpi(ig.novos_rotulo || 'Novos seguidores', num(ig.novos_seguidores), esc(ig.periodo))}
  ${window.__crmResumo ? kpi('Avaliações marcadas', num(window.__crmResumo().marcadas), 'no CRM de pacientes') : D.kpi4 ? kpi(esc(D.kpi4[0]), D.kpi4[1] == null ? null : esc(D.kpi4[1]), esc(D.kpi4[2])) : kpi('Avaliações agendadas', null, 'quando as campanhas começarem')}</div>`;
const metas = () => !(D.metas || []).length ? `<p class="sub" style="margin:0">${esc(D.semMetas || 'Sem metas numéricas ainda: a primeira medição define a base.')}</p>` : `<div class="lista">${(D.metas || []).map(([n, a, m]) => `<div><div style="display:flex;justify-content:space-between"><span>${esc(n)}</span><b>${a == null ? 'a medir' : num(a)} / ${num(m)}</b></div><div class="barra"><i style="width:${a == null ? 0 : Math.min(100, a / m * 100)}%"></i></div></div>`).join('')}</div>`;
const prox = () => (D.entregas || []).filter(e => e[3] !== 'entregue');

V.inicio = () => bomDia() + kpis() + `
 <div class="grade g21"><div class="card"><h3>Seu Instagram hoje</h3><p class="sub">Números do painel do Instagram em ${esc(ig.data)} (${esc(ig.periodo)}).</p>
  <div class="tab"><table><tbody>${[['Perfil', esc(ig.perfil)], ['Publicações', num(ig.posts)], ['Seguidores', num(ig.seguidores)], ['Visualizações em 30 dias', esc(ig.visualizacoes)], [(ig.novos_rotulo || 'Novos seguidores') + ' em 30 dias', num(ig.novos_seguidores)], ['Conteúdos publicados em 30 dias', num(ig.conteudos)]].map(([a, v]) => `<tr><td>${a}</td><td><b>${v ?? 'a medir'}</b></td></tr>`).join('')}</tbody></table></div></div>
  <div class="card"><h3>Metas</h3>${(D.metas || []).length ? '<p class="sub">Combinadas na estratégia. Começam a ser medidas com as campanhas.</p>' : ''}${metas()}</div></div>
 <div class="grade g2"><div class="card"><h3>Precisa da sua aprovação</h3><p class="sub">Conteúdos esperando você.</p><div class="lista">${APROV.filter(p => p.st === 'aguardando').map(p => `<div class="item"><div><div class="t">${esc(p.titulo)}</div><div class="d">${esc(p.t)}</div></div></div>`).join('') || vazio('Nada esperando por você agora.')}</div><a class="btn am" href="#aprovacoes" style="margin-top:12px;width:100%">Revisar agora</a></div>
  <div class="card"><h3>Próximos passos</h3><p class="sub">O que a agência está fazendo.</p><div class="lista">${prox().map(e => `<div class="item"><div><div class="t">${esc(e[0])}</div><div class="d">Previsto: ${esc(e[2])}</div></div><div class="fim">${chip(e[3])}</div></div>`).join('') || vazio('Tudo entregue até aqui.')}</div></div></div>`;

V.resultados = () => kpis() + `
 <div class="card"><h3>Conteúdos com mais visualizações</h3><p class="sub">Do seu perfil, em ${esc(ig.data)}.</p><div class="tab"><table><thead><tr><th>Conteúdo</th><th>Formato</th><th>Visualizações</th></tr></thead><tbody>
  ${(ig.destaques || []).map(r => `<tr>${r.map(c => `<td>${esc(c)}</td>`).join('')}</tr>`).join('') || '<tr><td colspan="3">a medir</td></tr>'}</tbody></table></div></div>
 ${ig.anterior ? `<div class="card"><h3>Comparação</h3><p class="sub">Como o perfil mudou desde o ${esc(ig.anterior.rotulo)}.</p><div class="tab"><table><thead><tr><th></th><th>Antes</th><th>Agora (${esc(ig.data)})</th></tr></thead><tbody>
  <tr><td>Seguidores</td><td>${num(ig.anterior.seguidores)}</td><td>${num(ig.seguidores)}</td></tr><tr><td>Visualizações em 30 dias</td><td>${esc(ig.anterior.visualizacoes)}</td><td>${esc(ig.visualizacoes)}</td></tr></tbody></table></div></div>` : ''}`;

V.relatorios = () => `<div class="card"><h3>Relatórios mensais</h3><p class="sub">Resumo do mês, o que funcionou e o plano do próximo mês.</p><div class="lista">${(D.relatorios || []).map(r => `<div class="item"><div><div class="t">Relatório de ${esc(r[0])}</div><div class="d">${esc(r[2] || '')}</div></div><div class="fim">${chip(r[1])}</div></div>`).join('') || vazio('Os relatórios aparecem aqui assim que forem entregues.')}</div></div>`;

V.entregas = () => `<div class="card"><h3>Entregas e arquivos</h3><p class="sub">Tudo o que a agência já entregou e o que está a caminho.</p><div class="tab"><table><thead><tr><th>Entrega</th><th>Tipo</th><th>Data</th><th>Status</th></tr></thead><tbody>${(D.entregas || []).map(e => `<tr><td>${esc(e[0])}</td><td>${esc(e[1])}</td><td>${esc(e[2])}</td><td>${chip(e[3])}</td></tr>`).join('')}</tbody></table></div></div>`;

V.campanhas = () => (D.campanhas || []).length ? `<div class="card"><h3>Campanhas</h3><p class="sub">Anúncios no Meta (Instagram e Facebook).</p><div class="tab"><table><thead><tr><th>Campanha</th><th>Status</th><th>Orçamento</th><th>Custo por conversa</th><th>Conversas</th></tr></thead><tbody>${D.campanhas.map(c => `<tr><td>${esc(c[0])}</td><td>${chip(c[1])}</td><td>${esc(c[2])}</td><td>${esc(c[3])}</td><td>${esc(c[4])}</td></tr>`).join('')}</tbody></table></div></div>`
  : `<div class="card"><h3>Campanhas</h3><p class="sub">As campanhas ainda não começaram. Quando entrarem no ar, aqui aparecem o investimento, as conversas no WhatsApp e o custo de cada uma.</p><div class="lista">${prox().filter(e => /campanh|anúnc/i.test(e[0] + e[1])).map(e => `<div class="item"><div><div class="t">${esc(e[0])}</div><div class="d">Previsto: ${esc(e[2])}</div></div><div class="fim">${chip(e[3])}</div></div>`).join('')}</div></div>`;

V.reunioes = () => `<div class="card"><h3>Reuniões</h3><p class="sub">Encontros marcados com a equipe.</p><div class="lista">${(D.reunioes || []).map(r => `<div class="item"><div><div class="t">${esc(r[0])}</div><div class="d">${esc(r[1])} · ${esc(r[2])}</div></div></div>`).join('') || vazio('Nenhuma reunião marcada.')}</div><a class="btn am" style="margin-top:12px" href="https://wa.me/5598985621808?text=Oi%2C%20Lindson%21%20Quero%20marcar%20uma%20reuni%C3%A3o." target="_blank" rel="noopener">Pedir reunião</a></div>`;

V.contrato = d => `<div class="grade g2"><div class="card"><h3>Seu plano</h3><p class="sub">Serviços contratados.</p><div class="lista"><div class="item"><div><div class="t">${esc(d.plano)}</div><div class="d">Cliente desde ${esc(d.inicio)}</div></div><div class="fim">${chip('Ativa')}</div></div></div></div>
 <div class="card"><h3>Pagamentos</h3><p class="sub">Mensalidades da agência.</p><div class="tab"><table><thead><tr><th>Mês</th><th>Vencimento</th><th>Status</th></tr></thead><tbody>${(D.pagamentos || []).map(p => `<tr><td>${esc(p[0])}</td><td>${esc(p[1])}</td><td>${chip(p[2])}</td></tr>`).join('') || '<tr><td colspan="3">Nenhum pagamento registrado aqui ainda.</td></tr>'}</tbody></table></div></div></div>`;


const PL = D.planejamento;
if (PL) V.planejamento = d => {
  const mx = Math.max(...PL.linhas.map(l => parseInt(l[1]) || 0), 1);
  return `<div class="card"><h3>Objetivo</h3><p class="sub" style="margin:0">${esc(PL.objetivo)}</p><p class="sub" style="margin:8px 0 0;font-size:12px">${esc(PL.fonte)} · ${esc(d.plano)}</p></div>
  <div class="card"><h3>Linhas editoriais</h3><p class="sub">Sobre o que falamos e por quê. O % é a fatia de cada linha nos posts do mês.</p>
   <div class="tab"><table><thead><tr>${PL.colunas.map(c => `<th>${esc(c)}</th>`).join('')}</tr></thead><tbody>${PL.linhas.map(l => `<tr><td><b>${esc(l[0])}</b><div class="barra" style="margin-top:6px;min-width:90px"><i style="width:${(parseInt(l[1]) || 0) / mx * 100}%"></i></div></td>${l.slice(1).map(c => `<td>${esc(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>
   ${PL.linhasNota ? `<p class="sub" style="margin:10px 0 0">${esc(PL.linhasNota)}</p>` : ''}</div>
  <div class="grade g21"><div class="card"><h3>Ritmo da semana</h3><p class="sub">${esc(PL.ritmoNota || '')}</p><div class="tab"><table><thead><tr><th>Dia</th><th>Feed</th><th>Stories</th></tr></thead><tbody>${(PL.ritmo || []).map(r => `<tr>${r.map(c => `<td>${esc(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></div></div>
   <div class="card"><h3>Plano de 90 dias</h3><div class="lista">${(PL.fases || []).map(([t, x]) => `<div class="fase"><b>${esc(t)}</b><span class="sub" style="margin:0">${esc(x)}</span></div>`).join('')}</div></div></div>
  ${(PL.datas || []).length ? `<div class="card"><h3>Datas comemorativas do ano</h3><p class="sub">${esc(PL.datasNota || '')}</p><div class="tab"><table><thead><tr><th>Data</th><th>O que é</th><th>Ideia de conteúdo</th></tr></thead><tbody>${PL.datas.map(r => `<tr>${r.map((c, i) => `<td>${i === 0 ? '<b>' + esc(c) + '</b>' : esc(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></div></div>` : ''}
  ${PL.regras ? `<div class="card" style="border-color:var(--amarelo)"><h3>Regras que valem para todo post</h3><p class="sub" style="margin:0">${esc(PL.regras)}</p></div>` : ''}`;
};

// Conteúdos › Datas comemorativas: as datas pesquisadas para o cliente (planejamento.datas), no lugar das datas genéricas do modelo
if (PL && (PL.datas || []).length) {
  const conteudosModelo = V.conteudos;
  V.conteudos = d => {
    const sub = window._sub || 'datas'; if (sub !== 'datas') return conteudosModelo(d);
    const bt = k => `<button aria-pressed="${sub === k}" data-sub="${k}">${{ datas: 'Datas comemorativas', carrosseis: 'Carrosséis', reels: 'Reels' }[k]}</button>`;
    return `<div class="card"><h3>Conteúdos</h3><p class="sub">Tudo que está sendo produzido para você.</p><div class="subabas" style="margin-bottom:14px">${bt('datas') + bt('carrosseis') + bt('reels')}</div>
     <p class="sub">${esc(PL.datasNota || '')}</p><div class="lista">${PL.datas.map(([dt, nome, ideia]) => `<div class="item"><div style="min-width:0"><div class="t">${esc(dt)} · ${esc(nome)}</div><div class="d">${esc(ideia)}</div></div></div>`).join('')}</div></div>`;
  };
}
const C = D.calendario;
if (!C) V.calendario = () => `<div class="card"><h3>Calendário</h3><p class="sub" style="margin:0">${esc(D.semCalendario || 'O calendário do mês aparece aqui quando estiver aprovado.')}</p></div>`;
if (C) V.calendario = () => {
  const ini = (new Date(C.ano, C.m - 1, 1).getDay() + 6) % 7, nd = new Date(C.ano, C.m, 0).getDate();
  let h = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'].map(x => `<div class="cab">${x}</div>`).join('') + '<div></div>'.repeat(ini);
  for (let d = 1; d <= nd; d++) h += `<div class="dia"><b>${d}</b>${(C.eventos[d] || []).map(([f, l, t]) => `<div class="ev" title="${esc(l + ' · ' + t)}">${esc(f)} · ${esc(l)}</div>`).join('')}</div>`;
  const lista = Object.keys(C.eventos).map(Number).sort((a, b) => a - b).map(d => C.eventos[d].map(([f, l, t]) => `<tr><td>${d}</td><td>${esc(f)}</td><td>${esc(l)}</td><td>${esc(t)}</td></tr>`).join('')).join('');
  return `<div class="card"><h3>${esc(C.mes)}</h3><p class="sub">Tema do mês: "${esc(C.tema)}". ${esc(C.fixos || '')}</p><div class="cal">${h}</div></div>
   <div class="card"><h3>Pautas do mês</h3><div class="tab"><table><thead><tr><th>Dia</th><th>Formato</th><th>Linha</th><th>Tema</th></tr></thead><tbody>${lista}</tbody></table></div></div>`;
};
document.querySelectorAll('.exemplo').forEach(e => e.textContent = 'Atualizado em ' + D.atualizado);
})();
