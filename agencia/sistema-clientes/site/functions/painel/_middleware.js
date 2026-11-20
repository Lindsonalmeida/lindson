// Protege /painel/*: sem login válido volta para a tela de acesso; cada cliente só abre o próprio painel; "admin" abre todos.
import { quemE } from '../_lib.js';
export async function onRequest({ request, env, next }) {
  const q = await quemE(request, env), u = new URL(request.url);
  const alvo = (u.pathname.split('/')[2] || '').replace(/\.html$/, '');
  if (!q) return Response.redirect(u.origin + '/', 302);
  // páginas só do admin, mesmo se um dia existir um cliente com esse nome (VEKTOR, conta Leandro, 09/11/2026)
  const SO_ADMIN = ['admin', 'comando', 'contas', 'membros', 'canais', 'motionforge'];  // canais: canais dark (conta Leandro, 09/11/2026) · motionforge: estúdio de IA (conta Leandro, 18/11/2026)
  // scripts comuns a todos os painéis (sem dado de cliente): Tarefas feitas, Postados e Biblioteca. Sem isso o cliente era mandado
  // de volta ao próprio painel ao pedir /painel/feitas.js e a aba não aparecia para ele (Builder Squad, 20/11/2026)
  const COMUNS = ['feitas.js', 'postados.js', 'biblioteca.js'];
  if (q.cli !== 'admin' && !COMUNS.includes(alvo) && (alvo !== q.cli || SO_ADMIN.includes(alvo))) return Response.redirect(u.origin + '/painel/' + q.cli, 302);
  const r = await next(), out = new Response(r.body, r);
  out.headers.set('Cache-Control', 'private, no-store'); out.headers.set('X-Robots-Tag', 'noindex');
  return out;
}
