// /membros/p/<slug>: página do produto com os arquivos para baixar. Só para quem comprou; quem não comprou volta para a área com o "Comprar".
import { quemMembro, ativos, slugOk, NOMES, ARQUIVOS, esc, primeiroNome } from '../../_membros.js';
const INFO = {
  'kit-mes-pronto': ['KIT MÊS', 'PRONTO', 'O SEU MÊS DE INSTAGRAM PRONTO PARA GRAVAR', 'Comece pelo PDF: escolha o ritmo (leve ou completo), abra o calendário no domingo e grave a semana inteira de uma vez.'],
  'kit-whatsapp-que-fecha': ['WHATSAPP', 'QUE FECHA', 'DO PRIMEIRO OI ATÉ A VENDA', 'Leia o script de 6 passos no PDF e cadastre os atalhos como respostas rápidas no WhatsApp Business.'],
  'kit-prospeccao': ['KIT', 'PROSPECÇÃO', '100 MENSAGENS QUE ABREM CONVERSA', 'Escolha o seu nicho no arquivo das mensagens e acompanhe os 4 toques na planilha da cadência.'],
  'raio-x-do-perfil': ['RAIO-X', 'DO PERFIL', 'EU OLHO O SEU PERFIL E TE MOSTRO O CAMINHO', ''],
  'bio-que-vende': ['BIO QUE', 'VENDE', 'A SUA BIO PRONTA EM 15 MINUTOS', ''],
};
const ICONE = f => (f.split('.').pop() || '').toUpperCase();
export async function onRequestGet({ request, env, params }) {
  const u = new URL(request.url), slug = String(params.slug || '');
  if (!slugOk(slug)) return Response.redirect(u.origin + '/membros/area', 302);
  const q = await quemMembro(request, env);
  if (!q) return Response.redirect(u.origin + '/membros/', 302);
  if (!ativos(q.rec).includes(slug)) return Response.redirect(`${u.origin}/membros/area?comprar=${slug}#loja`, 302);
  const [l1, l2, slog, dica] = INFO[slug], arqs = ARQUIVOS[slug] || [];
  const lista = arqs.length
    ? arqs.map(a => `<a class="arq" href="/api/membros/arquivo?p=${encodeURIComponent(slug)}&amp;f=${encodeURIComponent(a.f)}" download><span class="ic">${esc(ICONE(a.f))}</span><span class="tx"><b>${esc(a.nome)}</b><small>${esc(a.f)}</small></span><span class="bx">Baixar ↓</span></a>`).join('')
    : `<div class="prod"><b>Em produção</b><p>Este produto é entregue pelo WhatsApp: o Lindson fala com você no número da compra. Assim que o material ficar pronto, ele aparece aqui também.</p></div>`;
  const html = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(NOMES[slug])} · Área de Membros</title><meta name="robots" content="noindex">
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
:root{--p:#07090C;--s:#0E1116;--l:#1C2028;--t:#F5F3EE;--ap:#9AA0A8;--am:#F5C518}
*{box-sizing:border-box;margin:0;padding:0}html,body{background:var(--p)}body{color:var(--t);font-family:Manrope,system-ui,sans-serif;min-height:100vh}a{color:inherit;text-decoration:none}
.nav{display:flex;align-items:center;gap:28px;padding:22px 56px}.logo{font:500 18px 'JetBrains Mono',monospace;letter-spacing:.5em}.logo b{color:var(--am)}
.nav a.l{font:600 15px Manrope;color:#c9cdd3}.nav .d{margin-left:auto;display:flex;gap:16px;align-items:center}.nav .d a{font:600 13px Manrope;color:var(--ap)}
.av{width:36px;height:36px;border-radius:50%;background:var(--am);color:#111;display:grid;place-items:center;font:800 13px Manrope}
.topo{display:grid;grid-template-columns:260px 1fr;gap:44px;align-items:center;padding:30px 56px 10px;max-width:1200px}
.po{aspect-ratio:2/3;border-radius:14px;background:#111 center/cover;box-shadow:0 30px 60px rgba(0,0,0,.5)}
.orig{font:500 13px 'JetBrains Mono',monospace;letter-spacing:.42em;color:#cfd3d8}.orig b{color:var(--am)}
h1{font:400 96px/.88 Anton,Impact,sans-serif;text-transform:uppercase;margin:18px 0 14px}h1 span{display:block;font-size:.62em}
.slog{font:600 13px 'JetBrains Mono',monospace;letter-spacing:.36em;color:#d7dbe0}.dica{font:500 16px/1.55 Manrope;color:#c3c8ce;max-width:560px;margin-top:20px}
.sel{display:inline-block;margin-top:18px;background:rgba(245,197,24,.12);color:var(--am);border-radius:99px;padding:5px 12px;font:700 11px 'JetBrains Mono',monospace;letter-spacing:.14em}
main{padding:30px 56px 70px;max-width:1200px}h2{font:700 20px Manrope;margin-bottom:14px}
.arq{display:grid;grid-template-columns:56px 1fr auto;gap:16px;align-items:center;background:var(--s);border:1px solid var(--l);border-radius:16px;padding:16px 18px;margin-bottom:12px;transition:border-color .2s,transform .2s}
.arq:hover{border-color:var(--am);transform:translateY(-2px)}.ic{width:56px;height:56px;border-radius:12px;background:#151a21;display:grid;place-items:center;font:700 12px 'JetBrains Mono',monospace;color:var(--am)}
.tx b{display:block;font:700 15px Manrope}.tx small{font:500 12px 'JetBrains Mono',monospace;color:var(--ap)}.bx{background:var(--am);color:#111;border-radius:99px;padding:10px 18px;font:800 14px Manrope;white-space:nowrap}
.prod{background:var(--s);border:1px solid var(--l);border-radius:16px;padding:24px}.prod b{font:800 18px Manrope;color:var(--am)}.prod p{font:500 15px/1.55 Manrope;color:#c3c8ce;margin-top:8px;max-width:620px}
.volta{display:inline-block;margin-top:26px;border:1px solid rgba(255,255,255,.3);border-radius:99px;padding:12px 22px;font:700 14px Manrope}
@media(max-width:900px){.nav{padding:16px}.nav a.l{display:none}.topo{grid-template-columns:1fr;padding:10px 16px;gap:22px}.po{max-width:220px}h1{font-size:62px}main{padding:24px 16px 60px}.arq{grid-template-columns:44px 1fr}.ic{width:44px;height:44px}.bx{grid-column:1/-1;text-align:center}}
</style></head><body>
<nav class="nav"><a class="logo" href="/membros/area">LINDSON<b>.</b></a><a class="l" href="/membros/area">Início</a><a class="l" href="/membros/area#meus">Meus produtos</a><a class="l" href="/membros/area#loja">Loja</a>
<div class="d"><a href="/membros/sair">Sair</a><div class="av">${esc(primeiroNome(q.rec.nome).slice(0, 2).toUpperCase() || 'EU')}</div></div></nav>
<section class="topo"><div class="po" style="background-image:url(/membros/img/p-${slug}.jpg)"></div>
<div><div class="orig">UM PRODUTO <b>LINDSON ALMEIDA</b></div><h1>${esc(l1)}<span>${esc(l2)}</span></h1><div class="slog">${esc(slog)}</div>
${dica ? `<p class="dica">${esc(dica)}</p>` : ''}<span class="sel">LIBERADO PARA VOCÊ</span></div></section>
<main><h2>${arqs.length ? 'Seus arquivos' : 'Como você recebe'}</h2>${lista}<a class="volta" href="/membros/area">← Voltar para a área</a></main>
</body></html>`;
  return new Response(html, { headers: { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'private, no-store', 'X-Robots-Tag': 'noindex' } });
}
