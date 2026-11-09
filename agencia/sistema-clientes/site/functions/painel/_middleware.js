// Protege /painel/*: sem login válido volta para a tela de acesso; cada cliente só abre o próprio painel; "admin" abre todos.
import { quemE } from '../_lib.js';
export async function onRequest({ request, env, next }) {
  const q = await quemE(request, env), u = new URL(request.url);
  const alvo = (u.pathname.split('/')[2] || '').replace(/\.html$/, '');
  if (!q) return Response.redirect(u.origin + '/', 302);
  // páginas só do admin, mesmo se um dia existir um cliente com esse nome (Central de Comando, conta Leandro, 09/11/2026)
  const SO_ADMIN = ['admin', 'comando', 'contas', 'membros', 'canais'];  // canais: canais dark (conta Leandro, 09/11/2026)
  if (q.cli !== 'admin' && (alvo !== q.cli || SO_ADMIN.includes(alvo))) return Response.redirect(u.origin + '/painel/' + q.cli, 302);
  const r = await next(), out = new Response(r.body, r);
  out.headers.set('Cache-Control', 'private, no-store'); out.headers.set('X-Robots-Tag', 'noindex');
  return out;
}
