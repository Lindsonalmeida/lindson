// Área de membros dos produtos do Lindson (Builder Squad · backend, 04/11/2026).
// Venda na Hubla (checkout de cada produto); o webhook POST /api/hubla libera ou tira o produto (ver functions/api/hubla.js).
// Todos os 5 produtos ficam na mesma área (/membros/area); a pessoa só abre o que comprou, os outros aparecem com "Comprar".
// Dados mínimos (LGPD): nome, e-mail, hash PBKDF2 do CPF (nunca o CPF), 4 últimos dígitos do telefone, produtos e senha em PBKDF2.
// KV (mesmo vínculo CONTAS da Central):
//   membro:<email>              → { nome, email, docHash:{sal,hash}, tel4, produtos:{slug:{ativo,desde,ate,at,v,sub,origem}}, senha:{sal,hash}, sv, criado }
//   hubla:idem:<sha256(x-hubla-idempotency)> → '1' (30 dias), para não processar o mesmo evento duas vezes
//   membro-tent:<tipo>:<hmac(email)>         → nº de tentativas erradas (15 min), contra adivinhação de senha e CPF
// Sessão: cookie lm_membro (separado do cookie "central" da agência), assinado com HMAC(SEGREDO), 30 dias.
import { hmac, normEmail, emailOk, hashSenha, iguais, json, quemE } from './_lib.js';

export const SLUGS = ['kit-mes-pronto', 'kit-whatsapp-que-fecha', 'kit-prospeccao', 'raio-x-do-perfil', 'bio-que-vende'];
export const NOMES = {
  'kit-mes-pronto': 'Kit Mês Pronto',
  'kit-whatsapp-que-fecha': 'Kit WhatsApp que Fecha',
  'kit-prospeccao': 'Kit Prospecção',
  'raio-x-do-perfil': 'Raio-X do Perfil',
  'bio-que-vende': 'Bio que Vende',
};

// >>> LINDSON PREENCHE AQUI <<<
// ID de cada produto na Hubla → produto da área. Onde achar: Hubla → Produtos → abra o produto → o ID aparece no endereço
// (app.hub.la/.../products/<ID>/...) e no campo "event.product.id" do histórico de webhooks (Integrações → Webhooks → Histórico).
// Pode ter mais de um ID para o mesmo produto (ex.: um produto de combo). IDs que não estão aqui são ignorados.
export const MAPA_HUBLA = {
  'PREENCHER-ID-HUBLA-KIT-MES-PRONTO': 'kit-mes-pronto',
  'PREENCHER-ID-HUBLA-KIT-WHATSAPP': 'kit-whatsapp-que-fecha',
  'PREENCHER-ID-HUBLA-KIT-PROSPECCAO': 'kit-prospeccao',
  'PREENCHER-ID-HUBLA-RAIO-X': 'raio-x-do-perfil',
  'PREENCHER-ID-HUBLA-BIO': 'bio-que-vende',
};
// Link do checkout de cada produto (Hubla → Produtos → Links de venda). Enquanto tiver "PREENCHER", o botão Comprar fica "em breve".
export const CHECKOUT = {
  'kit-mes-pronto': 'https://pay.hub.la/PREENCHER-kit-mes-pronto',
  'kit-whatsapp-que-fecha': 'https://pay.hub.la/PREENCHER-kit-whatsapp-que-fecha',
  'kit-prospeccao': 'https://pay.hub.la/PREENCHER-kit-prospeccao',
  'raio-x-do-perfil': 'https://pay.hub.la/PREENCHER-raio-x-do-perfil',
  'bio-que-vende': 'https://pay.hub.la/PREENCHER-bio-que-vende',
};
// Link "Falar com o Lindson" (ex.: https://wa.me/55DDNUMERO). Vazio = o botão some.
export const CONTATO = '';
// <<< FIM DO QUE O LINDSON PREENCHE >>>

// Arquivos de cada produto (só estes nomes podem ser baixados). Ficam em /membros-arquivos/<slug>/ (bloqueado ao público pela guarda geral).
export const ARQUIVOS = {
  'kit-mes-pronto': [
    { f: 'Kit-Mes-Pronto.pdf', nome: 'Kit Mês Pronto · PDF com os 30 roteiros, ganchos e legendas', tipo: 'application/pdf' },
    { f: 'calendario-30-dias.xlsx', nome: 'Calendário de 30 dias · planilha (Excel / Google Planilhas)', tipo: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' },
    { f: 'calendario-30-dias.csv', nome: 'Calendário de 30 dias · CSV', tipo: 'text/csv; charset=utf-8' },
  ],
  'kit-whatsapp-que-fecha': [
    { f: 'Kit-WhatsApp-que-Fecha.pdf', nome: 'Kit WhatsApp que Fecha · PDF com o script e as respostas', tipo: 'application/pdf' },
    { f: 'atalhos.txt', nome: '43 atalhos de resposta rápida · texto', tipo: 'text/plain; charset=utf-8' },
    { f: 'atalhos.csv', nome: '43 atalhos de resposta rápida · CSV', tipo: 'text/csv; charset=utf-8' },
  ],
  'kit-prospeccao': [
    { f: 'Kit-Prospeccao-pelo-WhatsApp.pdf', nome: 'Kit Prospecção pelo WhatsApp · PDF com o método, a cadência e as 100 mensagens', tipo: 'application/pdf' },
    { f: '100-Mensagens-Kit-Prospeccao.txt', nome: '100 mensagens de prospecção · texto', tipo: 'text/plain; charset=utf-8' },
    { f: 'Planilha-Cadencia-Kit-Prospeccao.xlsx', nome: 'Planilha da cadência de 4 toques · Excel', tipo: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' },
  ],
  'raio-x-do-perfil': [],
  'bio-que-vende': [],
};
export const arquivoDe = (slug, f) => (ARQUIVOS[slug] || []).find(a => a.f === f) || null;

export const COOKIE_M = 'lm_membro';
export const chave = email => 'membro:' + email;
export const configuradoM = env => !!(env.SEGREDO && env.CONTAS);
export const faltaConfigM = () => json({ erro: 'A área de membros ainda não foi configurada.' }, 503);
export const soDigitos = s => String(s || '').replace(/\D/g, '');
export const docOk = d => d.length === 11 || d.length === 14; // CPF ou CNPJ, só números
export const slugOk = s => SLUGS.includes(s);
export const ativos = rec => SLUGS.filter(s => rec && rec.produtos && rec.produtos[s] && rec.produtos[s].ativo);
export const checkoutPublico = () => Object.fromEntries(SLUGS.map(s => [s, /PREENCHER/.test(CHECKOUT[s] || '') || !/^https:\/\//.test(CHECKOUT[s] || '') ? '' : CHECKOUT[s]]));
export { normEmail, emailOk, json };

const enc = new TextEncoder();
const hex = b => [...new Uint8Array(b)].map(x => x.toString(16).padStart(2, '0')).join('');
export const sha256 = async t => hex(await crypto.subtle.digest('SHA-256', enc.encode(t)));
// comparação em tempo constante mesmo com tamanhos diferentes (compara HMACs com chave aleatória do momento)
export async function iguaisSeguro(a, b) {
  const k = hex(crypto.getRandomValues(new Uint8Array(32)));
  return iguais(await hmac(k, String(a)), await hmac(k, String(b)));
}
export const dormir = ms => new Promise(r => setTimeout(r, ms));

// ---- tentativas erradas (por e-mail, 15 min) ----
const LIMITE = 10;
const kTent = async (env, tipo, email) => `membro-tent:${tipo}:${(await hmac(env.SEGREDO, 'tent|' + email)).slice(0, 32)}`;
export async function bloqueado(env, tipo, email) { return (+(await env.CONTAS.get(await kTent(env, tipo, email))) || 0) >= LIMITE; }
export async function errou(env, tipo, email) { const k = await kTent(env, tipo, email); await env.CONTAS.put(k, String((+(await env.CONTAS.get(k)) || 0) + 1), { expirationTtl: 900 }); }
export async function acertou(env, tipo, email) { await env.CONTAS.delete(await kTent(env, tipo, email)); }

// ---- grava o registro do membro com conferência (o KV não tem transação) ----
// fn recebe uma cópia do registro atual (ou null) e devolve o novo (ou null = nada a mudar). fn tem de ser idempotente.
// Lê, aplica, grava, espera um pouco e lê de novo: só termina quando a leitura já mostra a mudança (protege dois webhooks juntos).
export async function alteraMembro(env, email, fn) {
  for (let i = 0; i < 5; i++) {
    const cur = await env.CONTAS.get(chave(email), 'json');
    const nxt = fn(cur ? JSON.parse(JSON.stringify(cur)) : null);
    if (!nxt || JSON.stringify(nxt) === JSON.stringify(cur)) return { ok: true, rec: cur };
    await env.CONTAS.put(chave(email), JSON.stringify(nxt));
    await dormir(40 + Math.floor(Math.random() * 160));
  }
  return { ok: false };
}

// ---- sessão do membro: lm_membro=<exp>.<email b64url>.<sv>.<assinatura> ----
const b64 = s => btoa(unescape(encodeURIComponent(s))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const deb64 = s => decodeURIComponent(escape(atob(s.replace(/-/g, '+').replace(/_/g, '/'))));
const DIAS = 30;
export async function cookieMembro(env, email, sv) {
  const exp = Date.now() + DIAS * 864e5, val = `${exp}.${b64(email)}.${sv | 0}`, sig = await hmac(env.SEGREDO, 'lm_membro|' + val);
  return `${COOKIE_M}=${val}.${sig}; Path=/; Max-Age=${DIAS * 86400}; HttpOnly; Secure; SameSite=Lax`;
}
export const cookieSair = () => `${COOKIE_M}=; Path=/; Max-Age=0; HttpOnly; Secure; SameSite=Lax`;
export async function quemMembro(request, env) {
  if (!configuradoM(env)) return null;
  const m = (request.headers.get('Cookie') || '').match(/(?:^|;\s*)lm_membro=([^;]+)/);
  if (!m) return null;
  const partes = m[1].split('.');
  if (partes.length !== 4) return null;
  const [exp, em, sv, sig] = partes;
  if (!/^\d{10,16}$/.test(exp) || !/^\d{1,9}$/.test(sv) || !/^[0-9a-f]{64}$/.test(sig) || Date.now() > +exp) return null;
  if (!iguais(await hmac(env.SEGREDO, `lm_membro|${exp}.${em}.${sv}`), sig)) return null;
  let email; try { email = deb64(em); } catch (e) { return null; }
  const rec = await env.CONTAS.get(chave(email), 'json');
  if (!rec || !rec.senha || (rec.sv | 0) !== +sv) return null; // senha trocada, saiu ou admin zerou: sessão antiga não vale mais
  return { email, rec };
}

// admin da agência (cookie "central" com cli admin)
export async function adminAgencia(request, env) { const q = await quemE(request, env); return q && q.cli === 'admin' ? q : null; }

export const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
export const primeiroNome = n => String(n || '').trim().split(/\s+/)[0].slice(0, 40);
export { hashSenha, iguais };
