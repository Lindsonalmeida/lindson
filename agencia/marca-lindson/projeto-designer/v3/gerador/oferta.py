# Projeto Designer v3 (conta Leandro, 16/11/2026): página de venda, proposta (PDF) e anúncio com mockups reais.
# 16/11 tarde: tudo no padrão escuro da placa em arco APROVADA (escuro.py) e com Fraunces (família da holding v2).
# Sem preço nas peças públicas e sem placeholder: o exemplo é "Sua marca" ou um case real.
# Uso: python3 oferta.py <mockups> <saida_v2>
import sys, os, shutil, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location('dk', os.path.join(HERE, 'escuro.py')); dk = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(dk)
from PIL import Image
MK, OUT = [os.path.abspath(a) for a in sys.argv[1:3]]
OFF, INK, AMB, LAP = '#EEEAE2', '#0A0C10', '#B4935A', '#2B3A8F'
WA = 'https://wa.me/5598985621808?text=Oi%2C%20Barzakh!%20Quero%20um%20or%C3%A7amento%20de%20identidade%20visual.'
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;700;800&family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">'
CASES = [('realtime', 'Real Time', 'Produtora audiovisual'), ('oregano', 'Orégano Turbo', 'Marketing para pizzarias'), ('curso', 'Processo Legislativo', 'Curso para câmaras'),
         ('wf', 'WF Celulares', 'Loja de iPhone'), ('duble', 'Dublê', 'Aplicativo de voz'), ('leo', 'Leo Pinto', 'Comunicação pública')]
PACOTES = [('Limiar', 'Para quem está começando e precisa de uma marca profissional.', ['Briefing e persona', 'Pesquisa de referências', 'Logo + versões', 'Paleta e tipografia', '2 rodadas de ajuste', 'Arquivos finais (PNG, SVG, PDF)', 'Até 10 dias úteis']),
           ('Travessia', 'Para quem já vende e quer a mesma cara em tudo.', ['Tudo do Limiar', '2 caminhos de conceito', 'Elementos e direção de foto', 'Tom de voz', 'Instagram, cartão e assinatura', 'Guia de marca em PDF', 'Até 20 dias úteis']),
           ('Horizonte', 'Para quem quer a marca inteira pronta para crescer.', ['Tudo da Travessia', 'Brand book de 17 páginas', 'Social kit (post, carrossel, Stories)', 'Mini site na identidade (opcional)', 'Apresentação da marca', 'Até 30 dias úteis'])]
ETAPAS = [('Briefing', 'Formulário e conversa: negócio, cliente, concorrentes, gosto.'), ('Persona e pesquisa', 'Quem compra de você e referências premiadas do mundo todo.'),
          ('Conceito', 'A ideia da marca e o logo, apresentados já em mockup.'), ('Sistema', 'Cores, letras, elementos, fotografia e voz.'),
          ('Aplicações', 'Instagram, papelaria, embalagem, site: a marca no mundo.'), ('Entrega', 'Arquivos finais, brand book e apoio para usar.')]

GRAF = dk.GRAF
CSS = dk.CSS + f"""*{{box-sizing:border-box;margin:0}}html,body{{background:{INK};color:{OFF};font-family:'Inter Tight',sans-serif;overflow-x:hidden}}img{{display:block;max-width:100%}}
.lbl{{font:500 13px 'JetBrains Mono',monospace;letter-spacing:.18em;text-transform:uppercase}}.serif{{font-family:'Fraunces',serif;font-weight:400;font-optical-sizing:auto;letter-spacing:-.01em}}
a.btn{{display:inline-flex;gap:12px;align-items:center;background:transparent;color:{OFF};text-decoration:none;font:600 17px 'Inter Tight';padding:17px 28px;border-radius:999px;border:1px solid {AMB}}}a.btn i{{width:10px;height:10px;border-radius:50%;background:{dk.OURO}}}
a.btn.full{{background:{dk.OURO};color:{INK};border:0}}a.btn.full i{{background:{INK}}}
.logo{{display:inline-flex;align-items:center;gap:14px}}"""

def logo(h=34):
    return (f'<span class="logo">{dk.mono_inline(h*1.25)}<span><span class="foil" style="display:block;width:{h*5}px;height:{h*.62}px;-webkit-mask-image:{dk.mask("logotipo-mono-branco")};mask-image:{dk.mask("logotipo-mono-branco")};-webkit-mask-position:left;mask-position:left"></span>'
            f'<span class="lbl" style="display:block;font-size:{max(10, h*.3):.0f}px;color:{AMB};margin-top:6px">{dk.ENDOSSO(max(10, h*.3), AMB)}</span></span></span>')

def pagina(img):
    cases = ''.join(f'<figure style="margin:0"><div style="overflow:hidden;border-radius:4px;box-shadow:0 30px 60px rgba(0,0,0,.5)"><img src="{img}/{k}-cartoes.jpg" style="aspect-ratio:4/3;object-fit:cover;width:100%"></div><figcaption style="display:flex;justify-content:space-between;gap:12px;padding:16px 2px 0;border-top:1px solid rgba(180,147,90,.3);margin-top:16px"><b class="serif" style="font-size:24px">{n}</b><span class="lbl" style="color:{AMB};font-size:11px;text-align:right">{s}</span></figcaption></figure>' for k, n, s in CASES)
    pac = ''.join(f'<div style="background-color:{"#13151a" if i != 1 else "#171a24"};border:1px solid {"rgba(238,234,226,.12)" if i != 1 else AMB};padding:36px;border-radius:6px;display:flex;flex-direction:column;gap:18px;position:relative;overflow:hidden">{"<div class=beam style=right:-80px;top:-80px;width:320px;height:260px;opacity:.6></div>" if i == 1 else ""}<div class="lbl" style="color:{AMB};position:relative">{"0"+str(i+1)}{" · mais escolhido" if i == 1 else ""}</div><div class="serif" style="font-size:48px;position:relative">{n}</div><p style="opacity:.75;font-size:18px;line-height:1.5">{d}</p><ul style="padding-left:18px;line-height:1.9;font-size:17px;color:#d6d2ca">{"".join(f"<li>{x}</li>" for x in it)}</ul></div>' for i, (n, d, it) in enumerate(PACOTES))
    et = ''.join(f'<div class="et" style="border-top:1px solid rgba(180,147,90,.3);padding:24px 0;display:grid;grid-template-columns:70px 260px minmax(0,1fr);gap:16px;align-items:baseline"><span class="lbl" style="color:{AMB}">{i+1:02d}</span><b class="serif" style="font-size:28px">{n}</b><span style="color:#bdb9b1;font-size:18px;line-height:1.5">{d}</span></div>' for i, (n, d) in enumerate(ETAPAS))
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Identidade visual · Barzakh</title>
<meta name="description" content="Identidade visual completa para o seu negócio: logo, cores, brand book e a marca aplicada no mundo real. Barzakh · um estúdio Al Kántara, São Luís (MA).">{FONTS}<style>{CSS}
.w{{max-width:1240px;margin:0 auto;padding:0 24px}}section{{padding:100px 0;position:relative}}h2{{font:400 clamp(38px,5.6vw,72px)/1.02 'Fraunces';letter-spacing:-.01em}}
.g3{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:30px}}.hero{{display:grid;grid-template-columns:1fr 1.05fr;gap:40px;align-items:center}}.two{{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}}
@media(max-width:820px){{.g3,.hero,.two{{grid-template-columns:minmax(0,1fr)!important}}.et{{grid-template-columns:44px minmax(0,1fr)!important}}.et span:last-child{{grid-column:2}}section{{padding:64px 0}}header a.btn{{display:none}}.hx{{flex-direction:column;align-items:flex-start!important;gap:14px}}}}</style></head><body>
<div class="grain" style="position:relative;overflow:hidden;background:{INK}"><div class="conc" style="position:absolute;inset:0;opacity:.28"></div><div class="win" style="opacity:.7"></div><div style="position:absolute;inset:0;background:linear-gradient(90deg,{INK} 25%,rgba(10,12,16,.55))"></div>
<header class="w" style="position:relative;z-index:7;display:flex;justify-content:space-between;align-items:center;padding-top:26px;padding-bottom:26px">{logo(30)}<a class="btn" href="{WA}"><i></i>Pedir orçamento</a></header>
<section class="w hero" style="z-index:7;padding-top:30px">
<div><div class="lbl" style="color:{AMB}">Identidade visual · brand book · web design</div><h1 class="serif" style="font-size:clamp(46px,6.4vw,92px);line-height:1;margin:22px 0">Sua marca do tamanho que o seu negócio já é.</h1>
<p style="font-size:19px;line-height:1.6;color:#c9c5bd;max-width:520px">Logo, cores, letras e a marca aplicada no mundo real: cartão, Instagram, embalagem, fachada. Tudo pensado em quem compra de você.</p>
<div style="margin-top:34px;display:flex;gap:18px;align-items:center;flex-wrap:wrap"><a class="btn full" href="{WA}"><i></i>Quero a minha marca</a><span class="lbl" style="color:#8a8f98">resposta no WhatsApp</span></div></div>
<img src="{img}/placa-hero.jpg" alt="Placa em arco grafite com o símbolo da Barzakh em ouro escovado, presa em parede de concreto" style="width:100%;border-radius:4px"></section></div>
<section class="w"><div class="hx" style="display:flex;justify-content:space-between;align-items:end;margin-bottom:46px"><h2>Marcas que já saíram daqui</h2><span class="lbl" style="color:{AMB}">6 cases reais</span></div><div class="g3">{cases}</div></section>
<section class="grain" style="background-color:#121418;overflow:hidden"><div class="beam" style="left:10%;top:20%;width:520px;height:420px;opacity:.5"></div><div class="w two" style="position:relative"><img src="{img}/realtime-celular.jpg" style="border-radius:4px;box-shadow:0 40px 80px rgba(0,0,0,.6)">
<div><div class="lbl" style="color:{AMB}">O que muda</div><h2 style="margin:18px 0 22px">Cada post com a mesma cara. O cliente lembra de você.</h2><p style="color:#c9c5bd;line-height:1.7;font-size:18px">Quando a marca tem sistema (cores com proporção, letras certas, regras simples), tudo o que você publica parece da mesma empresa. É isso que faz o cliente confiar antes de perguntar o preço.</p></div></div></section>
<section class="w"><h2 style="margin-bottom:40px">Como funciona</h2>{et}</section>
<section class="w"><div class="hx" style="display:flex;justify-content:space-between;align-items:end;margin-bottom:46px"><h2>Escolha o tamanho do projeto</h2><span class="lbl" style="color:{AMB}">valores no WhatsApp</span></div><div class="g3">{pac}</div></section>
<section class="w"><div style="position:relative;overflow:hidden;border-radius:4px"><img src="{img}/barzakh-papelaria.jpg" style="aspect-ratio:16/8;object-fit:cover;width:100%"></div></section>
<section class="grain" style="text-align:center;padding-bottom:110px;overflow:hidden"><div class="beam" style="left:50%;top:10%;width:640px;height:400px;margin-left:-320px;opacity:.7"></div><div class="w" style="position:relative">{dk.mono_inline(96).replace('flex:none', 'flex:none;margin:0 auto 30px')}<h2 style="max-width:900px;margin:0 auto 34px">Vamos tirar a sua marca do improviso?</h2><a class="btn full" href="{WA}"><i></i>Falar com a Barzakh no WhatsApp</a>
<div class="lbl" style="margin-top:60px;color:#8a8f98;line-height:2">{dk.ENDOSSO(12, '#8a8f98')} · São Luís, MA · @barzakhstudio<br>direção criativa Lindson Almeida</div></div></section></body></html>"""

def proposta(img):
    pg = lambda body, extra='': f'<section class="grain" style="width:1754px;height:1240px;background:{INK};color:{OFF};position:relative;overflow:hidden;page-break-after:always">{extra}<div style="position:relative;height:100%">{body}</div></section>'
    fundo = f'<div class="conc" style="position:absolute;inset:0;opacity:.22"></div><div class="win" style="opacity:.6"></div>'
    P = []
    P.append(pg(f'<div style="position:absolute;left:0;top:0;bottom:0;width:820px;padding:110px;display:flex;flex-direction:column;justify-content:space-between">{logo(44)}<div><div class="lbl" style="color:{AMB};font-size:20px">Proposta · identidade visual</div><div class="serif" style="font-size:112px;line-height:1;margin-top:26px">Sua marca,<br>pronta para<br>o mundo.</div></div><div class="lbl" style="color:#8a8f98;font-size:18px">Preparada para: sua marca · São Luís, MA</div></div>'
                f'<img src="{img}/placa-hero.jpg" style="position:absolute;right:0;top:0;width:934px;height:1240px;object-fit:cover">'))
    P.append(pg(f'<div style="padding:130px;display:grid;grid-template-columns:1fr 1fr;gap:110px;height:100%;align-items:center"><div><div class="lbl" style="color:{AMB};font-size:20px">01 · O ponto de partida</div><div class="serif" style="font-size:84px;line-height:1.02;margin:30px 0">A marca parece menor do que o negócio é.</div><p style="font-size:28px;line-height:1.6;color:#c9c5bd">Cada post sai de um jeito, o cliente não lembra do nome e fica difícil cobrar o que o trabalho vale. A identidade visual resolve isso com um sistema simples que qualquer pessoa da equipe consegue seguir.</p></div><img src="{img}/wf-celular.jpg" style="border-radius:6px;box-shadow:0 40px 80px rgba(0,0,0,.6)"></div>', fundo))
    et = ''.join(f'<div style="border-top:1px solid rgba(180,147,90,.35);padding:28px 0;display:grid;grid-template-columns:110px 400px 1fr;font-size:28px;align-items:baseline"><span class="lbl" style="font-size:20px;color:{AMB}">{i+1:02d}</span><b class="serif" style="font-size:40px">{n}</b><span style="color:#c9c5bd">{d}</span></div>' for i, (n, d) in enumerate(ETAPAS))
    P.append(pg(f'<div style="padding:120px 130px"><div class="lbl" style="color:{AMB};font-size:20px">02 · Como vamos trabalhar</div><div class="serif" style="font-size:84px;margin:24px 0 46px">Seis etapas, do briefing à entrega.</div>{et}</div>'))
    pac = ''.join(f'<div style="background-color:{"#13151a" if i != 1 else "#171a24"};border:1px solid {"rgba(238,234,226,.14)" if i != 1 else AMB};padding:52px;border-radius:8px"><div class="lbl" style="color:{AMB};font-size:18px">Pacote {i+1:02d}</div><div class="serif" style="font-size:72px;margin:16px 0">{n}</div><p style="font-size:24px;opacity:.78;margin-bottom:26px;line-height:1.4">{d}</p><ul style="padding-left:26px;font-size:24px;line-height:1.85;color:#d6d2ca">{"".join(f"<li>{x}</li>" for x in it)}</ul></div>' for i, (n, d, it) in enumerate(PACOTES))
    P.append(pg(f'<div style="padding:100px 130px"><div class="lbl" style="color:{AMB};font-size:20px">03 · Pacotes</div><div class="serif" style="font-size:80px;margin:20px 0 46px">Escolha o tamanho do projeto.</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:36px">{pac}</div><div class="lbl" style="margin-top:36px;color:#8a8f98;font-size:18px">Investimento e forma de pagamento combinados na conversa.</div></div>', '<div class="beam" style="left:640px;top:300px;width:600px;height:500px;opacity:.5"></div>'))
    grid = ''.join(f'<div><img src="{img}/{k}-{c}.jpg" style="aspect-ratio:4/3;object-fit:cover;width:100%;border-radius:4px;box-shadow:0 26px 50px rgba(0,0,0,.55)"><div style="display:flex;justify-content:space-between;margin-top:16px;padding-top:14px;border-top:1px solid rgba(180,147,90,.3)"><b class="serif" style="font-size:32px">{n}</b><span class="lbl" style="font-size:16px;color:{AMB}">{s}</span></div></div>' for (k, n, s), c in zip(CASES, ['papelaria', 'embalagem', 'poster', 'celular', 'cartoes', 'papelaria']))
    P.append(pg(f'<div style="padding:96px 130px"><div class="lbl" style="color:{AMB};font-size:20px">04 · Trabalhos reais</div><div class="serif" style="font-size:80px;margin:20px 0 40px">Marcas que já saíram daqui.</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:34px">{grid}</div></div>'))
    P.append(pg(f'<img src="{img}/barzakh-cartao.jpg" style="position:absolute;right:0;top:0;width:900px;height:100%;object-fit:cover;object-position:top"><div style="position:absolute;right:900px;top:0;bottom:0;width:200px;background:linear-gradient(90deg,transparent,{INK});transform:translateX(200px)"></div><div style="padding:130px;width:860px"><div class="lbl" style="color:{AMB};font-size:20px">05 · O que você recebe</div><div class="serif" style="font-size:80px;line-height:1.02;margin:24px 0 40px">A marca aplicada, não só um logo.</div><ul style="font-size:30px;line-height:2;padding-left:30px;color:#d6d2ca"><li>Logo e versões em PNG, SVG e PDF</li><li>Cores com proporção e letras</li><li>Brand book para a equipe seguir</li><li>Instagram, cartão, papelaria</li><li>Mockups para divulgar a nova marca</li></ul></div>'))
    P.append(pg(f'<div style="height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:38px">{dk.mono_inline(170)}<div class="serif" style="font-size:120px;line-height:1">Vamos começar?</div><p style="font-size:30px;color:#c9c5bd">Responda esta proposta no WhatsApp e marcamos o briefing.</p><div style="background:{dk.OURO};color:{INK};font:700 34px Inter Tight;padding:26px 46px;border-radius:999px">wa.me/5598985621808</div><div class="lbl" style="color:#8a8f98;font-size:18px">{dk.ENDOSSO(18, "#8a8f98")} · São Luís, MA · lindsonalmeida.pages.dev</div></div>', fundo + '<div class="beam" style="left:577px;top:200px;width:600px;height:500px"></div>'))
    return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}@page{{size:1754px 1240px;margin:0}}</style></head><body>{"".join(P)}</body></html>'

def anuncio(img):
    T = []
    tela = lambda body: f'<div class="t grain" style="width:1080px;height:1350px;background:{INK};color:{OFF};position:relative;overflow:hidden">{body}</div>'
    fundo = f'<div class="conc" style="position:absolute;inset:0;opacity:.25"></div><div class="win" style="opacity:.6"></div>'
    T.append(tela(f'<img src="{img}/placa-hero.jpg" style="position:absolute;inset:0;width:1080px;height:1080px;object-fit:cover"><div style="position:absolute;left:0;right:0;top:760px;height:330px;background:linear-gradient(transparent,{INK})"></div><div style="position:absolute;left:70px;right:70px;bottom:80px"><div class="serif" style="font-size:88px;line-height:1">Sua marca parece do tamanho do seu negócio?</div><div class="lbl" style="margin-top:28px;color:{AMB};font-size:18px">arraste →</div></div>'))
    T.append(tela(f'{fundo}<div style="position:relative;padding:90px 70px 0"><div class="lbl" style="color:{AMB};font-size:18px">o problema</div><div class="serif" style="font-size:84px;line-height:1.02;margin-top:24px">Cada post de um jeito. O cliente não lembra de você.</div></div><img src="{img}/wf-celular.jpg" style="position:absolute;bottom:0;width:1080px;height:640px;object-fit:cover">'))
    T.append(tela(f'<img src="{img}/barzakh-cartao.jpg" style="position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover;object-position:top"><div style="position:absolute;left:0;right:0;bottom:0;height:560px;background:linear-gradient(transparent,{INK} 45%)"></div><div style="position:absolute;left:70px;right:70px;bottom:90px"><div class="lbl" style="color:{AMB};font-size:18px">a solução</div><div class="serif" style="font-size:72px;line-height:1.04;margin-top:18px">Identidade visual completa: logo, cores, letras e a marca aplicada.</div></div>'))
    T.append(tela(f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;height:1100px">{"".join(f"<img src={chr(34)}{img}/{k}-{c}.jpg{chr(34)} style={chr(34)}width:100%;height:100%;object-fit:cover{chr(34)}>" for k, c in [("curso", "poster"), ("duble", "cartoes"), ("oregano", "embalagem"), ("leo", "papelaria")])}</div><div style="padding:56px 70px;display:flex;justify-content:space-between;align-items:center;border-top:1px solid {AMB}"><div class="serif" style="font-size:64px">Cases reais</div><div class="lbl" style="color:{AMB};font-size:18px">São Luís · MA</div></div>'))
    T.append(tela(f'{fundo}<div class="beam" style="left:240px;top:160px;width:600px;height:500px"></div><div style="position:relative;height:100%;padding:90px 70px;display:flex;flex-direction:column;justify-content:space-between;align-items:center;text-align:center">{logo(40)}<div>{dk.mono_inline(200).replace("flex:none", "flex:none;margin:0 auto 50px")}<div class="serif" style="font-size:100px;line-height:1">Vamos tirar a sua marca do improviso?</div><div style="margin-top:50px;display:inline-block;background:{dk.OURO};color:{INK};font:700 34px Inter Tight;padding:24px 44px;border-radius:999px">Chame no WhatsApp</div></div><div class="lbl" style="color:#8a8f98;font-size:16px">sem promessa de milagre · processo em etapas</div></div>'))
    return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}.t{{margin-bottom:10px}}</style></head><body>{"".join(T)}</body></html>'

def placa_hero():
    return f'<div class="grain" style="position:relative;width:1200px;height:1200px;overflow:hidden">{dk.parede(1200, 1200)}<div style="position:absolute;left:230px;top:220px;filter:drop-shadow(0 60px 60px rgba(0,0,0,.55))">{dk.placa(740/680)}</div></div>'

if __name__ == '__main__':
    from playwright.sync_api import sync_playwright
    d = f'{OUT}/oferta'; os.makedirs(f'{d}/pagina/img', exist_ok=True); os.makedirs(f'{d}/anuncio', exist_ok=True)
    usados = set()
    for k, _, _ in CASES:
        for c in ['cartoes', 'papelaria', 'celular', 'poster', 'embalagem']:
            im = Image.open(f'{MK}/{k}-{c}.jpg'); im.thumbnail((1400, 1400)); im.save(f'{d}/pagina/img/{k}-{c}.jpg', quality=82)
    for n in ['papelaria', 'cartao']:
        im = Image.open(f'{OUT}/pinterest/pins/barzakh-{n}.jpg'); im = im.crop((0, 120, 1000, 1310)); im.save(f'{d}/pagina/img/barzakh-{n}.jpg', quality=84)
    with sync_playwright() as pw:
        b = pw.chromium.launch(proxy={'server': os.environ['HTTPS_PROXY']} if os.environ.get('HTTPS_PROXY') else None, args=['--allow-file-access-from-files'])
        p = b.new_page(viewport={'width': 1200, 'height': 1200})
        hp0 = f'{d}/pagina/_ph.html'; open(hp0, 'w').write(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}body{{margin:0}}</style></head><body>{placa_hero()}</body></html>')
        p.goto('file://' + hp0, wait_until='networkidle'); p.wait_for_timeout(600); p.screenshot(path=f'{d}/pagina/img/_ph.png')
        Image.open(f'{d}/pagina/img/_ph.png').convert('RGB').save(f'{d}/pagina/img/placa-hero.jpg', quality=86); os.remove(f'{d}/pagina/img/_ph.png'); os.remove(hp0)
        # a página publicada não lê arquivos locais: CSS do escuro.py aponta o concreto para img/concreto.jpg
        Image.open(dk.CONCRETO[7:]).convert('RGB').resize((1400, 933)).save(f'{d}/pagina/img/concreto.jpg', quality=80)
        open(f'{d}/pagina/index.html', 'w').write(pagina('img').replace(dk.CONCRETO, 'img/concreto.jpg'))
        p.set_viewport_size({'width': 1440, 'height': 900})
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
