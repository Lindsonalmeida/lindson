# Real Time · pronúncias para a narração (conta Zuleide, 16/11/2026)

Pedido do Lindson (15/11): "as pronúncias estão erradas. filtro N D como as letras" e "pesquise os termos, palavras, origens e use a pronúncia certa". Voz: pt-BR-AntonioNeural +4%. Na tela fica a grafia correta; no TTS vai a grafia fonética (aplicada sozinha por `drive-15-11/motor/pronuncias.json`). Cada termo foi conferido no Whisper (small, pt).

| Termo | Origem | Pronúncia certa | Grafia no TTS | Fonte |
|---|---|---|---|---|
| Real Time | marca do cliente, do inglês "real time" | "riál táime" | Riál Táime | ordem do Lindson, 15/11 |
| Tilta | marca chinesa (Shenzhen, 2010; escritório em Burbank, EUA) | "tíl-ta" | Tílta, (vírgula antes do nome seguinte) | wikipedia.org/wiki/Tilta |
| Mirage (Pro) | produto Tilta, palavra inglesa "mirage" /mɪˈrɑːʒ/ | "mi-ráj" | Miráje | dicionário inglês |
| Nucleus-M II | produto Tilta, inglês "nucleus" + "M dois" | "núcleus ême dois" | Núcleus ême dois | uso dos videomakers brasileiros |
| DZOFilm | marca chinesa (Shenzhen Dongzheng Optical, 2013); DZO é sigla, dita letra por letra | "dê zê ô film" | Dê, zê, ô, Film, | provideocoalition.com, equipboard.com |
| Arcana | linha anamórfica da DZOFilm, do latim "arcana" | "arcána" | Arcána | petapixel.com (lançamento, abr/2026) |
| ND (filtro) | sigla inglesa de Neutral Density, dita letra por letra | "ene dê" | ene, dê, | pro.sony (filtro ND variável) |
| matte box | inglês | "méti bóx" | méti bóx | uso no set |
| REC | inglês "record" | "réc" | rréque | uso no set |
| squeeze 1.5x | inglês | "squízi de um ponto cinco" | Isquíz de um ponto cinco | DZOFilm Arcana 1.5x |
| full frame | inglês | "ful frêim" | Ful frêime | uso no set |
| T2.1 / T16 | T-stop, abertura de cinema | "tê dois ponto um / tê dezesseis" | tê dois ponto um / tê dezesseis | ficha da Arcana |
| bokeh | japonês "boke" (desfoque) | "bokê" | Bokê | uso dos fotógrafos |
| coating | inglês | "côu-tin" | Côu-tin | uso no set |
| flare | inglês | "flér" | Flér | uso no set |
| follow focus, gimbal, rig | inglês | "fólou fôcus", "gímbal", "rígui" | (não usados agora) | uso no set |

Evite "pro set": o TTS lê "procede". Use "pra gravar" ou "para gravar".

## Termos novos dos 6 Reels de 16/11/2026 (conta Zuleide)
| Termo | Origem | Pronúncia certa | Grafia no TTS | Fonte |
|---|---|---|---|---|
| Sony FX3 | câmera Sony (Japão); FX dito letra por letra | "sôni éfe xis três" | Sôni éfe xis três | uso dos videomakers brasileiros |
| VESPID (Prime 2) | linha DZOFilm, do inglês "vespid" (vespa) /ˈvɛspɪd/ | "véspid" | Véspide | dicionário inglês |
| Prime | inglês, lente de foco fixo | "práim" | Práime | uso no set |
| teleprompter | inglês | "teleprômpter" | teleprômpter | uso no Brasil |
| videocast | híbrido pt/en | "vídeo cást" | vídeo cást | uso no Brasil |
| job | inglês, "trabalho" no mercado audiovisual | "djób" | djób | uso no set |
| kit | inglês aportuguesado | "quít" | kit (a grafia "quit" saiu "kick" no Whisper) | Whisper 16/11 |
| cage | inglês, gaiola da câmera | "quêidj" | (o TTS erra: "conquede"; na fala usar "gaiola", na tela "cage") | Whisper 16/11 |

## Revisão com Whisper medium sem prompt (16/11/2026, conta Zuleide) · voz mantida: pt-BR-AntonioNeural
Testadas: Antonio, Brian/Andrew Multilingual (en-US) e Thalita Multilingual (feminina). Brian acerta Tilta, matte box, REC e VESPID, mas lê o português com sotaque americano ("paterias inclusis", "em caixas no puno", "no 7"), então Antonio ficou nos 9 vídeos.
| Termo | Grafia no TTS agora | Resultado |
|---|---|---|
| Tilta | Tilta (sem acento; "Tílta," e "Tiltá" saíam "Tilt-A"/"Tiutá") | ouvido "Tilta" colado ao nome seguinte |
| matte box | máti bóx | "matte box"/"matbox" (som certo; a grafia "matchbox" sumiu em 4 de 5) |
| Squeeze | Squeeze (inglês direto) | "squeezy" (som certo) |
| REC | na fala troca por "gravar"/"gravação" ("réc" e "rréque" saem "hack") | na tela continua REC |
| Primeiro | na fala "Pra começar" (saía "Primer") | ok |
| a equipe | "Nossa equipe" (saía "aí Fipe") | ok |
| DZOFilm | Dê zê ô Film, | letras + film (Whisper escreve "Dayz/Deiseo film"); limite da voz |
| VESPID | Véspide | "véspede/vesp de"; limite da voz |
| Real Time | Riál Táime | ok nos 9 |
Grafias do Brian (se um dia trocar a voz): `motor/pronuncias_brian.json`; motor aceita `VOZ=` e `PRON=`.
**Atualização 16/11 (conta Zuleide):** pt-BR-MacerioMultilingualNeural não existe no edge-tts (NoAudioReceived). Plano B aplicado: as marcas DZOFilm, VESPID e Tilta saíram da narração (continuam no lettering). Falas novas: 01 "Olha essa matte box sem fio!", 02 "Foco sem fio, na sua mão!" e "Foco e gravar.", 03 "Lentes anamórficas Arcana!", 04 "Agora, a lente de cinema.", 06 "Agora, a maleta das lentes." e "São seis lentes de cinema…". Whisper medium sem prompt: sem erro de termo nos 9.
