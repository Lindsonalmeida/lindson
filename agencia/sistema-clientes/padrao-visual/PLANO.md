# Plano · padrão visual Apple na Central (conta Leandro, 11/11/2026). Ainda NÃO aplicado.

Base: `template/` (tokens.css + componentes.css + demo.html). Regra: tela nova ou mexida só usa essas classes; nada de estilo inline nem emoji.

1. **Base comum** · `prototipo/painel.html` passa a carregar tokens.css + componentes.css; a biblioteca de ícones SVG (sprite único, traço 1.5) substitui todos os emojis e os ícones repetidos (cada item do menu com ícone próprio). Atinge todos os painéis de uma vez, porque todos saem do modelo.
2. **Admin** · barra lateral de vidro (estilo Ajustes do macOS) com busca; Visão geral com cabeçalho de data + título, 4 números (só os que não estão zerados ganham destaque), lista "Feitos hoje" e "Esperando você"; clientes vira tabela (Instagram, pedidos, última entrega) em vez de cartões iguais. Sai "XP/pontos" da tela principal.
3. **Quadro de atividades** · segmento iOS (A fazer, Com você, Com cliente, Equipe, Feitos); Feitos em lista agrupada por dia com hora mono e selo; `admin-quadro.js` sem `style=""`.
4. **Painéis de clientes (jaci, leo, rt, sf, oregano, tribuna, wf)** · mesma estrutura e componentes; a cor do cliente entra só no token `--c-acento` e na marca do topo (Jaci vinho, Leo azul, Orégano verde…). Corrige o topo azul do Orégano. "a medir" vira estado vazio desenhado ("Mande o print do Instagram").
5. **Textos** · glossário: "fila" → "pedidos", "XP" → sai, "a confirmar" → sai, "claude.ai" → "abre em outra aba"; nomes únicos dos clientes (Dra. Jaci Cunha, Leo Pinto, Real Time, Curso legislativo…) num só lugar (`NOMES`).
6. **Recomeço 90** · mesmos tokens e 1 família (Inter); mantém o jogo (é a proposta do app), sem emoji e sem 5 fontes.
7. **Central de Comando / VEKTOR** · mantém o visual futurista aprovado; só harmoniza: Inter no lugar de Manrope, mesmos cinzas e amarelo, toasts e modais do template, sem sobrepor avisos no 390.
8. **Conferência** · captura 1440 e 390 de cada tela, lado a lado com `capturas-antes/` e com a demo; Lindson aprova antes de publicar.
