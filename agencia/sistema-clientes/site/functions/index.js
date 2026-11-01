// Quem já entrou e abre o endereço principal vai direto para o próprio painel.
import { quemE } from './_lib.js';
export async function onRequestGet({ request, env, next }) {
  const q = await quemE(request, env);
  return q ? Response.redirect(new URL(request.url).origin + '/painel/' + q.cli, 302) : next();
}
