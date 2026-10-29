# Raposa e Leão — processo de produção (versão humanizada)

Correção estrutural pedida pelo Peter (diagnóstico de conteúdo inautêntico): voz crua, modelo igual em todos os Shorts e nenhuma conversa com o ouvinte.

## O que mudou
- **Voz humanizada** (`conteudo/youtube/comum/voz_humana.py`): cada frase gerada separada, com variação de ritmo e tom, pausas naturais, respiração antes de frase longa e tratamento de estúdio. As falas diretas ao ouvinte saem mais calorosas. Voz base do canal: AntonioNeural, rate +7, pitch -6.
- **Conversa com o ouvinte**: cada vídeo tem falas próprias, sem bordão copiado entre vídeos.
  - **Shorts:** 2 por vídeo, no meio e no fim.
  - **Longos:** 3 a 5 por vídeo, mais inscreva, compromisso e fim reescritos.
  - **Tipos de fala:** check-in ("tá comigo?"), pergunta para os comentários ligada à lição, convite a seguir no momento de valor, salvar ou mandar para alguém.
- **Componente na tela** (`motor/interage.inc`): comentário sendo digitado, botão Inscrever-se com clique e sino, ícone de salvar, enviar ou check-in. É acionado pelo campo `interage` (Shorts) ou pela tela `conversa` (longos).
- **Variação de modelo:**
  - Cena `conversa` com retrato em movimento.
  - 3 aberturas (`zoom`, `flash`, `tremor`) e 3 fechamentos (`classico`, `seguir`, `pergunta`) com frase própria.
  - Andamento e desenho do pulso variam por Short; tons da trilha variam por longo.
  - O gancho começa no primeiro segundo, sem vinheta.
- **Sem número inventado**: o contador de curtidas falso da tela de compromisso foi retirado.

## Arquivos
| Arquivo | Para quê |
|---|---|
| `motor/conversa_shorts.py` | falas, telas, abertura, fecho e pulso de cada Short |
| `motor/short2.py NN` | monta o texto novo, gera a voz, reancora as cenas e renderiza |
| `shorts/NN/cenas_v1.json`, `palavras_v1.json` | versão original (base para reancorar; não editar) |
| `motor/conversa_longos.py` | conversas e textos novos dos longos (`roteiro_v1.json` guarda o original) |
| `motor/longo2.py` | render dos longos (`LIMITE=60` gera só a prévia do começo em `previa.mp4`) |
| `motor/lote.sh` | renderiza o lote |

## Como renderizar
```bash
cd conteudo/youtube/raposa-e-leao/motor
./lote.sh shorts            # todos os Shorts (ou: ./lote.sh shorts 05 06)
./lote.sh longos            # todos os longos (ou: ./lote.sh longos 07)
python3 short2.py 12 --seco # só mostra o texto novo com as falas, sem gerar nada
```

## Regra para roteiros novos
Toda fala ao ouvinte é escrita para aquele vídeo e ligada à lição dele. Nunca reutilizar a frase de outro vídeo. Linguagem simples de WhatsApp. Citação de O Príncipe sempre com o capítulo.
