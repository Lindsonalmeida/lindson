// POST /api/criar {nome, email, senha, codigo} → cria a conta (uma vez), ligada ao painel do código, e já entra.
import { json, espera, normEmail, emailOk, clienteDoCodigo, hashSenha, cookieDe, configurado, faltaConfig } from '../_lib.js';
export async function onRequestPost({ request, env }) {
  if (!configurado(env)) return faltaConfig();
  let b = {}; try { b = await request.json(); } catch (e) {}
  const nome = String(b.nome || '').trim().slice(0, 80), email = normEmail(b.email), senha = String(b.senha || '');
  if (!nome || !emailOk(email)) return json({ erro: 'Preencha o nome e um e-mail válido.' }, 400);
  if (senha.length < 8 || senha.length > 200) return json({ erro: 'Use uma senha com pelo menos 8 caracteres.' }, 400);
  const cli = await clienteDoCodigo(env, b.codigo);
  if (!cli) { await espera(); return json({ erro: 'Código de acesso não encontrado. Confira o código com a nossa equipe.' }, 401); }
  if (await env.CONTAS.get('conta:' + email)) return json({ erro: 'Já existe uma conta com este e-mail. Use a aba Entrar.' }, 409);
  const { sal, hash } = await hashSenha(senha);
  await env.CONTAS.put('conta:' + email, JSON.stringify({ nome, email, cli, sal, hash, criada: new Date().toISOString() }));
  return json({ ok: true, destino: '/painel/' + cli }, 200, { 'Set-Cookie': await cookieDe(env, cli, email) });
}
