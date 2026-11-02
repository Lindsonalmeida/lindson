// /_blob/<id>: imagens antigas da Fábrica de Conteúdo (o app guardava "/_blob/<id>"); servidas de /painel/fabrica-fotos/. Só o admin.
import { json, quemE } from '../_lib.js';
export async function onRequestGet({ request, env, params }) {
  const q = await quemE(request, env);
  if (!q || q.cli !== 'admin') return json({ erro: 'Só o administrador.' }, 403);
  const id = String(params.id || '');
  if (!/^[A-Za-z0-9_-]{6,80}$/.test(id)) return json({ erro: 'Pedido inválido.' }, 400);
  for (const ext of ['jpg', 'webp', 'png']) {
    const r = await env.ASSETS.fetch(new URL('/painel/fabrica-fotos/' + id + '.' + ext, request.url));
    if (r.status === 200) { const h = new Headers(r.headers); h.set('Cache-Control', 'private, max-age=86400'); return new Response(r.body, { headers: h }); }
  }
  return json({ erro: 'Imagem não encontrada.' }, 404);
}
