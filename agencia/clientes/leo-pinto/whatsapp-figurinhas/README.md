# Figurinhas de WhatsApp · Vereador Leo Pinto (conta Leandro, 05/11/2026)

**Pedido do Lindson:** "Quero 10 figurinhas pra WhatsApp do Léo Pinto. Pense e crie com a melhor estratégia." Agentes: Marketing Squad (estratégia) e Design Squad (peças).

## Persona (quem vai usar)
- **Quem é:** morador de São João Batista e dos povoados, de 25 a 65 anos, nos grupos de família, de povoado, de igreja e de futebol.
- **Rotina:** manda "bom dia" no grupo todo dia, agradece, parabeniza aniversariante e responde com figurinha porque é mais rápido que escrever.
- **O que valoriza:** proximidade, gente da terra, bom humor.
- **Do que desconfia:** propaganda.
- **Teste:** "essa pessoa usaria isso numa conversa normal?" Figurinha com cara de anúncio ninguém reenvia; figurinha útil roda sozinha.

## Estratégia
1. **Utilidade antes de propaganda.** Cada figurinha é uma reação do dia a dia: bom dia, boa noite, obrigado, parabéns, kkkk, tamo junto. Quem usa leva o rosto do Leo para dentro de cada grupo, todo dia, sem ele postar nada.
2. **O rosto é a marca.** Foto real do Leo em 10 expressões diferentes, sem logo nem número. Só as cores e a letra da identidade.
3. **Duas figurinhas da marca do mandato,** sem pedir nada: "Pediu? Tá feito!" (frase do Motion v3 aprovado) e "Me chama no zap!".
4. **Regras do Leo:**
   - situação: nada de cobrar, fiscalizar ou falar de demanda;
   - sem pedir voto, sem número, sem raio, faixa, ícone ou sol;
   - a camisa não tem adesivo de campanha.
5. **Distribuição:**
   - o Leo e a equipe usam primeiro nos grupos;
   - o pacote vai para os grupos de povoado com "fiz umas figurinhas, pode usar à vontade";
   - story do Leo mostrando as figurinhas com o link do pacote;
   - um "bom dia" com figurinha em grupo grande vale mais que um post.

## As 10
| # | Frase | Pose (vem do Motion v1) |
|---|---|---|
| 01 | Bom dia, meu povo! | Close sorrindo, polo laranja |
| 02 | Tamo junto! | Punho erguido |
| 03 | Obrigado! | Mãos juntas, polo laranja |
| 04 | Pediu? Tá feito! | Braços cruzados, polo branca |
| 05 | Me chama no zap! | Celular na mão, apontando |
| 06 | Bora trabalhar! | Punhos fechados |
| 07 | KKKKKK | Mãos juntas rindo de lado |
| 08 | Boa noite! | Close, polo amarela |
| 09 | Conte comigo! | Mãos abertas, polo branca |
| 10 | Parabéns! Felicidades! | Close sorrindo largo |

## Como gerar de novo
- **Fotos:** são quadros dos vídeos do Motion v1 (privado `painel/leo/videos/`), extraídos com ffmpeg e recortados com BiRefNet. Ficam no privado `dados/clientes-arquivos/leo/figurinhas/` (`poses/`, `recortes/`); foto de pessoa não vai para o Git.
- **Comandos:**
  - `node gerar.js <pasta privada>` gera as brutas em 1024 px;
  - `python3 acabamento.py <pasta privada> <logo.png>` gera `figurinhas/NN.webp` e `.png` em 512x512 (cerca de 40 KB cada, dentro do limite de 100 KB) e o `icone-pacote.png` em 96x96.
- **Para trocar frase, cor ou pose:** edite a lista `F` no `gerar.js`.

## Como instalar no WhatsApp
- **Mais fácil:** no WhatsApp Web ou Desktop, arraste os arquivos `.webp` para uma conversa (pode ser a sua). Eles chegam como figurinha. No celular, toque em cada uma e escolha "Adicionar às favoritas".
- **Para distribuir:**
  - no app gratuito **Sticker.ly** (ou "Sticker Maker"), crie o pacote "Leo Pinto" com os 10 `.png` e o ícone;
  - o app gera um link que qualquer pessoa toca para adicionar o pacote inteiro;
  - esse link vai no story e nos grupos.

Situação: **aprovado e em uso** (Lindson, 05/11/2026).
