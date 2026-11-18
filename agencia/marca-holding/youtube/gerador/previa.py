# Prévia: banner + avatar + 3 thumbs numa folha (conta Zuleide 18/11/2026)
from PIL import Image, ImageDraw
import os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'pecas')
o = lambda n: Image.open(os.path.join(P, n))
c = Image.new('RGB', (2000, 1300), '#1c1d21'); c.paste(o('banner.jpg').resize((1440, 810)), (40, 40))
a = o('avatar.jpg').resize((440, 440)); m = Image.new('L', (440, 440), 0); ImageDraw.Draw(m).ellipse((0, 0, 440, 440), fill=255); c.paste(a, (1520, 40), m)
for i in range(3): c.paste(o(f'thumb-0{i+1}.jpg').resize((620, 349)), (40 + i * 650, 900))
c.save(os.path.join(P, '..', 'previa.jpg'), quality=90)
