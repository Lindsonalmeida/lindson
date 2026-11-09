// /api/automacao: acesso das automações da agência (postagem programada) às aprovações dos clientes, sem login de pessoa.
// Pedido do Lindson (08/11/2026, conta Leandro): "me diga o que precisa pra ter acesso" à aba Aprovados para postar sozinho.
// Proteção: cabeçalho "Authorization: Bearer <AUTOMACAO_TOKEN>". O token é um SEGREDO criado pelo Lindson na Cloudflare
// (Configurações do projeto Pages → Variáveis e segredos → AUTOMACAO_TOKEN). Sem o segredo configurado, a rota fica fechada.
// GET  /api/automacao?cli=rt                 → { itens: [...] } da aba de aprovações (f=aprov), só leitura.
// POST /api/automacao?cli=rt  {titulo, link} → marca o post como postado (mesmo campo do botão "Marquei como postado").
// FILA DA CENTRAL DE COMANDO (conta Leandro, 09/11/2026; v2 no mesmo dia): as 4 contas do Claude leem e marcam os pedidos do Lindson.
// GET  /api/automacao?fila=ped                                                → { itens, versao }
// POST /api/automacao?fila=ped {id, acao:'pegar', conta}                      → só se "novo" (ou "ajuste" da mesma conta); senão 409: uma conta por pedido
// POST /api/automacao?fila=ped {id, acao:'pronto', conta, link?, midia?[], resumo?} → só a conta que pegou; até 10 links https de mídia (imagem, vídeo, PDF, site)
// POST /api/automacao?fila=ped {id, acao:'pergunta', conta, texto, opcoes?[]} → pergunta ao Lindson (aparece "Esperando você"; até 6 respostas rápidas)
// POST /api/automacao?fila=ped {id, acao:'nota', conta, texto}                → recado da conta no pedido
// POST /api/automacao?fila=ped {id, acao:'dividir', conta, partes:[{texto, func?}]} → a conta que pegou cria até 6 subpedidos (cada um designado pelo distribuidor)
// POST /api/automacao?fila=ped {acao:'criar', conta, cli, func, texto, id?, pegar?, forcar?} → pedido novo feito na conversa de uma conta (v4, conta Zuleide, 09/11/2026).
//      cli e func iguais aos da página; texto 1–500. Pedido igual aberto nos últimos 14 dias → 409 com o existente (forcar:true manda mesmo assim).
//      pegar:true = a própria conta já está fazendo (st andamento, designada = ela); sem pegar, o distribuidor escolhe a conta.
// Distribuição: cada pedido tem `designada` (só ela pega) e `motivo`. Em toda leitura da fila o servidor redistribui (functions/_distribuir.js).
// Grava em dados:admin:ped (a mesma chave que /painel/comando usa por /api/dados), com a versão +1. A resposta do Lindson fica em item.conversa.
// QUADRO DA EQUIPE: GET /api/automacao?fila=equipe → { contas, hist, versao }
// POST /api/automacao?fila=equipe {conta, estado:'trabalhando'|'livre'|'limite-sessao'|'limite-semana', ate?, tarefa?} → grava em dados:admin:eq (ate obrigatório nos limites)
import { json, iguais } from '../_lib.js';
import { distribuir, redistribuir, NOMES_CLI, NOMES_FN } from '../_distribuir.js';
const FILA = 'dados:admin:ped', EQUIPE = 'dados:admin:eq', CONTAS = ['Lindson', 'Zuleide', 'Pedro', 'Leandro'], ACOES = ['pegar', 'pronto', 'pergunta', 'nota', 'dividir', 'criar'];
const ABERTOS = ['novo', 'espera', 'andamento', 'pronto', 'ajuste'];
const ESTADOS = ['trabalhando', 'livre', 'limite-sessao', 'limite-semana'];
const qual = request => new URL(request.url).searchParams.get('fila');
const httpsOk = u => typeof u === 'string' && u.length <= 500 && /^https:\/\/[^\s<>"']+$/.test(u);
const txtOk = (t, n) => typeof t === 'string' && t.trim().length > 0 && t.length <= n;
async function ler(env, k, vazio) { return (await env.CONTAS.get(k, 'json')) || { dados: vazio, versao: 0 }; }
async function corpo(request) {
  const txt = await request.text(); if (txt.length > 8000) return { erro: json({ erro: 'Dados grandes demais.' }, 413) };
  try { const b = JSON.parse(txt); return b && typeof b === 'object' ? { b } : { erro: json({ erro: 'Dados inválidos.' }, 400) }; } catch (e) { return { erro: json({ erro: 'Dados inválidos.' }, 400) }; }
}
async function filaGet(env) {
  const r = await ler(env, FILA, { itens: [] }), itens = (r.dados && r.dados.itens) || [];
  const eq = (await ler(env, EQUIPE, { contas: {} })).dados || {};
  let versao = r.versao || 0;
  if (redistribuir(itens, eq, Date.now())) { // redesigna sem cron: designada sem tempo, sem tarefa ativa, ou 2 h sem pegar
    versao += 1; await env.CONTAS.put(FILA, JSON.stringify({ dados: Object.assign({}, r.dados, { itens }), versao, por: 'automacao:distribuidor', em: new Date().toISOString() }));
  }
  return json({ itens, versao });
}
async function filaPost(request, env) {
  const { b, erro } = await corpo(request); if (erro) return erro;
  if (b.acao === 'criar') return filaCriar(b, env);
  if (typeof b.id !== 'string' || !/^[a-z0-9-]{4,40}$/i.test(b.id)) return json({ erro: 'id inválido.' }, 400);
  if (!ACOES.includes(b.acao)) return json({ erro: 'acao deve ser pegar, pronto, pergunta, nota, dividir ou criar.' }, 400);
  if (!CONTAS.includes(b.conta)) return json({ erro: 'conta deve ser Lindson, Zuleide, Pedro ou Leandro.' }, 400);
  let midia = [];
  if (b.acao === 'pronto') {
    if (b.link !== undefined && b.link !== '' && !httpsOk(b.link)) return json({ erro: 'link deve ser https (até 500 caracteres).' }, 400);
    if (b.midia !== undefined && (!Array.isArray(b.midia) || b.midia.length > 10 || !b.midia.every(httpsOk))) return json({ erro: 'midia: lista de até 10 links https.' }, 400);
    midia = b.midia || [];
    if (!b.link && !midia.length) return json({ erro: 'Mande o link ou a mídia do resultado.' }, 400);
    if (b.resumo !== undefined && (typeof b.resumo !== 'string' || b.resumo.length > 300)) return json({ erro: 'resumo até 300 caracteres.' }, 400);
  }
  if (b.acao === 'dividir' && (!Array.isArray(b.partes) || !b.partes.length || b.partes.length > 6 || !b.partes.every(p => p && txtOk(p.texto, 300) && (p.func === undefined || /^[a-z]{2,20}$/.test(p.func))))) return json({ erro: 'partes: de 1 a 6 itens {texto (até 300), func?}.' }, 400);
  if ((b.acao === 'nota' || b.acao === 'pergunta') && !txtOk(b.texto, 500)) return json({ erro: 'texto obrigatório (até 500 caracteres).' }, 400);
  if (b.acao === 'pergunta' && b.opcoes !== undefined && (!Array.isArray(b.opcoes) || b.opcoes.length > 6 || !b.opcoes.every(o => txtOk(o, 40)))) return json({ erro: 'opcoes: até 6 respostas de até 40 caracteres.' }, 400);
  const atual = await ler(env, FILA, { itens: [] });
  if (b.versao !== undefined && (b.versao | 0) !== (atual.versao || 0)) return json({ erro: 'A fila mudou. Leia de novo.', versao: atual.versao || 0 }, 409);
  const itens = (atual.dados && Array.isArray(atual.dados.itens)) ? atual.dados.itens : [], x = itens.find(i => i.id === b.id);
  if (!x) return json({ erro: 'Pedido não encontrado.' }, 404);
  const agora = new Date().toISOString(), conv = m => { x.conversa = (Array.isArray(x.conversa) ? x.conversa : []).concat([m]).slice(-30); };
  if (b.acao === 'pegar') {
    if (x.st !== 'novo' && x.st !== 'ajuste') return json({ erro: `Pedido já está "${x.st}"${x.conta ? ' com ' + x.conta : ''}.`, st: x.st, conta: x.conta || '' }, 409);
    if (x.designada && x.designada !== b.conta) return json({ erro: `Pedido designado para ${x.designada}.`, st: x.st, designada: x.designada }, 409);
    if (!x.designada && x.st === 'ajuste' && x.conta && x.conta !== b.conta) return json({ erro: `Ajuste é de ${x.conta}, que fez o pedido.`, st: x.st, conta: x.conta }, 409);
    x.st = 'andamento'; x.conta = b.conta; x.pegoEm = agora;
  } else if (b.acao === 'dividir') {
    if (x.st !== 'andamento' || x.conta !== b.conta) return json({ erro: 'Só a conta que pegou o pedido pode dividir.', st: x.st, conta: x.conta || '' }, 409);
    const eq = (await ler(env, EQUIPE, { contas: {} })).dados || {};
    x.partes = (x.partes || []).slice();
    b.partes.forEach((p, n) => {
      const sub = { id: (x.id + '-' + (x.partes.length + 1)).slice(0, 40), mae: x.id, cli: x.cli, func: p.func || x.func, texto: p.texto.trim(), st: 'novo', conta: '', link: '', criado: agora, atualizado: agora, nota: '', ajustes: 0 };
      const d = distribuir(sub, itens, eq, Date.now()); sub.designada = d.designada; sub.motivo = d.motivo; sub.volta = d.volta || null; sub.designadaEm = agora; if (!d.designada) sub.st = 'espera';
      itens.push(sub); x.partes.push(sub.id);
    });
  } else if (b.acao === 'pronto' || b.acao === 'pergunta') {
    if (x.st !== 'andamento' || x.conta !== b.conta) return json({ erro: 'Só a conta que pegou o pedido pode fazer isso.', st: x.st, conta: x.conta || '' }, 409);
    if (b.acao === 'pronto') { x.st = 'pronto'; x.link = b.link || ''; x.midia = midia; x.resumo = (b.resumo || '').trim(); x.prontoEm = agora; x.esperando = false; }
    else { conv({ de: b.conta, tipo: 'pergunta', texto: b.texto.trim(), opcoes: (b.opcoes || []).map(o => o.trim()), em: agora }); x.esperando = true; }
  } else {
    conv({ de: b.conta, tipo: 'nota', texto: b.texto.trim(), em: agora });
  }
  x.atualizado = agora;
  const novo = { dados: Object.assign({}, atual.dados, { itens }), versao: (atual.versao || 0) + 1, por: 'automacao:' + b.conta, em: agora };
  await env.CONTAS.put(FILA, JSON.stringify(novo));
  return json({ ok: true, versao: novo.versao, item: x });
}
async function filaCriar(b, env) {
  // mesmas regras da página (/painel/comando, função envia): cliente e função da lista, texto curto, aviso de "já existe"
  if (!CONTAS.includes(b.conta)) return json({ erro: 'conta deve ser Lindson, Zuleide, Pedro ou Leandro.' }, 400);
  if (typeof b.cli !== 'string' || !Object.prototype.hasOwnProperty.call(NOMES_CLI, b.cli)) return json({ erro: 'cli deve ser ' + Object.keys(NOMES_CLI).join(', ') + '.' }, 400);
  if (typeof b.func !== 'string' || !Object.prototype.hasOwnProperty.call(NOMES_FN, b.func)) return json({ erro: 'func deve ser ' + Object.keys(NOMES_FN).join(', ') + '.' }, 400);
  if (!txtOk(b.texto, 500)) return json({ erro: 'texto obrigatório (até 500 caracteres).' }, 400);
  if (b.id !== undefined && (typeof b.id !== 'string' || !/^[a-z0-9-]{4,40}$/i.test(b.id))) return json({ erro: 'id inválido.' }, 400);
  if (b.pegar !== undefined && typeof b.pegar !== 'boolean') return json({ erro: 'pegar deve ser true ou false.' }, 400);
  if (b.forcar !== undefined && typeof b.forcar !== 'boolean') return json({ erro: 'forcar deve ser true ou false.' }, 400);
  for (let i = 0; i < 3; i++) {
    const atual = await ler(env, FILA, { itens: [] }), itens = (atual.dados && Array.isArray(atual.dados.itens)) ? atual.dados.itens.slice() : [];
    const id = b.id || ('p' + Date.now().toString(36) + Math.random().toString(36).slice(2, 5));
    if (itens.some(x => x.id === id)) return json({ erro: 'Já existe um pedido com esse id.', item: itens.find(x => x.id === id) }, 409);
    const lim = Date.now() - 14 * 864e5;
    const igual = itens.filter(x => x.cli === b.cli && x.func === b.func && ABERTOS.includes(x.st) && !x.mae && Date.parse(x.criado || 0) >= lim).sort((x, y) => (y.criado || '').localeCompare(x.criado || ''))[0];
    if (igual && !b.forcar) return json({ erro: 'Já existe um pedido igual aberto. Use forcar:true se for outro.', item: igual }, 409);
    const agora = new Date().toISOString();
    const x = { id, cli: b.cli, func: b.func, texto: b.texto.trim(), st: 'novo', conta: '', link: '', criado: agora, atualizado: agora, nota: '', ajustes: 0, origem: 'conta:' + b.conta };
    if (b.pegar) Object.assign(x, { st: 'andamento', conta: b.conta, designada: b.conta, motivo: 'pedido feito na conversa com ' + b.conta, designadaEm: agora, pegoEm: agora });
    else {
      const eq = (await ler(env, EQUIPE, { contas: {} })).dados || {}, d = distribuir(x, itens, eq, Date.now());
      Object.assign(x, { designada: d.designada, motivo: d.motivo, volta: d.volta || null, designadaEm: agora, st: d.designada ? 'novo' : 'espera' });
    }
    itens.unshift(x);
    // grava só se ninguém mudou a fila no meio (KV não tem transação: confere a versão logo antes)
    const conf = await ler(env, FILA, { itens: [] });
    if ((conf.versao || 0) !== (atual.versao || 0)) continue;
    const novo = { dados: Object.assign({}, atual.dados, { itens }), versao: (atual.versao || 0) + 1, por: 'automacao:' + b.conta, em: agora };
    await env.CONTAS.put(FILA, JSON.stringify(novo));
    return json({ ok: true, versao: novo.versao, item: x }, 201);
  }
  return json({ erro: 'A fila mudou várias vezes seguidas. Tente de novo.' }, 409);
}
async function equipeGet(env) {
  const r = await ler(env, EQUIPE, { contas: {}, hist: [] }), d = r.dados || {};
  return json({ contas: d.contas || {}, hist: d.hist || [], versao: r.versao || 0 });
}
async function equipePost(request, env) {
  const { b, erro } = await corpo(request); if (erro) return erro;
  if (!CONTAS.includes(b.conta)) return json({ erro: 'conta deve ser Lindson, Zuleide, Pedro ou Leandro.' }, 400);
  if (!ESTADOS.includes(b.estado)) return json({ erro: 'estado deve ser trabalhando, livre, limite-sessao ou limite-semana.' }, 400);
  let ate = null;
  if (b.estado.startsWith('limite')) {
    const t = Date.parse(b.ate || '');
    if (!t || t < Date.now() - 6e4 || t > Date.now() + 8 * 864e5) return json({ erro: 'ate: data ISO do reset, nos próximos 8 dias.' }, 400);
    ate = new Date(t).toISOString();
  }
  if (b.tarefa !== undefined && (typeof b.tarefa !== 'string' || b.tarefa.length > 200)) return json({ erro: 'tarefa até 200 caracteres.' }, 400);
  const atual = await ler(env, EQUIPE, { contas: {}, hist: [] }), d = Object.assign({ contas: {}, hist: [] }, atual.dados || {}), agora = new Date().toISOString();
  const antes = d.contas[b.conta] || {};
  d.contas[b.conta] = { estado: b.estado, ate, tarefa: b.tarefa !== undefined ? b.tarefa.trim() : (antes.tarefa || ''), em: agora, batida: agora, por: 'conta' };
  if (antes.estado !== b.estado || (ate && antes.ate !== ate)) d.hist = (d.hist || []).concat([{ conta: b.conta, estado: b.estado, ate, em: agora, por: 'conta' }]).slice(-300);
  const novo = { dados: d, versao: (atual.versao || 0) + 1, por: 'automacao:' + b.conta, em: agora };
  await env.CONTAS.put(EQUIPE, JSON.stringify(novo));
  return json({ ok: true, versao: novo.versao, conta: d.contas[b.conta] });
}
const CLIS = /^[a-z0-9-]{2,30}$/;
function autorizado(request, env) {
  const t = env.AUTOMACAO_TOKEN || '', h = request.headers.get('Authorization') || '', v = h.replace(/^Bearer\s+/i, '');
  return t.length >= 24 && v.length > 0 && iguais(v, t);
}
function chave(request) { const cli = (new URL(request.url).searchParams.get('cli') || '').toLowerCase(); return CLIS.test(cli) ? `dados:${cli}:aprov` : null; }
export async function onRequestGet({ request, env }) {
  if (!env.CONTAS || !autorizado(request, env)) return json({ erro: 'Sem acesso.' }, 401);
  if (qual(request) === 'ped') return filaGet(env);
  if (qual(request) === 'equipe') return equipeGet(env);
  const k = chave(request); if (!k) return json({ erro: 'Cliente inválido.' }, 400);
  const r = (await env.CONTAS.get(k, 'json')) || { dados: { itens: [] }, versao: 0 };
  return json({ itens: (r.dados && r.dados.itens) || [], versao: r.versao || 0 });
}
export async function onRequestPost({ request, env }) {
  if (!env.CONTAS || !autorizado(request, env)) return json({ erro: 'Sem acesso.' }, 401);
  if (qual(request) === 'ped') return filaPost(request, env);
  if (qual(request) === 'equipe') return equipePost(request, env);
  const k = chave(request); if (!k) return json({ erro: 'Cliente inválido.' }, 400);
  let b; try { b = await request.json(); } catch (e) { return json({ erro: 'Dados inválidos.' }, 400); }
  if (!b || typeof b.titulo !== 'string' || b.titulo.length > 300) return json({ erro: 'Título inválido.' }, 400);
  const atual = (await env.CONTAS.get(k, 'json')) || { dados: { itens: [] }, versao: 0 };
  const itens = (atual.dados && atual.dados.itens) || [], x = itens.find(i => i.titulo === b.titulo);
  if (!x) return json({ erro: 'Post não encontrado nas aprovações.' }, 404);
  if (x.st !== 'aprovado') return json({ erro: 'Este post não está aprovado.' }, 409);
  const agora = new Date().toISOString();
  x.postado = true; x.postadoPor = 'Automação da agência'; x.postadoEm = agora; if (b.link && String(b.link).length < 500) x.link = String(b.link);
  const novo = { dados: Object.assign({}, atual.dados, { itens }), versao: (atual.versao || 0) + 1, por: 'automacao', em: agora };
  await env.CONTAS.put(k, JSON.stringify(novo));
  return json({ ok: true, versao: novo.versao });
}
