# Curso de processo legislativo · pesquisa premium (conta Leandro, 07/11/2026)

**Status: PARCIAL. Não conta como entregue.** A regra pede 8 referências de 3 países, confirmadas pela própria página. Até agora: **4 referências com captura, 1 país confirmado pelo texto da página** (Países Baixos). A meta não foi cumprida.

Regra: `agencia/processos/pesquisa-premium.md`. Capturas em `referencias/` (Playwright, 1440 px). A identidade do Tribuna 98 **não** é modelo para este curso (reprovada em 07/11).

## Persona (antes da pesquisa, a confirmar com o Lindson)
Quem vê e compra: pessoa que atua ou quer atuar no processo legislativo (assessor parlamentar, servidor de casa legislativa, vereador ou deputado em início de mandato, candidato). Procura conteúdo prático, não teoria. Confia em quem explica com exemplo e fonte. Está no Instagram. **Hipótese**: a persona real ainda não foi confirmada pelo Lindson. Pergunta de teste: "essa pessoa pagaria por este curso?"

## Referências capturadas
| # | Captura | Quem | País (confirmado pela página?) | O que a página confirma | Prêmio/destaque confirmado? | Usar? |
|---|---|---|---|---|---|---|
| 1 | `referencias/01-pentagram-dashboard.png` | Pentagram (studio) | Não na captura (Reino Unido/EUA é o conhecido, não conferido) | Página de trabalhos, nome do estúdio | Não conferido | Candidata (tipografia e grid) |
| 2 | `referencias/03-brandnew-us.png` | Brand New (UnderConsideration) | Não confirmado na captura | Vitrine de identidades | Não conferido | Candidata (hierarquia de número e título) |
| 3 | `referencias/04-studio-dumbar-nl.png` | Studio Dumbar | Não confirmado na captura (Países Baixos é o conhecido) | Lista de trabalhos (NextStep, North Sea Jazz, MTV VMAs) | Não conferido | Candidata (sistema tipográfico) |
| 4 | `referencias/11-dennis-snellenberg-nl.png` | Dennis Snellenberg | **Sim: "Located in the Netherlands"** | Designer e desenvolvedor freelancer | Não conferido (há link para Awwwards, sem captura) | Candidata (menu e tipografia limpa) |
| 5 | `referencias/08-dribbble-dashboard-dark.png` | Dribbble (busca "dashboard dark") | — | Página de busca, não estúdio | — | **Não conta** como referência: é vitrine de busca |

## Descartadas e por quê
- **Koto (Reino Unido):** `kotoagency.com/work` deu **404**. Sem captura.
- **Locomotive (Canadá):** captura saiu em branco (página não renderizou). Sem captura válida.
- **Framer Marketplace (dashboard):** página "fora do ar". Sem captura válida.
- **Behance (busca dashboard):** erro HTTP 400. Sem captura válida.
- **Collins Creative:** o domínio mostra "parked free, courtesy of GoDaddy": não é o estúdio. Descartada.
- **Awwwards (dashboard):** **conexão recusada** pelo proxy (ERR_CONNECTION_RESET). Não capturada. É a fonte principal de sites premiados e não foi possível usá-la.
- **Lundgren+Lindqvist (Suécia):** túnel recusado pelo proxy (ERR_TUNNEL_CONNECTION_FAILED). Não capturada.

## Fontes que bloquearam (para o Lindson ou outra conta conferir)
- Awwwards: conexão recusada (proxy). Sem isso, não há painel premium comparável.
- Behance: erro 400 na busca. Tentar pelo perfil de um designer, se o Lindson indicar.
- Framer Marketplace: página fora do ar na URL testada. Outra URL de template de dashboard para tentar.

## O que falta para fechar (meta: 8 de 3 países)
1. Capturar pelo menos 4 referências a mais, de 2 países além dos Países Baixos, com o país confirmado no texto da página (ex.: estúdio do Reino Unido, do Canadá ou dos EUA com página que diga onde fica).
2. Quando o Awwwards voltar a responder, pegar 2 sites de painel/dashboard premiados (Awwwards mostra prêmio e país na própria página).
3. Escolher **3 combinadas** para a identidade, dizer o que se copia (grid, tipografia, uso de cor) e registrar aqui as descartadas.
4. Mostrar as 3 ao Lindson junto com o painel.

## Escolhidas
Nenhuma ainda. Só depois de 8 de 3 países.

## Painel (estrutura, não identidade)
O painel `agencia/sistema-clientes/curso-processo-legislativo/painel-curso.html` usa a estrutura do modelo da Central (`prototipo/painel.html`) com as cores da Central, sem a identidade do Tribuna. A identidade do curso fica **a definir**.
