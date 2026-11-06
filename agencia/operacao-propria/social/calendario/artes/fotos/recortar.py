# Recorte em quadro cheio (mesmo tamanho da foto, fundo transparente) para a letra passar POR TRÁS do produto/pessoa.
# Mesmo método de ../../../v3/recortar.py. Uso: MODELO=birefnet-portrait python3 recortar.py B5-motoboy [sufixo]
# Um recorte por processo (memória limitada). Paollo, 06/11/2026.
import sys, os
from rembg import remove, new_session
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
n = sys.argv[1]; suf = sys.argv[2] if len(sys.argv) > 2 else ''
base = os.path.join(D, '../../../../identidade/fotos-ia/hd', n)
src = base + '.png' if os.path.exists(base + '.png') else base + '.jpg'
im = Image.open(src).convert('RGB')
im = im.resize((1296, round(1296 * im.height / im.width)), Image.LANCZOS)
r = remove(im, session=new_session(os.environ.get('MODELO', 'birefnet-general')))
r.save(os.path.join(D, 'recortes', n + suf + '.webp'), quality=92, method=6)
print(n + suf, r.size, r.getbbox())
