# Raposa e Leão · 10 carrosséis v1 (Designer gráfico, conta Zuleide, 18/11/2026)

**Situação: aguardando aprovação do Lindson.** Capas com obra do acervo; quando o Lindson mandar os fundos do Gemini (`PROMPTS-GEMINI.md`), trocar só a capa.

Texto: `produto/fonte/conteudo.py` (citação idêntica; só cena e caso encurtados para caber). Estrutura: `redes-sociais/LINHAS-EDITORIAIS-CARROSSEIS-v2.md`. Modelo copiado: capas v2 Economist 2027 (aprovadas). Pesquisa: `TEMPLATE.md`. Obras: `../../FOTOS-USADAS.md`.

| Carrossel | Linha | Pauta | Capa |
|---|---|---|---|
| c01 | L1 Ler o jogo | S02 Todo mundo julga você pela vitrine | Castiglione (Rafael) |
| c02 | L7 Ele nunca disse isso | F1 "Os fins justificam os meios" (carimbo NÃO EXISTE, isca "comenta FONTE") | César Bórgia |
| c03 | L2 Carreira e comando | S07 Ser querido ou ser respeitado | Busto de Aníbal |
| c04 | L8 A pergunta do Príncipe | P01 A verdade efetiva (texto de S01, Príncipe XV) | Maquiavel (Santi di Tito) |
| c05 | L4 Aliados e traição | S16 Você ajudou alguém a subir | Júlio II (Rafael) |
| c06 | L2 Carreira e comando | S08 A notícia ruim que você precisa dar | Busto de Caracala |
| c07 | L5 Rivais e conflito | S25 O atalho sujo que funciona | A Prisão de Cristo (Caravaggio) |
| c08 | L3 Dinheiro e negociação | S12 Do outro lado da mesa tem um arrogante | Busto de Júlio César |
| c09 | L5 Rivais e conflito | S23 Estão falando de você pelas costas | Savonarola (Fra Bartolomeo) |
| c10 | L6 Fortuna e domínio próprio | S27 A culpa é da sorte | Um naufrágio (Vernet) |

8 telas 4:5 (2160×2700): 1 capa · 2 a cena · 3 o texto (pergaminho) · 4 no livro (dossiê) · 5 lance I (numeral + lupa) · 6 lances II e III (faixa + checklist) · 7 o freio (a única tarja) · 8 fecho (retrato + mockup do manual). Cada pasta `cNN/` tem as 8 telas, `prancha.jpg` e `LEGENDA.md`.

## Como rodar
```
python3 gerar.py            # pecas.html (prepara as obras em _img/, que fica fora do git)
node render.js              # todas as telas  ·  node render.js c03-01  = só a capa do c03
python3 prancha.py          # pranchas
python3 legendas.py         # LEGENDA.md
```
As obras do acervo (`img/acervo/*.jpg`) não vão para o git: baixe com `motor/acervo_wga.py` (Web Gallery of Art) e, as do SMK, pela API aberta `api.smk.dk` (número da obra no `creditos.json`).

**Fundo Gemini:** salve como `fundos/cNN-capa.jpg` e rode `python3 gerar.py && node render.js cNN-01 && python3 prancha.py`. A capa troca de imagem e passa a mostrar "imagem gerada por IA".

## Pendente
- Lindson: aprovar; gerar as 10 capas no Gemini (opcional); link da Hubla do manual e lugar da isca (fecho do c02).
- Capturas que os sites bloquearam (The School of Life, Penguin/David Pearson, Criterion, The Economist): ver `TEMPLATE.md`.
