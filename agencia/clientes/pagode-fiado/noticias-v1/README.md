# Pagode Fiado · Notícias do pagode v1 (conta Zuleide, 16/11/2026) · aguardando aprovação
Linha editorial "Notícias do pagode": 1 a 2 por semana, objetivo alcance e salvamento. 8 posts 1080x1350 (01 e 02 em carrossel de 3 telas), 8 composições (A amarelo manchete, B número gigante, C caderno, D moldura verde, E bilhete, F tipografia repetida, G selo redondo, H tarjas). Sem foto de artista (direito autoral): só tipografia e paleta do brand book. Prévia: `grade.jpg`. Legendas: `LEGENDAS.md`.

## Modelo semanal (equipe)
1. Pesquisar notícias reais da semana (Billboard Brasil Samba e Pagode, g1 Música, sites oficiais); anotar fonte e data. Nada sem fonte.
2. Editar `noticias.json`: `tipo` (A–H, nunca dois iguais seguidos), `chapeu`, `big` (até 4 palavras; no tipo H use "Nome + Nome"), `l2` (1 frase), `fonte`, `carrossel` opcional (lista de `{t,x}`).
3. `python3 gerar.py noticias.json artes` → `artes/noticia-NN.jpg` e `grade.jpg`. Abrir a grade e conferir cortes.
4. Legenda: título com palavra-chave, 1 linha, CTA, fonte com data, 3 a 5 hashtags variadas.
Regras: não anunciar show do Pagode Fiado (grupo fictício), não pedir PIX, nada de promessa.
