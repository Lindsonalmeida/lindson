# Projeto Designer v2 (conta Leandro, 16/11/2026): renderiza os mockups 3D (cenas.js) de cada marca.
# Uso: python3 mockups.py <pasta_texturas> <saida> <pasta node_modules/three> [marca:cena ...] [--retrato]
import sys, os, json, base64, urllib.parse, random
from PIL import Image, ImageFilter, ImageChops, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
TEX, OUT, THREE = [os.path.abspath(a) for a in sys.argv[1:4]]
RET = '--retrato' in sys.argv
JOBS = [a for a in sys.argv[4:] if ':' in a]
PAL = {  # chão/parede neutros que conversam com a paleta oficial de cada marca
    'leo': dict(bg='#082063', bg2='#2350F5', ac='#FFC20E', chao='#c9c3b8', parede='#e8e3da', fachada='#3a3d44'),
    'realtime': dict(bg='#05070B', bg2='#11161F', ac='#2E9BFF', chao='#8d9097', parede='#d9d9d6', fachada='#2b2d31'),
    'curso': dict(bg='#0A1F17', bg2='#123528', ac='#C8A96B', chao='#cfc6b5', parede='#e7e0d2', fachada='#3b3a36'),
    'wf': dict(bg='#000000', bg2='#1D1D1F', ac='#C7C9CC', chao='#9a9894', parede='#dcdad6', fachada='#2a2a2c'),
    'oregano': dict(bg='#1E5B3B', bg2='#141311', ac='#F2B33D', chao='#c8b9a1', parede='#ece4d6', fachada='#3d3530'),
    'duble': dict(bg='#0B0B10', bg2='#15151C', ac='#8B7CFF', chao='#b7b4bd', parede='#e4e2e7', fachada='#2c2b33'),
}
CENAS = ['cartoes', 'papelaria', 'celular', 'poster', 'embalagem', 'outdoor']

def gobo(im, kind, seed):
    # sombra de janela/folhas projetada (luz natural de estúdio)
    w, h = im.size; random.seed(seed)
    m = Image.new('L', (w, h), 255); d = ImageDraw.Draw(m)
    if kind == 'janela':
        for i in range(4):
            x = int(w * (-0.2 + i * 0.32)); d.polygon([(x, 0), (x + int(w * .05), 0), (x + int(w * .25), h), (x + int(w * .2), h)], fill=150)
        d.polygon([(0, int(h * .45)), (w, int(h * .2)), (w, int(h * .25)), (0, int(h * .5))], fill=150)
    else:
        for _ in range(26):
            cx, cy = random.randint(int(w * .55), w), random.randint(0, int(h * .6)); rr = random.randint(int(w * .02), int(w * .06))
            d.ellipse([cx - rr * 2, cy - rr, cx + rr * 2, cy + rr], fill=140)
    m = m.filter(ImageFilter.GaussianBlur(w / 90))
    sh = Image.merge('RGB', [m, m, m])
    return ImageChops.multiply(im, Image.blend(sh, Image.new('RGB', (w, h), (255, 255, 255)), 0.35))

def finish(im, cena):
    w, h = im.size
    if cena in ('papelaria', 'cartoes', 'celular'): im = gobo(im, 'janela', 3)
    if cena == 'poster': im = gobo(im, 'janela', 5)
    # vinheta suave + grão de filme
    v = Image.new('L', (w, h), 0); ImageDraw.Draw(v).ellipse([-w * .25, -h * .25, w * 1.25, h * 1.25], fill=255)
    v = v.filter(ImageFilter.GaussianBlur(w / 6)); im = Image.composite(im, ImageChops.multiply(im, Image.new('RGB', (w, h), (205, 205, 205))), v)
    n = Image.effect_noise((w, h), 14).convert('RGB'); im = Image.blend(im, ImageChops.overlay(im, n), 0.10)
    return im

if __name__ == '__main__':
    from playwright.sync_api import sync_playwright
    os.makedirs(OUT, exist_ok=True)
    W, H = (2000, 3000) if RET else (2800, 2100)
    jobs = [j.split(':') for j in JOBS] or [(k, c) for k in PAL for c in CENAS]
    hp = os.path.join(OUT, '_cena.html')
    open(hp, 'w').write(f'''<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0;background:#000}}</style>
<script type="importmap">{{"imports":{{"three":"file://{THREE}/build/three.module.js","three/addons/":"file://{THREE}/examples/jsm/"}}}}</script>
<script type="module" src="file://{HERE}/cenas.js"></script></head><body></body></html>''')
    with sync_playwright() as pw:
        b = pw.chromium.launch(args=['--allow-file-access-from-files', '--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
        for k, c in jobs:
            p = b.new_page(viewport={'width': 800, 'height': 600})
            p.on('console', lambda m: print('  js:', m.text) if m.type == 'error' else None)
            q = urllib.parse.urlencode({'tex': 'file://' + TEX + '/' + k, 'cena': c, 'w': W, 'h': H, 'pal': json.dumps(PAL[k])})
            p.goto('file://' + hp + '?' + q); p.wait_for_function('window.ready===true', timeout=60000)
            data = p.evaluate('window.render()')
            raw = os.path.join(OUT, f'{k}-{c}{"-r" if RET else ""}.png')
            open(raw, 'wb').write(base64.b64decode(data.split(',')[1]))
            im = Image.open(raw).convert('RGB'); im = finish(im, c)
            im = im.resize((W // 2, H // 2), Image.LANCZOS)
            im.save(raw[:-4] + '.jpg', quality=90); os.remove(raw); p.close()
            print(k, c, 'ok')
        b.close()
