// /api/membros/admin: só o admin da agência (cookie "central", cli admin).
// GET → lista os membros (sem CPF nem senha). POST {acao, email, produto?, nome?, cpf?}:
//   acao "liberar"  → libera o produto (venda manual ou teste); cria o membro se não existir (nome e CPF opcionais, CPF vira hash)
//   acao "remover"  → tira o produto
//   acao "zerar-senha" → apaga a senha (esqueceu): a pessoa faz o Primeiro acesso de novo com e-mail e CPF; derruba as sessões
//   acao "apagar"   → apaga o membro (pedido de exclusão de dados, LGPD)
import { adminAgencia, SLUGS, slugOk, chave, ativos, alteraMembro, normEmail, emailOk, soDigitos, docOk, hashSenha, json } from '../../_membros.js';
export async function onRequestGet({ request, env }) {
  if (!env.CONTAS || !env.SEGREDO) return json({ erro: 'Não configurado.' }, 503);
  if (!await adminAgencia(request, env)) return json({ erro: 'Só o administrador.' }, 403);
  const out = []; let cursor;
  do {
    const r = await env.CONTAS.list({ prefix: 'membro:', cursor });
    for (const k of r.keys) { const m = await env.CONTAS.get(k.name, 'json'); if (m) out.push({ email: m.email, nome: m.nome || '', tel4: m.tel4 || '', produtos: ativos(m), historico: m.produtos || {}, temSenha: !!m.senha, temCpf: !!m.docHash, criado: m.criado || '' }); }
    cursor = r.list_complete ? null : r.cursor;
  } while (cursor);
  return json({ membros: out.sort((a, b) => (b.criado || '').localeCompare(a.criado || '')), produtos: SLUGS });
}
export async function onRequestPost({ request, env }) {
  if (!env.CONTAS || !env.SEGREDO) return json({ erro: 'Não configurado.' }, 503);
  if (!await adminAgencia(request, env)) return json({ erro: 'Só o administrador.' }, 403);
  const origem = request.headers.get('Origin');
  if (origem && origem !== new URL(request.url).origin) return json({ erro: 'Origem recusada.' }, 403);
  if (!/^application\/json/i.test(request.headers.get('Content-Type') || '')) return json({ erro: 'Envie JSON.' }, 415);
  let b = {}; try { b = await request.json(); } catch (e) { return json({ erro: 'Dados inválidos.' }, 400); }
  const acao = String(b.acao || ''), email = normEmail(b.email), slug = String(b.produto || '');
  if (!emailOk(email)) return json({ erro: 'E-mail inválido.' }, 400);
  if (!['liberar', 'remover', 'zerar-senha', 'apagar'].includes(acao)) return json({ erro: 'Ação inválida.' }, 400);
  if ((acao === 'liberar' || acao === 'remover') && !slugOk(slug)) return json({ erro: 'Produto inválido.' }, 400);
  if (acao === 'apagar') { await env.CONTAS.delete(chave(email)); return json({ ok: true }); }
  const agora = new Date().toISOString(), nome = String(b.nome || '').trim().slice(0, 80), doc = soDigitos(b.cpf);
  if (b.cpf && !docOk(doc)) return json({ erro: 'CPF inválido (11 números) ou CNPJ (14).' }, 400);
  const docHash = docOk(doc) ? await hashSenha(doc) : null;
  const r = await alteraMembro(env, email, rec => {
    if (acao === 'zerar-senha') { if (!rec || !rec.senha) return null; delete rec.senha; rec.sv = (rec.sv | 0) + 1; return rec; }
    if (acao === 'remover') { if (!rec || !rec.produtos || !rec.produtos[slug] || rec.produtos[slug].ativo === false) return null; rec.produtos[slug] = { ...rec.produtos[slug], ativo: false, ate: agora, at: agora, origem: 'manual' }; return rec; }
    rec = rec || { email, criado: agora, produtos: {}, sv: 0 };
    rec.produtos = rec.produtos || {};
    if (nome) rec.nome = nome;
    if (docHash && !rec.senha) rec.docHash = docHash;
    const p = rec.produtos[slug] || {};
    if (p.ativo && !docHash && !nome) return null;
    const n = { ...p, ativo: true, desde: p.desde || agora, at: p.ativo ? p.at : agora, origem: p.ativo ? p.origem : 'manual' }; delete n.ate;
    rec.produtos[slug] = n;
    return rec;
  });
  if (!r.ok) return json({ erro: 'Não confirmou a gravação. Tente de novo.' }, 503);
  const m = await env.CONTAS.get(chave(email), 'json');
  return json({ ok: true, membro: m ? { email: m.email, nome: m.nome || '', produtos: ativos(m), temSenha: !!m.senha, temCpf: !!m.docHash } : null });
}
