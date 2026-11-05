# PDF "Roteiro de gravação" dos Reels de novembro e dezembro da Dra. Jaci (conta Leandro, 05/11/2026).
# python3 roteiro-pdf.py <saida.html>  → depois: node ../../../../ferramentas... (render com Playwright, ver README do mês)
import json, sys, importlib.util, io, contextlib, html
spec = importlib.util.spec_from_file_location('t', '../conteudo-nov/textos.py'); m = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
nov = [c for v in vars(m).values() if isinstance(v, list) and v and isinstance(v[0], dict) for c in v if c.get('tipo') == 'reels']
dez = json.load(open('reels.json'))
e = html.escape
def bloco(r, mes):
    linhas = ''.join(f'<tr><td class="t">{e(t)}</td><td>{e(f)}</td><td class="x">{e(x)}</td></tr>' for t, f, x in r['roteiro'])
    cena = f'<p class="cena"><b>Cena:</b> {e(r["cena"])}</p>' if r.get('cena') else ''
    pac = '<p class="tcle">Só grave com paciente real, com TCLE assinado, e com as palavras dela.</p>' if r['linha'] == 'Pacientes' else ''
    return f'<section class="r"><div class="cab"><span class="d">{e(r["data"])}</span><span class="l">{e(r["linha"])}</span><span class="id">{mes} · {r["id"]}</span></div>{cena}{pac}<table><tr><th>Tempo</th><th>O que falar</th><th>Texto na tela</th></tr>{linhas}</table><p class="ok">☐ gravado &nbsp; ☐ editado &nbsp; ☐ postado</p></section>'
corpo = ''.join(bloco(r, 'Nov') for r in nov) + '<div class="quebra"></div>' + ''.join(bloco(r, 'Dez') for r in dez)
open(sys.argv[1], 'w').write(f'''<!doctype html><html lang="pt-BR"><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>@page{{size:A4;margin:14mm 14mm 16mm}}*{{box-sizing:border-box;margin:0}}body{{font:400 10.5px/1.45 'Inter Tight',sans-serif;color:#191614}}
.capa{{height:265mm;background:radial-gradient(90% 80% at 100% 0%,#8E1F2E,#2B070D 65%);color:#F6E9E3;padding:22mm 16mm;display:flex;flex-direction:column;justify-content:space-between;page-break-after:always;border-radius:6px}}
.capa h1{{font:400 64px/.95 'Instrument Serif';}}.capa h1 em{{color:#E8CFA0}}.capa p{{font-size:13px;max-width:120mm;color:#e7cfc8}}.capa small{{color:#E8CFA0;letter-spacing:.12em;text-transform:uppercase;font-size:10px}}
.dicas{{display:grid;gap:7px;margin-top:10mm}}.dicas div{{border-top:1px solid rgba(232,207,160,.4);padding-top:6px;font-size:11.5px}}
.r{{border:1px solid #ead9d3;border-top:3px solid #C9A46A;border-radius:6px;padding:10px 12px;margin-bottom:9px;page-break-inside:avoid;background:#FBF8F5}}
.cab{{display:flex;gap:10px;align-items:baseline;margin-bottom:5px}}.d{{font:italic 400 20px 'Instrument Serif';color:#6B1620}}.l{{font-weight:600;font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:#8E1F2E}}.id{{margin-left:auto;font-size:9px;color:#8A7E74}}
.cena{{font-size:10px;color:#57504A;margin-bottom:5px}}.tcle{{font-size:9.5px;color:#8E1F2E;font-weight:600;margin-bottom:5px}}
table{{width:100%;border-collapse:collapse}}th{{text-align:left;font-size:8.5px;text-transform:uppercase;letter-spacing:.08em;color:#8A7E74;font-weight:500;padding:3px 6px;border-bottom:1px solid #e3d3cc}}td{{padding:5px 6px;border-bottom:1px solid #f0e4df;vertical-align:top}}.t{{white-space:nowrap;color:#8A7E74;width:46px}}.x{{width:150px;font:italic 400 13px/1.2 'Instrument Serif';color:#6B1620}}
.ok{{font-size:9.5px;color:#8A7E74;margin-top:6px}}.quebra{{page-break-after:always}}</style>
<div class="capa"><div><small>Clínica Dra. Jaci Cunha · CRO-MA 8514</small><h1 style="margin-top:14mm">Roteiro de<br><em>gravação</em></h1><p style="margin-top:8mm">Os {len(nov) + len(dez)} Reels de novembro e dezembro. Leve impresso no dia de gravar e marque cada um.</p>
<div class="dicas"><div>1. Os 3 primeiros segundos: rosto da Dra. olhando para a câmera e a frase do gancho.</div><div>2. Celular na vertical, de pé, com luz de frente (janela ou ring light).</div><div>3. Grave cada trecho 2 vezes. Pode errar: a edição junta o melhor.</div><div>4. O texto na tela entra na edição. Não precisa decorar: leia a fala e fale do seu jeito.</div><div>5. Paciente só com TCLE assinado e com as palavras dela. Nada de preço, "grátis", promessa ou antes e depois.</div></div></div>
<small>Novembro: {len(nov)} Reels · Dezembro: {len(dez)} Reels · capa = o próprio vídeo</small></div>{corpo}</html>''')
print(len(nov), len(dez))
