# Páginas do Plano de Autoridade CEO v1 (executado dentro de gerar.py)
FOTO = globals().get('FOTO_CAPA')  # caminho file:// de uma foto do Lindson (opcional)

def tile(i, fmt, linha, gancho, w=300):
    # miniatura de post da grade nova: alterna Tinta / Calcário / Latão (xadrez), 1 ideia por peça
    estilos = [(INK, LIME, BRASS), (LIME, INK, '#8a6a35'), (GRAPH, LIME, BRASS)]
    bg, fg, ac = estilos[[0, 1, 2, 1, 0, 1, 2, 1, 0][i]]
    pal = gancho.split()
    t = ' '.join(pal[:-1]) + f' <span style="font-style:italic;color:{ac}">{pal[-1]}</span>'
    k = corte(w * .028, w * .62, w * .55, ac, .22) if i in (0, 4, 8) else ''
    return (f'<div style="width:{w}px;height:{w*1.25}px;background:{bg};color:{fg};position:relative;overflow:hidden;box-shadow:0 18px 40px -18px rgba(0,0,0,.6)">{k}'
            f'<div style="position:absolute;left:{w*.08}px;top:{w*.08}px;font:500 {w*.034}px M;letter-spacing:.14em;text-transform:uppercase;color:{ac}">{i+1:02d} · {fmt} · {linha}</div>'
            f'<div style="position:absolute;left:{w*.08}px;right:{w*.08}px;bottom:{w*.1}px;font:400 {w*.098}px/1.02 F">{t}</div></div>')

# 01 CAPA ---------------------------------------------------------------------------------
foto = (f'<div class="col" style="right:0;top:0;width:900px;height:1080px;background:url({FOTO}) center 20%/cover"></div>'
        f'<div class="col" style="right:0;top:0;width:900px;height:1080px;background:linear-gradient(90deg,{INK} 0%,rgba(11,12,14,.35) 40%,rgba(11,12,14,0) 70%)"></div>') if FOTO else corte(52, 1020, -110, '#16181b', 1, 1, BRASS)
P(f'''{foto}
<div class="col" style="left:120px;top:120px">{logo('horizontal', 'negativo', 46)}</div>
<div class="col ey" style="left:120px;top:330px">Plano de comunicação de autoridade · v1</div>
<div class="col h1" style="left:112px;top:380px;font-size:190px">Lindson<br>Almeida<span class="it">.</span></div>
<div class="col" style="left:120px;top:800px;font:400 44px/1.2 F">Fundador e CEO do <span class="it">Al Kántara Group</span></div>
<div class="col ps" style="left:120px;top:870px;max-width:760px">Posicionamento, narrativa, auditoria, perfil novo, linhas editoriais, kit para vereadores e plano de 90 dias.</div>
''', '', 'none')

# 02 TESE + SUMÁRIO ----------------------------------------------------------------------
sumario = [('01', 'Posicionamento e arquitetura', '03'), ('02', 'Prova de autoridade', '08'), ('03', 'Narrativa, manifesto, one-liner', '09'),
           ('04', 'Auditoria dos pontos de contato', '12'), ('05', 'O novo perfil', '14'), ('06', 'Linhas e calendário', '19'),
           ('07', 'Receber os vereadores', '21'), ('08', 'Plano de 90 dias e metas', '23'), ('09', 'Time, referências e decisões', '25')]
s = ''.join(f'<div style="display:flex;gap:28px;padding:16px 0;border-top:1px solid rgba(11,12,14,.18)"><span class="mono" style="color:#8a6a35;width:40px">{a}</span><span style="font:400 30px F;flex:1">{b}</span><span class="mono">{c}</span></div>' for a, b, c in sumario)
P(f'''<div class="col ey" style="left:120px;top:170px">A tese em uma frase</div>
<div class="col h2" style="left:120px;top:220px;width:820px">Sair de “o cara que faz <span class="it">Instagram</span>” para “o dono do grupo que pensa a comunicação de quem <span class="it">lidera</span>”.</div>
<div class="col ps" style="left:120px;top:800px;width:760px">Neste momento chegam muitos vereadores. O plano usa essa onda sem deixar que ela defina quem ele é: a política vira uma frente entre quatro, e o Lindson aparece como dono de um grupo com método, sistemas e padrão.</div>
<div class="col" style="left:1060px;top:200px;width:740px">{s}</div>''', 'l', 'Sumário')

# 03 PERSONAS -----------------------------------------------------------------------------
cards = ''.join(f'<div style="flex:1;border-top:2px solid {BRASS};padding-top:26px"><div class="mono" style="color:{BRASS}">Persona 0{i+1}</div><div class="h3" style="margin:18px 0 22px">{n}</div><div class="ps">{t}</div></div>' for i, (n, t) in enumerate(PERSONAS))
P(f'''<div class="col ey" style="left:120px;top:170px">01 · Posicionamento</div>
<div class="col h2" style="left:120px;top:215px">Quem precisa <span class="it">acreditar</span> nele.</div>
<div class="col" style="left:120px;right:120px;top:470px;display:flex;gap:70px">{cards}</div>
<div class="col q" style="left:120px;bottom:110px;font-size:28px;opacity:.8">Pergunta-teste de toda peça: essa pessoa contrataria o dono deste perfil para pensar a comunicação dela?</div>''', '', 'Personas')

# 04 POSICIONAMENTO -----------------------------------------------------------------------
tit = ''.join(f'<tr><td style="width:300px" class="mono">{a}</td><td style="font:400 30px F">{c}</td></tr>' for a, b, c in TITULOS)
P(f'''{corte(30, 1380, 560, '#16181b', 1)}
<div class="col ey" style="left:120px;top:170px">01 · Posicionamento</div>
<div class="col h2" style="left:120px;top:215px;width:1500px">Um nome, uma casa, <span class="it">um título por público</span>.</div>
<div class="col p" style="left:120px;top:440px;width:760px">Lindson Almeida é o fundador e CEO do Al Kántara Group e estrategista de comunicação. Ele não vende post: decide, com quem lidera, o que as pessoas vão lembrar dela, e o grupo executa com padrão.</div>
<div class="col" style="left:120px;top:640px;width:1100px"><table class="tb"><tr><th>Público</th><th>Como ele se apresenta</th></tr>{tit}</table></div>
<div class="col mono" style="left:120px;bottom:100px;opacity:.6">Maquiavel: o político compra a pessoa; o empresário compra a estrutura. Por isso o título muda e o nome não.</div>''', '', 'Posicionamento')

# 05 ARQUITETURA --------------------------------------------------------------------------
div = [('Labs', 'Sistemas e IA', 'Central de Comando · VEKTOR · Dublê · robô SDR'), ('Barzakh', 'Marca e design', 'identidade, sites, brand book'),
       ('Media', 'Canais próprios', 'Passaporte da Bíblia · Raposa e Leão'), ('Ventures', 'Negócios próprios', 'Orégano Turbo · Estado Próprio')]
dv = ''.join(f'<div style="flex:1;background:{GRAPH};padding:28px;border-top:6px solid {DIVC[n]}"><div class="h4">{n}</div><div class="mono" style="margin:12px 0 18px;opacity:.7">{a}</div><div class="pm">{b}</div></div>' for n, a, b in div)
P(f'''<div class="col ey" style="left:120px;top:170px">01 · Arquitetura de marca</div>
<div class="col h2" style="left:120px;top:215px">Pessoa, grupo e <span class="it">frentes</span>.</div>
<div class="col" style="left:120px;right:120px;top:400px;display:flex;align-items:center;gap:40px;padding:30px 0;border-top:1px solid rgba(239,234,225,.2)">
 <div style="width:420px"><div class="mono" style="color:{BRASS}">Nível 1 · a pessoa</div><div class="h3" style="margin-top:10px">Lindson Almeida</div><div class="ps" style="margin-top:8px">fundador e CEO · a autoridade e a voz</div></div>
 <div style="width:420px"><div class="mono" style="color:{BRASS}">Nível 2 · a casa</div><div style="margin-top:16px">{logo('horizontal', 'negativo', 40)}</div><div class="ps" style="margin-top:12px">estrutura, padrão, contratos</div></div>
 <div style="flex:1" class="box"><div class="mono" style="color:{BRASS}">Prática pessoal · fora da vitrine do grupo</div><div class="h4" style="margin-top:10px">Lindson Almeida · Estratégia Política</div><div class="pm" style="margin-top:8px">Mandatos e pré-campanha. Dossiê e painel pela Labs, peças pela Barzakh. Sem partido, um mandato por cidade.</div></div></div>
<div class="col" style="left:120px;right:120px;top:700px;display:flex;gap:24px">{dv}</div>''', '', 'Arquitetura')

# 06 DE → PARA ----------------------------------------------------------------------------
dp = ''.join(f'<tr><td style="width:46%;opacity:.6;text-decoration:line-through;text-decoration-color:rgba(11,12,14,.35)">{a}</td><td style="font:400 25px/1.3 F">{b}</td></tr>' for a, b in DE_PARA)
P(f'''<div class="col ey" style="left:120px;top:170px">01 · O que muda na percepção</div>
<div class="col h2" style="left:120px;top:215px">De prestador a <span class="it">dono</span>.</div>
<div class="col" style="left:120px;right:120px;top:410px"><table class="tb"><tr><th>Hoje</th><th>A partir de dezembro</th></tr>{dp}</table></div>''', 'l', 'Percepção')

# 07 FRASE DE PODER (Maquiavel) ------------------------------------------------------------
P(f'''{corte(44, -140, 120, '#121316', 1)}
<div class="col ey" style="left:780px;top:260px">Maquiavel · O Príncipe, cap. XVIII</div>
<div class="col q" style="left:780px;top:320px;width:1000px;font-size:62px;line-height:1.15">“Todos veem o que você <span style="color:{BRASS}">parece</span>; poucos sentem o que você <span style="color:{BRASS}">é</span>.”</div>
<div class="col ps" style="left:780px;top:640px;width:900px">A aparência abre a porta; só a entrega a mantém aberta. O dossiê é o “parecer” com dado por baixo: nunca prometer o que ele não mostra. (Cap. XXI: nada faz estimar tanto quanto grandes obras e exemplos raros. Um case-vitrine vale mais que cem posts.)</div>
<div class="col mono" style="left:780px;top:880px;opacity:.55">Citação do texto; a aplicação ao plano é interpretação da equipe.</div>''', 's', 'Princípio')

# 08 PROVA --------------------------------------------------------------------------------
pv = ''.join(f'<div style="border-top:1px solid rgba(239,234,225,.22);padding-top:22px"><div style="font:400 120px/.9 F;color:{BRASS}">{n}</div><div class="h4" style="margin:12px 0 10px">{t}</div><div class="mono" style="font-size:12px;line-height:1.6;opacity:.6;text-transform:none;letter-spacing:.04em">{f}</div></div>' for n, t, f in PROVAS)
P(f'''<div class="col ey" style="left:120px;top:170px">02 · Prova de autoridade</div>
<div class="col h2" style="left:120px;top:215px">Só o que <span class="it">dá para mostrar</span>.</div>
<div class="col" style="left:120px;right:120px;top:420px;display:grid;grid-template-columns:repeat(3,1fr);gap:46px 70px">{pv}</div>''', '', 'Prova')

# 09 NARRATIVA ----------------------------------------------------------------------------
nr = ''.join(f'<div style="display:flex;gap:40px;padding:20px 0;border-top:1px solid rgba(11,12,14,.18)"><div class="mono" style="width:230px;color:#8a6a35;padding-top:6px">{a}</div><div style="flex:1;font:400 27px/1.35 F">{b}</div></div>' for a, b in NARRATIVA)
P(f'''<div class="col ey" style="left:120px;top:170px">03 · Narrativa do fundador</div>
<div class="col h2" style="left:120px;top:215px;width:560px">Da rua ao <span class="it">grupo</span>.</div>
<div class="col ps" style="left:120px;top:470px;width:520px">Estrutura de história (Story Chief): origem, virada, construção, hoje e o compromisso. O herói da história continua sendo o cliente; o Lindson é o guia que já passou pelo caminho.</div>
<div class="col" style="left:760px;right:120px;top:190px">{nr}</div>''', 'l', 'Narrativa')

# 10 MANIFESTO ----------------------------------------------------------------------------
mf = '<br>'.join(f'<span style="color:{BRASS};font-style:italic">{l}</span>' if i in (3, 5) else l for i, l in enumerate(MANIFESTO))
P(f'''{corte(40, 1300, 300, '#131416', 1, 1, '#1d1f23')}
<div class="col ey" style="left:120px;top:150px">03 · Manifesto · para Reel de 45 s e para a home do site</div>
<div class="col" style="left:120px;top:220px;font:400 54px/1.28 F;width:1300px">{mf}</div>''', '', 'Manifesto')

# 11 ONE-LINER ----------------------------------------------------------------------------
P(f'''<div class="col ey" style="left:120px;top:170px">03 · One-liner (StoryBrand)</div>
<div class="col h2" style="left:120px;top:240px;width:1600px;font-size:76px">“Quem lidera precisa ser lembrado pelo que <span class="it">entrega</span>. Eu construo essa percepção com método: posicionamento, narrativa e execução, do negócio ao mandato.”</div>
<div class="col" style="left:120px;right:120px;top:700px;display:flex;gap:60px">
 <div style="flex:1;border-top:2px solid #8a6a35;padding-top:20px"><div class="mono" style="color:#8a6a35">Problema</div><div class="ps" style="margin-top:10px">quem trabalha bem e não é lembrado</div></div>
 <div style="flex:1;border-top:2px solid #8a6a35;padding-top:20px"><div class="mono" style="color:#8a6a35">Solução</div><div class="ps" style="margin-top:10px">método em 3 passos, executado pelo grupo</div></div>
 <div style="flex:1;border-top:2px solid #8a6a35;padding-top:20px"><div class="mono" style="color:#8a6a35">Resultado (sem promessa)</div><div class="ps" style="margin-top:10px">ser lembrado pelo que entrega</div></div>
 <div style="flex:1;border-top:2px solid #8a6a35;padding-top:20px"><div class="mono" style="color:#8a6a35">Assinatura do grupo</div><div class="ps" style="margin-top:10px">Estrutura para o que vem.</div></div></div>''', 'b', 'One-liner')

# 12-14 AUDITORIA ---------------------------------------------------------------------------
for k, (a, b) in enumerate([(0, 4), (4, 8)]):
    rows = ''.join(f'<tr><td style="width:300px;font:400 30px/1.2 F;padding-top:22px;padding-bottom:22px">{n}</td><td style="width:42%;opacity:.8;padding-top:22px;padding-bottom:22px">{x}</td><td style="padding-top:22px;padding-bottom:22px">{y}</td></tr>' for n, x, y in AUDITORIA[a:b])
    cls = ['', 'l'][k]
    P(f'''<div class="col ey" style="left:120px;top:170px">04 · Auditoria · {k+1}/2</div>
<div class="col h2" style="left:120px;top:215px">{['O que <span class="it">derruba</span> hoje.', 'Os detalhes que <span class="it">assinam</span>.'][k]}</div>
<div class="col" style="left:120px;right:120px;top:420px"><table class="tb"><tr><th>Ponto de contato</th><th>O que derruba a autoridade</th><th>O que fazer</th></tr>{rows}</table></div>''', cls, 'Auditoria')

# 15 BIO + DESTAQUES (celular) --------------------------------------------------------------
bio = BIO_IG[0][2].replace('\n', '<br>')
dest = ''.join(f'<div style="text-align:center;width:74px"><div style="width:62px;height:62px;margin:0 auto;border-radius:50%;border:1.5px solid {BRASS};display:flex;align-items:center;justify-content:center;background:{INK}">{K(1.4, BRASS)}</div><div style="font:500 12px I;margin-top:6px">{n}</div></div>' for n, _ in DESTAQUES)
cel = f'''<div style="width:470px;height:900px;border-radius:56px;background:#050506;padding:16px;box-shadow:0 40px 90px -30px rgba(0,0,0,.8)">
<div style="width:100%;height:100%;border-radius:42px;background:{INK};overflow:hidden;padding:56px 26px 0;color:{LIME}">
<div style="font:600 19px I">lindsonalmeida_</div>
<div style="display:flex;align-items:center;gap:26px;margin-top:22px"><div style="width:104px;height:104px;border-radius:50%;background:{GRAPH};border:2px solid {BRASS};display:flex;align-items:center;justify-content:center;font:500 11px M;color:{BRASS};text-align:center;line-height:1.3">FOTO NOVA<br>(p. 18)</div>
<div style="font:500 14px I;opacity:.7">foto de perfil = lote CEO</div></div>
<div style="font:600 16px I;margin-top:18px">{BIO_IG[0][1]}</div>
<div style="font:500 15px/1.45 I;margin-top:6px;opacity:.92">{bio}</div>
<div style="font:500 14px I;margin-top:6px;color:#9fb8ff">lindsonalmeida.pages.dev</div>
<div style="display:flex;gap:6px;margin-top:22px;flex-wrap:wrap">{dest}</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3px;margin-top:20px">{''.join(f'<div style="transform:scale(1);height:178px;overflow:hidden">{tile(i, *NOVE[i][:3], w=136)}</div>' for i in range(3))}</div></div></div>'''
dl = ''.join(f'<tr><td style="width:180px;font:400 26px F">{n}</td><td>{t}</td></tr>' for n, t in DESTAQUES)
P(f'''<div class="col" style="left:1260px;top:90px">{cel}</div>
<div class="col ey" style="left:120px;top:170px">05 · Instagram @lindsonalmeida_</div>
<div class="col h2" style="left:120px;top:215px;width:1000px">A bio de um <span class="it">fundador</span>.</div>
<div class="col" style="left:120px;top:400px;width:500px"><div class="mono" style="color:{BRASS}">Bio A · recomendada</div><div style="font:400 25px/1.4 F;margin-top:12px">{bio}</div>
<div class="mono" style="color:{BRASS};margin-top:30px">Bio B</div><div class="ps" style="margin-top:10px">{BIO_IG[1][2].replace(chr(10), '<br>')}</div>
<div class="mono" style="color:{BRASS};margin-top:30px">Nome (campo buscável)</div><div class="ps" style="margin-top:10px">{BIO_IG[0][1]}</div></div>
<div class="col" style="left:680px;top:400px;width:500px"><table class="tb"><tr><th>Destaques</th><th>O que entra</th></tr>{dl}</table><div class="mono" style="margin-top:20px;opacity:.55;line-height:1.6">Capas: símbolo latão sobre Tinta, iguais.<br>Sem preço na bio.</div></div>''', '', 'Perfil')

# 16 GRADE 9 -----------------------------------------------------------------------------
grid = ''.join(tile(i, *NOVE[i][:3], w=232) for i in range(9))
lista = ''.join(f'<tr><td style="width:40px" class="mono">{i+1:02d}</td><td style="width:120px">{f}</td><td>{d}</td></tr>' for i, (f, l, g, d) in enumerate(NOVE))
P(f'''<div class="col" style="left:120px;top:150px;display:grid;grid-template-columns:repeat(3,232px);gap:6px">{grid}</div>
<div class="col ey" style="left:900px;top:170px">05 · Os 9 primeiros posts</div>
<div class="col h3" style="left:900px;top:215px;width:880px">Xadrez de Tinta, Calcário e Grafite; Reel, post e carrossel <span class="it">alternados</span>.</div>
<div class="col" style="left:900px;top:400px;width:880px"><table class="tb"><tr><th>#</th><th>Formato</th><th>O que mostra</th></tr>{lista}</table>
<div class="mono" style="margin-top:18px;opacity:.6">Fixar 9, 3 e 1 · Reels gravados com a voz dele · prévia de composição, não arte final</div></div>''', 'l', 'Grade')

# 17 LINKEDIN ----------------------------------------------------------------------------
P(f'''<div class="col" style="left:900px;top:150px;width:900px;background:#fff;color:#191919;box-shadow:0 30px 70px -30px rgba(0,0,0,.7)">
<div style="height:200px;background:{INK};position:relative;overflow:hidden">{corte(14, 560, -40, '#1d1f23', 1, 1, BRASS)}<div style="position:absolute;left:40px;top:70px;font:400 40px F;color:{LIME}">Estrutura para o que <span style="font-style:italic;color:{BRASS}">vem.</span></div></div>
<div style="padding:0 40px 36px"><div style="width:150px;height:150px;border-radius:50%;background:{GRAPH};border:5px solid #fff;margin-top:-75px;display:flex;align-items:center;justify-content:center;font:500 12px M;color:{BRASS}">FOTO 02</div>
<div style="font:600 32px I;margin-top:14px">Lindson Almeida</div>
<div style="font:500 19px/1.4 I;margin-top:6px">{LINKEDIN_TIT}</div>
<div style="font:500 16px I;color:#666;margin-top:8px">São Luís, Maranhão · Al Kántara Group</div></div></div>
<div class="col ey" style="left:120px;top:170px">05 · LinkedIn</div>
<div class="col h2" style="left:120px;top:215px;width:700px">O perfil que o <span class="it">empresário</span> confere.</div>
<div class="col ps" style="left:120px;top:440px;width:700px">{LINKEDIN_SOBRE}</div>
<div class="col mono" style="left:120px;bottom:110px;width:700px;line-height:1.7;opacity:.65">URL: /in/lindsonalmeida · página da empresa Al Kántara Group · 2 textos por semana (linhas Estratégia, Grupo e Visão) · datas de experiência: o Lindson preenche</div>
<div class="col mono" style="left:900px;top:720px;width:900px;line-height:1.7;opacity:.65">Substitui a proposta de 16/11 (“Designer de marcas · Lindson Almeida Studio”), que reduzia o cargo.</div>''', '', 'LinkedIn')

# 18 PADRÃO VISUAL -------------------------------------------------------------------------
cores = ''.join(f'<div style="flex:{int(p[:2]) if p[:2].isdigit() else 5}"><div style="height:150px;background:{h};border:1px solid rgba(239,234,225,.15)"></div><div class="mono" style="margin-top:12px">{n} · {p}</div><div class="mono" style="opacity:.5;margin-top:4px">{h}</div></div>' for n, h, p in VISUAL_CORES)
comp = ''.join(f'<div style="flex:1;border-top:2px solid {BRASS};padding-top:16px"><div class="h4" style="font-size:26px">{n}</div><div class="pm" style="margin-top:10px">{t}</div></div>' for n, t in COMPOSICOES)
nun = ' · '.join(NUNCA)
P(f'''<div class="col ey" style="left:120px;top:170px">05 · Padrão visual CEO premium</div>
<div class="col h2" style="left:120px;top:215px">Al Kántara, com <span class="it">vida</span>.</div>
<div class="col" style="left:120px;right:120px;top:390px;display:flex;gap:16px">{cores}</div>
<div class="col" style="left:120px;right:120px;top:600px;display:flex;gap:40px">{comp}</div>
<div class="col" style="left:120px;right:120px;top:840px"><div class="mono" style="color:{BRASS}">Tipografia</div><div class="ps" style="margin-top:8px">Fraunces 600 grande (2ª linha em itálico latão) · Inter Tight no texto · JetBrains Mono nos rótulos. Nunca serifa fina e pequena.</div>
<div class="mono" style="color:{BRASS};margin-top:20px">Nunca</div><div class="pm" style="margin-top:8px">{nun}</div></div>''', '', 'Visual')

# 19 FOTOS ---------------------------------------------------------------------------------
ft = ''.join(f'<div style="border-top:1px solid rgba(11,12,14,.2);padding-top:14px"><div class="mono" style="color:#8a6a35">{i+1:02d} · {n}</div><div class="pm" style="margin-top:8px">{t}</div></div>' for i, (n, t) in enumerate(FOTOS))
P(f'''<div class="col ey" style="left:120px;top:170px">05 · Lote de 8 fotos de CEO · Gemini</div>
<div class="col h3" style="left:120px;top:215px;width:1600px">Todas as fotos atuais já foram usadas. O perfil novo começa por <span class="it">uma sessão nova</span>.</div>
<div class="col" style="left:120px;right:120px;top:380px;display:grid;grid-template-columns:repeat(4,1fr);gap:30px 40px">{ft}</div>
<div class="col fill" style="left:120px;right:120px;top:800px"><div class="mono" style="color:#8a6a35">Bloco base (colar junto de cada cena, com 1 a 3 fotos do rosto anexadas)</div><div class="pm" style="margin-top:10px">{FOTO_BASE}</div></div>''', 'l', 'Foto')

# 20 LINHAS --------------------------------------------------------------------------------
ln = ''.join(f'<div style="flex:1;background:{GRAPH};padding:26px"><div style="font:400 72px/.9 F;color:{BRASS}">{p}</div><div class="h4" style="margin:14px 0 6px">{n}</div><div class="mono" style="opacity:.6;font-size:12px">{o} · {f}</div><div style="margin-top:18px">' + ''.join(f'<div class="pm" style="padding:8px 0;border-top:1px solid rgba(239,234,225,.15)">{x}</div>' for x in pts) + '</div></div>' for n, p, o, f, pts in LINHAS)
P(f'''<div class="col ey" style="left:120px;top:170px">06 · Linhas editoriais de CEO</div>
<div class="col h2" style="left:120px;top:215px">Cinco linhas. A política é <span class="it">uma</span>.</div>
<div class="col" style="left:120px;right:120px;top:400px;display:flex;gap:18px">{ln}</div>''', '', 'Linhas')

# 21 CALENDÁRIO ----------------------------------------------------------------------------
cor = {'Reel': BRASS, 'Post': LIME, 'Carrossel': '#8E8A82', 'Stories': '#3a3d43'}
cl = ''
for d, t in enumerate(CAL):
    f = t.split(' · ')[0]
    c = cor.get(f, '#3a3d43')
    cl += f'<div style="background:{GRAPH};padding:12px 14px;height:118px;border-top:3px solid {c}"><div class="mono" style="font-size:12px;opacity:.6">Dia {d+1:02d}</div><div style="font:500 15px/1.3 I;margin-top:6px">{t}</div></div>'
P(f'''<div class="col ey" style="left:120px;top:150px">06 · Calendário de 30 dias</div>
<div class="col h3" style="left:120px;top:190px">4 posts por semana, stories todo dia e 2 textos no LinkedIn</div>
<div class="col" style="left:120px;right:120px;top:290px;display:grid;grid-template-columns:repeat(6,1fr);gap:8px">{cl}</div>
<div class="col mono" style="left:120px;bottom:100px;opacity:.6">Faixa latão = Reel · creme = post · pedra = carrossel · grafite = stories · * = só com autorização do cliente · horários 8h45 a 20h45</div>''', 's', 'Calendário')

# 22 VEREADORES ---------------------------------------------------------------------------
rn = ''.join(f'<tr><td style="width:110px;font:400 34px F;color:#8a6a35">{a}</td><td style="width:220px;font:400 26px F">{b}</td><td>{c}</td></tr>' for a, b, c in REUNIAO)
nd = ''.join(f'<div class="pm" style="padding:9px 0;border-top:1px solid rgba(11,12,14,.18)">✕ {x}</div>' for x in NUNCA_DIZER)
P(f'''<div class="col ey" style="left:120px;top:170px">07 · Receber os vereadores</div>
<div class="col h2" style="left:120px;top:215px;width:1100px">Conselheiro, não <span class="it">marqueteiro</span>.</div>
<div class="col ps" style="left:120px;top:440px;width:1060px">Postura de quem escolhe com quem trabalha. A conversa é sobre o mandato até 2028, nunca sobre “fazer as redes”. Primeira reunião em 30 minutos:</div>
<div class="col" style="left:120px;top:540px;width:1060px"><table class="tb">{rn}</table></div>
<div class="col" style="left:1300px;top:440px;width:500px"><div class="mono" style="color:#8a6a35">Nunca dizer</div><div style="margin-top:10px">{nd}</div>
<div class="mono" style="margin-top:26px;opacity:.6;line-height:1.6">Regras eleitorais e contrato: conferir com advogado.</div></div>''', 'l', 'Vereadores')

# 23 KIT -----------------------------------------------------------------------------------
kt = ''.join(f'<div style="display:flex;gap:30px;padding:20px 0;border-top:1px solid rgba(239,234,225,.2)"><div style="font:400 56px/.9 F;color:{BRASS};width:70px">{i+1}</div><div style="width:400px" class="h4">{n}</div><div class="ps" style="flex:1">{t}</div></div>' for i, (n, t) in enumerate(KIT))
P(f'''{corte(12, 1530, 110, '#16181b', 1, 3, BRASS)}
<div class="col ey" style="left:120px;top:170px">07 · Kit de autoridade</div>
<div class="col h2" style="left:120px;top:215px">O que ele <span class="it">deixa na mesa</span>.</div>
<div class="col" style="left:120px;right:120px;top:420px">{kt}</div>''', '', 'Kit')

# 24 90 DIAS -------------------------------------------------------------------------------
pl = ''.join(f'<div style="flex:1;border-top:{"4px solid " + BRASS if i == 0 else "1px solid rgba(239,234,225,.3)"};padding-top:24px"><div class="mono" style="color:{BRASS}">{m}</div><div class="h3" style="margin:12px 0 20px">{n}</div>' + ''.join(f'<div class="ps" style="padding:10px 0;border-top:1px solid rgba(239,234,225,.12)">{x}</div>' for x in it) + '</div>' for i, (m, n, it) in enumerate(PLANO90))
P(f'''<div class="col ey" style="left:120px;top:170px">08 · Plano de 90 dias</div>
<div class="col h2" style="left:120px;top:215px">Fundação, prova, <span class="it">escala</span>.</div>
<div class="col" style="left:120px;right:120px;top:410px;display:flex;gap:60px">{pl}</div>''', 's', '90 dias')

# 25 METAS ---------------------------------------------------------------------------------
mt = ''.join(f'<tr><td style="width:200px" class="mono">{a}</td><td style="font:400 26px F">{b}</td><td style="width:520px">{c}</td></tr>' for a, b, c in METAS)
P(f'''<div class="col ey" style="left:120px;top:170px">08 · Metas mensuráveis</div>
<div class="col h2" style="left:120px;top:215px">Medir o que <span class="it">ele controla</span>.</div>
<div class="col" style="left:120px;right:120px;top:410px"><table class="tb"><tr><th>Eixo</th><th>Indicador</th><th>Meta</th></tr>{mt}</table></div>
<div class="col mono" style="left:120px;bottom:100px;opacity:.6">Sem número inventado: metas de conversa nascem da linha de base do 1º relatório (dezembro).</div>''', 'l', 'Metas')

# 26 TIME + REFERÊNCIAS --------------------------------------------------------------------
tm = ''.join(f'<tr><td style="width:240px;font:400 25px F">{n}</td><td style="width:110px" class="mono">{p}</td><td class="pm">{t}</td></tr>' for n, p, t in TIME)
rf = ''.join(f'<div style="flex:1"><div style="height:150px;background:url(file://{B}/referencias/{img}.jpg) top/cover;border:1px solid rgba(239,234,225,.15)"></div><div class="h4" style="font-size:22px;margin-top:12px">{n} <span class="mono" style="opacity:.6;font-size:12px">· {p}</span></div><div class="pm" style="margin-top:6px;font-size:15px">{t}</div></div>'
             for (n, p, t), img in zip(REFS, ['ct-group-uk', 'marcelo-vitorino-br', 'debbie-millman-us']))
P(f'''<div class="col ey" style="left:120px;top:150px">09 · Time de agentes e referências</div>
<div class="col" style="left:120px;top:200px;width:1000px"><table class="tb"><tr><th>Agente</th><th>Papel</th><th>O que mudou</th></tr>{tm}</table></div>
<div class="col" style="left:1180px;top:200px;width:620px;display:flex;flex-direction:column;gap:22px">{rf}</div>''', '', 'Time')

# 27 DECISÕES + LIMITES -------------------------------------------------------------------
dc = ''.join(f'<div style="border-top:2px solid {INK};padding-top:18px"><div style="font:400 60px/.9 F">{i+1}</div><div class="h4" style="margin:10px 0">{n}</div><div class="pm" style="opacity:.9">{t}</div></div>' for i, (n, t) in enumerate(DECISOES))
lm = ''.join(f'<div class="pm" style="padding:7px 0;border-top:1px solid rgba(11,12,14,.25)">{x}</div>' for x in LIMITES)
P(f'''<div class="col ey" style="left:120px;top:150px">09 · O que o Lindson decide</div>
<div class="col h3" style="left:120px;top:195px">Três decisões destravam dezembro.</div>
<div class="col" style="left:120px;right:120px;top:300px;display:grid;grid-template-columns:repeat(3,1fr);gap:50px">{dc}</div>
<div class="col" style="left:120px;right:120px;top:690px"><div class="mono">Limitações conhecidas</div><div style="margin-top:8px;columns:2;column-gap:60px">{lm}</div></div>''', 'b', 'Decisões')
