# Barzakh · fixados v4 · crivo do time (conta Leandro, 21/11/2026)
Arquivos lidos: `.claude/agents/social-media.md`, `designer-grafico.md`, `maquiavel.md`, `REGRAS-GERAIS.md`, `conferencia-imagem-ia.md`, `BARZAKH-ESTADO.md`, `brand.json`. Os agentes Xquads (Donald Miller, brand-chief, copy-chief) NÃO estão instalados neste contêiner (procurei em todo o disco): a revisão deles abaixo aplica o método publicado (StoryBrand SB7, sistema de marca, clareza de copy), não o arquivo do agente.

| Agente | Contribuição | Nota |
|---|---|---|
| Social media (lidera) | 3 fixados = funil (01 conceito, 02 entrega, 03 contato); ordem de postar 03→02→01; legendas blog SEO com CTA WhatsApp; ritmo de 9 posts em xadrez | 9 |
| Designer gráfico (executa) | painel único 3240×1440 com 1 foto real; frase contínua sem texto na divisa; óculo atravessa a divisa 01/02 como herói; composição de John Pawson + Landor/Koto + Kinfolk | 8,5 (resolução, abaixo) |
| Donald Miller (one-liner) | cliente é o herói: "A passagem da SUA marca"; plano em 3 passos no post 03; CTA direto. Corrigido: post 02 dizia só "Identidade visual", virou "Marca · Sistema · Aplicações" | 9 |
| Brand squad | paleta e fontes do brand.json; símbolo vetorial plano sem redesenho. Corrigido: ouro sobre a luz marfim tem contraste 1,76 (proibido no brand.json), então o símbolo dentro do óculo vai em Obsidiana, recortado contra a luz | 9 |
| Copy squad | frase curta, sem promessa, sem preço ("valor fecha na conversa"); hashtags variadas (tema + nicho + local) | 9 |
| Maquiavel (confere) | nada reprovado repetido (sem chapado, sem render de produto, sem rosto, sem motion). Aprova o caminho; segura a postagem até a foto em alta | ver pendências |

## Conferência das imagens (8 critérios, zoom em 01, 02, 03 e painel)
1-5 lógica/olhar/fixação/anatomia/geometria: ok (foto real de arquitetura, sem pessoas, sem montagem). 6 texto falso: ok. 7 mensagem em 1 s: ok (luz + símbolo + "A passagem da sua marca"). Frase alinhada na mesma linha de base nos 3 posts, nada cortado, margens 80 px das divisas: ok.
**8 resolução: ERRO.** A foto disponível tem 1920 px; o painel pede 3240 → ampliação 1,69× (limite 1,5×). O Wikimedia respondeu 429 em todas as 40 tentativas (21/11) para os originais de 4752 px (Panteão Sunbeam) e 5524 px (Siq). Por isso esta versão é PRÉVIA para aprovar o caminho, não para postar.

## Pendências (ditas, não escondidas)
- Trocar a foto pelo original em alta: rodar `gerador/tratar.py <original> foto.jpg 0.5 0.36 1` e `gerador/compor.py foto.jpg .. 740 460 <x do óculo> '#0E0F12'` quando o Wikimedia liberar, ou com a imagem do Gemini (`PROMPT-GEMINI.md`).
- Risco de "escuro": o feed v1 foi reprovado por "morto". Aqui a luz do óculo é o centro, mas é um painel escuro; a opção B (mar) é mais clara porém tem navios cortando o símbolo e tom sépia, ficou em segundo.
