# LinkCard

Cartão clicável do mini site: ícone, título, subtítulo e seta de avanço.

**Variantes**
- `la-link` (padrão): vidro `panel`, borda `line`, ícone `signal`. Para redes e projetos.
- `la-link--cta`: fundo `sun`, texto `sun-ink`, sombra `glow-sun`. **Só um por página**: o contato principal no WhatsApp.
- `la-link--mini`: borda em gradiente girando (`signal` → `sun` → `violet`), ícone em gradiente e selo `la-badge` "NOVO". Só para a oferta do mini site.

**O que você fornece:** o `href`, um ícone SVG de traço (24×24) dentro de `.la-ico`, o título em `<strong>` e o subtítulo em `<span>`. Empilhe vários dentro de `.la-links` (espaço `space-stack`).

**Faça:** escreva o título como ação ou nome da rede ("Fale comigo no WhatsApp", "Instagram"); use o @ ou uma frase curta no subtítulo.
**Não faça:** dois `--cta` na mesma tela; subtítulos com mais de uma linha.
