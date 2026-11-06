# Artes com foto do calendário · @oreganoturbo (Paollo, 06/11/2026)

**Pedido:** 5 peças do calendário (`../../calendario.json`) que pediam foto, feitas com o lote novo do Gemini (`../../../../identidade/fotos-ia/hd/`). Cada foto entra **uma vez só** e está registrada em `../../../FOTOS-USADAS.md`. No `calendario.json` (e no `montar_calendario.py` e no `CALENDARIO.md`), o campo "imagem" dessas 5 entradas passou de F3/F7/F10/F12/F15 para o código da foto usada.

**Padrão:** kit v3 aprovado ("AGORA SIM, ESSE É O PADRÃO"). O `gerar_fotos.py` **carrega as funções de marca de `../../../v3/gerar.py`**, do mesmo jeito que `s1-2/gerar_s12.py` e `s3-4/gerar_s34.py`. Recorte com BiRefNet (`recortar.py`, um por processo) para a letra passar **por trás** da pessoa ou do produto.

**Prévia:** `previa-fotos.jpg`.

| Dia | Hora | Formato | Manchete | Foto | Arquivo | Composição |
|---|---|---|---|---|---|---|
| 9 (ter 17/11) | 19h | Feed | SEU CLIENTE SUMIU? | IA:B8a pizzaria vazia | `d09-19h-seu-cliente-sumiu.jpg` | Cartaz de "DESAPARECIDO" colado com fita (cartaz retrô retro-13 + humor pop), com a foto emoldurada; manchete em 2 tamanhos ("SUMIU?" gigante cruzando o cartaz); selo e adesivo; carvão com faixa de xadrez |
| 11 (qui 19/11) | 19h | Feed | DOMINGO É DIA DE PIZZA. TERÇA TAMBÉM. | IA:B7 moça no carro | `d11-19h-domingo-e-terca-tambem.jpg` | Flash com céu azul (Decaf Girl); "TERÇA" gigante POR TRÁS da fatia e da moça; "também." sobre a porta amarela; tira da semana com DOM e TER marcados; estrela |
| 13 (sáb 21/11) | 12h | Feed | PIZZA BOA NÃO VENDE SOZINHA. | IA:B4 cesta | `d13-12h-pizza-boa-nao-vende-sozinha.jpg` | Cesta recortada vista de cima com **anel de texto em volta da pizza**; "PIZZA BOA" por trás da tampa; faixa açafrão girada; verde com padrão |
| 15 (seg 23/11) | 08h | Story | Bom dia, forno aceso. | IA:B8b pizzaria vazia | `d15-08h-bom-dia-forno-aceso.jpg` | **Arco do forno a lenha** como janela da foto, com brilho de brasa; "Bom dia," em script; "FORNO" e "ACESO." gordos; estrela da data e faixa "bora vender" |
| 16 (ter 24/11) | 19h | Feed | PIZZA FRIA NÃO TEM PERDÃO. | IA:B5 motoboy | `d16-19h-pizza-fria-nao-tem-perdao.jpg` | Motoboy de baixo, recortado, sobre raios de cartaz em tomate; "FRIA" gigante azul-gelo por trás dele; tarja carvão girada; selo, estrela "quente na porta" |

## Regras conferidas
- Todas as peças levam "imagem gerada por IA".
- **Sem promessa de resultado.** O d13 repete o apoio do calendário ("quem aparece mais vende mais") como frase de cultura, sem número e sem garantia.
- **Sem preço.**
- **Chamada para o zap** em todas, menos no story de bom dia, que é de cultura e fecha com "bora vender".
- Nenhuma borda cortada da foto aparece dentro da arte. A moça e o motoboy, que são cortados pelo quadro, ficam presos à própria foto ou à borda da arte.

## Como refazer
```
MODELO=birefnet-portrait python3 recortar.py B5-motoboy
MODELO=birefnet-portrait python3 recortar.py B7-moca-carro
MODELO=birefnet-general  python3 recortar.py B4-cesta
python3 gerar_fotos.py && node render.js && python3 previa.py
```
