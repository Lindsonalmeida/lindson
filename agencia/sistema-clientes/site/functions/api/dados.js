// /api/dados?cli=<cliente>&f=<crm|fin>: dados das ferramentas do painel (CRM e financeiro), salvos no KV por cliente.
// GET → {dados, versao}. PUT {dados, versao} → grava se a versão bate; se outra pessoa salvou antes, 409 com a versão atual (o painel junta e tenta de novo).
// Só o próprio cliente ou o admin. Conta Lindson, 01/11/2026.
import { json, quemE, configurado, faltaConfig } from '../_lib.js';
const FERR = ['crm', 'fin', 'dem', 'ag'];  // dem e ag: demandas e agenda do gabinete (painel do Leo)
async function acesso(request, env) {
  const q = await quemE(request, env), u = new URL(request.url);
  const cli = (u.searchParams.get('cli') || '').toLowerCase(), f = u.searchParams.get('f');
  if (!q) return { erro: json({ erro: 'Entre na Central de novo.' }, 401) };
  if (!/^[a-z0-9-]{2,30}$/.test(cli) || !FERR.includes(f)) return { erro: json({ erro: 'Pedido inválido.' }, 400) };
  if (q.cli !== 'admin' && q.cli !== cli) return { erro: json({ erro: 'Sem acesso a este painel.' }, 403) };
  return { q, chave: `dados:${cli}:${f}` };
}
export async function onRequestGet({ request, env }) {
  if (!configurado(env)) return faltaConfig();
  const a = await acesso(request, env); if (a.erro) return a.erro;
  const r = await env.CONTAS.get(a.chave, 'json');
  return json(r || { dados: null, versao: 0 });
}
export async function onRequestPut({ request, env }) {
  if (!configurado(env)) return faltaConfig();
  const a = await acesso(request, env); if (a.erro) return a.erro;
  const txt = await request.text();
  if (txt.length > 2_000_000) return json({ erro: 'Dados grandes demais.' }, 413);
  let b; try { b = JSON.parse(txt); } catch (e) { return json({ erro: 'Dados inválidos.' }, 400); }
  const atual = (await env.CONTAS.get(a.chave, 'json')) || { dados: null, versao: 0 };
  if ((b.versao | 0) !== atual.versao) return json(atual, 409);
  const novo = { dados: b.dados, versao: atual.versao + 1, por: a.q.email, em: new Date().toISOString() };
  await env.CONTAS.put(a.chave, JSON.stringify(novo));
  return json({ ok: true, versao: novo.versao });
}
