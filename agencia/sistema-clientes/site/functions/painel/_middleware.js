// Protege /painel/*: sem cookie válido volta para o login; cada cliente só abre o próprio painel; "admin" abre todos.
import { quemE } from '../_lib.js';
export async function onRequest({ request, env, next }) {
  const cli = await quemE(request, env), u = new URL(request.url);
  const alvo = (u.pathname.split('/')[2] || '').replace(/\.html$/, '');
  if (!cli) return Response.redirect(u.origin + '/', 302);
  if (cli !== 'admin' && alvo !== cli) return Response.redirect(u.origin + '/painel/' + cli, 302);
  const r = await next(), out = new Response(r.body, r);
  out.headers.set('Cache-Control', 'private, no-store'); out.headers.set('X-Robots-Tag', 'noindex');
  return out;
}
