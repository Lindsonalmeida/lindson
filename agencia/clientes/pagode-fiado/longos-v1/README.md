# Pagode Fiado · Vídeos longos v1 (sessão GOMINHO, conta Pedro, 18/11/2026)

Pedido do Lindson (18/11): "gere todos os vídeos longos que faltam do Pagode Fiado".

## O que é cada longo
Uma faixa do Álbum 01 inteira (~3 min), 16:9, 1080p, com a **letra sincronizada** numa tira de caderno do fiado, fotos reais de boteco e roda de samba (Wikimedia, tratadas em âmbar e verde), abertura no **quadro FIADO**, carimbos "refrão", fecho com o logo e "Pendura na conta.". VFX: Ken Burns, fusões, luz vazando nos cortes, grão e vinheta. Áudio: a música (voz e letra) + whoosh nos cortes e ambiente de bar na abertura.

## Situação
| Faixa | Música | Vídeo |
|---|---|---|
| 05 Bilhete na Geladeira (voz Vitinho) | pronta (vidIQ, 18/11) | pronto |
| 07 Visualizou e Não Voltou (voz Davi Lua) | pronta (vidIQ, 18/11) | pronto |
| 00, 01, 02, 03, 04, 06, 08, 09, 10 | **falta**: perdidas na sessão apagada | travado: sem crédito de música |
| Álbum completo (longo de ~30 min) | depende das 11 | travado |

**Trava:** cada música custa 25 créditos do vidIQ; sobraram 20 (renova em 30/11 com 150 = 6 faixas). A Runway está com saldo 0. Para as 9 que faltam: pôr crédito no vidIQ ou na Runway, ou esperar 30/11.

## Como refazer / continuar
1. Letra nova em `faixas.json` (título, voz, fotos, cortes, partes, letra com tempos) e música pelo `vidiq_generate_music` (prompt: pagode romântico ao vivo em roda de bar + letra com [Verso]/[Refrão], 180 s).
2. Tempos da letra: faster-whisper (modelo small, ler o wav 16 kHz com soundfile) e corrigir o texto à mão.
3. Fotos: Wikimedia (CC BY/BY-SA/CC0, paisagem ≥ 1600 px), nunca as já usadas (`../FOTOS-USADAS.md`), nunca artista real identificável como se fosse o grupo.
4. `python3 overlays.py <faixa> <pasta>` → `node render.js <pasta>/ov<faixa>` → `python3 montar.py <faixa> <pasta>`.
5. Créditos das fotos na descrição: `CREDITOS-FOTOS.md`. Títulos, descrições e tags: `publicar.json`.

Arquivos: vídeos e wav no privado `painel/canais/pagode/longos-v1/` (vídeo comprimido para o painel) e original em `dados/agencia/pagode-fiado/longos-v1/`.
