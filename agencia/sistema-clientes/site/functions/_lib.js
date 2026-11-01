// Funções comuns do acesso da Central (Cloudflare Pages Functions). Conta Lindson, 01/11/2026.
// Variáveis no painel da Cloudflare (Settings → Variables and Secrets, tipo Secret):
//   SEGREDO  = texto aleatório longo (assina o cookie e os códigos)
//   CODIGOS  = JSON {"<HMAC-SHA256(SEGREDO, código)>": "admin" | "jaci" | "leo" | "apple"}
// Os códigos nunca ficam no código nem no GitHub: só o HMAC deles, e só na Cloudflare.
const enc = new TextEncoder();
export async function hmac(segredo, texto) {
  const k = await crypto.subtle.importKey('raw', enc.encode(segredo), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const sig = await crypto.subtle.sign('HMAC', k, enc.encode(texto));
  return [...new Uint8Array(sig)].map(b => b.toString(16).padStart(2, '0')).join('');
}
export const normaliza = c => String(c || '').toUpperCase().replace(/[^A-Z0-9]/g, '');
export const COOKIE = 'central';
export async function quemE(request, env) {
  const m = (request.headers.get('Cookie') || '').match(/(?:^|;\s*)central=([^;]+)/);
  if (!m || !env.SEGREDO) return null;
  const [cli, exp, sig] = decodeURIComponent(m[1]).split('.');
  if (!cli || !exp || !sig || Date.now() > +exp) return null;
  return (await hmac(env.SEGREDO, cli + '.' + exp)) === sig ? cli : null;
}
