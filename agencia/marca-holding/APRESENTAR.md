# Barzakh · tudo o que podemos apresentar (feed, Behance, Pinterest)

Conta Zuleide (sessão Barzakh, agente Social media), 20/11/2026 · **AGUARDANDO DECISÃO DO LINDSON** (itens no fim).
Pedido: "no feed eu quero mostrar a qualidade do que fazemos; vamos também usar Behance e Pinterest. Liste tudo que podemos apresentar, use os agentes, veja o padrão de qualidade e exigências."
Referências dele (Pinterest, 20/11): privado `dados/agencia/referencias/branding-mockups-barzakh/` ref-01 a ref-05.
Prompts e método das cenas: `prompts-mockups/` (nesta pasta).

> **Decisão nova do Lindson (20/11): "não precisa ter minha imagem na marca".** A Barzakh **não usa a foto nem o rosto do Lindson** em nenhum canal (feed, destaques, Reels, banner, thumbs, Behance, Pinterest, LinkedIn). A autoridade vem dos **cases, do processo e do acabamento**. O nome dele pode aparecer só em texto de crédito ("Direção criativa: Lindson Almeida"). Isso substitui a regra de 16/11 ("feed precisa de rosto do Lindson"). A energia que tirou o feed do "morto" e do "sem vida" passa a vir da **cor dos cases, do objeto grande e da manchete gigante**, não do rosto.

---

## 0. O que as 5 referências ensinam (e o que não copiar)
| Ref | O que é | Lição para a Barzakh |
|---|---|---|
| 01 MOYA | flat lay de cima: boné, camiseta, ecobag, copo térmico, caneca, avental, caderno, cartões, tag, crachá, papel de seda, sacola, em fundo bege | **a marca vira família de objetos**: 15 a 20 itens, 2 cores, mesma luz, grade arrumada com respiro igual entre os itens |
| 02 brew. | linha de embalagem em cena de estúdio (copo, pouch, caixa, porta-copos, cartão), pedestal de pedra e sombra de folha | **embalagem em degraus** (alturas diferentes), 1 grafismo da marca repetido em escala gigante |
| 03 café de luxo | kit preto e dourado de cima, fundo grafite | é o **mesmo universo da Barzakh** (preto + ouro): bom para o case da própria Barzakh e dos clientes escuros (WF, Real Time) |
| 04 Fork & Flame | delivery: sacola kraft, marmitas com cinta, copo, bowl, cardápio, talher | **o produto do cliente aparece na embalagem** (comida, café): cena de uso, não só objeto vazio. Serve à Orégano Turbo |
| 05 kupss | brand board: logo grande + versões + paleta com hex + 4 janelas de mockup em grade | **uma tela resume a identidade inteira**: é o melhor formato de capa de carrossel, pin e capa de Behance |

Não copiar: os logos, as marcas e os textos delas (estudo). Três delas são imagem de IA com marca **inventada** (a ref-05 traz o selo "Modificado por IA"). Para cliente real, o logo tem de ser **o oficial e idêntico**. Esse é o problema que o método da seção 2 resolve.

Ponto em comum: a marca **aplicada em muitos objetos reais**, com a mesma luz e a mesma paleta, e cara de case de estúdio. É exatamente o que o Lindson já pediu em 16/11: "apresentação de designer = mockups fotorrealistas e imersivos, nunca slide recortado".

---

## 1. O time (arquivos lidos) e o que cada um deu
| Agente | Arquivo | Contribuição |
|---|---|---|
| **Social media** (lidera) | `.claude/agents/social-media.md` | linhas, xadrez do grid, intercalar vídeo e estático (4 em 4 h), legenda SEO, 1 objetivo por post, destaques pela jornada |
| **Designer gráfico** (executa) | `.claude/agents/designer-grafico.md` | "nada se cria, tudo se copia": cada formato copia a composição de uma ref (tabela da seção 0). Mockup é a prova (régua de 06/11: Decaf Girl, HOTWHIZ). Imagem de IA sempre marcada |
| **Alina Wheeler** (brand-squad) | `/root/.claude/commands/brand-squad/agents/alina-wheeler.md` | case em formato **objetivo → processo → estratégia → solução** e "toda aplicação reforça a mesma mensagem" (touchpoints). Daí a estrutura fixa do case (seção 3c) e o checklist de consistência |
| **Brand Chief** (brand-squad) | `brand-squad/agents/brand-chief.md` | não existe uma resposta só: **diferenciação** (conceito com significado: Kántara/ponte, Barzakh/passagem) + **distintividade** (os mesmos ativos repetidos: arco, monolito, ouro). Todo post da Barzakh leva 1 ativo fixo (arco ou monolito) no rodapé |
| **Design Chief** (design-squad) | `design-squad/agents/design-chief.md` | **sistema antes de peça**: 6 moldes fixos (flat lay, linha de embalagem, brand board, processo, antes/depois, manchete), um gerador só, consistência e "todos os estados": cada molde em claro e em escuro |
| **Copy Chief** (copy-squad) | `copy-squad/agents/copy-chief.md` | público "consciente do problema" (Schwartz): manchete pela dor ("SUA MARCA PARECE MENOR?") e prova logo depois; headline "diferenciação + prova"; legenda conta o desafio do cliente, não elogia o estúdio |
| **Hormozi Content** (hormozi-squad) | `hormozi-squad/agents/hormozi-content.md` | **dar o "o quê" e o "porquê", vender o "como"**: carrossel de processo e dica é grátis, a execução é o pacote. Gancho, retenção e recompensa em todo Reel; volume e constância vencem a peça genial isolada (1 case por semana, repurposing em 4 canais) |
| **Maquiavel** (gerente) | `.claude/agents/maquiavel.md` | "o cliente julga pelo que vê" (*Príncipe* XVIII): reputação vem de **grandes obras mostradas**. Abrir com o que é nosso e incontestável (Barzakh, Al Kántara, Orégano, Dublê), depois os pagantes autorizados. **Leo nunca abre a vitrine** (situação, político). Nada de número inventado; prova só com print real |

Nota do crivo (Maquiavel, conferência deste documento): 9/10. O ponto que falta é de execução: as cenas ainda não foram renderizadas nem conferidas com zoom (seção 4).

---

## 2. O método certo para mockup com logo (regra 18/11 "nada de montagem de foto")

**O que o repositório já decidiu:**
1. **18/11 (Leandro, Mova):** proibido colar tela, anúncio ou logo **em perspectiva** numa foto, juntar fotos, inserir recorte numa cena. A cena vem inteira da IA; por cima só tipografia e **logo plana**, como assinatura.
2. **18/11 (Pedro, Al Kántara, commits `9b877a2f` "regra Gemini sem logo" e `340da260` "prompts v4 sem logo"):** o Gemini **redesenha o logo e erra o K**. Regra: o Gemini faz só a cena, com **superfícies lisas**. O logo oficial é aplicado por nós depois. No commit `080bdcb2` ("imagens Gemini com o logo oficial aplicado"), o logo entrou **plano, numa área vazia** (assinatura no pé do post), e não impresso num objeto.
3. **06/11 (Leandro, Orégano, `2f0de398`):** o kit "logo PNG anexado ao Gemini" funcionou para alguns itens. Quando errava, o logo era "corrigido por cima" (o avental foi corrigido por clonagem). **Essa correção agora é montagem: está proibida.**
4. **16/11 (Leandro, Projeto Designer v2):** mockups **3D em Three.js** com o logo oficial como **textura** (`projeto-designer/v3/gerador/texturas.py` + `cenas.js` + `mockups.py`). O logo é idêntico, a luz e a sombra saem do próprio render e nada é colado numa foto. É o único caminho que já existe e cumpre as duas regras.

**Método proposto (3 trilhos, cada imagem num só):**

| Trilho | Quando usar | Como | Por que não é montagem |
|---|---|---|---|
| **A · Render 3D com a textura oficial** (PADRÃO) | todo objeto que **leva o logo**: flat lay de papelaria e merch, linha de embalagem, kit escuro, cartão, sacola, copo, caixa, boné, camiseta | o gerador do Projeto Designer, ampliado com 12 objetos novos (seção 4, passo 2), com luz de estúdio, sombra de janela (gobo), chão de concreto ou papel e grão. Saída 2160×2880 (3:4) e 2800 px (Behance) | a cena inteira é um render só, e o logo é a **estampa do objeto** dentro do render, não uma camada colada numa foto |
| **B · Cena Gemini SEM logo + assinatura plana** | atmosfera e mãos: mesa do estúdio, rabisco no papel, material (pedra, papel algodão, hot stamping vazio), bastidor, fundo de manchete | prompt da pasta `prompts-mockups/` com o final fixo "sem logo, sem letra, sem texto, superfícies lisas". Por cima só a manchete e o logo **plano**, numa área vazia | é a regra aprovada (Mova v5 e Al Kántara v4) |
| **C · Gemini com o logo anexado** (TESTE, depende do Lindson) | 1 imagem-herói "lifestyle" por case (ex.: copo do cliente na mão, sacola na rua), onde o 3D fica artificial | Nano Banana com o PNG oficial anexado, superfície **de frente** para a câmera. Aprovação: **sobrepor o SVG oficial a 100% de zoom**. Se uma letra, a proporção ou o espaçamento mudar, a imagem é **descartada** (nunca corrigida por cima) | o logo nasce dentro da cena, num prompt só. Fere só a regra de Pedro de 18/11 (feita porque o Gemini errava), e o teste de sobreposição responde a ela. **Por isso precisa de OK do Lindson** |

**Proibido nos três:** colar PNG em perspectiva, juntar duas fotos, pôr pessoa recortada na cena, corrigir logo errado por clonagem, foto do Lindson.
**Brand board (ref-05)** é uma prancha gráfica (grade de janelas com renders A e paleta com hex), e não finge ser foto. É permitida.
**Upgrade de realismo (teste técnico, sem depender do Lindson):** o mesmo trilho A renderizado no **Blender Cycles** (headless, `bpy`). A luz por path tracing aproxima as refs 01 e 02. Comparar com o Three.js lado a lado na cena "flat lay Barzakh" e ficar com o melhor.

---

## 3. A lista completa

### a) Formatos de apresentação (o objetivo de cada um)
| # | Formato | Objetivo | Ref / molde | Trilho | Canais |
|---|---|---|---|---|---|
| F1 | **Flat lay de papelaria e merch** (15–20 objetos de cima) | provar que a marca vira **sistema**, não um logo solto | ref-01, ref-03 | A | feed (capa de carrossel), Behance (módulo hero), Pinterest |
| F2 | **Linha de embalagem** em degraus | mostrar a marca **no produto que o cliente final pega** | ref-02, ref-04 | A (+C no herói) | feed, Behance, Pinterest (pin mais salvo do nicho) |
| F3 | **Brand board** (logo + versões + paleta hex + 4 janelas) | resumir a identidade em **1 tela** | ref-05 | prancha + A | capa de carrossel, capa do Behance, pin |
| F4 | **Antes e depois** (logo antigo × novo, perfil antigo × novo) | a transformação em 1 segundo | split screen (#173) | gráfico, print real | carrossel, Reel, Behance (módulo 02) |
| F5 | **Processo do logo** (rabisco → grade de construção → final) | provar **método** (não é "desenho") | Barzakh 02-construção | B no rabisco + vetor | carrossel, Reel, Behance |
| F6 | **Paleta e tipografia** (proporção 60/25/15, Aa gigante) | ensinar o "porquê" (Hormozi: dar o quê e o porquê) | Barzakh 05/06 | gráfico | carrossel dica, pin |
| F7 | **Aplicação em fachada, uniforme, veículo e site** | a marca **na rua** e no celular | outdoor/fachada v2 | A (fachada, uniforme, veículo), tela real do site | feed, Behance (10–12) |
| F8 | **Carrossel de case** (8–10 telas) | o case completo no Instagram | estrutura 3c | A + gráfico | feed (L1) |
| F9 | **Reel de processo** | bastidor que segura atenção | rabisco → vetor → mockup girando | tela gravada + A | Reels, Shorts, pin vídeo |
| F10 | **Reel de revelação** (logo montando + 6 aplicações no ritmo) | o "uau", que puxa compartilhamento | #41, #166, #169 | A animado | Reels (fixado), Behance (GIF) |
| F11 | **Bastidor** (mesa, mãos, impressão, prova de cor) | humanizar **sem rosto** | ref-03 | B (mãos, sem rosto) | stories, destaque Bastidor |
| F12 | **Prova social** (print real de mensagem ou avaliação, com autorização) | confiança | print real | real | destaque Cases, carrossel |
| F13 | **Oferta e pacotes** (Limiar, Travessia, Horizonte, o que inclui, sem preço) | venda | brand board da Barzakh | gráfico + A | destaque Pacotes, post CTA, stories |
| F14 | **Manchete de opinião** (dor do dono) com objeto gigante no lugar do rosto | alcance e comentário | feed v3 sem rosto: 02, 06, 07, 09 | A ou B | feed (L2) |

### b) Por cliente: o que dá para mostrar e o que falta
Legenda: ✅ pode · ⚠️ pode com condição · ⛔ não entra como case de branding

| Cliente | Situação | O que mostrar | O que falta | Autorização |
|---|---|---|---|---|
| **Barzakh** (própria) | ✅ placa, book v2 e manual v2 aprovados (16/11) | tudo: placa, construção, hot stamping, papelaria, flat lay preto e ouro (ref-03), brand board, Reel do monolito | flat lay F1 em render A, Reel de revelação novo, Behance sem rosto | não precisa |
| **Al Kántara Group** (holding) | ✅ v2 aprovada, "isso sim é premium" (16/11) | brand book de 27 p., manual de 31 p., K de pedra-chave, 4 divisões, cenas Gemini aprovadas | case no Behance (não existe ainda), flat lay das 4 divisões | não precisa |
| **Orégano Turbo** (própria) | ✅ identidade v4 em uso, Reels aprovados (15/11), mascote (15/11) | linha de embalagem de pizzaria (caixa, sacola, copo, adesivo PEDIDO SAINDO), 5 fotos de campanha Gemini HD, mascote | confirmar a versão vigente (v4 + mascote); renders A da linha delivery (ref-04) | não precisa |
| **Dublê** (produto do grupo) | ✅ identidade aprovada (03/11, régua premium) | app, cartões, tela Sermo, embalagem | case v3 já existe: trocar crédito para Barzakh | não precisa |
| **Real Time** (pagante) | ✅ rebranding em uso; feed v2/v6 aprovado e postado; manual com antes × depois | **antes × depois do logo**, manual, fachada, outdoor, papelaria, fotos reais de equipamento (Drive) | autorização por escrito; render F1 escuro | ⚠️ precisa |
| **Curso Processo Legislativo** (Tribuna/Thiago e Rafael) | ✅ identidade publicada; antes e depois aprovado (12/11) | antes × depois do perfil, sistema verde e dourado com §, capa do livro, destaques | autorização dos dois professores; os rostos deles não entram (foco na marca) | ⚠️ precisa |
| **WF Celulares** (pagante) | ✅ caminho B aprovado (10/11) | logo B, universo escuro e titânio, sacola, caixa, cartão, painel fixado | autorização; **nunca fundo claro**; fotos Apple são de imprensa (não usar como nossas) | ⚠️ precisa |
| **Dra. Jaci Cunha** (pagante) | ⚠️ identidade v2 (bordô e dourado); site v2 e prova social v1 reprovados | só a marca: papelaria, receituário, cartão, fachada (A) | autorização; **sem antes e depois de paciente, sem promessa, CRO-MA 8514** em tudo que citar o serviço | ⚠️ precisa |
| **Leo Pinto** | ⚠️ identidade antiga reprovada (18/11); identidade v2 aprovada, menos as redes | só o sistema v2 (logo, sol no O, azul e laranja, manual) | autorização; **nunca abre a vitrine**, nada de campanha nem crítica (situação); nada de grafismo | ⚠️ precisa, por último |
| **Mova Street** | ⚠️ logo é **do dono** ("não mude a logo"); branding v2 aguardando | só depois de aprovado: sistema de aplicação (adesivo, tela) com crédito honesto "sistema de marca", **nunca "criamos o logo"** | aprovação do Paulo + autorização | ⚠️ |
| **Pagode Fiado** | ⚠️ brand book premium (12/11); notícias v1 e longos v1 reprovados | o brand book, se o Lindson confirmar que foi aprovado | confirmar a aprovação + autorização | ⚠️ |
| **Desentupidora SF** | ⛔ como branding: a identidade vem do site; não criamos o logo; criativos v1 reprovados | entra só como **site e social** (mini site) | — | — |
| **Tribuna 98** | ⛔ como branding: o logo é dele; político | capas aprovadas só como "direção de arte" e só com autorização; fora do feed da Barzakh | — | — |
| **Rafael Imports** | ⛔ como branding: só mini site | entra só como **site** (categoria web) | — | — |

**Reprovado que nunca aparece:** identidade antiga do Leo (v1, v2, v3, v13), Al Kántara v1, Orégano v1 cartum e branches do Claude do Google, WF v1 verde-limão, Mova v1 com logo redesenhado, Jaci site v2 e prova social v1, Projeto Designer v1, Pinterest v1, feed Barzakh v1 e v2.

### c) Por canal

**Instagram @barzakhstudio**
- **Grid 3:4 (1080×1440)**, texto longe das bordas (regra de 19/11). Xadrez: **escuro Barzakh (preto e ouro) ↔ cor do case** em linhas e colunas; nunca 2 composições iguais seguidas; vídeo intercalado com estático.
- **Primeiros 9 posts** (ordem de postagem; no perfil o 1 fica embaixo à direita):

| # | Peça | Formato | Cor | Linha |
|---|---|---|---|---|
| 1 | **BARZAKH · a passagem da sua marca**: placa aprovada + flat lay preto e ouro (ref-03) | estático F1 | escuro | L5 manifesto |
| 2 | **Revelação Orégano Turbo**: logo monta → caixa, sacola, copo, adesivo | Reel F10 | verde | L1 case |
| 3 | **Brand board Real Time** (ref-05) → carrossel do case com antes × depois | carrossel F3+F8 | escuro e azul | L1 |
| 4 | **"SUA MARCA PARECE MENOR?"**, manchete gigante sobre cartão amassado × cartão Barzakh | estático F14 | ouro claro | L2 dor |
| 5 | **Processo do logo Barzakh**: rabisco → grade → monolito | Reel F9 | escuro | L3 processo |
| 6 | **Linha de embalagem Dublê** em degraus (ref-02) | estático F2 | violeta | L1 |
| 7 | **"60/25/15: cor tem proporção"** (dica) | carrossel F6 | creme ou marfim | L4 dica |
| 8 | **Antes × depois Curso Legislativo** (se autorizado; senão, Al Kántara flat lay das 4 divisões) | Reel F4 | verde e ouro | L1 |
| 9 | **Travessia: o que vem no pacote** (brand board da Barzakh, sem preço) | carrossel F13 | escuro | L6 oferta |

  A grade fica com escuro, verde, azul / ouro, escuro, violeta / creme, verde, escuro: nenhuma cor repete na vizinhança.
- **Reels:** revelação (1 por case), processo, "do rabisco à rua", antes × depois. Sempre com **voz** (Antonio +4% ou gravação de voz do Lindson, sem rosto), SFX nos cortes, VFX (grão, light leak), trilha com crédito. Legenda queimada, nunca sobre o logo.
- **Destaques (6):** Cases · Processo · Pacotes · Bastidor (mãos e mesa, **sem rosto**) · Dúvidas · Contato. Capas = arco e monolito com o glow da cor do case (já feitos).
- **Bio:** "A passagem da sua marca. / Identidade visual, embalagem e site · um estúdio Al Kántara / São Luís · atende todo o Brasil / ↓ Fale com o estúdio". Sem preço; o crédito "Direção: Lindson Almeida" fica opcional, só em texto.

**Behance behance.net/barzakhstudio**
- Estrutura de cada case (Wheeler): **capa 1616×1264** (brand board ou herói A, sem texto de anúncio) → 01 herói (aplicação mais forte) → 02 desafio e conceito (1 frase; antes × depois quando houver) → 03 construção do logo (grade) → 04 versões → 05 paleta com proporção → 06 tipografia → 07 **flat lay F1** → 08 **linha de embalagem F2** → 09 celular e Instagram → 10 detalhe (close de hot stamping, costura, papel) → 11 fachada, uniforme e veículo → 12 GIF do logo montando → 13 créditos ("Barzakh · um estúdio Al Kántara · Direção criativa: Lindson Almeida · render 3D / imagem gerada por IA onde houver").
- **Ordem da vitrine:** 1 Barzakh · 2 Al Kántara Group · 3 Real Time* · 4 Orégano Turbo · 5 Dublê · 6 Curso Legislativo* · 7 WF Celulares* · 8 Jaci* · 9 Leo* (por último). Publicar no sentido inverso. (* com autorização)

**Pinterest**
- **Pastas:** Identidade visual premium · Mockup de papelaria e merch (F1) · Embalagem de marca (F2) · Brand board e paleta de cores (F3, F6) · Antes e depois de logo (F4) · Processo de criação de logo (F5) · Identidade visual por nicho (pizzaria, produtora, curso, loja de celular, clínica, app) · Brand book e manual de marca.
- **Tipos de pin:** estático 2:3 (1000×1500) com mockup em tela cheia e legenda pequena (serifa + mono + monolito), sem chamada · carrossel de 2 a 5 imagens por case · pin de vídeo de 6 a 15 s (Reel de revelação, com áudio) · pin "brand board" (o mais salvo do nicho, ref-05).
- Mantém o Pinterest v3 por cliente; os pins novos de F1, F2 e F3 entram por cima. Pin com imagem de IA leva "imagem gerada por IA" na descrição.

### d) Plano de produção priorizado (o que impressiona primeiro)
1. **Hoje, sem depender de ninguém:** ampliar o gerador 3D (trilho A) com 12 objetos: ecobag, camiseta dobrada, boné, copo térmico, caneca, avental, caderno espiral, crachá com cordão, tag, papel de seda com padrão, caixa de presente, pouch de café. Testar Blender Cycles × Three.js na cena "flat lay Barzakh preto e ouro".
2. **Primeiras 4 cenas (as 5 mais fortes):** flat lay Barzakh (ref-03) · brand board Real Time (ref-05) · linha delivery Orégano (ref-04) · flat lay Al Kántara 4 divisões (ref-01). Conferência com zoom (8 critérios + sobreposição do logo).
3. **Lindson gera no Gemini** os prompts B01 a B06 de `prompts-mockups/PROMPTS.md` (fundos e mãos, sem logo) e, se aprovar o teste, os C01 a C03 (com o logo anexado).
4. **Refazer sem rosto** os itens da seção 5 (banner, thumbs e feed v3).
5. **Montar os 9 primeiros posts** + 3 capas de Reel + legendas SEO (Copy squad) → prévia do grid 3:4 → aprovação.
6. **Behance:** cases Barzakh e Al Kántara primeiro (não precisam de autorização), depois os autorizados.
7. **Pinterest:** 3 pins por dia dos renders novos (F1, F2, F3), em rodízio de pastas.
8. Reels de revelação (1 por case, por semana).

### e) Checklist de qualidade de case de branding (conferir em toda peça, com zoom)
1. **Consistência:** a mesma luz (direção, temperatura e sombra) em todas as imagens de um case; a mesma paleta oficial (hex do manual) e o mesmo chão ou fundo por série.
2. **Logo nunca distorcido:** é o arquivo oficial (SVG ou PNG transparente), sem esticar, girar fora do plano, trocar a cor fora das versões do manual nem redesenhar. Em fundo escuro, a versão negativa. **Sobreposição com o SVG a 100%** em toda imagem do trilho C.
3. **Área de proteção** e tamanho mínimo do manual respeitados em cada objeto.
4. **Escala real:** cartão de 9×5, caneca de 9 cm, boné e sacola coerentes entre si (critério 3 da IA).
5. **Resolução:** imagem final ≥ 2/3 da largura de saída; ampliação máxima de 1,5×; Behance a 2800 px, feed a 2160×2880, pin a 2000×3000.
6. **Nada de texto falso:** nenhum texto inventado, lorem ipsum legível, QR falso, telefone falso nem marca de terceiros. Texto de embalagem só o real do cliente ou faixa lisa.
7. **Crédito:** "Barzakh · um estúdio Al Kántara"; foto de banco com autor; **"imagem gerada por IA"** ou **"render 3D"** quando for o caso; nunca apresentar render como foto de cliente.
8. **Autorização do cliente** registrada antes de publicar (seção 3b).
9. **Regras do cliente:** Jaci (CFO e CRO, sem antes e depois), Leo (situação, sem grafismo), WF (sem fundo claro), Mova (logo do dono), preço sempre "a partir de" e só fora da bio.
10. **Sem rosto do Lindson** (20/11).
11. **Cara de case, não de colagem:** 1 ideia por imagem, respiro igual entre os objetos, nada de pílula, card de UI ou glow espalhado (18/11).
12. **Mensagem de 1 segundo:** dá para entender qual é a marca e o que ela vende só de bater o olho.

---

## 4. Conferência deste documento
- Diretrizes lidas: REGRAS-GERAIS, CLAUDE.md (2 repositórios), padrão de exigência, conferência IA, MEMORIA (Barzakh 16 a 18/11 e clientes), BARZAKH-ESTADO, estratégias de Instagram, Behance, Pinterest e YouTube, kit-contas, feed v3, Projeto Designer v2 e v3, kit Gemini da Orégano, prompts v3 e v4 da Al Kántara, log `gemini|mockup` de todos os branches.
- Pendente (dito, não escondido): as cenas ainda não foram renderizadas nem conferidas; as autorizações dos pagantes não existem no repositório; a versão vigente da Orégano (v4 + mascote) e a aprovação do brand book do Pagode Fiado precisam de confirmação.

## 5. Peças já feitas com o rosto do Lindson: REFAZER (decisão de 20/11)
| Peça | Onde | O que trocar |
|---|---|---|
| Banner do YouTube | `kit-contas/02-youtube/banner-2560x1440.jpg` e `youtube/pecas/banner.jpg` | placa + flat lay preto e ouro; "A PASSAGEM DA SUA MARCA"; sem "com o fundador" |
| Thumbs 01, 02 e 03 do YouTube | `kit-contas/02-youtube/thumb-0{1,2,3}.jpg` e `youtube/pecas/thumb-0*.jpg` | objeto ou mockup gigante no lugar do rosto (logo "barato" × marca Barzakh; arco; grade) |
| Feed v3 · posts 01, 03, 05, 08, 11, 12 | `marca-lindson/projeto-designer/v3/feed-v3/posts/` | manchete gigante + objeto ou render (F14); mantém as cores e a energia |
| Feed v3 · capas c1/1 e c1/5, c2/1 e c2/5 | `feed-v3/carrosseis/` | mesmo tratamento |
| Estratégia do YouTube | `youtube/ESTRATEGIA.md` ("canal de autoridade com o rosto do Lindson", regras de thumb, gravação de rosto) | canal de **processo e cases**: tela, mãos, mockup e voz |
| Estratégia do Instagram | `instagram/ESTRATEGIA.md` (L2 "foto do Lindson", "o rosto do diretor criativo", grade "foto do Lindson grande") | trocar por objeto ou render; destaque Bastidor só com mãos |
| Manual Barzakh p. 05 (endosso) | `projeto-designer/v3/marca/gerador/manual.py` ("O Lindson continua o rosto") | "Direção criativa: Lindson Almeida" só em crédito de texto |
| Grade de prévia | `feed-v3/grade.jpg`, `instagram/previa.jpg`, `youtube/previa.jpg` | gerar de novo depois das trocas |

Não têm rosto e ficam: avatar, destaques, banner do Behance, capas de Behance, pins, capas de Reel do feed v3 e a placa.

## 6. O que o Lindson decide ou manda
1. **Trilho C** (Gemini com o logo anexado, aprovado só se a sobreposição com o SVG bater): sim ou não. Sem ele, tudo com logo sai em render 3D (trilho A).
2. **Autorização** para mostrar a marca de Real Time, Curso Legislativo, WF, Jaci e Leo (uma mensagem por cliente; modelo em `prompts-mockups/README.md`).
3. **Gerar no Gemini** os prompts B01 a B06 (e C01 a C03, se aprovar o trilho C) e mandar um por mensagem.
4. Confirmar a versão vigente da Orégano (v4 + mascote) e se o brand book do Pagode Fiado foi aprovado.
5. Se algum cliente imprimiu cartão, sacola ou fachada: **foto real** dessa peça vale mais que qualquer render.
