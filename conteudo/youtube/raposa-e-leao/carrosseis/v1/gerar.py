# Raposa e Leão · 10 carrosséis v1 (Designer gráfico, conta Zuleide, 18/11/2026). python3 gerar.py && node render.js && python3 prancha.py
# Gera pecas.html (80 telas 1080x1350). Identidade: raposa-e-leao/IDENTIDADE.md. Texto: dados.py <- produto/fonte/conteudo.py.
# Composições copiadas (TEMPLATE.md):
#  capa ........ capas v2 Economist 2027 aprovadas ("ficaram perfeitas"): imagem full-bleed + tag amarela + Anton gigante + selo
#  2 cena ...... The School of Life (UK): frase grande na 2ª pessoa sobre pintura apagada, aspas gigantes
#  3 texto ..... Penguin Great Ideas / David Pearson (UK): a citação como objeto tipográfico em papel
#  4 dossiê .... explicadores Vox (EUA) + modelo dossiê Economist: foto em papel com fita, círculo vermelho, ficha ARQUIVO
#  5 lance I ... Brut (FR): numeral gigante em contorno + imagem em lupa
#  6 II e III .. Nexo (BR): faixa de imagem no topo + checklist numerado
#  7 freio ..... The Economist IG (UK): carimbo + uma única tarja de destaque
#  8 fecho ..... Folio Society (UK): retrato + objeto-livro (mockup do manual) + CTA de salvar
# Fundo Gemini: se existir fundos/cNN-capa.jpg, a capa usa ele (com "imagem gerada por IA"); senão usa a obra do acervo.
import os, re, sys
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D)
import dados as X
C = X.C
IMG = os.path.join(D, '..', '..', 'img'); TMP = os.path.join(D, '_img'); os.makedirs(TMP, exist_ok=True)
FONTS = '../../produto/fonts/'; MOCK = '../../produto/venda/img/'

def g(t):
    t = re.sub(r'\*\*(.+?)\*\*', r'<b class="o">\1</b>', t)
    return re.sub(r'\[\[(.+?)\]\]', r'<span class="tj">\1</span>', t)

def prep(k, modo):
    """modo: cor (contraste), duo (P&B brasa/ouro), ouro (duotone ouro), sangue (fundo do freio), cinza (textura)"""
    arq, cred, pos, *crop = X.OBRAS[k]; out = f'{k}_{modo}.jpg'; dst = os.path.join(TMP, out)
    if not os.path.exists(dst):
        im = Image.open(os.path.join(IMG, arq)).convert('RGB')
        if crop:
            a, b, c, d = crop[0]; im = im.crop((int(a*im.width), int(b*im.height), int(c*im.width), int(d*im.height)))
        s = 1700 / max(im.size)
        if s < 1: im = im.resize((int(im.width*s), int(im.height*s)), Image.LANCZOS)
        if modo == 'cor':
            im = ImageEnhance.Contrast(im).enhance(1.15); im = ImageEnhance.Color(im).enhance(1.15)
        else:
            gr = ImageOps.autocontrast(ImageOps.grayscale(im), cutoff=1)
            if modo == 'duo': im = ImageOps.colorize(gr, black='#070605', mid='#7a4420', white='#F6E6C2', midpoint=110)
            elif modo == 'ouro': im = ImageOps.colorize(gr, black='#0B0A08', mid='#6a4f12', white='#F2D47E', midpoint=120)
            elif modo == 'sangue': im = ImageOps.colorize(gr, black='#050404', white='#9a2420').filter(ImageFilter.GaussianBlur(3))
            elif modo == 'cinza': im = ImageOps.colorize(gr, black='#0B0A08', white='#cdbfa3').filter(ImageFilter.GaussianBlur(5))
        im = im.filter(ImageFilter.UnsharpMask(2, 80, 2)) if modo in ('cor', 'duo', 'ouro') else im
        im.save(dst, quality=88)
    return f'_img/{out}', cred, pos

def aspas(t): return re.sub(r'"([^"]+)"', r'“\1”', t)

def topo(c, n): return f'<div class="tp"><span>{c["linha"]}</span><span>{n:02d}/08</span></div>'
SELO = '<div class="selo"><i>R</i> RAPOSA E LEÃO</div>'
def prox(t): return f'<div class="cont">{t} <em>→</em></div>'
def cr(t): return f'<div class="cr">Obra: {t} · domínio público</div>' if 'domínio público' not in t and 'SMK' not in t else f'<div class="cr">Obra: {t}</div>'
def modo_selo(m):
    cls = 'rap' if m == 'RAPOSA' else ('leo' if m == 'LEÃO' else 'amb')
    return f'<div class="modo {cls}"><small>MODO</small><span>{m.replace(" E ", "<br>E ")}</span></div>'

def capa(c):
    f = os.path.join(D, 'fundos', c['id'] + '-capa.jpg')
    if os.path.exists(f):
        src, pos, cred, ia = f'fundos/{c["id"]}-capa.jpg', '50% 40%', '', '<div class="ia">imagem gerada por IA</div>'
        klass = 'gem'
    else:
        src, cred, pos = prep(c['img']['capa'], 'duo'); ia = f'<div class="ia">{cred}</div>'; klass = 'ace'
    return (f'<section class="f capa {klass}" id="{c["id"]}-01"><img class="bg" src="{src}" style="object-position:{pos}"><div class="glow"></div>'
            f'<div class="grad"></div><div class="gr"></div><div class="vg"></div>'
            f'<div class="et"><span class="fonte">{c["et"]}</span><span>ARRASTE →</span></div>{modo_selo(c["modo"])}'
            f'{"<div class=stamp>NÃO EXISTE</div>" if c["id"] == "c02" else ""}'
            f'<div class="tx"><div class="hk">{c["hk"]}</div><h1>{c["h1"]}</h1></div>{SELO}{ia}</section>')

def cena(c, n, big, rest, nx, lab='A CENA'):
    src, _, pos = prep(c['img']['dossie'], 'cinza')
    return (f'<section class="f cena" id="{c["id"]}-{n:02d}"><img class="bgx" src="{src}" style="object-position:{pos}"><div class="gr"></div><div class="vg"></div>'
            f'{topo(c, n)}<div class="aspas">“</div><div class="cbox"><div class="lab">{lab}</div><h2 class="big">{g(big)}</h2><p class="rest">{g(rest)}</p></div>{prox(nx)}{SELO}</section>')

def texto(c, n, it, pt, ref, nx, lab='O TEXTO ORIGINAL', nota='Palavra por palavra. Conferido no original italiano.'):
    num = re.search(r'cap\. ([IVXL]+|\d+)', ref); num = num.group(1) if num else ''
    return (f'<section class="f texto" id="{c["id"]}-{n:02d}"><div class="couro"></div><div class="rom">{num}</div><div class="gr"></div><div class="vg"></div>{topo(c, n)}'
            f'<div class="perg{' curto' if len(pt) < 80 else ''}"><div class="lab2">{lab}</div><p class="it">“{it}”</p><div class="fio"></div><p class="pt">“{pt}”</p><div class="ref">— {ref}</div></div>'
            f'<p class="nota">{nota}</p>{prox(nx)}{SELO}</section>')

def dossie(c, n, ref, nx, h='NO LIVRO'):
    src, cred, pos = prep(c['img']['dossie'], 'cor')
    return (f'<section class="f dossie" id="{c["id"]}-{n:02d}"><div class="mesa"></div><div class="gr"></div><div class="vg"></div>{topo(c, n)}'
            f'<div class="pv"><img src="{src}" style="object-position:{pos}"><div class="ci" style="{c["ci"]}"></div><div class="cap">ILUSTRAÇÃO · {cred.split(",")[0].upper()}</div></div>'
            f'<div class="arq"><div class="an">ARQUIVO Nº {c["id"][1:]}</div><div class="ar"><small>FONTE</small>{ref}</div><div class="ar"><small>NO CASO</small>{c["quem"]}</div></div>'
            f'<h2 class="dh">{h}</h2><p class="caso{' curto' if len(c['caso']) < 200 else ''}">{g(c["caso"])}</p>{cr(cred)}{prox(nx)}{SELO}</section>')

def lance1(c, n, num, lab, t, nx):
    src, cred, pos = prep(c['img']['lupa'], 'cor')
    return (f'<section class="f lance" id="{c["id"]}-{n:02d}"><div class="brasa"></div><div class="gr"></div><div class="vg"></div>{topo(c, n)}<div class="giga{' long' if len(num) > 2 else ''}">{num}</div>'
            f'<div class="lupa"><img src="{src}" style="object-position:{pos}"></div><div class="cabo"></div>'
            f'<div class="lbox"><div class="lab3">{lab}</div><h2 class="lt{' curto' if len(t) < 60 else ''}">{g(aspas(t))}</h2></div>{cr(cred)}{prox(nx)}{SELO}</section>')

def check(c, n, head, itens, nx):
    src, cred, pos = prep(c['img']['faixa'], 'ouro')
    lis = ''.join(f'<li><span class="nb">{a}</span><p>{g(aspas(b))}</p></li>' for a, b in itens)
    return (f'<section class="f check" id="{c["id"]}-{n:02d}"><img class="faixa" src="{src}" style="object-position:{pos}"><div class="ff"></div><div class="gr"></div><div class="vg"></div>{topo(c, n)}'
            f'<div class="cwrap"><h2 class="ch">{g(head)}</h2><ul class="cl n{len(itens)}">{lis}</ul></div>{cr(cred)}{prox(nx)}{SELO}</section>')

def freio(c, n, txt, nx='SALVA'):
    src, _, pos = prep(c['img']['faixa'], 'sangue')
    return (f'<section class="f freio" id="{c["id"]}-{n:02d}"><img class="bgx" src="{src}" style="object-position:{pos}"><div class="gr"></div><div class="vg"></div>{topo(c, n)}'
            f'<div class="carimbo">O FREIO</div><div class="lab4">ONDE A IDEIA VIRA ABUSO</div><p class="ft">{g(txt)}</p>{prox(nx)}{SELO}</section>')

def fecho(c, n, h, sub, mock, btn):
    f = os.path.join(D, 'fundos', c['id'] + '-capa.jpg')
    src, cred, pos = prep(c['img']['capa'], 'duo')
    return (f'<section class="f fecho" id="{c["id"]}-{n:02d}"><img class="ret" src="{src}" style="object-position:{pos}"><div class="rf"></div><div class="glow2"></div><div class="gr"></div><div class="vg"></div>{topo(c, n)}'
            f'<img class="mock {"isca" if "isca" in mock else ""}" src="{MOCK}{mock}"><div class="fbox"><h2 class="fh">{h}</h2><p class="fs">{g(sub)}</p></div><div class="btn">{btn}</div>{SELO}</section>')

FECHO_MANUAL = ('MAIS 29 SITUAÇÕES<br>COMO ESTA NO<br><b class="o">MANUAL DE CAMPO</b>', 'Cada uma com a cena, o texto original, o caso, o lance e o freio.')

def carrossel(c):
    o = [capa(c)]
    if c['id'] == 'c02':
        F = C.FALSAS[0]; S25 = X.S(25)
        o.append(cena(c, 2, '“Os fins justificam os **meios**.”', 'Circula em camiseta, palestra e post como se fosse de Maquiavel. Procure em O Príncipe, nos Discursos e nas cartas.', 'O QUE ELE ESCREVEU', 'A FRASE'))
        o.append(texto(c, 3, F['it'], F['pt'], F['ref'], 'DE ONDE VEIO', 'O QUE ELE ESCREVEU DE VERDADE'))
        o.append(dossie(c, 4, 'Nenhuma obra nem carta dele', 'O CERTO', 'DE ONDE VEIO'))
        o.append(lance1(c, 5, 'XVIII', 'O QUE O CAP. XVIII DIZ', 'Ele descreve **como as pessoas julgam**: pelo resultado e pela aparência.', 'E O CAP. VIII'))
        o.append(check(c, 6, 'E no capítulo VIII ele <b class="o">fecha a porta</b>', [('VIII', f'“{S25["pt"]}.” <i>({S25["it"]})</i>'), ('✕', 'Nenhuma licença: o crime pode dar poder, **mas não glória**.')], 'O FREIO'))
        o.append(freio(c, 7, c['freio']))
        o.append(fecho(c, 8, 'COMENTA<br><b class="o">FONTE</b>', 'e receba grátis as **7 frases que Maquiavel nunca disse**, com o texto certo de cada uma.', 'isca.jpg', 'COMENTA “FONTE” AQUI EMBAIXO'))
        return o
    s = X.S(c['s'])
    o.append(cena(c, 2, c['big'], c['rest'], 'O TEXTO'))
    o.append(texto(c, 3, s['it'], s['pt'], s['ref'], 'NO LIVRO'))
    o.append(dossie(c, 4, s['ref'], 'O LANCE'))
    if c['id'] == 'c04':
        P = C.PERGUNTAS[0]
        o.append(lance1(c, 5, '?', 'A PERGUNTA Nº 1 · ' + P[2].upper().replace('PRÍNCIPE', 'O PRÍNCIPE, CAP.'), 'O que está acontecendo **de fato**? Separe fato de esperança.', 'COMO USAR'))
        o.append(check(c, 6, 'Como usar a <b class="o">pergunta</b>', [('I', s['lance'][0]), ('II', s['lance'][1]), ('III', s['lance'][2])], 'O FREIO'))
        o.append(freio(c, 7, c['freio']))
        o.append(fecho(c, 8, 'A PERGUNTA 1 DE 13.<br>AS OUTRAS ESTÃO NO<br><b class="o">MANUAL DE CAMPO</b>', 'Com as 30 situações: cena, texto original, caso, lance e freio.', 'mockup.jpg', 'SALVA PARA A PRÓXIMA DECISÃO'))
        return o
    L = s['lance']
    o.append(lance1(c, 5, 'I', 'LANCE I · O PRIMEIRO PASSO', c.get('l1', L[0]), 'II E III'))
    o.append(check(c, 6, 'Os próximos <b class="o">lances</b>', [('II', L[1]), ('III', L[2])], 'O FREIO'))
    o.append(freio(c, 7, c['freio']))
    o.append(fecho(c, 8, *FECHO_MANUAL, 'mockup.jpg', 'SALVA PARA A PRÓXIMA VEZ'))
    return o

FF = ''.join(f"@font-face{{font-family:'{n}';src:url('{FONTS}{f}');font-weight:100 900;font-style:{st}}}" for n, f, st in
             [('Anton', 'Anton-Regular.ttf', 'normal'), ('Cinzel', 'Cinzel.ttf', 'normal'), ('Cormorant Garamond', 'CormorantGaramond-Italic.ttf', 'italic'),
              ('Cormorant Garamond', 'CormorantGaramond.ttf', 'normal'), ('Inter', 'Inter.ttf', 'normal')])
CSS = FF + open(os.path.join(D, 'estilo.css'), encoding='utf-8').read()
if __name__ == '__main__':
    so = sys.argv[1:]
    out = ['<!doctype html><html><head><meta charset="utf-8"><style>' + CSS + '</style></head><body>']
    for c in X.CAR:
        if so and c['id'] not in so: continue
        out += carrossel(c)
    open(os.path.join(D, 'pecas.html'), 'w', encoding='utf-8').write('\n'.join(out) + '</body></html>')
    print('ok', len(out) - 1, 'telas')
