# Manual de Campo · produto digital do Raposa e Leão

Conta Pedro, 14/11/2026. Pedido do Lindson: "crie um produto digital pro raposa e leão. verifique todos os agentes e veja o que dá pra fazer". **Situação: aguardando aprovação.**

## O que é
- **Produto:** *Manual de Campo* — PDF 4:5 de 50 páginas: 30 situações de poder (trabalho, negócios, vida), cada uma com a cena, o texto de Maquiavel em italiano e português com obra e capítulo, o caso do livro, 3 passos ("o lance") e o limite ("o freio"). Ferramentas: 13 perguntas do Príncipe, folha de decisão para imprimir, O Príncipe em 26 linhas, 7 frases falsas. Fontes e créditos no fim.
- **Isca grátis:** *7 frases que Maquiavel nunca disse* — PDF de 11 páginas, para a descrição e o comentário fixado.
- **Preço sugerido:** R$ 37 (faixa R$ 19-37 do `agencia/ofertas/low-ticket/hormozi.md` 12.1; mesmo preço do Passaporte da Bíblia). Decisão do Lindson.
- Sem nome do Lindson no produto (ficção do canal). Imagens: obras em domínio público do acervo do canal.

## Arquivos
| O quê | Onde |
|---|---|
| PDF do manual (15 MB) | `entrega/Raposa-e-Leao-Manual-de-Campo.pdf` |
| PDF da isca (2 MB) | `entrega/7-Frases-que-Maquiavel-Nunca-Disse.pdf` |
| Página de venda (HTML único, `{{PRECO}}`, `{{CHECKOUT}}`, `{{LINK_ISCA}}`) | `venda/index.html` + `venda/img/`; prévias `venda/previa-celular.jpg`, `previa-desktop.jpg` |
| Capa Hubla horizontal 1640x880 | `venda/img/capa-hubla.jpg` |
| Mockup quadrado | `venda/img/mockup.jpg` |
| Kit de lançamento (fixado, descrição, CTA de longo, 3 Shorts) | `lancamento/KIT.md` |
| Consulta aos agentes e decisão | `CONSULTA-AGENTES.md` |
| Pesquisa premium e persona | `TEMPLATE.md`, `referencias/` |
| Conteúdo (texto) | `fonte/conteudo.py` |
| Gerar de novo os PDFs e prévias | `python3 fonte/gerar.py` (prévias em `fonte/previa/`) |
| Conferir as citações | `python3 fonte/conferir.py` (37 trechos contra `conteudo/referencias/maquiavel/revisao/citacoes-tabela.tsv`: 0 falhas) |
| Capas e prints da página | `python3 fonte/mockup.py`, `python3 fonte/shot.py` |
Cópia da página no privado: `CentralLindsonALmeida/produtos/landing/raposa-e-leao/` (mesmo modelo das outras landings).

## Como publicar na Hubla (o Lindson faz)
1. Hubla → Produtos → Novo produto → "Raposa e Leão · Manual de Campo", tipo produto digital, pagamento único.
2. Capa: `venda/img/capa-hubla.jpg`. Preço: decidir (sugestão R$ 37). Pix e cartão.
3. Entrega: área de membros com uma aula "Baixe o seu manual" e o PDF anexado (não como link externo).
4. Copiar o link do checkout e trocar `{{CHECKOUT}}` e `{{PRECO}}` em `venda/index.html` (ou pedir a qualquer conta).
5. Isca: subir o PDF da isca (Hubla produto grátis, ou e-mail/WhatsApp) e trocar `{{LINK_ISCA}}` no `KIT.md` e na página. Pôr o link de venda em `LINK_VENDA` no `fonte/gerar.py` e gerar a isca de novo.
6. Fixar o comentário e colar o bloco da descrição (`lancamento/KIT.md`).

## Depende do Lindson
Aprovar o manual e a isca; preço; criar o produto na Hubla e mandar o link; onde a isca será entregue; confirmar se quer o canal (não o nome dele) como vendedor na Hubla.

## Verificado × não verificado
- Verificado: as 37 citações em italiano (programa), cada página dos PDFs olhada (sem transbordo, checagem automática), página em 390 px e 1440 px sem rolagem lateral.
- Não verificado: taxas e regras atuais da Hubla e do YouTube (link em Short), traduções brasileiras publicadas de O Príncipe.
