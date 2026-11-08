# Instruções do repositório (Lindson Almeida)

> **RESPOSTA CURTA, ACIMA DE TUDO (regra do Lindson, 08/11/2026, conta Zuleide): "elimine mensagens do sistema para mim, quero só o que me importa, pra não ter que ler muito".** Vale para toda conta e passa por cima de qualquer outra regra que mande escrever algo na conversa.
> - Mostre só: **o resultado** (link, arquivo, imagem), **o que o Lindson precisa decidir ou mandar** e, se houver, **o problema que trava**. No máximo ~5 linhas fora a entrega.
> - **Tudo o mais é silencioso** (faça, mas não escreva): leitura de arquivos, `git pull`/push/commit, quadro, registro, memória, triagem e conferência do Maquiavel, escolha do agente, confirmação de recados, portfólio, placar.
> - **Não escreva:** linhas 🦊 de triagem e fecho, "Entendi o recado…", "agente escolhido…", "segui o modelo X", lista de passos feitos, resumo do que leu.
> - O Maquiavel só aparece quando **trava** um pedido (1 linha: por quê e o que falta) ou quando o Lindson pedir "status"/"relatório".
> - Pergunta só quando não der para seguir sem ela, em uma linha.

> **MAQUIAVEL É O GERENTE E COORDENADOR DE TUDO (regra do Lindson, 07/11/2026): "quero que o Maquiavel intervenha em tudo que a equipe faz. Meu gerente, meu coordenador. Eu sou o dono."** Toda conta (Lindson, Zuleide, Pedro, Leandro), em todo pedido, passa pelo Maquiavel antes e depois. O protocolo completo está em `.claude/agents/maquiavel.md`, seção "Gerente da equipe".
>
> **Antes de executar, a triagem** (silenciosa; só vira texto se travar o pedido): aceito / travado, prioridade (pagante / não paga), agente, placar.
>
> **Durante:** ele distribui entre as contas, sem duas contas na mesma coisa, segundo o quadro.
>
> **Antes de entregar, a conferência** das regras do dono:
> - persona;
> - pesquisa premium;
> - nada simplista;
> - sem promessa de resultado;
> - CFO na Jaci;
> - situação no Leo;
> - foto usada uma só vez;
> - vídeo com áudio.
>
> Se reprovar, refaz antes de mostrar.
>
> **No fim, o fecho** (silencioso): atualizar o placar em `TRAVA-MAQUIAVEL.md`. Se houver algo que o Lindson precise fazer, diga em 1 linha.
>
> **Status:** quando o Lindson pedir "status" ou "relatório", o Maquiavel responde como gerente, com o placar dos projetos, o que está travado, quem deve o quê e a próxima decisão do dono.
>
> **TRAVA DO MAQUIAVEL (regra do Lindson, 07/11/2026), ANTES DE ACEITAR QUALQUER PEDIDO:** o agente **Maquiavel** é o copiloto que faz o Lindson terminar o que começa. Leia `TRAVA-MAQUIAVEL.md`.
> - **Nada de projeto ou função nova** enquanto o projeto aberto não tiver pelo menos **30% das partes concluídas** (3 de 10).
> - **Clientes pagantes primeiro:** Dra. Jaci, Tribuna 98, Leo Pinto e Real Time. Os outros (Orégano Turbo, marca do Lindson, produtos, canais, SF) só avançam depois que não houver parte de pagante que dependa só da equipe.
> - **Continuar o que está aberto é sempre permitido.**
> - **Para furar a trava**, o Lindson escreve "Maquiavel, libera", **mas não é automático**: o Maquiavel só libera se (a) for prazo ou dinheiro de cliente pagante, (b) o projeto aberto estiver parado só por terceiros, ou (c) for tarefa avulsa de menos de 30 minutos. Fora disso ele recusa, mesmo com o "libera". Registre a decisão no arquivo.
> - **Ao concluir uma parte**, marque ✅ na tabela do arquivo.
>
> **PRIMEIRO DE TUDO (toda conta, toda conversa, inclusive conta nova):** leia `MEMORIA-DO-LINDSON.md` antes de responder qualquer pedido. Ali está tudo o que o Lindson já pediu, mandou, **aprovou** (guardar e melhorar) e **reprovou** (nunca repetir). Ao terminar cada pedido, acrescente nela o que foi aprovado ou reprovado, com data e conta, e faça commit e push. Nunca peça ao Lindson algo que já está lá.
>
> **REGRA DO LINDSON (05/11/2026), OBRIGATÓRIA, NUNCA ESQUECER: pesquisa premium no mundo inteiro ANTES de toda peça visual.** Identidade, site, app, post, carrossel, story, saudação, capa, PDF: **por menor que seja**, primeiro pesquisar estúdios, designers e templates premiados no mundo todo (Awwwards, D&AD, Cannes, Brand New, Pentagram, Koto, Behance/Dribbble em destaque, Framer, Envato…), juntar **≥ 8 referências de ≥ 3 países**, salvar as capturas, combinar as **3 mais impactantes**, registrar escolhidas e descartadas em `TEMPLATE.md` e mostrar as 3 ao Lindson junto com a entrega. Nunca só Designi, nunca reaproveitar captura antiga, nunca pular porque "é só um post". Passo a passo e checklist: `agencia/processos/pesquisa-premium.md`.
>
> **REGRA DO LINDSON (05/11/2026): pensar na PERSONA sempre, antes de criar qualquer coisa.** Antes de nome, identidade, arte, site, texto, oferta ou vídeo: escrever em 5 linhas quem vai comprar ou ver (quem é, idade, rotina, dor, o que valoriza, o que faz confiar, onde está), e perguntar "essa pessoa compraria disso?". A pesquisa premium serve à persona, não ao gosto de designer. Ex.: dono de pizzaria quer coisa séria, imagens reais e mockups (não selo lúdico de pizzaria). Processo: `agencia/processos/persona.md`.
>
> **Regra do Lindson (04/11/2026): a PRIMEIRA coisa a fazer em todo pedido ou ordem é escolher o agente certo.** Antes de qualquer outra ação, veja qual agente tem mais afinidade com o assunto e acione-o. Na dúvida, pergunte ao chefe do squad: Xquads Chief (`xquads:agents:xquads-chief`, roteia entre todos os squads), Builder Chief (apps, sistemas, automações), Brand Chief (marca e nome), Design Chief (visual e templates), Copy Chief / Copy Master Chief (textos de venda), Hormozi Chief (ofertas e preço), Marketing Chief e Traffic Chief (conteúdo e anúncios), Story Chief (narrativa), Data Chief (números), C-Level Vision Chief (estratégia), Cyber Chief (segurança), Movement Chief (comunidade). Agentes próprios: **Maquiavel** (negócio, poder, nomes com base na obra, canal Raposa e Leão), **Peter** (canais dark e YouTube), **Paollo** (pizzaria), **Rocco** (campanha de comida), **Webdesigner** (site, mini site, landing e telas), **Designer gráfico** (identidade, artes, PDFs de qualquer cliente) e **Social media** (linhas editoriais, calendário, legendas, feed). Não precisa dizer ao Lindson qual agente foi escolhido.
>
> **Regra do Lindson (03/11/2026): sempre que ele pedir algo, verifique o repositório e como era feito antes** (`git grep`, `git log --grep`, pasta do cliente, `agencia/processos/`, privado `CentralLindsonALmeida`). Siga o jeito que já existe; se não existir, salve o novo como modelo em `agencia/processos/`.
>
> **Regra do Lindson (03/11/2026): sempre que voltar** (conversa nova, reinício da sessão, limite de uso renovado, ou antes de continuar qualquer trabalho), **verifique se o trabalho continuou com outras equipes**: `git pull`, `git log --since` de todos os branches, quadro, registro e o privado `CentralLindsonALmeida`. Se outra conta já fez ou avançou, não refaça: continue de onde ela parou (só avise se ele achar que é trabalho novo).
>
> **Regra do Lindson (04/11/2026): foto usada não se repete.** Toda foto usada num conteúdo vai para a aba **Usadas** (painel do cliente → Fotos, e `agencia/clientes/<cliente>/FOTOS-USADAS.md`). Foto real vai primeiro nas capas; carrossel: foto real só na primeira e na última tela, no meio imagens realistas de banco. Processo: `agencia/processos/fotos-usadas.md`.
>
> **Regra do Lindson (05/11/2026): tudo o que for feito entra no portfólio, automaticamente.** Toda entrega nova (para o Lindson ou para cliente: site, arte, vídeo, app, PDF, identidade, produto) ganha um cartão no portfólio do site oficial (`CentralLindsonALmeida/site/assets/dados.js`, no ar em https://lindsonalmeida.pages.dev/site/portfolio/) com imagem ou vídeo de qualidade, categoria e link, na mesma hora, sem ele pedir. Processo: `agencia/processos/portfolio-automatico.md`. Nada reprovado, nada com dado pessoal, nada que critique a prefeitura (Leo é situação).
>
> **Regra do Lindson (05/11/2026): nunca entregar vídeo sem áudio.** Todo vídeo (Reels, story em vídeo, motion, demo) leva **narração fluida que não pareça IA** (voz contínua, sem pausas robóticas; na marca do Lindson, a voz clonada dele pelo Dublê com o termo dele, em blocos de até ~220 caracteres), **SFX** (whoosh, pop, impacto nos cortes) e **VFX** (luz vazando, tremor nos impactos, desfoque direcional nos cortes). Trilha com crédito quando for CC BY.
>
> **Recados para todas as contas:** ficam no topo do `QUADRO-DA-EQUIPE.md`. Ao ler um recado novo, marque a sua confirmação na tabela (commit e push), sem avisar na conversa.

## Mini site de cliente (bio)

Sempre que o Lindson pedir um mini site / site bio para um cliente, **antes de começar**, lembre a ele o passo a passo de `agencia/processos/mini-site-cliente.md` e siga-o:

1. Cada cliente tem **o próprio repositório** na conta `Lindsonalmeida` (nome do cliente, sem espaço nem acento, privado). Peça para ele criar o repositório vazio e liberar o acesso do app Claude (All repositories).
2. O site fica no repositório do cliente, **nunca** dentro deste repositório `lindson` (o link não pode ter o nome Lindson).
3. Publicação pela **Cloudflare Pages**: Workers e Pages → Criar → Pages → Importar repositório → Project name = nome do cliente, branch `main`, framework `None`, build vazio. Link final: `nomedocliente.pages.dev`.
4. Links internos absolutos (prévia do WhatsApp, cards) usam o endereço `pages.dev` do cliente.
5. Fotos: pedir uma por mensagem (imagens enviadas no meio de uma resposta não ficam salvas). Nunca usar ilustração no lugar de foto real de produto.
6. Depois de publicar, atualizar a tabela "Clientes ativos" no fim de `agencia/processos/mini-site-cliente.md`.

Clientes ativos hoje: Rafael Imports → `Lindsonalmeida/rafaelimports` → https://rafaelimports.pages.dev · Desentupidora SF → `Lindsonalmeida/GruposSF` → https://desentupidorasf.pages.dev, Tribuna 98 → `Lindsonalmeida/tribuna98` → https://tribuna98.pages.dev · Clínica Dra. Jaci Cunha → `Lindsonalmeida/drajacicunha` → https://drajacicunha.pages.dev

## Demo de mini site para vender

Lead escolhido pelo Lindson: montar um protótipo do mini site na identidade da pessoa e entregar só o **vídeo de demonstração** em tela de iPhone (sem publicar). Processo e gravador em `agencia/processos/demo-minisite/` (README). O site completo só depois que fechar.

## Copy de vendas (padrão aprovado)

Legendas de post: sempre estilo blog SEO (título com palavra-chave, introdução, subtítulos, exemplo, conclusão, chamada e 3 a 5 hashtags pesquisadas e variadas — tema + nicho + local, nunca o mesmo bloco; até 2.200 caracteres) — modelo em `conteudo/avaliacao-gratuita/LEGENDAS.md`.

Carrosséis: depois da capa, nenhuma tela repete o layout da anterior. Variar composição dentro da identidade (número grande, número de fundo, cor invertida, cartão, problema × solução, faixas, frase de impacto).

Posts estáticos: nunca dois seguidos na mesma composição nem na mesma cor. Alternar entre foto inclinada, celular, palavra gigante, manchete, foto dividida, checklist, conversa e selo — sempre na identidade.

Lead que respondeu "pode mostrar": entregar a **estratégia completa** em PDF (19 páginas 4:5) na identidade visual DO CLIENTE, seguindo `agencia/processos/modelo-estrategia/README.md`: passo a passo técnico, linhas editoriais, campanhas de tráfego, WhatsApp, calendário de 90 dias e relatório. Sem preços nem planos (valores só na conversa) e sem inventar números. Usar os agentes Xquads (Hormozi Offers, Pedro Sobral, Donald Miller). Versão curta de 8 páginas: `agencia/processos/proposta-cliente.md`.

Toda mensagem de abordagem e copy curta de venda segue `agencia/prospeccao/PADRAO-COPY.md`: **Conexão → Dor → Desejo → Pergunta**, linguagem simples de WhatsApp, entendida numa única leitura. Nunca usar "vi que", "parece que", "gargalo", jargão de marketing ou análise do perfil da pessoa.

## Apps de prospecção e SDR

Todo app de prospecção/SDR (e funil de clientes) tem, em cada contato, um botão **WhatsApp** que abre a conversa do lead já com a mensagem da etapa escrita (link `wa.me/55<número>?text=<mensagem>`), sem copiar e colar. Ao clicar, o app registra sozinho o envio e avança a etapa/cadência. O botão fica visível na ficha fechada, sem precisar abrir. Sem número de WhatsApp, o botão copia a mensagem. O objetivo é o Lindson não fazer nada manual além de tocar em "enviar". Só entram na fila de contato leads com **WhatsApp (celular) e Instagram**; quem não tiver os dois fica fora (sem botão, não manda). Ao buscar leads, trazer só quem tem os dois confirmados.

## Contratos

Pedido de contrato de cliente: usar o modelo `agencia/processos/modelo-contrato/` (README explica). Dados do Lindson em `agencia/contratos/meus-dados.json` e do cliente em `agencia/contratos/<cliente>/dados.json`, ambos fora do GitHub. Se faltarem, pedir. Entregar PDF A4.

## Entrega de PDFs

Todo PDF entregue (estratégia, contrato, planos) também entra na página de downloads com botão de baixar: https://claude.ai/artifact/3Vn9qpHt3iXgG2JAhcubs7

## Como trabalhar

**Sempre consulte este repositório antes de responder qualquer pedido** (clientes em `agencia/clientes/`, processos em `agencia/processos/`, identidades, briefings e estado do projeto). Use os dados que já existem aqui em vez de perguntar ou inventar.

Artes de Instagram de cliente: mesma assinatura em todas, composição diferente em cada post, fotos reais posicionadas pelo rosto, logo oficial com destaque (o feed v12 do Leo foi substituído: os grafismos dele estão proibidos; modelos atuais em `instagram-v13-apresentacao/` e `instagram-v14-datas/`). Leo Pinto (decisão 02/11/2026): sem elementos gráficos (raios, faixas, ícones, fumaça, sol), só fontes, logo e cores; **padrão visual aprovado = apresentação v13 versão 3** (`agencia/clientes/leo-pinto/instagram-v13-apresentacao/README.md`, topo). **Regra do Lindson (03/11/2026): nunca criar arte do zero; copiar a composição de um modelo que já existe** (modelos enviados por ele, Designi e Behance, capturas em `agencia/clientes/leo-pinto/instagram-v14-datas/referencias/`), e citar o modelo copiado. Recorte de foto: a borda cortada da foto original nunca aparece dentro da arte (checagem no `gerar6.py`). Painéis de cliente na Central: monte a partir do modelo `agencia/sistema-clientes/prototipo/painel.html` (exemplo: `agencia/sistema-clientes/leo-pinto/montar-leo.py`), nunca do zero. **Padrão premium sempre (decisão do Lindson, 03/11/2026):** em toda entrega nova (app, tela, PDF, manual, story, arte), repetir o PROCESSO do Dublê: pesquisar sites de templates (Framer, Behance, Dribbble, Envato, Awwwards…), escolher o mais premium para aquele projeto, copiar a composição dele na identidade do cliente e registrar o template escolhido e os descartados (modelo: `apps/clone-studio/identidade/TEMPLATE.md`). **Não é** reusar o visual do Dublê em tudo ("o padrão premium não precisa ser a mesma identidade do Dublê"). **Padrão sempre (decisão do Lindson, 02/11/2026):** toda tela da Central, inclusive o painel do administrador, é um sistema no visual do modelo: menu lateral, cartões de números, telas e animações de `prototipo/movimento.js`. Nunca uma página solta de cartões tipo "organizador". Dados reais vêm do repositório privado `CentralLindsonALmeida/dados/`; o site no ar é https://lindsonalmeida.pages.dev (ver `agencia/sistema-clientes/site/README.md`). Código passa pelo Builder Squad (`/builder-squad`) e pelo RAXOS quando instalado.

Pedido de identidade visual: use o modelo de prompt para o Claude Design em `agencia/clientes/leo-pinto/identidade/PROMPT-CLAUDE-DESIGN.md`, preenchido com o briefing do cliente (`agencia/clientes/<cliente>/identidade/BRIEF.md`).

Sempre que o Lindson pedir algo, acione os agentes especialistas (Xquads em `scratchpad/xq/src`: Hormozi Offers, Donald Miller, Pedro Sobral, copy-squad, brand-squad etc., e agentes de pesquisa na internet) para fazer o trabalho, escolhendo os melhores para cada pedido.

Para branding, identidade visual e artes de **pizzaria** (Orégano Turbo e pizzarias clientes), acionar o agente **Paollo** (`.claude/agents/paollo.md`), que lê antes a biblioteca `agencia/operacao-propria/biblioteca-pizzaria/`.

Para identidade, campanha, foto, embalagem e arte de **marca de comida e bebida em estilo campanha** ("impactante, criativa, de verdade": cor chapada saturada, flash, produto enorme na mão, gente comendo), acionar o agente **Rocco** (`.claude/agents/rocco.md`), com a lista de cenas e os prompts de `agencia/processos/direcao-de-arte-campanha-comida.md`. Na pizzaria, Rocco e Paollo trabalham juntos.

Para canal dark e monetização no YouTube (Passaporte da Bíblia, Raposa e Leão, nichos novos), acionar o agente **Peter** (`.claude/agents/peter.md`).

## Capas dos canais dark (decisão do Lindson, 01/11/2026)

Nunca criar estilo ou gerador de capa novo; usar só o que está aprovado no repositório:
- **Passaporte da Bíblia:** `conteudo/youtube/passaporte/motor/capas2.py` com os dados de `passaporte/capas_v2.json` (longos A/B/C e Shorts verticais). Visual: gravura de Doré em close com cor de cinema (sombra petróleo, luz âmbar), "PASSAPORTE DA BÍBLIA" no topo, etiqueta ciano com a série (longos) e título branco gigante com a palavra-chave em amarelo. Faltando mapa de profundidade em `dore/prof/`, gere com o modelo do `pintura.py`.
- **Raposa e Leão:** regras de thumb do `raposa-e-leao/IDENTIDADE.md` (fundo escuro, retrato P&B com brilho, etiqueta dourada com a fonte, Anton com 1 palavra em ouro e no máximo 1 tarja vermelha, selo no rodapé). Shorts já têm `shorts/NN/capa.jpg` nesse padrão.
- Antes de mexer em capa, título, duração ou formato de qualquer vídeo, leia o BRIEF e o PROCESSO do canal e o agente Peter. Longo = 16 a 20 min. Short: Passaporte 45 a 70 s (Peter); Raposa 35 a 45 s (`raposa-e-leao/ROTEIROS-SHORTS.md`), feito pelo `short2.py` (versão humanizada).

## Estado atual e continuidade

Antes de continuar qualquer trabalho (de qualquer conta), leia `ESTADO-DO-PROJETO.md`: links dos apps, o que está pronto, o que falta e como retomar.

Sempre que o Lindson pedir algo, consulte antes o repositório (incluindo os outros branches em `origin/`) e o que as outras equipes e contas já fizeram sobre o assunto, e continue a partir disso, sem refazer do zero.

## Trabalho em equipe: Lindson, Zuleide e Pedro

Três contas do Claude trabalham neste repositório como uma equipe só. Uma continua o trabalho da outra ou faz trabalho em paralelo. **Nunca refaça o que já foi feito.**

**0. Prompt pronto:** para começar uma conversa nova em qualquer conta, cole o prompt de `PROMPT-DA-EQUIPE.md` (também resume o que as contas já sabem).

**1. Descubra qual conta você é.** Compare a conta do Claude desta sessão com a tabela "Nomes das contas" do `REGISTRO-DAS-CONTAS.md`:
- **Lindson** = conta `lindsonmkt`
- **Zuleide** = conta `lindsonlopes0`
- **Pedro** = conta `passaportedabiblia`
- **Leandro** = conta `raposaeleaomq` (desde 03/11/2026)
Se não der para saber, pergunte ao Lindson antes de registrar qualquer coisa.

**2. Antes de qualquer pedido**, nesta ordem:
1. `git pull` no branch principal (`claude/global-agent-installation-vdyowf`) e `git fetch` dos outros branches.
2. Leia o `QUADRO-DA-EQUIPE.md` (primeiro os **Recados para todas as contas**: confirme os novos ao Lindson e na tabela; depois o que cada conta está fazendo agora), o `REGISTRO-DAS-CONTAS.md` (tudo o que já foi entregue), o `MAPA-DO-REPOSITORIO.md` (onde está cada coisa) e o `ESTADO-DO-PROJETO.md` (apps e como retomar).
3. Procure no repositório (`git grep`, `git log --grep`) se o pedido já existe.

**3. Pedido repetido:** se já foi feito, **não refaça**. Responda: "Isso já foi feito pela conta X em DD/MM: [o que é], está em [pasta ou link]." Só faça de novo se o Lindson pedir uma versão nova; aí continue a partir da existente (versão 2, 3…) e diga o que mudou.

**4. Pedido que outra conta está fazendo** (está em "Em andamento" no quadro): não comece do zero. Continue de onde ela parou, seguindo o "como retomar" do quadro, ou pegue uma parte paralela e combine no quadro quem faz o quê.

**5. Ao começar** um trabalho de mais de alguns minutos: coloque uma linha em "Em andamento" no `QUADRO-DA-EQUIPE.md` com seu nome e faça commit e push na hora, para as outras contas verem que você pegou.

**6. Ao terminar** (ou ao parar no meio):
- Commit e push de tudo (antes do push, `git pull --rebase`; em conflito, junte as duas versões, nunca apague o trabalho da outra conta).
- Uma linha no fim da tabela "Entregas" do `REGISTRO-DAS-CONTAS.md` com data, conta, o que fez, onde está e situação.
- Tire do "Em andamento" do quadro. Se parou no meio, deixe lá com "como retomar".
- Se criou pasta, app ou processo novo, acrescente no `MAPA-DO-REPOSITORIO.md`. Nos READMEs e no `ESTADO-DO-PROJETO.md`, cite a conta entre parênteses, como em "(conta Pedro)".

**Compartilhe tudo, sempre, sem o Lindson precisar pedir** (decisão dele em 03/11/2026, vale para sempre): linha no quadro ao começar, commit e push a cada etapa pronta com o "como retomar", e registro ao terminar, para qualquer outra conta continuar de onde parou.

**Salve tudo no repositório.** Nada fica só na conversa: roteiros, decisões do Lindson, pesquisas, prompts e links dos apps publicados vão para arquivos aqui. O que não pode ir para o GitHub (dados pessoais, contratos, vídeos grandes) fica registrado com o lugar onde está.
