// /api/fotos?cli=<cliente>: fotos que o cliente manda para a agência (guardadas no KV, sem índice: a lista vem do próprio KV).
// GET → lista (com quem mandou, categoria e data). POST (corpo = imagem; ?cat=&nome=&id=&thumb=1) → guarda. DELETE ?id= → apaga.
// Só o próprio cliente ou o admin. Conta Lindson, 01/11/2026.
import { json, quemE, configurado, faltaConfig } from '../_lib.js';
const TIPOS = ['image/jpeg', 'image/png', 'image/webp'];
export async function acessoFoto(request, env) {
  const q = await quemE(request, env), u = new URL(request.url), cli = (u.searchParams.get('cli') || '').toLowerCase();
  if (!q) return { erro: json({ erro: 'Entre na Central de novo.' }, 401) };
  if (!/^[a-z0-9-]{2,30}$/.test(cli)) return { erro: json({ erro: 'Pedido inválido.' }, 400) };
  if (q.cli !== 'admin' && q.cli !== cli) return { erro: json({ erro: 'Sem acesso a este painel.' }, 403) };
  return { q, cli, u };
}
const idOk = id => /^[a-z0-9]{6,40}$/.test(id || '');
export async function onRequestGet({ request, env }) {
  if (!configurado(env)) return faltaConfig();
  const a = await acessoFoto(request, env); if (a.erro) return a.erro;
  const fotos = []; let cursor;
  do { const r = await env.CONTAS.list({ prefix: `foto:${a.cli}:`, cursor }); r.keys.forEach(k => fotos.push({ id: k.name.split(':')[2], ...(k.metadata || {}) })); cursor = r.list_complete ? null : r.cursor; } while (cursor);
  return json({ fotos: fotos.sort((x, y) => (y.em || '').localeCompare(x.em || '')) });
}
export async function onRequestPost({ request, env }) {
  if (!configurado(env)) return faltaConfig();
  const a = await acessoFoto(request, env); if (a.erro) return a.erro;
  const tipo = (request.headers.get('content-type') || '').split(';')[0];
  if (!TIPOS.includes(tipo)) return json({ erro: 'Envie uma foto (JPG, PNG ou WEBP).' }, 415);
  const buf = await request.arrayBuffer();
  if (!buf.byteLength || buf.byteLength > 8e6) return json({ erro: 'Foto grande demais (máximo 8 MB).' }, 413);
  const p = a.u.searchParams, thumb = p.get('thumb') === '1';
  const id = thumb ? p.get('id') : Date.now().toString(36) + Math.random().toString(36).slice(2, 8);
  if (!idOk(id)) return json({ erro: 'Pedido inválido.' }, 400);
  if (thumb) { if (!(await env.CONTAS.get(`foto:${a.cli}:${id}`, 'stream'))) return json({ erro: 'Foto não encontrada.' }, 404); await env.CONTAS.put(`fotot:${a.cli}:${id}`, buf, { metadata: { tipo } }); return json({ ok: true, id }); }
  const meta = { tipo, cat: (p.get('cat') || 'Outras').slice(0, 40), nome: (p.get('nome') || 'foto').slice(0, 60), em: new Date().toISOString(), por: a.q.cli === 'admin' ? 'agência' : 'cliente', tam: buf.byteLength, w: +p.get('w') || 0, h: +p.get('h') || 0 };
  await env.CONTAS.put(`foto:${a.cli}:${id}`, buf, { metadata: meta });
  return json({ ok: true, id, ...meta });
}
export async function onRequestDelete({ request, env }) {
  if (!configurado(env)) return faltaConfig();
  const a = await acessoFoto(request, env); if (a.erro) return a.erro;
  const id = a.u.searchParams.get('id'); if (!idOk(id)) return json({ erro: 'Pedido inválido.' }, 400);
  await env.CONTAS.delete(`foto:${a.cli}:${id}`); await env.CONTAS.delete(`fotot:${a.cli}:${id}`);
  return json({ ok: true });
}
