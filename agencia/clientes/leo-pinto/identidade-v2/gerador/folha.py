# folha de conferência: python3 folha.py <glob> <saida> [larg] [alt] [colunas]
import sys, glob
from PIL import Image
fs = sorted(glob.glob(sys.argv[1])); w = int(sys.argv[3]) if len(sys.argv) > 3 else 300
h = int(sys.argv[4]) if len(sys.argv) > 4 else 380; n = int(sys.argv[5]) if len(sys.argv) > 5 else 7
c = Image.new('RGB', (w * n, h * ((len(fs) + n - 1) // n)), '#444')
for i, f in enumerate(fs):
    im = Image.open(f).convert('RGBA'); im.thumbnail((w - 10, h - 10)); c.paste(im, ((i % n) * w, (i // n) * h), im)
c.save(sys.argv[2], quality=85)
