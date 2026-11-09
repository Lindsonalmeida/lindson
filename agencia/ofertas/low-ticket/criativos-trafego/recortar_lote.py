"""Recorta as fotos do Lindson para os criativos de tráfego (conta Leandro, 09/11/2026).
python3 recortar_lote.py <pasta-saida>   → <pasta-saida>/fNN.png (BiRefNet portrait, alfa limpo).
As fotos vêm do CentralLindsonALmeida (privado): landing pages, área de membros e site."""
import sys, os
from PIL import Image, ImageFilter
from rembg import remove, new_session
C = '/home/user/centrallindsonalmeida/'
FOTOS = [  # 24 fotos diferentes: cada criativo com foto usa uma só (regra: foto usada uma só vez)
 'produtos/landing/bio-que-vende/img/hero.jpg', 'produtos/landing/bio-que-vende/img/sobre.jpg',
 'produtos/landing/kit-mes-pronto/img/hero.jpg', 'produtos/landing/kit-prospeccao/img/hero.jpg',
 'produtos/landing/kit-whatsapp-que-fecha/img/hero.webp', 'produtos/landing/kit-whatsapp-que-fecha/img/sobre.jpg',
 'produtos/landing/raio-x-do-perfil/img/hero.webp', 'produtos/landing/raio-x-do-perfil/img/sobre.jpg',
 'produtos/landing/kit-mes-pronto/img/sobre.png', 'produtos/landing/kit-prospeccao/img/sobre.png',
 'site/img/lindson-contato.jpg', 'site/img/lindson-sobre.jpg', 'bio/lindson-bio.jpg',
] + [f'membros/img/c{n:02d}.jpg' for n in range(7, 17)]
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
s = new_session('birefnet-portrait')
for i, f in enumerate(FOTOS, 1):
    dst = os.path.join(out, f'f{i:02d}.png')
    if os.path.exists(dst): continue
    im = Image.open(C + f).convert('RGB')
    if max(im.size) < 1400:  # sobe a resolução antes de recortar
        k = 1400 / max(im.size); im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    r = remove(im, session=s)
    a = r.getchannel('A').filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2)); r.putalpha(a)
    r = r.crop(a.point(lambda v: 255 if v > 30 else 0).getbbox())
    r.save(dst); print(dst, r.size, f, flush=True)
