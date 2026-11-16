"""Feed Instagram Al Kántara: 12 posts (estáticos, carrosséis e capas de Reel), 1080x1350. Conta Pedro, 16/11/2026.
python3 feed.py && node render.js ../_tmp/lista.json"""
import json, os
from base import *
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PL = json.load(open(f'{R}/plano/plano.json'))
FOTO = dict(p01='slz-centro-2', p02='servidores', p03='servidores-2', p04='sombra-tijolo', p05='arco-concreto', p06='estudio-video',
            p07='gerador', p08='sombra-kerry', p09='slz-centro-3', p10='arco-radial', p11='estudio-video-2', p12='slz-centro-4')
FOTO_FIM = dict(p02='estudio-monitores')  # última tela com foto (opcional)
T = f'{R}/_tmp'; os.makedirs(T, exist_ok=True); OUT = f'{R}/instagram'; os.makedirs(OUT, exist_ok=True)
W, Hh = 1080, 1350
EX = '''.pg{width:1080px;height:1350px}
.foto{position:absolute;inset:0;background-size:cover;background-position:center;filter:grayscale(1) contrast(1.15) brightness(.62)}
.duo{position:absolute;inset:0;mix-blend-mode:multiply}
.vinh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,12,14,.15) 0%,rgba(11,12,14,.0) 35%,rgba(11,12,14,.92) 100%)}
.topo{position:absolute;left:72px;right:72px;top:64px;display:flex;justify-content:space-between;align-items:center}
.topo img{height:44px}
.pe{position:absolute;left:72px;right:72px;bottom:56px;display:flex;justify-content:space-between;align-items:center;opacity:.75}
.tag{display:inline-flex;align-items:center;gap:14px}.tag i{width:14px;height:14px;background:var(--c)}
h1{font-size:132px;line-height:.92}h1 em{color:var(--c)}
.ap{font-size:34px;line-height:1.35;max-width:820px;margin-top:30px;opacity:.88}
.num{font:400 italic 420px/0.8 F;position:absolute;right:40px;bottom:80px;color:var(--c);opacity:.95}
.card{background:rgba(239,234,225,.06);border:1px solid rgba(239,234,225,.14);border-radius:28px;padding:44px}
.cla .card{background:rgba(11,12,14,.04);border-color:rgba(11,12,14,.14)}
'''
def ftag(k): return f'background-image:url(file://{R}/fotos/{k}.jpg)'
def topo(claro=False, div='grupo'):
    return f'<div class="topo"><img src="{LOGO_P if claro else LOGO_N}"><span class="mono tag"><i></i>{NOME[div].split(" · ")[0]}</span></div>'
def pe(t, n=''):
    return f'<div class="pe mono"><span>{t}</span><span>{n}</span></div>'
lista = []
def salva(nome, corpo, w=W, h=Hh, ex=EX):
    p = f'{T}/{nome}.html'; open(p, 'w').write(doc(w, h, corpo, ex)); lista.append(dict(html=p, png=f'{OUT}/{nome}.jpg', w=w, h=h))

def estatico(p, i):
    c = COR[p['divisao']]; f = p['fundo']; k = FOTO[p['id']]; d = p['divisao']
    if i % 3 == 0:   # A: foto P&B em tela cheia, título embaixo, K aceso cortado à direita
        corpo = f'''<div class="pg esc" style="--c:{c}"><div class="foto" style="{ftag(k)}"></div><div class="vinh"></div>
<div style="position:absolute;right:-260px;top:120px;width:720px;opacity:.9">{simb(IDX[d], c, 'rgba(11,12,14,.55)')}</div>
{topo(False, d)}<div style="position:absolute;left:72px;right:72px;bottom:150px"><p class="mono" style="color:{c}">{NOME[d]}</p><h1 style="margin-top:22px">{it(p['titulo'])}</h1><p class="ap">{H.escape(p['apoio'])}</p></div>
{pe('@alkantaragroup', 'São Luís · MA')}<div class="grao"></div></div>'''
    elif i % 3 == 1:   # B: fundo claro, foto em ARCO (pedra-chave) à direita, título gigante vazando
        corpo = f'''<div class="pg cla" style="--c:{c}">{topo(True, d)}
<div style="position:absolute;right:72px;top:190px;width:470px;height:760px;border-radius:235px 235px 0 0;overflow:hidden"><div class="foto" style="{ftag(k)};filter:grayscale(1) contrast(1.1) brightness(.85)"></div><div class="duo" style="background:{c};opacity:.35"></div></div>
<div style="position:absolute;left:72px;top:250px;width:560px"><p class="mono" style="color:{c}">{NOME[d]}</p></div>
<div style="position:absolute;left:66px;right:60px;bottom:170px"><h1 style="font-size:150px">{it(p['titulo'])}</h1></div>
<p class="ap" style="position:absolute;left:72px;bottom:96px;font-size:28px;max-width:900px">{H.escape(p['apoio'])}</p>
{pe('', '')}<div class="grao"></div></div>'''
    else:   # C: cor chapada da divisão, foto recortada em faixa, K tinta gigante
        corpo = f'''<div class="pg" style="background:{c};color:#0B0C0E;--c:#0B0C0E">
<div style="position:absolute;left:-120px;bottom:-140px;width:900px;opacity:.16">{simb(IDX[d], '#0B0C0E', '#0B0C0E')}</div>
{topo(True, d)}
<div style="position:absolute;left:72px;right:72px;top:180px;height:420px;overflow:hidden;border-radius:4px"><div class="foto" style="{ftag(k)};filter:grayscale(1) contrast(1.2) brightness(.9)"></div><div class="duo" style="background:{c}"></div></div>
<div style="position:absolute;left:72px;right:72px;bottom:150px"><h1 style="font-size:124px">{it(p['titulo']).replace('<em>','<em style="color:#EFEAE1">')}</h1><p class="ap">{H.escape(p['apoio'])}</p></div>
{pe('@alkantaragroup', NOME[d].split(' · ')[0])}<div class="grao"></div></div>'''
    salva(f"{p['id']}", corpo)

LAY = ['capa', 'num', 'cartao', 'frase', 'lista', 'fim']
def carrossel(p):
    c = COR[p['divisao']]; d = p['divisao']; tel = p['telas']; n = len(tel); claro = p['fundo'] == 'claro'
    cl = 'cla' if claro else 'esc'
    for j, t in enumerate(tel):
        tt, tx = it(t['titulo']), H.escape(t['texto']); pag = f'{j+1:02d} / {n:02d}'
        if j == 0:
            bg = 'esc' if not claro else 'cla'
            corpo = f'''<div class="pg {bg}" style="--c:{c}"><div style="position:absolute;inset:0 0 0 0"><div class="foto" style="{ftag(FOTO[p['id']])};{'filter:grayscale(1) contrast(1.1) brightness(.95);opacity:.55' if claro else ''}"></div></div>
<div class="vinh" style="{'background:linear-gradient(180deg,rgba(239,234,225,.2),rgba(239,234,225,.97) 78%)' if claro else ''}"></div>
<div style="position:absolute;right:-200px;top:-60px;width:620px">{simb(IDX[d], c, 'rgba(0,0,0,0)')}</div>
{topo(claro, d)}<div style="position:absolute;left:72px;right:72px;bottom:160px"><p class="mono" style="color:{c}">Carrossel · arraste →</p><h1 style="margin-top:24px;font-size:140px">{tt}</h1><p class="ap">{tx}</p></div>{pe(NOME[d], pag)}<div class="grao"></div></div>'''
        elif j == n - 1:
            ff = FOTO_FIM.get(p['id'])
            fbg = f'<div class="foto" style="{ftag(ff)};opacity:.5"></div><div class="vinh"></div>' if ff else ''
            corpo = f'''<div class="pg esc" style="--c:{c}">{fbg}<div style="position:absolute;left:50%;top:200px;width:380px;transform:translateX(-50%)">{simb(IDX[d], c, '#1f2126')}</div>
{topo(False, d)}<div style="position:absolute;left:72px;right:72px;bottom:170px;text-align:center"><h1 style="font-size:104px">{tt}</h1><p class="ap" style="margin:26px auto 0">{tx}</p>
<p class="mono" style="margin-top:40px;display:inline-block;padding:22px 34px;border:1px solid {c};border-radius:999px;color:#EFEAE1">Link na bio · alkantaragroup.pages.dev</p></div>{pe('@alkantaragroup', pag)}<div class="grao"></div></div>'''
        else:
            lay = ['num', 'cartao', 'frase', 'lista'][(j - 1 + hash(p['id']) % 2) % 4]
            bgc = cl if j % 2 else ('cor' if not claro else 'esc')
            st = f'background:{c};color:#0B0C0E' if bgc == 'cor' else ''
            cc = '#0B0C0E' if bgc == 'cor' else c
            cls = 'cla' if bgc == 'cla' else ('' if bgc == 'cor' else 'esc')
            em = tt.replace('<em>', f'<em style="color:{"#EFEAE1" if bgc=="cor" else c}">')
            if lay == 'num':
                inner = f'<div class="num" style="color:{cc};opacity:.9">{j:02d}</div><div style="position:absolute;left:72px;top:250px;width:640px"><h2 style="font-size:124px;line-height:.95">{em}</h2><p class="ap">{tx}</p></div>'
            elif lay == 'cartao':
                inner = f'<div style="position:absolute;left:72px;right:72px;top:240px"><p class="mono" style="color:{cc}">{j:02d} · {NOME[d].split(" · ")[0]}</p></div><div class="card" style="position:absolute;left:72px;right:72px;bottom:150px;padding:64px"><h2 style="font-size:104px;line-height:1">{em}</h2><p class="ap">{tx}</p></div><div style="position:absolute;right:72px;top:300px;width:300px">{simb(IDX[d], cc, "rgba(127,127,127,.18)")}</div>'
            elif lay == 'frase':
                inner = f'<div style="position:absolute;left:72px;right:72px;top:50%;transform:translateY(-50%)"><p style="font:400 italic 200px/.7 F;color:{cc}">“</p><h2 style="font-size:120px;line-height:1">{em}</h2><div style="height:4px;width:160px;background:{cc};margin:44px 0 30px"></div><p class="ap">{tx}</p></div>'
            else:
                partes = [s.strip() for s in t['texto'].replace(';', '.').split('.') if s.strip()]
                li = ''.join(f'<li style="display:grid;grid-template-columns:90px 1fr;padding:26px 0;border-top:1px solid rgba(127,127,127,.3)"><span class="mono" style="color:{cc}">{k+1:02d}</span><span style="font-size:36px">{H.escape(s)}.</span></li>' for k, s in enumerate(partes[:4]))
                inner = f'<div style="position:absolute;left:72px;right:72px;top:220px"><h2 style="font-size:112px;line-height:1">{em}</h2><ul style="list-style:none;margin-top:50px">{li}</ul></div>'
            ghost = f'<div style="position:absolute;right:-240px;bottom:-200px;width:900px;opacity:.07">{simb(IDX[d], "currentColor", "currentColor")}</div>'
            corpo = f'<div class="pg {cls}" style="{st};--c:{cc}"><style>.pg .ap{{font-size:40px}}</style>{ghost}{topo(bgc=="cla" or bgc=="cor", d)}{inner}{pe(NOME[d], pag)}<div class="grao"></div></div>'
        salva(f"{p['id']}-{j+1:02d}", corpo)

def capa_reel(p, i):
    c = COR[p['divisao']]; d = p['divisao']
    corpo = f'''<div class="pg esc" style="width:1080px;height:1920px;--c:{c}"><div class="foto" style="{ftag(FOTO[p['id']])}"></div><div class="vinh"></div>
<div style="position:absolute;right:-300px;top:260px;width:860px;opacity:.95">{simb(IDX[d], c, 'rgba(11,12,14,.5)')}</div>
{topo(False, d)}<div style="position:absolute;left:72px;right:72px;top:1010px"><p class="mono" style="color:{c}">Reel · {NOME[d]}</p><h1 style="margin-top:24px;font-size:140px">{it(p['titulo'])}</h1></div>
{pe('@alkantaragroup', 'Assista')}<div class="grao"></div></div>'''
    salva(f"{p['id']}-capa", corpo, 1080, 1920)

e = 0
for p in PL['posts']:
    if p['tipo'] == 'estatico': estatico(p, e); e += 1
    elif p['tipo'] == 'carrossel': carrossel(p)
    else: capa_reel(p, 0)
json.dump(lista, open(f'{T}/lista.json', 'w'))
print(len(lista))
