# Manual v2.1 · páginas (revisão conta Leandro 16/11/2026: Barzakh, corpo maior, mockups em foto real,
# grid e Alvenaria corrigidos, uma cor/gravação, redes, motion com quadros reais)
# Manual de Identidade v2 · páginas (executado dentro de gerar.py)
S = 'Al Kántara'
def card_frente(w=850, h=500):
    return chapa(w, h, INK, f'<div style="position:absolute;left:{w*.08}px;top:{h*.12}px">{K(h*.022, BRASS)}</div><div style="position:absolute;right:{w*.07}px;bottom:{h*.11}px">{logo("wordmark","negativo",h*.075)}</div>')
def card_verso(w=850, h=500, rz=0):
    return chapa(w, h, LIME, f'''<div style="position:absolute;left:{w*.08}px;top:{h*.14}px;color:{INK}"><div style="font:400 {h*.09}px F">Lindson Almeida</div><div style="font:500 {h*.035}px 'JetBrains Mono';letter-spacing:.14em;margin-top:{h*.03}px;opacity:.6">FUNDADOR · AL KÁNTARA GROUP</div></div>
<div style="position:absolute;left:{w*.08}px;bottom:{h*.12}px;font:500 {h*.036}px/1.6 I;color:{INK};opacity:.75">alkantara.group<br>São Luís · Maranhão</div><div style="position:absolute;right:-{h*.18}px;bottom:-{h*.2}px">{K(h*.03,"#e2dccf")}</div>''', rz=rz)

# 01 capa
P(f'''<div class="col" style="left:0;top:0;width:1920px;height:1080px;background:{LIME}"></div>{corte(58,780,-250,INK)}
<div class="col" style="left:120px;top:150px">{logo('horizontal','positivo',60)}</div>
<div class="col" style="left:120px;bottom:150px;color:{INK}"><div class="ey" style="color:{INK};opacity:.6">Manual de identidade · v2.1</div><div class="h1" style="font-size:210px;margin-top:22px">Símbolo,<br>sistema,<br><span class="it">aplicação.</span></div></div>''', sec='none')

# 02 conceito: o arco e a pedra-chave
arco = ''.join(f'<g transform="translate(560,1000) rotate({j*16}) translate(-96,-720)"><path fill="none" stroke="{LIME}" stroke-opacity="{0 if j==0 else .4}" stroke-width="1.5" d="{path(KEY,8)}"/></g>' for j in range(-5,6))
arco += f'<g transform="translate(464,280) scale(8)">' + ''.join(f'<path fill="{INK}" d="{path(p,1)}" opacity="0"/>' for p in pecas()) + '</g>'
P(f'''<svg class="col" style="left:0;top:40px" width="1120" height="1000">{arco}<g transform="translate(464,280) scale(8)">''' + ''.join(f'<path fill="{BRASS}" d="{path(p,1)}"/>' for p in pecas()) + f'''</g></svg>
<div class="col" style="left:1180px;top:170px;width:620px"><div class="ey">Conceito</div><div class="h2" style="margin-top:22px">A pedra que segura o arco.</div>
<div class="p" style="margin-top:30px">Al-qantara, em árabe, é a ponte, o arco. No topo de todo arco existe a aduela-chave: a última pedra a entrar, a que trava todas as outras. É o papel do grupo.</div>
<div class="p" style="margin-top:20px">Dentro da chave, as juntas entre quatro pedras desenham um K. Quatro pedras são as quatro divisões. Sem ponte literal, sem arco-íris, sem globo.</div></div>''', sec='01 · Símbolo')

# 03 grid de construção
s = 26; ox, oy = 180, 230
grid = ''.join(f'<line x1="{ox+i*s}" y1="{oy}" x2="{ox+i*s}" y2="{oy+24*s}"/><line x1="{ox}" y1="{oy+i*s}" x2="{ox+24*s}" y2="{oy+i*s}"/>' for i in range(25))
P(f'''<svg class="col" style="left:0;top:0" width="1920" height="1080"><g stroke="{INK}" stroke-opacity=".12">{grid}</g>
<polygon points="{ox},{oy} {ox+24*s},{oy} {ox+19*s},{oy+24*s} {ox+5*s},{oy+24*s}" fill="none" stroke="#E8461E" stroke-width="1.5" stroke-dasharray="6 5"/>
''' + ''.join(f'<path fill="{INK}" fill-opacity=".92" d="{path(p,s,ox,oy)}"/>' for p in pecas()) + f'''
<g stroke="#E8461E" stroke-width="1.5"><line x1="{ox+9*s}" y1="{oy-40}" x2="{ox+9*s}" y2="{oy+24*s+40}"/><line x1="{ox+9*s}" y1="{oy+12*s}" x2="{ox+21.6*s}" y2="{oy-1.6*s}"/><line x1="{ox+9*s}" y1="{oy+12*s}" x2="{ox+20.4*s}" y2="{oy+25.6*s}"/></g>
<circle cx="{ox+9*s}" cy="{oy+12*s}" r="9" fill="none" stroke="#E8461E" stroke-width="2"/>
<g font-family="JetBrains Mono" font-size="14" fill="{INK}" fill-opacity=".7"><text x="{ox}" y="{oy-20}">24 u</text><text x="{ox+5*s}" y="{oy+24*s+34}">14 u (base)</text><text x="{ox+9*s+16}" y="{oy+12*s+5}">nó · 12 u</text><text x="{ox+24*s+20}" y="{oy+10}">inclinação 1:4,8</text></g></svg>
<div class="col" style="left:1060px;top:200px;width:740px"><div class="ey" style="color:{INK};opacity:.6">Grid de construção</div><div class="h2" style="margin-top:20px">24 módulos, 3 juntas.</div>
<div style="margin-top:36px;display:grid;grid-template-columns:1fr 1fr;gap:24px 40px">''' +
  ''.join(f'<div style="border-top:1px solid rgba(11,12,14,.2);padding-top:12px"><div class="mono" style="opacity:.55;font-size:14px">{a}</div><div class="big" style="margin-top:6px">{b}</div></div>' for a, b in [('Quadro', '24 × 24 u'), ('Topo / base', '24 u / 14 u'), ('Junta', '1,6 u em toda a marca'), ('Nó do K', 'x 9 u · y 12 u'), ('Braço superior', 'sai do nó a 47°'), ('Perna inferior', 'sai do nó a 50°')]) + '</div></div>', 'l', '01 · Símbolo')

# 04 explodido: 4 pedras = 4 divisões
pcs = pecas(); offs = [(-40, 0), (30, -40), (60, 0), (30, 40)]
P(f'''<svg class="col" style="left:300px;top:190px" width="760" height="760"><g transform="translate(90,90) scale(24)">''' +
  ''.join(f'<g transform="translate({offs[i][0]/24},{offs[i][1]/24})"><path fill="{DIV[i][1]}" d="{path(p,1)}"/></g>' for i, p in enumerate(pcs)) + '''</g></svg>
<div class="col" style="left:1180px;top:200px;width:620px"><div class="ey">Quatro pedras</div><div class="h2" style="margin-top:20px">Cada divisão é uma pedra.</div>
<div style="margin-top:40px">''' + ''.join(f'<div style="display:flex;gap:20px;align-items:center;padding:16px 0;border-top:1px solid rgba(239,234,225,.15)"><div style="width:22px;height:22px;background:{c}"></div><div class="big" style="width:160px">{n}</div><div class="ps">{["Haste: a base técnica", "Topo: a forma · Barzakh", "Meio: o alcance", "Base: a prova"][i]}</div></div>' for i, (n, c, t, pr) in enumerate(DIV)) + '</div></div>', sec='01 · Símbolo')

# 05 wordmark e kerning
P(f'''<div class="col" style="left:120px;top:150px"><div class="ey">Wordmark</div><div class="h2" style="margin-top:20px">Inter Tight SemiBold, ajustada à mão.</div></div>
<div class="col" style="left:120px;top:400px;width:1680px;padding:60px;background:#15171a;border-radius:4px"><div class="mono" style="opacity:.5">Antes · espaçamento da fonte</div>
<div style="font:600 120px I;letter-spacing:.04em;margin-top:16px;opacity:.45">AL KÁNTARA</div>
<div class="mono" style="opacity:.5;margin-top:40px">Depois · kerning óptico (T·A −62 · K·Á −38 · R·A −30 · L·espaço −40)</div>
<div style="margin-top:22px">{logo('wordmark','negativo',150)}</div></div>''', sec='02 · Logotipo')

# 06 versões
vs = [('horizontal', 'Horizontal · principal', 80), ('vertical', 'Vertical · formatos altos', 220), ('simbolo', 'Símbolo · avatar e carimbo', 200), ('wordmark', 'Só nome · espaços estreitos', 70)]
P(f'''<div class="col" style="left:120px;top:140px"><div class="ey" style="color:{INK};opacity:.6">Versões</div></div>
<div class="col" style="left:120px;top:200px;width:1680px;height:780px;display:grid;grid-template-columns:1.3fr 1fr;grid-template-rows:1fr 1fr;gap:20px">''' +
  ''.join(f'<div style="background:{["#fff",INK,BRASS,"#fff"][i]};border-radius:4px;display:flex;align-items:center;justify-content:center;position:relative">{logo(k,["positivo","negativo","positivo","positivo"][i],h)}<div class="mono" style="position:absolute;left:24px;bottom:20px;font-size:14px;color:{[INK,LIME,INK,INK][i]};opacity:.6">{t}</div></div>' for i, (k, t, h) in enumerate(vs)) + '</div>', 'l', '02 · Logotipo')

# 06b endosso Barzakh (v2.1)
P(f'''<div class="col" style="left:0;top:0;width:900px;height:1080px;background:#2a2a2b url(../../../marca-lindson/projeto-designer/v3/marca/aprovado/placa-arco-monolito-ouro.png) center/cover"></div>
<div class="col" style="left:1000px;top:150px;width:800px"><div class="ey">Exceção escrita · divisão com nome próprio</div><div class="h2" style="margin-top:20px">Barzakh · um estúdio Al Kántara.</div>
<div class="p" style="margin-top:28px">O estúdio de marca e design é a única divisão com nome próprio. O endosso "um estúdio Al Kántara" vem sempre junto, embaixo ou na mesma linha.</div>
<div style="margin-top:36px;padding:34px;background:#15171a;display:inline-block">{divlogo('Barzakh','negativo',70)}</div>
<div style="margin-top:34px;display:grid;grid-template-columns:1fr 1fr;gap:20px 30px">''' + ''.join(f'<div style="border-top:1px solid rgba(239,234,225,.2);padding-top:12px"><div class="mono" style="color:{BRASS};font-size:14px">{a}</div><div class="ps" style="margin-top:6px">{b}</div></div>' for a,b in [('Na arquitetura do grupo','Laranja #E8461E e a pedra do topo'),('Na própria marca','Escuro, ouro metálico, arco, concreto'),('Símbolo','"Dois mares" / monolito, em ouro'),('Nunca','"Barzakh" sozinha na 1ª menção')]) + '</div></div>', sec='02 · Logotipo')

# 07 área de proteção
P(f'''<div class="col" style="left:120px;top:150px;width:560px"><div class="ey">Área de proteção e tamanho mínimo</div><div class="h2" style="margin-top:20px">Uma pedra de respiro.</div>
<div class="p" style="margin-top:28px">A área livre em volta é a largura da haste (8 u). Nada entra nela. Mínimo: símbolo 16 px / 5 mm; horizontal 96 px / 28 mm.</div>
<div style="margin-top:40px;display:flex;gap:40px;align-items:flex-end">{K(0.67,LIME)}<span class="mono" style="opacity:.6">16 px</span>{logo('horizontal','negativo',26)}<span class="mono" style="opacity:.6">96 px</span></div></div>
<div class="col" style="left:860px;top:230px;width:940px;height:620px;border:1px dashed rgba(184,149,90,.8);display:flex;align-items:center;justify-content:center">
<div style="padding:0;outline:1px solid rgba(239,234,225,.15)">{logo('horizontal','negativo',150)}</div>
<div style="position:absolute;left:0;top:0;width:190px;height:620px;background:repeating-linear-gradient(45deg,rgba(184,149,90,.12) 0 2px,transparent 2px 12px)"></div>
<div style="position:absolute;right:0;top:0;width:190px;height:620px;background:repeating-linear-gradient(45deg,rgba(184,149,90,.12) 0 2px,transparent 2px 12px)"></div>
<div class="mono" style="position:absolute;left:60px;top:290px;color:{BRASS}">8 u</div><div class="mono" style="position:absolute;right:60px;top:290px;color:{BRASS}">8 u</div></div>''', sec='02 · Logotipo')

# 08 cor da marca
P(f'''<div class="col" style="left:120px;top:140px"><div class="ey" style="color:{INK};opacity:.6">Aplicação em cor</div></div>
<div class="col" style="left:120px;top:200px;width:1680px;height:780px;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:20px">''' +
  ''.join(f'<div style="background:{bg};border-radius:4px;display:flex;align-items:center;justify-content:center;position:relative">{logo("vertical",v,190)}<div class="mono" style="position:absolute;left:20px;bottom:18px;font-size:14px;color:{tc};opacity:.6">{t}</div></div>' for bg, v, t, tc in
          [(INK, 'negativo', 'Negativo · preferencial', LIME), ('#fff', 'positivo', 'Positivo', INK), (BRASS, 'positivo', 'Sobre latão', INK), (GRAPH, 'latao', 'Latão sobre grafite · premium', LIME), ('#fff', 'mono-preto', 'Monocromático · carimbo', INK), ('#2E4BFF', 'mono-branco', 'Sobre cor de divisão', LIME)]) + '</div>', 'l', '02 · Logotipo')

# 08b uma cor · gravação e carimbo (v2.1)
P(f'''<div class="col" style="left:0;top:0;width:1100px;height:1080px;background:url(../fotos-v2.1/mock-gravacao.jpg) 40% center/cover"></div>
<div class="col" style="left:1180px;top:150px;width:620px"><div class="ey">Logo em uma cor</div><div class="h2" style="margin-top:20px">Gravação e carimbo.</div>
<div class="p" style="margin-top:26px">Uma cor só, chapada, sem degradê nem sombra. Serve para laser, hot stamping, carimbo, bordado e serigrafia.</div>
<div style="margin-top:34px;display:flex;gap:16px">''' + ''.join(f'<div style="width:190px;height:150px;background:{bg};display:flex;align-items:center;justify-content:center;border:1px solid rgba(239,234,225,.15)"><img src="../logos/svg/alkantara-simbolo-{v}.svg" style="height:90px"></div>' for bg,v in [('#fff','mono-preto'),(INK,'mono-branco'),(GRAPH,'latao')]) + '''</div>
<div class="ps" style="margin-top:26px">Mínimo para gravação: símbolo de 8 mm. A junta nunca abaixo de 0,3 mm; abaixo disso, só o símbolo.</div></div>
<div class="col" style="left:40px;bottom:40px;font:500 14px 'JetBrains Mono';color:#EFEAE1;opacity:.8;letter-spacing:.12em">CAPA FOSCA COM GRAVAÇÃO EM LATÃO · FOTO BASE CC0</div>''', sec='02 · Logotipo')

# 09 mau uso
mal = [('transform:scaleX(1.4)', 'Não distorcer'), ('transform:rotate(-12deg)', 'Não girar'), ('filter:drop-shadow(8px 8px 0 #E8461E)', 'Não aplicar sombra'), ('filter:hue-rotate(140deg) saturate(4)', 'Não trocar a cor'), ('opacity:.25', 'Não usar com pouco contraste'), ('outline:3px solid #F0A202;outline-offset:14px;border-radius:40px', 'Não emoldurar')]
P(f'''<div class="col" style="left:120px;top:140px"><div class="ey">Usos proibidos</div></div>
<div class="col" style="left:120px;top:200px;width:1680px;height:780px;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:20px">''' +
  ''.join(f'<div style="background:#15171a;border-radius:4px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden"><img src="../logos/svg/alkantara-horizontal-latao.svg" style="height:70px;{st}"><svg style="position:absolute;inset:0" width="100%" height="100%"><line x1="0" y1="100%" x2="100%" y2="0" stroke="#E8461E" stroke-width="2"/></svg><div class="mono" style="position:absolute;left:20px;bottom:18px;font-size:14px;color:#ff7a57">✕ {t}</div></div>' for st, t in mal) + '</div>', sec='02 · Logotipo')

# 10 paleta
pal = [('Tinta', INK, '11 12 14', '60%'), ('Calcário', LIME, '239 234 225', '25%'), ('Pedra', STONE, '142 138 130', '8%'), ('Grafite', GRAPH, '26 28 32', '5%'), ('Latão', BRASS, '184 149 90', '2%')]
P(f'''<div class="col" style="left:120px;top:140px"><div class="ey">Paleta do grupo · proporção</div></div>
<div class="col" style="left:120px;top:200px;width:1680px;height:640px;display:flex;gap:0">''' +
  ''.join(f'<div style="flex:{fl};background:{h};position:relative;border:1px solid rgba(239,234,225,.08)"><div style="position:absolute;left:22px;bottom:22px;color:{INK if n in ("Calcário","Latão","Pedra") else LIME}"><div class="h3" style="font-size:{40 if fl>10 else 24}px">{n}</div><div class="mono" style="font-size:14px;margin-top:10px;opacity:.7">{h}<br>RGB {r}<br>{p}</div></div></div>' for (n, h, r, p), fl in zip(pal, [60, 25, 8, 6, 5])) + f'''</div>
<div class="col" style="left:120px;top:880px;width:1100px" class=""><div class="p">60 Tinta · 25 Calcário · 15 apoio. O latão é joia: só no símbolo, em filetes e em números grandes. Nunca em fundo inteiro de texto.</div></div>''', sec='03 · Cor')

# 11 cores de divisão
P(f'''<div class="col" style="left:120px;top:140px"><div class="ey" style="color:{INK};opacity:.6">Cores de divisão</div></div>
<div class="col" style="left:120px;top:200px;width:1680px;height:780px;display:grid;grid-template-columns:repeat(4,1fr);gap:20px">''' +
  ''.join(f'''<div style="background:{c};border-radius:4px;position:relative;overflow:hidden;color:{INK if n == "Media" else LIME}"><div style="position:absolute;right:-120px;top:-60px">{K(22,"rgba(0,0,0,.14)",i,"rgba(255,255,255,.22)")}</div>
<div style="position:absolute;left:28px;bottom:28px"><div class="h2" style="font-size:72px">{n}</div><div class="mono" style="font-size:14px;margin-top:14px;opacity:.8">{c}<br>{t}</div></div></div>''' for i, (n, c, t, pr) in enumerate(DIV)) +
  '</div>', 'l', '03 · Cor')

# 12 tipografia
fs = [('F', 400, 'Fraunces', 'Títulos, manifesto, números', 'Aa'), ('I', 600, 'Inter Tight', 'Logotipo, textos, interfaces', 'Aa'), ("'JetBrains Mono'", 500, 'JetBrains Mono', 'Rótulos, dados, legendas', 'Aa')]
P(f'''<div class="col" style="left:120px;top:140px"><div class="ey">Tipografia · Google Fonts, licença OFL</div></div>
<div class="col" style="left:120px;top:200px;width:1680px;height:780px;display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:20px">''' +
  ''.join(f'''<div style="background:{["#15171a",LIME,"#15171a"][i]};color:{[LIME,INK,LIME][i]};border-radius:4px;padding:40px;display:flex;flex-direction:column;justify-content:space-between">
<div style="font:{w} {[400,260,200][i]}px/.85 {ff};letter-spacing:-.02em;{"color:"+BRASS if i==0 else ""}">{a}</div><div><div style="font:{w} 44px {ff}">{n}</div><div class="ps" style="margin-top:10px">{u}</div>
<div style="font:{w} 22px/1.4 {ff};margin-top:18px;opacity:.6">ABCDEFGHIJKLM<br>abcdefghijklm 0123456789</div></div></div>''' for i, (ff, w, n, u, a) in enumerate(fs)) + '</div>', sec='04 · Tipografia')

# 13 hierarquia
P(f'''<div class="col" style="left:120px;top:140px"><div class="ey" style="color:{INK};opacity:.6">Hierarquia</div></div>
<div class="col" style="left:120px;top:210px;width:1680px">
<div style="display:grid;grid-template-columns:260px 1fr;align-items:baseline;border-top:1px solid rgba(11,12,14,.15);padding:20px 0"><div class="mono" style="opacity:.55">Display · Fraunces 160/0,92 · −3,5%</div><div style="font:400 150px/.92 F;letter-spacing:-.035em">Construímos.</div></div>
<div style="display:grid;grid-template-columns:260px 1fr;align-items:baseline;border-top:1px solid rgba(11,12,14,.15);padding:20px 0"><div class="mono" style="opacity:.55">Título · Fraunces 64 · itálico para ênfase</div><div style="font:400 64px/1 F;letter-spacing:-.02em">Estrutura para o que <i>vem.</i></div></div>
<div style="display:grid;grid-template-columns:260px 1fr;align-items:baseline;border-top:1px solid rgba(11,12,14,.15);padding:20px 0"><div class="mono" style="opacity:.55">Destaque · Inter Tight 600 · 24</div><div style="font:600 26px I">Labs, Studio, Media e Ventures sob um só grupo.</div></div>
<div style="display:grid;grid-template-columns:260px 1fr;align-items:baseline;border-top:1px solid rgba(11,12,14,.15);padding:20px 0"><div class="mono" style="opacity:.55">Texto · Inter Tight 500 · 18/1,5</div><div style="font:500 19px/1.5 I;max-width:820px;opacity:.8">Texto corrido em frases curtas. Uma ideia por parágrafo. Números sempre com fonte.</div></div>
<div style="display:grid;grid-template-columns:260px 1fr;align-items:baseline;border-top:1px solid rgba(11,12,14,.15);padding:20px 0"><div class="mono" style="opacity:.55">Rótulo · Mono 13 · +14% · caixa alta</div><div class="mono" style="color:#9a7741">Divisão 01 · Labs · 2026</div></div></div>''', 'l', '04 · Tipografia')

# 14 grid editorial
cols = ''.join(f'<div style="background:rgba(184,149,90,.07);border-left:1px solid rgba(184,149,90,.4);border-right:1px solid rgba(184,149,90,.4)"></div>' for _ in range(12))
P(f'''<div class="col" style="inset:0;background:{GRAPH}"></div><div class="col" style="left:120px;top:0;width:1680px;height:1080px;display:grid;grid-template-columns:repeat(12,1fr);gap:24px">{cols}</div>
<div class="col" style="left:0;top:120px;width:1920px;height:1px;background:rgba(184,149,90,.6)"></div><div class="col" style="left:0;top:960px;width:1920px;height:1px;background:rgba(184,149,90,.6)"></div>
<div class="col" style="left:120px;top:170px;width:820px"><div class="ey">Grid</div><div class="h2" style="margin-top:20px">12 colunas, margem 120, calha 24.</div>
<div class="p" style="margin-top:26px">Título ocupa de 1 a 7 colunas; texto, 5 colunas no máximo. Símbolo cortado sempre encostado numa borda, nunca solto no meio.</div></div>
<div class="col" style="left:1090px;top:420px">{K(22, BRASS)}</div>
<div class="col" style="left:126px;bottom:70px;font:500 15px 'JetBrains Mono';color:#B8955A;letter-spacing:.14em">1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · 11 · 12</div>''', sec='05 · Grid')

# 15 iconografia: traço 1,6 u, ângulos das juntas
ic = {'Código': '<path d="M8 6 L3 12 L8 18 M16 6 L21 12 L16 18"/>', 'IA': '<rect x="5" y="5" width="14" height="14"/><path d="M9 9h6v6H9z M12 2v3 M12 19v3 M2 12h3 M19 12h3"/>',
      'Marca': '<path d="M4 4h16l-3 16H7z M10 4v16 M10 12l6-8 M10 12l5 8"/>', 'Mídia': '<rect x="3" y="6" width="18" height="12"/><path d="M10 9l5 3-5 3z"/>',
      'Crescer': '<path d="M3 20h18 M6 16l5-5 3 3 6-7 M15 7h5v5"/>', 'Pessoas': '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-4 3-6 6-6s6 2 6 6 M16 5a3 3 0 010 6 M18 14c2 1 3 3 3 6"/>',
      'Dados': '<ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v12c0 1.7 3.6 3 8 3s8-1.3 8-3V6 M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>', 'Global': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18 M12 3c3 3 3 15 0 18 M12 3c-3 3-3 15 0 18"/>',
      'Segurança': '<path d="M12 3l8 3v6c0 5-4 8-8 9-4-1-8-4-8-9V6z M9 12l2 2 4-4"/>', 'Voz': '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0014 0 M12 18v3"/>',
      'Agenda': '<rect x="3" y="5" width="18" height="16"/><path d="M3 10h18 M8 3v4 M16 3v4"/>', 'Conexão': '<path d="M4 18c3-8 13-8 16 0 M2 18h20 M8 18v-4 M16 18v-4 M12 18V10"/>'}
os.makedirs(B + '/icones', exist_ok=True)
for n, d in ic.items():
    open(f'{B}/icones/{n.lower()}.svg', 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="#0B0C0E" stroke-width="1.6" stroke-linecap="square" stroke-linejoin="miter">{d}</svg>')
P(f'''<div class="col" style="left:120px;top:150px;width:560px"><div class="ey">Iconografia</div><div class="h2" style="margin-top:20px">Traço da junta.</div>
<div class="p" style="margin-top:28px">Grid de 24 u, traço de 1,6 u (a mesma junta do símbolo), cantos vivos, sem preenchimento. Um estilo só.</div></div>
<div class="col" style="left:860px;top:150px;width:940px;display:grid;grid-template-columns:repeat(4,1fr);gap:16px">''' +
  ''.join(f'<div style="background:#15171a;border-radius:4px;height:220px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px"><svg viewBox="0 0 24 24" width="76" height="76" fill="none" stroke="{LIME if j%5 else BRASS}" stroke-width="1.6" stroke-linecap="square">{d}</svg><div class="mono" style="font-size:14px;opacity:.6">{n}</div></div>' for j, (n, d) in enumerate(ic.items())) + '</div>', sec='06 · Iconografia')

# 16 padrões gráficos
tile = ''.join(f'<g transform="translate({90 + x*130 + (65 if y%2 else 0)},{200 + y*130})">' + ''.join(f'<path fill="{LIME if (x+y)%7 else BRASS}" fill-opacity="{.9 if (x+y)%7 else 1}" d="{path(p,4.4)}"/>' for i, p in enumerate(pecas())) + '</g>' for y in range(6) for x in range(6) if 90 + x*130 + (65 if y%2 else 0) + 106 <= 900)
arcos = ''.join(f'<g transform="translate(470,620) rotate({j*12}) translate(-24,-420)"><path fill="{DIV[abs(j)%4][1] if j!=0 else LIME}" d="{path(KEY,2)}"/></g>' for j in range(-7, 8))
P(f'''<svg class="col" style="left:0;top:0" width="960" height="1080"><rect width="960" height="1080" fill="{INK}"/>{tile}</svg>
<svg class="col" style="left:960px;top:0" width="960" height="1080"><rect width="960" height="1080" fill="{GRAPH}"/>{arcos}</svg>
<div class="col" style="left:90px;top:130px"><div class="ey">Padrão 01 · Alvenaria</div></div><div class="col" style="left:90px;top:990px;width:800px"><div class="ps">Símbolos inteiros em fiada, 1 latão a cada 7. Nunca cortados na borda.</div></div>
<div class="col" style="left:1080px;top:820px;width:700px;background:{GRAPH};padding:20px"><div class="ey">Padrão 02 · Arco</div><div class="ps" style="margin-top:8px">Aduelas em leque nas cores das divisões. Capas, abertura de vídeo, fachada.</div></div>''', sec='07 · Padrões')

# 17 direção de foto
pedra_bg0 = "background:radial-gradient(500px 400px at 30% 20%,rgba(255,200,130,.45),transparent 70%),repeating-linear-gradient(0deg,#2b2824 0 118px,#0d0c0b 118px 121px),#2b2824"
P(f'''<div class="col" style="left:120px;top:150px;width:560px"><div class="ey">Direção de foto</div><div class="h2" style="margin-top:20px">Luz de fim de tarde, gente trabalhando.</div>
<div class="p" style="margin-top:28px">Foto real, cor natural levemente quente, sombra profunda. Pessoas fazendo (código, reunião, gravação), nunca posando. Arquitetura de São Luís em detalhe de pedra e luz.</div>
<div style="margin-top:30px" class="ps"><b style="color:#5fd1a8">Sim:</b> mãos, telas, pedra, contra-luz, grão leve.<br><b style="color:#ff7a57">Não:</b> banco de imagem sorrindo, aperto de mão, globo, circuito azul, sépia.</div></div>
<div class="col" style="left:860px;top:150px;width:940px;height:780px;display:grid;grid-template-columns:1.3fr 1fr;grid-template-rows:1fr 1fr;gap:16px">
<div style="grid-row:span 2;{pedra_bg0};border-radius:4px;position:relative"><div class="mono" style="position:absolute;left:18px;bottom:16px;font-size:14px;background:{INK};padding:6px 10px">Pedra · detalhe e escala</div></div>
<div style="background:url(../../gerador/slz2.jpg) center/cover;filter:saturate(.8) contrast(1.1);border-radius:4px;position:relative"><div class="mono" style="position:absolute;left:18px;bottom:16px;font-size:14px;background:{INK};padding:6px 10px">Cidade · origem</div></div>
<div style="background:linear-gradient(160deg,#2a1d12,#0b0c0e 60%),radial-gradient(circle at 70% 30%,#c8893c,transparent 50%);border-radius:4px;position:relative;display:flex;align-items:center;justify-content:center"><div style="width:62%;height:52%;background:linear-gradient(180deg,#1d2a4a,#0f1424);border:8px solid #000;border-radius:6px;box-shadow:0 0 80px rgba(200,137,60,.35)"></div><div class="mono" style="position:absolute;left:18px;bottom:16px;font-size:14px;background:{INK};padding:6px 10px">Tela · luz âmbar, quarto escuro</div></div></div>''', sec='08 · Imagem')

# 18 motion
fr = ['As 4 pedras entram de 4 lados', 'Encaixam: a junta forma o K', 'Clique seco (impacto + SFX)', 'Brilho de latão corre a chave', 'Wordmark sobe em 8 frames']
def frame(k):
    if k == 0:
        return ''.join(f'<g transform="translate({[-60,40,70,40][i]},{[0,-60,0,60][i]})"><path fill="{LIME}" fill-opacity=".5" d="{path(p,6)}"/></g>' for i, p in enumerate(pecas()))
    if k == 1:
        return ''.join(f'<g transform="translate({[-12,8,14,8][i]},{[0,-12,0,12][i]})"><path fill="{LIME}" d="{path(p,6)}"/></g>' for i, p in enumerate(pecas()))
    if k == 2:
        return ''.join(f'<path fill="{LIME}" d="{path(p,6)}"/>' for p in pecas()) + '<circle cx="72" cy="72" r="110" fill="none" stroke="#B8955A" stroke-opacity=".6"/>'
    if k == 3:
        return ''.join(f'<path fill="url(#gl)" d="{path(p,6)}"/>' for p in pecas())
    return ''.join(f'<path fill="{BRASS}" d="{path(p,4)}"/>' for p in pecas())
P(f'''<div class="col" style="left:120px;top:140px"><div class="ey">Motion · assinatura animada (3 s, com som)</div><div class="h2" style="margin-top:20px">A chave se fecha.</div></div>
<div class="col" style="left:120px;top:400px;width:1680px;display:grid;grid-template-columns:repeat(5,1fr);gap:16px">''' +
  ''.join(f'''<div><div style="height:186px;background:url(../fotos-v2.1/motion/f{t}.jpg) center/cover;border-radius:3px"></div><div class="mono" style="margin-top:14px;color:{BRASS}">{t.replace('.',',')} s</div><div class="ps" style="margin-top:6px;font-size:20px">{d}</div></div>''' for t, d in zip(['0.3','0.8','1.3','1.7','2.6'], fr)) +
  '''</div><div class="col" style="left:120px;top:800px;width:1680px;display:grid;grid-template-columns:repeat(3,1fr);gap:40px">''' + ''.join(f'<div style="border-top:1px solid rgba(239,234,225,.2);padding-top:14px"><div class="mono" style="color:{BRASS};font-size:14px">{a}</div><div class="ps" style="margin-top:6px">{b}</div></div>' for a,b in [('Arquivo','v2/motion/alkantara-logo.mp4 · 1920×1080'),('Curva','ease-out expo (0,16 1 0,3 1)'),('Som','dois toques graves de pedra + harmônico metálico')]) + '</div>', sec='09 · Motion')

# 19 abertura aplicações
P(f'''{corte(58, 860, -120, '#15171a', 1, 1, BRASS)}<div class="col" style="left:120px;bottom:150px"><div class="ey">Parte 2</div><div class="h1" style="font-size:220px;margin-top:20px">Aplica<span class="it" style="color:{BRASS}">ções.</span></div></div>''', sec='Aplicações')

# 20 papelaria (flat lay escuro)
timbrado = chapa(560, 792, '#f6f2ea', f'''<div style="position:absolute;left:48px;top:48px">{logo("horizontal","positivo",28)}</div><div style="position:absolute;left:48px;top:150px;right:48px;font:500 10px/1.8 I;color:#555">São Luís, 16 de novembro de 2026<br><br>Prezado Carlos,<br><br>{"Segue a proposta conforme combinado, com prazo e responsável por etapa. " * 6}</div><div style="position:absolute;left:48px;bottom:40px;right:48px;border-top:1px solid #ddd;padding-top:10px;font:500 8px 'JetBrains Mono';letter-spacing:.12em;color:#888">AL KÁNTARA GROUP · ALKANTARA.GROUP · SÃO LUÍS · MA</div><div style="position:absolute;right:-30px;top:-30px">{K(5,"#ebe5d9")}</div>''', rz=-6)
envelope = chapa(700, 340, INK, f'<div style="position:absolute;left:40px;top:36px">{K(2.4,BRASS)}</div><div style="position:absolute;right:40px;bottom:36px">{logo("wordmark","negativo",22)}</div>', rz=8)
P(f'''<div class="col" style="inset:0;{MESA}"></div>
<div class="col" style="left:300px;top:110px">{timbrado}</div><div class="col" style="left:900px;top:180px">{envelope}</div>
<div class="col" style="left:960px;top:600px">{card_frente(420, 247)}</div><div class="col" style="left:1420px;top:620px;transform:rotate(-10deg)">{card_verso(420, 247)}</div>
<div class="col" style="left:120px;bottom:100px"><div class="ey">Papelaria · timbrado A4, envelope DL, cartão 85 × 55</div></div>''', sec='Aplicações')

# 21 cartão close
P(f'''<div class="col" style="inset:0;{MESA_CLARA}"></div>
<div class="col" style="left:180px;top:230px">{card_frente(860, 506)}</div><div class="col" style="left:900px;top:400px;transform:rotate(-7deg)">{card_verso(860, 506)}</div>
<div class="col" style="left:120px;bottom:100px"><div class="ey" style="color:{INK};opacity:.6">Cartão de visita · papel Color Plus Preto 350 g + hot stamping latão / verso calcário</div></div>''', sec='Aplicações')

# 22 assinatura de e-mail
assin = f'''<div style="display:flex;gap:26px;align-items:center;padding:26px 0;border-top:1px solid #e6e1d8"><div style="width:84px;height:84px;background:{INK};display:flex;align-items:center;justify-content:center">{K(2.6,BRASS)}</div>
<div><div style="font:400 26px F;color:{INK}">Lindson Almeida</div><div style="font:500 11px 'JetBrains Mono';letter-spacing:.14em;color:#9a7741;margin-top:6px">FUNDADOR · AL KÁNTARA GROUP</div><div style="font:500 13px I;color:#666;margin-top:8px">alkantara.group · São Luís, MA</div></div>
<div style="margin-left:auto;display:flex;gap:6px">''' + ''.join(f'<div style="width:8px;height:44px;background:{c}"></div>' for _, c, _, _ in DIV) + '</div></div>'
P(f'''<div class="col" style="inset:0;background:linear-gradient(135deg,#1b1d22,#0b0c0e)"></div>
<div class="col" style="left:260px;top:140px">{chapa(1400, 800, '#fff', f"""<div style='height:46px;background:#f1efeb;display:flex;align-items:center;gap:8px;padding-left:18px'><i style='width:12px;height:12px;border-radius:50%;background:#ff5f57'></i><i style='width:12px;height:12px;border-radius:50%;background:#febc2e'></i><i style='width:12px;height:12px;border-radius:50%;background:#28c840'></i></div>
<div style='padding:40px 60px;color:#222;font:500 17px/1.7 I'><div style='font:600 22px I'>Proposta · automação do atendimento</div><div style='color:#888;font-size:14px'>para: carlos@empresa.com.br</div><br>Bom dia, Carlos.<br><br>Segue a proposta com o prazo combinado no contrato e relatório semanal. Qualquer dúvida, me chame no WhatsApp.<br><br>Abraço,<br>{assin}</div>""")}</div>
<div class="col" style="left:120px;bottom:100px"><div class="ey">Assinatura de e-mail · HTML em templates/assinatura.html</div></div>''', sec='Aplicações')

# 23 crachá
def cracha(nome, cargo, div, c, rz):
    return f'''<div style="transform:rotate({rz}deg);display:flex;flex-direction:column;align-items:center"><div style="width:46px;height:420px;background:repeating-linear-gradient(90deg,{INK} 0 6px,#16181b 6px 12px);box-shadow:inset 0 0 0 1px rgba(255,255,255,.04)"></div>
<div style="width:70px;height:40px;border:6px solid #9b9b9b;border-radius:10px;margin-top:-6px;background:transparent"></div>
{chapa(360, 560, LIME, f"""<div style='height:150px;background:{c}'></div><div style='position:absolute;left:30px;top:90px;width:120px;height:120px;background:{INK};display:flex;align-items:center;justify-content:center'>{K(3.4,BRASS)}</div>
<div style='position:absolute;left:30px;top:250px;color:{INK}'><div style='font:400 38px/1 F'>{nome}</div><div style='font:500 12px "JetBrains Mono";letter-spacing:.14em;margin-top:12px;opacity:.6'>{cargo}</div></div>
<div style='position:absolute;left:30px;bottom:30px'>{divlogo(div,'positivo',30)}</div>""", extra='border-radius:14px;margin-top:-4px')}</div>'''
P(f'''<div class="col" style="inset:0;background:url(../fotos-v2.1/notebook.jpg) center/cover;filter:brightness(.8)"></div><div class="col" style="inset:0;background:radial-gradient(900px 600px at 50% 40%,transparent,rgba(0,0,0,.45))"></div><div class="col" style="left:380px;top:-180px">{cracha('Ana Ribeiro', 'ENGENHARIA', 'Labs', '#2E4BFF', -4)}</div>
<div class="col" style="left:1080px;top:-140px">{cracha('Bruno Sá', 'DIREÇÃO DE ARTE', 'Labs', '#2E4BFF', 5)}</div>
<div class="col" style="left:120px;bottom:100px"><div class="ey">Crachá 54 × 86 · sobre mesa real (foto CC0) · nomes ilustrativos</div></div>''', sec='Aplicações')

# 24 fachada · parede de pedra com letra caixa em latão
pedra_bg = "background-color:#3a3631;background-image:url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='600'%3E%3Cfilter id='s'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.012 .03' numOctaves='5' seed='7'/%3E%3CfeColorMatrix values='0 0 0 0 .45 0 0 0 0 .41 0 0 0 0 .36 0 0 0 .9 0'/%3E%3C/filter%3E%3Crect width='600' height='600' filter='url(%23s)'/%3E%3C/svg%3E\");"
fiadas = ''.join(f'<div style="position:absolute;left:0;right:0;top:{y}px;height:2px;background:rgba(0,0,0,.45)"></div>' for y in range(60, 1080, 120))
P(f'''<div class="col" style="inset:0;background:url(../fotos-v2.1/mock-fachada.jpg) center/cover"></div>
<div class="col" style="left:0;right:0;bottom:0;height:260px;background:linear-gradient(0deg,rgba(11,12,14,.9),transparent)"></div>
<div class="col" style="left:120px;bottom:100px"><div class="ey" style="color:#e2c28a">Fachada · placa grafite e latão no Centro Histórico de São Luís · foto base Prburley, CC BY 4.0</div></div>''', sec='Aplicações')

# 24b placa em parede de concreto (v2.1: textura e luz rasante em CSS)
conc = "background-color:#8d8a84;background-image:radial-gradient(1400px 700px at 20% -10%,rgba(255,240,215,.45),transparent 60%),url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='700' height='700'%3E%3Cfilter id='c'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' seed='3'/%3E%3CfeColorMatrix values='0 0 0 0 .5 0 0 0 0 .49 0 0 0 0 .47 0 0 0 .55 0'/%3E%3C/filter%3E%3Crect width='700' height='700' filter='url(%23c)'/%3E%3C/svg%3E\");"
furos = ''.join(f'<div class="col" style="left:{x}px;top:{y}px;width:16px;height:16px;border-radius:50%;background:radial-gradient(circle at 60% 65%,#3d3b37,#5d5a55 70%);box-shadow:0 1px 0 rgba(255,255,255,.3)"></div>' for x in range(150, 1920, 480) for y in range(120, 1080, 360))
juntas_c = ''.join(f'<div class="col" style="left:0;right:0;top:{y}px;height:2px;background:rgba(40,38,35,.35)"></div>' for y in (300, 660)) + ''.join(f'<div class="col" style="top:0;bottom:0;left:{x}px;width:2px;background:rgba(40,38,35,.3)"></div>' for x in (390, 1350))
P(f'''<div class="col" style="inset:0;{conc}"></div>{juntas_c}{furos}
<div class="col" style="left:560px;top:170px;width:800px;height:640px;background:linear-gradient(160deg,#25272c,#101114);border-radius:4px;box-shadow:30px 46px 50px rgba(0,0,0,.45)">
<div style="position:absolute;left:300px;top:100px"><img src="../logos/svg/alkantara-simbolo-latao.svg" style="width:200px"></div>
<div style="position:absolute;left:0;right:0;top:380px;text-align:center"><img src="../logos/svg/alkantara-wordmark-latao.svg" style="height:58px"></div>
<div style="position:absolute;left:0;right:0;bottom:60px;text-align:center;font:500 16px 'JetBrains Mono';letter-spacing:.3em;color:#9b7d4b">SÃO LUÍS · MARANHÃO</div>
<div style="position:absolute;inset:0;background:linear-gradient(110deg,rgba(255,255,255,.09),transparent 40%);border-radius:4px"></div></div>
<div class="col" style="left:120px;bottom:100px"><div class="ey" style="color:{INK}">Placa de recepção · grafite e latão em concreto aparente, luz rasante</div></div>''', sec='Aplicações')

# 25 sinalização interna
P(f'''<div class="col" style="inset:0;background:linear-gradient(180deg,#d9d3c7,#bdb5a6)"></div>
<div class="col" style="left:0;right:0;top:820px;bottom:0;background:linear-gradient(180deg,#8d857a,#5f584f)"></div>
<div class="col" style="left:260px;top:130px">{chapa(520, 640, INK, f"""<div style='padding:44px'><div style='font:500 13px "JetBrains Mono";letter-spacing:.14em;color:{BRASS}'>2º ANDAR</div>""" + ''.join(f"""<div style='display:flex;align-items:center;gap:18px;padding:22px 0;border-top:1px solid rgba(239,234,225,.15);margin-top:{18 if j==0 else 0}px'><div style='width:14px;height:40px;background:{c}'></div><div style='font:400 40px F;color:{LIME}'>{n}</div><div style='margin-left:auto;font:600 30px I;color:{LIME}'>{['←','→','↑','↓'][j]}</div></div>""" for j, (n, c, _, _) in enumerate(DIV)) + '</div>')}</div>
<div class="col" style="left:1000px;top:200px">{chapa(260, 540, '#2E4BFF', f"<div style='position:absolute;left:36px;top:40px'>{K(7.5,LIME)}</div><div style='position:absolute;left:36px;bottom:44px;font:400 64px F;color:{LIME}'>Labs</div><div style='position:absolute;left:36px;bottom:24px;font:500 11px \"JetBrains Mono\";color:{LIME};opacity:.7;letter-spacing:.14em'>SALA 201</div>")}</div>
<div class="col" style="left:1340px;top:200px">{chapa(260, 540, '#E8461E', f"<div style='position:absolute;left:36px;top:40px'>{K(7.5,INK)}</div><div style='position:absolute;left:36px;bottom:44px;font:400 54px F;color:{INK}'>Barzakh</div><div style='position:absolute;left:36px;bottom:24px;font:500 11px \"JetBrains Mono\";color:{INK};opacity:.7;letter-spacing:.14em'>SALA 202</div>")}</div>
<div class="col" style="left:120px;bottom:100px"><div class="ey" style="color:{LIME}">Sinalização interna · totem e placas de sala por divisão</div></div>''', sec='Aplicações')

# 26 apresentação
slide = lambda c: f'''<div style="position:absolute;inset:0;background:{INK}"></div><div style="position:absolute;right:-60px;top:-40px">{K(16,"#16181c",1,BRASS)}</div><div style="position:absolute;left:50px;top:40px">{logo("horizontal","negativo",22)}</div><div style="position:absolute;left:50px;bottom:50px;color:{LIME}"><div style="font:500 11px 'JetBrains Mono';letter-spacing:.14em;color:{BRASS}">RELATÓRIO · 2026</div><div style="font:400 72px/.95 F;letter-spacing:-.02em;margin-top:14px">Quatro pedras,<br><i>uma chave.</i></div></div>'''
P(f'''<div class="col" style="inset:0;background:radial-gradient(1200px 700px at 50% 30%,#2a2c31,#0b0c0e)"></div>
<div class="col" style="left:310px;top:120px;width:1300px;height:770px;background:#050506;border-radius:22px;padding:22px;box-shadow:0 60px 120px rgba(0,0,0,.7)"><div style="position:relative;width:100%;height:100%;overflow:hidden;border-radius:4px">{slide(1)}</div></div>
<div class="col" style="left:860px;top:890px;width:200px;height:60px;background:linear-gradient(#202125,#0e0f11)"></div><div class="col" style="left:760px;top:948px;width:400px;height:14px;background:#26272b;border-radius:6px"></div>
<div class="col" style="left:120px;bottom:100px"><div class="ey">Apresentação 16:9 · modelo em templates/apresentacao.html</div></div>''', sec='Aplicações')

# 27 site
site = f'''<div style="height:44px;background:#e9e6e0;display:flex;align-items:center;gap:8px;padding-left:16px"><i style="width:11px;height:11px;border-radius:50%;background:#ff5f57"></i><i style="width:11px;height:11px;border-radius:50%;background:#febc2e"></i><i style="width:11px;height:11px;border-radius:50%;background:#28c840"></i><div style="margin-left:30px;background:#fff;border-radius:6px;padding:5px 160px 5px 14px;font:500 12px I;color:#666">alkantara.group</div></div>
<div style="position:relative;height:776px;background:{INK};overflow:hidden"><div style="position:absolute;left:60px;top:34px">{logo("horizontal","negativo",26)}</div>
<div style="position:absolute;right:60px;top:40px;display:flex;gap:34px;font:500 14px I;color:{LIME};opacity:.8"><span>Labs</span><span>Studio</span><span>Media</span><span>Ventures</span><span style="color:{BRASS}">Contato →</span></div>
<div style="position:absolute;right:-120px;top:60px">{K(26,"#15171a",2,BRASS)}</div>
<div style="position:absolute;left:60px;top:220px;color:{LIME}"><div style="font:500 12px 'JetBrains Mono';letter-spacing:.16em;color:{BRASS}">GRUPO DE TECNOLOGIA · SÃO LUÍS</div><div style="font:400 118px/.92 F;letter-spacing:-.02em;margin-top:22px">Estrutura<br>para o que <i style="color:{BRASS}">vem.</i></div>
<div style="font:500 18px/1.5 I;opacity:.75;max-width:520px;margin-top:26px">{PITCH}</div><div style="margin-top:30px;display:inline-block;background:{LIME};color:{INK};font:600 15px I;padding:16px 26px">Conheça as divisões</div></div>
<div style="position:absolute;left:0;right:0;bottom:0;display:grid;grid-template-columns:repeat(4,1fr)">''' + ''.join(f'<div style="border-top:4px solid {c};padding:22px 30px;background:#121316;color:{LIME}"><div style="font:400 30px F">{n}</div><div style="font:500 12px I;opacity:.6;margin-top:6px">{t}</div></div>' for n, c, t, _ in DIV) + '</div></div>'
P(f'''<div class="col" style="inset:0;background:url(../fotos-v2.1/mock-notebook.jpg) center/cover"></div>
<div class="col" style="left:0;right:0;bottom:0;height:240px;background:linear-gradient(0deg,rgba(11,12,14,.85),transparent)"></div>
<div class="col" style="left:120px;bottom:100px"><div class="ey" style="color:#e2c28a">Site · home no notebook · foto base CC0 (Pixabay, via Wikimedia)</div></div>''', sec='Aplicações')

# 28 redes: perfil + destaques
grid9 = ''.join(f'<div style="aspect-ratio:4/5;background:{bg};position:relative;overflow:hidden">{inner}</div>' for bg, inner in [
    (INK, f'<div style="position:absolute;left:12px;bottom:12px;font:400 22px/1 F;color:{LIME}">Quatro<br>pedras.</div>'), ('#2E4BFF', f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{K(2.6,LIME,0,INK)}</div>'), (LIME, f'<div style="position:absolute;left:12px;top:12px;font:400 20px/1 F;color:{INK}"><i>Estrutura</i> para o que vem.</div>'),
    ('#E8461E', f'<div style="position:absolute;left:12px;bottom:12px;font:400 26px F;color:{INK}">Studio</div>'), (GRAPH, f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{K(3,BRASS)}</div>'), ('#F0A202', f'<div style="position:absolute;left:12px;bottom:12px;font:400 26px F;color:{INK}">Media</div>'),
    (LIME, f'<div style="position:absolute;right:-20px;bottom:-20px">{K(4,INK)}</div>'), ('#0E8C66', f'<div style="position:absolute;left:12px;bottom:12px;font:400 26px F;color:{LIME}">Ventures</div>'), (INK, f'<div style="position:absolute;left:12px;top:12px;font:500 9px \'JetBrains Mono\';color:{BRASS};letter-spacing:.14em">MANIFESTO</div><div style="position:absolute;left:12px;bottom:12px;font:400 18px/1.05 F;color:{LIME}">Uma ponte não é decoração.</div>')])
phone = f'''<div style="width:430px;height:900px;background:#050506;border-radius:60px;padding:14px;box-shadow:0 50px 100px rgba(0,0,0,.6),inset 0 0 0 2px #2a2a2e"><div style="width:100%;height:100%;border-radius:48px;overflow:hidden;background:#fff;position:relative">
<div style="padding:60px 20px 0;display:flex;align-items:center;gap:22px"><div style="width:96px;height:96px;border-radius:50%;background:{INK};display:flex;align-items:center;justify-content:center">{K(2.3,BRASS)}</div><div style="display:flex;gap:22px;font:600 15px I;text-align:center"><div>9<br><span style="font-weight:500;font-size:12px">posts</span></div><div>—<br><span style="font-weight:500;font-size:12px">seguidores</span></div></div></div>
<div style="padding:12px 20px;font:600 14px I">Al Kántara Group</div><div style="padding:0 20px;font:500 13px/1.4 I;color:#333">Grupo de tecnologia · São Luís, MA<br>Labs · Studio · Media · Ventures<br>Estrutura para o que vem.</div>
<div style="display:flex;gap:14px;padding:16px 20px">''' + ''.join(f'<div style="text-align:center"><div style="width:60px;height:60px;border-radius:50%;border:2px solid #ddd;padding:3px"><div style="width:100%;height:100%;border-radius:50%;background:{c};display:flex;align-items:center;justify-content:center">{K(1.3,LIME if n!="Media" else INK,i,INK if n!="Media" else LIME)}</div></div><div style="font:500 10px I;margin-top:4px">{n}</div></div>' for i, (n, c, _, _) in enumerate(DIV)) + f'''</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2px">{grid9}</div></div></div>'''
P(f'''<div class="col" style="inset:0;{MESA}"></div><div class="col" style="left:240px;top:90px">{phone}</div>
<div class="col" style="left:860px;top:200px;width:940px"><div class="ey">Instagram · perfil, destaques e grade</div><div class="h2" style="margin-top:20px">Avatar = símbolo latão.</div>
<div class="p" style="margin-top:26px">Destaques nas cores das divisões com a pedra de cada uma. Grade em xadrez: escuro, cor, claro. A mesma identidade no LinkedIn, YouTube e site.</div>
<div style="margin-top:40px;display:flex;gap:20px">''' + ''.join(f'<div style="width:150px;height:150px;border-radius:50%;background:{c};display:flex;align-items:center;justify-content:center">{K(3.6,LIME if n!="Media" else INK,i,INK if n!="Media" else LIME)}</div>' for i, (n, c, _, _) in enumerate(DIV)) + '</div></div>', sec='Aplicações')

# 29 três posts
post = lambda bg, inner: chapa(500, 625, bg, inner)
P(f'''<div class="col" style="inset:0;background:{GRAPH}"></div>
<div class="col" style="left:150px;top:180px">{post(INK, f"<div style='position:absolute;right:-90px;top:-60px'>{K(16,'#16181c',0,'#2E4BFF')}</div><div style='position:absolute;left:36px;top:36px;font:500 11px JetBrains Mono;color:{BRASS};letter-spacing:.14em'>AL KÁNTARA LABS</div><div style='position:absolute;left:36px;bottom:40px;font:400 54px/1 F;color:{LIME}'>Sua equipe<br>não nasceu<br>para <i>copiar<br>e colar.</i></div>")}</div>
<div class="col" style="left:710px;top:130px">{post(LIME, f"<div style='position:absolute;left:36px;top:36px'>{logo('horizontal','positivo',22)}</div><div style='position:absolute;left:36px;top:180px;font:400 160px/.8 F;color:{INK};letter-spacing:-.02em'>4</div><div style='position:absolute;left:36px;bottom:40px;right:36px;font:400 34px/1.1 F;color:{INK}'>divisões, uma chave. Conheça o grupo.</div><div style='position:absolute;right:36px;top:200px;display:flex;flex-direction:column;gap:8px'>" + ''.join(f"<div style='width:120px;height:26px;background:{c}'></div>" for _, c, _, _ in DIV) + "</div>")}</div>
<div class="col" style="left:1270px;top:180px">{post('#E8461E', f"<div style='position:absolute;left:36px;top:36px;font:500 11px JetBrains Mono;color:{INK};letter-spacing:.14em'>BARZAKH · UM ESTÚDIO AL KÁNTARA</div><div style='position:absolute;left:36px;top:110px;right:36px;height:300px;background:{INK};display:flex;align-items:center;justify-content:center'>{card_frente(300,176)}</div><div style='position:absolute;left:36px;bottom:40px;font:400 44px/1 F;color:{INK}'>Marca no nível<br>do <i>seu preço.</i></div>")}</div>
<div class="col" style="left:120px;bottom:100px"><div class="ey">Posts 4:5 · Labs (ganho), Grupo (apresentação), Barzakh (case)</div></div>''', sec='Aplicações')

# 29b redes · story, capa do YouTube e avatar (v2.1)
story = chapa(380, 676, INK, f"<div style='position:absolute;right:-120px;top:120px'>{K(18,'#16181c',1,BRASS)}</div><div style='position:absolute;left:30px;top:40px'>{logo('horizontal','negativo',22)}</div><div style='position:absolute;left:30px;bottom:150px;font:400 52px/1 F;color:{LIME}'>Quatro<br>pedras,<br><i style='color:{BRASS}'>uma chave.</i></div><div style='position:absolute;left:30px;right:30px;bottom:50px;background:{LIME};color:{INK};font:600 17px I;padding:14px;text-align:center'>Conheça o grupo</div>")
yt = chapa(1000, 562, INK, f"<div style='position:absolute;inset:0;background:url(../fotos-v2.1/slz-portugal.jpg) center 40%/cover;filter:brightness(.35) saturate(.7)'></div><div style='position:absolute;left:250px;right:250px;top:190px;bottom:190px;border:1px dashed rgba(184,149,90,.6)'></div><div style='position:absolute;left:0;right:0;top:215px;text-align:center'>{logo('horizontal','latao',62)}</div><div style='position:absolute;left:0;right:0;top:300px;text-align:center;font:400 30px F;color:{LIME}'>Estrutura para o que <i>vem.</i></div>")
P(f'''<div class="col" style="inset:0;{MESA}"></div>
<div class="col" style="left:120px;top:150px">{story}<div class="mono" style="margin-top:22px;color:{BRASS}">Story 1080 × 1920</div></div>
<div class="col" style="left:600px;top:150px">{yt}<div class="mono" style="margin-top:22px;color:{BRASS}">Capa do YouTube 2560 × 1440 · área segura tracejada</div></div>
<div class="col" style="left:600px;top:820px;display:flex;gap:30px;align-items:center">''' + ''.join(f'<div style="width:120px;height:120px;border-radius:50%;background:{bg};display:flex;align-items:center;justify-content:center">{K(2.8,c)}</div>' for bg, c in [(INK, BRASS), (LIME, INK), (BRASS, INK)]) + '''<div class="ps" style="max-width:520px">Avatar: símbolo latão sobre tinta, igual em Instagram, LinkedIn, YouTube e WhatsApp.</div></div>''', sec='Aplicações')

# 30 brindes
caneca = f'''<div style="position:relative;width:300px;height:340px"><div style="position:absolute;right:-70px;top:80px;width:120px;height:170px;border:26px solid {INK};border-radius:0 80px 80px 0;border-left:none"></div>
<div style="position:absolute;inset:0;border-radius:10px 10px 40px 40px;background:linear-gradient(90deg,#050506,#24262b 40%,#0b0c0e 75%,#000);box-shadow:0 40px 60px rgba(0,0,0,.55)"></div><div style="position:absolute;left:105px;top:110px">{K(4,BRASS)}</div><div style="position:absolute;top:-8px;left:0;right:0;height:20px;border-radius:50%;background:#1b1c20"></div></div>'''
bolsa = f'''<div style="position:relative;width:420px;height:520px"><div style="position:absolute;left:90px;top:-120px;width:240px;height:220px;border:16px solid #d8d0c0;border-bottom:none;border-radius:120px 120px 0 0"></div>
<div style="position:absolute;inset:0;background:linear-gradient(100deg,#e7e0d2,#d6cdbb);box-shadow:0 40px 70px rgba(0,0,0,.35)"></div><div style="position:absolute;left:40px;bottom:40px">{logo('vertical','positivo',150)}</div><div style="position:absolute;right:-1px;top:0;width:60px;height:100%;background:#E8461E"></div></div>'''
caderno = chapa(380, 500, INK, f"<div style='position:absolute;left:0;top:0;bottom:0;width:22px;background:#000'></div><div style='position:absolute;left:60px;top:50px'>{logo('wordmark','latao',20)}</div><div style='position:absolute;right:-50px;bottom:-40px'>{K(11,'#16181c',3,'#0E8C66')}</div>", rz=-8)
P(f'''<div class="col" style="inset:0;{MESA_CLARA}"></div><div class="col" style="left:180px;top:420px">{caneca}</div><div class="col" style="left:700px;top:330px">{bolsa}</div><div class="col" style="left:1310px;top:320px">{caderno}</div>
<div class="col" style="left:120px;bottom:100px"><div class="ey" style="color:{INK};opacity:.7">Brindes · caneca preta com latão, ecobag cru com faixa de divisão, caderno com endosso</div></div>''', 'l', 'Aplicações')

# 31 entregáveis + contracapa
P(f'''<div class="col" style="left:120px;top:150px;width:760px"><div class="ey">Arquivos</div><div class="h2" style="margin-top:20px">Tudo no pacote.</div>
<div style="margin-top:36px" class="ps">logos/ · SVG, PNG e PDF (grupo e 4 divisões, 7 variações)<br>paleta/ · .ase e .json<br>fontes/ · Fraunces, Inter Tight (OFL)<br>icones/ · 12 SVG<br>templates/ · apresentação, post, assinatura de e-mail (HTML editável)<br>motion/ · animação do logo com som<br>logos/barzakh/ · Barzakh · um estúdio Al Kántara<br>fotos-v2.1/ · fotos livres e mockups (créditos em CREDITOS.md)</div></div>
<div class="col" style="left:1180px;top:300px">{K(20, BRASS)}</div><div class="col" style="left:1110px;top:830px"><div class="h3">Estrutura para o que vem.</div></div>''', sec='Arquivos')
