# Dossiê político (padrão Francisco Messias) · conta Leandro, 24/11/2026
Lindson, 24/11/2026: "Sempre vamos fazer todos no mesmo estilo." Todo dossiê de vereador/político segue o do Francisco Messias:
PDF 26 p. 16:9 (1600×900), grafite + 1 acento (cor do partido), Anton + Archivo + IBM Plex Mono, grid, números enormes, mapa esquemático, rede de alianças, gráficos de barra com rótulo direto.

## Onde está o modelo (repo privado CentralLindsonALmeida)
- Gerador parametrizado: `dados/clientes-arquivos/fabiano-fuba/` (`gerar.py` + `dados.json` + `estilo.css` + `render.js` + `mont.py`).
- Original: `dados/clientes-arquivos/francisco-messias/` (gerar.py com o texto embutido).

## Como gerar um dossiê novo
1. `cp -r dados/clientes-arquivos/fabiano-fuba dados/clientes-arquivos/<novo>` e apague PDF, prévia, fotos e material antigos.
2. Ponha a pesquisa da extensão em `<novo>/material/` e as fotos públicas em `<novo>/fotos/` (Câmara/SAPL, notícias, prints; fonte no README; ampliação ≤ 1,5×; recorte com rembg).
3. Edite `dados.json`: `titulo`, `pdf`, `rodape`, `acento` (+ `acento_escuro`, `acento_rgb`), `whatsapp`, `barras` e as 26 `paginas` (mesma ordem e seções). No html: `[[bar:CHAVE]]` = gráfico; `{{A}}` = cor de acento.
4. `python3 gerar.py && NODE_PATH=/opt/node-tools/node_modules node render.js` · prints: `node render.js 1,13 <pasta>` · prévia: `python3 mont.py <pasta> 1,6,10,12,13,22 previa.jpg`.
5. Conferir capa, meio e fim com zoom e cada número contra a pesquisa (conta no rodapé).

## As 26 seções
capa · resumo · quem é · trajetória e bens · linha do tempo eleitoral · votos em números · mapa da base (esquemático) · mandato · produção/pautas · alianças · contexto 2028 · pesquisa ou caso-chave · diagnóstico (% canais) · nota por canal · raio-X Instagram · concorrentes · lacunas · passivos ("o que os adversários vão usar") · SWOT · cenários · simulação 2028 · 4 fases da assessoria · metas e calendário · por que agora · provas e fontes · contato (WhatsApp (98) 98562-1808, "estrategista de comunicação política").

## Regras
Só dados da pesquisa, com fonte; notas = "avaliação da equipe" com critério; votos 2028 = "simulação"; mapa = "esquemático"; sem promessa de voto, sem preço, sem nota interna; passivos com fonte e lado e "sem condenação definitiva"; fotos só de fonte pública, sem login.
- 24/11/2026 · Rafael Campaner (Leandro): dossiê v1 no gerador do Fubá, acento ciano PP #0096D6, pasta privado dados/clientes-arquivos/rafael-campaner/.
