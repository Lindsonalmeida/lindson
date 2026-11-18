# Site do Manual de Campo · v2 (sessão especialista Raposa e Leão, conta Zuleide, 18/11/2026)

Substitui a página `venda/index.html` (v1, conta Pedro), que está no ar em lindsonalmeida.pages.dev/produtos/landing/raposa-e-leao/ mostrando "{{PRECO}}" cru.

- **Prévia:** https://claude.ai/artifact/68nQmAkcw3mytAUQGQTWzN (o botão de baixar o PDF grátis só funciona no site publicado).
- **Composição:** Stripe Press (página escura, rótulos espaçados, livro 3D), Folio Society (pintura em tela cheia), Antofágica (clássico com obra de arte). Pesquisa completa do produto em `../TEMPLATE.md`.
- **Mudanças da v2:** pinturas em tela cheia (hero, cena, terrenos, fim), faixa rolando com as 30 situações, página real anotada (a anatomia), 9 páginas para folhear, carimbos das frases falsas, guia grátis baixável direto no site (resolve a entrega da isca), isca fora da lista "incluso", sem "{{...}}": `CFG` no fim do HTML. Preço ou checkout vazio = preço some e todo botão vira "Baixar o guia grátis".
- **Para vender:** preencher `const CFG = { preco: "R$ 37", checkout: "https://pay.hub.la/..." }`.
- **Publicar (sem o nome Lindson no link):** criar o repositório `Lindsonalmeida/raposaeleao`, liberar o app Claude, Cloudflare Pages → `raposaeleao.pages.dev`. Copiar esta pasta inteira para a raiz.
