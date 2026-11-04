// GET /api/membros/arquivo?p=<slug>&f=<arquivo> → baixa um arquivo do produto, só para quem comprou (ou o admin da agência).
// Só nomes da lista ARQUIVOS (_membros.js). Os arquivos ficam em /membros-arquivos/, que a guarda geral bloqueia ao público.
import { quemMembro, adminAgencia, ativos, slugOk, arquivoDe, json } from '../../_membros.js';
export async function onRequestGet({ request, env }) {
  const u = new URL(request.url), slug = u.searchParams.get('p') || '', f = u.searchParams.get('f') || '';
  const a = slugOk(slug) ? arquivoDe(slug, f) : null;
  if (!a) return json({ erro: 'Arquivo não encontrado.' }, 404);
  const q = await quemMembro(request, env);
  const pode = (q && ativos(q.rec).includes(slug)) || (!q && await adminAgencia(request, env));
  if (!pode) return json({ erro: q ? 'Este produto não está liberado para você.' : 'Entre de novo.' }, q ? 403 : 401);
  const r = await env.ASSETS.fetch(new URL(`/membros-arquivos/${slug}/${a.f}`, u.origin));
  if (!r.ok) return json({ erro: 'Arquivo não encontrado.' }, 404);
  return new Response(r.body, { headers: {
    'Content-Type': a.tipo,
    'Content-Disposition': `attachment; filename="${a.f}"; filename*=UTF-8''${encodeURIComponent(a.f)}`,
    'Cache-Control': 'private, no-store', 'X-Content-Type-Options': 'nosniff', 'X-Robots-Tag': 'noindex' } });
}
