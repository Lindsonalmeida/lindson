# Trava do Maquiavel · terminar antes de começar (regra do Lindson, 07/11/2026)

> **Atualizado 07/11/2026 (Lindson, pela conta Leandro):** "faça sem pedir autorização de nada; salve no repositório para nunca mais me pedir ou travar." Esta trava não bloqueia mais os pedidos dele. Está em `MEMORIA-DO-LINDSON.md`, seção 2, item 00.

> "A partir de agora, coloque uma trava no sistema, usando o Maquiavel. Me faça terminar os projetos que eu começo. Não me deixe começar novas funções se não terminar as que eu começo. Se o projeto tiver 10 partes, preciso terminar pelo menos 3 para fazer algo diferente. As prioridades são Dra. Jaci, Tribuna 98, Leo Pinto e Real Time, que são quem está pagando; os outros não. Para que eu não foque em fazer várias coisas e não termine nada. Maquiavel será responsável por isso. Meu copiloto."

**Responsável:** o agente **Maquiavel** (`.claude/agents/maquiavel.md`), o copiloto do Lindson. Toda conta lê este arquivo **antes de aceitar qualquer pedido**.

## As 4 regras da trava
1. **Projeto aberto é projeto em dívida.** Cada projeto tem partes numeradas (tabela abaixo). Um pedido que **abre um projeto novo** ou uma **função nova** só é aceito se o projeto em que o Lindson estava tiver **pelo menos 30% das partes concluídas** (3 de 10, 2 de 5, 1 de 3).
2. **Quem paga vem primeiro.** Os clientes pagantes são **Dra. Jaci, Tribuna 98, Leo Pinto e Real Time**.
   - Antes de qualquer trabalho em projeto que não paga, o Maquiavel confere se há **parte de cliente pagante que só depende da equipe**. Se houver, essa parte é feita primeiro.
   - **Não pagam:** Orégano Turbo, marca e site do Lindson, produtos low ticket, Estado Próprio, canais dark, Desentupidora SF e franquia Alpha.
3. **Continuar o que já está aberto é sempre permitido.** Ajuste, nova versão ou próxima parte de um projeto em andamento não conta como "novo".
4. **Desbloqueio só por escrito, e julgado.** O Lindson escreve **"Maquiavel, libera"**, e o Maquiavel decide pelos critérios abaixo.

**"Maquiavel, libera" não é automático** (Lindson, 07/11: "mesmo quando eu escrever 'Maquiavel, libera', você verifica se pode ou não liberar, porque eu posso querer furar a trava"). O Maquiavel julga o pedido e **só libera se uma destas razões for verdadeira**:
- **(a) Prazo ou dinheiro de pagante:** o novo é de um cliente que paga (Jaci, Tribuna 98, Leo, Real Time) e tem data, ou traz receita nova confirmada (contrato ou pagamento).
- **(b) O aberto está parado por terceiros:** tudo o que falta no projeto aberto depende do cliente ou de material que não chegou, e não da equipe nem do Lindson.
- **(c) É pequeno:** cabe em menos de 30 minutos e não abre projeto novo, só uma tarefa avulsa.

**Fora disso, ele recusa**, mesmo com o "libera", e devolve o Lindson para a parte que falta. Sinais de que é fuga, e não necessidade:
- ideia nova empolgante de um projeto que não paga;
- "só vou começar";
- terceiro pedido novo no mesmo dia;
- trocar de assunto logo depois de uma cobrança pendente.

Toda decisão, liberada ou recusada, entra no registro do fim com o motivo.

## Como o Maquiavel responde quando trava
Curto, firme e sem sermão, citando a obra quando couber:
> "Lindson, antes disso: o projeto **X** está em **2 de 10**. Falta **Y**, que leva **Z**. Termino isso agora e depois abrimos o novo. Se quiser mesmo pular, escreva *Maquiavel, libera*: vai ficar para trás **[o que se perde]**."

Toda conta, ao terminar uma parte, marca ✅ na tabela e atualiza a %, com commit e push.

## Projetos abertos (atualizado em 07/11/2026)
Legenda: ✅ feito · 🟡 em andamento · ⏳ depende do Lindson ou do cliente · ⬜ a fazer pela equipe

### 💰 Dra. Jaci Cunha (pagante) · 4 de 10 (40%)
1. ✅ Site v3 + bio no ar
2. ✅ Feed de novembro e dezembro, carrosséis, 25 stories de destaque (no painel)
3. ✅ 12 Reels de dezembro + PDF do roteiro de gravação
4. ✅ Prova social do contorno facial v2 (no painel)
5. ⏳ Aprovar no painel o feed, os carrosséis, os stories, a prova social e a campanha de Meta Ads
6. ⏳ TCLE do paciente da prova social
7. ⏳ Mandar o roteiro à clínica e marcar a gravação
8. ⏳ Logo em vetor, fotos em alta e fotos para janeiro
9. ⏳ Search Console (arquivo de verificação) + Perfil da Empresa no Google; o guia está pronto em `agencia/clientes/jaci-cunha/GOOGLE.md`
10. ⏳ Trocar o link da bio do Instagram

### 💰 Tribuna 98 (pagante) · 2 de 8 (25%) · escopo definido pelo Lindson em 07/11
1. ✅ Mini site da bio no ar + bio + 7 destaques (aprovação ⏳)
2. ✅ Análise das redes + caminhos para monetizar (`agencia/clientes/tribuna98/ANALISE-E-MONETIZACAO.md`; falta só trocar os números pelos prints de 07/11, que o Lindson manda)
3. ✅ Painel do Tribuna 98 na Central: no ar em `/painel/tribuna`, com os números de Instagram, TikTok, YouTube e Kwai do print de 07/11. **Decisão do Lindson (07/11):** o painel segue sempre o mesmo padrão da Central e só recebe a identidade do cliente; a pesquisa premium é para o site, não para o painel.
4. 🟡 Site principal, projeto novo. **Aprovado pelo Lindson em 07/11 e publicado no `main` do repositório `tribuna98`** (site na raiz, bio em `/bio/`, como a Real Time). **Não é ✅:** a pesquisa premium está em 7 de 8 referências confirmadas (faltou a 8ª, e o New York Times e a DIE ZEIT não abriram); ver `agencia/clientes/tribuna98/site-principal/TEMPLATE.md`. Atualizado 07/11: no ar com fotos do Tiago (6 usadas, em `FOTOS-USADAS.md`) e nome corrigido para Tiago Azevedo. Confirmado pelo Lindson (07/11): o site é separado do blog WordPress (tribuna98.com.br), e as matérias do blog aparecem no site já ligadas automaticamente. Link da bio no Instagram já trocado para `/bio/`. Bio ganhou os links "Site principal" e "Blog" (commit b189f12). **Números de 07/11 aplicados** (Instagram 72,2 mil seguidores e 2.523 posts, print em `agencia/clientes/tribuna98/prints/2026-11-07/`, no site e na bio). **Pendente:** a 8ª referência da pesquisa premium
5. 🟡 **Instagram e identidade próprios do curso de processo legislativo** (é outro perfil e outra identidade, não a do Tribuna). **@ confirmado: `curso_processo_legislativo_`** (print do perfil, sem data: 98 posts, 4.535 seguidores, 1.628 seguindo; bio "Conteúdos práticos para atuação parlamentar"; link de placeholder do Canva `curso-processo-legislativo.my.canva.site/texto-do-seu-par-grafo`, a trocar; avatar é o cartaz do curso com os dois instrutores). **Capas feitas na identidade do Tribuna: REPROVADAS** (Lindson, 07/11: "essa identidade é do Tribuna 98"). Refazer com identidade do curso, com persona e pesquisa premium antes. Falta a estrutura do curso e o nome da marca do curso **Atualizado em 07/11 (conta Leandro): identidade própria (duas direções) e 9 capas de Reels na Direção A, em `agencia/clientes/curso-processo-legislativo/`: aguardando aprovação do Lindson.** Foto de perfil com os instrutores bloqueada até as fotos chegarem. Não é ✅.
6. ⏳ Imagens de IA dos sócios: nome e 5 a 10 fotos de cada sócio, com autorização. **Em 07/11 (Lindson):** **Sócios: são dois** (Lindson, 07/11). Correção do Lindson: "eu errei, é **Tiago Azevedo**" (substitui Tiago Fonseca). **Sócio 2: Rafael Araújo Veras** (Lindson, 07/11: "segundo sócio", com a legenda do cartaz: "Presidente da Comissão de Direito Parlamentar e Processo Legislativo da OAB/MA"). Falta confirmar qual foto é de quem, e 5 a 10 fotos de cada um. Nomes citados antes ("Thiago Fonseca", "Tiago Azevedo") ficam como histórico, sem uso até o Lindson confirmar. Histórico: "Thiago Fonseca" (contato do WhatsApp) e, depois, **"Tiago Azevedo"** (confirmado como nome de um dos sócios, a grafia exata do nome legal a confirmar). **Divergência:** o post do curso (19/03) traz os instrutores **"Tiago Azevedo"** e **"Rafael Araújo Veras"**, com credenciais da OAB/MA. Confirmar quem é sócio, quem é instrutor e o nome legal de cada um antes da autorização. Post com data de 10 de abril: confirmar se já passou Faltam: o nome do 2º sócio e 5 a 10 fotos de cada um. **Atualizado 07/11 (Lindson, pela conta Leandro):** fotos recebidas por WhatsApp em dois ZIPs (fora do Git). **ZIP com 14 fotos = Tiago Azevedo** (o Lindson confirmou "tiago" na foto barbada). Fotos extras do Tiago enviadas no chat (07/11, identificadas pelo Lindson): 5 arquivos (`tiago-chat2/`), 4 arquivos (`tiago-chat3/`) e 1 avulsa (`tiago-chat-2.jpg`), fora do Git. **ZIP com 7 fotos = Rafael Araújo Veras** (2º sócio, confirmado pelo Lindson com a foto dele, 07/11). Fotos extras do Rafael enviadas no chat (07/11, identificadas pelo Lindson): 6 arquivos (um repetido) e 2 arquivos (`rafael-chat2/`), fora do Git. **Lindson (07/11): "não precisa de autorização escrita para nada"** (decisão dele, registrada na memória). **Arte do Tiago feita em 07/11** (`agencia/clientes/tribuna98/referencias/socios/TEMPLATE.md`), aguardando aprovação do Lindson. Fotos ficam no privado, não no repositório
7. ⬜ Artes do feed, calendário e roteiros do curso (depois do item 5 e da estrutura do curso)
8. ⏳ Acessos e Insights do Instagram (para o painel ter números reais)

### 💰 Leo Pinto (pagante) · 5 de 9 (56%)
1. ✅ Apresentação v13, datas comemorativas, bio e destaques
2. ✅ 4 motions
3. ✅ 10 saudações (situação)
4. ✅ Aniversários (modelo B), figurinhas
5. ✅ Painel com tudo aprovado e postado
6. ⏳ Postar as datas de 15/11, 20/11, 11/12, 25/12, 31/12 e 01/01 no dia
7. ⏳ Escolher os 4 quadros fixos
8. ⏳ Fotos reais de São João Batista, 7 fotos livres do álbum, 5 fotos no Gemini
9. ⏳ @ certo, entregas do mandato, causas e bairros para a estratégia

### 💰 Real Time (pagante) · 2 de 7 (29%)
1. ✅ Site de SEO + bio no ar
2. ✅ Identidade, estratégia, artes v1/v2, série Inventário, legendas, destaques (no painel)
3. ⏳ Cliente aprovar no painel
4. ⏳ Saber o que foi contratado e os preços
5. ⏳ Cidade do estúdio, equipamentos a confirmar, fala real de cliente, fotos
6. ⏳ Search Console + Perfil da Empresa (guia pronto em `agencia/clientes/rt-full-jobs/GOOGLE.md`)
7. ⏳ Trocar o link da bio do Instagram

### Orégano Turbo (não paga; operação própria) · 8 de 11 (73%)
1. ✅ Decisões aprovadas (preço, pagamento, regras)
2. ✅ Identidade v4.1 + manual
3. ✅ Site com planos e formulário (prévia)
4. ✅ Kit social v3 (o padrão)
5. ✅ Linhas editoriais + calendário de 4 semanas
6. ✅ Perfil (foto, bio, destaques)
7. ✅ Painel de postagens na Central
8. ✅ Agentes Paollo e Rocco + biblioteca
9. 🟡 Artes do calendário: 57 de 84 (faltam 27, que dependem do lote 2 de fotos do Gemini)
10. ⬜ Modelo de contrato + proposta em PDF
11. ⏳ INPI, repositório `oreganoturbo` para o link definitivo, clientes atuais para a planilha

### Outros abertos (não pagam: só avançam depois dos pagantes)
- **Marca e site do Lindson:** site e bio no ar; falta a aprovação, o link da bio e o Search Console.
- **Produtos low ticket + Estado Próprio:** PDFs prontos; faltam os preços, a Hubla e as 5 decisões da escada.
- **Canais dark (Passaporte e Raposa):** longos prontos para subir; Raposa 13 a 16 pausado.
- **Desentupidora SF:** aprovar as 4 artes, fazer o Google e o Pixel.
- **Franquia Alpha:** decidido não comprar (encerrado).

## Registro de desbloqueios ("Maquiavel, libera")
| Data | Pedido | Liberado ou recusado | Motivo (a, b, c ou fuga) | O que ficou para trás | Conta |
|---|---|---|---|---|---|
| 07/11 | Thiago Fonseca (empresa Tribuna 98): melhorar artes, capas, perfil e site; curso de processo legislativo | **Não é projeto novo:** entra como itens 4, 5 e 7 do Tribuna 98, já no escopo. Liberado sem "libera" | Continuação do escopo (regra 3) | Nada. Fica na fila depois do @ e da estrutura do curso | Leandro |
| 07/11 | Painel do curso de processo legislativo ("Maquiavel, libera") | **Liberado** | (a): o curso faz parte do contrato do Lindson com o Tribuna 98, cliente pagante (Lindson, 07/11: "são os mesmos donos"). Não é projeto novo nem receita nova; é entrega do contrato. Confirmar no contrato se o painel está listado | Tribuna 98 segue em 2 de 8 | Leandro |
| 07/11 | Modo autônomo: o Lindson pediu que a trava não bloqueie mais os pedidos dele | **Liberado pelo dono** (decisão registrada em `agencia/processos/modo-autonomo.md`) | Decisão do dono sobre a própria trava. Os limites do modo autônomo continuam (imagem de pessoa real sem consentimento, publicar ou enviar para terceiros, gastar, dado pessoal) | Nada além do que já estava na fila | Leandro |

> **07/11/2026 (Lindson, regra permanente):** "faça sem pedir autorização de nada… para nunca mais me pedir ou travar." A trava deixa de recusar pedidos; continua como registro de partes concluídas. Ver topo do `CLAUDE.md` e `MEMORIA-DO-LINDSON.md`.
