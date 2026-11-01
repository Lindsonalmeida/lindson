# Registro das contas: quem fez o quê

Toda conta ou equipe que trabalhar neste repositório acrescenta aqui uma linha por entrega, **no fim da tabela** (a mais recente embaixo). Assim as outras sabem o que já existe, onde está e quem perguntar.

- **Conta:** o nome que o Lindson deu à conta (ex.: Zuleide). Conta ainda sem nome: use o identificador dela (ex.: `passaportedabiblia`) até ele dar um nome.
- **Onde:** pasta ou arquivo no repositório e, se houver, o link publicado.
- **Situação:** pronto, em andamento, pendente (e o que falta) ou desfeito (e por quê).

## Nomes das contas
| Nome | Conta do Claude |
|---|---|
| Zuleide | lindsonlopes0 (sessões na nuvem do repositório `lindson`, desde 30/10/2026) |
| Pedro | passaportedabiblia (nome dado pelo Lindson em 01/11/2026; as linhas antigas com "passaportedabiblia" são desta conta) |

## Entregas
| Data | Conta | O que fez | Onde | Situação |
|---|---|---|---|---|
| 31/10/2026 | passaportedabiblia | Painel do Vereador Leo Pinto na Central (identidade do manual do Claude Design, demandas e agenda com banco real) | `agencia/sistema-clientes/leo-pinto/` · https://claude.ai/artifact/7TjjwEUN5jASCbytXAvhHk | pronto (registro feito pela conta Zuleide, a partir do README da pasta) |
| 30/10/2026 | Zuleide | Identidade do Leo Pinto v2 (sistema de marca em 12 páginas) | `agencia/clientes/leo-pinto/identidade/v2/` | substituída pela v3 |
| 30/10/2026 | Zuleide | Identidade do Leo Pinto v3 "Leo da Baixada": monograma LP, selo de mandato, Azulejo da Baixada, 12 ícones, manual de 20 páginas 4:5 | `agencia/clientes/leo-pinto/identidade/v3/` · PDF na página de downloads | pronto; mockups fotográficos de boné e bandeira pendentes (precisam de gerador de imagem) |
| 30/10/2026 | Zuleide | Instalador global do Builder Squad (skills no `/` do Claude Code) | `ferramentas/instalar-builder-squad.sh` | pronto; já existia um da outra equipe em `instalar-builder-squad.sh` (raiz), use esse como principal |
| 30/10/2026 | Zuleide | Regra no CLAUDE.md: consultar o repositório e os outros branches antes de começar | `CLAUDE.md` | pronto |
| 01/11/2026 | Zuleide | Painel do Leo dentro do modelo `prototipo/painel.html` (tema e grupo Mandato) | commits `e4c7c82` e `baaff52` | desfeito: duplicava o painel da conta passaportedabiblia e mexia no modelo que o `montar-leo.py` usa |
| 01/11/2026 | Zuleide | Proposta comercial na identidade da Central do Cliente (preto e amarelo), sem quantidades de entregáveis | `proposta/proposta-central.html` e `proposta/proposta-lindson-almeida-central.pdf` · página de downloads | pronto; o original `proposta/index.html` continua intacto |
| 01/11/2026 | Zuleide | Verificação da campanha de Meta Ads da Desentupidora SF | repositórios `lindson` (todos os branches) e `Lindsonalmeida/GruposSF` | nada configurado: site sem Pixel da Meta nem UTM; Supermetrics sem conta do Facebook Ads ligada |
| 01/11/2026 | Zuleide | Criou este registro e a regra de manter ele atualizado | `REGISTRO-DAS-CONTAS.md` e `CLAUDE.md` | pronto |
| 01/11/2026 | Pedro | Raposa e Leão: acervo dos longos 12-16 (23 obras pela Web Gallery of Art, 6 trocadas por obra do mesmo tema) e render dos longos 12-16 | `conteudo/youtube/raposa-e-leao/motor/acervo_wga.py`, `acervo_trocas.py`, `img/acervo/creditos.json` · app https://claude.ai/artifact/2k4SSuvALdqXDcXnBQMVZH | em andamento: longo-12 renderizando (fila `filas/lote_rl.sh`) |
| 01/11/2026 | passaportedabiblia | Longos abaixo de 16 min refeitos pela regra do Peter (15 sessões, `conteudo/youtube/filas/REFAZER-LONGOS.md`); no app: Passaporte 03, 04 e 08, Raposa 07 a 11 | apps https://claude.ai/artifact/CT3Z4M3yrzGrqCt3nh95ak e https://claude.ai/artifact/2k4SSuvALdqXDcXnBQMVZH · vídeos do app no branch `entregas-videos` | em andamento: Passaporte 01, 02, 05, 06, 09 e Raposa 01-06 e 12-16 renderizando; capítulos do Raposa 07-09 pendentes |
| 01/11/2026 | Pedro | Raposa e Leão: capas no app para baixar (Shorts 01-30 e longos 01-06 e 12-16; 07-11 já tinham) | https://claude.ai/artifact/2k4SSuvALdqXDcXnBQMVZH · `conteudo/youtube/raposa-e-leao/ativos-novo.json` | pronto |
| 01/11/2026 | Zuleide | Fala de 40 s para a influencer política Katje Garcez sobre a entrega de brinquedos na comunidade | `agencia/clientes/katje-garcez/falas/2026-11-01-entrega-de-brinquedos.md` | pronto |
