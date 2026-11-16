"""Deck institucional/investidor (14 telas 16:9), resumo 1 página e kit comercial em HTML -> PDF (render.js).
Fase 2 Al Kántara, 16/11/2026. Sem número inventado: campos [ ] ficam para o Lindson preencher."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from site import DIV, simb  # noqa  (o gerador do site é a fonte única de textos)
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
F = '../site/f/'
CSS = f'''@font-face{{font-family:F;src:url({F}fraunces.ttf)}}@font-face{{font-family:F;font-style:italic;src:url({F}fraunces-it.ttf)}}
@font-face{{font-family:I;src:url({F}inter.ttf);font-weight:500}}@font-face{{font-family:I;src:url({F}inter-sb.ttf);font-weight:600}}
*{{box-sizing:border-box}}body{{margin:0;background:#333}}
.pg{{width:1920px;height:1080px;position:relative;overflow:hidden;background:#0B0C0E;color:#EFEAE1;font:500 26px/1.5 I;padding:110px 130px;page-break-after:always}}
.c{{background:#EFEAE1;color:#0B0C0E}}.mono{{font:600 18px I;letter-spacing:.24em;text-transform:uppercase;color:#8E8A82;margin:0 0 30px}}
h1{{font:400 190px/.9 F;letter-spacing:-.04em;margin:0}}h2{{font:400 110px/.95 F;letter-spacing:-.035em;margin:0 0 40px}}em{{color:#B8955A}}.c em{{color:#8a6a35}}
h3{{font:400 52px/1 F;margin:0 0 14px}}p{{margin:0}}.lead{{font-size:34px;max-width:1100px;opacity:.8}}
.simb{{position:absolute;right:-220px;top:80px;width:1000px}}.rod{{position:absolute;left:130px;right:130px;bottom:56px;display:flex;justify-content:space-between;font:600 15px I;letter-spacing:.2em;color:#8E8A82}}
.g4{{display:grid;grid-template-columns:repeat(4,1fr);gap:28px;margin-top:60px}}.g4>div{{border-top:4px solid var(--c,#B8955A);padding-top:26px}}
.g4 p{{font-size:24px;opacity:.75}}.g2{{display:grid;grid-template-columns:1fr 1fr;gap:80px;margin-top:40px}}
.camp{{display:inline-block;border:1.5px dashed #B8955A;color:#B8955A;padding:4px 14px;border-radius:8px;font-size:22px}}
ul{{margin:0;padding-left:28px}}li{{margin:0 0 12px}}'''
def pg(n, corpo, cls=''):
    return f'<section class="pg {cls}">{corpo}<div class="rod"><span>AL KÁNTARA GROUP · APRESENTAÇÃO 2026</span><span>{n:02d} / 14</span></div></section>'
C4 = ('#2E4BFF', '#E8461E', '#F0A202', '#0E8C66')
dv = list(DIV.values())
T = [
 simb(('#1A1C20', '#1A1C20', '#B8955A', '#1A1C20')) + '<div style="position:absolute;bottom:200px"><p class="mono">GRUPO DE TECNOLOGIA · SÃO LUÍS, MA</p><h1>Estrutura para<br><em>o que vem.</em></h1></div>',
 '<p class="mono">O PROBLEMA</p><h2>A tecnologia ficou barata.<br><em>A execução ficou rara.</em></h2><p class="lead">Empresas do Norte e do Nordeste compram sistema que ninguém usa, marca que não sustenta o preço e audiência que não é delas. Falta quem construa, opere e distribua com responsabilidade.</p>',
 '<p class="mono">A TESE</p><h2>Construir, operar e distribuir<br><em>no mesmo lugar.</em></h2><p class="lead">Software, marca, audiência e negócio próprio sob uma estrutura só. Cada divisão se sustenta sozinha e alimenta as outras.</p>',
 '<p class="mono">ARQUITETURA</p><h2>Quatro pedras, <em>uma chave.</em></h2><div class="g4">' + ''.join(f'<div style="--c:{v["cor"]}"><p class="mono">{v["num"]} · {v["area"]}</p><h3>{v["n"]}</h3><p>{v["verbo"]}</p></div>' for v in dv) + '</div>',
] + [
 simb(tuple(v['cor'] if j == i else '#1A1C20' for j in range(4))) + f'<p class="mono">DIVISÃO {v["num"]} · {v["area"].upper()}</p><h2>Al Kántara<br><em style="color:{v["cor"]}">{v["n"]}</em></h2><p class="lead" style="max-width:900px">{v["lead"]}</p><ul style="margin-top:40px;max-width:900px;font-size:28px">' + ''.join(f'<li><b style="font-weight:600">{a}</b>: {b}</li>' for a, b in v['prod']) + '</ul>'
 for i, v in enumerate(dv)
] + [
 '<p class="mono">O VOLANTE</p><h2>Uma pedra <em>segura a outra.</em></h2><div class="g4">' + ''.join(f'<div style="--c:{c}"><h3>{a}</h3><p>{b}</p></div>' for c, a, b in [(C4[0], 'Labs', 'cria a tecnologia que as outras usam'), (C4[1], 'Studio', 'dá marca a clientes e às empresas do grupo'), (C4[2], 'Media', 'gera audiência própria para vender e lançar'), (C4[3], 'Ventures', 'prova tudo isso em negócio real')]) + '</div>',
 '<p class="mono">PROVA APLICADA</p><h2>Já está <em>no ar.</em></h2><div class="g2"><div><h3>Clientes Studio</h3><p class="lead">Clínica Dra. Jaci Cunha · Tribuna 98 · Rafael Imports · Desentupidora SF</p></div><div><h3>Produtos próprios</h3><p class="lead">Dublê · Central de Comando · Passaporte da Bíblia · Raposa e Leão · Orégano Turbo</p></div></div>',
 '<p class="mono">NÚMEROS</p><h2>Só número real, <em>com fonte.</em></h2><p class="lead">Esta tela é preenchida pelo Lindson antes de cada reunião, com dados conferidos.</p><div class="g4">' + ''.join(f'<div><span class="camp">[ preencher ]</span><p style="margin-top:16px">{t}</p></div>' for t in ['Clientes ativos', 'Receita recorrente mensal', 'Audiência dos canais', 'Produtos em operação']) + '</div>',
 '<p class="mono">POR QUE AGORA, POR QUE DAQUI</p><h2>IA barata, <em>execução local.</em></h2><p class="lead">Custo de construir software caiu. O que falta é quem entenda o negócio da região, atenda com nome e telefone e entregue com prazo por escrito.</p>',
 '<p class="mono">GOVERNANÇA</p><h2>Divisões separadas, <em>contas claras.</em></h2><ul class="lead" style="font-size:32px"><li>Cada divisão com responsável e resultado próprios</li><li>Produtos e empresas investidas com marca própria e endosso do grupo</li><li>Código, dados e contratos documentados</li></ul>',
 '<p class="mono">O PEDIDO</p><h2>O que buscamos <em>agora.</em></h2><p class="lead">Parceiros, conselheiros e investidores que acreditem em estrutura de longo prazo. Valor, uso e prazo: <span class="camp">[ definido pelo Lindson ]</span></p>',
 simb(('#1A1C20', '#1A1C20', '#B8955A', '#1A1C20')) + '<div style="position:absolute;bottom:200px"><p class="mono">CONTATO</p><h1 style="font-size:150px">Vamos medir<br><em>antes de prometer.</em></h1><p class="lead" style="margin-top:40px">Lindson Almeida · WhatsApp (98) 98562-1808 · lindsonalmeida.pages.dev/alkantara</p></div>',
]
assert len(T) == 14
open(os.path.join(B, 'deck', 'deck.html'), 'w').write(f'<!doctype html><meta charset=utf-8><style>{CSS}</style>' + ''.join(pg(i + 1, t, 'c' if i in (2, 9, 12) else '') for i, t in enumerate(T)))

R = '<section class="pg c" style="width:1240px;height:1754px;padding:90px;font-size:22px"><p class="mono">AL KÁNTARA GROUP · RESUMO</p><h2 style="font-size:84px">Estrutura para<br><em>o que vem.</em></h2>' \
 '<p class="lead" style="font-size:26px">Grupo de tecnologia de São Luís (MA) que constrói, opera e distribui no mesmo lugar: software, marca, audiência e negócio próprio.</p>' \
 '<div style="display:grid;grid-template-columns:1fr 1fr;gap:34px;margin-top:50px">' + ''.join(f'<div style="border-top:4px solid {v["cor"]};padding-top:18px"><p class="mono" style="margin:0 0 8px">{v["num"]} · {v["area"]}</p><h3 style="font-size:44px">{v["n"]}</h3><p style="opacity:.75">{v["lead"]}</p><p style="margin-top:8px"><b>{" · ".join(p[0] for p in v["prod"])}</b></p></div>' for v in dv) + '</div>' \
 '<div style="margin-top:50px"><p class="mono">VALORES</p><p>Rigor · Clareza · Peso próprio · Longo prazo</p></div><div style="margin-top:30px"><p class="mono">NÚMEROS</p><p><span class="camp">[ preencher com dados reais ]</span></p></div>' \
 '<div style="position:absolute;bottom:80px;left:90px;right:90px;display:flex;justify-content:space-between"><b>Lindson Almeida · (98) 98562-1808</b><span>lindsonalmeida.pages.dev/alkantara</span></div></section>'
open(os.path.join(B, 'deck', 'resumo.html'), 'w').write(f'<!doctype html><meta charset=utf-8><style>{CSS}</style>' + R)
print('deck ok')
