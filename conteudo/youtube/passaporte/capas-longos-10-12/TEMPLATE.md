# Capas dos longos 10 a 12 · pesquisa premium e composição copiada

Pedido do Lindson (09/11/2026, conta Zuleide, Peter): "as novas capas, faça no estilo novo também, das nossas pesquisas de designer".
Exceção à regra "só `capas2.py`", **só para os longos 10 a 12**. As capas aprovadas do `capas2.py` (A, B e C) continuam como alternativa no teste A/B/C do YouTube ("Testar e comparar").

- Gerador novo: `motor/capas_estudo.py` → `capas/v2/<id>-N.jpg` (fora do Git) e a prévia `capas-longos-10-12/previa-capas-10-12.jpg` (à esquerda a nova, à direita a A aprovada).
- Gerador aprovado: `python3 motor/capas2.py longo-10 longo-11 longo-12` → `capas/v2/<id>-A/B/C.jpg`.
- **Status: aguardando aprovação do Lindson.**

## Persona (5 linhas)
1. Cristão brasileiro, católico ou evangélico, de 25 a 60 anos, que quer ler a Bíblia e trava.
2. Vê YouTube no celular, à noite ou no intervalo; decide o clique em menos de 1 segundo.
3. Dor: "leio e não entendo"; desconfia de vídeo sensacionalista ou com cara de IA.
4. Confia em arte clássica, referência bíblica e tom sério e acolhedor.
5. Clicaria numa capa que mostra uma cena da Bíblia e aponta um detalhe que ele nunca reparou.

## Referências (10, de 7 países)
Os links são dos canais e estúdios. **Não conferido nesta sessão:** a busca da web não trouxe as páginas, e o YouTube não abre por robô aqui. Por isso não há capturas salvas e nenhum número de inscritos é citado.

| # | Referência | País | O que tem | Situação |
|---|---|---|---|---|
| 1 | **Johnny Harris** (youtube.com/@johnnyharris) | EUA | Foto ou mapa com **uma anotação à mão** (círculo, seta e nota) mostrando o detalhe da história | **ESCOLHIDA** |
| 2 | **Fall of Civilizations**, Paul Cooper (youtube.com/@FallofCivilizations) | Reino Unido | Pintura de ponta a ponta, sem moldura, com **título serifado em caixa alta**, curto e grave | **ESCOLHIDA** |
| 3 | **Veritasium** (youtube.com/@veritasium) | Austrália/EUA | **Um único foco**, até 3 palavras, imagem clara e limpa | **ESCOLHIDA** |
| 4 | BibleProject (youtube.com/@bibleproject) | EUA | Ilustração autoral, quase sem texto | descartada: exige ilustração própria e foge da gravura de Doré |
| 5 | Kurzgesagt (youtube.com/@kurzgesagt) | Alemanha | Vetor chapado e colorido | descartada: estilo vetorial, sem ligação com a pintura clássica |
| 6 | Epic History (youtube.com/@EpicHistoryTV) | Reino Unido | Pintura histórica com título bold e vermelho | descartada: vermelho (hipótese do Peter: confunde com "já assistido") |
| 7 | Nota Bene (youtube.com/@NotaBeneMovies) | França | Pintura histórica com o rosto do apresentador | descartada: depende de rosto, e o canal é dark |
| 8 | História em Meia Hora (youtube.com/@HistoriaEmMeiaHora) | Brasil | Imagem histórica com texto amarelo gigante | descartada como nova: é o que o `capas2.py` já faz (fica como B) |
| 9 | The AI Bible / Pray.com | EUA | Épico gerado por IA, azul-petróleo e laranja | descartada: estética "Marvel de videogame", criticada (ver `pesquisa/biblia-estilos-video.md`) |
| 10 | Academia Play (youtube.com/@AcademiaPlay) | Espanha | Pintura clássica com recortes e setas | descartada: recorte de figura em gravura P&B serrilha; ficou só a ideia da seta, pela ref. 1 |

## O que cada capa copia
- **Da ref. 1 (Johnny Harris):** um círculo amarelo feito à mão em volta do detalhe, uma seta e uma nota manuscrita (Caveat, a fonte de anotações do canal) com a pergunta do vídeo: "e ele dormia?", "livres… e quiseram voltar", "cadê o cavalo?". Isso conversa com o roteiro, porque cada vídeo ensina a "olhar o detalhe".
- **Da ref. 2 (Fall of Civilizations):** a gravura de ponta a ponta e o título em serifa clássica (Cinzel 900) em caixa alta, embaixo à esquerda, sobre um degradê escuro só na base.
- **Da ref. 3 (Veritasium):** um foco por capa, título de 2 ou 3 palavras e imagem clara (brilho +32% sobre a cor de cinema do `capas2`).
- **Mantido da identidade do Passaporte:** a gravura de Doré com a cor de cinema do `capas2.py` (função `grade`), "PASSAPORTE DA BÍBLIA" em Special Elite, a etiqueta ciano da série e a palavra-chave em amarelo. Nada de vermelho.

| Vídeo | Nova (N) | Aprovadas (capas2) |
|---|---|---|
| longo-10 Milagres | gravura 064 (tempestade), círculo no barco, "e ele dormia?", NÃO ERA **SHOW** | A NÃO ERA SHOW · B FICA CALADO · C MAR vs TÚMULO |
| longo-11 Êxodo | gravura 019 (o cesto no Nilo), círculo no cesto, "livres… e quiseram voltar", POR QUE **VOLTAR?** | A POR QUE VOLTAR? · B TIRADO DAS ÁGUAS · C EGITO vs DESERTO |
| longo-12 Paulo | gravura 095 (a luz no caminho), círculo em Saulo, "cadê o cavalo?", ELE **PERSEGUIA** | A ELE PERSEGUIA · B 3 NAUFRÁGIOS · C PERSEGUIDOR vs APÓSTOLO |

## Conferência
- Legível no celular: o título tem 112 px de altura de letra em 1280×720 e a nota tem 64 px.
- Só no círculo da longo-11 a nota passa perto das figuras. Se o Lindson achar poluído, a nota sai e ficam o círculo e o título.
- Teste sugerido no YouTube: N contra A (e C, se houver 3 slots), por 2 semanas, ganhando a de maior tempo de exibição.
