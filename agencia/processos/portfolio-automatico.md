# Portfólio automático (regra do Lindson, 05/11/2026 · conta Pedro)

"Sempre que eu fizer algo novo, adicione automaticamente ao meu portfólio." Vale para todas as contas.

1. Ao terminar qualquer entrega (site, arte, carrossel, vídeo, motion, app, painel, PDF, identidade, produto, canal), acrescente um cartão no array do portfólio em `CentralLindsonALmeida/site/assets/dados.js` (repositório privado): título, cliente, categoria, o que foi feito, imagem ou vídeo curto de boa qualidade (em `site/assets/`) e link "Ver no ar" quando for público.
2. Commit e push no `main` do privado: o site atualiza sozinho em https://lindsonalmeida.pages.dev/site/portfolio/
3. Não entra: o que o Lindson ou o cliente reprovou, dado pessoal (CPF, contrato, telefone de cliente do cliente, leads, logins), `{{PRECO}}`, nada que critique a prefeitura (Leo Pinto é situação). Em dúvida, pergunte ao Lindson.
4. Cite a entrega no `REGISTRO-DAS-CONTAS.md` como sempre, com "portfólio: ok".

O agente do site pode deixar um script de apoio em `site/` (ver README do site, `agencia/marca-lindson/site/README.md`).

## Script de apoio (conta Pedro, 05/11/2026)
Na raiz do privado `CentralLindsonALmeida`:
```
node site/novo-trabalho.js --nome "Cliente X · site" --cliente "Loja de roupas" --cat sites \
  --faz "Mini site da bio com catálogo" --img caminho/da/imagem.jpg --url https://clientex.pages.dev [--largo]
```
- `--cat`: sites, marca, instagram, video, youtube, apps, produtos ou estrategia (o filtro aparece sozinho na página).
- A imagem é copiada para `site/img/pf/<id>.<ext>` (use print em alta, 1000 a 1600 px, ou a arte aprovada). Vídeo vertical já em `site/media/`: `--video nome-sem-mp4`.
- O trabalho entra no topo da lista. Depois: `git add site && git commit && git push`.
