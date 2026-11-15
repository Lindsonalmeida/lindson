# Folha de contato das 9 capas da semana 2 (OT-22..30) -> previa-semana-2.jpg
import os, json
from PIL import Image, ImageDraw
H = os.path.dirname(os.path.abspath(__file__)); R = json.load(open(os.path.join(H, 'roteiros.json')))['reels'][21:]
W, Hh, g = 300, 533, 12; im = Image.new('RGB', (3 * W + 4 * g, 3 * (Hh + 30) + g), '#141311'); d = ImageDraw.Draw(im)
for k, r in enumerate(R):
    p = os.path.join(H, 'semana-2', r['id'][3:], 'capa.jpg'); x, y = g + (k % 3) * (W + g), g + (k // 3) * (Hh + 30)
    if os.path.exists(p): im.paste(Image.open(p).resize((W, Hh)), (x, y))
    d.text((x, y + Hh + 4), f"{r['id']} {r['post']['data']} {r['post']['hora']} {r['tipo'].upper()}", fill='#F3EEE6')
im.save(os.path.join(H, 'previa-semana-2.jpg'), quality=85); print('ok')
