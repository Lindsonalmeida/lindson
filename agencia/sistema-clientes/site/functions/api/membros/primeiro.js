// POST /api/membros/primeiro {email, cpf, senha} → primeiro acesso: confere o e-mail e o CPF da compra (hash) e cria a senha.
// Só para quem tem pelo menos um produto e ainda não criou senha. Esqueceu a senha: o admin zera em /painel/membros e a pessoa faz o primeiro acesso de novo.
import { configuradoM, faltaConfigM, normEmail, emailOk, chave, soDigitos, docOk, hashSenha, iguais, ativos, alteraMembro, cookieMembro, bloqueado, errou, acertou, json } from '../../_membros.js';
import { espera } from '../../_lib.js';
const ERRO = 'Não encontramos uma compra com este e-mail e CPF. Use o mesmo e-mail e CPF da compra na Hubla.';
export async function onRequestPost({ request, env }) {
  if (!configuradoM(env)) return faltaConfigM();
  let b = {}; try { b = await request.json(); } catch (e) {}
  const email = normEmail(b && b.email), doc = soDigitos(b && b.cpf), senha = String((b && b.senha) || '');
  if (!emailOk(email) || !docOk(doc)) return json({ erro: 'Preencha o e-mail e o CPF (só os números) da compra.' }, 400);
  if (senha.length < 8 || senha.length > 200) return json({ erro: 'Crie uma senha com pelo menos 8 caracteres.' }, 400);
  if (await bloqueado(env, 'primeiro', email)) { await espera(); return json({ erro: 'Muitas tentativas. Espere 15 minutos e tente de novo.' }, 429); }
  const rec = await env.CONTAS.get(chave(email), 'json');
  const confere = !!(rec && rec.docHash && iguais((await hashSenha(doc, rec.docHash.sal)).hash, rec.docHash.hash));
  if (!rec || !rec.docHash) await hashSenha(doc); // mesmo tempo com ou sem cadastro
  if (!confere || !ativos(rec).length) { await errou(env, 'primeiro', email); await espera(); return json({ erro: ERRO }, 401); }
  if (rec.senha) return json({ erro: 'Você já criou a sua senha. Use a aba Entrar. Esqueceu? Fale com o suporte.' }, 409);
  const senhaH = await hashSenha(senha), sv = (rec.sv | 0) + 1, agora = new Date().toISOString();
  const r = await alteraMembro(env, email, x => { if (!x || x.senha) return null; x.senha = senhaH; x.sv = sv; x.primeiroAcesso = agora; return x; });
  const fin = await env.CONTAS.get(chave(email), 'json');
  if (!r.ok || !fin || !fin.senha || fin.senha.hash !== senhaH.hash) return json({ erro: 'Não deu para criar a senha agora. Tente de novo em instantes.' }, 409);
  await acertou(env, 'primeiro', email);
  return json({ ok: true, destino: '/membros/area' }, 200, { 'Set-Cookie': await cookieMembro(env, email, fin.sv | 0) });
}
