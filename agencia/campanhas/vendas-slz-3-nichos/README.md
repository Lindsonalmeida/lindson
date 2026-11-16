# Vendas SLZ · advogados, barbeiros e dentistas (conta Leandro, 16/11/2026)
- `ESTRATEGIA-DE-VENDAS.md` · `estrategia-vendas-slz-3-nichos.pdf` (24 p. 4:5) · `folha.jpg` · `paginas/`
- `stories/<adv|barba|dente>/01-10.png` + `folha.jpg` (alterna estilo impacto, ref. Denis Bugatti, e editorial, ref. Gomes & Moura) · `stories/TEMPLATE.md` · `stories/PROMPTS-GEMINI.md`
- Gerar: `python3 gerador/pdf.py <recortes> <fotos_nicho>` · `python3 gerador/stories.py <recortes> <cenas> <fotos_nicho>` · `python3 gerador/prompts.py`. Recortes = fotos c07-c16 (privado `membros/img/`) por `agencia/marca-lindson/ferramentas/recorte2.py`; fotos de nicho/cenas = Unsplash (IDs nos geradores).
- Cenas do Gemini: salvar em `stories/cenas-gemini/<nicho>/NN.jpg` e rodar de novo; o layout troca a composição provisória pela cena.
- Situação: aguardando aprovação do Lindson (preços, data de fundador 15/12, cenas do Gemini).
