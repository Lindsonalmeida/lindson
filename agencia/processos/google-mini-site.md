# Processo: colocar o mini site do cliente no Google

Reconstruído pela conta Zuleide em 03/11/2026 a partir do que foi feito na Desentupidora SF em 26/10/2026 (histórico do repositório `Lindsonalmeida/GruposSF`). Vale para todo mini site de cliente.

## Parte 1 · No site (o Claude faz)
1. **SEO local:** uma página por serviço e uma por cidade atendida, com título e descrição com a palavra-chave local ("Desentupidora em São Luís MA…"), links internos entre elas e o telefone e WhatsApp em todas. Na SF: 6 serviços + 4 cidades (`gerar.py` no repositório do cliente).
2. **`sitemap.xml`** com todas as páginas e **`robots.txt`** liberando tudo e apontando para o sitemap.
3. **Meta tags:** `index,follow`, canonical com o endereço `pages.dev` do cliente, Open Graph.
4. **Arquivo de verificação do Google Search Console** (método "Arquivo HTML"): o Lindson baixa o arquivo `googleXXXX.html` no Search Console e manda; o Claude coloca na raiz do site.
5. **Regra no `_redirects`** para o arquivo abrir sem redirecionar (a Cloudflare tira o `.html` e o Google não aceita redirecionamento): `/googleXXXX.html /googleXXXX 200`.

## Parte 2 · No Google (o Lindson faz, na conta Google dele)
1. **search.google.com/search-console** → Adicionar propriedade → **Prefixo do URL** → `https://<cliente>.pages.dev/` → método **Arquivo HTML** → baixar o arquivo e mandar ao Claude → depois que ele publicar, clicar em **Verificar**.
2. **Sitemaps** → enviar `sitemap.xml`.
3. **Inspeção de URL** → colar cada página (início, serviços, cidades) → **Solicitar indexação**.
4. **Perfil da Empresa no Google** (business.google.com): nome, categoria, área atendida, telefone, horário, link do site, fotos reais. É o que aparece em "perto de mim" e no Maps.
5. **Bio do Instagram e Perfil da Empresa** com o link do site; pedir **avaliações no Google** a cada cliente atendido.
6. **Acompanhar** em 1 a 4 semanas: Search Console → Páginas (indexadas) e Desempenho (buscas e posição). Mandar print para o Claude analisar.

## Situação dos clientes
| Cliente | Parte 1 | Parte 2 |
|---|---|---|
| Desentupidora SF | feita em 26/10 (Search Console verificado por arquivo) | em 03/11 o site ainda não aparecia nas buscas: falta conferir se o **sitemap foi enviado** e **pedir a indexação**, e criar o Perfil da Empresa |
| Real Time | a fazer quando o site for publicado | a fazer |
