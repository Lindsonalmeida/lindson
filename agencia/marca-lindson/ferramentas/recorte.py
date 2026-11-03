# PADRÃO DE RECORTE (decisão 03/11, depois de 2 erros de recorte com o MediaPipe): 
# Recorte de alta precisão (BiRefNet portrait, via rembg) com alpha matting fino para cabelo; saída do tamanho da foto inteira.
import sys, numpy as np
from PIL import Image
from rembg import remove, new_session
ses = new_session('birefnet-portrait')
for f in sys.argv[1:]:
    im = Image.open(f).convert('RGB')
    m = remove(im, session=ses, only_mask=True)            # máscara 0-255 com transição suave no cabelo
    a = np.asarray(m).astype(float) / 255; a = np.clip((a - .35) / .4, 0, 1); a = a * a * (3 - 2 * a)   # borda firme, sem halo
    rgba = im.copy(); rgba.putalpha(Image.fromarray((a * 255).astype('uint8')))
    rgba.save(f.replace('.jpg', '-full.png')); print(f, im.size)
