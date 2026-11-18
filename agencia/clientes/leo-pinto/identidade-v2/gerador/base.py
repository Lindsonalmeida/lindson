# Leo Pinto · identidade v2 premium (conta Pedro, 18/11/2026) · base comum: cores, fontes e CSS
# Cores = EXATAS do logo e da identidade atual (partido). Luxo vem de preto-base, tons profundos das mesmas cores,
# tipografia romana (Cinzel) + condensada (Barlow Condensed), retas e direção de foto. Modelo de processo: Al Kántara v2.
A = '../assets'
COR = {
    'laranja':  ('#FF7A1A', 'Laranja Solidário', 'primária · cor do partido'),
    'marinho':  ('#05316E', 'Marinho do Logo', 'secundária · letras do logo'),
    'royal':    ('#2350F5', 'Azul Royal', 'apoio · água do símbolo'),
    'ouro':     ('#FFC20E', 'Amarelo-Sol', 'acento metálico · sol do símbolo'),
    'preto':    ('#08090C', 'Preto Base', 'fundo de luxo'),
    'laranja2': ('#B4500C', 'Laranja Profundo', 'derivado (mesma matiz, 70%)'),
    'marinho2': ('#021A3D', 'Marinho Noite', 'derivado (mesma matiz, 55%)'),
    'branco':   ('#F4F2EE', 'Branco Osso', 'texto sobre escuro'),
}
def c(k): return COR[k][0]

CSS = f"""
@font-face{{font-family:Cinzel;src:url({A}/fontes/Cinzel-500.ttf);font-weight:500}}
@font-face{{font-family:Cinzel;src:url({A}/fontes/Cinzel-700.ttf);font-weight:700}}
@font-face{{font-family:Cinzel;src:url({A}/fontes/Cinzel-900.ttf);font-weight:900}}
@font-face{{font-family:Barlow;src:url({A}/fontes/BarlowCondensed-500.ttf);font-weight:500}}
@font-face{{font-family:Barlow;src:url({A}/fontes/BarlowCondensed-600.ttf);font-weight:600}}
@font-face{{font-family:Barlow;src:url({A}/fontes/BarlowCondensed-800.ttf);font-weight:800}}
@font-face{{font-family:Mont;src:url({A}/fontes/Montserrat-400.ttf);font-weight:400}}
@font-face{{font-family:Mont;src:url({A}/fontes/Montserrat-600.ttf);font-weight:600}}
@font-face{{font-family:Mont;src:url({A}/fontes/Montserrat-800.ttf);font-weight:800}}
:root{{--la:{c('laranja')};--ma:{c('marinho')};--ro:{c('royal')};--ou:{c('ouro')};--pr:{c('preto')};--la2:{c('laranja2')};--ma2:{c('marinho2')};--br:{c('branco')}}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#000;font-family:Mont,sans-serif;color:var(--br)}}
.ci{{font-family:Cinzel,serif;font-weight:700;letter-spacing:.02em;line-height:.95;text-transform:uppercase}}
.bc{{font-family:Barlow,sans-serif;font-weight:800;text-transform:uppercase;line-height:.86;letter-spacing:-.005em}}
.lab{{font-family:Barlow,sans-serif;font-weight:600;text-transform:uppercase;letter-spacing:.28em;font-size:20px}}
.foto{{position:absolute;filter:contrast(1.14) saturate(.92) brightness(.96) drop-shadow(-10px 0 0 rgba(255,122,26,.0)) drop-shadow(-14px -4px 26px rgba(255,122,26,.55)) drop-shadow(0 40px 60px rgba(0,0,0,.7))}}
.grao{{position:absolute;inset:0;pointer-events:none;background:url({A}/grao.png)}}
.vin{{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 40%,transparent 45%,rgba(0,0,0,.55) 100%)}}
.hz{{position:absolute;height:3px;background:var(--ou)}}
.box{{position:absolute}}
"""

def logo(var='branco'):
    return {'branco': f'{A}/logo.png', 'marinho': f'{A}/logo-marinho.png', 'preto': f'{A}/logo-mono-preto.png',
            'mono': f'{A}/logo-mono-branco.png', 'ouro': f'{A}/logo-mono-ouro.png'}[var]

def foto(n): return f'{A}/fotos/{n}.png'
