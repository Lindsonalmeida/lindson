// Teste da distribuição do time de SDR (/api/sdr) com um KV falso em memória. Não manda WhatsApp.
// Uso: node testes/api-sdr.test.mjs [/caminho/CentralLindsonALmeida]   (padrão: /home/user/centrallindsonalmeida)
import assert from 'node:assert/strict';
const CENTRAL = process.argv[2] || '/home/user/centrallindsonalmeida';
const api = await import(CENTRAL + '/functions/api/sdr.js');
const { CONTATOS } = await import(CENTRAL + '/functions/_sdr.js');
const TOKEN = 'x'.repeat(32);
const kv = () => { const m = new Map(); return { m, get: async (k, t) => m.has(k) ? (t === 'json' ? JSON.parse(m.get(k)) : m.get(k)) : null, put: async (k, v) => { m.set(k, v); } }; };
const env = { CONTAS: kv(), SDR_TOKEN: TOKEN };
const req = (url, corpo, tk = TOKEN) => ({ request: new Request('https://x/api/sdr' + url, { method: corpo ? 'POST' : 'GET', headers: { Authorization: 'Bearer ' + tk, 'Content-Type': 'application/json' }, body: corpo ? JSON.stringify(corpo) : undefined }), env });
const get = async u => (await api.onRequestGet(req(u))).json();
const post = async b => { const r = await api.onRequestPost(req('', b)); return { s: r.status, j: await r.json() }; };
let ok = 0; const t = async (nome, f) => { await f(); ok++; console.log('ok', nome); };

await t('sem token = 401', async () => { assert.equal((await api.onRequestGet(req('', null, 'errado'))).status, 401); });
await t('numero inválido = 400', async () => { assert.equal((await api.onRequestGet(req('?lote=1&numero=sdr9'))).status, 400); assert.equal((await post({ acao: 'robo', numero: '../x' })).s, 400); });
await t('robôs ligados', async () => { for (const n of api.NUMEROS) assert.equal((await post({ acao: 'robo', numero: n, estado: 'Trabalhando', enviados: 0, limite: 20 })).s, 200); });
await t('nenhum lead repetido entre os 3 números (30 rodadas cada, intercaladas)', async () => {
  const visto = new Map();
  for (let i = 0; i < 30; i++) for (const n of api.NUMEROS) {
    const { lote } = await get('?lote=1&numero=' + n);
    for (const c of lote) { assert.ok(!visto.has(c.id), `${c.id} saiu para ${visto.get(c.id)} e ${n}`); visto.set(c.id, n); assert.equal((await post({ id: c.id, acao: 'enviado', canal: 'whatsapp', numero: n })).s, 200); }
  }
  const por = {}; for (const n of visto.values()) por[n] = (por[n] || 0) + 1; console.log('   distribuição', por, 'de', CONTATOS.filter(c => c.wa).length);
  assert.equal(Object.keys(por).length, api.NUMEROS.length);
});
await t('reserva: mesmo número pedindo 2x sem enviar não pega o mesmo lead', async () => {
  const a = (await get('?lote=1&numero=sdr1')).lote[0], b = (await get('?lote=1&numero=sdr1')).lote[0];
  if (a && b) assert.notEqual(a.id, b.id);
});
await t('status guarda qual número enviou', async () => {
  const { contatos } = await get(''); const e = contatos.filter(c => c.etapa === 'enviado');
  assert.ok(e.length > 0 && e.every(c => api.NUMEROS.includes(c.sdr)));
});
await t('(28/11) robô não devolve lead enviado para "novo"', async () => {
  const { contatos } = await get(''); const e = contatos.find(c => c.etapa === 'enviado');
  const r = await post({ id: e.id, acao: 'etapa', etapa: 'novo', numero: e.sdr }); assert.equal(r.s, 409); // já enviado: bloqueado (devolver reserva nunca enviada continua permitido)
  const depois = (await get('')).contatos.find(c => c.id === e.id); assert.equal(depois.etapa, 'enviado');
});
await t('(28/11) lead com "enviado" no hist nunca sai no lote, mesmo com reserva vencida mais nova em outro chip', async () => {
  const c = { id: 'x1', nome: 'Vereador Teste', nicho: 'vereador', wa: '5598900000000' };
  const j = api.junta([{ st: { x1: { etapa: 'enviado', em: '2026-11-24T10:00:00Z', hist: [{ etapa: 'enviado' }] } }, sdr: 'sdr1' }, { st: { x1: { etapa: 'reservado', ate: '2026-11-27T10:00:00Z', em: '2026-11-27T09:45:00Z' } }, sdr: 'sdr3' }], [c])[0];
  assert.equal(api.livre(j, Date.now()), false);
  const k = api.junta([{ st: { x1: { etapa: 'novo', em: '2026-11-27T15:47:00Z', hist: [{ etapa: 'enviado' }, { etapa: 'novo' }] } }, sdr: 'sdr1' }], [c])[0];
  assert.equal(api.livre(k, Date.now()), false);
});
await t('pausa por número', async () => {
  await post({ acao: 'pausa', numero: 'sdr2', pausado: true });
  const r = await get('?lote=1&numero=sdr2'); assert.equal(r.pausado, true); assert.equal(r.lote.length, 0);
  const { robos } = await get('?robo=1'); assert.equal(robos.sdr2.pausado, true); assert.ok(!robos.sdr1.pausado);
  assert.equal((await post({ acao: 'robo', numero: 'sdr2', estado: 'x' })).j.pausado, true);
});
await t('compatível: sdr:robo antigo vira sdr1', async () => {
  const e2 = { CONTAS: kv(), SDR_TOKEN: TOKEN }; await e2.CONTAS.put('sdr:robo', JSON.stringify({ visto: '2026-11-20T10:00:00Z', pausado: true }));
  const r = await (await api.onRequestGet({ request: new Request('https://x/api/sdr?robo=1', { headers: { Authorization: 'Bearer ' + TOKEN } }), env: e2 })).json();
  assert.equal(r.robos.sdr1.pausado, true); assert.equal(r.robo.pausado, true);
});
await t('(28/11) lead já enviado não volta para "novo" nem pela chave antiga', async () => {
  const { contatos } = await get(''); const c = contatos.find(x => x.etapa === 'enviado');
  await new Promise(r => setTimeout(r, 5)); assert.equal((await post({ id: c.id, acao: 'etapa', etapa: 'novo' })).s, 409);
  assert.equal((await get('')).contatos.find(x => x.id === c.id).etapa, 'enviado');
});
await t('variações seguem o padrão (saudação e pergunta mudam, dor igual)', async () => {
  const m = CONTATOS[0].msg, v = api.NUMEROS.map(n => api.varia(m, n));
  assert.equal(new Set(v).size, api.NUMEROS.length); for (const x of v) { assert.equal(x.split('\n')[1], m.split('\n')[1]); assert.ok(!/vi que|parece que|gargalo/i.test(x)); assert.ok(x.length <= 300); }
});
await t('lead sem WhatsApp nunca entra no lote', async () => { const s = api.escolhe(CONTATOS.map(c => ({ ...c, etapa: 'novo' })), 'sdr1', {}, Date.now(), 999); assert.ok(s.every(c => c.wa)); });
await t('fallback: chip fora do NE sem lead livre passa a receber do Nordeste, sem repetir (23/11/2026)', async () => {
  const agora = Date.now(), v = new Date(agora).toISOString(), robos = { sdr1: { visto: v, regiao: 'NE' }, sdr2: { visto: v, regiao: 'FORA_NE' }, sdr3: { visto: v, regiao: 'NE' } };
  const base = CONTATOS.filter(c => c.wa).map(c => ({ ...c, etapa: 'novo' })), neLivres = base.filter(c => api.ehNE(c));
  // 1) com lead fora do NE livre: sdr2 só pega fora do NE, e os do NE ficam com sdr1/sdr3
  const fora = [{ id: 'teste-sp-1', wa: '5511999990001', cidade: 'São Paulo / SP', etapa: 'novo' }];
  const s2 = api.escolhe(base.concat(fora), 'sdr2', robos, agora, 999); assert.ok(s2.length >= 1 && s2.every(c => !api.ehNE(c)));
  // 2) sem lead fora do NE livre: sdr2 recebe NE; os três juntos cobrem todos os NE livres sem repetir
  const todos = base.map(c => api.ehNE(c) ? c : { ...c, etapa: 'enviado' }), vistos = new Map();
  for (const n of api.NUMEROS) for (const c of api.escolhe(todos, n, robos, agora, 9999)) { assert.ok(api.ehNE(c)); assert.ok(!vistos.has(c.id), `${c.id} repetiu`); vistos.set(c.id, n); }
  assert.equal(vistos.size, neLivres.length);
  if (neLivres.length >= 6) assert.ok([...vistos.values()].includes('sdr2'), 'sdr2 não recebeu lead do NE');
  console.log('   fallback: NE livres', neLivres.length, 'sdr2 recebeu', [...vistos.values()].filter(n => n === 'sdr2').length);
});
await t('SDR só de políticos (24/11): lote e fila sem varejo', async () => {
  const pol = await import(CENTRAL + '/functions/_sdr_fluxo.js');
  const ehPol = c => pol.segmento(c.nicho || '', c.nome || '', c.ig || '', c.bio || '', c.tag || '', c.msg || '', c.motivo || '') === 'politica';
  const l = (await get('?lote=20')).lote; assert.ok(l.length > 0); assert.ok(l.every(ehPol), 'lote com varejo');
  assert.ok((await get('')).contatos.every(ehPol), 'fila com varejo');
  assert.equal(api.junta([{ st: {}, sdr: null }], [{ id: 'pz', nome: 'Pizzaria X', nicho: 'pizzaria', wa: '5598900000000' }]).length, 0);
});
console.log(`\n${ok} testes passaram.`);
