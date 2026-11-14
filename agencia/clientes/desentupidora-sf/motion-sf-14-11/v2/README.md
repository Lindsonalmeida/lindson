# SF motion v2 (conta Zuleide, 14/11/2026) · aguardando aprovação
v1 reprovada pelo Lindson: número errado e fotos genéricas. Mudanças:
- WhatsApp corrigido para **(98) 92010-5710** (o do site no ar, `const N='5598920105710'`).
- Fotos que geram identificação, geradas por IA grátis (Stable Horde, Juggernaut XL; `horde.py`, prompts em `lista.tsv`): banheiro brasileiro com vaso transbordando, morador preocupado, mulher com desentupidor, pia de cozinha cheia, box alagado, caixa de gordura de restaurante, dono do restaurante, técnico de uniforme azul e laranja (como o do flyer da SF). Aviso "Imagens geradas por IA" em todos.
- Pessoas recortadas (`recortar.py`, agora só com a maior mancha: some a sobra que aparecia no técnico do 05).
- Mesmo motor, roteiro e voz da v1 (`../voz/`). Gerar: `python3 gerar.py` → `./fazer.sh 1 2 3 4 5`. MP4 fora do Git, nesta pasta, na máquina da Zuleide.
