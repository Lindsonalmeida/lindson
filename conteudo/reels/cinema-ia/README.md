# Reels "Cinema IA" · marca do Lindson (conta Leandro, 21/11/2026)

Substitui as "miniaturas 3D" (reprovadas 2x: **nunca mais** bonecos low-poly em mesa preta). O Lindson gera as cenas no Gemini com o rosto dele (estilo Denis Bugatti) e o motor transforma cada imagem em plano de cinema.

- `PROMPTS-GEMINI.md`: 3 a 4 cenas para cada um dos 6 roteiros (`../miniaturas-3d/roteiros.json`), bloco de fidelidade de rosto, ficha técnica e vídeo opcional (Veo).
- `motor/cinema.py`: parallax 2.5D (recorte rembg + fundo por inpaint), push/pull/pan/rise, luz volumétrica, poeira, flare anamórfico, grão, vinheta, whip pan e zoom punch com SFX, Anton gigante com 1 palavra neon no tempo da fala, legenda palavra por palavra (Whisper), assinatura, -14 LUFS.
- `motor/plano-04.json`: plano do Reel 04 (cenas, foco, movimento, luz, títulos, tempos). `motor/upscale.py`: Real-ESRGAN x2 (`/root/.modelos/real_esrgan_x2.onnx`).
- `whisper/04.json`: palavras com tempo da voz 6 do Reel 04.

## Rodar
1. Cenas em `cenas/`: `python3 motor/upscale.py cena.jpg cenas/uNN.jpg`; máscara: `rembg` sessão `u2net_human_seg` (`only_mask=True`) → `cenas/mNN.png` (apague `~/.u2net` depois: disco curto).
2. Voz 6 em `voz/NN-voz6.wav` (Chatterbox, ref6.wav) e palavras do Whisper em `whisper/NN.json`.
3. `cd motor && python3 cinema.py plano-NN.json ../saida/NN.mp4` (≈ 1 s por quadro em CPU). Teste rápido: `QUADROS=3,8,14 python3 cinema.py ...` salva só esses quadros.

## Prova de conceito (21/11)
Reel 04 com as 5 cenas já geradas (`membros/img/gemini-16-11/31-35.jpg`, privado). MP4 e folha no privado: `painel/admin-rede/reels-cinema-ia/`.
Limitações: a voz veio do 04 antigo (voz 6 já mixada com a trilha e SFX antigos, porque esta máquina não tem torch nem disco para o Chatterbox); as cenas 31-35 não foram feitas para este roteiro (genéricas, repetidas em 8 falas); a fala 7 sai "você não gosta de aparecer" no Whisper (pronúncia da voz 6: regravar).
