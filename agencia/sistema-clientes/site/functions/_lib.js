// Funções comuns do acesso da Central (Cloudflare Pages Functions). Conta Lindson, 01/11/2026.
// Um sistema só: a pessoa cria a conta UMA vez com nome, e-mail, senha e o código de acesso (o código diz qual é o painel dela).
// Depois entra só com e-mail e senha e cai direto no painel dela. Conta "admin" (Lindson) abre todos.
// Na Cloudflare (Configurações do projeto Pages):
//   Variáveis e segredos (tipo Segredo):
//     SEGREDO = texto aleatório longo (assina o cookie e os códigos)
//     CODIGOS = JSON {"<HMAC-SHA256(SEGREDO, código)>": "admin" | "jaci" | "leo" | "apple"}
//   Vínculos (Bindings) → KV: variável CONTAS = namespace "central-contas" (guarda as contas, com a senha em PBKDF2)
// Os códigos nunca ficam no código nem no GitHub: só o HMAC deles, e só na Cloudflare.
// Códigos de clientes novos (sem mexer nos segredos da Cloudflare): _codigos.js lista {sal, hash, cli} com o hash PBKDF2 do código.
// O _codigos.js de verdade existe SÓ no repositório privado (CentralLindsonALmeida); aqui no público ele fica vazio. Nunca copie o vazio por cima do privado.
import { EXTRA } from './_codigos.js';
const enc = new TextEncoder();
const hex = b => [...new Uint8Array(b)].map(x => x.toString(16).padStart(2, '0')).join('');
export async function hmac(segredo, texto) {
  const k = await crypto.subtle.importKey('raw', enc.encode(segredo), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  return hex(await crypto.subtle.sign('HMAC', k, enc.encode(texto)));
}
export const normaliza = c => String(c || '').toUpperCase().replace(/[^A-Z0-9]/g, '');
export const normEmail = e => String(e || '').trim().toLowerCase();
export const emailOk = e => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e) && e.length <= 120;
export const COOKIE = 'central';
export const json = (o, s = 200, h = {}) => new Response(JSON.stringify(o), { status: s, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store', ...h } });
export const espera = () => new Promise(r => setTimeout(r, 800));

// senha: PBKDF2-SHA256, 100 mil voltas (máximo do Workers), sal aleatório por conta
export async function hashSenha(senha, salHex) {
  const sal = salHex ? Uint8Array.from(salHex.match(/../g).map(h => parseInt(h, 16))) : crypto.getRandomValues(new Uint8Array(16));
  const k = await crypto.subtle.importKey('raw', enc.encode(senha), 'PBKDF2', false, ['deriveBits']);
  const bits = await crypto.subtle.deriveBits({ name: 'PBKDF2', hash: 'SHA-256', salt: sal, iterations: 100000 }, k, 256);
  return { sal: hex(sal), hash: hex(bits) };
}
export function iguais(a, b) { if (a.length !== b.length) return false; let d = 0; for (let i = 0; i < a.length; i++) d |= a.charCodeAt(i) ^ b.charCodeAt(i); return d === 0; }

// código de acesso → cliente (ou null)
export async function clienteDoCodigo(env, codigo) {
  const c = normaliza(codigo); if (c.length !== 11) return null;
  let mapa = {}; try { mapa = JSON.parse(env.CODIGOS); } catch (e) {}
  const cli = mapa[await hmac(env.SEGREDO, c)];
  if (cli) return cli;
  for (const x of EXTRA || []) { const { hash } = await hashSenha(c, x.sal); if (iguais(hash, x.hash)) return x.cli; }
  return null;
}

// cookie assinado: cli.exp.emailBase64url.sig
const b64 = s => btoa(unescape(encodeURIComponent(s))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const deb64 = s => decodeURIComponent(escape(atob(s.replace(/-/g, '+').replace(/_/g, '/'))));
export async function cookieDe(env, cli, email) {
  const exp = Date.now() + 30 * 864e5, val = `${cli}.${exp}.${b64(email)}`, sig = await hmac(env.SEGREDO, val);
  return `${COOKIE}=${val}.${sig}; Path=/; Max-Age=${30 * 86400}; HttpOnly; Secure; SameSite=Lax`;
}
export async function quemE(request, env) {
  const m = (request.headers.get('Cookie') || '').match(/(?:^|;\s*)central=([^;]+)/);
  if (!m || !env.SEGREDO) return null;
  const [cli, exp, em, sig] = m[1].split('.');
  if (!cli || !exp || !em || !sig || Date.now() > +exp) return null;
  if (!iguais(await hmac(env.SEGREDO, `${cli}.${exp}.${em}`), sig)) return null;
  let email; try { email = deb64(em); } catch (e) { return null; }
  if (env.CONTAS) { const c = await env.CONTAS.get('conta:' + email, 'json'); if (!c || c.cli !== cli) return null; } // conta apagada pelo admin perde o acesso
  return { cli, email };
}
export const configurado = env => env.SEGREDO && env.CODIGOS && env.CONTAS;
export const faltaConfig = () => json({ erro: 'A Central ainda não foi configurada (faltam SEGREDO, CODIGOS ou o vínculo CONTAS na Cloudflare).' }, 500);
