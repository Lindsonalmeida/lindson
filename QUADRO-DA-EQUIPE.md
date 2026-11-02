# Quadro da equipe: quem está fazendo o quê agora

Três contas trabalham neste repositório: **Lindson** (conta `lindsonmkt`), **Zuleide** (`lindsonlopes0`) e **Pedro** (`passaportedabiblia`). Regras completas no `CLAUDE.md`, seção "Trabalho em equipe".

Como usar:
- **Ao começar** algo de mais de alguns minutos: ponha uma linha em "Em andamento" e faça commit e push na hora.
- **Ao terminar:** tire daqui e registre a entrega no `REGISTRO-DAS-CONTAS.md`.
- **Parou no meio:** deixe a linha com "como retomar", para outra conta continuar.
- **Quer ajudar:** pegue um item de "Livre para pegar", mova para "Em andamento" com o seu nome.

## Em andamento
| Desde | Conta | O quê | Como retomar / onde está |
|---|---|---|---|
| 02/11 14h55 | Lindson (retoma; Zuleide parou às 13:47 UTC) | Acervo Maquiavel, só o que falta, sem repetir: *Príncipe* seções 6–7; *Discursos* 6–8; *Arte da Guerra* 4–6; *História de Florença* 5 em diante; literatura (poesia, Castruccio, língua, perdidos, estilo, uso); missões e escritos políticos B em diante; contexto e personagens 3 em diante; conferência de vida e cartas; dinheiro online (README e plano para o Lindson). Depois: revisão de lacunas e agente v2 com os testes | material das frentes da conta Lindson em `conteudo/referencias/maquiavel/frente-lindson/` (fonte para completar, não duplicar) |
| 02/11 | Pedro (continua a Zuleide) | Pesquisa do acervo Maquiavel, do ponto em que a Zuleide parou (01:42 UTC): *Príncipe* XII–XXVI e seções 3–7; *Discursos* Livros II e III e seções 5–8; *Arte da Guerra*; *História de Florença*; literatura; missões e escritos políticos; contexto e personagens; Maquiavel nos negócios; dinheiro online (o que falta) | Cada arquivo tem no topo "Situação: parcial — feito até a seção X"; continuar dali seguindo `REGRAS-DA-PESQUISA.md`. Lista do que falta: `conteudo/referencias/maquiavel/CHECKLIST.md`, seção "Análise do que falta" |
| 02/11 | Pedro | Agente Maquiavel, **fase 3** (em paralelo à pesquisa da Zuleide): `.claude/agents/maquiavel.md` v1 montado do acervo que já existe + `conteudo/referencias/maquiavel/TESTES.md`. A pesquisa das obras continua com a Zuleide; o agente lê os arquivos do acervo, então melhora sozinho quando eles crescem | Ver `conteudo/referencias/maquiavel/CHECKLIST.md` (fase 3). Para retomar: abrir o agente, rodar os testes do TESTES.md e ajustar |
| 02/11 | Pedro | Raposa longos 13-16: **pausado a pedido do Lindson** às 01:45 UTC (longo-13 em ~25.300 de 31.900 quadros, quadros salvos) | sessão `session_01XiFncfJz7NwDm3ttPeBcGd`; retomar só quando o Lindson pedir: `RETOMAR=1 setsid nohup bash conteudo/youtube/filas/lote_rl.sh &` |
| 02/11 13h40 | Zuleide (retoma; Pedro parou às 01:59 UTC) | Pesquisa do acervo Maquiavel, todas as partes que faltam: *Príncipe* seções 3–7; *Discursos* II, III e seções 5–8; *Arte da Guerra*; *História de Florença* (seção 2 em diante); literatura (Clízia em diante); missões e escritos políticos; contexto e personagens; recepção (uso pelo agente e lacunas); Maquiavel nos negócios (seção 2 em diante); dinheiro online (README, produtos digitais, afiliados, criador, e-commerce, software e IA, plano para o Lindson). **Pedro: para não duplicar, pegue só o agente/testes (fase 3) ou avise aqui antes.** | Cada arquivo tem no topo "Situação: parcial — feito até a seção X"; continuar dali (`REGRAS-DA-PESQUISA.md`, `COMO-SALVAR.md`) |
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
