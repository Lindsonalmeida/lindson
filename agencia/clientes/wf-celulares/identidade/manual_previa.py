# Prévia do manual WF: miniaturas das 22 páginas (conta Leandro, 10/11/2026)
from PIL import Image
import glob, os
d = os.path.dirname(os.path.abspath(__file__))
fs = sorted(glob.glob(f'{d}/manual-pags/*.jpg')); w, h = 480, 270
im = Image.new('RGB', (4 * w + 50, 6 * h + 70), '#111')
for i, f in enumerate(fs): im.paste(Image.open(f).resize((w, h)), (10 + (i % 4) * (w + 10), 10 + (i // 4) * (h + 10)))
im.save(f'{d}/manual-previa.jpg', quality=85)
