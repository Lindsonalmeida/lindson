# Projeto Designer v2 (conta Leandro, 16/11/2026): monta os cases do Behance, os pins do Pinterest e a folha.
# Visual editorial claro (Collins + Porto Rocha/Manual + Lundgren+Lindqvist, ver PESQUISA.md).
# Uso: BB_TMP=<tmp> python3 compor.py <texturas> <mockups> <saida_v2>
import sys, os, html, csv, importlib.util
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.argv, ARGS = sys.argv[:2], sys.argv[1:]
spec = importlib.util.spec_from_file_location('tx', os.path.join(HERE, 'texturas.py')); tx = importlib.util.module_from_spec(spec); spec.loader.exec_module(tx)
TEX, MK, OUT = [os.path.abspath(a) for a in ARGS[:3]]
bb = tx.bb; e = html.escape
STUDIO = 'Lindson Almeida Studio'
OFF, INK, AMB = '#F2EFE9', '#0A0A0A', '#F5C518'
# id do case v1 -> chave do brand book
CASES = [('leo-pinto', 'leo'), ('real-time', 'realtime'), ('processo-legislativo', 'curso'), ('wf-celulares', 'wf'), ('oregano-turbo', 'oregano'), ('duble', 'duble')]
spec2 = importlib.util.spec_from_file_location('ct', os.path.join(HERE, '../../gerador/conteudo.py')); ct = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(ct)
INFO = {c['id']: c for c in ct.CASES}
FONTS = 'https://fonts.googleapis.com/css2?family=Anton&family=Manrope:wght@400;500;700&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@500&display=swap'
CSS = f'*{{box-sizing:border-box;margin:0}}body{{background:{OFF};color:{INK};font-family:Manrope}}.m{{position:relative;overflow:hidden}}.lbl{{font:500 15px "JetBrains Mono";letter-spacing:.18em;text-transform:uppercase}}img{{display:block}}'

def f(p): return 'file://' + p

def modulos(cid, k):
    c = bb.C[k]; I = INFO[cid]; nome = tx.MARCAS[k]; m = lambda n: f(f'{MK}/{k}-{n}.jpg')
    logo = f(f'{TEX}/{k}/logo.png')
    disp = f"font-family:{c['disp']};font-weight:{c['dw']};text-transform:{'uppercase' if c['up'] else 'none'}"
    pal = c['paleta']; tot = sum(p[2] for p in pal)
    mods = []
    mods.append(('01-hero', 1050, f'<img src="{m("cartoes")}" style="width:1400px;height:1050px;object-fit:cover">'))
    mods.append(('02-conceito', 760, f'''<div style="padding:110px 120px;height:100%;display:flex;flex-direction:column;justify-content:space-between">
<div style="display:flex;justify-content:space-between" class="lbl"><span>{e(nome)}</span><span>{e(I["cliente"])}</span><span>2026</span></div>
<div style="font:400 104px/1 'Instrument Serif';letter-spacing:-.01em;max-width:1120px">“{e(tx.FRASE[k])}”</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:80px;font:400 21px/1.55 Manrope;color:#3a3a3a"><p><b class="lbl" style="display:block;margin-bottom:12px;color:{INK}">Desafio</b>{e(I["desafio"])}</p><p><b class="lbl" style="display:block;margin-bottom:12px;color:{INK}">Conceito</b>{e(I["conceito"])}</p></div></div>'''))
    mods.append(('03-logo', 900, f'<div style="height:100%;background:{c["bg"]};display:grid;place-items:center"><img src="{logo}" style="width:760px"></div><div class="lbl" style="position:absolute;left:60px;bottom:50px;color:{c["fg"]};opacity:.6">Assinatura principal</div>'))
    mods.append(('04-versoes', 520, f'''<div style="height:100%;display:grid;grid-template-columns:1fr 1fr 1fr">
<div style="background:{c["bg2"]};display:grid;place-items:center;padding:70px"><img src="{logo}" style="width:100%"></div>
<div style="background:{c["ac"]};display:grid;place-items:center"><div style="width:250px;height:250px;border-radius:56px;background:{c["bg"]};display:grid;place-items:center;padding:34px;box-shadow:0 30px 60px #0003"><img src="{logo}" style="width:100%"></div></div>
<div style="overflow:hidden"><img src="{m('papelaria')}" style="width:1400px;height:1050px;object-fit:cover;margin:-330px 0 0 -560px"></div></div></div>'''))
    cols = ''.join(f'<div style="flex:{max(p[2], 7)};background:{p[1]};padding:28px 22px;display:flex;flex-direction:column;justify-content:flex-end;color:{"#111" if sum(tx.bb.rgb(p[1])) > 450 else "#fff"}"><div style="font:700 22px Manrope">{e(p[0])}</div><div class="lbl" style="font-size:13px;margin-top:6px;opacity:.75">{p[1].upper()} · {p[2]}%</div></div>' for p in pal)
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
    mods.append((f'{len(mods)+1:02d}-fecho', 620, f'''<div style="height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:34px">
<div style="background:{c["bg"]};padding:34px 46px;border-radius:14px"><img src="{logo}" style="width:300px"></div><div style="font:400 70px/1 'Instrument Serif'">Obrigado.</div>
<div class="lbl">{STUDIO} · Identidade visual, brand book e web design · São Luís, MA</div><div style="width:60px;height:6px;background:{AMB}"></div></div>'''))
    return mods

def pin(k, n, titulo, sub):
    return f'''<div class="m" style="width:1000px;height:1500px;background:{OFF}">
<img src="{f(f'{MK}/{k}-{n}-r.jpg')}" style="width:1000px;height:1320px;object-fit:cover">
<div style="position:absolute;left:0;right:0;bottom:0;height:180px;padding:34px 56px;display:flex;justify-content:space-between;align-items:center">
<div><div style="font:400 50px/1.05 'Instrument Serif'">{e(titulo)}</div><div class="lbl" style="margin-top:12px;color:#555">{e(sub)}</div></div>
<div style="text-align:right"><div style="width:44px;height:6px;background:{AMB};margin-left:auto"></div><div class="lbl" style="margin-top:14px;font-size:13px">Lindson Almeida<br>Studio</div></div></div></div>'''

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
        with open(f'{OUT}/pinterest/PINS.csv', 'w', newline='') as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
        b.close()
    os.remove(OUT + '/_tmp.html')
