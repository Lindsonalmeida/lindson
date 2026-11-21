# Renderiza apresentacao.html -> slides/NN.png e carrossel.html -> carrossel/NN.png; monta PDF e folha.jpg
import os, sys
from playwright.sync_api import sync_playwright
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome')
    for f, pre, out in [('apresentacao.html', 's', 'slides'), ('carrossel.html', 'c', 'carrossel')]:
        pg = b.new_page(viewport={'width': 1920, 'height': 1200})
        pg.goto('file://' + os.path.join(D, f), wait_until='networkidle'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(1200)
        os.makedirs(os.path.join(D, out), exist_ok=True)
        for el in pg.query_selector_all('section'):
            i = el.get_attribute('id')[1:]
            el.screenshot(path=os.path.join(D, out, f'{i}.png'))
    b.close()
ims = [Image.open(os.path.join(D, 'slides', f'{i:02d}.png')).convert('RGB') for i in range(1, 18)]
ims[0].save(os.path.join(D, 'apresentacao.pdf'), save_all=True, append_images=ims[1:], resolution=96)
W = Image.new('RGB', (3 * 640 + 4 * 32, 6 * 360 + 7 * 32 + 120), (63, 52, 32))
for k, im in enumerate(ims):
    t = im.resize((640, 360)); W.paste(t, (32 + (k % 3) * 672, 152 + (k // 3) * 392))
from PIL import ImageDraw, ImageFont
dr = ImageDraw.Draw(W)
try: fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 34)
except Exception: fnt = None
dr.text((32, 50), 'BARZAKH · UM ESTÚDIO AL KÁNTARA  ·  IDENTIDADE VISUAL  ·  17 SLIDES', fill=(207, 174, 116), font=fnt)
logo = Image.open(os.path.join(D, 'assets', 'barzakh-simbolo-ouro.png')).resize((300, 300))
W.paste(logo, (32 + 2 * 672 + 170, 152 + 5 * 392 + 30), logo)
W.save(os.path.join(D, 'folha.jpg'), quality=90)
print('ok')
