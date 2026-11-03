# Como deixar o app de clone gratuito e bom (conta Pedro, 03/11/2026)

> Pedido do Lindson (03/11): "pesquise tudo que possa fazer o app ser extremamente gratuito e bom".
> Fontes públicas. `research.google.com` (FAQ do Colab) e `huggingface.co` não abriram na rede da sessão; vários números vêm de blogs. **As cotas mudam: reveja a cada 3 meses.** **[INFERÊNCIA]** = dedução nossa.

## 1. Placa de vídeo grátis na nuvem

| Serviço | GPU | Cota | Interface web? | Pode para o nosso uso? |
|---|---|---|---|---|
| **Modal** | T4 a H100 | **US$ 30 de crédito por mês** ([pricing](https://modal.com/pricing)) | Sim, feito para isso | **Sim. O melhor para automatizar**: o app chama uma função Python na GPU |
| **Kaggle** | P100 16 GB ou 2× T4 | ~30 h por semana, sessão de até 12 h; pede verificar o telefone | Túnel/Gradio público costuma ser derrubado | **Só pessoal e não comercial**; proíbe "server farming" ([AUP](https://kaggle.com/aup)). Serve para teste e lote pela CLI |
| **Google Colab grátis** | T4 (sem garantia) | Não divulgado (~12 h por sessão, segundo blogs) | **Derruba interface web** no grátis ([FAQ](https://research.google.com/colaboratory/faq.html)) | **Proíbe deepfake** desde 2022 ([unite.ai](https://www.unite.ai/google-has-banned-the-training-of-deepfakes-in-colab/)). Só manual, como reserva |
| HF ZeroGPU | Fatia de H200 | 3,5 a 5 min por dia | Gradio | Só testes curtos |
| Lightning AI | T4/L4/A100 | Crédito único de até 30 (mudou em 09/2026) | Sim | Banco de horas de reserva |
| SageMaker Studio Lab | T4 | 4 h por sessão | Jupyter | Reserva |
| Paperspace, Saturn | fracos ou instáveis | — | — | Não depender |
| GCP / AWS / Azure | sem GPU no teste grátis | — | — | Não servem |

**Automação:**
- **Kaggle:** `kaggle kernels push` com `enable_gpu: true`, depois `kaggle kernels status` e `kaggle kernels output`, com os arquivos de entrada num dataset privado.
- **Modal:** função Python com GPU chamada direto do app.
- **Colab:** não tem API para isso.

## 2. Fazer caber nos 4 GB da RTX 3050

- **MuseTalk 1.5 em fp16:** UNet de ~1,6 GB, mínimo citado de 4 GB, 1,5 a 2× mais rápido ([model card](https://huggingface.co/marcosremar2/MuseTalk1.5)). **Candidato nº 1 para o notebook.**
- **Qwen3-TTS 0,6B:** ~2 GB em fp16. Cabe.
- **LivePortrait:** leve; no Windows usar ONNX Runtime GPU (o TensorRT do FasterLivePortrait é só Linux).
- **Applio e faster-whisper int8:** leves.
- **LatentSync** (8/18 GB), **InfiniteTalk, Wan 2.2, EchoMimic:** nuvem. O Wan2GP começa em 6 GB, lento; **em 4 GB não é realista**.
- **ComfyUI:** `--novram` (mais lento), `--reserve-vram 2`, modelos GGUF, "block swap" do kijai.
- **Windows:**
  - driver NVIDIA Studio atualizado;
  - no Painel NVIDIA, "CUDA – Sysmem Fallback Policy" em "Prefer Sysmem Fallback" (evita erro de memória, mas fica lento);
  - o ideal é ter 32 GB de RAM;
  - paginação grande no SSD;
  - fechar o navegador durante a geração;
  - tomada ligada e perfil de máximo desempenho no NitroSense;
  - WSL2 só para o que for apenas Linux.

## 3. Qualidade grátis e liberada

| Ferramenta | Para quê | Licença |
|---|---|---|
| Real-ESRGAN | Aumentar resolução | BSD-3 |
| GFPGAN | Restaurar rosto | Apache 2.0 (conferir os pesos) |
| **CodeFormer** | Restaurar rosto | **Não comercial: evitar** |
| Practical-RIFE | 25 → 50 fps, lip-sync mais suave | MIT |
| DeepFilterNet | Tirar ruído da voz (CPU) | MIT/Apache |
| Resemble Enhance | Realçar voz | MIT |
| Demucs | Separar voz e música | MIT |
| faster-whisper + FFmpeg | Legenda queimada, cortes, volume -14 LUFS | MIT / LGPL |
| Música e efeitos | Biblioteca de Áudio do YouTube, Pixabay, Freesound (só CC0) | conferir cada faixa |

**Ordem que dá qualidade:** TTS → DeepFilterNet/Resemble Enhance → Applio (timbre) → lip-sync → GFPGAN só no rosto → Real-ESRGAN → RIFE → legenda e mixagem no FFmpeg.

## 4. Planos grátis de serviços pagos

ElevenLabs (10 mil créditos, não comercial, com atribuição), HeyGen (3 vídeos, 720p, marca d'água) e Hedra (marca d'água, não comercial): **servem só para comparar**. Uma exceção útil: **Cloudflare Workers AI** dá 10 mil "neurons" por dia grátis, inclusive Whisper, e o Lindson já usa a Cloudflare ([docs](https://developers.cloudflare.com/workers-ai/platform/pricing/)).

## 5. Receita final

- **No notebook (sem cota):**
  - voz: Qwen3-TTS 0,6B / Chatterbox pt-br → Applio → DeepFilterNet;
  - legenda: faster-whisper;
  - boca: MuseTalk fp16;
  - gravuras: LivePortrait;
  - acabamento: GFPGAN, Real-ESRGAN, RIFE e FFmpeg.
- **Na nuvem grátis:**
  1. **Modal (US$ 30/mês)** como motor principal e automático para LatentSync, InfiniteTalk e EchoMimic.
  2. **Kaggle** só para teste e lote noturno pela CLI, sem túnel.
  3. Colab só manual.
  4. Lightning e Studio Lab como reserva.
- **Ligação entre as duas partes:** o app local tem uma fila. Cada trabalho vira um JSON, e um "despachante" escolhe onde rodar: local se couber, senão Modal, senão Kaggle. Ele envia o trabalho, acompanha e baixa o MP4. Os notebooks prontos ficam versionados no repositório.
- **Riscos:**
  - Kaggle e Colab grátis não servem para conteúdo monetizado ou de cliente (são uso comercial). O conteúdo final passa pelo notebook ou pelo Modal.
  - Nada de várias contas para fugir de cota.
  - Só rosto e voz com consentimento escrito.
  - CodeFormer fica fora.
