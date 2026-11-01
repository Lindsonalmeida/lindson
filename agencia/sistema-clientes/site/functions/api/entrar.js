// POST /api/entrar {email, senha} → confere a senha no servidor e abre o painel da pessoa (cookie assinado, 30 dias).
import { json, espera, normEmail, hashSenha, iguais, cookieDe, configurado, faltaConfig } from '../_lib.js';
export async function onRequestPost({ request, env }) {
  if (!configurado(env)) return faltaConfig();
  let b = {}; try { b = await request.json(); } catch (e) {}
  const email = normEmail(b.email), senha = String(b.senha || '').slice(0, 200);
  const c = email ? await env.CONTAS.get('conta:' + email, 'json') : null;
  const ok = c && iguais((await hashSenha(senha, c.sal)).hash, c.hash);
  if (!ok) { await espera(); return json({ erro: 'E-mail ou senha não conferem. Primeira vez aqui? Use a aba Criar conta.' }, 401); }
  return json({ ok: true, destino: '/painel/' + c.cli }, 200, { 'Set-Cookie': await cookieDe(env, c.cli, email) });
}
