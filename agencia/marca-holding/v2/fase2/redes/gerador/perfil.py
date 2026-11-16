"""Avatar, 6 capas de destaque, banner YouTube 2560x1440 (área segura 1546x423). Conta Pedro 16/11/2026."""
import json, os
from base import *
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')); T = f'{R}/_tmp'; os.makedirs(T, exist_ok=True)
PL = json.load(open(f'{R}/plano/plano.json')); YT = json.load(open(f'{R}/youtube/youtube.json'))
lista = []
def salva(dirr, nome, corpo, w, h):
    os.makedirs(f'{R}/{dirr}', exist_ok=True); p = f'{T}/{nome}.html'; open(p, 'w').write(doc(w, h, corpo)); lista.append(dict(html=p, png=f'{R}/{dirr}/{nome}.png', w=w, h=h))
# avatar: símbolo latão sobre tinta, centrado com margem para o recorte redondo
for rede in ['instagram', 'tiktok', 'youtube']:
    salva(rede, 'avatar', f'<div class="esc" style="width:1080px;height:1080px;display:grid;place-items:center;background:radial-gradient(circle at 50% 40%,#1c1e23,#0B0C0E 70%)">{simb(2, "#B8955A", "#EFEAE1", "width:560px")}<div class="grao"></div></div>', 1080, 1080)
DST = dict(Grupo=('grupo', 2), Labs=('labs', 0), Barzakh=('barzakh', 1), Media=('media', 2), Ventures=('ventures', 3))
for k, dd in enumerate(PL['destaques']):
    t = dd['titulo']; div, ac = DST.get(t, ('grupo', None))
    c = COR[div]
    if ac is None:   # Contato: as 4 pedras acesas
        s = '<svg viewBox="0 0 480 480" style="width:420px">' + ''.join(f'<path fill="{cc}" d="{p}"/>' for cc, p in zip(['#2E4BFF', '#E8461E', '#F0A202', '#0E8C66'], P)) + '</svg>'
    else: s = simb(ac, c, '#2a2c31', 'width:420px')
    salva('instagram/destaques', f'{k+1:02d}-{t.lower()}', f'''<div class="esc" style="width:1080px;height:1920px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:70px;background:radial-gradient(circle at 50% 46%,#191b20,#0B0C0E 62%)">
<div style="width:760px;height:760px;border-radius:50%;border:2px solid {c};display:grid;place-items:center">{s}</div>
<p style="font:400 italic 110px/1 F;color:#EFEAE1">{t}</p><div class="grao"></div></div>''', 1080, 1920)
# banner YouTube
b = YT['canal'].get('banner') or YT['canal'].get('texto_banner') or {}
tit = (b.get('texto') if isinstance(b, dict) else str(b)).replace('do Maranhão', '*do Maranhão.*')
apo = b.get('apoio', '') if isinstance(b, dict) else ''
salva('youtube', 'banner', f'''<div class="esc" style="width:2560px;height:1440px;position:relative;overflow:hidden">
<div style="position:absolute;right:-120px;top:-200px;width:1500px">{simb(2, '#B8955A', '#16181c')}</div>
<div style="position:absolute;left:0;right:0;bottom:0">{FAIXA.replace('6px','14px')}</div>
<div style="position:absolute;left:507px;top:508px;width:1546px;height:423px;display:flex;flex-direction:column;justify-content:center">
<img src="{LOGO_N}" style="height:58px;width:max-content;margin-bottom:30px">
<h1 style="font-size:104px;line-height:1">{it(tit or 'Estrutura para *o que vem.*')}</h1>
<p class="mono" style="margin-top:22px;color:#B8955A;font-size:26px">{H.escape(apo or 'Labs · Barzakh · Media · Ventures')}</p></div>
<div class="grao"></div></div>''', 2560, 1440)
json.dump(lista, open(f'{T}/lista-perfil.json', 'w')); print(len(lista), tit, '|', apo)
