# Criativos de tráfego · Orégano Turbo (Paollo + Rocco + Sobral/Hormozi, 15/11/2026)
Pedido do Lindson: "crie 10 criativos de alta conversão para o Orégano Turbo. use nossos agentes". Situação: aguardando aprovação.
- 10 ângulos, cada um em 1080x1350 (feed) e 1080x1920 (Stories/Reels): `pecas/`. Prévias: `folha-feed.jpg`, `folha-story.jpg`.
- Textos do anúncio (texto principal, título, CTA, foto e crédito): `criativos.json`. Referências: `TEMPLATE.md`.
- Base visual: kit social v5 (`marca.py` copia os elementos do `social/v5/gerar.py`). Fotos Pexels inteiras em moldura (sem recorte), texto nunca sobre a pizza.
- Cores em sequência: carvão, tomate, verde, creme, carvão, tomate, verde, creme, tomate, verde.
- Refazer: `python3 gerar.py && NODE_PATH=$(npm root -g) node render.js`
- Fotos: `fotos/` (Pexels, licença livre; registradas em `../social/FOTOS-USADAS.md`).

## v2 (15/11/2026): a v1 foi reprovada
O Lindson: "eu quero mais fome, mais imagens, menos cor e fundo sem nada" e "compare com o público".

**Persona:** dono de pizzaria de São Luís, 30 a 55 anos. Fica no forno das 17h à meia-noite e olha o celular à noite, entre um pedido e outro. Para de rolar a tela quando vê pizza que dá fome e reconhece o próprio problema.

- **Arquivos:** `pecas-v2/`, `folha-v2.jpg` e `folha-stories-v2.jpg`.
- **Como refazer:** `python3 gerar2.py && V2=1 NODE_PATH=$(npm root -g) node render.js && python3 folha2.py`.

| Critério (persona) | v1 (reprovada) | v2 |
|---|---|---|
| Para o dedo no feed? | Não: fundo de cor chapada e foto pequena | Sim: a pizza ocupa de 60% a 80% da arte e a foto sangra |
| Dá fome? | Pouco, 1 foto em moldura | Close, queijo esticando, borda e fogo, com luz quente |
| Imagens | 1 por peça | De 1 a 8 por peça (mosaico, sequência, foto dentro da letra) |
| Cor | Tomate, verde e creme no fundo | Base escura ou foto; a cor da marca só no detalhe |
| Fundo vazio | Sim (c06, c09 e c10 no stories) | Não: o fundo é sempre foto |

**Peça por peça:**
- **c01:** Para: o forno aceso e o "salão vazio" é a terça dele, e a pergunta fala com ele.
- **c02:** Para: pepperoni em close dá fome, e "fatia do app" é a conta que ele faz toda noite.
- **c03:** Para: vê 7 fotos de pizza num celular igual ao dele e lembra do próprio feed parado.
- **c04:** Para: 5 fotos de forno, caixa e pizzaiolo, e entende o processo sem ler muito.
- **c05:** Para: cheese pull na tela inteira e o preço claro na comanda (R$ 297).
- **c06:** Para: o "5" feito de pizza e 5 fotos, uma por vaga, mostram a escassez.
- **c07:** Para: fogo em tela cheia e a tabela responde "por que vocês e não a agência do meu primo".
- **c08:** Para: a fatia com cebola é a pizza dele, e a frase é a objeção que ele mesmo diz.
- **c09:** Para: "SÓ PIZZA" com pizza dentro das letras é lido em 1 segundo.
- **c10:** Para: queijo esticando na mão e o nome da cidade dele no título.
