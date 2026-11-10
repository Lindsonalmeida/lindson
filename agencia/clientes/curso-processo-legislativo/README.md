# Curso de processo legislativo · identidade própria
Conta Leandro, 07/11/2026 · Instagram **@curso_processo_legislativo_** (4.535 seguidores, 98 posts, conforme o print) · item 5 do escopo do Tribuna 98 (`TRAVA-MAQUIAVEL.md`).
**Status: aguardando aprovação do Lindson.** Não é ✅ até ele aprovar.

Este curso tem **outro perfil e outra identidade**. Não usa nada do Tribuna 98. As capas antigas feitas com a identidade do Tribuna (em `agencia/clientes/tribuna98/capas-reels-curso/`) foram **reprovadas** e não podem ser publicadas.

## O que está aqui
| Pasta/arquivo | O que é |
|---|---|
| `TEMPLATE.md` | Persona em 5 linhas, pesquisa premium com países confirmados na página, escolhidas e descartadas |
| `referencias/` | 10 capturas das páginas da pesquisa (com os descartes) |
| `identidade/DIRECOES.md` | v1 (descartada): Direção A "Ata" (reprovada) e B "Regimento" |
| `TEMPLATE-V2.md` · `identidade/DIRECAO-C-SINAL.md` | **v2 atual**: direção C "Sinal", pesquisa nova com 3 escolhidas (EUA, Reino Unido, Austrália) |
| `capas-v2/capa-01…09.png` | **9 capas v2, atuais** (gerador `gerar-v2.js`, prancha `identidade/direcoes-v2.png`) |
| `identidade/direcoes.png` | Prancha com as duas direções lado a lado, para o Lindson escolher |
| `capas/capa-01…09.png` | v1 (Direção A, reprovada): fica só para histórico |
| `avatar/avatar-marca-provisoria.png` | Foto de perfil **provisória**: só a marca, sem pessoas. Não substitui a foto dos instrutores |
| `gerar.js` | Gera tudo de novo: `node gerar.js` (Node + Playwright) |

## Foto de perfil com os dois instrutores: **bloqueada**
- O cartaz do curso e as fotos dos instrutores **não estão no repositório**. Sem as fotos reais, não há como montar a foto de perfil com eles. Ilustração no lugar de foto real não é permitida.
- Nomes que aparecem no cartaz, com a grafia a confirmar: **Tiago Azevedo** (também sócio do Tribuna 98) e **Rafael Araújo Veras** (credenciais OAB/MA no post de 19/03).
- Para liberar: o Lindson manda **uma foto por mensagem** de cada instrutor (nome legal confirmado). Nada de foto dos sócios sem o que foi decidido na memória (07/11: sem autorização escrita).

## Pendências
1. Fotos dos dois instrutores (uma por mensagem) → foto de perfil.
2. Estrutura do curso (ordem das aulas) → confirmar os títulos das capas. Os de 02, 03, 05 e 06 são propostas, porque estavam cortados nos prints.
3. Link de placeholder da bio (`curso-processo-legislativo.my.canva.site/texto-do-seu-par-grafo`) a trocar pelo link real.
4. Aprovação do Lindson: Direção A ou B, e as capas.
5. Visual final da fonte de título: instalar Fraunces, para não usar a serifa de fallback.

## Não tem nada disto
Sem promessa de resultado nas peças (ex.: "vai ganhar a votação"). Sem nome de modelo em arquivo ou mensagem.

## Recorte dos sócios (pronto, conta Leandro, 07/11/2026)
- Ferramenta: `rembg` com o modelo BiRefNet, o mesmo processo do `agencia/operacao-propria/identidade/recortar4.py`. Testado nesta sessão: o modelo baixa e roda.
- Fluxo das fotos: o Lindson envia pela aba **Fotos dos sócios** do painel do curso (botão "Escolher fotos", envio pela Central). As fotos ficam fora do Git.
- Depois do envio: recorta cada foto (fundo transparente, sem quadrado) e põe no espaço do instrutor da capa.
- Pendente: as fotos limpas dos dois sócios. Os prints de vídeo não serão usados (decisão do Lindson).
