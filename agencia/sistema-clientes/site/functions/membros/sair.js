// /membros/sair: encerra a sessão do membro (e invalida o cookie em todos os aparelhos) e volta para a tela de acesso.
import { quemMembro, alteraMembro, cookieSair } from '../_membros.js';
export async function onRequest({ request, env }) {
  const q = await quemMembro(request, env);
  if (q) { const sv = (q.rec.sv | 0) + 1; await alteraMembro(env, q.email, x => { if (!x || (x.sv | 0) >= sv) return null; x.sv = sv; return x; }); }
  return new Response(null, { status: 302, headers: { Location: new URL(request.url).origin + '/membros/', 'Set-Cookie': cookieSair(), 'Cache-Control': 'no-store' } });
}
