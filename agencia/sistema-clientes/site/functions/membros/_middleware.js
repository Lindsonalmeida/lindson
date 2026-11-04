// Protege /membros/*: a tela de acesso (/membros/) e as imagens são abertas; a área e as páginas dos produtos pedem a sessão do membro.
// Quem já entrou e abre /membros/ vai direto para a área. Builder Squad · backend, 04/11/2026.
import { quemMembro } from '../_membros.js';
export async function onRequest({ request, env, next }) {
  const u = new URL(request.url), p = u.pathname.replace(/\/{2,}/g, '/');
  const semCache = r => { const out = new Response(r.body, r); out.headers.set('Cache-Control', 'private, no-store'); out.headers.set('X-Robots-Tag', 'noindex'); return out; };
  if (p.startsWith('/membros/img/')) return next();
  if (p === '/membros/sair') return next();
  if (p === '/membros' || p === '/membros/' || p === '/membros/index' || p === '/membros/index.html') {
    if (await quemMembro(request, env)) return Response.redirect(u.origin + '/membros/area', 302);
    return semCache(await next());
  }
  if (!(await quemMembro(request, env))) return Response.redirect(u.origin + '/membros/', 302);
  return semCache(await next());
}
