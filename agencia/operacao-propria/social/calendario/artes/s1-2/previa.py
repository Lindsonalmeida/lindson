# Prévia das 19 artes tipográficas das semanas 1 e 2 (ordem do calendário). Paollo, conta Leandro, 06/11/2026.
import os, glob
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
fs = sorted(glob.glob(os.path.join(D, 'd[0-9]*.jpg')))
W, G, C = 300, 10, 5          # largura da miniatura, espaço, colunas
H = int(W * 1920 / 1080)       # altura da célula (cabe story; post fica centralizado)
linhas = (len(fs) + C - 1) // C
s = Image.new('RGB', (C * W + (C + 1) * G, linhas * H + (linhas + 1) * G), '#141311')
for i, f in enumerate(fs):
    im = Image.open(f); h = int(W * im.height / im.width)
    x = G + (i % C) * (W + G); y = G + (i // C) * (H + G) + (H - h) // 2
    s.paste(im.resize((W, h), Image.LANCZOS), (x, y))
s.save(os.path.join(D, 'previa-s1-2.jpg'), quality=90)
print(len(fs), 'miniaturas')
