# Lê os recortes (assets/recortes/fNN.png) e grava assets/meta.js: tamanho, caixa do rosto (OpenCV Haar),
# topo do cabelo e quais bordas da foto original o recorte toca (essas bordas têm de ficar fora do quadro).
# Uso: python meta.py <pasta-assets>     (conta Pedro, 04/11/2026)
import sys, os, json, glob, numpy as np, cv2
from PIL import Image
A = sys.argv[1]; casc = cv2.CascadeClassifier(f'{A}/modelos/haar_face.xml')  # haarcascade_frontalface_default do OpenCV
meta = {}
for f in sorted(glob.glob(f'{A}/recortes/f*.png')):
    im = Image.open(f); W, H = im.size; a = np.asarray(im.getchannel('A'))
    g = cv2.cvtColor(np.asarray(im.convert('RGB')), cv2.COLOR_RGB2GRAY)
    faces = casc.detectMultiScale(g, 1.08, 6, minSize=(W // 12, W // 12))
    fx, fy, fw, fh = max(faces, key=lambda r: r[2] * r[3]) if len(faces) else (0, 0, 0, 0)
    rows = np.where(a.max(1) > 128)[0]; top = int(rows[0])
    edge = {k: bool(v) for k, v in dict(l=(a[:, :3] > 128).any(), r=(a[:, -3:] > 128).any(), t=(a[:3] > 128).any(), b=(a[-3:] > 128).any()).items()}
    meta[os.path.basename(f)[:-4]] = dict(W=W, H=H, fx=int(fx), fy=int(fy), fw=int(fw), fh=int(fh), top=top, edge=edge)
    print(os.path.basename(f), meta[os.path.basename(f)[:-4]])
open(f'{A}/meta.js', 'w').write('window.META=' + json.dumps(meta) + ';\n')
