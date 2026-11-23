# 5 roteiros prontos (OT-31 a OT-35) no formato de ../reels/roteiros.json (conta Leandro, 23/11/2026)
import json
def r(id_,data,hora,tit,tipo,linha,etapa,visual,cor,cta,entrega,cenas,legenda):
    falas=[c[0] for c in cenas]
    meio=len(falas)//2
    return dict(id=id_,post=dict(data=data,hora=hora),titulo=tit,tipo=tipo,linha_editorial=linha,etapa_funil=etapa,visual=visual,capa_cor=cor,
      cta_palavra=cta,entrega_no_video=entrega,blocos_voz=[' '.join(falas[:meio]),' '.join(falas[meio:])],
      cenas=[dict(narracao=n,texto_tela=t,texto_tela_palavras=t.split(' ',1) if ' ' in t else [t],imagem=i) for n,t,i in cenas],legenda=legenda)
R=[
r('OT-31','26/11','12:10','Quanto o app leva de cada pizza','conteudo','Dinheiro que vaza','Topo','Pizza real (vídeo)','preto','TAXA',
 'Te mando a conta da taxa numa planilha simples.',
 [('O aplicativo comeu sua margem?','Comeu sua margem?','vídeo: pizza sendo fatiada em close, fundo escuro'),
  ('Pega uma pizza de sessenta reais.','Pizza de R$ 60','mesma pizza, preço em tipografia grande (ilustrativo)'),
  ('Tira a taxa que está no seu contrato com o app. Tira a entrega, a caixa, o queijo e a massa.','Tira, tira, tira','fatias saindo uma a uma da pizza a cada item'),
  ('Sobra quanto pra você? A maioria dos donos nunca fez essa conta no papel.','Sobra quanto?','uma fatia sozinha na tábua'),
  ('O app traz cliente novo. O problema é o cliente que já é seu pedir lá todo mês.','Cliente seu, taxa deles','vídeo: celular com o app aberto na mão do motoboy'),
  ('Comenta TAXA que eu te mando a conta numa planilha simples. Faz com o seu número.','Comenta TAXA','Seu Turbo aponta para o texto, logo no canto')],
 'Taxa do iFood na pizzaria: quanto sobra de cada pizza\n\nVocê sabe quanto sobra de uma pizza vendida pelo aplicativo? ...\n(legenda SEO completa: gerar com ../reels/legendas_seo.py no padrão aprovado)\n#pizzaria #donodepizzaria #ifood #gestaodepizzaria #saoluis'),
r('OT-32','26/11','19:10','Foto de pizza no celular com luz da janela','conteudo','Aula rápida','Meio','Tela real (gravação)','creme','FOTO',
 'Te mando o checklist de 5 itens da foto que dá fome.',
 [('Sua foto de pizza tira a fome do cliente?','Tira a fome?','gravação real: foto escura de pizza com luz amarela de teto'),
  ('O erro mais comum é a luz do teto. Ela deixa o queijo amarelo e a borda sem cor.','Luz do teto: não','mesma pizza, comparação lado a lado gravada'),
  ('Leva a pizza pra perto da janela. Luz de lado, sem flash.','Luz da janela','gravação: celular sendo levado até a janela'),
  ('Fotografa de cima ou num ângulo baixo, na altura da borda.','De cima ou baixo','tela do celular: modo câmera, grade ligada'),
  ('E puxa uma fatia. Queijo esticando vende mais do que pizza inteira parada.','Puxa a fatia','vídeo real: fatia puxada com queijo esticando'),
  ('Comenta FOTO que eu te mando o checklist de cinco itens. Testa na pizza de hoje.','Comenta FOTO','Seu Turbo com joinha')],
 'Foto de pizza no celular: 3 ajustes de luz e ângulo\n...\n#fotodepizza #pizzaria #marketingparapizzaria #donodepizzaria #fotografiadecomida'),
r('OT-33','26/11','23:40','O que vem no Raio-X grátis do Instagram','venda','Raio-X','Fundo','Seu Turbo','verde','RAIO-X',
 'Te mando como pedir o Raio-X grátis do seu Instagram.',
 [('Seu perfil espanta cliente e você nem percebe?','Seu perfil espanta?','Seu Turbo surpreso, fundo verde forno'),
  ('A gente grava um vídeo curto olhando o Instagram da sua pizzaria.','Um vídeo sobre o SEU perfil','gravação real de tela: rolagem de um perfil de exemplo (pizzaria fictícia)'),
  ('Três coisas: a foto, a bio com o link, e o caminho até o seu WhatsApp.','Foto · bio · WhatsApp','Seu Turbo conta nos dedos 1, 2, 3'),
  ('Você recebe o que mudar primeiro, em ordem. Sem enrolação e sem custo.','Em ordem. Sem custo.','tipografia grande, pizza real ao fundo desfocada'),
  ('Comenta RAIO-X que eu te mando como pedir. Só pizzaria.','Comenta RAIO-X','Seu Turbo aponta, logo e @oreganoturbo')],
 'Raio-X grátis do Instagram da pizzaria: o que a gente olha\n...\n#raioxdapizzaria #marketingparapizzaria #instagramparapizzaria #pizzaria #nordeste'),
r('OT-34','27/11','12:10','POV: cliente pede "manda o cardápio" e some','conteudo','Humor de dono','Topo','Seu Turbo','tomate','SUMIU',
 'Te mando a mensagem que traz esse cliente de volta.',
 [('Mandou o cardápio. Sumiu.','Mandou. Sumiu.','Seu Turbo olhando o celular, expressão hmm'),
  ('POV: o cliente pede o cardápio, você manda o PDF de doze páginas...','PDF de 12 páginas','Seu Turbo segurando um PDF enorme que cai até o chão'),
  ('e ele visualiza e não responde nunca mais.','Visualizou.','Seu Turbo com cara de choque, som de grilo'),
  ('Cardápio grande demais trava a escolha. Manda os três mais pedidos e pergunta qual ele quer.','3 sabores + 1 pergunta','pizza real: três pizzas lado a lado em vídeo'),
  ('Pergunta fecha pedido. PDF abre conversa e some.','Pergunta fecha','Seu Turbo confiante'),
  ('Comenta SUMIU que eu te mando a mensagem pra trazer esse cliente de volta. Marca quem já viveu isso.','Comenta SUMIU','Seu Turbo acenando')],
 'Cliente pede cardápio e some no WhatsApp: o que fazer\n...\n#whatsappparapizzaria #donodepizzaria #pizzariadelivery #atendimento #pizzaria'),
r('OT-35','27/11','19:10','Resposta pronta para "tá caro"','conteudo','Aula rápida','Meio','Tela real (gravação)','preto','CARO',
 'Te mando 3 respostas prontas para "tá caro".',
 [('"Tá caro" não é um não.','"Tá caro" ≠ não','gravação real de WhatsApp de exemplo: mensagem "tá caro"'),
  ('Quando o cliente diz que tá caro, ele está pedindo um motivo pra pagar.','Ele pede um motivo','pizza real saindo do forno'),
  ('Não baixa o preço. Responde com o que ele leva: tamanho, ingrediente, tempo de entrega.','Não baixa. Explica.','gravação: digitando a resposta, sem nome de cliente real'),
  ('E oferece uma opção menor, sem desconto. Média em vez de grande.','Opção menor','tipografia + fatia real'),
  ('Assim ele escolhe entre duas pizzas, e não entre você e o concorrente.','Escolhe entre duas','Seu Turbo apresenta'),
  ('Comenta CARO que eu te mando três respostas prontas pra copiar.','Comenta CARO','logo e @oreganoturbo')],
 'Cliente disse que a pizza está cara: 3 respostas sem dar desconto\n...\n#precodepizza #pizzaria #vendasnowhatsapp #donodepizzaria #saoluis'),
]
json.dump(dict(leva='Funil · OT-31 a OT-35',criado='2026-11-23',conta='Leandro',reels=R),open('roteiros-ot31-35.json','w'),ensure_ascii=False,indent=1)
L=['# 5 roteiros prontos para produzir · OT-31 a OT-35 (conta Leandro, 23/11/2026)','',
'Formato igual aos 21 Reels aprovados (`../reels/roteiros.json`: blocos de voz + cenas com texto de tela). Dados para o motor: `roteiros-ot31-35.json`. Voz Antonio +4% (só Orégano), 20 a 30 s, gancho na tela no 1º segundo, SFX nos cortes, trilha com crédito, -14 LUFS.','',
'**Produção:** pizza real = vídeo real (banco de vídeo/gravação/Cinema IA), nunca foto parada com zoom; tela real = gravação de celular com perfil/conversa de exemplo, sem dado de cliente real; Seu Turbo pelo `../mascote/demo/fazer.py`. Composição copiada dos Reels aprovados (sistema v4: comanda, tomate/verde/creme/carvão, Bagel). Legenda SEO completa sai do `../reels/legendas_seo.py`. Valor de pizza no OT-31 é **ilustrativo** (escrever na tela).','']
for x in R:
    L+=[f"## {x['id']} · {x['titulo']}",f"{x['post']['data']} às {x['post']['hora']} · {x['etapa_funil']} · {x['linha_editorial']} · visual: {x['visual']} · capa {x['capa_cor']} · CTA **{x['cta_palavra']}** ({x['entrega_no_video']})",'',
        '| # | Narração | Texto na tela | Imagem |','|---|---|---|---|']
    for i,c in enumerate(x['cenas'],1): L.append(f"| {i} | {c['narracao']} | {c['texto_tela']} | {c['imagem']} |")
    L+=['',f"**Título da legenda:** {x['legenda'].splitlines()[0]}  ",f"**Hashtags:** {x['legenda'].splitlines()[-1]}",'']
open('ROTEIROS-OT31-35.md','w').write('\n'.join(L))
