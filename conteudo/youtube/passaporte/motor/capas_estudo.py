"""Capas "Pintura anotada" (estilo novo das pesquisas de designer, pedido do Lindson em 09/11/2026, conta Zuleide, Peter).
Exceção aprovada só para os longos 10 a 12; as capas aprovadas do capas2.py continuam como alternativa no teste A/B.

Composição copiada (ver ../capas/TEMPLATE-LONGOS-10-12.md):
- Johnny Harris (EUA): a imagem com UMA anotação feita à mão (círculo + seta + nota manuscrita) apontando o detalhe da história;
- Fall of Civilizations (Reino Unido): a pintura de ponta a ponta, sem moldura, com título serifado em caixa alta, curto e grave;
- Veritasium (Austrália/EUA): um único foco, no máximo 3 palavras, imagem clara (sem fundo escuro chapado).
Identidade do Passaporte mantida: gravura de Doré com a cor de cinema do capas2 (grade), "PASSAPORTE DA BÍBLIA" em Special Elite,
etiqueta ciano da série e palavra-chave em amarelo; a nota manuscrita usa a Caveat, fonte de anotações do canal (IDENTIDADE.md).

python3 capas_estudo.py [ids] -> ../capas/v2/<id>-N.jpg (1280x720) e ../capas/previa-capas-10-12.jpg (nova x aprovada)"""
import json, os, subprocess, sys
D = os.path.dirname(os.path.abspath(__file__))
# reaproveita do capas2 só as funções de cor e recorte (sem rodar o gerador dele)
_src = open(os.path.join(D, 'capas2.py')).read(); exec(_src[:_src.index('ESTILOS = ')])
from PIL import Image, ImageEnhance

NOVAS = {
 # foco = (x, y) relativo na gravura; circ = (x, y, raio) relativo na gravura; nota = texto manuscrito
 'longo-10': dict(grav='064', foco=(.5, .47), circ=(.45, .5, .2), nota='e ele dormia?', seta='dir',
                  txt='NÃO ERA <b>SHOW</b>', tag='MILAGRES DE JESUS'),
 'longo-11': dict(grav='019', foco=(.5, .8), circ=(.17, .76, .1), nota='livres... e quiseram voltar', seta='dir',
                  txt='POR QUE <b>VOLTAR?</b>', tag='ÊXODO'),
 'longo-12': dict(grav='095', foco=(.5, .58), circ=(.66, .53, .12), nota='cadê o cavalo?', seta='esq',
                  txt='ELE <b>PERSEGUIA</b>', tag='APÓSTOLO PAULO'),
}

CSS2 = '''<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Caveat:wght@700&display=swap" rel="stylesheet"><style>
.tt{position:absolute;left:56px;bottom:46px;font:900 112px/0.95 Cinzel;color:#fff;letter-spacing:.01em;max-width:1100px;
 text-shadow:0 6px 0 rgba(0,0,0,.55),0 0 40px rgba(0,0,0,.85)}.tt b{color:#FFD23F;font-weight:900}
.nt{position:absolute;font:700 64px/1 Caveat;color:#FFD23F;text-shadow:0 3px 0 #000,0 0 18px rgba(0,0,0,.9);white-space:nowrap;transform:rotate(-4deg)}
.tg2{position:absolute;left:56px;top:84px;padding:6px 16px;border:3px solid #5EE6EB;color:#5EE6EB;font:400 26px Anton;letter-spacing:.08em;
 background:rgba(6,20,26,.55);transform:rotate(-2deg)}
</style>'''


def nova(k, c, W=1280, H=720):
    im = Image.open(f'{RAIZ}/dore/{c["grav"]}.jpg').convert('RGB'); fx, fy = c['foco']
    cw = im.width; ch = cw / (16 / 9); y0 = min(max(fy * im.height - ch * .45, 0), im.height - ch)
    bg = recorte(c['grav'], 1.0, c['foco'])
    bg = ImageEnhance.Contrast(ImageEnhance.Brightness(bg).enhance(1.32)).enhance(1.08)   # capa clara (hipótese do Peter: claras > escuras)
    cx, cy, r = c['circ']; X = cx * W; Y = (cy * im.height - y0) / ch * H; R = r * W
    # círculo "à mão": elipse com o traço passando um pouco do ponto de partida
    path = f'M{X - R:.0f},{Y + R * .08:.0f} C{X - R:.0f},{Y - R * .75:.0f} {X + R * 1.05:.0f},{Y - R * .8:.0f} {X + R * 1.02:.0f},{Y:.0f} ' \
           f'C{X + R:.0f},{Y + R * .78:.0f} {X - R * .9:.0f},{Y + R * .85:.0f} {X - R * .92:.0f},{Y - R * .25:.0f}'
    d = 1 if c['seta'] == 'dir' else -1
    ax0, ay0 = X + d * R * .9, Y - R * .7; ax1, ay1 = ax0 + d * 150, ay0 - 95
    if ay1 < 190: ay0 = Y + R * .2; ax0 = X + d * R * 1.02; ax1, ay1 = ax0 + d * 150, ay0 + 40   # sem espaço em cima: a seta vem do lado
    seta = f'M{ax1:.0f},{ay1:.0f} Q{ax0 + d * 110:.0f},{ay0 - 10:.0f} {ax0:.0f},{ay0:.0f} M{ax0:.0f},{ay0:.0f} l{d * 34:.0f},-6 M{ax0:.0f},{ay0:.0f} l{d * 4:.0f},-34'
    nx = ax1 + (12 if d > 0 else -12); npos = f'left:{nx:.0f}px' if d > 0 else f'right:{W - nx:.0f}px'
    return pagina(CSS2 + f'''<div class="bg" style="background-image:url({uri(bg)})"></div>
<div style="position:absolute;inset:0;background:linear-gradient(0deg,rgba(4,10,14,.78),rgba(4,10,14,0) 46%)"></div>
<svg width="{W}" height="{H}" style="position:absolute;inset:0"><g fill="none" stroke="#000" stroke-opacity=".55" stroke-width="15" stroke-linecap="round"><path d="{path}"/><path d="{seta}"/></g>
<g fill="none" stroke="#FFD23F" stroke-width="8" stroke-linecap="round"><path d="{path}"/><path d="{seta}"/></g></svg>
<div class="nt" style="{npos};top:{ay1 - 70:.0f}px">{c['nota']}</div>
<div class="mk" style="left:56px;top:40px">PASSAPORTE DA BÍBLIA</div><div class="tg2">{c['tag']}</div>
<div class="tt">{c['txt']}</div>''')


ids = sys.argv[1:] or list(NOVAS)
pages = []
for k in ids:
    f = f'{TMP}/{k}-N.html'; open(f, 'w').write(nova(k, NOVAS[k])); pages.append((f, f'{OUT}/{k}-N.jpg', 1280, 720))
js = "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();for(const [f,o,w,h] of " + json.dumps(pages) + \
     "){const p=await b.newPage({viewport:{width:w,height:h}});await p.goto('file://'+f,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);" \
     "await p.waitForTimeout(400);await p.screenshot({path:o,type:'jpeg',quality:92});await p.close()}await b.close()})();"
subprocess.run(['node', '-e', js], check=True)
# prévia: nova (esquerda) x aprovada A do capas2 (direita), uma linha por longo
linhas = [(Image.open(f'{OUT}/{k}-N.jpg'), Image.open(f'{OUT}/{k}-A.jpg') if os.path.exists(f'{OUT}/{k}-A.jpg') else None) for k in ids]
pv = Image.new('RGB', (1280 * 2 + 60, 720 * len(linhas) + 40 * (len(linhas) + 1)), (14, 16, 22))
for i, (a, b) in enumerate(linhas):
    y = 40 + i * 760; pv.paste(a, (20, y))
    if b: pv.paste(b, (1300 + 20, y))
pv = pv.resize((pv.width // 2, pv.height // 2), Image.LANCZOS)
pv.save(f'{RAIZ}/capas/previa-capas-10-12.jpg', quality=90); print(len(pages), 'capas novas em', OUT, '+ prévia', f'{RAIZ}/capas/previa-capas-10-12.jpg')
