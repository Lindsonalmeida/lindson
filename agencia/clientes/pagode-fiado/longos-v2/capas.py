# Capas (thumbnails 1280x720) dos longos v2: foto do personagem da faixa + título grande na identidade.
# Uso: python3 capas.py <pasta_trabalho>  ->  <pasta>/capas/paginas.json (depois: node render.js <pasta>/capas)
import json, sys, os, base64, html, io
from PIL import Image
W = sys.argv[1]; AQUI = os.path.dirname(os.path.abspath(__file__)); L = json.load(open(AQUI + '/letras.json'))
OUT = f'{W}/capas'; os.makedirs(OUT, exist_ok=True)
def b64(arq, crop=None, larg=1400):
    im = Image.open(f'{W}/img/{arq}').convert('RGB')
    if crop: im = im.crop(crop)
    if im.width > larg: im = im.resize((larg, int(im.height * larg / im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=88); return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
LOGO = 'data:image/png;base64,' + base64.b64encode(open(f'{W}/img/marca-dagua-150.png', 'rb').read()).decode()
DAVI = ('01-davi-lua-limpa.png', (0, 0, 690, 1024))
FOTO = {'00': ('07-seu-tiao.png', None), '01': ('capa-youtube-pagode-fiado.jpg', (0, 300, 1050, 1440)), '02': DAVI, '03': ('03-rafa-tanta.png', None),
        '04': ('06-bia-rebolo.png', None), '05': DAVI, '06': ('capa-album-copo-americano-3000.jpg', (0, 1000, 1900, 2900)), '07': DAVI,
        '08': ('05-mestre-ze-pandeiro.png', None), '09': ('06-bia-rebolo.png', None), '10': ('capa-youtube-pagode-fiado.jpg', (1480, 300, 2560, 1440))}
GANCHO = {'00': 'Mesa sete de novo?', '01': 'Ela entrou no bar…', '02': 'O primeiro verão', '03': 'Tum, tum…', '04': 'Termina e volta', '05': 'Três linhas e o fim',
          '06': 'Pendura o coração', '07': 'Dois risquinhos azuis', '08': 'O causo do Mestre', '09': 'Levanta, Davi!', '10': 'Olha quem chegou'}
e = html.escape; pags = []
for k, f in L.items():
    arq, cr = FOTO[k]; pal = f['titulo'].replace('Prólogo: ', '').split(); a, z = ' '.join(pal[:-1]), pal[-1]
    pags.append(dict(nome=f'capa{k}', sel='.c', html=f'''<html><head><style>@import url('https://fonts.googleapis.com/css2?family=Shrikhand&family=Caveat+Brush&family=Work+Sans:wght@800&display=block');
*{{margin:0;box-sizing:border-box}}body{{background:#111}}</style></head><body>
<div class="c" style="position:relative;width:1280px;height:720px;overflow:hidden;background:#111">
<div style="position:absolute;right:0;top:0;width:820px;height:720px;background:url({b64(arq, cr)}) center 30%/cover;filter:saturate(1.08) contrast(1.05)"></div>
<div style="position:absolute;inset:0;background:linear-gradient(90deg,#111 0,#111 33%,rgba(17,17,17,.82) 48%,rgba(17,17,17,0) 74%)"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:16px;background:repeating-conic-gradient(#C0392B 0 25%,#F3E9D2 0 50%) 0 0/32px 32px"></div>
<img src="{LOGO}" style="position:absolute;left:52px;top:44px;width:104px">
<div style="position:absolute;left:180px;top:62px;font:800 19px 'Work Sans';letter-spacing:.24em;color:#F2B705">AO VIVO NO BAR<br>DO SEU TIÃO</div>
<div style="position:absolute;left:52px;top:200px;width:700px;font:400 {96 if len(f['titulo']) < 20 else 82}px/0.98 Shrikhand;color:#F3E9D2;text-shadow:0 8px 28px #000">{e(a)}<br><span style="color:#F2B705">{e(z)}</span></div>
<div style="position:absolute;left:56px;bottom:66px;font:400 52px 'Caveat Brush';color:#111;background:#F3E9D2;padding:2px 26px;transform:rotate(-2deg);box-shadow:0 10px 24px rgba(0,0,0,.5)">{e(GANCHO[k])}</div>
</div></body></html>'''))
json.dump(pags, open(f'{OUT}/paginas.json', 'w'), ensure_ascii=False); print(len(pags))
