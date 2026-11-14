"""Limpa o recorte para a borda cortada NUNCA aparecer (regra do Lindson, 14/11/2026: "as fotos estão todas mal cortadas,
nunca mais cometa esse erro"). python3 limpar_recorte.py entrada.png saida.png
1. Fica só a pessoa: o maior pedaço ligado do alfa (somem mão solta, celular cortado, sobras do fundo).
2. Toda lateral e a base em que a pessoa encosta na borda da foto original (braço ou ombro cortado pelo quadro) somem num degradê longo,
   em vez de terminar numa linha reta. A borda de cima nunca é cortada (cabeça inteira).
3. Alfa suavizado (MinFilter 3 + blur 1,2) para não ficar serrilhado."""
import sys, numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
im = Image.open(sys.argv[1]).convert('RGBA'); A = np.array(im.getchannel('A')).astype(float) / 255
h, w = A.shape
lab, n = ndimage.label(A > .25)
if n > 1:
    tam = ndimage.sum(np.ones_like(A), lab, range(1, n + 1)); keep = 1 + int(np.argmax(tam))
    mask = ndimage.binary_dilation(lab == keep, iterations=6); A *= mask
toca = lambda faixa: (faixa > .5).mean() > .01            # a pessoa encosta nessa borda?
R = lambda frac, n_: (np.linspace(0, 1, n_) ** 1.3)
# laterais: só abaixo da cabeça (a partir de 38% da altura, entrando aos poucos), para nunca apagar rosto ou cabelo
v = np.clip((np.arange(h) / h - .38) / .12, 0, 1)[:, None]
if toca(A[int(h * .38):, :3]):  n_ = int(w * .16); A[:, :n_] *= 1 - v * (1 - R(0, n_)[None, :])
if toca(A[int(h * .38):, -3:]): n_ = int(w * .16); A[:, -n_:] *= 1 - v * (1 - R(0, n_)[::-1][None, :])
if toca(A[-3:, :]): n_ = int(h * .22); A[-n_:, :] *= R(0, n_)[::-1][:, None]
a = Image.fromarray((A * 255).astype('uint8')).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
bb = a.point(lambda v: 255 if v > 12 else 0).getbbox(); im.putalpha(a); im.crop(bb).save(sys.argv[2]); print(sys.argv[2], bb)
