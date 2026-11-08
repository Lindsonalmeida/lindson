// /api/automacao: acesso das automações da agência (postagem programada) às aprovações dos clientes, sem login de pessoa.
// Pedido do Lindson (08/11/2026, conta Leandro): "me diga o que precisa pra ter acesso" à aba Aprovados para postar sozinho.
// Proteção: cabeçalho "Authorization: Bearer <AUTOMACAO_TOKEN>". O token é um SEGREDO criado pelo Lindson na Cloudflare
// (Configurações do projeto Pages → Variáveis e segredos → AUTOMACAO_TOKEN). Sem o segredo configurado, a rota fica fechada.
// GET  /api/automacao?cli=rt                 → { itens: [...] } da aba de aprovações (f=aprov), só leitura.
// POST /api/automacao?cli=rt  {titulo, link} → marca o post como postado (mesmo campo do botão "Marquei como postado").
import { json, iguais } from '../_lib.js';
const CLIS = /^[a-z0-9-]{2,30}$/;
function autorizado(request, env) {
  const t = env.AUTOMACAO_TOKEN || '', h = request.headers.get('Authorization') || '', v = h.replace(/^Bearer\s+/i, '');
  return t.length >= 24 && v.length > 0 && iguais(v, t);
}
function chave(request) { const cli = (new URL(request.url).searchParams.get('cli') || '').toLowerCase(); return CLIS.test(cli) ? `dados:${cli}:aprov` : null; }
export async function onRequestGet({ request, env }) {
  if (!env.CONTAS || !autorizado(request, env)) return json({ erro: 'Sem acesso.' }, 401);
  const k = chave(request); if (!k) return json({ erro: 'Cliente inválido.' }, 400);
  const r = (await env.CONTAS.get(k, 'json')) || { dados: { itens: [] }, versao: 0 };
  return json({ itens: (r.dados && r.dados.itens) || [], versao: r.versao || 0 });
}
export async function onRequestPost({ request, env }) {
  if (!env.CONTAS || !autorizado(request, env)) return json({ erro: 'Sem acesso.' }, 401);
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
