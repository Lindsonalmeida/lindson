# Recorta a comida das fotos v4 (fundo transparente) com BiRefNet via rembg. Um arquivo por processo (memória).
# Uso: python3 recortar4.py fotos-v4/calabresa.jpg   → recortes-v4/calabresa.png   (conta Leandro · Paollo, 06/11/2026)
import sys, os
from rembg import remove, new_session
from PIL import Image
f = sys.argv[1]; out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'recortes-v4', os.path.basename(f).rsplit('.', 1)[0] + '.png')
im = Image.open(f).convert('RGB')
r = remove(im, session=new_session(os.environ.get('MODELO', 'birefnet-general')), alpha_matting=False)
bb = r.getbbox(); r = r.crop(bb); r.save(out); print(out, r.size)
