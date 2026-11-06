# Prova social "Contorno facial masculino" da Dra. Jaci (conta Leandro, 06/11/2026).
# Alinha os pares antes x depois pelo MESMO ângulo (frente x frente, perfil x perfil, 3/4 x 3/4):
# só escala, giro e recorte (transformação de semelhança por 2 pontos do rosto) + a MESMA correção leve de exposição nos dois lados.
# Nada de retoque. As fotos ficam só no privado: python3 preparar_fotos.py <material-2026-11-06> <saida/fotos>
import sys, numpy as np
from PIL import Image, ImageEnhance
M, OUT = sys.argv[1], sys.argv[2]
A, D = M + '/lote-16.29.29/WhatsApp Image 2026-11-03 at ', M + '/lote-16.31.31/WhatsApp Image 2026-11-05 at '
# pontos marcados à mão sobre grade (px da foto original): (arquivo, ponto1, ponto2)
# perfil: olho e trago da orelha; frente: as duas pupilas; 3/4: pupila de trás e trago.
PARES = {
  'perfil': ((A + '21.38.16 (1).jpeg', (527, 527), (268, 615)), (D + '17.31.05.jpeg', (535, 625), (276, 765))),
  'frente': ((A + '21.38.15.jpeg', (324, 628), (499, 628)), (D + '17.31.09.jpeg', (338, 647), (520, 647))),
  'tres4':  ((A + '21.38.15 (1).jpeg', (246, 645), (596, 698)), (D + '17.31.02 (2).jpeg', (253, 601), (603, 657))),
}
S0 = 2.0  # amplia o quadro do "antes" para manter nitidez no 1080
def expo(im): return ImageEnhance.Contrast(ImageEnhance.Brightness(im).enhance(1.04)).enhance(1.03)  # igual nos dois lados
for nome, ((fa, a1, a2), (fd, d1, d2)) in PARES.items():
    ia, idd = Image.open(fa).convert('RGB'), Image.open(fd).convert('RGB')
    W, H = int(ia.width * S0), int(ia.height * S0)
    pa = Image.open(fa).convert('RGB').resize((W, H), Image.LANCZOS)
    # semelhança que leva d1->a1*S0 e d2->a2*S0 (complexos)
    za1, za2 = complex(*a1) * S0, complex(*a2) * S0; zd1, zd2 = complex(*d1), complex(*d2)
    k = (za2 - za1) / (zd2 - zd1); b = za1 - k * zd1           # z_saida = k*z_depois + b
    ki = 1 / k; bi = -b / k                                     # inversa p/ PIL: z_depois = ki*z_saida + bi
    coef = (ki.real, -ki.imag, bi.real, ki.imag, ki.real, bi.imag)
    pd = idd.transform((W, H), Image.AFFINE, coef, resample=Image.BICUBIC)
    mask = np.array(Image.new('L', idd.size, 255).transform((W, H), Image.AFFINE, coef, resample=Image.NEAREST)) > 0
    x0, y0, x1, y1 = 0, 0, W, H   # encolhe até o retângulo inteiro ser válido nas duas fotos
    while True:
        ch = False
        if not mask[y0, x0:x1].all(): y0 += 2; ch = True
        if not mask[y1 - 1, x0:x1].all(): y1 -= 2; ch = True
        if not mask[y0:y1, x0].all(): x0 += 2; ch = True
        if not mask[y0:y1, x1 - 1].all(): x1 -= 2; ch = True
        if not ch: break
    box = (x0, y0, x1, y1)
    import math
    print(nome, 'giro do depois: %.1f°' % math.degrees(math.atan2(k.imag, k.real)), 'escala %.2f' % abs(k), 'recorte', box,
          'olho em', (int(za1.real - x0), int(za1.imag - y0)))
    expo(pa.crop(box)).save(f'{OUT}/{nome}-antes.jpg', quality=93)
    expo(pd.crop(box)).save(f'{OUT}/{nome}-depois.jpg', quality=93)
c = Image.open(M + '/avulsas/cadeira-perfil.jpg').convert('RGB'); c = c.resize((c.width * 2, c.height * 2), Image.LANCZOS)
expo(c).save(f'{OUT}/bastidor-cadeira.jpg', quality=93)
