# WF Celulares · motion-02: criativos de alta retenção (conta Leandro, 10/11/2026) · aguardando aprovação

Mesmos 5 produtos e preços do motion-01. Vídeos de 13 a 15 s, 1080×1920, com 4,6 a 6 MB cada. Capas em `capa-0N.jpg`; folha dos 3 primeiros segundos em `folha-3s.jpg` (1 quadro a cada 0,25 s).
- **Gancho (0 a 3 s), diferente em cada vídeo:** 01 preço gigante primeiro · 02 POV · 03 "pare de rolar" com glitch · 04 pergunta-dor seguida do Laudo WF · 05 antes × depois. No 05, o "antes" é o preço anterior real da própria loja (R$ 6.499), não um preço de tabela.
- **O que todos têm:** voz desde o quadro 0, impacto no 0, quadro 0 já com o texto cheio (sem logo e sem fade), corte a cada cerca de 1 s com whoosh e flash, legenda palavra por palavra pelo tempo do Whisper, barra de progresso, loop aberto ("o melhor vem no final") aos 3 s, micro-reveals (capacidade, teste, garantia, parcelamento), CTA falado e escrito com o número grande nos 2,6 s finais, e os últimos 0,3 s voltando ao 1º quadro para emendar o loop. A zona segura fica livre: nada de texto em 0 a 288 px nem em 1632 a 1920 px.
- **Escassez:** só "consulte disponibilidade". Para escrever "1 unidade", o Lindson precisa confirmar.
- **Estilos (edit-ia-pro / motion):** nº 2 Gancho na tela, nº 10 Palavra de impacto, nº 1 Legenda palavra por palavra; #41 tipografia cinética, #163 zoom punch, #166 corte na batida, #169 flash, #103 glitch (só no 03), #152 light leak, #35 grão, motion blur e shake.
- **Voz:** pt-BR-AntonioNeural +4%, sem pitch e sem eco. O Giuseppe foi reprovado. Teste de vozes grátis em `vozes-teste/` (resultado.json): Antonio sim 0,976 · Piper faber 0,894 · Piper edresson 0,847 (errou "laudo") · gTTS 0,930 (feminina, só referência). XTTS e Kokoro não foram testados porque precisam de torch e de vários GB de download, e a rede daqui baixa a ~350 KB/s.
- **Gerar:** `python3 voz.py` (gera e confere no Whisper, sim ≥ 0,93 e sem erro em modelo, número ou preço) → `python3 gerar.py` → quadros (ver o README do motion-01) → `python3 montar.py`.

## Conferência da voz (Whisper small, pt)
| # | Texto | Whisper | sim |
|---|---|---|---|
| 1 | Dois mil seiscentos e noventa e nove reais num iPhone 13 Pro Max? 256 gigas, com garantia. E com laudo. E até 18 vezes. Chama no WhatsApp agora. | R $ 2 .699 no iPhone 13 Pro Max, R $ 256 GB com garantia, e com um laudo, e até 18 vezes. Chama no WhatsApp agora. | 0.954 |
| 2 | Você entrando na WF com 3.950 reais e saindo com um iPhone 15 Pro Max. Testado e com garantia. No Pix tem desconto. Chama no WhatsApp agora. | Você entrando na WF com R $ 3 .950 e saindo com o iPhone 15 Pro Max testado e com garantia. No Pix tem desconto. Chama no WhatsApp e agora! | 0.952 |
| 3 | Pare de rolar! iPhone 12 Pro Max por 2.299 reais. Com laudo e garantia. E o melhor vem no final: até 18 vezes. Chama no WhatsApp agora. | Pare de rolar! iPhone 12 Pro Max por R $ 2 .299 ,00, com um laudo e garantia. E o melhor vem no final, até 18 vezes. Chama no WhatsApp e agora! | 0.971 |
| 4 | Medo de comprar seminovo bichado? Na WF o iPhone sai testado. E com laudo. iPhone 14 Pro Max por 3.299 reais. Chama no WhatsApp agora. | medo de comprar seminovo bichado? Na WF, o iPhone sai testado. E com o laudo? iPhone 14 Pro Max por R $ 3 .299. Chama no WhatsApp e agora! | 0.969 |
| 5 | Era 6.499 reais. Agora 6.399. iPhone 17 Pro Max, cor silver, na garantia Apple. Chama no WhatsApp agora. | Era R $ 6 .499. Agora R $ 6 .399. iPhone 17 Pro Max, Core Silver, na garantia Apple. Chama no WhatsApp e agora. | 0.935 |

## Legendas (gancho na 1ª linha)
**01**
R$ 2.699 num iPhone 13 Pro Max? Sim, é isso mesmo.
Preto, 256 GB, com garantia e Laudo WF. E ainda dá pra parcelar em até 18x.
Consulte disponibilidade: chama no WhatsApp agora, (98) 98827-1882.
#iPhone13ProMax #WFCelulares #iPhoneSaoLuis #Seminovo

**02**
POV: você entra na WF com R$ 3.950 no bolso...
...e sai com um iPhone 15 Pro Max 256 GB, testado e com garantia. No Pix tem desconto.
Chama no WhatsApp agora: (98) 98827-1882.
#iPhone15ProMax #WFCelulares #SaoLuisMA #iPhoneSeminovo

**03**
PARE DE ROLAR: iPhone 12 Pro Max por R$ 2.299.
128 GB, com laudo e garantia, em até 18x. O melhor Pro Max pelo menor preço da loja.
Chama no WhatsApp agora: (98) 98827-1882.
#iPhone12ProMax #WFCelulares #iPhoneBarato #SaoLuis

**04**
Medo de comprar seminovo bichado?
Na WF, todo iPhone sai testado e com Laudo WF. Este é o iPhone 14 Pro Max 128 GB, por R$ 3.299, com garantia e Pix com desconto.
Chama no WhatsApp agora: (98) 98827-1882.
#iPhone14ProMax #WFCelulares #LojaDeIphone #SaoLuisMA

**05**
Era R$ 6.499. Agora: R$ 6.399.
iPhone 17 Pro Max Silver 256 GB, seminovo e na garantia Apple. Até 18x.
Consulte disponibilidade no WhatsApp: (98) 98827-1882.
#iPhone17ProMax #WFCelulares #iPhoneSaoLuis #Silver
