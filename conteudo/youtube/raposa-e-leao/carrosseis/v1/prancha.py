# Prancha de cada carrossel (8 telas em 2 linhas) -> cNN/prancha.jpg. Conta Zuleide, 18/11/2026.
import os, sys
from PIL import Image, ImageDraw, ImageFont
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D); import dados as X
fa = ImageFont.truetype(os.path.join(D, '../../produto/fonts/Anton-Regular.ttf'), 44)
for c in X.CAR:
    p = os.path.join(D, c['id']); ims = [os.path.join(p, f'{c["id"]}-{i:02d}.jpg') for i in range(1, 9)]
    if not all(map(os.path.exists, ims)): continue
    w, h, m = 432, 540, 16; W = Image.new('RGB', (4*w+5*m, 2*h+3*m+80), '#0B0A08'); d = ImageDraw.Draw(W)
    d.text((m, 18), f'{c["id"].upper()} · {c["linha"]}', font=fa, fill='#E2BE4A')
    for i, f in enumerate(ims):
        W.paste(Image.open(f).convert('RGB').resize((w, h), Image.LANCZOS), (m + (i % 4)*(w+m), 80 + m + (i // 4)*(h+m)))
    W.save(os.path.join(p, 'prancha.jpg'), quality=85)
print('ok')
