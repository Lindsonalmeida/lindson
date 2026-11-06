# A4-avental (Gemini) saiu com o símbolo numa variação em contorno. Aqui o símbolo errado é apagado (inpaint + textura
# do próprio tecido) e o símbolo OFICIAL (folha com seta, gerar4.simbolo) é estampado em branco com a trama do tecido.
# Saída: fotos/A4-avental-corrigido.jpg  (Paollo, conta Leandro, 06/11/2026)
import os, numpy as np, cv2
from PIL import Image, ImageDraw
D = os.path.dirname(os.path.abspath(__file__))
im = cv2.imread(os.path.join(D, '../../identidade/fotos-ia/A4-avental.jpg'))
x0, y0, x1, y1 = 600, 880, 1030, 1370
roi = im[y0:y1, x0:x1]
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
m = ((hsv[..., 2] > 120) & (hsv[..., 1] < 110)).astype(np.uint8) * 255
m = cv2.dilate(m, np.ones((5, 5), np.uint8), iterations=3)
mask = np.zeros(im.shape[:2], np.uint8); mask[y0:y1, x0:x1] = m
# cobre o símbolo errado com tecido limpo de logo abaixo (espelhado para ter altura), clonagem de Poisson só na marca antiga
out = im.copy()
clean = im[1330:1600, x0:x1]
patch = np.vstack([clean, clean[::-1]])[:y1 - y0]
mk = cv2.dilate(m, np.ones((9, 9), np.uint8), iterations=3)
mk[:6] = 0; mk[-6:] = 0; mk[:, :6] = 0; mk[:, -6:] = 0
out = cv2.seamlessClone(patch, out, mk, ((x0 + x1) // 2, (y0 + y1) // 2), cv2.NORMAL_CLONE)
# textura: alta frequência de um pedaço de tecido limpo logo abaixo
src = patch.astype(np.float32)
hf = src - cv2.GaussianBlur(src, (0, 0), 3)
blk = out[y0:y1, x0:x1].astype(np.float32)
mm = (cv2.GaussianBlur(m, (0, 0), 2).astype(np.float32) / 255)[..., None]
# símbolo oficial
S = 4; size = 360
cv = Image.new('L', (100 * S, 100 * S), 0); dr = ImageDraw.Draw(cv)
def bez(p0, p1, p2, p3, n=60):
    return [tuple(S * ((1 - t) ** 3 * a + 3 * (1 - t) ** 2 * t * b + 3 * (1 - t) * t * t * c + t ** 3 * d) for a, b, c, d in zip(p0, p1, p2, p3)) for t in np.linspace(0, 1, n)]
leaf = bez((18, 86), (14, 50), (40, 18), (86, 14)) + bez((86, 14), (86, 58), (58, 88), (18, 86))
dr.polygon(leaf, fill=255)
w = int(7 * S)
for seg in [[(26, 76), (44, 58), (54, 66), (72, 40)], [(60, 38), (74, 38), (74, 52)]]:
    pts = [(x * S, y * S) for x, y in seg]
    dr.line(pts, fill=0, width=w, joint='curve')
    for p in pts: dr.ellipse((p[0] - w / 2, p[1] - w / 2, p[0] + w / 2, p[1] + w / 2), fill=0)
sym = np.array(cv.resize((size, size), Image.LANCZOS).rotate(4, resample=Image.BICUBIC)).astype(np.float32) / 255
cx, cy = 815 - x0, 1125 - y0
H, W = blk.shape[:2]
a = np.zeros((H, W), np.float32); sy, sx = cy - size // 2, cx - size // 2
a[sy:sy + size, sx:sx + size] = sym
gray = cv2.cvtColor(np.clip(blk, 0, 255).astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)
shade = np.clip(gray / max(gray.mean(), 1), .92, 1.06)[..., None]
rng = np.random.default_rng(3); wear = np.clip(1 - rng.random((H, W)) * .22, 0, 1)
a = cv2.GaussianBlur(a, (0, 0), .8) * .96 * cv2.GaussianBlur(wear, (0, 0), .6)
white = np.array([236, 240, 242], np.float32) * shade + hf * .9
blk = blk * (1 - a[..., None]) + white * a[..., None]
out[y0:y1, x0:x1] = np.clip(blk, 0, 255).astype(np.uint8)
cv2.imwrite(os.path.join(D, 'fotos/A4-avental-corrigido.jpg'), out, [cv2.IMWRITE_JPEG_QUALITY, 93])
cv2.imwrite('/tmp/claude-0/-home-user/b9464785-a028-5189-b9f0-a7ed9d7dd59e/scratchpad/s/a4fix.jpg', cv2.resize(out[700:1600, 400:1300], (450, 450)))
