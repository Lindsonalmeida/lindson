# Gera roteiros.json e LEGENDAS.md da leva de Reels de 30 s (conta Zuleide, 08/11/2026)
import json, re, sys

import os
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
LIM_BLOCO = 220

# Cada cena: (ini, fim, narracao, tela, visual, vfx, sfx)
R = []

def reel(**k):
    R.append(k)

FOTO_LS = "Lindson em lip-sync (foto de estúdio colorida, variação nunca usada, boca sincronizada com a voz do Dublê)"

# ---------------------------------------------------------------- R01
reel(
 id="L30-01", formato="POV", linha="Erro que custa cliente",
 titulo="POV: o cliente entrou no seu perfil e saiu em 3 segundos",
 intencao="Alcance e conversa: fazer o dono de negócio se ver no lugar do cliente que desiste e pedir a avaliação.",
 cta_palavra="PERFIL",
 entrega_no_video="O teste dos 3 segundos: foto que mostra quem atende, bio que diz o que o cliente ganha e botão para o WhatsApp.",
 entregavel={"o_que":"Avaliação gratuita do perfil: 3 problemas e 1 solução prática, por DM ou WhatsApp","arquivo":"processo em conteudo/avaliacao-gratuita/PLANO.md (isca PERFIL, código AV em agencia/marca-lindson/ESTRATEGIA.md §4)","situacao":"existe"},
 capa_cor="amarelo",
 capa="Amarelo c2y: palavra gigante preta SAIU atrás; Lindson recortado de corpo inteiro na frente, braços cruzados, olhando de lado (desconfiado); degradê preto embaixo com a manchete branca 'Ele entrou no seu perfil e' + caixa amarela SAIU.",
 musica="Trap/lo-fi escuro, 90 BPM, batida seca; ducking de -18 dB sob a voz; corte de batida no 'saiu'.",
 cenas=[
  (0.0,2.0,"Ele entrou no seu perfil. E saiu em três segundos.","Entrou. · Saiu.","Banco: 'man scrolling phone dark room close up' (Mixkit/Coverr), tela do celular trocada por perfil fictício","zoom punch + shake no 'saiu'","swipe + hit"),
  (2.0,5.0,"E nem te disse por quê.","Por quê?","Motion: contador 3 · 2 · 1 gigante em amarelo sobre preto","motion blur direcional na troca","tick de relógio + whoosh"),
  (5.0,9.0,"Um: a foto. Escura, de longe. Ninguém sabe quem atende.","1 · A foto","Motion: perfil fictício com a foto borrada piscando; card amarelo com o número","light leak curto","pop"),
  (9.0,13.0,"Dois: a bio. Fala de você, não do que ele ganha.","2 · A bio","Motion: bio fictícia sendo riscada linha por linha","zoom in lento","click + risco (marker)"),
  (13.0,16.0,"E o terceiro é o que mais espanta.","O pior…","Card de impacto amarelo em tela cheia, texto preto","glitch de 3 quadros + shake","riser → hit"),
  (16.0,21.0,"Nenhum caminho pro WhatsApp. Ele quer chamar e não acha onde.","3 · Sem caminho pro zap","Banco: 'hand holding smartphone confused' + motion do botão de WhatsApp que some","motion blur direcional","whoosh + 'erro' curto"),
  (21.0,27.5,"Comenta PERFIL que eu olho o seu e te digo o que ajustar.","Comenta PERFIL","%s; pose apontando para baixo, para os comentários; card amarelo 'Comenta PERFIL' na área livre abaixo do rosto" % FOTO_LS,"light leak âmbar na entrada","pop + ding"),
  (27.5,30.0,"Antes que o próximo entre… e saia.","Entrou. · Saiu.","Mesma tomada da abertura (loop)","zoom punch igual ao início","swipe"),
 ],
 legenda_titulo="POR QUE O CLIENTE ENTRA NO SEU PERFIL DO INSTAGRAM E SAI EM 3 SEGUNDOS",
 legenda="""O cliente entrou no seu perfil. Olhou. E foi embora sem chamar. Isso acontece todo dia com negócio local em São Luís, e o dono quase nunca fica sabendo.

📌 O que o cliente olha nos primeiros segundos
Quem chega no seu perfil decide rápido se fica ou se sai. Ele não lê tudo. Ele bate o olho em três coisas.

1️⃣ A foto
Foto escura, de longe ou só a logo pequena. A pessoa não sabe quem vai atender e não sente segurança.

2️⃣ A bio
Bio que fala de você ("apaixonada pelo que faço") e não diz o que o cliente ganha, pra quem é e onde fica.

3️⃣ O caminho pro WhatsApp
Esse é o que mais espanta. A pessoa quer chamar e não acha o botão, ou acha um link que não diz o que tem dentro.

💡 Exemplo
Uma manicure no Cohama troca a logo por uma foto dela sorrindo, escreve na bio "unhas em gel que duram, no Cohama · chama no zap 👇" e coloca o link do WhatsApp com mensagem pronta. Quem entra entende em um olhar o que ela faz e como pedir.

✅ Conclusão
Antes de postar mais, confira as três coisas que o cliente olha primeiro. Perfil claro segura quem já chegou.

📲 Quer que eu olhe o seu?
Comenta PERFIL que eu olho o seu perfil e te mando o que ajustar primeiro. De graça.

Narração com a voz do Lindson gerada por IA (Dublê).""",
 hashtags=["#perfilprofissional","#instagramparanegocios","#donodenegocio","#saoluisma"],
)

# ---------------------------------------------------------------- R02
reel(
 id="L30-02", formato="Lista", linha="Faz comigo",
 titulo="3 frases na bio que espantam cliente",
 intencao="Salvamento e conversa: entregar a fórmula da bio e puxar a Folha da Bio (porta para o Bio que Vende).",
 cta_palavra="FÓRMULA",
 entrega_no_video="A fórmula da bio em uma linha: o que você faz + pra quem + onde + como chamar no WhatsApp.",
 entregavel={"o_que":"Folha da Bio: 1 página 4:5 com a fórmula e 6 exemplos de bio por nicho (amostra grátis do Bio que Vende)","arquivo":"a criar: produtos/bio-que-vende/amostra/Folha-da-Bio.pdf (privado), tirada do PDF Bio que Vende em 15 Minutos","situacao":"precisa criar (Designer gráfico, 1 página)"},
 capa_cor="preto",
 capa="Preto r1: foto colorida inteira com a luz do estúdio, Lindson de frente apontando para a lente, sério; degradê preto; manchete Manrope '3 frases na bio que' + caixa amarela ESPANTAM + 'cliente'; rótulo mono amarelo BIO.",
 musica="Boom bap moderno, 92 BPM, baixo marcado; ducking -18 dB; um 'drop' de silêncio antes da fórmula.",
 cenas=[
  (0.0,2.0,"Se a sua bio tem uma dessas frases, ela tá espantando cliente.","Sua bio · espanta","Motion: bio fictícia num iPhone, palavras tremendo; fundo preto","zoom punch + shake","hit grave"),
  (2.0,4.5,"E a terceira quase todo mundo usa.","A 3ª…","Card de impacto amarelo tela cheia","glitch curto","riser curto"),
  (4.5,9.0,"Um: apaixonada pelo que faço. Não diz o que você vende.","1 · Apaixonada pelo que faço","Motion: frase em aspas gigantes amarelas, risco preto atravessando","motion blur na entrada do risco","whoosh + risco"),
  (9.0,13.0,"Dois: qualidade e bom atendimento. Todo concorrente diz igual.","2 · Qualidade e bom atendimento","Banco: 'row of shop signs street night' (Coverr), letreiros iguais; frase riscada por cima","light leak lateral","click + risco"),
  (13.0,17.5,"Três: link na bio, sem dizer o que tem lá. Ninguém toca.","3 · Link na bio","Motion: dedo indo até o link e desistindo","glitch + shake no 'ninguém toca'","hit + 'erro'"),
  (17.5,22.5,"Troca por isso: o que você faz, pra quem, onde, e como chamar.","O quê + pra quem + onde + chama no zap","Card amarelo com a fórmula montando peça por peça (a entrega)","zoom out suave, pop em cada peça","4 pops em sequência"),
  (22.5,28.0,"Comenta FÓRMULA que eu te mando com exemplos.","Comenta FÓRMULA","%s; pose segurando o celular virado para a câmera; card abaixo do rosto" % FOTO_LS,"light leak âmbar","pop + ding"),
  (28.0,30.0,"Agora olha a sua bio. Tem alguma?","Tem alguma?","Volta ao iPhone da abertura (loop)","zoom punch","swipe"),
 ],
 legenda_titulo="BIO DO INSTAGRAM: 3 FRASES QUE ESPANTAM CLIENTE (E O QUE ESCREVER NO LUGAR)",
 legenda="""A bio é a primeira coisa que o cliente lê no seu perfil. E tem frase que faz ele ir embora antes de chegar no botão do WhatsApp.

🚫 Frase 1: "Apaixonada pelo que faço"
É bonita, mas não responde o que o cliente quer saber: o que você vende e se serve pra ele.

🚫 Frase 2: "Qualidade e bom atendimento"
Todo concorrente escreve a mesma coisa. Se todo mundo diz igual, nada te diferencia.

🚫 Frase 3: "Link na bio"
Sem dizer o que tem no link, ninguém toca. A pessoa não arrisca sair do Instagram sem saber pra onde vai.

✅ A fórmula da bio que vende
O que você faz + pra quem + onde + como chamar.
Uma linha pra cada parte. Simples, direto, do jeito que você explicaria no balcão.

💡 Exemplo
Antes: "Apaixonada por doces 💕 qualidade e carinho em cada detalhe · link na bio"
Depois: "Bolos de festa sob encomenda · entrega no Renascença e Calhau · pede pelo zap 👇"
O cliente entende em um olhar e já sabe como pedir.

📌 Conclusão
Bio boa não é a mais bonita. É a que faz o cliente entender e chamar.

📲 Quer a fórmula completa?
Comenta FÓRMULA que eu te mando a Folha da Bio com exemplos prontos pra vários tipos de negócio.

Narração com a voz do Lindson gerada por IA (Dublê).""",
 hashtags=["#biodoinstagram","#dicasdeinstagram","#empreendedorlocal","#saoluis"],
)

# ---------------------------------------------------------------- R03
reel(
 id="L30-03", formato="Antes × depois", linha="Antes e depois",
 titulo="Ninguém lê a sua legenda: antes × depois",
 intencao="Salvamento e envio: mostrar a virada de uma legenda que ninguém lê para uma que chama no WhatsApp.",
 cta_palavra="LEGENDA",
 entrega_no_video="A estrutura da legenda que chama: dor na 1ª linha → solução → próximo passo claro.",
 entregavel={"o_que":"5 modelos de legenda prontos, adaptados ao nicho de quem comentou (texto por DM)","arquivo":"a criar: conteudo/reels/leva-30s/entregaveis/5-modelos-de-legenda.txt (base genérica tirada de conteudo/avaliacao-gratuita/LEGENDAS.md); a equipe troca o nicho na hora","situacao":"precisa criar (Social media, texto)"},
 capa_cor="amarelo",
 capa="Amarelo c2y: palavra gigante preta LEGENDA atrás; Lindson recortado de corpo inteiro segurando o celular, cara de 'nem li'; manchete branca no degradê 'Ninguém lê a sua' + caixa amarela LEGENDA.",
 musica="Funk lo-fi/beat brasileiro leve, 100 BPM; ducking -18 dB; scratch na troca antes → depois.",
 cenas=[
  (0.0,2.0,"Ninguém lê a sua legenda. E a culpa é da primeira linha.","Ninguém lê.","Banco: 'fast scrolling social media phone' (Mixkit) em velocidade alta","motion blur vertical forte + zoom punch","whoosh longo + hit"),
  (2.0,4.5,"Olha o antes e o depois.","Antes × Depois","Motion: tela dividida preto | amarelo abrindo do centro","split com light leak no meio","scratch de vinil"),
  (4.5,9.5,"Antes: bom dia, pessoal, hoje vim falar de um assunto importante. Passou direto.","Antes: 'Bom dia, pessoal…'","Motion: legenda fictícia num post, dedo rolando e passando","shake leve no 'passou direto'","swipe + 'erro'"),
  (9.5,13.5,"Depois: começa pela dor do cliente, numa frase só.","Depois: a dor na 1ª linha","Motion: a mesma legenda reescrita, 1ª linha em amarelo","zoom in na 1ª linha","pop"),
  (13.5,16.5,"Mas o segredo tá no final.","O segredo tá no final","Card de impacto amarelo tela cheia","glitch + shake","riser → hit"),
  (16.5,22.5,"Termina dizendo o próximo passo: chama no WhatsApp, comenta, agenda. Sem isso, ela lê e vai embora.","Dor → solução → próximo passo","Motion: 3 blocos empilhando com seta para o botão do WhatsApp (a entrega)","motion blur direcional entre os blocos","3 clicks + whoosh"),
  (22.5,28.0,"Comenta LEGENDA que eu te mando cinco modelos prontos pro seu negócio.","Comenta LEGENDA","%s; pose de quem mostra algo com a mão aberta; card abaixo do rosto" % FOTO_LS,"light leak âmbar","pop + ding"),
  (28.0,30.0,"E apaga esse bom dia, pessoal.","Apaga.","Volta à rolagem da abertura (loop)","zoom punch","whoosh"),
 ],
 legenda_titulo="COMO ESCREVER LEGENDA PARA INSTAGRAM QUE O CLIENTE LÊ ATÉ O FIM",
 legenda="""Você escreve, capricha, posta… e ninguém lê a legenda. Quase sempre o problema está na primeira linha.

❌ O antes
"Bom dia, pessoal! Hoje vim falar de um assunto muito importante…"
O cliente não sabe do que se trata e rola pra baixo. A legenda morre na primeira linha.

✅ O depois
Comece pela dor do cliente, numa frase só, com as palavras que ele usa.
"Seu bolo murcha depois que sai do forno?" prende muito mais do que "bom dia".

📌 A estrutura que funciona
1. Dor na primeira linha.
2. A solução, curta e prática.
3. O próximo passo: chama no WhatsApp, comenta, agenda.

O terceiro é o que mais se esquece. Sem ele, a pessoa lê, concorda e vai embora.

💡 Exemplo
Uma oficina no Turu troca "Bom dia, clientes!" por "Barulho no freio não é normal. Veja o que pode ser." Explica em 3 linhas e termina com "Manda um áudio do barulho no zap que a gente te fala". A legenda vira conversa.

🎯 Conclusão
Legenda boa não é a mais longa. É a que começa pela dor e termina com um passo claro.

📲 Quer modelos prontos?
Comenta LEGENDA que eu te mando 5 modelos adaptados pro seu negócio.

Narração com a voz do Lindson gerada por IA (Dublê).""",
 hashtags=["#legendaparainstagram","#copywriting","#negociolocal","#maranhao"],
)

# ---------------------------------------------------------------- R04
reel(
 id="L30-04", formato="Erro × acerto", linha="Erro que custa cliente",
 titulo="O cliente sumiu depois do orçamento: o erro está na sua mensagem",
 intencao="Envio e conversa: dor de quem perde venda no WhatsApp; porta para o Kit WhatsApp que Fecha.",
 cta_palavra="SUMIU",
 entrega_no_video="A mensagem de retomada pronta: 'Separei duas opções pro seu caso. Quer que eu te mostre a mais em conta?'",
 entregavel={"o_que":"5 mensagens prontas para cliente que sumiu (imagem 4:5 ou texto por DM)","arquivo":"a separar de CentralLindsonALmeida/produtos/kit-whatsapp-que-fecha/entrega/atalhos.txt (Kit WhatsApp que Fecha); salvar em conteudo/reels/leva-30s/entregaveis/5-mensagens-cliente-sumiu.txt","situacao":"conteúdo existe; precisa separar as 5 (equipe, poucos minutos)"},
 capa_cor="preto",
 capa="Preto r1: foto colorida com luz de estúdio, Lindson olhando o celular com a mão na testa; degradê preto; manchete 'O cliente' + caixa amarela SUMIU + 'depois do orçamento'; rótulo mono amarelo WHATSAPP.",
 musica="Suspense eletrônico, 85 BPM, pulso grave; ducking -18 dB; som de notificação usado como batida.",
 cenas=[
  (0.0,2.0,"O cliente pediu orçamento e sumiu. E você mandou: e aí, pensou?","E aí, pensou?","Motion: conversa de WhatsApp fictícia, visto azul e nada de resposta","zoom punch no 'pensou?' + shake","notificação + hit"),
  (2.0,4.5,"Essa mensagem afasta. Olha o erro e o acerto.","Erro × Acerto","Motion: tela dividida preto | amarelo","light leak no corte","whoosh"),
  (4.5,9.5,"Erro: cobrar resposta. A pessoa se sente pressionada e some de vez.","Erro: cobrar","Banco: 'man ignoring phone notification couch' (Coverr)","desfoque direcional saindo","'erro' curto + whoosh"),
  (9.5,13.0,"Acerto: dar um motivo pra ela responder.","Acerto: dar um motivo","Card amarelo com a palavra MOTIVO","zoom in","pop"),
  (13.0,16.0,"E esse motivo não é desconto.","Não é desconto.","Card de impacto amarelo tela cheia, 'desconto' riscado","glitch + shake","riser → hit"),
  (16.0,22.5,"Manda assim: separei duas opções pro seu caso. Quer que eu te mostre a mais em conta?","Separei 2 opções pro seu caso","Motion: a mensagem sendo digitada e a resposta 'quero sim' chegando (ilustrativo)","motion blur no balão que chega","digitação + notificação"),
  (22.5,28.0,"Comenta SUMIU que eu te mando cinco mensagens prontas pra cliente que sumiu.","Comenta SUMIU","%s; pose segurando o celular com a tela para fora; card abaixo do rosto" % FOTO_LS,"light leak âmbar","pop + ding"),
  (28.0,30.0,"Antes que ele feche com outro.","Antes que ele suma.","Volta à conversa da abertura (loop)","zoom punch","notificação"),
 ],
 legenda_titulo="CLIENTE SUMIU DEPOIS DO ORÇAMENTO NO WHATSAPP? O QUE MANDAR PARA ELE RESPONDER",
 legenda="""Você mandou o orçamento, ele visualizou… e sumiu. Aí vem a vontade de mandar "e aí, pensou?". Essa é a mensagem que mais afasta.

❌ O erro: cobrar resposta
"E aí, pensou?", "Vai fechar?", "Conseguiu ver?". A pessoa se sente pressionada e, em vez de responder, some de vez.

✅ O acerto: dar um motivo pra ela responder
Quem sumiu quase sempre tem uma dúvida que não falou: preço, prazo ou se serve pra ela. A mensagem certa abre essa porta sem pressão.

💬 Mensagem pronta pra copiar
"Separei duas opções pro seu caso. Quer que eu te mostre a mais em conta?"
Ela responde com sim ou não. E a conversa volta.

⚠️ E não precisa dar desconto
Desconto logo de cara ensina o cliente a sumir pra ganhar abatimento. Primeiro ofereça opção, não preço menor.

💡 Exemplo
Um vidraceiro no São Cristóvão manda o orçamento do box. O cliente some. Dois dias depois: "Separei duas opções de vidro pro seu banheiro. Quer ver a mais em conta?". A pessoa responde perguntando a diferença.

🎯 Conclusão
Cobrar afasta. Oferecer opção traz de volta.

📲 Quer mais mensagens assim?
Comenta SUMIU que eu te mando 5 mensagens prontas pra cliente que sumiu.

Narração com a voz do Lindson gerada por IA (Dublê).""",
 hashtags=["#vendaspelowhatsapp","#atendimentoaocliente","#pequenosnegocios","#saoluisma"],
)

# ---------------------------------------------------------------- R05
reel(
 id="L30-05", formato="Mito × verdade", linha="Papo reto do Lindson",
 titulo="Mito: quem tem Instagram não precisa de site",
 intencao="Consideração: quebrar a crença e abrir conversa para mini site (degrau Instagram que Vende).",
 cta_palavra="SITE",
 entrega_no_video="As 3 partes de uma página que passa confiança: o que você faz, fotos reais e um botão direto pro WhatsApp.",
 entregavel={"o_que":"Vídeo de demonstração do mini site com o nome do negócio de quem comentou (tela de iPhone, sem publicar)","arquivo":"processo e gravador em agencia/processos/demo-minisite/ (isca SITE, código MS)","situacao":"existe; capacidade limitada: o Lindson escolhe quais leads recebem a demo"},
 capa_cor="amarelo",
 capa="Amarelo c2y: palavra gigante preta MITO atrás; Lindson recortado de corpo inteiro com o dedo em 'não'; manchete branca no degradê 'Instagram basta?' + caixa amarela MITO.",
 musica="Eletrônico confiante, 110 BPM; ducking -18 dB; impacto de tambor no 'é mito'.",
 cenas=[
  (0.0,2.0,"Tenho Instagram, não preciso de site. Isso custa cliente.","Não preciso de site.","Motion: a frase em aspas gigantes, carimbo MITO amarelo batendo por cima","shake forte no carimbo","hit + carimbo"),
  (2.0,4.5,"É mito. E eu te mostro em três coisas.","3 coisas","Card de impacto amarelo tela cheia com o 3 gigante","zoom punch","riser curto"),
  (4.5,9.0,"Um: no Instagram, o cliente se perde entre post e story.","1 · Ele se perde","Banco: 'woman scrolling phone lost confused street' (Mixkit)","motion blur direcional","whoosh"),
  (9.0,13.0,"Dois: quem procura no Google nem sempre chega no seu perfil.","2 · O Google","Banco: 'typing search on laptop close up' (Coverr)","light leak lateral","teclado + click"),
  (13.0,16.0,"E a terceira é a que mais pesa.","A que mais pesa…","Card de impacto amarelo tela cheia","glitch + shake","riser → hit"),
  (16.0,22.0,"Uma página simples passa confiança: o que você faz, fotos reais e botão pro WhatsApp.","Faz + fotos reais + botão do zap","Gravação de tela no iPhone de um mini site real de cliente (rafaelimports.pages.dev ou desentupidorasf.pages.dev), rolando até o botão (a entrega)","zoom in no botão","3 pops"),
  (22.0,28.0,"Comenta SITE que eu monto uma demonstração com o nome do seu negócio.","Comenta SITE","%s; pose segurando o iPhone com o site; card abaixo do rosto" % FOTO_LS,"light leak âmbar","pop + ding"),
  (28.0,30.0,"Ainda acha que o Instagram basta?","Ainda basta?","Volta ao carimbo MITO (loop)","shake","carimbo"),
 ],
 legenda_titulo="NEGÓCIO LOCAL PRECISA DE SITE SE JÁ TEM INSTAGRAM? O MITO QUE CUSTA CLIENTE",
 legenda=""""Eu já tenho Instagram, não preciso de site." Muito dono de negócio pensa assim. E perde cliente sem perceber.

🔍 Por que é mito
O Instagram é ótimo pra mostrar o dia a dia. Mas ele não foi feito pra ser a sua vitrine principal.

1️⃣ O cliente se perde
Entre post, story, destaque e reels antigos, a pessoa não acha o que precisa: o que você faz, onde fica, como pedir.

2️⃣ Nem todo mundo te procura no Instagram
Muita gente pesquisa no Google: "desentupidora em São Luís", "loja de celular no centro". Se você só existe no Instagram, nem sempre aparece pra essa pessoa.

3️⃣ Confiança
Esse é o que mais pesa. Uma página simples, com seu nome, passa a imagem de negócio sério.

✅ O que essa página precisa ter
- O que você faz, em uma frase.
- Fotos reais do seu trabalho.
- Um botão que leva direto pro WhatsApp, com mensagem pronta.

💡 Exemplo
Uma desentupidora coloca o link da página na bio, no Google e no adesivo do carro. Quem vê em qualquer lugar cai no mesmo lugar e toca no botão do WhatsApp.

🎯 Conclusão
Instagram mostra. A página organiza e leva pra conversa. Um ajuda o outro.

📲 Quer ver como ficaria a sua?
Comenta SITE que eu monto um vídeo de demonstração com o nome do seu negócio.

Narração com a voz do Lindson gerada por IA (Dublê).""",
 hashtags=["#sitepraempresa","#minisite","#marketinglocal","#saoluis","#linkdabio"],
)

# ---------------------------------------------------------------- R06
reel(
 id="L30-06", formato="Tier list", linha="Papo reto do Lindson",
 titulo="Tier list: os posts que mais trazem cliente (e os que só ganham curtida)",
 intencao="Alcance e debate nos comentários (cada um diz o nível do seu post); isca dos 3 roteiros.",
 cta_palavra="ROTEIRO",
 entrega_no_video="O ranking D → S do tipo de post e o nível S explicado: cliente real contando como foi, com botão pro WhatsApp.",
 entregavel={"o_que":"3 roteiros de Reels para o nicho de quem comentou (texto por DM)","arquivo":"isca ROTEIRO (código VD) de agencia/marca-lindson/ESTRATEGIA.md §4; a equipe tira da esteira de 300 roteiros (conteudo/esteira/teste-01-roteiros.json) e adapta ao nicho","situacao":"existe"},
 capa_cor="preto",
 capa="Preto r1: foto colorida com luz de estúdio, Lindson segurando um cartão em branco (vira o selo S na arte); degradê preto; manchete 'Do' + caixa amarela PIOR + 'ao melhor post pra vender'; rótulo mono amarelo TIER LIST.",
 musica="Game/chiptune moderno com 808, 120 BPM; ducking -18 dB; som de 'level up' em cada nível.",
 cenas=[
  (0.0,2.0,"Post de data comemorativa? Tá no fundo dessa lista.","Fundo da lista","Motion: tier list D C B A S em faixas pretas e amarelas, cartão 'data comemorativa' caindo no D","shake no impacto do cartão","hit + queda"),
  (2.0,4.5,"O primeiro lugar quase ninguém faz.","O 1º quase ninguém faz","Mesma tier list, faixa S piscando vazia","glitch na faixa S","riser curto"),
  (4.5,8.0,"Nível D: data comemorativa. Todo mundo posta igual.","D · Data comemorativa","Cartão entrando no D","motion blur direcional","whoosh + 'level down'"),
  (8.0,11.5,"C: foto de produto solta, sem dizer como pedir.","C · Produto solto","Banco: 'product photo on table rotating' (Mixkit) dentro do cartão","zoom punch","pop"),
  (11.5,15.0,"B: dica útil. Sozinha não vende.","B · Dica útil","Cartão no B","light leak curto","pop"),
  (15.0,18.5,"A: bastidor. Mostra quem faz e como faz.","A · Bastidor","Banco: 'barber working behind the scenes' (Coverr) dentro do cartão","motion blur","pop + 'level up'"),
  (18.5,23.0,"E o S: cliente real contando como foi, com o botão pro WhatsApp do lado.","S · Cliente real + botão","Card de impacto amarelo tela cheia, faixa S acendendo (a entrega)","shake + flash","hit + 'level up' longo"),
  (23.0,28.0,"Comenta ROTEIRO que eu te mando três roteiros pro seu negócio.","Comenta ROTEIRO","%s; pose de quem conta nos dedos; card abaixo do rosto" % FOTO_LS,"light leak âmbar","pop + ding"),
  (28.0,30.0,"E o seu último post, tá em qual nível?","Qual o seu nível?","Volta à tier list com a faixa D piscando (loop)","zoom punch","hit"),
 ],
 legenda_titulo="QUE TIPO DE POST TRAZ MAIS CLIENTE PARA NEGÓCIO LOCAL? TIER LIST DO PIOR AO MELHOR",
 legenda="""Nem todo post serve pra vender. Tem post que só ganha curtida da família. Ranqueei os tipos de post do pior ao melhor pra quem tem negócio local, pelo que eu vejo no dia a dia dos meus clientes.

📉 Nível D: data comemorativa
Dia das Mães, Natal, Dia do Cliente. Todo mundo posta a mesma arte. O cliente rola sem ver.

📦 Nível C: foto de produto solta
Mostra o produto, mas não diz pra quem é nem como pedir. Fica bonito e parado.

💡 Nível B: dica útil
Gera confiança e salvamento. Mas, sozinha, não leva ninguém pro WhatsApp.

🎬 Nível A: bastidor
Mostra quem faz e como faz. A pessoa conhece você antes de comprar.

🏆 Nível S: cliente real contando como foi
Um cliente de verdade falando da experiência, com o botão do WhatsApp do lado. É prova e convite no mesmo post. E quase ninguém faz.

💡 Exemplo
Um salão no Turu grava 20 segundos da cliente saindo do horário e dizendo o que achou. Na legenda: "Quer marcar o seu? Chama no zap 👇".

🎯 Conclusão
Não pare de postar dica e bastidor. Mas toda semana precisa ter pelo menos um post nível S.

📲 Quer começar pelo nível S?
Comenta ROTEIRO que eu te mando 3 roteiros de Reels pro seu negócio.

Narração com a voz do Lindson gerada por IA (Dublê).""",
 hashtags=["#ideiasdepost","#reelsparanegocios","#marketingdeconteudo","#saoluisdomaranhao"],
)

# ---------------------------------------------------------------- R07
reel(
 id="L30-07", formato="Pare de", linha="Faz comigo",
 titulo="Pare de colocar o link do WhatsApp sem mensagem pronta",
 intencao="Salvamento e conversa: ensinar o link wa.me com texto e oferecer montar o da pessoa.",
 cta_palavra="LINK",
 entrega_no_video="Como montar o link: wa.me/55 + seu número + ?text= + a mensagem ('Oi, vim pelo Instagram, quero um orçamento').",
 entregavel={"o_que":"O link do WhatsApp da pessoa pronto, com a mensagem certa pro nicho dela (por DM)","arquivo":"sem arquivo; a equipe monta na hora com o modelo de mensagem de agencia/prospeccao/PADRAO-COPY.md","situacao":"existe (só precisa do número que a pessoa manda no direct)"},
 capa_cor="amarelo",
 capa="Amarelo c2y: palavra gigante preta PARE atrás; Lindson recortado de corpo inteiro com a mão espalmada para a câmera; manchete branca no degradê 'Seu link do zap tá' + caixa amarela ERRADO.",
 musica="Pop eletrônico urgente, 115 BPM; ducking -18 dB; som de 'trava' no cursor piscando.",
 cenas=[
  (0.0,2.0,"Pare de colocar o link do zap assim. Tá perdendo conversa.","PARE.","Motion: link wa.me cru sendo carimbado com X amarelo","zoom punch + shake","freio + hit"),
  (2.0,5.0,"Ele toca, abre o zap… e trava. Não sabe o que escrever.","E trava.","Motion: conversa vazia, cursor piscando","shake leve no 'trava'","click + 'tic tic' do cursor"),
  (5.0,8.5,"Ele fecha e deixa pra depois. E o depois não chega.","O depois não chega.","Banco: 'person locking phone putting it down' (Mixkit)","desfoque direcional saindo","whoosh descendo"),
  (8.5,11.5,"O conserto leva um minuto.","1 minuto","Card de impacto amarelo tela cheia","glitch + shake","riser → hit"),
  (11.5,19.5,"Depois do seu número, coloca interrogação, text, igual, e a mensagem: oi, vim pelo Instagram.","wa.me/55 + número · ?text= · Oi, vim pelo Instagram","Motion: o link sendo digitado peça por peça em mono amarelo (a entrega); legenda do link grande e legível para print","zoom in em cada peça","teclado + pop em cada peça"),
  (19.5,23.0,"Pronto: a mensagem já vem escrita.","Já vem escrito","Motion: toque no link abre o zap com o texto pronto e o botão enviar pulsando","light leak","click + whoosh + 'enviado'"),
  (23.0,28.0,"Comenta LINK que a minha equipe monta o seu.","Comenta LINK","%s; pose apontando para o lado do card; card abaixo do rosto" % FOTO_LS,"light leak âmbar","pop + ding"),
  (28.0,30.0,"E para de perder conversa no primeiro toque.","PARE.","Volta ao carimbo da abertura (loop)","zoom punch","freio"),
 ],
 legenda_titulo="COMO CRIAR LINK DO WHATSAPP COM MENSAGEM PRONTA PARA A BIO DO INSTAGRAM",
 legenda="""O cliente tocou no seu link do WhatsApp, a conversa abriu vazia… e ele travou. Não sabia o que escrever, fechou e deixou pra depois. E o depois não chegou.

📌 O problema do link sem mensagem
Conversa vazia dá trabalho pro cliente. Ele precisa pensar o que dizer. Muita gente desiste nessa hora.

✅ O conserto leva um minuto
Monte o link assim:
wa.me/55 + DDD + seu número + ?text= + a mensagem

Exemplo com número fictício:
wa.me/5598900000000?text=Oi,%20vim%20pelo%20Instagram,%20quero%20um%20orçamento

O "%20" é o espaço. Teste no seu celular antes de colocar na bio.

💬 Que mensagem colocar
Algo que a pessoa diria mesmo:
- "Oi, vim pelo Instagram, quero um orçamento."
- "Oi, quero saber os horários livres."
- "Oi, quero ver o cardápio de hoje."

💡 Exemplo
Uma assistência de celular no Centro troca o link cru por um com "Oi, vim pelo Instagram, meu celular tá com problema". Quem toca já chega dizendo o que precisa, e o atendimento começa mais rápido.

🎯 Conclusão
Quanto menos o cliente precisar pensar, mais fácil ele chama.

📲 Quer o seu pronto?
Comenta LINK que a minha equipe monta o seu link com a mensagem certa pro seu negócio.

Narração com a voz do Lindson gerada por IA (Dublê).""",
 hashtags=["#linkdowhatsapp","#whatsappbusiness","#dicasparaempreendedores","#saoluisma"],
)

# ---------------------------------------------------------------- R08
reel(
 id="L30-08", formato="Bastidor", linha="Bastidor de cliente",
 titulo="Bastidor: como eu decido o que um cliente vai postar na semana",
 intencao="Prova de método e desejo: mostrar o processo da agência e entregar uma semana pronta (porta para o Kit Mês Pronto).",
 cta_palavra="CALENDÁRIO",
 entrega_no_video="O método em 3 passos: perguntas do balcão viram posts → um post por objetivo (atrair, confiar, chamar) → dia fixo (segunda a dor, quarta o bastidor, sexta o convite).",
 entregavel={"o_que":"Semana pronta: calendário de 7 dias com tema, formato e legenda-base de cada dia (PDF de 1 a 2 páginas, amostra grátis do Kit Mês Pronto)","arquivo":"a criar: CentralLindsonALmeida/produtos/kit-mes-pronto/amostra/Semana-Pronta.pdf, tirada da 1ª semana do Kit Mês Pronto (agencia/ofertas/low-ticket/produtos/kit-mes-pronto/)","situacao":"precisa criar (Designer gráfico + Social media)"},
 capa_cor="preto",
 capa="Preto r1: foto colorida de estúdio, Lindson de lado olhando para um notebook/quadro com luz âmbar; degradê preto; manchete 'Como eu monto a' + caixa amarela SEMANA + 'de um cliente'; rótulo mono amarelo BASTIDOR.",
 musica="Lo-fi hip hop de estúdio, 88 BPM; ducking -18 dB; som de caneta e papel nas trocas.",
 cenas=[
  (0.0,2.0,"Você posta o que dá na cabeça. É por isso que não vende.","O que dá na cabeça","Banco: 'messy desk overhead sticky notes chaos' (Coverr)","zoom punch + shake","hit"),
  (2.0,5.0,"Olha como eu monto a semana de um cliente.","Bastidor","Gravação de tela do painel da Central do Cliente (calendário), sem dado de cliente à mostra","light leak de abertura","whoosh + click"),
  (5.0,10.0,"Um: as perguntas que ele mais ouve no balcão. Cada uma vira post.","1 · Perguntas do balcão","Banco: 'hand writing notes notebook close up' (Mixkit); perguntas surgindo em post-its amarelos","motion blur direcional nos post-its","caneta + pop"),
  (10.0,13.5,"Dois: separo em atrair, confiar e chamar.","2 · Atrair · Confiar · Chamar","Motion: 3 colunas preto/amarelo/preto, post-its caindo em cada uma","zoom out","3 pops"),
  (13.5,16.5,"Mas o que muda tudo é o terceiro passo.","O 3º muda tudo","Card de impacto amarelo tela cheia","glitch + shake","riser → hit"),
  (16.5,22.5,"Dia e horário fixos. Segunda a dor, quarta o bastidor, sexta o convite.","Seg dor · Qua bastidor · Sex convite","Motion: grade da semana se montando (a entrega), legível para print","zoom in na sexta","3 clicks + whoosh"),
  (22.5,28.0,"Comenta CALENDÁRIO que eu te mando uma semana pronta pra copiar.","Comenta CALENDÁRIO","%s; pose com caderno ou tablet na mão; card abaixo do rosto" % FOTO_LS,"light leak âmbar","pop + ding"),
  (28.0,30.0,"E amanhã você já sabe o que postar.","Amanhã já sabe.","Volta à mesa bagunçada, agora arrumada (loop invertido)","zoom punch","whoosh"),
 ],
 legenda_titulo="CALENDÁRIO DE POSTAGEM PARA INSTAGRAM: COMO PLANEJAR A SEMANA DO SEU NEGÓCIO",
 legenda="""Postar o que dá na cabeça é o jeito mais rápido de ter um perfil cheio e um WhatsApp vazio. Vou te mostrar como eu monto a semana de posts de um cliente.

📝 Passo 1: as perguntas do balcão
Anoto as perguntas que o cliente mais ouve no dia a dia: "quanto tempo demora?", "atende no sábado?", "dói?". Cada pergunta vira um post. Assim nunca falta assunto, e todo assunto é o que o cliente quer saber.

🎯 Passo 2: um post pra cada objetivo
- Atrair: um erro ou uma dor que o público reconhece.
- Confiar: bastidor, prova, cliente real.
- Chamar: convite claro pro WhatsApp.
Se a semana só tem post de atrair, ninguém chama. Se só tem convite, ninguém confia.

📅 Passo 3: dia e horário fixos
Esse é o que muda tudo. Segunda a dor, quarta o bastidor, sexta o convite. Você para de decidir todo dia o que postar, e o seguidor se acostuma com o seu ritmo.

💡 Exemplo
Uma clínica de estética: segunda "3 erros que mancham a pele no verão", quarta "como é uma sessão por dentro", sexta "agenda da próxima semana aberta, chama no zap".

✅ Conclusão
Calendário não é burocracia. É o que faz o post de hoje levar ao convite de sexta.

📲 Quer uma semana pronta?
Comenta CALENDÁRIO que eu te mando uma semana de posts pra copiar.

Narração com a voz do Lindson gerada por IA (Dublê).""",
 hashtags=["#calendariodepostagem","#planejamentodeconteudo","#socialmedia","#maranhao"],
)

# ---------------------------------------------------------------- R09
reel(
 id="L30-09", formato="Pergunta", linha="Faz comigo",
 titulo="Por que ninguém assiste o seu vídeo até o fim?",
 intencao="Retenção e salvamento: vídeo meta (mostra a técnica usando a própria técnica) e isca dos 10 ganchos.",
 cta_palavra="GANCHO",
 entrega_no_video="A regra dos 2 primeiros segundos: começar com um erro, uma perda ou uma pergunta que incomoda, e guardar a resposta para o final.",
 entregavel={"o_que":"10 modelos de começo (gancho) para vídeo, com um exemplo de negócio local em cada (imagem 4:5 ou PDF de 1 página)","arquivo":"a diagramar: os 10 modelos de gancho já existem em conteudo/esteira/teste-01-reels.json (campo ganchos); salvar em conteudo/reels/leva-30s/entregaveis/10-ganchos.pdf","situacao":"conteúdo existe; precisa diagramar 1 página (Designer gráfico)"},
 capa_cor="amarelo",
 capa="Amarelo c2y: palavra gigante preta PULOU atrás; Lindson recortado de corpo inteiro com a mão no queixo, cara de pergunta; manchete branca no degradê 'Por que ele' + caixa amarela PULOU + 'seu vídeo?'.",
 musica="Cinematográfico tenso com pulso, 95 BPM; ducking -18 dB; rewind (fita voltando) no loop final.",
 cenas=[
  (0.0,2.0,"Por que ninguém assiste seu vídeo até o fim? Tá nos dois primeiros segundos.","2 segundos","Motion: barra de progresso de Reels parando em 2 s, contador gigante","zoom punch + shake","tick + hit"),
  (2.0,4.5,"E não é a qualidade da câmera.","Não é a câmera.","Banco: 'professional camera lens close up' (Mixkit) com X amarelo por cima","glitch","riser curto + 'erro'"),
  (4.5,8.5,"Você começa com: oi, gente, tudo bem? Ali ele já pulou.","'Oi, gente…' · pulou","Banco: 'thumb swiping phone fast' (Coverr)","motion blur vertical forte","swipe + whoosh"),
  (8.5,13.0,"O começo tem que doer: um erro, uma perda ou uma pergunta.","Erro · Perda · Pergunta","Card amarelo com as 3 palavras entrando uma por uma (a entrega)","zoom in a cada palavra","3 hits"),
  (13.0,16.0,"Repara no que eu fiz no começo desse vídeo.","Repara.","Card de impacto amarelo tela cheia","glitch + shake","riser → hit"),
  (16.0,22.0,"Pergunta, promessa, e a resposta guardada pro fim. Por isso você ainda tá aqui.","Pergunta → promessa → resposta no fim","Motion: linha do tempo do próprio vídeo com marcadores em 0 s, 2 s e 28 s","motion blur direcional na linha","3 clicks + whoosh"),
  (22.0,28.0,"Comenta GANCHO que eu te mando dez modelos de começo.","Comenta GANCHO","%s; pose apontando para a própria cabeça (ideia); card abaixo do rosto" % FOTO_LS,"light leak âmbar","pop + ding"),
  (28.0,30.0,"Agora volta pro começo e repara.","Volta e repara.","Rebobinar visual até o quadro de abertura (loop literal)","rewind + glitch","fita voltando"),
 ],
 legenda_titulo="COMO PRENDER A ATENÇÃO NOS PRIMEIROS SEGUNDOS DO REELS (GANCHO PARA VÍDEO)",
 legenda="""Você grava, edita, posta… e quase ninguém assiste até o fim. Não é a câmera, não é a luz. Quase sempre é o começo.

⏱️ Os 2 primeiros segundos decidem
É ali que a pessoa resolve se fica ou se rola. "Oi, gente, tudo bem?" não dá motivo nenhum pra ficar.

🪝 O começo tem que incomodar
Três jeitos de abrir que seguram a atenção:
- Um erro: "Você tá respondendo o cliente do jeito errado."
- Uma perda: "Esse link na sua bio tá te fazendo perder conversa."
- Uma pergunta que incomoda: "Por que o cliente some depois do preço?"

🔁 Guarde a resposta pro final
Abra a pergunta, prometa a resposta e só entregue no fim. Quem quer saber, fica. Repare: foi exatamente o que esse vídeo fez com você.

💡 Exemplo
Uma barbearia troca "E aí, rapaziada!" por "Esse corte deixa o rosto mais redondo. E quase todo mundo pede." O vídeo mostra o porquê e só no final diz qual corte usar no lugar.

✅ Conclusão
Câmera boa ajuda. Começo bom segura.

📲 Quer modelos prontos?
Comenta GANCHO que eu te mando 10 modelos de começo pra usar nos seus vídeos.

Narração com a voz do Lindson gerada por IA (Dublê).""",
 hashtags=["#ganchoparareels","#comogravarreels","#criadordeconteudo","#saoluis"],
)

# ---------------------------------------------------------------- R10
reel(
 id="L30-10", formato="Desafio", linha="Porta aberta",
 titulo="Desafio de 7 dias: seu perfil para de espantar cliente",
 intencao="Comentário e comunidade: compromisso público de 7 dias; quem faz o desafio vira lead quente para a avaliação e o Raio-X.",
 cta_palavra="DESAFIO",
 entrega_no_video="Os 7 dias, um por um: foto, bio, link com mensagem, destaques, post de prova, convite direto e resposta rápida.",
 entregavel={"o_que":"Checklist do Desafio de 7 dias (imagem 4:5 ou PDF de 1 página, uma tarefa por dia, com caixinha para marcar)","arquivo":"a criar: conteudo/reels/leva-30s/entregaveis/desafio-7-dias.pdf, adaptado do modelo do Plano de 7 Dias do Raio-X do Perfil (agencia/ofertas/low-ticket/produtos/raio-x-do-perfil/)","situacao":"precisa criar (Designer gráfico, 1 página)"},
 capa_cor="preto",
 capa="Preto r1: foto colorida de estúdio, Lindson confiante com o braço estendido para a câmera ('vem'); degradê preto; manchete 'Seu perfil espanta cliente?' + caixa amarela 7 DIAS; rótulo mono amarelo DESAFIO.",
 musica="Motivacional eletrônico com bateria crescente, 124 BPM; ducking -18 dB; build-up até o dia 7.",
 cenas=[
  (0.0,2.0,"Seu perfil espanta cliente. Te desafio a consertar em sete dias.","7 dias","Motion: contador de calendário 1 → 7 batendo forte, fundo preto","zoom punch + shake","hit + tambor"),
  (2.0,4.5,"Uma tarefa curta por dia.","1 tarefa por dia","Card de impacto amarelo tela cheia","light leak","whoosh"),
  (4.5,8.0,"Dia um: troca a foto. Rosto de frente, bem iluminado.","Dia 1 · Foto","Banco: 'man taking selfie by window light' (Mixkit)","motion blur direcional","pop + flash de câmera"),
  (8.0,11.5,"Dia dois: bio com o que você faz e pra quem.","Dia 2 · Bio","Motion: bio fictícia sendo reescrita","zoom in","teclado + pop"),
  (11.5,14.5,"Dia três: link do WhatsApp com mensagem pronta.","Dia 3 · Link do zap","Motion: link wa.me com ?text= (retoma o L30-07)","light leak","click"),
  (14.5,17.0,"E os dias seis e sete são os que trazem conversa.","Dia 6 e 7…","Card de impacto amarelo tela cheia","glitch + shake","riser → hit"),
  (17.0,22.5,"Quatro: destaques. Cinco: prova. Seis: convite direto. Sete: resposta rápida.","4 Destaques · 5 Prova · 6 Convite · 7 Resposta rápida","Motion: checklist dos 7 dias completando (a entrega), legível para print","zoom out, check em cada linha","4 clicks em ritmo"),
  (22.5,28.0,"Comenta DESAFIO que eu te mando o checklist.","Comenta DESAFIO","%s; pose com o braço estendido ('vem'); card abaixo do rosto" % FOTO_LS,"light leak âmbar","pop + ding"),
  (28.0,30.0,"Dia um. Agora.","Dia 1. Agora.","Volta ao contador da abertura parado no 1 (loop)","zoom punch","tambor"),
 ],
 legenda_titulo="DESAFIO DE 7 DIAS PARA MELHORAR O PERFIL DO INSTAGRAM DO SEU NEGÓCIO",
 legenda="""Se o seu perfil espanta cliente, não precisa refazer tudo de uma vez. Uma tarefa curta por dia, durante 7 dias. Topa?

📸 Dia 1: a foto
Rosto de frente, bem iluminado, de preferência com luz de janela. Cliente confia em gente, não em logo pequena.

✍️ Dia 2: a bio
O que você faz, pra quem, onde e como chamar. Uma linha pra cada.

🔗 Dia 3: o link do WhatsApp
Com mensagem pronta (?text=). Quem toca já chega dizendo o que quer.

⭐ Dia 4: os destaques
Poucos e na ordem da compra: o que é, como funciona, clientes, dúvidas, como pedir.

🏆 Dia 5: um post de prova
Um cliente real, um antes e depois autorizado ou um bastidor do seu trabalho.

📣 Dia 6: o convite direto
Um post que diz, sem rodeio, como agendar ou pedir.

⚡ Dia 7: responder rápido
Responda todo comentário e direct do dia. Quem demora perde a conversa pro concorrente.

💡 Exemplo
Uma confeitaria no Araçagi faz um dia por vez, no intervalo entre uma encomenda e outra. No fim da semana, o perfil diz o que ela faz, mostra prova e leva direto pro WhatsApp.

✅ Conclusão
Perfil que vende não se arruma num dia. Mas em uma semana dá pra tirar o que mais espanta.

📲 Quer o checklist?
Comenta DESAFIO que eu te mando o checklist dos 7 dias. E me conta aqui em qual dia você está.

Narração com a voz do Lindson gerada por IA (Dublê).""",
 hashtags=["#desafio7dias","#instagramquevende","#empreendedorismolocal","#saoluisma"],
)

# ---------------------------------------------------------------- montagem
AGENDA = [("10/11","08:30"),("10/11","18:00"),("11/11","08:30"),("11/11","18:00"),("12/11","08:30"),
          ("12/11","18:00"),("13/11","08:30"),("13/11","18:00"),("14/11","08:30"),("14/11","18:00")]

def blocos(textos):
    out, cur = [], ""
    for t in textos:
        cand = (cur + " " + t).strip()
        if len(cand) <= LIM_BLOCO:
            cur = cand
        else:
            out.append(cur); cur = t
    if cur: out.append(cur)
    return out

erros = []
reels = []
for i, r in enumerate(R):
    cenas = []
    prev = 0.0
    for (a, b, n, t, v, vfx, sfx) in r["cenas"]:
        if abs(a - prev) > 1e-6: erros.append(f"{r['id']}: buraco de tempo em {a}")
        prev = b
        cenas.append({"tempo": f"{a:.1f}–{b:.1f}", "ini": a, "fim": b, "narracao": n,
                      "texto_tela": t, "texto_tela_palavras": t.replace("·", " ").split(),
                      "visual": v, "vfx": vfx, "sfx": sfx})
    if abs(prev - 30.0) > 1e-6: erros.append(f"{r['id']}: termina em {prev}")
    narr = " ".join(c["narracao"] for c in cenas)
    palavras = len(re.findall(r"\w+", narr))
    if not 68 <= palavras <= 86: erros.append(f"{r['id']}: {palavras} palavras")
    bl = blocos([c["narracao"] for c in cenas])
    if any(len(b) > LIM_BLOCO for b in bl): erros.append(f"{r['id']}: bloco > 220")
    leg = r["legenda_titulo"] + "\n\n" + r["legenda"] + "\n\n" + " ".join(r["hashtags"])
    if len(leg) > 2200: erros.append(f"{r['id']}: legenda {len(leg)}")
    if not 3 <= len(r["hashtags"]) <= 5: erros.append(f"{r['id']}: hashtags")
    for proib in ["vi que", "parece que", "gargalo", "garant", "%"]:
        if proib in (narr + leg).lower().replace("%20", ""): erros.append(f"{r['id']}: proibido '{proib}'")
    d, h = AGENDA[i]
    reels.append({
        "id": r["id"], "ordem": i + 1, "post": {"data": d, "hora": h},
        "titulo": r["titulo"], "formato": r["formato"], "linha_editorial": r["linha"],
        "intencao": r["intencao"], "duracao_s": 30,
        "capa_cor": r["capa_cor"], "capa": r["capa"],
        "cta_palavra": r["cta_palavra"], "entrega_no_video": r["entrega_no_video"],
        "entregavel": r["entregavel"], "musica": r["musica"],
        "voz": "Voz clonada do Lindson no Dublê, gerada nos blocos abaixo (até ~220 caracteres), pausa ~0,2 s entre frases, sem respiração artificial.",
        "narracao_palavras": palavras, "blocos_voz": bl,
        "cenas": cenas,
        "legenda": {"titulo": r["legenda_titulo"], "corpo": r["legenda"], "hashtags": r["hashtags"],
                    "texto_completo": leg, "caracteres": len(leg)},
    })

# xadrez: alternância estrita a partir de a2 (preto)
cores = ["preto"] + [x["capa_cor"] for x in reels]
for a, b in zip(cores, cores[1:]):
    if a == b: erros.append("xadrez quebrado")
hs = [h for x in reels for h in x["legenda"]["hashtags"]]
if len(set(" ".join(x["legenda"]["hashtags"]) for x in reels)) != len(reels): erros.append("bloco de hashtag repetido")

if erros:
    print("\n".join(erros)); sys.exit(1)

doc = {
 "leva": "Reels 30 s · @lindsonalmeida_", "criado": "2026-11-08", "conta": "Zuleide (agente Social media)",
 "estrategia": "conteudo/reels/leva-30s/ESTRATEGIA.md", "legendas": "conteudo/reels/leva-30s/LEGENDAS.md",
 "identidade": {"cores": {"preto": "#0B0B0B", "amarelo": "#F5C518", "branco": "#FFFFFF"},
   "fontes": "Anton (palavra gigante) + Manrope (manchete e legenda) + mono (rótulo)",
   "cards_de_impacto": "amarelo #F5C518 com texto preto (troca o verde-limão da skill reels-viral pela cor da marca)",
   "assinatura": "@lindsonalmeida_ no canto superior direito, mono branco 60%",
   "legenda_na_tela": "palavra por palavra com entrada em blur, sentence case, sempre abaixo do rosto e fora das margens de segurança (topo 250 px, rodapé 380 px em 1080×1920)"},
 "reels": reels,
}
json.dump(doc, open(OUT + "roteiros.json", "w"), ensure_ascii=False, indent=1)

md = ["# Legendas · Leva de Reels de 30 s (@lindsonalmeida_)", "",
      "Conta Zuleide (agente Social media), 08/11/2026. Padrão blog SEO de `conteudo/avaliacao-gratuita/LEGENDAS.md`: título com a palavra-chave, introdução, subtítulos, exemplo, conclusão, chamada e 3 a 5 hashtags variadas (tema + nicho + local). Os exemplos de negócio são ilustrativos. Fonte única: `roteiros.json` (gerado por `gerar.py`).", ""]
for x in reels:
    md += [f"## {x['ordem']:02d} · {x['post']['data']} {x['post']['hora']} · {x['titulo']}",
           f"Capa {x['capa_cor']} · CTA **{x['cta_palavra']}** · {x['legenda']['caracteres']} caracteres", "",
           x["legenda"]["texto_completo"], ""]
open(OUT + "LEGENDAS.md", "w").write("\n".join(md))
for x in reels:
    print(x["id"], x["narracao_palavras"], "palavras", x["legenda"]["caracteres"], "car", len(x["blocos_voz"]), "blocos", x["capa_cor"])
