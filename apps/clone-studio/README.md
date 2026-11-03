# Clone Studio (nome provisório): app interno de clone de voz e imagem (conta Pedro, 03/11/2026)

App do Lindson para clonar voz (e, na etapa 2, rosto) **só com autorização**. Roda no notebook dele (Acer Nitro 5, RTX 3050 com 4 GB, 24 GB de RAM) e abre no navegador. Pesquisa e plano em `conteudo/referencias/ia-video-voz/` (`PLANO-DO-APP.md`).

## O que já faz (etapa 1)
- **Biblioteca:** cadastra Lindson, clientes e personagens, com amostra de voz, termo assinado, vídeo de consentimento, validade e fonte.
  - **Trava:** cliente e Lindson só geram com termo + vídeo de consentimento em dia.
  - Personagem só gera com a fonte registrada.
- **Voz:** texto → voz clonada em português (Chatterbox Multilingual, MIT), frase a frase, com a humanização do `voz_humana.py` (variação, pausas, respiração, som de estúdio). O áudio sai em `dados/saidas/`.

## Próximas etapas
1. Vídeo: boca sincronizada no vídeo base (MuseTalk 1.5, fp16, cabe nos 4 GB).
2. Gravuras vivas (LivePortrait) para os canais dark.
3. O pesado (corpo e gestos) vai para o Modal (US$ 30 grátis por mês).
4. Identidade visual e nome definitivo (`identidade/`).

## Instalar no Windows (uma vez)
1. Instale o **Python 3.11** em https://www.python.org/downloads/ e marque **"Add python.exe to PATH"**.
2. Baixe esta pasta (`apps/clone-studio`) para o **disco D:**, por exemplo `D:\clone-studio`.
3. Dê dois cliques em **`instalar.bat`**. Ele baixa cerca de 5 GB (PyTorch com CUDA para a RTX 3050 e o Chatterbox) e leva de 10 a 30 minutos.
4. Para abrir: dois cliques em **`abrir.bat`**. O navegador abre em http://127.0.0.1:7860.

Na primeira geração, o modelo de voz (cerca de 2 GB) é baixado automaticamente.

## Usar
1. **Biblioteca:**
   - nome, tipo e amostra de voz (10 s a 2 min de fala limpa, sem música);
   - para pessoa real: termo assinado (PDF ou foto), vídeo de consentimento lendo a frase da tela e validade;
   - salvar.
2. **Voz:**
   - escolha a voz e escreva o texto como se fala (frases curtas, números por extenso);
   - clique em **Gerar voz**.

## Privacidade
A pasta `dados/` (vozes, termos, vídeos e áudios gerados) fica **só no computador do Lindson**. Ela está no `.gitignore` e nunca vai para o GitHub, que é público. Toda saída realista deve ser marcada como "feita com IA" ao publicar. O Chatterbox também grava uma marca d'água inaudível (PerTh).

## Arquivos
| Arquivo | O que faz |
|---|---|
| `app.py` | Interface: abas Biblioteca, Voz e Vídeo |
| `motor_voz.py` | Clonagem e humanização da voz |
| `biblioteca.py` | Cadastro e trava de consentimento |
| `instalar.bat` | Instalação no Windows |
| `abrir.bat` | Abre o app |
| `requisitos.txt` | Pacotes Python |
