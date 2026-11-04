// POST /api/membros/entrar {email, senha} → entra na área de membros (cookie lm_membro, 30 dias). Mensagem de erro genérica.
import { configuradoM, faltaConfigM, normEmail, chave, hashSenha, iguais, cookieMembro, bloqueado, errou, acertou, json } from '../../_membros.js';
import { espera } from '../../_lib.js';
const ERRO = 'E-mail ou senha não conferem. Primeira vez aqui? Use a aba Primeiro acesso.';
export async function onRequestPost({ request, env }) {
  if (!configuradoM(env)) return faltaConfigM();
  let b = {}; try { b = await request.json(); } catch (e) {}
  const email = normEmail(b && b.email).slice(0, 120), senha = String((b && b.senha) || '').slice(0, 200);
  if (!email || !senha) { await espera(); return json({ erro: ERRO }, 401); }
  if (await bloqueado(env, 'entrar', email)) { await espera(); return json({ erro: 'Muitas tentativas. Espere 15 minutos e tente de novo.' }, 429); }
  const rec = await env.CONTAS.get(chave(email), 'json');
  const ok = !!(rec && rec.senha && iguais((await hashSenha(senha, rec.senha.sal)).hash, rec.senha.hash));
  if (!ok) { if (!rec || !rec.senha) await hashSenha(senha); await errou(env, 'entrar', email); await espera(); return json({ erro: ERRO }, 401); } // hash extra: mesmo tempo com ou sem conta
  await acertou(env, 'entrar', email);
  return json({ ok: true, destino: '/membros/area' }, 200, { 'Set-Cookie': await cookieMembro(env, email, rec.sv | 0) });
}
