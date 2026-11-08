# Prévia do feed 3×3 (ordem de publicação: p01 no canto superior esquerdo). kit v4, conta Zuleide, 08/11/2026.
import os, glob
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
fs = sorted(glob.glob(os.path.join(D, 'pecas', 'p0*.jpg')))[:9]
W, H, G = 360, 450, 6
s = Image.new('RGB', (W * 3 + G * 2, H * 3 + G * 2), '#fff')
for i, f in enumerate(fs):
    s.paste(Image.open(f).resize((W, H), Image.LANCZOS), ((i % 3) * (W + G), (i // 3) * (H + G)))
s.save(os.path.join(D, 'previa-feed.jpg'), quality=90)
print(len(fs))
