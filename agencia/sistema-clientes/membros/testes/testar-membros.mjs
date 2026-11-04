// Testes da área de membros (webhook da Hubla, primeiro acesso, login, downloads, admin, guardas). Builder Squad, 04/11/2026.
// Roda as Functions de verdade com um KV falso (Map) e os arquivos estáticos do repositório privado no lugar do ASSETS.
// Uso: node agencia/sistema-clientes/membros/testes/testar-membros.mjs [/caminho/do/CentralLindsonALmeida]
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const RAIZ = path.resolve(process.argv[2] || path.join(path.dirname(new URL(import.meta.url).pathname), '../../../../../centrallindsonalmeida'));
const F = rel => import(pathToFileURL(path.join(RAIZ, 'functions', rel)).href);
const M = await F('_membros.js');
const lib = await F('_lib.js');
const hubla = await F('api/hubla.js');
const entrar = await F('api/membros/entrar.js');
const primeiro = await F('api/membros/primeiro.js');
const eu = await F('api/membros/eu.js');
const arquivo = await F('api/membros/arquivo.js');
const admin = await F('api/membros/admin.js');
const guarda = await F('_middleware.js');
const guardaM = await F('membros/_middleware.js');
const sair = await F('membros/sair.js');
const pagina = await F('membros/p/[slug].js');
const painel = await F('painel/_middleware.js');
const entrarAgencia = await F('api/entrar.js');

class KV {
  constructor() { this.m = new Map(); }
  async get(k, t) { const v = this.m.get(k); if (v == null) return null; return t === 'json' ? JSON.parse(v) : v; }
  async put(k, v, o = {}) { this.m.set(k, typeof v === 'string' ? v : JSON.stringify(v)); if (o.expirationTtl) this.ttl = { ...(this.ttl || {}), [k]: o.expirationTtl }; }
  async delete(k) { this.m.delete(k); }
  async list({ prefix = '' } = {}) { return { keys: [...this.m.keys()].filter(k => k.startsWith(prefix)).map(name => ({ name })), list_complete: true }; }
}
const ASSETS = { fetch: async u => { const p = decodeURIComponent(new URL(u).pathname); const f = path.join(RAIZ, p); if (!f.startsWith(RAIZ) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) return new Response('nf', { status: 404 }); return new Response(fs.readFileSync(f)); } };
const env = { CONTAS: new KV(), SEGREDO: 'segredo-de-teste-' + Math.random(), CODIGOS: '{}', HUBLA_TOKEN: 'token-hubla-de-teste-123', ASSETS };

const ORIG = 'https://lindsonalmeida.pages.dev';
const req = (p, o = {}) => new Request(ORIG + p, o);
const cookieDe = r => { const c = r.headers.get('Set-Cookie') || ''; return c.split(';')[0]; };

// payload do membro.md (Pagamento Único), com o ID do produto trocado por um ID do MAPA_HUBLA
const idKit = Object.keys(M.MAPA_HUBLA).find(k => M.MAPA_HUBLA[k] === 'kit-mes-pronto');
const idWpp = Object.keys(M.MAPA_HUBLA).find(k => M.MAPA_HUBLA[k] === 'kit-whatsapp-que-fecha');
const evento = (type, prodId, extra = {}) => ({
  type,
  event: {
    product: { id: prodId, name: 'Produto' },
    products: [{ id: prodId, name: 'Produto', offers: [{ id: 'of1', name: 'Principal', cohorts: [{ id: '3a96c85e-cf82-4236-b242-7431f405c521' }] }] }],
    subscription: { id: 'e144be20-01d8-4fdc-9eb7-5ca255035c4b', sellerId: 'O4fg', payerId: 'Yf7A', type: 'one_time', status: type.endsWith('added') ? 'active' : 'inactive', billingCycleMonths: 1, credits: 31, paymentMethod: 'credit_card', autoRenew: true, freeTrial: false, activatedAt: '2024-03-28T15:46:46.839Z', modifiedAt: '2024-03-28T15:46:47.436Z', createdAt: '2024-03-28T15:46:47.436Z', version: 4, ...extra },
    user: { id: 'Yf7A', firstName: 'John', lastName: 'Doe', document: '08351973955', email: 'John.Doe@hub.la', phone: '+5511988646782' },
  },
  version: '2.0.0',
});
const posta = (corpo, h = {}) => hubla.onRequestPost({ request: req('/api/hubla', { method: 'POST', headers: { 'content-type': 'application/json', 'x-hubla-token': env.HUBLA_TOKEN, ...h }, body: JSON.stringify(corpo) }), env });
const pj = (p, corpo, cookie) => req(p, { method: 'POST', headers: { 'Content-Type': 'application/json', ...(cookie ? { Cookie: cookie } : {}) }, body: JSON.stringify(corpo) });

let ok = 0, falhou = 0;
async function caso(nome, fn) { try { await fn(); ok++; console.log('  ok   ' + nome); } catch (e) { falhou++; console.log('  FALHOU ' + nome + ' → ' + e.message); } }
const espera = (c, m) => { if (!c) throw new Error(m || 'esperado verdadeiro'); };
const rec = async () => env.CONTAS.get('membro:john.doe@hub.la', 'json');

console.log('Área de membros · testes (' + RAIZ + ')\n');
console.log('Webhook /api/hubla');
await caso('token errado → 401 e nada gravado', async () => {
  const r = await posta(evento('customer.member_added', idKit), { 'x-hubla-token': 'errado', 'x-hubla-idempotency': 'i0' });
  espera(r.status === 401, 'status ' + r.status); espera(!(await rec()));
});
await caso('sem token → 401', async () => {
  const r = await hubla.onRequestPost({ request: req('/api/hubla', { method: 'POST', body: '{}' }), env }); espera(r.status === 401);
});
await caso('acesso concedido → libera kit-mes-pronto, CPF só em hash, telefone só 4 dígitos', async () => {
  const r = await posta(evento('customer.member_added', idKit), { 'x-hubla-idempotency': 'i1' });
  espera(r.status === 200, 'status ' + r.status);
  const m = await rec(); espera(m && m.produtos['kit-mes-pronto'].ativo, 'não liberou');
  const bruto = env.CONTAS.m.get('membro:john.doe@hub.la');
  espera(!bruto.includes('08351973955') && !bruto.includes('988646782'), 'CPF ou telefone em texto');
  espera(m.tel4 === '6782' && m.docHash && m.docHash.hash.length === 64 && m.nome === 'John Doe');
  espera(env.CONTAS.ttl[[...env.CONTAS.m.keys()].find(k => k.startsWith('hubla:idem:'))] === 30 * 86400, 'TTL 30 dias');
});
await caso('evento repetido (mesmo x-hubla-idempotency) → 200 repetido, sem reprocessar', async () => {
  const antes = env.CONTAS.m.get('membro:john.doe@hub.la');
  const r = await posta(evento('customer.member_added', idKit), { 'x-hubla-idempotency': 'i1' }); const j = await r.json();
  espera(r.status === 200 && j.repetido === true); espera(env.CONTAS.m.get('membro:john.doe@hub.la') === antes);
});
await caso('produto que não está no MAPA_HUBLA → 200 ignorado', async () => {
  const r = await posta(evento('customer.member_added', 'id-desconhecido'), { 'x-hubla-idempotency': 'i2' }); const j = await r.json();
  espera(r.status === 200 && j.ignorado); espera(Object.keys((await rec()).produtos).length === 1);
});
await caso('outro tipo de evento → 200 ignorado', async () => {
  const r = await posta({ type: 'invoice.created', event: {} }, { 'x-hubla-idempotency': 'i3' }); espera(r.status === 200 && (await r.json()).ignorado);
});
await caso('JSON inválido → 400', async () => {
  const r = await hubla.onRequestPost({ request: req('/api/hubla', { method: 'POST', headers: { 'x-hubla-token': env.HUBLA_TOKEN }, body: '{x' }), env }); espera(r.status === 400);
});

console.log('\nPrimeiro acesso e login');
await caso('primeiro acesso com CPF errado → 401 genérico', async () => {
  const r = await primeiro.onRequestPost({ request: pj('/api/membros/primeiro', { email: 'john.doe@hub.la', cpf: '11111111111', senha: 'senhaforte1' }), env });
  espera(r.status === 401 && /Não encontramos/.test((await r.json()).erro));
});
await caso('primeiro acesso de e-mail sem compra → mesma mensagem 401', async () => {
  const r = await primeiro.onRequestPost({ request: pj('/api/membros/primeiro', { email: 'ninguem@x.com', cpf: '08351973955', senha: 'senhaforte1' }), env });
  espera(r.status === 401 && /Não encontramos/.test((await r.json()).erro));
});
await caso('primeiro acesso com senha curta → 400', async () => {
  const r = await primeiro.onRequestPost({ request: pj('/api/membros/primeiro', { email: 'john.doe@hub.la', cpf: '083.519.739-55', senha: '123' }), env }); espera(r.status === 400);
});
let sessao;
await caso('primeiro acesso certo (CPF com pontos) → cria senha e cookie lm_membro', async () => {
  const r = await primeiro.onRequestPost({ request: pj('/api/membros/primeiro', { email: 'JOHN.DOE@hub.la ', cpf: '083.519.739-55', senha: 'senhaforte1' }), env });
  espera(r.status === 200, 'status ' + r.status + ' ' + JSON.stringify(await r.clone().json()));
  const c = r.headers.get('Set-Cookie'); espera(/^lm_membro=/.test(c) && /HttpOnly/.test(c) && /Secure/.test(c) && /SameSite=Lax/.test(c) && /Max-Age=2592000/.test(c), c);
  sessao = cookieDe(r);
});
await caso('primeiro acesso de novo (senha já criada) → 409', async () => {
  const r = await primeiro.onRequestPost({ request: pj('/api/membros/primeiro', { email: 'john.doe@hub.la', cpf: '08351973955', senha: 'outrasenha1' }), env }); espera(r.status === 409);
});
await caso('login com senha errada → 401 genérico', async () => {
  const r = await entrar.onRequestPost({ request: pj('/api/membros/entrar', { email: 'john.doe@hub.la', senha: 'errada123' }), env }); espera(r.status === 401);
});
await caso('login certo → 200 e cookie', async () => {
  const r = await entrar.onRequestPost({ request: pj('/api/membros/entrar', { email: 'john.doe@hub.la', senha: 'senhaforte1' }), env });
  espera(r.status === 200 && /^lm_membro=/.test(r.headers.get('Set-Cookie'))); sessao = cookieDe(r);
});
await caso('GET /api/membros/eu → {nome, produtos:[kit-mes-pronto]}', async () => {
  const r = await eu.onRequestGet({ request: req('/api/membros/eu', { headers: { Cookie: sessao } }), env }); const j = await r.json();
  espera(r.status === 200 && j.nome === 'John' && JSON.stringify(j.produtos) === '["kit-mes-pronto"]', JSON.stringify(j));
  espera(!JSON.stringify(j).includes('docHash') && !JSON.stringify(j).includes('senha'));
});
await caso('cookie falsificado → 401', async () => {
  const falso = sessao.replace(/.$/, c => (c === 'a' ? 'b' : 'a'));
  const r = await eu.onRequestGet({ request: req('/api/membros/eu', { headers: { Cookie: falso } }), env }); espera(r.status === 401);
});
await caso('cookie da agência não abre a área de membros', async () => {
  const r = await eu.onRequestGet({ request: req('/api/membros/eu', { headers: { Cookie: 'central=admin.9999999999999.eA.abc' } }), env }); espera(r.status === 401);
});
await caso('10 senhas erradas → bloqueio de 15 min (429), mesmo com a senha certa', async () => {
  env.CONTAS.m.set('membro:alvo@x.com', JSON.stringify({ email: 'alvo@x.com', senha: await lib.hashSenha('certa1234'), sv: 1, produtos: {} }));
  for (let i = 0; i < 10; i++) await entrar.onRequestPost({ request: pj('/api/membros/entrar', { email: 'alvo@x.com', senha: 'x' + i }), env });
  const r = await entrar.onRequestPost({ request: pj('/api/membros/entrar', { email: 'alvo@x.com', senha: 'certa1234' }), env }); espera(r.status === 429, 'status ' + r.status);
});

console.log('\nDownloads e páginas');
const baixa = (p, f, cookie) => arquivo.onRequestGet({ request: req(`/api/membros/arquivo?p=${p}&f=${encodeURIComponent(f)}`, { headers: cookie ? { Cookie: cookie } : {} }), env });
await caso('baixar arquivo do produto comprado → 200 attachment, private no-store, PDF inteiro', async () => {
  const r = await baixa('kit-mes-pronto', 'Kit-Mes-Pronto.pdf', sessao);
  espera(r.status === 200, 'status ' + r.status); espera(/attachment/.test(r.headers.get('Content-Disposition')) && r.headers.get('Cache-Control') === 'private, no-store' && r.headers.get('Content-Type') === 'application/pdf');
  const b = Buffer.from(await r.arrayBuffer()); espera(b.length === fs.statSync(path.join(RAIZ, 'membros-arquivos/kit-mes-pronto/Kit-Mes-Pronto.pdf')).size && b.slice(0, 4).toString() === '%PDF');
});
await caso('todos os arquivos da lista existem em membros-arquivos/', async () => {
  for (const [s, l] of Object.entries(M.ARQUIVOS)) for (const a of l) espera(fs.existsSync(path.join(RAIZ, 'membros-arquivos', s, a.f)), 'falta ' + s + '/' + a.f);
});
await caso('baixar arquivo de produto NÃO comprado → 403', async () => { const r = await baixa('kit-whatsapp-que-fecha', 'Kit-WhatsApp-que-Fecha.pdf', sessao); espera(r.status === 403, 'status ' + r.status); });
await caso('baixar sem sessão → 401', async () => { const r = await baixa('kit-mes-pronto', 'Kit-Mes-Pronto.pdf'); espera(r.status === 401); });
await caso('nome fora da lista / caminho ../ → 404', async () => {
  for (const f of ['../../functions/_codigos.js', 'x.pdf', '../kit-whatsapp-que-fecha/atalhos.txt']) { const r = await baixa('kit-mes-pronto', f, sessao); espera(r.status === 404, f + ' → ' + r.status); }
  const r = await baixa('..', 'Kit-Mes-Pronto.pdf', sessao); espera(r.status === 404);
});
await caso('página /membros/p/kit-mes-pronto lista os 3 arquivos', async () => {
  const r = await pagina.onRequestGet({ request: req('/membros/p/kit-mes-pronto', { headers: { Cookie: sessao } }), env, params: { slug: 'kit-mes-pronto' } });
  const h = await r.text(); espera(r.status === 200 && (h.match(/class="arq"/g) || []).length === 3);
});
await caso('página de produto não comprado → volta para a área com ?comprar=', async () => {
  const r = await pagina.onRequestGet({ request: req('/membros/p/kit-prospeccao', { headers: { Cookie: sessao } }), env, params: { slug: 'kit-prospeccao' } });
  espera(r.status === 302 && r.headers.get('Location') === ORIG + '/membros/area?comprar=kit-prospeccao#loja', r.headers.get('Location'));
});
await caso('slug inválido na página → área (sem redirecionamento aberto)', async () => {
  const r = await pagina.onRequestGet({ request: req('/membros/p/x', { headers: { Cookie: sessao } }), env, params: { slug: '//evil.com' } });
  espera(r.status === 302 && r.headers.get('Location') === ORIG + '/membros/area');
});

console.log('\nGuardas (middleware)');
const nx = async () => new Response('estatico', { status: 200 });
const g = async p => (await guarda.onRequest({ request: req(p), env: { ...env }, next: nx })).status;
await caso('/membros-arquivos/* e variações → 404', async () => {
  for (const p of ['/membros-arquivos/kit-mes-pronto/Kit-Mes-Pronto.pdf', '/membros-arquivos/', '/MEMBROS-ARQUIVOS/kit-mes-pronto/Kit-Mes-Pronto.pdf', '/membros%2Darquivos/kit-mes-pronto/Kit-Mes-Pronto.pdf', '//membros-arquivos/kit-mes-pronto/atalhos.csv'])
    espera((await g(p)) === 404, p);
});
await caso('/produtos/* (entregas e fontes) → 404, /produtos/landing/* continua aberto', async () => {
  for (const p of ['/produtos/kit-mes-pronto/entrega/Kit-Mes-Pronto.pdf', '/produtos/kit-prospeccao/100-Mensagens-Kit-Prospeccao.txt', '/produtos', '/produtos/landingx/a']) espera((await g(p)) === 404, p);
  espera((await g('/produtos/landing/kit-mes-pronto/index.html')) === 200);
});
await caso('rotas da agência e da área continuam passando', async () => {
  for (const p of ['/', '/painel/admin', '/api/entrar', '/api/criar', '/membros/', '/membros/img/c16.jpg', '/api/hubla']) espera((await g(p)) === 200, p);
  espera((await g('/dados/jaci.json')) === 404 && (await g('/functions/_lib.js')) === 404);
});
const gm = async (p, cookie) => guardaM.onRequest({ request: req(p, { headers: cookie ? { Cookie: cookie } : {} }), env, next: nx });
await caso('/membros/area sem sessão → /membros/; com sessão → abre com no-store', async () => {
  let r = await gm('/membros/area'); espera(r.status === 302 && r.headers.get('Location') === ORIG + '/membros/');
  r = await gm('/membros/area', sessao); espera(r.status === 200 && r.headers.get('Cache-Control') === 'private, no-store');
});
await caso('/membros/ com sessão → vai para a área; sem sessão → tela de acesso', async () => {
  let r = await gm('/membros/', sessao); espera(r.status === 302 && r.headers.get('Location') === ORIG + '/membros/area');
  r = await gm('/membros/'); espera(r.status === 200);
  r = await gm('/membros/img/c16.jpg'); espera(r.status === 200);
});

console.log('\nAdmin e revogação');
// conta admin da agência (mesmo formato de /api/criar)
env.CONTAS.m.set('conta:lindson@x.com', JSON.stringify({ nome: 'Lindson', email: 'lindson@x.com', cli: 'admin', ...(await lib.hashSenha('adminsenha1')), criada: new Date().toISOString() }));
env.CONTAS.m.set('conta:cliente@x.com', JSON.stringify({ nome: 'Cli', email: 'cliente@x.com', cli: 'jaci', ...(await lib.hashSenha('clisenha12')), criada: new Date().toISOString() }));
const cAdm = cookieDe(await entrarAgencia.onRequestPost({ request: pj('/api/entrar', { email: 'lindson@x.com', senha: 'adminsenha1' }), env }));
const cCli = cookieDe(await entrarAgencia.onRequestPost({ request: pj('/api/entrar', { email: 'cliente@x.com', senha: 'clisenha12' }), env }));
await caso('login da agência continua funcionando (admin e cliente)', async () => { espera(/^central=admin\./.test(cAdm) && /^central=jaci\./.test(cCli)); });
await caso('painel da agência: cliente não abre /painel/membros, admin abre', async () => {
  let r = await painel.onRequest({ request: req('/painel/membros', { headers: { Cookie: cCli } }), env, next: nx }); espera(r.status === 302);
  r = await painel.onRequest({ request: req('/painel/membros', { headers: { Cookie: cAdm } }), env, next: nx }); espera(r.status === 200);
});
await caso('admin: cliente da agência e membro → 403; admin lista sem CPF/senha', async () => {
  espera((await admin.onRequestGet({ request: req('/api/membros/admin', { headers: { Cookie: cCli } }), env })).status === 403);
  espera((await admin.onRequestGet({ request: req('/api/membros/admin', { headers: { Cookie: sessao } }), env })).status === 403);
  const r = await admin.onRequestGet({ request: req('/api/membros/admin', { headers: { Cookie: cAdm } }), env }); const t = await r.text();
  espera(r.status === 200 && t.includes('john.doe@hub.la') && !t.includes('docHash') && !t.includes('"hash"'));
});
await caso('admin: POST de outra origem → 403', async () => {
  const r = await admin.onRequestPost({ request: req('/api/membros/admin', { method: 'POST', headers: { Cookie: cAdm, 'Content-Type': 'application/json', Origin: 'https://evil.com' }, body: JSON.stringify({ acao: 'liberar', email: 'a@b.com', produto: 'kit-prospeccao' }) }), env });
  espera(r.status === 403);
});
await caso('admin libera kit-prospeccao à mão → membro baixa a planilha', async () => {
  const r = await admin.onRequestPost({ request: pj('/api/membros/admin', { acao: 'liberar', email: 'john.doe@hub.la', produto: 'kit-prospeccao' }, cAdm), env });
  espera(r.status === 200, 'status ' + r.status);
  espera((await baixa('kit-prospeccao', 'Planilha-Cadencia-Kit-Prospeccao.xlsx', sessao)).status === 200);
});
await caso('admin cria venda manual com CPF → primeiro acesso funciona', async () => {
  let r = await admin.onRequestPost({ request: pj('/api/membros/admin', { acao: 'liberar', email: 'maria@x.com', nome: 'Maria Silva', cpf: '529.982.247-25', produto: 'bio-que-vende' }, cAdm), env }); espera(r.status === 200);
  r = await primeiro.onRequestPost({ request: pj('/api/membros/primeiro', { email: 'maria@x.com', cpf: '52998224725', senha: 'mariasenha1' }), env }); espera(r.status === 200, 'status ' + r.status);
  const c = cookieDe(r); const j = await (await eu.onRequestGet({ request: req('/api/membros/eu', { headers: { Cookie: c } }), env })).json();
  espera(JSON.stringify(j.produtos) === '["bio-que-vende"]');
  const pg = await pagina.onRequestGet({ request: req('/membros/p/bio-que-vende', { headers: { Cookie: c } }), env, params: { slug: 'bio-que-vende' } });
  espera(/Em produção/.test(await pg.text()));
});
await caso('admin baixa qualquer arquivo para conferir', async () => { espera((await baixa('kit-whatsapp-que-fecha', 'atalhos.txt', cAdm)).status === 200); });
await caso('acesso removido (Hubla) → produto bloqueado na hora (download 403)', async () => {
  const r = await posta(evento('customer.member_removed', idKit, { version: 5, modifiedAt: '2024-04-01T00:00:00.000Z' }), { 'x-hubla-idempotency': 'i9' });
  espera(r.status === 200, 'status ' + r.status);
  const m = await rec(); espera(m.produtos['kit-mes-pronto'].ativo === false && m.produtos['kit-mes-pronto'].ate);
  espera((await baixa('kit-mes-pronto', 'Kit-Mes-Pronto.pdf', sessao)).status === 403);
});
await caso('"acesso concedido" atrasado (versão mais velha) não desfaz a remoção', async () => {
  const r = await posta(evento('customer.member_added', idKit, { version: 4 }), { 'x-hubla-idempotency': 'i10' }); espera(r.status === 200);
  espera((await rec()).produtos['kit-mes-pronto'].ativo === false);
});
await caso('compra nova (versão mais nova) libera de novo', async () => {
  await posta(evento('customer.member_added', idKit, { version: 6, modifiedAt: '2024-05-01T00:00:00.000Z' }), { 'x-hubla-idempotency': 'i11' });
  espera((await rec()).produtos['kit-mes-pronto'].ativo === true);
});
await caso('dois webhooks ao mesmo tempo (2 produtos) → os dois ficam liberados', async () => {
  const [a, b] = await Promise.all([
    posta({ ...evento('customer.member_added', idWpp, { id: 'sub-w' }), event: { ...evento('customer.member_added', idWpp, { id: 'sub-w' }).event, user: { ...evento('x', 'x').event.user, email: 'novo@x.com' } } }, { 'x-hubla-idempotency': 'c1' }),
    posta({ ...evento('customer.member_added', idKit, { id: 'sub-k' }), event: { ...evento('customer.member_added', idKit, { id: 'sub-k' }).event, user: { ...evento('x', 'x').event.user, email: 'novo@x.com' } } }, { 'x-hubla-idempotency': 'c2' }),
  ]);
  espera(a.status === 200 && b.status === 200);
  const m = await env.CONTAS.get('membro:novo@x.com', 'json'); espera(m.produtos['kit-whatsapp-que-fecha'].ativo && m.produtos['kit-mes-pronto'].ativo, JSON.stringify(m.produtos));
});
await caso('admin zera a senha → sessão antiga cai; sair invalida o cookie', async () => {
  const r0 = await entrar.onRequestPost({ request: pj('/api/membros/entrar', { email: 'maria@x.com', senha: 'mariasenha1' }), env }); const c = cookieDe(r0);
  const s = await sair.onRequest({ request: req('/membros/sair', { headers: { Cookie: c } }), env });
  espera(s.status === 302 && /Max-Age=0/.test(s.headers.get('Set-Cookie')));
  espera((await eu.onRequestGet({ request: req('/api/membros/eu', { headers: { Cookie: c } }), env })).status === 401, 'cookie continuou valendo depois de sair');
  espera((await eu.onRequestGet({ request: req('/api/membros/eu', { headers: { Cookie: sessao } }), env })).status === 200);
  await admin.onRequestPost({ request: pj('/api/membros/admin', { acao: 'zerar-senha', email: 'john.doe@hub.la' }, cAdm), env });
  espera((await eu.onRequestGet({ request: req('/api/membros/eu', { headers: { Cookie: sessao } }), env })).status === 401);
});
await caso('nenhum CPF, telefone completo ou senha em texto em todo o KV', async () => {
  const tudo = [...env.CONTAS.m.entries()].map(([k, v]) => k + v).join('\n');
  for (const s of ['08351973955', '52998224725', '988646782', 'senhaforte1', 'mariasenha1']) espera(!tudo.includes(s), s);
});

console.log(`\n${ok} certos, ${falhou} com falha`);
process.exit(falhou ? 1 : 0);
