# Behance Barzakh (conta Zuleide, 18/11/2026): capas novas dos 6 cases, banner, avatar e prévia do perfil.
# Referências copiadas (ver ../TEMPLATE.md):
#  - Anagrama (MX, behance.net/anagrama): banner escuro com a assinatura grande no centro.
#  - Bratus (VN, behance.net/bratus): grade de capas com a COR de cada marca saturada dando vida ao perfil escuro.
#  - Atipus (ES, behance.net/atipus): capa = aplicação real fotográfica, sem texto de anúncio.
#  Tudo dentro do padrão aprovado Barzakh: placa em arco no concreto, ouro escovado, brilho Lápis.
# Uso: python3 gerar.py   (gera pecas/*.jpg e previa.jpg com Playwright)
import os, base64
from playwright.sync_api import sync_playwright
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, '..', 'pecas'); os.makedirs(OUT, exist_ok=True)
R = os.path.abspath(os.path.join(H, '../../../..'))
PD = f'{R}/agencia/marca-lindson/projeto-designer/v3'
CONC = f'{PD}/marca/gerador/trat/concreto-escuro-v2.jpg'
LOGOS = f'{PD}/marca/logos/png'
FONTS = f'{R}/agencia/marca-holding/v2/fontes'
def u(p): return 'file://' + p
CSS = f'''@font-face{{font-family:Fr;src:url({u(FONTS+"/Fraunces-Regular.ttf")})}}@font-face{{font-family:FrS;src:url({u(FONTS+"/Fraunces-SemiBold.ttf")})}}
@font-face{{font-family:Mono;src:url({u(FONTS+"/JetBrainsMono-Medium.ttf")})}}@font-face{{font-family:IT;src:url({u(FONTS+"/InterTight-Medium.ttf")})}}@font-face{{font-family:ITS;src:url({u(FONTS+"/InterTight-SemiBold.ttf")})}}
*{{margin:0;box-sizing:border-box}}body{{background:#0A0C10}}
.gold{{background:linear-gradient(100deg,#7a5f33,#e9d29a 35%,#b4935a 55%,#f3e2b0 72%,#8a6c3b);-webkit-background-clip:text;color:transparent}}
.grain{{position:absolute;inset:0;opacity:.09;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)'/%3E%3C/svg%3E")}}
.mono{{font-family:Mono;letter-spacing:.3em;text-transform:uppercase}}'''

# case: pasta, nome, cor da placa (= fundo do 03-logo), brilho (cor da marca), composição
CASES = [
 ('real-time', 'Real Time', '#06070B', '#3D8BFF', 'c'),
 ('duble', 'Dublê', '#0C0B10', '#8B7CFF', 'e'),
 ('oregano-turbo', 'Orégano Turbo', '#1E5B3A', '#E8B23A', 'd'),
 ('processo-legislativo', 'Processo Legislativo', '#0A1F18', '#C9A46A', 'c'),
 ('wf-celulares', 'WF Celulares', '#000000', '#C9CBD6', 'e'),
 ('leo-pinto', 'Leo Pinto', '#081F63', '#F2A23A', 'd'),
]

def logo_crop(pasta):
    p = f'{PD}/behance/{pasta}/03-logo.jpg'; out = f'{OUT}/_logo-{pasta}.png'
    box = (560, 260, 1160, 640) if pasta == 'processo-legislativo' else (260, 230, 1140, 670)
    Image.open(p).convert('RGB').crop(box).save(out); return out

def placa(cor, glow, logo, w, h):
    return f'''<div style="position:absolute;left:-60%;top:-30%;width:220%;height:160%;background:radial-gradient(closest-side,{glow}aa,{glow}33 50%,transparent);filter:blur(24px)"></div>
<div style="position:absolute;inset:0;border-radius:{w/2}px {w/2}px 8px 8px;background:{cor};box-shadow:26px 34px 40px rgba(0,0,0,.75),6px 8px 10px rgba(0,0,0,.6),inset 0 2px 0 rgba(255,255,255,.18),inset 0 0 0 3px rgba(180,147,90,.55),inset 0 -40px 80px rgba(0,0,0,.45)">
<div style="position:absolute;inset:0;border-radius:inherit;background:linear-gradient(160deg,rgba(255,255,255,.16),transparent 40%,rgba(0,0,0,.25))"></div>
<img src="{u(logo)}" style="position:absolute;left:8%;width:84%;top:{h*0.42}px;mix-blend-mode:lighten;-webkit-mask-image:linear-gradient(90deg,transparent,#000 4%,#000 96%,transparent),linear-gradient(transparent,#000 10%,#000 90%,transparent);-webkit-mask-composite:source-in">
<div class="mono gold" style="position:absolute;bottom:{h*0.09}px;width:100%;text-align:center;font-size:{w*0.032}px">Identidade · Barzakh</div></div>'''

def capa(i, pasta, nome, cor, glow, comp):
    logo = logo_crop(pasta); W, Hh = 808, 632
    cor = '#%02x%02x%02x' % Image.open(logo).getpixel((3, 3))  # placa = fundo exato do logo (sem caixa visível)
    if comp == 'c':
        pw, ph = 330, 470; left = (W - pw) / 2; extra = ''
    else:
        pw, ph = 300, 430; left = 90 if comp == 'e' else W - 90 - 300
        mx = W - 90 - 300 if comp == 'e' else 90
        mock = f'{PD}/behance/{pasta}/07-papelaria.jpg'
        extra = f'''<div style="position:absolute;left:{mx}px;top:{(Hh-430)/2}px;width:300px;height:430px;border-radius:150px 150px 8px 8px;overflow:hidden;box-shadow:24px 30px 40px rgba(0,0,0,.7),inset 0 0 0 3px rgba(180,147,90,.6)">
<img src="{u(mock)}" style="width:100%;height:100%;object-fit:cover;object-position:50% 45%;transform:scale(1.25)"><div style="position:absolute;inset:0;border-radius:inherit;box-shadow:inset 0 0 0 3px #b4935a,inset 0 0 60px rgba(0,0,0,.45)"></div></div>'''
    top = (Hh - ph) / 2 - 6
    return f'''<html><head><style>{CSS}</style></head><body><div style="position:relative;width:{W}px;height:{Hh}px;overflow:hidden;background:url({u(CONC)}) center/cover">
<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,transparent 30%,rgba(5,6,9,.75))"></div>
<div style="position:absolute;inset:0;background:linear-gradient(115deg,rgba(255,240,210,.10),transparent 45%)"></div>
<div style="position:absolute;left:{left}px;top:{top}px;width:{pw}px;height:{ph}px">{placa(cor, glow, logo, pw, ph)}</div>{extra}
<div class="mono" style="position:absolute;left:28px;bottom:22px;font-size:10px;color:#b4935a;opacity:.8">0{i} · {nome}</div>
<div class="grain"></div></div></body></html>'''

def banner():
    arcs = ''.join(f'<div style="position:absolute;left:{880+k*170 if k<3 else 1720+(k-3)*170}px;top:96px;width:120px;height:190px;border-radius:60px 60px 4px 4px;background:{c[2]};box-shadow:14px 18px 20px rgba(0,0,0,.75),inset 0 0 0 2px rgba(180,147,90,.6),inset 0 1px 0 rgba(255,255,255,.2)"><div style="position:absolute;inset:-30px;background:radial-gradient(closest-side,{c[3]}55,transparent);z-index:-1;filter:blur(10px)"></div><div style="position:absolute;inset:0;border-radius:inherit;background:linear-gradient(160deg,rgba(255,255,255,.14),transparent 45%)"></div></div>' for k, c in enumerate(CASES))
    return f'''<html><head><style>{CSS}</style></head><body><div style="position:relative;width:3200px;height:410px;overflow:hidden;background:url({u(CONC)}) center 40%/cover">
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(5,6,9,.85),rgba(5,6,9,.35) 30%,rgba(5,6,9,.35) 70%,rgba(5,6,9,.85))"></div>
<div style="position:absolute;left:1600px;top:205px;width:900px;height:400px;transform:translate(-50%,-50%);background:radial-gradient(closest-side,#2B3A8Faa,transparent);filter:blur(20px)"></div>
{arcs}
<div style="position:absolute;left:1600px;top:70px;transform:translateX(-50%);text-align:center">
<img src="{u(LOGOS+'/barzakh-monolito-bronze.png')}" style="width:150px;display:block;margin:0 auto 8px">
<div class="gold" style="font-family:Fr;font-size:66px;letter-spacing:.32em;padding-left:.32em">BARZAKH</div>
<div class="mono" style="font-size:15px;color:#c9b07a;margin-top:12px">Um estúdio Al Kántara · identidade visual e branding</div></div>
<div class="grain"></div></div></body></html>'''

def b64(p): return 'data:image/jpeg;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

def previa(capas):
    cards = ''.join(f'<div><img src="{u(c)}" style="width:100%;border-radius:6px;display:block"><div style="font:600 13px ITS;color:#191919;margin-top:8px">{t}</div><div style="font:500 11px IT;color:#707070;margin-top:3px">Barzakh</div></div>' for c, t in capas)
    side = '''<div style="font:600 22px ITS;color:#191919">Barzakh</div><div style="font:500 13px IT;color:#555;margin-top:6px;line-height:1.5">Identidade visual e branding · um estúdio Al Kántara<br>São Luís, MA, Brasil<br><span style="color:#0057ff">lindsonalmeida.pages.dev/site/identidade</span></div>
<div style="margin-top:16px;background:#0057ff;color:#fff;font:600 13px ITS;text-align:center;padding:10px;border-radius:20px">Seguir</div>
<div style="margin-top:8px;border:1px solid #ddd;color:#191919;font:600 13px ITS;text-align:center;padding:10px;border-radius:20px">Contratar Barzakh</div>
<div style="margin-top:18px;font:500 12px IT;color:#444;line-height:1.6"><b>Serviços</b><br>Identidade visual · Brand book · Rebranding · Social kit · Site e landing page · Direção de arte</div>
<div style="margin-top:14px;font:500 12px IT;color:#444;line-height:1.6"><b>Sobre</b><br>Barzakh é o limiar entre dois mundos. É onde trabalhamos: no espaço entre a marca que um negócio tem hoje e a marca do tamanho que ele já é.</div>'''
    return f'''<html><head><style>{CSS} body{{background:#fff}}</style></head><body><div style="width:1440px;background:#fff;position:relative">
<div style="height:56px;border-bottom:1px solid #eee;display:flex;align-items:center;padding:0 24px;font:700 22px ITS;color:#191919">Bē<span style="font:500 13px IT;color:#666;margin-left:24px">Para você · Explorar · Contratar · Vagas</span></div>
<img src="{u(OUT+'/banner-3200x410.jpg')}" style="width:1440px;height:290px;object-fit:cover;display:block">
<div style="display:grid;grid-template-columns:300px 1fr;gap:28px;padding:0 28px 40px">
<div style="margin-top:-60px;background:#fff;border-radius:8px;padding:20px;box-shadow:0 4px 20px rgba(0,0,0,.08)"><img src="{u(OUT+'/avatar-500.jpg')}" style="width:110px;height:110px;border-radius:50%;margin-bottom:14px">{side}</div>
<div><div style="font:600 14px ITS;color:#191919;padding:18px 0;border-bottom:1px solid #eee;margin-bottom:20px">Trabalho <span style="color:#999;margin-left:18px">Moodboards</span><span style="color:#999;margin-left:18px">Serviços</span><span style="color:#999;margin-left:18px">Avaliações</span></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px">{cards}</div></div></div></div></body></html>'''

def shot(pg, html, path, w, h, sel='body > div'):
    tmp = f'{OUT}/_tmp.html'; open(tmp, 'w').write(html); pg.set_viewport_size({'width': w, 'height': h}); pg.goto(u(tmp)); pg.wait_for_timeout(500)
    pg.locator(sel).first.screenshot(path=path + '.png'); Image.open(path + '.png').convert('RGB').save(path, quality=92); os.remove(path + '.png')

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(device_scale_factor=2)
    capas = []
    for i, c in enumerate(CASES, 1):
        out = f'{OUT}/capa-{i:02d}-{c[0]}-808x632.jpg'; shot(pg, capa(i, *c), out, 808, 632)
        im = Image.open(out); im.save(out.replace('808x632', '1616x1264'), quality=92); im.resize((808, 632), Image.LANCZOS).save(out, quality=93)
        capas.append((out, f'{c[1]} · Identidade visual'))
    capas.append((f'{PD}/behance/barzakh/00-capa-808x632.jpg', 'Barzakh · identidade do estúdio'))
    pg2 = b.new_page(device_scale_factor=1)
    shot(pg2, banner(), f'{OUT}/banner-3200x410.jpg', 3200, 410)
    Image.open(f'{LOGOS}/barzakh-avatar-obsidiana.png').convert('RGB').resize((500, 500), Image.LANCZOS).save(f'{OUT}/avatar-500.jpg', quality=93)
    order = [capas[6]] + capas[:6]  # Barzakh fixado primeiro + 6 cases (ver ESTRATEGIA.md)
    shot(pg2, previa(order[:6]), os.path.join(H, '..', 'previa.jpg'), 1440, 1400)
    b.close()
for f in os.listdir(OUT):
    if f.startswith('_'): os.remove(f'{OUT}/{f}')
print('ok')
