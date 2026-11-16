# Recomeço 90 v2 · TEMPLATE (conta Leandro, 16/11/2026)

Pedido do Lindson: "coloque no formato correto de computador, e crie um outro visual, nunca crie nada parecendo com vibe code".
Persona: o próprio Lindson, no computador (1440-1920 px) e no celular, abrindo todo dia para prospectar e marcar missões. Quer ver em 3 segundos: em que dia dos 90 está, quantos pontos, o que falta hoje.

## Referências (estudo de linguagem; nada copiado)
| # | Referência | País | Reconhecimento | O que se aproveita |
|---|---|---|---|---|
| 1 | **Linear** (linear.app) | EUA/Finlândia | referência de mercado em UI de produto; prêmio não conferido | grade fina, rótulos mono pequenos, aba ativa marcada só por uma linha |
| 2 | **Attio** (attio.com) | Reino Unido | CRM premiado em design (não conferido) | lista de contatos como linhas de tabela finas, sem cartões |
| 3 | **Things 3** (Cultured Code) | Alemanha | Apple Design Award | checklist com respiro, círculo fino que se preenche |
| 4 | Height (height.app) | EUA | não conferido | colunas laterais fixas e centro rolando |
| 5 | Superhuman | EUA | não conferido | atalhos discretos, muito preto, um acento só |
| 6 | Pitch (pitch.com) | Alemanha | não conferido | números grandes e finos como protagonistas |
| 7 | Craft Docs | Hungria | Apple Design Award (não conferido) | tipografia editorial na interface |
| 8 | Al Kántara Group v2 (nosso, aprovado) | Brasil | padrão premium do Lindson | números finos gigantes, linhas finas, um acento |

awwwards.com e Dribbble bloqueiam robô nesta rede: não acessados (sem contornar).

## Escolhidas (3)
1. **Linear**: grade de 12 colunas, abas sublinhadas, rótulos mono.
2. **Attio**: missões, leads e roteiros viram linhas de CRM com faixa lateral de status (amarelo = hoje, vermelho = atrasado, verde = fechado).
3. **Al Kántara v2 / Pitch**: números grandes e finos (Big Shoulders 200) para pontos, dia e Regra dos 100.

## Descartadas
- Bento grid de cartões (é exatamente a "cara de vibe code" reprovada).
- Dashboards com gráfico neon e vidro fosco (fora da marca e pesado).
- Gamificação colorida estilo Duolingo (amador para o público dele).

## O que mudou (só visual e layout; lógica intacta)
- Computador (≥ 980 px): topo com linha do tempo dos 90 dias e 3 fases; esquerda nível, pontos, sequência e fase; centro abas + aba ativa; direita Regra dos 100 e missões do dia (fixas ao rolar).
- Celular: coluna única, mesma ordem de antes, abas roláveis.
- Amarelo só como acento (aba ativa, missão feita, barra de nível). Botões em contorno fino.
- Arquivos: `prototipo/tema-recomeco.css`, `prototipo/recomeco-layout.js`, ligados no `site/montar-site.py`. Capturas em `capturas/`.
