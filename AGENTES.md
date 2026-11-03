# Nossos agentes, por categoria

Lista feita pela conta Zuleide em 03/11/2026, a partir do repositório (`.claude/agents/`) e dos pacotes oficiais do **Xquads** (github.com/ohmyjahh/xquads-squads, 15 squads, 183 agentes) e do **Builder Squad** (github.com/ohmyjahh/builder-squad, 16 agentes). Total: **201 agentes** (2 nossos + 183 Xquads + 16 Builder).

**Onde funcionam:**
- **Nossos (Maquiavel e Peter):** estão no repositório, funcionam em qualquer conta e sessão deste repositório. Chame com "chama o Maquiavel" / "chama o Peter".
- **Xquads e Builder Squad:** instalados no computador com `instalar-xquads.sh`/`.ps1` e `instalar-builder-squad.sh`/`.ps1`. No Claude Code aparecem como `/<squad>` e `/<squad>:agents:<agente>` (Xquads) e `/builder-squad:<agente>`. Nas sessões na nuvem eles não vêm instalados: a conta precisa baixar o pacote ou seguir o método do agente pelo arquivo dele.
- O nome entre parênteses é o apelido do chefe do squad.

---

## 1. Agentes próprios (feitos para o Lindson)
| Agente | Para quê | Arquivo |
|---|---|---|
| **Maquiavel** | parceiro de negócios: decisões de poder, clientes, preço, sócio, equipe, crise, negociação; professor de dinheiro na internet; conteúdo do Raposa e Leão; confere frases | `.claude/agents/maquiavel.md` (v3.2) |
| **Peter** | canal dark e monetização no YouTube: nicho, roteiros, títulos, capas, retenção, regras do YPP | `.claude/agents/peter.md` |

## 2. Estratégia, negócios e conselho
**Hormozi Squad (16)** — ofertas, preço, leads, vendas e escala: Hormozi Chief (chefe), Offers, Pricing, Leads, Ads, Hooks, Copy, Content, Closer, Launch, Retention, Scale, Models, Audit, Advisor, Workshop.

**Advisory Board (11)** — conselho de grandes pensadores: Board Chair (chefe), Charlie Munger, Naval Ravikant, Peter Thiel, Ray Dalio, Reid Hoffman, Derek Sivers, Simon Sinek, Patrick Lencioni, Brené Brown, Yvon Chouinard.

**C-Level Squad (6)** — diretoria virtual: Vision Chief (chefe), CMO Architect, COO Orchestrator, CTO Architect, CIO Engineer, CAIO Architect (IA).

## 3. Copy e persuasão
**Copy Squad (23)** — Copy Chief (Cyrus), David Ogilvy, Eugene Schwartz, Gary Halbert, Gary Bencivenga, Dan Kennedy, Claude Hopkins, Joe Sugarman, John Carlton, Clayton Makepeace, Robert Collier, Jim Rutz, Parris Lampropoulos, Todd Brown, Stefan Georgi, Jon Benson, Russell Brunson, Frank Kern, Ry Schwartz, Ben Settle, Andre Chaperon, David Deutsch, Dan Koe.

**Copy Master (33)** — os 22 do Copy Squad (menos o chefe) e mais 11: Copy Master Chief (Cyrus), Alex Hormozi, Chris Voss (negociação), Robert Cialdini (persuasão), Blair Warren, Oren Klaff, Joanna Wiebe, John Caples, Rosser Reeves, Sabri Suby, Evaldo Albuquerque.

## 4. Marketing e tráfego pago
**Marketing Squad (5)** — Marketing Chief (Mira), Pedro Sobral, Donald Miller, Eugene Schwartz, Visual Generator.

**Traffic Masters (16)** — Traffic Chief (chefe), Pedro Sobral, Molly Pittman, Depesh Mandalia, Nicholas Kusmich, Ralph Burns, Kasim Aslam (Google), Tom Breeze (YouTube Ads), Media Buyer, Ads Analyst, Creative Analyst, Performance Analyst, Pixel Specialist, Scale Optimizer, Ad Midas, Fiscal (orçamento).

## 5. Marca, posicionamento e narrativa
**Brand Squad (15)** — Brand Chief (chefe), Donald Miller, Miller Sticky Brand, Marty Neumeier, David Aaker, Kevin Lane Keller, Jean-Noël Kapferer, Al Ries, Byron Sharp, Alina Wheeler, Denise Lee Yohn, Emily Heyward, Archetype Consultant, Naming Strategist, Domain Scout.

**Storytelling (12)** — Story Chief (chefe), Joseph Campbell, Blake Snyder, Dan Harmon, Shawn Coyne, Kindra Hall, Matthew Dicks, Nancy Duarte, Park Howell, Marshall Ganz, Keith Johnstone, Oren Klaff.

**Movement (7)** — criar movimento/comunidade em volta da marca: Movement Chief, Movement Architect, Manifestador, Identitário, Fenomenólogo, Estrategista de Ciclo, Analista de Impacto.

## 6. Design
**Design Squad (8)** — Design Chief (chefe), Brad Frost, Dan Mall, Dave Malouf, Design System Architect, UX Designer, UI Engineer, Visual Generator.

## 7. Dados, métricas e retenção
**Data Squad (7)** — Data Chief (Datum), Avinash Kaushik (análise), Sean Ellis (growth), Peter Fader (valor do cliente), Nick Mehta (sucesso do cliente), David Spinks (comunidade), Wes Kao.

## 8. Tecnologia, apps e automação
**Builder Squad (16)** — monta apps e sistemas (a Central passa por ele): Builder Chief (chefe), Estrategista de Produto, Gerente de Projeto, Analista de Processos, Arquiteto de Soluções, Arquiteto de Dados, Arquiteto de Agentes de IA, Engenheiro de Frontend, Engenheiro de Backend, Engenheiro de Automações e Integrações, Designer de UX/UI, Engenheira de Qualidade, Revisor de Segurança e Privacidade, Engenheiro de Release e Operações, Especialista em Documentação, Estrategista de Growth e Vendas.

**Claude Code Mastery (8)** — configurar o próprio Claude Code: Orion (chefe), Sigil (configuração), Latch (hooks), Piper (MCP), Anvil (skills), Nexus (vários agentes), Conduit (projetos), Vigil (atualizações).

**Cybersecurity (15)** — segurança e testes autorizados: Cyber Chief (chefe), Omar Santos, Georgia Weidman, Jim Manico, Chris Sanders, Marcus Carey, Peter Kim, Cartographer, Command Generator, Busterer, Dirber, Fuzzer, Ripper, Rogue, Shannon Runner.

## 9. Coordenação
**Xquads Chief (Xander)** — o chefe geral: recebe o pedido e escolhe o squad certo (`/xquads`).

## 10. Outros
- **Agentes de pesquisa na internet** (gerais do Claude): usados nas pesquisas em todos os idiomas (acervo Maquiavel, dinheiro online, engenharia reversa).
- **RAXOS:** citado no `CLAUDE.md` para revisar código "quando instalado"; ainda não está instalado nem no repositório.

---

## Qual chamar para cada pedido (atalho)
| Pedido | Agentes |
|---|---|
| Decisão de negócio, cliente difícil, sócio, crise | Maquiavel; Advisory Board |
| Oferta, preço, esteira, pacote | Hormozi Offers e Pricing |
| Copy de post, anúncio, página, WhatsApp | Copy Squad / Copy Master (e `PADRAO-COPY.md`) |
| Campanha de Meta/Google Ads | Pedro Sobral, Traffic Masters |
| Mensagem da marca, posicionamento | Donald Miller, Brand Squad |
| Identidade visual, artes, design system | Design Squad, Brand Squad |
| Roteiro, história, apresentação | Storytelling |
| YouTube e canais dark | Peter (e Tom Breeze para anúncio no YouTube) |
| Métricas, retenção, relatório | Data Squad, Hormozi Retention |
| App, Central, automação | Builder Squad |
| Negociação | Chris Voss, Maquiavel |
