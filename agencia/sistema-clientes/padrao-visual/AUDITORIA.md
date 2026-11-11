# Auditoria visual "não parecer vibe code" (conta Leandro, 11/11/2026)

Capturas "antes" (1440 e 390, cópia local com fetch simulado): `capturas-antes/` (28 imagens: admin-inicio, admin-quadro, admin-clientes, admin-rede, admin-repetidos, jaci, leo, rt, sf, oregano, tribuna, wf, comando, recomeco).

## Números (contagem no HTML no ar, 11/11)
| Tela | estilos inline | emojis | cores hex diferentes | fontes | gradientes | tamanhos de letra | raios diferentes |
|---|---|---|---|---|---|---|---|
| admin | 268 | 157 | 43 | Big Shoulders + Manrope + IBM Plex Mono | 10 | 13 | 10 |
| jaci | 144 | 215 | 27 | Montserrat + Cormorant | 10 | 10 | 12 |
| leo | 128 | 137 | 27 | Montserrat | 11 | 10 | 10 |
| rt | 137 | 83 | 28 | Geist + Geist Mono | 9 | 10 | 11 |
| oregano | 136 | 148 | 30 | Montserrat | 10 | 10 | 12 |
| sf / wf / tribuna | 136 / 110 / 18 | 12 / 11 / 3 | 25 / 20 / 23 | 1 a 2 | 10 a 13 | 9 a 10 | 10 a 11 |
| comando | 24 | 6 | 51 | Anton + Manrope + JetBrains Mono | 20 | 14 | 4 |
| recomeco | 16 | 67 | 34 | 5 famílias | 8 | 12 | 11 |

## Os problemas, do pior para o menor
1. **Emojis como ícones** (857 no total): ☀ no "Bom dia", 👏 em "Tudo feito aqui" (admin-quadro), 🔥👑🏅 nas missões de todos os painéis, 🍕 no Orégano, 🚀📊 no Recomeço. É o sinal nº 1 de "feito por IA".
2. **Cartões todos iguais**: admin-inicio e admin-clientes são grades de cartões com a mesma borda, o mesmo tamanho e o mesmo peso (4 KPI + cartões de cliente idênticos); não há tela com lista, tabela ou hierarquia (capturas `admin-inicio-1440.jpg`, `admin-clientes-1440.jpg`).
3. **Sem escala**: 43 cores, 13 tamanhos de letra e 10 raios no admin; estilos inline em 268 lugares (ex.: a aba Feitos do quadro é toda `style="..."` em `site/admin-quadro.js`).
4. **Tipografia misturada**: título condensado em caixa alta (Big Shoulders) + corpo Manrope + mono; Recomeço com 5 famílias; cada cliente com a sua (aceitável na marca do cliente, não na estrutura).
5. **Gamificação e textos técnicos para o usuário**: "0 XP", "Pontos de hoje", "Ver missões", "fila", "Rec", "P/ VOCÊ", "Os apps abrem no claude.ai, com a conta indicada", "a confirmar"; números "a medir" gigantes no Orégano 390 (`oregano-390.jpg`) parecem erro.
6. **Estados vazios sem desenho**: "Nada pendente. Tudo em dia!" numa caixa cinza solta; KPIs com 0 em destaque (Pedidos 0, Ajustes 0, Fotos 0) dominam a tela inicial.
7. **Nomes inconsistentes**: "Clínica Dra. Jaci Cunha" / "Dra. Jaci Cunha"; "Vereador Leo Pinto" / "Leo Pinto"; "Curso de processo legislativo" / "Curso legislativo"; "Canais dark" é título da aba e de um cartão; o card "Recomeço 90" e o menu "Recomeço 90 · Funil e leads".
8. **Ícones repetidos**: a mesma seta ↗ para todos os clientes; o mesmo ícone de Instagram para Visão da rede, Minhas fotos, Artes, Fábrica e Legendas; o funil para Gerador de propostas e Relatório.
9. **Resto de outro cliente**: topo do Orégano em azul-marinho (herdado do painel SF; o gerador troca só 5 cores).
10. **Excesso de gradiente e brilho**: 10 a 20 gradientes por tela; faixa amarela de "NOVO · PEÇA TUDO AQUI" com borda brilhante; no 390 o Comando tem aviso, balão e toast sobrepostos (`comando-390.jpg`).
11. **Falta de hierarquia no celular**: cabeçalho de 3 linhas, KPIs de 2 colunas com números quebrando ("a / medir"), menu ☰ como emoji.
