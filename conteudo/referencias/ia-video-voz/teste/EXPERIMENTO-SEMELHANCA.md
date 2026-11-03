# Experimento: voz clonada idêntica à do Lindson (conta Pedro, 03/11/2026)

> Pedido do Lindson (03/11): "ficou bem melhor, verifique formas de deixar a voz 10 idêntica, quase imperceptível de ser detectado que é uma IA".
> Áudios do Lindson (2 de WhatsApp + áudio de 9 vídeos, 4:52 no total) ficam **fora do Git**. Aqui só o método e os números.

## Como medimos
- **Juiz independente:** Resemblyzer (modelo de reconhecimento de voz diferente do que gera). Nota = semelhança de 0 a 1 com a média da voz real.
- **Teto:** pedaços de 6 s da voz real comparados com a média dos outros pedaços: **0,924** (mínimo 0,852, 46 pedaços). Nem a voz real tira 1,0.
- Frase de teste: "Fala, pessoal, aqui é o Lindson. Hoje eu vou te mostrar como conseguir mais clientes pelo Instagram, sem gastar nada." Duas gerações por versão (sementes 0 e 1).

## Resultados (Chatterbox Multilingual, CPU)
| Versão | Nota |
|---|---|
| 1. Trecho fixo de 12 s (como era) | 0,931 |
| 2. Identidade média de todo o áudio | 0,929 (instável: 0,948/0,910) |
| 3. Melhor trecho de 10 s, escolhido pelo juiz | 0,934 |
| 4. Melhor trecho + identidade média | 0,937 |
| 5. = 4 + ritmo mais solto (cfg 0,3) | 0,934 |
| **6. = 4 + temperatura 0,6 e expressão 0,45** | **0,945** (0,945/0,945) **← vencedora, aplicada no Dublê** |
| 6 + conversor de voz ChatterboxVC (alvo: melhor trecho, x-vector médio) | 0,949: ganho dentro da margem e dobra o tempo, **não usado** |

Com o tratamento final (texto completo, `motor_voz.py`): **teste 01/02 = 0,895 → teste 03 = 0,935**.

## Conclusão
- O **timbre** já passa no juiz como a voz real. O que ainda denuncia a IA é o **jeito de falar**: ritmo, entonação, gírias, sotaque.
- Para chegar ao "10": (a) **20 a 30 min** de áudio dele falando do jeito de sempre (aulas, lives, áudios longos), limpos, para ajuste fino (LoRA) do Chatterbox; (b) escrever o texto como ele fala; (c) comparar Qwen3-TTS e VoxCPM2 com o mesmo juiz.
- **Não fazemos:** tirar a marca d'água PerTh nem tentar enganar detectores de IA. O objetivo é soar como ele; a publicação continua marcada como feita com IA (regra do app e das plataformas).

## Arquivos
`experimento_semelhanca.py` (6 versões) e `experimento_vc.py` (conversor de voz). Rodam com o venv do teste (chatterbox-tts + resemblyzer).
