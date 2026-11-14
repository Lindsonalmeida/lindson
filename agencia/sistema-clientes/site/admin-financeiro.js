// Tela "Financeiro" do painel do ADMINISTRADOR (conta Leandro, 14/11/2026).
// Pedido do Lindson: "no meu painel, crie um painel completo de financeiro, extremamente completo".
// Dados no banco do admin (/api/db): coleção "financeiro" (lançamentos) e "financeiro-config" (doc "cfg": saldo inicial, meta, imposto).
// Lançamento: {tipo: receita|despesa, desc, valor, cat, cli, forma, venc: 'AAAA-MM-DD', rec: bool (todo mês desde venc), fim: 'AAAA-MM' opcional,
//              pago: {'AAAA-MM': 'AAAA-MM-DD'}}  → cada mês vira uma "ocorrência" paga ou pendente. Nada vem preenchido: só o que o Lindson lançar.
// Abas: Visão geral · Lançamentos · A receber · A pagar · Fluxo de caixa (12 meses) · DRE · Clientes e MRR · Configurações. Exporta CSV.
(() => {
const V = window.__V, T = window.__T, CLI = (window.__CLIENTES || []).map(c => [c.cliente, c.nome]);
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const render = () => window.__render && window.__render(), toast = t => window.__toast && window.__toast(t);
const R$ = v => (v < 0 ? '-' : '') + 'R$ ' + Math.abs(v || 0).toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
const R0 = v => (v < 0 ? '-' : '') + 'R$ ' + Math.round(Math.abs(v || 0)).toLocaleString('pt-BR');
const hojeISO = () => { const d = new Date(); return new Date(d - d.getTimezoneOffset() * 6e4).toISOString().slice(0, 10); };
const mesDe = iso => iso.slice(0, 7), addMes = (m, n) => { const [a, b] = m.split('-').map(Number), d = new Date(a, b - 1 + n, 1); return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0'); };
const NOMES = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'];
const nomeMes = m => NOMES[+m.slice(5) - 1] + '/' + m.slice(2, 4), br = iso => iso ? iso.slice(8, 10) + '/' + iso.slice(5, 7) + '/' + iso.slice(0, 4) : '';
const CAT = {
  receita: ['Gestão de redes (mensal)', 'Site / mini site', 'Identidade visual', 'Tráfego pago (gestão)', 'Produção de vídeo', 'Produto digital (Hubla)', 'Consultoria', 'Outras receitas'],
  despesa: ['Ferramentas e assinaturas', 'Anúncios (verba própria)', 'Equipe / freelancer', 'Impostos', 'Taxas (cartão, Hubla, banco)', 'Equipamento', 'Transporte', 'Alimentação', 'Aluguel / contas fixas', 'Pró-labore', 'Outras despesas'] };
const FORMAS = ['Pix', 'Cartão', 'Boleto', 'Hubla', 'Dinheiro', 'Transferência'];
let L = {}, cfg = { saldo: 0, meta: 0, imposto: 6, reserva: 0 }, carregou = false, aba = 'geral', mes = mesDe(hojeISO()), editando = null, busca = '', ftipo = '';
async function carrega() {
  try { const [a, b] = await Promise.all([fetch('/api/db?col=financeiro'), fetch('/api/db?col=financeiro-config')]);
    if (a.ok) L = ((await a.json()) || {}).docs || {}; if (b.ok) Object.assign(cfg, ((((await b.json()) || {}).docs || {}).cfg) || {}); } catch (e) {}
  carregou = true; render();
}
async function grava(ops, msg) {
  try { const r = await fetch('/api/db', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ ops }) }); if (!r.ok) throw 0; toast(msg); }
  catch (e) { toast('Não salvou. Confira a conexão e tente de novo.'); }
}
// ocorrências de um mês: lançamento único no mês do vencimento; recorrente em todo mês de venc até fim
function ocorr(m) {
  const out = [];
  for (const [id, x] of Object.entries(L)) {
    if (!x.venc) continue; const m0 = mesDe(x.venc);
    if (x.rec ? (m >= m0 && (!x.fim || m <= x.fim)) : m === m0) {
      const venc = x.rec ? m + x.venc.slice(7) : x.venc, pagoEm = (x.pago || {})[m] || '';
      out.push({ id, x, m, venc, pagoEm, valor: +x.valor || 0, atrasado: !pagoEm && venc < hojeISO() });
    }
  }
  return out.sort((a, b) => a.venc.localeCompare(b.venc));
}
const soma = (arr, f) => arr.filter(f).reduce((s, o) => s + o.valor, 0);
function resumo(m) {
  const o = ocorr(m), R = o.filter(i => i.x.tipo === 'receita'), D = o.filter(i => i.x.tipo === 'despesa');
  const rec = soma(R, i => i.pagoEm), desp = soma(D, i => i.pagoEm), recP = soma(R, () => 1), despP = soma(D, () => 1);
  return { o, R, D, rec, desp, recP, despP, lucro: rec - desp, lucroP: recP - despP, aRec: soma(R, i => !i.pagoEm), aPag: soma(D, i => !i.pagoEm),
    atrasoR: soma(R, i => i.atrasado), atrasoD: soma(D, i => i.atrasado), mrr: soma(R, i => i.x.rec), fixo: soma(D, i => i.x.rec) };
}
// saldo acumulado: saldo inicial + tudo que foi pago até o fim do mês m (desde o lançamento mais antigo)
function saldoAte(m) {
  const vs = Object.values(L).filter(x => x.venc).map(x => mesDe(x.venc)); if (!vs.length) return +cfg.saldo || 0;
  let s = +cfg.saldo || 0; for (let k = vs.sort()[0]; k <= m; k = addMes(k, 1)) { const r = resumo(k); s += r.rec - r.desp; } return s;
}
const kpi = (r, v, nota, cor) => `<div class="card kpi"><div class="rot">${r}</div><div class="val" style="${cor ? 'color:' + cor : ''}">${v}</div><div class="var up"><span>${nota || ''}</span></div></div>`;
const chip = (on, attr, txt) => `<button class="btn${on ? ' am' : ''}" ${attr} style="padding:7px 14px;font-size:13px">${txt}</button>`;
const ABAS = [['geral', 'Visão geral'], ['lanc', 'Lançamentos'], ['receber', 'A receber'], ['pagar', 'A pagar'], ['fluxo', 'Fluxo de caixa'], ['dre', 'DRE'], ['clientes', 'Clientes e MRR'], ['cfg', 'Configurações']];
// gráfico de barras em SVG: receitas x despesas pagas nos últimos 12 meses + linha do saldo
function grafico(meses) {
  const d = meses.map(k => ({ k, ...resumo(k), s: saldoAte(k) })), W = 900, H = 260, P = 34, mx = Math.max(1, ...d.map(x => Math.max(x.rec, x.desp, Math.abs(x.s)))), bw = (W - P * 2) / d.length;
  const y = v => H - P - (v / mx) * (H - P * 2), lin = d.map((x, i) => `${P + bw * i + bw / 2},${y(Math.max(0, x.s))}`).join(' ');
  return `<svg viewBox="0 0 ${W} ${H}" style="width:100%;height:auto;display:block">
   ${[0, .5, 1].map(f => `<line x1="${P}" x2="${W - P}" y1="${y(mx * f)}" y2="${y(mx * f)}" stroke="var(--linha)"/><text x="${P - 6}" y="${y(mx * f) + 4}" fill="var(--apagado)" font-size="10" text-anchor="end">${f ? (mx * f / 1000).toFixed(1) + 'k' : '0'}</text>`).join('')}
   ${d.map((x, i) => `<rect x="${P + bw * i + bw * .14}" y="${y(x.rec)}" width="${bw * .34}" height="${H - P - y(x.rec)}" rx="3" fill="var(--ok)"><title>${nomeMes(x.k)} receitas ${R$(x.rec)}</title></rect>
     <rect x="${P + bw * i + bw * .52}" y="${y(x.desp)}" width="${bw * .34}" height="${H - P - y(x.desp)}" rx="3" fill="var(--erro)"><title>${nomeMes(x.k)} despesas ${R$(x.desp)}</title></rect>
     <text x="${P + bw * i + bw / 2}" y="${H - 12}" fill="var(--apagado)" font-size="11" text-anchor="middle">${nomeMes(x.k)}</text>`).join('')}
   <polyline points="${lin}" fill="none" stroke="var(--amarelo)" stroke-width="2.5"/>${d.map((x, i) => `<circle cx="${P + bw * i + bw / 2}" cy="${y(Math.max(0, x.s))}" r="3.5" fill="var(--amarelo)"><title>Saldo ${R$(x.s)}</title></circle>`).join('')}</svg>
   <div style="display:flex;gap:16px;font-size:12px;color:var(--apagado);margin-top:6px"><span><b style="color:var(--ok)">■</b> Receitas recebidas</span><span><b style="color:var(--erro)">■</b> Despesas pagas</span><span><b style="color:var(--amarelo)">●</b> Saldo em caixa</span></div>`;
}
function barrasCat(lista, cor) {
  const por = {}; lista.forEach(o => { por[o.x.cat || 'Sem categoria'] = (por[o.x.cat || 'Sem categoria'] || 0) + o.valor; });
  const e = Object.entries(por).sort((a, b) => b[1] - a[1]), tot = e.reduce((s, x) => s + x[1], 0) || 1;
  return e.length ? e.map(([c, v]) => `<div style="margin:9px 0"><div style="display:flex;justify-content:space-between;font-size:13px"><span>${esc(c)}</span><b>${R$(v)} <span style="color:var(--apagado);font-weight:500">${Math.round(v / tot * 100)}%</span></b></div>
    <div style="height:7px;background:var(--painel2);border-radius:9px;margin-top:5px"><div style="height:100%;width:${v / tot * 100}%;background:${cor};border-radius:9px"></div></div></div>`).join('') : '<p class="sub" style="margin:0">Nada lançado neste mês.</p>';
}
function linha(o, acoes = true) {
  const x = o.x, rec = x.tipo === 'receita', st = o.pagoEm ? ['Pago ' + br(o.pagoEm).slice(0, 5), 'var(--ok)'] : o.atrasado ? ['Atrasado', 'var(--erro)'] : ['Pendente', 'var(--alerta)'];
  const cli = x.cli ? (CLI.find(c => c[0] === x.cli) || [0, x.cli])[1] : '';
  return `<tr><td>${br(o.venc).slice(0, 5)}</td><td><b>${esc(x.desc)}</b>${x.rec ? ' <span style="font-size:11px;color:var(--amarelo)">↻ mensal</span>' : ''}<div style="font-size:12px;color:var(--apagado)">${esc(x.cat || '')}${cli ? ' · ' + esc(cli) : ''}${x.forma ? ' · ' + esc(x.forma) : ''}</div></td>
   <td style="text-align:right;color:${rec ? 'var(--ok)' : 'var(--erro)'};font-weight:800;white-space:nowrap">${rec ? '+' : '−'} ${R$(o.valor)}</td><td><span style="color:${st[1]};font-weight:700;font-size:12px">${st[0]}</span></td>
   ${acoes ? `<td style="white-space:nowrap;text-align:right"><button class="btn${o.pagoEm ? '' : ' am'}" data-fpaga="${o.id}|${o.m}" style="padding:5px 10px;font-size:12px">${o.pagoEm ? 'Desfazer' : rec ? 'Recebi' : 'Paguei'}</button>
     <button class="btn" data-fedit="${o.id}" style="padding:5px 10px;font-size:12px">Editar</button></td>` : ''}</tr>`;
}
const tabela = (arr, acoes = true) => arr.length ? `<div class="tab"><table><thead><tr><th>Venc.</th><th>Descrição</th><th style="text-align:right">Valor</th><th>Situação</th>${acoes ? '<th></th>' : ''}</tr></thead><tbody>${arr.map(o => linha(o, acoes)).join('')}</tbody></table></div>` : '<p class="sub" style="margin:0">Nada por aqui.</p>';
function form() {
  const x = editando && editando !== 'novo' ? L[editando] : { tipo: ftipo || 'receita', venc: hojeISO(), forma: 'Pix' };
  const op = (lst, v) => lst.map(c => `<option${c === v ? ' selected' : ''}>${esc(c)}</option>`).join('');
  return `<div class="card" style="border:1px solid var(--amarelo)"><h3>${editando === 'novo' ? 'Novo lançamento' : 'Editar lançamento'}</h3>
   <form id="f-fin" class="grade g2" style="gap:12px">
    <label class="sub" style="margin:0">Tipo<select name="tipo" id="f-tipo"><option value="receita"${x.tipo === 'receita' ? ' selected' : ''}>Receita (entrada)</option><option value="despesa"${x.tipo === 'despesa' ? ' selected' : ''}>Despesa (saída)</option></select></label>
    <label class="sub" style="margin:0">Valor (R$)<input name="valor" inputmode="decimal" required value="${x.valor ? String(x.valor).replace('.', ',') : ''}" placeholder="0,00"></label>
    <label class="sub" style="margin:0;grid-column:1/-1">Descrição<input name="desc" required value="${esc(x.desc || '')}" placeholder="Ex.: Mensalidade gestão de redes"></label>
    <label class="sub" style="margin:0">Categoria<select name="cat">${op(CAT[x.tipo || 'receita'], x.cat)}</select></label>
    <label class="sub" style="margin:0">Cliente<select name="cli"><option value="">—</option>${CLI.map(c => `<option value="${c[0]}"${c[0] === x.cli ? ' selected' : ''}>${esc(c[1])}</option>`).join('')}</select></label>
    <label class="sub" style="margin:0">Vencimento<input type="date" name="venc" required value="${x.venc || hojeISO()}"></label>
    <label class="sub" style="margin:0">Forma<select name="forma">${op(FORMAS, x.forma)}</select></label>
    <label class="sub" style="margin:0;display:flex;align-items:center;gap:8px"><input type="checkbox" name="rec"${x.rec ? ' checked' : ''} style="width:auto"> Repete todo mês (mensalidade, assinatura)</label>
    <label class="sub" style="margin:0">Termina em (opcional)<input type="month" name="fim" value="${x.fim || ''}"></label>
    ${editando === 'novo' ? `<label class="sub" style="margin:0;display:flex;align-items:center;gap:8px;grid-column:1/-1"><input type="checkbox" name="jaPago" style="width:auto"> Já foi pago/recebido</label>` : ''}
    <div style="grid-column:1/-1;display:flex;gap:10px;flex-wrap:wrap"><button class="btn am">Salvar</button><button type="button" class="btn" id="f-cancela">Cancelar</button>
     ${editando !== 'novo' ? '<button type="button" class="btn" id="f-apaga" style="margin-left:auto;color:var(--erro)">Apagar</button>' : ''}</div></form></div>`;
}
const cab = () => `<div class="card" style="display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:space-between">
  <div style="display:flex;gap:8px;flex-wrap:wrap">${ABAS.map(([k, n]) => chip(aba === k, `data-faba="${k}"`, n)).join('')}</div>
  <div style="display:flex;gap:8px;align-items:center"><button class="btn" data-fmes="-1" style="padding:7px 12px">‹</button><b style="min-width:76px;text-align:center;text-transform:capitalize">${nomeMes(mes)}</b><button class="btn" data-fmes="1" style="padding:7px 12px">›</button>
   <button class="btn am" data-fnovo="" style="padding:7px 14px;font-size:13px">+ Lançar</button></div></div>${editando ? form() : ''}`;
const TELAS = {
  geral() {
    const r = resumo(mes), ant = resumo(addMes(mes, -1)), saldo = saldoAte(mes), margem = r.rec ? Math.round(r.lucro / r.rec * 100) : 0;
    const var_ = (a, b) => b ? ((a - b) / Math.abs(b) * 100).toFixed(0) + '% vs mês anterior' : '';
    const meta = +cfg.meta || 0, pctMeta = meta ? Math.min(100, Math.round(r.rec / meta * 100)) : 0, fol = r.fixo ? (saldo / r.fixo).toFixed(1) : '—';
    const prox = [0, 1].flatMap(k => ocorr(addMes(mes, k))).filter(o => !o.pagoEm).slice(0, 8);
    return `<div class="grade g4">${kpi('Saldo em caixa', R0(saldo), 'saldo inicial + tudo que foi pago', saldo < 0 ? 'var(--erro)' : '')}${kpi('Recebido no mês', R0(r.rec), var_(r.rec, ant.rec), 'var(--ok)')}${kpi('Pago no mês', R0(r.desp), var_(r.desp, ant.desp), 'var(--erro)')}${kpi('Lucro do mês', R0(r.lucro), 'margem ' + margem + '%', r.lucro < 0 ? 'var(--erro)' : 'var(--amarelo)')}</div>
     <div class="grade g4">${kpi('A receber no mês', R0(r.aRec), r.atrasoR ? R0(r.atrasoR) + ' atrasado' : 'nada atrasado')}${kpi('A pagar no mês', R0(r.aPag), r.atrasoD ? R0(r.atrasoD) + ' atrasado' : 'nada atrasado')}${kpi('MRR (receita recorrente)', R0(r.mrr), 'mensalidades ativas')}${kpi('Fôlego de caixa', fol + (r.fixo ? ' meses' : ''), 'saldo ÷ custo fixo mensal')}</div>
     <div class="grade g21"><div class="card"><h3>Últimos 12 meses</h3>${grafico([...Array(12)].map((_, i) => addMes(mes, i - 11)))}</div>
      <div class="card"><h3>Meta de faturamento</h3>${meta ? `<div style="font:800 30px var(--f-titulo)">${pctMeta}%</div><div style="height:10px;background:var(--painel2);border-radius:9px;margin:10px 0"><div style="height:100%;width:${pctMeta}%;background:var(--amarelo);border-radius:9px"></div></div><p class="sub" style="margin:0">${R0(r.rec)} de ${R0(meta)} · faltam ${R0(Math.max(0, meta - r.rec))}</p>` : '<p class="sub">Defina a meta em Configurações.</p>'}
       <h3 style="margin-top:18px">Previsto no mês</h3><p class="sub" style="margin:0">Receitas ${R0(r.recP)} · Despesas ${R0(r.despP)}<br>Resultado previsto <b style="color:${r.lucroP < 0 ? 'var(--erro)' : 'var(--ok)'}">${R0(r.lucroP)}</b></p>
       <h3 style="margin-top:18px">Imposto estimado</h3><p class="sub" style="margin:0">${cfg.imposto}% sobre o recebido: <b>${R$(r.rec * cfg.imposto / 100)}</b></p></div></div>
     <div class="grade g2"><div class="card"><h3>Receitas por categoria</h3>${barrasCat(r.R, 'var(--ok)')}</div><div class="card"><h3>Despesas por categoria</h3>${barrasCat(r.D, 'var(--erro)')}</div></div>
     <div class="card"><h3>Próximos vencimentos</h3>${tabela(prox)}</div>`;
  },
  lanc() {
    const o = ocorr(mes).filter(i => (!ftipo || i.x.tipo === ftipo) && (!busca || (i.x.desc + ' ' + (i.x.cat || '') + ' ' + (i.x.cli || '')).toLowerCase().includes(busca.toLowerCase())));
    return `<div class="card"><div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px">${chip(!ftipo, 'data-ftipo=""', 'Tudo')}${chip(ftipo === 'receita', 'data-ftipo="receita"', 'Receitas')}${chip(ftipo === 'despesa', 'data-ftipo="despesa"', 'Despesas')}
      <input id="f-busca" placeholder="Buscar…" value="${esc(busca)}" style="flex:1;min-width:160px"><button class="btn" id="f-csv" style="padding:7px 14px;font-size:13px">Exportar CSV</button></div>${tabela(o)}</div>`;
  },
  receber() { const o = [...Array(12)].flatMap((_, i) => ocorr(addMes(mes, i - 11))).filter(i => i.x.tipo === 'receita' && !i.pagoEm && i.m <= mes);
    const prox = ocorr(addMes(mes, 1)).filter(i => i.x.tipo === 'receita');
    return `<div class="grade g3">${kpi('Em aberto até ' + nomeMes(mes), R0(soma(o, () => 1)), o.length + ' cobrança(s)')}${kpi('Atrasado', R0(soma(o, i => i.atrasado)), 'cobre hoje', 'var(--erro)')}${kpi('Previsto mês que vem', R0(soma(prox, () => 1)), prox.length + ' lançamento(s)', 'var(--ok)')}</div><div class="card"><h3>Contas a receber</h3>${tabela(o)}</div>`; },
  pagar() { const o = [...Array(12)].flatMap((_, i) => ocorr(addMes(mes, i - 11))).filter(i => i.x.tipo === 'despesa' && !i.pagoEm && i.m <= mes);
    const prox = ocorr(addMes(mes, 1)).filter(i => i.x.tipo === 'despesa');
    return `<div class="grade g3">${kpi('Em aberto até ' + nomeMes(mes), R0(soma(o, () => 1)), o.length + ' conta(s)')}${kpi('Atrasado', R0(soma(o, i => i.atrasado)), 'pague primeiro', 'var(--erro)')}${kpi('Previsto mês que vem', R0(soma(prox, () => 1)), prox.length + ' lançamento(s)')}</div><div class="card"><h3>Contas a pagar</h3>${tabela(o)}</div>`; },
  fluxo() { const ms = [...Array(12)].map((_, i) => addMes(mes, i - 5));
    return `<div class="card"><h3>Fluxo de caixa · 6 meses atrás e 6 à frente</h3><p class="sub">Meses futuros usam o previsto (recorrentes e lançamentos com vencimento).</p>
     <div class="tab"><table><thead><tr><th>Mês</th><th style="text-align:right">Entradas</th><th style="text-align:right">Saídas</th><th style="text-align:right">Resultado</th><th style="text-align:right">Saldo</th></tr></thead><tbody>${(() => { let s = saldoAte(addMes(ms[0], -1));
       return ms.map(k => { const r = resumo(k), fut = k > mesDe(hojeISO()), e = fut ? r.recP : r.rec, sa = fut ? r.despP : r.desp; s += e - sa;
         return `<tr${k === mes ? ' style="background:var(--painel2)"' : ''}><td style="text-transform:capitalize">${nomeMes(k)}${fut ? ' <span style="font-size:11px;color:var(--apagado)">previsto</span>' : ''}</td><td style="text-align:right;color:var(--ok)">${R$(e)}</td><td style="text-align:right;color:var(--erro)">${R$(sa)}</td><td style="text-align:right;font-weight:800">${R$(e - sa)}</td><td style="text-align:right;font-weight:800;color:${s < 0 ? 'var(--erro)' : 'var(--texto)'}">${R$(s)}</td></tr>`; }).join(''); })()}</tbody></table></div></div>`; },
  dre() { const r = resumo(mes), imp = r.rec * cfg.imposto / 100, cat = c => soma(r.D, i => i.pagoEm && i.x.cat === c);
    const taxas = cat('Taxas (cartão, Hubla, banco)'), impPago = cat('Impostos'), cv = cat('Equipe / freelancer') + cat('Anúncios (verba própria)'), pro = cat('Pró-labore');
    const desp = r.desp - taxas - impPago - cv - pro, liq = r.rec - Math.max(imp, impPago) - taxas, bruto = liq - cv, op = bruto - desp, fin = op - pro;
    const l = (t, v, f) => `<tr${f ? ' style="font-weight:800;background:var(--painel2)"' : ''}><td>${t}</td><td style="text-align:right;color:${v < 0 ? 'var(--erro)' : 'inherit'}">${R$(v)}</td><td style="text-align:right;color:var(--apagado)">${r.rec ? Math.round(v / r.rec * 100) + '%' : '—'}</td></tr>`;
    return `<div class="card"><h3>DRE · ${nomeMes(mes)} (regime de caixa)</h3><div class="tab"><table><tbody>
     ${l('Receita bruta (recebida)', r.rec, 1)}${l('(−) Impostos (lançados ou estimados a ' + cfg.imposto + '%)', -Math.max(imp, impPago))}${l('(−) Taxas de cartão, Hubla e banco', -taxas)}${l('= Receita líquida', liq, 1)}
     ${l('(−) Custo direto (equipe/freelancer e anúncios)', -cv)}${l('= Lucro bruto', bruto, 1)}${l('(−) Despesas operacionais', -desp)}${l('= Resultado operacional', op, 1)}${l('(−) Pró-labore', -pro)}${l('= Lucro líquido', fin, 1)}
    </tbody></table></div><p class="sub" style="margin-top:10px">Separe "Impostos", "Taxas", "Equipe / freelancer", "Anúncios" e "Pró-labore" nas categorias certas para a DRE ficar exata.</p></div>`; },
  clientes() {
    const por = {}; [...Array(12)].forEach((_, i) => ocorr(addMes(mes, i - 11)).filter(o => o.x.tipo === 'receita').forEach(o => {
      const k = o.x.cli || '—'; const p = por[k] = por[k] || { tot: 0, ab: 0, mrr: 0, at: 0 }; if (o.pagoEm) p.tot += o.valor; else { p.ab += o.valor; if (o.atrasado) p.at += o.valor; } if (o.x.rec && o.m === mes) p.mrr += o.valor; }));
    const e = Object.entries(por).sort((a, b) => b[1].tot - a[1].tot), tot = e.reduce((s, x) => s + x[1].tot, 0) || 1, mrr = e.reduce((s, x) => s + x[1].mrr, 0);
    return `<div class="grade g3">${kpi('MRR do mês', R0(mrr), 'mensalidades ativas')}${kpi('ARR (MRR × 12)', R0(mrr * 12), 'receita anual recorrente')}${kpi('Ticket médio por cliente', R0(e.length ? tot / e.length : 0), 'recebido em 12 meses')}</div>
     <div class="card"><h3>Receita por cliente · 12 meses</h3><div class="tab"><table><thead><tr><th>Cliente</th><th style="text-align:right">Recebido</th><th style="text-align:right">% do total</th><th style="text-align:right">MRR</th><th style="text-align:right">Em aberto</th></tr></thead><tbody>
      ${e.map(([k, p]) => `<tr><td><b>${esc((CLI.find(c => c[0] === k) || [0, k === '—' ? 'Sem cliente' : k])[1])}</b></td><td style="text-align:right">${R$(p.tot)}</td><td style="text-align:right">${Math.round(p.tot / tot * 100)}%</td><td style="text-align:right">${R$(p.mrr)}</td><td style="text-align:right;color:${p.at ? 'var(--erro)' : 'inherit'}">${R$(p.ab)}${p.at ? ' (atrasado)' : ''}</td></tr>`).join('') || '<tr><td colspan="5">Nenhuma receita lançada.</td></tr>'}
     </tbody></table></div><p class="sub" style="margin-top:10px">Concentração: se um cliente passa de 30% do total, a agência depende demais dele.</p></div>`;
  },
  cfg() { return `<div class="card"><h3>Configurações do financeiro</h3><form id="f-cfg" class="grade g2" style="gap:12px">
    <label class="sub" style="margin:0">Saldo inicial em caixa (R$)<input name="saldo" inputmode="decimal" value="${String(cfg.saldo || 0).replace('.', ',')}"></label>
    <label class="sub" style="margin:0">Meta de faturamento mensal (R$)<input name="meta" inputmode="decimal" value="${String(cfg.meta || 0).replace('.', ',')}"></label>
    <label class="sub" style="margin:0">Imposto estimado (% do recebido)<input name="imposto" inputmode="decimal" value="${String(cfg.imposto).replace('.', ',')}"></label>
    <label class="sub" style="margin:0">Reserva de emergência desejada (R$)<input name="reserva" inputmode="decimal" value="${String(cfg.reserva || 0).replace('.', ',')}"></label>
    <div style="grid-column:1/-1"><button class="btn am">Salvar</button></div></form>
    ${+cfg.reserva ? `<p class="sub" style="margin-top:14px">Reserva: ${R0(Math.max(0, saldoAte(mesDe(hojeISO()))))} de ${R0(cfg.reserva)} (${Math.min(100, Math.round(Math.max(0, saldoAte(mesDe(hojeISO()))) / cfg.reserva * 100))}%).</p>` : ''}
    <p class="sub" style="margin-top:14px">Simples Nacional, anexo III (serviços), começa em 6%. MEI paga valor fixo mensal: lance o DAS como despesa "Impostos" e coloque 0% aqui.</p></div>`; },
};
T.financeiro = 'Financeiro';
V.financeiro = () => { if (!carregou) { carrega(); return '<div class="card"><p class="sub" style="margin:0">Carregando o financeiro…</p></div>'; } return cab() + TELAS[aba](); };
const num = v => parseFloat(String(v || '0').replace(/\./g, '').replace(',', '.')) || 0;
const ant = window.__pos;
window.__pos = view => {
  if (ant) ant(view); if (view !== 'financeiro') return;
  const $$ = s => document.querySelectorAll('#conteudo ' + s), $1 = s => document.querySelector('#conteudo ' + s);
  $$('[data-faba]').forEach(b => b.onclick = () => { aba = b.dataset.faba; render(); });
  $$('[data-fmes]').forEach(b => b.onclick = () => { mes = addMes(mes, +b.dataset.fmes); render(); });
  $$('[data-fnovo]').forEach(b => b.onclick = () => { editando = 'novo'; render(); });
  $$('[data-fedit]').forEach(b => b.onclick = () => { editando = b.dataset.fedit; render(); scrollTo(0, 0); });
  $$('[data-ftipo]').forEach(b => b.onclick = () => { ftipo = b.dataset.ftipo; render(); });
  $$('[data-fpaga]').forEach(b => b.onclick = () => { const [id, m] = b.dataset.fpaga.split('|'), x = L[id]; x.pago = x.pago || {};
    if (x.pago[m]) delete x.pago[m]; else x.pago[m] = hojeISO(); render(); grava([{ op: 'set', col: 'financeiro', id, data: x }], x.pago[m] ? 'Marcado como pago' : 'Voltou para pendente'); });
  const bu = $1('#f-busca'); if (bu) bu.oninput = () => { busca = bu.value; clearTimeout(bu._t); bu._t = setTimeout(() => { render(); const n = $1('#f-busca'); if (n) { n.focus(); n.setSelectionRange(busca.length, busca.length); } }, 300); };
  const ft = $1('#f-tipo'); if (ft) ft.onchange = () => { const sel = $1('#f-fin [name=cat]'); sel.innerHTML = CAT[ft.value].map(c => `<option>${esc(c)}</option>`).join(''); };
  const fc = $1('#f-cancela'); if (fc) fc.onclick = () => { editando = null; render(); };
  const fa = $1('#f-apaga'); if (fa) fa.onclick = () => { if (!confirm('Apagar este lançamento (todos os meses)?')) return; const id = editando; delete L[id]; editando = null; render(); grava([{ op: 'delete', col: 'financeiro', id }], 'Lançamento apagado'); };
  const f = $1('#f-fin'); if (f) f.onsubmit = e => { e.preventDefault(); const d = Object.fromEntries(new FormData(f)), novo = editando === 'novo';
    const id = novo ? Date.now().toString(36) + Math.random().toString(36).slice(2, 6) : editando, velho = L[id] || {};
    const x = { tipo: d.tipo, desc: d.desc.trim(), valor: num(d.valor), cat: d.cat, cli: d.cli, forma: d.forma, venc: d.venc, rec: !!d.rec, fim: d.fim || '', pago: velho.pago || {}, criado: velho.criado || new Date().toISOString() };
    if (!x.valor) { toast('Coloque o valor.'); return; } if (novo && d.jaPago) x.pago[mesDe(x.venc)] = x.venc;
    L[id] = x; editando = null; render(); grava([{ op: 'set', col: 'financeiro', id, data: x }], 'Lançamento salvo'); };
  const fg = $1('#f-cfg'); if (fg) fg.onsubmit = e => { e.preventDefault(); const d = Object.fromEntries(new FormData(fg));
    cfg = { saldo: num(d.saldo), meta: num(d.meta), imposto: num(d.imposto), reserva: num(d.reserva) }; render(); grava([{ op: 'set', col: 'financeiro-config', id: 'cfg', data: cfg }], 'Configurações salvas'); };
  const cs = $1('#f-csv'); if (cs) cs.onclick = () => { const linhas = [['vencimento', 'tipo', 'descricao', 'categoria', 'cliente', 'forma', 'valor', 'pago_em', 'mensal']].concat(ocorr(mes).map(o => [o.venc, o.x.tipo, o.x.desc, o.x.cat, o.x.cli, o.x.forma, String(o.valor).replace('.', ','), o.pagoEm, o.x.rec ? 'sim' : 'não']));
    const blob = new Blob(['﻿' + linhas.map(l => l.map(c => '"' + String(c ?? '').replace(/"/g, '""') + '"').join(';')).join('\n')], { type: 'text/csv' });
    const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'financeiro-' + mes + '.csv'; a.click(); };
};
})();
