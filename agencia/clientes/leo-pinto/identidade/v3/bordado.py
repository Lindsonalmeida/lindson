import cv2, numpy as np, cairosvg, io, sys
from PIL import Image, ImageFilter, ImageChops
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGBA'); a = im.split()[3]
rgb = np.array(im.convert('RGB'))[:, :, ::-1].copy()
# 1) remove o bordado da fabricante (região do peito)
cx, cy, r = 630, 903, 40
mask = np.zeros(rgb.shape[:2], np.uint8); cv2.circle(mask, (cx, cy), r, 255, -1)
rgb = cv2.inpaint(rgb, mask, 9, cv2.INPAINT_TELEA)
# textura do tecido de volta sobre a área limpa
noise = np.random.normal(0, 3.2, rgb.shape[:2]).astype(np.float32)
noise = cv2.GaussianBlur(noise, (0, 0), .6)
m = cv2.GaussianBlur(mask.astype(np.float32) / 255, (0, 0), 6)[..., None]
rgb = np.clip(rgb.astype(np.float32) + noise[..., None] * m, 0, 255).astype(np.uint8)
base = Image.fromarray(rgb[:, :, ::-1]).convert('RGBA'); base.putalpha(a)
# 2) monograma em "bordado"
S = 88
svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200"><circle cx="100" cy="100" r="98" fill="#F26A1B"/><g transform="translate(8 3)"><rect x="58" y="38" width="32" height="118" rx="3" fill="#fff"/><path d="M90 38h12a37 37 0 0 1 0 74H90z" fill="#FFC20E"/><path d="M90 156V132c10-8 20-8 30 0s20 8 30 0v24z" fill="#3FB8E8"/></g><circle cx="100" cy="100" r="94" fill="none" stroke="#C9500F" stroke-width="5"/></svg>'''
logo = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(), output_width=S * 4, output_height=S * 4))).convert('RGBA')
# ponto de bordado: linhas diagonais finas
st = Image.new('L', logo.size, 0); px = st.load()
for y in range(logo.size[1]):
    for x in range(logo.size[0]):
        px[x, y] = 255 if ((x + y) % 7) < 4 else 150
lum = ImageChops.multiply(logo.convert('RGB'), Image.merge('RGB', [st] * 3))
logo = Image.merge('RGBA', (*lum.split(), logo.split()[3])).resize((S, S), Image.LANCZOS)
# leve curvatura do peito (perspectiva) e sombreamento da própria foto
logo = logo.transform((S, S), Image.PERSPECTIVE, (1.0, -0.02, 1, 0.015, 1.0, -1, 0, 0), Image.BICUBIC)
x0, y0 = cx - S // 2, cy - S // 2 - 6
patch = base.crop((x0, y0, x0 + S, y0 + S)).convert('L')
shade = patch.point(lambda v: int(min(255, 190 + v * 0.30)))
r_, g_, b_, al = logo.split()
r_, g_, b_ = [ImageChops.multiply(c, shade) for c in (r_, g_, b_)]
logo = Image.merge('RGBA', (r_, g_, b_, al))
sh = Image.new('RGBA', (S, S), (90, 60, 0, 0)); sh.putalpha(al.point(lambda v: int(v * .45)).filter(ImageFilter.GaussianBlur(2)))
base.alpha_composite(sh, (x0 + 1, y0 + 2)); base.alpha_composite(logo, (x0, y0))
base.save(out)
