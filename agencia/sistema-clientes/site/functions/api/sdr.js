// /api/sdr: aba SDR do painel do ADMINISTRADOR + extensão de prospecção (pedido do Lindson, 11/11/2026).
// Contatos: functions/_sdr.js (100 negócios do Brasil com nota de potencial >= 80). Status de cada um: KV "sdr:status" → {id: {etapa, canal, em, hist[]}}.
// Acesso: admin logado (cookie) OU extensão com "Authorization: Bearer <AUTOMACAO_TOKEN>" (o mesmo segredo de /api/automacao).
// GET  /api/sdr                 → { contatos: [...com etapa], etapas }
// GET  /api/sdr?lote=20         → { lote: os próximos 20 com etapa "novo" (maior nota primeiro) } (para a extensão)
// POST /api/sdr {id, acao:'enviado', canal:'instagram'|'whatsapp'} → sai da lista e entra na esteira (etapa "enviado")
// POST /api/sdr {id, acao:'etapa', etapa}                           → move na esteira
import { json, quemE, iguais } from '../_lib.js';
import { CONTATOS } from '../_sdr.js';
export const ETAPAS = ['novo', 'enviado', 'respondeu', 'reuniao', 'proposta', 'fechado', 'perdido'];
const CHAVE = 'sdr:status';
async function pode(request, env) {
  const t = env.AUTOMACAO_TOKEN || '', v = (request.headers.get('Authorization') || '').replace(/^Bearer\s+/i, '');
  if (t.length >= 24 && v.length > 0 && iguais(v, t)) return 'extensao';
  const q = await quemE(request, env); return q && q.cli === 'admin' ? 'admin' : null;
}
const junta = st => CONTATOS.map(c => ({ ...c, etapa: 'novo', ...(st[c.id] || {}) }));
export async function onRequestGet({ request, env }) {
  if (!env.CONTAS || !await pode(request, env)) return json({ erro: 'Sem acesso.' }, 401);
  const st = (await env.CONTAS.get(CHAVE, 'json')) || {}, todos = junta(st);
  const n = parseInt(new URL(request.url).searchParams.get('lote') || '', 10);
  if (n > 0) return json({ lote: todos.filter(c => c.etapa === 'novo').sort((a, b) => b.nota - a.nota).slice(0, Math.min(n, 20)) });
  return json({ contatos: todos, etapas: ETAPAS });
}
export async function onRequestPost({ request, env }) {
  const quem = env.CONTAS && await pode(request, env);
  if (!quem) return json({ erro: 'Sem acesso.' }, 401);
  let b; try { b = await request.json(); } catch (e) { return json({ erro: 'Dados inválidos.' }, 400); }
  if (!b || !CONTATOS.some(c => c.id === b.id)) return json({ erro: 'Contato não existe.' }, 404);
  let etapa;
  if (b.acao === 'enviado') { if (!['instagram', 'whatsapp'].includes(b.canal)) return json({ erro: 'Canal inválido.' }, 400); etapa = 'enviado'; }
  else if (b.acao === 'etapa' && ETAPAS.includes(b.etapa)) etapa = b.etapa;
  else return json({ erro: 'Ação inválida.' }, 400);
  const st = (await env.CONTAS.get(CHAVE, 'json')) || {}, at = st[b.id] || { hist: [] }, em = new Date().toISOString();
  at.hist = (at.hist || []).concat({ etapa, canal: b.canal || null, em, por: quem }).slice(-30);
  at.etapa = etapa; at.em = em; if (b.canal) at.canal = b.canal;
  if (etapa === 'enviado' && !at.enviadoEm) at.enviadoEm = em;
  if (etapa === 'novo') { delete at.canal; delete at.enviadoEm; }  // voltou para a lista: limpa o envio
  st[b.id] = at;
  await env.CONTAS.put(CHAVE, JSON.stringify(st));
  return json({ ok: true, id: b.id, ...at });
}
