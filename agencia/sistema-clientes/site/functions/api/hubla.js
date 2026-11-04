// POST /api/hubla: webhook da Hubla (eventos "Acesso concedido" e "Acesso removido") → libera ou tira o produto na área de membros.
// Segurança: cabeçalho x-hubla-token conferido com o segredo HUBLA_TOKEN da Cloudflare (tempo constante); evento repetido
// (x-hubla-idempotency) é ignorado por 30 dias; eventos fora de ordem não desfazem um mais novo (version/modifiedAt).
// Nada pessoal vai para o log. Builder Squad · backend, 04/11/2026.
import { MAPA_HUBLA, SLUGS, chave, alteraMembro, hashSenha, iguais, iguaisSeguro, sha256, soDigitos, docOk, normEmail, emailOk, json } from '../_membros.js';

const TIPOS = { 'customer.member_added': 'liberar', 'customer.member_removed': 'remover' };
const MAX = 64 * 1024;
const log = (...a) => console.log('[hubla]', ...a);

// evento novo é mais velho que o que já foi aplicado neste produto?
function velho(p, ev) {
  if (!p) return false;
  if (ev.sub && p.sub === ev.sub && Number.isFinite(p.v) && Number.isFinite(ev.v)) return ev.v < p.v;
  return !!(p.at && ev.at && ev.at < p.at);
}

export async function onRequestPost({ request, env }) {
  if (!env.CONTAS || !env.HUBLA_TOKEN) { log('sem configuração (HUBLA_TOKEN ou KV)'); return json({ erro: 'não configurado' }, 503); }
  if (!(await iguaisSeguro(request.headers.get('x-hubla-token') || '', env.HUBLA_TOKEN))) { log('token recusado'); return json({ erro: 'não autorizado' }, 401); }

  const corpo = await request.text();
  if (corpo.length > MAX) return json({ erro: 'grande demais' }, 413);
  let b; try { b = JSON.parse(corpo); } catch (e) { return json({ erro: 'json inválido' }, 400); }
  if (!b || typeof b !== 'object') return json({ erro: 'json inválido' }, 400);

  const idem = String(request.headers.get('x-hubla-idempotency') || '').slice(0, 300);
  const kIdem = 'hubla:idem:' + (await sha256(idem || 'corpo|' + corpo));
  if (await env.CONTAS.get(kIdem)) { log('repetido', b.type); return json({ ok: true, repetido: true }); }

  const acao = TIPOS[b.type];
  if (!acao) { log('tipo ignorado', String(b.type).slice(0, 60)); return json({ ok: true, ignorado: true }); }
  const e = b.event || {}, u = e.user || {}, s = e.subscription || {};

  const ids = [...new Set([...(Array.isArray(e.products) ? e.products.map(p => p && p.id) : []), e.product && e.product.id].filter(x => typeof x === 'string'))];
  const slugs = [...new Set(ids.map(id => MAPA_HUBLA[id]).filter(x => SLUGS.includes(x)))];
  if (!slugs.length) { log('produto sem mapa', ids.join(',').slice(0, 200)); await env.CONTAS.put(kIdem, '1', { expirationTtl: 30 * 86400 }); return json({ ok: true, ignorado: true }); }

  const email = normEmail(u.email);
  if (!emailOk(email)) { log('evento sem e-mail válido'); return json({ erro: 'e-mail ausente' }, 422); }

  const agora = new Date().toISOString();
  const ev = { at: typeof s.modifiedAt === 'string' ? s.modifiedAt.slice(0, 40) : agora, v: Number.isFinite(s.version) ? s.version : null, sub: typeof s.id === 'string' ? s.id.slice(0, 80) : null };
  const nome = [u.firstName, u.lastName].filter(x => typeof x === 'string').join(' ').trim().slice(0, 80);
  const tel = soDigitos(u.phone), tel4 = tel.length >= 4 ? tel.slice(-4) : null;
  const doc = soDigitos(u.document);

  // hash do CPF calculado uma vez, fora da gravação (o sal é aleatório). Só enquanto a pessoa ainda não criou a senha.
  let docHash = null;
  if (acao === 'liberar' && docOk(doc)) {
    const cur = await env.CONTAS.get(chave(email), 'json');
    if (!cur || !cur.senha) {
      const mesmo = cur && cur.docHash && iguais((await hashSenha(doc, cur.docHash.sal)).hash, cur.docHash.hash);
      docHash = mesmo ? cur.docHash : await hashSenha(doc);
    }
  }

  const r = await alteraMembro(env, email, rec => {
    if (acao === 'remover') {
      if (!rec) return null; // não é membro: nada a tirar
      rec.produtos = rec.produtos || {};
      for (const sl of slugs) {
        const p = rec.produtos[sl] || {};
        if (velho(p, ev)) continue;
        rec.produtos[sl] = { ...p, ativo: false, ate: p.ativo === false && p.ate ? p.ate : agora, at: ev.at, v: ev.v, sub: ev.sub, origem: 'hubla' };
      }
      return rec;
    }
    rec = rec || { email, criado: agora, produtos: {}, sv: 0 };
    rec.produtos = rec.produtos || {};
    if (nome) rec.nome = nome;
    if (tel4) rec.tel4 = tel4;
    if (docHash && !rec.senha) rec.docHash = docHash;
    for (const sl of slugs) {
      const p = rec.produtos[sl] || {};
      if (velho(p, ev)) continue;
      const n = { ...p, ativo: true, desde: p.desde || agora, at: ev.at, v: ev.v, sub: ev.sub, origem: 'hubla' };
      delete n.ate;
      rec.produtos[sl] = n;
    }
    return rec;
  });
  if (!r.ok) { log('gravação não confirmada, a Hubla vai reenviar'); return json({ erro: 'tente de novo' }, 503); }

  await env.CONTAS.put(kIdem, '1', { expirationTtl: 30 * 86400 });
  log(acao, slugs.join(','));
  return json({ ok: true, acao, produtos: slugs });
}
