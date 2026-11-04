# Dra. Jaci · conteúdos do calendário de novembro/2026 (conta Leandro, 04/11/2026)

Pedido do Lindson (04/11): "use as fotos da jaci e crie todos os conteúdos do calendário que montamos" e depois "crie primeiro só as artes de feed".

- **Calendário:** `../estrategia/LINHAS-EDITORIAIS-NOV.md` (Reels seg/qua/sex/sáb) + 3 datas de `../estrategia/DATAS-COMEMORATIVAS.md` (Novembro Azul, Consciência Negra, Black Friday). Os carrosséis das terças já existem em `../instagram-nov/` (conta Lindson).
- **Feito agora:** 19 artes de feed 4:5 em alta (2160×2700) em `feed/`, uma por conteúdo, com legenda SEO em `TEXTOS.md`. Também no painel dela (Aprovações), com botão Baixar arte.
- **Depois (já escrito, falta gerar):** capas 9:16 dos Reels (`node render.js` sem FEED → `artes/`) e roteiros para gravar (em `TEXTOS.md`).
- **Fotos:** as 36 fotos novas que o Lindson subiu no painel em 04/11 (privado `dados/clientes-arquivos/jaci/fotos-novas/`, melhoradas com Real-ESRGAN em `hd/`), uma foto diferente por arte. Lista em `../FOTOS-USADAS.md`.
- **Composições (nada se cria, tudo se copia):** as 8 dos posts reais dela (`../instagram-estilo/README.md`), as mesmas dos carrosséis de novembro: `balao` ("botox · O QUE NINGUÉM RESPONDE"), `fio` ("Bioestimulador de Colágeno"), `faixa` ("Preenchimento facial… artificiais"), `faixas` ("Entramos na reta final do ano"), `tablet` ("checklist do pós botox"), `frases` ("frases que eu amo ouvir"), `cafe` ("Antes de qualquer procedimento, eu observo"), `invertido` (tríptico "a artista:" em vinho). Nunca a mesma composição em dois posts seguidos.
- **CFO:** sem preço, sem "grátis", sem promessa, sem antes e depois, sem depoimento inventado (as frases das artes são dúvidas comuns ou frases da Dra.; depoimento real só com TCLE), CRO-MA 8514 no rodapé de todas.
- **Gerar:** `python3 textos.py && FEED=1 python3 gerar.py <pasta das fotos> && FEED=1 node render.js`.
