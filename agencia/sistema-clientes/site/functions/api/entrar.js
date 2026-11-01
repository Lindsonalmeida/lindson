// POST /api/entrar {email, codigo} → confere o código no servidor e grava o cookie assinado (30 dias).
import { hmac, normaliza, COOKIE } from '../_lib.js';
const json = (o, s = 200, h = {}) => new Response(JSON.stringify(o), { status: s, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store', ...h } });
export async function onRequestPost({ request, env }) {
  if (!env.SEGREDO || !env.CODIGOS) return json({ erro: 'A Central ainda não foi configurada (faltam as variáveis SEGREDO e CODIGOS).' }, 500);
  let corpo = {}; try { corpo = await request.json(); } catch (e) {}
  const codigo = normaliza(corpo.codigo);
  let mapa = {}; try { mapa = JSON.parse(env.CODIGOS); } catch (e) {}
  const cli = codigo.length === 11 ? mapa[await hmac(env.SEGREDO, codigo)] : null;
  if (!cli) { await new Promise(r => setTimeout(r, 800)); return json({ erro: 'Código de acesso não encontrado. Confira o código com a nossa equipe.' }, 401); }
  const exp = Date.now() + 30 * 864e5, val = cli + '.' + exp, sig = await hmac(env.SEGREDO, val);
  return json({ ok: true, destino: '/painel/' + cli }, 200, {
    'Set-Cookie': `${COOKIE}=${encodeURIComponent(val + '.' + sig)}; Path=/; Max-Age=${30 * 86400}; HttpOnly; Secure; SameSite=Lax` });
}
