# Passaporte da Bíblia · processo de produção (Pintura Viva)

Correção estrutural de 29/10/2026, seguindo o agente Peter (`.claude/agents/peter.md`) e o vídeo "Canal Dark: da criação à monetização".

## Ordem
1. Roteiros em `pintura.json` (lote 2: `motor/lote2.py`).
2. `python3 motor/conversa.py`: insere a conversa com o ouvinte e os balões na tela. **Rodar sempre depois do lote2.py.**
3. `python3 motor/pintura.py pintura.json <id>`: vídeo em `videos/<id>.mp4` (`STEP=15` para prévia, `RETOMAR=1` para continuar).
4. `python3 motor/capas_pv.py`: capas (Shorts; longos A, B e C clara para o teste A/B/C).
5. `python3 motor/app_pv.py ativos.json`: app de postagem. `motor/fabrica_pv.py`: aba Passaporte na Fábrica.

## O que mudou
- **Voz humanizada** (`conteudo/youtube/comum/voz_humana.py`): mesma voz de sempre (AntonioNeural). Cada frase é gerada separada, com variação de ritmo e tom, pausas conforme a pontuação, respiração antes de frase longa e tratamento de estúdio. Nas falas para o ouvinte a voz fica mais calma e calorosa.
- **Conversa com o ouvinte**: de 1 a 3 momentos por Short e de 4 a 6 por longo. São check-ins ("tá comigo até aqui?"), perguntas para comentar ligadas ao que a pessoa acabou de aprender, seguir, salvar e mandar pra alguém. Cada fala é única do vídeo. Na tela entra um balão (comentário, inscrever, salvar, compartilhar) com um "plim" suave.
- **Gancho imediato**: a narração começa em 0,35 s e o título entra por cima da 1ª cena. Há perguntas abertas no começo que são respondidas no fim.
- **Sem modelo repetido**: 3 aberturas, 3 fechamentos e 4 trilhas com andamentos diferentes, escolhidos pelo id do vídeo. As pausas entre cenas também variam.
- **Prova de trabalho humano**: roteiros, decisões e histórico ficam no Git, para mostrar ao YouTube se algum dia precisar recorrer.
