# Projeto Designer v3 (conta Leandro, 16/11/2026): página de venda, proposta (PDF) e anúncio com mockups reais.
# Sem preço nas peças públicas e sem placeholder: o exemplo é "Sua marca" ou um case real.
# Uso: python3 oferta.py <mockups> <saida_v2>
import sys, os, shutil
from PIL import Image
MK, OUT = [os.path.abspath(a) for a in sys.argv[1:3]]
OFF, INK, AMB, LAP = '#EEEAE2', '#0A0C10', '#B4935A', '#2B3A8F'
WA = 'https://wa.me/5598985621808?text=Oi%2C%20Barzakh!%20Quero%20um%20or%C3%A7amento%20de%20identidade%20visual.'
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;700;800&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">'
CASES = [('realtime', 'Real Time', 'Produtora audiovisual'), ('oregano', 'Orégano Turbo', 'Marketing para pizzarias'), ('curso', 'Processo Legislativo', 'Curso para câmaras'),
         ('wf', 'WF Celulares', 'Loja de iPhone'), ('duble', 'Dublê', 'Aplicativo de voz'), ('leo', 'Leo Pinto', 'Comunicação pública')]
PACOTES = [('Limiar', 'Para quem está começando e precisa de uma marca profissional.', ['Briefing e persona', 'Pesquisa de referências', 'Logo + versões', 'Paleta e tipografia', '2 rodadas de ajuste', 'Arquivos finais (PNG, SVG, PDF)', 'Até 10 dias úteis']),
           ('Travessia', 'Para quem já vende e quer a mesma cara em tudo.', ['Tudo do Limiar', '2 caminhos de conceito', 'Elementos e direção de foto', 'Tom de voz', 'Instagram, cartão e assinatura', 'Guia de marca em PDF', 'Até 20 dias úteis']),
           ('Horizonte', 'Para quem quer a marca inteira pronta para crescer.', ['Tudo da Travessia', 'Brand book de 17 páginas', 'Social kit (post, carrossel, Stories)', 'Mini site na identidade (opcional)', 'Apresentação da marca', 'Até 30 dias úteis'])]
ETAPAS = [('Briefing', 'Formulário e conversa: negócio, cliente, concorrentes, gosto.'), ('Persona e pesquisa', 'Quem compra de você e referências premiadas do mundo todo.'),
          ('Conceito', 'A ideia da marca e o logo, apresentados já em mockup.'), ('Sistema', 'Cores, letras, elementos, fotografia e voz.'),
          ('Aplicações', 'Instagram, papelaria, embalagem, site: a marca no mundo.'), ('Entrega', 'Arquivos finais, brand book e apoio para usar.')]
CSS = f'''*{{box-sizing:border-box;margin:0}}body{{background:{OFF};color:{INK};font-family:Inter Tight,sans-serif}}img{{display:block;max-width:100%}}
.lbl{{font:500 13px "JetBrains Mono",monospace;letter-spacing:.18em;text-transform:uppercase}}.serif{{font-family:"Instrument Serif",serif;font-weight:400}}
a.btn{{display:inline-flex;gap:12px;align-items:center;background:{INK};color:#fff;text-decoration:none;font:700 17px Inter Tight;padding:18px 28px;border-radius:999px}}a.btn i{{width:10px;height:10px;border-radius:50%;background:{AMB}}}'''

def pagina(img):
    cases = ''.join(f'<figure style="margin:0"><img src="{img}/{k}-cartoes.jpg" style="aspect-ratio:4/3;object-fit:cover;width:100%"><figcaption style="display:flex;justify-content:space-between;padding:14px 2px 0"><b style="font:700 18px Inter Tight">{n}</b><span class="lbl" style="color:#666">{s}</span></figcaption></figure>' for k, n, s in CASES)
    pac = ''.join(f'<div style="background:{"#fff" if i != 2 else INK};color:{INK if i != 2 else "#fff"};padding:36px;border-radius:20px;display:flex;flex-direction:column;gap:18px"><div class="lbl" style="color:{"#777" if i != 2 else AMB}">{"0"+str(i+1)}</div><div class="serif" style="font-size:46px">{n}</div><p style="opacity:.75">{d}</p><ul style="padding-left:18px;line-height:1.9">{"".join(f"<li>{x}</li>" for x in it)}</ul></div>' for i, (n, d, it) in enumerate(PACOTES))
    et = ''.join(f'<div style="border-top:1px solid #0002;padding:22px 0;display:grid;grid-template-columns:minmax(40px,60px) minmax(0,220px) minmax(0,1fr);gap:16px" class="et"><span class="lbl">{i+1:02d}</span><b>{n}</b><span style="color:#555">{d}</span></div>' for i, (n, d) in enumerate(ETAPAS))
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Identidade visual · Barzakh · um estúdio Al Kántara</title>
<meta name="description" content="Identidade visual completa para o seu negócio: logo, cores, brand book e a marca aplicada no mundo real. Barzakh · um estúdio Al Kántara, São Luís (MA).">{FONTS}<style>{CSS}
.w{{max-width:1240px;margin:0 auto;padding:0 24px}}section{{padding:90px 0}}h2{{font:400 clamp(40px,6vw,76px)/1 "Instrument Serif"}}
.g3{{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}}@media(max-width:820px){{.g3{{grid-template-columns:1fr}}.hero{{grid-template-columns:1fr!important}}.et{{grid-template-columns:40px 1fr!important}}.et span:last-child{{grid-column:2}}}}</style></head><body>
<header class="w" style="display:flex;justify-content:space-between;align-items:center;padding-top:26px;padding-bottom:26px"><b style="font:400 30px Instrument Serif;letter-spacing:.14em">BARZAKH <span style="font:500 11px JetBrains Mono;letter-spacing:.2em;color:{AMB}">UM ESTÚDIO AL KÁNTARA</span></b><a class="btn" href="{WA}"><i></i>Pedir orçamento</a></header>
<section class="w hero" style="display:grid;grid-template-columns:1fr 1.1fr;gap:56px;align-items:center;padding-top:40px">
<div><div class="lbl" style="color:#666">Identidade visual · brand book · web design</div><h1 class="serif" style="font-size:clamp(52px,7vw,96px);line-height:.98;margin:22px 0">Sua marca do tamanho que o seu negócio já é.</h1>
<p style="font-size:19px;line-height:1.6;color:#444;max-width:520px">Logo, cores, letras e a marca aplicada no mundo real: cartão, Instagram, embalagem, fachada. Tudo pensado em quem compra de você.</p>
<div style="margin-top:34px;display:flex;gap:18px;align-items:center"><a class="btn" href="{WA}"><i></i>Quero a minha marca</a><span class="lbl" style="color:#666">resposta no WhatsApp</span></div></div>
<img src="{img}/oregano-papelaria.jpg" style="border-radius:6px;aspect-ratio:4/3;object-fit:cover"></section>
<section class="w"><div style="display:flex;justify-content:space-between;align-items:end;margin-bottom:40px"><h2>Marcas que já saíram daqui</h2><span class="lbl">6 cases reais</span></div><div class="g3">{cases}</div></section>
<section style="background:{INK};color:#fff"><div class="w" style="display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center" class="hero"><img src="{img}/realtime-celular.jpg" style="border-radius:6px">
<div><div class="lbl" style="color:{AMB}">O que muda</div><h2 style="margin:18px 0 22px">Cada post com a mesma cara. O cliente lembra de você.</h2><p style="color:#bbb;line-height:1.7;font-size:18px">Quando a marca tem sistema (cores com proporção, letras certas, regras simples), tudo o que você publica parece da mesma empresa. É isso que faz o cliente confiar antes de perguntar o preço.</p></div></div></section>
<section class="w"><h2 style="margin-bottom:40px">Como funciona</h2>{et}</section>
<section class="w"><div style="display:flex;justify-content:space-between;align-items:end;margin-bottom:40px"><h2>Escolha o tamanho do projeto</h2><span class="lbl">valores no WhatsApp</span></div><div class="g3">{pac}</div></section>
<section class="w"><img src="{img}/curso-poster.jpg" style="border-radius:6px;aspect-ratio:16/8;object-fit:cover;width:100%"></section>
<section class="w" style="text-align:center;padding-bottom:120px"><h2 style="max-width:900px;margin:0 auto 34px">Vamos tirar a sua marca do improviso?</h2><a class="btn" href="{WA}"><i></i>Falar com a Barzakh no WhatsApp</a>
<div class="lbl" style="margin-top:60px;color:#777">Barzakh · um estúdio Al Kántara · São Luís, MA · @barzakhstudio · direção criativa Lindson Almeida</div></section></body></html>'''

def proposta(img):
    pg = lambda body, bg=OFF, fg=INK: f'<section style="width:1754px;height:1240px;background:{bg};color:{fg};position:relative;overflow:hidden;page-break-after:always">{body}</section>'
    P = []
    P.append(pg(f'<img src="{img}/realtime-cartoes.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"><div style="position:absolute;left:0;top:0;bottom:0;width:720px;background:{OFF};padding:110px;display:flex;flex-direction:column;justify-content:space-between"><b style="font:400 36px Instrument Serif;letter-spacing:.14em">BARZAKH <span style="font:500 11px JetBrains Mono;letter-spacing:.2em;color:{AMB}">UM ESTÚDIO AL KÁNTARA</span></b><div><div class="lbl">Proposta · identidade visual</div><div class="serif" style="font-size:120px;line-height:.95;margin-top:24px">Sua marca,<br>pronta para o mundo.</div></div><div class="lbl" style="color:#666">Preparada para: Sua marca · São Luís, MA</div></div>'))
    P.append(pg(f'<div style="padding:130px;display:grid;grid-template-columns:1fr 1fr;gap:110px;height:100%;align-items:center"><div><div class="lbl">01 · O ponto de partida</div><div class="serif" style="font-size:88px;line-height:1;margin:30px 0">A marca parece menor do que o negócio é.</div><p style="font-size:28px;line-height:1.6;color:#444">Cada post sai de um jeito, o cliente não lembra do nome e fica difícil cobrar o que o trabalho vale. A identidade visual resolve isso com um sistema simples que qualquer pessoa da equipe consegue seguir.</p></div><img src="{img}/wf-celular.jpg" style="border-radius:8px"></div>'))
    et = ''.join(f'<div style="border-top:2px solid #0002;padding:30px 0;display:grid;grid-template-columns:110px 380px 1fr;font-size:30px"><span class="lbl" style="font-size:20px">{i+1:02d}</span><b>{n}</b><span style="color:#555">{d}</span></div>' for i, (n, d) in enumerate(ETAPAS))
    P.append(pg(f'<div style="padding:130px"><div class="lbl">02 · Como vamos trabalhar</div><div class="serif" style="font-size:88px;margin:24px 0 50px">Seis etapas, do briefing à entrega.</div>{et}</div>'))
    pac = ''.join(f'<div style="background:{"#fff" if i != 2 else INK};color:{INK if i != 2 else "#fff"};padding:56px;border-radius:24px"><div class="lbl" style="color:{"#777" if i != 2 else AMB};font-size:18px">Pacote {i+1:02d}</div><div class="serif" style="font-size:76px;margin:16px 0">{n}</div><p style="font-size:24px;opacity:.75;margin-bottom:26px">{d}</p><ul style="padding-left:26px;font-size:25px;line-height:1.9">{"".join(f"<li>{x}</li>" for x in it)}</ul></div>' for i, (n, d, it) in enumerate(PACOTES))
    P.append(pg(f'<div style="padding:110px 130px"><div class="lbl">03 · Pacotes</div><div class="serif" style="font-size:80px;margin:20px 0 50px">Escolha o tamanho do projeto.</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:36px">{pac}</div><div class="lbl" style="margin-top:40px;color:#666">Investimento e forma de pagamento combinados na conversa.</div></div>'))
    grid = ''.join(f'<div><img src="{img}/{k}-{c}.jpg" style="aspect-ratio:4/3;object-fit:cover;width:100%;border-radius:6px"><div style="display:flex;justify-content:space-between;margin-top:14px;font-size:24px"><b>{n}</b><span class="lbl" style="font-size:16px;color:#666">{s}</span></div></div>' for (k, n, s), c in zip(CASES, ['papelaria', 'embalagem', 'poster', 'celular', 'cartoes', 'papelaria']))
    P.append(pg(f'<div style="padding:100px 130px"><div class="lbl">04 · Trabalhos reais</div><div class="serif" style="font-size:80px;margin:20px 0 40px">Marcas que já saíram daqui.</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:34px">{grid}</div></div>'))
    P.append(pg(f'<img src="{img}/oregano-papelaria.jpg" style="position:absolute;right:0;top:0;width:1000px;height:100%;object-fit:cover"><div style="padding:130px;width:820px"><div class="lbl">05 · O que você recebe</div><div class="serif" style="font-size:80px;line-height:1;margin:24px 0 40px">A marca aplicada, não só um logo.</div><ul style="font-size:30px;line-height:2;padding-left:30px"><li>Logo e versões em PNG, SVG e PDF</li><li>Cores com proporção e letras</li><li>Brand book para a equipe seguir</li><li>Instagram, cartão, papelaria</li><li>Mockups para divulgar a nova marca</li></ul></div>'))
    P.append(pg(f'<div style="height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:40px"><div class="serif" style="font-size:120px;line-height:1">Vamos começar?</div><p style="font-size:30px;color:#bbb">Responda esta proposta no WhatsApp e marcamos o briefing.</p><div style="background:{AMB};color:{INK};font:800 34px Inter Tight;padding:26px 46px;border-radius:999px">wa.me/5598985621808</div><div class="lbl" style="color:#888;font-size:18px">Barzakh · um estúdio Al Kántara · São Luís, MA · lindsonalmeida.pages.dev</div></div>', INK, '#fff'))
    return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}@page{{size:1754px 1240px;margin:0}}</style></head><body>{"".join(P)}</body></html>'

def anuncio(img):
    T = []
    tela = lambda body, bg=OFF, fg=INK: f'<div class="t" style="width:1080px;height:1350px;background:{bg};color:{fg};position:relative;overflow:hidden">{body}</div>'
    T.append(tela(f'<img src="{img}/oregano-cartoes.jpg" style="width:1080px;height:860px;object-fit:cover"><div style="padding:56px 70px"><div class="serif" style="font-size:96px;line-height:.95">Sua marca parece do tamanho do seu negócio?</div><div class="lbl" style="margin-top:28px;color:#666">arraste →</div></div>'))
    T.append(tela(f'<div style="padding:80px 70px 0"><div class="lbl" style="color:{AMB}">o problema</div><div class="serif" style="font-size:92px;line-height:1;margin-top:24px">Cada post de um jeito. O cliente não lembra de você.</div></div><img src="{img}/wf-celular.jpg" style="position:absolute;bottom:0;width:1080px;height:640px;object-fit:cover">', INK, '#fff'))
    T.append(tela(f'<img src="{img}/realtime-papelaria.jpg" style="width:1080px;height:810px;object-fit:cover"><div style="padding:56px 70px"><div class="lbl">a solução</div><div class="serif" style="font-size:80px;line-height:1;margin-top:18px">Identidade visual completa: logo, cores, letras e a marca aplicada.</div></div>'))
    T.append(tela(f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;height:1100px">{"".join(f"<img src={chr(34)}{img}/{k}-{c}.jpg{chr(34)} style={chr(34)}width:100%;height:100%;object-fit:cover{chr(34)}>" for k, c in [("curso", "poster"), ("duble", "cartoes"), ("oregano", "embalagem"), ("leo", "papelaria")])}</div><div style="padding:50px 70px;display:flex;justify-content:space-between;align-items:center"><div class="serif" style="font-size:64px">Cases reais</div><div class="lbl">São Luís · MA</div></div>'))
    T.append(tela(f'<img src="{img}/duble-embalagem.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.35"><div style="position:relative;height:100%;padding:90px 70px;display:flex;flex-direction:column;justify-content:space-between"><b style="font:400 46px Instrument Serif;letter-spacing:.14em">BARZAKH <span style="font:500 13px JetBrains Mono;letter-spacing:.2em;color:{AMB}">UM ESTÚDIO AL KÁNTARA</span></b><div><div class="serif" style="font-size:110px;line-height:.95">Vamos tirar a sua marca do improviso?</div><div style="margin-top:44px;display:inline-block;background:{AMB};color:{INK};font:800 34px Inter Tight;padding:24px 40px;border-radius:999px">Chame no WhatsApp</div></div></div>', INK, '#fff'))
    return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}.t{{margin-bottom:10px}}</style></head><body>{"".join(T)}</body></html>'

if __name__ == '__main__':
    from playwright.sync_api import sync_playwright
    d = f'{OUT}/oferta'; os.makedirs(f'{d}/pagina/img', exist_ok=True); os.makedirs(f'{d}/anuncio', exist_ok=True)
    usados = set()
    for k, _, _ in CASES:
        for c in ['cartoes', 'papelaria', 'celular', 'poster', 'embalagem']:
            im = Image.open(f'{MK}/{k}-{c}.jpg'); im.thumbnail((1400, 1400)); im.save(f'{d}/pagina/img/{k}-{c}.jpg', quality=82)
    open(f'{d}/pagina/index.html', 'w').write(pagina('img'))
    with sync_playwright() as pw:
        b = pw.chromium.launch(proxy={'server': os.environ['HTTPS_PROXY']} if os.environ.get('HTTPS_PROXY') else None, args=['--allow-file-access-from-files'])
        p = b.new_page(viewport={'width': 1440, 'height': 900})
        p.goto(f'file://{d}/pagina/index.html', wait_until='networkidle'); p.wait_for_timeout(500); p.screenshot(path=f'{d}/pagina-previa.png', full_page=True)
        Image.open(f'{d}/pagina-previa.png').convert('RGB').save(f'{d}/pagina-previa.jpg', quality=80); os.remove(f'{d}/pagina-previa.png')
        hp = f'{d}/pagina/_prop.html'; open(hp, 'w').write(proposta('file://' + d + '/pagina/img'))
        p.set_viewport_size({'width': 1754, 'height': 1240}); p.goto('file://' + hp, wait_until='networkidle'); p.wait_for_timeout(500)
        p.pdf(path=f'{d}/proposta-identidade-visual-barzakh.pdf', width='1754px', height='1240px', print_background=True)
        p.query_selector('section').screenshot(path=f'{d}/proposta-capa.png'); Image.open(f'{d}/proposta-capa.png').convert('RGB').save(f'{d}/proposta-capa.jpg', quality=85); os.remove(f'{d}/proposta-capa.png')
        for i, s in enumerate(p.query_selector_all('section')):
            s.screenshot(path=f'{d}/_p{i}.png')
        hp2 = f'{d}/pagina/_anu.html'; open(hp2, 'w').write(anuncio('file://' + d + '/pagina/img'))
        p.set_viewport_size({'width': 1080, 'height': 1350}); p.goto('file://' + hp2, wait_until='networkidle'); p.wait_for_timeout(500)
        for i, t in enumerate(p.query_selector_all('.t')):
            t.screenshot(path=f'{d}/anuncio/tela-{i+1}.png'); Image.open(f'{d}/anuncio/tela-{i+1}.png').convert('RGB').save(f'{d}/anuncio/tela-{i+1}.jpg', quality=88); os.remove(f'{d}/anuncio/tela-{i+1}.png')
        b.close()
    os.remove(hp); os.remove(hp2)
    print('oferta ok')
