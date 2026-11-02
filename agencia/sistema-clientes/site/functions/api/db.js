// /api/db?col=<caminho>: banco de documentos do ADMINISTRADOR com a mesma forma do banco do claude.ai (coleções e documentos por caminho).
// Usado pelos apps do Lindson trazidos para a Central (Recomeço 90, Fábrica). Cada coleção é um valor no KV: db:<caminho> → {docs: {id: dados}}.
// GET → {docs}. POST {op: set|update|delete, id, data} → grava. Só o admin. Conta Lindson, 02/11/2026.
import { json, quemE, configurado, faltaConfig } from '../_lib.js';
const caminhoOk = c => /^[A-Za-z0-9_\-.~:@+]{1,200}(\/[A-Za-z0-9_\-.~:@+]{1,200}){0,14}$/.test(c || '') && c.split('/').length % 2 === 1;
async function admin(request, env) { const q = await quemE(request, env); return q && q.cli === 'admin'; }
export async function onRequestGet({ request, env }) {
  if (!configurado(env)) return faltaConfig();
  if (!await admin(request, env)) return json({ erro: 'Só o administrador.' }, 403);
  const col = new URL(request.url).searchParams.get('col'); if (!caminhoOk(col)) return json({ erro: 'Caminho inválido.' }, 400);
  return json((await env.CONTAS.get('db:' + col, 'json')) || { docs: {} });
}
export async function onRequestPost({ request, env }) {
  if (!configurado(env)) return faltaConfig();
  if (!await admin(request, env)) return json({ erro: 'Só o administrador.' }, 403);
  let b; try { b = await request.json(); } catch (e) { return json({ erro: 'Dados inválidos.' }, 400); }
  const ops = Array.isArray(b.ops) ? b.ops : [b], porCol = {};
  for (const o of ops) { if (!caminhoOk(o.col) || !/^[A-Za-z0-9_\-.~:@+]{1,200}$/.test(o.id || '') || !['set', 'update', 'delete'].includes(o.op)) return json({ erro: 'Operação inválida.' }, 400); (porCol[o.col] = porCol[o.col] || []).push(o); }
  for (const [col, lista] of Object.entries(porCol)) {
    const atual = (await env.CONTAS.get('db:' + col, 'json')) || { docs: {} };
    for (const o of lista) {
      if (o.op === 'delete') delete atual.docs[o.id];
      else if (o.op === 'set') atual.docs[o.id] = o.data || {};
      else atual.docs[o.id] = Object.assign(atual.docs[o.id] || {}, o.data || {});
    }
    const txt = JSON.stringify(atual); if (txt.length > 20e6) return json({ erro: 'Coleção grande demais.' }, 413);
    await env.CONTAS.put('db:' + col, txt);
  }
  return json({ ok: true });
}
