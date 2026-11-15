// /api/feitas: Tarefas feitas no painel de cada cliente (pedido do Lindson, 15/11/2026, conta Zuleide).
// GET → { cli, itens } só as linhas do cliente logado (o cli vem do login, nunca da URL); o admin vê todas ou ?cli=<cliente>.
// DELETE ?id=<id> → só o admin: tira a linha e guarda o id em "apagadas".
import { json, quemE, configurado, faltaConfig } from '../_lib.js';
const K = 'dados:admin:feitas';
const limpa = x => ({ id: x.id, data: x.data || '', hora: x.hora || '', cli: x.cli, atividade: x.atividade, por: x.por || '' });
// linha sem hora que repete outra do mesmo dia e cliente (lançada de novo depois) não aparece
function semDup(itens) {
  const pal = s => new Set(String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').split(/[^a-z0-9]+/).filter(w => w.length > 3));
  return itens.filter(x => x.hora || !itens.some(y => y !== x && y.hora && y.cli === x.cli && y.data === x.data && (() => { const a = pal(x.atividade), b = pal(y.atividade); let c = 0; b.forEach(w => a.has(w) && c++); return c >= Math.min(3, b.size); })()));
}
export async function onRequestGet({ request, env }) {
  if (!configurado(env)) return faltaConfig();
  const q = await quemE(request, env); if (!q) return json({ erro: 'Entre na Central de novo.' }, 401);
  const r = (await env.CONTAS.get(K, 'json')) || {}, todos = semDup(((r.dados && r.dados.itens) || []).filter(x => x && x.cli && x.atividade));
  let cli = q.cli;
  if (q.cli === 'admin') { cli = (new URL(request.url).searchParams.get('cli') || '').toLowerCase(); if (cli && !/^[a-z0-9-]{2,30}$/.test(cli)) return json({ erro: 'Pedido inválido.' }, 400); }
  const itens = (cli ? todos.filter(x => x.cli === cli) : todos).map(limpa).sort((a, b) => (b.data + b.hora).localeCompare(a.data + a.hora));
  return json({ cli: cli || 'todos', eu: q.cli === 'admin' ? 'admin' : 'cliente', itens }, 200);
}
export async function onRequestDelete({ request, env }) {
  if (!configurado(env)) return faltaConfig();
  const q = await quemE(request, env); if (!q || q.cli !== 'admin') return json({ erro: 'Só o admin.' }, 403);
  const id = new URL(request.url).searchParams.get('id') || ''; if (!/^[a-z0-9-]{3,40}$/i.test(id)) return json({ erro: 'id inválido.' }, 400);
  const r = (await env.CONTAS.get(K, 'json')) || { dados: { itens: [] }, versao: 0 }, d = Object.assign({ itens: [] }, r.dados || {});
  const antes = d.itens.length; d.itens = d.itens.filter(x => x.id !== id); d.apagadas = [...new Set((d.apagadas || []).concat([id]))];
  if (d.itens.length === antes) return json({ erro: 'Não achei essa linha.' }, 404);
  await env.CONTAS.put(K, JSON.stringify({ dados: d, versao: (r.versao || 0) + 1, por: q.email, em: new Date().toISOString() }));
  return json({ ok: true, removida: id });
}
