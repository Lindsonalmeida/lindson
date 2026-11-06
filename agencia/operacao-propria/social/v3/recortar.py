# Recorte em quadro cheio (mesmo tamanho da foto, fundo transparente) para a letra passar POR TRÁS do produto/pessoa.
# Uso: MODELO=birefnet-portrait python3 recortar.py B1-mordida   → recortes/B1-mordida.webp  (Paollo, conta Leandro, 06/11/2026)
# Um recorte por processo (memória limitada).
import sys, os
from rembg import remove, new_session
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
n = sys.argv[1]
src = os.path.join(D, '../../identidade/fotos-ia/hd', n + '.png')
im = Image.open(src).convert('RGB')
im = im.resize((1296, round(1296 * im.height / im.width)), Image.LANCZOS)
r = remove(im, session=new_session(os.environ.get('MODELO', 'birefnet-general')))
r.save(os.path.join(D, 'recortes', n + '.webp'), quality=92, method=6)
print(n, r.size, r.getbbox())
