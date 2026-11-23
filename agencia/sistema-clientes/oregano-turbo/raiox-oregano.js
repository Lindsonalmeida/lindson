// /api/raiox-oregano: recebe o formulário PÚBLICO do Raio-X automático (oreganoturbo.pages.dev/raio-x) e grava o lead
// no SDR da Orégano (KV "sdr:oregano:leads"), com fonte "raio-x", a nota e as respostas. Sem segredo no cliente.
// Proteções: só aceita origem do site da Orégano, limite por IP (5/hora), campos validados, WhatsApp celular e @ obrigatórios.
// Funil v2 aprovado pelo Lindson em 23/11/2026 (conta Leandro).
const KL = 'sdr:oregano:leads', KS = 'sdr:oregano:status';
const OK_ORIG = /^https:\/\/([a-z0-9-]+\.)?oreganoturbo\.pages\.dev$/;
const cors = o => ({ 'Access-Control-Allow-Origin': o, 'Access-Control-Allow-Methods': 'POST, OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type', 'Vary': 'Origin' });
const resp = (o, s, h) => new Response(JSON.stringify(o), { status: s, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store', ...h } });
const origem = r => { const o = r.headers.get('Origin') || ''; return OK_ORIG.test(o) ? o : ''; };
export function onRequestOptions({ request }) { const o = origem(request); return new Response(null, { status: o ? 204 : 403, headers: o ? cors(o) : {} }); }
export async function onRequestPost({ request, env }) {
  const o = origem(request); if (!o) return resp({ erro: 'Origem não permitida.' }, 403, {});
  const h = cors(o);
  if (!env.CONTAS) return resp({ erro: 'Indisponível.' }, 503, h);
  const ip = request.headers.get('CF-Connecting-IP') || 'x', kr = 'raiox:ip:' + ip + ':' + new Date().toISOString().slice(0, 13);
  const n = +(await env.CONTAS.get(kr) || 0); if (n >= 5) return resp({ erro: 'Muitos envios. Tente mais tarde.' }, 429, h);
  await env.CONTAS.put(kr, String(n + 1), { expirationTtl: 3700 });
  let b; try { b = await request.json(); } catch (e) { return resp({ erro: 'Dados inválidos.' }, 400, h); }
  if (b.site) return resp({ ok: true }, 200, h); // campo isca contra robô
  const ig = String(b.ig || '').trim().replace(/^@/, '').toLowerCase().replace(/[^a-z0-9._]/g, '').slice(0, 30);
  let wa = String(b.wa || '').replace(/\D/g, ''); if (wa.length === 11) wa = '55' + wa;
  if (!ig || !/^55\d{2}9\d{8}$/.test(wa)) return resp({ erro: 'Confira o @ e o WhatsApp (celular com DDD).' }, 400, h);
  if (b.lgpd !== true) return resp({ erro: 'É preciso aceitar o uso dos dados.' }, 400, h);
  const nota = Math.max(0, Math.min(100, Math.round(+b.nota || 0)));
  const resps = {}; for (const [k, v] of Object.entries(b.respostas || {}).slice(0, 12)) resps[String(k).slice(0, 4)] = String(v).slice(0, 12);
  const ref = String(b.ref || '').replace(/[^A-Za-z0-9_\-]/g, '').slice(0, 30);
  const L = (await env.CONTAS.get(KL, 'json')) || [], em = new Date().toISOString();
  const i = L.findIndex(c => c.wa === wa || (c.ig || '').toLowerCase() === ig);
  const dado = { nome: String(b.nome || '').slice(0, 80), pizzaria: String(b.pizzaria || '').slice(0, 80), cidade: String(b.cidade || '').slice(0, 60), raiox: { nota, resps, ref, em } };
  if (i >= 0) { Object.assign(L[i], { raiox: dado.raiox }); }
  else L.push({ id: ig, ig, wa, dia: em.slice(0, 10), nome: dado.pizzaria || dado.nome, contato: dado.nome, cidade: dado.cidade, fonte: 'raio-x' + (ref ? ' · ' + ref : ''), motivo: `Raio-X automático: nota ${nota}/100`, raiox: dado.raiox });
  await env.CONTAS.put(KL, JSON.stringify(L));
  const st = (await env.CONTAS.get(KS, 'json')) || {}, id = i >= 0 ? L[i].id : ig, at = st[id] || { etapa: 'novo', hist: [] };
  at.hist = (at.hist || []).concat({ ev: 'raio-x', etapa: at.etapa, em, por: 'site', nota }).slice(-30); at.em = em; at.origem = 'raio-x'; st[id] = at;
  await env.CONTAS.put(KS, JSON.stringify(st));
  return resp({ ok: true }, 200, h);
}
