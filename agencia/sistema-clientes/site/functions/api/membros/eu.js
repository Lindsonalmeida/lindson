// GET /api/membros/eu → {nome, produtos:[slugs liberados], checkout:{slug: link}, contato}. Só com a sessão do membro.
import { quemMembro, ativos, primeiroNome, checkoutPublico, CONTATO, json } from '../../_membros.js';
export async function onRequestGet({ request, env }) {
  const q = await quemMembro(request, env);
  if (!q) return json({ erro: 'Entre de novo.' }, 401);
  return json({ nome: primeiroNome(q.rec.nome) || 'Membro', produtos: ativos(q.rec), checkout: checkoutPublico(), contato: /^https:\/\//.test(CONTATO) ? CONTATO : '' }, 200, { 'Cache-Control': 'private, no-store' });
}
