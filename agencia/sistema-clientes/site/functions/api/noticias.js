// /api/noticias?q=<busca>: notícias recentes (Google Notícias, com o Bing de reserva), guardadas por 3 horas no KV.
// Só para quem entrou na Central (não é um proxy aberto). Conta Lindson, 01/11/2026.
import { json, quemE, configurado, faltaConfig } from '../_lib.js';
const ent = s => s.replace(/<!\[CDATA\[([\s\S]*?)\]\]>/g, '$1').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;|&apos;/g, "'").replace(/&#(\d+);/g, (_, n) => String.fromCharCode(+n)).replace(/&amp;/g, '&').replace(/<[^>]+>/g, '').trim();
const tag = (x, t) => { const m = x.match(new RegExp(`<${t}[^>]*>([\\s\\S]*?)</${t}>`, 'i')); return m ? ent(m[1]) : ''; };
export function lerRss(xml) {
  return [...xml.matchAll(/<item>([\s\S]*?)<\/item>/gi)].map(m => {
    const x = m[1]; let titulo = tag(x, 'title'), fonte = tag(x, 'source') || tag(x, 'news:Source');
    if (fonte && titulo.endsWith(' - ' + fonte)) titulo = titulo.slice(0, -(fonte.length + 3));
    return { titulo, link: tag(x, 'link'), data: tag(x, 'pubDate'), fonte };
  }).filter(n => n.titulo && /^https?:\/\//.test(n.link)).slice(0, 25);
}
const FONTES = q => [
  `https://news.google.com/rss/search?q=${encodeURIComponent(q + ' when:30d')}&hl=pt-BR&gl=BR&ceid=BR:pt-419`,
  `https://www.bing.com/news/search?q=${encodeURIComponent(q)}&format=rss&setlang=pt-BR&cc=BR`];
export async function onRequestGet({ request, env }) {
  if (!configurado(env)) return faltaConfig();
  if (!await quemE(request, env)) return json({ erro: 'Entre na Central de novo.' }, 401);
  const q = (new URL(request.url).searchParams.get('q') || '').trim().slice(0, 80);
  if (q.length < 3) return json({ erro: 'Busca curta demais.' }, 400);
  const chave = 'news:' + q.toLowerCase(), guardado = await env.CONTAS.get(chave, 'json');
  if (guardado && Date.now() - guardado.em < 3 * 3600e3) return json(guardado);
  for (const url of FONTES(q)) {
    try {
      const r = await fetch(url, { headers: { 'User-Agent': 'Mozilla/5.0 (Central do Cliente)' }, cf: { cacheTtl: 1800 } });
      if (!r.ok) continue;
      const itens = lerRss(await r.text());
      if (itens.length) { const out = { q, em: Date.now(), itens }; await env.CONTAS.put(chave, JSON.stringify(out), { expirationTtl: 86400 }); return json(out); }
    } catch (e) {}
  }
  return guardado ? json(guardado) : json({ q, em: Date.now(), itens: [], erro: 'As fontes de notícias não responderam agora. Tente mais tarde.' });
}
