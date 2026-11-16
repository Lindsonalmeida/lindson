# Gera stories/PROMPTS-GEMINI.md a partir das cenas de stories.py (conta Leandro, 16/11/2026)
import sys; sys.argv=['x','.','.','.']
src=open(__file__.replace('prompts.py','stories.py')).read().split('async def main')[0]
src=src.replace("REC,CEN,NF=[pathlib.Path(a) for a in sys.argv[1:4]]","REC=CEN=NF=pathlib.Path('.')")
exec(src)
CENA={PALCO:'em pé diante de uma cortina de veludo vermelho de teatro, um canhão de luz de palco recortando ele do escuro, poeira no feixe',
POKER:'sentado a uma mesa de pôquer de feltro verde num salão escuro e esfumaçado, segurando cartas, fichas na mesa, luz pendente de tungstênio sobre a mesa',
XADREZ:'debruçado sobre um tabuleiro de xadrez gigante de madeira, mão sobre o rei, peças em primeiro plano desfocadas',
CAVALOS:'num salão escuro com peças de xadrez enormes (cavalo preto e cavalo branco) ao lado dele, luz lateral dura de cinema',
LUVAS:'num ringue de boxe escuro, luvas pretas penduradas no ombro do terno, holofotes do ringue no alto, fumaça',
DINHEIRO:'segurando um leque de notas de real na mão em primeiro plano, mesa de escritório escura, luz quente lateral',
QUEDA:'diante de uma parede de telas com gráfico vermelho caindo, rosto iluminado pelo vermelho das telas, sala escura',
PROJETOR:'em pé no feixe de luz de um projetor de cinema numa sala escura, poeira no feixe, sombra dele na parede',
NEON:'numa rua noturna de São Luís com letreiros de neon desfocados ao fundo, reflexo de neon no rosto e no asfalto molhado'}
NICHO={'1505664194779-8beaceb93744':'numa biblioteca jurídica antiga com estantes de livros de couro e bustos de mármore','1589829545856-d10d557cf95f':'ao lado de uma estátua de bronze da Justiça com a balança, escritório escuro','1450101499163-c8848c66ca85':'assinando um contrato com caneta-tinteiro numa mesa de madeira escura','1521791055366-0d553872125f':'segurando um contrato assinado, mesa de escritório de advocacia, luz de janela','1497366216548-37526070297c':'num corredor de escritório moderno de vidro, à noite',
'1622286342621-4bd786c2447c':'dentro de uma barbearia escura, barbeiro cortando cabelo desfocado em primeiro plano','1503951914875-452162b0f3f1':'numa barbearia vintage à noite, cliente com toalha quente na cadeira ao fundo','1585747860715-2ba37e788b70':'no centro de uma barbearia de tijolinho com três cadeiras de couro e luminárias pendentes','1621605815971-fbc98d665033':'numa bancada de barbearia com máquinas, navalha e pomada em primeiro plano','1599351431202-1e0f0137899a':'numa barbearia, barbeiro tatuado fazendo degradê ao fundo',
'1598256989800-fe5f95da9787':'num consultório odontológico moderno com cadeira laranja vazia ao lado dele','1588776814546-1ffcf47267a5':'diante de um negatoscópio com radiografias dentárias acesas','1629909613654-28e377c37b09':'num consultório odontológico branco e limpo, luz suave','1606811971618-4486d14f3f99':'na recepção de uma clínica odontológica premium, balcão de mármore'}
L=['# Prompts para o Gemini · 30 Stories de venda (conta Leandro, 16/11/2026)','',
'O Lindson gera as cenas no Gemini (app). Cada prompt vira **1 imagem 9:16 sem texto**, salva em `stories/cenas-gemini/<nicho>/NN.jpg` (adv, barba, dente). Depois rode `python3 gerador/stories.py <recortes> <cenas> <fotos_nicho>`: o layout usa a imagem do Gemini no lugar da composição provisória e coloca título, palavra neon/itálico, CTA e assinatura por cima.',
'','**Anexar em todo prompt:** 2 fotos reais do Lindson (privado `membros/img/`): a indicada + `c13.jpg` (rosto de frente). Descarte a imagem se o rosto não parecer ele.',
'**Base fixa (cole no fim de todos):** "Use a foto anexada como referência do rosto: mantenha o rosto, a barba, o tom de pele e o corpo dele idênticos. Terno azul-marinho, camisa branca aberta no colarinho, relógio prata. Fotografia cinematográfica fotorrealista, lente 50 mm f/1.8, grão de filme, proporção 9:16 vertical. Ele ocupa a metade de baixo do quadro; deixe o terço de cima mais escuro e limpo para texto. Sem texto, sem letras, sem logotipo na imagem."','',
'Estilos: **impacto** (stories ímpares 01, 03…: metáfora forte, luz dura de cinema, contraste alto) · **editorial** (pares 02, 04…: luz quente dourada de fim de tarde, tons de café e couro, muito ar, elegância).','']
for n,nome in [('adv','Advogados'),('barba','Barbeiros'),('dente','Dentistas')]:
  L+=[f'## {nome}','','| # | Estilo | Anexar | Prompt (cena) | Texto que entra depois |','|---|---|---|---|---|']
  for i,(cena,nicho,k,l1,neon,l3,apoio,lay) in enumerate(S[n]):
    est='editorial' if i%2 else 'impacto'
    pose={'c':'centralizado, olhando para a câmera, braços cruzados ou mão no paletó','l':'no lado esquerdo do quadro, corpo três-quartos, olhando para a câmera','r':'no lado direito do quadro, apoiado numa mesa, olhando para a câmera'}[lay]
    luz='luz dourada quente de janela, atmosfera de café e couro' if est=='editorial' else 'luz dura lateral de cinema, contraluz forte, fumaça leve'
    desc=CENA.get(cena) or NICHO[cena]
    L.append(f'| {i+1:02d} | {est} | c{ORD[n][i]}.jpg + {"c07" if ORD[n][i]=="13" else "c13"}.jpg | Homem da foto {desc}, {pose}, {luz}. + base fixa | {l1} / **{neon}** / {l3} |')
  L.append('')
open(B/'stories/PROMPTS-GEMINI.md','w').write('\n'.join(L)); print('ok')
