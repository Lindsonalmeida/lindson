"""Capa vertical CLARA dos Shorts (1080x1920), igual para os dois canais.
Regra (BRIEF dos canais e pesquisa/top5-canais-dark.md): clara, quente ou ciano, até 3 palavras, 1 figura forte, SEM vermelho.
Substitui a capa escura da 1ª versão (fundo noturno e selo com borda vermelha).

Uso: python3 capa_short.py lista.json
lista.json = [{"img": "<caminho da imagem>", "texto": "ATÉ 3 PALAVRAS", "marca": "PASSAPORTE DA BÍBLIA", "saida": "<arquivo>.jpg",
               "cor": "#FFB547" (opcional), "pos": "50% 30%" (opcional, foco da imagem)}, ...]"""
import base64, json, os, sys
from playwright.sync_api import sync_playwright

CORES = ['#FFB547', '#7FE3F0', '#FFD36B', '#9BE7C4']  # quentes e ciano; nunca vermelho


def uri(p):
    ext = 'png' if p.lower().endswith('.png') else 'jpeg'
    return f'data:image/{ext};base64,' + base64.b64encode(open(p, 'rb').read()).decode()


def html(c, i):
    cor = c.get('cor') or CORES[i % len(CORES)]
    pal = c['texto'].split()
    fs = min(132, int(1100 / max(len(w) for w in pal)))  # a maior palavra cabe inteira na faixa
    assert len(pal) <= 3, 'capa com mais de 3 palavras: ' + c['texto']
    return f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@800&family=Special+Elite&display=swap" rel="stylesheet"><style>
*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1920px;overflow:hidden;background:#F4E7CF}}
.g{{position:absolute;inset:-30px;background:url({uri(c['img'])}) {c.get('pos', '50% 30%')}/cover;filter:grayscale(1) sepia(.7) contrast(1.4) brightness(1.1) saturate(1.6)}}
.luz{{position:absolute;inset:0;background:radial-gradient(circle at 65% 28%,rgba(255,214,140,.55),rgba(255,170,60,0) 55%);mix-blend-mode:screen}}
.base{{position:absolute;inset:auto 0 0 0;height:46%;background:linear-gradient(180deg,rgba(244,231,207,0),rgba(244,231,207,.55) 60%,rgba(244,231,207,.8))}}
.mk{{position:absolute;top:84px;width:100%;text-align:center;font:400 30px 'Special Elite';letter-spacing:.3em;color:#2A2013;text-shadow:0 0 18px rgba(255,240,210,.9)}}
.tag{{position:absolute;left:70px;right:70px;bottom:300px;display:flex;justify-content:center}}
.tag b{{background:{cor};color:#14110B;font:800 {fs}px/1.02 Manrope;text-transform:uppercase;padding:30px 46px;border-radius:26px;
 box-shadow:0 16px 50px rgba(40,25,5,.35);transform:rotate(-2deg);text-align:center;max-width:100%;overflow-wrap:normal}}
</style></head><body><div class="g"></div><div class="luz"></div><div class="base"></div>
<div class="mk">{c['marca']}</div><div class="tag"><b>{c['texto']}</b></div></body></html>'''


def gerar(lista):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get('CHROMIUM') or next((x for x in ['/opt/pw-browsers/chromium/chrome-linux/chrome', '/opt/pw-browsers/chromium'] if os.path.isfile(x)), None)); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        for i, c in enumerate(lista):
            pg.set_content(html(c, i), wait_until='networkidle'); pg.wait_for_timeout(300)
            os.makedirs(os.path.dirname(os.path.abspath(c['saida'])), exist_ok=True)
            pg.screenshot(path=c['saida'], type='jpeg', quality=88); print(c['saida'])
        b.close()


if __name__ == '__main__':
    gerar(json.load(open(sys.argv[1])))
