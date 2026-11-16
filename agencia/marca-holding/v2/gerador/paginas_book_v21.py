# Brand Book v2.1 · páginas (revisão conta Leandro 16/11/2026 sobre a v2 da conta Pedro)
# Brand Book v2 · páginas (executado dentro de gerar.py)
# 01 capa · copia Base Design/DixonBaxi: símbolo gigante cortado na borda + título editorial
P(f'''{corte(52, 900, -170, BRASS, 1)}{juntas(LIME,.08)}
<div class="col" style="left:120px;top:150px">{logo('horizontal','negativo',64)}</div>
<div class="col" style="left:120px;bottom:150px"><div class="ey">Brand Book v2.1 · Plataforma, públicos e arquitetura</div>
<div class="h1" style="font-size:230px;margin-top:26px">Quatro<br>pedras,<br><span class="it" style="color:{BRASS}">uma chave.</span></div></div>''', sec='none')

# 02 sumário
itens = [('01', 'Plataforma', 'Propósito, visão, missão, valores, posicionamento'), ('02', 'Personalidade', 'Arquétipo, tom de voz, manifesto, tagline'),
         ('03', 'Sistema verbal', 'Nomenclatura e vocabulário'), ('04', 'Públicos e personas', 'Mapa, 6 personas, jornadas, mensagens'),
         ('05', 'Arquitetura', 'Grupo e as quatro divisões'), ('06', 'Bastidores', 'Métodos usados e referências')]
P(f'''<div class="col" style="left:120px;top:170px"><div class="ey">Sumário</div><div class="h2" style="margin-top:24px">O que está<br>neste livro.</div>
<div class="p" style="margin-top:30px;max-width:620px">O manual de identidade traz símbolo, cor, letra e aplicações. Aqui está o porquê.</div>
<div style="margin-top:40px;width:640px;height:400px;background:url(../fotos-v2.1/slz-portugal.jpg) 50% 30%/150% auto;position:relative;border-radius:3px">
<div style="position:absolute;left:0;right:0;bottom:0;padding:16px 20px;background:linear-gradient(0deg,rgba(11,12,14,.85),transparent);font:500 19px/1.35 I">A pedra-chave já está nas portas de São Luís.<div class="mono" style="font-size:13px;opacity:.7;margin-top:6px">Centro Histórico · foto Prburley, CC BY 4.0</div></div></div></div>
<div class="col" style="left:860px;top:170px;width:940px">''' + ''.join(f'''<div style="display:grid;grid-template-columns:110px 1fr;padding:26px 0;border-top:1px solid rgba(239,234,225,.18)">
<div class="mono" style="color:{BRASS};padding-top:12px">{a}</div><div><div class="h3">{b}</div><div class="ps" style="margin-top:8px">{c}</div></div></div>''' for a, b, c in itens) + '</div>', sec='Sumário')

# 03 manifesto · copia SoftBank/Temasek: declaração serifada gigante, linha a linha
P(f'''{corte(30, 1420, 560, '#16181c')}<div class="col" style="left:120px;top:150px;width:1500px"><div class="ey">Manifesto</div>
<div style="margin-top:34px;font:400 58px/1.16 F;letter-spacing:-.02em">''' + ''.join(f'<div style="opacity:{1 if i in (0,4,6) else .55}">{l}</div>' for i, l in enumerate(MANIFESTO)) + '</div></div>', sec='01 · Plataforma')

# 04 propósito / visão / missão
P(f'''<div class="col" style="left:120px;top:150px;width:1680px"><div class="ey">Propósito</div><div class="h2" style="margin-top:22px;max-width:1500px">{PROPOSITO}</div></div>
<div class="col" style="left:120px;top:640px;width:1680px;display:grid;grid-template-columns:1fr 1fr;gap:80px">
<div><div class="rule"></div><div class="ey" style="margin-top:24px">Visão</div><div class="h3" style="margin-top:16px;font-size:38px">{VISAO}</div></div>
<div><div class="rule"></div><div class="ey" style="margin-top:24px">Missão</div><div class="h3" style="margin-top:16px;font-size:38px">{MISSAO}</div></div></div>''', 'l', '01 · Plataforma')

# 05 valores: cada valor = uma pedra do símbolo
def pedra(i, cor, s=10):
    return K(s, '#2a2c30', i, cor)
P(f'''<div class="col" style="left:120px;top:150px"><div class="ey">Valores</div><div class="h2" style="margin-top:22px">Cada pedra sustenta.</div></div>
<div class="col" style="left:120px;top:470px;width:1680px;display:grid;grid-template-columns:repeat(4,1fr);gap:40px">''' +
  ''.join(f'''<div style="border-top:1px solid rgba(239,234,225,.2);padding-top:30px">{pedra(i, BRASS, 9)}<div class="h3" style="margin-top:30px">{n}</div><div class="ps" style="margin-top:14px">{t}</div></div>''' for i, (n, t) in enumerate(VALORES)) + '</div>', sec='01 · Plataforma')

# 06 posicionamento (Neumeier · onlyness)
P(f'''{corte(40, -250, 160, BRASS, .18)}<div class="col" style="left:640px;top:170px;width:1160px"><div class="ey">Posicionamento · método "onlyness" (livro Zag)</div>
<div style="margin-top:30px;font:400 56px/1.18 F;letter-spacing:-.02em">{ONLYNESS}</div>
<div class="ps" style="margin-top:44px;max-width:900px">O quê: grupo de tecnologia. Como: constrói, opera e distribui no mesmo lugar. Para quem: empresas da região que querem crescer. Onde: Maranhão para o Brasil. Por quê importa: execução é o que falta. Quando: agora, com IA barata.</div></div>''', sec='01 · Plataforma')

# 07 arquétipo
a1, a2, at = ARQUETIPO
P(f'''<div class="col" style="left:120px;top:150px"><div class="ey">Arquétipo</div></div>
<div class="col" style="left:120px;top:250px;font:400 300px/.85 F;letter-spacing:-.02em">{a1}</div>
<div class="col" style="left:130px;top:560px;font:400 120px/1 F;letter-spacing:-.02em;color:{BRASS}" ><span class="it">com</span> {a2}</div>
<div class="col" style="left:1180px;top:770px;width:620px"><div class="p">{at}</div>
<div style="margin-top:22px;display:flex;gap:10px;flex-wrap:wrap"><span class="chip">ordem</span><span class="chip">responsabilidade</span><span class="chip">autoria</span><span class="chip">sobriedade</span></div></div>''', 'l', '02 · Personalidade')

# 08 tagline + pitch
P(f'''{corte(70, 960, -320, '#15171a')}<div class="col" style="left:120px;top:300px"><div class="ey">Tagline</div>
<div class="h1" style="margin-top:28px;font-size:200px">Estrutura<br>para o que <span class="it" style="color:{BRASS}">vem.</span></div>
<div class="rule" style="margin-top:70px;width:900px"></div><div class="ey" style="margin-top:26px">Pitch de 1 frase · método one-liner (StoryBrand)</div>
<div class="h3" style="margin-top:14px;max-width:1100px">{PITCH}</div></div>''', sec='02 · Personalidade')

# 09 tom de voz
P(f'''<div class="col" style="left:120px;top:140px"><div class="ey">Tom de voz</div><div class="h2" style="margin-top:20px">Fala como quem segura o arco.</div></div>
<div class="col" style="left:120px;top:400px;width:1680px">
<div style="display:grid;grid-template-columns:330px 1fr 1fr;gap:40px;padding-bottom:14px" class="mono"><span>Princípio</span><span style="color:#0E8C66">Faz</span><span style="color:#E8461E">Não faz</span></div>''' +
  ''.join(f'''<div style="display:grid;grid-template-columns:330px 1fr 1fr;gap:40px;padding:24px 0;border-top:1px solid rgba(11,12,14,.15)">
<div class="big">{p}</div><div style="font:400 26px/1.3 F">“{f}”</div><div style="font:400 26px/1.3 F;opacity:.45;text-decoration:line-through;text-decoration-thickness:1px">“{n}”</div></div>''' for p, f, n in TOM) + '</div>', 'l', '02 · Personalidade')

# 10 sistema verbal
P(f'''<div class="col" style="left:120px;top:140px"><div class="ey">Sistema verbal · nomenclatura</div></div>
<div class="col" style="left:120px;top:200px;width:1100px">''' + ''.join(f'''<div style="padding:18px 0;border-top:1px solid rgba(239,234,225,.18);display:grid;grid-template-columns:200px 1fr;gap:30px">
<div class="mono" style="color:{BRASS};padding-top:8px">{a}</div><div><div class="h3" style="font-size:36px">{b}</div><div class="ps" style="margin-top:8px">{c}</div></div></div>''' for a, b, c in NOMENCLATURA) + f'''</div>
<div class="col" style="left:1340px;top:210px;width:460px"><div class="mono" style="color:#5fd1a8">Usamos</div><div style="font:400 32px/1.35 F;margin-top:14px">{' · '.join(VOCAB_SIM)}</div>
<div class="mono" style="color:#ff7a57;margin-top:46px">Evitamos</div><div style="font:400 32px/1.35 F;margin-top:14px;opacity:.5;text-decoration:line-through;text-decoration-thickness:1px">{' · '.join(VOCAB_NAO)}</div></div>''', sec='03 · Sistema verbal')

# 11 mapa de públicos (v2.1: texto completo à esquerda, corpo 21 px; anéis só com nomes)
P(f'''<div class="col" style="left:120px;top:140px;width:700px"><div class="ey">Mapa de públicos</div><div class="h2" style="margin-top:20px">Quem precisa acreditar.</div>
<div style="margin-top:34px">''' + ''.join(f'<div style="border-top:1px solid rgba(239,234,225,.18);padding:16px 0"><div class="mono" style="color:{BRASS}">{n}</div><div class="ps" style="margin-top:6px">{t}</div></div>' for n, t in PUBLICOS) + '''</div></div>
<div class="col" style="left:930px;top:120px;width:840px;height:840px">''' +
  ''.join(f'<div style="position:absolute;left:{i*105}px;top:{i*105}px;width:{840-i*210}px;height:{840-i*210}px;border-radius:50%;border:1px solid rgba(239,234,225,{.18+i*.12});background:rgba(184,149,90,{.03+i*.05})"></div>' for i in range(4)) +
  f'<div style="position:absolute;left:345px;top:345px">{K(6.25, LIME)}</div>' +
  ''.join(f'<div class="mono" style="position:absolute;left:0;right:0;top:{y}px;text-align:center;color:{BRASS if j==0 else LIME};opacity:{1 if j==0 else .8}">{n}</div>' for j, (n, y) in enumerate(zip([p[0] for p in PUBLICOS], [520, 630, 735, 40]))) + '</div>', sec='04 · Públicos')

# 12-17 personas (v2.1: "persona ilustrativa", corpo 20-21 px)
cores_p = ['#2E4BFF', '#E8461E', '#F0A202', BRASS, '#0E8C66', STONE]
for i, p in enumerate(PERSONAS):
    c = cores_p[i]
    ini = ''.join(w[0] for w in p['nome'].split()[:2])
    tc = INK if c in ('#F0A202', BRASS, STONE) else LIME
    P(f'''<div class="col" style="left:0;top:0;width:620px;height:1080px;background:{c}"></div>
<div class="col" style="left:-40px;top:300px;font:400 520px/.8 F;letter-spacing:-.02em;color:rgba(0,0,0,.16)">{ini}</div>
<div class="col" style="left:70px;top:120px;width:500px;color:{tc}"><div class="mono">Persona {i+1:02d} · {p['pub']}</div>
<div style="margin-top:16px;display:inline-block;padding:6px 12px;border:1px solid currentColor;font:500 14px 'JetBrains Mono';letter-spacing:.14em">PERSONA ILUSTRATIVA</div>
<div class="h2" style="margin-top:24px;font-size:80px">{p['nome']}</div><div class="big" style="margin-top:16px">{p['idade']} anos · {p['cargo']}</div>
<div style="position:absolute;top:660px;width:480px"><div class="mono" style="opacity:.8">Mensagem-chave</div><div class="h3" style="margin-top:12px;font-size:38px">“{p['msg']}”</div></div></div>
<div class="col" style="left:690px;top:120px;width:1110px;display:grid;grid-template-columns:1fr 1fr;gap:22px 50px">''' +
      ''.join(f'<div style="border-top:1px solid rgba(239,234,225,.18);padding-top:12px"><div class="mono" style="color:{BRASS};font-size:15px">{k}</div><div class="ps" style="margin-top:6px;font-size:20px;opacity:.88">{p[v]}</div></div>' for k, v in [('Rotina', 'rotina'), ('Dores', 'dores'), ('Desejos', 'desejos'), ('Objeções', 'objecoes'), ('O que faz confiar', 'confia'), ('Onde está · canais', 'canais')]) +
      f'''</div><div class="col" style="left:690px;top:700px;width:1110px"><div class="mono" style="color:{BRASS};font-size:15px">Jornada</div><div style="display:grid;grid-template-columns:repeat(5,1fr);gap:16px;margin-top:14px">''' +
      ''.join(f'<div style="border-top:3px solid {c};padding-top:12px"><div class="mono" style="font-size:14px;opacity:.65">{["Descobre","Considera","Conversa","Experimenta","Defende"][j]}</div><div class="ps" style="font-size:20px;margin-top:6px">{st}</div></div>' for j, st in enumerate(p['jornada'])) + '</div></div>', 's', '04 · Personas')

# 18 mensagens-chave
P(f'''<div class="col" style="left:120px;top:140px"><div class="ey">Mensagem-chave por público</div><div class="h2" style="margin-top:20px">Uma frase para cada um.</div></div>
<div class="col" style="right:120px;top:150px"><span class="il" style="color:#7a5f30">Personas ilustrativas</span></div>
<div class="col" style="left:120px;top:380px;width:1680px;display:grid;grid-template-columns:repeat(3,1fr);gap:30px">''' +
  ''.join(f'''<div style="background:#fff;padding:34px;border-radius:4px;min-height:270px;border-top:6px solid {cores_p[i]}"><div class="mono" style="opacity:.75">{p['pub']}</div><div style="font:400 34px/1.15 F;margin-top:18px">“{p['msg']}”</div></div>''' for i, p in enumerate(PERSONAS)) + '</div>', 'l', '04 · Públicos')

# 19 prova persona → decisão
P(f'''<div class="col" style="left:120px;top:140px;width:600px"><div class="ey">Regra persona.md</div><div class="h2" style="margin-top:20px">Cada decisão serve a alguém.</div>
<div class="p" style="margin-top:28px">Teste: "essa pessoa, olhando no celular, confiaria nisso?". Ao lado, a prova de cada escolha.</div></div>
<div class="col" style="left:860px;top:140px;width:940px">''' + ''.join(f'''<div style="padding:26px 0;border-top:1px solid rgba(239,234,225,.18)"><div class="h3" style="font-size:34px">{a}</div><div class="ps" style="margin-top:10px">{b}</div></div>''' for a, b in PROVA) + '</div>', sec='04 · Públicos')

# 20 arquitetura (Aaker · espectro)
esp = [('Branded house', 'Google, Virgin', .35), ('Sub-marcas', 'Apple iPhone', 1), ('Endossada', 'Marriott Courtyard', .6), ('House of brands', 'P&G', .35)]
P(f'''<div class="col" style="left:120px;top:140px;width:760px"><div class="ey">Arquitetura de marca · método do espectro (livro Brand Leadership)</div><div class="h2" style="margin-top:20px">Sub-marcas fortes, uma chave só.</div>
<div class="p" style="margin-top:28px">As divisões usam a marca-mãe com modificador (Al Kántara Labs). Produtos e empresas investidas mantêm nome próprio com endosso. A Barzakh é a exceção escrita: estúdio com nome próprio e endosso do grupo.</div></div>
<div class="col" style="left:120px;top:640px;width:1680px;display:grid;grid-template-columns:repeat(4,1fr);gap:0">''' +
  ''.join(f'''<div style="border-top:{'4px solid ' + BRASS if o == 1 else '1px solid rgba(239,234,225,.25)'};padding-top:24px;opacity:{o}"><div class="h3" style="font-size:40px">{a}</div><div class="mono" style="margin-top:10px;opacity:.8">{b}</div>{'<div class="ey" style="margin-top:20px">Labs, Media, Ventures</div>' if o == 1 else ('<div class="ey" style="margin-top:20px;opacity:.9">Barzakh, produtos e investidas</div>' if o == .6 else '')}</div>''' for a, b, o in esp) + '</div>', sec='05 · Arquitetura')

# 21 árvore
P(f'''<div class="col" style="left:120px;top:140px"><div class="ey">Árvore de marcas</div></div>
<div class="col" style="left:760px;top:170px">{logo('vertical','positivo',250)}</div>
<svg class="col" style="left:0;top:0" width="1920" height="1080"><g stroke="{INK}" stroke-opacity=".3"><line x1="960" y1="470" x2="960" y2="530"/><line x1="330" y1="530" x2="1590" y2="530"/>''' + ''.join(f'<line x1="{330+i*420}" y1="530" x2="{330+i*420}" y2="580"/>' for i in range(4)) + '''</g></svg>
<div class="col" style="left:120px;top:600px;width:1680px;display:grid;grid-template-columns:repeat(4,1fr);gap:0">''' +
  ''.join(f'''<div style="text-align:center;padding:0 20px"><div style="display:inline-block;height:76px">{divlogo(n,'positivo',58)}</div><div class="mono" style="margin-top:26px;color:{c if n != 'Media' else '#a86f00'}">{t}</div><div class="ps" style="margin-top:12px">{pr if n != 'Barzakh' else 'Única divisão com nome próprio · endosso sempre junto'}</div></div>''' for n, c, t, pr in DIV) + '</div>', 'l', '05 · Arquitetura')

# 22-25 divisões (v2.1: Barzakh com capa própria · placa aprovada pelo Lindson em 16/11)
for i, (n, c, t, pr) in enumerate(DIV):
    txt = INK if n == 'Media' else LIME
    if n == 'Barzakh':
        P(f'''<div class="col" style="left:0;top:0;width:960px;height:1080px;background:{c}"></div>
<div class="col" style="left:960px;top:0;width:960px;height:1080px;background:#2a2a2b url(../../../marca-lindson/projeto-designer/v3/marca/aprovado/placa-arco-monolito-ouro.png) center/cover"></div>
<div class="col" style="left:120px;top:150px;color:{LIME}"><div class="mono">Divisão 02 · {t}</div></div>
<div class="col" style="left:120px;top:250px;width:760px;color:{LIME}"><div class="h1" style="font-size:190px">Barzakh</div>
<div class="mono" style="margin-top:22px;font-size:20px;letter-spacing:.2em">um estúdio Al Kántara</div>
<div class="h3" style="margin-top:44px;font-size:44px">Damos forma e voz.</div>
<div class="ps" style="margin-top:26px;font-size:22px;opacity:.95;max-width:700px">A única divisão com nome próprio. Na arquitetura do grupo ela usa o laranja {c} e a pedra do topo do símbolo. Dentro da própria marca, vale o manual da Barzakh: escuro, ouro metálico, arco e concreto.</div>
<div style="margin-top:34px;display:flex;gap:14px;flex-wrap:wrap"><span class="chip" style="color:{LIME}">Regra: Barzakh · um estúdio Al Kántara</span><span class="chip" style="color:{LIME}">Endosso sempre junto</span></div></div>
<div class="col" style="left:990px;bottom:60px;font:500 14px 'JetBrains Mono';letter-spacing:.14em;color:{LIME};opacity:.7">PLACA APROVADA · ARCO GRAFITE, MONOLITO EM OURO ESCOVADO</div>''', '', '05 · Barzakh')
        continue
    P(f'''<div class="col" style="left:0;top:0;width:1920px;height:1080px;background:{c}"></div>
<div class="col" style="left:860px;top:-200px">{K(62, 'rgba(0,0,0,.16)', i, txt)}</div>
<div class="col" style="left:120px;top:150px;color:{txt}">{divlogo(n, 'positivo' if n == 'Media' else 'negativo', 70)}</div>
<div class="col" style="left:120px;bottom:150px;width:820px;color:{txt}"><div class="mono">Divisão {i+1:02d} · {t}</div>
<div class="h1" style="font-size:200px;margin-top:20px">{n}</div><div class="h3" style="margin-top:30px;font-size:44px">{['Construímos a tecnologia.', 'Damos forma e voz.', 'Levamos longe.', 'Provamos na prática.'][i]}</div>
<div class="ps" style="margin-top:22px;font-size:22px;opacity:.95">{pr}. Cor da divisão: {c} · a pedra {['da haste', 'do topo', 'do meio', 'da base'][i]} do símbolo.</div></div>''', '', f'05 · {n}')

# 26 métodos usados (v2.1: no lugar de "Quem pensou junto"; nenhum autor aparece como participante)
P(f'''<div class="col" style="left:120px;top:140px;width:1680px;display:flex;justify-content:space-between;align-items:flex-end"><div><div class="ey">Bastidores</div><div class="h2" style="margin-top:20px">Métodos usados.</div></div>
<div class="ps" style="max-width:640px">Livros e processos que guiaram as decisões. São ferramentas de trabalho: nenhum autor participou deste projeto.</div></div>
<div class="col" style="left:120px;top:400px;width:1680px;display:grid;grid-template-columns:repeat(4,1fr);gap:34px 40px">''' +
  ''.join(f'<div style="border-top:1px solid rgba(239,234,225,.2);padding-top:18px"><div class="mono" style="color:{BRASS};font-size:14px">{c}</div><div class="big" style="margin-top:8px">{a}</div><div class="ps" style="margin-top:10px;font-size:20px">{b}</div></div>' for a, b, c in METODOS) + '</div>', sec='06 · Bastidores')

# 27 contracapa
P(f'''<div class="col" style="left:744px;top:250px">{K(18, BRASS)}</div><div class="col" style="left:0;right:0;top:760px;text-align:center"><div class="h3">Estrutura para o que vem.</div>
<div class="mono" style="margin-top:22px;opacity:.5">Al Kántara Group · São Luís, Maranhão · Brand Book v2.1</div></div>''', sec='none')
