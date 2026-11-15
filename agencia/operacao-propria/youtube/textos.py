# Gera TEXTOS.md (todos os textos do canal) a partir dos 21 Reels aprovados. Paollo + Peter, conta Zuleide, 15/11/2026.
import json, os
D = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(D, '../reels/roteiros.json')))['reels']
ZAP = 'https://wa.me/5598985621808?text=Quero%20o%20Raio-X%20da%20minha%20pizzaria%20%5BYT%5D'
SITE = 'https://oreganoturbo.pages.dev'
TAGS = {'História da pizza': '#historiadapizza', 'Humor de dono': '#donodepizzaria', 'Raio-X': '#marketingparapizzaria',
        'Dados do setor': '#mercadodepizza', 'Técnica de massa': '#massadepizza', 'Método': '#deliverydepizza',
        'Forno': '#fornodepizza', 'Resposta pronta': '#atendimentopizzaria', 'Chamada para diagnóstico': '#marketingparapizzaria',
        'Gestão': '#gestaodepizzaria', 'Curiosidade': '#curiosidadesdepizza', 'Ferramenta grátis': '#googlemeunegocio',
        'Bastidor': '#videoparapizzaria', 'Insumo': '#queijoparapizza', 'Dia da Pizza': '#diadapizza'}
o = ['# Canal do YouTube · Orégano Turbo · textos prontos', '', '_Paollo + Peter, conta Zuleide, 15/11/2026. Nada publicado; o canal ainda não foi criado._', '',
     '## Nome e @', '- **Nome do canal:** Orégano Turbo | Marketing para Pizzaria',
     '- **@ sugerido:** `@oreganoturbo` (mesmo do Instagram, `NOME-E-PERFIL.md`; reserva `@oregano.turbo`). Conferir se está livre no YouTube ao criar.', '',
     '## Descrição do canal (cole em Personalizar canal > Informações básicas)', '```',
     'Marketing para pizzaria, feito só para pizzarias.',
     '',
     'Aqui o dono de pizzaria aprende a vender mais no delivery, depender menos do aplicativo e trazer o cliente para o próprio WhatsApp. Sem fórmula mágica: conteúdo de quem vive forno, balcão e motoboy.',
     '',
     'O que você encontra:',
     '- Shorts todo dia: dicas rápidas de delivery, cardápio, atendimento e redes sociais',
     '- Aula nova toda quinta: um assunto da pizzaria explicado do começo ao fim',
     '- Raio-X ao vivo: perfis de pizzaria analisados com o que dá para melhorar já',
     '- Gestão: CMV, ficha técnica, dia fraco, taxa do app, Google Meu Negócio',
     '',
     'Quer saber o que está travando os pedidos da sua pizzaria? Peça o Raio-X gratuito pelo WhatsApp:',
     ZAP,
     '',
     'Site: ' + SITE,
     'Instagram: https://instagram.com/oreganoturbo',
     '',
     'Orégano Turbo · São Luís - MA · atendemos pizzarias de todo o Brasil.', '```', '',
     '## Links do canal (Personalizar > Links)',
     f'1. Peça o Raio-X da sua pizzaria → {ZAP}', f'2. Site → {SITE}', '3. Instagram → https://instagram.com/oreganoturbo', '',
     '## Palavras-chave do canal (Configurações > Canal > Palavras-chave)', '```',
     'marketing para pizzaria, pizzaria delivery, como vender mais pizza, dono de pizzaria, gestão de pizzaria, cardápio de pizzaria, ifood pizzaria, taxa do ifood, pizzaria no whatsapp, instagram para pizzaria, google meu negócio pizzaria, cmv pizzaria, ficha técnica pizza, abrir pizzaria, pizzaria São Luís, Orégano Turbo', '```', '',
     '## Roteiro do trailer (75 s, para quem ainda não se inscreveu) · voz Antonio', '',
     '| Tempo | Imagem | Narração |', '|---|---|---|',
     '| 0-5 s | Forno aceso, pá entrando, corte seco para celular sem pedido | "Forno quente. Massa pronta. E o celular… parado." |',
     '| 5-15 s | Tela do app com taxa, caixa de pizza fechando | "Se você é dono de pizzaria, sabe: fazer pizza boa é a parte fácil. Difícil é fazer o pedido chegar, e sem o aplicativo levar a metade." |',
     '| 15-35 s | Montagem rápida dos Shorts (Margherita, massa, CMV, upsell) | "Aqui no Orégano Turbo a gente fala só de pizzaria. Todo dia um Short: cardápio, atendimento, foto que dá fome, dia fraco, taxa do app." |',
     '| 35-55 s | Tela de Raio-X com faixa de scanner, comanda PEDIDO Nº | "Toda quinta, uma aula completa. E no Raio-X ao vivo, a gente abre o perfil de uma pizzaria e mostra o que dá pra melhorar hoje." |',
     '| 55-70 s | Pizza voando, logo, xadrez | "Sem promessa mágica. Só o que funciona no balcão, no forno e no WhatsApp." |',
     '| 70-75 s | Botão inscrever + comanda | "Se inscreve. E se quiser o Raio-X da sua pizzaria, o link está aqui embaixo." |', '',
     '**Título do trailer:** Marketing para pizzaria: o canal feito só para donos de pizzaria', '',
     '## Shorts · 21 títulos e descrições SEO (reaproveitam os Reels aprovados da semana 1)', '',
     '_Regra: título até 60 caracteres com a palavra-chave no começo; descrição com 1ª linha forte, link do Raio-X e 3 hashtags (tema + nicho + local). Postar o vídeo `reels/semana-1/NN/OT-NN.mp4` sem mudar nada, 1 por dia, às 12h._', '']
for r in R:
    n = r['id'][-2:]; tag = TAGS.get(r['linha_editorial'], '#pizzaria')
    t = r['titulo'] if len(r['titulo']) <= 70 else r['titulo'][:67] + '…'
    o += [f'### {r["id"]} · {r["linha_editorial"]} ({r["tipo"]})', f'**Título:** {t} #shorts', '', '```',
          f'{r["titulo"]}. {r["entrega_no_video"]} Comente {r["cta_palavra"]} ou chame no WhatsApp.',
          f'Raio-X gratuito da sua pizzaria: {ZAP}',
          f'{tag} #donodepizzaria #pizzariasaoluis', '```', '']
o += ['## 4 vídeos longos (16 a 20 min, toda quinta) · ideias e títulos', '',
      '1. **Dia fraco: 5 ações que enchem o forno na terça (sem dar desconto)**: o que fazer de segunda a quarta; cardápio do dia, combo com nome próprio, lista de transmissão, story de forno aceso, parceria de bairro. Thumb: `pecas/thumb-longo-1-dia-fraco.jpg`.',
      '2. **Taxa do iFood: como trazer o cliente para o WhatsApp da pizzaria**: cupom na caixa, cardápio digital, código de rastreio, sem brigar com o app. Thumb: `pecas/thumb-longo-2-taxa-do-app.jpg` (número de capa só se tiver fonte; não prometer resultado).',
      '3. **Raio-X ao vivo: analisei 3 perfis de pizzaria (e o que eu mudaria hoje)**: Instagram, Google e iFood de pizzarias que autorizarem; só com autorização (LGPD).',
      '4. **CMV de pizzaria na prática: a ficha técnica que mostra se a sua pizza dá lucro**: planilha passo a passo, preço de venda, perda de insumo.', '',
      '**Descrição base dos longos:** 1ª linha = título com palavra-chave; capítulos (00:00 …); link do Raio-X; site; 3 hashtags.']
open(os.path.join(D, 'TEXTOS.md'), 'w').write('\n'.join(o) + '\n')
print('ok', len(R))
