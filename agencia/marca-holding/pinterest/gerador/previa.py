# Capas de pasta (1000x1000, recorte do pin, sem texto) + prévia do perfil (conta Zuleide, 18/11/2026)
import os, json
from PIL import Image
from playwright.sync_api import sync_playwright
O = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')); V3 = '/home/user/lindson/agencia/marca-lindson/projeto-designer/v3/pinterest/pins'
PL = json.load(open(O + '/plano.json'))
def src(p): return p.replace('V3/', V3 + '/').replace('NOVO/', O + '/pins/')
for i, b in enumerate(PL['pastas'], 1):
    im = Image.open(src(b['capa_origem'])).convert('RGB'); y = b.get('capa_y', 180)
    im.crop((0, y, 1000, y + 1000)).save(f"{O}/capas/pasta-{i:02d}-{b['slug']}.jpg", quality=90)
pins = [src(p['imagem']) for p in PL['calendario'][:18]]
fu = lambda p: 'file://' + p
boards = ''.join(f'<div><img src="{fu(O)}/capas/pasta-{i:02d}-{b["slug"]}.jpg" style="width:100%;border-radius:16px"><div style="font:600 15px Inter Tight;margin-top:8px">{b["nome"]}</div><div style="font:12px Inter Tight;color:#767676">Pasta · seções: {len(b["secoes"])}</div></div>' for i, b in enumerate(PL['pastas'], 1))
mas = ''.join(f'<img src="{fu(p)}" style="width:100%;border-radius:16px;margin-bottom:14px;display:block">' for p in pins)
pf = PL['perfil']
H = f'''<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;600;700&display=swap" rel="stylesheet"></head>
<body style="margin:0;background:#fff;font-family:Inter Tight;color:#111;width:1440px">
<div style="height:64px;display:flex;align-items:center;padding:0 24px;gap:14px;border-bottom:1px solid #eee"><div style="width:30px;height:30px;border-radius:50%;background:#e60023"></div><div style="flex:1;height:44px;border-radius:22px;background:#f1f1f1;padding:0 18px;display:flex;align-items:center;color:#767676">Pesquisar · identidade visual luxo</div></div>
<div style="width:1000px;height:562px;margin:24px auto 0;border-radius:28px;overflow:hidden"><img src="{fu(O)}/capas/capa-do-perfil-1600x900.jpg" style="width:100%"></div>
<div style="text-align:center;margin-top:-60px"><img src="{fu('/home/user/lindson/agencia/marca-lindson/projeto-designer/v3/marca/logos/png/barzakh-avatar-obsidiana.png')}" style="width:120px;height:120px;border-radius:50%;border:5px solid #fff;object-fit:cover;background:#0a0c10">
<div style="font:700 34px Inter Tight;margin-top:8px">{pf["nome"]}</div><div style="color:#767676;margin-top:4px">{pf["usuario"]} · alkantaragroup.pages.dev</div>
<div style="max-width:620px;margin:10px auto 0;font-size:16px;line-height:1.45">{pf["bio"]}</div>
<div style="margin-top:16px;display:flex;gap:10px;justify-content:center"><span style="background:#efefef;padding:12px 18px;border-radius:24px;font-weight:600">Compartilhar</span><span style="background:#e60023;color:#fff;padding:12px 18px;border-radius:24px;font-weight:600">Seguir</span></div></div>
<div style="display:flex;gap:28px;justify-content:center;margin:30px 0 18px;font-weight:600"><span>Criados</span><span style="border-bottom:3px solid #111;padding-bottom:6px">Salvos</span></div>
<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:16px;padding:0 40px">{boards}</div>
<div style="columns:6;column-gap:14px;padding:30px 40px 0;height:1500px;overflow:hidden">{mas}</div></body></html>'''
hp = O + '/gerador/_p.html'; open(hp, 'w').write(H)
with sync_playwright() as pw:
    b = pw.chromium.launch(proxy={'server': os.environ['HTTPS_PROXY']} if os.environ.get('HTTPS_PROXY') else None, args=['--allow-file-access-from-files'])
    p = b.new_page(viewport={'width': 1440, 'height': 2400}); p.goto('file://' + hp, wait_until='networkidle'); p.wait_for_timeout(600)
    p.screenshot(path=O + '/previa.png', full_page=True)
Image.open(O + '/previa.png').convert('RGB').save(O + '/previa.jpg', quality=85); os.remove(O + '/previa.png'); os.remove(hp)
# refs-3: as 3 referências escolhidas (TEMPLATE.md)
R = [O + '/pesquisa/' + n for n in ['01-pinterest-busca-branding-luxo.jpg', '05-koto-uk.jpg', '07-porto-rocha-us-br.jpg']]
c = Image.new('RGB', (2160, 500), 'white')
for i, r in enumerate(R): c.paste(Image.open(r).convert('RGB').resize((720, 500)), (i * 720, 0))
c.save(O + '/refs-3.jpg', quality=85); print('ok')
