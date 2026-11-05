"""Acabamento das figurinhas do Leo (conta Leandro, 05/11/2026).
python3 acabamento.py <pasta>  (lê <pasta>/brutas/*.png, grava <pasta>/figurinhas/NN.webp e .png e <pasta>/figurinhas/icone-pacote.png)
Padrão do WhatsApp: 512x512, fundo transparente, margem de 16 px, .webp de até 100 KB; ícone do pacote 96x96 PNG de até 50 KB."""
import sys, os, glob, io
from PIL import Image, ImageFilter, ImageChops
pasta = sys.argv[1]; out = os.path.join(pasta, 'figurinhas'); os.makedirs(out, exist_ok=True)
def contorno(im, r=22):
    a = im.getchannel('A'); d = a.filter(ImageFilter.GaussianBlur(r / 2)).point(lambda v: 255 if v > 8 else 0)
    d = d.filter(ImageFilter.GaussianBlur(1.6))                      # borda branca lisa
    sombra = d.filter(ImageFilter.GaussianBlur(14)).point(lambda v: int(v * .35))
    base = Image.new('RGBA', im.size, (0, 0, 0, 0))
    sh = Image.new('RGBA', im.size, (5, 20, 60, 255)); sh.putalpha(sombra); base.alpha_composite(sh, (0, 8))
    br = Image.new('RGBA', im.size, (255, 255, 255, 255)); br.putalpha(d); base.alpha_composite(br)
    base.alpha_composite(im); return base
for f in sorted(glob.glob(os.path.join(pasta, 'brutas', '*.png'))):
    im = contorno(Image.open(f).convert('RGBA'))
    bb = im.getchannel('A').point(lambda v: 255 if v > 10 else 0).getbbox(); im = im.crop(bb)
    im.thumbnail((480, 480), Image.LANCZOS)                           # 512 - 2 x 16 de margem
    c = Image.new('RGBA', (512, 512), (0, 0, 0, 0)); c.alpha_composite(im, ((512 - im.width) // 2, (512 - im.height) // 2))
    n = os.path.splitext(os.path.basename(f))[0]
    c.save(os.path.join(out, n + '.png'))
    for q in (90, 80, 70, 60):
        b = io.BytesIO(); c.save(b, 'WEBP', quality=q, method=6)
        if b.tell() < 100_000: break
    open(os.path.join(out, n + '.webp'), 'wb').write(b.getvalue()); print(n, f'{b.tell() // 1024} KB (q{q})')
logo = sys.argv[2] if len(sys.argv) > 2 else None
if logo:
    l = Image.open(logo).convert('RGBA'); l = l.crop(l.getchannel('A').getbbox()); l.thumbnail((88, 88), Image.LANCZOS)
    ic = Image.new('RGBA', (96, 96), (0, 0, 0, 0)); ic.alpha_composite(l, ((96 - l.width) // 2, (96 - l.height) // 2))
    ic.save(os.path.join(out, 'icone-pacote.png')); print('icone-pacote.png')
