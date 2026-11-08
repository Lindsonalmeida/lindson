# Prévia das artes tipográficas novas (v4) em ordem de publicação. Cópia de ../s3-4/previa.py (conta Zuleide, 08/11/2026).
import os, glob
from PIL import Image, ImageDraw, ImageFont
D = os.path.dirname(os.path.abspath(__file__))
chave = lambda f: (int(os.path.basename(f)[1:3]), int(os.path.basename(f).split('-')[1][:-1]), f)
fs = sorted(glob.glob(os.path.join(D, 'd*.jpg')), key=chave)
C, TW, TH, G, LB = 6, 300, 533, 14, 34
L = (len(fs) + C - 1) // C
s = Image.new('RGB', (C * TW + (C + 1) * G, L * (TH + LB) + (L + 1) * G), '#141311')
dr = ImageDraw.Draw(s)
try:
    fnt = ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Bold.otf', 17)
except Exception:
    fnt = ImageFont.load_default()
for i, f in enumerate(fs):
    im = Image.open(f); im.thumbnail((TW, TH), Image.LANCZOS)
    x, y = G + (i % C) * (TW + G), G + (i // C) * (TH + LB + G)
    s.paste(im, (x + (TW - im.width) // 2, y + (TH - im.height) // 2))
    dr.text((x, y + TH + 8), os.path.basename(f)[:-4][:30], fill='#F3EEE6', font=fnt)
s.save(os.path.join(D, 'previa-tipo-v4.jpg'), quality=90)
print(len(fs))
