"""Gera a foto principal da tela de acesso a partir da foto original do Lindson (mãos no queixo). Conta Lindson, 01/11/2026.
  python3 tratar-foto.py <foto-original> [modelo-depth-anything-v2-small.onnx]
Saída em ../fotos/ (fora do Git, dado pessoal):
  rec-68.webp         recorte sem fundo (rembg, u2net_human_seg)
  principal-cine.webp cor de cinema (contraste, pele quente, realces dourados) + luz de contorno dourada à direita e no topo
  principal-prof.webp mapa de profundidade para o efeito 3D (Depth Anything V2 small; sem o modelo, usa a silhueta)
Corte 768x1214 (proporção do .principal no login.html), tirando a parte de baixo (onde fica a marca d'água da foto)."""
import sys, os, numpy as np
from PIL import Image, ImageFilter
from rembg import remove, new_session
D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(D, '..', 'fotos'); os.makedirs(OUT, exist_ok=True)
W, H = 768, 1214
im = Image.open(sys.argv[1]).convert('RGB')
im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS).crop((0, 0, W, H))

# 1 · recorte
rec = remove(im, session=new_session('u2net_human_seg'), alpha_matting=True)
rec.save(os.path.join(OUT, 'rec-68.webp'), quality=92)

# 2 · cor de cinema + luz de contorno dourada
a = np.asarray(rec).astype(np.float32) / 255; rgb, al = a[..., :3], a[..., 3:]
lum = rgb @ np.array([.299, .587, .114], np.float32)
rgb = np.clip((rgb - .5) * 1.10 + .5, 0, 1)                                  # contraste
rgb = rgb * np.array([1.04, 1.0, .93], np.float32)                           # pele quente
hi = np.clip((lum - .55) / .45, 0, 1)[..., None]
rgb = rgb * (1 - .18 * hi) + np.array([1.0, .84, .52], np.float32) * .18 * hi   # realces dourados
sh = np.clip((.35 - lum) / .35, 0, 1)[..., None]; rgb = rgb * (1 - .08 * sh)  # sombras mais densas
A = Image.fromarray((al[..., 0] * 255).astype(np.uint8))
er = np.asarray(A.filter(ImageFilter.MinFilter(9)).filter(ImageFilter.GaussianBlur(6))).astype(np.float32) / 255
borda = np.clip(al[..., 0] - er, 0, 1)
borda = np.asarray(Image.fromarray((borda * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))).astype(np.float32) / 255
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
lado = np.clip((xx / W - .35) / .65, 0, 1) * .8 + np.clip(1 - yy / (H * .45), 0, 1) * .6
rgb = np.clip(rgb + (borda * np.clip(lado, 0, 1) * 1.1)[..., None] * np.array([1.0, .78, .35], np.float32), 0, 1)
Image.fromarray((np.dstack([rgb, al]) * 255).astype(np.uint8), 'RGBA').save(os.path.join(OUT, 'principal-cine.webp'), quality=92)

# 3 · profundidade
if len(sys.argv) > 2:
    import onnxruntime as ort
    s = ort.InferenceSession(sys.argv[2], providers=['CPUExecutionProvider'])
    x = np.asarray(im.resize((518, 812), Image.BICUBIC)  # múltiplos de 14, mesma proporção).astype(np.float32) / 255
    x = ((x - [.485, .456, .406]) / [.229, .224, .225]).transpose(2, 0, 1)[None].astype(np.float32)
    d = s.run(None, {s.get_inputs()[0].name: x})[0].squeeze()
    d = (d - d.min()) / (d.max() - d.min() + 1e-6)
    d = np.asarray(Image.fromarray((d * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC)).astype(np.float32) / 255
else:
    from scipy.ndimage import distance_transform_edt
    d = distance_transform_edt(al[..., 0] > .5); d = np.sqrt(d / (d.max() + 1e-6))
d = d * al[..., 0]                                                           # fundo no plano de trás
Image.fromarray((d * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2)).save(os.path.join(OUT, 'principal-prof.webp'), quality=90)
print('ok:', os.listdir(OUT))
