"""Capa 12 (Paulo), 3 opções no padrão aprovado das capas 10 e 11 (conta Zuleide, 10/11/2026).
Base: Caravaggio, "Conversão de São Paulo" (1600-01, Santa Maria del Popolo), domínio público, Wikimedia Commons, 1920 px
(../capas-longos-10-12/fontes/caravaggio-conversao-de-sao-paulo-commons-1920.jpg). Rosto grande, luz forte, manto vermelho.
O fundo escuro do Caravaggio (tenebrismo) é trocado por cor viva com chave de luminância: só o que está iluminado
(Saulo, braços, manto) fica na frente da palavra gigante.
- 12a "CEGO?"   copia EPIC HISTORY "MUTINY": palavra branca gigante no alto, braços erguidos de Saulo na frente dela, fundo azul vivo.
- 12b "ELE CAIU" copia CIÊNCIA TODO DIA "FLOW": close extremo no rosto, cor quente saturada, palavra atravessando com brilho.
- 12c "MUDOU"   copia JOHNNY HARRIS: céu aberto de fim de tarde, horizonte limpo de um lado, Saulo em meio corpo do outro.
python3 capa12_opcoes.py -> ../capas-longos-10-12/capa-12a.jpg, capa-12b.jpg, capa-12c.jpg"""
import json, os, subprocess, sys
import numpy as np, cv2
from PIL import Image, ImageEnhance
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from capas_jovem import uri, pagina, nuvens, P, FT, TMP, W, H

SRC = FT + 'caravaggio-conversao-de-sao-paulo-commons-1920.jpg'

def corte(box):
    im = Image.open(SRC).convert('RGB').crop(box).resize((W, H), Image.LANCZOS)
    im = ImageEnhance.Color(im).enhance(1.35); im = ImageEnhance.Contrast(im).enhance(1.12)
    return np.array(im).astype(np.float32)

def chave(rgb, a=.11, b=.24):
    """Máscara do que está iluminado (fica na frente), pela luminância suavizada."""
    L = cv2.GaussianBlur(cv2.cvtColor(rgb.astype(np.uint8), cv2.COLOR_RGB2GRAY), (0, 0), 2.2).astype(np.float32) / 255
    m = np.clip((L - a) / (b - a), 0, 1); m = m * m * (3 - 2 * m)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))
    return cv2.GaussianBlur(m, (0, 0), 1.2)

def comp(fundo, rgb, m, luz=1.15):
    fg = np.dstack([np.clip(rgb * luz, 0, 255).astype(np.uint8), (m * 255).astype(np.uint8)])
    return Image.fromarray(fundo.astype(np.uint8)), Image.fromarray(fg, 'RGBA')

def gradiente(c1, c2, cx=.5, cy=.0, raio=1.1):
    yy, xx = np.mgrid[0:H, 0:W]; r = np.clip(np.sqrt(((xx / W - cx) * 1.6) ** 2 + (yy / H - cy) ** 2) / raio, 0, 1)[..., None]
    return np.array(c1) * (1 - r) + np.array(c2) * r

def html(bg, antes, fg, depois):
    return pagina(f'<img class="l" style="inset:0" src="{uri(bg, "JPEG")}">{antes}<img class="l" style="inset:0" src="{uri(fg)}">{depois}')

def a():
    # MUTINY: Saulo caído de braços erguidos, recortado pela luz, na frente de "CEGO?" gigante; fundo azul vivo com feixe de luz.
    rgb = corte((80, 1290, 1920, 2325)); m = chave(rgb)
    f = gradiente((70, 150, 255), (14, 40, 150), cx=.62, cy=-.1)
    n = np.clip((nuvens(7) - .5) / .4, 0, 1)[..., None] ** 1.5; f = f * (1 - n * .35) + 255 * n * .35
    bg, fg = comp(f, rgb, m)
    return html(bg, '<div class="sh" style="mix-blend-mode:screen;background:linear-gradient(100deg,rgba(0,0,0,0) 40%,rgba(255,250,220,.55) 52%,rgba(0,0,0,0) 64%);filter:blur(16px)"></div>'
                    '<div class="t" style="left:0;right:0;top:14px;text-align:center;font-size:300px;letter-spacing:.03em;text-shadow:0 12px 0 rgba(5,15,60,.45)">CEGO?</div>', fg,
                '<div class="sh" style="background:linear-gradient(0deg,rgba(5,15,60,.45),rgba(0,0,0,0) 26%)"></div>'
                '<div class="selo"><div>PASSAPORTE</div><span>DA BÍBLIA</span></div><div class="tag" style="right:36px;bottom:34px">APÓSTOLO PAULO</div>')

def b():
    # FLOW: close extremo no rosto de Saulo (olhos fechados, luz no rosto), cor quente saturada, "ELE CAIU" atravessando.
    rgb = corte((820, 1880, 1880, 2476)); m = chave(rgb, .08, .2)
    f = gradiente((255, 120, 30), (120, 10, 10), cx=.55, cy=.75, raio=1.0)
    bg, fg = comp(f, rgb * np.array([1.08, 1.0, .9]), m, luz=1.2)
    return html(bg, '', fg,
                '<div class="t" style="left:0;right:0;top:60px;text-align:center;font-size:250px;letter-spacing:.02em;'
                'background:linear-gradient(180deg,#fff 55%,#d9f6ff);-webkit-background-clip:text;color:transparent;'
                'filter:drop-shadow(0 0 3px #FFD23F) drop-shadow(0 12px 18px rgba(0,0,0,.7)) drop-shadow(0 0 40px rgba(255,170,60,.6))">ELE CAIU</div>'
                '<div class="mk" style="left:40px;bottom:30px">PASSAPORTE DA BÍBLIA</div><div class="tag" style="right:40px;bottom:30px">APÓSTOLO PAULO</div>')

def c():
    # JOHNNY HARRIS: céu de fim de tarde e horizonte limpo à esquerda; Saulo de braços erguidos em meio corpo à direita, contra o sol.
    rgb = corte((391, 1480, 1920, 2340)); m = chave(rgb)
    hz = 520; yy = np.arange(H)[:, None, None].astype(np.float32); xx = np.arange(W)[None, :, None].astype(np.float32)
    t = np.clip(yy / hz, 0, 1)
    ceu = np.array([40, 110, 220]) * (1 - t) ** 1.5 + np.array([255, 170, 80]) * (1 - (1 - t) ** 1.5)
    ceu = ceu + np.exp(-(((xx - 760) / 300) ** 2 + ((yy - hz) / 140) ** 2)) * np.array([255, 210, 130]) * .8
    chao = np.array([170, 96, 50]) * np.ones_like(yy)
    f = np.where(yy < hz, ceu, chao + 0 * xx)
    bg, fg = comp(f, rgb, m, luz=1.2)
    fgA = np.array(fg); xs = np.arange(W)[None, :]; fgA[..., 3] = (fgA[..., 3] * np.clip((xs - 330) / 160, 0, 1)).astype(np.uint8)
    return html(bg, '', Image.fromarray(fgA, 'RGBA'),
                '<div class="t" style="left:44px;top:70px;font-size:250px;text-shadow:0 10px 0 rgba(0,0,0,.45),0 0 40px rgba(0,0,0,.35)">MUDOU</div>'
                '<div class="mk" style="left:48px;bottom:36px">PASSAPORTE DA BÍBLIA</div><div class="tag" style="left:48px;top:300px">APÓSTOLO PAULO</div>')

OPC = {'capa-12a': a, 'capa-12b': b, 'capa-12c': c}
if __name__ == '__main__':
    pages = []
    for k in sys.argv[1:] or list(OPC):
        f = f'{TMP}/{k}.html'; open(f, 'w').write(OPC[k]()); pages.append((f, f'{P}/{k}.jpg'))
    js = "const {chromium}=require('/opt/node-tools/node_modules/playwright');(async()=>{const b=await chromium.launch();for(const [f,o] of " + json.dumps(pages) + "){const p=await b.newPage({viewport:{width:1280,height:720}});await p.goto('file://'+f,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:o,type:'jpeg',quality:92});await p.close()}await b.close()})()"
    subprocess.run(['nice', 'node', '-e', js], check=True); print(len(pages), 'opções')
