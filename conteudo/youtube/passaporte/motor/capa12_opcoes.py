"""Capa 12 (Paulo), 3 opções no padrão aprovado das capas 10 e 11 (conta Zuleide, 10/11/2026).
Base: Caravaggio, "Conversão de São Paulo" (1600-01, Santa Maria del Popolo), domínio público, Wikimedia Commons, 1920 px
(../capas-longos-10-12/fontes/caravaggio-conversao-de-sao-paulo-commons-1920.jpg). Rosto grande, luz forte, manto vermelho.
Saulo recortado (BiRefNet portrait + chave de luz no braço direito, restos do cavalo apagados) e posto na frente da
palavra gigante, sobre fundo de cor viva.
- 12a "CEGO?"   copia EPIC HISTORY "MUTINY": palavra branca gigante no alto, braços erguidos de Saulo na frente dela, fundo azul vivo.
- 12b "ELE CAIU" copia CIÊNCIA TODO DIA "FLOW": close extremo no rosto, cor quente saturada, palavra atravessando com brilho.
- 12c "MUDOU"   copia JOHNNY HARRIS: céu aberto de fim de tarde, horizonte limpo de um lado, Saulo em meio corpo do outro.
python3 capa12_opcoes.py -> ../capas-longos-10-12/capa-12a.jpg, capa-12b.jpg, capa-12c.jpg"""
import json, os, subprocess, sys
import numpy as np, cv2
from PIL import Image, ImageEnhance, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from capas_jovem import uri, pagina, nuvens, P, FT, TMP, W, H

SRC = FT + 'recorte-saulo-caravaggio.png'   # recorte 1920x1143 (faixa y 1380-2523 do quadro), BiRefNet + chave de luz no braço direito

def fig(escala, box=None):
    im = Image.open(SRC)
    if box: im = im.crop(box)
    im = im.resize((int(im.width * escala), int(im.height * escala)), Image.LANCZOS)
    rgb = im.convert('RGB'); rgb = ImageEnhance.Color(rgb).enhance(1.3); rgb = ImageEnhance.Contrast(rgb).enhance(1.1); rgb = ImageEnhance.Brightness(rgb).enhance(1.12)
    rgb.putalpha(im.getchannel('A')); return rgb

def sombra(im, alfa=.5, raio=18):
    s = Image.new('RGBA', im.size, (5, 10, 40, 0)); s.putalpha(im.getchannel('A').filter(ImageFilter.GaussianBlur(raio)).point(lambda v: int(v * alfa))); return s

def gradiente(c1, c2, cx=.5, cy=.0, raio=1.1):
    yy, xx = np.mgrid[0:H, 0:W]; r = np.clip(np.sqrt(((xx / W - cx) * 1.6) ** 2 + (yy / H - cy) ** 2) / raio, 0, 1)[..., None]
    return np.array(c1) * (1 - r) + np.array(c2) * r

def fundo(arr): return uri(Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)), 'JPEG')

def a():
    # EPIC HISTORY "MUTINY": fundo azul vivo com nuvens e feixe de luz, "CEGO?" gigante no alto, Saulo caído com os braços
    # erguidos NA FRENTE da palavra; selo do canal no canto.
    f = gradiente((90, 170, 255), (16, 44, 170), cx=.55, cy=-.05)
    n = np.clip((nuvens(7) - .5) / .4, 0, 1)[..., None] ** 1.5; f = f * (1 - n * .4) + 255 * n * .4
    p = fig(.68)
    return pagina(f'''<img class="l" style="inset:0" src="{fundo(f)}">
<div class="sh" style="mix-blend-mode:screen;background:linear-gradient(100deg,rgba(0,0,0,0) 38%,rgba(255,250,220,.6) 50%,rgba(0,0,0,0) 62%);filter:blur(18px)"></div>
<div class="t" style="left:0;right:0;top:16px;text-align:center;font-size:300px;letter-spacing:.04em;text-shadow:0 12px 0 rgba(5,15,60,.4)">CEGO?</div>
<img class="l" style="left:{580 - p.width // 2 + 26}px;top:34px" src="{uri(sombra(p))}"><img class="l" style="left:{580 - p.width // 2}px;top:8px" src="{uri(p)}">
<div class="selo"><div>PASSAPORTE</div><span>DA BÍBLIA</span></div><div class="tag" style="right:36px;bottom:34px">APÓSTOLO PAULO</div>''')

def b():
    # CIÊNCIA TODO DIA "FLOW": close no rosto de Saulo (olhos fechados, luz no rosto), fundo quente saturado,
    # "ELE CAIU" gigante atravessando com brilho.
    f = gradiente((255, 150, 40), (140, 14, 10), cx=.55, cy=.7, raio=1.0)
    p = fig(1.0, (820, 420, 1920, 1100))
    return pagina(f'''<img class="l" style="inset:0" src="{fundo(f)}">
<img class="l" style="left:{640 - p.width // 2 + 40}px;top:70px" src="{uri(sombra(p, .45, 22))}"><img class="l" style="left:{640 - p.width // 2 + 10}px;top:46px" src="{uri(p)}">
<div class="t" style="left:0;right:0;top:40px;text-align:center;font-size:240px;letter-spacing:.02em;
 background:linear-gradient(180deg,#fff 55%,#d9f6ff);-webkit-background-clip:text;color:transparent;
 filter:drop-shadow(0 0 3px #FFD23F) drop-shadow(0 12px 18px rgba(0,0,0,.75)) drop-shadow(0 0 40px rgba(255,190,80,.7))">ELE CAIU</div>
<div class="mk" style="left:40px;bottom:30px">PASSAPORTE DA BÍBLIA</div><div class="tag" style="right:40px;bottom:30px">APÓSTOLO PAULO</div>''')

def c():
    # JOHNNY HARRIS: céu aberto de fim de tarde e horizonte limpo à esquerda; Saulo em meio corpo à direita, contra o sol.
    hz = 500; yy = np.arange(H)[:, None, None].astype(np.float32); xx = np.arange(W)[None, :, None].astype(np.float32)
    t = np.clip(yy / hz, 0, 1)
    ceu = np.array([40, 120, 230]) * (1 - t) ** 1.5 + np.array([255, 176, 84]) * (1 - (1 - t) ** 1.5)
    ceu = ceu + np.exp(-(((xx - 900) / 300) ** 2 + ((yy - hz) / 140) ** 2)) * np.array([255, 214, 140]) * .8
    chao = np.array([196, 116, 60]) * (1 - np.clip((yy - hz) / 220, 0, 1)) + np.array([120, 60, 30]) * np.clip((yy - hz) / 220, 0, 1)
    f = np.where(yy < hz, ceu, chao + 0 * xx)
    p = fig(.62)
    return pagina(f'''<img class="l" style="inset:0" src="{fundo(f)}">
<div class="t" style="left:44px;top:60px;font-size:270px;text-shadow:0 10px 0 rgba(0,0,0,.4),0 0 40px rgba(0,0,0,.3)">MUDOU</div>
<img class="l" style="right:{-120 - 20}px;bottom:{-60 - 20}px" src="{uri(sombra(p, .4, 24))}"><img class="l" style="right:-120px;bottom:-60px" src="{uri(p)}">
<div class="mk" style="left:48px;bottom:36px">PASSAPORTE DA BÍBLIA</div><div class="tag" style="left:50px;top:330px">APÓSTOLO PAULO</div>''')

OPC = {'capa-12a': a, 'capa-12b': b, 'capa-12c': c}
if __name__ == '__main__':
    pages = []
    for k in sys.argv[1:] or list(OPC):
        f = f'{TMP}/{k}.html'; open(f, 'w').write(OPC[k]()); pages.append((f, f'{P}/{k}.jpg'))
    js = "const {chromium}=require('/opt/node-tools/node_modules/playwright');(async()=>{const b=await chromium.launch();for(const [f,o] of " + json.dumps(pages) + "){const p=await b.newPage({viewport:{width:1280,height:720}});await p.goto('file://'+f,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:o,type:'jpeg',quality:92});await p.close()}await b.close()})()"
    subprocess.run(['nice', 'node', '-e', js], check=True); print(len(pages), 'opções')
