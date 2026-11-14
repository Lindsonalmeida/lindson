# Desentupidora SF · 4 roteiros só de CAIXA DE GORDURA (14/11/2026, conta Lindson, agente Social media)

Pedido do Lindson: "foque só em caixa de gordura, mostrando mais as caixas, a gordura, a parte entupida, pro cliente se identificar. Faça 4 diferentes só de caixa de gordura."

Base usada: `../falados2/README.md` (vídeos 5 a 8, mesma fórmula de falas e cartão final), `../PROMPTS.md` (vídeo 4 de caixa de gordura, cenas HeyGen), `../../identidade/TEMPLATE.md` (farda), `conteudo/avaliacao-gratuita/LEGENDAS.md` (legenda SEO). A padaria já teve caixa de gordura no vídeo 6, por isso ficou fora daqui.

## Regras fixas dos 4 vídeos
- **Formato:** 9:16, 1080×1920, 25 a 35 s. Gancho na tela de 0 a 2 s (até 5 palavras, Montserrat Black Italic, branco com 1 palavra em laranja #FF8A00 sobre tarja marinho #061A4A).
- **Promessas permitidas (só estas):** orçamento grátis por foto ou vídeo no WhatsApp, sem quebra-quebra, máquina de cabo rotativo, técnico uniformizado, teste na hora, atende casas, condomínios, restaurantes e empresas. **Proibido:** prazo, preço, "garantido", número inventado, "mesmo dia".
- **Farda (sempre igual):** macacão azul royal (#1D5FD0) com peito e ombros laranja (#FF8A00), patch redondo no lado esquerdo do peito, luvas pretas de nitrila, botina preta. Nos prompts o patch vem **em branco, sem texto**: a logo SF redonda **original** entra na montagem (`../falados2/logo_av.py`), para não repetir o erro da "logo dançando".
- **Caixa de gordura realista, sem nojeira:** crosta branca/amarelada de gordura solidificada boiando, água turva parada, borda de concreto ou PVC, luz natural. Nada de vômito, larva, close gosmento escorrendo ou exagero.
- **Pronúncia na voz:** "Esse Efe" (SF), número por extenso: "noventa e oito, nove dois zero um zero, cinco sete um zero".
- **Áudio (nunca sem):** fala em lip sync ou voz por cima, SFX (tampa de concreto arrastando, borbulho, sucção do equipamento, água escoando, whoosh nos cortes), trilha baixa em ducking, -14 LUFS. VFX: flash branco nos cortes, tremor leve no gancho, light leak no cartão final.
- **Legenda queimada:** palavra por palavra, nunca sobre o rosto.
- **Marcação:** `[LIP SYNC]` = personagem fala olhando para a câmera (HeyGen avatar/lip sync). `[VOZ POR CIMA]` = fala gravada sobre cena de serviço, sem boca na tela (pode ser TTS se os créditos acabarem).
- **Cartão final (igual nos 4):** fundo marinho #061A4A, logo SF original, "ORÇAMENTO GRÁTIS" em laranja, "(98) 92010-5710" gigante em branco, ícone do WhatsApp, "@desentupidorasf_slz". Selo pequeno: "Imagens geradas por IA".
- **Fala final do técnico (igual nos 4, [LIP SYNC]):** "Caixa de gordura cheia? Manda uma foto no WhatsApp: noventa e oito, nove dois zero um zero, cinco sete um zero. O orçamento é grátis."

---

## Vídeo 9 · DONA DE CASA · "O cheiro vem da caixa"
**Persona:** Dona Rose, 48 anos, Cohama, casa térrea com quintal. Cozinha todo dia para a família (peixe frito, arroz de cuxá). A caixa de gordura fica no quintal, perto da área de serviço, e ninguém lembra dela. Dor: cheiro ruim subindo no quintal e na pia, mosquinha, vergonha quando chega visita. Confia em técnico uniformizado que não quebra o piso de cerâmica que ela acabou de colocar.

**Gancho na tela (0-2 s):** "O CHEIRO VEM DAQUI" (laranja: "DAQUI")
**Duração:** ~30 s

### Falas
| # | Tempo | Quem | Tipo | Fala |
|---|---|---|---|---|
| 1 | 2-7 s | Dona Rose | [LIP SYNC] | "Eu limpava a pia todo dia e o cheiro não saía! Era a caixa de gordura." |
| 2 | 7-11 s | Dona Rose | [VOZ POR CIMA] | "Tava cheia, com mosquinha, e a água da pia voltando." |
| 3 | 11-17 s | Técnica SF (Jéssica) | [VOZ POR CIMA] | "A gordura da cozinha endurece e tampa a saída. A gente retira tudo e desentope o cano com cabo rotativo." |
| 4 | 17-21 s | Técnica SF | [LIP SYNC] | "Sem quebra-quebra no seu piso. E o teste é na hora, na sua frente." |
| 5 | 21-24 s | Dona Rose | [LIP SYNC] | "Acabou o cheiro! Agora eu lembro dela." |
| 6 | 24-31 s | Técnica SF | [LIP SYNC] | Fala final padrão (WhatsApp). |

### Cenas (plano a plano)
1. **0-2 s · Gancho:** top shot, tampa de concreto da caixa de gordura sendo puxada no quintal; dentro, crosta branca/amarelada de gordura cobrindo tudo, mosquinhas leves voando. Tremor leve + texto de gancho.
2. **2-7 s:** Dona Rose na porta da cozinha, pano de prato no ombro, nariz franzido, falando para a câmera.
3. **7-11 s:** pia da cozinha com água turva parada até a metade, borbulha e volta um pouco; corta para close da caixa com a água no limite da borda.
4. **11-14 s:** close do cano de saída dentro da caixa, tampado por um "tampão" de gordura endurecida.
5. **14-17 s:** técnica de farda, luvas pretas, retira as placas de gordura com pá/concha de aço para baldes com tampa; depois passa o cabo rotativo no cano.
6. **17-21 s:** técnica de pé no quintal, piso de cerâmica intacto, falando para a câmera.
7. **21-24 s:** caixa limpa, paredes de concreto visíveis, água clara; abre-se a torneira da pia e a água desce rápido, espiral limpo no ralo. Dona Rose sorri.
8. **24-31 s:** técnica falando o WhatsApp + cartão final (últimos 3 s).

### Prompts (HeyGen / Veo, 9:16)
**Cena 1**
```
Vertical 9:16 realistic top-down video of a backyard in a simple Brazilian house in São Luís, ceramic tile floor, laundry area in the background. Gloved hands slide open a square concrete grease trap lid. Inside, a thick white-and-yellowish layer of solidified kitchen grease covers the water surface completely, a few small flies lift off. Natural daylight, documentary look, realistic, not gross. Audio: heavy concrete lid scraping, small flies buzzing. No on-screen text, no logos.
```
**Cena 2**
```
Vertical 9:16 realistic video, medium close-up of a Brazilian woman in her late 40s, brown skin, hair tied in a bun, simple floral blouse, dish towel on her shoulder, standing at the door of a modest home kitchen in São Luís. She wrinkles her nose and speaks to the camera in Brazilian Portuguese, annoyed but friendly. Warm natural light. Leave the lower third free of the face. No on-screen text, no logos.
```
**Cena 3**
```
Vertical 9:16 realistic close-up video, stainless steel home kitchen sink half full of cloudy greasy water that does not drain; it bubbles and rises slightly. Cut to the backyard grease trap with murky water at the very edge of the concrete rim, a layer of yellowish grease floating. Natural light, realistic, not gross. Audio: slow gurgling, water bubbling. No on-screen text, no logos.
```
**Cena 4**
```
Vertical 9:16 realistic macro video inside an open concrete grease trap: the white PVC outlet pipe is blocked by a hard plug of solidified yellowish-white grease, murky water standing still around it. Daylight from above, documentary realism, not gross. Audio: low water drip echo. No on-screen text, no logos.
```
**Cena 5**
```
Vertical 9:16 realistic video, Brazilian female technician in her 30s, brown skin, hair in a ponytail, wearing a royal blue work coverall with an orange chest panel and orange shoulders, a small round blank badge patch on the left chest with no text, black nitrile gloves, black safety boots. Kneeling by an open backyard grease trap, she removes slabs of solidified grease with a steel scoop into a lidded bucket, then feeds a rotating cable drain machine into the outlet pipe. Professional, clean, realistic. Audio: scraping, motor hum of the drain machine. No on-screen text, no readable logos.
```
**Cena 6**
```
Vertical 9:16 realistic medium shot, the same Brazilian female technician in a royal blue coverall with orange chest panel and orange shoulders, small round blank chest patch with no text, black gloves, standing on an intact ceramic tile backyard floor next to a closed grease trap, speaking confidently to the camera in Brazilian Portuguese. Natural daylight. No on-screen text, no readable logos.
```
**Cena 7**
```
Vertical 9:16 realistic video: a clean concrete grease trap with clear water and visible walls; cut to a home kitchen sink where the tap is opened and clear water drains fast in a clean spiral. The Brazilian woman in her late 40s with a dish towel on her shoulder smiles, relieved. Bright natural light. Audio: fast water draining, light relieved laugh. No on-screen text, no logos.
```
**Cena 8**
```
Vertical 9:16 realistic medium close-up, Brazilian female technician in a royal blue coverall with orange chest panel and orange shoulders, small round blank chest patch with no text, smiling and speaking to the camera in Brazilian Portuguese, holding a smartphone. Clean kitchen background, soft daylight. Leave empty space at the bottom of the frame. No on-screen text, no readable logos.
```

### Legenda
```
CAIXA DE GORDURA ENTUPIDA EM CASA: O CHEIRO QUE NINGUÉM DESCOBRE DE ONDE VEM

Você limpa a pia, joga desinfetante no ralo, e o cheiro ruim continua? Em muita casa de São Luís o problema não está na pia. Está no quintal, embaixo de uma tampa que ninguém abre: a caixa de gordura.

📌 O que acontece dentro da caixa de gordura
Toda gordura que desce da pia (óleo de fritura, resto de comida, sabão) esfria e vira uma crosta branca por cima da água. Com o tempo essa crosta engrossa, tampa a saída do cano e a água começa a voltar.

⚠️ Sinais de que a caixa de gordura da sua casa está cheia
• cheiro ruim no quintal ou subindo pela pia
• mosquinha perto do ralo da cozinha
• pia demorando para escoar ou voltando água
• água da caixa chegando na borda da tampa

🔧 Como a Desentupidora SF resolve
O técnico uniformizado abre a caixa, retira a gordura acumulada e desentope o cano de saída com máquina de cabo rotativo, sem quebra-quebra no seu piso. No fim, o teste é feito na hora, na sua frente, com a água escoando.

💡 Exemplo
Pia voltando e cheiro no quintal? Tire uma foto da caixa aberta (ou da pia) e mande no nosso WhatsApp. Você recebe o orçamento sem pagar nada por isso.

✅ Conclusão
Cheiro na cozinha nem sempre é falta de limpeza. Muitas vezes é a caixa de gordura pedindo socorro.

📲 Orçamento grátis por foto ou vídeo no WhatsApp (98) 92010-5710. Atendemos casas, condomínios, restaurantes e empresas em São Luís e região.

Imagens geradas por IA.

#caixadegordura #limpezadecaixadegordura #dicasdecasa #saoluisma #slz
```

---

## Vídeo 10 · DONA DE MARMITARIA · "A marmita parou"
**Persona:** Cláudia, 38 anos, marmitaria de delivery no Turu/Maiobão, cozinha de fundo de casa, 2 ajudantes. Frita peixe e frango todo dia, almoço sai das 10h às 14h pelo app e pelo zap. Dor: a pia da cozinha trava no meio do preparo, a caixa de gordura transborda no chão da cozinha, medo de perder o almoço e de cliente ver a bagunça. Confia em quem resolve sem quebrar e mostra que funcionou.

**Gancho na tela (0-2 s):** "TRANSBORDOU NO MEIO DO ALMOÇO" (laranja: "ALMOÇO")
**Duração:** ~32 s

### Falas
| # | Tempo | Quem | Tipo | Fala |
|---|---|---|---|---|
| 1 | 2-6 s | Cláudia | [LIP SYNC] | "Dez e meia, cinquenta marmitas pra sair, e a caixa de gordura transbordou!" |
| 2 | 6-10 s | Ajudante (Thiago) | [VOZ POR CIMA] | "Dona Cláudia, a água tá saindo pelo chão da cozinha!" |
| 3 | 10-14 s | Cláudia | [VOZ POR CIMA] | "Tirei uma foto e mandei no WhatsApp da Esse Efe." |
| 4 | 14-21 s | Técnico SF (Márcio) | [VOZ POR CIMA] | "Cozinha que frita todo dia enche a caixa rápido. A gente tira a gordura e passa o cabo rotativo no cano." |
| 5 | 21-25 s | Técnico SF | [LIP SYNC] | "Pronto, testado na hora. Pode abrir a torneira." |
| 6 | 25-33 s | Técnico SF | [LIP SYNC] | Fala final padrão (WhatsApp). |

> "Cinquenta marmitas" é fala de cena da personagem (exemplo de rotina), não é número de resultado da SF.

### Cenas (plano a plano)
1. **0-2 s · Gancho:** close no chão de piso branco da cozinha: tampa da caixa de gordura levantada pela pressão, água turva com placas amarelas de gordura escorrendo pela borda. Tremor + texto.
2. **2-6 s:** Cláudia de touca e avental na bancada cheia de marmitas de alumínio abertas, falando para a câmera, aflita.
3. **6-10 s:** ajudante aponta para o chão; pia industrial cheia de água parada com espuma de gordura.
4. **10-14 s:** close das mãos de Cláudia fotografando a caixa aberta com o celular e enviando no WhatsApp (tela sem nome legível).
5. **14-18 s:** técnico de farda abre bem a caixa: camada grossa de gordura sólida; retira com concha de aço para baldes com tampa.
6. **18-21 s:** close do cabo rotativo entrando no cano de saída, gordura se soltando.
7. **21-25 s:** caixa limpa; torneira da pia industrial aberta, água descendo rápido; técnico falando para a câmera.
8. **25-33 s:** técnico com Cláudia ao fundo fechando marmitas; fala final + cartão final.

### Prompts (HeyGen / Veo, 9:16)
**Cena 1**
```
Vertical 9:16 realistic low-angle close-up video, small commercial home-based kitchen in São Luís, white tile floor. A square floor grease trap lid is slightly lifted and murky water with floating yellowish grease slabs overflows onto the tiles. Busy cooking sounds in the background. Documentary realism, not gross. Audio: water gurgling and overflowing, pans sizzling. No on-screen text, no logos.
```
**Cena 2**
```
Vertical 9:16 realistic medium shot, Brazilian woman in her late 30s, light brown skin, white hairnet cap and apron, at a steel counter covered with open aluminum lunch containers with rice, beans and fried fish. She speaks to the camera in Brazilian Portuguese, stressed and in a hurry. Warm kitchen light, steam. Leave the lower third free of the face. No on-screen text, no logos.
```
**Cena 3**
```
Vertical 9:16 realistic video, a young Brazilian kitchen helper in his 20s with an apron points at the wet floor; cut to an industrial stainless steel sink full of still, cloudy water with a greasy foam layer that does not drain. Audio: urgent voice, water bubbling. No on-screen text, no logos.
```
**Cena 4**
```
Vertical 9:16 realistic close-up video, a woman's hands with a phone take a photo of an open floor grease trap full of solid yellowish grease, then send it in a messaging app; the phone screen shows only a blurred chat, no readable names. Audio: camera shutter, message sent pop. No on-screen text, no logos.
```
**Cena 5**
```
Vertical 9:16 realistic video, Brazilian male technician in his 30s, dark brown skin, short hair, wearing a royal blue work coverall with an orange chest panel and orange shoulders, a small round blank badge patch on the left chest with no text, black nitrile gloves, black safety boots. He kneels by an open kitchen floor grease trap with a thick layer of solidified grease and removes it with a steel scoop into lidded buckets. Professional, clean, realistic, not gross. Audio: scraping, buckets. No on-screen text, no readable logos.
```
**Cena 6**
```
Vertical 9:16 realistic macro video: a rotating steel drain cable from a professional drain cleaning machine enters the outlet pipe of a concrete grease trap, loosening a grease blockage; water starts to move. Hands in black gloves, sleeve of a royal blue coverall with orange detail visible. Audio: machine motor hum, water starting to flow. No on-screen text, no logos.
```
**Cena 7**
```
Vertical 9:16 realistic video: a clean grease trap with clear water, then an industrial kitchen tap opens and water drains fast and clean. The Brazilian male technician in a royal blue coverall with orange chest panel and orange shoulders, small round blank chest patch with no text, turns to the camera and speaks in Brazilian Portuguese with a calm smile. Audio: water draining fast. No on-screen text, no readable logos.
```
**Cena 8**
```
Vertical 9:16 realistic medium close-up, the same Brazilian male technician in a royal blue coverall with orange chest panel and orange shoulders, small round blank chest patch with no text, holding a smartphone and speaking to the camera in Brazilian Portuguese. In the soft-focus background, a woman in a hairnet closes lunch containers at the counter. Leave empty space at the bottom. No on-screen text, no readable logos.
```

### Legenda
```
CAIXA DE GORDURA DE MARMITARIA: COMO EVITAR QUE ELA PARE SEU ALMOÇO

Quem tem marmitaria em São Luís sabe: a hora mais corrida do dia é justamente quando a pia resolve travar. E quase sempre o motivo é o mesmo: a caixa de gordura da cozinha cheia.

📌 Por que a caixa de gordura enche tão rápido na marmitaria
Cozinha que frita peixe, frango e bife todo dia manda muito óleo para o ralo. Esse óleo esfria dentro da caixa, vira uma camada grossa e tampa o cano de saída. Aí a água não tem para onde ir e volta pela pia ou pelo ralo do chão.

⚠️ Sinais de alerta na cozinha comercial
• pia industrial demorando para escoar
• cheiro forte perto do ralo
• tampa da caixa úmida ou água no chão
• gordura branca visível quando a caixa é aberta

🔧 Como a Desentupidora SF atende a sua cozinha
Técnico uniformizado, retirada da gordura acumulada e desentupimento do cano com máquina de cabo rotativo, sem quebra-quebra. Antes de ir embora, o teste é feito na hora, com a torneira aberta.

💡 Exemplo
Viu a pia voltando? Não espere transbordar no meio do preparo. Tire uma foto da caixa aberta e mande no WhatsApp para receber o orçamento grátis.

✅ Conclusão
Na marmitaria, caixa de gordura cheia não é só sujeira: é almoço atrasado e cliente esperando.

📲 Orçamento grátis por foto ou vídeo no WhatsApp (98) 92010-5710. Atendemos restaurantes, lanchonetes, marmitarias, casas, condomínios e empresas em São Luís.

Imagens geradas por IA.

#caixadegordura #marmitaria #cozinhaindustrial #desentupidorasaoluis #saoluis
```

---

## Vídeo 11 · DONO DE RESTAURANTE DE FRUTOS DO MAR · "Fila na porta, cheiro no salão"
**Persona:** Seu Raimundo, 55 anos, restaurante de peixe e frutos do mar perto da Litorânea / Ponta d'Areia, salão cheio no fim de semana, muita fritura (peixe pedra, camarão empanado). Dor: cheiro de esgoto chegando ao salão na hora do movimento, ralo do chão da cozinha voltando, medo de reclamação de cliente e de fiscalização. Confia em empresa que atende restaurante, vem uniformizada e não quebra a cozinha.

**Gancho na tela (0-2 s):** "CHEIRO NO SALÃO? OLHA ISSO" (laranja: "OLHA ISSO")
**Duração:** ~33 s

### Falas
| # | Tempo | Quem | Tipo | Fala |
|---|---|---|---|---|
| 1 | 2-7 s | Seu Raimundo | [LIP SYNC] | "Sábado, salão lotado, e o cliente reclamando do cheiro! Fui ver, era a caixa de gordura." |
| 2 | 7-11 s | Seu Raimundo | [VOZ POR CIMA] | "Fritura o dia todo, e a gordura foi juntando até tampar tudo." |
| 3 | 11-18 s | Técnico SF (Márcio) | [LIP SYNC] | "Restaurante que frita muito precisa limpar a caixa com frequência. Senão o cheiro e a água voltam pra cozinha." |
| 4 | 18-23 s | Técnico SF | [VOZ POR CIMA] | "A gente retira a gordura e desentope o cano com cabo rotativo, sem quebrar o piso da cozinha." |
| 5 | 23-26 s | Seu Raimundo | [LIP SYNC] | "E testaram na hora, antes de abrir o salão." |
| 6 | 26-34 s | Técnico SF | [LIP SYNC] | Fala final padrão (WhatsApp). |

### Cenas (plano a plano)
1. **0-2 s · Gancho:** split vertical: em cima, salão bonito com mesas e vista do mar; embaixo, tampa de ferro da caixa de gordura da cozinha abrindo e revelando crosta grossa amarelada. Corte seco, tremor.
2. **2-7 s:** Seu Raimundo, camisa social de manga curta, no corredor entre salão e cozinha, falando para a câmera.
3. **7-11 s:** close da fritadeira com óleo, depois ralo de grelha no chão da cozinha com água parada e gordura boiando.
4. **11-18 s:** técnico de farda, de pé ao lado da caixa aberta, falando para a câmera; a caixa grande de restaurante aparece em primeiro plano com a camada de gordura.
5. **18-21 s:** retirada da gordura com equipamento (concha e baldes), close do cano de saída entupido.
6. **21-23 s:** cabo rotativo no cano, a água começa a descer.
7. **23-26 s:** caixa limpa; mangueira de água no ralo do chão, água escoando; Seu Raimundo de braços cruzados, satisfeito.
8. **26-34 s:** técnico falando o WhatsApp + cartão final.

### Prompts (HeyGen / Veo, 9:16)
**Cena 1**
```
Vertical 9:16 realistic video, split composition: top half shows a full seafood restaurant dining room near the beach in São Luís at sunset, wooden tables, ocean view; bottom half shows gloved hands lifting a cast-iron grease trap lid in the restaurant kitchen floor, revealing a thick crust of yellowish-white solidified grease over murky water. Documentary realism, not gross. Audio: restaurant chatter, heavy metal lid scraping. No on-screen text, no logos.
```
**Cena 2**
```
Vertical 9:16 realistic medium shot, Brazilian man in his mid 50s, tan skin, grey hair, short-sleeve button shirt, restaurant owner standing in the corridor between the dining room and the kitchen, speaking to the camera in Brazilian Portuguese, worried and frustrated. Warm evening light. Leave the lower third free of the face. No on-screen text, no logos.
```
**Cena 3**
```
Vertical 9:16 realistic close-up video: a commercial deep fryer bubbling with oil and fried fish; cut to a steel floor drain grate in a restaurant kitchen with still, cloudy water and floating grease that does not drain. Audio: frying sizzle, slow gurgle. No on-screen text, no logos.
```
**Cena 4**
```
Vertical 9:16 realistic medium shot, Brazilian male technician in his 30s, dark brown skin, wearing a royal blue work coverall with an orange chest panel and orange shoulders, a small round blank badge patch on the left chest with no text, black nitrile gloves, black safety boots, standing beside a large open restaurant grease trap whose surface is covered by a thick yellowish grease layer in the foreground. He speaks to the camera in Brazilian Portuguese, calm and expert. Kitchen with stainless steel equipment, morning light. No on-screen text, no readable logos.
```
**Cena 5**
```
Vertical 9:16 realistic close-up video: the technician in a royal blue coverall with orange details removes thick slabs of solidified grease from a large restaurant grease trap with a long steel scoop into lidded buckets; then a close-up of the outlet pipe blocked by hardened grease. Professional, realistic, not gross. Audio: scraping, splashing lightly. No on-screen text, no logos.
```
**Cena 6**
```
Vertical 9:16 realistic macro video: a rotating steel cable from a professional drain cleaning machine pushes into the grease trap outlet pipe, breaking the blockage; water begins to flow out. Black gloves, royal blue sleeve with orange cuff detail. Audio: motor hum, rush of water. No on-screen text, no logos.
```
**Cena 7**
```
Vertical 9:16 realistic video: a clean, empty restaurant grease trap with clear water; a hose pours water into the kitchen floor drain and it drains quickly. The restaurant owner in his 50s with a short-sleeve shirt stands with arms crossed and nods, satisfied. Bright morning light. Audio: water draining. No on-screen text, no logos.
```
**Cena 8**
```
Vertical 9:16 realistic medium close-up, the Brazilian male technician in a royal blue coverall with orange chest panel and orange shoulders, small round blank chest patch with no text, holding a smartphone, smiling and speaking to the camera in Brazilian Portuguese. Clean restaurant kitchen behind him in soft focus. Leave empty space at the bottom. No on-screen text, no readable logos.
```

### Legenda
```
CAIXA DE GORDURA DE RESTAURANTE: QUANDO O CHEIRO CHEGA NO SALÃO

Restaurante de peixe e frutos do mar em São Luís frita o dia inteiro. E toda essa gordura tem um destino: a caixa de gordura da cozinha. Quando ela enche, o primeiro a perceber nem é você. É o cliente sentado no salão.

📌 O que a caixa de gordura faz no restaurante
Ela segura a gordura antes de ir para o esgoto. Só que a gordura esfria, endurece e forma uma camada grossa. Se a caixa não é limpa com frequência, essa camada tampa a saída e o cheiro e a água voltam para a cozinha.

⚠️ Sinais de que está na hora de limpar
• cheiro de esgoto perto da cozinha ou do banheiro do salão
• ralo do chão da cozinha com água parada
• pia demorando a descer no meio do serviço
• camada de gordura grossa quando a tampa é aberta

🔧 Como a Desentupidora SF trabalha em restaurante
Técnico uniformizado, retirada da gordura acumulada e desentupimento do cano com máquina de cabo rotativo, sem quebra-quebra no piso da cozinha. O teste é feito na hora, com água escoando, antes de você abrir as portas.

💡 Exemplo
Sentiu cheiro no fim do expediente? Abra a caixa, tire uma foto e mande no WhatsApp. O orçamento é grátis, e você decide com calma.

✅ Conclusão
Cliente que sente cheiro ruim não reclama duas vezes: ele só não volta. Cuidar da caixa de gordura também é cuidar do salão.

📲 Orçamento grátis por foto ou vídeo no WhatsApp (98) 92010-5710. Atendemos restaurantes, condomínios, casas e empresas em São Luís.

Imagens geradas por IA.

#caixadegordura #restaurantesaoluis #donoderestaurante #desentupidora #slz
```

---

## Vídeo 12 · SÍNDICO DE CONDOMÍNIO · "O grupo do prédio explodiu"
**Persona:** Seu Carlos, 60 anos, síndico morador de um condomínio de prédios no Turu/Calhau. A caixa de gordura coletiva fica no térreo, perto do salão de festas e da guarita. Dor: morador do térreo reclamando de cheiro e de água voltando na pia, mensagens no grupo do WhatsApp do condomínio, cobrança na assembleia. Confia em empresa que atende condomínio, chega uniformizada e mostra o teste para quem estiver olhando.

**Gancho na tela (0-2 s):** "SÍNDICO, A CAIXA ESTOUROU" (laranja: "ESTOUROU")
**Duração:** ~32 s

### Falas
| # | Tempo | Quem | Tipo | Fala |
|---|---|---|---|---|
| 1 | 2-6 s | Seu Carlos | [LIP SYNC] | "O grupo do condomínio não para: cheiro no térreo e pia voltando no apartamento 101." |
| 2 | 6-10 s | Seu Carlos | [VOZ POR CIMA] | "Abri a caixa de gordura do prédio e tava assim, cheia até a boca." |
| 3 | 10-16 s | Técnica SF (Jéssica) | [LIP SYNC] | "Caixa de gordura de prédio recebe a cozinha de todo mundo. Uma hora ela enche e tampa a saída." |
| 4 | 16-22 s | Técnica SF | [VOZ POR CIMA] | "A gente retira a gordura, desentope o cano com cabo rotativo e não quebra o piso do condomínio." |
| 5 | 22-25 s | Seu Carlos | [LIP SYNC] | "E testaram na hora, na frente dos moradores. Mandei o vídeo no grupo." |
| 6 | 25-33 s | Técnica SF | [LIP SYNC] | Fala final padrão (WhatsApp). |

> "Apartamento 101" é exemplo de cena, sem dado real.

### Cenas (plano a plano)
1. **0-2 s · Gancho:** celular na mão do síndico com notificações de grupo subindo (texto borrado, ilegível); corte seco para a tampa de concreto da caixa coletiva aberta no térreo, gordura amarelada cobrindo a água até a borda.
2. **2-6 s:** Seu Carlos de camisa polo, crachá de síndico sem texto legível, no pátio do térreo, falando para a câmera.
3. **6-10 s:** close da caixa grande de concreto: camada espessa de gordura branca e amarelada, água turva parada, cano de saída submerso e tampado.
4. **10-16 s:** técnica de farda ao lado da caixa, prédio ao fundo, falando para a câmera.
5. **16-19 s:** retirada da gordura com concha e baldes com tampa, técnica e ajudante; cone de sinalização ao lado.
6. **19-22 s:** cabo rotativo entrando no cano de saída; água começando a correr.
7. **22-25 s:** caixa limpa; moradora do térreo abre a torneira da pia do 101 e a água desce rápido; Seu Carlos filma com o celular.
8. **25-33 s:** técnica falando o WhatsApp + cartão final.

### Prompts (HeyGen / Veo, 9:16)
**Cena 1**
```
Vertical 9:16 realistic video: close-up of an older man's hand holding a smartphone with many group chat notifications sliding in, all text blurred and unreadable; hard cut to the ground floor of a Brazilian apartment condominium in São Luís, where a large square concrete grease trap lid is open and yellowish-white solidified grease covers the murky water up to the rim. Daylight, documentary realism, not gross. Audio: rapid notification pings, heavy concrete lid scraping. No on-screen text, no logos.
```
**Cena 2**
```
Vertical 9:16 realistic medium shot, Brazilian man around 60, light brown skin, grey hair and moustache, polo shirt, a blank lanyard badge with no text, standing in the paved ground-floor courtyard of a residential condominium with apartment towers behind him, speaking to the camera in Brazilian Portuguese, tired and worried. Natural daylight. Leave the lower third free of the face. No on-screen text, no logos.
```
**Cena 3**
```
Vertical 9:16 realistic top-down close-up of a large open concrete grease trap in a condominium: a thick layer of white and yellowish solidified grease, murky still water, the outlet pipe submerged and clogged with hardened grease. Natural daylight, documentary realism, not gross. Audio: slow drip echo. No on-screen text, no logos.
```
**Cena 4**
```
Vertical 9:16 realistic medium shot, Brazilian female technician in her 30s, brown skin, ponytail, wearing a royal blue work coverall with an orange chest panel and orange shoulders, a small round blank badge patch on the left chest with no text, black nitrile gloves, black safety boots, standing next to the open condominium grease trap with apartment towers behind her, speaking to the camera in Brazilian Portuguese, calm and confident. An orange safety cone nearby. No on-screen text, no readable logos.
```
**Cena 5**
```
Vertical 9:16 realistic video: the female technician and a male colleague, both in royal blue coveralls with orange chest panels and orange shoulders and blank round chest patches with no text, remove slabs of solidified grease from a large condominium grease trap with long steel scoops into lidded buckets; orange safety cone beside them. Professional, clean, realistic. Audio: scraping, bucket lids. No on-screen text, no readable logos.
```
**Cena 6**
```
Vertical 9:16 realistic macro video: a rotating steel cable from a professional drain cleaning machine enters the outlet pipe of a concrete grease trap, freeing the blockage, and water starts to flow away. Black gloves, royal blue sleeves with orange cuffs. Audio: machine motor, rushing water. No on-screen text, no logos.
```
**Cena 7**
```
Vertical 9:16 realistic video: a clean condominium grease trap with clear water; cut to a ground-floor apartment kitchen where a Brazilian woman in her 40s opens the tap and water drains fast and clean; the grey-haired building manager with a polo shirt films it with his smartphone and nods. Bright natural light. Audio: water draining, satisfied murmur. No on-screen text, no logos.
```
**Cena 8**
```
Vertical 9:16 realistic medium close-up, the Brazilian female technician in a royal blue coverall with orange chest panel and orange shoulders, small round blank chest patch with no text, holding a smartphone, smiling and speaking to the camera in Brazilian Portuguese. Condominium courtyard in soft focus behind her. Leave empty space at the bottom. No on-screen text, no readable logos.
```

### Legenda
```
CAIXA DE GORDURA DE CONDOMÍNIO: O PROBLEMA QUE CAI NO COLO DO SÍNDICO

Se você é síndico em São Luís, já sabe como começa: uma mensagem no grupo reclamando de cheiro no térreo. Depois outra. Depois a pia do apartamento de baixo voltando água. Na maioria das vezes, a origem é a caixa de gordura do prédio.

📌 Por que a caixa de gordura do condomínio enche
Ela recebe a água da cozinha de todos os apartamentos. Óleo, resto de comida e sabão descem juntos, a gordura esfria e forma uma camada grossa. Quando essa camada tampa o cano de saída, quem sofre primeiro são os moradores do térreo.

⚠️ Sinais que o síndico precisa observar
• reclamação de cheiro perto da caixa ou do salão de festas
• pia dos apartamentos de baixo escoando devagar ou voltando
• tampa da caixa úmida ou com água em volta
• camada de gordura grossa quando a caixa é aberta

🔧 Como a Desentupidora SF atende condomínios
Técnicos uniformizados, retirada da gordura acumulada e desentupimento com máquina de cabo rotativo, sem quebra-quebra no piso do condomínio. O teste é feito na hora, na frente de quem quiser acompanhar, e você pode gravar e mandar no grupo.

💡 Exemplo
Recebeu reclamação de cheiro? Abra a caixa, tire uma foto e mande no WhatsApp. O orçamento é grátis, e você já leva a informação pronta para os moradores.

✅ Conclusão
Caixa de gordura em dia é menos mensagem no grupo e menos dor de cabeça na assembleia.

📲 Orçamento grátis por foto ou vídeo no WhatsApp (98) 92010-5710. Atendemos condomínios, casas, restaurantes e empresas em São Luís e região.

Imagens geradas por IA.

#caixadegordura #sindico #condominio #manutencaopredial #saoluisma
```

---

## Ordem de postagem sugerida (xadrez com o feed, vídeo intercalado com estático)
1. Vídeo 11 · Restaurante (gancho mais forte, persona que mais paga)
2. Vídeo 9 · Dona de casa
3. Vídeo 12 · Síndico
4. Vídeo 10 · Marmitaria

Horários: 08h45, 12h45, 16h45 ou 20h45, de 4 em 4 h, dentro da janela 8h-21h (regra 09/11).

## Personagens (repetir o mesmo rosto em todas as cenas do vídeo)
| Vídeo | Cliente | Técnico(a) SF |
|---|---|---|
| 9 | Dona Rose, 48, dona de casa | Jéssica (técnica, 30 e poucos, rabo de cavalo) |
| 10 | Cláudia, 38, marmitaria + ajudante Thiago | Márcio (técnico, 30 e poucos, pele escura) |
| 11 | Seu Raimundo, 55, restaurante de frutos do mar | Márcio |
| 12 | Seu Carlos, 60, síndico | Jéssica + colega |
