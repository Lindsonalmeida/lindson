# Projeto Designer v3 (conta Leandro, 16/11/2026): folha de contato (6 capas + 6 pins + 3 mockups).
# Uso: python3 folha.py <v2> <mockups> <saida.jpg>
import sys, os
from PIL import Image, ImageDraw, ImageFont
V, MK, OUT = sys.argv[1:4]
CASES = ['barzakh', 'leo-pinto', 'real-time', 'processo-legislativo', 'wf-celulares', 'oregano-turbo', 'duble']
PINS = ['barzakh-placa', 'barzakh-cartao', 'barzakh-papelaria', 'barzakh-avatar', 'curso-poster', 'oregano-embalagem', 'realtime-celular', 'wf-cartoes']
MOCK = ['oregano-papelaria', 'realtime-outdoor', 'curso-embalagem']
W, M = 2400, 40; bg = (10, 12, 16)
cw = (W - M * 5) // 4; chh = int(cw * 632 / 808)
pw = (W - M * 9) // 8; ph = int(pw * 1.5)
mw = (W - M * 4) // 3; mh = int(mw * 0.75)
H = 180 + 2 * (chh + M) + 60 + ph + M + 60 + mh + M + 40
S = Image.new('RGB', (W, H), bg); d = ImageDraw.Draw(S)
fb = '/home/user/lindson/agencia/marca-holding/v2/fontes/Fraunces-Regular.ttf'; fr = '/usr/share/fonts/opentype/inter/Inter-Medium.otf'
d.text((M, 50), 'Projeto Designer v3 · Barzakh · um estúdio Al Kántara', fill=(238, 234, 226), font=ImageFont.truetype(fb, 54))
d.text((M, 120), 'Padrão escuro da placa aprovada · Fraunces · Behance 808x632 (7 cases) · Pinterest 1000x1500 (34 pins)', fill=(180, 147, 90), font=ImageFont.truetype(fr, 28))
d.rectangle([W - M - 70, 62, W - M, 74], fill=(180, 147, 90))
y = 180
for i, c in enumerate(CASES):
    im = Image.open(f'{V}/behance/{c}/00-capa-808x632.jpg').resize((cw, chh), Image.LANCZOS)
    S.paste(im, (M + (i % 4) * (cw + M), y + (i // 4) * (chh + M)))
S.paste(Image.open(f'{V}/oferta/pagina/img/placa-hero.jpg').resize((cw, chh), Image.LANCZOS), (M + 3 * (cw + M), y + chh + M))
y += 2 * (chh + M) + 20
for i, p in enumerate(PINS):
    S.paste(Image.open(f'{V}/pinterest/pins/{p}.jpg').resize((pw, ph), Image.LANCZOS), (M + i * (pw + M), y))
y += ph + M + 20
for i, m in enumerate(MOCK):
    S.paste(Image.open(f'{MK}/{m}.jpg').resize((mw, mh), Image.LANCZOS), (M + i * (mw + M), y))
S.save(OUT, quality=88); print(OUT, S.size)
