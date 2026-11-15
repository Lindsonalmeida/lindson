# Semana 2 dos Reels da Orégano Turbo (OT-22 a OT-30, fecha os 30). 15/11/2026, conta Zuleide, agente Paollo + Rocco + Social media + Copy.
# Mesma identidade, motor e voz da semana 1 (pt-BR-AntonioNeural +4%). 6 de conteúdo + 3 de venda (total 30 = 21 conteúdo / 9 venda).
# Acrescenta OT-22..30 ao roteiros.json (mantém OT-01..21) e grava motor/producao/OT-NN.json. Fotos Pexels NOVAS (nunca usadas), em ../fotos/.
import json, os, re
H = os.path.dirname(os.path.abspath(__file__))
TRILHAS = ['pop-track-03-108bpm.mp3', 'trap-electro-vibes-112bpm.mp3', 'midnight-funk-117bpm.mp3']
DIAS = ['23/11', '24/11', '25/11']; HORAS = ['12:10', '19:10', '23:40']

def F(n, t, **k): return ('fotofull', n, t, k)
def I(n, t, **k): return ('impacto', n, t, k)
def Q(n, t, **k): return ('frase', n, t, k)
def B(n, t, clip, **k): return ('banco', n, t, dict(clip=clip, **k))
def LI(n, tit, itens, em, **k): return ('lista', n, [], dict(titulo=tit, itens=itens, tempos_em=em, **k))
def CH(n, nome, msgs, em, **k): return ('chat', n, [], dict(nome=nome, msgs=msgs, tempos_em=em, **k))
def C(n, etiquetas): return ('cta', n, [], dict(etiquetas=etiquetas, vfx=['leak']))

R = [
 # ---------------- DIA 8 (23/11) ----------------
 dict(t='conteudo', linha='Técnica de massa', titulo='Molho cru ou cozido: o que a napolitana usa', palavra='MOLHO', capa=('MOLHO', 'Cru ou cozido?', 'O molho da pizza'),
  fotos=['32449727', '18437686'], entrega='Te mando a receita base de molho cru pra testar.', cenas=[
  F('Molho de pizza: cru ou cozido?', ['Cru ou', 'cozido?'], hl=[1], hit=['cozido'], vfx=['punch']),
  I('Na napolitana tradicional, o molho vai cru. Sem panela, sem refogar.', ['Molho', 'cru'], hl=[1], hit=['cru']),
  Q('Ele cozinha junto com a pizza, dentro do forno, e fica com gosto de tomate fresco.', ['Cozinha', 'no forno'], carimbo='NAPOLITANA', carimboAt='forno'),
  LI('Tomate pelado amassado, sal e um fio de azeite. Só isso.', 'Molho cru', [['1', 'Tomate pelado'], ['2', 'Sal'], ['3', 'Azeite']], ['tomate', 'sal', 'azeite']),
  B('Fica mais vermelho na foto, e ainda poupa uma panela no fogão da cozinha.', ['Mais', 'vermelho'], 'cafe-instagram', hl=[1]),
  C('Comenta MOLHO que eu te mando a receita base pra testar.', ['Receita', 'Molho cru']),
  I('Testa numa pizza só.', ['Testa numa', 'pizza só'], hl=[1])]),
 dict(t='conteudo', linha='Bastidor', titulo='Foto de pizza no celular: 3 ajustes que mudam o cardápio', palavra='FOTO', capa=('FOTO', 'Sua pizza é linda.', 'E a foto?'),
  fotos=['14538481', '19786235'], entrega='Te mando o guia de foto de pizza no celular.', cenas=[
  F('Sua pizza é linda. Por que a foto não mostra isso?', ['E a', 'foto?'], hl=[1], hit=['foto'], vfx=['punch']),
  LI('Luz de janela, de lado. Celular de cima. E limpa a lente antes.', '3 ajustes', [['1', 'Luz de janela'], ['2', 'Foto de cima'], ['3', 'Lente limpa']], ['janela', 'cima', 'lente']),
  I('Nada de flash na cozinha escura.', ['Sem', 'flash'], hl=[1], hit=['flash'], vfx=['glitch'], som_hit='glitch-quebra'),
  Q('Fotografa a pizza saindo do forno, com o queijo ainda brilhando.', ['Saindo', 'do forno'], carimbo='NA HORA', carimboAt='brilhando'),
  B('É essa foto que o cliente vê antes de pedir.', ['Antes de', 'pedir'], 'rolando-feed-cama', hl=[1]),
  C('Comenta FOTO que eu te mando o guia de foto no celular.', ['Guia', 'No celular']),
  I('Troca a foto hoje.', ['Troca a', 'foto hoje'], hl=[1])]),
 dict(t='venda', linha='Raio-X', titulo='Quanto tempo sua pizzaria demora pra responder no WhatsApp?', palavra='ZAP', capa=('ZAP', 'Quanto tempo o cliente', 'espera sua resposta?'),
  fotos=['16055182', '27647972'], entrega='Te mando como pedir o Raio-X do seu atendimento.', cenas=[
  F('Quanto tempo o cliente espera a sua resposta no WhatsApp?', ['Quanto tempo', 'ele espera?'], hl=[1], hit=['WhatsApp'], vfx=['punch']),
  CH('Ele mandou: tem calabresa? E ninguém respondeu.', 'Cliente', [['ele', 'Boa noite! Tem calabresa?'], ['ele', 'Oi?? 👀']], ['calabresa', 'ninguém']),
  I('Com fome, ele pede em outro lugar.', ['Pede em', 'outro lugar'], hl=[1], hit=['lugar']),
  Q('Mensagem pronta, cardápio fixado e alguém olhando o celular na hora do pico.', ['Hora do', 'pico'], carimbo='ATENDIMENTO', carimboAt='pico'),
  B('No Raio-X a gente olha o seu atendimento junto com você.', ['Raio-X do', 'atendimento'], 'respondendo-whatsapp', hl=[1]),
  C('Comenta ZAP que eu te explico como pedir o Raio-X.', ['Raio-X', 'Só pizzarias']),
  I('Resposta rápida vende.', ['Resposta', 'rápida'], hl=[1])]),
 # ---------------- DIA 9 (24/11) ----------------
 dict(t='conteudo', linha='Curiosidade', titulo='Pizza de calabresa: o sabor mais brasileiro do cardápio', palavra='SABOR', capa=('CALABRESA', 'O sabor mais', 'brasileiro da pizzaria'),
  fotos=['40262802', '6068713'], entrega='Te mando 5 ideias de nome para sabores da casa.', cenas=[
  F('A calabresa é o sabor mais brasileiro da pizzaria.', ['Sabor', 'brasileiro'], hl=[1], hit=['brasileiro'], vfx=['punch']),
  I('O nome vem da Calábria, no sul da Itália.', ['Calábria', 'Itália'], hl=[0], hit=['Calábria']),
  Q('Mas a pizza de calabresa com cebola, do jeito que a gente come, é coisa nossa.', ['Coisa', 'nossa'], carimbo='BRASIL', carimboAt='nossa'),
  LI('Calabresa, portuguesa, frango com catupiry. Sabores que o cliente já conhece.', 'Clássicos', [['1', 'Calabresa'], ['2', 'Portuguesa'], ['3', 'Frango catupiry']], ['calabresa', 'portuguesa', 'frango']),
  B('Dá um nome da casa pro clássico e ele vira assinatura.', ['Nome', 'da casa'], 'celular-noite-digitando', hl=[1]),
  C('Comenta SABOR que eu te mando cinco ideias de nome pra sabor da casa.', ['5 nomes', 'Sabor da casa']),
  I('Qual é o seu campeão?', ['Qual é seu', 'campeão?'], hl=[1])]),
 dict(t='conteudo', linha='Gestão', titulo='A caixa de pizza é a mídia mais vista da sua marca', palavra='CAIXA', capa=('CAIXA', 'A mídia que entra', 'na casa do cliente'),
  fotos=['17403901', '6151210'], entrega='Te mando 5 ideias de cartão para a caixa.', cenas=[
  F('Qual anúncio entra na casa do cliente e fica na mesa por meia hora?', ['Entra na', 'casa dele'], hl=[1], hit=['mesa'], vfx=['punch']),
  I('A caixa da sua pizza.', ['A caixa'], hl=[0], hit=['caixa']),
  LI('Adesivo com a marca, cartão com o WhatsApp e um código pro próximo pedido.', 'Na caixa', [['1', 'Adesivo da marca'], ['2', 'Cartão com zap'], ['3', 'Código do pedido']], ['adesivo', 'cartão', 'código']),
  Q('Assim o próximo pedido vem direto pra você.', ['Direto', 'pra você'], carimbo='CANAL PRÓPRIO', carimboAt='você'),
  B('Custa pouco e trabalha toda noite.', ['Toda', 'noite'], 'cidade-noite', hl=[1]),
  C('Comenta CAIXA que eu te mando cinco ideias de cartão pra caixa.', ['5 cartões', 'Pra caixa']),
  I('Olha sua caixa hoje.', ['Olha sua', 'caixa'], hl=[1])]),
 dict(t='venda', linha='Método', titulo='Por que a Orégano Turbo só trabalha com pizzaria', palavra='PIZZARIA', capa=('SÓ PIZZA', 'Por que a gente', 'só atende pizzaria'),
  fotos=['32641694', '29626981'], entrega='Te mando como funciona o Raio-X da sua pizzaria.', cenas=[
  F('A gente não atende hamburgueria, açaí nem sushi.', ['Só', 'pizzaria'], hl=[1], hit=['sushi'], vfx=['punch']),
  I('Só pizzaria.', ['Só', 'pizzaria'], hl=[1], hit=['pizzaria']),
  LI('Porque pizzaria tem noite de pico, forno lotado, motoboy e caixa. É outro jogo.', 'Outro jogo', [['1', 'Noite de pico'], ['2', 'Forno lotado'], ['3', 'Motoboy e caixa']], ['pico', 'forno', 'motoboy']),
  Q('Quem só faz isso conhece o seu dia a dia.', ['Seu dia', 'a dia'], carimbo='ESPECIALISTA', carimboAt='dia'),
  B('O primeiro passo é o Raio-X da sua pizzaria.', ['Primeiro', 'o Raio-X'], 'empreendedora-notebook', hl=[1]),
  C('Comenta PIZZARIA que eu te explico como funciona o Raio-X.', ['Raio-X', 'Só pizzarias']),
  I('Feito pra quem tem forno.', ['Pra quem', 'tem forno'], hl=[1])]),
 # ---------------- DIA 10 (25/11) ----------------
 dict(t='conteudo', linha='Humor de dono', titulo='POV: sexta, nove da noite, e o motoboy não chegou', palavra='SEXTA', capa=('SEXTA', 'Nove da noite', 'e cadê o motoboy?'),
  fotos=['27927612', '1653877'], entrega='Te mando o checklist da sexta à noite.', cenas=[
  F('POV: sexta, nove da noite. Dez pizzas prontas e o motoboy não chegou.', ['POV:', 'sexta 21h'], hl=[1], hit=['chegou'], vfx=['punch']),
  CH('O cliente já mandou mensagem.', 'Cliente', [['ele', 'Já saiu??'], ['ele', 'Tô com fome 😩']], ['cliente', 'mensagem']),
  I('E o queijo esfriando na caixa.', ['Queijo', 'esfriando'], hl=[1], hit=['esfriando']),
  LI('Motoboy reserva, escala fechada até quinta e aviso ao cliente antes dele perguntar.', 'Na sexta', [['1', 'Motoboy reserva'], ['2', 'Escala na quinta'], ['3', 'Avisa antes']], ['reserva', 'escala', 'aviso'], compacto=True),
  B('Sexta boa se prepara na quinta.', ['Prepara', 'na quinta'], 'notificacao-acorda', hl=[1]),
  C('Comenta SEXTA que eu te mando o checklist da sexta à noite.', ['Checklist', 'Sexta']),
  I('Marca seu motoboy.', ['Marca seu', 'motoboy'], hl=[1])]),
 dict(t='conteudo', linha='Resposta pronta', titulo='Avaliação ruim no iFood ou no Google: como responder', palavra='AVALIAÇÃO', capa=('1 ESTRELA', 'Avaliação ruim?', 'Responde assim'),
  fotos=['12288359', '17402721'], entrega='Te mando 5 respostas prontas para avaliação ruim.', cenas=[
  F('Chegou avaliação de uma estrela. E agora?', ['Uma', 'estrela'], hl=[1], hit=['estrela'], vfx=['punch']),
  I('Primeiro: não responde com raiva.', ['Sem', 'raiva'], hl=[1], hit=['raiva']),
  Q('Quem lê a resposta é o próximo cliente, não só quem reclamou.', ['O próximo', 'cliente'], carimbo='TODOS LEEM', carimboAt='reclamou'),
  CH('Agradece, pede desculpa e chama pro privado pra resolver.', 'Resposta', [['eu', 'Obrigado por avisar e desculpa pela experiência. Chama a gente no WhatsApp pra resolver? (ilustrativo)']], ['agradece', 'privado']),
  B('Resposta educada mostra que tem dono cuidando.', ['Tem dono', 'cuidando'], 'sorrindo-no-celular', hl=[1]),
  C('Comenta AVALIAÇÃO que eu te mando cinco respostas prontas.', ['5 respostas', 'Avaliação']),
  I('Responde todas.', ['Responde', 'todas'], hl=[1])]),
 dict(t='venda', linha='Chamada para diagnóstico', titulo='Antes de impulsionar o post da pizzaria, olhe isto', palavra='ANÚNCIO', capa=('IMPULSIONAR', 'Antes de apertar', 'esse botão'),
  fotos=['20793369', '36375362'], entrega='Te mando como pedir o Raio-X antes do anúncio.', cenas=[
  F('Antes de apertar o botão impulsionar, olha isto.', ['Antes de', 'impulsionar'], hl=[1], hit=['impulsionar'], vfx=['punch']),
  LI('Pra onde o cliente vai depois do clique? Tem cardápio? Tem alguém respondendo?', 'Depois do clique', [['?', 'Pra onde vai'], ['?', 'Tem cardápio'], ['?', 'Quem responde']], ['clique', 'cardápio', 'respondendo']),
  I('Se não tem, o anúncio para no vazio.', ['Para no', 'vazio'], hl=[1], hit=['vazio']),
  Q('Anúncio bom precisa de caminho pronto até o pedido.', ['Caminho', 'até o pedido'], carimbo='PRIMEIRO ISSO', carimboAt='pedido'),
  B('O Raio-X mostra esse caminho na sua pizzaria.', ['O seu', 'caminho'], 'rolando-pagina-venda', hl=[1]),
  C('Comenta ANÚNCIO que eu te explico como pedir o Raio-X.', ['Raio-X', 'Antes do anúncio']),
  I('Primeiro o caminho.', ['Primeiro', 'o caminho'], hl=[1])]),
]

rot = json.load(open(os.path.join(H, 'roteiros.json')))
rot['reels'] = [r for r in rot['reels'] if r['ordem'] <= 21]; rot['leva'] = 'Reels Orégano Turbo · semanas 1 e 2 (30)'
lista = json.load(open(os.path.join(H, 'fotos', 'lista.json'))); cat = {}
for c in json.load(open(os.path.join(H, '..', '..', 'bancos', 'pexels-pizza', 'catalogo.json')))['categorias']:
    for f in c['fotos']: cat[f['id']] = c['categoria']
usadas = {f['id'] for f in lista[:42]}
for k, r in enumerate(R):
    nn = 22 + k; rid = f'OT-{nn:02d}'; fot = list(r['fotos'])
    assert not (set(fot) & usadas), rid; usadas |= set(fot)
    cenas_r, cenas_p = [], []
    for tipo, narr, tela, ex in r['cenas']:
        cenas_r.append(dict(narracao=narr, texto_tela=' '.join(tela), texto_tela_palavras=tela or ['·']))
        p = dict(tipo=tipo, texto=tela, **{x: y for x, y in ex.items()})
        if tipo in ('fotofull', 'cta'):
            i = fot.pop(0); p['foto'] = i + '.jpg'; p['_cred'] = f'https://www.pexels.com/photo/{i}/'
        if tipo == 'impacto': p.setdefault('size', 200); p.setdefault('top', 640); p.setdefault('flash', True)
        if tipo == 'banco': p.setdefault('size', 170); p.setdefault('top', 560); p.setdefault('vfx', ['punch'])
        if tipo == 'frase': p.setdefault('size', 170); p.setdefault('top', 560)
        if tipo == 'fotofull': p.setdefault('top', 470); p.setdefault('size', 180)
        cenas_p.append(p)
    frases = re.split(r'(?<=[.?!])\s+', ' '.join(c['narracao'] for c in cenas_r)); blocos = ['']
    for f in frases:
        if len(blocos[-1]) + len(f) + 1 > 220: blocos.append('')
        blocos[-1] = (blocos[-1] + ' ' + f).strip()
    capa_foto = next(p['foto'] for p in cenas_p if p['tipo'] in ('fotofull', 'cta'))
    pal, man, cx = r['capa']
    rot['reels'].append(dict(id=rid, ordem=nn, post=dict(data=DIAS[k // 3], hora=HORAS[k % 3]), titulo=r['titulo'], tipo=r['t'],
        linha_editorial=r['linha'], capa_cor='preto', cta_palavra=r['palavra'], entrega_no_video=r['entrega'], blocos_voz=blocos, cenas=cenas_r))
    json.dump(dict(_nota='Ficha OT semana 2 (15/11/2026). Fotos Pexels (licença livre) em ../fotos/, nunca usadas antes.', beat_sync=True, voz_rate='+4%', voz_max=27.5,
                   trilha=TRILHAS[k % 3], trilha_ini=[14, 32, 24][k % 3],
                   capa=dict(foto=capa_foto, palavra=pal, manchete=man, caixa=cx, rotulo=r['linha'], wordTop=330, wordSize={4: 420, 5: 340, 6: 290, 7: 250, 8: 220, 9: 200}.get(len(pal), 170), headTop=1290, tagTop=1225, auto=False, fx=0, fy=0, fw=1080),
                   cenas=cenas_p), open(os.path.join(H, 'motor', 'producao', rid + '.json'), 'w'), ensure_ascii=False, indent=1)
    for i in r['fotos']:
        if not any(x['id'] == i for x in lista): lista.append(dict(id=i, cat=cat.get(i, ''), pagina=f'https://www.pexels.com/photo/{i}/'))
json.dump(rot, open(os.path.join(H, 'roteiros.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(lista, open(os.path.join(H, 'fotos', 'lista.json'), 'w'), ensure_ascii=False, indent=0)
print(len(R), 'reels; total', len(rot['reels']), '; venda', sum(r['tipo'] == 'venda' for r in rot['reels']))
