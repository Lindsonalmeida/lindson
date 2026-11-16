# Al Kántara · fase 3: site v2 e site bio (conta Leandro, 16/11/2026)
Continua a v1 da conta Zuleide (`../fase2/site/`).

- `site/`: home, labs, barzakh, media, ventures, cases, sobre, contato (+ `barzakh-oferta/`, cópia da página de venda de `projeto-designer/v3/oferta/pagina/`). Gerador: `python3 gerador/site.py`.
- `bio/`: link da bio do Instagram (mobile-first, OG 1200x630 em `bio/og.jpg`). Gerador: `python3 gerador/bio.py`.
- `previas/`: página inteira em 1440 e 390. Conferência: `NODE_PATH=$(npm root -g) node gerador/shots.js` (rolagem lateral, links internos, erros).
- O que mudou da v1: Studio → Barzakh (ouro, página com a placa e link para a página de venda), cases com mockups reais, manifesto em fundo escuro com contraste, faixa de aplicação (fachada, notebook, celular). Sem número inventado.

## Deploy atual
Copiado para o privado `CentralLindsonALmeida/alkantara/` (site) e `alkantara/bio/` → `lindsonalmeida.pages.dev/alkantara/` e `/alkantara/bio/` depois do commit e push.

## Link próprio (alkantara.pages.dev), se o Lindson quiser
1. No GitHub, conta `Lindsonalmeida`: criar o repositório **privado** `alkantara`, vazio, e liberar o app Claude (All repositories).
2. Avisar: a conta copia `site/` para a raiz e `bio/` para `bio/` desse repositório.
3. Cloudflare → Workers e Pages → Criar → Pages → Importar repositório `alkantara`, branch `main`, framework `None`, build vazio. Link: `alkantara.pages.dev` (bio em `alkantara.pages.dev/bio/`).
4. Depois, trocar `SITE` em `gerador/bio.py` e a imagem OG em `gerador/site.py` para o endereço novo e gerar de novo.
