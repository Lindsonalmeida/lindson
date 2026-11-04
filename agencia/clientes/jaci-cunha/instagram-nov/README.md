# Dra. Jaci · carrosséis de novembro/2026 (conta Lindson, 03/11/2026)

4 carrosséis de 6 telas (terças do calendário da Zuleide), textos e legendas do copy-squad (`TEXTOS.md`, `textos.json`), fotos de estúdio dela (`../fotos/`). **Nada se cria, tudo se copia** — cada capa copia um post real dela:
| Carrossel | Data | Linha | Capa copiada de |
|---|---|---|---|
| c1 · 3 perguntas antes de qualquer procedimento | 03/11 | Dúvidas | "botox · O QUE NINGUÉM RESPONDE" (balão + serif gigante) |
| c2 · Biossegurança: o que você não vê | 10/11 | Autoridade | "Bioestimulador de Colágeno" (faixa dourada com fio) |
| c3 · Mitos × verdades da harmonização | 17/11 | Dúvidas | "Preenchimento facial, por que alguns ficam artificiais…" |
| c4 · Vem me conhecer | 24/11 | Acolhimento | "Entramos na reta final do ano… / faixas vinho" |
Telas do meio (v2, 03/11, pedido do Lindson: sem foto nem composição repetida): 4 composições diferentes por carrossel — A foto nítida dividida (cópia do tríptico "a artista:"), B creme tipográfico com número dourado e faixa com fio (cópia de "Bioestimulador"), C cor invertida vinho (faixas vinho de "E EU SEMPRE AVISO"), D foto desfocada com véu e checks (cópia de "Seu botox, dia após dia"); nenhuma foto se repete dentro do carrossel; fechamento copia "Antes de qualquer procedimento, eu observo" (faixa café + pílula).
Gerar: `python3 gerar.py <pasta com textos.json> ../fotos && node render.js <pasta>`.
**Confirmar com a Dra.:** c2 diz que ela usa produtos com registro na Anvisa de fornecedores autorizados e segue protocolos de biossegurança.
No painel dela (Aprovações) com todas as telas e a legenda, aguardando aprovação no site.

Alta qualidade (conta Leandro, 04/11): `node render2x.js <pasta>` gera as telas em 2160×2700 (fotos melhoradas com `ferramentas/melhorar_foto.py`); são as que estão no painel, em `painel/jaci/feed/c1-1.jpg`…
