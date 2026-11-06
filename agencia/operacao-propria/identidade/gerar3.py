# Identidade visual Orégano Turbo · v3 SÉRIA (conta Leandro, 05/11/2026) · Brand Squad + Design Squad
# Lindson: "você acha que um dono de pizzaria vai querer comprar de uma identidade assim? … prefiro coisa mais séria,
# imagens reais, mockups". Persona (BRIEF.md): dono de pizzaria em São Luís, 30–55 anos, vive no balcão e no celular,
# depende do iFood, confia em seriedade, foto real, prova e número; desconfia de coisa "fofinha" de designer.
# Composição copiada de (TEMPLATE.md, seção v3):
#  1. Toast · "Built for Busy" (EUA): foto real de cozinha escurecida, título curto em sans pesada, UMA palavra
#     circulada à mão na cor de destaque (laranja), botão na mesma cor → capa, post 1, página de foto.
#  2. Owner.com (EUA): celular em close mostrando dado real do restaurante ("quem está te vencendo no Google"),
#     prova social em uma linha (estrelas + nº de avaliações), verde como cor de marca → mockups WhatsApp e relatório.
#  3. Lightspeed (Canadá): pessoa real trabalhando com o equipamento na mão, fundo limpo, etiqueta em versalete
#     espaçada acima do título → páginas de aplicação, cartão e proposta.
# Gera pecas3.html → node render3.js → pecas-v3/*.png. Fotos: fotos-v3/ (créditos em fotos-v3/CREDITOS.md).
CARVAO, CREME, VERDE, BRASA, CINZA, PAPEL = '#141311', '#F3EEE6', '#1E5B3B', '#E4572E', '#8A857C', '#FBF8F3'
VERDE_CL = '#7CC596'  # verde para texto sobre carvão
FOTO = lambda n: f'fotos-v3/{n}.jpg'

def simbolo(tam, folha=VERDE, seta=CREME):
    """Folha de orégano cuja nervura é uma seta subindo: orégano + venda crescendo."""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="{tam}" height="{tam}">'
            f'<path d="M18 86 C 14 50, 40 18, 86 14 C 86 58, 58 88, 18 86 Z" fill="{folha}"/>'
            f'<path d="M26 76 L44 58 L54 66 L72 40" fill="none" stroke="{seta}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M60 38 L74 38 L74 52" fill="none" stroke="{seta}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def logo(tam, cor=CARVAO, folha=VERDE, seta=CREME, sub=True):
    s = f'<div style="display:flex;align-items:center;gap:{tam * .28}px">{simbolo(tam * 1.15, folha, seta)}<div>'
    s += f'<div style="font:800 {tam}px/0.9 \'Inter Tight\';letter-spacing:-.045em;color:{cor}">Orégano Turbo</div>'
    if sub: s += f'<div style="font:500 {tam * .2}px/1 \'IBM Plex Mono\';letter-spacing:.16em;color:{cor};opacity:.7;margin-top:{tam * .2}px">MARKETING DE VENDAS PARA PIZZARIAS</div>'
    return s + '</div></div>'

def circulo(palavra, cor=BRASA, pad=.07):
    """Palavra circulada à mão (Toast · Built for Busy)."""
    return (f'<span style="position:relative;display:inline-block">{palavra}<svg viewBox="0 0 200 80" preserveAspectRatio="none" '
            f'style="position:absolute;left:-{pad * 100}%;top:-22%;width:{100 + pad * 200}%;height:144%;overflow:visible">'
            f'<path d="M30 14 C 90 0, 190 6, 194 38 C 198 70, 80 80, 20 66 C -10 56, 6 22, 60 10" fill="none" stroke="{cor}" stroke-width="4" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg></span>')

ETQ = lambda t, cor=CINZA, extra='': f'<div style="white-space:nowrap;font:500 18px/1 \'IBM Plex Mono\';letter-spacing:.16em;text-transform:uppercase;color:{cor};{extra}">{t}</div>'
A = lambda x, y, inner, w=None, extra='': f'<div class="a" style="left:{x}px;top:{y}px;{f"width:{w}px;" if w else ""}{extra}">{inner}</div>'
def fundo_foto(n, escuro=.55, pos='center', grad=True):
    g = f'linear-gradient(180deg,rgba(20,19,17,{escuro * .6}) 0%,rgba(20,19,17,{escuro}) 45%,rgba(20,19,17,.94) 100%),' if grad else ''
    return f'<div class="a" style="inset:0;background:{g}url({FOTO(n)}) {pos}/cover"></div>'
RODAPE = lambda n, cor=CINZA: A(80, 1270, f'<div style="display:flex;justify-content:space-between;width:920px">{ETQ("Orégano Turbo · v3", cor)}{ETQ(n, cor)}</div>')

def iphone(inner, w=420, h=860, bg='#fff'):
    return (f'<div style="width:{w}px;height:{h}px;border-radius:64px;background:#0b0b0a;padding:14px;box-shadow:0 50px 90px -30px rgba(0,0,0,.55),0 0 0 2px #3a3833 inset">'
            f'<div style="position:relative;width:100%;height:100%;border-radius:52px;overflow:hidden;background:{bg}">'
            f'<div style="position:absolute;left:50%;top:12px;transform:translateX(-50%);width:118px;height:34px;border-radius:20px;background:#0b0b0a;z-index:5"></div>'
            f'<div style="display:flex;justify-content:space-between;padding:18px 34px 0;font:600 16px \'Inter\';color:{"#fff" if bg in (CARVAO, "#0b141a") else "#111"}"><span>19:42</span><span>●●● ▮</span></div>'
            f'{inner}</div></div>')

def balao(txt, eu=False, hora='19:4'):
    cor = '#d9fdd3' if eu else '#fff'
    return (f'<div style="align-self:{"flex-end" if eu else "flex-start"};max-width:78%;background:{cor};border-radius:12px;padding:10px 12px 6px;'
            f'font:400 16px/1.35 \'Inter\';color:#111;box-shadow:0 1px 1px rgba(0,0,0,.12)">{txt}<div style="text-align:right;font-size:11px;color:#667">{hora}{" ✓✓" if eu else ""}</div></div>')

P = []
# 1 · CAPA — Toast: foto real escurecida + título com uma palavra circulada
P.append(('v3-01-capa', 1080, 1350, CARVAO, fundo_foto('pa-no-forno', .5, '40% center') +
  A(80, 80, logo(46, CREME, VERDE, CREME, sub=False)) + A(720, 96, ETQ('Identidade visual · 2026', CREME)) +
  A(80, 690, f'<div style="font:800 128px/.95 \'Inter Tight\';letter-spacing:-.05em;color:{CREME}">Mais {circulo("pedidos.")}<br>Menos achismo.</div>', 940) +
  A(80, 990, f'<div style="font:400 32px/1.4 \'Inter\';color:{CREME};opacity:.85;width:760px">Estratégia, conteúdo e anúncios para sua pizzaria, com os números na mesa toda segunda.</div>') +
  A(80, 1180, f'<div style="display:inline-block;background:{BRASA};color:#fff;font:700 26px \'Inter\';padding:22px 34px;border-radius:999px">Quero mais pedidos →</div>') +
  A(700, 1205, ETQ('Foto real · luz de forno', CREME, 'opacity:.6'))))

# 2 · LOGO
cx = lambda x, y, w, h, bg, inner: A(x, y, inner, w, f'height:{h}px;background:{bg};border-radius:18px;display:grid;place-items:center')
P.append(('v3-02-logo', 1080, 1350, PAPEL,
  A(80, 80, ETQ('02 · Logo')) +
  A(80, 150, f'<div style="font:800 64px/1 \'Inter Tight\';letter-spacing:-.04em;color:{CARVAO};width:900px">Uma folha que sobe.</div>') +
  A(80, 240, f'<div style="font:400 26px/1.45 \'Inter\';color:#4a4740;width:880px">A folha de orégano é o tempero que fecha a pizza. A nervura dela é a seta das vendas subindo. Nada de mascote: o dono de pizzaria compra de quem parece empresa séria.</div>') +
  cx(80, 400, 920, 420, CREME, logo(92, CARVAO)) +
  cx(80, 850, 440, 200, CARVAO, logo(40, CREME, VERDE_CL, CARVAO, sub=False)) +
  cx(560, 850, 440, 200, VERDE, logo(40, CREME, CREME, VERDE, sub=False)) +
  cx(80, 1070, 210, 170, CREME, simbolo(110)) + cx(316, 1070, 210, 170, VERDE, simbolo(110, CREME, VERDE)) +
  cx(552, 1070, 210, 170, CARVAO, simbolo(110, VERDE_CL, CARVAO)) +
  A(788, 1070, f'<div style="width:212px;height:170px;border-radius:18px;background:url({FOTO("forno-pizza")}) center/cover;display:grid;place-items:center">{simbolo(110, CREME, CARVAO)}</div>') +
  RODAPE('Versões e símbolo')))

# 3 · CORES E LETRAS
sw = lambda bg, fg, nome, hx, uso, h: f'<div style="background:{bg};color:{fg};height:{h}px;border-radius:18px;padding:28px;display:flex;flex-direction:column;justify-content:space-between;{"border:2px solid #e3ddd2;" if bg == PAPEL else ""}"><div style="font:700 30px \'Inter Tight\'">{nome}</div><div style="font:500 18px/1.5 \'IBM Plex Mono\'">{hx}<br>{uso}</div></div>'
P.append(('v3-03-cores-letras', 1080, 1350, PAPEL,
  A(80, 80, ETQ('03 · Cores e letras')) +
  A(80, 140, f'<div style="display:grid;grid-template-columns:1.4fr 1fr;gap:20px;width:920px">{sw(CARVAO, CREME, "Carvão do forno", CARVAO, "fundo · texto · 45%", 300)}{sw(VERDE, CREME, "Verde orégano", VERDE, "marca · 25%", 300)}</div>') +
  A(80, 460, f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;width:920px">{sw(CREME, CARVAO, "Creme", CREME, "papel · 20%", 200)}{sw(BRASA, "#fff", "Brasa", BRASA, "só botão e destaque · 5%", 200)}{sw(PAPEL, CARVAO, "Papel", PAPEL, "fundo claro · 5%", 200)}</div>') +
  A(80, 720, f'<div style="border-top:2px solid {CARVAO};width:920px;padding-top:26px;display:grid;grid-template-columns:1fr 1fr;gap:40px">'
     f'<div>{ETQ("Títulos · Inter Tight 800")}<div style="font:800 96px/.95 \'Inter Tight\';letter-spacing:-.05em;color:{CARVAO};margin-top:18px">Pedido<br>chegando.</div></div>'
     f'<div>{ETQ("Texto · Inter 400")}<div style="font:400 24px/1.5 \'Inter\';color:#3a3833;margin-top:18px">Frase curta, de WhatsApp. O dono lê entre um pedido e outro, então cada frase diz uma coisa só.</div>'
     f'<div style="margin-top:30px">{ETQ("Números · IBM Plex Mono")}</div><div style="font:500 54px \'IBM Plex Mono\';color:{VERDE};margin-top:14px;letter-spacing:-.02em">R$ 4,10</div><div style="font:400 18px \'Inter\';color:{CINZA}">de volta para cada R$ 1 no anúncio (exemplo)</div></div></div>') +
  RODAPE('Sóbrio e quente')))

# 4 · FOTOGRAFIA — direção de foto real
ft = lambda n, w, h, pos='center': f'<div style="width:{w}px;height:{h}px;border-radius:14px;background:url({FOTO(n)}) {pos}/cover"></div>'
P.append(('v3-04-fotografia', 1080, 1350, CARVAO,
  A(80, 80, ETQ('04 · Fotografia', VERDE_CL)) +
  A(80, 140, f'<div style="font:800 64px/1 \'Inter Tight\';letter-spacing:-.04em;color:{CREME};width:920px">Foto real. Luz de forno. Mão trabalhando.</div>') +
  A(80, 320, f'<div style="display:grid;grid-template-columns:560px 340px;grid-template-rows:330px 330px;gap:20px">'
     f'<div style="grid-row:span 2">{ft("pa-no-forno", 560, 680, "40% center")}</div>{ft("brasa", 340, 330)}{ft("pizza-close", 340, 330)}</div>') +
  A(80, 1030, f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;width:920px;font:400 22px/1.5 \'Inter\';color:{CREME}">'
     f'<div><b style="color:{VERDE_CL}">Sempre</b><br>a cozinha de verdade da pizzaria do cliente, o forno, a massa, a caixa saindo. Tom quente, sombra profunda.</div>'
     f'<div><b style="color:{BRASA}">Nunca</b><br>ilustração, mascote, foto de banco com gente sorrindo para a câmera, pizza de outra marca, filtro colorido.</div></div>') +
  RODAPE('Fotos CC · créditos no manual', CINZA)))

# 5 · MOCKUP WhatsApp — Owner.com: celular em close mostrando o resultado
chat = (f'<div style="background:#075e54;color:#fff;padding:20px 20px 14px;display:flex;align-items:center;gap:12px;margin-top:10px">'
        f'<div style="width:42px;height:42px;border-radius:50%;background:{CREME};display:grid;place-items:center;font:800 18px \'Inter Tight\';color:{VERDE}">P</div>'
        f'<div><div style="font:600 18px \'Inter\'">Pizzaria do Exemplo</div><div style="font:400 13px \'Inter\';opacity:.8">online</div></div></div>'
        f'<div style="background:#efeae2;height:100%;padding:16px 14px;display:flex;flex-direction:column;gap:10px">'
        + balao('Boa noite! Vi o anúncio da pizza de calabresa. Ainda dá pra pedir?', hora='19:38')
        + balao('Dá sim! Média ou grande? Entrega em 40 min.', True, '19:38')
        + balao('Grande, metade calabresa metade frango. Rua das Flores, 120.', hora='19:39')
        + balao('Anotado ✅ Total R$ 54,90. Pix ou cartão na entrega?', True, '19:39')
        + balao('Pix. Manda a chave', hora='19:40')
        + f'<div style="align-self:center;background:#fff3c4;font:500 13px \'Inter\';padding:6px 12px;border-radius:8px;color:#5a4a00">Pedido 14 de hoje vindo do anúncio</div></div>')
P.append(('v3-05-mockup-whatsapp', 1080, 1350, CREME,
  A(0, 0, '', 1080, f'height:1350px;background:linear-gradient(90deg,{CREME} 52%,transparent 52%),url({FOTO("bancada")}) right center/cover') +
  A(80, 90, ETQ('05 · Mockup · WhatsApp')) +
  A(80, 160, f'<div style="font:800 76px/.98 \'Inter Tight\';letter-spacing:-.045em;color:{CARVAO};width:450px;font-size:66px">O anúncio vira mensagem. A mensagem vira pedido.</div>') +
  A(80, 560, f'<div style="font:400 24px/1.5 \'Inter\';color:#4a4740;width:440px">Tudo o que a gente faz termina aqui: no WhatsApp da pizzaria, com o pedido anotado.</div>') +
  A(80, 760, f'<div style="display:flex;gap:10px;align-items:center;font:600 22px \'Inter\';color:{CARVAO}"><span style="color:{BRASA}">●</span> Vagas para 5 pizzarias fundadoras</div>') +
  A(80, 805, f'<div style="font:400 14px \'IBM Plex Mono\';color:{CINZA};width:440px">CONVERSA ILUSTRATIVA · NOMES E VALORES DE EXEMPLO</div>') +
  A(590, 230, iphone(chat, 420, 880, '#075e54'), extra='transform:rotate(3deg)') +
  RODAPE('Cópia: Owner.com')))

# 6 · MOCKUP relatório de segunda
lin = lambda r, v, c=CREME: f'<div style="display:flex;justify-content:space-between;padding:14px 0;border-bottom:1px solid #2c2a26;font:400 17px \'Inter\';color:#bdb7ab"><span>{r}</span><span style="font:500 18px \'IBM Plex Mono\';color:{c}">{v}</span></div>'
barras = ''.join(f'<div style="flex:1;height:{h}px;background:{VERDE_CL if i == 6 else "#3b3a35"};border-radius:6px 6px 0 0"></div>' for i, h in enumerate([40, 52, 48, 66, 74, 92, 120]))
rel = (f'<div style="padding:26px 26px 0;color:{CREME}">'
       f'<div style="font:700 11px \'IBM Plex Mono\';color:{BRASA};letter-spacing:.08em;margin-bottom:12px">EXEMPLO ILUSTRATIVO · DADOS FICTÍCIOS</div>'
       f'<div style="display:flex;align-items:center;gap:10px">{simbolo(30, VERDE_CL, CARVAO)}<div style="font:700 17px \'Inter\'">Relatório de segunda</div></div>'
       f'<div style="font:500 13px \'IBM Plex Mono\';color:{CINZA};margin-top:20px;letter-spacing:.12em">SEMANA 27/10 – 02/11</div>'
       f'<div style="font:800 76px/1 \'Inter Tight\';letter-spacing:-.04em;margin-top:10px">128</div><div style="font:400 16px \'Inter\';color:#bdb7ab">pedidos que vieram do anúncio</div>'
       f'<div style="display:flex;gap:8px;align-items:flex-end;height:130px;margin-top:22px">{barras}</div>'
       f'<div style="display:flex;justify-content:space-between;font:400 12px \'IBM Plex Mono\';color:{CINZA};margin-top:6px"><span>S1</span><span>S7</span></div>'
       + lin('Investido no anúncio', 'R$ 900') + lin('Vendido pelo anúncio', 'R$ 3.690', VERDE_CL) + lin('Retorno', '4,1×', VERDE_CL) + lin('Custo por pedido', 'R$ 7,03')
       + f'<div style="margin-top:18px;background:{VERDE};border-radius:14px;padding:14px 16px;font:500 15px/1.4 \'Inter\'">Exemplo de ação: revisar o anúncio da calabresa e avaliar o combo de terça.</div></div>')
P.append(('v3-06-mockup-relatorio', 1080, 1350, CARVAO,
  A(80, 90, ETQ('06 · Mockup · toda segunda-feira', VERDE_CL)) +
  A(80, 160, f'<div style="font:800 76px/.98 \'Inter Tight\';letter-spacing:-.045em;color:{CREME};width:470px">Número na mesa, toda segunda.</div>') +
  A(80, 470, f'<div style="font:400 24px/1.5 \'Inter\';color:#bdb7ab;width:440px">O dono não precisa entender de anúncio. Ele vê quanto pôs, quanto voltou e o que muda na semana.</div>') +
  A(80, 700, ''.join(f'<div style="display:flex;gap:14px;align-items:baseline;margin-bottom:18px"><span style="font:500 18px \'IBM Plex Mono\';color:{BRASA}">0{i + 1}</span><span style="font:500 24px \'Inter\';color:{CREME}">{t}</span></div>' for i, t in enumerate(['Quanto investiu', 'Quantos pedidos vieram', 'Quanto voltou para cada R$ 1', 'O que fazer nesta semana']))) +
  A(80, 1010, f'<div style="font:400 16px \'IBM Plex Mono\';color:{CINZA};width:440px">EXEMPLO DE LAYOUT · DADOS FICTÍCIOS</div>') +
  A(600, 200, iphone(rel, 410, 860, CARVAO), extra='transform:rotate(-3deg)') +
  RODAPE('Cópia: Owner.com')))

# 7 · INSTAGRAM — perfil @oreganoturbo
mini = lambda bg, inner, foto=None: f'<div style="aspect-ratio:4/5;background:{(f"linear-gradient(180deg,rgba(20,19,17,.2),rgba(20,19,17,.85)),url({FOTO(foto)}) center/cover") if foto else bg};position:relative;overflow:hidden;padding:14px;display:flex;flex-direction:column;justify-content:flex-end">{inner}</div>'
tt = lambda t, c=CREME, s=22: f'<div style="font:800 {s}px/1 \'Inter Tight\';letter-spacing:-.04em;color:{c}">{t}</div>'
grade = ''.join([
  mini(0, tt('Forno cheio na terça?'), 'brasa'), mini(VERDE, tt('Relatório', CREME, 22) + tt('toda segunda', CREME, 14)), mini(CREME, tt('3 erros que esvaziam o seu WhatsApp', CARVAO, 20)),
  mini(CARVAO, tt('Relatório de segunda', CREME, 20)), mini(0, tt('Pizza boa não vende sozinha.'), 'pizza-close'), mini(BRASA, tt('Quero mais pedidos →', '#fff', 20)),
  mini(CREME, tt('iFood ou pedido direto?', CARVAO, 22)), mini(0, tt('A caixa que sai é o anúncio que volta.'), 'caixas'), mini(VERDE, tt('5 vagas fundadoras', CREME, 22))])
perfil = (f'<div style="padding:16px 20px 0;font-family:Inter;color:#111">'
          f'<div style="font:700 19px Inter;margin:6px 0 14px">oreganoturbo ⌄</div>'
          f'<div style="display:flex;align-items:center;gap:22px"><div style="width:96px;height:96px;border-radius:50%;background:{VERDE};display:grid;place-items:center;flex:none">{simbolo(60, CREME, VERDE)}</div>'
          f'<div style="display:flex;gap:22px;text-align:center;font:400 14px Inter"><div><b style="font-size:18px">9</b><br>posts</div><div><b style="font-size:18px">—</b><br>seguidores</div><div><b style="font-size:18px">—</b><br>seguindo</div></div></div>'
          f'<div style="font:600 15px Inter;margin-top:12px">Orégano Turbo | Mkt Pizzarias</div>'
          f'<div style="font:400 14px/1.4 Inter;margin-top:2px">Marketing de vendas só para pizzarias 🍕<br>Anúncio, Instagram e WhatsApp<br>Relatório toda segunda · São Luís/MA<br><span style="color:#00376b">Fale com a equipe ↓</span></div>'
          f'<div style="display:flex;gap:6px;margin-top:12px"><div style="flex:1;background:#efefef;border-radius:8px;padding:8px;text-align:center;font:600 14px Inter">Seguir</div><div style="flex:1;background:#efefef;border-radius:8px;padding:8px;text-align:center;font:600 14px Inter">Mensagem</div></div>'
          f'<div style="display:flex;gap:16px;margin:14px 0 10px">' + ''.join(f'<div style="text-align:center;font:400 11px Inter"><div style="width:58px;height:58px;border-radius:50%;border:2px solid #ddd;padding:3px"><div style="width:100%;height:100%;border-radius:50%;background:{c};display:grid;place-items:center;font:800 13px \'Inter Tight\';color:{CREME}">{s}</div></div>{n}</div>' for c, s, n in [(CARVAO, '01', 'Método'), (VERDE, 'R$', 'Planos'), (BRASA, '✓', 'Relatórios'), (CARVAO, '?', 'Dúvidas')]) +
          f'</div></div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2px">{grade}</div>')
P.append(('v3-07-instagram', 1080, 1350, PAPEL,
  A(80, 90, ETQ('07 · Aplicação · Instagram')) +
  A(80, 160, f'<div style="font:800 76px/.98 \'Inter Tight\';letter-spacing:-.045em;color:{CARVAO};width:470px">Um feed que parece empresa.</div>') +
  A(80, 450, f'<div style="font:400 24px/1.5 \'Inter\';color:#4a4740;width:440px">Três tipos de post se revezam: foto real com frase curta, número grande e dica direta. Nunca dois iguais lado a lado.</div>') +
  A(80, 720, ''.join(f'<div style="display:flex;gap:16px;align-items:center;margin-bottom:16px"><div style="width:22px;height:22px;border-radius:5px;background:{c}"></div><span style="font:500 22px Inter;color:{CARVAO}">{t}</span></div>' for c, t in [(CARVAO, 'Foto real + frase'), (VERDE, 'Número / prova'), (CREME, 'Dica direta'), (BRASA, 'Chamada (1 a cada 9)')])) +
  A(590, 150, iphone(perfil, 430, 900)) +
  RODAPE('Cópia: Lightspeed + Toast')))

# 8 · POST 1 — foto real + palavra circulada (Toast)
P.append(('v3-08-post-foto', 1080, 1350, CARVAO, fundo_foto('brasa', .45) +
  A(80, 80, logo(34, CREME, VERDE_CL, CARVAO, sub=False)) +
  A(80, 820, f'<div style="font:800 112px/.95 \'Inter Tight\';letter-spacing:-.05em;color:{CREME}">Forno cheio<br>na sexta.<br>E na {circulo("terça?")}</div>', 940) +
  A(80, 1210, f'<div style="font:500 26px \'Inter\';color:{CREME};opacity:.85">Dia fraco tem conserto. Arrasta →</div>') +
  A(840, 1215, ETQ('@oreganoturbo', CREME, 'opacity:.7'))))

# 9 · POST 2 — proposta de valor (copy aprovada, sem número fictício)
P.append(('v3-09-post-processo', 1080, 1350, VERDE,
  A(80, 80, f'<div style="display:flex;justify-content:space-between;width:920px">{logo(34, CREME, CREME, VERDE, sub=False)}{ETQ("Marketing de pizzarias", CREME, "opacity:.7;margin-top:10px")}</div>') +
  A(80, 330, f'<div style="font:800 112px/.98 \'Inter Tight\';letter-spacing:-.05em;color:{CREME};width:920px">Mais {circulo("pedidos.")}<br>Menos achismo.</div>') +
  A(80, 680, f'<div style="font:400 31px/1.45 \'Inter\';color:{CREME};width:850px">Anúncio, Instagram e WhatsApp trabalhando para sua pizzaria vender mais.</div>') +
  A(80, 950, f'<div style="height:2px;background:{CREME};opacity:.3;width:920px"></div>') +
  A(80, 1010, f'<div style="font:500 22px/1.5 \'IBM Plex Mono\';color:{CREME};width:860px">ACOMPANHAMENTO COM DADOS REAIS<br>RELATÓRIO TODA SEGUNDA · SÃO LUÍS/MA</div>') +
  A(80, 1170, f'<div style="display:inline-block;background:{BRASA};color:#fff;font:700 22px \'Inter\';padding:18px 30px;border-radius:999px">Fale com a equipe →</div>') +
  RODAPE('Mensagem aprovada')))
# 10 · CARTÃO + PROPOSTA (Lightspeed: etiqueta espaçada + título + produto na mão)
cartao_f = f'<div style="width:420px;height:240px;border-radius:12px;background:{VERDE};padding:30px;display:flex;flex-direction:column;justify-content:space-between;box-shadow:0 30px 60px -20px rgba(0,0,0,.5)">{simbolo(64, CREME, VERDE)}<div style="font:800 34px/1 \'Inter Tight\';letter-spacing:-.04em;color:{CREME}">Orégano Turbo</div></div>'
cartao_v = f'<div style="width:420px;height:240px;border-radius:12px;background:{PAPEL};padding:30px;display:flex;flex-direction:column;justify-content:space-between;box-shadow:0 30px 60px -20px rgba(0,0,0,.5)"><div><div style="font:700 24px Inter;color:{CARVAO}">Lindson Almeida</div><div style="font:400 15px Inter;color:{CINZA};margin-top:4px">Estrategista de vendas para pizzarias</div></div><div style="font:500 14px/1.7 \'IBM Plex Mono\';color:{CARVAO}">@oreganoturbo<br>WhatsApp: link na bio<br>São Luís · MA</div></div>'
proposta = (f'<div style="width:500px;height:640px;background:{CARVAO};border-radius:6px;position:relative;overflow:hidden;box-shadow:0 40px 80px -24px rgba(0,0,0,.6)">'
            f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,19,17,.3),rgba(20,19,17,.95) 70%),url({FOTO("forno-pizza")}) center/cover"></div>'
            f'<div style="position:absolute;left:36px;top:36px">{logo(22, CREME, VERDE_CL, CARVAO, sub=False)}</div>'
            f'<div style="position:absolute;left:36px;bottom:40px;right:36px"><div style="font:500 13px \'IBM Plex Mono\';letter-spacing:.18em;color:{VERDE_CL}">RAIO-X DO DELIVERY · PIZZARIA DO EXEMPLO</div>'
            f'<div style="font:800 52px/.98 \'Inter Tight\';letter-spacing:-.045em;color:{CREME};margin-top:14px">Onde estão os pedidos que você está perdendo.</div></div></div>')
P.append(('v3-10-cartao-proposta', 1080, 1350, '#D9D2C5',
  A(0, 0, '', 1080, 'height:1350px;background:radial-gradient(circle at 30% 30%,#ece6db,#cfc6b6)') +
  A(80, 90, ETQ('10 · Aplicação · papelaria e proposta')) +
  A(80, 160, f'<div style="font:800 64px/1 \'Inter Tight\';letter-spacing:-.04em;color:{CARVAO};width:900px">O que chega na mão do dono.</div>') +
  A(500, 330, proposta, extra='transform:rotate(4deg)') +
  A(90, 420, cartao_f, extra='transform:rotate(-6deg)') + A(110, 730, cartao_v, extra='transform:rotate(3deg)') +
  A(80, 1060, f'<div style="font:400 22px/1.5 \'Inter\';color:#4a4740;width:380px">Proposta e Raio-X sempre com a foto da pizzaria do próprio cliente na capa.</div>') +
  RODAPE('Cópia: Lightspeed')))

# 11 · AVATAR 1080×1080
P.append(('v3-11-avatar', 1080, 1080, VERDE, A(0, 0, f'<div style="width:1080px;height:1080px;display:grid;place-items:center">{simbolo(620, CREME, VERDE)}</div>')))

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@600;700;800&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">'
CSS = 'body{margin:0;background:#888}section.f{position:relative;overflow:hidden;margin:0 0 40px}.a{position:absolute}*{box-sizing:border-box}'
import os
d = os.path.dirname(os.path.abspath(__file__))
open(os.path.join(d, 'pecas3.html'), 'w').write(
    f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>'
    + ''.join(f'<section class="f" id="{i}" style="width:{w}px;height:{h}px;background:{bg}">{c}</section>' for i, w, h, bg, c in P) + '</body></html>')
print(len(P), 'pranchas → pecas3.html')
