# Feed de dezembro da Dra. Jaci (conta Leandro, 04/11/2026): usa as composições do ../conteudo-nov/gerar.py (cópias dos posts reais dela)
# para os posts e as capas/últimas telas dos carrosséis; as telas do meio copiam as telas B (creme tipográfico com número dourado e fio)
# e C (cor invertida vinho) dos carrosséis de novembro (../instagram-nov/gerar.py), sem foto (regra 04/11: foto real só na 1ª e na última).
# Uso: python3 gerar.py <pasta das fotos> && node render.js
import sys, json, re, importlib.util, os
os.environ['FEED'] = '1'
spec = importlib.util.spec_from_file_location('nov', os.path.join(os.path.dirname(os.path.abspath(__file__)), '../conteudo-nov/gerar.py'))
N = importlib.util.module_from_spec(spec); spec.loader.exec_module(N); N.F = sys.argv[1]
md, VINHO, OURO, CAFE, CREME = N.md, N.VINHO, N.OURO, N.CAFE, N.CREME
def tom(h, t): return h.replace('color:#fff', 'color:#5A4033').replace('color:#F3EADD', 'color:#5A4033') if t == 'claro' else h
def topo(cor): return N.topo_base(0, cor)
def rod(cor): return N.rodape(0, cor, False)
def pontos(i, n, cor): return f'<div class="a dots">{"".join(f"<i style=\'background:{cor};opacity:{1 if k == i else .4}\'></i>" for k in range(n))}</div>'
def conteudo(t, check='#2F5B3A', fv=VINHO):
    if t['tipo'] == 'lista': return ''.join(f'<div class="li"><i style="border-color:{check};color:{check}">✓</i><span>{md(x)}</span></div>' for x in t['itens'])
    if t['tipo'] == 'mito': return (f'<div class="mv"><span class="fv" style="background:{fv}">MITO</span><p>{md(t["mito"])}</p></div>'
                                    f'<div class="mv"><span class="fv" style="background:{OURO}">VERDADE</span><p>{md(t["verdade"])}</p></div>')
    return f'<p class="tx">{md(t["texto"])}</p>'
def meio(t, i, n):
    tit = t.get('titulo', 'Mito ou verdade?'); tit = re.sub(r'^\d+\.\s*', '', tit)
    if i % 2:   # B: creme tipográfico, número grande dourado, título na faixa com fio
        return (f'<div class="a" style="inset:0;background:{CREME}"></div>' + topo(CAFE) +
                f'<div class="a" style="left:0;width:1080px;top:200px;height:960px;display:flex;flex-direction:column;justify-content:center;text-align:center;color:{CAFE}"><div class="S" style="font-size:200px;line-height:1;color:{OURO}">{i:02d}</div>'
                f'<div class="fio"><i></i><span class="S" style="font-size:54px">{tit}</span><i></i></div><div style="width:820px;margin:34px auto 0">{conteudo(t)}</div></div>' + pontos(i, n, CAFE) + rod(CAFE))
    return (f'<div class="a" style="inset:0;background:radial-gradient(900px 800px at 30% 20%,#86283B,{VINHO} 60%,#4A0F1B)"></div>' + topo('#F3EADD') +   # C: vinho
            f'<div class="a" style="left:110px;width:860px;top:250px;height:900px;display:flex;flex-direction:column;justify-content:center;color:#F7EFE6">'
            f'<div class="S" style="font-size:64px;line-height:1.05;border-left:4px solid {OURO};padding-left:26px;margin-bottom:34px">{tit}</div>'
            f'<div class="inv">{conteudo(t, check=OURO, fv="#2A0A10")}</div></div>' + pontos(i, n, '#F3EADD') + rod('#F3EADD'))
EXTRA = """.tx{font-family:Poppins;font-size:46px;line-height:1.35;text-align:center} .tx b{font-weight:700} .inv .tx,.inv .mv{text-align:left}
.li{display:flex;gap:24px;align-items:flex-start;font-family:Poppins;font-size:40px;line-height:1.25;margin-bottom:36px;text-align:left} .li i{flex:none;display:grid;place-items:center;width:46px;height:46px;border:2.5px solid #2F5B3A;border-radius:50%;font-style:normal;font-size:24px;margin-top:-2px} .li b{font-weight:700}
.mv{margin-bottom:38px;text-align:center} .mv .fv{font-size:40px} .mv p{font-family:Poppins;font-size:40px;line-height:1.3;margin-top:14px} .mv b{font-weight:700}
.dots{right:88px;top:1170px;display:flex;gap:8px} .dots i{width:12px;height:12px;border-radius:50%;display:block}"""
secs = []
for p in json.load(open('textos.json')):
    secs.append(f'<section class="f {p["tom"]}" id="{p["id"]}" style="height:1350px">{tom(N.arte(p, 1350), p["tom"])}</section>')
for k, c in json.load(open('carrosseis.json')).items():
    T = c['telas']; n = len(T)
    for i, t in enumerate(T):
        if t['tipo'] == 'capa':
            d = dict(id=k, foto=c['capa_foto'], comp=c['capa_comp'], tom=c['tom'], **{x: t[x] for x in ('topo', 'serif', 'sans')}); h = tom(N.arte(d, 1350), c['tom']); cl = c['tom']
        elif t['tipo'] == 'fim':   # cópia de "Antes de qualquer procedimento, eu observo." (faixa café + pílula), tom claro
            d = dict(id=k, foto=c['fim_foto'], comp='cafe', tom='claro', topo='', serif=t['serif'], sans=t['sans']); h = tom(N.arte(d, 1350), 'claro'); cl = 'claro'
        else: h = meio(t, i, n); cl = ''
        secs.append(f'<section class="f {cl}" id="{k}-{i+1}" style="height:1350px">{h}</section>')
open('artes.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400;1,500;1,600;1,700&family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">
<style>{N.CSS}{EXTRA}</style></head><body>{''.join(secs)}</body></html>""")
print(len(secs), 'artes')
