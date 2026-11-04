# Memória do Lindson: o que ele pediu, aprovou e reprovou

> **Leia isto antes de qualquer pedido.** Vale para as três contas (Lindson, Zuleide, Pedro) e para qualquer conta nova.
>
> **Como usar:**
> 1. Antes de começar, procure aqui o assunto do pedido. Se já foi feito, responda "já foi feito" (seção 7). Se foi reprovado, não repita (seção 4).
> 2. O que está em APROVADO é o ponto de partida: copie e melhore, nunca comece do zero.
> 3. Ao fim de cada pedido, atualize este arquivo: o que ele aprovou ou reprovou, com data e conta (ex.: "03/11 · Lindson"). Pedido novo vai na seção 7; o que ficou faltando, na seção 8.
> 4. Este arquivo não substitui o `CLAUDE.md`, o `QUADRO-DA-EQUIPE.md` e o `REGISTRO-DAS-CONTAS.md`. Ele resume o gosto e as decisões do Lindson.
>
> Repositório público: aqui não entram dados pessoais, códigos de acesso, senhas, segredos nem nomes de pacientes.

Compilado em 03/11/2026 pela conta Lindson, a partir da conversa completa (22/10 a 03/11) e dos arquivos do repositório.

---

## 1. Quem é o Lindson, a agência e as 3 contas

- Lindson Almeida: estrategista digital e conteudista em São Luís/MA, com agência de gestão de redes sociais. Também é assessor político. Instagram @lindsonalmeida_.
- É a única pessoa que pede, aprova e decide. Ele usa três contas do Claude como uma equipe só:
  - **Lindson** = conta `lindsonmkt` (a primeira; tudo de 08/10 a 29/10 é dela).
  - **Zuleide** = conta `lindsonlopes0` (desde 30/10).
  - **Pedro** = conta `passaportedabiblia`.
  - **Leandro** = conta `raposaeleaomq` (desde 03/11/2026).
- Repositório `Lindsonalmeida/lindson`, branch principal `claude/global-agent-installation-vdyowf`.
- O que ele vende: a esteira de produtos (5 degraus até R$ 3.500, **não mexer**) e um produto master: curso + mentoria para donos de negócio venderem no Instagram (`agencia/ofertas/`).
- Clientes ativos: Vereador Leo Pinto, Dra. Jaci Cunha (clínica de harmonização e odontologia), Rafael Imports e Desentupidora SF (mini sites). Apple Black: só contrato, sem painel. Katje Garcez: só falas (não chamar de cliente ativa).
- Projetos próprios: Central do Cliente, Recomeço 90, esteira de Reels, canais dark do YouTube (Passaporte da Bíblia e Raposa e Leão) e Agente Maquiavel.

## 2. Jeito de trabalhar que ele exige

0. **Sempre que ele pedir algo, verifique o repositório e como era feito** (03/11 · Leandro: "sempre que eu pedir algo, verifique o repositório e como era feito"). Antes de qualquer entrega: `git pull`, `git grep -i` e `git log --grep` pelo assunto, pasta do cliente, `agencia/processos/` e o repositório privado `CentralLindsonALmeida`. Se já existe um jeito, siga e cite qual seguiu; se não existe, crie o modelo em `agencia/processos/` para a próxima vez.
1. **Sempre use os agentes e o time** (Xquads: copy-squad, brand-squad, design-squad, Hormozi, Donald Miller, Pedro Sobral; Peter no YouTube; Maquiavel nos negócios; agentes de pesquisa). Ele disse em 02/11: "sempre use nossos agentes e time".
2. **Nada se cria, tudo se copia** (03/11). Nunca crie arte do zero: copie a composição de um modelo que já existe (os que ele manda, Designi, Behance) e diga qual modelo copiou.
3. **Nunca refaça o que já existe.** Se o pedido for repetido, diga "já foi feito pela conta X em DD/MM, está em…". Versão nova parte da anterior (v2, v3…).
4. **Continue de onde a outra conta parou**, sem repetir nada ("continue de onde ela parou, não repita nada").
5. **Salve tudo no repositório**: decisões, roteiros, pesquisas, prompts e links. Nada fica só na conversa.
6. **Veja sempre o feed.** Toda arte é mostrada na prévia do feed, na ordem de postagem, antes de ir para aprovação.
7. **Duas aprovações** (03/11): a do Lindson na conversa aprova só a **criação**; a aprovação da arte é do **cliente no site** (Central). No card aparece só o nome de quem aprovou no site, tirado da conta de acesso (nunca "cliente" genérico, nunca o nome do Lindson como aprovador da arte).
7c. **Aprovações na Central têm 3 abas** (03/11): Para aprovar · Aprovados (a postar) · Postados. Depois de postar no Instagram, clicar em "Marquei como postado" muda o post de aba (fica registrado quem marcou e quando).
7b. **Só suba para o painel o que ele aprovou.** Quando ele pedir ajuste, tire do painel e só suba de novo depois de aprovado ("tire de lá e suba só quando ajustar").
8. **Imagem: uma por mensagem.** Imagem enviada no meio de uma resposta não fica salva. Peça assim.
9. **Estude só o necessário.** Pesquisa e engenharia reversa servem para aplicar no trabalho, não para virar relatório longo.
10. **Pesquisa completa quando ele pedir "completo"**: em todos os idiomas, revisando até não ter mais o que agregar (missão Maquiavel).
11. **Compartilhe tudo, sempre, sem ele pedir** (03/11 · Pedro: "lembre-se sempre de compartilhar tudo que está fazendo, para outras equipes continuarem. Não preciso mais pedir isso, salve pra sempre"). Toda conta, em todo pedido: ao começar, linha no `QUADRO-DA-EQUIPE.md`; durante o trabalho, commit e push a cada etapa pronta (pesquisa, decisão, roteiro, código, link publicado), com o "como retomar"; ao terminar, linha no `REGISTRO-DAS-CONTAS.md` e atualização desta memória. Nada fica só na conversa.
11. **Trabalhe rápido e em paralelo**: ele autorizou abrir quantas sessões e agentes forem precisos ("abra quantas sessões precisar").
12. **Permissões liberadas** ("permita tudo", `.claude/settings.json`). Ações irreversíveis, como apagar artifact, continuam pedindo o OK dele.
13. **Use os dados reais que existem no repositório** antes de perguntar ou inventar. Nunca invente números, fatos ou resultados. Fato público não confirmado (ex.: "mais bem votado") deve ser marcado para conferir.
14. **Português simples**, respostas curtas e diretas. Quando ele pedir "só o texto", mande só o texto.
15. **Sem dados de exemplo nos sites**: tudo o que o cliente vê tem que ser dado real.
16. **Foto real sempre.** Nada de ilustração no lugar de foto real de produto ou de pessoa. Fotos de banco gratuitas (Pexels) são permitidas como cenário, com véu na cor da marca.
17. **Recortes de foto sem corte aparente**: a borda cortada da foto original nunca pode aparecer dentro da arte.
18. **Coloque a tag da linha editorial em cada arte** (na prévia e no card de aprovação, não na arte publicada), para saber com quem ela fala.
19. **Alterne foto e só logo** entre os posts e mantenha o feed harmonizado na ordem de postagem.
20. **Negatividade gera mais audiência** (22/10): nas dores e nos ganchos, use o lado negativo.

- **Sempre que voltar, verificar se o trabalho continuou com outras equipes** (03/11 · Pedro, para todas as contas): pull, log de todos os branches, quadro, registro e privado; nunca refazer o que outra conta já fez. Recados para as contas ficam no topo do `QUADRO-DA-EQUIPE.md`, e cada conta confirma ao Lindson "Entendi o recado".

## 3. APROVADO: guardar e melhorar

**Leo Pinto**
1. **Apresentação v13, versão 3** = padrão visual do Leo ("ficaram ótimos", 02/11): degradê azul profundo, mapa de São João Batista em camada, retrato grande, nome em blocos (LEO na caixa amarela, PINTO na caixa branca), etiquetas, Montserrat Black + Kaushan Script, logo na base. Está em `agencia/clientes/leo-pinto/instagram-v13-apresentacao/` (`gerar3.py`).
2. **Textos da apresentação** ditados por ele: "vereador mais bem votado", "do povo para o povo", "jovem, engenheiro, compromisso com São João Batista". Mesma pasta, `TEXTOS.md` (legendas da versão 3 na seção 3).
3. **Foto de perfil v2**: foto leo-14, do busto para cima, fundo laranja com degradê amarelo atrás da cabeça (lembrando o sol), sem raios. Está em `agencia/clientes/leo-pinto/instagram-perfil/montar2.py`. Ele não reclamou e seguiu adiante, mas não disse "aprovado" com essa palavra.
4. **Datas comemorativas v14** (todas aprovadas em 03/11), em `agencia/clientes/leo-pinto/instagram-v14-datas/`:
   - **15/11:** cartão-checklist "se liga! O que faz um vereador?" na frente do peito, fundo laranja. Aprovado primeiro.
   - **20/11:** retrato P&B ocupando a arte, "20" grande, "ORGULHO DA NOSSA GENTE". Copiado do Designi "Ser preto é ser resistência".
   - **11/12:** ficha técnica "ENGENHEIRO" com anotações, logo marinho sobre laranja.
   - **25/12:** modelo "SOU PEDRO" enviado por ele: "FELIZ NATAL" repetido 3 vezes atrás do Leo, faixa clara na base, logo grande sem balão (letras marinho cheias, contorno branco), foto de Natal quase transparente no fundo.
   - **31/12:** cartão de enquete "Conta pra gente!" com 4 opções numeradas e "2027" gigante atrás. A legenda diz "comenta o número".
   - **01/01:** modelo "CONTRATE · DEZEMBRO": "2027" repetido atrás e placa "FELIZ ANO NOVO". O Leo velho (foto envelhecida pelo Lindson) olha para "Adeus, 2026" e o Leo novo (polo amarela) olha para "Olá, 2027". Os dois ficam na mesma altura, o de amarelo na frente com o ombro por cima.
   - Versão atual: `gerar9.py`. A logo marinho corrigida (`assets/logo-marinho-forte.png`, centro do sol claro) vale para todas.
5. **Laranja é a cor principal** do Leo (cor do partido); o azul é apoio. No feed, laranja e azul alternam em xadrez.
6. **Logo aplicada direto no post**, sem balão nem placa, com destaque (letras cheias e contorno quando preciso).
7. **Linhas editoriais do Leo** (estratégia 2028 da Zuleide): Mandato que entrega, Nossa Baixada, Leo de perto, Voz do povo, A cidade que eu sonho, Leo na rua.
8. **Aprovações na Central** com legenda (ver e copiar), tag da linha editorial e "quem aprovou": a agência e o nome do cliente, puxado da conta de acesso. Calendário editorial com abas por mês (nov/26 a jan/27).

**Dra. Jaci Cunha**
9. **Identidade real** (manual v2): bordô e dourado, Cormorant Garamond + Montserrat, logo JC com perfil. Está em `agencia/clientes/jaci-cunha/identidade/v2/`.
10. **Estilo das artes** aprendido dos 12 posts reais, para copiar: assinatura fixa no topo e no rodapé, serifada itálica + sans, faixas vinho e douradas e 5 composições. Está em `agencia/clientes/jaci-cunha/instagram-estilo/README.md`.
11. **Painel na Central** com a identidade dela, CRM de pacientes, Financeiro, Notícias do nicho, Agenda cheia (avaliações, plano de 90 dias, pautas) e envio de fotos.

**Central do Cliente** (https://lindsonalmeida.pages.dev)
12. **Um sistema só**: o cliente cria a conta com código e senha e cai direto no painel dele; o Lindson (admin) vê todos. O cliente não precisa de aprovação para entrar, porque já tem o código.
13. **Visual da Central é o padrão sempre** ("esse é o padrão sempre", 02/11): menu lateral, cartões de números, telas e animações (`prototipo/movimento.js`). Vale também para o painel do administrador.
14. **Apps do Lindson dentro da Central** com a mesma identidade: Recomeço 90, Fábrica de Conteúdo, Legendas Top X, Marca e Design System, Gerador de propostas. Os apps dos canais dark ficam só como link.
15. **Vídeos tutoriais** verticais, com voz e exemplos, conversando com o cliente ("Oi, Dra. Jaci! Oi, equipe!" e "Oi, Vereador Leo! Oi, equipe!"). Estão em `agencia/processos/demo-minisite/`.

**Lindson e agência**
16. **Agente Maquiavel v3.2 (final, 03/11, conta Zuleide)**: acervo revisado em 2 ciclos, 641 ensinamentos, índice de 50 situações, passou 20/20 nos testes (v2.1 tinha passado 12/12); tem modo professor de dinheiro e memória de decisões em `CONSELHOS.md`. Está em `.claude/agents/maquiavel.md` e no acervo `conteudo/referencias/maquiavel/`. Para usar, escreva "chama o Maquiavel".
17. **Padrão de copy de abordagem** (17/10): Conexão → Dor → Desejo → Pergunta. Está em `agencia/prospeccao/PADRAO-COPY.md`.
18. **Legenda estilo blog SEO** (`conteudo/avaliacao-gratuita/LEGENDAS.md`).
19. **Esteira de Reels, Teste 01**: 3 formatos × 10 conteúdos × 10 ganchos = 300 roteiros de 30 s, com check e botão para enviar o print das métricas (aba Conteúdo do Recomeço 90).
20. **Reels de 45 s** vendendo os serviços para negócio local, com tom agressivo, gatilhos e ganchos (`conteudo/reels/vender-servicos-negocio-local-45s.md`).
21. **Canais dark**: capas pelo `capas2.py` (Passaporte) e pela identidade do Raposa; longos de 16 a 20 min (regras no `CLAUDE.md` e no agente Peter).

- **Carrosséis (03/11, Jaci):** telas do meio nunca repetem foto nem composição dentro do carrossel (nem a foto da capa ou do fechamento). Reprovado: as 4 telas do meio iguais (foto desfocada com véu em todas).

- **Treinamento (03/11, Jaci):** vídeos para a equipe do cliente ficam na aba Treinamento do painel, **incorporados** (assiste dentro da Central) e com o botão "Abrir no YouTube" de reserva. Lista em `dados/<cliente>.json` → `treinamento`; código genérico em `prototipo/treinamento.js`.

- **Clone de voz, teste 01** (03/11 · Pedro): Chatterbox Multilingual em português ("ficou ótimo"). Base aprovada para o app de clone. Está em `conteudo/referencias/ia-video-voz/teste/`.
- **Dublê: nome, identidade e tela v2** (03/11 · Pedro): identidade aprovada ("a identidade visual eu gostei") e tela copiada do template **Sermo** (Framer) aprovada: **"isso sim é um padrão premium"**. É a **régua de "premium"** para TUDO (03/11: "siga o mesmo padrão premium do Dublê, sempre" + "não precisa ser a mesma identidade do Dublê, sempre faça a pesquisa de templates igual você fez no Dublê e escolha um com padrão premium"). Ou seja: o premium é o PROCESSO (pesquisar templates, escolher o melhor para cada projeto, copiar a composição na identidade do cliente e citar), não o visual do Dublê. No Dublê, o escolhido foi: halo animado atrás de título gigante, menu em pílulas flutuantes, console do app logo abaixo, aviso flutuante, cartões de números reais com gráfico, título em duas cores, passo a passo numerado ao lado de painel de vidro. Sempre copiado de um template de mercado e citado. Está em `apps/clone-studio/web/` e `identidade/TEMPLATE.md`.
- **Voz do Lindson para o Dublê** (03/11 · Pedro): ele mandou 2 áudios de WhatsApp como "minha voz" (02/11 1:33 e 19/10 1:09, limpos, ruído ~50 dB abaixo). **Não vão para o GitHub** (dado biométrico; repositório público). Ficaram só na sessão da conta Pedro; no PC dele, cadastrar no Dublê como "Lindson" usando esses mesmos áudios. Já autorizou a própria voz ao enviar; para o app liberar falta só o termo e o vídeo de consentimento dele (trava do Dublê). Melhor trecho de referência: áudio de 02/11, de 1:06 a 1:18. Teste 01: "ficou ótimo, mas tem umas pausas e ruídos, deixe a voz limpa e fluida". **Regra do Dublê desde 03/11: voz limpa e fluida** = pausas curtas (~0,2 s entre frases), sem respiração artificial, sem eco, chiado e estalo do fim cortados, redução de ruído leve. Teste 02: "ficou bem melhor". Pediu voz "10 idêntica": experimento com juiz independente (`conteudo/referencias/ia-video-voz/teste/EXPERIMENTO-SEMELHANCA.md`): melhor trecho automático + identidade média de todo o áudio + temperatura 0,6 → nota 0,935 (antes 0,895; voz real 0,924), aplicado no `motor_voz.py`. Teste 03 enviado, aguardando opinião. Próximo para o "10": 20 a 30 min de áudio dele para ajuste fino (LoRA). Não removemos a marca d'água nem tentamos enganar detector. **Divulgação (03/11):** pediu 3 stories em APNG + vídeo de 30 s com a voz clonada dele dizendo que é um clone, com a foto dele no cantinho: entregues (`apps/clone-studio/divulgacao/`). Reprovou a v1: "a voz não ficou fluida, e não adianta ter minha imagem sem eu falar". **Regras:** (1) voz gerada em **blocos de até ~220 caracteres** (várias frases de uma vez), não frase por frase; (2) **nunca pôr foto parada dele em vídeo**: rosto só com a boca sincronizada (lip-sync). v2 (voz fluida, sem foto, 30 s) enviada, aguardando opinião. Lip-sync com MuseTalk bloqueado pela segurança da sessão na nuvem; ele precisa autorizar ou rodar no notebook dele. **Vídeos dele** (03/11): 9 selfies de WhatsApp de 19/10 (464×832, 60 fps, ~2 min no total; melhores v9 50 s e v4 37 s), segurando um microfone de lapela perto do queixo. Também fora do Git. Para o vídeo base ideal: microfone preso na camisa e mãos abaixadas, porque mão perto da boca atrapalha a sincronização.

- **Artes v2 da marca pessoal do Lindson APROVADAS** (03/11 · Pedro): capa de Reels "Post de bom dia não vende nada" (foto colorida inteira com a luz do estúdio, degradê preto, manchete Manrope com a palavra-chave em caixa amarela, rótulo mono amarelo) e post "Papo reto" (foto à direita, texto à esquerda, aspas amarelas gigantes). São os 2 modelos de todas as artes dele (`agencia/marca-lindson/artes-v2/`).

- **16 artes v2 da marca pessoal APROVADAS** (03/11 · Pedro): "aprovado" (`agencia/marca-lindson/artes-v2/`). Pedido junto: "não se esqueça de que quero um perfil harmônico, então use o amarelo de fundo também, encontre um jeito, busque referências" → o feed precisa alternar fundo preto e amarelo (a capa amarela "BIO" vazada continua reprovada).

- **Versões premium APROVADAS** (03/11 · Pedro): a1p, r1p, p1p, c2yp (`artes-v2/artes.html`): selo de vidro fosco no rótulo, cantos de corte + numeração (01), vinheta e grão de filme, letra gigante com luz (degradê), sombra dele projetada nas letras, halo só atrás de recorte (nunca por cima do rosto), brilho anamórfico só em cima do neon. Pedido seguinte: "crie as próximas e crie uma foto de perfil e capas de destaques".

- **Semana 2, foto de perfil e 6 capas de destaques APROVADAS** (04/11 · Pedro): "todos aprovados" (`artes-v2/artes.html` ids s2_*, `artes-v2/perfil.html`). Pedido seguinte: "crie mais 10 modelos diferentes entre amarelo e preto buscando as referências premium".

## 4. REPROVADO: nunca repetir

0c. **Capas amarelas a2y, c1y e r3y** (03/11 · Pedro): "os outros estão reprovados". Não usar foto "nascendo" do amarelo em degradê, nem pessoa pequena no amarelo com lista ao lado. **Amarelo APROVADO = c2y**: amarelo com textura, palavra gigante preta (Anton) atrás dele, ele recortado (BiRefNet) de corpo inteiro na frente, degradê preto embaixo com a manchete branca e a palavra em caixa amarela. Pediu em seguida: "busque maneiras e técnicas para melhorar ainda mais os que já aprovei, implementar, deixar mais moderno, premium, bonito e atrativo".
0b. **Capa de carrossel amarela com "BIO" vazado e foto em cartão** (v2, 03/11 · Pedro): "reprovado". Não usar fundo amarelo chapado com letra de contorno nem foto dentro de cartão. Aprovados: fundo escuro com a foto colorida, amarelo só no acento. Apresentação "LINDSON" atrás dele: "gostei dessa", mas o recorte do corpo (terno escuro no fundo escuro) saiu com degrau: agora o corpo vem da própria foto e o recorte só aparece na cabeça e nos ombros, onde o nome passa por trás.
0. **Artes v1 da marca pessoal do Lindson com foto em preto e branco** (03/11 · Pedro): "não gostei, achei as fotos também muito cinzas, busque referências premium, melhores". Nunca usar foto dele P&B lavada; usar foto COLORIDA cinematográfica (v2: Jonatas Torres + INFLURY + Man UpRight, `agencia/marca-lindson/identidade/TEMPLATE.md`). Pediu também: "quero meu perfil harmônico em preto e amarelo" e subiu 17 fotos de estúdio na aba Minhas fotos do admin (criada 03/11).
1. **Elementos gráficos na identidade do Leo**: raios, faixas de padrão, ícones, fumaça, sol desenhado e bandeirinhas. Motivo: "esses elementos estão feios" (02/11). A identidade do Leo é só fontes, logo e cores.
2. **Foto de perfil v1 do Leo** (raios atrás da cabeça, anel, foto leo-23). Motivo: ele pediu cor sólida, sem raios e uma foto melhor.
3. **Logo do Leo com balão, cápsula ou placa de fundo**. Motivo: "não gosto dessa logo com esse balão de fundo, prefiro ela aplicada ao post" e, de novo, no Natal.
4. **Logo fina demais e sem destaque.** Motivo: some na arte. Use letras cheias e contorno.
5. **Logo vertical do Leo com o sol no lugar do "O"** usada sozinha. Motivo: lê-se "LE PINTO".
6. **Logo marinho com o centro do sol escuro.** Motivo: parecia um bonequinho dentro do "O".
7. **1º estilo das datas comemorativas do Leo** (v14 inicial). Motivo: "exclua esses estilos das datas, eu não gostei".
8. **Datas v3 e v6, exceto as aprovadas** (canteiro de obras ao pôr do sol no 11/12, Natal só de luzes azuis, Ano Novo só tipográfico com balões dourados, entre outras). Motivo: "não gostei das outras"; ele quer estilos mais profissionais, modernos, jovens e tecnológicos, como os grandes players usam.
9. **01/01 com um Leo bem mais alto que o outro** (novo em cima, velho embaixo). Motivo: "ficou horrível". Os dois ficam na mesma altura, cada um olhando para um lado.
10. **Cortes aparentes nos recortes de foto** (borda reta na cintura, no braço ou no cotovelo). Motivo: "não pode aparecer cortes".
11. **Fundo azul chapado sem textura.** Motivo: fica "duro". Ponha uma foto quase transparente no fundo para compor.
12. **Painel do administrador como "organizador" de cartões**, ou página solta que só leva para outros apps. Motivo: ele quer um sistema completo no visual original da Central, com tudo dentro dela.
13. **Apps com identidade diferente da Central.** Motivo: "quero com a mesma identidade todos".
14. **Refazer os apps dos canais dark.** Motivo: "não precisa refazer, apenas vincule à Central".
15. **Identidade v1 da Dra. Jaci** (inventada). Motivo: não era a marca dela, que já existia (bordô e dourado).
16. **Dados e artes de exemplo do modelo nos painéis.** Motivo: ele mandou retirar ("retire as que estavam lá de exemplo").
17. **Mexer na esteira de produtos** (até R$ 3.500). Motivo: "não mexa neles".
18. **Arte criada do zero, sem modelo.** Motivo: regra "nada se cria, tudo se copia".
19. **Rabiscos à mão, estrelas, emojis, adesivos, ícones 3D, papel rasgado e sombra 3D** nas artes do Leo. Motivo: são grafismos, proibidos desde 02/11.
20. **Cor da roupa trocada por edição** (deixou manchas na manga). Motivo: tem cara de amador. Realce a cor só de leve.
21. **Tela de app com cara de Gradio/formulário padrão** (Dublê v1, 03/11). Motivo: "o template não". Tela de app é copiada de um template premium pesquisado (régua: Sermo).
22. **Voz clonada gerada frase por frase** (Dublê, vídeo v1, 03/11). Motivo: "a voz não ficou fluida". Gerar em blocos de várias frases.
23. **Foto parada da pessoa num vídeo em que ela "fala"** (03/11). Motivo: "não adianta ter minha imagem, sem eu falar". Só com lip-sync.
24. **Reusar o visual do Dublê em outro cliente** (manual da Real Time v1, 03/11). Motivo: "o padrão premium não precisa ser a mesma identidade do Dublê". Pesquisar templates e escolher um premium para cada projeto.

## 5. Regras por cliente

**Vereador Leo Pinto** (São João Batista/MA, mandato, não campanha)
- **Cores:** laranja principal (partido); azul royal #2350F5 e marinho #082063 como apoio; amarelo #FFC20E nos destaques. No feed, xadrez laranja e azul.
- **Fontes:** Montserrat Black (nome e frases), Kaushan Script (toque manuscrito), Anton (títulos condensados das datas).
- **Logo:** a oficial, aplicada direto no post e sempre "LEO PINTO" por extenso. No laranja, usar a versão marinho forte.
- **Pode:** foto real do álbum (30 fotos de estúdio), recortada e posicionada pelo rosto; foto de banco como cenário com véu; mapa oficial da cidade em camada; cartão de checklist ou enquete na frente do peito; palavra repetida atrás.
- **Assinatura fixa:** o @ no topo e a logo na base.
- **Não pode:** grafismos (seção 4); número de urna; pedir voto; falar de 2028; atacar adversário (Lei Eleitoral, art. 36-A).
- **Antes de publicar, conferir:** "mais bem votado" no TSE 2024.
- **Grade:** apresentação de 3 posts com sangria de 34 px. Postar na ordem 3, 2, 1 e fixar as três.
- **Foto de perfil e artes:** imagens do cliente ficam fora do Git.

**Dra. Jaci Cunha** (clínica em Zé Doca/MA)
- **Cores e fontes:** bordô e dourado; Cormorant Garamond + Montserrat no manual. Nos posts: serifada itálica de alto contraste e sans geométrica, fundo creme, faixas vinho e douradas.
- **Assinatura fixa** em todo post: topo com 3 colunas, rodapé com o nome e a clínica.
- **Foto:** a Dra. Jaci grande, em estúdio claro com sombra de janela. Use as 8 fotos de `fotos/`.
- **Regras do CFO:** sem promessa de resultado. Antes e depois só com autorização da paciente, e foto de paciente nunca vai para o Git.
- **Copie as composições do guia** `instagram-estilo/README.md`.
- **Faltam dela:** logo em vetor e fotos em alta.
- **Aprovação:** pelo WhatsApp em até 48 h, com 2 rodadas de ajuste (contrato).

**Rafael Imports e Desentupidora SF**
- **Desentupidora SF (03/11 · Zuleide):** artes v1 aprovadas = padrão (`agencia/clientes/desentupidora-sf/instagram-v1/`): identidade do site (marinho, royal, laranja, Montserrat itálico 900), assinatura logo + @desentupidorasf_slz + WhatsApp no rodapé, modelos do Designi, ganchos pela dor. Painel em /painel/sf.
- Mini site no repositório privado de cada cliente, publicado na Cloudflare Pages (`nomedocliente.pages.dev`), nunca dentro do `lindson`.
- Fotos reais, pedidas uma por mensagem.
- Desentupidora: falta Pixel e UTM antes de medir a campanha.

**Passaporte da Bíblia**
- **Capas:** só pelo `capas2.py`: gravura de Doré com cor de cinema, etiqueta ciano e título branco com palavra-chave amarela.
- **Duração:** longos de 16 a 20 min; Shorts de 45 a 70 s.
- **Antes de mexer:** leia o BRIEF, o PROCESSO e o agente Peter.

**Raposa e Leão**
- **Capas:** fundo escuro, retrato P&B com brilho, etiqueta dourada com a fonte, Anton com 1 palavra em ouro, no máximo 1 tarja vermelha e selo no rodapé.
- **Duração:** longos de 16 a 20 min; Shorts de 35 a 45 s pelo `short2.py`.
- **Situação:** longos 13 a 16 pausados a pedido do Lindson; só retomar quando ele mandar.

**Lindson (marca pessoal)**
- **Identidade:** marca escura ("no ar", sinal, território do Maranhão), Bricolage Grotesque + Manrope, um único elemento de ação por tela (`branding/README.md`).
- **Voz:** "você", frases curtas, números exatos, sem jargão.
- **Na peça gráfica:** sem emoji.

## 6. Padrões de copy, legenda, carrossel, post, prospecção, SDR, contratos e PDFs

1. **Legenda:** estilo blog SEO. Título com a palavra-chave, introdução, subtítulos, exemplo, conclusão e chamada, até 2.200 caracteres. Use 3 a 5 hashtags variadas (tema + nicho + local), nunca o mesmo bloco.
2. **Carrossel:** depois da capa, nenhuma tela repete o layout da anterior.
3. **Post estático:** nunca dois seguidos com a mesma composição nem a mesma cor. Alterne foto e só logo.
4. **Abordagem e copy curta:** Conexão → Dor → Desejo → Pergunta, até 280 caracteres, linguagem de WhatsApp, entendida numa leitura só.
   - **Proibido:** "vi que", "parece que", "gargalo", jargão e análise do perfil.
5. **Roteiro de venda:** gancho forte, retenção (recompra de atenção) e gatilhos. Tom agressivo quando ele pedir.
6. **Apps de prospecção e SDR:**
   - **Botão WhatsApp** em cada contato, com a mensagem da etapa pronta (`wa.me/55…?text=`).
   - **Ao clicar:** registra o envio e avança a etapa sozinho. Sem número de WhatsApp, o botão copia a mensagem.
   - **Fila de contato:** só entra lead com WhatsApp (celular) **e** Instagram.
7. **Estratégia para lead que disse "pode mostrar":**
   - **Formato:** PDF de 19 páginas 4:5, na identidade do cliente (`modelo-estrategia/README.md`).
   - **Proibido:** preço e números inventados.
   - **Versão curta:** 8 páginas.
8. **Demo de mini site para vender:** só o vídeo em tela de iPhone, sem publicar (`demo-minisite/`).
9. **Contrato:**
   - **Modelo:** `modelo-contrato/`, entregue em PDF A4.
   - **Dados:** os do Lindson e os do cliente ficam fora do GitHub. Se faltarem, peça.
10. **PDFs entregues:** também vão para a página de downloads. A do `CLAUDE.md` (3Vn9…) é de outra organização; a conta Lindson usa a Downloads Lindson (VLijrTZy…).
11. **Painel novo de cliente:** sempre a partir de `prototipo/painel.html` + `montar-<cliente>.py`, nunca do zero.
12. **Identidade visual de cliente:** use o prompt do Claude Design (`leo-pinto/identidade/PROMPT-CLAUDE-DESIGN.md`) com o BRIEF do cliente. Se o cliente já tem identidade, documente a que existe.

## 7. Pedidos que ele já fez (responda "já foi feito")

| Data | Pedido | Situação | Onde |
|---|---|---|---|
| 22/10 | Agentes Xquads disponíveis | pronto | `instalar-xquads.sh` |
| 22/10 | Produto master (curso + mentoria para donos de negócio) | pronto | `agencia/ofertas/produto-master.md` |
| 22/10 | 10 maiores autoridades do nicho, bios e links (incluindo Valter Azevedo e Afonso Molina) | pronto | `agencia/ofertas/pesquisa-autoridades-instagram.md` |
| 22/10 | Dores e desejos do público, com versão negativa | pronto | `agencia/ofertas/dores-e-desejos.md` |
| 22/10 | 10 formatos que mais engajam | pronto | `conteudo/formatos-que-engajam.md` |
| 22/10 | Esteira de Reels: 300 roteiros, check e upload de métricas | pronto; aguarda as métricas | aba Conteúdo do Recomeço 90 · `conteudo/esteira/` |
| 01/11 | 3 contas como equipe (nunca refazer, avisar pedido repetido) | pronto | `CLAUDE.md`, `QUADRO`, `REGISTRO`, `MAPA` |
| 01/11 | Prompt para todas as contas | pronto | `PROMPT-DA-EQUIPE.md` |
| 01/11 | Informações da Dra. Jaci e o PDF de identidade dela | pronto (v2, a real) | `agencia/clientes/jaci-cunha/` |
| 01/11 | Central: página da Jaci, código de admin e site publicado | no ar | https://lindsonalmeida.pages.dev |
| 01/11 | Dados reais dos clientes nos painéis | no ar | `CentralLindsonALmeida/dados/` |
| 01/11 | Jaci: CRM, financeiro e notícias do nicho | no ar | painel da Jaci |
| 01/11 | Linhas editoriais nos sites de cada cliente | no ar | tela Planejamento |
| 01/11 | Calendário editorial da Jaci (novembro) | pronto (Zuleide) | `jaci-cunha/estrategia/LINHAS-EDITORIAIS-NOV.md` |
| 01/11 | 4 quadros para o Instagram do Leo | sugeridos; ele ainda não escolheu | `leo-pinto/estrategia/QUADROS.md` |
| 01/11 | Envio de fotos funcionando no site | no ar | `prototipo/fotos.js` |
| 01/11 | Conectar o Nano Banana | script pronto | `ferramentas/nano_banana.py` |
| 01/11 | 30 fotos do Leo no sistema dele | no ar | painel do Leo › Fotos |
| 01/11 | Vídeos tutoriais com voz (Jaci e Leo) | entregues | `agencia/processos/demo-minisite/` |
| 01/11 | Datas comemorativas para os dois clientes (nov/26 a out/27) | pronto | `*/estrategia/DATAS-COMEMORATIVAS.md` |
| 01/11 | Varredura de erros nos sites | pronto | `REGISTRO` |
| 02/11 | Abas do admin, apps dentro da Central com a mesma identidade, animações | no ar | `site/admin-sistema.js`, `admin-apps.js` |
| 02/11 | Permitir tudo nas sessões | pronto | `.claude/settings.json` |
| 02/11 | Agente Maquiavel completo + dinheiro online | pronto v2.1; revisão continua | `.claude/agents/maquiavel.md` |
| 03/11 | "Quando terminar tudo, finalize o agente" | **feito: v3.2 final**, revisão concluída, 20/20 nos testes (Zuleide) | `.claude/agents/maquiavel.md`, `conteudo/referencias/maquiavel/TESTES.md` |
| 02/11 | Reels de 45 s vendendo serviços para negócio local | pronto | `conteudo/reels/vender-servicos-negocio-local-45s.md` |
| 02/11 | Foto de perfil do Leo | v2 pronta | `leo-pinto/instagram-perfil/` |
| 02/11 | 3 primeiras artes do feed do Leo + legendas + aprovação no site | aprovado (v13 v3) e no painel | `leo-pinto/instagram-v13-apresentacao/` |
| 02/11 e 03/11 | 6 datas comemorativas do Leo com tag, legenda e prévia do feed | aprovadas e no painel | `leo-pinto/instagram-v14-datas/` |
| 03/11 | Aprender o estilo das artes da Dra. Jaci | pronto | `jaci-cunha/instagram-estilo/README.md` |
| 03/11 | Calendário editorial do Leo (nov a jan) e quem aprovou cada arte (nome do cliente pela conta) | no ar | painel do Leo › Aprovações e Calendário |
| 03/11 | Painel da Desentupidora SF na Central, com código de acesso | no ar (Zuleide) | https://lindsonalmeida.pages.dev/painel/sf |
| 03/11 | 4 artes da Desentupidora SF | **aprovadas pelo Lindson** ("aprovado, pode subir") e no painel do cliente (Zuleide) | `agencia/clientes/desentupidora-sf/instagram-v1/` |
| 03/11 | Real Time: reformulação do Instagram, plano de vendas, painel e mini site | Instagram, estratégia e painel feitos por Pedro e Leandro; mini site em rascunho (Zuleide), aguardando o repositório do cliente | `agencia/clientes/rt-full-jobs/` |
| 03/11 | Todas as possibilidades de produtos low ticket (lista primeiro) | lista pronta (Zuleide): 118 produtos, 10 serviços e 11 kits | `agencia/ofertas/low-ticket/LISTA.md` |
| 03/11 | Lista de todos os agentes por categoria | pronto (Zuleide) | `AGENTES.md` |
| 03/11 | Este documento de memória, compartilhado com todas as contas | pronto | `MEMORIA-DO-LINDSON.md` |

## 8. Pendências abertas

0. **Cliente novo RT Full Jobs** (03/11 · Zuleide → Pedro): produtora audiovisual @realtime_fulljobs. Tudo em `agencia/clientes/rt-full-jobs/`. Pedro (03/11): estratégia completa 19 p. (modelo Villa; PDF no privado `dados/clientes-arquivos/rt-full-jobs/estrategia/`) e, a pedido ("refaça a logo e o manual de marca"), **identidade v1** premium (símbolo visor + rt + ponto REC; wordmark "realtime"; manual 20 p.) em `identidade/v1/`, aguardando aprovação. Falta: estratégia no padrão premium com a marca nova, Instagram v1, painel na Central e mini site.

1. **Agente de criatividade**, criado do mesmo jeito que o Maquiavel. Ele monta as identidades das artes junto com o time, seguindo a regra "nada se cria, tudo se copia". Foi pedido para depois da aprovação das artes do Leo, que já aconteceu.
2. **Artes da Dra. Jaci** copiando o estilo dela, depois que as do Leo acabarem.
3. **Leo:** o Leo precisa aprovar as 9 artes no painel.
   - **Datas a confirmar:** a data da apresentação (05/11 foi escolhida pela conta) e o aniversário de São João Batista.
   - **A conferir no TSE:** "mais bem votado".
   - **A escolher:** os 4 quadros.
4. **Nano Banana:** o Lindson ativa o faturamento no Google. Em 03/11 o Gemini de imagem já respondeu numa sessão, então confirme antes de cobrar dele.
5. **Apagar os apps originais do claude.ai** que já estão dentro da Central. Só quando ele mandar ("depois").
6. **Liberar os domínios bloqueados** para a próxima revisão do Maquiavel (treccani.it, degruyter.com, hal.science, planalto.gov.br). A revisão continua com a Zuleide (pendências 2 e 3).
7. **Dra. Jaci:**
   - **Executar** as semanas 1 e 2 da estratégia.
   - **Pedir:** logo em vetor e fotos em alta.
   - **Confirmar:** aniversário da clínica.
8. **Carrosséis da esteira** de conteúdo, no mesmo modelo dos Reels.
9. **Teste 01 de Reels:** esperar os prints das métricas e decidir o Teste 02.
10. **Produto master:**
    - aula grátis;
    - turma piloto;
    - assistentes de IA;
    - garantia.
11. **Central:**
    - conferir no ar se "Notícias do nicho" carrega;
    - chave de IA da Fábrica e das propostas;
    - painel da Apple Black, que ainda não existe.
12. **Desentupidora SF:** Pixel da Meta, UTM e Facebook Ads no Supermetrics.
13. **Leo:** mockups de boné e bandeira. Ainda falta o @ oficial, as entregas do mandato, as causas e os bairros.
14. **Canais dark:** faltam longos do Passaporte (01, 02, 09) e do Raposa (01, 05; 13 a 16 pausados) e subir nos apps os longos já entregues. Só retomar o Raposa quando ele mandar.
15. **Tarefas agendadas** da conta Lindson (leads diários, cidades, notícias BOMBOU): desligadas desde 26/10. Só religar com o OK dele.
16. **App de clone de imagem e voz** (pedido 03/11 · Pedro): uso **interno**; roda no **computador do Lindson**; clona o próprio Lindson, clientes **com termo de autorização** e personagens dos canais (domínio público). Pesquisa em `conteudo/referencias/ia-video-voz/` (HeyGen, ElevenLabs e outras ferramentas). PC: RTX 3050 4 GB, 24 GB RAM (pilha em `PLANO-DO-APP.md`). Nome e identidade (03/11): **Dublê**, grafite + violeta Eco #8B7CFF, amarelo da Central só no consentimento, fontes Geist + Manrope (`apps/clone-studio/identidade/`): **identidade APROVADA** ("a identidade visual eu gostei"). **Template Gradio REPROVADO** ("o template não"): tela v2 copiada do Sermo (Framer), `identidade/TEMPLATE.md`; aguardando OK.
17. **Real Time, legendas v1** (03/11 · Leandro): 8 legendas do feed e figurinhas dos stories em `agencia/clientes/rt-full-jobs/instagram-v1/LEGENDAS.md`, aguardando OK. Falta confirmar a cidade e o bairro do estúdio (briefing só diz Maranhão) e conseguir falas reais de clientes para o post 05 e o story 03.
18. **Real Time, estratégia v2** (03/11 · Leandro): 19 páginas com a marca nova em `agencia/clientes/rt-full-jobs/estrategia/v2/`, aguardando OK. Feita sem acesso à v1 (privado); quem tiver acesso compara as duas.
19. **Real Time, painel e perfil** (03/11 · Leandro): pediu "crie nova bio, novos destaques" (feito, `instagram-v1/perfil/`), apontou que faltava o rebranding no manual (página antes × depois acrescentada) e mandou "suba o painel do cliente e todos esses conteúdos lá": painel /painel/rt no ar, com aprovações e arquivos. Aprovação das artes agora é do cliente no site.
20. **Mensagem de acesso à Central** (03/11 · Leandro): a oficial é a curta do Leo (saudação, o que faz no painel, link, código, "depois é só entrar com seu e-mail e senha"). Modelo em `agencia/processos/mensagem-acesso-central.md`. A versão longa com passo a passo e lista não é o padrão.
21. **Leo, modelo de aniversário** (03/11 · Leandro): v1 (título + nome + foto, copiada do Designi Paulo André) **reprovada**: "está muito simples… quero algo detalhado e criativo". Regra nova: **buscar referências em sites externos e aplicar a nossa identidade, sem copiar as nossas próprias artes** ("para não ficar tudo igual"). v2 combina 3 modelos externos (Carla Silva, Pr André Vieira, Pedro Sampaio), aguardando OK. Bio v2 do Leo em `instagram-perfil/BIO.md`, aguardando OK.
22. **Real Time, fotos dos equipamentos** (03/11 · Leandro): pediu "pesquise fotos reais de todos os materiais que a Real Time trabalha". 56 fotos reais (fabricante, Wikimedia Commons, Pexels) em `agencia/clientes/rt-full-jobs/fotos-equipamentos/`, com licença de cada uma em `FONTES.md` (livre × do fabricante). Fotos do próprio equipamento da RT continuam sendo as melhores; pedir ao cliente. Confirmar com ele: STORM 1200 (1200x ou 1000c?), amaran 300c, Mirage ou Mirage Pro, 24-70 GM ou GM II, Solidcom C1, modelo do teleprompter e dos modificadores.
22. **Leo, aniversário do Josef APROVADO** (03/11 · Leandro: "aprovado" + "pode subir no painel"): está nas Aprovações do painel do Leo (1º card, Leo de perto). Ajustes pedidos e feitos: avatar do @ = **a foto de perfil oficial** (busto, polo amarela, fundo laranja), "FELIZ ANIVERSÁRIO" na ordem certa (nome embaixo). **Regra nova: sempre enviar a arte na conversa para ele ver e subir sempre em alta qualidade** (gerar em 2×, 2160×2700; no painel, 1080×1350 qualidade 92).
23. **Leo, aniversário** (03/11 · Leandro): o cliente não gostou do modelo A (aprovado pelo Lindson e no painel). Feitos os modelos B e C e a foto melhorada (Real-ESRGAN). Regra: **sempre melhorar a qualidade da foto antes de usar** (`ferramentas/melhorar_foto.py`).
24. **Leo, aniversário modelo B APROVADO** (03/11 · Leandro: "aprovada, mande a legenda e faça um pra storys"): modelo B (editorial claro) é o padrão de aniversário; tem versão story (`"story":true`). No painel, o post B e o story substituíram o modelo A.
25. **Real Time, artes v2** (03/11 · Leandro): "missão do Leo concluída por agora, continue o trabalho da Real Time". 6 artes com as fotos reais dos equipamentos, referências externas diferentes em cada post, marca nova v1, em `agencia/clientes/rt-full-jobs/instagram-v2/`, aguardando OK.
26. **Central: botão de baixar** (03/11 · Leandro): "no painel não tem botão de download para baixar os conteúdos aprovados, coloque o botão em todos". Feito em todos os painéis (e no modelo). **Regra: todo card de aprovação tem "Baixar arte".**
27. **Real Time: conteúdo de todos os materiais** (03/11 · Leandro): "busque por todos os materiais que eles citam, e vamos criar conteúdos com todos eles". Série Inventário com 14 posts (um por item; o "STORM 1200" sem x fica de fora até o cliente confirmar o modelo) + as 6 artes v2, todas no painel.
28. **Real Time, dois sites** (03/11 · Leandro): "quero um mini site pra bio do insta e um site de verdade principal, pra ranquear no google". Padrão novo para cliente: **site principal de SEO na raiz + mini site da bio em /bio/** no mesmo projeto Cloudflare (bio com noindex). Site da RT: https://realtimeslz.pages.dev (template GAFFER).
29. **Dra. Jaci, bio, destaques e site** (03/11 · Leandro): "melhore a bio da dra jaci e vamos reorganizar os destaques e fazer um site oficial pra ela". Bio v2 e 7 destaques (Avaliação, Harmonização, Odonto, Dúvidas, Pacientes, A Clínica, Como chegar) entregues; site no padrão da Real Time (site de SEO + /bio/ com chat), template Solenne, aguardando repositório e WhatsApp da clínica.
30. **Cliente novo: Tribuna 98, Thiago Azevedo** (03/11 · Leandro): jornalismo político do Maranhão; ficha em `agencia/clientes/tribuna98/README.md`. Falta saber o que foi contratado.
31. **Tribuna 98, bio, mini site e destaques** (03/11 · Leandro): "quero um minisite pra bio dele, uma nova bio capas de destaques, sempre usando a regra de busca de referencias e templates premium". Quando o cliente já tem site/blog próprio, o pages.dev é só a bio (na raiz) e puxa as manchetes do blog ao vivo. Aguardando OK.
32. **Foto usada não se repete** (04/11 · Leandro, regra para todas as contas): "sempre que usar uma foto em um conteúdo, coloque essa foto em uma aba USADA para não repetir. priorize as capas para usar fotos, se for carrossel, usar na primeira e última, e no meio pode usar imagens realistas de banco". Aba Fotos do painel ganhou Disponíveis/Usadas; processo em `agencia/processos/fotos-usadas.md`.
