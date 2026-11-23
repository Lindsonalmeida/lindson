# Leva viral (23/11/2026, conta Leandro, Paollo + Rocco + Social media + Copy): OT-31 TAXA, OT-34 CARO, OT-35 SUMIU do funil v2,
# todos com CTA RAIO-X (pedido do Lindson: viralizar). Mesmo motor/identidade/voz dos 21 aprovados (Antonio +4%).
# Sem fotofull (foto parada com zoom é reprovada): só tipografia em movimento, chat, lista, split, vídeo de banco e pizza girando na CTA.
# Loop: a última frase devolve ao gancho. Fotos Pexels novas (nunca usadas) em ../fotos/.
import json, os, re
H = os.path.dirname(os.path.abspath(__file__))
def I(n, t, **k): return ('impacto', n, t, k)
def Q(n, t, **k): return ('frase', n, t, k)
def B(n, t, clip, **k): return ('banco', n, t, dict(clip=clip, **k))
def LI(n, tit, itens, em, **k): return ('lista', n, [], dict(titulo=tit, itens=itens, tempos_em=em, **k))
def CH(n, nome, msgs, em, **k): return ('chat', n, [], dict(nome=nome, msgs=msgs, tempos_em=em, **k))
def V(n, t, clip, **k): return ('banco', n, t, dict(clip='vb-'+clip, top=200, size=150, **k))
def SP(n, e, d, **k): return ('split', n, [], dict(esq=e, dir=d, **k))
CTA = ('cta', 'Comenta RAIO-X que eu te mando o link do Raio-X grátis da sua pizzaria.', [], dict(etiquetas=['Raio-X grátis', 'Só pizzarias'], vfx=['leak']))
ENT = 'Te mando o link do Raio-X grátis da sua pizzaria.'
R = [
 dict(id='OT-35', nn=35, titulo='POV: o cliente pede o cardápio e some', linha='Humor de dono', foto='33593003', trilha='trap-electro-vibes-112bpm.mp3', ini=32,
  capa=('SUMIU', 'Mandou o cardápio.', 'E ele sumiu.'), cenas=[
  V('Mandou o cardápio. Sumiu.', ['Mandou.', 'Sumiu.'], 'close-up-shot-of-a-freshly-made-hot-pizza', hl=[1], hit=['Sumiu'], vfx=['punch', 'glitch'], som_hit='glitch-quebra'),
  CH('POV: o cliente pede o cardápio e você manda um PDF de doze páginas.', 'Cliente', [['ele', 'Boa noite! Manda o cardápio?'], ['eu', '📄 cardapio-completo.pdf · 12 páginas']], ['cardápio', 'PDF']),
  Q('Ele visualiza. E nunca mais responde.', ['Visualizou.', 'E sumiu.'], carimbo='VISTO ✓✓', carimboAt='nunca'),
  V('Cardápio grande demais trava a escolha.', ['Trava a', 'escolha'], 'waiter-serving-a-pizza-at-a-table', hl=[1], hit=['trava']),
  LI('Manda os três mais pedidos e pergunta qual ele quer.', 'Manda assim', [['1', 'Os 3 mais pedidos'], ['2', 'Uma pergunta'], ['3', 'Qual vai ser?']], ['três', 'pergunta', 'quer']),
  V('Pergunta fecha pedido. PDF abre conversa e some.', ['Pergunta', 'fecha pedido'], 'pizza-while-someone-takes-a-slice', hl=[1]),
  CTA,
  V('Ou manda o PDF de novo, e ele some.', ['Mandou.', 'Sumiu.'], 'close-up-shot-of-a-freshly-made-hot-pizza', hl=[1], hit=['some'])]),
 dict(id='OT-34', nn=34, titulo='Cliente disse "tá caro": responde sem dar desconto', linha='Resposta pronta', foto='5903317', trilha='pop-track-03-108bpm.mp3', ini=14,
  capa=('TÁ CARO', 'Não é um não.', 'Responde assim'), cenas=[
  V('Tá caro não é um não.', ['"Tá caro"', '≠ não'], 'chef-puts-the-pizza-in-the-oven', hl=[1], hit=['não'], vfx=['punch']),
  CH('Quando o cliente diz que tá caro, ele tá pedindo um motivo pra pagar.', 'Cliente', [['ele', 'Quanto tá a grande?'], ['ele', 'Hmm… tá caro 😬']], ['cliente', 'caro']),
  V('Não baixa o preço. Responde com o que ele leva.', ['Não baixa.', 'Explica.'], 'spreading-cheese-on-a-pizza', hl=[1]),
  LI('Tamanho, ingrediente e tempo de entrega.', 'O que ele leva', [['1', 'Tamanho'], ['2', 'Ingrediente'], ['3', 'Tempo de entrega']], ['tamanho', 'ingrediente', 'entrega']),
  SP('E oferece uma opção menor, sem desconto. Média em vez de grande.', 'Grande', 'Média'),
  V('Assim ele escolhe entre duas pizzas, e não entre você e o concorrente.', ['Entre duas', 'pizzas'], 'chef-shaping-a-pizza', hl=[1], hit=['concorrente']),
  CTA,
  V('Porque tá caro não é um não.', ['"Tá caro"', '≠ não'], 'chef-puts-the-pizza-in-the-oven', hl=[1], hit=['não'])]),
 dict(id='OT-31', nn=31, titulo='Taxa do app na pizzaria: quanto sobra de cada pizza', linha='Dinheiro que vaza', foto='40135592', trilha='midnight-funk-117bpm.mp3', ini=24,
  capa=('TAXA', 'O app comeu', 'sua margem?'), cenas=[
  V('O aplicativo comeu sua margem?', ['Comeu sua', 'margem?'], 'hot-oven-baking-pizzas', hl=[1], hit=['margem'], vfx=['punch']),
  Q('Pega uma pizza de sessenta reais. Valor de exemplo.', ['Pizza de', 'R$ 60'], carimbo='EXEMPLO', carimboAt='exemplo'),
  LI('Tira a taxa do seu contrato com o app. Tira a entrega, a caixa, o queijo e a massa.', 'Tira', [['−', 'Taxa do app'], ['−', 'Entrega'], ['−', 'Caixa'], ['−', 'Queijo e massa']], ['taxa', 'entrega', 'caixa', 'queijo'], compacto=True),
  I('Sobra quanto pra você?', ['Sobra', 'quanto?'], hl=[1], hit=['quanto'], vfx=['glitch'], som_hit='glitch-quebra'),
  B('Você já fez essa conta no papel?', ['Fez a conta', 'no papel?'], 'celular-noite-digitando', hl=[1]),
  SP('O app traz cliente novo. O problema é o cliente que já é seu pedir lá todo mês.', 'Cliente novo', 'Cliente seu'),
  CTA,
  V('Antes que o app coma a sua margem de novo.', ['Comeu sua', 'margem?'], 'hot-oven-baking-pizzas', hl=[1], hit=['margem'])]),
]
rot = json.load(open(os.path.join(H, 'roteiros.json')))
rot['reels'] = [r for r in rot['reels'] if r['id'] not in [x['id'] for x in R]]
for r in R:
    cr, cp = [], []
    for tipo, narr, tela, ex in r['cenas']:
        cr.append(dict(narracao=narr, texto_tela=' '.join(tela), texto_tela_palavras=tela or ['·']))
        p = dict(tipo=tipo, texto=tela, **ex)
        if tipo == 'cta': p['foto'] = r['foto'] + '.jpg'; p['_cred'] = f"https://www.pexels.com/photo/{r['foto']}/"
        if tipo == 'impacto': p.setdefault('size', 200); p.setdefault('top', 640); p.setdefault('flash', True)
        if tipo == 'banco': p.setdefault('size', 170); p.setdefault('top', 560); p.setdefault('vfx', ['punch'])
        if tipo == 'frase': p.setdefault('size', 170); p.setdefault('top', 560)
        cp.append(p)
    frases = re.split(r'(?<=[.?!])\s+', ' '.join(c['narracao'] for c in cr)); bl = ['']
    for f in frases:
        if len(bl[-1]) + len(f) + 1 > 220: bl.append('')
        bl[-1] = (bl[-1] + ' ' + f).strip()
    pal, man, cx = r['capa']
    rot['reels'].append(dict(id=r['id'], ordem=r['nn'], titulo=r['titulo'], tipo='conteudo', linha_editorial=r['linha'], capa_cor='preto',
        cta_palavra='RAIO-X', entrega_no_video=ENT, blocos_voz=bl, cenas=cr))
    json.dump(dict(_nota='Leva viral 23/11/2026 (conta Leandro). Foto Pexels nova.', beat_sync=True, voz_rate='+4%', voz_max=40, total_max=40, total_min=25,
        trilha=r['trilha'], trilha_ini=r['ini'],
        capa=dict(foto=r['foto'] + '.jpg', palavra=pal, manchete=man, caixa=cx, rotulo=r['linha'], wordTop=330, wordSize={4: 420, 5: 340, 6: 290, 7: 250}.get(len(pal), 220),
                  headTop=1290, tagTop=1225, auto=False, fx=0, fy=0, fw=1080), cenas=cp),
        open(os.path.join(H, 'motor', 'producao', r['id'] + '.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(rot, open(os.path.join(H, 'roteiros.json'), 'w'), ensure_ascii=False, indent=1)
print('ok', len(rot['reels']))
