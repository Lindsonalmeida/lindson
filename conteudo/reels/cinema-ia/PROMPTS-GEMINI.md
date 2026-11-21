# Reels "Cinema IA" · prompts para o Gemini (conta Leandro, 21/11/2026)

Caminho escolhido pelo Lindson depois de reprovar 2x as "miniaturas 3D" (nunca mais bonecos low-poly em mesa preta). Ele gera as cenas no Gemini com o rosto dele; a equipe anima no motor `motor/cinema.py`. Referência de linguagem: Denis Bugatti (capturas 22-26 em `agencia/campanhas/trafego-slz-3-nichos/referencias-lindson/`). Mesmo padrão de `painel/admin-rede/trafego-slz/v3/PROMPTS-GEMINI.md` (privado).

**Como usar:** no Gemini (modo imagem) anexe **`membros/img/c13.jpg` (foto 1, rosto)** + **`c08.jpg`** (terno, corpo) ou **`c10.jpg`** (camisa, casual) conforme indicado; cole o BLOCO DE FIDELIDADE + o prompt da cena; 9:16. Se o rosto não sair idêntico: "refaça mantendo o rosto 100% idêntico à foto 1". Salve como `cenas/<reel>-<cena>.jpg` (ex.: `cenas/01-A.jpg`) e mande ao Claude. O vídeo opcional (Veo/Gemini) é para quem quiser gerar o movimento lá: o motor anima a imagem parada mesmo sem ele.

## BLOCO DE FIDELIDADE (cole no início de TODO prompt)
> FIDELIDADE DE ROSTO 100%: a pessoa da imagem é EXATAMENTE o homem das fotos anexadas. Preserve sem nenhuma alteração: formato do rosto e da mandíbula, olhos (formato, distância, cor), sobrancelhas, nariz, boca e lábios, orelhas, linha do cabelo e corte, barba e bigode (densidade e contorno), tom e textura da pele, marcas e pintas, idade aparente, altura e porte físico. Não embeleze, não afine, não rejuvenesça, não mude etnia, não suavize a pele. Rosto nítido e em foco crítico, pele com poros reais. Use a foto 1 como referência principal do rosto e as demais para corpo e postura.
> REGRAS: fotorrealista, aparência de still de cinema feito com câmera real, não ilustração nem 3D. Vertical 9:16, 2160×3840. Sem nenhum texto, letra, logo, marca d'água, número ou tela legível na imagem (telas e notificações só como luz/brilho borrado). Mãos anatômicas com 5 dedos. Pessoa centralizada da cabeça à cintura, com ar em volta (o motor recorta e move em camadas). Terço inferior mais escuro e limpo para tipografia. Uma fonte de luz forte e visível no quadro (feixe, janela, neon) com poeira/fumaça no ar.

**Conferência antes de mandar (8 critérios de `agencia/processos/conferencia-imagem-ia.md`):** lógica da cena, olhar, escala, mãos, texto falso, mensagem, resolução. Um erro = gera de novo.

---

## Reel 01 · "O cliente sumiu" (SUMIU) · WhatsApp

**01-A · SUMIU** · anexar c13 + c10 · fala "mandou: quanto custa? E sumiu"
- **Cena:** quarto escuro; um celular caindo em câmera lenta no vazio em primeiro plano, tela acesa espalhando balões de notificação desfocados (só luz verde, sem texto); Lindson ao fundo, desfocado leve, olhando o celular cair.
- **Direção:** em pé, mão ainda aberta como quem deixou escapar, expressão de frustração contida. Camisa preta.
- **Câmera:** 35 mm, f/1.8, 1/500 s, ISO 1600; câmera baixa, celular a 40 cm da lente.
- **Luz:** única luz é a tela (verde-esmeralda subindo no rosto); contraluz azul fraco atrás; razão 8:1.
- **Grade:** teal profundo, pretos esmagados, grão 35 mm, halation na tela.
- **Vídeo (opcional, 6 s):** "slow motion: the phone falls past the camera, notification glows trail behind it, the man watches, dust in the air, static camera, no text".

**01-B · RELÓGIO** · anexar c13 + c08 · "o problema é o relógio"
- **Cena:** Lindson diante de um relógio de parede gigante (3 m) de estação antiga, ponteiros girando, poeira no feixe de luz da claraboia.
- **Direção:** de costas três quartos para o relógio, virando o rosto para a câmera; terno azul-marinho, mãos nos bolsos.
- **Câmera:** 24 mm, f/2.8, contra-plongée leve, plano médio.
- **Luz:** feixe duro de claraboia em diagonal (luz volumétrica), rim âmbar nos ombros, fill frio baixo.
- **Grade:** teal & orange, contraste alto.
- **Vídeo (opcional, 6 s):** "clock hands spin fast, light beam with floating dust, slow push-in on the man".

**01-C · 3 LOJAS** · anexar c13 + c10 · "mandou a mesma pergunta pra três lojas"
- **Cena:** rua de comércio à noite, chuva fina; três vitrines iluminadas lado a lado ao fundo (sem letreiro legível); Lindson no meio da rua, celular na mão brilhando.
- **Câmera:** 50 mm, f/1.6, ISO 3200, altura dos olhos; poças refletindo as vitrines.
- **Luz:** vitrines quentes ao fundo (bokeh), luz do celular no rosto, neon magenta lateral.
- **Grade:** cinema noturno, magenta e ciano, pretos ricos.

**01-D · CONDUZ** · anexar c13 + c08 · "quem pergunta, conduz"
- **Cena:** salão escuro, Lindson conduzindo uma conversa (gesto de mão aberta, apresentando), holofote único de cima, fumaça.
- **Câmera:** 85 mm, f/1.8, plano americano, câmera na altura do peito.
- **Luz:** spot de cima a 70°, contorno quente, resto no preto.
- **Grade:** preto e âmbar, look Bugatti "palco".

## Reel 02 · "Quanto custa um cliente" (PERFIL) · CAC

**02-A · PEGADINHA** · anexar c13 + c08 · "não é o valor do anúncio"
- **Cena:** mesa de jogo de cartas num bar escuro; Lindson segurando cartas viradas contra o peito, ficha de cassino empilhada; fumaça de charuto no feixe da luminária (ref. Bugatti "CRIATIVOS").
- **Câmera:** 50 mm, f/2.0, plano médio, câmera na altura da mesa.
- **Luz:** luminária pendente verde sobre a mesa, rosto meio no escuro; rim quente.
- **Grade:** verde garrafa e preto, grão forte.
- **Vídeo (opcional):** "he slowly flips one card toward camera (card face blank), smoke drifts".

**02-B · A CONTA** · anexar c13 + c08 · "soma e divide pelos clientes novos"
- **Cena:** escritório à noite, Lindson ao lado de uma balança antiga de dois pratos: num prato moedas, no outro pequenas silhuetas de pessoas de metal (sem rosto).
- **Câmera:** 35 mm, f/2.2, plano médio; balança em primeiro plano.
- **Luz:** abajur âmbar lateral, janela azul ao fundo.
- **Grade:** teal & orange.

**02-C · A DÉCIMA PIZZA** · anexar c13 + c10 · "o dinheiro está na segunda, na décima"
- **Cena:** cozinha de pizzaria de verdade, forno a lenha aceso atrás; Lindson segurando uma pá de pizza com várias caixas empilhadas ao lado (sem marca).
- **Câmera:** 35 mm, f/2.0, ISO 1600; brasas e fagulhas flutuando.
- **Luz:** fogo do forno como key laranja, fill azul frio da porta.
- **Grade:** quente, pretos profundos.

**02-D · QUEM VOLTA** · anexar c13 + c08 · "o cliente que volta vale mais"
- **Cena:** porta de vidro de loja se abrindo, sininho, luz de fim de tarde entrando em feixe; Lindson do lado de dentro, sorriso discreto de quem reconhece o cliente (cliente de costas, desfocado).
- **Câmera:** 50 mm, f/1.8, contraluz.
- **Luz:** sol baixo dourado em feixe com poeira; flare natural.
- **Grade:** golden hour, contraste médio.

## Reel 03 · "Curtida não basta" (GANCHO) · envios

**03-A · CURTIDA** · anexar c13 + c10 · "curtida não faz o post crescer"
- **Cena:** chuva de corações vermelhos de vidro caindo e se quebrando no chão escuro em volta de Lindson, que nem olha para eles.
- **Câmera:** 35 mm, f/2.0, 1/1000 s (cacos congelados no ar).
- **Luz:** spot de cima, reflexos vermelhos nos cacos.
- **Grade:** preto e vermelho, look Bugatti "PERDEDOR".

**03-B · ENVIO** · anexar c13 + c08 · "o sinal mais forte é o envio"
- **Cena:** Lindson soltando um avião de papel que vira um rastro de luz cruzando o quadro sobre a cidade à noite vista de um terraço.
- **Câmera:** 24 mm, f/2.8, contra-plongée; cidade em bokeh.
- **Luz:** rastro de luz quente como key, neon da cidade como fill frio.
- **Grade:** ciano e âmbar.
- **Vídeo (opcional, 6 s):** "the paper plane leaves a glowing trail across the night city, camera follows it".

**03-C · 71 MIL** · anexar c13 + c10 · "setenta e um mil envios"
- **Cena:** centenas de aviões de papel iluminados voando em revoada atrás dele num galpão escuro.
- **Câmera:** 35 mm, f/2.0, plano médio.
- **Luz:** feixes de janelas altas cortando a poeira.
- **Grade:** teal & orange.

**03-D · MANDARIA?** · anexar c13 + c08 · "alguém mandaria isso pra um amigo?"
- **Cena:** close-médio, Lindson olhando para a lente com um celular aceso na mão (tela só brilho), dois amigos desfocados ao fundo rindo de algo no celular deles.
- **Câmera:** 85 mm, f/1.6.
- **Luz:** key suave 45°, rim quente, fundo de bar âmbar.

## Reel 04 · "Não te acham no Google" (SITE) · perfil da empresa

**04-A · NINGUÉM TE ACHA** · anexar c13 + c08 · "cliente procurando e não te achando"
- **Cena:** Lindson diante de uma vitrine de loja APAGADA numa rua de neon (as lojas vizinhas acesas, a dele no escuro), chuva fina, reflexos no asfalto.
- **Direção:** em pé, de frente, terno escuro, mãos nos bolsos, olhar direto, sério.
- **Câmera:** 35 mm, f/1.8, ISO 2500, altura do peito.
- **Luz:** neon magenta e ciano das vizinhas como contornos; rosto com key suave fria; vitrine dele preta.
- **Grade:** cinema noturno, pretos ricos, halation no neon.
- **Vídeo (opcional, 6 s):** "rain falls, neon signs flicker around a single dark storefront, slow push-in on the man, no text".

**04-B · PELA METADE** · anexar c13 + c08 · "perfil pela metade, sem horário, sem foto"
- **Cena:** quarto vazio com moldura de quadro na parede pela metade, metade da sala sem móveis, poeira no feixe da janela; Lindson no meio.
- **Câmera:** 24 mm, f/2.8, plano médio largo.
- **Luz:** feixe de janela duro com poeira (volumétrica); resto no escuro.

**04-C · CONFIÁVEL** · anexar c13 + c08 · "2,7 vezes mais chance de ser visto como confiável" (já gerada: `gemini-16-11/32.jpg`, biblioteca com a estátua da Justiça)

**04-D · ENDEREÇO ERRADO** · anexar c13 + c10 · "o cliente chega, não acha e não volta"
- **Cena:** cruzamento à noite em neblina, placas de rua sem texto legível, um pin de mapa luminoso caído e apagado no chão; Lindson olhando para ele.
- **Câmera:** 35 mm, f/2.0, câmera baixa no nível do pin.
- **Luz:** poste de sódio laranja em feixe na neblina, contraluz.
- **Grade:** laranja e azul petróleo.

## Reel 05 · "Pularam o seu vídeo" (ROTEIRO) · retenção

**05-A · DOIS SEGUNDOS** · anexar c13 + c10 · "pulado em menos de dois segundos"
- **Cena:** Lindson segurando uma ampulheta grande com a areia caindo rápido, fundo de estúdio preto, partículas de areia brilhando no feixe.
- **Câmera:** 85 mm, f/2.0; ampulheta em primeiro plano.
- **Luz:** spot lateral duro, rim branco.
- **Grade:** preto e dourado.

**05-B · BOM DIA** · anexar c13 + c08 · "começar com bom dia, tudo bem?"
- **Cena:** palco de teatro vazio, plateia de cadeiras vazias, Lindson na beira do palco sob um único holofote.
- **Câmera:** 24 mm, f/2.8, contra-plongée da plateia.
- **Luz:** canhão de luz de cima, fumaça; resto preto. (próximo de `gemini-16-11/35.jpg`)

**05-C · O DEDO PASSA** · anexar c13 + c10 · "se nada muda na tela, o dedo passa"
- **Cena:** mão gigante (escala de prédio) arrastando para cima uma "faixa" de luz como num feed, passando por cima de Lindson numa rua escura; ele firme no lugar.
- **Câmera:** 24 mm, f/2.8, câmera baixa.
- **Luz:** a faixa de luz como key fria em movimento.
- **Grade:** ciano, contraste alto.

**05-D · LEGENDA** · anexar c13 + c08 · "sem legenda, não entende nada"
- **Cena:** metrô lotado à noite, todos olhando celulares com fone desligado; Lindson em pé no meio, encarando a lente.
- **Câmera:** 35 mm, f/1.8, ISO 3200.
- **Luz:** fluorescente verde do vagão + brilho de telas nos rostos.

## Reel 06 · "Link do WhatsApp na Black Friday" (LINK)

**06-A · BLACK FRIDAY** · anexar c13 + c08 · "a Black Friday está chegando"
- **Cena:** galeria comercial escura com vitrines cobertas por plástico preto; uma contagem regressiva só em luz vermelha borrada (sem números legíveis); Lindson no corredor.
- **Câmera:** 35 mm, f/2.0, perspectiva central.
- **Luz:** vermelho de cima, fumaça, rim branco.
- **Grade:** preto e vermelho.

**06-B · CONVERSA EM BRANCO** · anexar c13 + c10 · "abre a conversa em branco e fecha"
- **Cena:** porta de loja que se fecha sozinha em câmera lenta diante de Lindson, cartaz em branco pendurado.
- **Câmera:** 50 mm, f/1.8.
- **Luz:** luz verde de dentro da loja escapando pela fresta que se fecha.

**06-C · MENSAGEM PRONTA** · anexar c13 + c08 · "o cliente só toca em enviar"
- **Cena:** close-médio, Lindson segurando o celular virado para a câmera; da tela sai um feixe verde de luz com um único balão luminoso desfocado (sem texto).
- **Câmera:** 85 mm, f/1.6.
- **Luz:** tela como key verde, rim quente.
- **Vídeo (opcional):** "a glowing chat bubble floats out of the phone toward the camera".

**06-D · UM LINK PRA CADA LUGAR** · anexar c13 + c10 · "um link diferente pra cada lugar"
- **Cena:** Lindson no centro de uma sala escura com três fios de luz verde saindo da mão dele para três portas diferentes iluminadas.
- **Câmera:** 24 mm, f/2.8, simétrico.
- **Luz:** os fios de luz como key; fumaça.

---

## O que o motor faz com cada cena
Recorta a pessoa (rembg), reconstrói o fundo, move as 2 camadas em velocidades diferentes (parallax 2.5D), põe feixe de luz com poeira, flare, grão e vinheta, entra a palavra neon no tempo da fala, faz whip pan ou zoom punch no corte com SFX. Plano de cada Reel: `motor/plano-<nn>.json` (modelo: `motor/plano-04.json`).
