"""Gera o pitch deck (16:9), o plano de negócios (A4) e o one-pager (A4) em HTML e PDF.
Uso: python3 documentos.py <pasta_saida>
Fotos do Lindson e fontes vêm do repositório privado CentralLindsonALmeida e das pastas do
repositório (nada de foto é copiado para o repositório público). Números: modelo.py."""
import sys, os, subprocess, base64, pathlib
import modelo as M
from textos import *

OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'saida'); OUT.mkdir(parents=True, exist_ok=True)
PRIV = pathlib.Path('/home/user/centrallindsonalmeida')
REPO = pathlib.Path(__file__).resolve().parents[2]
def achar(*cands):
    for c in cands:
        if pathlib.Path(c).exists(): return pathlib.Path(c)
    raise SystemExit('não achei: ' + str(cands))
ANTON = achar(REPO/'conteudo/youtube/raposa-e-leao/produto/fonts/Anton-Regular.ttf', '/tmp/claude-0/-home-user/fabab33e-729e-58f9-992e-e0c09a689812/scratchpad/fonts/Anton-Regular.ttf')
MANROPE = achar(REPO/'agencia/operacao-propria/reels/motor/fontes/manrope.woff2', '/tmp/claude-0/-home-user/fabab33e-729e-58f9-992e-e0c09a689812/scratchpad/fonts/manrope.woff2')
def foto(rel): return (PRIV/rel).as_uri()
# cada foto uma vez só (regra do dono). Deck: capa, solução, time, pedido. Plano: capa e time. One-pager: 1.
F = dict(capa='membros/img/c16.jpg', solucao='membros/img/c10.jpg', time='site/img/lindson-sobre.jpg', pedido='membros/img/c13.jpg',
         plano_capa='site/img/lindson-hero.webp', plano_time='membros/img/c08.jpg', one='produtos/landing/raio-x-do-perfil/img/sobre.jpg')
assert len(set(F.values())) == len(F)

CSS = f"""
@font-face{{font-family:Anton;src:url('{ANTON.as_uri()}')}}
@font-face{{font-family:Manrope;src:url('{MANROPE.as_uri()}');font-weight:200 800}}
:root{{--p:#0A0A0A;--a:#F5C518;--b:#FFFFFF;--c:#A8A8A8;--l:#1C1C1C}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Manrope,sans-serif;color:var(--b);background:var(--p);-webkit-print-color-adjust:exact;print-color-adjust:exact}}
h1,h2,h3,.an{{font-family:Anton,sans-serif;font-weight:400;letter-spacing:.5px;text-transform:uppercase;line-height:1.02}}
.am{{color:var(--a)}} .cz{{color:var(--c)}}
table{{border-collapse:collapse;width:100%}}
th{{background:var(--a);color:var(--p);text-align:left;font-weight:800}}
td,th{{padding:7px 10px;border-bottom:1px solid #2a2a2a;vertical-align:top}}
.tag{{display:inline-block;background:var(--a);color:var(--p);font-weight:800;font-size:13px;letter-spacing:2px;text-transform:uppercase;padding:5px 12px}}
.box{{background:var(--l);border-top:4px solid var(--a);padding:18px 20px}}
.nota{{color:var(--c);font-size:13px}}
"""

def pdf(html_path, pdf_path):
    subprocess.run(['google-chrome', '--headless=new', '--no-sandbox', '--disable-gpu', '--allow-file-access-from-files',
                    '--no-pdf-header-footer', '--virtual-time-budget=8000', f'--print-to-pdf={pdf_path}', html_path.as_uri()],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# ---------- números ----------
R = {n: M.projetar(n) for n in M.CEN}; R60 = {n: M.projetar(n, meses=60) for n in M.CEN}
U = {n: M.unit(n) for n in M.CEN}
def mes(n, m): return R[n]['linhas'][m-1]
def luc24(n): return sum(l['lucro'] for l in R[n]['linhas'])
b = lambda v, d=0: M.brl(v, d).replace(' ', '\u00a0')

def barras(metrica='rec', meses=(6, 12, 18, 24), alt=480):
    mx = max(mes(n, m)[metrica] for n in M.CEN for m in meses)
    cores = {'Conservador': '#5a5a5a', 'Base': '#F5C518', 'Otimista': '#FFFFFF'}
    g = ''
    for m in meses:
        g += '<div style="display:flex;flex-direction:column;align-items:center;flex:1"><div style="display:flex;gap:6px;align-items:flex-end;height:%dpx">' % alt
        for n in M.CEN:
            v = mes(n, m)[metrica]; h = max(4, v/mx*(alt-30))
            g += f'<div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end"><span style="font-size:17px;font-weight:700;margin-bottom:4px">{b(v/1000,0).replace("R$\u00a0","")}k</span><div style="width:56px;height:{h:.0f}px;background:{cores[n]}"></div></div>'
        g += f'</div><div style="margin-top:8px;font-weight:800;font-size:20px">Mês {m}</div></div>'
    leg = ''.join(f'<span style="display:inline-flex;align-items:center;gap:6px;margin-right:18px"><i style="width:14px;height:14px;background:{c};display:inline-block"></i>{n}</span>' for n, c in cores.items())
    return f'<div style="display:flex;gap:14px">{g}</div><div style="margin-top:14px;font-size:20px">{leg}</div>'

def tabela_cen(meses=(6, 12, 18, 24)):
    h = '<table><tr><th>Cenário</th><th>Premissas</th>' + ''.join(f'<th>Mês {m}</th>' for m in meses) + '<th>Lucro 24m</th></tr>'
    for n in M.CEN:
        c = M.CEN[n]
        h += f'<tr><td><b>{n}</b></td><td class="cz">{c["novos_d"]} novos/mês · {b(c["ticket"])} · churn {c["churn"]*100:.0f}%</td>'
        h += ''.join(f'<td>{mes(n,m)["cli"]:.0f} clientes<br><b>{b(mes(n,m)["rec"])}</b><br><span class="cz">lucro {b(mes(n,m)["lucro"])}</span></td>' for m in meses)
        h += f'<td><b>{b(luc24(n))}</b></td></tr>'
    return h + '</table>'

def tabela_uso():
    h = '<table><tr><th>Item</th><th>Detalhe</th><th>Quando</th><th style="text-align:right">Valor</th></tr>'
    for a, d, v, q in M.USO:
        h += f'<tr><td><b>{a}</b></td><td class="cz">{d}</td><td>{q}</td><td style="text-align:right"><b>{b(v)}</b></td></tr>'
    return h + f'<tr><td colspan="3"><b>TOTAL</b></td><td style="text-align:right" class="am"><b>{b(M.P["aporte"])}</b></td></tr></table>'

def tabela_unit():
    rows = [('Ticket médio/mês', 'ticket', b), ('Margem de contribuição/mês', 'margem', b), ('Vida média (meses)', 'vida', lambda v: f'{v:.0f}'),
            ('LTV limitado a 12 meses', 'ltv12', b), ('CAC só de tráfego', 'cac', b), ('CAC cheio (+R$ 500 comercial)', None, None),
            ('Payback do CAC cheio', None, None)]
    h = '<table><tr><th>Métrica (premissa)</th>' + ''.join(f'<th>{n}</th>' for n in M.CEN) + '</tr>'
    for rot, k, f in rows:
        h += f'<tr><td>{rot}</td>'
        for n in M.CEN:
            u = U[n]
            if rot.startswith('CAC cheio'): v = b(u['cac']+500)
            elif rot.startswith('Payback'): v = f'{(u["cac"]+500)/u["margem"]:.1f} mês'.replace('.', ',')
            else: v = f(u[k])
            h += f'<td><b>{v}</b></td>'
        h += '</tr>'
    return h + '</table>'

ctx = dict(b=b, M=M, R=R, R60=R60, U=U, mes=mes, luc24=luc24, barras=barras, tabela_cen=tabela_cen, tabela_uso=tabela_uso, tabela_unit=tabela_unit, foto=foto, F=F)

# ---------- DECK ----------
def deck():
    slides = slides_deck(ctx)
    css = CSS + """
@page{size:1600px 900px;margin:0}
.s{width:1600px;height:900px;position:relative;overflow:hidden;page-break-after:always;padding:70px 90px;background:#0A0A0A}
.s h2{font-size:96px;margin-bottom:34px}
.s .k{position:absolute;top:34px;left:90px;font-size:14px;letter-spacing:4px;color:#F5C518;font-weight:800;text-transform:uppercase}
.s .n{position:absolute;bottom:30px;right:90px;font-size:14px;color:#777}
.s .rod{position:absolute;bottom:30px;left:90px;font-size:14px;color:#888;max-width:860px}
.s p,.s li{font-size:27px;line-height:1.45}
.s td,.s th{font-size:23px;padding:13px 14px}
.s .box{padding:26px 28px}
.s .k{font-size:17px!important}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:40px}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:26px}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}
.big{font-family:Anton;font-size:84px;color:#F5C518;line-height:1}
.fot{position:absolute;top:0;right:0;height:900px;width:620px;object-fit:cover;object-position:center 20%}
.fade{position:absolute;top:0;right:440px;width:180px;height:900px;background:linear-gradient(90deg,#0A0A0A,transparent)}
ul{padding-left:28px} li{margin-bottom:12px}
.tuso td,.tuso th{font-size:20px!important;padding:10px 10px!important}
.tcen td,.tcen th{font-size:20px!important;padding:9px 8px!important}
"""
    corpo = ''
    for i, (kicker, html) in enumerate(slides, 1):
        corpo += f'<section class="s"><div class="k">{kicker}</div>{html}<div class="n">{i:02d} / {len(slides):02d}</div></section>'
    return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Plano Investidor · Pitch</title><style>{css}</style></head><body>{corpo}</body></html>', len(slides)

def plano():
    css = CSS + """
@page{size:A4;margin:0}
.pg{width:210mm;min-height:297mm;padding:20mm 18mm 22mm;background:#0A0A0A;page-break-after:always;position:relative}
.pg h2{font-size:48px;margin:0 0 16px} .pg h3{font-size:25px;color:#F5C518;margin:22px 0 10px}
.pg p,.pg li{font-size:15px;line-height:1.6;margin-bottom:8px} .pg td,.pg th{font-size:13.5px;padding:7px 8px}
.pg ul{padding-left:18px}
.pg .num{position:absolute;bottom:10mm;right:18mm;font-size:10px;color:#777}
.pg .rod{position:absolute;bottom:10mm;left:18mm;font-size:9.5px;color:#777;max-width:150mm}
.pg .box{padding:12px 14px} .pg .box p{margin:0}
.big{font-family:Anton;font-size:46px;color:#F5C518;line-height:1}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:14px} .g3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
"""
    pags = paginas_plano(ctx)
    corpo = ''.join(f'<section class="pg">{h}<div class="rod">Plano investidor · Lindson Almeida · documento privado, sem oferta pública · projeções não são promessa</div><div class="num">{i}/{len(pags)}</div></section>' for i, h in enumerate(pags, 1))
    return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Plano de Negócios</title><style>{css}</style></head><body>{corpo}</body></html>', len(pags)

def one():
    css = CSS + """
@page{size:A4;margin:0}
.pg{width:210mm;height:297mm;padding:14mm 14mm 12mm;background:#0A0A0A;overflow:hidden;position:relative}
p,li,td{font-size:12.8px;line-height:1.45} th{font-size:12.5px} td,th{padding:5px 7px}
h3{font-size:21px;color:#F5C518;margin:14px 0 6px} ul{padding-left:18px}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
"""
    return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>One-pager investidor</title><style>{css}</style></head><body><section class="pg">{onepager(ctx)}</section></body></html>', 1

for nome, fn in (('PITCH-DECK-INVESTIDOR', deck), ('PLANO-DE-NEGOCIOS', plano), ('ONE-PAGER-INVESTIDOR', one)):
    html, n = fn(); hp = OUT/f'{nome}.html'; hp.write_text(html, encoding='utf-8')
    pdf(hp, OUT/f'{nome}.pdf'); print(nome, n, 'páginas')
