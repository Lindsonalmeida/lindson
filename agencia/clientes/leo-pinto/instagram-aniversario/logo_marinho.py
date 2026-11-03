"""Gera logo-marinho.png (letras LEO PINTO em marinho #05316E, sem o brilho difuso atrás do sol; centro do sol continua claro) a partir da logo oficial.
python3 logo_marinho.py <pasta>  (conta Leandro, 03/11/2026; mesma regra da logo-marinho-forte das datas v14)"""
import sys, os, numpy as np
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
a = np.array(Image.open(os.path.join(D, '..', 'instagram-v12-feed', 'marca', 'logo_principal.png')).convert('RGBA')).astype(float)
yy, xx = np.mgrid[0:a.shape[0], 0:a.shape[1]]; fora = ((xx - 1037) ** 2 + (yy - 555) ** 2) > 272 ** 2
mn = a[..., :3].min(-1); branco = (mn > 235) & (a[..., 3] > 200) & fora
a[fora & (mn > 120) & ~branco, 3] = 0; a[branco, 0:3] = [5, 49, 110]
Image.fromarray(a.astype('uint8')).save(os.path.join(sys.argv[1], 'logo-marinho.png'))
