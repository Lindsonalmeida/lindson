// /api/foto?cli=&id=[&mini=1][&baixar=1]: devolve a imagem (ou a miniatura). Só o próprio cliente ou o admin.
import { json, configurado, faltaConfig } from '../_lib.js';
import { acessoFoto } from './fotos.js';
export async function onRequestGet({ request, env }) {
  if (!configurado(env)) return faltaConfig();
  const a = await acessoFoto(request, env); if (a.erro) return a.erro;
  const p = a.u.searchParams, id = p.get('id') || ''; if (!/^[a-z0-9]{6,40}$/.test(id)) return json({ erro: 'Pedido inválido.' }, 400);
  let r = p.get('mini') === '1' ? await env.CONTAS.getWithMetadata(`fotot:${a.cli}:${id}`, 'stream') : null;
  if (!r || !r.value) r = await env.CONTAS.getWithMetadata(`foto:${a.cli}:${id}`, 'stream');
  if (!r || !r.value) return json({ erro: 'Foto não encontrada.' }, 404);
  const tipo = (r.metadata && r.metadata.tipo) || 'image/jpeg', ext = tipo.split('/')[1].replace('jpeg', 'jpg');
  const h = { 'Content-Type': tipo, 'Cache-Control': 'private, max-age=86400', 'X-Content-Type-Options': 'nosniff' };
  if (p.get('baixar') === '1') h['Content-Disposition'] = `attachment; filename="${a.cli}-${((r.metadata && r.metadata.nome) || id).replace(/[^\w.-]+/g, '-')}.${ext}"`;
  return new Response(r.value, { headers: h });
}
