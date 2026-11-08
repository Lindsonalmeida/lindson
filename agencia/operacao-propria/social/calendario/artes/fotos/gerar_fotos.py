# Artes COM FOTO do calendário do @oreganoturbo (lote 2 do Gemini) · Paollo · 06/11/2026
# Base: kit v3 aprovado ("AGORA SIM, ESSE É O PADRÃO"), ../../../v3/gerar.py. As funções de marca de lá (símbolo, logo, selo,
# padrão de ícones, xadrez, adesivo, estrela, faixa em loop, tarja) são CARREGADAS daquele arquivo, como em s1-2 e s3-4.
# Regra do Lindson (06/11): cada foto UMA vez só (registro em ../../../FOTOS-USADAS.md).
#   d09 19h SEU CLIENTE SUMIU?                     → B8a-pizzaria-vazia  (cartaz de "desaparecido")
#   d11 19h DOMINGO É DIA DE PIZZA. TERÇA TAMBÉM.  → B7-moca-carro       (palavra gigante POR TRÁS da moça)
#   d13 12h PIZZA BOA NÃO VENDE SOZINHA.           → B4-cesta            (pizza gigante com texto em círculo)
#   d15 08h story Bom dia, forno aceso.            → B8b-pizzaria-vazia  (arco do forno a lenha como janela)
#   d16 19h PIZZA FRIA NÃO TEM PERDÃO.             → B5-motoboy          (de baixo, raios de cartaz, "FRIA" por trás)
# Uso: python3 recortar.py <foto> (1 por processo) && python3 gerar_fotos.py && node render.js && python3 previa.py
import os, json
D = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(D, '..', 'sistema_v4.py'), encoding='utf-8').read())   # sistema v4 (08/11, conta Zuleide): lê ../../../v4/gerar.py
D = os.path.dirname(os.path.abspath(__file__))
FONTS = FONTS.replace('&family=Inter:', '&family=Kaushan+Script&family=Inter:')
FOTO = lambda n: f'../../../../identidade/fotos-ia/hd/{n}.jpg'
REC = lambda n: f'recortes/{n}.webp'
FIT = lambda html, w, extra='': f'<div data-w="{w}" style="width:{w}px;{extra}">{html}</div>'   # encolhe a letra até caber em w
KAU = lambda t, s, cor, extra='': BAGEL(t, s * .72, cor, 1, extra)   # v4: manuscrito saiu, Bagel em toda manchete
SEL = lambda tam, txt, bg, fg, rot, centro=None, fs=12.5: f'<div style="transform:rotate({rot}deg)">{selo(tam, txt, bg, fg, centro, fs)}</div>'
IAT = 'imagem gerada por IA · @oreganoturbo'
def icone(n, tam, cor, w=6):
    return (f'<svg viewBox="0 0 100 100" width="{tam}" height="{tam}" style="display:block;overflow:visible"><g fill="none" stroke="{cor}" '
            f'stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{IC[n]}</g></svg>')
fita = lambda rot, cor='rgba(243,238,230,.78)': f'<div style="width:170px;height:46px;background:{cor};transform:rotate({rot}deg);box-shadow:0 3px 0 rgba(0,0,0,.12)"></div>'

P, COMP = [], {}
POS = {'d09-19h-seu-cliente-sumiu': (800, 40, 5), 'd11-19h-domingo-e-terca-tambem': (40, 560, -4), 'd13-12h-pizza-boa-nao-vende-sozinha': (30, 720, -5), 'd16-19h-pizza-fria-nao-tem-perdao': (40, 560, -4)}  # lugar fixo da comanda (x, y, rot) quando o automático não serve
feed = lambda n, h, c: (P.append((n, 1080, 1350, h + COMANDA(n, POS.get(n)) + GRAO)), COMP.__setitem__(n, c))
stor = lambda n, h, c: (P.append((n, 1080, 1920, h + COMANDA(n, POS.get(n)) + GRAO)), COMP.__setitem__(n, c))

# ================================================================== d09 19h · SEU CLIENTE SUMIU? (B8a, cartaz de desaparecido)
# Copia: cartaz retrô de pizzaria (retro-13: título gordo + faixa de rodapé) virado "PROCURA-SE" (humor e referência pop,
# "Penso, logo PEÇO") + manchete em 2 tamanhos ("AQUI / não tem / ERRO"). A foto entra emoldurada, colada com fita.
cartaz = (f'<div style="position:relative;width:860px;height:880px;background:{CREME};border:6px solid {CARVAO};box-shadow:18px 20px 0 rgba(0,0,0,.45);padding:26px 34px">'
          f'<div style="position:absolute;inset:0;background:{padrao(TOMATE, .10, 260)}"></div>'
          f'<div style="position:relative;display:flex;justify-content:space-between;align-items:center">{MONO("Procura-se · São Luís - MA", 17, CARVAO)}{MONO("Nº 0001", 17, TOMATE)}</div>'
          f'<div style="position:relative;display:flex;justify-content:center;margin-top:6px">{ANTON("Desaparecido", 132, TOMATE, .95, "letter-spacing:.01em")}</div>'
          f'<div style="position:relative;margin-top:10px;height:440px;border:6px solid {CARVAO};background:url({FOTO("B8a-pizzaria-vazia")}) 58% 52%/118% auto;'
          f'filter:contrast(1.08) saturate(1.1)"><div style="position:absolute;left:14px;bottom:12px">{MONO("imagem gerada por IA", 11, CREME, "opacity:.8")}</div></div>'
          f'<div style="position:relative;margin-top:20px;display:grid;grid-template-columns:1fr 1fr;gap:10px 26px">'
          + ''.join(f'<div>{MONO(a, 13, TOMATE)}<div style="font:700 25px/1.2 Inter;color:{CARVAO};margin-top:4px">{b}</div></div>' for a, b in [
              ('Visto pela última vez', 'Pediu uma vez. Só.'), ('Sinais', 'Não lembra o seu nome.'),
              ('Onde procurar', 'No zap e no Instagram.'), ('Paradeiro provável', 'Na pizzaria do lado.')])
          + '</div></div>')
feed('d09-19h-seu-cliente-sumiu',
     BOX(0, 0, 1080, 1350, CARVAO) + f'<div class="a" style="inset:0;background:{padrao(CREME, .07, 300)}"></div>' +
     BOX(0, 0, 1080, 30, xadrez(TOMATE, CREME, 15)) +
     A(44, 60, ANTON('Seu cliente', 100, CREME, .9)) +
     A(110, 230, cartaz, 'transform:rotate(-3deg)') +
     A(140, 196, fita(-14)) + A(800, 214, fita(10)) +
     A(30, 985, FIT(BAGEL('Sumiu?', 250, TOMATE, .9, SH(CREME, 10)), 1010)) +
     A(20, 610, SEL(210, 'ELE PEDIU UMA VEZ · E ESQUECEU DE VOCÊ · ', ACAFRAO, CARVAO, 12)) +
     A(690, 700, adesivo('Traz de volta<br>pelo zap ↗', ACAFRAO, CARVAO, -7, 34, '18px 26px', extra='border-radius:28px;line-height:1.02;text-align:center')) +
     tarja_ass(1258, TOMATE, CREME, IAT),
     'Cartaz de "DESAPARECIDO" colado com fita (cartaz retrô retro-13 + humor pop "Penso, logo PEÇO") com a foto da pizzaria vazia emoldurada; '
     'manchete em 2 tamanhos ("SEU CLIENTE" fino, "SUMIU?" gigante cruzando o cartaz); selo girado e adesivo; carvão com faixa de xadrez')

# ================================================================== d11 19h · DOMINGO É DIA DE PIZZA. TERÇA TAMBÉM. (B7, palavra por trás)
# Copia: Decaf Girl (céu azul, flash, gente comendo com bagunça) + "PIZZA gigante atrás" (a palavra TERÇA passa POR TRÁS
# da fatia, do braço e da moça, recorte BiRefNet) + tira da semana (figurinha de calendário com DOM e TER marcados).
dias = ''.join(f'<div style="width:66px;height:66px;border-radius:50%;display:grid;place-items:center;font:400 22px/1 Anton;'
               f'background:{TOMATE if d in ("TER", "DOM") else CREME};color:{CREME if d in ("TER", "DOM") else CARVAO};'
               f'box-shadow:0 0 0 {5 if d in ("TER", "DOM") else 0}px {CARVAO}">{d}</div>'
               for d in ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SÁB', 'DOM'])
semana = (f'<div style="display:flex;gap:10px;background:{CARVAO};padding:14px 18px;border-radius:999px;box-shadow:0 0 0 7px {CREME},12px 14px 0 7px rgba(20,19,17,.3)">{dias}</div>')
feed('d11-19h-domingo-e-terca-tambem',
     foto('B7-moca-carro') +
     A(40, 24, ANTON('Domingo é dia de pizza.', 66, CREME, .9, SH(CARVAO, 5))) +
     A(24, 66, FIT(BAGEL('Terça', 330, TOMATE, .86, SH(CREME, 10)), 1030)) +
     frente('B7-moca-carro') +
     A(34, 1040, BAGEL('também.', 196, CARVAO, .9, SH(CREME, 8))) +
     A(30, 905, semana, 'transform:rotate(-4deg) scale(.86);transform-origin:0 0') +
     A(820, 690, estrela(210, TOMATE, BAGEL('Quem<br>disse<br>que não?', 34, CREME, .95), 10)) +
     tarja_ass(1258, CARVAO, CREME, IAT),
     'Foto inteira de flash com céu azul (Decaf Girl) e a palavra gigante "TERÇA" passando POR TRÁS da fatia e da moça (recorte BiRefNet, "PIZZA gigante atrás"); '
     '"também." gordo sobre a porta amarela; tira da semana com DOM e TER marcados; estrela "quem disse que não?"')

# ================================================================== d13 12h · PIZZA BOA NÃO VENDE SOZINHA. (B4, texto em círculo)
# Copia: pizza inteira vista de cima com texto em círculo em volta (biblioteca, item 5) + produto visto de cima numa cesta
# (favoritas) + "PIZZA gigante atrás" (a manchete passa por trás da tampa da caixa).
cx, cy, rr = 541, 824, 228
anel = (f'<svg class="a" style="left:{cx - 300}px;top:{cy - 300}px" width="600" height="600" viewBox="0 0 600 600">'
        f'<defs><path id="anel" d="M300 300 m-{rr} 0 a{rr} {rr} 0 1 1 {rr * 2} 0 a{rr} {rr} 0 1 1 -{rr * 2} 0"/></defs>'
        f'<circle cx="300" cy="300" r="{rr}" fill="none" stroke="{CARVAO}" stroke-width="62"/>'
        f'<circle cx="300" cy="300" r="{rr}" fill="none" stroke="{TOMATE}" stroke-width="50"/>'
        f'<text font-family="Anton" font-size="35" letter-spacing="3.2" fill="{CREME}" dy="12"><textPath href="#anel">'
        f'PIZZA BOA NÃO VENDE SOZINHA ✦ QUEM APARECE MAIS VENDE MAIS ✦ </textPath></text></svg>')
feed('d13-12h-pizza-boa-nao-vende-sozinha',
     BOX(0, 0, 1080, 1350, VERDE) + f'<div class="a" style="inset:0;background:{padrao(CREME, .12, 300)}"></div>' +
     A(30, 26, FIT(BAGEL('Pizza boa', 250, CREME, .86, SH(CARVAO, 10)), 1020)) +
     IMG(REC('B4-cesta'), 60, 225, 960, 'filter:drop-shadow(22px 26px 0 rgba(20,19,17,.32))') +
     anel +
     A(-30, 1088, f'<div style="width:1140px;background:{ACAFRAO};border-top:6px solid {CARVAO};border-bottom:6px solid {CARVAO};transform:rotate(-3deg);'
                  f'padding:20px 0 24px;display:flex;justify-content:center;box-shadow:0 14px 0 rgba(20,19,17,.3)">'
                  + BAGEL('não vende sozinha.', 104, TOMATE, .95, SH(CARVAO, 6)) + '</div>') +
     A(800, 330, SEL(220, 'SÓ PIZZARIAS · SÃO LUÍS - MA · ', TOMATE, CREME, 14)) +
     A(40, 470, adesivo('Ela precisa<br>aparecer', TOMATE, CREME, -8, 32, '18px 26px', extra='border-radius:28px;line-height:1.02;text-align:center')) +
     A(780, 940, adesivo('Chama no zap ↗', CREME, VERDE, 6, 32, borda=CARVAO)) +
     tarja_ass(1258, CARVAO, CREME, IAT),
     'Cesta com a pizza vista de cima (recorte BiRefNet) com anel de texto girando em volta da pizza; "PIZZA BOA" gigante passando por trás da tampa; '
     'faixa açafrão girada com "não vende sozinha."; selo e adesivos; verde com padrão de ícones')

# ================================================================== d15 08h story · Bom dia, forno aceso. (B8b, arco do forno)
# Copia: arco do forno a lenha com chama (símbolo forte, Bella Pizza, biblioteca item 2) usado como JANELA da foto
# + cartaz retrô (título gordo, faixa de rodapé) + script de apoio (Kaushan).
arco = (f'<div style="position:relative;width:900px;height:1040px;border-radius:450px 450px 0 0;overflow:hidden;'
        f'box-shadow:0 0 0 16px {CREME},0 0 0 22px {CARVAO},0 0 120px 40px rgba(240,106,31,.45)">'
        f'<div style="position:absolute;inset:0;background:url({FOTO("B8b-pizzaria-vazia")}) -860px -330px/1760px auto;filter:contrast(1.1) saturate(1.2) brightness(1.08)"></div>'
        f'<div style="position:absolute;inset:0;background:radial-gradient(circle at 62% 46%,rgba(240,106,31,.0) 0,rgba(240,106,31,.0) 18%,rgba(20,19,17,.35) 70%)"></div>'
        f'<div style="position:absolute;right:30px;bottom:24px">{MONO("imagem gerada por IA", 12, CREME, "opacity:.8")}</div></div>')
tijolos = ''.join(BOX(90 + i * 75 + (37 if j % 2 else 0), 1450 + j * 34, 66, 26, '#8E2A1E', 'border-radius:3px;opacity:.55') for j in range(2) for i in range(12) if 90 + i * 75 + (37 if j % 2 else 0) < 960)
stor('d15-08h-bom-dia-forno-aceso',
     BOX(0, 0, 1080, 1920, 'radial-gradient(circle at 50% 62%,#5A1E0E 0,#2A130C 38%,#141311 75%)') +
     f'<div class="a" style="inset:0;background:{padrao(ACAFRAO, .08, 300)}"></div>' +
     A(48, 150, KAU('Bom dia,', 150, ACAFRAO, SH(CARVAO, 6))) +
     A(90, 420, arco) +
     A(30, 300, FIT(BAGEL('Forno', 290, CREME, .86, SH(TOMATE, 10)), 1020, 'display:flex;justify-content:center')) +
     A(30, 1330, FIT(BAGEL('aceso.', 300, TOMATE, .86, SH(CREME, 10)), 1020, 'display:flex;justify-content:center')) +
     A(770, 1060, f'<div style="transform:rotate(10deg)">{estrela(230, ACAFRAO, MONO("seg", 22, CARVAO) + BAGEL("23/11", 54, TOMATE, .9), 10)}</div>') +
     A(40, 1100, adesivo('Segunda<br>de novo.', VERDE, CREME, -8, 40, '20px 28px', extra='border-radius:30px;line-height:1.02;text-align:center')) +
     A(880, 130, f'<div style="transform:rotate(12deg)">{icone("chama", 130, ACAFRAO, 7)}</div>') +
     faixa('bora vender', 1640, ACAFRAO, CARVAO, -3, 100, 60, x=-60, w=1240) +
     tarja_ass(1820, CARVAO, CREME, IAT, 100),
     'Arco do forno a lenha como janela da foto da pizzaria (símbolo de forno, Bella Pizza) com brilho de brasa; "Bom dia," em script, '
     '"FORNO" e "ACESO." gordos em cima e embaixo do arco; estrela da data, adesivo e faixa em loop; carvão com brasa')

# ================================================================== d16 19h · PIZZA FRIA NÃO TEM PERDÃO. (B5, raios + palavra por trás)
# Copia: grande-angular de baixo com flash (favoritas, "flash com céu azul") recortada sobre raios de cartaz retrô (retro-13)
# + "PIZZA gigante atrás" (a palavra FRIA passa POR TRÁS do motoboy) + tarja girada cruzando a foto (p07 v3).
raios = 'repeating-conic-gradient(from 0deg at 50% 46%,#E4322B 0 7.5deg,#C5081F 7.5deg 15deg)'
feed('d16-19h-pizza-fria-nao-tem-perdao',
     BOX(0, 0, 1080, 1350, raios) +
     A(44, 34, ANTON('Pizza', 150, CREME, .9, SH(CARVAO, 6))) +
     A(20, 140, FIT(BAGEL('Fria', 400, CREME, .84, SH(CARVAO, 12)), 1040)) +
     IMG(REC('B5-motoboy'), 150, 300, 860, 'filter:drop-shadow(-18px 22px 0 rgba(20,19,17,.30)) saturate(1.06) contrast(1.04)') +
     A(-30, 1010, f'<div style="width:1140px;background:{CARVAO};border-top:6px solid {ACAFRAO};border-bottom:6px solid {ACAFRAO};transform:rotate(-4deg);'
                  f'padding:18px 0 22px;display:flex;justify-content:center;box-shadow:0 14px 0 rgba(20,19,17,.3)">'
                  + BAGEL('não tem perdão.', 116, ACAFRAO, .95, SH(TOMATE, 6)) + '</div>') +
     A(700, 40, SEL(230, 'ENTREGA É PARTE DA PIZZA · ENTREGA É PARTE DA PIZZA · ', VERDE, CREME, 12, fs=11)) +
     A(720, 640, estrela(220, ACAFRAO, MONO('quente', 20, CARVAO) + BAGEL('na<br>porta', 52, TOMATE, .9), 8)) +
     A(40, 1166, adesivo('Entrega é parte da pizza', CREME, TOMATE, -2, 30, borda=CARVAO)) +
     A(700, 1300, MONO(IAT, 12, CREME, 'opacity:.85')) +
     A(640, 1170, adesivo('Chama no zap ↗', ACAFRAO, CARVAO, 4, 32)),
     'Motoboy de baixo (recorte BiRefNet) sobre raios de cartaz retrô em tomate; "FRIA" gigante em creme (v4: sem azul) passando POR TRÁS dele; '
     'tarja carvão girada com "não tem perdão."; selo, estrela "quente na porta" e adesivos')

open(os.path.join(D, 'pecas.html'), 'w', encoding='utf-8').write(
    f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style>{FIT_JS}</head><body>' +
    ''.join(f'<section class="f" id="{i}" style="width:{w}px;height:{h}px">{c}</section>' for i, w, h, c in P) + '</body></html>')
json.dump(COMP, open(os.path.join(D, 'composicoes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'peças')
