# WF Celulares · mini site da bio (conta Leandro, 10/11/2026) · aguardando aprovação
HTML/CSS/JS puro, sem build. Endereço previsto: https://wfcelulares.pages.dev (OG e canonical já apontam para ele).
- Capturas 390×844 @2x: `capturas/` (`node capturar.js`, que também gera `img/og.jpg` e `img/apple-touch-icon.png`). Pesquisa: `TEMPLATE.md`.
- Imagens: Apple Newsroom (press images), marcadas "Imagem ilustrativa"; fontes em `../artes-02/README.md`.
- Preços da vitrine = os que a loja publicou (artes v2), com "consulte disponibilidade".

## Publicar
1. Lindson cria o repositório privado `Lindsonalmeida/wfcelulares` e libera o app Claude.
2. Copiar para a raiz dele: `index.html`, `favicon.svg`, `_headers`, `robots.txt`, `sitemap.xml` e `img/` (não precisa de `referencias/`, `capturas/`, `capturar.js`, `.md`).
3. Cloudflare Pages: Importar repositório → nome `wfcelulares`, branch `main`, framework None, build vazio.
4. Se o nome vier diferente, trocar `wfcelulares.pages.dev` no `index.html`, `robots.txt` e `sitemap.xml`.

## Falta confirmar
- Endereço exato das 2 lojas (hoje só bairro; botão do Maps faz busca) e horário.
- Prints reais de clientes com autorização para os 2 espaços de prova.
- Se o cliente trocar o @ do Instagram, atualizar o link.
