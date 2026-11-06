# Pranchas de campanha da Orégano Turbo com as fotos geradas por IA pelo Lindson (Rocco + Paollo, conta Leandro, 06/11/2026).
# Formatos do Rocco: foto de campanha ocupando tudo, manchete gorda (Anton) no espaço vazio da foto, logo pequeno, selo.
# Uso: python3 gerar-campanha.py && node render-campanha.js  → pecas-campanha/*.jpg (1080x1350)
import os
D = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(D, 'gerar4.py')).read().split('\nP = []')[0]
g = {'__file__': os.path.join(D, 'gerar4.py')}
exec(src, g)
V, C, CA, T, AC = g['VERDE'], g['CREME'], g['CARVAO'], g['TOMATE'], g['ACAFRAO']
logo, selo = g['logo'], g['selo']
F = lambda n: f'fotos-ia/hd/{n}.jpg'

def peca(id, foto, pos, inner):
    return (id, f'<div class="a" style="inset:0;background:url({F(foto)}) {pos}/cover"></div>' + inner)

H = lambda t, s, cor, x, y, extra='': f'<div class="a" style="left:{x}px;top:{y}px;font:400 {s}px/.86 Anton;text-transform:uppercase;color:{cor};letter-spacing:-.005em;{extra}">{t}</div>'
L = lambda x, y, cor=C, folha=None, seta=None: f'<div class="a" style="left:{x}px;top:{y}px">{logo(34, cor, folha or cor, seta or V, sub=False)}</div>'
T2 = lambda t, x, y, cor=C, w=520, extra='': f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;font:500 26px/1.35 Inter;color:{cor};{extra}">{t}</div>'
SELO = lambda x, y, tam, bg=V, fg=C, gid='c': f'<div class="a" style="left:{x}px;top:{y}px">{selo(tam, "SÓ PIZZARIAS · MARKETING DE VENDAS · ", bg, fg, gid=gid)}</div>'
SOMBRA = 'text-shadow:0 6px 0 rgba(0,0,0,.18)'

P = [
    peca('c01-mais-pedidos', 'B3-pizza-voando', 'center',
         H('Mais<br>pedidos.', 190, C, 60, 70, SOMBRA) + L(64, 1250) + SELO(860, 1120, 170, CA, C, 'c1')),
    peca('c02-menos-app-mais-zap', 'B2-caixa-ceu', 'center',
         H('Menos app.', 128, '#fff', 56, 60, SOMBRA) + H('Mais zap.', 128, AC, 56, 172, SOMBRA) + L(64, 1250, '#fff', '#fff', CA)),
    peca('c03-fome-se-vende', 'B1-mordida', '70% center',
         H('Fome<br>se vende<br>com foto.', 104, CA, 52, 80) + T2('A gente grava a sua pizza do jeito que dá fome. E coloca no anúncio certo.', 56, 420, CA, 330) + L(64, 1250, CA, V, C)),
    peca('c04-so-pizzarias-bone', 'A6-bone', 'center',
         H('Só<br>pizzarias.', 150, V, 56, 70) + L(64, 1250, CA, V, C)),
    peca('c05-pedido-saindo', 'A8-adesivo-pedido-saindo', 'center',
         H('Do balcão<br>até a porta.', 120, C, 56, 64, SOMBRA) + L(64, 1250)),
]
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter+Tight:wght@600;700;800&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">'
CSS = 'body{margin:0;background:#888}section.f{position:relative;overflow:hidden;margin:0 0 40px;width:1080px;height:1350px}.a{position:absolute}*{box-sizing:border-box}'
open(os.path.join(D, 'pecas-campanha.html'), 'w').write(
    f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>' +
    ''.join(f'<section class="f" id="{i}">{c}</section>' for i, c in P) + '</body></html>')
print(len(P), 'pranchas')
