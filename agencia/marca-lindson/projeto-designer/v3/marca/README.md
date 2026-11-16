# Barzakh · um estúdio Al Kántara · marca (conta Leandro, 16/11/2026)

Situação: para aprovação do Lindson.

## O que tem
- `ESTRATEGIA.md` · nome, propósito, posicionamento, manifesto, tom, persona, endosso.
- `TEMPLATE.md` · pesquisa premium + **Referências do Lindson (Behance e Pinterest)** (prioridade) + direção do símbolo "Dois mares" e da variação **monolito**.
- `logos/` · SVG e PNG de todas as versões (horizontal, vertical, símbolo, logotipo, assinatura, avatar e monolito).
- `entregas/barzakh-branding-book.pdf` (16 p.) e `entregas/barzakh-manual-de-marca.pdf` (33 p.), 1920×1080.
- `entregas/paginas/<pdf>/NN.jpg` · cada página em JPG.
- `entregas/elementos.zip` · logos, `paleta.json`, `fontes.txt`.

## Como refazer
```
cd gerador
python3 logos.py <pasta_fontes> ..        # logos principais (só se mudar o desenho)
python3 manual.py                         # monolito + PDFs + JPGs + zip; confere texto cortado
```
`manual.py` copia o modelo da holding (`agencia/marca-holding/gerador/gerar.py`). Fotos em `gerador/fotos/` (originais) e `gerador/trat/` (tratadas).

## Créditos das fotos (Wikimedia Commons)
Roman Aqueduct Segovia night 2012 (CC0) · Detail aqueduct Segovia at dusk (CC0) · Shadows in the colonnade 53700098106 (CC BY 2.0) · Between shadow & light (CC BY-SA 4.0) · Hyogo Prefectural Museum of Art spiral staircase, dllu (CC BY-SA 4.0) · Langen Foundation, Raketenstation Hombroich 2014 (CC BY-SA 4.0) · Monochrome ships on horizon (CC0) · Centro histórico São Luís (CC BY-SA 4.0) · Conference Pavilion Ando Tadao Vitra 2023 (CC0). Nomes completos dos autores: página de cada arquivo no Commons; conferir antes de publicar fora do manual.
