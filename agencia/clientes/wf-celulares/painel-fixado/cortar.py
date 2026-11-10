# Corta pano.jpg (3240x1350) em 01/02/03 (1080x1350) e monta a prévia da grade 3:4 do Instagram. Conta Pedro, 10/11/2026.
from PIL import Image, ImageDraw
import os
D = os.path.dirname(os.path.abspath(__file__)); P = Image.open(os.path.join(D, 'pano.jpg')).convert('RGB')
for i in range(3): P.crop((i*1080, 0, (i+1)*1080, 1350)).save(os.path.join(D, f'0{i+1}.jpg'), quality=94)
# grade: cada post 4:5 aparece cortado em 3:4 (1012x1350, centro), 3 colunas com 3 px de divisa
w = 1012; c = (1080-w)//2; esc = 0.5
G = Image.new('RGB', (int((3*w+6)*esc)+40, int(1350*esc)+40), '#0c0c0d'); d = ImageDraw.Draw(G)
for i in range(3):
    t = P.crop((i*1080+c, 0, i*1080+c+w, 1350)).resize((int(w*esc), int(1350*esc)))
    G.paste(t, (20+int(i*(w+3)*esc), 20))
G.save(os.path.join(D, 'previa-grade.jpg'), quality=92)
