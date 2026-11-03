"""Recorta a(s) pessoa(s) da foto para o modelo de aniversário (conta Leandro, 03/11/2026). Mesmo modelo de IA do recortar.py do feed v12 (BiRefNet portrait).
python3 recortar.py <foto.jpg> <pasta da pessoa> [x0 y0 x1 y1]   (o retângulo opcional tira gente da borda; a base da foto pode sair cortada:
no modelo, a pessoa sai pela base da arte, então o corte de baixo nunca aparece)."""
import sys, os
from PIL import Image
from rembg import remove, new_session
foto, pasta = sys.argv[1], sys.argv[2]; os.makedirs(pasta, exist_ok=True)
im = Image.open(foto).convert('RGB')
if len(sys.argv) == 7: im = im.crop(tuple(int(v) for v in sys.argv[3:7]))
out = remove(im, session=new_session('birefnet-portrait'))
bb = out.getchannel('A').point(lambda v: 255 if v > 30 else 0).getbbox(); out = out.crop(bb)
out.save(os.path.join(pasta, 'recorte.png')); print(os.path.join(pasta, 'recorte.png'), out.size)
