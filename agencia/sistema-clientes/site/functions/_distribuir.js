// Distribuidor da Central de Comando (conta Leandro, 09/11/2026). "Você vai ver qual conta está disponível e enviar o trabalho
// pra elas, escolhendo internamente, como um time de trabalho" (Lindson). O mesmo código roda no servidor (GET /api/automacao?fila=ped)
// e na página /painel/comando (o montar-comando.py cola este arquivo nela). Regras, nesta ordem:
//  a) só contas 🟢 trabalhando ou ⚪ livre, com batida da tarefa horária nas últimas 2 h; nunca conta esgotada;
//  b) continuidade: quem já está trabalhando no mesmo cliente (fila ou "Em andamento" do quadro);
//  c) especialidade: quem mais entregou aquela função ou aquele cliente (REGISTRO);
//  d) menor carga: menos pedidos abertos.
// eq = { contas: {Nome:{estado, ate, batida}}, perfil: {esp:{Nome:{cli:{}, func:{}}}, andamento:[{conta, cli, oque}]} }
export const CONTAS_EQ = ['Lindson', 'Zuleide', 'Pedro', 'Leandro'];
export const NOMES_CLI = { jaci: 'Dra. Jaci', tribuna: 'Tribuna 98', leo: 'Leo Pinto', rt: 'Real Time', oregano: 'Orégano Turbo', marca: 'Minha marca', outro: 'Outro' };
export const NOMES_FN = { reels: 'Reels', carrossel: 'Carrossel', post: 'Post', stories: 'Stories', legenda: 'Legenda SEO', data: 'Arte de data', site: 'Site', landing: 'Landing', painel: 'Painel do cliente', estrategia: 'Estratégia PDF', proposta: 'Proposta', contrato: 'Contrato', relatorio: 'Relatório' };
const ABERTO = ['novo', 'andamento', 'ajuste', 'espera'];
export function estadoReal(c, agora) {
  // estado efetivo da conta: limite vencido volta a livre; sem batida em 2 h = sem tarefa ativa
  const x = c || {}, t = agora || Date.now();
  let estado = x.estado || 'sem-dados';
  if (estado.startsWith('limite') && x.ate && Date.parse(x.ate) <= t) estado = 'livre';
  const ativa = !!x.batida && t - Date.parse(x.batida) <= 2 * 36e5;
  return { estado, ativa, disponivel: ativa && (estado === 'trabalhando' || estado === 'livre'), ate: x.ate || null };
}
export function carga(itens, conta) {
  return (itens || []).filter(i => ABERTO.includes(i.st) && (i.conta === conta || (!i.conta && i.designada === conta))).length;
}
export function distribuir(item, itens, eq, agora, evitar) {
  const t = agora || Date.now(), contas = (eq && eq.contas) || {}, perfil = (eq && eq.perfil) || {};
  let cand = CONTAS_EQ.filter(c => estadoReal(contas[c], t).disponivel);
  if (evitar && cand.length > 1) cand = cand.filter(c => c !== evitar);
  if (!cand.length) {
    const voltas = CONTAS_EQ.map(c => estadoReal(contas[c], t)).filter(e => e.estado.startsWith('limite') && e.ate).map(e => Date.parse(e.ate)).sort((a, b) => a - b);
    return { designada: null, motivo: voltas.length ? 'na espera: todas as contas sem tempo agora' : 'na espera: nenhuma conta com a tarefa horária ativa', volta: voltas.length ? new Date(voltas[0]).toISOString() : null };
  }
  const cli = NOMES_CLI[item.cli] || item.cli, fn = NOMES_FN[item.func] || item.func;
  // b) continuidade
  const naFila = (itens || []).find(i => i.id !== item.id && i.cli === item.cli && i.st === 'andamento' && cand.includes(i.conta));
  if (naFila) return { designada: naFila.conta, motivo: `${naFila.conta}: já está trabalhando em ${NOMES_FN[naFila.func] || naFila.func} de ${cli}` };
  const noQuadro = (perfil.andamento || []).find(a => a.cli === item.cli && cand.includes(a.conta));
  if (noQuadro) return { designada: noQuadro.conta, motivo: `${noQuadro.conta}: já está em "${String(noQuadro.oque || '').slice(0, 60)}"` };
  // c) especialidade
  const esp = perfil.esp || {};
  const pontos = c => ((esp[c] && esp[c].func && esp[c].func[item.func]) || 0) * 2 + ((esp[c] && esp[c].cli && esp[c].cli[item.cli]) || 0);
  const melhor = cand.slice().sort((a, b) => pontos(b) - pontos(a) || carga(itens, a) - carga(itens, b))[0];
  if (pontos(melhor) > 0) {
    const nf = (esp[melhor].func || {})[item.func] || 0, nc = (esp[melhor].cli || {})[item.cli] || 0;
    return { designada: melhor, motivo: `${melhor}: quem mais entregou ${nf >= nc ? fn + ' (' + nf + ')' : cli + ' (' + nc + ')'}` };
  }
  // d) menor carga
  const leve = cand.slice().sort((a, b) => carga(itens, a) - carga(itens, b))[0];
  return { designada: leve, motivo: `${leve}: menor carga (${carga(itens, leve)} aberto${carga(itens, leve) === 1 ? '' : 's'})` };
}
// redistribui a fila: pedido "novo"/"espera" cuja designada ficou indisponível, ou que ninguém pegou em 2 h. Devolve true se mudou algo.
export function redistribuir(itens, eq, agora) {
  const t = agora || Date.now(); let mudou = false;
  (itens || []).forEach(i => {
    if (!['novo', 'espera', 'ajuste'].includes(i.st)) return;
    const contas = (eq && eq.contas) || {};
    if (i.st === 'ajuste' && i.conta && estadoReal(contas[i.conta], t).disponivel) return; // ajuste fica com quem fez, se ela pode
    const des = i.designada, disp = des && estadoReal(contas[des], t).disponivel;
    const venceu = des && i.designadaEm && t - Date.parse(i.designadaEm) > 2 * 36e5;
    if (des && disp && !venceu) return;
    const r = distribuir(i, itens, eq, t, venceu ? des : null);
    if (r.designada === des && !venceu && i.st !== 'espera') return;
    if (r.designada === des && venceu) { i.designadaEm = new Date(t).toISOString(); mudou = true; return; } // só ela pode: renova o prazo
    i.designada = r.designada; i.motivo = r.motivo; i.volta = r.volta || null; i.designadaEm = new Date(t).toISOString();
    if (i.st !== 'ajuste') i.st = r.designada ? 'novo' : 'espera';
    i.historico = (i.historico || []).concat([{ em: i.designadaEm, de: des || null, para: r.designada, motivo: r.motivo }]).slice(-10);
    mudou = true;
  });
  return mudou;
}
