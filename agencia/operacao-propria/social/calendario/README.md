# Calendário de 4 semanas @oreganoturbo (09/11 a 06/12/2026)

As pautas estão em `CALENDARIO.md` e `calendario.json` (gerados por `montar_calendario.py`) e as legendas em `LEGENDAS.md`. As artes ficam em `artes/`. O painel da Central é montado por `montar_painel.py`.

## v4 · 08/11 · conta Zuleide
O sistema do kit v4 (`../v4/`) e a pesquisa de 08/11 (`../../biblioteca-pizzaria/PESQUISA-08-11-IDENTIDADES-E-SOCIAL.md`) foram levados a todas as artes do calendário. A v3 continua existindo e as referências "v3:arquivo" seguem funcionando.

**Como funciona agora:** `artes/sistema_v4.py` lê as funções de marca do `../v4/gerar.py` sem mexer nele e é carregado pelos 4 geradores (`s1-2`, `s3-4`, `fotos` e o novo `tipo-v4`). Ele aplica:
- **Conceito único, a comanda "PEDIDO Nº":**
  - toda arte tem a sua comanda, com número único na campanha (o kit v4 tem 01 a 12 e o calendário segue de 13 a 84, na ordem de publicação) e a linha editorial embaixo;
  - no render, a comanda procura sozinha o canto mais livre da arte. As peças em que o lugar automático não servia têm o lugar fixado em `POS`.
- **Bagel Fat One em toda manchete:** os títulos em Anton viraram Bagel, com encaixe automático para não estourar a largura. O manuscrito (Kaushan) também saiu. O Anton ficou só nas faixas em loop.
- **Paleta fixa** (tomate, verde, creme e carvão):
  - 8 fundos amarelo-açafrão foram trocados: d03-08h e d16-08h creme, d04-19h creme, d08-08h verde, d22-12h creme, d24-08h verde, d25-12h creme e o quadro amarelo do d28;
  - o "FRIA" azul do d16-19h virou creme.
- **Raio-X sem explosão de preço** (o padrão a evitar da pesquisa):
  - d12-08h virou cartaz escuro, com o preço escrito numa comanda grande;
  - no d24-19h, a estrela "R$297" saiu e o preço foi para a faixa verde, também em cartaz escuro.
- **Grade de 4 cores:** saiu no d28. Agora é uma faixa tomate inteira com SEMANA gigante e dois quadros, TEM e MAIS.
- **Ajustes de sobreposição:**
  - estrela do d17 e selos do d09 e do d16 mudaram de lugar;
  - o LOGO do d05 diminuiu;
  - as listas internas também passaram para Bagel.

**Artes re-renderizadas: 47** (19 em `s1-2`, 23 em `s3-4` e 5 em `fotos`, com as mesmas fotos). Re-renderizar a mesma arte com a mesma foto não é uso novo, por isso nada mudou em `../FOTOS-USADAS.md`.

**Novas tipográficas (`artes/tipo-v4/`, 4 pautas e 6 imagens):** são pautas que esperavam foto e viraram tipografia sem perder força, porque o assunto é a comanda, o método ou o preço, não a comida.
- **d12 12h, "Código em cada pedido" (era F8):** comanda gigante com o código PZ14 (exemplo ilustrativo).
- **d15 19h, "Como funciona em 4 passos" (era F13):** carrossel de 3 telas, com os passos da legenda (Raio-X, gravação, anúncio com código e relatório).
- **d20 19h, "Promoção todo dia cansa" (era F23):** parede de etiquetas de desconto rasgadas. As porcentagens são de exemplo.
- **d27 19h, "Primeiro passo: Raio-X" (era F30):** "1º" gigante e comanda com o preço. A F30 pedia pizza com estrela de preço, o padrão a evitar.

Nas legendas dessas 4, saiu a linha "imagem gerada por IA", porque não há imagem de IA nelas.

**Calendário:**
- `montar_calendario.py` marca as 4 pautas como TIPO e põe em cada peça do kit o campo `v4` (equivalente no kit v4) e o aviso v4 no `CALENDARIO.md`;
- o `PEDIDO-FOTOS-LOTE-2.txt` agora lista só as **23 fotos que faltam**, com as cores da v4 (sem fundo açafrão) e área livre no topo para o texto.

**Painel (`montar_painel.py`):**
- lê também `artes/tipo-v4`;
- quando o Lindson aprovar o kit v4, basta pôr `USAR_V4 = True` para o painel trocar as peças v3 pelas v4;
- não foi rodado, porque o privado `CentralLindsonALmeida` não está nesta máquina. O mapeamento foi testado: nenhum arquivo falta.

**Refazer tudo:**
```
cd artes/s1-2  && python3 gerar_s12.py   && node render.js && python3 previa.py
cd artes/s3-4  && python3 gerar_s34.py   && node render.js && python3 previa.py
cd artes/fotos && python3 gerar_fotos.py && node render.js && python3 previa.py
cd artes/tipo-v4 && python3 gerar_tipo.py && node render.js && python3 previa.py
```

**Pendente:** as 23 fotos do lote 2 (F1, F2, F4, F5, F6, F9, F11, F14, F16 a F22, F24 a F29, F31 e F32), a pedir ao Lindson no Gemini pelo `PEDIDO-FOTOS-LOTE-2.txt`.
