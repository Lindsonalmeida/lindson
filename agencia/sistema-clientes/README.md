# Central do Cliente · sistema multi-cliente do Lindson Almeida

Um painel único para todos os clientes da agência. O Lindson (admin) vê tudo, e cada cliente vê só o próprio painel. Este README é o ponto de partida para qualquer equipe ou conta que for continuar o projeto.

- **Status:** protótipos prontos da tela de acesso e do painel interno (v1 geral, com dados de exemplo). O login de verdade e o servidor ainda não foram construídos.
- **Painel interno (v1):** https://claude.ai/artifact/RJrQcfyPeML9AwT5YMGbBZ · código em `prototipo/painel.html` (arquivo único, sem imagens).
- **Protótipo publicado:** https://claude.ai/artifact/XjCkj5eULmE2Pg8KptnKcV
- **Histórico de pedidos e decisões do Lindson:** `IDEIAS.md` (leia antes de mudar qualquer coisa).

## Estrutura
| Caminho | O que é | No Git? |
|---|---|---|
| `IDEIAS.md` | todas as ideias e decisões, em ordem | sim |
| `prototipo/login.html` | código da tela de acesso, com marcadores `__NOME__` no lugar das imagens | sim |
| `prototipo/painel.html` | painel interno v1: visão geral, resultados, relatórios, aprovações, calendário, entregas, campanhas, leads, pedidos, reuniões, contrato e pagamentos | sim |
| `prototipo/montar.sh` | embute as imagens e gera `prototipo/central-lindson.html` | sim |
| `fotos/casos/*.webp` | prints dos mini sites dos clientes e capas dos canais (portfólio) | sim |
| `fotos/rec-68.webp`, `principal-cine.webp`, `principal-prof.webp` | foto do Lindson recortada, tratada e mapa de profundidade | **não** (dado pessoal: peça ao Lindson) |
| `privado/codigos-acesso.json` | códigos de acesso de cada cliente | **não** (segredo) |

## Como montar a tela
```bash
cd agencia/sistema-clientes/prototipo && bash montar.sh   # gera central-lindson.html
```
Sem as fotos pessoais, o script para com erro. Coloque as fotos em `fotos/` com os nomes acima. Como gerá-las:
- **Recorte:** `rembg`, modelo `u2net_human_seg`.
- **Tratamento de cor e luz de contorno:** script documentado no histórico.
- **Profundidade:** Depth Anything V2 (ONNX).

## Identidade (decidida pelo Lindson)
- **Visual:** sóbrio, premium, só **preto e amarelo** (`#09090A`, `#F5C518`). Fontes: Big Shoulders Display (títulos), Manrope (texto) e IBM Plex Mono (rótulos).
- **Lado esquerdo:** vitrine que passa sozinha para o lado a cada 7 s.
  1. A foto principal do Lindson, centralizada, com efeito 3D, luz dourada e o nome.
  2. Clientes e projetos, um por página, cada um com **"O que é"**, **"O que fizemos"** e **materiais produzidos**.
- **Fundo animado** (grade, rede, gráfico, ícones de redes e vendas) em toda a vitrine.
- **Botão "Quero contratar"** para o WhatsApp do Lindson (98) 98562-1808, com mensagem pronta.
- **O que o Lindson achou amador e não quer:** abertura com letreiro, várias cópias da foto, montagens com contorno, efeito espacial azul.

## Acesso e códigos
- **Abas "Entrar" e "Criar conta".** No cadastro: nome, e-mail, senha (mínimo de 8 caracteres) e **código de acesso**.
- **O código define qual painel é liberado.** Formato `XXX-XXXX-XXXX`:
  - Apple Black → `APB-…`
  - Dra. Jaci Cunha → `JAC-…`
  - Vereador Leo Pinto → `LEO-…`
- **No protótipo**, a página só guarda o SHA-256 de cada código.
- **No sistema real**, o código precisa ser conferido **no servidor**, com limite de uso e possibilidade de troca. A senha fica guardada com hash forte (bcrypt ou argon2), e toda consulta checa o `cliente_id` no servidor.

## Próximos passos
1. Painel interno (referência visual em `IDEIAS.md` item 6, Efferd dashboard 3): menu lateral, cartões de indicadores e gráficos.
2. Back-end: Cloudflare Workers + D1 (o Lindson já tem a conta conectada).
   - **Tabelas:** clientes, usuários, códigos e registro de acesso.
   - **Regra de acesso:** o perfil "admin" vê tudo.
3. Painel do Vereador Leo Pinto: demandas da população por bairro, atendimentos e redes. Seguir a LGPD, porque são dados de cidadãos.
4. Painéis da Apple Black e da Dra. Jaci Cunha: definir com o Lindson.

Antes de começar a construir, vale usar o **Builder Squad** (`/builder-squad`) para o briefing, a arquitetura e as checagens de qualidade.
