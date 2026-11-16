# Gera artigos de dúvidas (SEO local) para os clientes. Conta Leandro, 16/11/2026.
# python3 gerar.py  -> agencia/clientes/<cli>/artigos/<slug>.html e, se o repo do site existir, /dicas/<slug>/index.html + /dicas/ + sitemap + link na home
import json, html, os, re, sys, urllib.parse
sys.path.insert(0, os.path.dirname(__file__))
from conteudo import SF, JACI, RT, WF
AG = '/home/user/lindson/agencia/clientes'
CLI = [
 dict(k='desentupidora-sf', nome='Desentupidora SF', base='https://desentupidorasf.pages.dev', repo='/home/user/GruposSF', wa='5598920105710', arts=SF,
      cor='#0a2a6e', dest='#ff8a00', fundo='#f4f8ff', ink='#0d1b33', font='Montserrat', tipo='Plumber', cidade='São Luís',
      msg='Olá! Li o artigo do site e quero um orçamento.', rod='Desentupidora SF · São Luís, São José de Ribamar, Paço do Lumiar e Raposa'),
 dict(k='jaci-cunha', nome='Clínica Dra. Jaci Cunha', base='https://drajacicunha.pages.dev', repo='/home/user/drajacicunha', wa='559885672646', arts=JACI,
      cor='#6B1620', dest='#C9A46A', fundo='#FBFAF8', ink='#191614', font='Inter Tight', tipo='Dentist', cidade='Zé Doca',
      msg='Olá! Li o artigo do site e quero agendar uma avaliação.', rod='Clínica Dra. Jaci Cunha · Av. Militar, em frente à Praça do Viva, Zé Doca (MA) · Responsável técnica: Dra. Jaci Cunha, cirurgiã-dentista, CRO-MA 8514. Conteúdo educativo, não substitui consulta. Resultados variam de pessoa para pessoa.'),
 dict(k='rt-full-jobs', nome='Real Time · Full Jobs', base='https://realtimeslz.pages.dev', repo='/home/user/realtime', wa='5598991331727', arts=RT,
      cor='#0B0D12', dest='#2E9BFF', fundo='#F4F7FB', ink='#0B0D12', font='Geist', tipo='LocalBusiness', cidade='São Luís',
      msg='Olá! Li o artigo do site e quero um orçamento.', rod='Real Time · Full Jobs · Locação audiovisual, estúdio e produção de vídeo em São Luís (MA)'),
 dict(k='wf-celulares', nome='WF Celulares', base='https://wfcelulares.pages.dev', repo=None, wa='5598988271882', arts=WF,
      cor='#1D1D1F', dest='#2F6BFF', fundo='#F5F5F7', ink='#1D1D1F', font='Inter', tipo='Store', cidade='São Luís',
      msg='Olá! Li o artigo do site e quero saber mais.', rod='WF Celulares · iPhone lacrado e seminovo e assistência em São Luís (MA)'),
]

def bloco(b):
    if isinstance(b, tuple):
        return '<ul>' + ''.join(f'<li>{html.escape(i)}</li>' for i in b[1]) + '</ul>'
    return f'<p>{html.escape(b)}</p>'

def texto(a):
    t = ' '.join(a['intro'] + [a['fim']] + [p + ' ' + r for p, r in a['faq']])
    for h, bs in a['secoes']:
        t += ' ' + h + ' ' + ' '.join(b if isinstance(b, str) else ' '.join(b[1]) for b in bs)
    return t

def pagina(c, a, outros):
    url = f"{c['base']}/dicas/{a['slug']}/"
    wa = f"https://wa.me/{c['wa']}?text=" + urllib.parse.quote(c['msg'] + ' (' + a['h1'] + ')')
    serv_url = a['servico'][0] if a['servico'][0].startswith('http') else c['base'] + a['servico'][0]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": a['h1'], "description": a['desc'], "inLanguage": "pt-BR", "mainEntityOfPage": url,
         "datePublished": "2026-11-16", "author": {"@type": "Organization", "name": c['nome']},
         "publisher": {"@type": c['tipo'], "name": c['nome'], "url": c['base'] + '/', "telephone": '+' + c['wa'],
                       "address": {"@type": "PostalAddress", "addressLocality": c['cidade'], "addressRegion": "MA", "addressCountry": "BR"}}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": p, "acceptedAnswer": {"@type": "Answer", "text": r}} for p, r in a['faq']]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Início", "item": c['base'] + '/'},
            {"@type": "ListItem", "position": 2, "name": "Dicas", "item": c['base'] + '/dicas/'},
            {"@type": "ListItem", "position": 3, "name": a['h1'], "item": url}]}]}
    corpo = ''.join(f'<h2>{html.escape(h)}</h2>' + ''.join(bloco(b) for b in bs) for h, bs in a['secoes'])
    faq = ''.join(f'<details><summary>{html.escape(p)}</summary><p>{html.escape(r)}</p></details>' for p, r in a['faq'])
    rel = ''.join(f'<li><a href="/dicas/{o["slug"]}/">{html.escape(o["h1"])}</a></li>' for o in outros)
    f = c['font'].replace(' ', '+')
    return f'''<!doctype html>
<html lang="pt-BR"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(a['title'])}</title>
<meta name="description" content="{html.escape(a['desc'])}">
<link rel="canonical" href="{url}"><meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="article"><meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{html.escape(a['title'])}"><meta property="og:description" content="{html.escape(a['desc'])}"><meta property="og:url" content="{url}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={f}:wght@400;600;800&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>
:root{{--c:{c['cor']};--d:{c['dest']};--f:{c['fundo']};--i:{c['ink']}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--f);color:var(--i);font:17px/1.7 '{c['font']}',system-ui,sans-serif}}
header{{background:var(--c);color:#fff;padding:14px 16px}}header a{{color:#fff;text-decoration:none;font-weight:800}}
nav.bc{{font-size:13px;opacity:.75;margin:18px 0 0}}nav.bc a{{color:inherit}}
main{{max-width:760px;margin:0 auto;padding:0 16px 40px}}
h1{{font-size:clamp(28px,6vw,42px);line-height:1.15;margin:14px 0 18px;color:var(--c)}}
h2{{font-size:23px;line-height:1.3;margin:34px 0 8px;color:var(--c)}}
ul{{padding-left:22px}}li{{margin:6px 0}}
.cta{{display:flex;flex-wrap:wrap;gap:10px;background:#fff;border-left:5px solid var(--d);padding:18px;border-radius:12px;margin:30px 0;box-shadow:0 6px 24px rgba(0,0,0,.06)}}
.cta p{{margin:0;flex:1 1 260px;font-weight:600}}
.bt{{display:inline-block;background:#25D366;color:#fff;font-weight:800;text-decoration:none;padding:13px 20px;border-radius:999px}}
.bt.s{{background:var(--c)}}
details{{background:#fff;border-radius:10px;padding:12px 16px;margin:8px 0}}summary{{font-weight:700;cursor:pointer}}
footer{{max-width:760px;margin:0 auto;padding:20px 16px 90px;font-size:13px;opacity:.75}}
.flut{{position:fixed;right:16px;bottom:16px;box-shadow:0 8px 24px rgba(0,0,0,.25)}}
</style></head><body>
<header><a href="/">{html.escape(c['nome'])}</a></header>
<main>
<nav class="bc"><a href="/">Início</a> › <a href="/dicas/">Dicas</a> › {html.escape(a['h1'])}</nav>
<article>
<h1>{html.escape(a['h1'])}</h1>
{''.join(f'<p>{html.escape(p)}</p>' for p in a['intro'])}
{corpo}
<h2>Conclusão</h2><p>{html.escape(a['fim'])}</p>
<div class="cta"><p>Fale direto com a equipe da {html.escape(c['nome'])} pelo WhatsApp. O orçamento vem antes de qualquer serviço.</p>
<a class="bt" href="{wa}" target="_blank" rel="noopener">Chamar no WhatsApp</a>
<a class="bt s" href="{serv_url}">{html.escape(a['servico'][1])}</a></div>
<h2>Perguntas frequentes</h2>{faq}
</article>
<h2>Leia também</h2><ul>{rel}</ul>
</main>
<footer>{html.escape(c['rod'])}</footer>
<a class="bt flut" href="{wa}" target="_blank" rel="noopener">WhatsApp</a>
</body></html>
'''

def indice(c):
    itens = ''.join(f'<li><a href="/dicas/{a["slug"]}/"><b>{html.escape(a["h1"])}</b></a><br>{html.escape(a["desc"])}</li>' for a in c['arts'])
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dicas e dúvidas | {html.escape(c['nome'])}</title><meta name="description" content="Respostas para as dúvidas mais comuns dos clientes da {html.escape(c['nome'])}.">
<link rel="canonical" href="{c['base']}/dicas/">
<style>body{{margin:0;background:{c['fundo']};color:{c['ink']};font:17px/1.6 system-ui,sans-serif}}main{{max-width:760px;margin:0 auto;padding:24px 16px}}h1{{color:{c['cor']}}}li{{margin:0 0 18px}}a{{color:{c['cor']}}}</style></head>
<body><main><p><a href="/">← Início</a></p><h1>Dicas e dúvidas</h1><ul>{itens}</ul></main></body></html>
'''

for c in CLI:
    os.makedirs(f"{AG}/{c['k']}/artigos", exist_ok=True)
    for a in c['arts']:
        assert len(a['title']) <= 60, a['title']; assert len(a['desc']) <= 155, a['desc']
        n = len(texto(a).split()); print(c['k'], a['slug'], n, 'palavras')
        p = pagina(c, a, [o for o in c['arts'] if o is not a])
        open(f"{AG}/{c['k']}/artigos/{a['slug']}.html", 'w').write(p)
        if c['repo']:
            os.makedirs(f"{c['repo']}/dicas/{a['slug']}", exist_ok=True)
            open(f"{c['repo']}/dicas/{a['slug']}/index.html", 'w').write(p)
    if not c['repo']:
        continue
    open(f"{c['repo']}/dicas/index.html", 'w').write(indice(c))
    sm = open(f"{c['repo']}/sitemap.xml").read()
    novos = [f"{c['base']}/dicas/"] + [f"{c['base']}/dicas/{a['slug']}/" for a in c['arts']]
    add = ''.join(f'<url><loc>{u}</loc><lastmod>2026-11-16</lastmod></url>\n' for u in novos if f'<loc>{u}</loc>' not in sm)
    if add: open(f"{c['repo']}/sitemap.xml", 'w').write(sm.replace('</urlset>', add + '</urlset>'))
    idx = open(f"{c['repo']}/index.html").read()
    if '/dicas/' not in idx:
        links = ' · '.join(f'<a href="/dicas/{a["slug"]}/">{html.escape(a["h1"])}</a>' for a in c['arts'])
        bloco_home = f'<div class="dicas-seo" style="padding:12px 16px;font-size:14px;line-height:1.8"><b><a href="/dicas/">Dicas e dúvidas</a>:</b> {links}</div>'
        i = idx.rfind('</footer>')
        open(f"{c['repo']}/index.html", 'w').write(idx[:i] + bloco_home + idx[i:])
