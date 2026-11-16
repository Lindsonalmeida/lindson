# Projeto Designer v3 (conta Leandro, 16/11/2026): monta os cases do Behance, os pins do Pinterest e a folha.
# 16/11: conceito, fecho e rodapé dos pins no padrão escuro da placa aprovada (escuro.py). Antes: visual editorial claro (Collins + Porto Rocha/Manual + Lundgren+Lindqvist, ver PESQUISA.md).
# Uso: BB_TMP=<tmp> python3 compor.py <texturas> <mockups> <saida_v2>
import sys, os, html, csv, importlib.util
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.argv, ARGS = sys.argv[:2], sys.argv[1:]
spec = importlib.util.spec_from_file_location('tx', os.path.join(HERE, 'texturas.py')); tx = importlib.util.module_from_spec(spec); spec.loader.exec_module(tx)
TEX, MK, OUT = [os.path.abspath(a) for a in ARGS[:3]]
spec3 = importlib.util.spec_from_file_location('dk', os.path.join(HERE, 'escuro.py')); dk = importlib.util.module_from_spec(spec3); spec3.loader.exec_module(dk)
bb = tx.bb; e = html.escape
STUDIO = 'Barzakh · um estúdio Al Kántara'
OFF, INK, AMB, LAP = '#EEEAE2', '#0A0C10', '#B4935A', '#2B3A8F'
# id do case v1 -> chave do brand book
CASES = [('leo-pinto', 'leo'), ('real-time', 'realtime'), ('processo-legislativo', 'curso'), ('wf-celulares', 'wf'), ('oregano-turbo', 'oregano'), ('duble', 'duble')]
spec2 = importlib.util.spec_from_file_location('ct', os.path.join(HERE, '../../gerador/conteudo.py')); ct = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(ct)
INFO = {c['id']: c for c in ct.CASES}
FONTS = 'https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;700&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@500&display=swap'
CSS = dk.CSS + f'*{{box-sizing:border-box;margin:0}}body{{background:{OFF};color:{INK};font-family:Inter Tight}}.m{{position:relative;overflow:hidden}}.lbl{{font:500 15px "JetBrains Mono";letter-spacing:.18em;text-transform:uppercase}}img{{display:block}}'

def f(p): return 'file://' + p

def modulos(cid, k):
    c = bb.C[k]; I = INFO[cid]; nome = tx.MARCAS[k]; m = lambda n: f(f'{MK}/{k}-{n}.jpg')
    logo = f(f'{TEX}/{k}/logo.png')
    disp = f"font-family:{c['disp']};font-weight:{c['dw']};text-transform:{'uppercase' if c['up'] else 'none'}"
    pal = c['paleta']; tot = sum(p[2] for p in pal)
    mods = []
    mods.append(('01-hero', 1050, f'<img src="{m("cartoes")}" style="width:1400px;height:1050px;object-fit:cover">'))
    # 02 e fecho no padrão escuro aprovado (placa em arco: concreto, ouro só em detalhe, brilho Lápis)
    mods.append(('02-conceito', 760, f'''<div class="grain" style="position:absolute;inset:0;background:{dk.OB}"><div class="conc" style="position:absolute;inset:0;opacity:.22"></div><div class="win" style="opacity:.6"></div><div class="beam" style="left:760px;top:120px;width:700px;height:520px;opacity:.6"></div></div>
<div style="position:relative;padding:110px 120px;height:100%;display:flex;flex-direction:column;justify-content:space-between;color:{dk.MA}">
<div style="display:flex;justify-content:space-between;color:{dk.BR}" class="lbl"><span>{e(nome)}</span><span>{e(I["cliente"])}</span><span>2026</span></div>
<div style="font:400 104px/1 'Instrument Serif';letter-spacing:-.01em;max-width:1120px"><span class="ouro">“</span>{e(tx.FRASE[k])}<span class="ouro">”</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:80px;font:300 21px/1.55 Inter Tight;color:#c9c5bd"><p style="border-top:1px solid rgba(180,147,90,.4);padding-top:22px"><b class="lbl" style="display:block;margin-bottom:12px;color:{dk.BR}">Desafio</b>{e(I["desafio"])}</p><p style="border-top:1px solid rgba(180,147,90,.4);padding-top:22px"><b class="lbl" style="display:block;margin-bottom:12px;color:{dk.BR}">Conceito</b>{e(I["conceito"])}</p></div></div>'''))
    mods.append(('03-logo', 900, f'<div style="height:100%;background:{c["bg"]};display:grid;place-items:center"><img src="{logo}" style="width:760px"></div><div class="lbl" style="position:absolute;left:60px;bottom:50px;color:{c["fg"]};opacity:.6">Assinatura principal</div>'))
    mods.append(('04-versoes', 520, f'''<div style="height:100%;display:grid;grid-template-columns:1fr 1fr 1fr">
<div style="background:{c["bg2"]};display:grid;place-items:center;padding:70px"><img src="{logo}" style="width:100%"></div>
<div style="background:{c["ac"]};display:grid;place-items:center"><div style="width:250px;height:250px;border-radius:56px;background:{c["bg"]};display:grid;place-items:center;padding:34px;box-shadow:0 30px 60px #0003"><img src="{logo}" style="width:100%"></div></div>
<div style="overflow:hidden"><img src="{m('papelaria')}" style="width:1400px;height:1050px;object-fit:cover;margin:-330px 0 0 -560px"></div></div></div>'''))
    cols = ''.join(f'<div style="flex:{max(p[2], 7)};background:{p[1]};padding:28px 22px;display:flex;flex-direction:column;justify-content:flex-end;color:{"#111" if sum(tx.bb.rgb(p[1])) > 450 else "#fff"}"><div style="font:700 22px Inter Tight">{e(p[0])}</div><div class="lbl" style="font-size:13px;margin-top:6px;opacity:.75">{p[1].upper()} · {p[2]}%</div></div>' for p in pal)
    mods.append(('05-paleta', 640, f'<div style="height:100%;display:flex">{cols}</div>'))
    fn = c['fonts'].split('&family=')[0].split(':')[0].replace('+', ' '); fb = c['body'].strip("'")
    mods.append(('06-tipografia', 760, f'''<link href="https://fonts.googleapis.com/css2?family={c["fonts"]}&display=swap" rel="stylesheet">
<div style="height:100%;display:grid;grid-template-columns:1.1fr 1fr;align-items:center;padding:0 120px;gap:80px">
<div style="{disp};font-size:420px;line-height:.8;color:{c["bg"] if c["bg"] != "#000000" else INK}">Aa</div>
<div><div class="lbl">Títulos</div><div style="{disp};font-size:64px;margin:10px 0 40px">{e(fn)}</div><div class="lbl">Texto</div><div style="font:500 40px {c["body"]};margin:10px 0 30px">{e(fb)}</div>
<div style="font:400 22px/1.5 {c["body"]};color:#444">{e(c["essencia"][0])}. {e(c["essencia"][1])}. {e(c["essencia"][2])}.</div></div></div>'''))
    for n, h in [('papelaria', 1050), ('celular', 1050)]:
        mods.append((f'{len(mods)+1:02d}-{n}', h, f'<img src="{m(n)}" style="width:1400px;height:{h}px;object-fit:cover">'))
    mods.append((f'{len(mods)+1:02d}-detalhe', 820, f'<img src="{m("cartoes")}" style="width:2400px;height:1800px;object-fit:cover;margin:-520px 0 0 -700px">'))
    for n in (['embalagem', 'poster'] if k == 'leo' else ['embalagem', 'poster', 'outdoor']):  # Leo: sem outdoor (nada de cara de campanha)
        mods.append((f'{len(mods)+1:02d}-{n}', 1050, f'<img src="{m(n)}" style="width:1400px;height:1050px;object-fit:cover">'))
    mods.append((f'{len(mods)+1:02d}-fecho', 620, f'''<div class="grain" style="position:absolute;inset:0;background:{dk.OB}"><div class="conc" style="position:absolute;inset:0;opacity:.35"></div><div class="win" style="opacity:.75"></div><div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 50%,transparent 20%,rgba(10,12,16,.8))"></div><div class="beam" style="left:430px;top:120px;width:540px;height:380px;opacity:.7"></div></div>
<div style="position:relative;height:100%;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;padding:0 110px;gap:70px;color:{dk.MA}">
<div style="justify-self:end;background:{c["bg"]};padding:30px 40px;border-radius:12px;box-shadow:0 30px 60px rgba(0,0,0,.6)"><img src="{logo}" style="width:260px"></div>
<div style="text-align:center"><div style="position:relative;width:170px;height:170px;margin:0 auto">{dk.mono(170)}</div><div style="font:400 78px/1 'Instrument Serif';margin-top:26px">Obrigado.</div></div>
<div><div class="foil" style="width:300px;height:56px;-webkit-mask-image:{dk.mask("logotipo-mono-branco")};mask-image:{dk.mask("logotipo-mono-branco")};-webkit-mask-position:left;mask-position:left"></div><div class="lbl" style="margin-top:20px;color:{dk.BR};font-size:13px;line-height:1.9">Um estúdio Al Kántara<br>Identidade visual · brand book<br>web design · São Luís, MA</div></div></div>'''))
    return mods

def pin(k, n, titulo, sub):
    return f'''<div class="m" style="width:1000px;height:1500px;background:{dk.OB}">
<img src="{f(f'{MK}/{k}-{n}-r.jpg')}" style="width:1000px;height:1310px;object-fit:cover">
{dk.rodape_pin(e(titulo), e(sub))}</div>'''

def pins_barzakh():
    """4 pins só da marca Barzakh, no padrão da placa aprovada, cada um com composição própria."""
    P = []
    # 1 · placa em arco na parede (a peça aprovada, de frente, grande)
    P.append(('placa', 'Placa em arco · Barzakh', 'Sinalização · metal escovado e ouro', f'''<div class="grain" style="position:absolute;inset:0;overflow:hidden">{dk.parede(1000, 1500)}</div>
<div style="position:absolute;left:110px;top:250px;filter:drop-shadow(0 60px 60px rgba(0,0,0,.55))">{dk.placa(780/680)}</div>
<div class="lbl" style="position:absolute;left:56px;top:60px;color:{dk.MA};opacity:.7">01 · Estúdio</div>'''))
    # 2 · cartão em hot stamping, close diagonal sobre papel escuro
    P.append(('cartao', 'Cartão em hot stamping · Barzakh', 'Papelaria · ouro sobre papel grafite', f'''<div class="paper grain" style="position:absolute;inset:0;background-color:#0e1014;overflow:hidden"><div class="win" style="opacity:.75"></div><div class="beam" style="left:150px;top:300px;width:800px;height:700px;opacity:.55"></div></div>
<div style="position:absolute;left:-40px;top:170px;transform:perspective(1800px) rotateX(30deg) rotateZ(-18deg)">{dk.cartao(820, 480)}</div>
<div style="position:absolute;left:330px;top:760px;transform:perspective(1800px) rotateX(30deg) rotateZ(9deg)">{dk.cartao(700, 410, True)}</div>
<div class="lbl" style="position:absolute;right:56px;top:60px;color:{dk.BR}">02 · Hot stamping</div>'''))
    # 3 · papelaria escura em flat lay: timbrado, envelope Lápis, cartão
    P.append(('papelaria', 'Papelaria escura · Barzakh', 'Timbrado, envelope e cartão', f'''<div class="grain" style="position:absolute;inset:0;overflow:hidden">{dk.parede(1000, 1500, .7)}<div style="position:absolute;inset:0;background:rgba(10,12,16,.45)"></div></div>
<div style="position:absolute;left:90px;top:110px;transform:rotate(-6deg)">{dk.timbrado(520)}</div>
<div style="position:absolute;left:400px;top:700px;transform:rotate(8deg)">{dk.envelope(560)}</div>
<div style="position:absolute;left:560px;top:250px;transform:rotate(12deg)">{dk.cartao(360, 210)}</div>
<div class="lbl" style="position:absolute;left:56px;top:1210px;color:{dk.MA};opacity:.7">03 · Papelaria</div>'''))
    # 4 · avatar: o monolito no círculo, em três tamanhos, com a régua do perfil
    av = lambda d: f'<div style="position:relative;width:{d}px;height:{d}px;border-radius:50%;background:radial-gradient(circle at 50% 45%,#1f2747,{dk.OB} 70%);box-shadow:0 0 0 1px rgba(180,147,90,.5),0 40px 80px rgba(0,0,0,.6);overflow:hidden;flex:none">{dk.mono(d*.62, d*.19, d*.17)}</div>'
    P.append(('avatar', 'Avatar do perfil · Barzakh', 'Instagram, WhatsApp e Behance', f'''<div class="grain" style="position:absolute;inset:0;background:{dk.OB};overflow:hidden"><div class="conc" style="position:absolute;inset:0;opacity:.18"></div><div class="beam" style="left:100px;top:160px;width:800px;height:760px;opacity:.75"></div></div>
<div style="position:absolute;left:180px;top:150px">{av(640)}</div>
<div style="position:absolute;left:180px;right:180px;top:880px;display:flex;justify-content:space-between;align-items:end">{av(200)}{av(120)}{av(64)}</div>
<div style="position:absolute;left:180px;right:180px;top:1110px;display:flex;justify-content:space-between;color:{dk.BR}" class="lbl"><span>200 px</span><span>120 px</span><span>64 px</span></div>
<div class="lbl" style="position:absolute;left:56px;top:60px;color:{dk.MA};opacity:.7">04 · Avatar</div>'''))
    return [(n, t, sub, f'<div class="m" style="width:1000px;height:1500px;background:{dk.OB}">{body}{dk.rodape_pin(t, sub)}</div>') for n, t, sub, body in P]

def placa_capa():
    """Capa 808x632 sem texto: a placa aprovada no concreto."""
    return f'''<div class="grain" style="position:absolute;inset:0;overflow:hidden">{dk.parede(808, 632)}</div><div style="position:absolute;left:174px;top:62px;filter:drop-shadow(0 40px 40px rgba(0,0,0,.55))">{dk.placa(460/680)}</div>'''

PASTAS = [
    ('Identidade visual para pequenas empresas', 'Cases reais de identidade visual para negócios locais brasileiros: logo, paleta de cores, tipografia e a marca aplicada em mockups. Branding para loja, clínica, curso, produtora e restaurante.'),
    ('Mockup de cartão de visita e papelaria', 'Cartão de visita, papel timbrado e envelope com identidade visual profissional. Inspiração de papelaria de marca e mockup de cartão de visita.'),
    ('Instagram com identidade visual', 'Perfil e feed de Instagram na identidade visual da marca: posts, grade e foto de perfil que parecem do tamanho do negócio.'),
    ('Embalagem e branding de produto', 'Embalagem, caixa, copo e sacola com a identidade visual da marca. Ideias de packaging e branding de produto para pequenas empresas.'),
    ('Pôster e outdoor de marca', 'Pôster, quadro e outdoor com a marca aplicada: identidade visual vista de longe, com frase de conceito e cor da marca.'),
    ('Identidade visual para restaurante e pizzaria', 'Branding de comida: identidade visual para pizzaria e restaurante, embalagem, cartão e Instagram com a mesma marca.'),
]
PIN_CENAS = [('cartoes', 'Cartão de visita', 1), ('papelaria', 'Papelaria', 1), ('celular', 'Instagram', 2), ('embalagem', 'Embalagem', 3), ('poster', 'Pôster', 4)]
NICHO = {'leo': 'comunicação pública', 'realtime': 'produtora audiovisual', 'curso': 'curso online', 'wf': 'loja de iPhone', 'oregano': 'marketing para pizzaria', 'duble': 'aplicativo'}

if __name__ == '__main__':
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch(proxy={'server': os.environ['HTTPS_PROXY']} if os.environ.get('HTTPS_PROXY') else None, args=['--allow-file-access-from-files'])
        p = b.new_page(viewport={'width': 1400, 'height': 1000})
        def shot(body, w, h, out):
            hp = OUT + '/_tmp.html'; open(hp, 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><link href="{FONTS}" rel="stylesheet"><style>{CSS}</style></head><body><div class="m" style="width:{w}px;height:{h}px">{body}</div></body></html>')
            p.set_viewport_size({'width': w, 'height': h}); p.goto('file://' + hp, wait_until='networkidle'); p.evaluate('document.fonts.ready'); p.wait_for_timeout(250)
            p.screenshot(path=out + '.png', clip={'x': 0, 'y': 0, 'width': w, 'height': h})
            Image.open(out + '.png').convert('RGB').save(out + '.jpg', quality=88); os.remove(out + '.png')
        rows = []
        for cid, k in CASES:
            d = f'{OUT}/behance/{cid}'; os.makedirs(d, exist_ok=True)
            # capa 808x632 sem texto: recorte do mockup de cartões
            im = Image.open(f'{MK}/{k}-cartoes.jpg'); W, H = im.size; cw = int(H * 808 / 632); ch = int(cw * 632 / 808)
            im.crop(((W - cw) // 2, (H - ch) // 2, (W + cw) // 2, (H + ch) // 2)).resize((808, 632), Image.LANCZOS).save(f'{d}/00-capa-808x632.jpg', quality=92)
            for nm, h, body in modulos(cid, k): shot(body, 1400, h, f'{d}/{nm}')
            I = INFO[cid]
            open(f'{d}/TEXTO.md', 'w').write(f'''# {I["titulo"]}

**Capa:** `00-capa-808x632.jpg` (sem texto, como pede a curadoria). **Módulos:** 01 a 14 em ordem, largura 1400 px, espaçamento 0.

**Título:** {I["titulo"]}
**Cliente:** {I["cliente"]}
**Frase de conceito:** "{tx.FRASE[k]}"

**Descrição:**
{I["desafio"]}
{I["conceito"]}
Entregas: {I["entregas"]}
Mockups: renders 3D próprios do estúdio (Three.js), com o logo e as cores oficiais do brand book.

**Tags:** {I["tags"]}, mockup, papelaria, cartão de visita
**Ferramentas:** Figma, Adobe Illustrator, Three.js, Claude
**Créditos:** Direção de arte e design: {STUDIO} (São Luís, MA)
''')
            for n, nomec, pi in PIN_CENAS:
                pasta = PASTAS[5][0] if (k == 'oregano' and n in ('embalagem', 'cartoes')) else PASTAS[0][0] if n == 'poster' and k in ('leo', 'curso') else PASTAS[pi][0]
                titulo = f'{nomec} · {tx.MARCAS[k]}'
                out = f'{OUT}/pinterest/pins/{k}-{n}'; os.makedirs(os.path.dirname(out), exist_ok=True)
                shot(pin(k, n, titulo, f'Identidade visual · {NICHO[k]}'), 1000, 1500, out)
                tit = f'{nomec} com identidade visual: {tx.MARCAS[k]} ({NICHO[k]})'
                rows.append(dict(Title=tit[:100], **{'Media URL': f'pinterest/pins/{k}-{n}.jpg', 'Pinterest board': pasta},
                                 Description=f'{nomec} da identidade visual de {tx.MARCAS[k]}, {NICHO[k]}. Projeto completo do {STUDIO}, estúdio de identidade visual e branding em São Luís (MA): logo, paleta de cores, tipografia e aplicações reais. Inspiração de branding para pequenas empresas.'[:500],
                                 Link='https://lindsonalmeida.pages.dev/site/identidade/', Keywords=f'identidade visual, branding, {nomec.lower()}, mockup, logo, {NICHO[k]}',
                                 Alt=f'Mockup fotorrealista de {nomec.lower()} com o logo de {tx.MARCAS[k]} sobre a mesa, luz natural.'))
            print(cid, 'ok')
        # 7º case: Barzakh · identidade do estúdio (capa = placa aprovada; 10 módulos do manual)
        d = f'{OUT}/behance/barzakh'; os.makedirs(d, exist_ok=True)
        p.set_viewport_size({'width': 808, 'height': 632})
        hp = OUT + '/_tmp.html'; open(hp, 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><link href="{FONTS}" rel="stylesheet"><style>{CSS}</style></head><body><div class="m" style="width:808px;height:632px">{placa_capa()}</div></body></html>')
        p2 = b.new_page(viewport={'width': 808, 'height': 632}, device_scale_factor=2); p2.goto('file://' + hp, wait_until='networkidle'); p2.wait_for_timeout(400)
        p2.screenshot(path=d + '/_c.png'); Image.open(d + '/_c.png').convert('RGB').resize((808, 632), Image.LANCZOS).save(d + '/00-capa-808x632.jpg', quality=92); os.remove(d + '/_c.png'); p2.close()
        MAN = os.path.join(HERE, '../marca/entregas/paginas/barzakh-manual-de-marca')
        for i, (pg, nm) in enumerate([(1, 'abertura'), (5, 'construcao'), (7, 'monolito'), (8, 'versoes'), (13, 'paleta'), (16, 'tipografia'), (18, 'horizonte'), (27, 'papelaria'), (29, 'hot-stamping'), (31, 'placa')]):
            Image.open(f'{MAN}/{pg:02d}.jpg').convert('RGB').resize((1400, 788), Image.LANCZOS).save(f'{d}/{i+1:02d}-{nm}.jpg', quality=90)
        open(f'{d}/TEXTO.md', 'w').write('''# Barzakh · identidade do estúdio

**Capa:** `00-capa-808x632.jpg` (sem texto: a placa em arco aprovada). **Módulos:** 01 a 10, largura 1400 px, espaçamento 0, fundo #0A0C10.

**Título:** Barzakh · identidade do estúdio
**Cliente:** Barzakh · um estúdio Al Kántara (marca própria)
**Frase de conceito:** "Dois mares que se encontram e não se misturam."

**Descrição:**
Barzakh é o ponto exato da travessia: onde uma marca deixa de ser rascunho e ainda está tomando forma. O símbolo usa a régua dos arcos do grupo Al Kántara e ganha o reflexo abaixo da linha do horizonte. A variação monolito, em arco cheio, foi feita para gravar: hot stamping em ouro, placa de metal, avatar.
Entregas: branding book, manual de marca, logos (SVG e PNG), paleta com proporção, tipografia, papelaria, perfil e placa do estúdio.

**Tags:** identidade visual, branding, brand book, manual de marca, hot stamping, papelaria, São Luís
**Ferramentas:** Figma, Adobe Illustrator, Claude
**Créditos:** Direção criativa: Lindson Almeida. Fotos do manual: Wikimedia Commons (licenças livres, créditos no manual).
''')
        for n, t, sub, body in pins_barzakh():
            shot(body, 1000, 1500, f'{OUT}/pinterest/pins/barzakh-{n}')
        # PINS.csv: mantém os textos SEO já revisados (30 pins) e acrescenta os 4 da marca
        csvp = f'{OUT}/pinterest/PINS.csv'
        old = [r for r in csv.DictReader(open(csvp))] if os.path.exists(csvp) else rows
        old = [r for r in old if 'pins/barzakh-' not in r['Media URL']]
        BZ = {'placa': ('Placa em arco com logo em ouro: identidade visual do estúdio Barzakh', 'Pôster e outdoor de marca', 'Placa em arco de metal escovado grafite presa no concreto, com o símbolo monolito em ouro escovado e um brilho azul Lápis atrás.', 'placa em arco, sinalização, fachada'),
              'cartao': ('Cartão de visita em hot stamping dourado: identidade visual Barzakh', 'Mockup de cartão de visita e papelaria', 'Cartões de visita em papel grafite com o símbolo monolito em hot stamping dourado, luz de janela na diagonal.', 'cartão de visita, hot stamping, papelaria'),
              'papelaria': ('Papelaria escura com ouro: identidade visual do estúdio Barzakh', 'Mockup de cartão de visita e papelaria', 'Papel timbrado grafite, envelope azul Lápis e cartão com o monolito em ouro, sobre concreto com sombra de janela.', 'papelaria, papel timbrado, envelope'),
              'avatar': ('Avatar de Instagram com símbolo em ouro: identidade visual Barzakh', 'Instagram com identidade visual', 'Avatar redondo do estúdio Barzakh: o símbolo monolito em ouro escovado sobre Obsidiana, em 200, 120 e 64 px.', 'avatar, foto de perfil, Instagram')}
        for n, (tt, pasta, alt, kw) in BZ.items():
            old.append({'Title': tt[:100], 'Media URL': f'pinterest/pins/barzakh-{n}.jpg', 'Pinterest board': pasta,
                        'Description': f'{alt} Identidade visual do próprio estúdio: Barzakh · um estúdio Al Kántara, estúdio de branding em São Luís (MA). Direção criativa: Lindson Almeida. Inspiração de identidade visual premium escura, com ouro e azul, para pequenas empresas.'[:500],
                        'Link': 'https://lindsonalmeida.pages.dev/site/identidade/', 'Keywords': f'identidade visual, branding, {kw}, Barzakh', 'Alt': alt})
        with open(csvp, 'w', newline='') as fh:
            w = csv.DictWriter(fh, fieldnames=list(old[0])); w.writeheader(); w.writerows(old)
        b.close()
    os.remove(OUT + '/_tmp.html')
