"""Melhora foto de celular para arte (conta Leandro, 03/11/2026): Real-ESRGAN x2 (mais resolução e nitidez, menos ruído) em blocos,
+ ajuste leve de cor (contraste, brilho e vibração). Modelo ONNX em ~/.modelos/real_esrgan_x2.onnx
(https://huggingface.co/facefusion/models-3.0.0/resolve/main/real_esrgan_x2.onnx). Uso: python3 melhorar_foto.py entrada.jpg saida.png"""
import sys, os, numpy as np, onnxruntime as ort
from PIL import Image, ImageEnhance
M = os.path.expanduser('~/.modelos/real_esrgan_x2.onnx')
s = ort.InferenceSession(M, providers=['CPUExecutionProvider']); ent = s.get_inputs()[0]
im = np.asarray(Image.open(sys.argv[1]).convert('RGB')).astype(np.float32) / 255.
h, w, _ = im.shape; T, P, E = 256, 16, 2; out = np.zeros((h * E, w * E, 3), np.float32)
for y in range(0, h, T):
    for x in range(0, w, T):
        y0, x0, y1, x1 = max(y - P, 0), max(x - P, 0), min(y + T + P, h), min(x + T + P, w)
        t = im[y0:y1, x0:x1]; ph, pw = t.shape[0] % 2, t.shape[1] % 2  # o modelo pede lados pares
        t = np.pad(t, ((0, ph), (0, pw), (0, 0)), mode='edge').transpose(2, 0, 1)[None]
        r = s.run(None, {ent.name: t})[0][0].transpose(1, 2, 0)
        oy, ox = (y - y0) * E, (x - x0) * E; th, tw = (min(y + T, h) - y) * E, (min(x + T, w) - x) * E
        out[y * E:y * E + th, x * E:x * E + tw] = r[oy:oy + th, ox:ox + tw]
o = Image.fromarray((np.clip(out, 0, 1) * 255).round().astype(np.uint8))
o = ImageEnhance.Contrast(o).enhance(1.06); o = ImageEnhance.Brightness(o).enhance(1.04); o = ImageEnhance.Color(o).enhance(1.08)
o.save(sys.argv[2]); print(sys.argv[2], o.size)
