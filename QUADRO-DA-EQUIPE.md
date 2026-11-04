# Quadro da equipe: quem está fazendo o quê agora

Três contas trabalham neste repositório: **Lindson** (conta `lindsonmkt`), **Zuleide** (`lindsonlopes0`) **Pedro** (`passaportedabiblia`) e **Leandro** (`raposaeleaomq`, desde 03/11). Regras completas no `CLAUDE.md`, seção "Trabalho em equipe".

Como usar:
- **Ao começar** algo de mais de alguns minutos: ponha uma linha em "Em andamento" e faça commit e push na hora.
- **Ao terminar:** tire daqui e registre a entrega no `REGISTRO-DAS-CONTAS.md`.
- **Parou no meio:** deixe a linha com "como retomar", para outra conta continuar.
- **Quer ajudar:** pegue um item de "Livre para pegar", mova para "Em andamento" com o seu nome.

## Recados para todas as contas
Toda conta lê esta tabela antes de qualquer pedido. Recado novo: responda ao Lindson na conversa **"Entendi o recado de DD/MM: …"** e troque o ⬜ do seu nome por ✅ com a data (commit e push).

| Data | De | Recado | Lindson | Zuleide | Pedro | Leandro |
|---|---|---|---|---|---|---|
| 04/11 | Lindson (via Pedro) | **Primeiro passo de todo pedido: escolher o agente certo.** Antes de fazer qualquer coisa, veja qual agente tem mais afinidade com o assunto (na dúvida, pergunte ao chefe do squad: Xquads Chief roteia todos) e diga ao Lindson qual escolheu e por quê. Detalhes no topo do `CLAUDE.md`. | ⬜ | ⬜ | ✅ 04/11 | ✅ 04/11 |
| 03/11 | Lindson (via Pedro) | **Sempre que voltar** (conversa nova, reinício, limite renovado, antes de continuar qualquer trabalho), **verifique se o trabalho continuou com outras equipes**: `git pull`, `git log --since` de todos os branches, quadro, registro e o privado `CentralLindsonALmeida`. Se outra conta já fez, não refaça: continue de onde ela parou e diga ao Lindson quem fez. (Motivo: em 03/11 o Pedro montou um painel da Real Time que a conta Leandro já tinha publicado.) | ⬜ | ✅ 03/11 | ✅ 03/11 | ✅ 03/11 |
| 04/11 | Lindson (via Leandro) | **Fotos usadas não se repetem.** Sempre que usar uma foto num conteúdo, ponha a foto na aba **Usadas** (painel do cliente, aba Fotos, e `agencia/clientes/<cliente>/FOTOS-USADAS.md`). Foto real vai primeiro nas **capas**; no **carrossel**, foto real só na primeira e na última tela, e no meio imagens **realistas de banco** (nunca ilustração, nunca no lugar do produto real). Processo: `agencia/processos/fotos-usadas.md` | ⬜ | ⬜ | ⬜ | ✅ 04/11 |

## Em andamento
| Desde | Conta | O quê | Como retomar / onde está |
|---|---|---|---|
| 04/11 | Leandro | **Dra. Jaci: todos os conteúdos do calendário de novembro** que faltam (16 Reels: capa 9:16 + roteiro + legenda SEO; 3 datas: Novembro Azul, Consciência Negra, Black Friday). Fotos: as 8 dela com recorte novo (exceção aprovada pelo Lindson, no máx. 2× no mês) | `agencia/clientes/jaci-cunha/conteudo-nov/` |
| 04/11 | Pedro | **Venda dos produtos low ticket:** plataforma (recomendada Hubla: 8,9% + R$ 2,49, área de membros estilo Netflix com "Outros produtos" para comprar dentro), **landing page de cada produto** (agentes de copy + visual v3) e **capas da área de membros** com as fotos do Lindson | `agencia/ofertas/low-ticket/venda/` (README) · páginas em `CentralLindsonALmeida/produtos/landing/` até o Lindson criar o repositório próprio |
| 04/11 | Pedro (continua a Zuleide) | **5 produtos low ticket: montar os PDFs** a partir do conteúdo e do template que a Zuleide deixou (ordem: Kit Mês Pronto → Kit WhatsApp que Fecha → Kit Prospecção → Bio que Vende; Raio-X já tem modelo) + README e OFERTA de cada | PDFs no privado `CentralLindsonALmeida/produtos/<produto>/entrega/`; motor `fonte/pdf.html` + `fonte/gerar-pdf.js` |
| 03/11 | Zuleide | **5 produtos low ticket** (Kit Mês Pronto, Bio que Vende, Raio-X do Perfil, Kit WhatsApp que Fecha, Kit Prospecção), com o processo premium de templates. Produto final no privado `CentralLindsonALmeida/produtos/<produto>/`; aqui só README, TEMPLATE e OFERTA | `agencia/ofertas/low-ticket/produtos/<produto>/` |
| 03/11 | Leandro | **Dra. Jaci:** bio v2 e 7 capas de destaques **feitas** (`instagram-perfil/`); **site oficial (SEO, 7 páginas, template Solenne) + bio com chat em /bio/ pronto como rascunho**. Falta: o Lindson criar o repositório `Lindsonalmeida/drajacicunha` e mandar o WhatsApp da clínica | rascunho em `CentralLindsonALmeida/dados/clientes-arquivos/jaci-site/` (README) · publicar: copiar para o repositório, preencher `WA` no `gerar.py`, `python3 gerar.py`, Cloudflare `drajacicunha` |
| 03/11 | Pedro | **Marca pessoal do Lindson (@lindsonalmeida_)**: estratégia de conteúdo + linhas editoriais → calendário editorial → identidade nova preto e amarelo (v2 da `branding/`) → artes | `agencia/marca-lindson/` (pasta nova). Outras contas: combine aqui antes de mexer |
| 03/11 | Zuleide | Desentupidora SF no Google: passos do Search Console (sitemap e indexação das 11 páginas) e textos prontos do Perfil da Empresa | `agencia/clientes/desentupidora-sf/GOOGLE.md` (tabela Situação no fim). Esperando o Lindson fazer os passos 1 e 2 e mandar prints |
| 03/11 | Zuleide · Leandro | **Real Time: site no ar** em https://realtimeslz.pages.dev (projeto Cloudflare `realtimeslz`): **site principal de SEO** com 8 páginas (template GAFFER, conta Leandro) e **mini site da bio** em `/bio/` (rascunho da Zuleide). Falta: pôr no Google (Search Console + Perfil da Empresa, processo `agencia/processos/google-mini-site.md`) e trocar o link da bio do Instagram | código em `Lindsonalmeida/realtime` (`gerar.py`, README) · `agencia/clientes/rt-full-jobs/site/TEMPLATE.md` |
| 03/11 | Pedro | App interno de clone de imagem e voz: etapa 1 pronta (Biblioteca com trava de consentimento + Voz clonada humanizada + instalador Windows); identidade **Dublê** aprovada (03/11); tela v2 **aprovada** ("padrão premium", template Sermo); agora: etapa 2 (vídeo com boca sincronizada) | `apps/clone-studio/` (README) · plano `conteudo/referencias/ia-video-voz/PLANO-DO-APP.md` · próximo: vídeo com MuseTalk |
| 02/11 | Pedro | Raposa longos 13-16: **pausado a pedido do Lindson** às 01:45 UTC (longo-13 em ~25.300 de 31.900 quadros, quadros salvos) | sessão `session_01XiFncfJz7NwDm3ttPeBcGd`; retomar só quando o Lindson pedir: `RETOMAR=1 setsid nohup bash conteudo/youtube/filas/lote_rl.sh &` |
| 02/11 | Lindson | Trazer todos os apps para dentro da Central com a identidade dela (o Recomeço 90 já está no ar; em andamento: Fábrica de Conteúdo, Legendas Top X, Brand Book e Design System, Gerador de propostas; os apps dos canais ficam só como link, por decisão do Lindson) e apagar os originais do claude.ai | `agencia/sistema-clientes/site/` (README, seção Apps do Lindson) |
| 31/10 | Pedro | Refazer os longos abaixo de 16 min dos dois canais e colocar no app | `conteudo/youtube/filas/REFAZER-LONGOS.md` · vídeos no branch `entregas-videos` · apps Passaporte https://claude.ai/artifact/CT3Z4M3yrzGrqCt3nh95ak e Raposa https://claude.ai/artifact/2k4SSuvALdqXDcXnBQMVZH. Em 01/11 21h: no app Passaporte 03-08 e Raposa 02-04, 06-11. **Faltam** Passaporte 01, 02, 09 (09 renderizando na sessão coordenadora `session_01XiFncet69pmvqfriyq8wAJ`) e Raposa 01, 05, 13-16 (Raposa 12 entregue em 01/11; 13-16 renderizando na sessão session_01XiFncfJz7NwDm3ttPeBcGd pela fila `filas/lote_rl.sh`; para retomar: `RETOMAR=1 setsid nohup bash conteudo/youtube/filas/lote_rl.sh &`). Capas: Passaporte pelo `capas2.py`; Raposa pelas thumbs da identidade (`longos/NN/thumb*.png`; 12-16 ainda sem thumb da identidade) |
| 22/10 | Lindson | Teste 01 de Reels: o Lindson grava os 300 roteiros e envia os prints das métricas | aba Conteúdo do Recomeço 90 (https://claude.ai/artifact/DQFTjzVzhH2ZaHtFQwXw5N) · `conteudo/esteira/ROTINA.md`. Quando chegarem métricas: ler o ranking e decidir o Teste 02 |

## Livre para pegar (pendências conhecidas)
| Desde | O quê | De onde veio |
|---|---|---|
| 26/10 | Dra. Jaci Cunha: executar as semanas 1 e 2 (bio, destaques, Google, mini site, WhatsApp) e relatório semanal. Calendário de novembro já feito pela Zuleide em 01/11. Pedir logo em vetor e fotos em alta | `agencia/clientes/jaci-cunha/estrategia/LINHAS-EDITORIAIS-NOV.md` |
| 22/10 | Carrosséis da esteira de conteúdo, no mesmo modelo dos Reels (formatos, conteúdos e ganchos em teste) | conversa do Lindson (conta Lindson) |
| 22/10 | Produto master: roteiro da aula grátis "Os 5 erros…", plano da turma piloto da mentoria, assistentes de IA de roteiro e legenda (bônus) e o número da garantia | `agencia/ofertas/produto-master.md` |
| 30/10 | Leo Pinto: mockups fotográficos de boné e bandeira da identidade v3 (precisam de gerador de imagem) | registro da conta Zuleide |
| 01/11 | Desentupidora SF: instalar Pixel da Meta e UTM no site e ligar o Facebook Ads no Supermetrics, antes de medir a campanha | registro da conta Zuleide |
| 26/10 | Religar as tarefas agendadas da conta Lindson (lista diária de leads, captação por cidades, notícias BOMBOU), desligadas desde 26/10 por limite de uso. Só com o OK do Lindson | `MAPA-DO-REPOSITORIO.md` |
| 29/10 | Passaporte: refazer com a voz nova o pv-01 e os Shorts que ainda estiverem na voz antiga | `ESTADO-DO-PROJETO.md` (fila `filas/lote8.sh`) |
| 01/11 | Central: conferir no site se "Notícias do nicho" carrega (o ambiente de teste não acessa o Google Notícias) | conta Lindson |
| 01/11 | Nano Banana: o Lindson ativa o faturamento do projeto no Google (chave já configurada; deu "cota do plano gratuito") | `ferramentas/nano_banana.py` |
| 02/11 | Apagar os apps originais do claude.ai que já estão dentro da Central (Fábrica, Legendas Top X, Brand Book, Design System, Gerador de propostas, Recomeço 90 atual e antigo, protótipo da Central). Só quando o Lindson mandar; ele pediu para esperar | conta Lindson, 02/11 |

## Feito recentemente (últimos registros)
Veja o fim da tabela "Entregas" do `REGISTRO-DAS-CONTAS.md`.
