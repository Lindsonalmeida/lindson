// /api/contas: só o admin. GET lista as contas (sem senha). DELETE ?email=... apaga uma conta (a pessoa cria de novo com o código).
import { json, quemE, normEmail, configurado, faltaConfig } from '../_lib.js';
async function admin(request, env) { const q = await quemE(request, env); return q && q.cli === 'admin' ? q : null; }
export async function onRequestGet({ request, env }) {
  if (!configurado(env)) return faltaConfig();
  if (!await admin(request, env)) return json({ erro: 'Só o administrador.' }, 403);
  const out = []; let cursor;
  do { const r = await env.CONTAS.list({ prefix: 'conta:', cursor }); for (const k of r.keys) { const c = await env.CONTAS.get(k.name, 'json'); if (c) out.push({ nome: c.nome, email: c.email, cli: c.cli, criada: c.criada }); } cursor = r.list_complete ? null : r.cursor; } while (cursor);
  return json({ contas: out.sort((a, b) => (a.cli + a.nome).localeCompare(b.cli + b.nome)) });
}
export async function onRequestDelete({ request, env }) {
  if (!configurado(env)) return faltaConfig();
  const q = await admin(request, env); if (!q) return json({ erro: 'Só o administrador.' }, 403);
  const email = normEmail(new URL(request.url).searchParams.get('email'));
  if (email === q.email) return json({ erro: 'Você não pode apagar a sua própria conta.' }, 400);
  await env.CONTAS.delete('conta:' + email);
  return json({ ok: true });
}
