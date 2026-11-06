# Exporta as peças da marca Orégano Turbo em PNG transparente para gerar mockups realistas no Gemini (conta Leandro, 06/11/2026).
# Uso: python3 kit_mockup.py && node kit_mockup.js  → kit-mockup/*.png
import os
D = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(D, 'gerar4.py')).read().split('\nP = []')[0]
g = {'__file__': os.path.join(D, 'gerar4.py')}
exec(src, g)
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter+Tight:wght@600;700;800&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">'
V, C, CA = g['VERDE'], g['CREME'], g['CARVAO']
pecas = {
    'logo-horizontal-verde': (1800, 420, g['logo'](150, CA, V, C)),
    'logo-horizontal-creme': (1800, 420, g['logo'](150, C, C, V)),
    'logo-monocromatico-branco': (1800, 420, g['logo'](150, '#ffffff', '#ffffff', CA, sub=False)),
    'simbolo-verde': (1000, 1000, g['simbolo'](900)),
    'simbolo-branco': (1000, 1000, g['simbolo'](900, '#ffffff', CA)),
    'selo-redondo': (1000, 1000, g['selo'](900, 'MARKETING DE VENDAS PARA PIZZARIAS · ', V, C)),
}
os.makedirs(os.path.join(D, 'kit-mockup'), exist_ok=True)
html = '<!doctype html><html><head><meta charset="utf-8">' + FONTS + '<style>body{margin:0;background:transparent}.p{display:flex;align-items:center;justify-content:center;margin:0 0 20px}</style></head><body>'
for n, (w, h, inner) in pecas.items():
    html += f'<div class="p" id="{n}" style="width:{w}px;height:{h}px">{inner}</div>'
open(os.path.join(D, 'kit-mockup', 'pecas.html'), 'w').write(html + '</body></html>')
print('ok', list(pecas))
